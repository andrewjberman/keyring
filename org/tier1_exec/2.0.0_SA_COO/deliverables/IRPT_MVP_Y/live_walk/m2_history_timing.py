#!/usr/bin/env python3
"""Row S270 M2, measured OFFLINE against the LIVE tables (CTO rulings batch 171): the owned-request history at the M2
commit, sequential (1 worker) against the pool (8 workers), same principal, same page.

    python m2_history_timing.py <ir-source-root> <out.json> [--runs 2]

<ir-source-root> is infra/aws/lambda/investor-reporting in the worktree checked out at the M2 commit. The real
`status_installed.compose_ports` composes the ports with live boto3 clients (reads only: DynamoDB GetItem/Query, S3
Head/Get); writes nothing. The principal is the service principal's recorded owner identity for Cottonwood. Each
configuration is run `--runs` times after one warm-up; wall times and the answer (item ids, order) are compared. This
is a laptop measurement: absolute times include the laptop's distance to us-east-1, so the RATIO is the reading; the
served REPORT duration after the apply is the acceptance. ASCII only.
"""
import json
import os
import sys
import time


def main(argv):
    root, out = argv[1], argv[2]
    runs = int(argv[argv.index("--runs") + 1]) if "--runs" in argv else 2
    repo = os.path.abspath(os.path.join(root, "..", "..", "..", ".."))
    for sub in ("ops", "reports", "ycharts/generate", "_authz", "_scope", "_ids", "_keys", "intake", "directory"):
        sys.path.insert(0, os.path.join(root, sub))
    sys.path.insert(0, os.path.join(repo, "lib"))
    os.environ.setdefault("AWS_REGION", "us-east-1")
    os.environ.setdefault("IRPT_DIRECTORY_BUCKET_MAP", json.dumps(
        {"49financial": "opal-data-bd", "cottonwood": "opal-data-cot", "inflection": "opal-data-inf"}))
    import owned_requests
    import status_installed as si
    print("owned_requests from", os.path.relpath(owned_requests.__file__, repo), "| HISTORY_WORKERS",
          owned_requests.HISTORY_WORKERS)
    env = {si.REQUESTS_TABLE_ENV: "irpt-requests", si.JOBS_TABLE_ENV: "irpt-jobs"}
    ports = si.compose_ports(environ=env)
    reader = ports["requests"]
    principal = {"firm_id": "cottonwood", "home_firm_id": "opal-capital",
                 "principal_id": "svc-irpt-analysis@opalinvest.com", "principal_class": "OPAL_GLOBAL"}
    result = {"runs": runs, "configs": {}}
    answers = {}
    for workers in (1, 8):
        owned_requests.HISTORY_WORKERS = workers
        reader.history(principal, limit=50, data_firm="cottonwood")  # warm-up
        walls = []
        for _ in range(runs):
            t0 = time.time()
            page = reader.history(principal, limit=50, data_firm="cottonwood")
            walls.append(round(time.time() - t0, 2))
        answers[workers] = [item["identity"]["request_id"] for item in page["items"]]
        result["configs"][str(workers)] = {"walls_s": walls, "items": len(page["items"])}
        print("workers %d: items %d, wall %s s" % (workers, len(page["items"]), walls))
    result["same_answer_in_same_order"] = answers[1] == answers[8]
    best1, best8 = min(result["configs"]["1"]["walls_s"]), min(result["configs"]["8"]["walls_s"])
    result["speedup"] = round(best1 / best8, 2) if best8 else None
    print("same answer, same order: %s | speedup (best of runs) %.2fx" % (result["same_answer_in_same_order"],
                                                                        result["speedup"] or 0))
    json.dump(result, open(out, "w", encoding="utf-8", newline="\n"), indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
