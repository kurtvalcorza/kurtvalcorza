#!/usr/bin/env python3
"""Check that every repository link on a public surface points at a live repo.

The two public surfaces -- the profile README.md / PORTFOLIO.md and the
index.html of kurtvalcorza.github.io -- are hand-curated, so they drift as
repositories are created, archived, or made private. This script is the
check that catches that drift.

It answers two questions:

  bad links  a surface links to a repository that is archived, private, or
             gone. Those are dead ends for a visitor and are reported as
             failures.

  uncovered  a live repository is named by no surface at all. That is
             reported for review rather than as a failure: not every
             repository is meant to be surfaced.

PORTFOLIO.md names repositories as backticked glob families (`mitra-*`)
rather than as links, so pass it with --patterns instead of as a surface.
A repository matched by one of its globs counts as covered.

The fleet inventory is supplied as JSON rather than fetched, so the check is
offline, deterministic, and reviewable. Produce it with the GitHub CLI:

    gh repo list kurtvalcorza --limit 300 --no-archived --json name \
        --jq '[.[].name]' > live.json
    gh repo list kurtvalcorza --limit 300 --archived --json name \
        --jq '[.[].name]' > archived.json
    python3 scripts/link_oracle.py --live live.json --archived archived.json \
        README.md PORTFOLIO.md ../kurtvalcorza.github.io/index.html

or as a single file holding {"live": [...], "archived": [...]}:

    python3 scripts/link_oracle.py --fleet fleet.json README.md ...

A check that cannot fail is not a check, so --self-test seeds one archived
link and one nonexistent link into a scratch copy of each surface and
asserts that both are rejected. Run it with every real check.

Exit status is 0 when every link resolves and the self-test (if asked for)
passes, 1 otherwise.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
import tempfile
from pathlib import Path

OWNER = "kurtvalcorza"

# github.com/<owner>/<repo>, stopping before any /tree/..., #anchor, or
# trailing punctuation that belongs to the surrounding prose.
LINK_RE = re.compile(
    r"https?://(?:www\.)?github\.com/" + OWNER + r"/([A-Za-z0-9._-]+)",
    re.IGNORECASE,
)

# `mitra-*`, `agent-*`, `sam*-*` -- a backticked glob naming a repository
# family. Requires a hyphen or a star so that ordinary inline code
# (`STATUS.md`, `main`) is not mistaken for a family name.
PATTERN_RE = re.compile(r"`([a-z0-9][a-z0-9.*-]*[-*][a-z0-9.*-]*)`")


def load_names(path: Path) -> set[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        raise SystemExit(f"{path}: expected a JSON list of repository names")
    return {str(n).strip().rstrip("/") for n in data if str(n).strip()}


def load_fleet(args: argparse.Namespace) -> tuple[set[str], set[str]]:
    if args.fleet:
        data = json.loads(Path(args.fleet).read_text(encoding="utf-8"))
        return (
            {str(n) for n in data.get("live", [])},
            {str(n) for n in data.get("archived", [])},
        )
    if not (args.live and args.archived):
        raise SystemExit("pass --fleet, or both --live and --archived")
    return load_names(Path(args.live)), load_names(Path(args.archived))


def links_in(path: Path) -> list[str]:
    """Every repository name linked from a surface, in order, deduplicated."""
    text = path.read_text(encoding="utf-8")
    seen: dict[str, None] = {}
    for match in LINK_RE.finditer(text):
        # A repository name never ends in a period; that is sentence
        # punctuation that the character class swallowed.
        seen.setdefault(match.group(1).rstrip("."), None)
    return list(seen)


def patterns_in(path: Path) -> list[str]:
    """Every repository-family glob named by a pattern surface."""
    text = path.read_text(encoding="utf-8")
    return sorted({m.group(1) for m in PATTERN_RE.finditer(text)})


def covered_by(name: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatchcase(name, p) for p in patterns)


def check_surface(
    path: Path, live: set[str], archived: set[str]
) -> tuple[int, list[str]]:
    """Return (link count, failure lines) for one surface."""
    failures = []
    names = links_in(path)
    for name in names:
        if name in live:
            continue
        reason = "archived" if name in archived else "not a live public repo"
        failures.append(f"{path}: {name} -> {reason}")
    return len(names), failures


def self_test(surfaces: list[Path], live: set[str], archived: set[str]) -> bool:
    """The check must reject a seeded archived link and a seeded dead link."""
    if not archived:
        print("  SKIP: no archived repositories to seed with")
        return True
    seeds = {
        "archived link": f"https://github.com/{OWNER}/{sorted(archived)[0]}",
        "nonexistent link": f"https://github.com/{OWNER}/this-repo-does-not-exist",
    }
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        for label, url in seeds.items():
            probe = Path(tmp) / "probe.md"
            probe.write_text(
                surfaces[0].read_text(encoding="utf-8") + f"\n\n[seed]({url})\n",
                encoding="utf-8",
            )
            _, failures = check_surface(probe, live, archived)
            rejected = any(url.rsplit("/", 1)[1] in f for f in failures)
            print(f"  {'OK  ' if rejected else 'FAIL'}: seeded {label} -> "
                  f"{'rejected' if rejected else 'ACCEPTED'}")
            ok = ok and rejected
    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("surfaces", nargs="+", type=Path)
    parser.add_argument("--fleet", help="JSON with {live: [...], archived: [...]}")
    parser.add_argument("--live", help="JSON list of live repository names")
    parser.add_argument("--archived", help="JSON list of archived repository names")
    parser.add_argument("--patterns", type=Path, action="append", default=[],
                        help="surface naming families as backticked globs "
                             "(PORTFOLIO.md); repeatable")
    parser.add_argument("--self-test", action="store_true",
                        help="also prove the check rejects known-bad links")
    parser.add_argument("--show-uncovered", action="store_true",
                        help="list live repositories no surface names")
    args = parser.parse_args()

    live, archived = load_fleet(args)
    all_failures: list[str] = []
    linked: set[str] = set()

    for surface in args.surfaces:
        if not surface.exists():
            all_failures.append(f"{surface}: missing")
            continue
        count, failures = check_surface(surface, live, archived)
        linked.update(links_in(surface))
        status = "OK  " if not failures else "FAIL"
        print(f"{status} {surface}: {count} links, {len(failures)} bad")
        all_failures.extend(failures)

    for pattern_file in args.patterns:
        if not pattern_file.exists():
            all_failures.append(f"{pattern_file}: missing")
            continue
        globs = patterns_in(pattern_file)
        matched = {n for n in live if covered_by(n, globs)}
        linked.update(matched)
        print(f"OK   {pattern_file}: {len(globs)} family globs, "
              f"{len(matched)} live repos matched")

    for failure in all_failures:
        print(f"  {failure}")

    if args.self_test:
        print("\n--- negative controls (the check must reject these) ---")
        if not self_test(args.surfaces, live, archived):
            all_failures.append("self-test: a known-bad link was accepted")

    if args.show_uncovered:
        uncovered = sorted(live - linked - {OWNER, f"{OWNER}.github.io"})
        print(f"\n--- live repositories no surface names: {len(uncovered)} ---")
        for name in uncovered:
            print(f"  {name}")

    print()
    if all_failures:
        print(f"FAIL: {len(all_failures)} problem(s)")
        return 1
    print("PASS: every link resolves to a live public repository")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        # Piping into head closes stdout early; that is not a failure.
        sys.exit(0)
