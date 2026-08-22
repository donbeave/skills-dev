# Source cluster: vendor skill systems and frameworks

These are **production designs**. None published a controlled SKILL.md A/B with pass^k. Compare against empirical literature; do not treat as proven optima.

## Anthropic Agent Skills (2025) + agentskills.io spec

Measured? No public ablation of skill shape vs reliability.

Design choices that **align** with independent evidence:

| Choice | Independent support |
| --- | --- |
| Progressive disclosure (metadata → body → files) | Liu lost-in-the-middle; Shi distractors; τ-knowledge failure at 195K tokens |
| `description` = what + when | Routing is activation consistency; IFEval-style specificity |
| Scripts for deterministic work | OpenAI structured outputs; JSONSchemaBench; Huang (external feedback) |
| Eval-first authoring | τ-bench pass^k; IFEval++ reliable@k |
| SKILL.md <500 lines / <5k tokens (spec recommendation) | Context dilution; not a measured optimum |
| One-level file references | Lost-in-the-middle / fan-out |

Gaps: no published trigger-precision numbers; no split-vs-monolith experiment; “think from Claude’s perspective” is anecdotal.

## OpenAI: function calling, structured outputs, instruction hierarchy, Codex/Agent SDK

- Structured Outputs: **100%** schema follow on internal eval via **constrained decoding** after 93% from training (see 04).
- Instruction hierarchy: **+63%** prompt-extraction robustness (Wallace 2024).
- Function calling native > prompt-ReAct on τ-bench.
- JSON mode ≠ schema.
- Custom GPT instructions / Agent SDK: product docs, not evals of instruction architecture.

## Cursor / Copilot / Gemini / Claude Code / Codex CLI

- Mechanisms: rules files, AGENTS.md, custom instructions, skills, MCP.
- Overlapping rule files = instruction conflict (Wallace hierarchy; Sclar format; Shi distractors).
- No public pass^k of “.cursor/rules vs one SKILL.md”.
- Copilot: tests/CI as the real reliability layer for code, matching SWE-bench oracles.

## SWE-agent ACI vs OpenHands vs Agentless vs Devin-like

- Public systems use materially different scaffolds, but this corpus does not preserve a controlled same-model effect size.
- ACI (constrained edit/view commands) is a **reduced decision surface**.
- Agentless (fixed pipeline) sometimes matches agents — evidence that **explicit procedures** can replace free agent loops.

## MCP

- Tools as APIs. BFCL shows that selection and abstention are imperfect, but its reported slices do not isolate tool-count effects.
- Skills should expose a complete, task-scoped `allowed-tools` set: every required call, no unrelated authority. Treat the reliability benefit of fewer tools as a hypothesis; least authority remains a safety control.

## DSPy / Guidance / Outlines / LMQL / Instructor

- DSPy: compile prompts against metrics — closest to “skill as program + eval”. Published gains are task-specific; treat as **LIKELY** process analogue, not a skill-format winner.
- Guidance/Outlines: constrained decoding (see JSONSchemaBench).
- Instructor: generate → validate → retry. Matches verifier-loop **95%** coverage result.

## LangGraph / state-machine agents

- External state machine = decision surface moved to software.
- Aligns with “unnecessary decisions create variance” hypothesis. Direct skill-eval evidence: **not published**. **HYPOTHESIS** with strong adjacent support (ACI, Agentless, structured outputs).
