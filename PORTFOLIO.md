# Repository portfolio

This document is the maintenance layer behind the public profile README. It exists to make a large repository portfolio manageable without treating every repository as an equally active project.

## Lifecycle model

| State | Meaning | Management expectation |
| --- | --- | --- |
| **Active** | Receiving meaningful development attention now | Keep deliberately small; target 5–10 projects/families |
| **Maintained** | Stable/useful and supported when needed | No expectation of continuous development |
| **Experimental / Incubating** | Prototype, scaffold, spike, or future direction | May change substantially; evaluate before promoting |
| **Archive candidate** | Completed, superseded, or no longer expected to evolve | Review before archiving; do not delete by default |
| **Archived** | Historical/read-only project | Retained for provenance and reference |

**Portfolio rule:** active is a deliberate priority state, not a proxy for recent commits. This file is the authoritative lifecycle inventory and repository-creation policy for the profile portfolio.

## Current portfolio audit

Audit date: **2026-09-18**. Scope: **public repositories only**. Private repositories are deliberately not tracked, named, or described in this file; a private project enters the inventory when it becomes public, and leaves it when it stops being public. One Maintained repository left the inventory on 2026-09-13 on that basis. Twenty-one DIMER pipelines shipped between 2026-09-13 and 2026-09-15 and entered the inventory on 2026-09-18, opening two coverage areas the portfolio did not have before: document AI and OCR, and a detection family beyond the single zero-shot detector. This classification is intentionally conservative: it does not archive, delete, rename, or consolidate repositories automatically.

### Active

| Project / family | Notes |
| --- | --- |
| `agent-*` | Agent infrastructure family: `agent-relay`, `agent-router`, `agent-control`, `agent-toolchain`. All public; each independently usable |
| `agentic-vault` | Agent-agnostic knowledge infrastructure / Obsidian vault system |
| `agentic-analytics` | Agent-agnostic analytical runtime |
| DIMER model pipelines | Model integrations for the DIMER platform, treated as one family and now the largest part of the public portfolio. Tabular (`mitra-*`, `tabicl-*`, `tabpfn-*`, `tabdpt-*`), vision (`swin-*`, `sam*-*`, `clipseg-*`, `depth-anything-*`, `zoedepth-*`, `vitpose-*`, `xclip-*`, `dinov2-*`, `swin2sr-*`, `eva02-*`, `convnext-*`, `resnet50-*`, `mobilenetv4-*`, `vit-*`), detection (`grounding-dino-*`, `owlv2-*`, `rtdetr-*`, `yolox-*`), document AI and OCR (`got-ocr2-*`, `smoldocling-*`, `layoutlm-*`, `pix2struct-*`, `table-transformer-*`, `deplot-*`), vision-language (`siglip2-*`, `florence2-*`, `smolvlm-*`, `blip-*`), time series (`chronos-2-*`, `tirex-*`, `toto-*`, `moment-*`), audio and multimodal (`whisper-*`, `ast-*`, `kokoro-*`, `phi4-*`), and language (`language-model-*`, `bert-*`, `gpt2-*`, `t5-*`, `gliner-*`, `qwen3-*`) including the text-task pipelines `roberta-*`, `tapas-*`, `bart-*`, and `marianmt-*`. One shared contract throughout — pinned model revision, checksum-verified weights, validation before inference, machine-readable provenance, and a model card per repository. Maturity is recorded per repository in its own `STATUS.md`, not here |
| `litert-lm-plugin-cc` | On-device/local-model tooling |

### Maintained

| Project / family | Notes |
| --- | --- |
| `agentic-research` | Systematic-review skill pipeline |
| `ai-readiness-assessment` | Public AI-readiness assessment |
| `citation-audit` | Citation verification tool |
| `keynote-builder` | Governed keynote-generation workflow |
| `market-study-template` | Reusable market-study scaffold |
| `mlops-lite` | Single-GPU MLOps platform |
| `office-reports` | Institutional reporting skills |
| `pdf-signer-pwa` | Offline PDF-signing utility |
| `presentation-builder` | General presentation-building skills |
| `research-deck-builder` | Research/training deck workflow |
| `kurtvalcorza.github.io` | Personal site |
| `kurtvalcorza` | Profile/portfolio control surface |

### Experimental / incubating

| Project / family | Notes |
| --- | --- |
| Empty pipeline scaffolds | Three public repositories created but still not implemented: `prithvi-eo-segmentation-pipeline`, `prithvi-eo-regression-pipeline`, `timesfm-forecasting-pipeline`. Public but empty; not carried on the profile README or the site portfolio until they ship. Four others flagged here on 2026-09-11 (`whisper-asr-*`, `tirex-*`, `toto-*`, `phi4-*`) have since shipped and moved into the DIMER family |

### Archived

Read-only; retained for provenance. Archived projects are not carried in the profile README or the site portfolio listing. Archived private repositories are out of scope for this file and are not listed.

| Project | Prior state | Notes |
| --- | --- | --- |
| `acabai-ph` | Maintained | Public DOST-ASTI showcase site (NAIRA, DIMER, iTANONG) |
| `benchmarking-harness` | Maintained | Three-tier evaluation gate for computer-vision models |
| `dost-progress-report` | Maintained | DOST report-generation workflow |
| `inference-bench` | Maintained | MLPerf/TensorRT inference and GPU/CPU hardware benchmarking |
| `research-writer` | Maintained | Citation-checked literature-review drafting |
| `wsl-crew` | Maintained | WSL2 service-management utility |

### Archive / consolidation review candidates

These are **review candidates, not automatic actions**.

1. **Empty public scaffolds** — three pipeline repositories are public with no implementation. Public-but-empty repositories carry a reputational cost that private-but-empty ones do not: a visitor cannot distinguish a placeholder from an abandoned project. Either implement, make private until implemented, or archive.
2. **Tabular-model component families** — `mitra-*` and `tabicl-*` carry six repositories each (pipeline, finetuner, dataset validator, per task), while `tabpfn-*` and `tabdpt-*` carry two. Keep the six-repo split only where pipeline, finetuner, and validator are independently versioned and consumed; otherwise evaluate a family monorepo.
3. **Pipeline-family visibility is uneven** — some families publish all component repositories, others publish only the contract repository. That is a defensible choice, but it should be a stated one rather than an accident of when each repository was created.

## Repository families

GitHub personal repositories have no folder hierarchy, so repository names act as namespaces.

| Namespace | Portfolio meaning |
| --- | --- |
| `agent-*` | Agent runtime infrastructure: relay, routing, control, distribution |
| `agentic-*` | Agent infrastructure and agent-native workflows |
| `mlops-*` | ML platform / operations infrastructure |
| `mitra-*`, `tabicl-*`, `tabpfn-*`, `tabdpt-*` | Tabular foundation-model pipelines |
| `swin-*`, `siglip2-*`, `blip-*`, `prithvi-*` | Vision, vision-language, and Earth-observation pipelines |
| `grounding-dino-*`, `owlv2-*`, `rtdetr-*`, `yolox-*` | Object-detection pipelines |
| `got-ocr2-*`, `smoldocling-*`, `layoutlm-*`, `pix2struct-*`, `table-transformer-*`, `deplot-*` | Document AI and OCR pipelines: text recognition, document QA, tables, charts |
| `chronos-*`, `moment-*`, `timesfm-*`, `tirex-*`, `toto-*` | Time-series forecasting pipelines |
| `bart-*`, `roberta-*`, `tapas-*`, `marianmt-*` | Language task pipelines: summarization, QA, zero-shot classification, translation |
| `research-*` | Research and research-communication tooling |

Do not rename stable repositories merely to make the taxonomy perfect. Namespace consistency is useful when it reduces search and navigation cost.

## When to create a new repository

Create a separate repository when at least one of these boundaries is real:

1. **Independent product** — it has a distinct purpose, users, and roadmap.
2. **Independent release/versioning** — it must be packaged or released separately.
3. **Independent reuse** — other projects consume it as a standalone component.
4. **Access-control boundary** — public/private or collaborator permissions materially differ.
5. **CI/deployment boundary** — independent build, test, or deployment workflows provide a concrete operational benefit.

Otherwise prefer an existing repository, package/module, or monorepo workspace.

### Consolidation test

> Can this component meaningfully change, release, and be consumed independently?

If **yes**, a separate repo is defensible. If **no**, consolidation should be evaluated.

## Portfolio operating rules

- This file tracks **public repositories only**. Do not add, name, or describe a private repository here; wait until it is public.
- Keep **Active** to roughly 5–10 projects or families.
- Treat a repository family as one cognitive project when its component repos serve one product/system.
- Do not create a repository for an idea that has no implementation boundary yet; use an issue/spec in the parent project first.
- Archive completed/superseded work rather than leaving it indistinguishable from active work.
- Do not delete historical repositories unless they contain no useful provenance and deletion is intentional.
- Review visibility consistency inside repository families before making a family public.
- When a repository is made private, remove it from this file, the profile README, and the site portfolio in the same change; a link a visitor cannot open is worse than no link.
- Prefer `main` for new repositories; do not rename established default branches solely for cosmetic consistency.
- Review this file quarterly or after a major project cycle and update `README.md` when the active set changes.

## Hygiene observations

The audit surfaced several low-cost consistency items for later review:

- Some established repositories still use `master` (`agentic-vault`, `mlops-lite`). This is not a blocker; normalize only when there is a practical reason. `acabai-ph` also uses `master` but is archived, so the question is moot for it.
- Many pipeline repositories still carry no GitHub description, though the batch created on 2026-09-13 mostly does. The description is the only text a visitor sees in search results and on the profile's repository tab, so an empty one costs more than it saves.
- Repository `size` reported by the GitHub API is not computed immediately for newly created repositories, so it cannot be used to tell an empty scaffold from a populated one within hours of creation. Check the file tree instead.
- Empty scaffold repositories contribute substantial visible repository count without adding current operational capability. Their value should be judged by roadmap intent, not by the sunk cost of having created them.

## Review cadence

At the end of each quarter or major project cycle:

1. Reconfirm the 5–10 Active projects/families.
2. Move dormant Active projects to Maintained or Experimental.
3. Review Experimental repos for promotion, consolidation, or archiving.
4. Review archive candidates explicitly before changing repository state.
5. Update the profile README only when the public-facing portfolio changes.

The governing principle is simple: **manage projects, not repository count**. Repository boundaries should reflect architecture, distribution, access, or operations—not the need for a new place to put an idea.
