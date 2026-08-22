# Evidence matrix

No numeric “measured effect” without a source. Skill applicability is often **extrapolated** from prompt/agent papers; that is marked.

| Technique | Evidence | Measured effect | Confidence | Recommendation |
| --- | --- | --- | --- | --- |
| Constrained decoding / JSON Schema (`strict`) | OpenAI Structured Outputs 2024 [37] | Internal complex-schema eval: gpt-4-0613 **<40%**; gpt-4o-2024-08-06 **93%** trained, **100%** with constrained decoding | High for **syntax** on supported schemas | **Do.** Constrain final artifacts. Never equate 100% schema with 100% semantics. |
| JSON Schema coverage on real schemas | JSONSchemaBench [22] | GlaiveAI: Guidance emp. **96%** / OpenAI **89%** emp. **100%** compliance; GitHub Hard: Guidance **41%**, Outlines **3%** | High | Keep schemas in the engine’s supported subset; always validate in software; retry. |
| Generate → validate → retry | Verifier-loop paper [50] | gpt-5-nano structured-output coverage **~50%** vs validate/retry **~94–99%** (9,558 schemas, +1–4s) | High | Default postcondition loop for structured skill outputs. |
| Native function calling vs ReAct text | τ-bench [14] | FC beats ReAct/Act; gpt-4o FC retail **~61%** vs ReAct **32.5%** (paper/GitHub tables) | High for tool agents | Skills that use tools should use **typed FC**, not “emit a JSON action blob”. |
| Restrict tool set / lower choice entropy | BFCL [31]; τ-bench wrong-arg fails | Multi-turn/miss-func **6.0%** vs simple AST **77.2%** (GPT-4o FC one table); irrelevance is a first-class fail | High | `allowed-tools`; one job → few tools. |
| Policy / skill document in context | τ-bench policy ablation [14] | gpt-4o airline **33.2→10.8** without policy; retail **61.2→56.8**; gpt-3.5 airline **10.8→9.6** | High | Put **binding rules** in the skill. Weaker models may ignore complex policy — compensate with code. |
| Repeated-trial reliability (pass^k) | τ-bench [14]; IFEval++ [44] | gpt-4o retail pass^8 **<25%** vs pass^1 **~61%**; IFEval→reliable@10 **−18.3%** (GPT-5) to **−61.8%** (Qwen3-0.6B) | High | Never certify a skill on one run. Use pass^k. |
| Format pinning | Sclar FormatSpread [2]; Brittlebench [43] | Up to **76** pts (LLaMA-2-13B); ~**10** avg; GPT-3.5 median **6.4** max **56**; 2026 ranking flip **63%** | High | Freeze markdown/structure; mutation-test wording. |
| Example order pinning | Lu 2022 [3] | Same 4-shot: ~**50%** to **>85%**; orders **not** transferable (88.7→51.6) | High for ICL | Pin example order; cover branches; do not shuffle in prod. |
| Example content (labels vs format) | Min 2022 [5] | Random labels typically **0–5%** drop on classif./MCQ | High for ICL classif.; low for tool args | Treat examples as **format+branch specs**. Still use correct tool-arg examples. |
| Calibration / label bias | Zhao 2021 [4] | Up to **+30.0 pp**; reduces variance; majority/recency/common-token | High for classif. | Replace “pick a label” with enums/tables. |
| Short / well-placed context | Liu 2023 [1] | Mid-context **53.8%** vs first **75.8%**; mid **<** closed-book **56.1%** | High | Constraints at start **and** end; no unused files. |
| Strip irrelevant context | Shi 2023 [8] | ≤**18%** of solvable items stay consistent across all distractors; macro **<30%** | High (math) | Minimum sufficient context. Progressive disclosure. |
| Long reference packs | τ-knowledge [40] | 698 docs / ~195K tok: pass^1 **25.5–37.4%**, pass^4 **9.3–20.6%**; gold-docs ceiling **~40%** | High | Do not dump wikis into skills. |
| Progressive disclosure architecture | Anthropic Skills [38]; spec [39] | No public A/B. Aligns with [1][8][40] | Medium (design) | Metadata always; body on trigger; files/scripts on demand. Spec: body **<5k tokens**, **<500 lines**. |
| Verifiable instructions | IFEval [9] | GPT-4 ~**76.9%** prompt-strict vs PaLM 2 S **43.1%**; 25 checkable types | High | Write requirements a program can check. |
| Instruction hierarchy | Wallace 2024 [20] | Up to **+63%** extraction robustness; **+30%** held-out jailbreak | High for conflicts | Put invariants in the highest-privilege channel; don’t expect SKILL.md to beat a jailbreak user. |
| Intrinsic self-review | Huang 2023 [10]; Tyen 2024 [11] | GSM8K **77.4→75.9**; CSQA **66.8→55.4**; mistake-find GPT-4 ~**40–53%** | High | Ban unaided self-critique as the reliability mechanism. Use external oracles. |
| Self-consistency ensemble | Wang 2023 [12] | GSM8K **+17.9 pp** (40 paths) | High for math; costly | Optional on hard symbolic branches; not default skill control flow. |
| Mandatory CoT/planning | Sprague 2025 [13]; τ-bench methods [14] | CoT **+0.7** on non-math; **+12–14** math/symbolic; τ-bench skipped planning for live agents | High that CoT is **not** universal | Conditional CoT; forbid open plans on simple schema tasks. |
| Constraining *reasoning* to JSON | Tam 2024 [21] | JSON-mode forced answer-before-reason on 100% of one task (GPT-3.5 last-letter) | Medium (confounded; rebuttal exists) | Constrain the **artifact**, not the scratchpad. |
| Semantic ≠ syntactic JSON | SO-Bench [46] | Schema val **>95%**; full correct structure **~19%** best fuzzy | Medium | Validators + evals for meaning, not only parse. |
| Negation-only constraints | Truong 2023 [19]; 2026 negation processing [47] | Llama-3.1 **50.5%** neg vs **95.2%** pos; NLI often ≤ chance (2023) | High for the failure | Positive path + code prohibition. Pair every NEVER with DO + check. |
| Scaffold / ACI vs free agent | SWE-agent [16]; OpenHands vs Agentless | Same-model scaffold gaps **~3–10+ pp**; Agentless **50.8%** vs OpenHands **53%** Verified (Sonnet 3.5 era) | High for coding agents | Reduce action space; tests as oracles. |
| Word-level robustness eval | PromptBench [7] | **33–39%** avg drop | High | Mutation evals in the skill suite. |
| Metamorphic prompt testing | Wang & Zhu 2024 [23]; MT4NLP [24] | **75%** of GPT-4 HumanEval errors caught (8.6% FP); mean MR fail **18%** | High as a method | Standardize invariant-preserving paraphrases. |
| Split vs monolith skills | No direct SKILL.md RCT | Analogues: compound τ-bench writes harder; IFEval multi-instruction; BFCL multiple; context dilution [1][8] | Medium (extrapolation) | Split when independently invokable + conflicting rules + separate evals. See REPORT §5. **Experiment A** required. |
| Decision tables vs “appropriate” | No direct skill RCT | Analogues: Zhao biases [4]; τ-bench 25% wrong-decision; FC enums | Medium | Default to explicit conditions. **Experiment C**. |
| Duplicate critical rules | No quantitative LLM duplication study | Adjacent: Sclar sensitivity; maintenance cost; contradiction risk | Low | One home per fact (skill-design principle). Repeat only a **short invariant block** at end if LITM is a risk. |
| Weaker models + more explicit skills | τ-bench policy ablation [14]; IFEval gap [9] | gpt-3.5 barely uses airline policy (−1.2 pp); IFEval GPT-4 **76.9** vs PaLM 2 S **43.1** | Medium | Explicit skills **help** models that can follow them; they do **not** magically equalize capability. Test cheap models. |
| Freeze option/method order or use enums | Pezeshkpour [52]; Zheng [53] | MCQ oracle-reorder gap **13–75%**; judge swap consistency Claude **23.8%**, GPT-4 **65%** | High for choice tasks | Do not leave “pick an option” unconstrained. Schema enums; freeze listed order. |
| Cap simultaneous markdown guardrails | Mu RealGuardrails [54] | Pass → **~0** as system guardrails go **1→20**; GPT Store avg **5.1** rules | High for system prompts | Split or move rules to code. Do not grow SKILL.md as a rule pile. |
| System vs user channel | Wallace [20]; Mu [54] | +63% extraction robustness from hierarchy training; S-IFEval user→system transfer incomplete | High for privilege; not 100% | Highest-privilege channel **plus** checker. Channel ≠ enforcement. |

Weights in Part VII of the report are **heuristics requiring calibration**, not fitted coefficients.
