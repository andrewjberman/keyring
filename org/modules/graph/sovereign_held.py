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

# =============================================================================
# TWO PREDICATES, ONE VALUE SET. They were fused; the fusion was the bug.
# =============================================================================
# This leaf used to express ONE tuple serving TWO unrelated purposes:
#   (1) GOVERNANCE -- the 2026-07-09 sovereign hold: "do not READ bd/49F/Schwab source or data."
#       Andrew RETRACTED this COMPLETELY on 2026-07-14 ~03:3xZ to COO, verbatim:
#       "Oh that is retarded, 49 is back on the menu now, take the sovereign block off completely,
#        that is no excuse to not verify the work."
#   (2) PROD-TARGET SAFETY -- "an automated PROBE must never WRITE to / target a production bd bucket."
#       Nobody retracted this. It is not governance and does not move with any retraction.
# Because both were one tuple, honouring the retraction by deleting the values would have silently
# destroyed (2). Splitting by PURPOSE is what lets (1) lift while (2) stays armed. (CTO ruling
# 2026-07-22: "SPLIT the predicate, do NOT rip it.")
#
# A RETRACTION IS NOT A FIND-AND-DELETE WHEN A LIVE CONTROL IS COINCIDENTALLY EXPRESSED IN THE SAME
# PREDICATE. Before changing either set, ask which of the two you mean.

# ---- (1) GOVERNANCE: the 2026-07-09 hold. RETRACTED 2026-07-14. Empty is the correct state. ----
SOVEREIGN_HELD_PATHS: tuple[str, ...] = ()
SOVEREIGN_HELD_BUCKETS: tuple[str, ...] = ()

# Back-compat aliases -- the historical names, still imported by comp_constants_cli, trace_graph and
# comp-secrets. They alias the GOVERNANCE set, so those three lift automatically and correctly.
HELD_PATH_MARKERS = SOVEREIGN_HELD_PATHS
HELD_BUCKET_PREFIXES = SOVEREIGN_HELD_BUCKETS

# The lifted values, RETAINED so a future hold is a one-line re-point rather than a rebuild.
# A guard you cannot re-arm is not a fix, it is a removal.
RETRACTED_20260709_PATHS = (
    "data/black_diamond/",
    "data/canonical/schwab/silver/",
    "schwab/silver/",
)
RETRACTED_20260709_BUCKETS = (
    "opal-data-bd",
    "opal-data-schwab",
)

# ---- (2) PROD-TARGET SAFETY: NOT governance, NOT retracted, UNCHANGED IN FORCE. ----
# A compproof probe's run-argv, scratch write target, or IAM fixture ARN may never name a production
# bd/schwab resource -- a recurring probe would otherwise touch production on every re-run. Consumers:
# compproof/tool_probe.py (_assert_scratch_in_scope + the IAM fixture ARN check + the kuzu query guard)
# and compproof/tool_corpus.py (assert_sovereign_safe, which fails the corpus LOAD).
PROD_WRITE_FORBIDDEN_PATHS = (
    "data/black_diamond/",
    "data/canonical/schwab/silver/",
    "schwab/silver/",
)
PROD_WRITE_FORBIDDEN_BUCKETS = (
    "opal-data-bd",
    "opal-data-schwab",
)

# The ONE canonical lift signal: COMP_INCLUDE_HELD=1 lifts the hold for ALL tools at once (COO's
# bd-hold-lift resumption checklist collapses to setting this single var).
CANONICAL_INCLUDE_HELD_VAR = "COMP_INCLUDE_HELD"


def _path_matches(path, markers) -> bool:
    """Substring match of `path` against `markers`. PURE string check -- never opens a file."""
    if not path or not markers:
        return False
    s = str(path).replace("\\", "/")
    return any(m in s for m in markers)


def _bucket_matches(bucket, prefixes) -> bool:
    """Family match: exact | '<p>-*' | '<p>/*' -- so opal-data-bdx does NOT match (a distinct bucket),
    but opal-data-bd, opal-data-bd-raw and opal-data-bd/key DO. Accepts an s3://bucket[/key], an
    arn:aws:s3:::bucket[/key] (S3 resource ARN -- no region/account), or a bare bucket[/key]. The ARN
    form is REQUIRED: extract_iam / comp-iam / any IAM-resource caller passes an S3 ARN, and without
    this strip a bd ARN read as not-matching (a safety hole; CTO 2026-07-12)."""
    if not bucket or not prefixes:
        return False
    # .strip().lower() matches the original freeze_monitor._bucket_is_held EXACTLY and is CONSERVATIVE:
    # lowercasing can only ADD matches (OPAL-DATA-BD -> opal-data-bd), never remove one -> matching is
    # the safe failure direction. S3 bucket names are lowercase by AWS rule.
    s = str(bucket).replace("\\", "/").strip().lower()
    for pfx in ("s3://", "arn:aws:s3:::"):   # normalize URI + S3-ARN forms to bucket[/key] first
        if s.startswith(pfx):
            s = s[len(pfx):]
            break
    return any(s == p or s.startswith(p + "-") or s.startswith(p + "/") for p in prefixes)


def is_held_path(path) -> bool:
    """GOVERNANCE predicate: is `path` under the 2026-07-09 sovereign hold?

    The hold was RETRACTED 2026-07-14, so this is now always False by design. It is kept (rather than
    deleted) so the ~12 governance consumers need no edit and so a future hold is one re-point away.
    DO NOT use this to answer "may an automated probe target this?" -- that is
    is_prod_write_forbidden, a different control that did NOT lift."""
    return _path_matches(path, SOVEREIGN_HELD_PATHS)


def is_held_bucket(bucket) -> bool:
    """GOVERNANCE predicate for S3 buckets. Retracted 2026-07-14 -> always False by design.
    For probe/scratch write targets use is_prod_write_forbidden instead."""
    return _bucket_matches(bucket, SOVEREIGN_HELD_BUCKETS)


def is_prod_write_forbidden(target) -> bool:
    """PROD-WRITE SAFETY predicate -- IN FORCE, never retracted, not governance.

    NAME NOTE: named PROD_WRITE_* per the CTO R7 ruling. The semantics are slightly BROADER than
    "write": it also guards an IAM fixture's simulate targets (role_arn / held_resource), which are
    not writes. The ruled name is kept anyway -- a spec name is a coordination contract, and an
    unflagged rename here made a reviewer's positive control return a false ABSENT (2026-07-22).

    True if `target` names a production bd/schwab path OR bucket, in any of the accepted forms
    (bare path, bucket, bucket/key, s3://..., arn:aws:s3:::...). An automated compproof probe must
    never carry such a target in its run-argv, scratch URI, or IAM fixture ARN: a recurring probe
    would touch production on every re-run. Checks BOTH the path and bucket sets because a probe
    target can be either shape, which is why the original callers had to OR two predicates."""
    return (_path_matches(target, PROD_WRITE_FORBIDDEN_PATHS)
            or _bucket_matches(target, PROD_WRITE_FORBIDDEN_BUCKETS))


def include_held(*legacy_var_names: str) -> bool:
    """True => the hold is LIFTED / overridden (INCLUDE held paths). False => hold in force (skip held).

    Precedence (EXACT): COMP_INCLUDE_HELD=="1" lifts ALL tools; else any passed legacy per-tool var =="1"
    lifts THIS tool (back-compat during the deprecation window). Neither set -> held. The caller passes
    its own legacy var(s), e.g. include_held("COMP_VALIDATE_INCLUDE_HELD")."""
    if os.environ.get(CANONICAL_INCLUDE_HELD_VAR) == "1":
        return True
    return any(os.environ.get(v) == "1" for v in legacy_var_names)
