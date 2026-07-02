"""comp-debt -- generalizable estate-debt identification (FUSION + GUARD).

A fusion over existing signal-sources + the dormant-vs-dead GUARD, NOT a new scanner.
Canonical spec: docs/architecture/NFRA_COMPDEBT_PRD.md. Design owner: 0.0.0_AB_MSTR.
Builder: 0.7.0_AE_CloudOps (graph-module owner lane). CTO arch-gates each signal + the
dormant_guard keystone specifically.

EMIT-ONLY: comp-debt NEVER acts. Decommission is downstream, comp-blast-preceded, and
human-gated for unrecoverable classes (EC2/S3/IAM).
"""
from __future__ import annotations

__all__ = ["grounding_lib"]
