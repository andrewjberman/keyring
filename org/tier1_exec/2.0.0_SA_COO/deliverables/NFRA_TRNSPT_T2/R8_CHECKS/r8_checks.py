"""NFRA_TRNSPT round 8 -- the issuer's mechanical checks (2.0.0_SA_COO~T2), one subcommand per criterion.

  k8-notland  TR8-k8-AC1  the fake-route test that an internal encrypted author email does NOT land passes, by name
  k8-revert   TR8-k8-AC2  the five outlook modules and test_outlook_silver.py are byte-equal to their pre-TR-g7 content (8394179dec,
                          the first parent of merge ff7846f9f7), test_encrypted_class.py is gone, and the Lambda bundle import check passes

Each prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import re
import subprocess
import sys
from pathlib import Path

PRE = "8394179dec"
MODULES = ["data/transcripts/scripts/outlook/%s.py" % m for m in ("criterion", "pull", "land_bronze", "silver", "gold")]
SILVER_TEST = "data/transcripts/scripts/tests/test_outlook_silver.py"
GONE = "data/transcripts/scripts/tests/test_encrypted_class.py"
NEW_TEST = Path("data/transcripts/scripts/tests/test_internal_encrypted_not_landed.py")
BUNDLE = "org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R2_CHECKS/r2_bundle_import_check.py"


def _blob(ref, path):
    r = subprocess.run(["git", "show", "%s:%s" % (ref, path)], capture_output=True, timeout=60)
    if r.returncode != 0 or not r.stdout:
        raise RuntimeError("git show %s:%s rc=%d (empty read is an error)" % (ref, path, r.returncode))
    return r.stdout.replace(b"\r\n", b"\n")


def k8_notland():
    if not NEW_TEST.exists():
        return False, "absent: %s" % NEW_TEST.as_posix()
    if "def test_internal_encrypted_author_email_not_landed(" not in NEW_TEST.read_text(encoding="utf-8"):
        return False, "missing test_internal_encrypted_author_email_not_landed"
    r = subprocess.run([sys.executable, "-m", "pytest", str(NEW_TEST), "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=110)
    tail = re.sub(r"\x1b\[[0-9;]*m", "", ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1])
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    return (r.returncode == 0 and passed > 0), tail


def k8_revert():
    diffs = []
    for path in MODULES + [SILVER_TEST]:
        p = Path(path)
        if not p.exists():
            return False, "absent: %s" % path
        if p.read_bytes().replace(b"\r\n", b"\n") != _blob(PRE, path):
            diffs.append(Path(path).name)
    if diffs:
        return False, "differ from %s: %s" % (PRE, ", ".join(diffs))
    if Path(GONE).exists():
        return False, "still present: %s" % GONE
    r = subprocess.run([sys.executable, BUNDLE], capture_output=True, text=True, timeout=110)
    line = ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1]
    if r.returncode != 0 or "BUNDLE-IMPORT-OK" not in line:
        return False, "bundle: %s" % line
    return True, "6 files == %s; %s; %s" % (PRE, Path(GONE).name + " gone", line)


CHECKS = {"k8-notland": ("R8-K8-NOTLAND", k8_notland), "k8-revert": ("R8-K8-REVERT", k8_revert)}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in CHECKS:
        print("usage: r8_checks.py {%s}" % "|".join(CHECKS))
        sys.exit(2)
    token, fn = CHECKS[sys.argv[1]]
    ok, why = fn()
    print("%s-%s %s" % (token, "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
