#!/usr/bin/env python3
"""C-S219, PART 1 of 3 -- the render chain completed where the round-18 chain stopped.

Row IRPT_BCKEND-C-S219 (REMEDIATION_v9; CTO round-18 analysis, `ledger/ROUND_ANALYSIS.round18.md:35`) names
what worker 21's chain (`deliverables/0.9.0_WK_IRPT_BCKEND~21/test_actual_module_chain.py`, 12 of 12 today)
does not prove. This part closes three of those gaps with the SAME real modules and bridge, imported, never
restated:

  ONE TOKEN   one minted token (one bundle pinning accountSetId, jobId AND reportId) is admitted by the real
              V3 and V2 on ALL THREE print-route reads and resolves RENDER_DELEGATE through the real resolver
              and Enforcer for each (worker 21 used three tokens in three worlds);
  SWAPPED ID  that same token is refused by V2 on each of the three routes when the path id is not the
              pinned one (worker 21 swapped one route);
  EXPIRY      the boundary is MEASURED at both verifiers for tokens whose `exp` lies 1, 30, 59, 61 and 120
              seconds in the past (exp - iat = 300 s, inside the bound), and STATED beside PRD item 2
              ("nbf/iat with at most 60 s skew leeway") and item 7(c) ("a token past exp is refused").

Parts 2 and 3 (a real human-key token on the same routes, actual V1 verification, served.Entry and the
report-body read with an unpinned same-account negative) follow on the next ticks.

OFFLINE: no AWS call, no key provisioning, no deploy. Node modules are the main workspace's, junctioned
into this worktree (gitignored). Output: a receipt (--out) and rc 0 only if every asserted arm passes.

Usage (backend worktree root):
  python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/render_chain_c_s219.py --out <receipt.json>
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
W21 = ROOT / "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~21"

_spec = importlib.util.spec_from_file_location("w21_chain", W21 / "test_actual_module_chain.py")
w = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(w)          # module level only: the key pair, the helpers, the worlds; main() is not run

API = "/api/scoped/investor-reporting"
IDS = {"accountSetId": "AS-S219-1", "jobId": "JOB-S219-1", "reportId": "REP-S219-1"}
ROUTES = [
    ("performance-report", "GET %s/performance/{accountSetId}" % API, "accountSetId",
     "%s/performance/%s" % (API, IDS["accountSetId"])),
    ("analysis-report", "GET %s/analysis/{jobId}/sections" % API, "jobId",
     "%s/analysis/%s/sections" % (API, IDS["jobId"])),
    ("narrative-packet", "GET %s/narrative/{reportId}" % API, "reportId",
     "%s/narrative/%s" % (API, IDS["reportId"])),
]
WORLD = w.make_world("S219", "cottonwood", IDS["accountSetId"], IDS["jobId"], IDS["reportId"],
                     "performance-report", ROUTES[0][1], "accountSetId", IDS["accountSetId"])


def _route(route_key, claim, value):
    return {"routeKey": route_key, "pathParameters": {claim: value}}


def one_token_three_routes():
    token = w._mint.mint_render_token(WORLD["bundle"], private_key_pem=w.PRIV_PEM).token
    jti = w.jose_jwt.get_unverified_claims(token)["jti"]
    rows = []
    for published_op, route_key, claim, uri in ROUTES:
        out, _err = w.call_bridge(token, uri, "GET", _route(route_key, claim, IDS[claim]))
        v3, v2 = out["v3"], out["v2"]
        row = {"route": route_key, "jti": jti, "v3_admitted": v3["admitted"], "v2_authorized": v2["authorized"]}
        w.check("ONE TOKEN %s: V3 admits" % published_op, v3["admitted"] is True, str(v3.get("message")))
        w.check("ONE TOKEN %s: V2 authorizes" % published_op, v2["authorized"] is True, str(v2.get("error", "")))
        if v3["admitted"]:
            trusted, _dropped = w._scope.trusted_only(v3["headers"])
            principal_class, reason = w._scope.classify_principal(trusted)
            key_op = w._served.key_operation(published_op)
            scope, refusal = w.build_enforcer(WORLD).resolve_now(
                w._enforce.Request(v3["headers"], key_op, "account", WORLD["a"]))
            covered = bool(scope) and w.build_enforcer(WORLD).covers(scope, "account", WORLD["a"])[0]
            row.update(principal_class=principal_class, operation=key_op, refusal=repr(refusal), covered=covered)
            w.check("ONE TOKEN %s: RENDER_DELEGATE" % published_op, principal_class == "RENDER_DELEGATE", reason)
            w.check("ONE TOKEN %s: resolve_now admits and covers the pinned account" % published_op,
                    refusal is None and covered, repr(refusal))
        rows.append(row)
    w.check("ONE TOKEN: the three reads carried one jti", len({r["jti"] for r in rows}) == 1)
    return {"token_count": 1, "reads": rows}


def swapped_id_each_route():
    token = w._mint.mint_render_token(WORLD["bundle"], private_key_pem=w.PRIV_PEM).token
    rows = []
    for published_op, route_key, claim, uri in ROUTES:
        other = IDS[claim] + "-OTHER"
        out, _err = w.call_bridge(token, uri.replace(IDS[claim], other), "GET", _route(route_key, claim, other))
        rows.append({"route": route_key, "v3_admitted": out["v3"]["admitted"],
                     "v2_authorized": out["v2"]["authorized"], "v2_error": out["v2"].get("error")})
        w.check("SWAPPED ID %s: V2 refuses a path id the token does not pin" % published_op,
                out["v2"]["authorized"] is False, str(out["v2"].get("error")))
    return rows


def _forged(seconds_past_exp):
    claims = w.jose_jwt.get_unverified_claims(
        w._mint.mint_render_token(WORLD["bundle"], private_key_pem=w.PRIV_PEM).token)
    now = int(time.time())
    claims["exp"] = now - seconds_past_exp
    claims["iat"] = claims["exp"] - 300
    if "nbf" in claims:
        claims["nbf"] = claims["iat"]
    return w.jose_jwt.encode(claims, w.PRIV_PEM, algorithm="RS256")


def expiry_boundary():
    published_op, route_key, claim, uri = ROUTES[0]
    rows = []
    for past in (1, 30, 59, 61, 120):
        out, _err = w.call_bridge(_forged(past), uri, "GET", _route(route_key, claim, IDS[claim]))
        rows.append({"seconds_past_exp": past, "v3_admitted": out["v3"]["admitted"],
                     "v2_authorized": out["v2"]["authorized"]})
        if past > 60:
            w.check("EXPIRY %ss past exp: refused at V3 and V2" % past,
                    out["v3"]["admitted"] is False and out["v2"]["authorized"] is False)
    admitted_past_exp = [r["seconds_past_exp"] for r in rows if r["v3_admitted"] or r["v2_authorized"]]
    return {"measured": rows,
            "stated_boundary": ("a render token is refused at both verifiers once more than 60 s past exp; "
                                "within 60 s past exp it is %s (both verifiers pass clockTolerance 60 to "
                                "jsonwebtoken, which applies it to exp as well as nbf)"
                                % ("ADMITTED at %s s" % admitted_past_exp if admitted_past_exp else "refused")),
            "prd": ("IRPT_BCKEND_PRD.md item 2: nbf/iat with at most 60 s skew leeway; item 7(c): a token past "
                    "exp is refused"),
            "consistent_with_prd_literal": not admitted_past_exp,
            "effective_max_life_s": 300 + (60 if admitted_past_exp else 0)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)
    receipt = {"schema_version": "irpt-render-chain-c-s219-v1", "part": "1 of 3", "by": "2.0.0_SA_COO~P",
               "row": "IRPT_BCKEND-C-S219", "base": "worker 21 chain (34366c30d1), imported, 12 of 12 today",
               "one_token_three_routes": one_token_three_routes(),
               "swapped_id_each_route": swapped_id_each_route(),
               "expiry": expiry_boundary()}
    receipt["failures"] = list(w.FAILURES)
    receipt["verdict"] = "PASS" if not w.FAILURES else "FAIL"
    Path(args.out).write_text(json.dumps(receipt, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: receipt[k] for k in ("verdict", "failures")}, indent=1))
    print(json.dumps(receipt["expiry"], indent=1))
    return 0 if not w.FAILURES else 1


if __name__ == "__main__":
    sys.exit(main())
