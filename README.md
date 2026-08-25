### Strategic comms for AI R&D. Practical AI tools for the Philippine public sector.

Practical tools ***built with AI*** — assessment chatbots, agent skills, and lightweight ML systems — spec-driven and human-gated where it matters.

---

#### 🚧 Current focus

Repository lifecycle: **Active** → **Maintained** → **Experimental/Incubating** → **Archived**. Component repos stay separate only when independent versioning, reuse, access control, CI, or deployment boundaries justify it. See **[PORTFOLIO.md](PORTFOLIO.md)**.

- **[agentic-vault](https://github.com/kurtvalcorza/agentic-vault)** — agent-agnostic knowledge infrastructure for Obsidian, including graph-aware retrieval, provenance, and multi-agent governance
- **[agentic-analytics](https://github.com/kurtvalcorza/agentic-analytics)** — MCP-native analytical runtime with reproducible execution and evidence provenance
- **agent-router** — agent-agnostic model routing and policy infrastructure *(private)*
- **aiaas-market-study** — reproducible AI-as-a-Service market/feasibility research workflow *(private)*
- **inventory-intelligence** — applied inventory intelligence system *(private)*
- **[litert-lm-plugin-cc](https://github.com/kurtvalcorza/litert-lm-plugin-cc)** — local/on-device LiteRT-LM integration for Claude Code
- **mlops-grid** — MLOps infrastructure work *(private)*
- **[MITRA model pipelines](https://github.com/kurtvalcorza/mitra-regressor-pipeline)** — reusable classifier/regressor pipeline, finetuning, and dataset-validation components

#### 🔬 Research & synthesis
- **[market-study-template](https://github.com/kurtvalcorza/market-study-template)** — a scaffold for structured market research studies: a Quarto book rendering to PDF/DOCX, a TypeScript survey instrument, and pre-specified analysis contracts so the output tables exist *before* any data is collected
- **[citation-audit](https://github.com/kurtvalcorza/citation-audit)** — audits a finished reference list against the bibliographic record, catching fabricated, misattributed, and misdirected citations — including identifiers that resolve cleanly to an entirely different paper. Keyless; the calls that change what a document claims stay with the human
- **[agentic-research](https://github.com/kurtvalcorza/agentic-research)** — 23-skill PRISMA 2020 / GRADE systematic-review pipeline: a *question* → a *defensible synthesis*
- **[agentic-analytics](https://github.com/kurtvalcorza/agentic-analytics)** — an agent-agnostic, MCP-native analytical runtime: reproducible sandboxed execution with source→execution→evidence provenance and deterministic validation, so an agent's analysis can be re-run and checked instead of taken on trust
- **[research-writer](https://github.com/kurtvalcorza/research-writer)** — subagent-orchestrated, citation-checked literature-review drafting

#### 📚 Knowledge work
- **[dost-progress-report](https://github.com/kurtvalcorza/dost-progress-report)** — one Markdown file → a Word progress report in the DOST prescribed format (Forms 6 & 7), with nine checks that catch dropped chapters, stale cross-references, and citation gaps
- **[keynote-builder](https://github.com/kurtvalcorza/keynote-builder)** — a governed, human-gated pipeline that turns a brief into a stage-ready keynote (slide deck + speaker script)
- **[office-reports](https://github.com/kurtvalcorza/office-reports)** — agent skills for institutional document drafting: travel reports, minutes, and a weekly → terminal M&E reporting pipeline, evidence-only with gap flags
- **[presentation-builder](https://github.com/kurtvalcorza/presentation-builder)** — composable skills for finished presentations: Marp, native PPTX, HTML slides, talk scripts
- **[research-deck-builder](https://github.com/kurtvalcorza/research-deck-builder)** — a research/training module → a presenter-ready, source-checked deck
- **[agentic-vault](https://github.com/kurtvalcorza/agentic-vault)** — an Obsidian vault template for working *with* AI agents (PARA + multi-agent governance)

#### 🏛️ Applied AI for government & organizations
- **[acabai-ph](https://github.com/kurtvalcorza/acabai-ph)** — the DOST-ASTI showcase site for the Philippines' national AI initiatives (NAIRA, DIMER, iTANONG), with an embedded chatbot and automatic failover
- **[ai-readiness-assessment](https://github.com/kurtvalcorza/ai-readiness-assessment)** — an AI-readiness assessment chatbot for Philippine government agencies & NGOs

#### ⚙️ ML infrastructure & experiments
- **[litert-lm-plugin-cc](https://github.com/kurtvalcorza/litert-lm-plugin-cc)** — an unofficial Claude Code plugin for a local, on-device model served by LiteRT-LM: offline, no API tokens, nothing leaving the machine — and a metadata repair for the silent CPU fallback that costs a measured 4.3×
- **[inference-bench](https://github.com/kurtvalcorza/inference-bench)** — an MLPerf + TensorRT inference and GPU/CPU hardware benchmark suite across heterogeneous hardware (RTX 5070 Ti, T4, A100/H200, CPU), with reproducible scripts, notebooks, and results
- **[benchmarking-harness](https://github.com/kurtvalcorza/benchmarking-harness)** — a model-class-aware, three-tier evaluation gate for computer-vision models (capability → domain stress → operational safety) with a human review gate and auto-generated Model Cards
- **[mlops-lite](https://github.com/kurtvalcorza/mlops-lite)** — a full-lifecycle, single-GPU MLOps platform (data → train → serve → monitor → retrain)
- **[mitra-classifier-pipeline](https://github.com/kurtvalcorza/mitra-classifier-pipeline)** — a DIMER pipeline that fine-tunes Mitra (AutoGluon, Apache-2.0) — a tabular foundation model pretrained on 45M synthetic datasets and no real data — on your own categorical target; ships as a CPU dataset validator plus a GPU fine-tuner
- **[mitra-regressor-pipeline](https://github.com/kurtvalcorza/mitra-regressor-pipeline)** — the same pipeline for a numeric target, with a zero-shot in-context mode when no GPU is available
- **[tabicl-classifier-pipeline](https://github.com/kurtvalcorza/tabicl-classifier-pipeline)** — a DIMER pipeline for TabICLv2 (Inria Soda, BSD-3-Clause), an in-context learner that reads labelled rows as context: a column-wise pass builds a distribution-aware embedding per feature, then a row-wise pass classifies
- **[tabicl-regressor-pipeline](https://github.com/kurtvalcorza/tabicl-regressor-pipeline)** — the TabICLv2 regressor, fine-tuned through `FinetunedTabICLRegressor` with a pinball/quantile loss and validation-based selection
- **[notebooks](https://github.com/kurtvalcorza/notebooks)** — ready-to-run Colab speech & ML experiments (ASR, diarization, TTS)

#### 🧰 Web apps & tools
- **[wsl-crew](https://github.com/kurtvalcorza/wsl-crew)** — a Windows tray app that keeps WSL2-hosted services alive: survives idle shutdowns, re-points portproxy rules when the distro IP changes on reboot, and turns the commands you'd otherwise re-Google into one-click repairs
- **[pdf-signer-pwa](https://github.com/kurtvalcorza/pdf-signer-pwa)** — private, offline PKCS#12 PDF signing that never leaves your device

![](https://komarev.com/ghpvc/?username=kurtvalcorza&style=pixel)
