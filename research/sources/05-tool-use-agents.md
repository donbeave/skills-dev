# Source cluster: tool use, agents, scaffolds

## Yao, Shinn, Razavi, Narasimhan 2024 — τ-bench

- Paper: https://arxiv.org/abs/2406.12045
- Setup: domain APIs + policy document + LM-simulated user. Reward = exact DB state × required outputs.
- Metric **pass^k**: P(all k i.i.d. trials succeed). Distinct from pass@k (at least one of k).
- gpt-4o function-calling: **~61%** pass^1 retail, **~35%** airline; **pass^8 < 25%** retail (~60% relative drop).
- Paper Fig 3 (τ-**retail**): native FC beats ReAct and Act for SOTA models. gpt-4o FC retail pass^1 **61.2%**. GitHub later table: airline ReAct gpt-4o **0.325** is **airline**, not retail (retail ReAct listed `??`).
- Policy ablation: removing policy, gpt-4o airline **33.2 → 10.8**; retail only **61.2 → 56.8**. gpt-3.5 barely uses airline policy (**10.8 → 9.6**).
- Failure mix (36 gpt-4o retail fails): ~55% wrong argument/info (DB reasoning), ~25% wrong decision (rule following), ~19% partial compound requests.
- Cost: **95.9%** of agent $ is input tokens (long policy + tool defs).
- Temperature 0.0 agent still inconsistent (user simulator T=1.0; even T=0 is not deterministic in production APIs).
- Implication: **policy documents are skills**. Consistency ≠ single-run success. Compound responsibilities fail more. Native function calling > text-ReAct. Domain rules only help if the model can actually apply them (weaker models ignore complex policy).

**Grade:** Strong empirical. **Closest published analogue of agent skills.**

## τ² / τ³ / τ-knowledge (Sierra, 2025–2026)

- Dual-control telecom: ~20 point pass^1 drop vs autonomous.
- τ-knowledge (698 docs, ~195K tokens, 18.6 docs/task, 9.5 tool calls): GPT-5.2 high **25.5%** pass^1, **9.3%** pass^4 at launch; later GPT-5.5 xhigh **37.4% / 20.6%**. Even with gold docs, ceiling **~40%** pass^1.
- Implication: large reference corpora **do not** produce reliable skill execution. Retrieval + many tool steps + policy is still the bottleneck.

**Grade:** Strong empirical (vendor benchmark; methods public).

## Berkeley Function Calling Leaderboard (Yan / Patil et al.)

- Categories: simple / multiple / parallel / parallel-multiple; AST vs execute; irrelevance.
- GPT-4o-2024-11-20 (FC) overall **~65.8–84.4%** depending on slice; simple AST **77.2%**, multiple **93.5%**, parallel **93.0%**, parallel-multiple **86.0%**. BFCL overall CSV 2025-04-25: **Live Acc 78.85%**, **Relevance Detection 83.33%**, **Irrelevance 81.31%**. Do **not** call 78.8% “relevance” — that cell is Live Acc / live-multiple in some tables. **multi-turn** much worse (base **62.5**, miss-func **6.0** in one table).
- Small specialized models (Qwen2.5-7B-FC **82.3%** overall) can beat larger general models on single-turn FC.
- Irrelevance / abstain is a first-class failure mode (**Irrelevance 81.31%**, **Relevance Detection 83.33%** ≠ 100%).
- **miss-func 6.0%** is the multi-turn slice where the **needed** function is absent — it does **not** measure “too many tools”. Dropping the right tool from an allowlist would look like this.
- Implication: restrict a skill to `allowed-tools` that still **contain** the needed calls. Typed function calling > free JSON in a blob. Do not cite miss-func as proof that smaller catalogs always win (on this snapshot multiple **>** simple). Do not cite Live Acc **78.85%** as relevance/irrelevance.

**Grade:** Strong empirical.

## SWE-bench / SWE-agent / OpenHands

- SWE-agent (Yang et al., NeurIPS 2024): Agent-Computer Interface. GPT-4 **12.5%** full SWE-bench at launch; later Verified scores much higher with better models/scaffolds.
- Same model, different scaffold: OpenHands vs SWE-agent vs Agentless differ by **several points** (e.g. Claude 3.5 Sonnet OpenHands **53%** Verified vs Agentless **50.8%** vs Tools Claude **49%**; unique solves per scaffold).
- Historical Verified: 1.96% (2023) → ~12.5% (SWE-agent+GPT-4) → 53% (OpenHands+Sonnet 3.5) → 70–79% (2025 scaffolds+Opus 4.5).
- SWE-Bench Pro (harder): Sonnet 4.5 **43.6%** public; private set much lower (Opus 4.1 **17.8%**).
- Implication: **deterministic interface + tests** (ACI, unit tests as oracles) raise reliability more than prompt wording. Scaffold is a skill-runtime. Do not treat vendor scores as skill-authoring proof.

**Grade:** Strong empirical for scaffolding/tests; **not** a SKILL.md ablation.

## HumanEval / Codex (Chen et al. 2021)

- Codex 12B pass@1 **28.8%**, pass@100 **70.2%**.
- Implication: sampling helps **discovery** (pass@k). For skills we need **pass^k** (all k succeed). Opposite metric.

**Grade:** Strong empirical.
