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

# Agentic Vault Template
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/kurtvalcorza/agentic-vault)

An Obsidian vault template for working *with* AI agents — PARA + Zettelkasten organization, a multi-agent governance layer (`AGENTS.md` as a shared constitution for Claude Code, Gemini CLI, Kiro, Codex, etc.), 36 reusable agent skills, and hands-off automation: session logs with agent provenance, secret-gated git snapshots, and off-site history backups.

# Notebooks: Colab ML & Audio Experiments
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/kurtvalcorza/notebooks)

Ready-to-run Google Colab notebooks for speech and ML experiments — audio transcription, speaker diarization, and text-to-speech with OpenAI Whisper, `gpt-4o-transcribe-diarize`, Microsoft VibeVoice-ASR, and Qwen3-ASR/TTS, plus utilities like H2O Flow. Open any notebook in Colab straight from the [repo README](https://github.com/kurtvalcorza/notebooks#readme).
