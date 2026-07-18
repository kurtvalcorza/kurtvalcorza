# AI Readiness Assessment Chatbot
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/kurtvalcorza/ai-readiness-assessment)

Self-service chatbot for assessing AI readiness of Philippine government agencies and NGOs.

# Research Writer: Subagent-Based Research Orchestration
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/kurtvalcorza/research-writer)

Multi-agent literature review workflow for Claude Code. Turns research PDFs into a structured, citation-checked literature review draft through an optional search-strategy phase plus 7 core phases, each running in an isolated context — with human checkpoints, two quality gates (citation integrity and cross-phase consistency), and resumable execution.

# Agentic Research: AI-Agent Pipeline for Literature & Systematic Reviews
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/kurtvalcorza/agentic-research)

A suite of 23 composable agent skills that take a review from a *question* to a *defensible synthesis* — design a registrable PRISMA-P protocol, search the literature (multi-database + snowball with a PRISMA-S log), deduplicate, screen (single or dual-reviewer with Cohen's κ), extract, appraise risk of bias, grade certainty with GRADE, draft, and verify every citation against the real bibliographic record — emitting a PRISMA 2020 flow diagram whose numbers reconcile or the build fails. Keyless by default (OpenAlex/CrossRef + Python stdlib), aligned with PRISMA 2020, Cochrane, and GRADE, and deliberately human-gated where LLMs are weak (risk-of-bias appraisal, numeric verification).

# Research Deck Builder
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/kurtvalcorza/research-deck-builder)

Claude Code skill that turns a written research/training module (Markdown with references) into a polished, presenter-ready PowerPoint deck — outline, source-checked citations, an embedded speaker script, and a clean dark + blue design built from vector shapes. Also repairs existing decks: reinstates dropped citations, embeds notes, and re-skins backgrounds, with a QA gate that verifies structure and fidelity against the source.

# Presentation Builder
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/kurtvalcorza/presentation-builder)

A suite of composable, agent-ready skills for turning source material into finished presentations — synthesize research into Marp decks, generate native PowerPoint, build HTML slides, draft a spoken talk script, turn speeches into producer rundowns/storyboards, or summarize a folder of slide images into a note. Each skill follows the open [Agent Skills](https://agentskills.io) standard (a `SKILL.md` plus supporting scripts), works on its own, and chains into a single source-to-deck pipeline.

# Agentic Vault Template
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/kurtvalcorza/agentic-vault)

An Obsidian vault template for working *with* AI agents — PARA + Zettelkasten organization, a multi-agent governance layer (`AGENTS.md` as a shared constitution for Claude Code, Gemini CLI, Kiro, Codex, etc.), 36 reusable agent skills, and hands-off automation: session logs with agent provenance, secret-gated git snapshots, and off-site history backups.

# Notebooks: Colab ML & Audio Experiments
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/kurtvalcorza/notebooks)

Ready-to-run Google Colab notebooks for speech and ML experiments — audio transcription, speaker diarization, and text-to-speech with OpenAI Whisper, `gpt-4o-transcribe-diarize`, Microsoft VibeVoice-ASR, and Qwen3-ASR/TTS, plus utilities like H2O Flow. Open any notebook in Colab straight from the [repo README](https://github.com/kurtvalcorza/notebooks#readme).

# PDF Signer PWA
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/kurtvalcorza/pdf-signer-pwa)

Sign PDFs privately on your phone or computer — a fully client-side, installable PWA where your document, signature image, and Digital ID **never leave the device** (a strict `connect-src 'none'` policy makes uploading structurally impossible), and it works offline once loaded. Applies real PKCS#12 (`.p12`/`.pfx`) digital signatures with your signature image as the visible appearance, can create a self-signed Digital ID in-app, and counter-signs already-signed PDFs on any page without invalidating the existing signatures. TypeScript · React · Vite · `pdf-lib` · `pdf.js` · `@signpdf`; the signing path is verified end-to-end with pyHanko.

# AIaaS Demand Viability Index (DVI) Chatbot
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/kurtvalcorza/aiaas-marketability)

A chatbot-supported **marketability and demand-validation** instrument for a localized AI-as-a-Service platform (DOST-NAIRA). A two-phase hybrid — a structured form plus a short reconciling chat — that routes respondents into an RR/DD segment matrix with an Advanced-Demand overlay, gathers competitor-friction and value-proposition evidence, and computes a study-specific **Demand Viability Index** deterministically in code (the language model never computes a score). Built on the ai-readiness-assessment infrastructure: streaming chat, rate limiting, PII redaction, consent-gated contact storage, and dual Neon / Google Sheets storage.

# MLOps-Lite
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/kurtvalcorza/mlops-lite)

A lightweight, full-lifecycle MLOps platform that runs **locally on one machine** — data → train → register → serve → monitor → retrain — around a single GPU held by at most one tenant under a race-free, in-process admission lock. Serves five modalities (LLM text-generation, vision, embeddings, ASR, tabular), fine-tunes with LoRA lineage and adapter-chaining, and gates promotion through an offline eval harness with champion-challenger, Optuna hyperparameter optimization, ground-truth quality monitoring, and a closed declarative drift → retrain → gate → promote policy loop. Spec-driven (GitHub Spec Kit); MLflow registry/tracking, a Garage object store, Postgres monitoring/job state, and Prometheus + Grafana.

![](https://komarev.com/ghpvc/?username=kurtvalcorza&style=pixel)
