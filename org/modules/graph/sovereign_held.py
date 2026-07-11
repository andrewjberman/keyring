"""Sovereign-hold predicates -- the ONE canonical answer to "is this a held bd/schwab path/bucket?" and
"is the hold lifted?" for every comp-tool guard.

LOAD-BEARING SECURITY LEAF. Every bd-reader guard imports from here, so this module:
  - imports ONLY the Python standard library (os). ZERO third-party/internal deps -- it can NEVER fail to
    import or be perturbed by a dependency change. Asserted by tests/test_sovereign_held.py (an ast check
    over this module's own import nodes). DO NOT add a non-stdlib import.
  - is_held_path / is_held_bucket are PURE STRING checks -- they NEVER open a file (the property the whole
    sovereign hold rests on: a metadata check must not itself read held content).

Consolidates the scattered held-predicate copies (trace_graph._held_path_hit, comp_constants
SOVEREIGN_HELD_MARKERS, extract_iam._rel_is_held, freeze_monitor._bucket_is_held, validate_cli.
_is_held_bd_path, and the comp_dispatch / comp_recognizers / freshness_manifest_gen C0 locals) into ONE
predicate set + ONE lift signal. NFRA_TOOLPASS post-sweep consolidation TO (CTO-gated 2026-07-11).
Sovereign hold: bd / 49F / Schwab (2026-07-09).
"""

from __future__ import annotations

import os

# Held SOURCE-path markers (substring match on a "/"-normalized path string).
HELD_PATH_MARKERS = (
    "data/black_diamond/",
    "data/canonical/schwab/silver/",
    "schwab/silver/",
)

# Held S3 BUCKET prefixes. Family match: exact | "<p>-*" | "<p>/*" -- so opal-data-bdx is NOT held (a
# distinct bucket), but opal-data-bd, opal-data-bd-raw, and opal-data-bd/key ARE. Lifted verbatim from
# freeze_monitor._bucket_is_held so the AE~C migration is a true no-op refactor.
HELD_BUCKET_PREFIXES = (
    "opal-data-bd",
    "opal-data-schwab",
)

# The ONE canonical lift signal: COMP_INCLUDE_HELD=1 lifts the hold for ALL tools at once (COO's
# bd-hold-lift resumption checklist collapses to setting this single var).
CANONICAL_INCLUDE_HELD_VAR = "COMP_INCLUDE_HELD"


def is_held_path(path) -> bool:
    """True if `path` is under a held bd/schwab SOURCE tree. PURE string check -- never opens a file."""
    if not path:
        return False
    s = str(path).replace("\\", "/")
    return any(m in s for m in HELD_PATH_MARKERS)


def is_held_bucket(bucket) -> bool:
    """True if `bucket` is a held bd/schwab S3 bucket. Family: exact | '<p>-*' | '<p>/*'. PURE str check.
    opal-data-bdx is NOT held; opal-data-bd / opal-data-bd-raw / opal-data-bd/key ARE. Accepts an
    s3://bucket[/key] or a bare bucket[/key]."""
    if not bucket:
        return False
    s = str(bucket).replace("\\", "/")
    if s.startswith("s3://"):
        s = s[len("s3://"):]
    return any(s == p or s.startswith(p + "-") or s.startswith(p + "/") for p in HELD_BUCKET_PREFIXES)


def include_held(*legacy_var_names: str) -> bool:
    """True => the hold is LIFTED / overridden (INCLUDE held paths). False => hold in force (skip held).

    Precedence (EXACT): COMP_INCLUDE_HELD=="1" lifts ALL tools; else any passed legacy per-tool var =="1"
    lifts THIS tool (back-compat during the deprecation window). Neither set -> held. The caller passes
    its own legacy var(s), e.g. include_held("COMP_VALIDATE_INCLUDE_HELD")."""
    if os.environ.get(CANONICAL_INCLUDE_HELD_VAR) == "1":
        return True
    return any(os.environ.get(v) == "1" for v in legacy_var_names)
