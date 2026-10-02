#!/usr/bin/env python3
"""The irpt-status packet's per-piece proof (E7b + E6 + item 22; CTO rulings batches 142 and 146), read on the LIVE routes.

    python e7b_read_proof.py <tenant> <out.json> <request-id> [<request-id> ...]

One login as svc-irpt-analysis; every call is a GET; nothing is created and no vendor is reached. The password is read
by NAME into memory and never printed. For each request id:
  read          GET analysis/requests/{id}                         (E7b: the answer a caller that does not ask gets)
  read+include  GET analysis/requests/{id}&include=comparisons     (E7b: before the apply the served read REFUSES it)
  status        GET status/{id}                                    (E6: the memo changes no shape)
and once: history (GET analysis/requests, item 22 without client_id) and history+client (with client_id, which the
served history refuses before the apply). Recorded per call: HTTP status, ok, state, reason, and the `data` value itself
for the request read and history (request metadata: identity, accepted_at, and E7b's comparisons {key, label} -- no
client holding, no cookie, no credential), plus key NAMES for the status answer. Run once before the apply and once
after; `--compare <before.json>` prints, per call, whether the plain answers are equal key for key.
ASCII only.
"""
import json
import sys

import served_reads_before_after as reads
import svc_principal as sp


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
    calls = [("history", "analysis/requests" + query, True),
             ("history+client", "analysis/requests" + query + "&client_id=no-such-client", True)]
    for rid in request_ids:
        calls += [("read %s" % rid, "analysis/requests/%s%s" % (rid, query), True),
                  ("read+include %s" % rid, "analysis/requests/%s%s&include=comparisons" % (rid, query), True),
                  ("status %s" % rid, "status/%s%s" % (rid, query), False)]
    rows = []
    for name, path, keep in calls:
        code, resp = sp._call("GET", reads.BASE + path, None, headers, log)
        row = {"call": name, "http": code}
        row.update(reads.shape(resp))
        data = resp.get("data") if isinstance(resp, dict) else None
        if keep:
            row["data"] = data
        rows.append(row)
        print("%-46s HTTP %s ok %s state %s reason %s data keys %s" % (
            name, code, row.get("ok"), row.get("state"), row.get("reason"), ",".join(row.get("data_keys") or []) or "-"))
    del token
    result = {"at": sp._now(), "principal": sp.EMAIL, "tenant": tenant, "request_ids": request_ids, "rows": rows}
    if compare is not None:
        before = {r["call"]: r for r in compare["rows"]}
        verdicts = []
        for r in rows:
            b = before.get(r["call"])
            if b is None:
                continue
            same = (b.get("data") == r.get("data")) if "data" in r else (b.get("data_keys") == r.get("data_keys"))
            verdicts.append({"call": r["call"], "equal_to_before": same, "http_before": b.get("http"), "http_after": r["http"]})
            print("COMPARE %-46s before HTTP %s after HTTP %s equal %s" % (r["call"], b.get("http"), r["http"], same))
        result["compare"] = verdicts
    json.dump(result, open(out, "w", encoding="utf-8", newline="\n"), indent=1, default=str)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
