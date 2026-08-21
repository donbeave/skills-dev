# Source cluster: evaluation, mutation, statistics

## pass^k vs pass@k

- τ-bench (Yao et al. 2024): pass^k = P(all k trials succeed). gpt-4o retail **pass^1 ~61%**, **pass^8 <25%**.
- HumanEval (Chen et al. 2021): pass@100 **70.2%** vs pass@1 **28.8%** — discovery, not reliability.
- IFEval++: accuracy → reliable@10 drops **18–62%** relative depending on model.

**Skill implication:** a skill that is 10/10 on one prompt is **not** 99% reliable. Use pass^k, not pass@k, as the skill reliability metric.

## Binomial sample size (standard statistics; not an LLM paper)

Let true success probability be p. Observe s successes in n i.i.d. trials.

- Point estimate: ŝ = s/n.
- 95% Wilson/Clopper-Pearson interval for n=10, s=10: **~69%–100%**, not 99%.
- Rule of three (zero failures): 95% upper bound on failure rate ≈ 3/n. For ≥99% reliability (failure ≤1%), need **n ≥ 300** with zero failures, or a designed sequential test.
- n=3: almost no power. n=5: can reject p=0.5 sometimes, cannot claim 95%+. n=10: 10/10 ⇒ likely p>0.7, **not** p>0.99. n=30: 30/30 ⇒ ~88–100% (Clopper-Pearson 95%). n=50: 50/50 ⇒ ~93–100%. n=100: 100/100 ⇒ ~96.4–100%.

**Grade:** Strong (statistics). **Our engineering inference** for applying it to skills: treat each (skill, case, model) as a Bernoulli; report CI + pass^k.

Independence caveat: same prompt + T=0 + cached prefix is **not** i.i.d. Use paraphrases, context noise, and explicit seeds. Production APIs at T=0 still vary (τ-bench).

## PromptBench / Brittlebench / FormatSpread

- See 01. Mutation of wording/format is a **standard** robustness method.
- Brittlebench: ranking flips **63%** under one perturbation; up to **half** of variance from surface form.

## Metamorphic testing of LLMs

- Wang & Zhu 2024: metamorphic prompt testing detects **75%** of GPT-4 erroneous HumanEval programs, **8.6%** FP.
- MT4NLP / LLMORPH: 36 MRs, ~560k tests, GPT-4 / Llama 3 / Hermes-2; **mean failure rate 18%** (up to **80%** per MR); manual TP **~62%**.
- MORTAR: multi-turn dialogue MT, **+150%** bugs vs single-turn baseline.

**Implication:** mutation/metamorphic evals should be **standard** in skill development (paraphrase, order, noise, filename, tool-subset). Oracle = skill invariants, not “same string”.

## Prompt Stability Score

- Intra-run (same prompt) and inter-prompt (paraphrase) agreement as reliability coefficients.
- Maps to skill: structural consistency + semantic variance.

## Reproducibility of LLM evals

- Biderman / Eleuther and later reproducibility papers: seeds, decoding, dates, system prompts all move numbers.
- Skill regression suites must pin **model version, decoding, skill hash, case hash**.
