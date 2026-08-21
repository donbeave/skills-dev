# Spawn prompt: skill predictability research

Copy everything below the line into a research agent. Do **not** run model evals in the research workspace unless the operator explicitly opts in. Design experiments; do not execute them.

---

You are conducting evidence-driven research on **how to design, author, structure, test, evaluate, and maintain AI/agent skills** so that repeated executions of a **non-deterministic language model** converge on intended behavior.

## Hard constraints

- Do **not** try to make LLMs deterministic. Accept stochastic inference (including T=0 API variance).
- Do **not** run live model evals, agent rollouts, or 30–100 trial loops in this workspace.
- Base recommendations on **measured evidence**: controlled experiments, benchmarks, ablations, repeated-run / variance / success-rate studies. Prefer peer-reviewed, then arXiv-with-experiments, then lab/provider empirical docs.
- Do **not** rest major recommendations on blog lore, X posts, or generic prompt-engineering lists.
- Tag every major recommendation: **Strong empirical / Moderate empirical / Weak-anecdotal / Our engineering inference**, and **PROVEN / LIKELY / HYPOTHESIS**.
- Include numbers (effect size, models, tasks, n) when published. Never invent measured effects.
- Write all notes and the report as markdown in the repo. Commit with DCO (`git commit -s`).

## Core question

How do we engineer a skill and the skill-development **process** so that repeated executions:

1. activate the right skill (and not the wrong one),
2. interpret the objective the same way,
3. follow a stable procedure,
4. make constrained rather than arbitrary decisions,
5. call tools with predictable names/args/order,
6. emit the required artifact/schema,
7. stay in an acceptable quality band,
8. fail in known ways instead of improvising,
9. degrade gracefully on weaker models,
10. resist unrelated conversation/context.

## Required definitional work

Do not treat these as synonyms: determinism, reproducibility, reliability, consistency, robustness, instruction adherence, task success, variance, calibration, schema adherence, behavioral predictability.

Decompose **Skill Predictability** into: activation, procedural, decision, tool-call, output-schema, semantic-result, task-success, failure-mode consistency. State which dimensions can approach 100% and which cannot.

## Literature you must actually open

Search and extract numbers from (non-exhaustive): Lost in the Middle (Liu); FormatSpread (Sclar); Fantastically Ordered Prompts (Lu); Calibrate Before Use (Zhao); Rethinking Demonstrations (Min); PromptBench; Brittlebench; GSM-IC (Shi); IFEval / IFEval++; Instruction Hierarchy (Wallace); negation (Truong, later 2025–26); Structured Outputs (OpenAI 100%/93%/40%); JSONSchemaBench; Let Me Speak Freely (Tam) + rebuttal; τ-bench pass^k; BFCL; SWE-bench/SWE-agent/OpenHands; Self-Consistency; Cannot Self-Correct (Huang); To CoT or not to CoT (Sprague); metamorphic prompt testing; Anthropic Agent Skills + agentskills.io (as **design**, not proof).

Also search adjacent fields: constrained decoding, metamorphic testing, API/DSL/compiler design, property-based testing, workflow engines.

## Topics that must appear (do not skip)

Prompt sensitivity; monolithic vs narrow skills; instruction architecture (goal / workflow / state machine / decision tree / checklist / contract); decision surface; ambiguity; positive vs prohibitions; examples as specs; API-like contracts; structured outputs vs semantic correctness; move work to deterministic code; context engineering / progressive disclosure; duplication; routing/triggers; self-verification; planning (not assumed helpful); model strength × skill explicitness; SE analogy and where it breaks; complexity metrics; lifecycle; eval methodology; statistics of n=3/5/10/30/50/100 (10/10 ≠ ≥99%); mutation testing; BDD/contracts; smell catalog; vendor systems compared to evidence; failure taxonomy (model vs skill vs context vs routing vs tool vs validation).

## Experiments

Where evidence is insufficient, **design** (do not run) experiments A–H: monolith vs split; prose vs algorithm; ambiguous vs decision table; 0/1/3/5/10 examples; context noise; 30–100 repeats; model strength; mutations. Each needs IV, DVs, controls, n, metrics, stats, interpretation.

## Deliverable shape

Markdown report with:

- **Part I** — 10 principles ranked by expected impact, with evidence tags
- **Part II** — evidence matrix (Technique | Evidence | Measured Effect | Confidence | Recommendation); no unsourced numbers
- **Part III** — skill template **derived from evidence**, each section justified
- **Part IV** — objectively answerable checklist
- **Part V** — linter rules: mechanical vs model-evaluated
- **Part VI** — Skill Reliability Suite (activation, happy, boundary, negative, mutation, adversarial, tool-use, cross-model, regression)
- **Part VII** — 0–100 score with heuristic weights marked as needing calibration
- **Part VIII** — skill-create / skill-update / skill-refactor workflows

Final architecture answer (not philosophy): what **surrounding system** (narrow responsibility, contract, low decision freedom, minimal context, deterministic tools, structured I/O, validation, statistical evals, regression) gives the closest practical equivalent of deterministic skill behavior — treated as a hypothesis qualified by evidence.

Store paper notes with extracted numbers in `research/sources/`. Keep a citation list.

## Quality bar for each important claim

1. What evidence? 2. Measured? 3. Models? 4. Tasks? 5. Effect size? 6. Trials? 7. Reproduced? 8. Directly about skills or extrapolated? 9. Contradictions? 10. Confidence?
