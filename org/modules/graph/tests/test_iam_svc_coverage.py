"""NFRA_COMPIAM_SVCCOV -- the 13 used-but-unmodeled services now return REAL verdicts.

THE GAP (CTO campaign, 2026-07-11, Andrew-direct "get everything we can for comp-iam"):
    comp-iam's `_BOTO3_BY_SERVICE` registry modeled only 10 services. A boto3 client
    of any OTHER service produced a `<svc>:UNMODELED` coverage-unknown sentinel --
    comp-iam could not say GRANTED / UNGRANTED / UNGRANTED-RESOURCE at all. The
    trigger was an `ses:FromAddress` question comp-iam could not evaluate because
    `ses` was not modeled. The estate's used-but-unmodeled set was:
        ses, events, iam, logs, sts, sqs, rds, cloudtrail, ce, kms, ecs,
        apigateway, apigatewayv2.

WHAT THIS FILE ENFORCES:
    For each newly-modeled service, a representative estate call now:
      1. emits its GROUNDED IAM action (not a `<svc>:UNMODELED` sentinel), and
      2. reaches a REAL verdict -- GRANTED-BROAD when the action is held, UNGRANTED
         (via grants()) when it is not. A COVERAGE-UNKNOWN service could satisfy
         neither.

NON-VACUITY (an assertion that never fails has never been tested):
    * test_a_still_unmodeled_service_still_sentinels -- the instrument's own control:
      a service we did NOT model (athena) must STILL sentinel. If it does not, the
      whole suite is vacuous (it would pass even if the maps did nothing).
    * test_reverting_a_map_reintroduces_the_sentinel -- executable mutation: pop
      `ses` from the registry in-process and the exact snippet that GREENs must
      revert to `ses:UNMODELED`. Proves the passing assertions are COUPLED to the
      map, not to something incidental.

A WRONG action map is worse than COVERAGE-UNKNOWN: a false GRANT suppresses
UNGRANTED-RESOURCE, the verdict this tool exists to emit. Every action below is
grounded in a cited estate call site (see the map comments in extract_iam.py).
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_GRAPH_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_GRAPH_DIR))

import extract_iam as E  # noqa: E402


# (label, source snippet creating a client + calling ONE grounded method, expected action)
_CASES = [
    ("ses",          'c = boto3.client("ses")\nc.send_email(Source="a", Destination={}, Message={})',              "ses:SendEmail"),
    ("ses-raw",      'c = boto3.client("ses")\nc.send_raw_email(Source="a", Destinations=[], RawMessage={})',       "ses:SendRawEmail"),
    ("events",       'c = boto3.client("events")\nc.put_rule(Name="r")',                                            "events:PutRule"),
    ("events-list",  'c = boto3.client("events")\nc.list_targets_by_rule(Rule="r")',                                "events:ListTargetsByRule"),
    ("iam",          'c = boto3.client("iam")\nc.list_users()',                                                     "iam:ListUsers"),
    ("iam-role",     'c = boto3.client("iam")\nc.get_role_policy(RoleName="r", PolicyName="p")',                    "iam:GetRolePolicy"),
    ("logs",         'c = boto3.client("logs")\nc.filter_log_events(logGroupName="g")',                             "logs:FilterLogEvents"),
    ("sts",          'c = boto3.client("sts")\nc.get_caller_identity()',                                            "sts:GetCallerIdentity"),
    ("sqs",          'c = boto3.client("sqs")\nc.send_message(QueueUrl="u", MessageBody="b")',                      "sqs:SendMessage"),
    ("rds",          'c = boto3.client("rds")\nc.describe_db_instances()',                                          "rds:DescribeDBInstances"),
    ("cloudtrail",   'c = boto3.client("cloudtrail")\nc.describe_trails()',                                         "cloudtrail:DescribeTrails"),
    ("ce",           'c = boto3.client("ce")\nc.get_cost_and_usage(TimePeriod={}, Granularity="DAILY", Metrics=[])', "ce:GetCostAndUsage"),
    ("kms",          'c = boto3.client("kms")\nc.describe_key(KeyId="k")',                                          "kms:DescribeKey"),
    ("ecs",          'c = boto3.client("ecs")\nc.describe_task_definition(taskDefinition="a")',                     "ecs:DescribeTaskDefinition"),
    ("apigateway",   'c = boto3.client("apigateway")\nc.get_rest_apis()',                                           "apigateway:GET"),
    ("apigatewayv2", 'c = boto3.client("apigatewayv2")\nc.get_apis()',                                              "apigateway:GET"),
]

# The 13 services this batch adds, plus the pre-existing 10 (the scorecard baseline).
_NEWLY_MODELED = ["ses", "events", "iam", "logs", "sts", "sqs", "rds",
                  "cloudtrail", "ce", "kms", "ecs", "apigateway", "apigatewayv2"]
_BEFORE_10 = ["s3", "ssm", "dynamodb", "secretsmanager", "ec2", "lambda",
              "sns", "stepfunctions", "cloudfront", "cloudwatch"]


def _scan(snippet: str):
    return E._scan_python_for_operations("import boto3\n" + snippet + "\n", "fixture.py")


@pytest.mark.parametrize("label,snippet,action", _CASES, ids=[c[0] for c in _CASES])
def test_service_emits_real_action_not_unmodeled(label, snippet, action):
    """The transition this campaign exists to make: COVERAGE-UNKNOWN -> a real action.

    A now-modeled service must NOT emit a `<svc>:UNMODELED` sentinel, and MUST emit
    the grounded IAM action for the representative call.
    """
    ops = _scan(snippet)
    all_actions = [a for op in ops for a in op.iam_actions]
    assert not any(a.endswith(":UNMODELED") for a in all_actions), \
        f"{label}: still emitting an UNMODELED sentinel -- {all_actions}"
    assert action in all_actions, f"{label}: expected {action}, got {all_actions}"


@pytest.mark.parametrize("label,snippet,action", _CASES, ids=[c[0] for c in _CASES])
def test_service_reaches_a_real_verdict_both_ways(label, snippet, action):
    """A modeled action must yield a real verdict: GRANTED-BROAD when held on
    Resource:'*', and grants()==False for a role that holds only an unrelated
    action. A COVERAGE-UNKNOWN service could produce neither.
    """
    prefix = action.split(":")[0]
    held = E.IamRole("held", "held", statements=[
        E.IamStatement(effect="Allow", actions=[action], resources=["*"], source_file="fx")])
    v_held, _s, _n = held.resource_verdict(
        action, "arn:aws:%s:us-east-1:123456789012:x" % prefix, exact=True)
    assert v_held in (E.V_GRANTED, E.V_GRANTED_BROAD), f"{label}: got {v_held}"
    assert held.grants(action) is True, f"{label}: held role must grant {action}"

    other = E.IamRole("other", "other", statements=[
        E.IamStatement(effect="Allow", actions=["s3:GetObject"], resources=["*"], source_file="fx")])
    assert other.grants(action) is False, \
        f"{label}: a role without {action} must not grant it"


def test_all_thirteen_services_are_registered():
    missing = [s for s in _NEWLY_MODELED if s not in E._MODELED_BOTO3_SERVICES]
    assert not missing, f"unmodeled after the batch: {missing}"


def test_coverage_scorecard_10_to_23():
    """Before: 10 modeled services. After: 23 (the 10 + these 13). Aliases
    (s3_client, DynamoDB, sfn) are not counted as distinct services."""
    for s in _BEFORE_10:
        assert s in E._MODELED_BOTO3_SERVICES, f"pre-existing {s} lost"
    distinct = set(_BEFORE_10) | set(_NEWLY_MODELED)
    assert len(distinct) == 23, f"expected 23 distinct services, got {len(distinct)}"
    assert distinct <= E._MODELED_BOTO3_SERVICES


def test_apigateway_v1_and_v2_share_one_map():
    """API Gateway v1 and v2 use the SAME IAM prefix (apigateway:); both boto3
    client names must resolve to the same method map."""
    assert E._BOTO3_BY_SERVICE["apigateway"] is E._BOTO3_BY_SERVICE["apigatewayv2"]


# ---------------------------------------------------------------------------
# NON-VACUITY CONTROLS -- prove the suite above is coupled to the maps.
# ---------------------------------------------------------------------------

def test_a_still_unmodeled_service_still_sentinels():
    """The instrument's own control. A service we did NOT model (athena) must
    STILL produce a `<svc>:UNMODELED` sentinel. If this ever fails, every
    `not ...UNMODELED` assertion above is vacuous -- it would pass even if the
    maps did nothing.
    """
    assert "athena" not in E._MODELED_BOTO3_SERVICES
    ops = _scan('c = boto3.client("athena")\nc.start_query_execution(QueryString="x")')
    all_actions = [a for op in ops for a in op.iam_actions]
    assert "athena:UNMODELED" in all_actions, \
        f"athena must still sentinel -- the mechanism is the control; got {all_actions}"


def test_reverting_a_map_reintroduces_the_sentinel(monkeypatch):
    """Executable mutation: remove `ses` from the registry in-process and the exact
    snippet that GREENs in test_service_emits_real_action_not_unmodeled must revert
    to a `ses:UNMODELED` sentinel with NO `ses:SendEmail`. Proves the passing
    assertions are coupled to `_BOTO3_SES`, not to something incidental.
    """
    reg = dict(E._BOTO3_BY_SERVICE)
    reg.pop("ses")
    monkeypatch.setattr(E, "_BOTO3_BY_SERVICE", reg)
    monkeypatch.setattr(E, "_MODELED_BOTO3_SERVICES", set(reg))

    ops = _scan('c = boto3.client("ses")\nc.send_email(Source="a", Destination={}, Message={})')
    all_actions = [a for op in ops for a in op.iam_actions]
    assert "ses:UNMODELED" in all_actions, \
        f"with ses removed the call must revert to the sentinel; got {all_actions}"
    assert "ses:SendEmail" not in all_actions, \
        "a real action survived the map revert -- the assertion is not coupled to the map"
