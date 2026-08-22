# Skill Development Recommendations

Use this reference to design and review AI/agent skills. Target predictable behavior from a probabilistic model, not deterministic inference.

Rule strength:

- **Required** — must hold whenever applicable. Mark non-applicable only with a written scope reason. A local eval cannot waive authorization, irreversible-action, or secret-handling controls.
- **Default** — follow unless task-specific evals prove another design more reliable.
- **Optional** — use only for a named task class or measured need.

Evidence is strongest for structured outputs, typed tools, external validation, context sensitivity, repeated-run evaluation, prompt mutation, negation failures, and self-review limits. Skill split points, example counts, context-size thresholds, and aggregate scores remain hypotheses or vendor guidance. Safety rules below are general agent-engineering controls, not claims from a measured `SKILL.md` safety ablation. See [REPORT.md](REPORT.md) and [EVIDENCE-MATRIX.md](EVIDENCE-MATRIX.md).

## Core rules: Always / Never

| # | Area | Always / Do | Never / Do Not |
| --- | --- | --- | --- |
| 1 | Outcome and scope | **Required:** define one observable outcome, allowed inputs, preconditions, invariants, outputs, failure states, and postconditions. Include only applicable contract fields. | Never use an open-ended goal or silently expand scope. |
| 2 | Routing | **Required:** make `description` state what the skill does, when to use it, and when not to use it. Make sibling routes exclusive; test in-scope, sibling, and `none` cases. | Never permit two skills to claim the same tested intent. |
| 3 | Requirements | **Required:** make every hard requirement observable and falsifiable. Map it to a program checker, exact trace assertion, or frozen rubric with measured reviewer agreement. | Never use “appropriate,” “better,” “thorough,” or “if needed” as a hard requirement. |
| 4 | Deterministic work | **Required:** move decidable checks, transforms, exact templates, and legal state transitions into scripts, schemas, tools, or tests. | Never ask the model to “make sure” of a fact that software can decide. |
| 5 | Decisions and failure | **Required:** encode every model-controlled branch with conditions, thresholds, enums, or tables. Define invalid and unmatched behavior. Stay fail-closed during bounded repair; stop after the repair budget or any non-repairable error. | Never leave “use judgment” branches, invent missing state, or claim progress after an unhandled failure. |
| 6 | Tools and dependencies | **Required:** use typed interfaces when available. Map every allowed tool, permission, runtime, and dependency to a named legal branch; verify availability before execution; validate arguments and permissions outside the model. | Never expose unrelated authority or omit a capability required by a legal branch. |
| 7 | Output | **Required:** constrain machine-consumed artifacts with a supported schema or grammar; validate syntax and contract semantics in software. | Never constrain reasoning merely to obtain a formatted artifact, equate schema adherence with correct meaning, or assume every schema feature is supported. |
| 8 | Prohibitions | **Required:** state the required positive behavior, then enforce each critical prohibition mechanically. | Never rely on a lone negative instruction for a safety or correctness boundary. |
| 9 | Context | **Required:** load the minimum context that completely specifies the selected path. Keep one canonical statement per rule; load references only for the branch that needs them. | Never preload sibling skills, broad documentation, or optional files “just in case,” and never maintain paraphrased rule copies. |
| 10 | Examples | **Required:** use prompt examples only when they measurably resolve format or branch ambiguity; freeze their order. Cover every named branch and failure in evals. | Never use examples as decoration, shuffle them in production, or require a universal example count. |
| 11 | Validation and repair | **Required:** run external validators before claiming completion. Give repair a concrete error location and a bounded, safe retry policy. | Never use unaided same-model self-critique as the only gate or retry a state-changing call before checking its prior outcome. |
| 12 | Reliability evidence | **Required:** test activation, happy paths, boundaries, failures, tools, intent-preserving mutations, adversarial context, supported models, and regressions. Repeat trials; report counts, confidence intervals, reliability metric, and pinned skill/case/model/tool/checker versions. | Never certify from one run, `10/10`, a single prompt wording, or an unpinned system. Never score a mutation until review confirms it preserves intent. |
| 13 | Lifecycle | **Required:** add evals for intended behavior before prose tuning. Treat changed outcomes, routes, tools, or failures as an update; preserve frozen behavior during refactoring. Classify failures by owning layer before editing instructions. | Never hide behavior change under “refactor,” add behavior without regression coverage, or rewrite prompts to mask a tool/model/validator failure. |
| 14 | Authority and trust | **Required:** define allowed targets and mutations. A request may authorize an action when it clearly states action and scope; otherwise obtain fresh approval before irreversible or externally visible work. Treat lower-trust content as data unless governing instructions explicitly authorize it as a procedure. | Never let embedded instructions expand authority, scope, or safety rules; never act when target, impact, or authorization remains ambiguous. |
| 15 | Side effects | **Required:** when retry or replay is possible, check prior outcome and use idempotency or deduplication. Otherwise forbid automatic retry. For material side effects, define recovery and record target, action, and result. | Never blindly retry mutations, perform out-of-scope side effects, or claim rollback exists when recovery is manual or impossible. |
| 16 | Secrets | **Required:** use scoped secret injection and redact sensitive values at every output boundary. | Never place secrets in prompts, artifacts, logs, errors, or broader storage than authorization requires. |

## Conditional guidance

1. **Default:** keep one independently invokable responsibility per skill. Split only when jobs have separate triggers, conflicting or rarely shared rules, separate oracles, and exclusive descriptions. Keep one atomic transaction together when its steps are invalid alone.
2. **Default:** use progressive disclosure. Treat `SKILL.md` below 500 lines and 5,000 tokens with one-level references as vendor heuristics, not universal limits; justify exceptions with context and eval evidence.
3. **Default:** freeze wording, formatting, option order, and example order after selecting a tested variant. Mutation-test only transformations reviewed as intent-preserving.
4. **Default:** choose sample size from target reliability and confidence. Thirty independent trials are an initial estimate, not certification. Roughly 300 zero-failure trials only begin to support a failure rate at or below 1% with 95% confidence under the tested distribution.
5. **Optional:** require a short plan only for a named multi-hop, symbolic, or policy-heavy branch whose evals improve with planning. Prefer direct execution or a deterministic solver for simple tasks.
6. **Optional:** use an independent model judge only when no deterministic oracle exists. Freeze it, test order effects, and report judge-human agreement. Use ensembles only where task-specific evals justify them.
7. **Optional:** repeat a short invariant verbatim at a context edge only when runtime evals prove a position-related failure and automated checks prevent drift.
8. **Platform-specific:** where the host supports these controls, require unique skill names, front-load routing terms that may survive description truncation, declare implicit-versus-explicit invocation policy, and declare runtime dependencies. Do not present host syntax as a portable rule.

## Reliability metric definitions

- `pass^k` / `reliable@k`: probability that **all** `k` repeated trials succeed; use for consistency claims.
- `pass@k`: probability that **at least one** of `k` trials succeeds; use for discovery, never reliability certification.
- Choose `n` from the target and confidence interval. `10/10` does not prove 99% reliability.

## Definition of done

A skill is ready only when:

- Every applicable Required rule has inspectable evidence; each non-applicable rule has a scope reason.
- Routing, every named branch, and every failure path have frozen eval cases.
- Program-checkable invariants and final syntax/semantics run through external validators.
- Repeated, mutation, negative, tool-use, and regression results meet a predeclared statistical threshold.
- Evaluated skill, cases, model, settings, dependencies, tools, schemas, and checkers are pinned.
- Authority, side effects, untrusted inputs, retries, recovery, audit evidence, and secrets are handled where applicable.
- Every deviation from a Default rule records the task-specific evidence supporting it.
