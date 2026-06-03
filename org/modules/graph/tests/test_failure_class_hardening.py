"""Regression tests for the comp-* failure-class hardening (Andrew-direct
2026-06-03 cleanup). Locks the two failure classes that were fixed across the
suite so a later edit can't silently regress them:

  (A) DRIFT  -- a tool reading a hand-maintained doc instead of deriving at runtime.
  (B) CONFIDENTLY-INCOMPLETE -- a tool reporting clean/pass while structurally blind.

These assert the *contract* (the behavior change), not brittle counts, so they
survive legit data/config evolution. Pure importable-function level -- no live
AWS/S3, fast + deterministic.

Anchors: comp-pii 16a7d0cd4, comp-iam c0df8f0fd + b76721009, comp-blast fb1f95e86,
comp-incrparity 847ba967c, comp-validate 1bb8b7766/316e97967.
"""
from __future__ import annotations

import os
import sys

import pytest

GRAPH_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if GRAPH_DIR not in sys.path:
    sys.path.insert(0, GRAPH_DIR)

import extract_iam as iam  # noqa: E402
import extract_validate as ev  # noqa: E402
import incrparity_core as ip  # noqa: E402
import pii_cli as pii  # noqa: E402


# ---------------------------------------------------------------------------
# comp-pii (A: runtime-derive from live pseudonymizer; B: PII-name heuristic)
# ---------------------------------------------------------------------------

def test_pii_derives_hashed_set_from_live_pseudonymizer():
    """DRIFT fix: the hashed-field set is parsed from the LIVE pseudonymizer.py at
    runtime (it only CLAIMED to before)."""
    derived, src = pii._derive_pseudonymized_fields(pii._WORKSPACE)
    assert src is not None, "pseudonymizer.py must be locatable for runtime derivation"
    # The pseudonymizer's _transform_field hashes these (prefix-mapped):
    assert derived.get("relationship_name") == "Client"
    assert derived.get("account_id") == "Acct"
    assert derived.get("client_key") == "id"
    assert derived.get("city") == "Location"


def test_pii_account_number_clientkey_not_in_runtime_hashed_set():
    """The static list FALSELY claimed account_number + clientKey are hashed; the
    live pseudonymizer hashes NEITHER. The runtime derivation must not include them
    (they were demoted to cleartext-potential)."""
    derived, _ = pii._derive_pseudonymized_fields(pii._WORKSPACE)
    assert "account_number" not in derived
    assert "clientKey" not in derived


@pytest.mark.parametrize("field", ["ssn", "client_phone", "customer_email",
                                    "date_of_birth", "tax_id", "account_number"])
def test_pii_heuristic_flags_sensitive_names(field):
    """B: an unrecognized PII-looking field is flagged (not silently clean)."""
    assert pii._looks_like_pii(field) is True


@pytest.mark.parametrize("field", ["total_aua", "advisor_name", "state", "nna_canonical"])
def test_pii_heuristic_high_precision_no_false_positives(field):
    """Heuristic must NOT fire on ambiguous/non-PII field names (would flood)."""
    assert pii._looks_like_pii(field) is False


# ---------------------------------------------------------------------------
# comp-iam (B: model previously-unmodeled services; A-adjacent: Deny-awareness)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("service", ["secretsmanager", "ec2", "lambda", "sns",
                                     "stepfunctions", "cloudfront", "cloudwatch"])
def test_iam_previously_unmodeled_services_now_modeled(service):
    """B: these 7 produced zero-ops 'no gap' before; now modeled -> verified."""
    assert service in iam._MODELED_BOTO3_SERVICES
    assert iam._BOTO3_BY_SERVICE.get(service), f"{service} must have a method map"


def test_iam_secretsmanager_get_secret_value_maps_to_action():
    assert iam._BOTO3_BY_SERVICE["secretsmanager"]["get_secret_value"] == ["secretsmanager:GetSecretValue"]


def test_iam_stepfunctions_uses_states_prefix():
    """client('stepfunctions') but IAM prefix is 'states:'."""
    assert iam._BOTO3_BY_SERVICE["stepfunctions"]["start_execution"] == ["states:StartExecution"]


def test_iam_grants_allow_and_missing_unchanged():
    role = iam.IamRole(role_name="t", tf_resource="t", statements=[
        iam.IamStatement(effect="Allow", actions=["s3:GetObject"], resources=["*"], source_file="x"),
    ])
    assert role.grants("s3:GetObject") is True
    assert role.grants("s3:DeleteObject") is False


def test_iam_deny_matches_surfaces_deny_not_silently_ignored():
    """grants() considered only Allow (silently ignored Deny -> false-GRANTED).
    deny_matches() must surface a matching Deny."""
    role = iam.IamRole(role_name="t", tf_resource="t", statements=[
        iam.IamStatement(effect="Allow", actions=["s3:GetObject"], resources=["arn:aws:s3:::b/*"], source_file="x"),
        iam.IamStatement(effect="Deny", actions=["s3:*"], resources=["arn:aws:s3:::b/*"], source_file="bucket-policy"),
    ])
    denies = role.deny_matches("s3:GetObject")
    assert len(denies) == 1
    assert denies[0].effect.lower() == "deny"


# ---------------------------------------------------------------------------
# comp-incrparity (B: unregistered -> UNVERIFIED, not PASS)
# ---------------------------------------------------------------------------

def test_incrparity_unverified_is_not_passed():
    """absence != PASS: an unverified result must NOT report passed."""
    r = ip.DiffResult(script_id="X", mode="quick", full_prefix="(none registered)",
                      incremental_prefix="(none registered)", unverified=True)
    assert r.passed is False
    assert "UNVERIFIED" in r.summary()


def test_incrparity_clean_still_passes():
    r = ip.DiffResult(script_id="X", mode="quick", full_prefix="a", incremental_prefix="b")
    assert r.passed is True
    assert "PARITY OK" in r.summary()


# ---------------------------------------------------------------------------
# comp-validate (waiver: validation:not_required -> WAIVED, not NO_CONFIG)
# ---------------------------------------------------------------------------

def test_validate_waiver_parsed_and_short_circuits(tmp_path):
    """A deliberate `validation: not_required` + reason waiver is parsed + the
    artifact-check short-circuits to WAIVED (no artifact load needed)."""
    cfg = tmp_path / "cfg.yaml"
    cfg.write_text(
        "scripts:\n"
        "  WAIVED_X:\n"
        "    primary_artifact: x.json\n"
        "    validation: not_required\n"
        "    reason: \"diagnostic emitter; no downstream data contract\"\n"
        "  NORMAL_X:\n"
        "    primary_artifact: y.json\n"
        "    checks:\n"
        "      - {type: key_present, name: k, severity: ERROR, key: foo}\n"
    )
    configs = ev.load_validate_config(tmp_path, cfg)
    assert configs["WAIVED_X"].validation_not_required is True
    assert "diagnostic" in configs["WAIVED_X"].waiver_reason
    assert configs["NORMAL_X"].validation_not_required is False
    # short-circuits to WAIVED without needing the artifact to exist
    res = ev.run_validate("WAIVED_X", tmp_path / "does_not_exist.json", configs)
    assert len(res) == 1 and res[0].status == "WAIVED"


def test_validate_all_script_check_config_is_zero_checks(tmp_path):
    """ZERO_CHECKS precondition (LD-0148 §10.1b): a config whose checks are ALL
    source-level (script_check, deferred to comp-pipescript / a named validator)
    yields 0 runnable checks -> all SKIP -> pass_count==0. The CLI maps that to
    ZERO_CHECKS exit-2 (NOT 'PASS: all 0 checks') -- verified live on C_01/nna_atomic.
    This locks the data-layer precondition."""
    cfg = tmp_path / "cfg.yaml"
    cfg.write_text(
        "scripts:\n"
        "  ALLSKIP_X:\n"
        "    primary_artifact: x.json\n"
        "    checks:\n"
        "      - {type: script_check, name: 'deferred to validate_x.py',"
        " severity: INFO, description: 'run validate_x.py'}\n"
    )
    art = tmp_path / "x.json"
    art.write_text("{}")
    configs = ev.load_validate_config(tmp_path, cfg)
    res = ev.run_validate("ALLSKIP_X", art, configs)
    assert res, "expected at least one (SKIP) result"
    assert all(r.status == "SKIP" for r in res), "all-script_check config must yield all-SKIP"
    assert not any(r.status == "PASS" for r in res), "0 PASS checks == the ZERO_CHECKS condition"
