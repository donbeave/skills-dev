"""Drive scripts/verify_report.py against the shipped research files."""

from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import verify_report  # noqa: E402


def test_verify_corpus_on_shipped_report():
    problems = verify_report.verify_corpus(ROOT)
    assert problems == {}, problems


def test_main_exit_zero_on_shipped_report():
    code = verify_report.main()
    assert code == 0


def test_recommendation_markers_detect_missing_rule():
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        shutil.copytree(ROOT / "research", root / "research")
        path = root / "research" / "SKILL-DEVELOPMENT-RECOMMENDATIONS.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(
            text.replace("## Definition of done", "## Broken final section"),
            encoding="utf-8",
        )
        problems = verify_report.verify_corpus(root)
        assert problems["recommendations"] == ["## Definition of done"]


def test_recommendation_structure_detects_bad_table_and_order():
    path = ROOT / "research" / "SKILL-DEVELOPMENT-RECOMMENDATIONS.md"
    text = path.read_text(encoding="utf-8")

    missing_row = "\n".join(
        line for line in text.splitlines() if not line.startswith("| 16 |")
    )
    assert "core rules must be numbered exactly 1 through 16" in (
        verify_report.verify_recommendations(missing_row)
    )

    empty_cell = text.replace(
        "Never use an open-ended goal or silently expand scope.", ""
    )
    assert "each core rule must have four nonempty cells" in (
        verify_report.verify_recommendations(empty_cell)
    )

    wrong_order = (
        text.replace("## Conditional guidance", "## TEMP")
        .replace("## Reliability metric definitions", "## Conditional guidance")
        .replace("## TEMP", "## Reliability metric definitions")
    )
    assert "recommendation sections are out of order" in (
        verify_report.verify_recommendations(wrong_order)
    )
