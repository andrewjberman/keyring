"""
Knowledge Function Execution Modules (KF_EXECUTION_MODES).

Each module implements one knowledge function stage with a standard interface.
Modules are registered in registry.json and invoked by the dispatch planner.

Spec: ONT.CORE.KF_EXECUTION_MODES
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal


@dataclass
class AxisResult:
    """Single classification axis with confidence."""
    code: str = ""
    confidence: float = 0.0
    evidence: str = ""


@dataclass
class Classification:
    """Minimal classification record used across modules."""
    path: str = ""
    category: str = ""
    lifecycle_role: AxisResult = field(default_factory=lambda: AxisResult())
    behavior_class: AxisResult = field(default_factory=lambda: AxisResult())
    governance_intent: AxisResult = field(default_factory=lambda: AxisResult())
    confidence: float = 0.0
    confident: bool = False
    metadata: Any = None
    fingerprint: Any = None


@dataclass
class ModuleOutput:
    """Standard output from any execution module.

    Every module returns this regardless of execution mode (D/R/I).
    The dispatch planner reads `escalations` to decide whether to
    forward items to the next mode.
    """
    data: Any = None                   # Primary output (list of records, classification results, etc.)
    confident: list[Any] = field(default_factory=list)    # Items resolved at this stage
    ambiguous: list[Any] = field(default_factory=list)    # Items needing escalation to next mode
    confidence_scores: dict[str, float] = field(default_factory=dict)  # Per-item or aggregate
    mode: Literal["D", "R", "I"] = "D"
    stage: str = ""                    # Pe, In, Ev, De, Ac, Ad
    stats: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
