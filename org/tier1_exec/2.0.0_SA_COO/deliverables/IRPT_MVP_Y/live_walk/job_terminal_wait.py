"""Block until ONE Analysis job reaches a terminal state, then hold a floor. Read-only.

    python job_terminal_wait.py <tenant> <REQ-id> [--floor 20] [--deadline 2026-09-29T18:18:34+00:00]

W24 serializes on the IRPT-JOBS row terminal, not the NORMALIZATION row (1.0.0_SA_CTO's condition 1 on packet blob
49148a2d2a): W22 failed while a GENERATION was in flight, so waiting for the upload to normalize is not enough.
live_chain.py returns as soon as its K5 POST is accepted, so the caller runs this between bodies.

Terminal is READY / FAILED / ATTENTION (job.py STATES). Prints each state change and the terminal row's
job_detail.code when there is one. Consistent Query only; no write, no queue access, no vendor call. Exit 0 on a
terminal state, 2 on the deadline, 3 on a read that never found the row.
"""
import argparse
import datetime
import json
import subprocess
import time

AWS = r"C:\Users\AndrewBerman\Desktop\ajb_workspace\.tools\aws.cmd"
TERMINAL = ("READY", "FAILED", "ATTENTION")


def now():
    return datetime.datetime.now(datetime.timezone.utc)


def say(*parts):
    print(now().strftime("%H:%M:%SZ"), *parts, flush=True)


def row(tenant, req):
    """The job row, or None. A failed read returns None and is never read as 'no job'."""
    out = subprocess.run(
        [AWS, "dynamodb", "query", "--table-name", "irpt-jobs", "--consistent-read",
         "--key-condition-expression", "tenant = :t AND begins_with(job, :p)",
         "--expression-attribute-values",
         json.dumps({":t": {"S": tenant}, ":p": {"S": req}}), "--output", "json"],
        capture_output=True, text=True)
    if out.returncode != 0 or not out.stdout.strip():
        say("WARN: read rc=%d %s" % (out.returncode, out.stderr.strip()[:160]))
        return None
    items = json.loads(out.stdout).get("Items", [])
    return items[0] if items else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tenant")
    ap.add_argument("request_id")
    ap.add_argument("--floor", type=int, default=20, help="seconds to hold AFTER terminal, before the next body")
    ap.add_argument("--deadline", default=None, help="ISO8601; the window cap")
    ap.add_argument("--every", type=int, default=15)
    args = ap.parse_args()
    deadline = datetime.datetime.fromisoformat(args.deadline) if args.deadline else None

    seen = None
    found = False
    while True:
        if deadline is not None and now() >= deadline:
            say("DEADLINE reached with state", seen, "-- not terminal")
            return 2
        item = row(args.tenant, args.request_id)
        if item is not None:
            found = True
            state = item.get("state", {}).get("S")
            if state != seen:
                detail = item.get("job_detail", {}).get("S")
                say("state", state, "| outbox", item.get("outbox_state", {}).get("S"),
                    ("| detail " + detail) if detail else "")
                seen = state
            if state in TERMINAL:
                say("TERMINAL", state, "-- holding the %d s floor before the next body" % args.floor)
                time.sleep(args.floor)
                say("floor held; next body may start")
                return 0
        time.sleep(args.every)
    return 3 if not found else 0


if __name__ == "__main__":
    raise SystemExit(main())
