#!/usr/bin/env python3
"""test_safe_commit_derivation.py -- CT-ad-2 (NFRA_CTLPLN round 14; row NFRA_MCPINDEX-Z-W34-S8).

The naming gate derives the COMMITTING PROJECT from the paths the commit stages. safe-commit.sh used to hand the gate only
the eight graded extensions, so a graded .json outside a project home plus a .md deliverable under that home derived no
project. The fix: safe-commit.sh passes EVERY in-scope staged path as --staged-paths (derivation only); the gate GRADES the
same eight extensions as before.

Arms (stdlib; temporary directories and temporary git repositories only; no network; no commit anywhere):
  (a) POSITIVE  a graded .json outside any project home + a .md under NFRA_MCPINDEX staged together derive NFRA_MCPINDEX
                and the registered legacy literal grades CONFORMANT; without the staged list it is REFUSE (rc 1).
  (b) a .md under a project home is never graded: no verdict names it, and a literal planted in it produces none.
  (c) staged paths under TWO project homes derive None (REFUSE, rc 1).
  (d) a foreign-home path that exists in the repository but is NOT staged derives nothing (staged paths only).
  (e) with no --staged-paths the gate's output and exit code on identical diffs are byte-identical to the base copy
      (git show BASE_REV:.tools/naming-gate.py, loaded from a temporary directory and pointed at the same repository).
  (f) an empty and an unreadable --staged-paths file fall back to today's result and exit code, with one NOTE line.
  (S) the naming stage of .tools/safe-commit.sh, extracted VERBATIM from the script at test time and run in a temporary
      repository against a stub gate: it passes --staged-paths with every in-scope path (a space in a path included), the
      --diff holds only the graded extensions, the derivation file is removed, WARN never changes the exit code and
      ENFORCE still stops the commit (fail-closed) and unstages every in-scope path it staged (W93-S1, round 15).

Final line: SAFE-COMMIT-DERIVATION cases=<k>/<n> ok=<True|False>
"""
import ast
import contextlib
import importlib.util
import io
import os
import shutil
import subprocess
import sys
import tempfile

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
WT = os.path.dirname(os.path.dirname(TESTS_DIR))
GATE = os.path.join(WT, ".tools", "naming-gate.py")
SAFE = os.path.join(WT, ".tools", "safe-commit.sh")
BASE_REV = "868b773335"  # the order's base commit: the gate and the stage as they stood before CT-ad-2
LIT_KEY = "harvest-gold-research-backlog"  # the registry key; LIT is lib/opal_naming.py legacy_address(LIT_KEY), read at run time
LIT = None
HOME_MCP = "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/"
HOME_CTL = "org/missions/D9/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~1/"
HOME_FOREIGN = "org/missions/D9/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~9/"
STAGE_START = 'if [ -n "$IN_SCOPE" ] && [ -f "$SCRIPT_DIR/naming-gate.py" ]; then'
CASES = []  # (name, ok)


def check(name, ok, detail=""):
    CASES.append((name, bool(ok)))
    print("CHECK %s %s%s" % ("PASS" if ok else "FAIL", name, (" -- " + detail) if detail else ""))


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def point_at_worktree(mod, tmp):
    """Read the worktree's registry and lib (read-only); keep the verdict log and the enforce switch inside the temp dir."""
    mod.REPO = WT
    mod.OPAL_PATH = os.path.join(WT, "lib", "opal_naming.py")
    mod.VERDICT_LOG = os.path.join(tmp, "verdicts.log")
    mod.ENFORCE_FILE = os.path.join(tmp, "no-naming-gate.enforce")
    mod._live_read_plane = None  # the live limb reads the AWS plane for S3 literals: switched OFF here (no AWS, no network)
    return mod


def run_gate(mod, argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        rc = mod.main(argv)
    return rc, out.getvalue(), err.getvalue()


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def add_diff(path, lines):
    body = "".join("+%s\n" % ln for ln in lines)
    return "--- /dev/null\n+++ b/%s\n@@ -0,0 +1,%d @@\n%s" % (path, len(lines), body)


def json_fixture(lit):
    return ["{", '  "prefix": "%s"' % lit, "}"]


def verdict_lines(out):
    return [ln for ln in out.split("\n") if ln.startswith("NAMING ")]


def bash_path():
    for cand in ("C:/Program Files/Git/bin/bash.exe", "C:/Program Files/Git/usr/bin/bash.exe"):
        if os.path.isfile(cand):
            return cand
    return shutil.which("bash")


def git_bin():
    return shutil.which("git") or "git"


def main():
    tmp = tempfile.mkdtemp(prefix="ctad2-derive-")
    try:
        new = point_at_worktree(load_module(GATE, "naming_gate_new"), tmp)
        opal = new.load_opal()
        global LIT
        LIT = opal.legacy_address(LIT_KEY)
        check("pre: the registered legacy literal resolves through legacy_address() (an S3 address)",
              isinstance(LIT, str) and LIT.startswith("s3://"), "%s" % (LIT,))

        d_json = os.path.join(tmp, "fixture.diff")
        write(d_json, add_diff("catalog/fixture.json", json_fixture(LIT)))
        s_pos = os.path.join(tmp, "staged-pos.txt")
        write(s_pos, "catalog/fixture.json\n%sa.md\n" % HOME_MCP)

        # (a) POSITIVE and its negative control (the same diff without the staged list)
        rc, out, err = run_gate(new, ["--diff", d_json, "--enforce", "--staged-paths", s_pos])
        check("(a) positive: derives NFRA_MCPINDEX from the staged .md under its home",
              new._LEGACY["project"] == "NFRA_MCPINDEX", "derived=%r" % new._LEGACY["project"])
        check("(a) positive: the .json literal grades CONFORMANT, rc 0",
              rc == 0 and "NAMING CONFORMANT catalog/fixture.json:2 " in out and "NAMING-GATE: PASS 1 graded" in out,
              "rc=%d %s" % (rc, verdict_lines(out)[:1]))
        rc, out, err = run_gate(new, ["--diff", d_json, "--enforce"])
        check("(a) control: without --staged-paths the same diff derives None and is REFUSE, rc 1",
              new._LEGACY["project"] is None and rc == 1 and "NAMING-GATE: REFUSE 1 graded" in out,
              "rc=%d derived=%r" % (rc, new._LEGACY["project"]))

        # (b) a .md under a project home is never graded
        planted = os.path.join(tmp, "planted.md")
        write(planted, "notes with the literal %s planted in it\n" % LIT)
        s_md = os.path.join(tmp, "staged-md.txt")
        write(s_md, "catalog/fixture.json\n%snotes.md\n" % HOME_MCP)
        rc, out, err = run_gate(new, ["--diff", d_json, "--enforce", "--staged-paths", s_md])
        check("(b) a .md under a project home produces no verdict and the literal in it is not graded",
              not any(".md" in ln for ln in verdict_lines(out)) and len(verdict_lines(out)) == 1,
              "verdict lines=%d" % len(verdict_lines(out)))

        # (c) staged paths under two project homes derive None
        s_two = os.path.join(tmp, "staged-two.txt")
        write(s_two, "catalog/fixture.json\n%sa.md\n%sb.md\n" % (HOME_MCP, HOME_CTL))
        rc, out, err = run_gate(new, ["--diff", d_json, "--enforce", "--staged-paths", s_two])
        check("(c) two project homes staged: derives None, REFUSE rc 1",
              new._LEGACY["project"] is None and rc == 1, "derived=%r rc=%d" % (new._LEGACY["project"], rc))

        # (d) a foreign home that exists in the repository but is NOT staged derives nothing
        repo = os.path.join(tmp, "repo-d")
        os.makedirs(repo)
        subprocess.run([git_bin(), "-C", repo, "init", "-q"], check=True)
        write(os.path.join(repo, "catalog", "fixture.json"), "{}\n")
        write(os.path.join(repo, HOME_FOREIGN, "c.md"), "# foreign, unstaged\n")
        subprocess.run([git_bin(), "-C", repo, "add", "--", "catalog/fixture.json"], check=True)
        listing = subprocess.run([git_bin(), "-C", repo, "diff", "--cached", "--name-only"], capture_output=True, check=True)
        staged_now = listing.stdout.decode("utf-8").splitlines()
        s_d = os.path.join(tmp, "staged-d.txt")
        write(s_d, "\n".join(staged_now) + "\n")
        rc, out, err = run_gate(new, ["--diff", d_json, "--enforce", "--staged-paths", s_d])
        check("(d) unstaged foreign home in the repository derives nothing (staged list = %s)" % staged_now,
              staged_now == ["catalog/fixture.json"] and new._LEGACY["project"] is None and rc == 1,
              "derived=%r rc=%d" % (new._LEGACY["project"], rc))

        # (e) with no --staged-paths: byte-identical to the base copy on identical diffs
        base_src = subprocess.run([git_bin(), "-C", WT, "show", "%s:.tools/naming-gate.py" % BASE_REV], capture_output=True)
        check("(e) base copy read from git (rc 0, non-empty)", base_src.returncode == 0 and len(base_src.stdout) > 0,
              "rc=%d bytes=%d" % (base_src.returncode, len(base_src.stdout)))
        base_dir = os.path.join(tmp, "base-copy")
        os.makedirs(base_dir)
        base_file = os.path.join(base_dir, "naming-gate.py")
        with open(base_file, "wb") as fh:
            fh.write(base_src.stdout)
        base = point_at_worktree(load_module(base_file, "naming_gate_base"), tmp)
        d_mixed = os.path.join(tmp, "mixed.diff")
        write(d_mixed, add_diff("catalog/fixture.json", json_fixture(LIT)) + add_diff("catalog/plain.json", ['{"k": "v"}']))
        identical = True
        for diff_path in (d_json, d_mixed):
            for extra in ([], ["--enforce"]):
                argv = ["--diff", diff_path] + extra
                got_b = run_gate(base, argv)
                got_n = run_gate(new, argv)
                identical = identical and got_b == got_n
        check("(e) no --staged-paths: stdout, stderr and rc identical to the base copy on 4 argv variants", identical)

        # (f) empty and unreadable --staged-paths fall back to today's result, with one NOTE line
        s_empty = os.path.join(tmp, "staged-empty.txt")
        write(s_empty, "")
        base_rc, base_out, base_err = run_gate(new, ["--diff", d_json, "--enforce"])
        for label, arg in (("empty", s_empty), ("unreadable", os.path.join(tmp, "repo-d"))):
            rc, out, err = run_gate(new, ["--diff", d_json, "--enforce", "--staged-paths", arg])
            notes = [ln for ln in err.split("\n") if ln.strip()]
            check("(f) %s --staged-paths: same stdout and rc as no option, one NOTE line on stderr" % label,
                  out == base_out and rc == base_rc and len(notes) == 1 and notes[0].startswith("NOTE:")
                  and new._LEGACY["project"] is None,
                  "rc=%d notes=%d" % (rc, len(notes)))

        check_stage(tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    k = sum(1 for _n, ok in CASES if ok)
    n = len(CASES)
    print("SAFE-COMMIT-DERIVATION cases=%d/%d ok=%s" % (k, n, k == n))
    return 0 if k == n else 1


STUB = '''import os, sys
argv = sys.argv[1:]
log = os.environ["STUB_LOG"]
def val(flag):
    return argv[argv.index(flag) + 1] if flag in argv else None
diff_path, staged = val("--diff"), val("--staged-paths")
rc = int(os.environ.get("STUB_RC", "0"))
with open(log, "a", encoding="utf-8", newline="\\n") as fh:
    fh.write("ARGV " + repr(argv) + "\\n")
    fh.write("DIFF " + repr([ln for ln in open(diff_path, encoding="utf-8").read().split("\\n") if ln.startswith("+++ ")]) + "\\n")
    fh.write("STAGED-FILE " + repr(staged) + "\\n")
    if staged and os.path.exists(staged):
        fh.write("STAGED " + repr(open(staged, encoding="utf-8").read().split("\\n")) + "\\n")
print("NAMING-GATE: %s 0 graded" % ("REFUSE" if rc else "PASS"))
sys.exit(rc)
'''


def stage_text():
    with open(SAFE, encoding="utf-8") as fh:
        src = fh.read().split("\n")
    starts = [i for i, ln in enumerate(src) if ln == STAGE_START]
    if len(starts) != 1:
        raise SystemExit("SAFE-COMMIT-DERIVATION: the naming stage start line occurs %d times" % len(starts))
    end = next(i for i in range(starts[0] + 1, len(src)) if src[i].startswith("# ---"))
    return "\n".join(src[starts[0]:end]) + "\n"


def run_stage(tmp, label, stub_rc, enforce):
    """One run of the extracted stage in a fresh temporary repository. Returns (rc, stdout+stderr, log lines, repo, tmpdir)."""
    repo = os.path.join(tmp, "stage-" + label)
    os.makedirs(os.path.join(repo, ".tools"))
    subprocess.run([git_bin(), "-C", repo, "init", "-q"], check=True)
    write(os.path.join(repo, ".tools", "naming-gate.py"), STUB)
    paths = ["catalog/fixture.json", "catalog/my fixture.json", HOME_MCP + "a.md", HOME_MCP + "my notes.md"]
    for p in paths:
        write(os.path.join(repo, p), "x\n")
    subprocess.run([git_bin(), "-C", repo, "add", "--"] + paths, check=True)
    tmpdir = os.path.join(repo, ".tmp")
    os.makedirs(tmpdir)
    log = os.path.join(repo, "stub.log")
    harness = os.path.join(repo, "harness.sh")
    write(harness, "set -euo pipefail\n"
          "SCRIPT_DIR=\"%s\"\n"
          "ISO_TS=2026-10-14T00:00:00Z\n"
          "AGENT=0.9.0_WK_NFRA_CTLPLN~93\n"
          "PATHSPEC=(.)\n"
          "COMMIT_ARGS=(-F msg.txt)\n"
          "IN_SCOPE=\"$(git diff --cached --name-only -- \"${PATHSPEC[@]}\")\"\n"
          "%s\n"
          "echo STAGE-REACHED\n" % (shlash(os.path.join(repo, ".tools")), stage_text()))
    env = dict(os.environ, STUB_LOG=shlash(log), STUB_RC=str(stub_rc), TMPDIR=shlash(tmpdir))
    if enforce:
        env["NAMING_GATE_ENFORCE"] = "1"
    else:
        env.pop("NAMING_GATE_ENFORCE", None)
    env.pop("NAMING_PLACE_OVERRIDE", None)
    proc = subprocess.run([bash_path(), shlash(harness)], cwd=repo, env=env, capture_output=True, timeout=120)
    text = (proc.stdout + proc.stderr).decode("utf-8", errors="replace")
    logtxt = open(log, encoding="utf-8", errors="replace").read().split("\n") if os.path.exists(log) else []
    still = staged_names(repo)
    return proc.returncode, text, logtxt, still, tmpdir


def staged_names(repo):
    out = subprocess.run([git_bin(), "-C", repo, "diff", "--cached", "--name-only"], capture_output=True, check=True)
    return out.stdout.decode("utf-8").splitlines()


def shlash(p):
    return p.replace("\\", "/")


def check_stage(tmp):
    if bash_path() is None:
        check("(S) bash available for the stage harness", False, "no bash found")
        return
    all_paths = sorted(["catalog/fixture.json", "catalog/my fixture.json", HOME_MCP + "a.md", HOME_MCP + "my notes.md"])
    graded = sorted(["catalog/fixture.json", "catalog/my fixture.json"])
    rc, text, logtxt, still, tmpdir = run_stage(tmp, "warn-ok", 0, enforce=False)
    argv_line = next((ln for ln in logtxt if ln.startswith("ARGV ")), "")
    staged_line = next((ln for ln in logtxt if ln.startswith("STAGED ")), "")
    diff_line = next((ln for ln in logtxt if ln.startswith("DIFF ")), "")
    staged_file = next((ln for ln in logtxt if ln.startswith("STAGED-FILE ")), "")
    staged_got = sorted(x for x in ast.literal_eval(staged_line[len("STAGED "):]) if x) if staged_line else None
    check("(S) WARN: the stage reaches its end and the gate gets --staged-paths", rc == 0 and "STAGE-REACHED" in text
          and "--staged-paths" in argv_line, "rc=%d" % rc)
    check("(S) the staged file lists every in-scope path, a spaced path included (%d paths)" % len(all_paths),
          staged_got == all_paths, "got=%r" % (staged_got,))
    diff_got = sorted(h.split("\t")[0] for h in ast.literal_eval(diff_line[len("DIFF "):])) if diff_line else None
    check("(S) the --diff carries only the graded extensions (no .md)",
          diff_got == ["+++ b/" + g for g in graded], "diff=%r" % (diff_got,))
    leftover = [f for f in os.listdir(tmpdir) if f.startswith("naming-staged.")]
    staged_path = ast.literal_eval(staged_file[len("STAGED-FILE "):]) if staged_file else None
    check("(S) the derivation file is removed after the stage", staged_path is not None and not leftover
          and not os.path.exists(staged_path), "leftover=%r" % leftover)
    rc, text, logtxt, still, _t = run_stage(tmp, "warn-rc1", 1, enforce=False)
    check("(S) WARN: a gate REFUSE (stub rc 1) does not change the stage exit code", rc == 0 and "STAGE-REACHED" in text,
          "rc=%d" % rc)
    rc, text, logtxt, still, _t = run_stage(tmp, "enforce-rc1", 1, enforce=True)
    # W93-S1 (NFRA_CTLPLN round 15, CT-ae-3): the refusal unstages EVERY path this call staged, the .md deliverables included
    check("(S) ENFORCE: a gate REFUSE still stops the commit (rc 1) and unstages every in-scope path (W93-S1)",
          rc == 1 and "STAGE-REACHED" not in text and sorted(still) == [], "rc=%d still=%r" % (rc, still))


if __name__ == "__main__":
    sys.exit(main())
