#!/usr/bin/env python3
"""Round-14 batch repair (NFRA_CTLPLN TO-CT-ad-1, cell CT-ad-1): arms for the four inert round-13 defects.

Arms: (1) routes.tf differs from its base (868b773335) in comment lines only, and its two comments name no deleted
file (W87-S2); (2) check_fence_scoped_rows.py's docstring no longer states the stale premises, and its executable code
equals the base's, so its printed result lines are unchanged on the same inputs (W89-S2; the run itself is the
acceptance criterion CTad1-AC3 and reads AWS, so it is not run here); (3) proof-of-spec-check.py prints the coverage
frame as NOTE:, counts violations= only for real violations, and a clean instance carries no VIOLATION frame
(W91-S2); (4) dell_fence_census.py --live refuses without an explicit --out before any AWS call, an explicit --out
writes the copy and leaves the baseline bytes unchanged, and an explicit --out naming the baseline warns first (W8-S7).

Standard library and temporary directories only. No AWS call: the census is driven in-process with run_live and aws
replaced by recorders, and a stub aws on PATH records any subprocess call; no network, nothing pushed, no terraform.
Run: python .tools/tests/test_round14_batch.py
LAST line: ROUND14-BATCH arms=<k>/<n> ok=<True|False>
"""
from __future__ import annotations

import ast
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
REPO = TOOLS.parent
BASE = "868b773335"  # the issuance commit: the cell's base for every comparison below
ROUTES = "infra/aws/terraform/nfra-ctlpln-identity/routes.tf"
SHARED_TESTS = REPO / "infra" / "aws" / "terraform" / "shared-infra" / "tests"
CHECK_REL = "infra/aws/terraform/shared-infra/tests/check_fence_scoped_rows.py"
CENSUS = SHARED_TESTS / "dell_fence_census.py"
BASELINE = SHARED_TESTS / "dell_fence_census.json"
PROOF = TOOLS / "proof-of-spec-check.py"
PREDECESSOR = (REPO / "org" / "missions" / "D0" / "NFRA" / "NFRA_CTLPLN" / "deliverables" / "0.9.0_WK_NFRA_CTLPLN~87"
               / "NFRA_CTLPLN.TO-CT-ac-1.batch-repair-round12-rows.proof_of_spec.json")
EXPECTED = "CTac1-AC1,CTac1-AC2,CTac1-AC3"
RESULTS = []


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def rm(path) -> None:
    """Remove a temporary tree; git object files are read-only on Windows, so the handler makes each one writable first."""
    shutil.rmtree(path, onerror=lambda f, p, _e: (os.chmod(p, 0o700), f(p)))


def arm(name, fn) -> None:
    try:
        ok, detail = fn()
    except Exception as exc:  # an arm that cannot run is a failed arm, never a skipped one
        ok, detail = False, "%s: %s" % (type(exc).__name__, exc)
    RESULTS.append((name, bool(ok), str(detail)[:200]))


def git(*args) -> str:
    proc = subprocess.run(["git", *args], cwd=str(REPO), capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=120)
    if proc.returncode != 0:
        raise RuntimeError("git %s rc=%s %s" % (args[0], proc.returncode, proc.stderr.strip()[:120]))
    return proc.stdout


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stub_aws(tmp: str) -> Path:
    """Write a stub aws (sh and cmd) into tmp; any call appends its argv to the log and exits 99."""
    log = Path(tmp) / "aws-calls.log"
    (Path(tmp) / "aws").write_text('#!/bin/sh\necho "$@" >> "%s"\nexit 99\n' % log.as_posix(), encoding="utf-8")
    (Path(tmp) / "aws.cmd").write_text('@echo %%* >> "%s"\r\n@exit /b 99\r\n' % str(log), encoding="utf-8")
    return log


# ---------------------------------------------------------------- item 1: routes.tf comments (W87-S2)

def arm_routes_diff_is_comments_only():
    diff = git("diff", "--unified=0", BASE, "--", ROUTES)
    changed = [ln for ln in diff.splitlines()
               if (ln.startswith("+") or ln.startswith("-")) and not ln.startswith(("+++", "---"))]
    non_comment = [ln for ln in changed if not ln[1:].lstrip().startswith("#")]
    return bool(changed) and not non_comment, "changed_lines=%d non_comment=%d" % (len(changed), len(non_comment))


def arm_routes_comments_name_no_deleted_file():
    text = (REPO / ROUTES).read_text(encoding="utf-8")
    named = text.count("simulate_policy")
    authority = text.count("each apply's live policy simulation")
    return named == 0 and authority == 2, "simulate_policy mentions=%d live-simulation authority named=%d" % (named, authority)


# ---------------------------------------------------------------- item 2: fence check docstring (W89-S2)

def exec_tree(src: str) -> str:
    """The module's AST with its docstring removed: equal trees mean equal executable code."""
    tree = ast.parse(src)
    first = tree.body[0] if tree.body else None
    if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant) and isinstance(first.value.value, str):
        tree.body = tree.body[1:]
    return ast.dump(tree)


def arm_check_docstring_rewritten():
    src = (REPO / CHECK_REL).read_text(encoding="utf-8")
    doc = ast.get_docstring(ast.parse(src)) or ""
    stale = [s for s in ("holds no scoped row", "AMENDMENT 7") if s in doc]
    kept = "before_pre" in doc and "AnyOtherAction" in doc and "ListingOutsidePrefix" in doc
    return not stale and kept, "stale=%s premises-stated=%s" % (stale or "none", kept)


def arm_check_executable_code_equals_base():
    tmp = tempfile.mkdtemp(prefix="r14-check-base-")
    try:
        base_copy = Path(tmp) / "check_fence_scoped_rows.base.py"
        base_copy.write_text(git("show", "%s:%s" % (BASE, CHECK_REL)), encoding="utf-8")
        same = exec_tree(base_copy.read_text(encoding="utf-8")) == exec_tree((REPO / CHECK_REL).read_text(encoding="utf-8"))
        return same, "executable code equal to base=%s" % same
    finally:
        rm(tmp)


# ---------------------------------------------------------------- item 3: coverage frame (W91-S2)

def scratch_in_tree(prefix: str) -> str:
    """A temporary directory inside the checkout's ignored .scratch/: proof-of-spec-check refuses (CHECKER-SCOPE) an
    instance outside its own tree, so a coverage fixture cannot sit in the system temp directory."""
    base = REPO / ".scratch"
    base.mkdir(exist_ok=True)
    return tempfile.mkdtemp(prefix=prefix, dir=str(base))


def run_proof(instance: Path, ids: str):
    proc = subprocess.run([sys.executable, str(PROOF), str(instance), ids], cwd=str(REPO), capture_output=True,
                          text=True, encoding="utf-8", errors="replace", timeout=120)
    return proc.returncode, proc.stdout


def violations_count(out: str):
    m = re.search(r"violations=(\d+)", out)
    return int(m.group(1)) if m else None


def arm_coverage_clean_instance_has_no_violation_frame():
    tmp = scratch_in_tree("r14-cov-clean-")
    try:
        inst = Path(tmp) / "instance.json"
        inst.write_bytes(PREDECESSOR.read_bytes())
        rc, out = run_proof(inst, EXPECTED)
        violation_frames = [ln for ln in out.splitlines() if ln.strip().startswith("VIOLATION: coverage-frame")]
        n = violations_count(out)
        return rc == 0 and n == 0 and not violation_frames, "rc=%s violations=%s violation-frames=%d" % (rc, n, len(violation_frames))
    finally:
        rm(tmp)


def arm_coverage_unexpected_row_is_one_violation_with_note_frame():
    tmp = scratch_in_tree("r14-cov-extra-")
    try:
        data = json.loads(PREDECESSOR.read_text(encoding="utf-8"))
        extra = dict(data["acceptance"][0])
        extra["criterion_id"] = "X9"
        data["acceptance"].append(extra)
        inst = Path(tmp) / "instance.json"
        inst.write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")
        rc, out = run_proof(inst, EXPECTED)
        frames = [ln.strip() for ln in out.splitlines() if "coverage-frame" in ln]
        note = any(f.startswith("NOTE: coverage-frame") for f in frames)
        as_violation = any(f.startswith("VIOLATION: coverage-frame") for f in frames)
        n = violations_count(out)
        ok = n == 1 and note and not as_violation and rc == 1
        return ok, "rc=%s violations=%s frame=%s" % (rc, n, frames[0][:70] if frames else "none")
    finally:
        rm(tmp)


# ---------------------------------------------------------------- item 4: census --out (W8-S7)

def arm_census_live_refuses_without_out():
    tmp = tempfile.mkdtemp(prefix="r14-census-refuse-")
    try:
        log = stub_aws(tmp)
        env = dict(os.environ)
        env["PATH"] = tmp + os.pathsep + env.get("PATH", "")
        before = sha(BASELINE)
        proc = subprocess.run([sys.executable, str(CENSUS), "--live"], env=env, capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=120)
        calls = log.read_text(encoding="utf-8") if log.exists() else ""
        ok = proc.returncode != 0 and "--out" in proc.stderr and calls == "" and sha(BASELINE) == before
        return ok, "rc=%s stub_calls=%r baseline_unchanged=%s" % (proc.returncode, calls, sha(BASELINE) == before)
    finally:
        rm(tmp)


def census_module(scratch: Path, calls: list, live_data: dict):
    """The census module with its AWS entry points replaced: run_live returns saved data, and any aws call is recorded and refused."""
    mod = load("dell_fence_census_r14", CENSUS)
    mod.ROOT = scratch  # the temporary directory the live branch creates is kept out of the repository

    def no_aws(args, timeout=90):
        calls.append(list(args))
        raise RuntimeError("AWS call reached in a no-AWS arm: %s" % args[:2])

    def fake_live(_scratch):
        calls.append("run_live")
        return json.loads(json.dumps(live_data))

    mod.aws = no_aws
    mod.run_live = fake_live
    return mod


def run_census_main(mod, argv):
    buf = io.StringIO()
    old = sys.argv
    sys.argv = ["dell_fence_census.py"] + argv
    try:
        with contextlib.redirect_stdout(buf):
            try:
                rc = mod.main()
            except SystemExit as exc:
                rc = exc.code
    finally:
        sys.argv = old
    return rc, buf.getvalue()


def arm_census_live_with_temp_out_keeps_baseline():
    tmp = tempfile.mkdtemp(prefix="r14-census-temp-")
    try:
        before = sha(BASELINE)
        calls = []
        mod = census_module(Path(tmp), calls, json.loads(BASELINE.read_text(encoding="utf-8")))
        out = Path(tmp) / "take.json"
        rc, text = run_census_main(mod, ["--live", "--out", str(out)])
        ok = (rc in (0, None, 1) and calls == ["run_live"] and out.exists() and "saved" in text
              and "WARN: overwriting" not in text and sha(BASELINE) == before)
        return ok, "run_live_calls=%s aws_calls=%d out_written=%s baseline_unchanged=%s" % (
            calls.count("run_live"), len([c for c in calls if isinstance(c, list)]), out.exists(), sha(BASELINE) == before)
    finally:
        rm(tmp)


def arm_census_explicit_baseline_out_warns_first():
    tmp = tempfile.mkdtemp(prefix="r14-census-warn-")
    try:
        before = sha(BASELINE)
        copy = Path(tmp) / "dell_fence_census.json"
        copy.write_bytes(BASELINE.read_bytes())
        calls = []
        mod = census_module(Path(tmp), calls, json.loads(BASELINE.read_text(encoding="utf-8")))
        mod.DEFAULT_JSON = copy  # the baseline path for this arm is the copy; the repository file is never written
        rc, text = run_census_main(mod, ["--live", "--out", str(copy)])
        lines = text.splitlines()
        warn_at = next((i for i, ln in enumerate(lines) if ln.startswith("WARN: overwriting the baseline")), -1)
        saved_at = next((i for i, ln in enumerate(lines) if ln.startswith("saved")), -1)
        ok = calls == ["run_live"] and warn_at == 0 and saved_at > warn_at and sha(BASELINE) == before
        return ok, "warn_line=%d saved_line=%d run_live_calls=%d" % (warn_at, saved_at, calls.count("run_live"))
    finally:
        rm(tmp)


def main() -> int:
    arm("1a routes.tf differs from its base in comment lines only", arm_routes_diff_is_comments_only)
    arm("1b routes.tf comments name no deleted file and state the live-simulation authority", arm_routes_comments_name_no_deleted_file)
    arm("2a the fence check docstring drops the stale premises and states the current ones", arm_check_docstring_rewritten)
    arm("2b the fence check executable code equals the base (result lines unchanged on the same inputs)", arm_check_executable_code_equals_base)
    arm("3a a clean instance carries no VIOLATION coverage-frame line", arm_coverage_clean_instance_has_no_violation_frame)
    arm("3b one unexpected row: violations=1 and the coverage-frame line begins NOTE:", arm_coverage_unexpected_row_is_one_violation_with_note_frame)
    arm("4a --live with no --out refuses before any AWS call, baseline unchanged", arm_census_live_refuses_without_out)
    arm("4b --live with an explicit temporary --out writes the copy, baseline bytes unchanged", arm_census_live_with_temp_out_keeps_baseline)
    arm("4c an explicit --out naming the baseline prints WARN: overwriting the baseline first", arm_census_explicit_baseline_out_warns_first)
    for name, ok, detail in RESULTS:
        print("%s %s%s" % ("ok  " if ok else "FAIL", name, "" if ok else "  -- " + detail))
    good = sum(1 for _, ok, _ in RESULTS if ok)
    print("ROUND14-BATCH arms=%d/%d ok=%s" % (good, len(RESULTS), bool(RESULTS) and good == len(RESULTS)))
    return 0 if RESULTS and good == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
