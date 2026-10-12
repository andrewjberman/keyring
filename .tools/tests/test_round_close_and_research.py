#!/usr/bin/env python3
"""Cases for .tools/round-close-check.py, .tools/research-owed.py and the one block in
.tools/git-hooks/missions-tree-check.sh that calls the first (NFRA_CTLPLN workstream SEATS, cell CT-s-8).

Run: python .tools/tests/test_round_close_and_research.py   (LAST line: CLOSE-GATES-TEST cases=<k>/<n> ok=<True|False>)

Both tools' own selftests run as they are. The hook is exercised in a SCRATCH git repository built in a temporary directory
(a template, copied once per case) that holds COPIES of the hook, the two tools it reaches, the seat files they read and a
one-project tree; the real tree is never staged, committed or written. The project-tree generator the hook runs first
(.tools/missions-tree-index.py) is a stub in the scratch copy that exits with the code the case sets: it validates 350 rows
in the real tree and is not what is under test (the real generator's own self-test is run on the real tree as one case, so
the hook's old behaviour is measured). The enforce file is created only inside a scratch tree. Nothing is sent, pushed or
deployed. Cases are independent and run on a small thread pool, reported in order.
"""
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import git_bash_resolver  # noqa: E402  the estate's canonical Git Bash, never a bare `bash`

PROJ = "org/missions/D0/TEST/TEST_PROJ"
ORDER = ("# TO\n<to_id>TEST_PROJ.TO-1</to_id>\n<issued_to>0.9.0_WK_TEST_PROJ~1</issued_to>\n<issued_by>2.0.0_SA_COO~C</issued_by>\n"
         "<status>complete</status>\n<round>1</round>\n"
         '<criterion id="T1-AC1" cell_refs="X"><invocation>x</invocation></criterion>\n'
         '<criterion id="T1-AC2" cell_refs="X" judgment="true"/>\n')
PROOF = {"to_id": "TEST_PROJ.TO-1", "acceptance": [
    {"criterion_id": "T1-AC1", "status": "PASS"},
    {"criterion_id": "T1-AC2", "status": "UNVERIFIABLE-BY-INSTRUMENT", "judgment": True}]}
ADJ = [{"id": "TEST_PROJ-C-S1", "surfaced_by": "3.0.0_SA_CVO", "adjudicates": ["T1-AC2"],
        "one_line": "TEST_PROJ.TO-1 T1-AC2: MET on this seat's read."}]
STUB = ('import os, sys\nprint("RESULT stub generator rc=" + os.environ.get("STUB_GEN_RC", "0"))\n'
        'sys.exit(int(os.environ.get("STUB_GEN_RC", "0")))\n')


def run(argv, cwd=None, env=None, timeout=100):
    try:
        p = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)
        return p.returncode, (p.stdout + p.stderr)
    except subprocess.TimeoutExpired:
        return 124, "TIMEOUT"


def git(repo, *args):
    return run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "-C", str(repo), *args])


def put(root, rel, text):
    p = Path(root) / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8", newline="\n")


def _rm_ro(func, path, _exc):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def last_line(out):
    lines = [x for x in out.replace("\r", "").split("\n") if x.strip()]
    return lines[-1] if lines else ""


def project_json(stage, note="a"):
    return json.dumps({"project_code": "TEST_PROJ", "macro_code": "TEST", "dep_stage": stage, "note": note}, indent=1) + "\n"


def make_template(tmp, device):
    t = Path(tmp) / "template"
    for rel in (".tools/git-hooks/missions-tree-check.sh", ".tools/round-close-check.py", ".tools/seat-list.py",
                "lib/seat_roles.py", "lib/devices.py", "org/ref/SEAT_ROLES.json", "org/devices/DEVICES.json"):
        dst = t / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPO / rel, dst)
    put(t, ".tools/missions-tree-index.py", STUB)
    put(t, PROJ + "/project.json", project_json("EXECUTING"))
    put(t, PROJ + "/task-orders/TEST_PROJ.TO-1.one.md", ORDER)
    put(t, PROJ + "/deliverables/0.9.0_WK_TEST_PROJ~1/TEST_PROJ.TO-1.one.proof_of_spec.json", json.dumps(PROOF))
    put(t, PROJ + "/surprise-channel/adjudications/ADJUDICATION_v1.md", "# rows\n\n```json\n%s\n```\n" % json.dumps(ADJ))
    run(["git", "init", "-q", "-b", "CLOUD", str(t)])
    git(t, "add", "-A")
    git(t, "commit", "-q", "-m", "template")
    return t


def hook(tmp, template, name, device, head="EXECUTING", staged="ROUND_CLOSE", enforce=False, reviewer=False, graded=True,
         override=None, gen_rc=0, drop_tool=False, stage_other=False, old_file=False, old_var_only=False):
    fx = Path(tmp) / name
    shutil.copytree(template, fx)
    now = int(time.time())
    seats = {"2.0.0_SA_COO~C": {"last_seen_epoch": now, "summary": "x"}}
    if reviewer:
        seats["3.0.0_SA_CVO"] = {"last_seen_epoch": now, "summary": "x"}
    put(fx, "org/mcp/liveness.json", json.dumps(seats))
    if not graded:
        # the hook runs round-close-check.py --staged, which reads the INDEX: the removal must be staged
        git(fx, "rm", "-q", PROJ + "/surprise-channel/adjudications/ADJUDICATION_v1.md")
    sgdir = fx / "scratch_seat_gates"
    sgdir.mkdir()
    if enforce:
        put(sgdir, "seat-gates.round-close.missions-tree-check.enforce", "scratch\n")
    if old_file:
        put(sgdir, "seat-gates.enforce", "scratch\n")
    if head != "EXECUTING":
        put(fx, PROJ + "/project.json", project_json(head))
        git(fx, "add", PROJ + "/project.json")
        git(fx, "commit", "-q", "-m", "head stage")
    if drop_tool:
        (fx / ".tools/round-close-check.py").unlink()
    if stage_other:
        put(fx, PROJ + "/task-orders/TEST_PROJ.TO-9.nine.md", ORDER.replace("TO-1", "TO-9"))
        git(fx, "add", PROJ + "/task-orders/TEST_PROJ.TO-9.nine.md")
    else:
        put(fx, PROJ + "/project.json", project_json(staged, note="b"))
        git(fx, "add", PROJ + "/project.json")
    env = dict(os.environ, PRECOMP_REPO_ROOT=str(fx), AGENTBUS_DEVICE=device, STUB_GEN_RC=str(gen_rc))
    env["OPAL_SEAT_GATES_ENFORCE_DIR"] = str(sgdir)
    env.pop("OPAL_SEAT_GATES_ENFORCE_FILE", None)
    if old_var_only:
        put(sgdir, "elsewhere.flag", "scratch\n")
        env["OPAL_SEAT_GATES_ENFORCE_FILE"] = str(sgdir / "elsewhere.flag")
    env.pop("OWNED_PATHS_STAGED_FILES", None)
    env.pop("SEAT_GATES_OVERRIDE", None)
    if override:
        env["SEAT_GATES_OVERRIDE"] = override
    rc, out = run(git_bash_resolver.bash_argv(str(fx / ".tools/git-hooks/missions-tree-check.sh")), cwd=str(fx), env=env)
    _dev = env.get("AGENTBUS_DEVICE", "").strip()
    _ok = bool(_dev) and all(c in "abcdefghijklmnopqrstuvwxyz0123456789-" for c in _dev)
    audit = fx / ("org/git-author-override-audit.%s.log" % _dev if _ok else "org/git-author-override-audit.log")
    return rc, out, (audit.read_text(encoding="utf-8") if audit.exists() else "")


def main():
    from importlib.util import module_from_spec, spec_from_file_location
    spec = spec_from_file_location("devs", REPO / "lib" / "devices.py")
    devs = module_from_spec(spec)
    spec.loader.exec_module(devs)
    device = devs.names(devs.load())[0]
    tmp = tempfile.mkdtemp(prefix="close_gates_")
    cases = []

    def add(name, fn):
        cases.append((name, fn))

    try:
        template = make_template(tmp, device)
        n = [0]

        def H(**kw):
            n[0] += 1
            return hook(tmp, template, "c%d" % n[0], device, **kw)

        def tool_selftest(script, want):
            def fn():
                rc, out = run([sys.executable, str(TOOLS / script), "--selftest"], timeout=110)
                line = last_line(out)
                return rc == 0 and re.fullmatch(want, line) is not None and line.endswith("ok=True"), line
            return fn

        add("round-close-check.py --selftest", tool_selftest("round-close-check.py", r"ROUND-CLOSE-SELFTEST cases=\d+/\d+ ok=True"))
        add("research-owed.py --selftest", tool_selftest("research-owed.py", r"RESEARCH-OWED-SELFTEST cases=\d+/\d+ ok=True"))

        def real_generator_selftest():
            rc, out = run([sys.executable, str(TOOLS / "missions-tree-index.py"), "--self-test"], cwd=str(REPO), timeout=110)
            m = re.search(r"missions-tree-index --self-test: (\d+)/(\d+) PASS", out)
            return rc == 0 and bool(m) and m.group(1) == m.group(2), last_line(out)
        add("the real generator's own self-test still passes with the hook edited", real_generator_selftest)

        def syntax():
            rc, out = run(git_bash_resolver.bash_argv("-n", str(TOOLS / "git-hooks" / "missions-tree-check.sh")))
            return rc == 0, out.strip()[:200] or "bash -n clean"
        add("the edited hook parses (bash -n)", syntax)

        def warn_admits():
            rc, out, _ = H()
            return rc == 0 and "verdict=REFUSED" in out and "WARN: missions-tree-check close-gate" in out and "would be REFUSED under ENFORCE" in out, "rc=%d %s" % (rc, last_line(out))
        add("WARN mode: a close with no reviewer on the box is printed and admitted", warn_admits)

        def old_file_alone():
            rc, out, _ = H(old_file=True)
            return (rc == 0 and "org/mcp/seat-gates.enforce is retired and turns on nothing" in out and "BLOCKED" not in out
                    and "would be REFUSED under ENFORCE" in out), "rc=%d %s" % (rc, last_line(out))
        add("the retired single file alone leaves the gate in WARN and prints the retired line", old_file_alone)

        def old_file_with_new():
            rc, out, _ = H(old_file=True, enforce=True)
            return rc == 1 and "is retired and turns on nothing" in out and "BLOCKED: missions-tree-check close-gate" in out, "rc=%d %s" % (rc, last_line(out))
        add("the new file still enforces when the retired file is also present", old_file_with_new)

        def old_var_ignored():
            rc, out, _ = H(old_var_only=True)
            return rc == 0 and "BLOCKED" not in out and "would be REFUSED under ENFORCE" in out, "rc=%d %s" % (rc, last_line(out))
        add("OPAL_SEAT_GATES_ENFORCE_FILE is no longer read (set to an existing file it changes nothing)", old_var_ignored)

        def enforce_refuses():
            rc, out, _ = H(enforce=True)
            return rc == 1 and "BLOCKED: missions-tree-check close-gate" in out and "reviewer=ABSENT" in out, "rc=%d %s" % (rc, last_line(out))
        add("ENFORCE (scratch enforce file): the same close is refused, the line printed", enforce_refuses)

        def enforce_admits_all_present():
            rc, out, _ = H(enforce=True, reviewer=True)
            return rc == 0 and "verdict=MAY-CLOSE" in out and "BLOCKED" not in out, "rc=%d %s" % (rc, last_line(out))
        add("ENFORCE: reviewer on the box and every judgment graded is admitted", enforce_admits_all_present)

        def enforce_ungraded():
            rc, out, _ = H(enforce=True, reviewer=True, graded=False)
            return rc == 1 and "ungraded=1" in out and "BLOCKED: missions-tree-check close-gate" in out, "rc=%d %s" % (rc, last_line(out))
        add("ENFORCE: reviewer present but a judgment criterion ungraded is refused", enforce_ungraded)

        def to_closed():
            rc, out, _ = H(enforce=True, staged="CLOSED")
            return rc == 1 and "dep_stage EXECUTING -> CLOSED" in out, "rc=%d %s" % (rc, last_line(out))
        add("ENFORCE: dep_stage to CLOSED is a close too", to_closed)

        def not_a_close():
            rc, out, _ = H(enforce=True, head="ROUND_CLOSE", staged="EXECUTING")
            return rc == 0 and "ROUND-CLOSE project=" not in out and "BLOCKED" not in out, "rc=%d %s" % (rc, last_line(out))
        add("a dep_stage change that is not a close (ROUND_CLOSE to EXECUTING) is untouched under ENFORCE", not_a_close)

        def other_stage():
            rc, out, _ = H(enforce=True, head="EXECUTING", staged="EXECUTING")
            return rc == 0 and "ROUND-CLOSE project=" not in out, "rc=%d %s" % (rc, last_line(out))
        add("a project.json edit that leaves dep_stage alone is untouched under ENFORCE", other_stage)

        def already_closed():
            rc, out, _ = H(enforce=True, head="ROUND_CLOSE", staged="ROUND_CLOSE")
            return rc == 0 and "ROUND-CLOSE project=" not in out, "rc=%d %s" % (rc, last_line(out))
        add("a project already at ROUND_CLOSE and edited again is not a new close", already_closed)

        def no_project_staged():
            rc, out, _ = H(enforce=True, stage_other=True)
            return rc == 0 and "ROUND-CLOSE project=" not in out, "rc=%d %s" % (rc, last_line(out))
        add("a staged task order and no project.json never reaches the close gate", no_project_staged)

        def override():
            rc, out, audit = H(enforce=True, override="scratch test of the audited override")
            return rc == 0 and "OVERRIDDEN (audited)" in out and "SEAT_GATES_OVERRIDE" in audit and "project=TEST_PROJ" in audit, "rc=%d audit=%s" % (rc, audit.strip()[:120])
        add("ENFORCE with SEAT_GATES_OVERRIDE admits and writes the audit line", override)

        def tool_missing_enforce():
            rc, out, _ = H(enforce=True, drop_tool=True)
            return rc == 1 and "gave no verdict" in out, "rc=%d %s" % (rc, last_line(out))
        add("ENFORCE: a close-check that cannot run refuses (fail-closed like the rest of the hook)", tool_missing_enforce)

        def tool_missing_warn():
            rc, out, _ = H(drop_tool=True)
            return rc == 0 and "gave no verdict" in out, "rc=%d %s" % (rc, last_line(out))
        add("WARN: a close-check that cannot run is printed and the close goes on", tool_missing_warn)

        def generator_first():
            rc, out, _ = H(enforce=True, reviewer=True, gen_rc=1)
            return rc == 1 and "the project tree's validator REFUSES" in out and "close-gate" not in out, "rc=%d %s" % (rc, last_line(out))
        add("the generator's refusal still comes first and unchanged", generator_first)

        def _rcc():
            from importlib.util import module_from_spec, spec_from_file_location
            sp = spec_from_file_location("rcc_t", TOOLS / "round-close-check.py")
            m = module_from_spec(sp)
            sp.loader.exec_module(m)
            return m

        def _order_case(body, name="P.TO-1.x", inst_to_id=None, want="match"):
            def fn():
                rcc = _rcc()
                d = tempfile.mkdtemp(prefix="rcc_ord_", dir=tmp)
                put(d, "task-orders/%s.md" % name, body)
                cid = "C1"
                if inst_to_id is not None:
                    put(d, "deliverables/w/%s.proof_of_spec.json" % name,
                        json.dumps({"to_id": inst_to_id, "acceptance": [{"criterion_id": cid, "status": "PASS"}]}))
                src = rcc.WorkTree(d)
                o = rcc.read_orders(src, d, None, None)[0]
                if want == "match":
                    ok, why = rcc.proof_state(src, o, d, str(REPO), False)
                    return ok, "id=%s %s" % (o["id"], why)
                return o["status"] == want, "status=%s" % o["status"]
            return fn

        crit = "<criterion id=%sC1%s><invocation>x</invocation></criterion>" % (chr(34), chr(34))
        nl = chr(10)
        add("no to_id: the order id is the file stem and a proof carrying the stem matches",
            _order_case(nl.join(["<status>complete</status>", crit]), inst_to_id="P.TO-1.x"))
        add("to_id present: the order still matches by to_id",
            _order_case(nl.join(["<to_id>P.TO-9</to_id>", "<status>complete</status>", crit]), inst_to_id="P.TO-9"))
        add("pending then complete reads complete",
            _order_case(nl.join(["<status>pending</status>", "<status>complete</status>", crit]), want="complete"))
        add("complete then pending reads pending",
            _order_case(nl.join(["<status>complete</status>", "<status>pending</status>", crit]), want="pending"))

        with ThreadPoolExecutor(max_workers=4) as pool:
            futures = [(name, pool.submit(fn)) for name, fn in cases]
            results = []
            for name, fut in futures:
                try:
                    ok, detail = fut.result()
                except Exception:  # noqa: BLE001 - a crashed case is a failed case, printed
                    ok, detail = False, traceback.format_exc().strip().splitlines()[-1]
                results.append(bool(ok))
                print("%s  %s -- %s" % ("PASS" if ok else "FAIL", name, detail))
    finally:
        shutil.rmtree(tmp, onerror=_rm_ro)
    ok = all(results) and len(results) == len(cases)
    print("CLOSE-GATES-TEST cases=%d/%d ok=%s" % (sum(results), len(cases), ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
