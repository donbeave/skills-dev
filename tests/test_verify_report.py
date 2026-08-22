"""Drive scripts/verify_report.py against the shipped research files."""

from __future__ import annotations

import sys
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
