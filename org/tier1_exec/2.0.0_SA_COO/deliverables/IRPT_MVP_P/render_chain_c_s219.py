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


# --------------------------------------------------------------------------- PART 2: V1 and the human path
BRIDGE2 = Path(__file__).resolve().parent / "c_s219_bridge.mjs"
_HUMAN_KEY = w.rsa.generate_private_key(public_exponent=65537, key_size=2048)
HUMAN_PRIV = _HUMAN_KEY.private_bytes(w.serialization.Encoding.PEM, w.serialization.PrivateFormat.PKCS8,
                                      w.serialization.NoEncryption()).decode("ascii")
HUMAN_PUB = _HUMAN_KEY.public_key().public_bytes(
    w.serialization.Encoding.PEM, w.serialization.PublicFormat.SubjectPublicKeyInfo).decode("ascii")
ORIGIN = "origin-" + w._hexid("s219", int(time.time()))
KEYS = {"human": HUMAN_PUB, "render": w.PUB_PEM, "origin": ORIGIN}


def human_token():
    """The claim set V1's generateAccessToken issues (auth-handler/src/jwt.ts:162-193), signed with the
    HUMAN key: a firm advisor with a partner identity, 15 minutes."""
    now = int(time.time())
    return w.jose_jwt.encode({
        "sub": WORLD["delegator_subject"], "name": "S219 Advisor", "role": "user", "tier": "advisor",
        "firmId": WORLD["tenant"], "advisorKey": WORLD["advisor_id"], "advisorName": "S219 Advisor",
        "advisorRole": "advisor", "advisorId": WORLD["advisor_id"],
        "iss": "opal-portal-auth", "aud": "opal-portal-api", "iat": now, "exp": now + 900,
    }, HUMAN_PRIV, algorithm="RS256")


def bridge2(mode, token, uri=None, route=None):
    proc = w.subprocess.run(["node", str(BRIDGE2), str(ROOT)], capture_output=True, text=True, timeout=60,
                            input=json.dumps({"mode": mode, "token": token, "uri": uri, "route": route,
                                              "keys": KEYS}))
    if proc.returncode != 0:
        raise RuntimeError("c_s219_bridge.mjs rc=%s stderr=%s" % (proc.returncode, proc.stderr[-3000:]))
    return json.loads(proc.stdout.strip().splitlines()[-1])


def v1_arms():
    render = w._mint.mint_render_token(WORLD["bundle"], private_key_pem=w.PRIV_PEM).token
    human = human_token()
    got_render, got_human = bridge2("v1", render), bridge2("v1", human)
    w.check("V1 (e): the real verifyAccessToken REFUSES the render token", got_render["verified"] is False,
            str(got_render.get("error")))
    w.check("V1 control: the same verifier ACCEPTS a human access token", got_human["verified"] is True,
            str(got_human.get("error")))
    return {"render_token": got_render, "human_token": got_human}


def human_on_three_routes():
    human = human_token()
    render = w._mint.mint_render_token(WORLD["bundle"], private_key_pem=w.PRIV_PEM).token
    rows = []
    for published_op, route_key, claim, uri in ROUTES:
        route = _route(route_key, claim, IDS[claim])
        v3, v2 = bridge2("v3", human, uri=uri), bridge2("v2", human, uri=uri, route=route)
        row = {"route": route_key, "v3_admitted": v3["admitted"], "v2_authorized": v2["authorized"],
               "v2_role": v2["context"].get("role"), "v3_status": v3.get("status"), "v3_message": v3.get("message")}
        w.check("HUMAN (f) %s: V3 admits the human token" % published_op, v3["admitted"] is True,
                str(v3.get("message")))
        w.check("HUMAN (f) %s: the full V2 handler authorizes it as the human it is" % published_op,
                v2["authorized"] is True and v2["context"].get("email") == WORLD["delegator_subject"]
                and v2["context"].get("role") != "renderer")
        if v3["admitted"]:
            trusted, _dropped = w._scope.trusted_only(v3["headers"])
            principal_class, reason = w._scope.classify_principal(trusted)
            row["principal_class"] = principal_class
            w.check("HUMAN (f) %s: resolves a human class, never RENDER_DELEGATE" % published_op,
                    principal_class not in ("RENDER_DELEGATE", "UNKNOWN"), "%s: %s" % (principal_class, reason))
        rv2 = bridge2("v2", render, uri=uri, route=route)
        row["render_token_full_v2_handler"] = rv2["authorized"]
        w.check("RENDER %s: the full V2 handler (origin gate first) authorizes the render token" % published_op,
                rv2["authorized"] is True and rv2["context"].get("role") == "renderer", json.dumps(rv2["context"])[:160])
        rows.append(row)
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)
    receipt = {"schema_version": "irpt-render-chain-c-s219-v1", "part": "1-2 of 3", "by": "2.0.0_SA_COO~P",
               "row": "IRPT_BCKEND-C-S219", "base": "worker 21 chain (34366c30d1), imported, 12 of 12 today",
               "one_token_three_routes": one_token_three_routes(),
               "swapped_id_each_route": swapped_id_each_route(),
               "expiry": expiry_boundary(),
               "v1": v1_arms(),
               "human_on_three_routes": human_on_three_routes()}
    receipt["failures"] = list(w.FAILURES)
    receipt["verdict"] = "PASS" if not w.FAILURES else "FAIL"
    Path(args.out).write_text(json.dumps(receipt, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: receipt[k] for k in ("verdict", "failures")}, indent=1))
    print(json.dumps(receipt["expiry"], indent=1))
    return 0 if not w.FAILURES else 1


if __name__ == "__main__":
    sys.exit(main())
