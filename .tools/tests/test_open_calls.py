#!/usr/bin/env python3
"""Cases for .tools/open-calls.py (NFRA_CTLPLN workstream SEATS, cell CT-s-5).

Run: python .tools/tests/test_open_calls.py   (LAST line: OPEN-CALLS-TEST cases=<k>/<n> ok=<True|False>)

Everything runs on a temporary state directory (OPAL_STATE_ROOT) and a temporary cross-box directory (OPAL_CROSSBOX_ROOT);
the real org/devices/state and org/devices/crossbox are never written. Box names come from the device register through
lib/devices.py. The tool is called in-process through its main(). Files this run creates are removed by name at the end.
"""
import contextlib
import importlib.util
import io
import json
import os
import re
import sys
import tempfile
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(HERE)
REPO = os.path.dirname(TOOLS)


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(REPO, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Scratch:
    def __init__(self):
        self.base = tempfile.mkdtemp(prefix="opalcalls_test_")
        self.files, self.dirs = [], [self.base]

    def write(self, rel, text):
        path = os.path.join(self.base, rel)
        d = os.path.dirname(path)
        chain = []
        while d != self.base and not os.path.isdir(d):
            chain.append(d)
            d = os.path.dirname(d)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.dirs.extend(reversed(chain))
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        if path not in self.files:
            self.files.append(path)
        return path

    def track(self, path):
        self.files.append(path)

    def cleanup(self):
        for path in self.files:
            for p in (path, path + ".tmp"):
                try:
                    os.remove(p)
                except OSError:
                    pass
        for d in reversed(self.dirs):
            try:
                os.rmdir(d)
            except OSError:
                pass


def main():
    tool = load("opal_open_calls", ".tools/open-calls.py")
    dev = load("opal_devices", "lib/devices.py")
    reg = dev.load()
    names = dev.names(reg)
    # the project the tests call about is NFRA_CTLPLN; its box is read from its own project.json, not typed here
    pj = json.load(open(os.path.join(REPO, "org", "missions", "D0", "NFRA", "NFRA_CTLPLN", "project.json"), encoding="utf-8"))
    here = dev.resolve(str(pj.get("placement") or pj.get("fabric")), reg)
    other = next(n for n in names if n != here)
    sc = Scratch()
    state_dir, cross_dir = os.path.join(sc.base, "state"), os.path.join(sc.base, "crossbox")
    os.makedirs(cross_dir)
    sc.dirs.extend([state_dir, cross_dir])
    os.makedirs(state_dir)
    os.environ["OPAL_STATE_ROOT"] = state_dir
    os.environ["OPAL_CROSSBOX_ROOT"] = cross_dir
    os.environ["AGENTBUS_DEVICE"] = here
    os.environ["OPAL_AGENT_SERIAL"] = "0.9.0_WK_TEST~1"
    mine_file = os.path.join(state_dir, here, "open_calls.json")
    other_file = os.path.join(state_dir, other, "open_calls.json")
    sc.dirs.extend([os.path.join(state_dir, here), os.path.join(state_dir, other)])
    sc.files.append(mine_file)
    sc.files.append(other_file)

    def run(*argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                rc = tool.main(list(argv))
            except SystemExit as exc:
                rc = exc.code if isinstance(exc.code, int) else 2
        return rc, out.getvalue(), err.getvalue()

    def rows():
        return json.load(open(mine_file, encoding="utf-8"))["rows"]

    cases = []
    ruling = sc.write("ruling.md", "RULING -- fixture\n")
    nowhere = sc.write("order_nowhere.md", "<status>issued</status>\n<risk>LOCAL</risk>\n<paths>\norg/zz_open_calls_test_nowhere/f.txt\n</paths>\n")
    # a fork needs its own --context (40-600 characters) and --rec (check_call_text in the tool); the test supplies both
    base_add = ["add", "--project", "NFRA_CTLPLN", "--asked-by", "1.0.0_SA_CTO", "--source", "docs/none.md",
                "--context", "Fixture call: the test creates it to exercise the list shape, the close path and the refusals.",
                "--rec", "Fixture recommendation: none; the test reads the row, it does not act on it."]
    try:
        # 1. add (an OWN-BOX call: a scratch order naming one path nobody owns)
        rc, out, err = run(*base_add, "--subject", "own-box call", "--orders", nowhere)
        m = re.search(r"ADDED id=(\S+)", out)
        cid_own = m.group(1) if m else ""
        doc = json.load(open(mine_file, encoding="utf-8")) if os.path.exists(mine_file) else {}
        cases.append(("add writes this box's list with the named shape and an id <device>-<UTC stamp>-<4 hex>",
                      rc == 0 and set(doc) == {"schema", "device", "written_at", "written_by", "rows"} and doc["device"] == here
                      and bool(re.fullmatch(re.escape(here) + r"-\d{8}T\d{6}Z-[0-9a-f]{4}", cid_own))
                      and rows()[0]["state"] == "OPEN" and set(rows()[0]["scope"]) >= {"paths", "placement", "resources", "shared", "risk", "verdict"}))
        cases.append(("the measured scope is saved on the call and an untouched path reads OWN-BOX",
                      rows()[0]["scope"]["verdict"] == "OWN-BOX" and "verdict=OWN-BOX" in out))

        # 2. list
        rc, out, err = run("list")
        cases.append(("list prints the row with the file's age", rc == 0 and cid_own in out and "age " in out and "OPEN-CALLS-LIST" in out))

        # 3. close (OWN-BOX needs no cross-box file)
        rc, out, err = run("close", "--id", cid_own, "--by", "1.0.0_SA_CTO", "--ruling", ruling)
        cases.append(("an OWN-BOX call closes with its ruling's path", rc == 0 and rows()[0]["state"] == "CLOSED"
                      and rows()[0]["closed"]["by"] == "1.0.0_SA_CTO" and rows()[0]["closed"]["crossbox"] is None))
        rc, out, err = run("close", "--id", cid_own, "--by", "1.0.0_SA_CTO", "--ruling", ruling)
        cases.append(("closing a closed call is refused", rc == 1 and "already CLOSED" in err))

        # 4. a CROSS-BOX call cannot be closed alone, and can with its CLOSED-BOTH file
        rc, out, err = run(*base_add, "--subject", "cross-box call", "--roots", "infra/aws/terraform/shared-infra")
        m = re.search(r"ADDED id=(\S+)", out)
        cid_x = m.group(1) if m else ""
        cases.append(("a call on the fence root reads CROSS-BOX and is routed", rc == 0 and "verdict=CROSS-BOX" in out and "ROUTE:" in out
                      and rows()[-1]["scope"]["verdict"] == "CROSS-BOX"))
        rc, out, err = run("close", "--id", cid_x, "--by", "1.0.0_SA_CTO", "--ruling", ruling)
        cases.append(("a CROSS-BOX call with no cross-box file cannot be closed", rc == 1 and "CLOSED-BOTH" in err and rows()[-1]["state"] == "OPEN"))
        sc.write("crossbox/c1.json", json.dumps({"id": "c1", "kind": "CALL", "from_device": here, "to_device": other, "subject": "about " + cid_x,
                                                 "state": "ACKED", "body_path": "docs/none.md"}))
        rc, out, err = run("close", "--id", cid_x, "--by", "1.0.0_SA_CTO", "--ruling", ruling)
        cases.append(("a cross-box file that is only ACKED does not close it", rc == 1 and rows()[-1]["state"] == "OPEN"))
        sc.write("crossbox/c2.json", json.dumps({"id": "c2", "kind": "CALL", "from_device": here, "to_device": other, "subject": "another call",
                                                 "state": "CLOSED-BOTH", "body_path": "docs/none.md"}))
        rc, out, err = run("close", "--id", cid_x, "--by", "1.0.0_SA_CTO", "--ruling", ruling)
        cases.append(("a CLOSED-BOTH file that does not name the call does not close it", rc == 1 and rows()[-1]["state"] == "OPEN"))
        sc.write("crossbox/c1.json", json.dumps({"id": "c1", "kind": "CALL", "from_device": here, "to_device": other, "subject": "about " + cid_x,
                                                 "state": "CLOSED-BOTH", "body_path": "docs/none.md"}))
        rc, out, err = run("close", "--id", cid_x, "--by", "1.0.0_SA_CTO", "--ruling", ruling)
        cases.append(("with its own CLOSED-BOTH file the CROSS-BOX call closes and cites the file",
                      rc == 0 and rows()[-1]["state"] == "CLOSED" and rows()[-1]["closed"]["crossbox"] == "c1"))
        rc, out, err = run("close", "--id", cid_x, "--by", "x", "--ruling", os.path.join(sc.base, "no_such_ruling.md"))
        cases.append(("a ruling that is not a file is refused", rc == 1))

        # 5. one writer per box
        before = os.path.exists(other_file)
        rc, out, err = run(*base_add, "--subject", "wrong box", "--orders", nowhere, "--device", other)
        cases.append(("a call written to another box's list is refused and nothing is written there",
                      rc == 1 and "One writer per box" in err and os.path.exists(other_file) == before))
        sc.write("state/%s/open_calls.json" % other, json.dumps({
            "schema": "open-calls/1", "device": other, "written_at": "2026-10-07T00:00:00Z", "written_by": "x",
            "rows": [{"id": other + "-20261007T000000Z-abcd", "project": "P", "subject": "s", "asked_by": "a", "source": "s",
                      "state": "OPEN", "opened_at": "2026-10-07T00:00:00Z", "scope": {"verdict": "OWN-BOX"}, "closed": None}]}))
        rc, out, err = run("close", "--id", other + "-20261007T000000Z-abcd", "--by", "x", "--ruling", ruling)
        cases.append(("closing a call that sits on another box's list is refused", rc == 1 and "writes its own list only" in err))

        # 6. --all names a box with no file as absent
        rc, out, err = run("list", "--all")
        absent_names = [n for n in names if n not in (here, other)]
        cases.append(("--all reads the files that exist and names every box with no file as ABSENT, not empty",
                      rc == 0 and all(("ABSENT %s:" % n) in out for n in absent_names) and "Absent is not empty" in out
                      and ("absent=" + ",".join(absent_names)) in out and other + "-20261007T000000Z-abcd" in out and "age " in out))
        rc, out, err = run("list", "--device", names[-1] if names[-1] not in (here, other) else here)
        cases.append(("list --device names one box's file", rc == 0 and "OPEN-CALLS-LIST" in out))

        # 7. a key the reader does not know is refused
        good = json.load(open(mine_file, encoding="utf-8"))
        bad_top = dict(good, surprise="x")
        sc.write("state/%s/open_calls.json" % here, json.dumps(bad_top))
        rc, out, err = run("list")
        cases.append(("an unknown top-level key in a list file is refused", rc == 3 and "unknown key" in out))
        bad_row = json.loads(json.dumps(good))
        bad_row["rows"][0]["surprise"] = "x"
        sc.write("state/%s/open_calls.json" % here, json.dumps(bad_row))
        rc, out, err = run("list")
        cases.append(("an unknown key in a row is refused", rc == 3 and "unknown key" in out))
        rc, out, err = run(*base_add, "--subject", "onto a bad file", "--orders", nowhere)
        cases.append(("add onto a file with an unknown key is refused, never overwrites it", rc == 3
                      and json.load(open(mine_file, encoding="utf-8"))["rows"][0].get("surprise") == "x"))
        sc.write("state/%s/open_calls.json" % here, json.dumps(dict(good, device=other)))
        rc, out, err = run("list")
        cases.append(("a file whose device is not the box named by its folder is refused", rc == 3))
    except Exception:   # a crashed case is a failed case, never a silent pass
        traceback.print_exc()
        cases.append(("no case raised", False))
    finally:
        sc.cleanup()
    fails = 0
    for label, ok in cases:
        print("  %s  %s" % ("PASS" if ok else "FAIL", label))
        fails += 0 if ok else 1
    print("OPEN-CALLS-TEST cases=%d/%d ok=%s" % (len(cases) - fails, len(cases), fails == 0))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
