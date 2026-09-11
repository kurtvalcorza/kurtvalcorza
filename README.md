### 🚧 Current focus

Repository lifecycle: **Active** → **Maintained** → **Experimental/Incubating** → **Archived**. Component repos stay separate only when independent versioning, reuse, access control, CI, or deployment boundaries justify it. See **[PORTFOLIO.md](PORTFOLIO.md)**.

- **[agentic-vault](https://github.com/kurtvalcorza/agentic-vault)** — agent-agnostic knowledge infrastructure for Obsidian, including graph-aware retrieval, provenance, and multi-agent governance
- **[agentic-analytics](https://github.com/kurtvalcorza/agentic-analytics)** — MCP-native analytical runtime with reproducible execution and evidence provenance
- **Agent infrastructure (`agent-*`)** — host-neutral, independently usable layers for running AI agents under real constraints: [agent-relay](https://github.com/kurtvalcorza/agent-relay) (roles, handoffs, verification), [agent-router](https://github.com/kurtvalcorza/agent-router) (cost-aware model and executor routing), [agent-control](https://github.com/kurtvalcorza/agent-control) (lifecycle, budgets, policy, audit), and [agent-toolchain](https://github.com/kurtvalcorza/agent-toolchain) (distribution across harnesses, *in progress*)
- **[litert-lm-plugin-cc](https://github.com/kurtvalcorza/litert-lm-plugin-cc)** — local/on-device LiteRT-LM integration for Claude Code
- **DIMER model pipelines** — model integrations for the DIMER platform across tabular, vision, time-series, and language tasks, each pinning one immutable model revision, verifying weight checksums before load, and shipping machine-readable provenance with every result

### 🔬 Research & synthesis
- **[market-study-template](https://github.com/kurtvalcorza/market-study-template)** — a scaffold for structured market research studies: a Quarto book rendering to PDF/DOCX, a TypeScript survey instrument, and pre-specified analysis contracts so the output tables exist *before* any data is collected
- **[citation-audit](https://github.com/kurtvalcorza/citation-audit)** — audits a finished reference list against the bibliographic record, catching fabricated, misattributed, and misdirected citations — including identifiers that resolve cleanly to an entirely different paper. Keyless; the calls that change what a document claims stay with the human
- **[agentic-research](https://github.com/kurtvalcorza/agentic-research)** — 23-skill PRISMA 2020 / GRADE systematic-review pipeline: a *question* → a *defensible synthesis*
- **[agentic-analytics](https://github.com/kurtvalcorza/agentic-analytics)** — an agent-agnostic, MCP-native analytical runtime: reproducible sandboxed execution with source→execution→evidence provenance and deterministic validation, so an agent's analysis can be re-run and checked instead of taken on trust

### 📚 Knowledge work
- **[keynote-builder](https://github.com/kurtvalcorza/keynote-builder)** — a governed, human-gated pipeline that turns a brief into a stage-ready keynote (slide deck + speaker script)
- **[office-reports](https://github.com/kurtvalcorza/office-reports)** — agent skills for institutional document drafting: travel reports, minutes, and a weekly → terminal M&E reporting pipeline, evidence-only with gap flags
- **[presentation-builder](https://github.com/kurtvalcorza/presentation-builder)** — composable skills for finished presentations: Marp, native PPTX, HTML slides, talk scripts
- **[research-deck-builder](https://github.com/kurtvalcorza/research-deck-builder)** — a research/training module → a presenter-ready, source-checked deck
- **[agentic-vault](https://github.com/kurtvalcorza/agentic-vault)** — an Obsidian vault template for working *with* AI agents (PARA + multi-agent governance)

### 🏛️ Applied AI for government & organizations
- **[ai-readiness-assessment](https://github.com/kurtvalcorza/ai-readiness-assessment)** — an AI-readiness assessment chatbot for Philippine government agencies & NGOs

### ⚙️ ML infrastructure & experiments
- **[litert-lm-plugin-cc](https://github.com/kurtvalcorza/litert-lm-plugin-cc)** — an unofficial Claude Code plugin for a local, on-device model served by LiteRT-LM: offline, no API tokens, nothing leaving the machine — and a metadata repair for the silent CPU fallback that costs a measured 4.3×
- **[mlops-lite](https://github.com/kurtvalcorza/mlops-lite)** — a full-lifecycle, single-GPU MLOps platform (data → train → serve → monitor → retrain)
- **DIMER model pipelines** — model integrations for the DIMER platform, all built to one contract: a pinned immutable model revision, checksum-verified weights, validation before inference, and machine-readable provenance with every result. Tabular classifier/regressor pairs for [Mitra](https://github.com/kurtvalcorza/mitra-classifier-pipeline), [TabICL](https://github.com/kurtvalcorza/tabicl-classifier-pipeline), [TabPFN](https://github.com/kurtvalcorza/tabpfn-classifier-pipeline), and [TabDPT](https://github.com/kurtvalcorza/tabdpt-classifier-pipeline); vision via [Swin](https://github.com/kurtvalcorza/swin-classification-pipeline) (classification, detection, segmentation) and [SigLIP 2](https://github.com/kurtvalcorza/siglip2-vision-language-pipeline) zero-shot vision-language; time series via [Chronos-2](https://github.com/kurtvalcorza/chronos-2-forecasting-pipeline) probabilistic forecasting and [MOMENT](https://github.com/kurtvalcorza/moment-pipeline) embeddings, imputation, and anomaly scoring; and [LoRA/QLoRA fine-tuning contracts](https://github.com/kurtvalcorza/language-model-pipeline) for compatible causal language models
- **[notebooks](https://github.com/kurtvalcorza/notebooks)** — ready-to-run Colab speech & ML experiments (ASR, diarization, TTS)

### 🧰 Web apps & tools
- **Agent infrastructure (`agent-*`)** — four independently usable layers for running AI agents under real constraints: [agent-relay](https://github.com/kurtvalcorza/agent-relay) hands work between agents through durable artifacts and a verifier gate; [agent-router](https://github.com/kurtvalcorza/agent-router) routes each subtask to the cheapest executor that can satisfy it, then escalates on failed verification; [agent-control](https://github.com/kurtvalcorza/agent-control) owns lifecycle, budgets, policy, and an append-only audit trail; [agent-toolchain](https://github.com/kurtvalcorza/agent-toolchain) *(in progress)* installs and validates all of it across harnesses
- **[pdf-signer-pwa](https://github.com/kurtvalcorza/pdf-signer-pwa)** — private, offline PKCS#12 PDF signing that never leaves your device

![](https://komarev.com/ghpvc/?username=kurtvalcorza&style=pixel)
