"""NFRA_COMPIAM_RESOURCE -- comp-iam must compare the RESOURCE, not just the ACTION.

THE DEFECT (2026-07-09, CTO 1.0.0_SA_CTO):
    comp-iam printed `s3:GetObject [GRANTED]` for mdpf-daily-trigger's
    head_object against opal-data-portal-v2, while
    `aws iam simulate-principal-policy` returned implicitDeny for the same key.
    `IamRole.grants()` matched the ACTION NAME and returned on the first hit; it
    never read `stmt.resources`. `Operation` had no resource field at all.

    The sharpest statement of it -- comp-iam's output did not change when the
    truth changed:

                        real portal-v2 grant   simulate       comp-iam
        before ed415e268   none                 implicitDeny   GRANTED
        after  (HEAD)      aggregate_aua/*      allowed        GRANTED

    A verdict independent of the property it claims to check. `never-fires` and
    `always-fires` are the same defect; this one was always-fires-GREEN.

WHAT THIS FILE ENFORCES (CTO: "both rails or it does not land"):
    NEGATIVE control -- an assertion that has never failed has never been tested.
      * wrong bucket entirely            -> must RED
      * SAME bucket, WRONG key prefix    -> must RED   <- the sharper rail. A
        bucket-only comparison passes the wrong-bucket test and still cannot see
        a mis-scoped prefix: the same defect one level down, shipping wearing a
        passing test.
      * time-travel to the pre-fix policy, using the REAL call site whose Key is
        a runtime variable -> must RED via bucket-level containment. This is the
        regression test for the original incident: had the tool behaved this way
        on 2026-06-29 it would have caught the permanent silent DEFER.
    POSITIVE control -- proves the checker can still say yes.
      * opal-data-inf/gold/meta/pipeline-complete.json -> must stay GRANTED.
    HONESTY control -- a tool that cannot state what it could not check has not
    checked.
      * a runtime-computed key inside a HELD bucket -> UNRESOLVABLE, never GRANTED.
      * a Resource:'*' role -> GRANTED-BROAD, never a silent GRANTED.

SOUNDNESS NOTE (the trap this file also guards):
    When the call's ARN is a PATTERN (we substituted '*' for a runtime segment),
    "no statement matched" is NOT evidence of absence -- the real key may land
    inside a granted prefix. Only BUCKET-LEVEL absence is a sound definitive
    claim there. Trading the false negative for a false positive would be the
    same failure wearing the opposite sign.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest

_GRAPH_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_GRAPH_DIR))

# CVO P2 (2026-07-10): the estate-reading tests called build_iam_report(Path('.')) --
# they read the Terraform tree from the CURRENT WORKING DIRECTORY. CVO's unmutated
# scratch copy went RED before a single mutation was applied; an integration test in a
# unit test's clothes. Anchor to the repo, not to wherever pytest was invoked.
_WORKSPACE_ROOT = _GRAPH_DIR.parent.parent.parent   # org/modules/graph -> repo root

import extract_iam as E  # noqa: E402


# ---------------------------------------------------------------------------
# A SECOND BLOCK-FINDER (CVO, 2026-07-10).
#
# The census recount used to re-derive its total with `E._TF_POLICY_RESOURCE` --
# the module's OWN regex. That is independent of the COUNTER and NOT independent
# of the PARSER. It would catch an attach/drop accounting bug and could NOT catch
# a regex that misses blocks entirely -- which is exactly the roleref hole that
# silently dropped 26 of 330 blocks, two of them NEVER#1's cross-firm Deny belts.
# *The test could not detect the next defect of the class it was written to close.*
#
# CVO: "an instrument's own perception is the last thing it occurs to you to doubt.
# A test inherits every blindness of the instrument it imports."
#
# So: a deliberately DIFFERENT implementation. Line-oriented, explicit alternation,
# comment-aware. It does not import a single regex from extract_iam.
_RE_BLOCK_DECL = re.compile(
    r'^\s*resource\s+"(?:aws_iam_role_policy|aws_iam_policy)"\s+"[A-Za-z0-9_-]+"\s*\{')


def _count_policy_blocks(hcl: str) -> int:
    """Count real (non-commented) IAM policy resource declarations, line by line."""
    n = 0
    for line in hcl.splitlines():
        s = line.lstrip()
        if s.startswith('#') or s.startswith('//'):
            continue
        if _RE_BLOCK_DECL.match(line):
            n += 1
    return n


def _stmt(actions, resources, effect="Allow", condition=""):
    return E.IamStatement(
        effect=effect, actions=list(actions), resources=list(resources),
        source_file="fixture", condition=condition,
    )


# The mdpf-daily-trigger role, as Terraform declared it AFTER ed415e268 landed
# the PlatinumRollSourceRead grant. Trimmed to the s3 statements under test.
def _role_after_fix() -> E.IamRole:
    return E.IamRole(
        role_name="mdpf-daily-trigger-lambda-role",
        tf_resource="mdpf_trigger_lambda",
        statements=[
            _stmt(["s3:GetObject"],
                  ["arn:aws:s3:::opal-data-inf/gold/meta/pipeline-complete.json"]),
            _stmt(["s3:GetObject"],
                  ["arn:aws:s3:::opal-data-bd/silver/allocations/*",
                   "arn:aws:s3:::opal-data-bd/silver/fees/*"]),
            _stmt(["s3:ListBucket"], ["arn:aws:s3:::opal-data-bd"]),
            _stmt(["s3:GetObject"],
                  ["arn:aws:s3:::opal-data-portal-v2/platinum/mdpf/aggregate_aua/*"]),
        ],
    )


# The SAME role as it stood at ed415e268~1: no portal-v2 Resource anywhere.
def _role_before_fix() -> E.IamRole:
    r = _role_after_fix()
    r.statements = [s for s in r.statements
                    if not any("portal-v2" in x for x in s.resources)]
    return r


_AGG_KEY = "arn:aws:s3:::opal-data-portal-v2/platinum/mdpf/aggregate_aua/2026-07-06.json"
# What the extractor actually resolves for
#   s3.head_object(Bucket=PLATINUM_BUCKET, Key=f"{PLATINUM_AGG_PREFIX}/{as_of}.json")
# `as_of` is a runtime value -> '*'. exact=False.
_AGG_PATTERN = "arn:aws:s3:::opal-data-portal-v2/platinum/mdpf/aggregate_aua/*.json"
_INF_SENTINEL = "arn:aws:s3:::opal-data-inf/gold/meta/pipeline-complete.json"


# ---------------------------------------------------------------------------
# NEGATIVE CONTROLS -- these MUST RED. An assertion that never fails is untested.
# ---------------------------------------------------------------------------

def test_negative_control_wrong_bucket_reds():
    """A bucket the role does not hold at all. Table stakes."""
    v, _s, note = _role_after_fix().resource_verdict(
        "s3:GetObject", "arn:aws:s3:::opal-data-cot/gold/x.json", exact=True)
    assert v == E.V_UNGRANTED_RESOURCE, f"wrong-bucket must RED, got {v} ({note})"


def test_negative_control_same_bucket_wrong_prefix_reds():
    """THE SHARPER RAIL. portal-v2 IS held -- but only under platinum/mdpf/aggregate_aua/*.

    A bucket-only comparison would call this GRANTED and ship wearing a passing
    wrong-bucket test.
    """
    v, _s, note = _role_after_fix().resource_verdict(
        "s3:GetObject", "arn:aws:s3:::opal-data-portal-v2/gold/not-granted/x.json",
        exact=True)
    assert v == E.V_UNGRANTED_RESOURCE, \
        f"same-bucket/wrong-prefix must RED, got {v} ({note})"


def test_time_travel_the_original_incident_reds():
    """The regression test for the incident itself.

    The REAL call site, whose Key is a runtime variable (exact=False), against
    the policy as it stood before ed415e268. Must RED via bucket-level
    containment -- WITHOUT ever resolving the key.
    """
    v, _s, note = _role_before_fix().resource_verdict(
        "s3:GetObject", _AGG_PATTERN, exact=False)
    assert v == E.V_UNGRANTED_RESOURCE, \
        f"pre-fix policy must RED on the real call, got {v} ({note})"
    assert "opal-data-portal-v2" in note and "NO Allow statement" in note


def test_exact_key_pre_fix_reds():
    """The exact key CTO simulated as implicitDeny."""
    v, _s, _n = _role_before_fix().resource_verdict("s3:GetObject", _AGG_KEY, exact=True)
    assert v == E.V_UNGRANTED_RESOURCE


# ---------------------------------------------------------------------------
# POSITIVE CONTROLS -- the checker must still be able to say yes.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("role_fn", [_role_after_fix, _role_before_fix],
                         ids=["after-fix", "before-fix"])
def test_positive_control_inf_sentinel_stays_granted(role_fn):
    """`opal-data-inf/gold/meta/pipeline-complete.json` is GRANTED under BOTH
    policies. CTO's control that proves the simulator -- and now the tool -- can
    say yes. A checker that REDs everything is as useless as one that GREENs it.
    """
    v, _s, note = role_fn().resource_verdict("s3:GetObject", _INF_SENTINEL, exact=True)
    assert v == E.V_GRANTED, f"positive control must stay GRANTED, got {v} ({note})"


def test_granted_after_fix_on_the_real_call():
    """At HEAD the grant exists; the real (pattern) call must GREEN.

    The policy `aggregate_aua/*` covers the whole set `aggregate_aua/*.json`.
    """
    v, _s, note = _role_after_fix().resource_verdict(
        "s3:GetObject", _AGG_PATTERN, exact=False)
    assert v == E.V_GRANTED, f"post-fix real call must GREEN, got {v} ({note})"


def test_the_invariance_is_gone():
    """The defect, stated as a property: the verdict must CHANGE when the truth
    changes. Before the fix this assertion was impossible to satisfy -- grants()
    returned GRANTED for both policies."""
    before = _role_before_fix().resource_verdict("s3:GetObject", _AGG_PATTERN, False)[0]
    after = _role_after_fix().resource_verdict("s3:GetObject", _AGG_PATTERN, False)[0]
    assert before != after, "comp-iam's output must not be independent of the grant"
    assert (before, after) == (E.V_UNGRANTED_RESOURCE, E.V_GRANTED)


# ---------------------------------------------------------------------------
# HONESTY CONTROLS -- never fold "could not check" into GRANTED.
# ---------------------------------------------------------------------------

def test_runtime_key_in_a_held_bucket_is_unresolvable_not_granted():
    """opal-data-bd IS held, but only under silver/allocations/* and silver/fees/*.
    A runtime key could land inside or outside. The honest answer is
    UNRESOLVABLE -- not GRANTED (false clear) and not RED (false accusation).
    """
    v, _s, note = _role_after_fix().resource_verdict(
        "s3:GetObject", "arn:aws:s3:::opal-data-bd/*", exact=False)
    assert v == E.V_UNRESOLVABLE, f"runtime key in held bucket -> UNRESOLVABLE, got {v}"
    assert "cannot confirm" in note


def test_unresolvable_call_resource_is_never_granted():
    v, _s, _n = _role_after_fix().resource_verdict("s3:GetObject", None, exact=False)
    assert v == E.V_UNRESOLVABLE


def test_wildcard_role_is_granted_broad_not_granted():
    """A Resource:'*' role cannot be falsified by any resource check. It must be
    surfaced as GRANTED-BROAD (NOT CLEARED), never silently folded into GRANTED.
    """
    role = E.IamRole("wild", "wild", statements=[_stmt(["s3:*"], ["*"])])
    v, _s, note = role.resource_verdict("s3:GetObject", _AGG_KEY, exact=True)
    assert v == E.V_GRANTED_BROAD
    assert "no resource check can falsify" in note


# ---------------------------------------------------------------------------
# META-CONTROL -- prove these tests would have FAILED against the old logic.
# "An assertion that has never failed has never been tested." A negative control
# that passes under the DEFECT is not a control at all.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "arn,exact",
    [(_AGG_KEY, True),                                              # exact key
     (_AGG_PATTERN, False),                                         # the real call
     ("arn:aws:s3:::opal-data-cot/gold/x.json", True),              # wrong bucket
     ("arn:aws:s3:::opal-data-portal-v2/gold/not-granted/x.json", True)],  # wrong prefix
    ids=["exact-key", "real-call", "wrong-bucket", "wrong-prefix"])
def test_the_old_action_only_logic_would_have_passed_every_negative_control(arn, exact):
    """`grants()` -- the shipped logic until 2026-07-10 -- returns True for ALL of
    these, including a bucket the role has never heard of. That is the defect,
    pinned as an executable fact: the action is held, so the action-only checker
    says GRANTED, and no negative control could ever have fired.

    `resource_verdict()` must disagree with it on every one of them.
    """
    before, after = _role_before_fix(), _role_after_fix()

    # The old checker: action-only, ignores the resource entirely.
    assert before.grants("s3:GetObject") is True
    assert after.grants("s3:GetObject") is True

    # ...and it is INVARIANT: identical answer for a granted key and a wrong bucket.
    assert before.grants("s3:GetObject") == after.grants("s3:GetObject")

    # The new checker must not be GRANTED on any of these against the pre-fix policy.
    v, _s, _n = before.resource_verdict("s3:GetObject", arn, exact)
    assert v != E.V_GRANTED, f"resource_verdict must not clear {arn}"
    assert v in (E.V_UNGRANTED_RESOURCE, E.V_UNRESOLVABLE)


def test_unparseable_resource_is_unresolvable_not_a_false_accusation():
    """An Allow statement whose Resource the parser could not see (an unquoted TF
    reference, e.g. `Resource = aws_sqs_queue.x.arn`) must degrade to
    UNRESOLVABLE. Absence of evidence is not evidence of absence -- reading it as
    'no coverage' would emit a confident false accusation.
    """
    role = E.IamRole("r", "r", statements=[_stmt(["sqs:SendMessage"], [])])
    v, _s, _n = role.resource_verdict("sqs:SendMessage", "arn:aws:sqs:us-east-1:1:q", True)
    assert v == E.V_UNRESOLVABLE


def test_unresolved_tf_interpolation_is_indeterminate():
    """`${aws_instance.x.id}` cannot be compared. Treating it as a match would be
    the original defect one level down."""
    assert E._iam_resource_matches(
        "arn:aws:ec2:us-east-1:1:instance/${aws_instance.x.id}",
        "arn:aws:ec2:us-east-1:1:instance/i-abc") is None


# ---------------------------------------------------------------------------
# CASE SENSITIVITY (CVO P0) -- a false GRANT suppresses UNGRANTED-RESOURCE.
#
# `_iam_resource_matches` carried `re.IGNORECASE`. S3 object keys are CASE-SENSITIVE
# and IAM matches the resource-id verbatim. EXERCISED live against lambda-execution-role
# (grant: arn:aws:s3:::opal-data-pm/*/processed/*):
#     .../PFDE/processed/x.json -> allowed
#     .../PFDE/PROCESSED/x.json -> implicitDeny
#     .../PFDE/Processed/x.json -> implicitDeny
# Not inferred from AWS docs -- run with simulate-principal-policy, 2026-07-10.
#
# The defect this tool fixes (output independent of the RESOURCE) had survived in the
# very same expression as output independent of the resource's CASE.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("policy_res,arn", [
    ("arn:aws:s3:::opal-data-bd/Public/*",   "arn:aws:s3:::opal-data-bd/public/secret.json"),
    ("arn:aws:s3:::opal-data-bd/PUBLIC/*",   "arn:aws:s3:::opal-data-bd/public/secret.json"),
    ("arn:aws:s3:::opal-data-bd/platinum/*", "arn:aws:s3:::opal-data-bd/PLATINUM/x.json"),
])
def test_key_matching_is_case_sensitive(policy_res, arn):
    """Each of these returned True (a FALSE GRANT) under re.IGNORECASE."""
    assert _iam_no_match(policy_res, arn), \
        f"{policy_res} must NOT cover {arn} -- S3 keys are case-sensitive"


def _iam_no_match(policy_res, arn):
    return E._iam_resource_matches(policy_res, arn) is False


def test_case_sensitivity_does_not_break_the_exact_match():
    """The positive rail: identical case still GRANTS. A checker that REDs everything
    is as useless as one that GREENs everything."""
    assert E._iam_resource_matches(
        "arn:aws:s3:::opal-data-pm/*/processed/*",
        "arn:aws:s3:::opal-data-pm/PFDE/processed/x.json") is True


def test_a_case_mismatched_key_reds_end_to_end():
    """Through resource_verdict, not just the matcher. Live says implicitDeny."""
    v, _s, _n = _role_pm().resource_verdict(
        's3:DeleteObject', 'arn:aws:s3:::opal-data-pm/PFDE/PROCESSED/x.json', exact=True)
    assert v == E.V_UNGRANTED_RESOURCE


# ---------------------------------------------------------------------------
# MY OWN UNCERTAINTY (CVO P1) -- the tri-state must apply to BOTH sides.
# ---------------------------------------------------------------------------

def test_the_exact_flag_is_never_trusted_over_the_ARN_itself():
    """CVO P1a. `exact` was a caller-supplied flag, and the invariant
    "a '*' in the ARN implies exact is False" was ASSUMED, never asserted.

    A literal `Key="prefix/*"` resolves exact=True with a '*' in the ARN, and the
    exact branch would emit a confident UNGRANTED-RESOURCE against a PATTERN -- a
    false accusation reading as "you are missing a permission," and someone grants a
    permission that was never needed. The tri-state was applied to the POLICY's
    uncertainty and not to the parser's own.
    """
    role = _role_after_fix()
    for claimed_exact in (True, False):
        v, _s, _n = role.resource_verdict(
            's3:GetObject', 'arn:aws:s3:::*/gold/meta.json', exact=claimed_exact)
        assert v == E.V_UNRESOLVABLE, \
            f"a '*' in the ARN must degrade regardless of exact={claimed_exact}"
    # ...and a genuinely exact ARN still reaches a definitive verdict.
    v, _s, _n = role.resource_verdict(
        's3:GetObject', 'arn:aws:s3:::opal-data-cot/gold/x.json', exact=True)
    assert v == E.V_UNGRANTED_RESOURCE


def test_an_unresolved_BUCKET_segment_is_unresolvable_not_a_false_accusation():
    """`Bucket=f"{env}-data"` yields `arn:aws:s3:::*-data/...`. The '*' is there because
    THIS parser could not resolve it -- not because the call spans buckets. Claiming
    bucket-level absence would emit "you are missing a permission" and someone would add
    a grant that was never needed: the same defect, inverted into over-permission.
    """
    v, _s, note = _role_after_fix().resource_verdict(
        's3:GetObject', 'arn:aws:s3:::*-data/gold/x.json', exact=False)
    assert v == E.V_UNRESOLVABLE, f"unresolved bucket must not accuse; got {v}"
    assert 'not statically resolvable' in note


def test_no_action_match_is_ungranted():
    v, _s, _n = _role_after_fix().resource_verdict("s3:PutObject", _AGG_KEY, exact=True)
    assert v == E.V_UNGRANTED


# ---------------------------------------------------------------------------
# THIRD RAIL (NFRA_COMPIAM_ROLEREF) -- the role-reference scan hole.
#
# comp-iam's sole estate-wide flag was `opal-pm-optimization-loader`
# s3:DeleteObject on opal-data-pm. Live `simulate-principal-policy` said ALLOWED.
# The first explanation offered was "a console-managed policy TF does not model"
# -- true in general, FALSE here. `OpalDataPMCacheBustAccess` IS Terraform-declared
# (portfolio-management/main.tf:323), inside a scanned tree. It attaches with
# `role = "lambda-execution-role"` -- a LITERAL name, not `aws_iam_role.X.name` --
# and the parser dropped the whole block on a bare `continue`. 26 of 330 blocks.
#
# A true explanation attached to a symptom it did not produce is worse than no
# explanation: it teaches the reader to dismiss the real bug. (Rule 22.)
# ---------------------------------------------------------------------------

def _role_pm() -> E.IamRole:
    """lambda-execution-role, both DeleteObject grants, as the FIXED parser sees them."""
    return E.IamRole(
        role_name="lambda-execution-role", tf_resource="lambda_execution",
        statements=[
            # shared-infra/lambda-execution-role.tf -- attached by TF REFERENCE
            _stmt(["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
                  ["arn:aws:s3:::opal-data-portal-v2/portfolio-management/*"]),
            # portfolio-management/main.tf:323 -- attached by LITERAL NAME.
            # Dropped entirely before the roleref fix.
            _stmt(["s3:DeleteObject"], ["arn:aws:s3:::opal-data-pm/*/processed/*"]),
        ],
    )


def test_roleref_the_literal_attached_policy_makes_the_flag_green():
    """The exact call comp-iam wrongly flagged. Live says allowed; the fixed tool
    must agree. Cross-plane: DESIRED == APPLIED."""
    v, _s, note = _role_pm().resource_verdict(
        "s3:DeleteObject", "arn:aws:s3:::opal-data-pm/PFDE/processed/20260204.json",
        exact=True)
    assert v == E.V_GRANTED, f"live simulate says allowed; comp-iam must too ({v}: {note})"


def test_roleref_negative_rail_raw_prefix_still_reds():
    """The grant is `opal-data-pm/*/processed/*`. A raw upload is NOT in the cache
    prefix and live returns implicitDeny. The fix must not GREEN the whole bucket --
    that would trade a false positive for a false negative."""
    v, _s, _n = _role_pm().resource_verdict(
        "s3:DeleteObject", "arn:aws:s3:::opal-data-pm/PFDE/raw/x.csv", exact=True)
    assert v == E.V_UNGRANTED_RESOURCE


def test_roleref_dropping_the_literal_policy_reproduces_the_false_positive():
    """Regression pin: with the literal-attached block absent -- the pre-fix parser --
    the call REDs. If anyone reverts _TF_ROLE_LITERAL, this test names the defect."""
    role = _role_pm()
    role.statements = [s for s in role.statements
                       if not any("opal-data-pm" in r for r in s.resources)]
    v, _s, note = role.resource_verdict(
        "s3:DeleteObject", "arn:aws:s3:::opal-data-pm/PFDE/processed/20260204.json",
        exact=True)
    assert v == E.V_UNGRANTED_RESOURCE
    assert "other resources" in note


def test_roleref_literal_regex_matches_literal_and_refuses_interpolation():
    assert E._TF_ROLE_LITERAL.search('role = "lambda-execution-role"').group(1) \
        == "lambda-execution-role"
    # `role = "${var.name}"` must NOT resolve to a literal -- it would attach a
    # policy to a role named '${var.name}'.
    assert E._TF_ROLE_LITERAL.search('role = "${var.role_name}"') is None
    # A TF reference is handled by _TF_ROLE_REF, not by the literal path.
    assert E._TF_ROLE_LITERAL.search('role = aws_iam_role.x.name') is None


def test_roleref_parser_attaches_the_literal_policy_from_the_REAL_tree():
    """END-TO-END on the real Terraform, not a hand-built role.

    Found by mutation-testing my own suite: disabling `_TF_ROLE_LITERAL` killed only
    the regex unit test, because every other roleref test constructs its statements
    by hand and never exercises the parser. A control that cannot die when the code
    it guards is reverted is not a control.

    This one dies. It reads infra/aws/terraform/portfolio-management/main.tf:323
    through the real `_parse_terraform_iam` and demands the literal-attached policy
    be present on the role.
    """
    _profiles, roles, _gaps = E.build_iam_report(_WORKSPACE_ROOT)
    role = roles['lambda-execution-role']
    granted = [r for s in role.statements
               if s.effect.lower() == 'allow'
               and any(a.lower() == 's3:deleteobject' for a in s.actions)
               for r in s.resources]
    assert 'arn:aws:s3:::opal-data-pm/*/processed/*' in granted, \
        f"OpalDataPMCacheBustAccess not attached (role = \"literal\" dropped?); saw {granted}"
    # ...and the call comp-iam once wrongly flagged now agrees with live `simulate`.
    v, _s, _n = role.resource_verdict(
        's3:DeleteObject', 'arn:aws:s3:::opal-data-pm/PFDE/processed/20260204.json',
        exact=True)
    assert v == E.V_GRANTED


def test_drop_reason_names_the_cause_and_never_lumps():
    roles = {'known-role': object()}
    assert 'for_each' in E._drop_reason('role = each.value', None, roles)
    assert 'interpolation' in E._drop_reason('role = "${var.x}"', None, roles)
    assert 'no aws_iam_role resource' in E._drop_reason(
        'role = "ghost-role"', 'ghost-role', roles)
    assert 'var/module/local' in E._drop_reason('role = module.x.role_name', None, roles)


def test_deny_overlay_incompleteness_is_counted_and_never_silent():
    """CTO arch-gate 2026-07-10: a tool that cannot see a Deny must SAY SO.

    NEVER#1's runtime limb is an IAM Deny. comp-iam's Deny overlay exists so an
    explicit Deny never reads as GRANTED -- and it cannot warn on a Deny it never
    parsed. Silence must not read as allowed.

    Written to stay true AFTER `for_each` resolution lands: it pins the INVARIANT
    (every unparsed Deny is enumerated with a named reason), not today's count of 2.
    """
    _profiles, roles, _gaps = E.build_iam_report(_WORKSPACE_ROOT)
    st = E._ATTACH_STATS

    # R2 (COO, 2026-07-10). The assertion that used to live here was
    #     assert len(st['deny_detail']) == st['deny_unparsed']
    # `deny_unparsed += 1` and `deny_detail.append(...)` are unconditionally paired in
    # the same branch, so it compared a counter to the length of the list that produced
    # it. IT COULD NOT FAIL -- the identical vacuous shape CVO found in my attach-census
    # test, reproduced by me in the very test written to fix that defect. A control that
    # cannot fail is not a control, and knowing the name of the defect is not immunity.
    #
    # Re-derive the count from the Terraform, by a SEPARATE walk that does not read
    # _ATTACH_STATS at all: a block is unattachable iff neither role-ref form resolves
    # to a known role; count the Deny statements inside those blocks.
    independent_denies = 0
    for root in E.TF_SCAN_ROOTS:
        rp = _WORKSPACE_ROOT / root
        if not rp.exists():
            continue
        for f in rp.rglob('*.tf'):
            if '.terraform' in f.parts:
                continue
            content = f.read_text(encoding='utf-8', errors='replace')
            for m in E._TF_POLICY_RESOURCE.finditer(content):
                block = E._extract_tf_block(content, m.start())
                ref = E._TF_ROLE_REF.search(block)
                lit = E._TF_ROLE_LITERAL.search(block)
                resolvable = bool(ref) or (lit is not None and lit.group(1) in roles)
                if resolvable:
                    continue
                for s in E._parse_iam_statements(block, str(f)):
                    if s.effect.lower() == 'deny':
                        independent_denies += 1

    assert st['deny_unparsed'] == independent_denies, (
        f"deny census {st['deny_unparsed']} disagrees with an independent walk "
        f"({independent_denies}) -- the counter and the Terraform do not agree")
    # Assert the LIST against the independent truth, not against the counter that
    # produced it (CVO: delete the tautology so no reader mistakes it for the assertion).
    assert len(st['deny_detail']) == independent_denies

    if st['deny_unparsed']:
        assert st['deny_reasons'], "an unparsed Deny must carry a named reason"
        assert all(r.strip() for r in st['deny_reasons'])
        # CONTENT, not count. When for_each resolution lands this goes to 0 and the
        # implication holds vacuously -- by design.
        assert any('cross-firm' in d for d in st['deny_detail'])


def test_attach_census_closes_against_an_INDEPENDENT_recount():
    """The census must close against a count this module did not produce.

    CVO P1 (2026-07-10): the original assertion here was
        assert len(st['dropped_detail']) == st['dropped']
    `dropped += 1` and `dropped_detail.append(...)` are unconditionally paired in the
    same branch, so it compared a counter to the length of the list that produced it.
    IT COULD NOT FAIL. A vacuous control, inside the suite written to kill vacuous
    controls -- and I wrote it while telling CVO to "check the contents, not the count."

    So: re-derive the block total independently, by scanning the same trees with the
    module's own block regex, and demand attached + dropped == that total.
    """
    E.build_iam_report(_WORKSPACE_ROOT)
    st = E._ATTACH_STATS

    tf_files = 0
    independent_blocks = 0
    for root in E.TF_SCAN_ROOTS:
        rp = _WORKSPACE_ROOT / root
        if not rp.exists():
            continue
        for f in rp.rglob('*.tf'):
            if '.terraform' in f.parts:
                continue
            tf_files += 1
            independent_blocks += _count_policy_blocks(
                f.read_text(encoding='utf-8', errors='replace'))

    assert tf_files == st['tf_files'], "scanned-file count disagrees with an independent walk"
    # The census must close over ALL THREE worlds. A standalone aws_iam_policy has no
    # `role =` by design; calling it an unattachable role-policy prints a reason that is
    # false for it.
    total = st['attached'] + st['dropped'] + st['standalone']
    assert total == independent_blocks, (
        f"census does not close: attached {st['attached']} + dropped {st['dropped']} "
        f"+ standalone {st['standalone']} = {total} != {independent_blocks} blocks")
    assert st['attached'] > 0 and independent_blocks > 0, "a clean bill from an empty set"


# A FROZEN FIXTURE with a HAND-COUNTED total. Neither the parser's regex nor the
# test's own scanner can define the truth here -- a human counted it.
#   2 x aws_iam_role_policy  (one TF-ref, one literal-name)
#   1 x aws_iam_policy       (standalone -- no `role =` BY DESIGN)
#   1 x commented-out ghost  (MUST NOT count)
_FROZEN_HCL = '''
# resource "aws_iam_role_policy" "ghost" {
#   role = aws_iam_role.x.name
# }
resource "aws_iam_role_policy" "a" {
  role   = aws_iam_role.x.name
  policy = jsonencode({ Statement = [{ Effect = "Allow", Action = ["s3:GetObject"], Resource = "arn:aws:s3:::b/*" }] })
}
resource "aws_iam_role_policy" "b" {
  role   = "lambda-execution-role"
  policy = jsonencode({ Statement = [{ Effect = "Deny", Action = ["s3:*"], Resource = "*" }] })
}
resource "aws_iam_policy" "standalone" {
  policy = jsonencode({ Statement = [{ Effect = "Allow", Action = ["s3:PutObject"], Resource = "arn:aws:s3:::b/*" }] })
}
resource "aws_iam_role" "x" { name = "some-role" }
'''
_FROZEN_TRUE_BLOCKS = 3   # hand-counted: a, b, standalone. NOT ghost.


def test_the_block_finder_ignores_commented_out_blocks():
    """Ground truth is hand-counted, so neither implementation can define it.

    Before the comment mask, `_TF_POLICY_RESOURCE` matched
    `# resource "aws_iam_role_policy" "ghost" {` and inflated the census by a policy
    that does not exist. Latent estate-wide (0 hits today) and INVISIBLE, because the
    recount used the same regex and inflated identically.
    """
    assert _count_policy_blocks(_FROZEN_HCL) == _FROZEN_TRUE_BLOCKS

    masked = E._mask_hcl_comments(_FROZEN_HCL)
    assert len(masked) == len(_FROZEN_HCL), "the mask must preserve offsets"
    assert len(E._TF_POLICY_RESOURCE.findall(masked)) == _FROZEN_TRUE_BLOCKS, \
        "the parser counts a commented-out block"

    # ...and the unmasked regex still would. That is the defect, pinned.
    assert len(E._TF_POLICY_RESOURCE.findall(_FROZEN_HCL)) == _FROZEN_TRUE_BLOCKS + 1


def test_standalone_policy_is_not_an_unattachable_role_policy():
    """`aws_iam_policy` has no `role =` BY DESIGN. Counting it as a drop, with the
    reason 'unresolvable role ref', is a false reason attached to a real count --
    two different worlds collapsed into one number. 5 of 330 estate-wide."""
    assert E._TF_STANDALONE_POLICY.search('resource "aws_iam_policy" "p" {')
    assert not E._TF_STANDALONE_POLICY.search('resource "aws_iam_role_policy" "p" {')

    E.build_iam_report(_WORKSPACE_ROOT)
    st = E._ATTACH_STATS
    assert st['standalone'] > 0, "the estate has standalone aws_iam_policy blocks"
    # every dropped entry must name a role-ref problem, never a standalone policy
    assert not any('aws_iam_policy' in d for d in st['dropped_detail'])


def test_the_never1_cross_firm_deny_belts_are_named_in_the_census():
    """CONTENT, not count. The highest-stakes item in the whole finding.

    CVO P1: "no test asserts that the NEVER#1 cross-firm Deny belts are among the
    dropped -- the highest-stakes content in your entire finding is asserted NOWHERE."
    Correct. comp-iam cannot see these two Deny statements; NEVER#1's runtime limb IS
    an IAM Deny, and silence about a Deny reads as allowed.

    Stays true after `for_each` resolution lands: once comp-iam can parse them they
    leave the dropped set AND leave deny_detail, and both halves of the implication
    below hold vacuously.
    """
    E.build_iam_report(_WORKSPACE_ROOT)
    st = E._ATTACH_STATS
    dropped_blob = ' '.join(st['dropped_detail'])
    deny_blob = ' '.join(st['deny_detail'])

    # An unparsed cross-firm Deny must appear in BOTH the drop census and the deny census.
    if 'cross-firm' in dropped_blob:
        assert 'cross-firm' in deny_blob, \
            "a cross-firm belt was dropped but NOT counted as an unparsed Deny"
        assert st['deny_unparsed'] >= 1
        # ...and it must name WHY, not merely that.
        assert any('for_each' in r or 'var/module/local' in r for r in st['deny_reasons'])
    else:
        # for_each resolution landed: nothing unparsed may still be a cross-firm Deny.
        assert 'cross-firm' not in deny_blob

    # The policy that produced comp-iam's only false positive must NOT be in the drop
    # census any more -- it is the roleref fix, asserted by content.
    assert 'OpalDataPMCacheBustAccess' not in dropped_blob, \
        "the literal-attached policy is being dropped again"


# ---------------------------------------------------------------------------
# S3 ARN SHAPE -- object actions and bucket actions address DIFFERENT ARNs.
# ---------------------------------------------------------------------------

def test_listbucket_addresses_the_bucket_arn_not_the_object_arn():
    """`bucket/*` does NOT grant s3:ListBucket; the bucket ARN does. Collapsing
    the two ARN spaces is `action` for `resource` one level down."""
    role = _role_after_fix()
    v_ok, _s, _n = role.resource_verdict(
        "s3:ListBucket", "arn:aws:s3:::opal-data-bd", exact=True)
    assert v_ok == E.V_GRANTED
    # GetObject is granted on bd/silver/* but the BUCKET arn is not an object arn
    v_bad, _s, _n = role.resource_verdict(
        "s3:GetObject", "arn:aws:s3:::opal-data-bd", exact=True)
    assert v_bad == E.V_UNGRANTED_RESOURCE


# ---------------------------------------------------------------------------
# CALL-SITE RESOLUTION -- the extractor must learn what a call touches.
# ---------------------------------------------------------------------------

_SRC = '''
import os, boto3
s3 = boto3.client("s3")
PLATINUM_BUCKET = os.environ.get("PLATINUM_BUCKET", "opal-data-portal-v2")
PLATINUM_AGG_PREFIX = os.environ.get("PLATINUM_AGG_PREFIX", "platinum/mdpf/aggregate_aua")
INF_BUCKET = os.environ.get("INF_BUCKET", "opal-data-inf")
INF_SENTINEL_KEY = os.environ.get("INF_SENTINEL_KEY", "gold/meta/pipeline-complete.json")

def f(as_of, key):
    s3.head_object(Bucket=PLATINUM_BUCKET, Key=f"{PLATINUM_AGG_PREFIX}/{as_of}.json")
    s3.get_object(Bucket=INF_BUCKET, Key=INF_SENTINEL_KEY)
    s3.get_object(Bucket="opal-data-bd", Key=key)
    s3.list_objects_v2(Bucket=INF_BUCKET, Prefix="gold/")
'''


def _ops_by_line(src: str) -> dict[int, E.Operation]:
    return {op.line_number: op for op in E._scan_python_for_operations(src, "fixture.py")}


def test_extractor_resolves_env_default_constants_and_fstrings():
    ops = _ops_by_line(_SRC)
    head = next(o for o in ops.values() if "head_object" in o.source_pattern)
    assert head.resource_arn == _AGG_PATTERN
    assert head.resource_exact is False, "the {as_of} segment is a runtime value"


def test_extractor_resolves_a_fully_static_key_as_exact():
    ops = _ops_by_line(_SRC)
    got = next(o for o in ops.values()
               if "get_object" in o.source_pattern and o.resource_arn == _INF_SENTINEL)
    assert got.resource_exact is True


def test_extractor_marks_a_runtime_key_inexact():
    ops = _ops_by_line(_SRC)
    bd = next(o for o in ops.values() if o.resource_arn == "arn:aws:s3:::opal-data-bd/*")
    assert bd.resource_exact is False


def test_extractor_uses_the_bucket_arn_for_bucket_level_actions():
    ops = _ops_by_line(_SRC)
    lb = next(o for o in ops.values() if "list_objects_v2" in o.source_pattern)
    assert lb.resource_arn == "arn:aws:s3:::opal-data-inf", "ListBucket addresses the bucket ARN"
    assert lb.resource_exact is True


def test_copy_object_refuses_to_guess():
    """copy_object emits s3:GetObject, but GetObject addresses the SOURCE, not
    `Bucket=` (the destination). A confident wrong ARN is worse than none."""
    src = ('import boto3\ns3 = boto3.client("s3")\n'
           's3.copy_object(Bucket="dst", Key="k", CopySource="src/k")\n')
    op = next(iter(_ops_by_line(src).values()))
    assert op.resource_arn is None
    assert "ambiguous" in op.resource_expr


def test_multiline_call_still_finds_the_bucket():
    """Line-local regex would miss a Bucket= on the continuation line."""
    src = ('import boto3\ns3 = boto3.client("s3")\nB = "opal-data-inf"\n'
           's3.get_object(\n    Bucket=B,\n    Key="gold/x.json",\n)\n')
    op = next(iter(_ops_by_line(src).values()))
    assert op.resource_arn == "arn:aws:s3:::opal-data-inf/gold/x.json"
    assert op.resource_exact is True


def test_unresolvable_bucket_yields_no_arn_rather_than_a_guess():
    """`os.environ["X"]` has no literal default. Guessing would manufacture a
    confident wrong ARN."""
    src = ('import os, boto3\ns3 = boto3.client("s3")\nB = os.environ["MYSTERY"]\n'
           's3.get_object(Bucket=B, Key="k")\n')
    op = next(iter(_ops_by_line(src).values()))
    assert op.resource_arn is None
