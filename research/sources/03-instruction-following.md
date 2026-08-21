# Source cluster: instruction following, hierarchy, negation

## Zhou et al. 2023 — IFEval

- Paper: https://arxiv.org/abs/2311.07911
- 25 verifiable instruction types, **541 prompts**, objective checkers (word count, JSON wrapper, all-caps, keyword frequency, etc.).
- PaLM 2 Small: prompt-level strict **43.07%**, inst-level strict **55.76%**, prompt-level loose **46.95%**, inst-level loose **59.11%**.
- Secondary reports of the same paper: GPT-4 (Nov 2023) prompt-level strict **76.89%**, inst-level strict **83.57%**; loose **79.30% / 85.37%**.
- Key design lesson: **verifiable** instructions beat subjective rubrics for reproducible eval.
- Implication: skill requirements must be **observable and checkable**. “Be thorough” is not an IFEval-class instruction.

**Grade:** Strong empirical.

## IFEval++ / Revisiting Reliability (2025, arXiv 2512.14754)

- GPT-5 IFEval accuracy **95.9%**.
- Drop from IFEval accuracy to **reliable@10** on IFEval++: **−18.3%** (GPT-5), **−54.7%** (GPT-3.5-turbo-1106), **−61.8%** (Qwen3-0.6B).
- Implication: single-run IF scores **massively overstate** reliability. `pass^k` / `reliable@k` is the right family of metrics for skills.

**Grade:** Strong empirical.

## Wallace et al. 2024 — The Instruction Hierarchy (OpenAI)

- Paper: https://arxiv.org/abs/2404.13208
- Privilege: system > user > tool/third-party.
- Applied to GPT-3.5: **up to +63%** robustness vs system-prompt extraction; **>+30%** jailbreak robustness on held-out attacks.
- Some over-refusal regressions.
- 2026 follow-up (IH-Challenge): GPT-5-Mini 84.1% → 94.1% IH robustness with RL; unsafe 6.6% → 0.7%.
- Implication for skills: skill rules compete with user/tool text. Put **non-overridable invariants** in the highest-privilege channel the runtime allows. Do not rely on SKILL.md prose to win against a conflicting user request unless the runtime enforces hierarchy.

**Grade:** Strong empirical (security/IF conflict). Skill mapping: LIKELY.

## Truong et al. 2023 — Language models are not naysayers (*SEM 2023)

- Paper: https://arxiv.org/abs/2306.08189
- LLMs: insensitivity to negation, weak lexical negation, **worse-than-random** on several negation NLI sets; scale did not clearly help in this study.

**Grade:** Strong empirical (2023 models).

## Later negation work

- 2025 Findings EMNLP: scaling **can** help; language-dependent; longer/explicit premises more robust.
- 2026 “How Language Models Process Negation”: output negation accuracy **~45–58%** vs positive **~92–96%** (Llama-3.1 **50.5% neg / 95.2% pos**; Qwen2.5 **57.6 / 93.5**). Logits **are** sensitive; later layers overwrite.
- MIT 2025 VLMs: negated captions drop retrieval **~25%**; best MCQ **~39%**.
- 2026 Negation Neglect: finetuning on “this claim is false” documents still installs the claim (belief **2.5% → 88.6%**); **local** negation (“X did not win”) is learned.
- Implication: **do not encode critical constraints as lone “Never do Y”**. Prefer **positive procedure + deterministic validator**. If a prohibition is needed, pair it with the **required alternative** and put the check in code.

**Grade:** Strong empirical for the failure; moderate for the encoding remedy.

## PNAS 2023 — Systematic testing of three LMs (grammar judgments)

- Mean accuracy **0.572**; **yes-response bias 74.7%** of answers; ungrammatical condition **below chance**.
- Repeated items 10×: **instability**.
- Implication: default-yes / default-comply is a real bias. Skills that ask “is this OK?” without a forced fail-closed option will over-accept.

**Grade:** Strong empirical (narrow task).
