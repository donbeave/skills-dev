# Deep Research: How to Design AI Skills for Maximum Predictability and Reliable Execution

Conduct a rigorous, evidence-driven research project on **how AI/agent skills should be designed, authored, structured, tested, evaluated, and maintained to produce the most predictable and reliable possible behavior from non-deterministic language models**.

The goal is **not** to make LLMs deterministic. We accept that model inference is inherently stochastic and that even nominally deterministic configurations can exhibit variation.

Instead, determine:

> **How can we engineer a skill and the skill-development process so that repeated executions converge toward the intended behavior, follow the intended procedure, produce structurally consistent results, and minimize unwanted behavioral variance?**

The final research should result in actionable engineering principles for building a **best-in-class skill authoring system**.

---

# 1. Core Research Question

Research:

> What properties of an AI skill make its execution maximally predictable, reproducible, constrained, and reliable?

Investigate predictability at several levels:

1. **Task selection**
   - Does the model reliably understand when the skill should be invoked?
   - Does it avoid invoking the skill when it should not?

2. **Instruction interpretation**
   - Does the model consistently interpret the skill's objective in the same way?

3. **Execution path**
   - Does it follow approximately the same procedure across runs?

4. **Decision making**
   - Are important decisions constrained sufficiently to avoid arbitrary model choices?

5. **Tool usage**
   - Are tools called consistently and correctly?
   - Are arguments predictable?
   - Does tool order vary unnecessarily?

6. **Output structure**
   - Does the skill reliably produce the expected artifact, schema, or result?

7. **Output quality**
   - Does quality remain within an acceptable band across repeated executions?

8. **Failure behavior**
   - Does the skill fail in known and controlled ways?
   - Does it recognize insufficient information?
   - Does it avoid improvising outside its intended responsibility?

9. **Cross-model behavior**
   - Does the skill behave consistently across stronger and weaker models?

10. **Context sensitivity**
   - How much does unrelated conversation/context alter execution?

---

# 2. Research the Meaning of "Predictability"

Establish a rigorous definition.

Do not treat these terms as equivalent:

- determinism
- reproducibility
- reliability
- consistency
- robustness
- instruction adherence
- task success
- variance
- calibration
- schema adherence
- behavioral predictability

Develop a model such as:

**Skill Predictability =**

- activation consistency
- procedural consistency
- decision consistency
- tool-call consistency
- output-schema consistency
- semantic-result consistency
- task-success consistency
- failure-mode consistency

Determine which dimensions can realistically approach 100% and which cannot.

---

# 3. Evidence Requirements

This research must be based primarily on **measured evidence rather than opinions or generic prompt-engineering advice**.

Prioritize sources containing:

- controlled experiments
- benchmark results
- ablation studies
- repeated-run measurements
- variance measurements
- task-success percentages
- instruction-following benchmarks
- tool-use benchmarks
- agent benchmarks
- reliability measurements
- structured-output measurements
- prompt sensitivity studies
- reproducibility studies

Prefer, in approximately this order:

1. peer-reviewed papers
2. arXiv papers with substantial experiments
3. research from OpenAI, Anthropic, Google DeepMind, Microsoft Research, Meta, Stanford, Berkeley, Princeton, CMU, etc.
4. official model/provider engineering documentation containing empirical results
5. agent-framework research containing actual evaluations
6. production engineering reports with measured outcomes
7. high-quality experiments from independent researchers

Avoid basing important recommendations on:

- blog opinions without experiments
- anecdotal X/Twitter posts
- generic "prompt engineering best practices"
- unsupported statements repeated across blogs

For every major recommendation, classify the evidence as:

- **Strong empirical evidence**
- **Moderate empirical evidence**
- **Weak / anecdotal evidence**
- **Our engineering inference**

Whenever numbers are available, include them.

---

# 4. Research Prompt Sensitivity and Behavioral Variance

Deeply investigate research showing that LLM behavior changes due to seemingly minor differences such as:

- wording
- instruction ordering
- formatting
- whitespace
- examples
- label names
- option ordering
- context position
- prompt length
- irrelevant context
- duplicated instructions
- conflicting instructions
- negative vs positive wording
- placement of constraints
- number of examples
- example diversity
- system vs user instructions

Find experiments quantifying these effects.

Answer:

> Which skill-authoring techniques demonstrably reduce sensitivity to superficial prompt changes?

---

# 5. Skill Size and Decomposition

Investigate whether predictable behavior is improved by:

### A. One large/monolithic skill

versus

### B. Multiple narrowly scoped skills

For example:

- `skill-create`
- `skill-update`
- `skill-audit`
- `skill-refactor`
- `skill-evaluate`

instead of one large:

- `skill-authoring`

Research this using evidence from:

- instruction-following research
- context-length research
- agent specialization
- task decomposition
- routing
- prompt interference
- context dilution
- instruction conflicts
- long-context performance
- "lost in the middle"
- multi-task prompting
- tool-selection reliability

Determine whether narrower skills provide:

- better trigger precision
- lower instruction ambiguity
- fewer conflicting rules
- lower token consumption
- higher adherence
- better testability
- easier eval design
- more stable execution
- easier maintenance

Identify the point where excessive decomposition becomes harmful.

The final result should propose an evidence-backed rule for determining:

> **When should one skill be split into multiple skills?**

---

# 6. Skill Instruction Architecture

Research the ideal internal structure of a skill.

Compare approaches such as:

### Goal only

vs.

### Goal + constraints

vs.

### Goal + explicit workflow

vs.

### State machine

vs.

### decision tree

vs.

### checklist

vs.

### pseudocode

vs.

### algorithm

vs.

### examples

vs.

### input/output contract

vs.

### explicit invariants

Investigate whether a highly explicit procedure improves predictability.

For example:

```text
1. Inspect input.
2. Classify task.
3. Validate prerequisites.
4. Select exactly one execution path.
5. Execute.
6. Validate result.
7. Return according to schema.
```

Compare this against descriptive prose.

Determine which representation provides the strongest behavioral reliability.

---

# 7. Decision Points

Pay particular attention to **decision freedom**.

Hypothesis:

> Every unnecessary decision delegated to the model creates another source of behavioral variance.

Research whether evidence supports this.

Analyze instructions such as:

```text
Use an appropriate method.
```

versus:

```text
If condition A → use method X.
If condition B → use method Y.
Otherwise → stop and report Z.
```

Research whether converting implicit judgment into:

- explicit conditions
- lookup tables
- decision trees
- thresholds
- schemas
- enumerated choices

improves reliability.

Develop the concept of a possible:

## Decision Surface

Measure how many unconstrained decisions a skill asks the model to make.

Investigate whether this could become an engineering metric.

---

# 8. Ambiguity

Research how ambiguity influences behavioral variance.

Find evidence regarding:

- underspecified instructions
- conflicting instructions
- overlapping responsibilities
- vague adjectives
- subjective criteria

Examples:

```text
Make the skill better.
```

versus:

```text
Reduce SKILL.md token count while preserving all tested behaviors.
```

Develop rules for writing requirements that are:

- observable
- measurable
- falsifiable
- testable

---

# 9. Positive Instructions vs Prohibitions

Compare:

```text
Do X.
```

with:

```text
Don't do Y.
```

and:

```text
Do X.
Never do Y.
```

Research measured evidence concerning:

- negative instructions
- negation failures
- forbidden behaviors
- competing instructions

Determine the best way to encode constraints.

---

# 10. Examples and Few-Shot Behavior

Research how examples affect consistency.

Investigate:

- zero-shot vs one-shot vs few-shot
- positive examples
- negative examples
- boundary examples
- adversarial examples
- counterexamples
- examples covering decision branches
- example ordering
- example similarity

Determine whether examples should be treated as:

### documentation

or

### executable behavioral specifications.

Research how many examples are beneficial before returns diminish or context interference increases.

---

# 11. Skill Contracts

Research whether skills should behave more like APIs.

For example, define:

## Inputs

What information must exist?

## Preconditions

What must be true before execution?

## Outputs

What must be produced?

## Invariants

What must always remain true?

## Forbidden behavior

What must never happen?

## Failure conditions

When should execution stop?

## Postconditions

What should be validated before completion?

Determine whether this style produces more reliable LLM behavior.

---

# 12. Structured Outputs

Research empirical results for:

- JSON Schema
- grammar-constrained generation
- constrained decoding
- typed tool calls
- structured outputs
- function calling
- enum restrictions
- validation/retry loops

Separate improvements in:

- syntactic reliability
- semantic reliability

Determine where deterministic software should replace model reasoning.

---

# 13. Move Work Out of the Model

Explore the principle:

> **Do not ask the model to perform work that deterministic software can perform more reliably.**

Examples:

Instead of asking the LLM:

```text
Check whether all required files exist.
```

use software to verify them.

Instead of:

```text
Make sure the JSON follows the schema.
```

use schema validation.

Research hybrid architectures combining:

- deterministic code
- linters
- schemas
- parsers
- state machines
- static validation
- scripts
- tests
- LLM reasoning

Determine what should live in:

- `SKILL.md`
- scripts
- schemas
- templates
- tests
- evals

Produce a strong architectural recommendation.

---

# 14. Context Engineering

Investigate how skill context affects predictability.

Research:

- minimum sufficient context
- irrelevant context degradation
- long-context degradation
- context distraction
- lost-in-the-middle effects
- prompt dilution
- conflicting context
- reference files
- progressive disclosure

Answer:

> Is the most reliable skill generally the smallest amount of context that completely specifies the task?

Determine whether referenced files should be loaded:

- always
- conditionally
- only for specific branches

Propose rules.

---

# 15. Instruction Duplication

Investigate whether repeating critical rules improves adherence or instead:

- wastes context
- creates slight contradictions
- increases attention competition
- makes maintenance harder

Determine how important constraints should be represented.

---

# 16. Skill Routing and Trigger Design

A predictable skill is useless if invocation itself is unreliable.

Research how descriptions should be designed so agents consistently determine:

- when to use the skill
- when not to use it
- which sibling skill to choose

Investigate:

- semantic overlap
- mutually exclusive descriptions
- positive triggers
- negative triggers
- examples
- classification/routing stages

Develop rules for minimizing routing ambiguity.

---

# 17. Self-Verification

Research whether requiring the model to validate its own result improves consistency.

Compare:

### Generate only

vs.

### Generate → inspect → fix

vs.

### Generate → deterministic validation → fix

vs.

### Generate → independent model judge → fix

Use empirical evidence.

Investigate failure modes of self-review, including cases where the same model fails to detect its own errors.

---

# 18. Planning

Research whether forcing a model to create a plan before execution improves reliability.

Compare different task classes.

Do not assume planning is universally helpful.

Investigate when planning:

- improves task success
- increases token consumption
- introduces new opportunities for mistakes
- causes overthinking
- reduces predictability

Determine whether planning should be:

- always required
- conditional
- prohibited for simple tasks

---

# 19. Model Capability vs Skill Complexity

Investigate interactions between skill design and model strength.

A skill should ideally behave correctly on both frontier and cheaper models.

Research:

- instruction-following differences
- reasoning differences
- context handling
- tool-use reliability
- schema adherence

Determine whether explicit skills reduce the capability requirements placed on the underlying model.

Test the hypothesis:

> Better engineered skills allow weaker models to behave closer to stronger models because less reasoning is left unspecified.

Find empirical evidence where available.

---

# 20. Skill Development as Software Engineering

Treat a skill as a **program executed by a probabilistic interpreter**.

Explore how software-engineering concepts translate:

| Software Engineering | Skill Engineering |
|---|---|
| Type system | Input/output schemas |
| Function contract | Skill contract |
| Unit tests | Behavioral evals |
| Integration tests | Tool/workflow evals |
| Regression tests | Skill regression suite |
| Static analysis | Skill linter |
| Cyclomatic complexity | Decision complexity |
| API surface | Skill responsibility |
| Module boundaries | Skill decomposition |
| Compiler errors | Deterministic validators |
| Code coverage | Behavioral branch coverage |

Assess whether this analogy is useful and where it breaks down.

---

# 21. Complexity Metrics

Investigate whether we can define measurable skill complexity metrics.

Potential candidates:

### Instruction Count

Number of independent behavioral requirements.

### Decision Count

Number of model-controlled branches.

### Unconstrained Decision Count

Number of decisions without explicit rules.

### Branching Factor

Number of possible execution paths.

### Context Weight

Tokens required before useful execution begins.

### Responsibility Count

Number of independent jobs performed by one skill.

### Reference Fan-Out

Number of auxiliary documents potentially loaded.

### Tool Choice Entropy

Number of tools/actions the model can arbitrarily choose between.

### Ambiguity Score

Number of subjective/vague requirements.

### Behavioral Coverage

Percentage of important branches exercised by evals.

Research whether analogous metrics exist.

Propose useful new metrics if necessary.

---

# 22. Skill Development Lifecycle

The final objective is not merely better `SKILL.md` files.

Design a development lifecycle optimized for predictable behavior.

Research and propose:

```text
Specify
   ↓
Design contract
   ↓
Identify decision branches
   ↓
Reduce ambiguity
   ↓
Implement deterministic components
   ↓
Write skill instructions
   ↓
Create behavioral evals
   ↓
Run repeated trials
   ↓
Measure variance
   ↓
Identify unstable branches
   ↓
Refactor
   ↓
Regression test
```

Determine what should happen during:

- skill creation
- skill update
- skill refactoring
- skill auditing

---

# 23. Evals Are Critical

Do not define predictability based on a single successful execution.

Every important claim must account for repeated runs.

Develop an eval methodology where a skill is executed multiple times against:

- identical prompts
- paraphrased prompts
- equivalent contexts
- noisy contexts
- boundary cases
- adversarial cases
- different models
- different model versions

Measure:

### Task success rate

```text
successful executions / total executions
```

### Structural consistency

Percentage matching required structure.

### Instruction adherence

Percentage satisfying every mandatory requirement.

### Branch consistency

Whether equivalent inputs choose equivalent execution branches.

### Tool consistency

Whether expected tools are selected and called correctly.

### Semantic variance

How different successful answers are semantically.

### Failure-mode consistency

Whether invalid inputs fail correctly instead of improvising.

### Regression rate

Behavior lost after modifying the skill.

---

# 24. Statistical Methodology

Recommend how many repetitions are needed before calling a skill reliable.

Compare:

- 3 runs
- 5 runs
- 10 runs
- 30 runs
- 50 runs
- 100+ runs

Explain confidence intervals and sample-size implications.

For example, distinguish between observing:

```text
10/10 success
```

and having sufficient evidence for:

```text
≥99% reliability
```

Recommend statistical methods appropriate for skill evaluation.

---

# 25. Mutation Testing for Skills

Explore a concept analogous to software mutation testing.

Automatically modify:

- user wording
- irrelevant context
- order
- formatting
- file names
- examples
- tool availability
- edge conditions

Then determine whether the intended behavior remains invariant.

Research existing work on:

- prompt perturbation
- metamorphic testing
- robustness testing
- fuzzing LLMs
- prompt mutation
- adversarial prompt testing

Determine whether these techniques should become standard skill-development practices.

---

# 26. Behavioral Specifications

Investigate whether skills should be defined primarily by:

```text
When X happens,
the agent MUST do Y.
```

rather than long explanatory prose.

Research analogies with:

- BDD
- Given/When/Then
- executable specifications
- property-based testing
- contracts
- formal methods

Example:

```text
GIVEN a skill with >N independent responsibilities
WHEN responsibilities can be independently invoked
THEN recommend splitting the skill.
```

Determine whether this improves testability and predictable interpretation.

---

# 27. Refactoring for Predictability

Develop concrete indicators that a skill should be refactored.

Potential smells:

- too many responsibilities
- many "if/otherwise" branches
- numerous exceptions
- duplicated rules
- vague judgments
- excessive references
- overlapping sibling skills
- repeated eval failures
- model-dependent behavior
- instruction conflicts
- excessive context
- many optional execution paths

Create an evidence-backed:

## Skill Predictability Smell Catalog

---

# 28. Search Existing Skill Systems

Research approaches used by:

- OpenAI
- Anthropic
- Claude Code
- Codex
- Cursor
- GitHub Copilot
- Gemini
- agent frameworks
- SWE-agent
- OpenHands
- Devin-like systems
- MCP-based systems
- agent skill repositories
- prompt/programming frameworks

However, do not assume their approach is optimal.

Compare their practices against empirical research.

---

# 29. Research Adjacent Fields

Look outside "AI skills."

Some of the strongest evidence may exist under different terminology.

Search:

- prompt robustness
- prompt sensitivity
- LLM reproducibility
- agent reliability
- instruction-following reliability
- constrained generation
- tool-use reliability
- workflow orchestration
- program synthesis
- probabilistic programming
- formal methods
- human factors
- API design
- DSL design
- compiler design
- workflow engines
- property-based testing
- metamorphic testing

Extract techniques applicable to skill engineering.

---

# 30. Separate Model Problems From Skill Problems

For every observed failure classify it as:

### Model limitation

Example: insufficient reasoning ability.

### Skill design failure

Example: ambiguous instructions.

### Context failure

Example: irrelevant/conflicting context.

### Routing failure

Example: wrong skill selected.

### Tool failure

Example: incorrect API interaction.

### Validation failure

Example: bad result was never checked.

This distinction is important because only some failures can be fixed by rewriting instructions.

---

# 31. Required Experiments

Where published evidence is insufficient, design experiments that could validate the hypotheses.

At minimum design experiments for:

### Experiment A — Monolithic vs Specialized

One 3,000-token skill versus three ~1,000-token specialized skills.

Measure reliability and context consumption.

### Experiment B — Prose vs Algorithm

Same requirements expressed as prose versus explicit ordered procedure.

### Experiment C — Ambiguous vs Explicit Decisions

Model chooses an "appropriate" method versus deterministic decision table.

### Experiment D — Examples

0 / 1 / 3 / 5 / 10 examples.

### Experiment E — Context Noise

0%, 25%, 50%, 100% unrelated additional context.

### Experiment F — Repeated Runs

Run identical cases 30–100 times.

### Experiment G — Model Strength

Repeat on frontier, mid-range, and cheap models.

### Experiment H — Skill Mutation

Paraphrase and perturb equivalent inputs while checking invariant behavior.

For each experiment specify:

- independent variable
- dependent variables
- controls
- sample size
- metrics
- expected interpretation
- statistical method

---

# 32. Final Deliverable

The report must culminate in a practical engineering doctrine.

Create:

# Part I — Executive Conclusion

Answer in plain language:

> What should we do if our #1 priority is predictable skill execution?

Provide the 10 most important principles ranked by expected impact.

---

# Part II — Evidence Matrix

Create a table:

| Technique | Evidence | Measured Effect | Confidence | Recommendation |
|---|---|---:|---|---|
| Explicit schemas | ... | ... | High | ... |
| Narrow responsibilities | ... | ... | ... | ... |
| Examples | ... | ... | ... | ... |
| Decision tables | ... | ... | ... | ... |
| Shorter context | ... | ... | ... | ... |

Do not claim numerical improvement without evidence.

---

# Part III — Anatomy of a Predictable Skill

Produce an ideal skill template containing only components justified by the research.

For example:

```text
---
metadata
---

# Purpose

# Use when

# Do not use when

# Inputs

# Preconditions

# Invariants

# Procedure

# Decision rules

# Output contract

# Validation

# Failure conditions

# Examples
```

But do not assume this template beforehand—derive it from the research.

---

# Part IV — Predictability Checklist

Create a checklist usable during skill creation and review.

Every item should be objectively answerable where possible.

Avoid vague checks such as:

```text
Is the skill clear?
```

Prefer:

```text
Can every conditional execution branch be identified from the instructions?
```

---

# Part V — Skill Linter Rules

Identify properties that can be statically checked automatically.

Examples:

- SKILL.md exceeds recommended complexity
- overlapping trigger descriptions
- undefined terminology
- excessive references
- duplicated instructions
- contradictory MUST/MUST NOT requirements
- unbounded phrases such as "as appropriate"
- output required without validation
- branching without explicit conditions

Separate:

### mechanically enforceable rules

from:

### model-evaluated rules.

---

# Part VI — Eval Standard

Create a recommended standard such as:

```text
Skill Reliability Suite
├── activation evals
├── happy-path evals
├── boundary evals
├── negative evals
├── mutation evals
├── adversarial evals
├── tool-use evals
├── cross-model evals
└── regression evals
```

Specify how each category should work.

---

# Part VII — Skill Predictability Score

Attempt to construct a practical scoring model from 0–100.

Potential dimensions:

- trigger precision
- responsibility isolation
- instruction specificity
- decision explicitness
- deterministic enforcement
- context efficiency
- behavioral coverage
- repeated-run stability
- failure handling
- cross-model robustness

Do not make arbitrary weights.

Either derive them from evidence or explicitly mark the score as an engineering heuristic requiring calibration.

---

# Part VIII — Creation / Update / Refactor Process

Produce separate workflows for:

## `skill-create`

Optimize a new skill from the beginning for low behavioral variance.

## `skill-update`

Add or change behavior without causing regressions.

Require new evals for newly introduced behavior and regression evals for existing behavior.

## `skill-refactor`

Improve structure **without intentionally changing behavior**.

Use evals to prove behavioral equivalence.

Determine when a skill should be:

- simplified
- split
- merged
- moved into deterministic code
- given additional validation
- given a narrower trigger

---

# 33. Most Important Final Question

Conclude by answering:

> **If an LLM is inherently non-deterministic, what engineering system surrounding the LLM gives us the closest practical equivalent of deterministic skill behavior?**

Do not answer this philosophically.

Answer it as an engineering architecture.

For example, determine how much predictability should come from:

```text
Narrow responsibility
        +
Explicit contract
        +
Low decision freedom
        +
Minimal context
        +
Deterministic tooling
        +
Structured interfaces
        +
Validation
        +
Repeated statistical evals
        +
Regression testing
```

But treat this as a hypothesis to validate rather than an assumed conclusion.

---

# Research Quality Bar

This should be **deep research, not a survey**.

For every important recommendation ask:

1. What evidence supports it?
2. Was it experimentally measured?
3. On which models?
4. On which tasks?
5. How large was the effect?
6. How many trials were performed?
7. Does newer research reproduce the finding?
8. Does the evidence apply directly to agent skills or are we extrapolating?
9. What evidence contradicts it?
10. How confident should we be?

Explicitly distinguish:

**PROVEN**
→ supported by repeated quantitative evidence.

**LIKELY**
→ good evidence but indirect or limited.

**HYPOTHESIS**
→ plausible engineering principle that still requires our own evals.

The final objective is to turn **skill authoring from prompt writing into reliability engineering for probabilistic programs**.