#!/usr/bin/env python3
"""V1 of the service-principal boundary move (ledger irpt-service-principal-boundary-served-20261001, IB-pr-275).

    python v1_boundary_read.py <out.json>

One login as svc-irpt-analysis (allowedFirmIds cottonwood), then for EACH of the three functions that received
served.py @f6c6b56f40 one request selecting a FOREIGN firm (expected: refused FIRM_BINDING) and one selecting
cottonwood (expected: any answer that is NOT FIRM_BINDING):

  irpt-performance-adapter  GET  performance/{accountSetId}   a set id that does not exist
  irpt-ycharts-generate     POST analysis                     an empty body (refused before any write or queue send)
  irpt-export-render        GET  export/{exportId}            an export id that does not exist

No request names a real client object, creates a request, or reaches the vendor. The password is read by NAME into
memory for the login and never printed. The log keeps status codes and reason codes; tokens are redacted. ASCII only.
"""
import json
import sys

import svc_principal as sp

FOREIGN, OWN = "inflection", "cottonwood"
BASE = "/api/scoped/investor-reporting/"
PROBES = [
    ("irpt-performance-adapter", "GET", "performance/ASET-00000000000000000000000000", None),
    ("irpt-ycharts-generate", "POST", "analysis", {}),
    ("irpt-export-render", "GET", "export/EXP-00000000000000000000000000", None),
]


def reason_of(resp):
    if not isinstance(resp, dict):
        return None
    status = resp.get("status") if isinstance(resp.get("status"), dict) else {}
    return status.get("public_reason_code") or resp.get("reason") or resp.get("error") or resp.get("message")


def main(out):
    log = []
    password = sp._sm().get_secret_value(SecretId=sp.SECRET)["SecretString"]
    status, login = sp._call("POST", "/auth/login", {"email": sp.EMAIL, "password": password},
                             {"Content-Type": "application/json"}, log)
    del password
    log[-1]["request"] = {"email": sp.EMAIL, "password": "<redacted>"}
    token = login.get("accessToken") if isinstance(login, dict) else None
    print("login: HTTP %d; token present %s" % (status, bool(token)))
    if not token:
        json.dump({"principal": sp.EMAIL, "at": sp._now(), "calls": log}, open(out, "w", encoding="utf-8", newline="\n"), indent=1)
        return 1
    headers = {"Authorization": "Bearer " + token, "X-Contract-Version": "v1", "Content-Type": "application/json"}
    results, held = [], 0
    for function, method, path, body in PROBES:
        row = {"function": function, "method": method, "route": path.split("/")[0]}
        for firm in (FOREIGN, OWN):
            code, resp = sp._call(method, BASE + path + "?selected_tenant=" + firm, body, headers, log)
            reason = reason_of(resp)
            row[firm] = {"http": code, "ok": resp.get("ok") if isinstance(resp, dict) else None, "reason": reason}
            print("%-26s %-4s %-12s selected_tenant=%-10s HTTP %s reason %s"
                  % (function, method, row["route"], firm, code, reason))
        good = row[FOREIGN]["reason"] == "FIRM_BINDING" and row[OWN]["reason"] != "FIRM_BINDING" \
            and row[OWN]["http"] is not None
        row["holds"] = good
        held += 1 if good else 0
        results.append(row)
    del token
    print("V1: %d of %d functions refuse the foreign firm FIRM_BINDING and do not refuse cottonwood FIRM_BINDING"
          % (held, len(PROBES)))
    json.dump({"principal": sp.EMAIL, "at": sp._now(), "foreign": FOREIGN, "own": OWN, "results": results,
               "held": held, "of": len(PROBES), "calls": log},
              open(out, "w", encoding="utf-8", newline="\n"), indent=1)
    print("log written:", out)
    return 0 if held == len(PROBES) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
