"""PROD-TARGET WRITE SAFETY -- the ONE canonical answer to "may an automated probe target this?"

NOT GOVERNANCE. This control was never retracted and does not move with any governance retraction.
It stops a compproof probe's run-argv, scratch write target, or IAM fixture ARN from naming a
PRODUCTION bd/schwab resource -- without it a recurring probe touches production on every re-run.

WHY THIS MODULE EXISTS AS ITS OWN FILE (NFRA_TOOLUNIFY.GOVRIP step 1, 2026-07-25):
    These symbols used to live in `sovereign_held.py` alongside the 2026-07-09 GOVERNANCE hold that
    Andrew RETRACTED on 2026-07-14. The two purposes were fused in one tuple once already, and the
    fusion WAS the bug (CTO ruling 2026-07-22: "SPLIT the predicate, do NOT rip it").

    Andrew then ruled on 2026-07-25 ~185538Z that no comp-tool may carry a governance predicate at
    all, which retires the governance half entirely. Extracting THIS half FIRST means the deletion
    of the governance module cannot take the live safety control with it:

      >> AFTER THIS EXTRACTION THERE IS NO WRONG HALF TO DELETE. <<

    The failure mode is removed STRUCTURALLY rather than warned about. A lane that misreads the
    spec, or greps by filename, still cannot destroy this control -- it is no longer in the file
    being deleted.

⛔ THE TRAP THIS MODULE WAS BUILT TO SURVIVE -- READ BEFORE EDITING THE TUPLES ⛔
    The retired `RETRACTED_20260709_*` tuples were **BYTE-IDENTICAL** to the live tuples below
    (verified independently by 0.8.0_AE_CloudComp~A, 1.0.0_SA_CTO and 1.0.0_SA_CTO~Z, 2026-07-25).
    So the dead governance set and this LIVE safety set are indistinguishable BY VALUE and
    separable ONLY BY IDENTIFIER NAME.

      **KEY EVERY DELETION ON THE SYMBOL NAME. NEVER ON THE PATH LITERALS.**

    A sweep driven by `grep -r 'data/black_diamond/'` or `'opal-data-bd'` cannot tell the retracted
    set from this one. It removes both, AND IT LOOKS LIKE IT WORKED. The path literals below are
    LOAD-BEARING; they are not leftovers of the retracted hold.

LOAD-BEARING SECURITY LEAF. Imports ONLY the Python standard library (currently: nothing at all
beyond __future__) so it can NEVER fail to import or be perturbed by a dependency change. Asserted
by tests/test_prod_write_guard.py via an ast check over this module's own import nodes -- the same
invariant `sovereign_held.py` carried. DO NOT add a non-stdlib import.

The predicates are PURE STRING checks -- they NEVER open a file.

Consumers: compproof/tool_probe.py (_assert_scratch_in_scope + the IAM fixture ARN check + the kuzu
query guard) and compproof/tool_corpus.py (assert_sovereign_safe, which fails the corpus LOAD).
"""

from __future__ import annotations

# ---- PROD-TARGET SAFETY: NOT governance, NOT retracted, UNCHANGED IN FORCE. ----
# Values moved VERBATIM from sovereign_held.py (GOVRIP step 1). See the byte-identity trap above:
# do not "clean these up" by matching them against anything found elsewhere in the repo.
PROD_WRITE_FORBIDDEN_PATHS = (
    "data/black_diamond/",
    "data/canonical/schwab/silver/",
    "schwab/silver/",
)
PROD_WRITE_FORBIDDEN_BUCKETS = (
    "opal-data-bd",
    "opal-data-schwab",
)


def _path_matches(path, markers) -> bool:
    """Substring match of `path` against `markers`. PURE string check -- never opens a file.

    COPY (not a shared import) of the sovereign_held helper, deliberately: this leaf must not
    depend on the module being deleted, nor on any module that could later grow a dependency.
    """
    if not path or not markers:
        return False
    s = str(path).replace("\\", "/")
    return any(m in s for m in markers)


def _bucket_matches(bucket, prefixes) -> bool:
    """Family match: exact | '<p>-*' | '<p>/*' -- so opal-data-bdx does NOT match (a distinct bucket),
    but opal-data-bd, opal-data-bd-raw and opal-data-bd/key DO. Accepts an s3://bucket[/key], an
    arn:aws:s3:::bucket[/key] (S3 resource ARN -- no region/account), or a bare bucket[/key]. The ARN
    form is REQUIRED: extract_iam / comp-iam / any IAM-resource caller passes an S3 ARN, and without
    this strip a bd ARN read as not-matching (a safety hole; CTO 2026-07-12).

    COPY (not a shared import) of the sovereign_held helper -- see _path_matches.
    """
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


def is_prod_write_forbidden(target) -> bool:
    """PROD-WRITE SAFETY predicate -- IN FORCE, never retracted, not governance.

    NAME NOTE: named PROD_WRITE_* per the CTO R7 ruling. The semantics are slightly BROADER than
    "write": it also guards an IAM fixture's simulate targets (role_arn / held_resource), which are
    not writes. The ruled name is kept anyway -- a spec name is a coordination contract, and an
    unflagged rename here made a reviewer's positive control return a false ABSENT (2026-07-22).
    The GOVRIP extraction likewise changed the FILE only, never this symbol.

    True if `target` names a production bd/schwab path OR bucket, in any of the accepted forms
    (bare path, bucket, bucket/key, s3://..., arn:aws:s3:::...). An automated compproof probe must
    never carry such a target in its run-argv, scratch URI, or IAM fixture ARN: a recurring probe
    would touch production on every re-run. Checks BOTH the path and bucket sets because a probe
    target can be either shape, which is why the original callers had to OR two predicates."""
    return (_path_matches(target, PROD_WRITE_FORBIDDEN_PATHS)
            or _bucket_matches(target, PROD_WRITE_FORBIDDEN_BUCKETS))
