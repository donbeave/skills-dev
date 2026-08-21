# Source cluster: self-correction, planning, CoT, self-consistency

## Huang et al. 2023 — LLMs Cannot Self-Correct Reasoning Yet (ICLR 2024)

- Paper: https://arxiv.org/abs/2310.01798
- **Intrinsic** self-correction (no external oracle): GPT-3.5 GSM8K **77.4 → 75.9 (−1.5)**; CommonSenseQA **66.8 → 55.4 (−11.4)**. GPT-4 GSM8K **92.0 → 91.5**.
- Oracle self-correct (told if wrong) **does** help (GPT-3.5 GSM8K **75.9 → 84.3** in the oracle table).
- Multi-agent debate **= self-consistency** at matched call count (both **84.7%** GSM8K at 3 calls).
- Implication: **do not** require a skill to “review your own work” as the reliability mechanism for reasoning. Require **external** checks: schema, tests, scripts, independent judge, oracles.

**Grade:** Strong empirical.

## Tyen et al. 2024 — LLMs cannot find reasoning errors, but can correct them given the location

- Paper: https://arxiv.org/abs/2311.08516
- Mistake-finding accuracy low (GPT-4 overall **~40–53%** depending on protocol; GPT-3.5 **~10–15%**).
- Given **ground-truth error location**, correction helps downstream tasks.
- Implication: self-verify fails at **detection**, not always at repair. Deterministic locators (linters, failing tests, schema errors) unlock repair.

**Grade:** Strong empirical.

## Wang et al. 2022 — Self-Consistency (ICLR 2023)

- Paper: https://arxiv.org/abs/2203.11171
- Sample diverse CoT paths, majority-vote the answer.
- PaLM-540B GSM8K **56.5 → 74.4 (+17.9)**; GPT-3 code-davinci-002 GSM8K **60.1 → 78.0 (+17.9)**; AQuA **+12.2**, SVAMP **+11.0**.
- Robust across prompt sets (CoT 56.5/54.6/54.0 vs SC 74.4/72.1/70.4).
- 40 paths. Costly.
- Implication: **ensembling** raises success **and** can be a confidence signal (low agreement → abstain). It does **not** make a single skill run deterministic. Use for hard symbolic tasks, not as default skill procedure.

**Grade:** Strong empirical.

## Sprague et al. 2024/2025 — To CoT or not to CoT? (ICLR 2025)

- Paper: https://arxiv.org/abs/2409.12183
- Meta-analysis 100+ papers + 20 datasets × 14 models.
- Average CoT deltas: symbolic **+14.2**, math **+12.3**, logic **+6.9**, other **+0.7**.
- Up to **95%** of MMLU CoT gain from items with `=` (math slice). Direct answer ≈ CoT elsewhere.
- CoT underperforms a **symbolic solver** on execution.
- Implication: **do not mandate planning/CoT in every skill**. Require it only for symbolic/multi-hop branches. Prefer scripts/solvers for execution.

**Grade:** Strong empirical.

## Plan-and-Solve / Tree-of-Thoughts / overthinking

- Plan-and-Solve (Wang et al. 2023): helps some arithmetic vs Zero-shot-CoT; not universal.
- Tree-of-Thoughts: search helps puzzles; high token cost; can add error paths.
- Reasoning-model overthinking papers (2024–2026): extra tokens can **hurt** simple tasks; non-monotonic “potential” in traces (tangents lower P(correct)).
- τ-bench authors explicitly skipped planning/self-reflection as **unrealistic** for live user agents (latency + one-shot serving).
- Implication: planning is **conditional**. Simple, schema-constrained skills should **forbid** open-ended plans.

**Grade:** Moderate empirical (task-dependent). **HYPOTHESIS** for skill-level policy: default off except classified hard tasks.

## Reflexion (Shinn et al. 2023)

- Helps when **external** reward/trace exists (coding with tests). Not intrinsic self-correct.
- Aligns with Huang: feedback must be **grounded**.

**Grade:** Moderate empirical (coding agents).
