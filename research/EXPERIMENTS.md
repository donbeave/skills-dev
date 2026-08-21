# Experiments A–H (design only)

**Not executed in this repository.** Operator rule: no local evals. These protocols exist so a later, isolated eval harness can falsify the doctrine.

Shared defaults unless an experiment overrides them:

| Item | Default |
| --- | --- |
| Models | Frontier, mid, cheap (one each). Pin versions. |
| Decoding | Primary: T=0. Secondary: T=0.7 for variance. |
| n | 30 independent trials per cell for binary metrics (see REPORT §24). 100 for any “≥99%” claim. |
| Skills | Same task family (e.g. skill-audit of a fixture SKILL.md). |
| Metrics | pass^1, pass^k (k=4,8), schema-valid %, procedure-trace match, tool-call exact-match, token-in, token-out, latency |
| Stats | Wilson CI on proportions; mixed-effects logistic regression with model as factor; pre-register success criterion |
| Independence | New request id; disable prefix cache if possible; paraphrase user wrapper as a factor |

## A — Monolithic vs specialized

- **IV:** one ~3000-token skill vs three ~1000-token siblings with mutually exclusive `description`s (create/update/audit).
- **DVs:** activation precision/recall; pass^1; pass^4; tokens to first useful action; wrong-sibling rate.
- **Controls:** same underlying procedures, same tools, same eval cases. Only packaging/routing changes.
- **n:** 30 per (packaging × model × case). ≥20 cases: 10 in-scope, 5 sibling-scope, 5 out-of-scope.
- **Interpretation:** split wins if activation precision ↑ and in-scope pass^k does not drop. Harmful decomposition if wrong-sibling + miss-both rise.
- **Stats:** McNemar on paired cases; bootstrap CI on token totals.
- **Why needed:** no published SKILL.md split ablation. τ-bench compound-write difficulty and IFEval multi-instruction drops are only **analogues**.

## B — Prose vs algorithm

- **IV:** same contract as (1) descriptive prose, (2) numbered procedure, (3) decision table + procedure.
- **DVs:** procedure-trace match (ordered tool names); pass^1; schema-valid %; cross-model gap (frontier−cheap).
- **Controls:** identical examples/tools/output schema. Word count matched ±10%.
- **n:** 30×3 formats×3 models×15 cases.
- **Interpretation:** algorithm wins if trace match ↑ especially on cheap models. Null if only frontier improves.
- **Stats:** ordinal mixed model on trace-match score.
- **Why needed:** Agentless vs agent on SWE-bench is adjacent, not skill-body format.

## C — Ambiguous vs explicit decisions

- **IV:** “use an appropriate method” vs `if A→X; if B→Y; else stop Z` (plus lookup table variant).
- **DVs:** decision entropy H = −Σ p_i log p_i over method choices; pass^1; unauthorized-improvisation rate.
- **Controls:** same methods available; only decision text changes.
- **n:** 30×2×3 models×12 cases (4 A, 4 B, 4 neither).
- **Interpretation:** supports Decision Surface hypothesis if H drops and neither-cases fail-closed more.
- **Stats:** permutation test on entropy; Fisher exact on fail-closed.

## D — Examples 0 / 1 / 3 / 5 / 10

- **IV:** number of I/O examples; secondary: diversity (all happy vs branch coverage including failure).
- **DVs:** pass^1, schema-valid %, format-copy rate (spurious example details), tokens.
- **Controls:** procedure text fixed. Example order shuffled as block factor (Lu 2022).
- **n:** 30×5 counts×2 diversity×3 models.
- **Interpretation:** diminishing returns when +2 examples <1 pp pass^1; interference if spurious-copy ↑.
- **Stats:** ANOVA/GAM of pass^1 on count.

## E — Context noise 0 / 25 / 50 / 100%

- **IV:** extra unrelated tokens as % of skill body (chat history, sibling skills, dummy files).
- **DVs:** pass^1; attention-to-constraint proxy = whether mandatory step still occurs; position of constraint (start/mid/end).
- **Controls:** gold constraint text unchanged. Noise from a fixed irrelevant corpus.
- **n:** 30×4 noise×3 positions×3 models.
- **Interpretation:** tests “minimum sufficient context”. Expect U-curve (Liu) on weaker/long packs; flatter on frontier (2410.14641) but relative spacing still hurts.
- **Stats:** logistic regression noise × position × model.

## F — Repeated runs

- **IV:** identical prompt, k ∈ {3,5,10,30,50,100}.
- **DVs:** pass^1; pass^k; unique trace count; semantic embedding variance of successful outputs.
- **Controls:** T=0 and T=0.7 arms.
- **n:** 100 per arm for the headline case; 30 for the rest.
- **Interpretation:** empirical pass^k curve vs binomial model. If T=0 unique traces >>1, document API non-determinism.
- **Stats:** Clopper-Pearson on p; plot pass^k(k).
- **Why needed:** τ-bench used user-simulator noise; we need **skill-only** repeats.

## G — Model strength

- **IV:** frontier / mid / cheap × (vague skill vs explicit contract+schema+scripts).
- **DVs:** pass^1; gap(frontier−cheap); schema-valid %.
- **Hypothesis:** explicit skills shrink the gap (weaker models behave closer to stronger).
- **n:** 30×3×2×15 cases.
- **Stats:** interaction term skill-type × model in logistic mixed model.
- **Why needed:** IFEval gap is instruction-following, not skill packaging. τ-bench policy ablation is the closest analogue (gpt-4o uses airline policy, gpt-3.5 does not).

## H — Skill mutation (metamorphic)

- **IV:** perturbation class: paraphrase, whitespace/format, option order, irrelevant prefix, filename, tool removed, extra sibling skill.
- **Oracle:** invariants (schema, forbidden tools, fail-closed on missing input) must hold; wording may change.
- **DVs:** invariant violation rate; pass^1 vs clean.
- **n:** 20 mutants × 10 cases × 10 trials (not 100 — mutation budget).
- **Stats:** per-class failure λ (as MT4NLP); Wilson CI.
- **Related:** PromptBench, Brittlebench, Wang & Zhu 75% detection on HumanEval errors.
