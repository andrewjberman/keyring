#!/usr/bin/env python3
"""Cases for .tools/crossbox-call.py (NFRA_CTLPLN workstream SEATS, cell CT-s-6).

Run: python .tools/tests/test_crossbox_call.py   (LAST line: CROSSBOX-TEST cases=<k>/<n> ok=<True|False>)

Part 1 runs the tool's own exchange between two scratch checkouts and reports each of its cases as a separate assertion.
Part 2 adds: the inbox file's name and header against the writer's code in org/mcp/server.py; the file landing where
org/mcp/inbox-watch.sh reads (the watcher's own resolution lines are run in bash, the watcher itself is NOT started); an order
for a serial with no inbox on the box refused ("no such seat on this box"); an unknown key refused; the command line end to
end; the two existing readers (.tools/crossbox-deploy-check.py, .tools/open-calls.py) reading a file this tool wrote; and the
pending probe in org/ref/SEAT_RULES.json for this cell.
Everything is built in temporary directories that are removed at the end. Nothing is sent, pushed or started.
"""
from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import git_bash_resolver  # noqa: E402  the estate's canonical Git Bash, never a bare `bash` (the WSL stub)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cb = load("crossbox_call_under_test", TOOLS / "crossbox-call.py")
LOCAL = threading.local()   # each part runs on its own thread and fills its own list; the lists are joined in order


def check(name, ok, detail=""):
    LOCAL.out.append((name, bool(ok), str(detail)[:200]))


def raised(kind, fn, needle=""):
    try:
        fn()
    except kind as exc:
        return needle in str(exc), str(exc)
    return False, "no %s raised" % kind.__name__


def publish(h, box, *paths):
    """Commit, then push to the fixture's OWN local origin (a temporary bare repository the Harness made). `line` refuses a commit
    that is not on origin, by design; the fixture makes its commits reachable from its own origin, so the checks below run the
    tool's real refusals and not a dependency on the state of any real remote."""
    h.commit(box, *paths)
    h.push(box.root)


def opened(h, subject="Order from the other box", call_id=None, to_serial=None, kind="ORDER"):
    lines = h.a.open(kind, h.b.device, to_serial or (cb.SEAT + cb.SEAT_LANE), "1.0.0_SA_CTO", subject, cb.BODY, call_id=call_id)
    cid = lines[0].split()[1]
    publish(h, h.a, h.a.rel(cid))
    return cid, h.a.line(cid)[0]


def part1():
    tmp = tempfile.mkdtemp(prefix="crossbox-test1-")
    try:
        for name, ok, detail in cb.run_cases(tmp):
            check("selftest case: " + name, ok, detail)
    except Exception as exc:
        check("selftest exchange ran", False, "%s: %s" % (type(exc).__name__, exc))
    finally:
        cb.rmtree_force(tmp)


def part2_writer_and_watcher():
    tmp = tempfile.mkdtemp(prefix="crossbox-test2-")
    try:
        h = cb.Harness(tmp)
        cid, line = opened(h)
        h.pull(h.b, h.a, ff=True)
        h.b.receive(line)
        inbox = h.b.root / "org" / "mcp" / "inbox" / cb.SEAT / cb.SEAT_LANE
        landed = sorted(inbox.glob("*.md"))
        text = landed[0].read_text(encoding="utf-8")
        server = (REPO / "org" / "mcp" / "server.py").read_text(encoding="utf-8")
        block = server[server.index("msg_content = ("):server.index("msg_path.write_text(msg_content")]
        writer_fields = re.findall(r"\*\*([A-Za-z-]+):\*\*", block)
        writer_head = re.search(r'f"# (Message from) \{from_agent\}', block)
        mine = re.findall(r"^\*\*([A-Za-z-]+):\*\*", text, re.M)
        check("inbox header: the writer's code writes To, Date, Subject in this order", writer_fields[:1] == ["To"] and writer_fields[-1] == "Subject", writer_fields)
        check("inbox header: the first line is the broker's '# Message from <serial>'", bool(writer_head) and text.startswith("# Message from 1.0.0_SA_CTO"), text.splitlines()[0])
        check("inbox header: same fields as the broker's plus one Cross-box stamp, Subject last", [f for f in mine if f != "Cross-box"] == [f for f in writer_fields if f in ("To", "Date", "Subject")] and "Cross-box" in mine and mine[-1] == "Subject", mine)
        fname = re.search(r'filename = f"([^"]+)"', server)
        check("inbox filename: the broker's pattern is {ts}_{safe_from}_{safe_subject}.md", fname is not None and fname.group(1) == "{ts}_{safe_from}_{safe_subject}.md", fname.group(1) if fname else "no match")
        check("inbox filename: this tool's name fits that pattern", re.fullmatch(r"\d{8}T\d{6}Z_[A-Za-z0-9._-]+_[A-Za-z0-9._-]{1,40}\.md", landed[0].name) is not None, landed[0].name)
        check("inbox body: only the cross-box file path and its body path", text.split("\n\n", 1)[1].strip().splitlines() == ["file: org/devices/crossbox/%s.json" % cid, "body: " + cb.BODY], text.split("\n\n", 1)[1])

        watcher = (REPO / "org" / "mcp" / "inbox-watch.sh").read_text(encoding="utf-8")
        resolve = watcher[watcher.index("# Resolve agent folder name"):watcher.index('mkdir -p "$WATCH_DIR/read"')]
        script = 'SCRIPT_DIR="%s"\nINBOX_BASE="$SCRIPT_DIR/inbox"\nSERIAL="%s"\nBASE_SERIAL="${SERIAL%%%%~*}"\nSUFFIX=""\n' \
                 'if [ "$SERIAL" != "$BASE_SERIAL" ]; then SUFFIX="${SERIAL#*~}"; fi\n%s\necho "$WATCH_DIR"\n' % (
                     (h.b.root / "org" / "mcp").as_posix(), cb.SEAT + cb.SEAT_LANE, resolve)
        proc = subprocess.run(git_bash_resolver.bash_argv("-c", script), capture_output=True, text=True, timeout=60)
        watch_dir = Path(proc.stdout.strip().splitlines()[-1]) if proc.stdout.strip() else None
        same = watch_dir is not None and watch_dir.resolve() == inbox.resolve() and any(watch_dir.glob("*.md"))
        check("watcher: its own resolution lines (run in bash, not started) read the directory the file landed in, and *.md is there", same and proc.returncode == 0, "%s rc=%s %s" % (watch_dir, proc.returncode, proc.stderr[:80]))
    except Exception as exc:
        check("writer and watcher comparison ran", False, "%s: %s" % (type(exc).__name__, exc))
    finally:
        cb.rmtree_force(tmp)


def part2_refusals():
    tmp = tempfile.mkdtemp(prefix="crossbox-test3-")
    try:
        h = cb.Harness(tmp)
        cid, line = opened(h, to_serial="9.9.1_ZZ_Absent")
        h.pull(h.b, h.a, ff=True)
        ok, why = raised(cb.Refused, lambda: h.b.receive(line), "no such seat on this box")
        check("an order for a serial with no agent folder on this box: no such seat on this box", ok, why)
        (h.b.root / "org" / "tier2_senior" / "9.9.1_ZZ_Absent").mkdir()
        ok, why = raised(cb.Refused, lambda: h.b.receive(line), "no such seat on this box")
        check("an order for a seat whose inbox directory does not exist: no such seat on this box", ok, why)
        check("a refused order wrote no inbox directory and no file", not (h.b.root / "org" / "mcp" / "inbox" / "9.9.1_ZZ_Absent").exists(), "")
        ok, why = raised(cb.Refused, lambda: h.a.receive(line), "this order is for box")
        check("an order read on the box that sent it is refused", ok, why)
        doc = json.loads(h.a.path(cid).read_text(encoding="utf-8"))
        doc["closed"]["extra"] = 1
        ok, why = raised(cb.Refused, lambda: cb.check_call(doc, "x"), "unknown key")
        check("an unknown key inside the closed block is refused", ok, why)
        doc = json.loads(h.a.path(cid).read_text(encoding="utf-8"))
        del doc["body_path"]
        ok, why = raised(cb.Refused, lambda: cb.check_call(doc, "x"), "missing key")
        check("a missing key is refused", ok, why)
        for bad in ("has a | bar", "caf\u00e9 non-ascii", ""):
            ok, why = raised(cb.Refused, lambda b=bad: h.a.open("CALL", h.b.device, cb.SEAT, "1.0.0_SA_CTO", b, cb.BODY))
            check("open refuses the subject %r" % bad, ok, why)
        ok, why = raised(cb.Refused, lambda: h.a.open("CALL", h.b.device, cb.SEAT, "1.0.0_SA_CTO", "s", "../outside.md"), "inside the repository")
        check("open refuses a body path that leaves the repository", ok, why)
        ok, why = raised(cb.Refused, lambda: h.a.open("CALL", "nowhere-box", cb.SEAT, "1.0.0_SA_CTO", "s", cb.BODY), "device register")
        check("open refuses a device the register does not hold", ok, why)
        ok, why = raised(cb.Refused, lambda: h.a.close(cid, "from", "1.0.0_SA_CTO"), "not acknowledged")
        check("close before an acknowledgement is refused", ok, why)
        ok, why = raised(cb.Refused, lambda: h.b.close(cid, "from", "1.0.0_SA_CTO"), "sending box")
        check("a side can be closed only on its own box", ok, why)
        ok, why = raised(cb.Refused, lambda: h.b.ack(cid, "2.0.0_SA_COO"), "named seat")
        check("only the named seat acknowledges", ok, why)
        lines = h.a.line(cid)
        check("the bus line is short and carries no substance (under 150 words, no body text)", len(lines[0].split()) < 150 and "selftest body" not in lines[0], lines[0])
        # a second copy that disagrees must not merge silently
        h.pull(h.b, h.a, ff=True)
        h.b.ack(cid, "9.9.1_ZZ_Absent", at="2026-10-08T01:00:00Z")
        mine = json.loads(h.a.path(cid).read_text(encoding="utf-8"))
        mine["ack"] = {"at": "2026-10-08T02:00:00Z", "by": "9.9.1_ZZ_Absent", "bus_message_id": None}
        h.a.path(cid).write_text(json.dumps(mine), encoding="utf-8")
        publish(h, h.a, h.a.rel(cid))
        h.pull(h.b, h.a, ff=False)
        ok, why = raised(cb.Refused, lambda: h.b.merge(cid, "FETCH_HEAD"), "different ack.at")
        check("merge refuses two copies that hold different values for one field", ok, why)
    except Exception as exc:
        check("refusal cases ran", False, "%s: %s" % (type(exc).__name__, exc))
    finally:
        cb.rmtree_force(tmp)


def part2_cli_and_readers():
    tmp = tempfile.mkdtemp(prefix="crossbox-test4-")
    try:
        h = cb.Harness(tmp)

        def cli(root, device, *argv):
            proc = subprocess.run([sys.executable, str(TOOLS / "crossbox-call.py"), "--root", str(root), "--device", device, *argv],
                                  capture_output=True, text=True, timeout=60)
            return proc.returncode, proc.stdout.strip()

        rc, out = cli(h.a.root, h.a.device, "open", "--kind", "CALL", "--to-device", h.b.device, "--to-serial", cb.SEAT + cb.SEAT_LANE,
                      "--from-serial", "1.0.0_SA_CTO", "--subject", "Needs the other box", "--body", cb.BODY, "--call-id", "OC-CLI-1")
        cid = out.split()[1] if out.startswith("OPENED") else ""
        check("cli: open exits 0 and prints the provisional line before the commit", rc == 0 and "@UNCOMMITTED" in out, out[:120])
        publish(h, h.a, h.a.rel(cid))
        rc, out = cli(h.a.root, h.a.device, "line", "--id", cid)
        check("cli: line exits 0 and prints the sendable line", rc == 0 and out.startswith("CROSSBOX " + cid), out)
        line = out
        rc2, out2 = cli(h.b.root, h.b.device, "receive", "--line", line)
        check("cli: receive before the pull exits 5 and says PULL-FIRST", rc2 == 5 and "PULL-FIRST" in out2, "rc=%s %s" % (rc2, out2[:80]))
        h.pull(h.b, h.a, ff=True)
        rc3, out3 = cli(h.b.root, h.b.device, "receive", "--line", line)
        check("cli: receive after the pull exits 0 and delivers", rc3 == 0 and out3.startswith("DELIVERED"), out3[:100])
        rc4, out4 = cli(h.b.root, h.b.device, "ack", "--id", cid, "--by", cb.SEAT + cb.SEAT_LANE)
        check("cli: ack exits 0 and prints the reply line last", rc4 == 0 and out4.splitlines()[-1].startswith("CROSSBOX-ACK " + cid), out4[-100:])
        rc5, out5 = cli(h.b.root, h.b.device, "list", "--open")
        check("cli: list --open shows the file with its state and a files/shown line", rc5 == 0 and cid in out5 and "CROSSBOX-LIST files=1 shown=1" in out5, out5[-100:])
        rc6, out6 = cli(h.a.root, h.a.device, "receive", "--line", "no line here")
        check("cli: a text with no CROSSBOX line exits 3", rc6 == 3, out6[:80])

        # the two existing readers read a file this tool wrote
        deploy = load("crossbox_deploy_check_cb", TOOLS / "crossbox-deploy-check.py")
        import datetime as dt
        now = dt.datetime(2026, 10, 8, 12, 0, 0)
        lines = h.a.open("CALL", h.b.device, cb.SEAT + cb.SEAT_LANE, "1.0.0_SA_CTO", "Hold the apply of infra/aws/terraform/rootx", cb.BODY, call_id="OC-CLI-2")
        deploy_hits, _ = deploy.measure_open_call(str(h.a.root), "infra/aws/terraform/rootx", [], now)
        check("reader crossbox-deploy-check.py: an OPEN file naming the root is a hit", any(lines[0].split()[1] in x for x in deploy_hits), deploy_hits)
        doc = json.loads(h.a.path(lines[0].split()[1]).read_text(encoding="utf-8"))
        doc["ack"] = {"at": "2026-10-08T01:00:00Z", "by": cb.SEAT + cb.SEAT_LANE, "bus_message_id": None}
        doc["closed"].update({"from_at": "2026-10-08T02:00:00Z", "from_by": "1.0.0_SA_CTO", "to_at": "2026-10-08T03:00:00Z", "to_by": cb.SEAT + cb.SEAT_LANE})
        h.a.path(doc["id"]).write_text(cb.dump(doc), encoding="utf-8")
        deploy_hits2, _ = deploy.measure_open_call(str(h.a.root), "infra/aws/terraform/rootx", [], now)
        check("reader crossbox-deploy-check.py: the same file at CLOSED-BOTH is no longer live", not any(doc["id"] in x for x in deploy_hits2), deploy_hits2)
        found = cb.open_calls_reader(h.a.root / cb.REL_DIR, "OC-CLI-2")
        check("reader open-calls.py: the call_id field links the CLOSED-BOTH file to its call", found == doc["id"] + ".json", found)
        other = cb.open_calls_reader(h.a.root / cb.REL_DIR, "OC-CLI-1")
        check("reader open-calls.py: a call whose file is not CLOSED-BOTH is not settled", other is None, other)
    except Exception as exc:
        check("cli and reader cases ran", False, "%s: %s" % (type(exc).__name__, exc))
    finally:
        cb.rmtree_force(tmp)


def probe_rule():
    rules = json.loads((REPO / "org" / "ref" / "SEAT_RULES.json").read_text(encoding="utf-8"))["rules"]
    mine = [r for r in rules if r.get("built_by") == "CT-s-6"]
    check("SEAT_RULES.json holds exactly one rule built by CT-s-6, with a probe for this tool", len(mine) == 1 and mine[0]["probe"] and mine[0]["probe"]["tool"] == ".tools/crossbox-call.py", [r["id"] for r in mine])
    return mine[0]["probe"] if len(mine) == 1 and mine[0]["probe"] else None


def probe_start(probe):
    argv = [sys.executable if a == "{PY}" else a.replace("{ROOT}", str(REPO)) for a in probe["argv"]]
    return subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)


def probe_finish(proc, probe):
    name = "the pending probe's argv runs this tool and its output matches the probe's expect regex"
    try:
        out, _ = proc.communicate(timeout=100)
    except subprocess.TimeoutExpired:
        proc.kill()
        check(name, False, "timeout")
        return
    last = out.strip().splitlines()[-1] if out.strip() else ""
    check(name, proc.returncode == 0 and re.search(probe["expect"], last) is not None, last)


def run_part(fn, *args):
    LOCAL.out = []
    fn(*args)
    return LOCAL.out


def main() -> int:
    LOCAL.out = []
    probe = probe_rule()
    running = probe_start(probe) if probe else None   # the probe's own selftest run goes on beside the other cases
    RESULTS = LOCAL.out
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(run_part, fn) for fn in (part1, part2_writer_and_watcher, part2_refusals, part2_cli_and_readers)]
        for fut in futures:
            RESULTS.extend(fut.result())
    LOCAL.out = RESULTS
    if running:
        probe_finish(running, probe)
    for name, ok, detail in RESULTS:
        print("%s %s%s" % ("ok  " if ok else "FAIL", name, "" if ok or not detail else "  -- " + detail))
    good = sum(1 for _, ok, _ in RESULTS if ok)
    print("CROSSBOX-TEST cases=%d/%d ok=%s" % (good, len(RESULTS), bool(RESULTS) and good == len(RESULTS)))
    return 0 if RESULTS and good == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
