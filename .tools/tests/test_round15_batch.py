#!/usr/bin/env python3
"""test_round15_batch.py -- the round-14 batch repair (NFRA_CTLPLN round 15, cell CT-ae-3, TO NFRA_CTLPLN.TO-CT-ae-3).

Arms (stdlib; temporary directories and temporary git repositories only; no AWS, no network, no commit anywhere):
  (1a) FILES MODE: a roots-named fork row matches the non-Terraform root (matched=1); the base copy (BASE_REV) printed 0.
  (1b) FILES MODE: a no-roots fork row whose project covers no root and whose text names no carried file does not match,
       and the output is byte-identical to the base copy's for the same fixture.
  (1c) FILES MODE: a fork row whose project covers the root keeps its project match; output identical to the base copy.
  (1d) FILES MODE: an act row with no roots still matches nothing.
  (1e) FILES MODE: an act row named by its own roots field still matches (CT-ad-5 kept).
  (2a) NAMING STAGE, ENFORCE on, stub gate refuses: after the refusal the staged .md AND the graded .json are both unstaged.
  (2b) NAMING STAGE, WARN (ENFORCE off), stub gate refuses: the exit code is unchanged and both stay staged.
  (3)  git check-ignore: the --check-fresh checkpoint name is ignored by infra/.gitignore; its neighbour is not ignored.
  (4)  the identity root has no simulate_policy mention in a comment or docstring (positive control: a planted prose mention
       is detected).

The naming stage is extracted from .tools/safe-commit.sh at test time by the same helper that
.tools/tests/test_safe_commit_derivation.py uses, and runs against a stub gate with the live limb OFF (no naming-gate.py
of the worktree is run). The base copy of the crossbox module is read from git at BASE_REV, never from HEAD.

Run: python .tools/tests/test_round15_batch.py   (LAST line: ROUND15-BATCH arms=<k>/<n> ok=<True|False>)
"""
import ast
import datetime
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import tokenize

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(TESTS_DIR)
WT = os.path.dirname(TOOLS)
GIT = shutil.which("git") or "git"
BASE_REV = "cd1e04765b"  # the pre-change commit (the round-15 issuance): the crossbox module before CT-ae-3
CHECK_PATH = os.path.join(TOOLS, "crossbox-deploy-check.py")
IDENTITY = os.path.join(WT, "infra", "aws", "terraform", "nfra-ctlpln-identity")
CHECKPOINT = "infra/aws/terraform/nfra-ctlpln-identity/tests/reached_roles_census.fresh_checkpoint.json"
NEIGHBOUR = "infra/aws/terraform/nfra-ctlpln-identity/tests/reached_roles_census.json"
NEEDLE = "simulate_policy"

DATA_ROOT = "data/black_diamond/scripts/silver"
CARRIED = ["data/black_diamond/scripts/silver/x.py"]
COVERING_IRPT = [("IRPT_BCKEND", "dell2", "infra/aws/terraform/investor-reporting", "placement field")]
NOW = datetime.datetime(2026, 10, 14, 3, 0, 0)
SUBJECT = "Send the execution ID of your own PROD analysis-request submission"

ARM_RESULTS = []  # (label, ok)
CURRENT = None  # the crossbox module as it stands in this worktree (set by arms_files_mode)


def arm(label, ok, detail=""):
    ARM_RESULTS.append((label, bool(ok)))
    print("ARM %s %s%s" % (label, "PASS" if ok else "FAIL", (" -- " + detail) if detail else ""))


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def body(lines):
    """The printed lines without the files-mode header line (the one printed sentence this cell rewords)."""
    return [ln for ln in lines if not ln.startswith("  files mode:")]


def load_base_check():
    """The crossbox module as it stood at BASE_REV, read from git and loaded from a temporary directory."""
    src = subprocess.run([GIT, "-C", WT, "show", "%s:.tools/crossbox-deploy-check.py" % BASE_REV], capture_output=True)
    if src.returncode != 0 or not src.stdout:
        raise SystemExit("ROUND15-BATCH: git show %s failed (rc=%d)" % (BASE_REV, src.returncode))
    d = tempfile.mkdtemp(prefix="r15-base-")
    path = os.path.join(d, "crossbox_base.py")
    with open(path, "wb") as fh:
        fh.write(src.stdout)
    return load_module(path, "crossbox_base"), d


def fixture(rows, root, files, covering, base, label):
    """One temporary repository holding one open_calls file; returns (hits, lines) of measure_open_call for root."""
    tmp = tempfile.mkdtemp(prefix="r15-%s-" % label)
    try:
        state_dir = os.path.join(tmp, "org", "devices", "state", "dell2")
        os.makedirs(state_dir)
        doc = {"schema": "open-calls/1", "device": "dell2", "written_at": "2026-10-13T22:00:00Z",
               "written_by": "fixture", "rows": rows}
        with open(os.path.join(state_dir, "open_calls.json"), "w", encoding="utf-8") as fh:
            json.dump(doc, fh)
        mod = base if base is not None else CURRENT
        return mod.measure_open_call(tmp, root, covering, NOW, files)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def row(rid, kind=None, roots=None, project="IRPT_BCKEND"):
    doc = {"id": rid, "project": project, "subject": SUBJECT, "state": "OPEN", "opened_at": "2026-10-13T21:47:15Z"}
    if kind is not None:
        doc["kind"] = kind
    if roots is not None:
        doc["roots"] = roots
    return doc


def arms_files_mode():
    global CURRENT
    base, base_dir = load_base_check()
    try:
        CURRENT = load_module(CHECK_PATH, "crossbox_new")
        # (1a) roots-named fork row in files mode: new matches, base printed none
        rows = [row("r15-a", kind="fork", roots=[DATA_ROOT], project="SOME_OTHER")]
        h_new, l_new = fixture(rows, DATA_ROOT, CARRIED, [], None, "1a-new")
        h_old, _l_old = fixture(rows, DATA_ROOT, CARRIED, [], base, "1a-old")
        arm("1a", len(h_new) == 1 and len(h_old) == 0 and "names the root in its roots field" in h_new[0]
            and l_new[-1] == "OPEN-CALL calls_scanned=1 matched=1",
            "new matched=%d base matched=%d | %s" % (len(h_new), len(h_old), l_new[-1]))

        # (1b) no-roots fork row, no covering project, text names no carried file: no match; identical to base
        rows = [row("r15-b", kind="fork")]
        h_new, l_new = fixture(rows, DATA_ROOT, CARRIED, [], None, "1b-new")
        h_old, l_old = fixture(rows, DATA_ROOT, CARRIED, [], base, "1b-old")
        arm("1b", len(h_new) == 0 and h_new == h_old and body(l_new) == body(l_old),
            "new matched=%d base matched=%d identical=%s" % (len(h_new), len(h_old), body(l_new) == body(l_old)))

        # (1c) fork row whose project covers the root: the project match is kept; identical to base
        rows = [row("r15-c", kind="fork")]
        h_new, l_new = fixture(rows, DATA_ROOT, CARRIED, COVERING_IRPT, None, "1c-new")
        h_old, l_old = fixture(rows, DATA_ROOT, CARRIED, COVERING_IRPT, base, "1c-old")
        arm("1c", len(h_new) == 1 and h_new == h_old and body(l_new) == body(l_old) and "names project IRPT_BCKEND" in h_new[0],
            "new matched=%d base matched=%d identical=%s" % (len(h_new), len(h_old), body(l_new) == body(l_old)))

        # (1d) act row with no roots matches nothing in files mode
        rows = [row("r15-d", kind="act")]
        h_new, l_new = fixture(rows, DATA_ROOT, CARRIED, COVERING_IRPT, None, "1d-new")
        arm("1d", len(h_new) == 0 and l_new[-1] == "OPEN-CALL calls_scanned=1 matched=0", "matched=%d" % len(h_new))

        # (1e) act row named by its own roots field still matches (CT-ad-5 rule kept)
        rows = [row("r15-e", kind="act", roots=[DATA_ROOT])]
        h_new, l_new = fixture(rows, DATA_ROOT, CARRIED, [], None, "1e-new")
        arm("1e", len(h_new) == 1 and "act row names the root in its roots field" in h_new[0],
            "matched=%d" % len(h_new))
    finally:
        shutil.rmtree(base_dir, ignore_errors=True)


def arms_naming_stage():
    """The derivation test's own extraction and stub harness, reused verbatim (its run_stage, STUB and stage_text)."""
    scd = load_module(os.path.join(TESTS_DIR, "test_safe_commit_derivation.py"), "scd_round15")
    if scd.bash_path() is None:
        arm("2a", False, "no bash found")
        arm("2b", False, "no bash found")
        return
    tmp = tempfile.mkdtemp(prefix="r15-stage-")
    try:
        md = scd.HOME_MCP + "a.md"
        js = "catalog/fixture.json"
        rc, text, _log, still, _t = scd.run_stage(tmp, "r15-enforce", 1, enforce=True)
        arm("2a", rc == 1 and "STAGE-REACHED" not in text and md not in still and js not in still,
            "rc=%d still=%r" % (rc, still))
        rc, text, _log, still, _t = scd.run_stage(tmp, "r15-warn", 1, enforce=False)
        arm("2b", rc == 0 and "STAGE-REACHED" in text and md in still and js in still,
            "rc=%d still=%r" % (rc, still))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def arm_check_ignore():
    def ignored(path):
        proc = subprocess.run([GIT, "-C", WT, "check-ignore", "-v", "--", path], capture_output=True)
        return proc.returncode, proc.stdout.decode("utf-8", errors="replace").strip()
    rc_c, out_c = ignored(CHECKPOINT)
    rc_n, out_n = ignored(NEIGHBOUR)
    print("    check-ignore checkpoint: rc=%d %s" % (rc_c, out_c))
    print("    check-ignore neighbour : rc=%d %s" % (rc_n, out_n or "(not ignored)"))
    arm("3", rc_c == 0 and "infra/.gitignore" in out_c and rc_n == 1,
        "checkpoint rc=%d neighbour rc=%d" % (rc_c, rc_n))


def scan(root):
    """Mentions of NEEDLE per file and class: prose (a comment or a docstring) or code. Returns (prose, code, files)."""
    prose, code, files = [], [], 0
    for dirpath, _dirs, names in os.walk(root):
        for name in names:
            path = os.path.join(dirpath, name)
            files += 1
            try:
                with open(path, encoding="utf-8", errors="replace") as fh:
                    lines = fh.read().split("\n")
            except OSError:
                continue
            if not any(NEEDLE in ln for ln in lines):
                continue
            if name.endswith(".py"):
                prose_lines = _py_prose_lines("\n".join(lines))
            else:
                prose_lines = set()
            for i, ln in enumerate(lines, start=1):
                if NEEDLE not in ln:
                    continue
                s = ln.strip()
                is_prose = i in prose_lines or (not name.endswith(".py") and s.startswith(("#", "//", "/*", "*")))
                (prose if is_prose else code).append("%s:%d" % (os.path.relpath(path, root).replace("\\", "/"), i))
    return prose, code, files


def _py_prose_lines(src):
    """Line numbers that are a comment or inside a docstring of a Python source."""
    out = set()
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type == tokenize.COMMENT:
                out.add(tok.start[0])
        tree = ast.parse(src)
    except (SyntaxError, tokenize.TokenError):
        return out
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and node.body:
            first = node.body[0]
            if isinstance(first, ast.Expr) and isinstance(getattr(first, "value", None), ast.Constant) \
                    and isinstance(first.value.value, str):
                out.update(range(first.lineno, first.end_lineno + 1))
    return out


def arm_identity_text():
    prose, code, files = scan(IDENTITY)
    # positive control: a planted prose mention must be detected as prose, or the scan proves nothing
    tmp = tempfile.mkdtemp(prefix="r15-ctl-")
    try:
        with open(os.path.join(tmp, "ctl.py"), "w", encoding="utf-8") as fh:
            fh.write('"""Docstring that names %s."""\n# comment naming %s\nx = 1\n' % (NEEDLE, NEEDLE))
        ctl_prose, ctl_code, _n = scan(tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("    identity root files scanned: %d; prose mentions: %d %s; code mentions: %d %s"
          % (files, len(prose), prose, len(code), code))
    print("    control: planted prose mentions detected: %d of 2" % len(ctl_prose))
    arm("4", len(prose) == 0 and len(ctl_prose) == 2 and files > 0,
        "identity files=%d prose=%d code=%d control=%d/2" % (files, len(prose), len(code), len(ctl_prose)))


def main():
    arms_files_mode()
    arms_naming_stage()
    arm_check_ignore()
    arm_identity_text()
    k = sum(1 for _l, ok in ARM_RESULTS if ok)
    n = len(ARM_RESULTS)
    print("ROUND15-BATCH arms=%d/%d ok=%s" % (k, n, k == n))
    return 0 if k == n else 1


if __name__ == "__main__":
    sys.exit(main())
