"""Offline CVO counterexamples; no source mutation, AWS calls or persisted keys.

Expected observations describe the reviewed defect, not desired production behavior.
Reuses worker21's actual-module bridge and fixtures, not its assertions.
"""
import importlib.util
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "CLAUDE.md").exists())
path = ROOT / "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~21/test_actual_module_chain.py"
spec = importlib.util.spec_from_file_location("r18_chain", path)
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
w = c.WORLD1
route = {"routeKey": w["route_key"], "pathParameters": {w["claim_name"]: w["claim_value"]}}
token = c._mint.mint_render_token(w["bundle"], private_key_pem=c.PRIV_PEM).token
out, _ = c.call_bridge(token, w["uri"], "GET", route)
assert out["v3"]["admitted"] and out["v2"]["authorized"]
headers = out["v3"]["headers"]
op = c._served.key_operation(w["published_op"])

def observe(label, enforcer, h=headers, kind="account", oid=None):
    request = c._enforce.Request(h, op, kind, oid or w["a"])
    result = enforcer.serve(request, lambda scope: {"fixture_payload": True})
    print(label, "SERVED" if result.ok else result.code)
    return result.ok

assert observe("positive_actual_mint_edge_v2_enforcer_serve", c.build_enforcer(w))
assert not observe("empty_bundle_control", c.build_enforcer(w, render_bundle_override=lambda t,r: {}))
assert not observe("declared_wrong_bundle_control", c.build_enforcer(w, render_bundle_override=lambda t,r: {"bundle_id":"WRONG", "account_ids":[w["a"]]}))
assert observe("missing_bundle_identity_ACCEPTED", c.build_enforcer(w, render_bundle_override=lambda t,r: {"account_ids":[w["a"]]}))
assert observe("wrong_returned_revision_and_tenant_ACCEPTED", c.build_enforcer(w, render_bundle_override=lambda t,r: {"bundle_id":w["bundle"]["bundle_id"], "revision":"WRONG", "firm_id":"WRONG", "account_ids":[w["a"]]}))

e = c.build_enforcer(w)
e.artifacts["unlisted-report"] = {"kind":"report", "firm":w["tenant"], "account_ids":[w["a"]]}
assert observe("unpinned_same_account_report_ACCEPTED", e, kind="report", oid="unlisted-report")

# A real token whose delegator subject equals a live advisor id, but the current
# identity lookup returns no identity. This isolates fallback from a valid mapping.
b = dict(w["bundle"], delegator_subject=w["advisor_id"])
t = c._mint.mint_render_token(b, private_key_pem=c.PRIV_PEM).token
o, _ = c.call_bridge(t, w["uri"], "GET", route)
assert o["v3"]["admitted"] and o["v2"]["authorized"]
e = c.build_enforcer(w)
e.load_delegator_identity = lambda tenant, subject: None
assert observe("identity_lookup_absent_falls_back_and_ACCEPTS", e, h=o["v3"]["headers"])
e = c.build_enforcer(w, ownership_override=lambda t: {"schema_version":1,"advisors":{}})
assert not observe("revoked_ownership_control", e)
print("OBSERVATIONS 8/8 matched; five admitted cases include one positive and four residual defect cases.")
