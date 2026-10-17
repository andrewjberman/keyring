#!/usr/bin/env python3
"""seat-list.py -- what each seat on a box is doing, published per box, and the laptop's view of every box with each
report's age (NFRA_CTLPLN workstream SEATS, cell CT-s-7; contract C-SEATS).

Andrew's word (2026-10-07): "COOs are the workers, they either run /canonical-drive /closer-drive to proceed projects,
running /remote-drive if a one-off request comes in", and "the laptop needs to know at all times what is going on across
the various devices". This is a READ made on demand. It writes ONE file (this box's seats.json) and nothing else. It builds
no alert, no notification and no monitor: nothing here runs unless a seat runs it.

    python .tools/seat-list.py write [--device <d>] [--window-minutes N]
    python .tools/seat-list.py show  [--device <d> | --all] [--stale-minutes N]
    (either command) --from-fixture <dir>      tests: read every source from <dir> instead of the live fabric

THE FILE is org/devices/state/<device>/seats.json (ONE WRITER: the box named, resolved from AGENTBUS_DEVICE through
lib/devices.py, never from a path). Shape (schema "seat-list/1"; every reader refuses a key it does not know):
    {"schema", "device", "written_at", "written_by", "rows": [ {serial, kind, liveness (LIVE|STALE), last_seen_minutes,
     summary, project, drive, drive_cite, open_orders, last_commit_minutes, doing} ]}
`project`, `drive` and `open_orders` are COO facts and are null on every other kind.

WHAT IS MEASURED, and from where (this box's tree: the main worktree, found through the git common dir, because the
broker's liveness file and the drive-mode leases are untracked and live only there):
  seats                 org/mcp/liveness.json, one row per registered seat; last_seen older than 600 s is STALE and still listed.
  kind                  lib/seat_roles.py kind_of(serial); a serial no kind matches is UNKNOWN. A base serial and its lane
                        (2.0.0_SA_COO and 2.0.0_SA_COO~C) are two seats.
  project (COO)         a project code in the seat's own summary that names a project row (org/missions/D*/*/<CODE>/project.json);
                        a summary naming none is UNRESOLVED.
  drive (COO)           canonical-drive | closer-drive | remote-drive | NONE. A live FAST lease in org/mcp/drive_mode/ whose seat
                        is this serial reads closer-drive (lapsed leases and HOLD leases are not a drive); else the first of the
                        three drive words in the org/ref/LIVE_ARMS.md "Arms" row that names the serial. That row is an
                        AUTHORISATION, not activity: drive_cite says which file and line gave it.
  open_orders (COO)     non-terminal task orders whose <issued_by> is exactly this serial, parsed from the order files; the
                        broker's base-scoped count is never used.
  last_commit_minutes   minutes since the newest commit whose author name is exactly this serial (any branch); NEVER when none.
  doing                 WORKING | IDLE | NOTHING.
                          COO:    NOTHING when it has no drive, no open order and no commit inside the window; WORKING when it
                                  has a commit inside the window or an open order; IDLE when only a drive is armed.
                          other:  WORKING with a commit inside the window, else IDLE (drive and order are COO notions; a
                                  non-COO seat is never NOTHING).
                        The seat's own summary is shown and never used to decide `doing`.
BLIND: what a seat does between commits; a drive the seat runs that no lease and no LIVE_ARMS row names; a LIVE_ARMS row whose
prose puts the drive word away from the serial; any box whose file has not been landed in this tree.

LAST line (write): SEAT-LIST device=<d> seats=<n> coo=<c> working=<w> idle=<i> nothing=<x> reviewer=<present|ABSENT> ok=<True|False>
LAST line (show):  SEAT-LIST-SHOW boxes=<n> read=<r> absent=<list> stale=<list> refused=<list> seats=<n>
Exit: 0 done, 1 refused or ok=False, 2 usage or an unresolved box, 3 an unreadable register, source or list file.
"""
from __future__ import annotations

import argparse
import datetime
import glob
import importlib.util
import json
import os
import re
import subprocess
import sys
import time

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)

SCHEMA = "seat-list/1"
TOP_KEYS = {"schema", "device", "written_at", "written_by", "rows"}
ROW_KEYS = {"serial", "kind", "liveness", "last_seen_minutes", "summary", "project", "drive", "drive_cite", "open_orders",
            "last_commit_minutes", "doing"}
DOING = ("WORKING", "IDLE", "NOTHING")
DRIVES = ("canonical-drive", "closer-drive", "remote-drive")
STALE_SECONDS = 600          # the fabric-check threshold: last activity older than this is STALE
PRESENCE_GRACE = 30 * 60     # .tools/drive-mode.py: presence extends a lease by this much
SUMMARY_MAX = 240
TERMINAL = {"complete", "superseded", "cancelled", "canceled", "withdrawn", "retired", "closed", "not_met"}
STATUS_WORDS = TERMINAL | {"pending", "staged", "open", "parked", "active", "in_progress", "in-progress",
                           "blocked", "held", "draft", "issued"}
PROJECT_TOKEN = re.compile(r"(?<![A-Za-z0-9_])[A-Z][A-Z0-9]{1,7}_[A-Z][A-Z0-9]{2,11}(?![A-Za-z0-9_])")
DRIVE_TOKEN = re.compile(r"/(canonical|closer|remote)-drive")


class Refused(Exception):
    pass


class BadFile(Exception):
    pass


def load_mod(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main_root() -> str:
    """The main worktree: the liveness file and the leases are untracked, so they live there, not in a linked worktree."""
    try:
        common = subprocess.run(["git", "-C", ROOT, "rev-parse", "--path-format=absolute", "--git-common-dir"],
                                capture_output=True, text=True, check=True).stdout.strip()
        return os.path.dirname(common)
    except Exception:  # noqa: BLE001
        return ROOT


class Ctx:
    """Where every source is read from: the live fabric, or one fixture directory."""

    def __init__(self, fixture):
        self.fixture = os.path.abspath(fixture) if fixture else None
        self.data = self.fixture or main_root()

    def path(self, *parts) -> str:
        return os.path.join(self.data, *parts)

    def now(self) -> int:
        if self.fixture:
            try:
                return int(open(self.path("now"), encoding="utf-8").read().strip())
            except (OSError, ValueError):
                pass
        return int(time.time())

    def state_root(self) -> str:
        env = os.environ.get("OPAL_STATE_ROOT", "").strip()
        if env:
            return env
        if self.fixture:
            return self.path("org", "devices", "state")
        return os.path.join(ROOT, "org", "devices", "state")


def stamp(epoch: int) -> str:
    return datetime.datetime.fromtimestamp(epoch, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def stamp_epoch(text):
    try:
        return int(datetime.datetime.strptime(str(text), "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=datetime.timezone.utc).timestamp())
    except (ValueError, TypeError):
        return None


# ---------------------------------------------------------------- the sources

def read_liveness(ctx: Ctx) -> dict:
    path = ctx.path("org", "mcp", "liveness.json")
    try:
        doc = json.load(open(path, encoding="utf-8"))
    except OSError as exc:
        raise BadFile("%s: unreadable (%s). An absent liveness file is not an empty box." % (path, exc))
    except ValueError as exc:
        raise BadFile("%s: not JSON (%s)" % (path, exc))
    if not isinstance(doc, dict):
        raise BadFile("%s: top level is not an object" % path)
    return doc


def kind_resolver():
    """kind_of(serial) through lib/seat_roles.py; a minimal local reader of org/ref/SEAT_ROLES.json if the module is absent."""
    try:
        mod = load_mod("opal_seat_roles", "lib/seat_roles.py")
        data = mod.load()
        return lambda serial: mod.kind_of(serial, data)
    except Exception:  # noqa: BLE001
        pass
    try:
        data = json.load(open(os.path.join(ROOT, "org", "ref", "SEAT_ROLES.json"), encoding="utf-8"))
    except (OSError, ValueError):
        return lambda serial: "UNKNOWN"

    def kind_of(serial: str) -> str:
        base = re.sub(r"~[A-Za-z0-9]+$", "", serial.strip())
        hits = [r["kind"] for r in data.get("kinds", []) if re.search(r["serial_pattern"], base)]
        return hits[0] if len(hits) == 1 else "UNKNOWN"
    return kind_of


def presence_last(ctx: Ctx, now: int) -> int:
    """Newest presence stamp, read as .tools/drive-mode.py reads it (a future value is skipped)."""
    best = 0
    for path in glob.glob(ctx.path("org", "mcp", "presence", "*.last")):
        try:
            raw = open(path, encoding="utf-8", errors="replace").read().strip()
        except OSError:
            continue
        val = int(raw) if raw.isdigit() else 0
        if val <= now + 300:
            best = max(best, val)
    return best


def live_leases(ctx: Ctx, now: int) -> list:
    """Live drive-mode leases, READ ONLY (drive-mode.py's own loader deletes a lapsed marker; this does not)."""
    out = []
    grace_to = presence_last(ctx, now) + PRESENCE_GRACE
    for path in sorted(glob.glob(ctx.path("org", "mcp", "drive_mode", "*.json"))):
        try:
            lease = json.load(open(path, encoding="utf-8", errors="replace"))
            exp = int(lease["expires_epoch"])
        except (OSError, ValueError, KeyError, TypeError):
            continue
        if max(exp, grace_to) > now:
            lease["_file"] = os.path.relpath(path, ctx.data).replace("\\", "/")
            out.append(lease)
    return out


def arms_drive(ctx: Ctx, serial: str):
    """(drive, cite) from the first LIVE_ARMS.md Arms row that names the serial and a drive word; ("NONE", "") otherwise."""
    rel = "org/ref/LIVE_ARMS.md"
    try:
        lines = open(ctx.path("org", "ref", "LIVE_ARMS.md"), encoding="utf-8", errors="replace").read().splitlines()
    except OSError:
        return "NONE", ""
    units, cur, section = [], None, ""
    for no, line in enumerate(lines, 1):
        if line.startswith("## "):
            section, cur = line[3:].strip(), None
            continue
        if section != "Arms":
            continue
        if re.match(r"^\s*- ", line):
            cur = [no, line]
            units.append(cur)
        elif line.strip() and cur is not None:
            cur[1] += " " + line.strip()
        else:
            cur = None
    full = re.compile(r"(?<![A-Za-z0-9_~.])%s(?![A-Za-z0-9_~])" % re.escape(serial))
    prefix, _, lane = serial.partition("~")
    short = re.compile(r"(?<![A-Za-z0-9_])~%s(?![A-Za-z0-9_])" % re.escape(lane)) if lane else None
    for no, text in units:
        ends = [m.end() for m in full.finditer(text)]
        if short is not None and prefix in text:
            ends += [m.end() for m in short.finditer(text)]
        if not ends:
            continue
        end = min(ends)
        after = DRIVE_TOKEN.search(text, end)
        if after:
            word = after.group(1)
        else:
            before = [m for m in DRIVE_TOKEN.finditer(text[:end])]
            if not before:
                continue
            word = before[-1].group(1)
        return word + "-drive", "%s line %d (an authorisation, not activity)" % (rel, no)
    return "NONE", ""


def project_rows(ctx: Ctx) -> set:
    return {os.path.basename(os.path.dirname(p)) for p in
            glob.glob(ctx.path("org", "missions", "D*", "*", "*", "project.json"))}


def resolve_project(summary: str, rows: set) -> str:
    for tok in PROJECT_TOKEN.findall(summary or ""):
        if tok in rows:
            return tok
    return "UNRESOLVED"


def open_order_counts(ctx: Ctx) -> dict:
    """{issued_by serial: count of non-terminal orders}, parsed from the order files (never the broker's count)."""
    counts = {}
    for path in glob.glob(ctx.path("org", "missions", "D*", "*", "*", "task-orders", "*.md")):
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        who = re.search(r"<issued_by>\s*([^<\s]+)\s*</issued_by>", text)
        if not who:
            continue
        word = None
        for st in re.finditer(r"<status>\s*([A-Za-z_-]+)", text):
            if st.group(1).lower() in STATUS_WORDS:
                word = st.group(1).lower()
                break
        if word in TERMINAL:
            continue
        counts[who.group(1)] = counts.get(who.group(1), 0) + 1
    return counts


def last_commits(ctx: Ctx) -> dict:
    """{author name: newest commit epoch}, one pass over every branch. The author name must equal the serial exactly."""
    if ctx.fixture:
        try:
            raw = open(ctx.path("gitlog.txt"), encoding="utf-8").read()
        except OSError:
            raw = ""
    else:
        try:
            raw = subprocess.run(["git", "-C", ctx.data, "log", "--all", "--format=%ct%x09%an"], capture_output=True,
                                 text=True, check=True, timeout=100).stdout
        except Exception as exc:  # noqa: BLE001
            raise BadFile("git log unreadable (%s)" % exc)
    best = {}
    for line in raw.splitlines():
        head, _, name = line.partition("\t")
        if head.isdigit() and name and int(head) > best.get(name, 0):
            best[name] = int(head)
    return best


# ---------------------------------------------------------------- the build

def decide(kind: str, drive, orders, commit_min, window: int) -> str:
    recent = commit_min != "NEVER" and commit_min <= window
    if kind != "COO":
        return "WORKING" if recent else "IDLE"
    has_drive = drive in DRIVES
    if recent or (orders or 0) > 0:
        return "WORKING"
    return "IDLE" if has_drive else "NOTHING"


def build(ctx: Ctx, device: str, window: int) -> list:
    now = ctx.now()
    live = read_liveness(ctx)
    kind_of = kind_resolver()
    leases = live_leases(ctx, now)
    rows_known = project_rows(ctx)
    orders = open_order_counts(ctx)
    commits = last_commits(ctx)
    rows = []
    for serial in sorted(live):
        info = live[serial] if isinstance(live[serial], dict) else {}
        kind = kind_of(serial)
        seen = info.get("last_seen_epoch")
        age = (now - int(seen)) if isinstance(seen, (int, float)) else None
        summary = str(info.get("summary", "")).replace("\r", " ").replace("\n", " ")[:SUMMARY_MAX]
        commit_min = "NEVER" if serial not in commits else max(0, (now - commits[serial]) // 60)
        project = drive = cite = norders = None
        if kind == "COO":
            project = resolve_project(info.get("summary", ""), rows_known)
            drive, cite = "NONE", "no live FAST lease and no LIVE_ARMS.md Arms row names a drive for this serial"
            for lease in leases:
                if lease.get("seat") == serial and lease.get("mode") == "FAST":
                    drive = "closer-drive"
                    cite = "%s (FAST, seat %s, until %s)" % (lease["_file"], serial, lease.get("expires_at", "?"))
                    break
            else:
                found, why = arms_drive(ctx, serial)
                if found != "NONE":
                    drive, cite = found, why
            norders = orders.get(serial, 0)
        rows.append({
            "serial": serial, "kind": kind,
            "liveness": "STALE" if (age is None or age > STALE_SECONDS) else "LIVE",
            "last_seen_minutes": None if age is None else max(0, age // 60),
            "summary": summary, "project": project, "drive": drive, "drive_cite": cite, "open_orders": norders,
            "last_commit_minutes": commit_min,
            "doing": decide(kind, drive, norders, commit_min, window)})
    return rows


def final_line(device: str, rows: list) -> str:
    coo = sum(1 for r in rows if r["kind"] == "COO")
    count = {d: sum(1 for r in rows if r["doing"] == d) for d in DOING}
    reviewer = "present" if any(r["kind"] == "CVO" and r["liveness"] == "LIVE" for r in rows) else "ABSENT"
    ok = all(r["doing"] in DOING for r in rows) and len({r["serial"] for r in rows}) == len(rows) \
        and sum(count.values()) == len(rows)
    return "SEAT-LIST device=%s seats=%d coo=%d working=%d idle=%d nothing=%d reviewer=%s ok=%s" % (
        device, len(rows), coo, count["WORKING"], count["IDLE"], count["NOTHING"], reviewer, ok)


# ---------------------------------------------------------------- the file

def list_path(ctx: Ctx, device: str) -> str:
    return os.path.join(ctx.state_root(), device, "seats.json")


def validate_doc(doc, device: str, where: str) -> dict:
    if not isinstance(doc, dict):
        raise BadFile("%s: top level is not an object" % where)
    unknown = sorted(set(doc) - TOP_KEYS)
    if unknown:
        raise BadFile("%s: unknown key(s) %s (readers refuse a key they do not know)" % (where, ", ".join(unknown)))
    missing = sorted(TOP_KEYS - set(doc))
    if missing:
        raise BadFile("%s: missing key(s) %s" % (where, ", ".join(missing)))
    if doc["schema"] != SCHEMA:
        raise BadFile("%s: schema %r is not %r" % (where, doc["schema"], SCHEMA))
    if doc["device"] != device:
        raise BadFile("%s: device %r is not %r (one file per box)" % (where, doc["device"], device))
    if not isinstance(doc["rows"], list):
        raise BadFile("%s: rows is not a list" % where)
    for i, row in enumerate(doc["rows"]):
        if not isinstance(row, dict):
            raise BadFile("%s: row %d is not an object" % (where, i))
        unknown = sorted(set(row) - ROW_KEYS)
        if unknown:
            raise BadFile("%s: row %s has unknown key(s) %s" % (where, row.get("serial", i), ", ".join(unknown)))
        missing = sorted(ROW_KEYS - set(row))
        if missing:
            raise BadFile("%s: row %s lacks %s" % (where, row.get("serial", i), ", ".join(missing)))
        if row["doing"] not in DOING:
            raise BadFile("%s: row %s doing %r is not one of %s" % (where, row["serial"], row["doing"], "/".join(DOING)))
    return doc


def read_list(ctx: Ctx, device: str) -> dict:
    path = list_path(ctx, device)
    try:
        doc = json.load(open(path, encoding="utf-8"))
    except OSError as exc:
        raise BadFile("%s: unreadable (%s)" % (path, exc))
    except ValueError as exc:
        raise BadFile("%s: not JSON (%s)" % (path, exc))
    return validate_doc(doc, device, path)


def write_list(ctx: Ctx, device: str, rows: list, serial: str) -> str:
    doc = {"schema": SCHEMA, "device": device, "written_at": stamp(ctx.now()), "written_by": serial, "rows": rows}
    path = list_path(ctx, device)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(doc, indent=1, ensure_ascii=True) + "\n")
    os.replace(tmp, path)
    return path


def this_box(dev, reg) -> str:
    name, basis = dev.this_device(reg)
    if name is None:
        raise Refused("this box is unresolved: %s" % basis)
    return name


# ---------------------------------------------------------------- commands

def cmd_write(args) -> int:
    dev = load_mod("opal_devices", "lib/devices.py")
    reg = dev.load()
    device = this_box(dev, reg)
    if args.device and dev.resolve(args.device, reg) != device:
        raise Refused("REFUSED: a seat list is written to this box's file only (%s); %s is another box's file. "
                      "One writer per box." % (device, args.device))
    ctx = Ctx(args.from_fixture)
    rows = build(ctx, device, args.window_minutes)
    serial = os.environ.get("OPAL_AGENT_SERIAL", "").strip() or "seat-list.py"
    path = write_list(ctx, device, rows, serial)
    print("WROTE %s | box %s | window %d min | sources: %s" % (
        path, device, args.window_minutes, "fixture " + ctx.fixture if ctx.fixture else ctx.data))
    for row in rows:
        print("  %-24s %-8s %-5s %-8s %-10s %-16s orders=%-4s commit=%s" % (
            row["serial"], row["kind"], row["liveness"], row["doing"], row["project"] or "-", row["drive"] or "-",
            "-" if row["open_orders"] is None else row["open_orders"],
            row["last_commit_minutes"] if row["last_commit_minutes"] == "NEVER" else "%dm" % row["last_commit_minutes"]))
    line = final_line(device, rows)
    print(line)
    return 0 if line.endswith("ok=True") else 1


def short(text, width: int) -> str:
    text = str(text)
    return text if len(text) <= width else text[:width - 3] + "..."


def cmd_show(args) -> int:
    dev = load_mod("opal_devices", "lib/devices.py")
    reg = dev.load()
    ctx = Ctx(args.from_fixture)
    if args.all:
        boxes = dev.names(reg)
    elif args.device:
        box = dev.resolve(args.device, reg)
        if box is None:
            print("ERROR: %r is not a device in the register (holds: %s)" % (args.device, ", ".join(dev.names(reg))),
                  file=sys.stderr)
            return 2
        boxes = [box]
    else:
        boxes = [this_box(dev, reg)]
    now = ctx.now()
    absent, stale, refused, read, seats = [], [], [], 0, 0
    for box in boxes:
        path = list_path(ctx, box)
        if not os.path.exists(path):
            absent.append(box)
            print("ABSENT %s: no seats.json for %s in this tree (%s). Absent is not empty: nothing here says that box has "
                  "no seats; its file reaches this tree when that box commits it and the manager lands it." % (box, box, path))
            continue
        try:
            doc = read_list(ctx, box)
        except BadFile as exc:
            refused.append(box)
            print("REFUSED %s" % exc)
            continue
        read += 1
        written = stamp_epoch(doc["written_at"])
        age = None if written is None else max(0, (now - written) // 60)
        is_stale = age is None or age > args.stale_minutes
        if is_stale:
            stale.append(box)
        rows = doc["rows"]
        seats += len(rows)
        print("FILE %s | device=%s written_by=%s written_at=%s | age %s min%s | seats=%d" % (
            path, doc["device"], doc["written_by"], doc["written_at"], "unknown" if age is None else age,
            "  ** STALE (older than %d min)" % args.stale_minutes if is_stale else "", len(rows)))
        print("  %-24s %-8s %-5s %-8s %-14s %-16s %-6s %-8s %s" % (
            "SERIAL", "KIND", "LIVE", "DOING", "PROJECT", "DRIVE", "ORDERS", "COMMIT", "SUMMARY"))
        for row in rows:
            commit = row["last_commit_minutes"]
            print("  %-24s %-8s %-5s %-8s %-14s %-16s %-6s %-8s %s" % (
                row["serial"], row["kind"], row["liveness"], row["doing"], row["project"] or "-", row["drive"] or "-",
                "-" if row["open_orders"] is None else row["open_orders"],
                commit if commit == "NEVER" else "%sm" % commit, short(row["summary"], 70)))
        idle_kinds = [r["serial"] for r in rows if r["kind"] == "COO" and r["doing"] == "NOTHING"]
        if idle_kinds:
            print("  ** DOING NOTHING: %s" % ", ".join(idle_kinds))
        if not any(r["kind"] == "CVO" and r["liveness"] == "LIVE" for r in rows):
            print("  ** no reviewer (CVO) live on %s" % box)
    print("SEAT-LIST-SHOW boxes=%d read=%d absent=%s stale=%s refused=%s seats=%d" % (
        len(boxes), read, ",".join(absent) or "none", ",".join(stale) or "none", ",".join(refused) or "none", seats))
    return 3 if refused else 0


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="seat-list.py", description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    wr = sub.add_parser("write", help="build this box's seat list and write its seats.json")
    wr.add_argument("--device", help="refused unless it is this box (one writer per box)")
    wr.add_argument("--window-minutes", type=int, default=120, help="a commit inside this window counts as work (default 120)")
    wr.add_argument("--from-fixture")
    sh = sub.add_parser("show", help="print the saved list(s) with each file's age")
    grp = sh.add_mutually_exclusive_group()
    grp.add_argument("--device")
    grp.add_argument("--all", action="store_true")
    sh.add_argument("--stale-minutes", type=int, default=90)
    sh.add_argument("--from-fixture")
    return ap


def main(argv: list) -> int:
    args = build_parser().parse_args(argv)
    try:
        return {"write": cmd_write, "show": cmd_show}[args.cmd](args)
    except Refused as exc:
        print(str(exc) if str(exc).startswith("REFUSED") else "ERROR: %s" % exc, file=sys.stderr)
        return 1 if str(exc).startswith("REFUSED") else 2
    except BadFile as exc:
        print("REFUSED: %s" % exc, file=sys.stderr)
        return 3
    except Exception as exc:   # a register that cannot be read stops the tool; there is no built-in device list
        if type(exc).__name__ == "RegisterError":
            print(str(exc), file=sys.stderr)
            return 3
        raise


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
