# Source cluster: context, position, distraction, progressive disclosure

## Liu et al. 2023 — Lost in the Middle (TACL 2023)

- Paper: https://arxiv.org/abs/2307.03172
- Tasks: multi-document QA (Natural Questions) and key-value retrieval.
- Models: GPT-3.5-Turbo, GPT-3.5-Turbo-16K, Claude-1.3 / 100K, LongChat-13B, MPT-30B-Instruct.
- Closed-book vs oracle (Table 1): GPT-3.5-Turbo **56.1%** closed-book, **88.3%** oracle.
- U-shaped curve. GPT-3.5-Turbo 20-document setting: **75.8%** gold at position 1, **53.8%** at index 9, **63.2%** last. Middle **below closed-book 56.1%**.
- 30-document GPT-3.5-Turbo-16K: **73.4%** index 0, **50.5%** index 9, **50.9%** index 14, **63.7%** last.
- Worst-case drop **>20 points**. Long-context variants do **not** fix utilization.
- Query-aware contextualization (query before **and** after) nearly solves synthetic KV retrieval (100% at 300 pairs for GPT-3.5-16K) but **does not** flatten the QA U-curve.
- Implication for skills: put **invariants, decision tables, and output contracts at the edges** of SKILL.md (start and/or end). Do not bury the binding rule in the middle of a long body. Do not dump unused reference files into context.

**Grade:** Strong empirical. **Caveat:** later long-context models (2024–2026) are more robust to **absolute** position; **relative** spacing of relevant pieces still hurts (see 2410.14641).

## Later long-context follow-up (arXiv 2410.14641)

- Most current commercial models more robust to “lost in the middle” as **absolute** position.
- **Relative** distance between relevant pieces still degrades all models (rapid then gradual decline).
- Implication: progressive disclosure still justified; packing many weakly related references still costs.

**Grade:** Moderate empirical (one paper, 11 models).

## Shi et al. 2023 — LLMs Can Be Easily Distracted by Irrelevant Context (ICML 2023)

- Paper: https://arxiv.org/abs/2302.00093
- Dataset: GSM-IC (GSM8K + one irrelevant sentence).
- Models: Codex (`code-davinci-002`), GPT-3.5 (`text-davinci-003`).
- Of originally solvable problems, **≤18%** remain consistently solved across **all** distractor types (greedy).
- Macro accuracy: **<30%** of base problems consistently solved after distractors.
- In-topic, role-overlap, in-range-number distractors are **harder**.
- Mitigations measured: self-consistency; explicit “ignore irrelevant information” instruction; least-to-most.
- Implication: **minimum sufficient context**. Conversation history, extra files, and sibling-skill text are distractors. Skills must **not** load unused references.

**Grade:** Strong empirical (math reasoning). **Skill extrapolation:** high for context packing.

## Anthropic 2025 — Equipping agents with Agent Skills

- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Progressive disclosure:
  1. Metadata (`name`, `description`) always in system prompt (~100 tokens / skill)
  2. `SKILL.md` body loaded on trigger
  3. Linked files / scripts loaded only as needed
- Scripts: run code **without** loading script or PDF into context; deterministic reliability.
- Authoring advice: **start with evaluation**; split when SKILL.md unwieldy; mutually exclusive contexts in separate files; watch `name`/`description` for routing.
- This is **engineering documentation**, not a controlled ablation of progressive disclosure vs monolith. Treat as **production design + Our engineering inference**, supported indirectly by Liu/Shi.

**Grade:** Weak-anecdotal as measured effect; **strong** as architectural description of a shipped system.

## Agent Skills spec (agentskills.io)

- https://agentskills.io/specification
- Recommended: metadata ~100 tokens; SKILL.md body **<5000 tokens**; keep main SKILL.md **under 500 lines**.
- File references **one level deep**.
- `description` must say **what** and **when**.
- No published A/B of 500 vs 2000 lines. Limits are **design constraints**, not measured optima.

**Grade:** Production spec / Our engineering inference.
