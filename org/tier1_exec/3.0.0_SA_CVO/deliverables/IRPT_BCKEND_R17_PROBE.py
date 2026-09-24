"""Offline CVO probes. Exit zero means counterexamples reproduced, NOT acceptance."""
import importlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
IRPT = ROOT / "infra/aws/lambda/investor-reporting"
sys.path.insert(0, str(IRPT / "_authz"))
ez = importlib.import_module("enforce")
rs = ez._scope


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


if len(sys.argv) > 1 and sys.argv[1] == "mint":
    arg = json.load(sys.stdin)
    mint = load("cvo_real_minter", IRPT / "_render_identity/mint.py")
    print(mint.mint_render_token(arg["bundle"], arg["key"]).token)
    sys.exit(0)

if len(sys.argv) > 1 and sys.argv[1] == "classify":
    trusted, dropped = rs.trusted_only(json.load(sys.stdin))
    print(json.dumps({"classification": rs.classify_principal(trusted), "dropped": dropped}))
    sys.exit(0)

fx = load("cvo_authz_fixtures", IRPT / "_authz/tests/fixtures.py")
deps = fx.Deps()
lookup_calls = []


def loader(tenant, revision):
    lookup_calls.append([tenant, revision])
    return {"account_ids": [fx.A1, fx.A2], "bundle_id": "bundle-1",
            "revision": "rev-1", "report_id": fx.REPORT_OK}


e = ez.Enforcer(ez.FirmBinding(fx.TENANT, fx.OPAQUE_FIRM),
                deps.load_directory, deps.load_ownership, deps.load_policy,
                load_render_bundle=loader)


def request(bundle="bundle-1", revision="rev-1", subject=fx.ADVISOR_A,
            operation="performance"):
    return ez.Request({"X-Origin-Verify": "cloudfront", "X-User-Email": "render:fixture",
                       "X-User-Role": "renderer", "X-Firm-Id": fx.TENANT,
                       "X-Render-Delegator": subject, "X-Render-Bundle": bundle,
                       "X-Render-Revision": revision}, operation, "account", fx.A1)


baseline, refusal = e.resolve_now(request())
assert refusal is None
other_bundle, refusal = e.resolve_now(request(bundle="not-bundle-1"))
assert refusal is None
other_rev, refusal = e.resolve_now(request(revision="rev-2"))
assert refusal is None
keys_equal = e.cache_key_for(baseline, request()) == e.cache_key_for(other_rev, request(revision="rev-2"))
assert keys_equal
subject_scope, subject_refusal = e.resolve_now(request(subject="advisor.a@49financial.com"))
human_scope, human_refusal = e.resolve_now(ez.Request(fx.headers(), "performance", "account", fx.A1))
assert human_refusal is None and subject_scope is None and subject_refusal.code == "EMPTY_GRANT"
operations = ["performance_report", "analysis_report", "narrative_packet"]
real_op_results = []
for operation in operations:
    scope, fail = e.resolve_now(request(operation=operation))
    assert scope is None and fail.code == "OBJECT_NOT_COVERED"
    real_op_results.append([operation, fail.code])
e.artifacts["unlisted-report"] = {"kind": "report", "firm": fx.OPAQUE_FIRM,
                                  "account_ids": [fx.A1]}
covered, _ = e.covers(baseline, "report", "unlisted-report")
assert covered
deps.revoke()
_, revoked = e.resolve_now(request())
assert revoked.code == "EMPTY_GRANT"
print(json.dumps({"positive_control": "advisor-id fixture resolves",
                  "subject_not_advisor_id": subject_refusal.code,
                  "same_human_with_actual_advisor_id": "accepted",
                  "different_bundle_accepted": True,
                  "bundle_loader_arguments": lookup_calls[:3],
                  "bundle_revision_cache_collision": keys_equal,
                  "unlisted_report_same_accounts_covered": covered,
                  "published_operations": real_op_results,
                  "revocation_control": revoked.code,
                  "verdict": "counterexamples reproduced, not acceptance"}, indent=2))
