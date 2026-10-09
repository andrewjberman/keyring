#!/usr/bin/env python3
"""seat-liveness.py -- is each seat on THIS box moving, quiet, hung, dead or unknown? (NFRA_CTLPLN workstream SEATS,
cell CT-s-4; contract C-SEATS clause 3).

Andrew's word (2026-10-07): the fabric manager "can manage /unstick /mstr-spawn /mstr-kill to keep their fabric running
cleanly". The manager's loop (/govern) had no step that MEASURES a hung or dead seat. This is that measurement. It READS;
it never unsticks, spawns or kills, sends nothing, and writes nothing. It builds no alert and no monitor: it runs when a seat
runs it. No switch file is needed because nothing here refuses anything.

    python .tools/seat-liveness.py [--minutes N] [--from-fixture <dir>]

THE BOX is AGENTBUS_DEVICE resolved through lib/devices.py (never a path); the live reads are this box's own.

THE SEATS are the union of: the serials in this box's org/mcp/liveness.json (REGISTERED); the serials carried by a running
claude.exe command line (PROCESS TRUTH, read as /mstr-spawn step 1pt reads it: the serial token is EXTRACTED and compared
with equality, never a substring, so a base serial never matches its own lanes); and the serials holding a non-terminal task
order whose kind is not WORKER or UNKNOWN and whose lane this box owns (a worker is a subagent with no process of its own).

THE CLASSES (N minutes from --minutes, default 45):
  MOVING   alive by process, and a commit by that serial's author inside N minutes (git log --all --author "^<serial> <",
           anchored, so a base serial never matches its lanes) or a file written under deliverables/<serial>/ in a live
           worktree inside N minutes.
  QUIET    alive, nothing inside N minutes, no open task order. An order's status is its LAST <status> tag; a STAGED order
           is waiting on its GO and is not open work (it counts toward none of HUNG, DEAD or ELSEWHERE; a seat's reason line
           carries staged=<n>).
  HUNG     alive by process, an open task order assigned to it (<issued_to> equal to the serial), nothing inside N minutes.
  DEAD     a registered session, or an open order whose project is PLACED ON THIS BOX, and no process. EXCEPTION, stated
           in the line: a seat whose broker heartbeat is under 10 minutes old with no process token is process-blind, not
           dead, and reads UNKNOWN (a respawn over a live seat is the worse error).
  ELSEWHERE(<box>)  no process on this box, and EVERY open order's project is placed on another box. The serial string is
           the same on every box and this box cannot see another box's sessions, so a seat working there has no process
           here and is not dead. It is that box's manager's to look at; it is never respawned from here.
  UNKNOWN  the author filter matches nothing at all in the repository's history (a serial that never committed is never
           QUIET); or the process list could not be read (no seat is called dead off a failed read); or no process, none of
           its orders placed here, and at least one order whose project has no readable placement ("placement unread for
           <n> order(s)": an unread placement never licenses a respawn).
PLACEMENT: an order's project is the folder two levels above the order file (.../<CODE>/task-orders/<file>); its project.json
`placement` field is resolved to a box by lib/devices.py resolve() (name or alias, case-insensitive; the same reader
.tools/open-calls.py project_box() uses for that field). A seat with orders both here and elsewhere is decided as before (DEAD
when no process) and its line carries both counts. The lane suffix (~Z) is used only through the register's `lane_letters`
(owned_here below: whether this box lists an order-only seat at all); the register gives no other lane meaning.
BLIND: a hang with no open order reads QUIET; a seat that works without committing or writing a deliverable reads HUNG or
QUIET; a worker subagent is never listed; an open order issued to a seat that never ran reads DEAD, so the manager reads
the order before it respawns.

Fixture directory (--from-fixture): now (epoch), org/mcp/liveness.json, org/missions/D*/*/*/task-orders/*.md (+ the project.json
beside each task-orders folder, for placement),
processes.json (list of command-line strings of the running claude processes), gitlog.txt ("epoch<TAB>author name" lines),
deliverables.txt ("serial<TAB>epoch" lines).

LAST line: SEAT-LIVENESS device=<d> seats=<n> moving=<a> quiet=<b> hung=<c> dead=<e> elsewhere=<f> unknown=<g> ok=<True|False>
Exit: 0 ok=True, 1 ok=False, 2 usage or an unresolved box, 3 an unreadable register or source.
"""
from __future__ import annotations

import argparse
import glob
import importlib.util
import json
import os
import re
import subprocess
import sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)

CLASSES = ("MOVING", "QUIET", "HUNG", "DEAD", "ELSEWHERE", "UNKNOWN")
FRESH_HEARTBEAT_SECONDS = 600
ORDER_DATES = {}
ORDER_PROJECTS = {}
ORDER_STAGED = {}
SERIAL_IN_CMDLINE = re.compile(r'"\s*([0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9]+(?:~[A-Za-z0-9]+)?)')
PS_SCRIPT = (
    "[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding($false); "
    "$all = @(Get-CimInstance Win32_Process); "
    "$cl = @($all | Where-Object { $_.Name -eq 'claude.exe' } | Select-Object ProcessId,CommandLine); "
    "ConvertTo-Json -Compress -Depth 3 -InputObject @{ total = $all.Count; claude = $cl }"
)


class BadSource(Exception):
    pass


def load_mod(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


SL = load_mod("opal_seat_list", ".tools/seat-list.py")


def clean_env() -> dict:
    return {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}


# ---------------------------------------------------------------- the sources

def read_processes(ctx) -> list:
    """[(pid, serial token or None, command line)] for every claude process. Raises BadSource on a failed or implausible read."""
    if ctx.fixture:
        try:
            lines = json.load(open(ctx.path("processes.json"), encoding="utf-8"))
        except (OSError, ValueError) as exc:
            raise BadSource("processes.json unreadable (%s)" % exc)
        return [(1000 + i, tok(line), line) for i, line in enumerate(lines)]
    try:
        res = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command", PS_SCRIPT], capture_output=True,
                             timeout=100)
    except (OSError, subprocess.SubprocessError) as exc:
        raise BadSource("process list unreadable (%s)" % exc)
    text = res.stdout.decode("utf-8-sig", "replace").strip()
    try:
        doc = json.loads(text)
    except ValueError:
        raise BadSource("process list not JSON (rc=%d): %s" % (res.returncode, (text or res.stderr.decode("utf-8", "replace"))[:200]))
    # the positive control: a read that sees no process at all (this query's own host is one) is a failed read, not an empty box
    if not isinstance(doc, dict) or not doc.get("total"):
        raise BadSource("process list read zero processes at all: the read failed, the box is not empty")
    rows = doc.get("claude") or []
    if isinstance(rows, dict):
        rows = [rows]
    return [(r.get("ProcessId"), tok(r.get("CommandLine") or ""), r.get("CommandLine") or "") for r in rows]


def tok(cmdline: str):
    hit = SERIAL_IN_CMDLINE.search(cmdline)
    return hit.group(1) if hit else None


def open_orders_to(ctx) -> dict:
    """{issued_to serial: [order file names]} for open orders, parsed from the order files: an order's status is its LAST
    status tag; a terminal order is skipped and a STAGED order is counted in ORDER_STAGED only. The newest <issued_date>
    per serial goes in ORDER_DATES so a stale order (a seat that never ran it) is visible beside the DEAD verdict."""
    out = {}
    for path in glob.glob(ctx.path("org", "missions", "D*", "*", "*", "task-orders", "*.md")):
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        who = re.search(r"<issued_to>\s*([^<\s]+)\s*</issued_to>", text)
        if not who:
            continue
        word = None
        for st in re.finditer(r"<status>\s*([A-Za-z_-]+)", text):
            if st.group(1).lower() in SL.STATUS_WORDS:
                word = st.group(1).lower()      # an order's status is its LAST status tag (CTO msg 107528): no break
        if word in SL.TERMINAL:
            continue
        if word == "staged":                    # waiting on its GO: not open work, kept visible as staged=<n>
            ORDER_STAGED[who.group(1)] = ORDER_STAGED.get(who.group(1), 0) + 1
            continue
        out.setdefault(who.group(1), []).append(os.path.basename(path))
        ORDER_PROJECTS.setdefault(who.group(1), []).append(os.path.dirname(os.path.dirname(path)))
        when = re.search(r"<issued_date>\s*(\d{4}-\d{2}-\d{2})", text)
        if when and when.group(1) > ORDER_DATES.get(who.group(1), ""):
            ORDER_DATES[who.group(1)] = when.group(1)
    return out


def author_pattern(serial: str) -> str:
    """The anchored author filter: the serial, then ' <' (the start of the e-mail), so a base serial never matches a lane."""
    return "^" + re.escape(serial) + " <"


def last_commit(ctx, serial: str):
    """Epoch of the newest commit by this serial on any branch, or None when the filter matches nothing in all history."""
    if ctx.fixture:
        best = None
        try:
            raw = open(ctx.path("gitlog.txt"), encoding="utf-8").read()
        except OSError:
            raw = ""
        for line in raw.splitlines():
            head, _, name = line.partition("\t")
            if name == serial and head.isdigit() and (best is None or int(head) > best):
                best = int(head)
        return best
    try:
        res = subprocess.run(["git", "-C", ctx.data, "log", "--all", "-1", "--author=" + author_pattern(serial), "--format=%ct"],
                             capture_output=True, text=True, timeout=100, env=clean_env())
    except (OSError, subprocess.SubprocessError) as exc:
        raise BadSource("git log unreadable (%s)" % exc)
    if res.returncode != 0:
        raise BadSource("git log rc=%d: %s" % (res.returncode, res.stderr.strip()[:200]))
    out = res.stdout.strip()
    return int(out) if out.isdigit() else None


def newest_deliverable(ctx, serial: str):
    """Newest mtime of anything directly under deliverables/<serial>/ in any live worktree, or None."""
    if ctx.fixture:
        best = None
        try:
            raw = open(ctx.path("deliverables.txt"), encoding="utf-8").read()
        except OSError:
            raw = ""
        for line in raw.splitlines():
            name, _, ep = line.partition("\t")
            if name == serial and ep.isdigit() and (best is None or int(ep) > best):
                best = int(ep)
        return best
    try:
        res = subprocess.run(["git", "-C", ctx.data, "worktree", "list", "--porcelain"], capture_output=True, text=True,
                             timeout=100, env=clean_env())
    except (OSError, subprocess.SubprocessError) as exc:
        raise BadSource("git worktree list unreadable (%s)" % exc)
    if res.returncode != 0:
        raise BadSource("git worktree list rc=%d: %s" % (res.returncode, res.stderr.strip()[:200]))
    best = None
    for line in res.stdout.splitlines():
        if not line.startswith("worktree "):
            continue
        wt = line[len("worktree "):].strip()
        pats = [os.path.join(glob.escape(wt), "org", "missions", "D*", "*", "*", "deliverables", glob.escape(serial)),
                os.path.join(glob.escape(wt), "org", "tier1_exec", glob.escape(serial), "deliverables")]
        for pat in pats:
            for folder in glob.glob(pat):
                try:
                    stamps = [os.path.getmtime(folder)] + [e.stat().st_mtime for e in os.scandir(folder)]
                except OSError:
                    continue
                top = int(max(stamps))
                if best is None or top > best:
                    best = top
    return best


def placement_of(serial: str, dev, reg: dict, device: str) -> dict:
    """{"here": n, "elsewhere": {box: n}, "unread": n} over the serial's open orders. The project's project.json `placement`
    is resolved by lib/devices.py; a missing file, an unparseable file, an empty field or a value the register does not hold
    counts as unread, never as here and never as elsewhere."""
    out = {"here": 0, "elsewhere": {}, "unread": 0}
    for home in ORDER_PROJECTS.get(serial, []):
        try:
            field = json.load(open(os.path.join(home, "project.json"), encoding="utf-8")).get("placement")
        except (OSError, ValueError, AttributeError):
            field = None
        box = dev.resolve(field, reg) if isinstance(field, str) and field.strip() else None
        if box is None:
            out["unread"] += 1
        elif box == device:
            out["here"] += 1
        else:
            out["elsewhere"][box] = out["elsewhere"].get(box, 0) + 1
    return out


def owned_here(serial: str, reg: dict, device: str) -> bool:
    """Does this box run the serial's lane? A base serial and an unclaimed lane run where the register's default says."""
    lane = serial.partition("~")[2]
    if not lane:
        return True
    mine = None
    for entry in reg["devices"]:
        if entry["name"] == device:
            mine = entry
        elif lane in entry.get("lane_letters", []):
            return False
    if mine is None:
        return False
    return lane in mine.get("lane_letters", []) or bool(mine.get("lane_letters_default"))


# ---------------------------------------------------------------- the classification

def classify(*, alive: bool, registered: bool, hb_age, orders: list, commit_ep, deliv_ep, now: int, minutes: int,
             process_read: bool, newest_order: str = "", placed: dict = None, staged: int = 0) -> tuple:
    """(class, reason). Pure: every input is a measured value. `placed` is placement_of()'s answer for the seat's open orders
    (None: no placement read, which is only ever correct for a seat with no open order). `staged` is the count of the seat's
    staged orders: not open work, named in the reason where the reason names orders."""
    tail = ", staged=%d" % staged if staged else ""
    if not process_read:
        return "UNKNOWN", "process list unreadable: no seat is called dead or hung off a failed read"
    if not alive:
        if registered and hb_age is not None and hb_age <= FRESH_HEARTBEAT_SECONDS:
            return "UNKNOWN", "no process token but a broker heartbeat %dm old: process-blind, not called dead" % (hb_age // 60)
        if not orders:
            return "DEAD", "no process carries this serial; registered session" + tail
        placed = placed or {"here": 0, "elsewhere": {}, "unread": len(orders)}
        away = sum(placed["elsewhere"].values())
        counts = "%d placed here, %d elsewhere, %d unread" % (placed["here"], away, placed["unread"])
        why = "%d open order(s) (%s), newest issued %s: %s%s" % (len(orders), counts, newest_order or "?", ", ".join(orders[:2]),
                                                               tail)
        if placed["here"] == 0 and placed["unread"] > 0:
            return "UNKNOWN", ("placement unread for %d order(s), %d placed elsewhere: never called dead off an unread placement; %s"
                               % (placed["unread"], away, why))
        if placed["here"] == 0:
            boxes = ",".join(sorted(placed["elsewhere"]))
            return "ELSEWHERE(%s)" % boxes, ("no process on this box and every open order is placed on another box, so this "
                                             "box cannot see it: that box's manager's to look at; %s" % why)
        return "DEAD", "no process carries this serial; %s" % why
    recent = max(commit_ep or 0, deliv_ep or 0)
    age_min = (now - recent) // 60 if recent else None
    if recent and age_min <= minutes:
        return "MOVING", "%s %dm ago" % ("commit" if (commit_ep or 0) >= (deliv_ep or 0) else "deliverable", max(0, age_min))
    if commit_ep is None:
        return "UNKNOWN", "the author filter matches nothing in the repository's history: a serial that never committed is not quiet"
    if orders:
        return "HUNG", "open order(s) %s and nothing for %dm%s" % (", ".join(orders[:2]), age_min, tail)
    return "QUIET", "alive, nothing for %dm, no open order%s" % (age_min, tail)


def build(ctx, device: str, reg: dict, minutes: int, dev) -> tuple:
    """(rows, notes). Raises BadSource when the liveness file or the git read fails."""
    now = ctx.now()
    try:
        live = SL.read_liveness(ctx)
    except SL.BadFile as exc:
        raise BadSource(str(exc))
    notes = []
    process_read = True
    try:
        procs = read_processes(ctx)
    except BadSource as exc:
        process_read = False
        procs = []
        notes.append("WARN: %s" % exc)
    proc_by_serial = {}
    for pid, serial, _ in procs:
        if serial:
            proc_by_serial.setdefault(serial, []).append(pid)
    orders = open_orders_to(ctx)
    kind_of = SL.kind_resolver()
    seats = set(live) | set(proc_by_serial)
    for serial in orders:
        if serial not in seats and kind_of(serial) not in ("WORKER", "UNKNOWN") and owned_here(serial, reg, device):
            seats.add(serial)
    rows = []
    for serial in sorted(seats):
        info = live.get(serial) if isinstance(live.get(serial), dict) else None
        seen = info.get("last_seen_epoch") if info else None
        try:
            hb_age = max(0, now - int(float(seen))) if seen is not None else None
        except (TypeError, ValueError):
            hb_age = None
        commit_ep = last_commit(ctx, serial)
        deliv_ep = newest_deliverable(ctx, serial)
        klass, why = classify(alive=serial in proc_by_serial, registered=info is not None, hb_age=hb_age,
                              orders=orders.get(serial, []), commit_ep=commit_ep, deliv_ep=deliv_ep, now=now,
                              minutes=minutes, process_read=process_read, newest_order=ORDER_DATES.get(serial, ""),
                              staged=ORDER_STAGED.get(serial, 0),
                              placed=placement_of(serial, dev, reg, device) if serial in orders else None)
        rows.append({"serial": serial, "kind": kind_of(serial), "class": klass.split("(")[0], "label": klass, "reason": why,
                     "pids": proc_by_serial.get(serial, []), "orders": len(orders.get(serial, []))})
    return rows, notes, process_read


def final_line(device: str, rows: list, ok: bool) -> str:
    count = {c: sum(1 for r in rows if r["class"] == c) for c in CLASSES}
    return ("SEAT-LIVENESS device=%s seats=%d moving=%d quiet=%d hung=%d dead=%d elsewhere=%d unknown=%d ok=%s" % (
        device, len(rows), count["MOVING"], count["QUIET"], count["HUNG"], count["DEAD"], count["ELSEWHERE"], count["UNKNOWN"], ok))


def main(argv: list) -> int:
    ap = argparse.ArgumentParser(prog="seat-liveness.py", description=__doc__.split("\n")[0])
    ap.add_argument("--minutes", type=int, default=45, help="quiet window in minutes (default 45)")
    ap.add_argument("--from-fixture", help="tests: read every source from this directory instead of the live fabric")
    args = ap.parse_args(argv)
    if args.minutes < 1:
        print("ERROR: --minutes must be at least 1", file=sys.stderr)
        return 2
    dev = load_mod("opal_devices", "lib/devices.py")
    try:
        reg = dev.load()
    except dev.RegisterError as exc:
        print(str(exc), file=sys.stderr)
        return 3
    device, basis = dev.this_device(reg)
    if device is None:
        print("ERROR: this box is unresolved: %s" % basis, file=sys.stderr)
        return 2
    ctx = SL.Ctx(args.from_fixture)
    try:
        rows, notes, process_read = build(ctx, device, reg, args.minutes, dev)
    except BadSource as exc:
        print("ERROR: %s" % exc, file=sys.stderr)
        print(final_line(device, [], False))
        return 3
    print("SEAT-LIVENESS read | box %s (%s) | window %d min | sources: %s" % (
        device, basis, args.minutes, "fixture " + ctx.fixture if ctx.fixture else ctx.data))
    for note in notes:
        print(note)
    for row in rows:
        print("  %-26s %-8s %-8s pid=%-8s orders=%-3d %s" % (
            row["serial"], row["kind"], row["label"], ",".join(str(p) for p in row["pids"]) or "none", row["orders"],
            row["reason"]))
    ok = process_read and sum(1 for r in rows if r["class"] in CLASSES) == len(rows)
    line = final_line(device, rows, ok)
    print(line)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
