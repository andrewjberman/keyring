#!/usr/bin/env python3
"""test_seat_list.py -- fixture cases for .tools/seat-list.py (NFRA_CTLPLN cell CT-s-7).

Every case builds its own fixture tree in a temporary directory and removes the files it made, by name. Nothing here reads
or writes the live fabric. LAST line:  SEAT-LIST-TEST cases=<k>/<n> ok=<True|False>
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import os
import re
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
NOW = 1_800_000_000
COO_C, COO_D, COO_E, COO_F, COO_G = ("2.0.0_SA_COO~%s" % x for x in "CDEFG")
BASE_COO = "2.0.0_SA_COO"

ARMS = """# LIVE ARMS

## Holds

- `2.0.0_SA_COO~D` `/closer-drive` is named here under Holds and must not be read.

## Arms

- `2.0.0_SA_COO~C` `/canonical-drive PROJ_AAA` DIRECTED.
- `2.0.0_SA_COO~G` `/remote-drive` for the one-off request.
- Paired: `2.0.0_SA_COO~E` / `~F` running `/canonical-drive <own project> 30m`.

## Struck

- `2.0.0_SA_COO~D` `/canonical-drive PROJ_AAA` struck.
"""


def load_tool():
    spec = importlib.util.spec_from_file_location("seat_list_tool", os.path.join(ROOT, ".tools", "seat-list.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


TOOL = load_tool()


class Fixture:
    def __init__(self):
        self.base = tempfile.mkdtemp(prefix="seatlist_")
        self.files, self.dirs = [], [self.base]

    def write(self, rel: str, text: str) -> str:
        path = os.path.join(self.base, rel)
        d, chain = os.path.dirname(path), []
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

    def cleanup(self):
        """Remove every file under this fixture's own temporary directory by name, then its directories."""
        for top, dirs, files in os.walk(self.base, topdown=False):
            for name in files:
                os.remove(os.path.join(top, name))
            for name in dirs:
                os.rmdir(os.path.join(top, name))
        os.rmdir(self.base)


def seat(summary, age=5):
    return {"pid": 1, "summary": summary, "base_serial": "x", "last_seen_epoch": NOW - age,
            "last_seen": "x", "registered_at": "x"}


def order(issued_by, status):
    return "# TO\n<issued_by>%s</issued_by>\n<status>%s</status>\n" % (issued_by, status)


def lease(code, mode, seat_serial, expires):
    return json.dumps({"code": code, "mode": mode, "seat": seat_serial, "surface": ["x"], "armed_by": "t",
                       "armed_at": "x", "expires_at": "2027-01-01T00:00:00Z", "expires_epoch": expires})


def base_fixture(fx, liveness, arms=ARMS, gitlog="", leases=(), orders=()):
    fx.write("now", str(NOW))
    fx.write("org/mcp/liveness.json", json.dumps(liveness))
    fx.write("org/ref/LIVE_ARMS.md", arms)
    fx.write("gitlog.txt", gitlog)
    fx.write("org/missions/D0/NFRA/PROJ_AAA/project.json", '{"project_code": "PROJ_AAA"}')
    fx.write("org/missions/D0/NFRA/PROJ_BBB/project.json", '{"project_code": "PROJ_BBB"}')
    for name, mode, who, exp in leases:
        fx.write("org/mcp/drive_mode/%s.json" % name, lease(name, mode, who, exp))
    for i, (who, status) in enumerate(orders):
        fx.write("org/missions/D0/NFRA/PROJ_AAA/task-orders/o%d.md" % i, order(who, status))


def run(argv, device="laptop"):
    """(rc, stdout, stderr) of one in-process main() call with AGENTBUS_DEVICE set."""
    old = os.environ.get("AGENTBUS_DEVICE")
    os.environ["AGENTBUS_DEVICE"] = device
    out, err = io.StringIO(), io.StringIO()
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = TOOL.main(argv)
    finally:
        if old is None:
            os.environ.pop("AGENTBUS_DEVICE", None)
        else:
            os.environ["AGENTBUS_DEVICE"] = old
    return rc, out.getvalue(), err.getvalue()


def rows_of(fx, device="laptop"):
    doc = json.load(open(os.path.join(fx.base, "org", "devices", "state", device, "seats.json"), encoding="utf-8"))
    return doc, {r["serial"]: r for r in doc["rows"]}


def main() -> int:
    cases = []

    def case(label, ok):
        cases.append((label, bool(ok)))

    fx = Fixture()
    try:
        # ---- a box with a COO on each drive, a NOTHING COO, a STALE seat, a bad project, a NEVER, base + lane
        liveness = {
            COO_C: seat("WORKING: PROJ_AAA round 1"),                      # canonical-drive from LIVE_ARMS, no order, commit old
            COO_D: seat("WORKING: PROJ_BBB round 2"),                      # closer-drive from a live FAST lease
            COO_G: seat("IDLE: one-off request desk PROJ_AAA"),            # remote-drive from LIVE_ARMS
            COO_E: seat("WORKING: NOTA_PROJX round 3"),                 # arms via shorthand; code is no project
            COO_F: seat("IDLE: nothing named here"),                    # shorthand canonical-drive; no project named
            BASE_COO: seat("IDLE: the base seat", age=2000),            # STALE, no drive, no order, no commit
            "2.0.0_SA_COO~H": seat("IDLE: PROJ_BBB"),                      # NOTHING: no drive, no order, no commit
            "2.0.0_SA_COO~J": seat("IDLE: PROJ_AAA"),                      # holds only a HOLD lease: not a drive
            "2.0.0_SA_COO~K": seat("IDLE: PROJ_AAA"),                      # holds only a lapsed FAST lease: not a drive
            "1.0.0_SA_CTO": seat("WORKING: self-drive"),
            "9.9.9_ZZ_ODD": seat("UNKNOWN KIND SEAT"),
        }
        gitlog = "\n".join([
            "%d\t%s" % (NOW - 30 * 60, COO_C),                           # 30 minutes ago: inside the window
            "%d\t%s" % (NOW - 5 * 3600, COO_D),                          # 300 minutes ago
            "%d\t%s" % (NOW - 10, "1.0.0_SA_CTO"),
            "%d\t%s" % (NOW - 60, "x" + COO_G),                          # a different author containing the serial: not anchored
        ]) + "\n"
        leases = [("PROJ_BBB", "FAST", COO_D, NOW + 3600),
                  ("PROJ_AAA", "HOLD", "2.0.0_SA_COO~J", NOW + 3600),      # a HOLD is not a drive
                  ("PROJ_XXX", "FAST", "2.0.0_SA_COO~K", NOW - 7200)]      # lapsed: not a drive
        orders = [(COO_C, "complete"), (COO_C, "issued"), (COO_C, "pending"), (COO_E, "issued"), (COO_E, "superseded"),
                  (BASE_COO, "complete"), (COO_F, "issued")]
        base_fixture(fx, liveness, gitlog=gitlog, leases=leases, orders=orders)
        rc, out, err = run(["write", "--from-fixture", fx.base])
        doc, rows = rows_of(fx)
        last = out.strip().splitlines()[-1]

        case("a COO armed in LIVE_ARMS reads canonical-drive, cited to the file and line",
             rows[COO_C]["drive"] == "canonical-drive" and "org/ref/LIVE_ARMS.md line " in rows[COO_C]["drive_cite"])
        case("a COO with a live FAST lease in its own name reads closer-drive, cited to the marker",
             rows[COO_D]["drive"] == "closer-drive" and "org/mcp/drive_mode/PROJ_BBB.json" in rows[COO_D]["drive_cite"])
        case("a COO named for /remote-drive in LIVE_ARMS reads remote-drive",
             rows[COO_G]["drive"] == "remote-drive")
        case("a HOLD lease and a lapsed FAST lease are not a drive",
             rows["2.0.0_SA_COO~J"]["drive"] == "NONE" and rows["2.0.0_SA_COO~K"]["drive"] == "NONE"
             and rows["2.0.0_SA_COO~J"]["doing"] == "NOTHING" and rows["2.0.0_SA_COO~K"]["doing"] == "NOTHING")
        case("the Holds and Struck sections of LIVE_ARMS arm nothing",
             TOOL.arms_drive(TOOL.Ctx(fx.base), "2.0.0_SA_COO~Q")[0] == "NONE"
             and TOOL.arms_drive(TOOL.Ctx(fx.base), COO_D)[0] == "NONE")
        case("a shorthand lane in a shared LIVE_ARMS row (`~F`) reads the row's drive",
             rows[COO_F]["drive"] == "canonical-drive")
        case("a COO with no drive, no open order and no commit is NOTHING",
             rows["2.0.0_SA_COO~H"]["doing"] == "NOTHING" and rows["2.0.0_SA_COO~H"]["drive"] == "NONE"
             and rows["2.0.0_SA_COO~H"]["open_orders"] == 0)
        case("a COO with a commit inside the window is WORKING, one with only a drive is IDLE, one with an order is WORKING",
             rows[COO_C]["doing"] == "WORKING" and rows[COO_G]["doing"] == "IDLE" and rows[COO_E]["doing"] == "WORKING")
        case("the seat's own summary is shown and never decides doing (an IDLE-worded summary with an order reads WORKING)",
             rows[COO_F]["summary"].startswith("IDLE") and rows[COO_F]["doing"] == "WORKING")
        case("a seat registered but STALE is listed as STALE, not dropped",
             rows[BASE_COO]["liveness"] == "STALE" and BASE_COO in rows and len(rows) == len(liveness))
        case("a summary naming a code that is no project row prints UNRESOLVED; one naming none does too",
             rows[COO_E]["project"] == "UNRESOLVED" and rows[COO_F]["project"] == "UNRESOLVED"
             and rows[COO_C]["project"] == "PROJ_AAA" and rows[COO_D]["project"] == "PROJ_BBB")
        case("a serial with no commit at all reads NEVER; a commit reads minutes; a longer-named author is not matched",
             rows[COO_G]["last_commit_minutes"] == "NEVER" and rows[COO_C]["last_commit_minutes"] == 30
             and rows[COO_D]["last_commit_minutes"] == 300)
        case("a base serial and its lane are two seats, each with its own order count",
             BASE_COO in rows and COO_C in rows and rows[BASE_COO]["open_orders"] == 0 and rows[COO_C]["open_orders"] == 2)
        case("open orders count only non-terminal orders issued by exactly that serial, read from the order files",
             rows[COO_E]["open_orders"] == 1 and rows[COO_F]["open_orders"] == 1)
        case("a serial no kind matches reads UNKNOWN and still gets exactly one doing",
             rows["9.9.9_ZZ_ODD"]["kind"] == "UNKNOWN" and rows["9.9.9_ZZ_ODD"]["doing"] in TOOL.DOING)
        case("a box with no CVO live reads reviewer=ABSENT, and the line has the named shape",
             "reviewer=ABSENT" in last and bool(re.match(
                 r"^SEAT-LIST device=\S+ seats=\d+ coo=\d+ working=\d+ idle=\d+ nothing=\d+ reviewer=(present|ABSENT) "
                 r"ok=(True|False)$", last)))
        case("the counts add up: coo= counts COO kinds and working+idle+nothing equals seats",
             "seats=11 coo=9 " in last and last.endswith("ok=True") and rc == 0)
        case("the file carries the sibling convention: schema, device, written_at, written_by, rows",
             set(doc) == TOOL.TOP_KEYS and doc["device"] == "laptop" and doc["written_at"] == TOOL.stamp(NOW))

        # ---- a CVO live: reviewer present
        fx2 = Fixture()
        try:
            base_fixture(fx2, {"3.0.0_SA_CVO": seat("IDLE: available"), COO_C: seat("WORKING: PROJ_AAA")}, arms="")
            _, out2, _ = run(["write", "--from-fixture", fx2.base])
            case("a live CVO-kind seat reads reviewer=present; a COO with nothing armed is NOTHING",
                 "reviewer=present" in out2.splitlines()[-1] and "nothing=1" in out2.splitlines()[-1])
        finally:
            fx2.cleanup()

        # ---- one box refusing to write another's file
        before = sorted(os.listdir(os.path.join(fx.base, "org", "devices", "state")))
        rc3, _, err3 = run(["write", "--device", "dell1", "--from-fixture", fx.base])
        after = sorted(os.listdir(os.path.join(fx.base, "org", "devices", "state")))
        case("a box refuses to write another box's file (rc 1, REFUSED, nothing created)",
             rc3 == 1 and "REFUSED" in err3 and before == after == ["laptop"])
        rc4, _, err4 = run(["write", "--from-fixture", fx.base], device="no-such-box")
        case("a box the register does not hold is an unresolved box (rc 2), never guessed", rc4 == 2 and "unresolved" in err4)

        # ---- show --all with one absent and one stale
        okfile = json.load(open(os.path.join(fx.base, "org", "devices", "state", "laptop", "seats.json"), encoding="utf-8"))
        stale = dict(okfile, device="dell1", written_at=TOOL.stamp(NOW - 200 * 60))
        fresh = dict(okfile, device="sitez", written_at=TOOL.stamp(NOW - 5 * 60))
        fx.write("org/devices/state/dell1/seats.json", json.dumps(stale))
        fx.write("org/devices/state/sitez/seats.json", json.dumps(fresh))
        rc5, out5, _ = run(["show", "--all", "--from-fixture", fx.base])
        last5 = out5.strip().splitlines()[-1]
        case("show --all names the box whose file is ABSENT (dell2) and the box whose file is older than 90 minutes (dell1)",
             "ABSENT dell2" in out5 and "absent=dell2" in last5 and "stale=dell1" in last5 and rc5 == 0)
        case("show prints each file's age in minutes beside what it reads",
             "age 200 min" in out5 and "age 5 min" in out5 and "age 0 min" in out5)
        case("show names a seat doing nothing and a box with no reviewer", "DOING NOTHING:" in out5 and "2.0.0_SA_COO~H" in out5.split("DOING NOTHING:")[1].splitlines()[0]
             and "no reviewer (CVO) live on laptop" in out5)
        rc5b, out5b, _ = run(["show", "--device", "dell1", "--stale-minutes", "300", "--from-fixture", fx.base])
        case("--stale-minutes moves the line (200 minutes old reads fresh at 300)", "stale=none" in out5b and rc5b == 0)

        # ---- an unknown key is refused (top level, row, and a file written for a different box)
        bad_top = dict(okfile, device="dell1", extra_key=1)
        fx.write("org/devices/state/dell1/seats.json", json.dumps(bad_top))
        rc6, out6, _ = run(["show", "--device", "dell1", "--from-fixture", fx.base])
        case("an unknown top-level key is refused (rc 3, REFUSED, named)",
             rc6 == 3 and "REFUSED" in out6 and "extra_key" in out6 and "refused=dell1" in out6)
        bad_row = json.loads(json.dumps(okfile))
        bad_row["device"] = "dell1"
        bad_row["rows"][0]["surprise"] = "x"
        fx.write("org/devices/state/dell1/seats.json", json.dumps(bad_row))
        rc7, out7, _ = run(["show", "--device", "dell1", "--from-fixture", fx.base])
        case("an unknown row key is refused", rc7 == 3 and "unknown key" in out7 and "surprise" in out7)
        wrong = dict(okfile, device="sitez")
        fx.write("org/devices/state/dell1/seats.json", json.dumps(wrong))
        rc8, out8, _ = run(["show", "--device", "dell1", "--from-fixture", fx.base])
        case("a file whose device is not the box it sits under is refused (one file per box)",
             rc8 == 3 and "one file per box" in out8)

        # ---- an unreadable liveness file is a refusal, not an empty box
        fx3 = Fixture()
        try:
            fx3.write("now", str(NOW))
            rc9, _, err9 = run(["write", "--from-fixture", fx3.base])
            case("a missing liveness file refuses (rc 3); it is not written as an empty box",
                 rc9 == 3 and "REFUSED" in err9 and not os.path.exists(os.path.join(fx3.base, "org", "devices", "state")))
        finally:
            fx3.cleanup()
    finally:
        fx.cleanup()

    fails = 0
    for label, ok in cases:
        print("  %s  %s" % ("PASS" if ok else "FAIL", label))
        fails += 0 if ok else 1
    print("SEAT-LIST-TEST cases=%d/%d ok=%s" % (len(cases) - fails, len(cases), fails == 0))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
