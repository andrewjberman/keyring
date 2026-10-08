#!/usr/bin/env python3
"""test_manager_on_every_box.py -- NFRA_CTLPLN workstream SEATS, cell CT-s-4 (the fabric manager on every box).

Runs on fixtures in temporary directories. It reads the live fabric nowhere, sends nothing and writes only inside its own
temporary directory (removed at the end).

    python .tools/tests/test_manager_on_every_box.py

LAST line: MANAGER-TEST cases=<k>/<n> ok=<True|False>
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
LIVENESS = os.path.join(ROOT, ".tools", "seat-liveness.py")
RECORD = os.path.join(ROOT, ".tools", "mstr-record-check.py")
SKILLS = os.path.join(ROOT, ".claude", "skills")
NOW = 1_800_000_000
MIN = 60

RESULTS = []


def case(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append(bool(ok))
    print("%s %s%s" % ("PASS" if ok else "FAIL", name, "" if ok else " -- " + str(detail)[:600]))


def write(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def order(root: str, name: str, issued_to: str, status: str) -> None:
    write(os.path.join(root, "org", "missions", "D0", "TST", "TST_ONE", "task-orders", name + ".md"),
          "# TO %s\n<issued_to>%s</issued_to>\n<issued_date>2026-10-07</issued_date>\n<status>%s</status>\n" % (
              name, issued_to, status))


def cmdline(serial: str) -> str:
    return '"C:\\bin\\claude.exe" --flag -- "%s\n\nFIRST: startup text mentioning other serials like 2.0.0_SA_COO~T1"' % serial


def register(base: str) -> str:
    path = os.path.join(base, "register.json")
    write(path, json.dumps({"schema_version": 1, "devices": [
        {"name": "alpha", "aliases": [], "inbound_queue": "q-alpha.fifo", "lane_letters": [], "lane_letters_default": True},
        {"name": "beta", "aliases": [], "inbound_queue": "q-beta.fifo", "lane_letters": ["Q"], "lane_letters_default": False},
    ]}))
    return path


def fixture(base: str, with_processes: bool = True) -> str:
    fx = os.path.join(base, "fx")
    os.makedirs(fx)
    write(os.path.join(fx, "now"), str(NOW))
    stale, fresh = NOW - 3600, NOW - 120
    seats = {
        "2.0.0_SA_COO~T1": stale,      # MOVING: process, commit 10 min ago
        "2.0.0_SA_COO~T2": stale,      # QUIET: process, commit 120 min ago, no open order (one terminal order does not count)
        "2.0.0_SA_COO~T3": stale,      # HUNG: process, commit 120 min ago, an open order
        "2.0.0_SA_COO~T4": stale,      # DEAD: registered, no process, stale heartbeat
        "2.0.0_SA_COO~T5": stale,      # UNKNOWN: process, the author filter matches nothing at all
        "2.0.0_SA_COO": stale,         # the BASE serial: its own commit is old; only its lanes are recent
        "2.0.0_SA_COO~T6": stale,      # a lane whose only look-alike process is the BASE serial: DEAD
        "1.0.0_SA_CTO": stale,         # MOVING by a deliverable written 5 minutes ago, though its commits are old
        "3.0.0_SA_CVO": fresh,         # no process but a heartbeat 2 minutes old: process-blind, UNKNOWN
    }
    write(os.path.join(fx, "org", "mcp", "liveness.json"),
          json.dumps({s: {"pid": "1", "summary": "x", "last_seen_epoch": ep} for s, ep in seats.items()}))
    procs = ["2.0.0_SA_COO~T1", "2.0.0_SA_COO~T2", "2.0.0_SA_COO~T3", "2.0.0_SA_COO~T5", "2.0.0_SA_COO", "1.0.0_SA_CTO"]
    if with_processes:
        write(os.path.join(fx, "processes.json"), json.dumps([cmdline(s) for s in procs]))
    write(os.path.join(fx, "gitlog.txt"), "\n".join([
        "%d\t2.0.0_SA_COO~T1" % (NOW - 10 * MIN),
        "%d\t2.0.0_SA_COO~T2" % (NOW - 120 * MIN),
        "%d\t2.0.0_SA_COO~T3" % (NOW - 120 * MIN),
        "%d\t2.0.0_SA_COO" % (NOW - 300 * MIN),
        "%d\t1.0.0_SA_CTO" % (NOW - 200 * MIN),
        "%d\t2.0.0_SA_COO~T4" % (NOW - 500 * MIN),
        "%d\t2.0.0_SA_COO~T6" % (NOW - 500 * MIN),
    ]) + "\n")
    write(os.path.join(fx, "deliverables.txt"), "1.0.0_SA_CTO\t%d\n" % (NOW - 5 * MIN))
    order(fx, "TST_ONE.TO-1", "2.0.0_SA_COO~T3", "issued")
    order(fx, "TST_ONE.TO-2", "2.0.0_SA_COO~T2", "complete")
    order(fx, "TST_ONE.TO-3", "0.9.0_WK_TST~1", "issued")          # a worker: a subagent with no process, never a seat
    order(fx, "TST_ONE.TO-4", "2.0.0_SA_COO~T7", "issued")          # order-only seat, lane owned here: DEAD
    order(fx, "TST_ONE.TO-5", "2.0.0_SA_COO~Q", "issued")           # lane Q belongs to the other box: not a seat here
    return fx


def run_liveness(fx: str, reg: str, extra=()) -> tuple:
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env["OPAL_DEVICE_REGISTER"] = reg
    env["AGENTBUS_DEVICE"] = "alpha"
    res = subprocess.run([sys.executable, LIVENESS, "--from-fixture", fx] + list(extra), capture_output=True, text=True,
                         env=env, timeout=100)
    return res.returncode, res.stdout, res.stderr


def klass_of(out: str, serial: str):
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 3 and parts[0] == serial:
            return parts[2]
    return None


def test_liveness(base: str) -> None:
    reg = register(base)
    fx = fixture(base)
    rc, out, err = run_liveness(fx, reg)
    want = {
        "2.0.0_SA_COO~T1": "MOVING", "2.0.0_SA_COO~T2": "QUIET", "2.0.0_SA_COO~T3": "HUNG", "2.0.0_SA_COO~T4": "DEAD",
        "2.0.0_SA_COO~T5": "UNKNOWN", "2.0.0_SA_COO": "QUIET", "2.0.0_SA_COO~T6": "DEAD", "1.0.0_SA_CTO": "MOVING",
        "3.0.0_SA_CVO": "UNKNOWN", "2.0.0_SA_COO~T7": "DEAD",
    }
    detail = "rc=%d\n%s\n%s" % (rc, out, err)
    case("MOVING: a process and a commit inside the window", klass_of(out, "2.0.0_SA_COO~T1") == want["2.0.0_SA_COO~T1"], detail)
    case("QUIET: alive, nothing in the window, no open order (a terminal order does not make it hung)",
         klass_of(out, "2.0.0_SA_COO~T2") == "QUIET", detail)
    case("HUNG: alive, an open order, nothing in the window", klass_of(out, "2.0.0_SA_COO~T3") == "HUNG", detail)
    case("DEAD: registered, no process, a stale heartbeat", klass_of(out, "2.0.0_SA_COO~T4") == "DEAD", detail)
    case("UNKNOWN: a serial that never committed is not QUIET", klass_of(out, "2.0.0_SA_COO~T5") == "UNKNOWN", detail)
    case("MOVING by a deliverable written in a live worktree, commits old", klass_of(out, "1.0.0_SA_CTO") == "MOVING", detail)
    case("a base serial does not match its own lanes' commits (QUIET, not MOVING)",
         klass_of(out, "2.0.0_SA_COO") == "QUIET", detail)
    case("a lane does not match the base serial's process (DEAD)", klass_of(out, "2.0.0_SA_COO~T6") == "DEAD", detail)
    case("a fresh heartbeat with no process token is process-blind: UNKNOWN, never DEAD",
         klass_of(out, "3.0.0_SA_CVO") == "UNKNOWN", detail)
    case("an open order to a seat that never ran reads DEAD", klass_of(out, "2.0.0_SA_COO~T7") == "DEAD", detail)
    case("a worker is never a seat and a lane another box owns is not listed",
         klass_of(out, "0.9.0_WK_TST~1") is None and klass_of(out, "2.0.0_SA_COO~Q") is None, detail)
    last = out.strip().splitlines()[-1] if out.strip() else ""
    case("the last line carries the counts, 10 seats: 2 moving 2 quiet 1 hung 3 dead 2 unknown, ok=True",
         last == "SEAT-LIVENESS device=alpha seats=10 moving=2 quiet=2 hung=1 dead=3 unknown=2 ok=True" and rc == 0,
         "%s rc=%d" % (last, rc))
    wide = run_liveness(fx, reg, ["--minutes", "1000"])[1]
    case("the window is a flag: at 1000 minutes the quiet and hung seats read MOVING",
         klass_of(wide, "2.0.0_SA_COO~T3") == "MOVING" and klass_of(wide, "2.0.0_SA_COO~T2") == "MOVING", wide)
    # a failed process read must never be turned into a verdict of dead seats
    os.makedirs(os.path.join(base, "noproc"))
    fx2 = fixture(os.path.join(base, "noproc"), with_processes=False)
    rc2, out2, _ = run_liveness(fx2, reg)
    last2 = out2.strip().splitlines()[-1] if out2.strip() else ""
    case("an unreadable process list: every seat UNKNOWN, none DEAD, ok=False and rc 1",
         rc2 == 1 and last2.endswith("ok=False") and " dead=0 " in last2 and "WARN" in out2, "rc=%d %s" % (rc2, out2))
    gone = os.path.join(base, "empty")
    os.makedirs(gone)
    write(os.path.join(gone, "now"), str(NOW))
    rc3, out3, err3 = run_liveness(gone, reg)
    case("an unreadable liveness file stops the tool: ok=False, rc 3, never an empty box",
         rc3 == 3 and out3.strip().endswith("seats=0 moving=0 quiet=0 hung=0 dead=0 unknown=0 ok=False"),
         "rc=%d %s %s" % (rc3, out3, err3))


# ---------------------------------------------------------------- the skill text

def prose_lines(path: str) -> list:
    """Lines that are not inside a fenced block and not a blockquote: a quoted example may name a box, the prose may not."""
    out, fenced = [], False
    for line in open(path, encoding="utf-8").read().splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced or line.lstrip().startswith(">"):
            continue
        out.append(line)
    return out


def device_words() -> list:
    reg = json.load(open(os.path.join(ROOT, "org", "devices", "DEVICES.json"), encoding="utf-8"))
    words = set()
    for entry in reg["devices"]:
        for word in [entry["name"]] + list(entry.get("aliases", [])):
            if len(word) >= 4:      # a one-letter alias ("Z") is a lane letter everywhere in the text
                words.add(word)
    return sorted(words)


OLD_TWO_BOX = ("laptop-placed", "sitez-placed", "BOTH fabrics", "both fabrics", "either machine", "laptop|sitez", "both devices",
               "the two of you")


def test_skills() -> None:
    words = device_words()
    for name in ("govern", "mstr-review", "agentbus"):
        path = os.path.join(SKILLS, name, "SKILL.md")
        lines = prose_lines(path)
        hits = [(n + 1, w) for n, line in enumerate(lines) for w in words if re.search(re.escape(w), line, re.I)]
        phrases = [(p, line[:80]) for line in lines for p in OLD_TWO_BOX if p in line]
        case("/%s names no register device outside a quoted example (%s)" % (name, ", ".join(words)), not hits,
             "%s %s" % (hits[:4], [lines[n - 1][:100] for n, _ in hits[:2]]))
        case("/%s carries none of the old two-box phrases" % name, not phrases, phrases[:4])
    govern = open(os.path.join(SKILLS, "govern", "SKILL.md"), encoding="utf-8").read()
    case("/govern Step 0 admits a manager serial with a lane", re.search(r"0\.0\.0_AB_MSTR~<lane>", govern.split("## Step 1")[0])
         is not None)
    step_3a = govern.split("## Step 3a")[1].split("## Step 3b")[0] if "## Step 3a" in govern else ""
    case("/govern has a seat-liveness step that runs the tool, /unstick for HUNG and /mstr-spawn for DEAD",
         ".tools/seat-liveness.py" in step_3a and "/unstick" in step_3a and "/mstr-spawn" in step_3a and "HUNG" in step_3a
         and "DEAD" in step_3a, step_3a[:200])
    step_3b = govern.split("## Step 3b")[1].split("## Step 4")[0] if "## Step 3b" in govern else ""
    case("/govern Step 3b reads the other boxes from the register's `devices` subcommand",
         "agentbus-sqs.sh devices" in step_3b and "EACH other box" in step_3b, step_3b[:200])
    review = open(os.path.join(SKILLS, "mstr-review", "SKILL.md"), encoding="utf-8").read()
    fixed = [s for s in ("1.0.0_SA_CTO", "2.0.0_SA_COO", "3.0.0_SA_CVO", "1.1.0_SA_CTO", "2.1.0_SA_COO", "3.1.0_SA_CVO")
             if s in review.split("**Tier-1 liveness check")[1].split("- **Spawn-mechanism")[0]]
    case("/mstr-review reads the Tier-1 kinds from SEAT_ROLES.json, with no fixed serial list, and a box with no reviewer is a "
         "finding", not fixed and "org/ref/SEAT_ROLES.json" in review and "no reviewer seat" in review, fixed)
    for name in ("mstr-spawn", "mstr-kill", "unstick"):
        text = open(os.path.join(SKILLS, name, "SKILL.md"), encoding="utf-8").read()
        case("/%s says it acts on THIS box only and points at the register" % name,
             "acts on THIS box only" in text and "org/devices/DEVICES.json" in text)
    script = open(os.path.join(ROOT, ".tools", "agentbus-sqs.sh"), encoding="utf-8").read()
    usage = [line for line in script.splitlines() if "usage:" in line]
    case("the bus script's usage lines name no box", usage and not any("laptop" in u or "sitez" in u for u in usage), usage)
    comments = [line for line in script.splitlines()[:50] if line.startswith("#   <device>") or "watch <this-device>" in line]
    case("the bus script's header usage text describes the register's boxes", len(comments) >= 2, comments)
    sys.path.insert(0, os.path.join(ROOT, ".tools"))
    from git_bash_resolver import git_bash      # never a bare `bash`: that resolves to the WSL stub from python
    bash = git_bash()
    if bash is None:
        case("the bus script still parses (bash -n)", False, "no Git Bash found")
    else:
        check = subprocess.run([bash, "-n", os.path.join(ROOT, ".tools", "agentbus-sqs.sh")], capture_output=True, text=True,
                               timeout=60)
        case("the bus script still parses (bash -n)", check.returncode == 0, check.stderr)


def test_record_selftest() -> None:
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    res = subprocess.run([sys.executable, RECORD, "--selftest"], capture_output=True, text=True, env=env, timeout=110)
    last = res.stdout.strip().splitlines()[-1] if res.stdout.strip() else ""
    case("mstr-record-check.py --selftest passes every case", res.returncode == 0 and last.startswith(
        "MSTR-RECORD-SELFTEST cases=") and last.endswith("ok=True"), "%s %s" % (last, res.stderr[:200]))


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="manager-on-every-box-") as base:
        test_liveness(base)
    test_skills()
    test_record_selftest()
    good = sum(1 for r in RESULTS if r)
    print("MANAGER-TEST cases=%d/%d ok=%s" % (good, len(RESULTS), good == len(RESULTS)))
    return 0 if good == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
