#!/usr/bin/env python3
"""The W2-06 irpt-status packet's proof (CTO rulings batch 165), read on the LIVE routes.

    python w206_read_proof.py <tenant> <out.json> <request-id> [<request-id> ...] [--compare <before.json>]

One login as svc-irpt-analysis; every call is a GET; nothing is created and no vendor is reached. The password is read
by NAME into memory and never printed. For each request id:
  read             GET analysis/requests/{id}                                  (unchanged: {identity, accepted_at})
  read+comparisons GET analysis/requests/{id}&include=comparisons              (unchanged: E7b)
  read+composition GET analysis/requests/{id}&include=composition              (W2-06; refused before the apply)
  read+both        GET analysis/requests/{id}&include=comparisons,composition  (W2-06; refused before the apply)
  read+duplicate   GET analysis/requests/{id}&include=composition,composition  (refused before AND after)
Recorded per call: HTTP status, ok, state, reason. The plain and comparisons reads keep their `data` (request metadata
only). A composition is NEVER recorded by value -- it carries a client's display text -- only its key NAMES and the
sha256 of its canonical JSON, so the two W2-06 reads can be compared to each other. ASCII only.
"""
import hashlib
import json
import sys

import served_reads_before_after as reads
import svc_principal as sp


def _composition_record(data):
    if not isinstance(data, dict) or not isinstance(data.get("composition"), dict):
        return {}
    composition = data["composition"]
    canonical = json.dumps(composition, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return {"composition_keys": sorted(composition), "composition_sha256": hashlib.sha256(canonical.encode()).hexdigest(),
            "other_keys": sorted(k for k in data if k != "composition")}


def main(argv):
    compare = None
    if "--compare" in argv:
        i = argv.index("--compare")
        compare = json.load(open(argv[i + 1], encoding="utf-8"))
        argv = argv[:i] + argv[i + 2:]
    tenant, out, request_ids = argv[1], argv[2], argv[3:]
    log = []
    password = sp._sm().get_secret_value(SecretId=sp.SECRET)["SecretString"]
    code, login = sp._call("POST", "/auth/login", {"email": sp.EMAIL, "password": password},
                           {"Content-Type": "application/json"}, log)
    del password
    token = login.get("accessToken") if isinstance(login, dict) else None
    print("login HTTP %s token %s" % (code, bool(token)))
    if not token:
        return 1
    headers = {"Authorization": "Bearer " + token, "X-Contract-Version": "v1", "Content-Type": "application/json"}
    query = "?selected_tenant=" + tenant
    calls = []
    for rid in request_ids:
        base = "analysis/requests/%s%s" % (rid, query)
        calls += [("read %s" % rid, base, "data"),
                  ("read+comparisons %s" % rid, base + "&include=comparisons", "data"),
                  ("read+composition %s" % rid, base + "&include=composition", "composition"),
                  ("read+both %s" % rid, base + "&include=comparisons,composition", "composition"),
                  ("read+duplicate %s" % rid, base + "&include=composition,composition", "composition")]
    rows = []
    for name, path, keep in calls:
        code, resp = sp._call("GET", reads.BASE + path, None, headers, log)
        row = {"call": name, "http": code}
        row.update(reads.shape(resp))
        data = resp.get("data") if isinstance(resp, dict) else None
        if keep == "data":
            row["data"] = data
        else:
            row.update(_composition_record(data))
        rows.append(row)
        print("%-52s HTTP %s ok %s state %s reason %s composition %s" % (
            name, code, row.get("ok"), row.get("state"), row.get("reason"),
            (row.get("composition_sha256") or "-")[:16]))
    del token
    result = {"at": sp._now(), "principal": sp.EMAIL, "tenant": tenant, "request_ids": request_ids, "rows": rows}
    if compare is not None:
        before = {r["call"]: r for r in compare["rows"]}
        verdicts = []
        for r in rows:
            b = before.get(r["call"])
            if b is None:
                continue
            same = b.get("data") == r.get("data") and b.get("composition_sha256") == r.get("composition_sha256") \
                and b.get("reason") == r.get("reason")
            verdicts.append({"call": r["call"], "equal_to_before": same, "http_before": b.get("http"),
                             "http_after": r["http"], "reason_before": b.get("reason"), "reason_after": r.get("reason")})
            print("COMPARE %-52s before HTTP %s %s after HTTP %s %s equal %s" % (
                r["call"], b.get("http"), b.get("reason"), r["http"], r.get("reason"), same))
        result["compare"] = verdicts
    json.dump(result, open(out, "w", encoding="utf-8", newline="\n"), indent=1, default=str)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
