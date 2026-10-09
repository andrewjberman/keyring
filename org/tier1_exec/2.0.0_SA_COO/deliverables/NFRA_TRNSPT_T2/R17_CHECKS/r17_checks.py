"""NFRA_TRNSPT round 17 -- the issuer's mechanical checks (2.0.0_SA_COO~T2).

  c17   TR17-c17-AC1  the live-ports test file passes and holds, by name, the three tests that close row D2-S8: every env name
                      lambda_handler._live_ports() reads is declared in commentary.tf; the ticket token is the `.token` field of the
                      secret's JSON value; the policy reads the svc-commentary secret and the composition prefix

Prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import re
import subprocess
import sys
from pathlib import Path

TEST = Path("data/transcripts/scripts/tests/test_commentary_live_ports.py")
NAMES = ["test_tf_env_declares_every_live_port_name", "test_token_reader_reads_the_token_field",
         "test_policy_reads_ticket_secret_and_composition"]


def c17():
    if not TEST.exists():
        return False, "absent: %s" % TEST.as_posix()
    text = TEST.read_text(encoding="utf-8")
    missing = [n for n in NAMES if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    r = subprocess.run([sys.executable, "-m", "pytest", str(TEST), "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=110)
    tail = re.sub(r"\x1b\[[0-9;]*m", "", ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1])
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    return (r.returncode == 0 and passed >= 3), tail


CHECKS = {"c17": ("R17-C17", c17)}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in CHECKS:
        print("usage: r17_checks.py {%s}" % "|".join(CHECKS))
        sys.exit(2)
    token, fn = CHECKS[sys.argv[1]]
    ok, why = fn()
    print("%s-%s %s" % (token, "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
