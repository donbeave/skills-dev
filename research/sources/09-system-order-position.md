# Source cluster: system vs user, option order, judge position

## Pezeshkpour & Hruschka 2024 — MCQ option order (NAACL Findings)

- Paper: https://arxiv.org/abs/2308.11483
- GPT-4 and InstructGPT (`text-davinci-003`); CSQA, MMLU slices, Big-Bench logical deduction.
- Sensitivity gap = max−min accuracy under **oracle** option reorder.
- Zero-shot gap **~13–75%** depending on set/model. GPT-4 still **~13%** gap on tasks with **>90%** accuracy.
- Few-shot (1/2/5) **does not** close the gap; error bars stay wide.
- Mechanism: uncertainty among top-2/3 + positional bias. >**94%** of sensitive items: model says more than one choice is highly probable.
- Majority vote over 10 random reorders: up to **+8 pp**.
- Skill implication: any skill that says “pick an appropriate option/method” inherits this axis. **Enums in schema** or **frozen option order** + **don't shuffle in prod**. Decision tables beat free choice.

**Grade:** Strong empirical (MCQ). Extra. to skill method-choice.

## Zheng et al. 2023 — MT-Bench LLM-as-judge position bias (NeurIPS)

- Paper: https://arxiv.org/abs/2306.05685
- Table 2 swap consistency: Claude-v1 **23.8%** (75% first), GPT-3.5 **46.2%** (50% first), GPT-4 **65.0%** (30% first, 5% second). GPT-4 few-shot **77.5%**.
- GPT-4 ↔ human agreement **>80%** on MT-Bench — still not a substitute for **program checkers** on skill MUSTs.
- Mitigation they measured: judge twice with swapped order; only count wins that survive both.
- Skill implication: **do not** use an LM judge as the only oracle for skill evals when a checker exists (IFEval design [9]). If you must judge, swap-and-agree.

**Grade:** Strong empirical.

## Mu et al. 2025 — System prompt robustness / RealGuardrails

- Paper: https://arxiv.org/abs/2502.12197
- Monkey Island: add 1–20 if-then guardrails to a real GPT Store system prompt. **All** tested API models (GPT-4o, 4o-mini, DeepSeek V3, o3-mini, R1) → pass rate **near 0** at 20 guardrails. Not adversarial; no tools; no long context.
- GPT Store vs HuggingChat: **5.1** mean guardrails across **both** prompt collections used in the paper (Fig 3: Store denser than HuggingChat).
- S-IFEval: moving IFEval constraints from **user** into **system** is **not** the same skill — transfer is incomplete; benefits from targeted training.
- DPO on realistic system-adherence data helps more than stacking more markdown rules.
- Double-check (feed response back to same model) **mixed**.
- Skill implication: **do not** grow SKILL.md as a pile of guardrails. Split, or enforce in code. System channel is **necessary** for privilege, **not sufficient** for 20 simultaneous MUSTs.

**Grade:** Strong empirical for system-prompt following. Extra. to SKILL.md body length, but **direct** for “how many rules can one prompt hold”.
