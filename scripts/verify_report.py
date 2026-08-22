#!/usr/bin/env python3
"""Structural checks on the research corpus. Not a model eval."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REPORT = REPO_ROOT / "research" / "REPORT.md"
MATRIX = REPO_ROOT / "research" / "EVIDENCE-MATRIX.md"
EXPERIMENTS = REPO_ROOT / "research" / "EXPERIMENTS.md"
CITATIONS = REPO_ROOT / "research" / "CITATIONS.md"

REQUIRED_HEADINGS = [
    "# 1. Core research question",
    "### 1.1 Task selection",
    "### 1.2 Instruction interpretation",
    "### 1.3 Execution path",
    "### 1.4 Decision making",
    "### 1.5 Tool usage",
    "### 1.6 Output structure",
    "### 1.7 Output quality",
    "### 1.8 Failure behavior",
    "### 1.9 Cross-model",
    "### 1.10 Context sensitivity",
    "# 2. Meaning of",
    "**Activation consistency**",
    "**Procedural consistency**",
    "**Decision consistency**",
    "**Tool-call consistency**",
    "**Output-schema consistency**",
    "**Semantic-result consistency**",
    "**Task-success consistency**",
    "**Failure-mode consistency**",
    "# 4. Prompt sensitivity",
    "# 5. Skill size",
    "# 6. Skill instruction architecture",
    "# 7. Decision points",
    "# 8. Ambiguity",
    "# 9. Positive instructions",
    "# 10. Examples",
    "# 11. Skill contracts",
    "# 12. Structured outputs",
    "# 13. Move work out",
    "# 14. Context engineering",
    "# 15. Instruction duplication",
    "# 16. Skill routing",
    "# 17. Self-verification",
    "# 18. Planning",
    "# 19. Model capability",
    "# 20. Skill development as software",
    "# 21. Complexity metrics",
    "# 22. Skill development lifecycle",
    "# 23. Evals are critical",
    "# 24. Statistical methodology",
    "# 25. Mutation testing",
    "# 26. Behavioral specifications",
    "# 27. Skill predictability smell",
    "# 28. Existing skill systems",
    "# 29. Adjacent fields",
    "# 30. Failure taxonomy",
    "# 31. Experiments",
    "# Part I",
    "# Part II",
    "# Part III",
    "# Part IV",
    "# Part V",
    "# Part VI",
    "# Part VII",
    "# Part VIII",
    "10/10 ≠ ≥99%",
    "pass^k",
    "**PROVEN**",
    "**LIKELY**",
    "**HYPOTHESIS**",
    "Strong empirical",
]

EXPERIMENT_MARKERS = [
    "## A —",
    "## B —",
    "## C —",
    "## D —",
    "## E —",
    "## F —",
    "## G —",
    "## H —",
    "**IV:**",
    "**DVs:**",
    "**Controls:**",
    "**n:**",
    "**Stats:**",
    "**Interpretation:**",
]


def missing_substrings(text: str, needles: list[str]) -> list[str]:
    return [n for n in needles if n not in text]


def verify_corpus(root: Path | None = None) -> dict[str, list[str]]:
    root = root or REPO_ROOT
    report = (root / "research" / "REPORT.md").read_text(encoding="utf-8")
    matrix = (root / "research" / "EVIDENCE-MATRIX.md").read_text(encoding="utf-8")
    experiments = (root / "research" / "EXPERIMENTS.md").read_text(encoding="utf-8")
    citations = (root / "research" / "CITATIONS.md").read_text(encoding="utf-8")
    problems: dict[str, list[str]] = {
        "report": missing_substrings(report, REQUIRED_HEADINGS),
        "experiments": missing_substrings(experiments, EXPERIMENT_MARKERS),
        "matrix": [],
        "citations": [],
    }
    if "Measured effect" not in matrix:
        problems["matrix"].append("missing Measured effect column")
    if "[37]" not in matrix and "OpenAI" not in matrix:
        problems["matrix"].append("no OpenAI structured-output citation")
    if "10/10" not in report:
        problems["report"].append("missing 10/10 vs 99% discussion")
    if "arxiv.org" not in citations.lower() and "https://arxiv.org" not in citations:
        # CITATIONS uses https://arxiv.org in entries
        if "arxiv.org" not in citations:
            problems["citations"].append("no arxiv citations")
    return {k: v for k, v in problems.items() if v}


def main() -> int:
    problems = verify_corpus()
    if problems:
        for section, items in problems.items():
            print(f"FAIL {section}:")
            for item in items:
                print(f"  - {item}")
        return 1
    print("OK research corpus structural checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
