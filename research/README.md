# Research corpus

This directory holds the research product and the notes it was built from.

## Read first

[`REPORT.md`](REPORT.md) is the deliverable. Everything else is supporting evidence.

## File map

| File | Role |
| --- | --- |
| `GUIDELINE.md` | Short operator process for predictable skills |
| `SPAWN-PROMPT.md` | Prompt to spawn a follow-on literature agent (no local evals) |
| `REPORT.md` | Topics 1–33 + Parts I–VIII + closing architecture |
| `CITATIONS.md` | Numbered bibliography |
| `EVIDENCE-MATRIX.md` | Technique × evidence × measured effect |
| `EXPERIMENTS.md` | Experiments A–H, designed not executed |
| `coverage.md` | Topic coverage checklist |
| `sources/` | Per-cluster notes with extracted measurements |

## Source clusters

| File | Cluster |
| --- | --- |
| `sources/01-prompt-sensitivity.md` | Formatting, order, few-shot, calibration, PromptBench, Brittlebench |
| `sources/02-context-position.md` | Lost-in-the-middle, distraction, progressive disclosure |
| `sources/03-instruction-following.md` | IFEval, IFEval++, instruction hierarchy, negation |
| `sources/04-structured-outputs.md` | Constrained decoding, JSON Schema, quality vs syntax |
| `sources/05-tool-use-agents.md` | τ-bench, BFCL, SWE-bench, scaffolds |
| `sources/06-self-correction-planning.md` | Self-correct, CoT, self-consistency, planning |
| `sources/07-vendor-skill-systems.md` | Anthropic Skills, OpenAI, Cursor, Copilot, OpenHands |
| `sources/08-evals-mutation-stats.md` | pass^k, sample size, metamorphic testing |
| `sources/09-system-order-position.md` | system vs user, MCQ option order, judge position |
