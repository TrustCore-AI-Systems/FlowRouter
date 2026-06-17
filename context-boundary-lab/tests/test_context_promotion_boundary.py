"""
Public-safe tests for the FlowRouter Context Boundary Lab.

Run from repository root after copying these files:

    python -m pytest docs/context-boundary-lab/tests

These tests intentionally validate only the included public example interface.
They do not represent production TrustCore logic.
"""

from __future__ import annotations

import json
from pathlib import Path

from docs.context_boundary_lab.gate_api.interface import ExampleConservativeContextBoundary


CASES_DIR = Path(__file__).resolve().parents[1] / "cases"


def load_case(name: str) -> dict:
    with (CASES_DIR / name).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def evaluate_case(name: str):
    case = load_case(name)
    gate = ExampleConservativeContextBoundary()
    return gate.evaluate(case["candidate_context_item"], case["context_snapshot"])


def test_stale_approval_is_denied_as_context() -> None:
    result = evaluate_case("stale_approval_reused_as_context.json")
    assert result.verdict == "DENY_TRANSFER"
    assert "STALE_APPROVAL" in result.reason_codes
    assert result.human_review_required is True


def test_private_signal_to_public_surface_requires_review() -> None:
    result = evaluate_case("private_signal_promoted_to_public_action.json")
    assert result.verdict == "REVIEW_TRANSFER"
    assert "PRIVATE_SIGNAL_PUBLIC_SURFACE" in result.reason_codes
    assert result.human_review_required is True


def test_recommendation_is_not_permission() -> None:
    result = evaluate_case("recommendation_reused_as_permission.json")
    assert result.verdict == "REVIEW_TRANSFER"
    assert "RECOMMENDATION_AS_PERMISSION" in result.reason_codes
    assert result.human_review_required is True


def test_raw_tool_output_requires_review_before_truth_promotion() -> None:
    result = evaluate_case("tool_output_becomes_truth.json")
    assert result.verdict == "REVIEW_TRANSFER"
    assert "RAW_TOOL_OUTPUT_UNVERIFIED" in result.reason_codes
    assert result.human_review_required is True


def test_summary_preserves_refusal_boundary() -> None:
    result = evaluate_case("summary_loses_refusal_boundary.json")
    assert result.verdict == "REVIEW_TRANSFER"
    assert "REFUSAL_BOUNDARY_LOST" in result.reason_codes
    assert result.human_review_required is True
