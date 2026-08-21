# Source cluster: structured outputs and constrained decoding

## OpenAI 2024 — Introducing Structured Outputs

- https://openai.com/index/introducing-structured-outputs-in-the-api/
- Internal complex JSON-schema eval:
  - `gpt-4-0613`: **<40%** schema adherence
  - `gpt-4o-2024-08-06` unconstrained (trained): **93%**
  - same model + constrained decoding (`strict: true`): **100%** on that eval
- Explicit statement: training alone **did not** meet reliability needs; **deterministic constrained decoding** was required for 100%.
- JSON mode ≠ schema adherence (valid JSON, wrong fields still possible).
- Implication: **syntactic/schema reliability can approach 100%** when moved out of free generation. **Semantic** correctness is not guaranteed.

**Grade:** Strong empirical (provider eval; schema not public — treat as provider-reported).

## JSONSchemaBench (Geng / EPFL-dlab et al. 2025)

- Paper: https://arxiv.org/abs/2501.10868
- ~10K real-world JSON schemas; engines: Guidance, Outlines, llama.cpp, XGrammar, OpenAI, Gemini.
- Coverage **collapses** on complex schemas:
  - GlaiveAI: Guidance empirical **96%**, compliance **98%**; OpenAI empirical **89%**, compliance **100%**; Gemini **86% / 100%**.
  - GitHub Easy: OpenAI empirical **~29–30%**, compliance **97%**.
  - GitHub Hard: Guidance **41%**, llama.cpp **39%**, XGrammar **28%**, Outlines **3%**.
- OpenAI/Gemini: **100% compliance on schemas they accept**, but they **reject / skip** many real schemas (coverage gap).
- XGrammar: **38 under-constrained** JSON Schema Test Suite categories (silent invalid JSON). Guidance: **1**.
- Quality: paper reports **~+3% average** task quality under constraints (contra Tam et al. on JSON-mode-for-reasoning).
- Implication: constrained decoding is **necessary but not sufficient**. Always **validate with a JSON Schema library**. Retry on failure. Keep skill schemas in the **supported subset**.

**Grade:** Strong empirical.

## Tam et al. 2024 — Let Me Speak Freely? (EMNLP Industry)

- Paper: https://arxiv.org/abs/2408.02442
- JSON-mode / format restrictions **hurt reasoning** (GSM8K, last-letter) vs free-form; **help classification**.
- GPT-3.5 JSON-mode: **100%** of last-letter responses put `"answer"` **before** `"reason"` — CoT was structurally prevented.
- Rebuttal (dottxt / Outlines): several results confounded by **schema that forces answer-before-reason**.
- Implication: **do not constrain the reasoning channel**. Constrain the **final artifact**. Allow free-form scratch, then emit schema-constrained output (or run a script).

**Grade:** Moderate empirical + important negative control. **PROVEN** that schema **shape** can destroy CoT; **not proven** that all constrained decoding hurts semantics.

## SO-Bench (2025)

- Schema validation can exceed **95%** on frontier models; **fully correct structured objects** as low as **~19%** fuzzy full-match (Gemini-2.5-Pro best in that paper).
- Implication: **syntax ≠ semantics**. A skill that “returns JSON” can be 98% valid and still 80%+ wrong.

**Grade:** Moderate empirical.

## Verifier-loop vs constrained decoding (OpenReview 2025, 9,558 schemas)

- gpt-5-nano structured-output coverage **~50%**; rejection sampling / verifier loop **~94–99%** at +1–4s latency.
- Implication: **generate → deterministic validate → repair** can beat “schema mode only” on real schemas.

**Grade:** Strong empirical for coverage; latency tradeoff documented.
