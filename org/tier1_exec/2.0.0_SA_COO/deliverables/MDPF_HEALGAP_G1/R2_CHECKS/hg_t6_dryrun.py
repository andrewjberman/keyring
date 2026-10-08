"""MDPF_HEALGAP round 2, HG-t-6 (FWD-3) criterion AC2: the two acts, dry-run against the real bucket (read-only).

Runs from the worktree root, each with --dry-run (no S3 write, no Lambda invoke, no vendor call):
  1. repair.py --date <a past date, 2026-09-01> --dry-run  -> must print a line starting `REFUSED ` that names the
     reason (the source serves current state only), and exit non-zero;
  2. repair.py --date <today UTC> --dry-run                 -> must print a line starting `MANIFEST ` (the date and the
     feeds it would fetch) or `NOTHING-TO-REPAIR ` (all three feeds already present), and no `INVOKED` line;
  3. mark_missing.py --from 2026-08-31 --to 2026-09-10 --feed rebalancer_model_detail --dry-run
                                                            -> must print exactly 11 `WOULD-MARK ` lines, one per day,
     and no `WROTE ` line.
DRYRUN-OK when all three hold; else DRYRUN-BAD <which>.
"""
from __future__ import annotations

import os
import subprocess
import sys
from datetime import datetime, timezone

RUNNER = os.path.join("infra", "aws", "lambda", "cot-pipeline", "cot-rebalancer-runner")


def _run(args: list[str]) -> tuple[int, str]:
    env = dict(os.environ)
    env.setdefault("AWS_DEFAULT_REGION", "us-east-1")
    r = subprocess.run([sys.executable] + args, capture_output=True, text=True, timeout=170, check=False,
                       cwd=RUNNER, env=env)
    return r.returncode, r.stdout + r.stderr


def main() -> int:
    for f in ("repair.py", "mark_missing.py"):
        if not os.path.isfile(os.path.join(RUNNER, f)):
            print("DRYRUN-BAD no file " + os.path.join(RUNNER, f))
            return 1
    bad = []
    rc, out = _run(["repair.py", "--date", "2026-09-01", "--dry-run"])
    print("[past] rc=%d\n%s" % (rc, out[-800:]))
    if rc == 0 or not any(ln.startswith("REFUSED ") for ln in out.splitlines()):
        bad.append("past-date not REFUSED")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    rc, out = _run(["repair.py", "--date", today, "--dry-run"])
    print("[today %s] rc=%d\n%s" % (today, rc, out[-800:]))
    lines = out.splitlines()
    if not any(ln.startswith(("MANIFEST ", "NOTHING-TO-REPAIR ")) for ln in lines) or any(ln.startswith("INVOKED") for ln in lines):
        bad.append("today dry-run gave no MANIFEST/NOTHING-TO-REPAIR or invoked")
    rc, out = _run(["mark_missing.py", "--from", "2026-08-31", "--to", "2026-09-10",
                    "--feed", "rebalancer_model_detail", "--dry-run"])
    print("[mark] rc=%d\n%s" % (rc, out[-1500:]))
    lines = out.splitlines()
    n = sum(1 for ln in lines if ln.startswith("WOULD-MARK "))
    if n != 11 or any(ln.startswith("WROTE ") for ln in lines):
        bad.append("mark dry-run WOULD-MARK=%d (want 11) or wrote" % n)
    if bad:
        print("DRYRUN-BAD " + "; ".join(bad))
        return 1
    print("DRYRUN-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
