#!/usr/bin/env python3
"""Cases for .tools/apply-who-check.py, .tools/crossbox-deploy-check.py and their one block in each wrapper
(NFRA_CTLPLN workstream SEATS, cell CT-s-3).

Run: python .tools/tests/test_apply_who_and_crossbox.py   (LAST line: APPLY-GATES-TEST cases=<k>/<n> ok=<True|False>)

AMENDMENT 1 cases: (1) four switch files, one per check per wrapper, in a scratch tree's org/mcp/ (or the directory named by
the test-only variable OPAL_SEAT_GATES_ENFORCE_DIR); (2) a check with no verdict BLOCKS under its own switch and only WARNs
without it; (3) safe-deploy's apply-who runs only when the deploy core would deploy a file (the fixture carries a STUB core with
the real core's function names, so no deploy can run; the helper is also proved against a byte copy of the REAL core, imported,
never run); (4) OVERLAP is judged on carried files (--files, --files-from, --files-vs-trunk); (5) seat-gates-dry-pass.py.

Everything is built in a temporary directory: a scratch git repository (a template, copied once per case) holding COPIES of
the tools and wrappers and the files they read (device register, projects, notices, cross-box calls, open-deploy sentinels).
The enforce file is created only in a scratch tree (or at a temp path named by OPAL_SEAT_GATES_ENFORCE_FILE), never in the
real tree. The wrappers run only through --dry-seat-gates, or as far as the scratch tree's missing halt-gate/core file (the
proof that the flow went on); the terraform named to them is a fake that writes a marker if it is ever called. No terraform,
no AWS call, no deploy, no network. Cases are independent and run on a small thread pool (each wrapper run costs seconds
of process start-up here), reported in order.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import git_bash_resolver  # noqa: E402  the estate's canonical Git Bash, never a bare `bash`

PIN = "8f761307bf"  # the commit the two wrappers are compared against: before this cell's block was added
FIRST_PASS = "ed1adcaa72"  # the commit the cell stood at when AMENDMENT 1 reopened it (the first pass's block)
ROOT_REL = "infra/aws/terraform/rootx"
PIPE_REL = "data/pipea"
RES = "aws_cloudwatch_event_target.guarded"
NOW_LIVE = "2026-10-08T05:00:00Z"
NOW_AFTER = "2026-10-08T07:00:00Z"
COPIES = [".tools/safe-apply.sh", ".tools/safe-deploy.sh", ".tools/apply-who-check.py", ".tools/crossbox-deploy-check.py",
          ".tools/placement-check.py", ".tools/lib/resolve-actor.sh", "lib/devices.py", "org/devices/DEVICES.json",
          ".tools/seat-gates-dry-pass.py"]
SWITCHES = ["apply-who.safe-apply", "apply-who.safe-deploy", "crossbox.safe-apply", "crossbox.safe-deploy"]
# A stub of .tools/safe_deploy_core.py: the real function names the helper imports, a tiny rule, and a main() that only prints.
STUB_CORE = (
    "import pathlib, subprocess, sys\n"
    "WORKSPACE = pathlib.Path(__file__).parent.parent\n"
    "def _changed_paths(commit_range):\n"
    "    r = subprocess.run(['git', 'diff', '--name-only', '--diff-filter=ACMRT', commit_range or 'HEAD~1..HEAD'],\n"
    "                       capture_output=True, text=True, cwd=str(WORKSPACE))\n"
    "    return [x.strip() for x in r.stdout.splitlines() if x.strip()]\n"
    "def file_to_s3_target(rel):\n"
    "    return ('b', 'k', 'l') if rel.startswith('data/pipea/scripts/gold/') and rel.endswith('.py') else None\n"
    "def detect_script_files(commit_range=None, explicit_files=None):\n"
    "    pool = explicit_files if explicit_files else _changed_paths(commit_range)\n"
    "    return [f for f in pool if file_to_s3_target(f)]\n"
    "def detect_bundle_member_files(commit_range=None, explicit_files=None):\n"
    "    pool = explicit_files if explicit_files else _changed_paths(commit_range)\n"
    "    return [f for f in pool if f == 'data/pipea/config/roster.json']\n"
    "if __name__ == '__main__':\n"
    "    print('STUB-CORE-RAN', sys.argv[1:])\n")
SERIALS = {"MSTR": "0.0.0_AB_MSTR", "CTO": "1.0.0_SA_CTO", "COO": "2.0.0_SA_COO~C", "CVO": "3.0.0_SA_CVO",
           "CRO": "4.0.0_SA_CRO", "CLOUDOPS": "0.7.0_AE_CloudOps~F", "TIER2": "0.4.0_DS_ClientPlatform~A",
           "WORKER": "0.9.0_WK_NFRA_CTLPLN~13"}
APPLY_ARGS = ["-chdir=" + ROOT_REL, "apply"]
DEPLOY_ARGS = [PIPE_REL + "/scripts/gold/x.py"]
DRY = "--dry-seat-gates"
WORKER, CLOUDOPS = SERIALS["WORKER"], SERIALS["CLOUDOPS"]

TMP = Path(tempfile.mkdtemp(prefix="apply_gates_"))
TEMPLATES = {}
COUNTER = [0]


def run(argv, cwd=None, env=None, stdin_text=None):
    r = subprocess.run(argv, cwd=cwd, env=env, input=stdin_text, capture_output=True, text=True, encoding="utf-8", errors="replace",
                       timeout=180)
    return r.returncode, (r.stdout + r.stderr).replace("\r", "")


def git(repo, *args):
    return run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "-C", str(repo), *args])


def put(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def build_template(placement):
    fx = TMP / ("template_" + placement)
    for rel in COPIES:
        dst = fx / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPO / rel, dst)
    put(fx / ".tools/safe_deploy_core.py", STUB_CORE)
    put(fx / "org/missions/D0/FX/PA/project.json", json.dumps(
        {"project_code": "PA", "status": "active", "fabric": "laptop", "placement": placement}))
    put(fx / "org/missions/D0/FX/PA/task-orders/PA.TO-1.md",
        "<to_id>PA.TO-1</to_id>\n<issued_to>0.4.0_DS_ClientPlatform~A</issued_to>\n<status>issued</status>\n"
        "<paths>\n%s/main.tf\n%s/scripts/gold/x.py\n</paths>\n" % (ROOT_REL, PIPE_REL))
    run(["git", "init", "-q", "-b", "CLOUD", str(fx)])
    git(fx, "add", "-A")
    git(fx, "commit", "-q", "-m", "fixture")
    return fx


def fresh(placement="DELL1"):
    COUNTER[0] += 1
    dst = TMP / ("fx%d" % COUNTER[0])
    shutil.copytree(TEMPLATES[placement], dst)
    return dst


def notice(fx, name, **kw):
    doc = {"id": name, "root": ROOT_REL, "resources": [RES], "rule": "targeted-only-excluding",
           "until": "2026-10-08T06:20:00Z", "by": "1.0.0_SA_CTO", "reason": "fixture", "record": "fixture.md"}
    doc.update(kw)
    put(fx / "org/devices/deploy_notices" / (name + ".json"), json.dumps(doc))


def env_for(serial, **extra):
    env = {k: v for k, v in os.environ.items() if k not in ("SEAT_GATES_OVERRIDE", "OPAL_SEAT_GATES_ENFORCE_FILE", "OPAL_SEAT_GATES_ENFORCE_DIR", "DEPLOY_COMMIT")}
    env.update(OPAL_AGENT_SERIAL=serial, AGENTBUS_DEVICE="laptop", CHECKPOINT_DISABLE="1")
    env.update(extra)
    return env


def cross(fx, *args, serial="", now=NOW_LIVE, root=ROOT_REL, stdin_text=None):
    argv = [sys.executable, str(fx / ".tools/crossbox-deploy-check.py"), "--repo-root", str(fx), "--root", root, "--now", now]
    if serial:
        argv += ["--serial", serial]
    return run(argv + list(args), cwd=str(fx), env=env_for(WORKER), stdin_text=stdin_text)


def who(fx, serial, orders=None):
    argv = [sys.executable, str(fx / ".tools/apply-who-check.py"), "--serial", serial, "--root", ROOT_REL]
    argv += ["--orders-root", str(orders if orders else fx / "org/missions")]
    return run(argv, cwd=str(fx), env=env_for(serial))


def field(out, key):
    lines = [ln for ln in out.splitlines() if (" %s=" % key) in ln]
    m = re.search(r"\b%s=(\S+)" % key, lines[-1]) if lines else None
    return m.group(1) if m else None


def last_line(out):
    return [ln for ln in out.splitlines() if ln.strip()][-1] if out.strip() else ""


def wrapper(fx, name, serial, args, bin_dir=None, script_dir=None, **extra):
    marker = fx / "TERRAFORM_WAS_CALLED"
    fake = fx / "fake_terraform"
    put(fake, "#!/bin/sh\necho called > '%s'\nexit 0\n" % str(marker).replace("\\", "/"))
    env = env_for(serial, SAFE_APPLY_TERRAFORM=str(fake).replace("\\", "/"), **extra)
    if bin_dir:
        env["PATH"] = str(bin_dir) + os.pathsep + env["PATH"]
    rc, out = run(git_bash_resolver.bash_argv(str(Path(script_dir or fx / ".tools") / name), *args), cwd=str(fx), env=env)
    return rc, out, marker.exists()


def enforce(fx, *names):
    """Create switch files in a SCRATCH tree's org/mcp/ -- the named ones (e.g. 'apply-who.safe-apply'), else all four."""
    for name in (names or SWITCHES):
        put(fx / "org/mcp" / ("seat-gates.%s.enforce" % name), "enforce\n")


# ------------------------------------------------------------------------------------------------ the cases
CASES = []


def case(label):
    def deco(fn):
        CASES.append((label, fn))
        return fn
    return deco


def kind_case(kind, want):
    @case("%s serial %s -> %s" % (kind, SERIALS[kind], want))
    def _():
        rc, out = who(fresh(), SERIALS[kind])
        ok = field(out, "verdict") == want and field(out, "kind") == kind and rc == (0 if want == "ADMITTED" else 1)
        return ok, last_line(out)


for _k, _w in (("MSTR", "REFUSED"), ("CTO", "REFUSED"), ("COO", "REFUSED"), ("CVO", "REFUSED"), ("CRO", "REFUSED"),
               ("CLOUDOPS", "ADMITTED"), ("TIER2", "ADMITTED"), ("WORKER", "REFUSED")):
    kind_case(_k, _w)


@case("TIER2 with no non-terminal task order issued to it -> REFUSED")
def _():
    fx = fresh()
    rc, out = who(fx, SERIALS["TIER2"], orders=TMP / "no_orders_here")
    return field(out, "verdict") == "REFUSED", last_line(out)


@case("a serial that matches no kind is UNKNOWN and REFUSED")
def _():
    rc, out = who(fresh(), "9.9.9_ZZ_Nobody")
    return field(out, "kind") == "UNKNOWN" and field(out, "verdict") == "REFUSED" and rc == 1, last_line(out)


@case("the kind source is printed (built-in when neither the module nor the file exists)")
def _():
    rc, out = who(fresh(), WORKER)
    return "source=built-in" in out, out.splitlines()[0]


@case("the file org/ref/SEAT_ROLES.json beats the built-in table")
def _():
    fx = fresh()
    put(fx / "org/ref/SEAT_ROLES.json", json.dumps({"schema": "seat-roles/1", "kinds": [
        {"kind": "CLOUDOPS", "serial_pattern": r"^9\.9\.9_ZZ_Nobody$"}]}))
    rc, out = who(fx, "9.9.9_ZZ_Nobody~Q")
    return "source=file" in out and field(out, "kind") == "CLOUDOPS" and field(out, "verdict") == "ADMITTED", out.splitlines()[0]


@case("the module lib/seat_roles.py beats the file")
def _():
    fx = fresh()
    put(fx / "org/ref/SEAT_ROLES.json", json.dumps({"schema": "seat-roles/1", "kinds": [
        {"kind": "CLOUDOPS", "serial_pattern": r"^9\.9\.9_ZZ_Nobody$"}]}))
    put(fx / "lib/seat_roles.py", "def kind_of(serial):\n    return 'MSTR' if serial == '9.9.9_ZZ_Nobody' else 'UNKNOWN'\n")
    rc, out = who(fx, "9.9.9_ZZ_Nobody")
    return "source=module" in out and field(out, "kind") == "MSTR" and field(out, "verdict") == "REFUSED", out.splitlines()[0]


@case("a module that raises falls through to the file, said so in a KIND-NOTE")
def _():
    fx = fresh()
    put(fx / "org/ref/SEAT_ROLES.json", json.dumps({"schema": "seat-roles/1", "kinds": [
        {"kind": "CLOUDOPS", "serial_pattern": r"^9\.9\.9_ZZ_Nobody$"}]}))
    put(fx / "lib/seat_roles.py", "def kind_of(serial):\n    raise RuntimeError('boom')\n")
    rc, out = who(fx, "9.9.9_ZZ_Nobody")
    return "KIND-NOTE module source unusable" in out and "source=file" in out, out


@case("a live notice naming the root STOPS an untargeted apply")
def _():
    fx = fresh()
    notice(fx, "n1")
    rc, out = cross(fx)
    return field(out, "upset") == "hit" and field(out, "verdict") == "STOP" and rc == 1, last_line(out)


@case("a live notice STOPS a targeted apply that names the excluded resource")
def _():
    fx = fresh()
    notice(fx, "n1")
    rc, out = cross(fx, "--target", RES)
    return field(out, "upset") == "hit" and "which the notice excludes" in out, last_line(out)


@case("a live notice CLEARS a targeted apply that does not name the resource")
def _():
    fx = fresh()
    notice(fx, "n1")
    rc, out = cross(fx, "--target", "aws_s3_bucket.other")
    return field(out, "upset") == "clear" and "clear of it" in out, last_line(out)


@case("an expired notice is ignored and listed as expired")
def _():
    fx = fresh()
    notice(fx, "n1")
    rc, out = cross(fx, now=NOW_AFTER)
    return field(out, "upset") == "clear" and "EXPIRED" in out, last_line(out)


@case("rule no-apply STOPS even a targeted apply")
def _():
    fx = fresh()
    notice(fx, "n1", rule="no-apply")
    rc, out = cross(fx, "--target", "aws_s3_bucket.other")
    return field(out, "upset") == "hit", last_line(out)


@case("an empty resources list means the whole root: a targeted apply is stopped")
def _():
    fx = fresh()
    notice(fx, "n1", resources=[])
    rc, out = cross(fx, "--target", "aws_s3_bucket.other")
    return field(out, "upset") == "hit" and "whole root" in out, last_line(out)


@case("a live notice that names another root does not stop this one")
def _():
    fx = fresh()
    notice(fx, "n1", root="infra/aws/terraform/another")
    rc, out = cross(fx)
    return field(out, "upset") == "clear" and "another root" in out, last_line(out)


@case("an unparseable notice is NOT clear: it reads hit with the reason")
def _():
    fx = fresh()
    put(fx / "org/devices/deploy_notices/n1.json", "{ this is not json")
    rc, out = cross(fx)
    return field(out, "upset") == "hit" and "unreadable" in out, last_line(out)


@case("a notice carrying a key the reader does not know is refused (hit)")
def _():
    fx = fresh()
    notice(fx, "n1", surprise_key="x")
    rc, out = cross(fx)
    return field(out, "upset") == "hit" and "unknown" in out, last_line(out)


@case("a notice whose until is not a UTC time is refused (hit)")
def _():
    fx = fresh()
    notice(fx, "n1", until="tomorrow-ish")
    rc, out = cross(fx)
    return field(out, "upset") == "hit", last_line(out)


@case("absent cross-box files read 'none recorded' and clear")
def _():
    rc, out = cross(fresh())
    return field(out, "open_call") == "clear" and out.count("none recorded") >= 3, last_line(out)


def call_doc(**kw):
    doc = {"id": "c1", "kind": "CALL", "from_device": "dell1", "to_device": "laptop", "from_serial": "a", "to_serial": "b",
           "subject": "about " + ROOT_REL, "body_path": "org/devices/crossbox/c1.body.md", "state": "OPEN",
           "sent": {"at": "x", "bus_message_id": "1"}, "ack": None, "closed": {"from_at": None, "to_at": None}}
    doc.update(kw)
    return json.dumps(doc)


@case("an OPEN cross-box call naming the root HITS")
def _():
    fx = fresh()
    put(fx / "org/devices/crossbox/c1.json", call_doc())
    put(fx / "org/devices/crossbox/c1.body.md", "see the root\n")
    rc, out = cross(fx)
    return field(out, "open_call") == "hit" and field(out, "verdict") == "STOP", last_line(out)


@case("a CLOSED-BOTH call does not hit")
def _():
    fx = fresh()
    put(fx / "org/devices/crossbox/c1.json", call_doc(state="CLOSED-BOTH"))
    rc, out = cross(fx)
    return field(out, "open_call") == "clear" and "not live" in out, last_line(out)


@case("the call's body file is read too (the message never carries the substance)")
def _():
    fx = fresh()
    put(fx / "org/devices/crossbox/c1.json", call_doc(subject="x"))
    put(fx / "org/devices/crossbox/c1.body.md", "the body names %s only here\n" % ROOT_REL)
    rc, out = cross(fx)
    return field(out, "open_call") == "hit", last_line(out)


@case("an unparseable cross-box file is NOT clear: hit with the reason")
def _():
    fx = fresh()
    put(fx / "org/devices/crossbox/c1.json", "{ broken")
    rc, out = cross(fx)
    return field(out, "open_call") == "hit" and "unreadable" in out, last_line(out)


@case("an open_calls.json row naming the root HITS and the file's age is printed")
def _():
    fx = fresh()
    put(fx / "org/devices/state/dell1/open_calls.json", json.dumps({"device": "dell1", "written_at": "2026-10-08T03:00:00Z",
        "written_by": "0.9.0_WK_X~1", "rows": [{"id": "r1", "state": "OPEN", "subject": "touches %s" % ROOT_REL}]}))
    rc, out = cross(fx)
    return field(out, "open_call") == "hit" and "age 2h00m" in out, last_line(out)


@case("another box's placed project naming the root HITS (placement DELL1, this box laptop)")
def _():
    rc, out = cross(fresh("DELL1"))
    return field(out, "overlap") == "hit" and "placed on dell1" in out, last_line(out)


@case("the same project placed on THIS box does not hit; with nothing else the verdict is CLEAR")
def _():
    rc, out = cross(fresh("LAPTOP"))
    return field(out, "overlap") == "clear" and field(out, "verdict") == "CLEAR" and rc == 0, last_line(out)


@case("a root no project names reads clear on overlap")
def _():
    rc, out = cross(fresh("DELL1"), root="infra/aws/terraform/unrelated")
    return field(out, "overlap") == "clear", last_line(out)


def sentinel_doc(slug, author, title):
    return json.dumps({"slug": slug, "author": author, "status": "OPEN", "opened_at": "2026-10-07T00:00:00Z", "title": title})


def with_sentinel():
    fx = fresh("LAPTOP")
    put(fx / "org/critical_paths/.open_deploys/s1.json", sentinel_doc("s1", "0.7.0_AE_CloudOps~F", "a change in " + ROOT_REL))
    git(fx, "add", "-A")
    git(fx, "commit", "-q", "-m", "sentinel")
    return fx


@case("another seat's open deploy on the root HITS (read from HEAD with ls-tree)")
def _():
    rc, out = cross(with_sentinel())
    return field(out, "open_deploy") == "hit", last_line(out)


@case("the applying seat's own open deploy does not hit")
def _():
    rc, out = cross(with_sentinel(), serial="0.7.0_AE_CloudOps~F")
    return field(out, "open_deploy") == "clear", last_line(out)


@case("a sentinel on ANOTHER worktree's branch is read; the per-worktree denominator is printed")
def _():
    fx = with_sentinel()
    wt = TMP / ("wt%d" % COUNTER[0])
    git(fx, "worktree", "add", "-q", "-b", "other", str(wt))
    put(wt / "org/critical_paths/.open_deploys/s2.json", sentinel_doc("s2", "0.7.0_AE_CloudComp~B", "other tree names " + ROOT_REL))
    git(wt, "add", "-A")
    git(wt, "commit", "-q", "-m", "sentinel in the second tree")
    rc, out = cross(fx, serial="0.7.0_AE_CloudOps~F")
    return field(out, "open_deploy") == "hit" and "open deploy s2" in out and "denominator: 2 worktree(s)" in out, last_line(out)


def wrap_fixture(extra_notice_roots=(ROOT_REL, PIPE_REL)):
    fx = fresh("LAPTOP")
    for i, root in enumerate(extra_notice_roots):
        notice(fx, "n%d" % i, root=root, until="2099-01-01T00:00:00Z")
    return fx


@case("safe-apply WARN mode: REFUSED + STOP printed, rc 0, terraform and the halt gate never run")
def _():
    rc, out, called = wrapper(wrap_fixture(), "safe-apply.sh", WORKER, APPLY_ARGS + [DRY])
    ok = rc == 0 and "verdict=REFUSED" in out and "verdict=STOP" in out and "would stop under ENFORCE" in out and not called \
        and "halt-gate" not in out
    return ok, "rc=%s called=%s %s" % (rc, called, last_line(out))


@case("safe-deploy WARN mode: REFUSED + STOP printed, rc 0, nothing deployed")
def _():
    rc, out, called = wrapper(wrap_fixture(), "safe-deploy.sh", WORKER, DEPLOY_ARGS + [DRY])
    ok = rc == 0 and "verdict=REFUSED" in out and "verdict=STOP" in out and "would stop under ENFORCE" in out \
        and "safe_deploy_core" not in out
    return ok, "rc=%s %s" % (rc, last_line(out))


def crash_tools(fx):
    put(fx / ".tools/crossbox-deploy-check.py", "import sys\nprint('garbage')\nsys.exit(7)\n")
    put(fx / ".tools/apply-who-check.py", "raise SystemExit(5)\n")


def same_as_pinned(name, args, mutate=None):
    """WARN mode, NOT dry: the new wrapper and the pinned original, same inputs -> same exit code, same output once the
    block's own lines are removed. The scratch tree has no halt-gate file and a STUB core, so both stop or end at the same later
    point. `mutate` breaks the block's tools first (they are the new wrapper's only: the original never calls them)."""
    fx = wrap_fixture()
    rc_o, orig = git(REPO, "show", "%s:.tools/%s" % (PIN, name))
    if rc_o != 0:
        return False, "git show %s failed: %s" % (PIN, orig[:200])
    put(fx / "orig/.tools" / name, orig)
    put(fx / "orig/.tools/safe_deploy_core.py", STUB_CORE)
    if mutate:
        mutate(fx)
    rc_n, out_n, _ = wrapper(fx, name, WORKER, args)
    rc_p, out_p, _ = wrapper(fx, name, WORKER, args, script_dir=fx / "orig/.tools")

    def norm(text):
        keep = [ln for ln in text.splitlines() if "seat-gates" not in ln and "seat gates" not in ln]
        return re.sub(r"[^\s'\"]*\.tools", "X", "\n".join(keep))
    ok = rc_n == rc_p and norm(out_n) == norm(out_p) and "[seat-gates]" in out_n and "[seat-gates]" not in out_p \
        and ("STUB-CORE-RAN" in out_n or rc_n == 3)
    return ok, "new rc=%s orig rc=%s | new: %s | orig: %s" % (rc_n, rc_p, norm(out_n)[-120:], norm(out_p)[-120:])


@case("safe-apply WARN mode, non-dry: same exit code and same output as the pinned original once the block's lines are removed")
def _():
    return same_as_pinned("safe-apply.sh", APPLY_ARGS)


@case("safe-deploy WARN mode, non-dry: same exit code and same output as the pinned original once the block's lines are removed")
def _():
    return same_as_pinned("safe-deploy.sh", DEPLOY_ARGS)


@case("safe-apply WARN mode + both tools crash: same exit code and output as the pinned original (the block never changes the flow)")
def _():
    return same_as_pinned("safe-apply.sh", APPLY_ARGS, crash_tools)


@case("safe-deploy WARN mode + both tools crash: same exit code and output as the pinned original")
def _():
    return same_as_pinned("safe-deploy.sh", DEPLOY_ARGS, crash_tools)


# ---------------------------------------------------------------------------------------- ITEM 1: four switches
def blocked_line(out):
    return next((ln for ln in out.splitlines() if "BLOCKED by the seat gates" in ln), "")


def one_switch_case(wname, args, rc_block):
    stem = wname.replace(".sh", "")
    for check, other, tag, other_tag in (("apply-who", "crossbox", "apply-who", "crossbox-deploy"),
                                         ("crossbox", "apply-who", "crossbox-deploy", "apply-who")):
        @case("%s: ONLY seat-gates.%s.%s.enforce is its own -> %s blocks (rc %d), the other check only WARNs; the other wrapper's two "
              "switch files and the retired seat-gates.enforce turn on nothing here (one 'retired' WARN line)" % (wname, check, stem, check, rc_block))
        def _(check=check, tag=tag, other_tag=other_tag):
            fx = wrap_fixture()
            enforce(fx, "%s.%s" % (check, stem))
            enforce(fx, *[n for n in SWITCHES if not n.endswith(stem)])
            put(fx / "org/mcp/seat-gates.enforce", "old\n")
            rc, out, called = wrapper(fx, wname, WORKER, args + [DRY])
            line = blocked_line(out)
            mode_other = "mode=WARN" in out and ("mode=ENFORCE" in out)
            retired = [ln for ln in out.splitlines() if "is retired and turns on nothing" in ln]
            names_all = bool(retired) and all(("seat-gates.%s.enforce" % n) in retired[0] for n in SWITCHES)
            ok = rc == rc_block and (" " + tag) in line and other_tag not in line and mode_other \
                and ("would stop under ENFORCE" in out) and len(retired) == 1 and names_all
            return ok, "rc=%s line=%s" % (rc, line[:200])


one_switch_case("safe-apply.sh", APPLY_ARGS, 9)
one_switch_case("safe-deploy.sh", DEPLOY_ARGS, 1)


@case("OPAL_SEAT_GATES_ENFORCE_DIR (the test-only directory variable) points the four switches at a temp directory; the scratch tree has none")
def _():
    fx = wrap_fixture()
    other = TMP / ("enf_dir_%d" % COUNTER[0])
    put(other / "seat-gates.crossbox.safe-apply.enforce", "x")
    rc, out, called = wrapper(fx, "safe-apply.sh", CLOUDOPS, APPLY_ARGS + [DRY], OPAL_SEAT_GATES_ENFORCE_DIR=str(other).replace("\\", "/"))
    ok = rc == 9 and "crossbox-deploy" in blocked_line(out) and "mode=ENFORCE" in out and not (fx / "org/mcp").exists()
    return ok, "rc=%s %s" % (rc, blocked_line(out)[:160])


@case("an audited override passes ENFORCE and writes the reason to the wrapper's audit log")
def _():
    fx = wrap_fixture()
    enforce(fx)
    rc, out, called = wrapper(fx, "safe-apply.sh", WORKER, APPLY_ARGS + [DRY], SEAT_GATES_OVERRIDE="fixture reason")
    audit = fx / "org/git-author-override-audit.log"
    text = audit.read_text("utf-8") if audit.exists() else ""
    return rc == 0 and "OVERRIDDEN" in out and "SEAT_GATES_OVERRIDE" in text and "fixture reason" in text, "rc=%s audit=%s" % (rc, text.strip()[-120:])


@case("safe-deploy: the same override writes org/safe-deploy-bypass-audit.log")
def _():
    fx = wrap_fixture()
    enforce(fx)
    rc, out, called = wrapper(fx, "safe-deploy.sh", WORKER, DEPLOY_ARGS + [DRY], SEAT_GATES_OVERRIDE="fixture reason 2")
    audit = fx / "org/safe-deploy-bypass-audit.log"
    text = audit.read_text("utf-8") if audit.exists() else ""
    return rc == 0 and "fixture reason 2" in text, "rc=%s audit=%s" % (rc, text.strip()[-120:])


@case("ENFORCE lets a CLOUDOPS seat with a clear root (targeted, not the excluded resource) through, rc 0")
def _():
    fx = wrap_fixture()
    enforce(fx)
    put(fx / "org/missions/D0/FX/PA/project.json", json.dumps({"project_code": "PA", "status": "complete", "fabric": "laptop"}))
    rc, out, called = wrapper(fx, "safe-apply.sh", CLOUDOPS, APPLY_ARGS + ["-target=aws_s3_bucket.other", DRY])
    return rc == 0 and "verdict=ADMITTED" in out and "verdict=CLEAR" in out and "BLOCKED" not in out, "rc=%s %s" % (rc, last_line(out))


# ------------------------------------------------------------------------------------ ITEM 2: ENFORCE fails closed
def broken_python(label):
    broken = TMP / ("brokenbin_" + label)
    put(broken / "python", "#!/bin/sh\nexit 127\n")
    return broken


@case("ENFORCE + python unavailable (exit 127): safe-apply BLOCKS (rc 9) and prints the error (was: WARN and proceed)")
def _():
    fx = wrap_fixture()
    enforce(fx)
    rc, out, called = wrapper(fx, "safe-apply.sh", WORKER, APPLY_ARGS + [DRY], bin_dir=broken_python("a"))
    return rc == 9 and "ERROR [seat-gates]" in out and "gave no verdict" in out and "BLOCKED by the seat gates" in out, "rc=%s %s" % (rc, last_line(out))


@case("ENFORCE + both tools crash: safe-apply BLOCKS rc 9 (the halt gate is not reached); the error lines are printed")
def _():
    fx = wrap_fixture()
    enforce(fx)
    crash_tools(fx)
    rc, out, called = wrapper(fx, "safe-apply.sh", WORKER, APPLY_ARGS)
    return rc == 9 and "ERROR [seat-gates] apply-who-check gave no verdict" in out \
        and "ERROR [seat-gates] crossbox-deploy-check gave no verdict" in out and "halt-gate" not in out, "rc=%s %s" % (rc, last_line(out))


@case("ENFORCE + both tools crash: safe-deploy BLOCKS rc 1 (the deploy core is not reached)")
def _():
    fx = wrap_fixture()
    enforce(fx)
    crash_tools(fx)
    rc, out, called = wrapper(fx, "safe-deploy.sh", WORKER, DEPLOY_ARGS)
    return rc == 1 and "gave no verdict" in out and "BLOCKED by the seat gates" in out and "STUB-CORE-RAN" not in out, "rc=%s %s" % (rc, last_line(out))


@case("ENFORCE + both tools crash + SEAT_GATES_OVERRIDE: the audited override passes the no-verdict block (safe-apply reaches the halt gate, rc 3)")
def _():
    fx = wrap_fixture()
    enforce(fx)
    crash_tools(fx)
    rc, out, called = wrapper(fx, "safe-apply.sh", WORKER, APPLY_ARGS, SEAT_GATES_OVERRIDE="override no-verdict")
    audit = fx / "org/git-author-override-audit.log"
    text = audit.read_text("utf-8") if audit.exists() else ""
    return rc == 3 and "OVERRIDDEN" in out and "no-verdict" in text and "halt-gate-check.sh not found" in out, "rc=%s audit=%s" % (rc, text.strip()[-120:])


@case("ENFORCE + both tools ABSENT: safe-apply BLOCKS rc 9 (an absent tool is no verdict)")
def _():
    fx = wrap_fixture()
    enforce(fx)
    os.remove(fx / ".tools/apply-who-check.py")
    os.remove(fx / ".tools/crossbox-deploy-check.py")
    rc, out, called = wrapper(fx, "safe-apply.sh", WORKER, APPLY_ARGS)
    return rc == 9 and "gave no verdict" in out and "halt-gate" not in out, "rc=%s %s" % (rc, last_line(out))


@case("per check: apply-who crashes but only the CROSSBOX switch is on -> WARN, no block; crossbox CLEAR, the wrapper goes on")
def _():
    fx = fresh("LAPTOP")
    enforce(fx, "crossbox.safe-apply")
    put(fx / ".tools/apply-who-check.py", "raise SystemExit(5)\n")
    rc, out, called = wrapper(fx, "safe-apply.sh", WORKER, APPLY_ARGS + [DRY])
    return rc == 0 and "WARN [seat-gates] apply-who-check gave no verdict" in out and "BLOCKED" not in out and "verdict=CLEAR" in out, "rc=%s %s" % (rc, last_line(out))


@case("per check: crossbox crashes and ITS switch is on, apply-who ADMITS -> blocked on the crossbox check alone (rc 9)")
def _():
    fx = fresh("LAPTOP")
    enforce(fx, "crossbox.safe-apply")
    put(fx / ".tools/crossbox-deploy-check.py", "import sys\nprint('garbage')\nsys.exit(7)\n")
    rc, out, called = wrapper(fx, "safe-apply.sh", CLOUDOPS, APPLY_ARGS + [DRY])
    line = blocked_line(out)
    return rc == 9 and "crossbox-deploy:no-verdict" in line and "verdict=ADMITTED" in out, "rc=%s %s" % (rc, line[:160])


@case("the block ITSELF errors (resolve-actor.sh exits 3) while a switch file exists -> safe-apply BLOCKS rc 9; with no switch it only WARNs")
def _():
    fx = wrap_fixture()
    put(fx / ".tools/lib/resolve-actor.sh", "exit 3\n")
    rc0, out0, _c = wrapper(fx, "safe-apply.sh", WORKER, APPLY_ARGS + [DRY])
    enforce(fx, "crossbox.safe-apply")
    rc1, out1, _c = wrapper(fx, "safe-apply.sh", WORKER, APPLY_ARGS + [DRY])
    ok = rc0 == 0 and "the block errored (rc=3); proceeding exactly as before" in out0 \
        and rc1 == 9 and "the block itself errored (rc=3)" in out1
    return ok, "warn rc=%s enforce rc=%s" % (rc0, rc1)


@case("the block ITSELF errors while a switch file exists -> safe-deploy BLOCKS rc 1")
def _():
    fx = wrap_fixture()
    put(fx / ".tools/lib/resolve-actor.sh", "exit 3\n")
    enforce(fx, "apply-who.safe-deploy")
    rc, out, _c = wrapper(fx, "safe-deploy.sh", WORKER, DEPLOY_ARGS + [DRY])
    return rc == 1 and "the block itself errored (rc=3)" in out, "rc=%s %s" % (rc, last_line(out))


# ---------------------------------------------------------------- ITEM 3: apply-who grades a deploy, not a push
def deploy_fixture(placement="LAPTOP"):
    return fresh(placement)


def commit_as(fx, files, author, message):
    for rel, text in files.items():
        put(fx / rel, text)
    git(fx, "add", "-A")
    return git(fx, "commit", "-q", "--author", "%s <a@a.a>" % author, "-m", message)


SKIP_LINE = "SKIP [seat-gates] apply-who: this invocation deploys nothing"


@case("safe-deploy: an invocation that deploys NOTHING (a README under a scripts path) prints the SKIP line and no apply-who verdict, MSTR seat, switch ON -> not blocked")
def _():
    fx = deploy_fixture()
    enforce(fx, "apply-who.safe-deploy")
    rc, out, _c = wrapper(fx, "safe-deploy.sh", SERIALS["MSTR"], [PIPE_REL + "/scripts/gold/README.md", DRY])
    return rc == 0 and SKIP_LINE in out and "APPLY-WHO" not in out and "BLOCKED" not in out, "rc=%s %s" % (rc, last_line(out))


@case("safe-deploy: a fabric manager's (MSTR) invocation that carries a DEPLOYABLE file -- here a bundle member the core deploys, so the root "
      "comes from the core's list -- is graded (REFUSED kind=MSTR): reported for a ruling, not exempted")
def _():
    fx = deploy_fixture()
    enforce(fx, "apply-who.safe-deploy")
    rc, out, _c = wrapper(fx, "safe-deploy.sh", SERIALS["MSTR"], [PIPE_REL + "/config/roster.json", DRY])
    return rc == 1 and "kind=MSTR" in out and "verdict=REFUSED" in out and "root=pipea" in out and SKIP_LINE not in out, \
        "rc=%s %s" % (rc, blocked_line(out)[:140])


@case("safe-deploy --commit-range (the pre-push shape): a pushed range whose only scripts-path change is a README SKIPs apply-who, MSTR seat, switch ON -> not blocked")
def _():
    fx = deploy_fixture()
    enforce(fx, "apply-who.safe-deploy")
    commit_as(fx, {PIPE_REL + "/scripts/gold/y.py": "x = 1\n"}, WORKER, "deployable")
    commit_as(fx, {PIPE_REL + "/scripts/gold/README.md": "doc\n"}, WORKER, "readme")
    rc1, out1, _c = wrapper(fx, "safe-deploy.sh", SERIALS["MSTR"], ["--commit-range", "HEAD~1..HEAD", DRY])
    return rc1 == 0 and SKIP_LINE in out1 and "APPLY-WHO" not in out1 and "BLOCKED" not in out1, "rc=%s %s" % (rc1, last_line(out1))


@case("safe-deploy: if the core's list cannot be read, apply-who runs as before and a WARN says so (nothing is assumed to deploy nothing)")
def _():
    fx = deploy_fixture()
    os.remove(fx / ".tools/safe_deploy_core.py")
    rc, out, _c = wrapper(fx, "safe-deploy.sh", WORKER, DEPLOY_ARGS + [DRY])
    return rc == 0 and "could not tell what this invocation deploys" in out and "verdict=REFUSED" in out and SKIP_LINE not in out, "rc=%s %s" % (rc, last_line(out))


@case("--list-deployable against a byte copy of the REAL safe_deploy_core.py (imported, never run): a gold .py deploys, a README, a tests path and an unknown pipeline do not")
def _():
    core_home = TMP / "realcore"
    (core_home / ".tools").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(REPO / ".tools/safe_deploy_core.py", core_home / ".tools/safe_deploy_core.py")
    stdin = "data/black_diamond/scripts/gold/x.py\ndata/black_diamond/scripts/gold/README.md\ndata/pipea/scripts/gold/x.py\ndata/black_diamond/scripts/tests/t.py\n"
    rc, out = run([sys.executable, str(REPO / ".tools/crossbox-deploy-check.py"), "--list-deployable", "--repo-root", str(core_home),
                   "--files-from", "-"], env=env_for(WORKER), stdin_text=stdin)
    lines = out.splitlines()
    ok = rc == 0 and lines == ["DEPLOYABLE data/black_diamond/scripts/gold/x.py", "DEPLOY-ROOT data/black_diamond", "DEPLOYABLE-COUNT n=1"]
    return ok, "rc=%s %s" % (rc, " / ".join(lines))


@case("--list-deployable in range mode (stub core): counts the files of the range; a missing core is rc 2 with the reason")
def _():
    fx = deploy_fixture()
    commit_as(fx, {PIPE_REL + "/scripts/gold/y.py": "x = 1\n", "docs/a.md": "d\n"}, WORKER, "one deployable")
    rc, out = run([sys.executable, str(fx / ".tools/crossbox-deploy-check.py"), "--list-deployable", "--repo-root", str(fx),
                   "--commit-range", "HEAD~1..HEAD"], env=env_for(WORKER))
    os.remove(fx / ".tools/safe_deploy_core.py")
    rc2, out2 = run([sys.executable, str(fx / ".tools/crossbox-deploy-check.py"), "--list-deployable", "--repo-root", str(fx)], env=env_for(WORKER))
    return rc == 0 and out.splitlines()[-1] == "DEPLOYABLE-COUNT n=1" and rc2 == 2 and "cannot read what the deploy core" in out2, "%s | %s" % (last_line(out), last_line(out2))


# ---------------------------------------------------- ITEM 4: overlap is judged on the files carried, never on a shared root
def crossf(fx, *args, stdin_text=None, root=ROOT_REL, serial=""):
    return cross(fx, *args, serial=serial, root=root, stdin_text=stdin_text)


MAIN_TF = ROOT_REL + "/main.tf"
OTHER_TF = ROOT_REL + "/other.tf"


@case("OVERLAP, files mode: the root is named by a project placed on dell1 but the carried file is NOT in its write set -> overlap=clear (the root-only reading still hits)")
def _():
    rc0, out0 = crossf(fresh("DELL1"))
    rc1, out1 = crossf(fresh("DELL1"), "--files", OTHER_TF)
    ok = field(out0, "overlap") == "hit" and field(out1, "overlap") == "clear" and field(out1, "verdict") == "CLEAR" and rc1 == 0 \
        and "files mode: 1 file(s) carried" in out1
    return ok, "root-only: %s | files: %s" % (field(out0, "overlap"), last_line(out1))


@case("OVERLAP, files mode: a carried file that IS in another box's write set -> hit, naming the file")
def _():
    rc, out = crossf(fresh("DELL1"), "--files", OTHER_TF, MAIN_TF)
    return field(out, "overlap") == "hit" and ("carried file %s" % MAIN_TF) in out and "placed on dell1" in out, last_line(out)


@case("OVERLAP, files mode: --files-from reads a file and '-' reads stdin; an EMPTY list reads clear 'no file carried'")
def _():
    fx = fresh("DELL1")
    listing = fx / "carried.txt"
    put(listing, MAIN_TF + "\n")
    rc1, out1 = crossf(fx, "--files-from", str(listing))
    rc2, out2 = crossf(fresh("DELL1"), "--files-from", "-", stdin_text=OTHER_TF + "\n")
    rc3, out3 = crossf(fresh("DELL1"), "--files-from", "-", stdin_text="\n")
    ok = field(out1, "overlap") == "hit" and field(out2, "overlap") == "clear" and field(out3, "overlap") == "clear" and "no file carried" in out3
    return ok, "%s | %s | %s" % (field(out1, "overlap"), field(out2, "overlap"), field(out3, "overlap"))


def trunk_fixture(placement="DELL1"):
    fx = fresh(placement)
    put(fx / MAIN_TF, "# main\n")
    put(fx / OTHER_TF, "# other\n")
    git(fx, "add", "-A")
    git(fx, "commit", "-q", "-m", "tf on the trunk")
    return fx


@case("--files-vs-trunk: nothing of the root differs from the merge base -> overlap=clear with the reason 'no file of this root differs'")
def _():
    rc, out = crossf(trunk_fixture(), "--files-vs-trunk")
    return field(out, "overlap") == "clear" and "no file of this root differs" in out and rc == 0, last_line(out)


@case("--files-vs-trunk: a committed branch change to main.tf (in dell1's write set) hits; a change only to other.tf, a README and a non-Terraform file is clear")
def _():
    fx = trunk_fixture()
    git(fx, "switch", "-q", "-c", "feature")
    put(fx / MAIN_TF, "# main changed\n")
    git(fx, "add", "-A")
    git(fx, "commit", "-q", "-m", "feature change")
    rc1, out1 = crossf(fx, "--files-vs-trunk")
    fy = trunk_fixture()
    git(fy, "switch", "-q", "-c", "feature")
    put(fy / OTHER_TF, "# other changed\n")
    put(fy / (ROOT_REL + "/README.md"), "doc\n")
    git(fy, "add", "-A")
    git(fy, "commit", "-q", "-m", "feature change 2")
    rc2, out2 = crossf(fy, "--files-vs-trunk")
    ok = field(out1, "overlap") == "hit" and ("carried file %s" % MAIN_TF) in out1 and field(out2, "overlap") == "clear" \
        and "1 Terraform file(s) of this root differ" in out2
    return ok, "%s | %s" % (field(out1, "overlap"), field(out2, "overlap"))


@case("--files-vs-trunk: an uncommitted edit and an untracked new .tf file of the root count as differing")
def _():
    fx = trunk_fixture()
    put(fx / MAIN_TF, "# edited, not committed\n")
    rc1, out1 = crossf(fx, "--files-vs-trunk")
    fy = trunk_fixture()
    put(fy / (ROOT_REL + "/brand_new.tf"), "# new\n")
    rc2, out2 = crossf(fy, "--files-vs-trunk")
    return field(out1, "overlap") == "hit" and field(out2, "overlap") == "clear" and "1 Terraform file(s)" in out2, "%s | %s" % (field(out1, "overlap"), field(out2, "overlap"))


@case("--files-vs-trunk: if the shared branch cannot be resolved the tool SAYS SO and falls back to the root alone (dell1 project hits)")
def _():
    fx = trunk_fixture()
    git(fx, "branch", "-m", "zzz")
    rc, out = crossf(fx, "--files-vs-trunk")
    return "FILES-NOTE:" in out and "cannot be resolved" in out and field(out, "overlap") == "hit", last_line(out)


@case("safe-deploy end to end (dell1 placement, the dell2 report): a deploy of y.py, a file NOT in the project's write set though its root is named, reads overlap=clear")
def _():
    fx = deploy_fixture("DELL1")
    rc1, out1, _c = wrapper(fx, "safe-deploy.sh", CLOUDOPS, [PIPE_REL + "/scripts/gold/y.py", DRY])
    return rc1 == 0 and "overlap=clear" in out1 and "verdict=CLEAR" in out1, last_line(out1)


@case("safe-apply end to end (dell1 placement): no Terraform file of the root differs -> overlap=clear")
def _():
    fx = trunk_fixture("DELL1")
    rc, out, _c = wrapper(fx, "safe-apply.sh", CLOUDOPS, APPLY_ARGS + [DRY])
    return rc == 0 and "overlap=clear" in out and "verdict=CLEAR" in out, "rc=%s %s" % (rc, last_line(out))


def sentinel_commit(text, root_fixture=None):
    fx = root_fixture or fresh("LAPTOP")
    put(fx / "org/critical_paths/.open_deploys/s1.json", sentinel_doc("s1", "0.7.0_AE_CloudOps~F", text))
    git(fx, "add", "-A")
    git(fx, "commit", "-q", "-m", "sentinel")
    return fx


@case("OPEN-DEPLOY, files mode (data root): a sentinel naming the SHARED ROOT but not a carried file does not hit; root-only still does")
def _():
    fx = sentinel_commit("a change in data/pipea")
    rc0, out0 = crossf(fx, root=PIPE_REL)
    rc1, out1 = crossf(fx, "--files", PIPE_REL + "/scripts/gold/y.py", root=PIPE_REL)
    ok = field(out0, "open_deploy") == "hit" and field(out1, "open_deploy") == "clear" and "files mode: a sentinel hits only if it names" in out1
    return ok, "root-only %s | files %s" % (field(out0, "open_deploy"), field(out1, "open_deploy"))


@case("OPEN-DEPLOY, files mode (data root): a sentinel naming the carried file by path, or by its bare name, hits")
def _():
    path = PIPE_REL + "/scripts/gold/x.py"
    rc1, out1 = crossf(sentinel_commit("touches " + path), "--files", path, root=PIPE_REL)
    rc2, out2 = crossf(sentinel_commit("re-runs x.py after the fix"), "--files", path, root=PIPE_REL)
    ok = field(out1, "open_deploy") == "hit" and "names a carried file" in out1 and field(out2, "open_deploy") == "hit"
    return ok, "%s | %s" % (field(out1, "open_deploy"), field(out2, "open_deploy"))


@case("OPEN-DEPLOY, files mode on a TERRAFORM root: the sentinel naming the root still hits (an apply works on the state of the whole root)")
def _():
    rc, out = crossf(sentinel_commit("a change in " + ROOT_REL), "--files", OTHER_TF)
    return field(out, "open_deploy") == "hit" and "names the root" in out, last_line(out)


@case("OPEN-CALL, files mode: a call naming only a project whose write set covers the root hits root-only, and does not when the carried file is outside its write set")
def _():
    fx = fresh("LAPTOP")
    put(fx / "org/devices/crossbox/c1.json", call_doc(subject="the PA project needs a word"))
    put(fx / "org/devices/crossbox/c1.body.md", "nothing about paths\n")
    rc0, out0 = cross(fx)
    rc1, out1 = cross(fx, "--files", OTHER_TF)
    rc2, out2 = cross(fx, "--files", MAIN_TF)
    ok = field(out0, "open_call") == "hit" and field(out1, "open_call") == "clear" and field(out2, "open_call") == "hit"
    return ok, "%s %s %s" % (field(out0, "open_call"), field(out1, "open_call"), field(out2, "open_call"))


# ------------------------------------------------------------------------- ITEM 5: the dry pass over real invocations
def dry_fixture():
    fx = fresh("LAPTOP")
    commit_as(fx, {ROOT_REL + "/main.tf": "# tf\n"}, CLOUDOPS, "a terraform change by a cloud-ops seat")
    commit_as(fx, {PIPE_REL + "/scripts/gold/y.py": "x = 1\n"}, WORKER, "a deploy by a worker serial")
    commit_as(fx, {PIPE_REL + "/scripts/gold/README.md": "doc\n"}, SERIALS["TIER2"], "a README under a scripts path")
    commit_as(fx, {PIPE_REL + "/scripts/gold/z.py": "z = 1\n"}, "Andrew Berman", "a human author, not a serial")
    commit_as(fx, {"docs/a.md": "d\n"}, SERIALS["CRO"], "a doc only")
    return fx


def dry(fx, *args):
    return run([sys.executable, str(fx / ".tools/seat-gates-dry-pass.py"), "--repo-root", str(fx), *args], cwd=str(fx), env=env_for(WORKER))


def tree_snapshot(fx):
    rc, status = git(fx, "status", "--porcelain")
    rc2, head = git(fx, "rev-parse", "HEAD")
    files = sorted(str(p.relative_to(fx)) for p in fx.rglob("*") if p.is_file() and ".git" not in p.parts)
    return status, head, files


@case("dry pass --last: attributes each commit to its author's serial; a worker's deploy WOULD STOP, a non-serial author is SKIPPED, a README deploys nothing (PASS)")
def _():
    fx = dry_fixture()
    rc, out = dry(fx, "--last", "10", "--ref", "CLOUD", "--device", "laptop")
    verdicts = [(m.group(1), m.group(2)) for m in (re.search(r"serial=(\S+) verdict=(\S+)", ln) for ln in out.splitlines()) if m]
    ok = rc == 1 and last_line(out) == "SEAT-GATES-DRY ranges=4 would_stop=1 skipped=1 ok=False" \
        and (WORKER, "WOULD-STOP") in verdicts and (CLOUDOPS, "PASS") in verdicts and (SERIALS["TIER2"], "PASS") in verdicts \
        and "SKIPPED" in out and "is not a serial" in out and "SKIP(deploys nothing)" in out and "WOULD-STOP" in out
    return ok, last_line(out)


@case("dry pass --range (repeatable) with --serial: the acting seat is the one named; a CLOUDOPS seat reading zero would-stops gives ok=True, rc 0")
def _():
    fx = dry_fixture()
    rc_, shas = git(fx, "log", "--format=%H", "-n", "4")
    top = shas.split()
    rc, out = dry(fx, "--range", "%s^..%s" % (top[2], top[2]), "--range", "%s^..%s" % (top[3], top[3]), "--serial", CLOUDOPS, "--device", "laptop")
    return rc == 0 and last_line(out) == "SEAT-GATES-DRY ranges=2 would_stop=0 skipped=0 ok=True", last_line(out)


@case("dry pass is READ-ONLY: no file, index or HEAD change in the tree it reads, and no Terraform or deploy runs")
def _():
    fx = dry_fixture()
    before = tree_snapshot(fx)
    rc, out = dry(fx, "--last", "10", "--ref", "CLOUD")
    after = tree_snapshot(fx)
    return before == after and not (fx / "TERRAFORM_WAS_CALLED").exists(), "same=%s" % (before == after)


@case("dry pass with no range is a usage error (rc 2); a fabric manager's push (MSTR serial) with a deployable file reads would-stop")
def _():
    fx = dry_fixture()
    rc, out = dry(fx)
    rc2, out2 = dry(fx, "--last", "10", "--ref", "CLOUD", "--serial", SERIALS["MSTR"])
    return rc == 2 and rc2 == 1 and "kind=MSTR" in out2 and "verdict=REFUSED" in out2, "%s | %s" % (rc, last_line(out2))


@case("the real tree has NONE of the five enforce files (WARN mode is the shipped default)")
def _():
    names = ["seat-gates.enforce"] + ["seat-gates.%s.enforce" % n for n in SWITCHES]
    present = [n for n in names if (REPO / "org/mcp" / n).exists()]
    return not present, "checked %d names under %s, present: %s" % (len(names), REPO / "org/mcp", present)


def hunk_ranges(diff_out):
    spans = []
    for ln in diff_out.splitlines():
        m = re.match(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", ln)
        if m:
            spans.append((int(m.group(1)), int(m.group(2) or 1), int(m.group(3)), int(m.group(4) or 1)))
    return spans


def block_span(text):
    lines = text.splitlines()
    start = next(i for i, ln in enumerate(lines, 1) if "SEAT GATES" in ln)
    end = max(i for i, ln in enumerate(lines, 1) if "--dry-seat-gates" in ln) + 1
    return start, end


def diff_case(name):
    @case("%s differs from the pre-block wrapper by ONE added hunk, no removed line, and bash -n is clean" % name)
    def _():
        rc, out = git(REPO, "diff", "-U0", PIN, "--", ".tools/" + name)
        hunks = [ln for ln in out.splitlines() if ln.startswith("@@")]
        removed = [ln for ln in out.splitlines() if ln.startswith("-") and not ln.startswith("---")]
        syntax = run(git_bash_resolver.bash_argv("-n", str(REPO / ".tools" / name)))
        return rc == 0 and len(hunks) == 1 and not removed and syntax[0] == 0, \
            "hunks=%d removed=%d bash -n rc=%s" % (len(hunks), len(removed), syntax[0])

    @case("%s: against the first pass every changed line, added or removed, lies inside the seat-gates block" % name)
    def _():
        rc, out = git(REPO, "diff", "-U0", FIRST_PASS, "--", ".tools/" + name)
        rc_o, old_text = git(REPO, "show", "%s:.tools/%s" % (FIRST_PASS, name))
        old_s, old_e = block_span(old_text)
        new_s, new_e = block_span((REPO / ".tools" / name).read_text("utf-8"))
        spans = hunk_ranges(out)
        removed = [ln for ln in out.splitlines() if ln.startswith("-") and not ln.startswith("---")]
        inside = all(old_s - 1 <= a and a + max(b, 1) - 1 <= old_e and new_s - 1 <= c and c + max(d, 1) - 1 <= new_e for a, b, c, d in spans)
        return rc == 0 and rc_o == 0 and spans and inside, "hunks=%d removed=%d old block %d-%d new block %d-%d" % (
            len(spans), len(removed), old_s, old_e, new_s, new_e)


diff_case("safe-apply.sh")
diff_case("safe-deploy.sh")


def execute(item):
    label, fn = item
    try:
        ok, detail = fn()
        return bool(ok), str(detail)
    except Exception:
        return False, "EXCEPTION " + traceback.format_exc()[-400:]


def main():
    try:
        for placement in ("DELL1", "LAPTOP"):
            TEMPLATES[placement] = build_template(placement)
        with ThreadPoolExecutor(max_workers=12) as pool:
            outcomes = list(pool.map(execute, CASES))
    finally:
        pass
    ok_count = 0
    for number, ((label, _fn), (ok, detail)) in enumerate(zip(CASES, outcomes), 1):
        ok_count += 1 if ok else 0
        print("%s case %d: %s%s" % ("PASS" if ok else "FAIL", number, label, (" | " + detail[:420].replace("\n", " / ")) if detail else ""))
    shutil.rmtree(str(TMP), ignore_errors=True)
    ok = ok_count == len(CASES) and len(CASES) > 0
    print("APPLY-GATES-TEST cases=%d/%d ok=%s" % (ok_count, len(CASES), ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
