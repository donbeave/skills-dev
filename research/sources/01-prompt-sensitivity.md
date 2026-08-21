# Source cluster: prompt sensitivity and few-shot variance

## Sclar et al. 2024 — Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design (ICLR 2024)

- Paper: https://arxiv.org/abs/2310.11324
- Models: LLaMA-2 family, GPT-3.5, others; 50+ tasks
- Finding: meaning-preserving format changes (separators, casing, spacing, wrappers) change accuracy by **up to 76 points** on LLaMA-2-13B; **~10 points average** across 50+ tasks.
- Sensitivity remains after scaling, more few-shot examples, and instruction tuning.
- Format performance **weakly correlates across models** — a “good prompt” for one model is not a good prompt for another.
- GPT-3.5 FormatSpread: **up to 56 points**, **median spread 6.4 points**, 320 formats × 53 tasks.
- Implication for skills: treat format as a reliability variable; report ranges; freeze format in production; do not assume transfer.

**Grade:** Strong empirical. **Applicability to skills:** direct for instruction text; extrapolated for SKILL.md body layout.

## Lu et al. 2022 — Fantastically Ordered Prompts (ACL 2022)

- Paper: https://arxiv.org/abs/2104.08786
- Finding: 4-shot example **order** can move SST-2 from **~50% (chance)** to **>85%** (near supervised).
- Present across model sizes including GPT-3 175B; not explained by a specific subset of samples.
- A permutation that scores **88.7%** on GPT2-XL can score **51.6%** on GPT2-Large — **orders do not transfer**.
- Entropy probing (GlobalE) yields **13% relative** improvement without a labeled dev set.
- Implication: examples in skills are **executable specifications of format and order**, not just documentation. Pin order. Test permutations.

**Grade:** Strong empirical.

## Zhao et al. 2021 — Calibrate Before Use (ICML 2021)

- Paper: https://arxiv.org/abs/2102.09690
- Finding: GPT-3 few-shot accuracy has **high variance across prompts**.
- Three biases: **majority-label**, **recency** (last example), **common-token**.
- Contextual calibration: **up to +30.0 percentage points** absolute; also **reduces variance**.
- Implication: unconstrained classification decisions in skills inherit these biases. Prefer explicit decision tables / schemas over “pick an appropriate label”.

**Grade:** Strong empirical (classification/ICL). **Skill extrapolation:** moderate.

## Min et al. 2022 — Rethinking the Role of Demonstrations (EMNLP 2022)

- Paper: https://arxiv.org/abs/2202.12837
- 12 models including GPT-3.
- Finding: **randomly replacing labels barely hurts** (typically **0–5%**) on classification/MCQ.
- What matters: **label space**, **input distribution**, **format**.
- Implication: examples teach **structure more than ground-truth mapping**. For skills, examples should cover **format, branches, and failure shapes**, not only “happy path answers”. Ground-truth labels still matter for generation/tool-call tasks (this paper’s result is classification-specific).

**Grade:** Strong empirical for ICL classification. Do not over-generalize to agent tool-calling.

## Zhu et al. 2023/2024 — PromptBench / PromptRobust

- Paper: https://arxiv.org/abs/2306.04528
- Word-level attacks: **~33–39% average performance drop**.
- Character-level: **~20%**. Semantic-level similar to character. Sentence-level weaker (**~12%**).
- Implication: skill evals that only use clean prompts overestimate reliability. Mutation/paraphrase evals are mandatory.

**Grade:** Strong empirical.

## Brittlebench (2026) — Quantifying LLM Robustness via Prompt Sensitivity

- Paper: https://arxiv.org/html/2603.13285
- Semantics-preserving perturbations: **up to ~12%** degradation on frontier models.
- A **single perturbation changes model ranking in 63%** of cases.
- Perturbations can account for **up to half** of a model’s performance variance.
- Implication: even 2026 frontier models are not format-invariant. Rankings from one prompt wording are unstable.

**Grade:** Strong empirical (newer models).

## Errica et al. 2024 — What Did I Do Wrong? Sensitivity and Consistency

- Paper: https://arxiv.org/abs/2406.12334
- Defines **sensitivity** (prediction change under rephrasing, no labels needed) vs **consistency** (within-class stability).
- Useful metric design for skill evals: measure both, not only accuracy.

**Grade:** Moderate empirical (classification).

## Prompt Stability Score (2024)

- Paper: https://arxiv.org/html/2407.02039
- Intra-prompt (repeated runs) and inter-prompt (paraphrases) agreement as reliability coefficients.
- Treats stability as **necessary but not sufficient** for accuracy.

**Grade:** Moderate empirical.

## Webson & Pavlick 2022 — Do Prompt-Based Models Really Understand Their Prompts?

- Finding: models often ignore instruction semantics and exploit surface cues.
- Implication: “clear prose” in SKILL.md is not evidence the model interpreted the objective.

**Grade:** Strong empirical (older models); still directionally relevant.
