"""BF-s-8: the proof checker answers VALID or a refusal with its reason when an artifact path is a directory.

Plain script. Default run: build the smallest instance (the shape of the BF-q-6 instance, one artifact row), once with
the row naming a DIRECTORY and once naming a FILE, run the checker, and assert directory=refused (rc 1, reason named,
no traceback), file=valid (rc 0), crash=False. `--self-test` runs the checker's own arms. ASCII only; Python 3.9.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHECKER = ROOT / ".tools" / "proof-of-spec-check.py"
SHAPE = ("org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/"
         "LGIC_BLANKFIX.TO-BF-q-6.every-mapped-root.proof_of_spec.json")
REASON = "is a directory; name its files"


def run(args):
    p = subprocess.run([sys.executable, str(CHECKER)] + args, cwd=str(ROOT), capture_output=True,
                       timeout=120, universal_newlines=True, encoding="utf-8", errors="replace")
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def selftest():
    rc, out = run(["--self-test"])
    line = [x for x in out.splitlines() if x.strip().startswith("RESULT:")]
    n = m = 0
    if line:
        parts = line[-1].replace("RESULT:", "").split()
        try:
            n, m = int(parts[0]), int(parts[2])
        except (IndexError, ValueError):
            n = m = 0
    ok = bool(line) and n == m and m >= 59
    print("PROOF-SELFTEST ok=%s arms=%d behaved=%d" % (ok, m, n))
    return 0 if ok else 1


def main():
    if "--self-test" in sys.argv[1:]:
        return selftest()
    inst = json.loads((ROOT / SHAPE).read_text(encoding="utf-8"))
    inst["artifacts_produced"] = inst["artifacts_produced"][:1]
    crit = inst["acceptance"][0]["criterion_id"]
    work = ROOT / ".scratch" / "proof_dir_test"
    if work.exists():
        shutil.rmtree(str(work))
    (work / "adir").mkdir(parents=True)
    (work / "adir" / "f.txt").write_text("x\n", encoding="utf-8")
    (work / "afile.txt").write_text("x\n", encoding="utf-8")
    res = {}
    try:
        for kind, rel in (("dir", ".scratch/proof_dir_test/adir"), ("file", ".scratch/proof_dir_test/afile.txt")):
            inst["artifacts_produced"][0]["path_or_key"] = rel
            f = work / ("inst_%s.json" % kind)
            f.write_text(json.dumps(inst, indent=1), encoding="utf-8")
            res[kind] = run([str(f.relative_to(ROOT).as_posix()), crit])
    finally:
        shutil.rmtree(str(work), ignore_errors=True)
    drc, dout = res["dir"]
    frc, fout = res["file"]
    refused = drc == 1 and REASON in dout and "INVALID" in dout
    valid = frc == 0 and "VALID (rc=0)" in fout
    crash = any(rc == 2 or "Traceback" in out for rc, out in res.values())
    ok = refused and valid and not crash
    print("PROOF-DIR ok=%s directory=%s file=%s crash=%s" % (
        ok, "refused" if refused else "NOT-refused(rc=%d)" % drc, "valid" if valid else "NOT-valid(rc=%d)" % frc, crash))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
