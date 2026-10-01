#!/usr/bin/env python3
"""Three live GETs of ONE job through the served routes, as the service principal: does any route serve a document?

    python job_status_route_read.py <tenant> <request-id> <out.json>

For a job that ended ATTENTION with a refused vendor PDF kept as evidence (CTO rulings batch 76 item 6; the st7
half's item 1): the status route, the request read and the sections route are read once each BEFORE the kept PDF is
used for anything. One login as svc-irpt-analysis; every request is a GET; nothing is created and no vendor is
reached. The password is read by NAME into memory and never printed. Recorded per call: HTTP status, ok, state,
reason code, and key NAMES (never a client's values). The last line is the verdict:

  DOCUMENT_VERDICT=NONE_SERVED     no route answered READY, sections, a report id or a document reference
  DOCUMENT_VERDICT=SERVED:<probe>  a route did; that is a stop, reported before anything else

ASCII only.
"""
import json
import sys

import served_reads_before_after as reads
import svc_principal as sp

DOCUMENT_KEYS = ("sections", "report_id", "report", "document", "pdf", "artifact_id", "download_url", "url")


def main(argv):
    tenant, request_id, out = argv[1], argv[2], argv[3]
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
    rows, served = [], []
    for name, path in (("status-job", "status/%s%s" % (request_id, query)),
                       ("request-read", "analysis/requests/%s%s" % (request_id, query)),
                       ("sections-by-request", "analysis/%s/sections%s" % (request_id, query))):
        code, resp = sp._call("GET", reads.BASE + path, None, headers, log)
        row = {"probe": name, "http": code}
        row.update(reads.shape(resp))
        data = resp.get("data") if isinstance(resp, dict) else None
        carried = sorted(k for k in DOCUMENT_KEYS if isinstance(data, dict) and data.get(k))
        row["document_keys_present"] = carried
        rows.append(row)
        if row.get("state") == "READY" or carried or row.get("count_sections"):
            served.append(name)
        print("%-20s HTTP %s ok %s state %s reason %s document keys %s data keys %s" % (
            name, code, row.get("ok"), row.get("state"), row.get("reason"), carried or "-",
            ",".join(row.get("data_keys") or []) or "-"))
    del token
    verdict = "SERVED:" + ",".join(served) if served else "NONE_SERVED"
    json.dump({"at": sp._now(), "principal": sp.EMAIL, "tenant": tenant, "request_id": request_id,
               "rows": rows, "verdict": verdict}, open(out, "w", encoding="utf-8", newline="\n"), indent=1)
    print("DOCUMENT_VERDICT=" + verdict)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
