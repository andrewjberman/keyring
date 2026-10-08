"""NFRA_TRNSPT round 11 -- the issuer's mechanical checks (2.0.0_SA_COO~T2).

  a11-list   TR11-a11-AC1  the versioned securities allowlist exists, names its source file and row counts, and carries the tokens for
                           MSFT/Microsoft, AAPL/Apple, AVGO/Broadcom, NVDA/NVIDIA
  a11-gate   TR11-a11-AC2  the gate test file passes and holds, by name, the planted-token test: a person name, a client name and an
                           account number are wiped while an allowlisted issuer survives

Prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ALLOW = Path("data/transcripts/scripts/teams/securities_allowlist.json")
TEST = Path("data/transcripts/scripts/tests/test_securities_allowlist.py")
NEED = {"msft", "microsoft", "aapl", "apple", "avgo", "broadcom", "nvda", "nvidia"}


def a11_list():
    if not ALLOW.exists():
        return False, "absent: %s" % ALLOW.as_posix()
    doc = json.loads(ALLOW.read_text(encoding="utf-8"))
    prov = doc.get("_provenance") or {}
    if not prov.get("source_file") or not isinstance(prov.get("source_rows"), int):
        return False, "provenance lacks source_file / source_rows"
    toks = {str(t).lower() for t in doc.get("tokens") or []}
    if not toks or doc.get("version") is None:
        return False, "no tokens or no version"
    missing = sorted(NEED - toks)
    if missing:
        return False, "missing tokens: %s" % ", ".join(missing)
    return True, "version=%s tokens=%d source_rows=%d" % (doc["version"], len(toks), prov["source_rows"])


def a11_gate():
    if not TEST.exists():
        return False, "absent: %s" % TEST.as_posix()
    if "def test_gate_person_client_account_wiped_issuer_survives(" not in TEST.read_text(encoding="utf-8"):
        return False, "missing test_gate_person_client_account_wiped_issuer_survives"
    r = subprocess.run([sys.executable, "-m", "pytest", str(TEST), "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=110)
    tail = re.sub(r"\x1b\[[0-9;]*m", "", ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1])
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    return (r.returncode == 0 and passed > 0), tail


CHECKS = {"a11-list": ("R11-A11-LIST", a11_list), "a11-gate": ("R11-A11-GATE", a11_gate)}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in CHECKS:
        print("usage: r11_checks.py {%s}" % "|".join(CHECKS))
        sys.exit(2)
    token, fn = CHECKS[sys.argv[1]]
    ok, why = fn()
    print("%s-%s %s" % (token, "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
