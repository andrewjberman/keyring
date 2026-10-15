#!/usr/bin/env python3
"""test_placement_unstage.py -- CT-af-3 (NFRA_CTLPLN round 16; rows NFRA_CTLPLN-W99-S1 and its twin NFRA_CTLPLN-W93-S1).

The naming stage of .tools/safe-commit.sh has two refusal branches. The ENFORCE branch (CT-ae-3, round 15) unstages EVERY
path the call staged (IN_SCOPE). The PLACEMENT branch (LGIC_BLANKFIX FWD-6, reached while org/mcp/naming-place.enforce is
present) unstaged only the eight graded extensions, so a non-graded deliverable staged beside them stayed in the index after
the refusal. CT-af-3 gives the placement branch the same unstage over IN_SCOPE.

Arms (stdlib; temporary directories and temporary git repositories only; no AWS, no network, no commit anywhere):
  (a) PLACEMENT refusal (org/mcp/naming-place.enforce present; the stub prints NAMING-PLACE: REFUSE and exits 1): a .md and a
      graded .json staged together are BOTH unstaged, rc 1. Control: the base copy leaves the .md staged on the same fixture.
  (b) placement file ABSENT, stub refusing WITH the placement line: the placement branch does not fire; rc, STAGE-REACHED and the
      staged set are identical to the base copy's on the same fixture.
  (c) ENFORCE refusal (naming-gate.enforce on, stub refusing without a placement line): both unstaged, rc 1 (CT-ae-3 behaviour).
  (d) clean pass (stub rc 0) with the placement file present: both stay staged, rc 0.

The naming stage is extracted from .tools/safe-commit.sh (and, for the base copy, from git show BASE_REV) at test time, with the
start line and end marker of .tools/tests/test_safe_commit_derivation.py. The naming gate is a STUB with the live limb switched
off: the real .tools/naming-gate.py is never run.

Run: python .tools/tests/test_placement_unstage.py   (LAST line: PLACEMENT-UNSTAGE arms=<k>/<n> ok=<True|False>)
"""
import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(TESTS_DIR)
WT = os.path.dirname(TOOLS)
SAFE = os.path.join(TOOLS, "safe-commit.sh")
GIT = "git"
BASE_REV = "cb843928c1"  # the round-16 issuance commit: safe-commit.sh before CT-af-3
MD = "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~102/fixture.md"
JSON = "catalog/fixture.json"
ARM_RESULTS = []  # (label, ok)

STUB = '''import os, sys
rc = int(os.environ.get("STUB_RC", "0"))
print("NAMING-GATE: %s 1 graded" % ("REFUSE" if rc else "PASS"))
if rc and os.environ.get("STUB_PLACE") == "1":
    print("NAMING-PLACE: REFUSE 1 graded")
sys.exit(rc)
'''


def load_scd():
    spec = importlib.util.spec_from_file_location("scd_ct_af3", os.path.join(TESTS_DIR, "test_safe_commit_derivation.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


SCD = load_scd()


def arm(label, ok, detail=""):
    ARM_RESULTS.append((label, bool(ok)))
    print("ARM %s %s -- %s" % (label, "PASS" if ok else "FAIL", detail))


def stage_text_of(src):
    lines = src.split("\n")
    starts = [i for i, ln in enumerate(lines) if ln == SCD.STAGE_START]
    if len(starts) != 1:
        raise SystemExit("PLACEMENT-UNSTAGE: the naming stage start line occurs %d times" % len(starts))
    end = next(i for i in range(starts[0] + 1, len(lines)) if lines[i].startswith("# ---"))
    return "\n".join(lines[starts[0]:end]) + "\n"


def base_source():
    proc = subprocess.run([GIT, "-C", WT, "show", "%s:.tools/safe-commit.sh" % BASE_REV], capture_output=True)
    if proc.returncode != 0 or not proc.stdout:
        raise SystemExit("PLACEMENT-UNSTAGE: git show %s failed (rc=%d)" % (BASE_REV, proc.returncode))
    return proc.stdout.decode("utf-8")


def run_case(tmp, label, stage_src, stub_rc, stub_place, naming_enforce, place_enforce):
    """One run of the extracted stage in a fresh temporary repository. Returns (rc, stdout+stderr, staged names)."""
    repo = os.path.join(tmp, "case-" + label)
    os.makedirs(os.path.join(repo, ".tools"))
    subprocess.run([GIT, "-C", repo, "init", "-q"], check=True)
    SCD.write(os.path.join(repo, ".tools", "naming-gate.py"), STUB)
    if place_enforce:
        SCD.write(os.path.join(repo, "org", "mcp", "naming-place.enforce"), "on\n")
    for p in (MD, JSON):
        SCD.write(os.path.join(repo, p), "x\n")
    subprocess.run([GIT, "-C", repo, "add", "--", MD, JSON], check=True)
    tmpdir = os.path.join(repo, ".tmp")
    os.makedirs(tmpdir)
    SCD.write(os.path.join(repo, "msg.txt"), "CT-af-3 fixture commit message\n")
    harness = os.path.join(repo, "harness.sh")
    SCD.write(harness, "set -euo pipefail\n"
              "SCRIPT_DIR=\"%s\"\n"
              "ISO_TS=2026-10-15T00:00:00Z\n"
              "AGENT=0.9.0_WK_NFRA_CTLPLN~102\n"
              "PATHSPEC=(.)\n"
              "COMMIT_ARGS=(-F msg.txt)\n"
              "IN_SCOPE=\"$(git diff --cached --name-only -- \"${PATHSPEC[@]}\")\"\n"
              "%s\n"
              "echo STAGE-REACHED\n" % (SCD.shlash(os.path.join(repo, ".tools")), stage_src))
    env = dict(os.environ, STUB_RC=str(stub_rc), STUB_PLACE="1" if stub_place else "0", TMPDIR=SCD.shlash(tmpdir))
    env.pop("NAMING_PLACE_OVERRIDE", None)
    if naming_enforce:
        env["NAMING_GATE_ENFORCE"] = "1"
    else:
        env.pop("NAMING_GATE_ENFORCE", None)
    proc = subprocess.run([SCD.bash_path(), SCD.shlash(harness)], cwd=repo, env=env, capture_output=True, timeout=120)
    text = (proc.stdout + proc.stderr).decode("utf-8", errors="replace")
    return proc.returncode, text, SCD.staged_names(repo)


def arms(tmp, new, base):
    want = sorted([MD, JSON])

    rc, text, still = run_case(tmp, "a-new", new, 1, True, False, True)
    rc_b, _t, still_b = run_case(tmp, "a-base", base, 1, True, False, True)
    ok_a = rc == 1 and "STAGE-REACHED" not in text and "placement step refused" in text and sorted(still) == []
    ctl_a = rc_b == 1 and sorted(still_b) == [MD]
    arm("a", ok_a and ctl_a, "new rc=%d still=%r | base rc=%d still=%r (control: base keeps the .md staged)"
        % (rc, sorted(still), rc_b, sorted(still_b)))

    rc, text, still = run_case(tmp, "b-new", new, 1, True, False, False)
    rc_b, text_b, still_b = run_case(tmp, "b-base", base, 1, True, False, False)
    same = rc == rc_b and sorted(still) == sorted(still_b) and ("STAGE-REACHED" in text) == ("STAGE-REACHED" in text_b)
    ok_b = same and rc == 0 and sorted(still) == want and "placement step refused" not in text
    arm("b", ok_b, "new rc=%d still=%r | base rc=%d still=%r identical=%s"
        % (rc, sorted(still), rc_b, sorted(still_b), same))

    rc, text, still = run_case(tmp, "c-new", new, 1, False, True, False)
    ok_c = rc == 1 and "STAGE-REACHED" not in text and "the naming limb refused" in text and sorted(still) == []
    arm("c", ok_c, "rc=%d still=%r" % (rc, sorted(still)))

    rc, text, still = run_case(tmp, "d-new", new, 0, False, False, True)
    ok_d = rc == 0 and "STAGE-REACHED" in text and sorted(still) == want
    arm("d", ok_d, "rc=%d still=%r" % (rc, sorted(still)))


def main():
    if SCD.bash_path() is None:
        print("PLACEMENT-UNSTAGE arms=0/4 ok=False")
        return 1
    with open(SAFE, encoding="utf-8") as fh:
        new = stage_text_of(fh.read())
    base = stage_text_of(base_source())
    tmp = tempfile.mkdtemp(prefix="ctaf3-unstage-")
    try:
        arms(tmp, new, base)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    k = sum(1 for _, ok in ARM_RESULTS if ok)
    n = len(ARM_RESULTS)
    print("PLACEMENT-UNSTAGE arms=%d/%d ok=%s" % (k, n, k == n))
    return 0 if k == n else 1


if __name__ == "__main__":
    sys.exit(main())
