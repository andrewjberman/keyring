"""Live before/after reads of the SERVED irpt-status under its own role: three direct invokes (rebuild 3, 2026-09-28).

    python status_live_reads.py <out_dir> <tag>

A: REQ-67e12718 status read with X-IRPT-Status-Dates prospect-v1 (READY PER_SECTION since rebuild 3);
B: the same read without the header (ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE);
C: an owner refusal with a bad firm token (FIRM_BINDING).
Writes <out_dir>/r3_<tag>.json.
"""
import base64
import copy
import datetime
import json
import os
import sys

import boto3

HERE = os.path.dirname(os.path.abspath(__file__))


def cases():
    base = json.load(open(os.path.join(HERE, "status_live_read_event.json"), encoding="utf-8"))
    dates = copy.deepcopy(base)
    dates["headers"]["x-irpt-status-dates"] = "prospect-v1"
    bad_firm = copy.deepcopy(base)
    bad_firm["headers"]["x-firm-id"] = "no-such-firm"
    return {"A_req67_status_dates": dates, "B_req67_plain": copy.deepcopy(base), "C_owner_refusal_bad_firm": bad_firm}


def read_one(lam, event):
    r = lam.invoke(FunctionName="irpt-status", LogType="Tail", Payload=json.dumps(event).encode())
    body = json.loads(r["Payload"].read())
    log = base64.b64decode(r["LogResult"]).decode(errors="replace")
    d = (body.get("data") or body.get("status") or {}) if isinstance(body, dict) else {}
    dates = d.get("source_dates") or {}
    n_dates = dates.get("section_dates")
    n_dates = len(n_dates) if isinstance(n_dates, (list, dict)) else n_dates
    internal = [json.loads(line) for line in log.splitlines() if line.startswith("{") and "irpt_internal" in line]
    return {"fn_error": r.get("FunctionError"), "state": d.get("state"), "reason": d.get("public_reason_code"),
            "date_basis": dates.get("date_basis"), "n_section_dates": n_dates,
            "internal": [(i.get("exception_type"), i.get("exception_text")) for i in internal],
            "tracebacks": log.count("Traceback"), "type_error": log.count("TypeError"),
            "init": log.count("Init Duration"), "access_denied": log.count("AccessDenied")}


def main(out_dir, tag):
    lam = boto3.client("lambda", region_name="us-east-1")
    cfg = lam.get_function_configuration(FunctionName="irpt-status")
    out = {"tag": tag, "at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "code_sha": cfg["CodeSha256"], "reads": {}}
    for name, event in cases().items():
        out["reads"][name] = read_one(lam, event)
        print(name, json.dumps(out["reads"][name]))
    print("code", out["code_sha"], out["at"])
    with open(os.path.join(out_dir, "r3_%s.json" % tag), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
