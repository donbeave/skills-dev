# Citations

Numbered bibliography for [`REPORT.md`](REPORT.md). Measured results live in `sources/`. Only include items used in the report.

## Peer-reviewed / arXiv with experiments

1. Liu et al. (2023). *Lost in the Middle: How Language Models Use Long Contexts.* TACL. https://arxiv.org/abs/2307.03172 — GPT-3.5 20-doc QA: 75.8% pos1 / 53.8% mid / closed-book 56.1%; >20 pt drop.
2. Sclar et al. (2024). *Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design.* ICLR. https://arxiv.org/abs/2310.11324 — LLaMA-2-13B format spread up to 76 pts; ~10 pts average; GPT-3.5 median 6.4, max 56.
3. Lu et al. (2022). *Fantastically Ordered Prompts and Where to Find Them.* ACL. https://arxiv.org/abs/2104.08786 — order: chance (~50%) to >85%; 13% relative via entropy; 88.7%→51.6% across models.
4. Zhao et al. (2021). *Calibrate Before Use.* ICML. https://arxiv.org/abs/2102.09690 — majority/recency/common-token bias; calibration up to +30.0 pp, lower variance.
5. Min et al. (2022). *Rethinking the Role of Demonstrations.* EMNLP. https://arxiv.org/abs/2202.12837 — random labels typically 0–5% drop; format/label-space/input distribution dominate.
6. Webson & Pavlick (2022). *Do Prompt-Based Models Really Understand the Meaning of Their Prompts?* NAACL.
7. Zhu et al. (2023/24). *PromptBench / PromptRobust.* https://arxiv.org/abs/2306.04528 — word-level PDR ~33–39%; character ~20%; sentence ~12%.
8. Shi et al. (2023). *Large Language Models Can Be Easily Distracted by Irrelevant Context.* ICML. https://arxiv.org/abs/2302.00093 — ≤18% consistently solved across all distractor types; macro <30%.
9. Zhou et al. (2023). *IFEval.* https://arxiv.org/abs/2311.07911 — 541 prompts, 25 verifiable types; PaLM 2 S 43.07% prompt-strict; GPT-4 ~76.89% prompt-strict (secondary report of same paper).
10. Huang et al. (2023/24). *Large Language Models Cannot Self-Correct Reasoning Yet.* https://arxiv.org/abs/2310.01798 — GPT-3.5 GSM8K 77.4→75.9; CSQA 66.8→55.4; debate = self-consistency.
11. Tyen et al. (2024). *LLMs cannot find reasoning errors, but can correct them given the error location.* https://arxiv.org/abs/2311.08516
12. Wang et al. (2023). *Self-Consistency Improves Chain of Thought Reasoning.* ICLR. https://arxiv.org/abs/2203.11171 — GSM8K +17.9 pp (PaLM-540B 56.5→74.4).
13. Sprague et al. (2024/25). *To CoT or not to CoT?* ICLR 2025. https://arxiv.org/abs/2409.12183 — CoT +14.2 symbolic / +12.3 math / +6.9 logic / +0.7 other; 95% of MMLU CoT gain from math.
14. Yao, Shinn, Razavi, Narasimhan (2024). *τ-bench.* https://arxiv.org/abs/2406.12045 — gpt-4o ~61% retail / ~35% airline; pass^8 <25% retail; FC > ReAct.
15. Yao et al. (2022/23). *ReAct.* https://arxiv.org/abs/2210.03629
16. Yang et al. (2024). *SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering.* NeurIPS. Launch GPT-4 12.5% SWE-bench.
17. Jimenez et al. (2023/24). *SWE-bench.* https://arxiv.org/abs/2310.06770
18. Chen et al. (2021). *Evaluating Large Language Models Trained on Code.* https://arxiv.org/abs/2107.03374 — Codex pass@1 28.8%, pass@100 70.2%.
19. Truong et al. (2023). *Language models are not naysayers.* *SEM. https://arxiv.org/abs/2306.08189
20. Wallace et al. (2024). *The Instruction Hierarchy.* https://arxiv.org/abs/2404.13208 — up to +63% system-prompt-extraction robustness; +30% jailbreak on held-out.
21. Tam et al. (2024). *Let Me Speak Freely?* EMNLP Industry. https://arxiv.org/abs/2408.02442
22. Geng / JSONSchemaBench authors (2025). *JSONSchemaBench.* https://arxiv.org/abs/2501.10868 — 10K schemas; OpenAI 100% compliance on accepted schemas, low coverage on hard GitHub schemas.
23. Wang & Zhu (2024). *Validating LLM-Generated Programs with Metamorphic Prompt Testing.* https://arxiv.org/abs/2406.06864 — 75% of GPT-4 HumanEval errors detected, 8.6% FP.
24. MT4NLP / LLMORPH (2025). Metamorphic testing survey+impl — mean λ=18%, up to 80% per MR; GPT-4 λ=0.14.
25. Shinn et al. (2023). *Reflexion.*
26. Wei et al. (2022). *Chain-of-Thought Prompting.*
27. Kassner & Schütze (2020). Negated LAMA.
28. Park et al. (2023). *Generative Agents.*
29. Liu et al. (2023). *AgentBench.* https://arxiv.org/abs/2308.03688
30. Schick et al. (2023). *Toolformer.*
31. Yan et al. (2024). Berkeley Function Calling Leaderboard. https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html
32. Huang et al. (2023). *MetaTool.*
33. Errica et al. (2024). *What Did I Do Wrong?* https://arxiv.org/abs/2406.12334
34. Dentella et al. (2023). PNAS systematic LM testing — mean acc 0.572, 74.7% yes-bias.
35. Wang et al. (2023). *Plan-and-Solve Prompting.*
36. Yao et al. (2023). *Tree of Thoughts.*

## Lab / provider empirical docs

37. OpenAI (2024). *Introducing Structured Outputs in the API.* gpt-4-0613 <40%; gpt-4o-2024-08-06 93% trained / 100% constrained. https://openai.com/index/introducing-structured-outputs-in-the-api/
38. Anthropic (2025). *Equipping agents for the real world with Agent Skills.* https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
39. Agent Skills specification. https://agentskills.io/specification — metadata ~100 tokens; body <5k tokens recommended; SKILL.md <500 lines.
40. Sierra (2024–2026). τ-bench blog + τ-knowledge. GPT-4o pass^8 ~25% retail; τ-knowledge pass^1 25.5%→37.4%.
41. OpenAI (2024). Instruction Hierarchy announcement. https://openai.com/index/the-instruction-hierarchy/
42. OpenAI (2026). *Improving instruction hierarchy in frontier LLMs.* GPT-5-Mini 84.1→94.1% IH.

## Later empirical papers used for caveats

43. Brittlebench (2026). https://arxiv.org/html/2603.13285 — ≤12% drop; ranking flip 63%; up to 50% of variance from surface form.
44. IFEval++ (2025). https://arxiv.org/html/2512.14754 — GPT-5 IFEval 95.9%; reliable@10 −18.3%; GPT-3.5 −54.7%.
45. Long-context position follow-up (2024). arXiv:2410.14641 — absolute LITM reduced on new models; relative spacing still hurts.
46. SO-Bench (2025). Schema val >95%; full correct structure ~19% best fuzzy.
47. How Language Models Process Negation (2026). Llama-3.1 50.5% neg vs 95.2% pos accuracy.
48. Negation Neglect (2026). Belief 2.5%→88.6% when finetuned on negated-false documents.
49. MIT VLM negation (2025). ~25% retrieval drop; ~39% MCQ.
50. Verifier-loop structured output (2025). Coverage ~50% structured-output vs ~94–99% validate/retry on 9,558 schemas.

## Statistics (methods)

51. Clopper-Pearson / Wilson binomial intervals; “rule of three” (n failures=0 ⇒ ~3/n upper 95% on p_fail).
52. Pezeshkpour & Hruschka (2024). *Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions.* NAACL Findings. https://arxiv.org/abs/2308.11483 — oracle reorder gap **~13–75%**; GPT-4 still ~13% at >90% acc; few-shot does not close.
53. Zheng et al. (2023). *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.* NeurIPS. https://arxiv.org/abs/2306.05685 — swap consistency Claude-v1 **23.8%**, GPT-3.5 **46.2%**, GPT-4 **65.0%** (30% first-bias).
54. Mu et al. (2025). *A Closer Look at System Prompt Robustness.* https://arxiv.org/abs/2502.12197 — pass→0 as system guardrails 1→20; GPT Store prompts avg **5.1** guardrails; S-IFEval channel transfer is incomplete.
55. Wang et al. (2023). *Large Language Models are not Fair Evaluators.* https://arxiv.org/abs/2305.17926 — order of candidate answers biases LLM judges (adjacent to [53]).
56. Li et al. (2024). *Measuring and Controlling Instruction (In)Stability in Language Model Dialogs.* Persona/instruction drift over turns.
