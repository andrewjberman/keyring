#!/usr/bin/env python3
"""Cases for .tools/apply-who-check.py, .tools/crossbox-deploy-check.py and their one block in each wrapper
(NFRA_CTLPLN workstream SEATS, cell CT-s-3).

Run: python .tools/tests/test_apply_who_and_crossbox.py   (LAST line: APPLY-GATES-TEST cases=<k>/<n> ok=<True|False>)

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
ROOT_REL = "infra/aws/terraform/rootx"
PIPE_REL = "data/pipea"
RES = "aws_cloudwatch_event_target.guarded"
NOW_LIVE = "2026-10-08T05:00:00Z"
NOW_AFTER = "2026-10-08T07:00:00Z"
COPIES = [".tools/safe-apply.sh", ".tools/safe-deploy.sh", ".tools/apply-who-check.py", ".tools/crossbox-deploy-check.py",
          ".tools/placement-check.py", ".tools/lib/resolve-actor.sh", "lib/devices.py", "org/devices/DEVICES.json"]
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


def run(argv, cwd=None, env=None):
    r = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
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
    env = {k: v for k, v in os.environ.items() if k not in ("SEAT_GATES_OVERRIDE", "OPAL_SEAT_GATES_ENFORCE_FILE", "DEPLOY_COMMIT")}
    env.update(OPAL_AGENT_SERIAL=serial, AGENTBUS_DEVICE="laptop", CHECKPOINT_DISABLE="1")
    env.update(extra)
    return env


def cross(fx, *args, serial="", now=NOW_LIVE, root=ROOT_REL):
    argv = [sys.executable, str(fx / ".tools/crossbox-deploy-check.py"), "--repo-root", str(fx), "--root", root, "--now", now]
    if serial:
        argv += ["--serial", serial]
    return run(argv + list(args), cwd=str(fx), env=env_for(WORKER))


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


def enforce(fx):
    put(fx / "org/mcp/seat-gates.enforce", "enforce\n")


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


def same_as_pinned(name, args):
    """WARN mode, NOT dry: the new wrapper and the pinned original, same inputs -> same exit code, same output once the
    block's own lines are removed. The scratch tree has no halt-gate/core file, so both stop at the same later point."""
    fx = wrap_fixture()
    rc_o, orig = git(REPO, "show", "%s:.tools/%s" % (PIN, name))
    if rc_o != 0:
        return False, "git show %s failed: %s" % (PIN, orig[:200])
    put(fx / "orig/.tools" / name, orig)
    rc_n, out_n, _ = wrapper(fx, name, WORKER, args)
    rc_p, out_p, _ = wrapper(fx, name, WORKER, args, script_dir=fx / "orig/.tools")

    def norm(text):
        keep = [ln for ln in text.splitlines() if "seat-gates" not in ln and "seat gates" not in ln]
        return re.sub(r"[^\s'\"]*\.tools", "X", "\n".join(keep))
    ok = rc_n == rc_p and rc_n != 0 and norm(out_n) == norm(out_p) and "[seat-gates]" in out_n and "[seat-gates]" not in out_p
    return ok, "new rc=%s orig rc=%s | new: %s | orig: %s" % (rc_n, rc_p, norm(out_n)[-120:], norm(out_p)[-120:])


@case("safe-apply WARN mode, non-dry: same exit code and same output as the pinned original once the block's lines are removed")
def _():
    return same_as_pinned("safe-apply.sh", APPLY_ARGS)


@case("safe-deploy WARN mode, non-dry: same exit code and same output as the pinned original once the block's lines are removed")
def _():
    return same_as_pinned("safe-deploy.sh", DEPLOY_ARGS)


@case("safe-apply ENFORCE (the scratch tree's file): REFUSED/STOP stop it with rc 9, before the halt gate and terraform")
def _():
    fx = wrap_fixture()
    enforce(fx)
    rc, out, called = wrapper(fx, "safe-apply.sh", WORKER, APPLY_ARGS)
    return rc == 9 and "BLOCKED by the seat gates" in out and not called and "halt-gate" not in out, "rc=%s %s" % (rc, last_line(out))


@case("safe-deploy ENFORCE: stopped with rc 1, before the deploy core")
def _():
    fx = wrap_fixture()
    enforce(fx)
    rc, out, called = wrapper(fx, "safe-deploy.sh", WORKER, DEPLOY_ARGS + [DRY])
    return rc == 1 and "BLOCKED by the seat gates" in out and "safe_deploy_core" not in out, "rc=%s %s" % (rc, last_line(out))


@case("OPAL_SEAT_GATES_ENFORCE_FILE points the enforce switch at a temp file (the scratch tree has none)")
def _():
    fx = wrap_fixture()
    other = TMP / "elsewhere.enforce"
    put(other, "x")
    rc, out, called = wrapper(fx, "safe-apply.sh", WORKER, APPLY_ARGS + [DRY], OPAL_SEAT_GATES_ENFORCE_FILE=str(other).replace("\\", "/"))
    return rc == 9 and "mode=ENFORCE" in out and not (fx / "org/mcp/seat-gates.enforce").exists(), "rc=%s %s" % (rc, last_line(out))


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


@case("ENFORCE + python unavailable (exit 127): the block WARNs and the wrapper proceeds, rc 0")
def _():
    fx = wrap_fixture()
    enforce(fx)
    broken = TMP / "brokenbin"
    put(broken / "python", "#!/bin/sh\nexit 127\n")
    rc, out, called = wrapper(fx, "safe-apply.sh", WORKER, APPLY_ARGS + [DRY], bin_dir=broken)
    return rc == 0 and "WARN [seat-gates]" in out and "BLOCKED" not in out, "rc=%s %s" % (rc, last_line(out))


@case("ENFORCE + both tools crash: WARN lines, no block; safe-apply reaches the halt gate (absent in the scratch tree: rc 3)")
def _():
    fx = wrap_fixture()
    enforce(fx)
    put(fx / ".tools/crossbox-deploy-check.py", "import sys\nprint('garbage')\nsys.exit(7)\n")
    put(fx / ".tools/apply-who-check.py", "raise SystemExit(5)\n")
    rc, out, called = wrapper(fx, "safe-apply.sh", WORKER, APPLY_ARGS)
    return rc == 3 and "gave no verdict" in out and "BLOCKED" not in out and "halt-gate-check.sh not found" in out, "rc=%s %s" % (rc, last_line(out))


@case("ENFORCE + both tools crash: safe-deploy WARNs, no block; it reaches the deploy core (absent in the scratch tree)")
def _():
    fx = wrap_fixture()
    enforce(fx)
    put(fx / ".tools/crossbox-deploy-check.py", "import sys\nprint('garbage')\nsys.exit(7)\n")
    put(fx / ".tools/apply-who-check.py", "raise SystemExit(5)\n")
    rc, out, called = wrapper(fx, "safe-deploy.sh", WORKER, DEPLOY_ARGS)
    return "gave no verdict" in out and "BLOCKED" not in out and "safe_deploy_core.py" in out, "rc=%s %s" % (rc, last_line(out))


@case("ENFORCE + both tools absent: WARN, safe-apply reaches the halt gate (rc 3), nothing blocked")
def _():
    fx = wrap_fixture()
    enforce(fx)
    os.remove(fx / ".tools/apply-who-check.py")
    os.remove(fx / ".tools/crossbox-deploy-check.py")
    rc, out, called = wrapper(fx, "safe-apply.sh", WORKER, APPLY_ARGS)
    return rc == 3 and "BLOCKED" not in out and "halt-gate-check.sh not found" in out, "rc=%s %s" % (rc, last_line(out))


@case("the real tree has no org/mcp/seat-gates.enforce (WARN mode is the shipped default)")
def _():
    return not (REPO / "org/mcp/seat-gates.enforce").exists(), str(REPO / "org/mcp/seat-gates.enforce")


def diff_case(name):
    @case("%s differs from the pre-change wrapper by ONE added hunk, no removed line, and bash -n is clean" % name)
    def _():
        rc, out = git(REPO, "diff", "-U0", PIN, "--", ".tools/" + name)
        hunks = [ln for ln in out.splitlines() if ln.startswith("@@")]
        removed = [ln for ln in out.splitlines() if ln.startswith("-") and not ln.startswith("---")]
        syntax = run(git_bash_resolver.bash_argv("-n", str(REPO / ".tools" / name)))
        return rc == 0 and len(hunks) == 1 and not removed and syntax[0] == 0, \
            "hunks=%d removed=%d bash -n rc=%s" % (len(hunks), len(removed), syntax[0])


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
        with ThreadPoolExecutor(max_workers=8) as pool:
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
