"""Read-only observer of one Analysis job (runbook hops 4-7): the irpt-jobs row, until a terminal state.

    python job_watch.py <tenant> [REQ-id] [--timeout 900] [--every 15]

With no REQ-id, the newest REQ- job for the tenant (by accepted order in a consistent Query) is followed. Prints each
change of state, outbox_state and any checkpoint_*/detail key, then the final row's keys. Consistent GetItem only; no
write, no queue access. Terminal: READY, FAILED, ATTENTION (job.py STATES).
"""
import json
import subprocess
import sys
import time

AWS = r"C:\Users\AndrewBerman\Desktop\ajb_workspace\.tools\aws.cmd"
TERMINAL = {"READY", "FAILED", "ATTENTION"}


def aws(*args):
    out = subprocess.run([AWS, *args, "--output", "json"], capture_output=True, text=True)
    if out.returncode:
        raise SystemExit("ERROR: aws %s rc=%d %s" % (args[1], out.returncode, out.stderr.strip()[:200]))
    # get-item on an absent key exits 0 with EMPTY stdout: that is "no row", not an error.
    return json.loads(out.stdout) if out.stdout.strip() else {}


def plain(v):
    t, x = next(iter(v.items()))
    if t == "M":
        return {k: plain(b) for k, b in x.items()}
    if t == "L":
        return [plain(b) for b in x]
    return x


def jobs(tenant):
    items, start = [], None
    while True:
        args = ["dynamodb", "query", "--table-name", "irpt-jobs", "--consistent-read",
                "--key-condition-expression", "tenant = :t AND begins_with(job, :p)",
                "--expression-attribute-values", json.dumps({":t": {"S": tenant}, ":p": {"S": "REQ-"}})]
        if start:
            args += ["--exclusive-start-key", json.dumps(start)]
        page = aws(*args)
        items += page.get("Items", [])
        start = page.get("LastEvaluatedKey")
        if not start:
            return [{k: plain(v) for k, v in i.items()} for i in items]


def row(tenant, job):
    item = aws("dynamodb", "get-item", "--table-name", "irpt-jobs", "--consistent-read",
               "--key", json.dumps({"tenant": {"S": tenant}, "job": {"S": job}})).get("Item")
    return {k: plain(v) for k, v in item.items()} if item else None


def summary(r):
    keep = {k: v for k, v in r.items() if k in ("state", "outbox_state", "request_revision") or k.startswith("checkpoint")}
    detail = r.get("detail")
    if isinstance(detail, str):
        try:
            detail = json.loads(detail)
        except ValueError:
            pass
    if isinstance(detail, dict):
        keep["detail_keys"] = sorted(detail)[:12]
        for k in ("reason", "public_reason_code", "report_id", "revision", "certification_sha256", "error"):
            if k in detail:
                keep["detail." + k] = str(detail[k])[:120]
    return keep


def main(argv):
    tenant = argv[1]
    job = next((a for a in argv[2:] if a.startswith("REQ-")), None)
    timeout = int(argv[argv.index("--timeout") + 1]) if "--timeout" in argv else 900
    every = int(argv[argv.index("--every") + 1]) if "--every" in argv else 15
    if job is None:
        all_jobs = jobs(tenant)
        print("irpt-jobs %s REQ- rows: %d" % (tenant, len(all_jobs)))
        if not all_jobs:
            return 1
        job = all_jobs[-1]["job"]
    print("following", tenant, job)
    last, end = None, time.time() + timeout
    while time.time() < end:
        r = row(tenant, job)
        s = summary(r) if r else {"row": "ABSENT"}
        if s != last:
            print(time.strftime("%H:%M:%SZ", time.gmtime()), json.dumps(s, default=str))
            last = s
        if r and r.get("state") in TERMINAL:
            print("TERMINAL", r.get("state"), "| row keys:", sorted(r))
            return 0
        time.sleep(every)
    print("TIMEOUT after %ds; last %s" % (timeout, json.dumps(last, default=str)))
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
