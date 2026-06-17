"""
Public-safe FlowRouter Context Boundary interface.

This interface is intentionally small and illustrative. It does not contain
private TrustCore architecture, production policy logic, secrets, customer data,
external network calls, analytics, or storage behavior.

The boundary modeled here is context transfer, not action execution.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Protocol


VALID_CONTEXT_VERDICTS = ("ALLOW_TRANSFER", "REVIEW_TRANSFER", "DENY_TRANSFER")


@dataclass(frozen=True)
class ContextEvaluationResult:
    """Result of evaluating whether an item may become future context."""

    verdict: str
    reason_codes: tuple[str, ...] = field(default_factory=tuple)
    explanation: str = ""
    safe_content: str | None = None
    human_review_required: bool = False

    def __post_init__(self) -> None:
        if self.verdict not in VALID_CONTEXT_VERDICTS:
            raise ValueError(f"Invalid context verdict: {self.verdict}")


class ContextBoundary(Protocol):
    """Public-safe protocol for context promotion evaluation."""

    def evaluate(
        self,
        context_item: Mapping[str, Any],
        context_snapshot: Mapping[str, Any],
    ) -> ContextEvaluationResult:
        """
        Evaluate whether a candidate item may become future working context.

        This method should not execute actions. It should only decide whether
        the information may be transferred, must be reviewed, or should be
        denied as future context.
        """
        ...


class ExampleConservativeContextBoundary:
    """
    Minimal public example implementation.

    Conservative behavior:
    - public/private surface mismatch => REVIEW_TRANSFER
    - recommendation-as-permission => REVIEW_TRANSFER
    - stale approval => DENY_TRANSFER
    - lost refusal boundary => REVIEW_TRANSFER
    - otherwise => ALLOW_TRANSFER

    This is not a production implementation.
    """

    def evaluate(
        self,
        context_item: Mapping[str, Any],
        context_snapshot: Mapping[str, Any],
    ) -> ContextEvaluationResult:
        flags = set(context_item.get("risk_flags", []))
        target_surface = str(context_snapshot.get("target_surface", ""))

        if "stale_approval" in flags:
            return ContextEvaluationResult(
                verdict="DENY_TRANSFER",
                reason_codes=("STALE_APPROVAL",),
                explanation="A stale approval must not be promoted as current authorization.",
                human_review_required=True,
            )

        if "private_signal" in flags and "public" in target_surface.lower():
            return ContextEvaluationResult(
                verdict="REVIEW_TRANSFER",
                reason_codes=("PRIVATE_SIGNAL_PUBLIC_SURFACE", "HUMAN_APPROVAL_REQUIRED"),
                explanation="A private signal is being considered for a public surface.",
                human_review_required=True,
            )

        if "recommendation_as_permission" in flags:
            return ContextEvaluationResult(
                verdict="REVIEW_TRANSFER",
                reason_codes=("RECOMMENDATION_AS_PERMISSION",),
                explanation="A recommendation must not be promoted as permission.",
                human_review_required=True,
            )

        if "refusal_boundary_lost" in flags:
            return ContextEvaluationResult(
                verdict="REVIEW_TRANSFER",
                reason_codes=("REFUSAL_BOUNDARY_LOST",),
                explanation="A summary or transfer candidate lost a refusal/review boundary.",
                human_review_required=True,
            )

        if "raw_tool_output_unverified" in flags:
            return ContextEvaluationResult(
                verdict="REVIEW_TRANSFER",
                reason_codes=("RAW_TOOL_OUTPUT_UNVERIFIED",),
                explanation="Raw tool output should be verified before it becomes future context.",
                human_review_required=True,
            )

        return ContextEvaluationResult(
            verdict="ALLOW_TRANSFER",
            reason_codes=(),
            explanation="No public-safe risk flags detected for context transfer.",
            safe_content=str(context_item.get("content", "")),
            human_review_required=False,
        )
