# Designing AI Skills for Maximum Predictability

Evidence-driven research on how to author, structure, test, evaluate, and maintain **AI/agent skills** so repeated executions converge on intended behavior — without pretending language models are deterministic.

**No model evals are run in this repository.** Experiments A–H are protocols only.

| Start here | Why |
| --- | --- |
| [`research/SKILL-DEVELOPMENT-RECOMMENDATIONS.md`](research/SKILL-DEVELOPMENT-RECOMMENDATIONS.md) | Simple rules: what to do and never do |
| [`research/GUIDELINE.md`](research/GUIDELINE.md) | Operator process (create/update/refactor) |
| [`research/REPORT.md`](research/REPORT.md) | Full argument, topics 1–33, Parts I–VIII |
| [`research/SPAWN-PROMPT.md`](research/SPAWN-PROMPT.md) | Prompt to spawn a follow-on literature agent |

Repository: [github.com/donbeave/skills-dev](https://github.com/donbeave/skills-dev)

## Question

> How can we engineer a skill and the skill-development process so that repeated executions converge toward the intended behavior, follow the intended procedure, produce structurally consistent results, and minimize unwanted behavioral variance?

The goal is **not** to make LLMs deterministic. Inference is stochastic. The goal is an engineering system around the model that yields the closest practical equivalent of deterministic skill behavior.

## Contents

| Path | What |
| --- | --- |
| [`research/REPORT.md`](research/REPORT.md) | Full report: topics 1–33, Parts I–VIII, experiments A–H |
| [`research/SKILL-DEVELOPMENT-RECOMMENDATIONS.md`](research/SKILL-DEVELOPMENT-RECOMMENDATIONS.md) | Standalone Always/Never reference and definition of done |
| [`research/CITATIONS.md`](research/CITATIONS.md) | Bibliography with measured results |
| [`research/EVIDENCE-MATRIX.md`](research/EVIDENCE-MATRIX.md) | Technique × evidence × measured effect |
| [`research/EXPERIMENTS.md`](research/EXPERIMENTS.md) | Designed experiments A–H (protocol, not executed) |
| [`research/sources/`](research/sources/) | Paper-level notes with numbers |
| [`PROMPT.md`](PROMPT.md) | Original research brief |

## Evidence grades used throughout

- **PROVEN** — repeated quantitative evidence, named source, reported n
- **LIKELY** — good evidence, limited or indirect for skills
- **HYPOTHESIS** — engineering inference that still needs our evals

Recommendation tags: **Strong empirical** / **Moderate empirical** / **Weak-anecdotal** / **Our engineering inference**

## Non-goals

- Zero-variance inference
- Shipping a production linter or eval harness in this repo
- Treating any vendor skill format as optimal without comparison

## License

[CC BY 4.0](LICENSE)
