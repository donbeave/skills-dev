# Operator guideline: skill development for predictability

This is the short process derived from [`REPORT.md`](REPORT.md). Numbers and citations live there. **No evals were run in this repo.**

Models will not become deterministic. Predictability is an **engineering property of the system around the model**.

## Non-negotiables

1. **Anything a program can check, a program must check.** Files exist, schema valid, required fields, forbidden tools, grep for banned patterns, unit tests. The model does not “make sure”.
2. **Constrain the artifact, not the thought.** JSON Schema / grammar / typed tool args on the *output*. Free-form scratch allowed *before* the artifact. Do not force CoT into JSON (Tam 2024: answer-before-reason killed reasoning).
3. **One independently invokable responsibility per skill.** Split only when jobs have separate triggers, conflicting or rarely shared rules, separate oracles, and exclusive descriptions. Keep an atomic transaction together when its steps are invalid alone.
4. **Explicit decisions.** Replace “as appropriate” with `if A then X else if B then Y else stop Z`. Count unconstrained decisions (Decision Surface). Drive that count down.
5. **Minimum context.** `description` always loaded. Body loaded on trigger. References/scripts only on the branch that needs them. Unused files are distractors (Shi: ≤18% items stay consistent across distractors).
6. **Triggers are a classifier.** `description` = what + when + when-not. Sibling skills must be mutually exclusive. Overlap is an activation bug.
7. **Requirements have explicit oracles.** Make them observable, measurable, and falsifiable. Prefer program checks; when meaning requires judgment, freeze the rubric and measure reviewer agreement.
8. **Do X (and validate).** Do not rely on “Never do Y” alone (negation accuracy can sit ~50% while positive sits ~95%).
9. **Examples resolve demonstrated ambiguity.** Use the smallest set that measurably helps; pin order. Cover every decision branch and failure in evals, not necessarily in prompt examples.
10. **Certify with pass^k, not a demo.** 10/10 ≠ ≥99%. Choose n from the target and confidence; n=30 is an initial estimate, while n≈300 zero-fail only begins 99% talk under the rule of three. Mutate prompts. Pin model version.

## What lives where

| Layer | Put here | Why |
| --- | --- | --- |
| `SKILL.md` frontmatter | `name`, `description` (what + when + not-when) | Routing; ~100 tokens always in context |
| `SKILL.md` body | Purpose, preconditions, procedure, decision table, output contract, failure stops | Loaded only when triggered |
| `scripts/` | Checks, transforms, schema validate, idempotent tools | Deterministic; output only enters context |
| `schemas/` / `assets/` | JSON Schema, enums, templates | Constrained decoding + validators |
| `references/` | Branch-specific docs | Load on demand, one level deep |
| `evals/` | Activation, happy, boundary, negative, mutation, tool, cross-model, regression | pass^k oracles |

## Create / update / refactor

**Create:** specify contract → list decision branches → move branches to code/schema where possible → write short procedure for the rest → add only examples that resolve measured ambiguity → evals **before** polishing prose → freeze format.

**Update:** add evals for new behavior first; run regression on old cases; do not expand responsibility without split review.

**Refactor:** no intended behavior change. Mutation + regression must stay green. New characterization cases may document existing behavior; changed expected behavior is an update.

## Smell → action

| Smell | Action |
| --- | --- |
| “as appropriate”, “better”, “thorough” | Rewrite as threshold or table, or drop |
| Two independently invokable jobs | Split |
| Overlapping sibling `description`s | Rewrite until mutually exclusive |
| Output with no validator | Add schema/script |
| >5k tokens or >500 lines in SKILL.md | Split files; progressive disclosure |
| Self-review as the only check | Replace with oracle |
| Mandatory plan on simple tasks | Make planning conditional or forbid |
| Tool buffet | `allowed-tools` |
| Lone NEVER | Add DO + mechanical check |

## Closest thing to determinism

```
narrow skill
+ explicit contract
+ low decision freedom
+ min context
+ deterministic scripts/schemas
+ typed tools / structured I/O
+ validate-or-stop
+ pass^k + mutation + regression
```

That stack is a **hypothesis** supported by adjacent measurements (structured outputs 100% syntax, τ-bench pass^k collapse, IFEval verifiability, Huang self-correct failure). It is **not** a published RCT on SKILL.md files. Run experiments A–H in an eval harness **outside** this research repo if you need skill-format proof.
