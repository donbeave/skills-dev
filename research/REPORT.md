# Designing AI Skills for Maximum Predictability and Reliable Execution

**Status:** literature synthesis. **No model evals were run in this repository.** Experiments A–H are specified, not executed.

**Companion files:** [GUIDELINE.md](GUIDELINE.md) (operator process), [EVIDENCE-MATRIX.md](EVIDENCE-MATRIX.md), [EXPERIMENTS.md](EXPERIMENTS.md), [CITATIONS.md](CITATIONS.md), [SPAWN-PROMPT.md](SPAWN-PROMPT.md), [sources/](sources/).

Numbers in brackets refer to [CITATIONS.md](CITATIONS.md).

---

## How to read evidence tags

| Tag | Meaning |
| --- | --- |
| **PROVEN** | Repeated quantitative evidence, named source, reported measurement |
| **LIKELY** | Solid evidence, limited or indirect for `SKILL.md` / agent skills |
| **HYPOTHESIS** | Engineering principle that still needs skill-format evals (A–H) |

Recommendation strength: **Strong empirical** / **Moderate empirical** / **Weak-anecdotal** / **Our engineering inference**.

A result on classification ICL or math CoT is **not** automatically a result on agent skills. When we extrapolate, we say so.

---

# 1. Core research question

**What properties of an AI skill make its execution maximally predictable, reproducible, constrained, and reliable — given that the interpreter is a stochastic LM?**

A skill is a package of metadata, instructions, optional scripts/schemas/references, and (ideally) evals, discovered and loaded by an agent [38][39]. It is **not** a deterministic program. It is a **program-shaped constraint** on a probabilistic interpreter.

### 1.1 Task selection (activation)

Measured analogue: tool/function **relevance** and **multiple-function** selection on BFCL [31]; sibling-skill routing is the same classifier with natural-language `description`s. τ-bench shows agents omit compound intents and stop early [14]. IFEval++ shows single-run instruction accuracy overstates reliability [44].

**No published number** for “skill description precision/recall” in Claude/Cursor/Codex runtimes. **HYPOTHESIS:** activation is a classification problem. Mutually exclusive, keyword-rich `description`s (what + when + not-when) are the control surface [38][39]. Overlap is an activation bug.

### 1.2 Instruction interpretation

Sclar [2]: format-only changes, up to **76** accuracy points. Lu [3]: example order, **chance to SOTA**. Webson & Pavlick [6]: models often ignore instruction *meaning*. IFEval [9]: even GPT-4 missed **~23%** of prompts under *strict verifiable* instructions (76.89% prompt-level strict, secondary report).

**LIKELY:** a skill is “understood” only to the degree its requirements are **checkable** and **unambiguous**. Prose consensus in the author’s head is not a measurement.

### 1.3 Execution path

τ-bench [14]: same task, same tools, same policy, T=0 agent — **pass^8 <25%** after **~61%** pass^1 (gpt-4o retail). Traces vary enough to change DB writes. SWE-bench [16][17]: **scaffold** (allowed actions + tests) moves resolve rate by several points with the same model.

**PROVEN** that free agent loops are unstable. **LIKELY** that an explicit procedure + reduced action set (ACI, Agentless-style pipeline) stabilizes path. **HYPOTHESIS** that numbered SKILL.md steps beat descriptive prose — Experiment B.

### 1.4 Decision making

Zhao [4]: unconstrained label choice inherits majority/recency/common-token bias (**+30 pp** when calibrated). τ-bench: **~25%** of inspected gpt-4o retail failures are **wrong decision type** (wrong tool family / policy) [14]. BFCL: choosing among tools is harder than filling a single known tool [31].

**LIKELY:** every unconstrained “use an appropriate method” is a noise source. Explicit conditions, enums, tables shrink the decision surface.

### 1.5 Tool usage

τ-bench: native function calling **>** ReAct/Act; wrong **arguments** dominate failures; weaker models hallucinate IDs (gpt-3.5 **2.08** bad IDs/task vs gpt-4o **0.46**) [14]. BFCL: parallel/multiple/multi-turn and **irrelevance** lag simple calls [31].

**PROVEN** for tool agents: typed FC, fewer tools, validate args in the tool implementation (τ-bench APIs return `"Error: …"`).

### 1.6 Output structure

OpenAI [37]: schema follow **<40% → 93% → 100%** (old GPT-4 / trained GPT-4o / constrained decoding) on **their** complex-schema eval. JSONSchemaBench [22]: **100% compliance ≠ 100% coverage** — hard real schemas drop empirical coverage to **single digits–40%**. SO-Bench [46]: **>95%** valid schema, **~19%** fully correct object (best fuzzy).

**PROVEN:** syntax can approach 100% with constrained decoding **on supported schemas**. **PROVEN:** semantics do not.

### 1.7 Output quality band

Self-consistency [12]: voting **+17.9 pp** GSM8K but 40 samples. PromptBench [7]: word mutations **−33–39%** average. Quality is a **distribution**, not a point.

### 1.8 Failure behavior

τ-bench tasks are written so **one** DB outcome is legal; agents still improvise (partial exchanges, skipped confirmations) [14]. IFEval “forbidden words” / “no commas” exist because models violate them. PNAS [34]: **74.7% yes-bias**.

**LIKELY:** fail-closed must be **mechanical** (precondition script, tool error, schema reject). “If unsure, stop” in prose is weak.

### 1.9 Cross-model

IFEval GPT-4 **76.9%** vs PaLM 2 S **43.1%** [9]. τ-bench: gpt-3.5 **does not** use complex airline policy (ablation **−1.2 pp** vs gpt-4o **−22.4 pp**) [14]. Explicit skills help models that can follow them; they do **not** equalize capability. **LIKELY** with **HYPOTHESIS** on the “explicitness closes the gap” claim — Experiment G.

### 1.10 Context sensitivity

Liu [1]: mid-context **53.8%** vs first **75.8%**, mid **below** closed-book. Shi [8]: **≤18%** items remain consistent across distractor types. τ-knowledge [40]: **~195K** tokens of docs, pass^1 **25–37%**. Brittlebench [43]: surface perturbations up to **12%** and **63%** rank flips on 2026 models.

**PROVEN:** extra context is not free. Skills should load the **smallest context that fully specifies the task**.

---

# 2. Meaning of “predictability”

These terms are **not** equivalent.

| Term | Definition used here | Can it approach 100%? |
| --- | --- | --- |
| **Determinism** | Same bits every run given same weights/seed/hardware | **No** for hosted APIs (τ-bench T=0 still varies). Only for local greedy + pinned kernels, and even then batching/kernels bite. |
| **Reproducibility** | Independent lab can rerun eval and get compatible CIs | **Yes** for the *eval harness* if versions pinned. Not for a single ChatGPT click. |
| **Reliability** | P(success) over the intended distribution | Can be high on **narrow** tasks with oracles; τ-bench shows **<50–60%** on realistic tool+policy. |
| **Consistency** | Agreement across paraphrases/runs (stability) | Measurable (PSS, pass^k). Rarely 100% if any open language remains. |
| **Robustness** | Invariance to perturbations that *should not* matter | PromptBench/Brittlebench: **not** 100%. Mutation testing exists to measure the gap. |
| **Instruction adherence** | Fraction of MUST clauses satisfied | IFEval-style clauses: GPT-4 ~**77%** prompt-strict (2023); later models higher on IFEval, still drop on reliable@k [44]. |
| **Task success** | Oracle says the job is done | Distinct from adherence (can follow format and fail the job, or vice versa). |
| **Variance** | Dispersion of traces/outputs | Reducible (T=0, constraints, less freedom); not zero. |
| **Calibration** | P(correct \| confidence) | Zhao [4] shows bias; self-consistency frequency is a **rough** signal [12]. |
| **Schema adherence** | Output ∈ grammar/schema | **Yes, ~100%** on **supported** schemas with constrained decoding [37]. **No** as coverage of *all* JSON Schema [22]. |
| **Behavioral predictability** | Observer can forecast activation, path, tools, schema, fail-closed | **Engineering target** of this report — a **bundle**, not one number. |

### Skill Predictability (decomposed)

| Dimension | Near-100% realistic? | How |
| --- | --- | --- |
| **Activation consistency** | High if descriptions disjoint and evald; not 100% | Classifier evals; exclusive triggers |
| **Procedural consistency** | Medium; scaffolds help | Numbered path + fewer tools |
| **Decision consistency** | High **if** decisions are tables/enums; low if “appropriate” | Shrink Decision Surface |
| **Tool-call consistency** | High for name+required args with FC+validation; low for optional arg soup | Typed tools, server-side checks |
| **Output-schema consistency** | **Yes** on supported schemas | Constrained decoding + validator |
| **Semantic-result consistency** | **No** in general | Oracles, pass^k, ensembles optional |
| **Task-success consistency** | Domain-capped (τ-bench, SWE-bench) | Narrow the task until pass^k is acceptable |
| **Failure-mode consistency** | High if fail-closed is code | Preconditions, tool errors, stop rules |

**PROVEN** split: **syntax/schema/tool-signature** can be made nearly deterministic by **software**. **Meaning, ranking, and open generation** cannot. Skill engineering is the art of moving mass from the second set into the first.

---

# 3. Evidence requirements (applied)

Sources are listed in [CITATIONS.md](CITATIONS.md). We **do not** treat Anthropic’s skill blog [38], Cursor rules folklore, or prompt-engineering roundups as effect-size evidence. We **do** treat them as **existence proofs of architecture** and then ask whether independent measurements support those choices.

Where the literature has no SKILL.md RCT, we **design** Experiments A–H rather than fabricate deltas.

---

# 4. Prompt sensitivity and behavioral variance

**PROVEN** (strong empirical):

- **Format** (Sclar [2]): up to **76** points (LLaMA-2-13B), **~10** average; persists with scale, more shots, instruction tuning; weak cross-model correlation; GPT-3.5 median spread **6.4**, max **56**.
- **Example order** (Lu [3]): **~50% ↔ >85%**; permutation **not** transferable.
- **Label/recency/majority bias** (Zhao [4]): calibration **+30.0 pp** and **lower variance**.
- **Adversarial/word mutations** (PromptBench [7]): **33–39%** average drop (word-level).
- **2026 surface perturbations** (Brittlebench [43]): up to **~12%**; **63%** of comparisons change model **rank**; up to **half** of variance from surface form.
- **Irrelevant context** (Shi [8]): **≤18%** consistent across distractor types.

**Techniques that demonstrably reduce superficial sensitivity** (direct or strongly analogous):

| Technique | Evidence | Notes |
| --- | --- | --- |
| Constrained decoding / schema | [37][22] | Removes format freedom in the **output**. |
| Contextual calibration | [4] | Classification; +30 pp / less variance. |
| Self-consistency | [12] | Robust across prompt *sets* (+16–18 pp GSM8K); expensive. |
| Pinned format + pinned example order | [2][3] | Does not *remove* sensitivity; **stops you from resampling the sensitive axis in prod**. |
| Instruction to ignore distractors + SC | [8] | Partial mitigation on GSM-IC. |
| Verifiable rather than stylistic requirements | [9] | Reduces judge noise; not prompt noise. |
| Mutation-aware eval (FormatSpread, PromptBench, MT) | [2][7][23] | Does not fix the model; **detects** brittle skills. |

**HYPOTHESIS** (Experiment H): skills with schemas + decision tables + min context show **smaller** FormatSpread than prose-only skills. Not yet measured on SKILL.md.

**Do not claim:** “better wording” as a quantified robustness method. Sclar shows wording/format effects are **large and unpredictable** across models.

---

# 5. Skill size and decomposition

### What is measured

There is **no** published RCT of one 3k-token skill vs three 1k-token skills. Analogues:

- **Multi-instruction prompts:** IFEval prompts bundle 1–3 verifiable instructions; prompt-level accuracy **<** instruction-level (PaLM 2 S **43%** vs **56%** strict) [9]. Extra simultaneous constraints reduce *all-must-pass*.
- **Compound agent tasks:** τ-bench retail tasks with more DB writes are **harder**; **~19%** of gpt-4o fails are partial compound resolution [14].
- **Tool choice:** BFCL multiple/parallel/irrelevance < simple [31].
- **Context packing:** Liu [1], Shi [8], τ-knowledge [40].
- **Instruction conflicts:** Wallace hierarchy [20] — when instructions compete, the model needs an explicit priority story or it is jailbroken.

### Narrower skills — expected gains (LIKELY, extrapolated)

Better trigger precision, fewer conflicting rules, less token load, higher adherence on the remaining MUSTS, **far** easier eval oracles (one job ⇒ one checker), easier maintenance (one home per fact).

### When splitting is harmful (HYPOTHESIS, need Exp A)

- Pipeline steps **always** run together (create-then-validate as one user intent) — split causes **routing misses** and lost state.
- Over-split descriptions **overlap** (“audit” vs “review” vs “evaluate”) — activation entropy rises (BFCL irrelevance analogue).
- Each shard too small to state preconditions — models improvise glue.

### Rule: when to split

**Split when all of the following hold:**

1. Responsibilities can be **independently invoked** (different user intents / slash commands).
2. Combining them creates **conflicting** or **rarely co-used** rule sets.
3. You can write **separate eval oracles**.
4. You can write **mutually exclusive** `description`s (positive triggers + negative “do not use when”).

**Keep together when** the steps are a single transaction with a shared invariant (e.g. “migrate schema then rewrite callers” if neither is valid alone).

**Move out of skills entirely** when the step is deterministic (lint, schema check, file existence) — that is not a sibling skill; it is a **script**.

This rule is **LIKELY** from the analogues above, **HYPOTHESIS** as a SKILL.md law — Experiment A is the test.

---

# 6. Skill instruction architecture

Comparison of representations:

| Form | What it constrains | Evidence |
| --- | --- | --- |
| Goal only | Objective, not path | High variance (τ-bench without usable policy; Webson [6]) |
| Goal + constraints | Outcome + bans | Constraints help if **checkable** [9]; bans fail if negation-only [19][47] |
| Goal + explicit workflow | Path | Agentless-style pipelines match agents on SWE-Verified [OpenHands 53% vs Agentless 50.8%, same era] — **LIKELY** |
| State machine | Path + legal transitions | Software engines; **HYPOTHESIS** in SKILL.md; **PROVEN** useful when the machine is **code** (tools reject illegal transitions in τ-bench APIs) |
| Decision tree / table | Branch choice | Zhao [4] analogue; **HYPOTHESIS** for skills (Exp C) |
| Checklist | Completeness | IFEval multi-constraint: all-must-pass is the checklist metric [9] |
| Pseudocode / algorithm | Path + branches | Closer to ACI [16]; **HYPOTHESIS** vs prose (Exp B) |
| Examples | Format + local generalization | Lu/Min [3][5] **PROVEN** for ICL |
| I/O contract | Schema | OpenAI [37] **PROVEN** for syntax |
| Invariants | Always-true properties | Need mechanical checks or they are slogans |

**Strongest reliability stack (synthesis, not a single paper):**  
**contract + explicit procedure + decision table + examples per remaining branch + schema/script validators.**  
Prose is for motivation only; if a sentence is not needed to execute, it is noise (Anthropic “onboarding guide” framing [38] is compatible but unmeasured).

---

# 7. Decision points and Decision Surface

**Hypothesis (objective):** *Every unnecessary decision delegated to the model is a variance source.*

Support:

- Zhao [4]: unconstrained class choice is biased and high-variance; **calibration** (a post-hoc constraint) **+30 pp**.
- Lu [3]: order is a hidden decision if the skill says “pick some examples”.
- τ-bench [14]: wrong **type** of tool (~25% of analyzed fails); illegal transitions caught **only when the API encodes them**.
- BFCL [31]: extra candidate functions change error modes.
- OpenAI [37]: removing the decision “what keys to emit” → 100% schema.

**Decision Surface (proposed metric — Our engineering inference):**

```
U = number of model-controlled branches without an explicit rule
    + log2(|tool set|) if the skill does not name the tool
    + 1 if output schema is unspecified
    + 1 per subjective adjective (“good”, “appropriate”, “thorough”)
```

Not validated. Use as a **lint signal**, not a score with weights (see Part VII).

**Encoding that reduces U:** if/else tables, enums in schema, lookup tables in `assets/`, thresholds, “else stop and report Z”.

**PROVEN** that *removing output-token freedom* raises syntactic reliability [37]. **LIKELY** that *removing method-choice freedom* raises behavioral reliability. **HYPOTHESIS** until Experiment C.

---

# 8. Ambiguity

IFEval’s entire design is a reaction to ambiguous criteria (“funny tone”) being **unevaluable** [9]. PromptBench/Sclar show **surface** ambiguity (format) already swings tens of points. τ-bench authors **iterated user instructions until one DB outcome was possible** — they treat residual ambiguity as an annotation bug [14].

Vague: `Make the skill better.`  
Operational: `Reduce SKILL.md tokens by ≥30% without decreasing pass^4 on the frozen eval set.`

**Rules for requirements (LIKELY, from IFEval + SE contracts):**

- **Observable:** a trace, file, or schema field exists.
- **Measurable:** number, enum, boolean, regex, hash.
- **Falsifiable:** a counterexample is constructible.
- **Testable:** a non-LM checker, or a frozen LM judge with reported agreement (IFEval preferred over judges [9]).

Subjective adjectives in SKILL.md are **Ambiguity Score** contributors (Part VII).

---

# 9. Positive instructions vs prohibitions

**PROVEN** that models mishandle negation: Truong [19] (2023 LLMs often ≤ chance on negation NLI); 2026 open models **~50–58%** accuracy on negated queries vs **~92–96%** on positive twins [47]; VLMs **~25%** retrieval drop [49]; Negation Neglect [48] shows even training data that *says a claim is false* can install the claim unless negation is **local** to the predicate.

IFEval still includes “Forbidden Words” / “No Commas” as **verifiable** negatives [9] — they are usable **when checked**, not because the model is good at them.

**Best encoding (LIKELY):**

1. State the **required** behavior (`Do X`).
2. If Y is dangerous, add `Never Y` **and** a **deterministic check** (schema enum, script, tool allowlist).
3. Prefer “else stop Z” over “don’t improvise”.
4. Do not rely on a lone prohibition as the only barrier.

**Weak/anecdotal:** “positive prompts always beat negative” as a universal. IFEval shows some negatives are followable *and checkable*. The failure mode is **unchecked** negation.

---

# 10. Examples and few-shot

**PROVEN:**

- Order can dominate accuracy [3].
- Ground-truth labels matter **less** than format/label-space/input distribution on classification ICL [5] (**0–5%** drop with random labels).
- More shots do not kill format sensitivity [2].

**LIKELY for skills:** examples are **executable behavioral specifications** (format, tool-arg shape, fail-closed shape), not documentation. Include:

- one happy path,
- one boundary,
- one forbidden/fail-closed,
- one example **per remaining unconstrained branch**.

**Diminishing returns:** no universal k. Literature shows 4-shot already saturates some classif. tasks **and** remains order-sensitive [3]. **HYPOTHESIS:** 3–5 **diverse branch** examples beat 10 near-duplicates (Experiment D). Over-similar examples can imprint spurious tokens (Min: models copy format).

Treat example **order as frozen production data**.

---

# 11. Skill contracts (API style)

τ-bench is literally this: APIs with typed args + policy + unique legal outcome [14]. Tools that return `"Error: non-delivered order cannot be exchanged"` implement **preconditions in software**. OpenAI structured outputs implement **postconditions on syntax** [37]. Design-by-contract / BDD are old SE; IFEval is the LM-native version of testable contracts [9].

**LIKELY** that declaring Inputs / Preconditions / Outputs / Invariants / Forbidden / Failure / Postconditions improves reliability **if** each clause has a checker. A contract that is only markdown is a **goal+constraints** prompt (section 6) — better than goal-only, weaker than enforced APIs.

---

# 12. Structured outputs

See sources/04. Summary:

- **Syntactic reliability:** constrained decoding can hit **100%** on provider evals [37]; **not** 100% coverage of real JSON Schema [22] (GitHub Hard: Outlines **3%**, Guidance **41%**; OpenAI **100% compliance / incomplete coverage**).
- **Semantic reliability:** SO-Bench full-object correctness **~19%** despite **>95%** schema val [46]. Tam [21]: putting reasoning *inside* a rigid JSON order can **destroy** CoT (100% answer-before-reason on one GPT-3.5 setting). Rebuttal: that was a **bad schema**, not a law of constrained decoding. JSONSchemaBench reports **~+3%** quality under constraints on their tasks [22].
- **Retry loops:** validate-in-software can beat native structured-output **coverage** (**~50% → ~95%+**) [50].

**Where software replaces the model:** parsing, required keys, types, enums, ranges, file existence, checksums, “did the tool return error”. **Where the model stays:** mapping messy user intent onto those fields — then the schema **clips** the tail.

---

# 13. Move work out of the model

**PROVEN** pattern: OpenAI [37] states training to **93%** was **not enough**; they added deterministic decoding for **100%**. τ-bench APIs encode rules the model **failed to apply from markdown** (~25% wrong-decision; policy ablation) [14]. Huang [10]: without external feedback, self-check **hurts**. SWE-bench: **tests** are the oracle; ACI reduces how the model edits [16]. Anthropic Skills [38]: PDF form extraction **script** so neither script nor PDF need to sit in context.

**Architectural assignment:**

| Asset | Owns |
| --- | --- |
| `SKILL.md` | Routing, remaining judgment, procedure the model *must* read |
| `scripts/` | Checks, transforms, idempotent actions |
| `schemas/` | Output/tool arg shape |
| `templates/` | Exact bytes you do not want sampled |
| `tests/` / `evals/` | Oracles, pass^k, mutations |

**Strong recommendation (PROVEN adjacent, Our engineering inference for skills):** if a step’s correctness is decidable without open-world knowledge, it **must not** be an LM-only step.

---

# 14. Context engineering

**PROVEN:** U-shaped position effects [1]; distractors destroy consistency [8]; huge doc packs fail as skills [40]; newer models improve **absolute** position robustness but **relative** spacing still hurts [45].

**Is the most reliable skill the smallest context that completely specifies the task?**  
**LIKELY yes**, with two caveats: (1) omitting a **binding** rule to save tokens **hurts** (τ-bench airline policy **−22.4 pp** for gpt-4o) [14]; (2) duplicating a 20-token invariant at start **and** end is cheap insurance against LITM [1] (query-aware contextualization helped KV retrieval, not always QA).

**Reference loading rules:**

| Load | When |
| --- | --- |
| Always | `name` + `description` only [38][39] |
| On trigger | SKILL.md body **<5k tokens / <500 lines** (spec recommendation, not a measured optimum) [39] |
| Conditionally | `references/*.md` named from the **taken branch** |
| Never “just in case” | Sibling skills, unrelated chat, whole wikis |

**HYPOTHESIS:** Experiment E.

---

# 15. Instruction duplication

No LLM paper isolates “repeat the invariant twice vs once” with a clean n. Adjacent: Sclar [2] (any wording change can move scores); Liu [1] (position matters, so one copy in the middle can be the *wrong* copy); maintenance cost of two slightly different MUSTs.

**Our engineering inference:** **one authoritative statement**. Optionally a **verbatim** 1–5 line “Invariants” block at **end** (and/or start) for LITM, not a paraphrase. Never two paraphrases of the same MUST (contradiction risk + FormatSpread).

---

# 16. Skill routing and trigger design

Activation is **function relevance** (BFCL) plus **instruction hierarchy** (user text vs skill metadata). Anthropic: Claude chooses from `name`+`description` only until it reads the body [38]. Spec: description must include **what** and **when** [39].

**Rules (LIKELY):**

- Positive triggers: verbs, artifacts, slash-command, keywords.
- Negative triggers: `Do not use when …` (sibling names explicit).
- Mutual exclusion: if two descriptions both match, **that is a bug** — merge or rewrite.
- Examples of use/not-use in the description if space (1024 char cap [39]).
- Optional **router eval** (activation suite, Part VI) — not optional if you have ≥3 siblings.
- Do not depend on the model to “just know” a skill exists if it is not in the metadata list.

**HYPOTHESIS:** a dedicated classification stage (cheap model, forced enum of skill ids + `none`) beats in-the-wild triggering. Unmeasured in public skill runtimes.

---

# 17. Self-verification

| Pattern | Evidence | Use in skills? |
| --- | --- | --- |
| Generate only | Baseline | Only if oracle is downstream CI |
| Generate → model inspect → fix | Huang [10]: **−1.5 to −11.4 pp**; Tyen [11]: cannot **find** errors | **No** as the reliability layer |
| Generate → **deterministic** validate → fix | OpenAI retry culture; verifier loop **~50→95%** coverage [50]; Reflexion-with-tests [25] | **Yes** |
| Generate → **independent** judge → fix | Judges are biased [9 cites]; debate **=** majority vote [10] | Expensive; optional second model, not same-prompt self-talk |

**PROVEN:** intrinsic self-review is not a reasoning fix. **PROVEN:** external locators enable repair [11].

---

# 18. Planning

Sprague [13]: CoT **+12–14 pp** math/symbolic, **+0.7** otherwise; **95%** of MMLU CoT gain from math items. τ-bench [14]: authors **rejected** planning/self-reflection for live user agents (latency, one-shot). ToT/overthinking: extra search can add error paths and tokens.

**Policy:**

- **Forbid** open-ended plans on schema-fill / single-tool / checklist skills.
- **Allow** a short plan on multi-hop tool+policy tasks **if** eval shows pass^k ↑ enough to pay tokens.
- **Never** “always plan”.
- Prefer **scripts** over mental arithmetic (Sprague: CoT < symbolic solver).

**HYPOTHESIS:** Experiment B/G interaction with planning on/off.

---

# 19. Model capability vs skill complexity

IFEval: large gap GPT-4 vs PaLM 2 S [9]. τ-bench: **only** the strong model **uses** a complex policy [14]. BFCL: small **FC-tuned** 7B can beat larger general models on **single-turn** FC [31] — specialization helps **that** interface, not general skill following.

**Hypothesis from the brief:** *Better engineered skills let weaker models behave closer to stronger ones.*

**Qualification (LIKELY, not proven):** explicit schemas/tools **do** let small models hit **100% syntax** (constrained decoding works without GPT-4). Explicit **policies in markdown** do **not** close the gap if the model cannot apply them (gpt-3.5 airline). So: **move difficulty into schemas/scripts** to help weak models; **do not** assume a longer SKILL.md equalizes them. Experiment G.

---

# 20. Skill development as software engineering

The analogy **is useful** for contracts, tests, modules, linters, coverage. It **breaks** here:

| SE | Break |
| --- | --- |
| Types | Constrained decoding ≈ types for **tokens**, not meaning [46] |
| Unit tests | Flaky interpreter; need pass^k not pass/fail once [14][44] |
| Compiler errors | Validators are the compiler; the “program” can still be the wrong program |
| Cyclomatic complexity | Decision Surface is the cousin; not calibrated |
| Referential transparency | Context, position, and format are **hidden state** [1][2] |

Treat skills as **probabilistic programs** with a **deterministic harness**. That sentence is the analogy’s salvageable core.

---

# 21. Complexity metrics

Analogues: IFEval instruction count; cyclomatic complexity; BFCL tool cardinality; Liu context length; τ-bench write-count as difficulty [14].

Proposed **lint metrics** (not validated scores):

| Metric | Definition | Why |
| --- | --- | --- |
| Instruction count | Independent MUSTs | IFEval prompt-level < inst-level [9] |
| Decision count | Named branches | §7 |
| Unconstrained decision count U | Branches without rules | §7 |
| Branching factor | Paths | Test design |
| Context weight | Tokens before first tool | [1][8][39] |
| Responsibility count | Independently invokable jobs | §5 |
| Reference fan-out | Linked files | LITM, distractors |
| Tool-choice entropy | log2(\|tools\|) if unspecified | BFCL |
| Ambiguity score | Count of vague adjectives | §8 |
| Behavioral coverage | Eval cases / named branches | §23 |

**Our engineering inference.** Do not ship a weighted 0–100 from these without calibration (Part VII).

---

# 22. Skill development lifecycle

```
Specify contract
  → enumerate branches
  → reduce U (tables, enums, scripts)
  → implement deterministic components
  → write SKILL.md (short procedure + examples per leftover branch)
  → write evals (including activation + mutation)
  → repeated trials (design n; run in a dedicated eval env — not this repo)
  → measure pass^k / variance
  → refactor unstable branches (more code, less prose)
  → regression pin
```

**Create:** evals first [38] is consistent with TDD and with τ-bench’s “annotate unique outcome then test agents”.  
**Update:** new evals for new behavior + regression.  
**Refactor:** no intended behavior change; mutation suite is the behavioral-equivalence test.  
**Audit:** Decision Surface, overlap of descriptions, unchecked MUSTs, context weight, pass^k vs last pin.

---

# 23. Evals are critical

A single success is a **demo**. τ-bench and IFEval++ exist because **pass^1 lies**.

Measure, on frozen cases:

| Metric | Definition |
| --- | --- |
| Task success rate | successes / n |
| Structural consistency | % schema/trace match |
| Instruction adherence | % of MUSTs each passing their checker |
| Branch consistency | same branch on equivalent inputs |
| Tool consistency | expected tool+required args |
| Semantic variance | embedding or oracle-equivalent among successes |
| Failure-mode consistency | invalid inputs fail-closed, no improvise |
| Regression rate | old cases lost after edit |

Cases: identical, paraphrased, noisy context, boundary, adversarial, other models, other versions.

---

# 24. Statistical methodology

Bernoulli skill-case success, i.i.d. **if** you actually resample (paraphrase, no cache, or accept API noise).

| n | 10/10 tells you | Cannot claim |
| --- | --- | --- |
| 3 | Almost nothing | Anything about production |
| 5 | Roughly not terrible | 90%+ |
| 10 | 95% CI ~ **69–100%** (Clopper-Pearson) | **≥99%** |
| 30 | 30/30 ⇒ ~**88–100%** | 99% |
| 50 | 50/50 ⇒ ~**93–100%** | 99% |
| 100 | 100/100 ⇒ ~**96.4–100%** | 99% with margin |
| ~300 zero fails | rule of three: 3/n ≤ 1% | That’s the **start** of 99% talk |

**10/10 ≠ ≥99% reliability.** That confusion is the most expensive eval error in this field.

Report Wilson or Clopper-Pearson intervals. For pass^k, use the τ-bench U-statistic on c successes in n trials [14]. Pre-register k (4 or 8 is consistent with τ-bench).

Independence: T=0 is **not** a license to n=1. τ-bench used T=0 and still saw pass^k collapse because the **user** and **sampling** varied; hosted APIs also vary at T=0.

---

# 25. Mutation testing for skills

**PROVEN methods:** PromptBench [7], FormatSpread [2], Brittlebench [43], metamorphic prompt testing (**75%** of GPT-4 HumanEval errors, **8.6%** FP) [23], MT4NLP mean fail **18%** [24].

**Should it be standard?** **Yes (LIKELY → treat as process PROVEN in NLP, HYPOTHESIS in skill tooling).** Mutate: user wording, irrelevant prefix, order, whitespace, filenames, tool availability, edge values. Oracle = **invariants**, not string equality.

---

# 26. Behavioral specifications

IFEval [9] **is** executable spec for surface constraints. τ-bench task JSON is Given/When/Then on **DB state**. Property-based / metamorphic testing [23][24] is the robustness layer.

**LIKELY:** skills should lead with `When X, the agent MUST Y` **paired with a checker**, not with essays. BDD text without oracles is still prose.

---

# 27. Skill predictability smell catalog

| Smell | Why (evidence) | Fix |
| --- | --- | --- |
| Multiple independently invokable jobs | §5, τ-bench compounds | Split |
| Many if/otherwise in prose | Decision Surface; missed branches | Table + tests per branch |
| Numerous exceptions | Conflicts, IFEval prompt-level drop | Encode in API/script |
| Duplicated paraphrased rules | §15, Sclar | One home |
| Vague judgments | §8, IFEval motivation | Operationalize or delete |
| Excessive references always loaded | Shi, Liu, τ-knowledge | Progressive disclosure |
| Overlapping sibling descriptions | BFCL irrelevance | Exclusive triggers |
| Repeated eval fails on one branch | Coverage hole | Code that branch |
| Model-dependent behavior | §19, policy ablation | Scripts/schemas |
| MUST vs MUST NOT contradictions | Wallace conflicts | Lint |
| Output with no validator | [37] vs 93% | Schema+retry |
| “as appropriate” | Zhao | Enum/table |
| Mandatory CoT on non-symbolic | Sprague | Conditional |
| Self-review as gate | Huang | Oracle |
| Tool buffet | BFCL | allowed-tools |
| >500 lines / >5k tokens body | spec [39] + context papers | Split files |

---

# 28. Existing skill systems vs evidence

| System | Practice | Empirically supported? |
| --- | --- | --- |
| Anthropic Skills | Progressive disclosure, scripts, eval-first, description routing | Architecture **aligns** with [1][8][37][14]; **no** public pass^k on skill shape |
| agentskills.io | <500 lines, <5k tokens, one-level refs | **Heuristic** [39] |
| OpenAI Structured Outputs / FC / IH | Constrain tokens; typed tools; system>user>tool | **PROVEN** [37][14][20] |
| Cursor/Copilot/Gemini rules | Piles of markdown | Risk of **conflict + distractors**; no public RCT |
| SWE-agent ACI | Reduced edit DSL + tests | **PROVEN** scaffold effect [16] |
| OpenHands / Agentless | Rich tools vs fixed pipeline | Pipeline ≈ agent on Verified in 2025 numbers — **procedure can replace freedom** |
| MCP | Many tools | BFCL: **subset** tools per skill |
| DSPy | Compile against metrics | **LIKELY** process analogue |

**Do not adopt a vendor format as optimal.** Adopt the pieces that match measurements: disclosure, scripts, schemas, typed tools, evals.

---

# 29. Adjacent fields (techniques to steal)

- **Constrained decoding / grammars** — syntax 100% [37].
- **Design by contract / BDD** — IFEval + τ-bench oracles.
- **Property-based + metamorphic testing** — [23][24].
- **Compiler / DSL design** — ACI as a tiny language [16].
- **Workflow engines / state machines** — illegal transitions unrepresentable.
- **API design** — small surface, typed errors (τ-bench APIs).
- **Human factors** — checklists beat memory; analogue to §6 checklists.
- **Calibration / majority vote** — [4][12] for confidence, not for default control flow.

---

# 30. Failure taxonomy

| Class | Example | Fixable by rewriting SKILL.md? |
| --- | --- | --- |
| **Model limitation** | gpt-3.5 cannot apply airline policy [14]; negation [47] | Only by **removing** the need to reason (script/schema) |
| **Skill design** | “as appropriate”; overlapping jobs | **Yes** |
| **Context** | Distractor history [8]; mid-file invariant [1] | **Yes** (load less; pin position) |
| **Routing** | Wrong sibling; missed skill | **Yes** (descriptions + activation evals) |
| **Tool** | Hallucinated ID [14]; unsupported schema feature [22] | Tool-side validation; simpler schema |
| **Validation** | JSON looks fine, meaning wrong [46] | Semantic oracle, not more adjectives |

Rewriting instructions **cannot** fix a missing validator or an over-capability task. Classify first.

---

# 31. Experiments A–H

Fully specified in [EXPERIMENTS.md](EXPERIMENTS.md). **Not run here.** They exist because SKILL.md packaging, prose vs tables, and example counts **lack** direct RCTs.

---

# Part I — Executive conclusion

## If #1 priority is predictable skill execution, do this

Stop treating skills as essays. Treat them as **narrow probabilistic programs with a deterministic harness**.

Move every decidable check into **code/schema/tools**. Leave the model only the mapping from messy intent onto a **small** set of enumerated decisions. Load **almost no** extra context. Certify with **pass^k and mutations**, not a screenshot of one good run.

### Top 10 principles (ranked by expected impact)

1. **Deterministic enforcement of anything checkable** — Strong empirical [37][14][50][10]. **PROVEN** (syntax/tools/tests), **LIKELY** as the #1 skill lever.  
2. **Typed tools + tiny tool set + server-side arg checks** — Strong [14][31]. **PROVEN** for agents.  
3. **Structured final artifacts (schema/grammar), unconstrained scratchpad** — Strong [37][21][22]. **PROVEN** syntax; **LIKELY** “don’t schema the CoT”.  
4. **Shrink Decision Surface (tables, enums, else-stop)** — Moderate [4][14]. **LIKELY**; Exp C.  
5. **Minimum sufficient context + progressive disclosure** — Strong [1][8][40]; vendor design [38]. **PROVEN** harm of extra context; **LIKELY** disclosure as the fix.  
6. **One independently invokable job per skill + exclusive triggers** — Moderate analogues [9][14][31]. **LIKELY**; Exp A.  
7. **Checkable contracts (IFEval-class MUSTs)** — Strong [9][14]. **PROVEN** for eval; **LIKELY** for authoring.  
8. **pass^k + mutation + regression as the definition of done** — Strong [14][44][7][23]. **PROVEN** that pass^1 lies.  
9. **Positive path + mechanical prohibitions** — Strong negation failures [19][47]. **LIKELY** encoding rule.  
10. **Conditional (not default) planning/self-review; examples as frozen branch specs** — Strong [13][10][3][5]. **PROVEN** not-universal CoT/self-correct; **LIKELY** example policy.

---

# Part II — Evidence matrix

See [EVIDENCE-MATRIX.md](EVIDENCE-MATRIX.md) (canonical table; not duplicated here to avoid drift).

---

# Part III — Anatomy of a predictable skill

Derived from the evidence above, **not** copied from a vendor template and then justified. Each section exists because a measurement or a named inference requires it.

```text
---
name: <kebab-case, matches directory>          # [39] routing key
description: >-                                # [38][39][31] activation classifier
  <what it does>. Use when <positive triggers>.
  Do not use when <siblings / out of scope>.
---

# Purpose
<one observable outcome>                       # [9] falsifiable goal

# Do not use when
<exclusive negatives>                          # §16

# Inputs / Preconditions
<must exist; prefer a script that exits 1>     # [14] API errors; §13

# Invariants
<short list; repeated verbatim at end if long file>  # [1] position; §15

# Decision rules
| Condition | Action | Else |
| ... | ... | stop and report |                 # §7 [4][14]

# Procedure
1. Run preconditions script.
2. Select exactly one row of the table.
3. Call named tools (no others).
4. Validate output schema.
5. Stop.                                      # §6 Agentless/ACI analogues

# Tools
<allowlist only>                               # [31][39 allowed-tools]

# Output contract
<JSON Schema / file path / enum>               # [37][22]

# Validation
<commands/checkers; retry once on schema fail> # [50][10]

# Failure conditions
<missing input / no table row / tool error → stop, do not improvise>  # [14][34]

# Examples
<one per table row + one fail-closed; order frozen>  # [3][5]

# Invariants (tail copy if body is long)
<verbatim>
```

**Omitted on purpose:** “think step by step” (Sprague [13]); “review your answer” (Huang [10]); long rationale; extra references; personality.

Scripts/schemas/evals sit **beside** this file, not inside it [38][13].

---

# Part IV — Predictability checklist

Answer yes/no/NA. “Clear” is not a valid item.

- [ ] Can every conditional branch be **listed** from the skill text?
- [ ] Does every branch have an explicit **else/stop**?
- [ ] Is there **≤1** independently invokable job?
- [ ] Does `description` include **when not** to use, naming siblings?
- [ ] Could two installed skills’ descriptions both match the same user utterance? (must be no)
- [ ] Is every MUST checkable by a program or a frozen IFEval-style detector?
- [ ] Is there a JSON Schema / grammar / typed tool for the artifact?
- [ ] Does a validator run **before** the skill may claim done?
- [ ] Are file-existence / schema / grep checks in **scripts**, not only prose?
- [ ] Is tool allowlist specified?
- [ ] Are examples frozen and do they cover **each** branch + one failure?
- [ ] Is CoT/planning **absent** or **gated** on a named hard-task condition?
- [ ] Is unaided self-review **absent** as a gate?
- [ ] Are references loaded only from the taken branch, one level deep?
- [ ] SKILL.md body **<500 lines / <5k tokens** or explicitly justified?
- [ ] No second paraphrase of the same MUST?
- [ ] No unbounded adjective (“appropriate”, “better”, “thorough”) without a threshold?
- [ ] Activation eval set exists (in / out / sibling)?
- [ ] Happy / boundary / negative / mutation cases exist?
- [ ] Success defined as pass^k with **n** and **k** written down (not “it worked once”)?
- [ ] Model version pinned in the eval record?

---

# Part V — Skill linter rules

### Mechanically enforceable

- Frontmatter `name`/`description` constraints [39].
- `name` == directory.
- Description length; must contain a when-not marker if a sibling list is provided in repo index.
- Token/line count of SKILL.md; fan-out of links >1 level.
- Regex for unbounded phrases: `as appropriate`, `use your best judgment`, `if needed`, `make it better`, `be thorough`.
- MUST/MUST NOT pair extraction; contradiction via simple coreference is **limited** — flag duplicate keys.
- Output contract section missing; no `schema`/`scripts/` when body says “JSON”.
- Example count vs table row count.
- `allowed-tools` vs tools mentioned in body (set diff).
- Invariant block present twice with **non-identical** bytes.

### Model-evaluated (optional, frozen judge, report agreement)

- Sibling description overlap (semantic similarity **or** forced choice on a trigger set — prefer **the latter** as an eval, not a linter).
- Ambiguous adjectives missed by regex.
- Procedure vs examples inconsistency.
- “Would this trigger on utterance U?” — that belongs in **activation evals**, not a silent lint.

---

# Part VI — Skill Reliability Suite

```text
Skill Reliability Suite
├── activation evals      # in-scope / sibling / none; precision/recall
├── happy-path evals      # pass^1 and pass^k
├── boundary evals        # table edges, missing optional fields
├── negative evals        # must fail-closed; no improvise
├── mutation evals        # paraphrase, format, noise, filenames, tools
├── adversarial evals     # “ignore the skill”, injection in files [20]
├── tool-use evals        # expected tool, args, order, no extras
├── cross-model evals     # frontier / mid / cheap
└── regression evals      # frozen set after every edit
```

Each case: pinned skill hash, model id, decoding, n, k, checkers (prefer programs). Judges only when no checker exists; then report judge–human agreement like IFEval’s motivation [9].

---

# Part VII — Skill Predictability Score (0–100)

**Heuristic. Needs calibration. Not fitted.** Do not treat as science.

Equal start weights (10 × 10) because we **lack** a regression of production incidents on these axes. Re-fit when Experiments A–H exist.

| Dimension | 0–10 | Evidence for including it |
| --- | --- | --- |
| Trigger precision | activation eval P/R | BFCL irrelevance; §16 |
| Responsibility isolation | 10 if 1 job | §5 |
| Instruction specificity | fraction MUSTs checkable | IFEval [9] |
| Decision explicitness | 10 × (1 − U/Umax) | §7 |
| Deterministic enforcement | scripts/schema/tests present | [37][14] |
| Context efficiency | body tokens vs spec 5k | [1][8][39] |
| Behavioral coverage | branches with evals | §23 |
| Repeated-run stability | pass^4 or pass^8 | [14][44] |
| Failure handling | negative-eval pass rate | [14][34] |
| Cross-model robustness | cheap/frontier gap | [9][14] |

Score = sum. **Until calibrated, report the ten numbers, not the sum**, in any gate that matters.

---

# Part VIII — Create / update / refactor

### skill-create

1. Write the **contract and eval oracles** (unique legal outcome, like τ-bench annotation [14]).
2. List branches; **delete** branches by using software.
3. Draft `description` with exclusive when/when-not.
4. Draft body from Part III; no extra sections.
5. Add examples last, one per leftover branch.
6. Activation + happy + negative + mutation cases.
7. Only then tune wording — and freeze format [2].

### skill-update

1. New behavior ⇒ **new evals first**.
2. Run **regression** (Part VI last folder).
3. If a second independently invokable job appeared ⇒ **split** (§5 rule), do not grow the blob.
4. If a check is now mechanical ⇒ **move to script**, delete prose.

### skill-refactor

1. Declare **no intended behavior change**.
2. Mutation + regression must stay within CI of the pin.
3. If you need new evals, it is an **update**.
4. Split / merge / move-to-code / add validator / narrow trigger using the smell catalog.

---

# Closing: closest practical equivalent of deterministic skill behavior

Not philosophy. An **engineering stack**, qualified by evidence:

```text
Narrow responsibility          # LIKELY (analogues [9][14][31]; Exp A)
+ Explicit contract            # LIKELY/PROVEN eval style [9][14]
+ Low decision freedom         # LIKELY [4][14][37]; Exp C
+ Minimal context              # PROVEN harm of extra context [1][8][40]
+ Deterministic tooling        # PROVEN [37][14][16][38 scripts]
+ Structured interfaces        # PROVEN syntax [37]; not semantics [46]
+ Validation + retry           # PROVEN coverage [50]; PROVEN self-check fails [10]
+ Statistical evals (pass^k)   # PROVEN pass^1 lies [14][44]
+ Mutation + regression        # PROVEN methods [2][7][23]
```

**What this stack does *not* do:** make the LM deterministic. It **shrinks the set of bits the LM is allowed to choose** until remaining variance is (a) measured, (b) small enough for the product, or (c) pushed into a human/tool abort.

**Validated vs assumed:** syntax constraints, tool typing, external oracles, pass^k, context distractors, format sensitivity, negation failure, non-universal CoT — **validated in adjacent experiments**. SKILL.md split sizes, exact example counts, and Decision Surface as a numeric gate — **hypotheses** (A–H).

The skill-authoring product to build is therefore **not a linter of adjectives**. It is a **reliability-engineering workbench**: contracts, schemas, scripts, exclusive triggers, Decision Surface lint, and a Skill Reliability Suite that refuses to certify 10/10 as 99%.
