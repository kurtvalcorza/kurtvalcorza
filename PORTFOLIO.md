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

Audit date: **2026-08-21**. Scope: repositories visible through the connected GitHub account. This classification is intentionally conservative: it does not archive, delete, rename, or consolidate repositories automatically.

### Active

| Project / family | Notes |
| --- | --- |
| `agentic-vault` | Agent-agnostic knowledge infrastructure / Obsidian vault system |
| `agentic-analytics` | Agent-agnostic analytical runtime |
| `agent-router` | Model-routing infrastructure; private |
| `aiaas-market-study` | Current AIaaS market/feasibility study; private |
| `inventory-intelligence` | Applied inventory intelligence system; private |
| `litert-lm-plugin-cc` | On-device/local-model tooling |
| `mlops-grid` | Current MLOps infrastructure work; private |
| `mitra-*` | Treat classifier/regressor pipeline, finetuner, and validator repos as one active family |

### Maintained

| Project / family | Notes |
| --- | --- |
| `agentic-research` | Systematic-review skill pipeline |
| `ai-readiness-assessment` | Public AI-readiness assessment |
| `acabai-ph` | Public DOST-ASTI showcase/site |
| `benchmarking-harness` | Model evaluation harness |
| `citation-audit` | Citation verification tool |
| `dost-progress-report` | DOST report-generation workflow |
| `inference-bench` | Hardware/model inference benchmarking |
| `keynote-builder` | Governed keynote-generation workflow |
| `market-study-template` | Reusable market-study scaffold |
| `mlops-lite` | Single-GPU MLOps platform |
| `notebooks` | Reusable Colab experiments |
| `office-reports` | Institutional reporting skills |
| `pdf-signer-pwa` | Offline PDF-signing utility |
| `presentation-builder` | General presentation-building skills |
| `research-deck-builder` | Research/training deck workflow |
| `research-writer` | Citation-checked literature-review drafting |
| `wsl-crew` | WSL2 service-management utility |
| `kurtvalcorza.github.io` | Personal site |
| `kurtvalcorza` | Profile/portfolio control surface |

### Experimental / incubating

| Project / family | Notes |
| --- | --- |
| `ai-readiness-bot` | Private adjacent implementation; evaluate overlap with `ai-readiness-assessment` |
| `aiaas-marketability` | Earlier/private marketability work; evaluate overlap with `aiaas-market-study` |
| `naira-market-analysis` | Earlier/private market-analysis work; evaluate whether superseded by the current study |
| `naira-narrative-report` | Private reporting project; retain until project-cycle status is clear |
| `naicri-deck-generator` | Private event/deck-specific generator |
| `opus-fable-mode` | Private experiment |
| `tabpfn-*` | Classifier/regressor component family; six repos |
| `tabicl-*` | Classifier/regressor component family; six repos |
| `chronos-forecasting-*` | Three-repo forecasting scaffold; currently empty in repository metadata |
| `timesfm-forecasting-*` | Three-repo forecasting scaffold; currently empty in repository metadata |
| `language-model-*` | Three-repo language-model scaffold; currently empty in repository metadata |
| `prithvi-eo-regression-*` | Three-repo EO regression scaffold; currently empty in repository metadata |
| `prithvi-eo-segmentation-*` | Three-repo EO segmentation scaffold; currently empty in repository metadata |

### Archive / consolidation review candidates

These are **review candidates, not automatic actions**.

1. **`aiaas-marketability` and `naira-market-analysis`** — determine whether they are superseded by `aiaas-market-study`. If they are historical source material, archive them rather than deleting them.
2. **`ai-readiness-bot`** — determine whether it is a distinct product or an earlier/private implementation of `ai-readiness-assessment`.
3. **`naicri-deck-generator`** — if tied to a completed event and no longer reusable, archive after confirming there is no ongoing maintenance need.
4. **Empty model scaffolds** — `chronos-*`, `timesfm-*`, `language-model-*`, and `prithvi-*` currently report zero repository size. Decide whether each family is an intentional near-term roadmap item; otherwise archive the empty scaffolds until work resumes.
5. **Tabular-model component families** — `tabpfn-*` and `tabicl-*` contain six repositories each. Keep them separate only if pipeline, finetuner, and validator components are independently versioned/consumed; otherwise evaluate a family monorepo.
6. **MITRA component family** — currently active and populated. Preserve the existing split for now; revisit consolidation only if cross-repo coordination becomes the dominant maintenance cost.

## Repository families

GitHub personal repositories have no folder hierarchy, so repository names act as namespaces.

| Namespace | Portfolio meaning |
| --- | --- |
| `agentic-*` | Agent infrastructure and agent-native workflows |
| `mlops-*` | ML platform / operations infrastructure |
| `mitra-*` | MITRA classifier and regressor ecosystem |
| `tabpfn-*` | TabPFN model pipeline ecosystem |
| `tabicl-*` | TabICL model pipeline ecosystem |
| `chronos-*` | Chronos forecasting ecosystem |
| `timesfm-*` | TimesFM forecasting ecosystem |
| `prithvi-*` | Prithvi Earth-observation ecosystem |
| `naira-*` | NAIRA-specific work products |
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

- Keep **Active** to roughly 5–10 projects or families.
- Treat a repository family as one cognitive project when its component repos serve one product/system.
- Do not create a repository for an idea that has no implementation boundary yet; use an issue/spec in the parent project first.
- Archive completed/superseded work rather than leaving it indistinguishable from active work.
- Do not delete historical repositories unless they contain no useful provenance and deletion is intentional.
- Review visibility consistency inside repository families before making a family public.
- Prefer `main` for new repositories; do not rename established default branches solely for cosmetic consistency.
- Review this file quarterly or after a major project cycle and update `README.md` when the active set changes.

## Hygiene observations

The audit surfaced several low-cost consistency items for later review:

- Some established repositories still use `master` (`acabai-ph`, `agentic-vault`, `ai-readiness-bot`, `mlops-lite`, `naicri-deck-generator`, `naira-narrative-report`). This is not a blocker; normalize only when there is a practical reason.
- Some model families mix public and private visibility (for example, Chronos and Prithvi EO regression). Confirm whether that split is intentional before publishing or consolidating family-level work.
- Empty scaffold families contribute substantial visual repository count without adding current operational capability. Their value should be judged by roadmap intent, not by the sunk cost of having created them.

## Review cadence

At the end of each quarter or major project cycle:

1. Reconfirm the 5–10 Active projects/families.
2. Move dormant Active projects to Maintained or Experimental.
3. Review Experimental repos for promotion, consolidation, or archiving.
4. Review archive candidates explicitly before changing repository state.
5. Update the profile README only when the public-facing portfolio changes.

The governing principle is simple: **manage projects, not repository count**. Repository boundaries should reflect architecture, distribution, access, or operations—not the need for a new place to put an idea.
