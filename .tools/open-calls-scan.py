#!/usr/bin/env python3
"""open-calls-scan.py -- ONE PASS of the per-box open-calls scan: an open call on this box makes this box's CTO adjudicate.

Andrew-direct 2026-10-09 ~00:0xZ, record org/tier1_exec/1.0.0_SA_CTO/deliverables/
ANDREW_DIRECT_20261009_000xZ_KEEP_WORK_DRIVING_OPEN_CALL_QUEUE_CROSS_ADJUDICATION_AND_NEXT_CALLS_ON_EMPTY_TICK.md: "there
should be a 'notification' function that scans that json per box every 10 min and if it has open-calls on it, the CTO on
that box has to adjudicate." That sentence is the explicit ask CLAUDE.md section 5's notification moratorium requires; this
tool is scoped to it and sends nothing off the fabric -- one inbox file to one seat on its own box. Design:
org/tier1_exec/4.0.0_SA_CRO~B/deliverables/DESIGN_KEEP_WORK_DRIVING_20261009.md. Owner 4.0.0_SA_CRO~B.
Run every 10 minutes by the box's scheduled task `Opal open-calls scan` (.tools/open-calls-scan-schedule.ps1).

    python .tools/open-calls-scan.py              one pass: read, nudge if due, publish the scan heartbeat
    python .tools/open-calls-scan.py --dry-run    print what the pass would send; write nothing, put nothing
    python .tools/open-calls-scan.py --log <file> one pass, output appended to <file> (the scheduled task's form)
    python .tools/open-calls-scan.py --selftest   LAST line  OPEN-CALLS-SCAN-SELFTEST cases=<k>/<n> ok=<True|False>

ONE PASS on box B:
  1. DUE = rows of B's list (org/devices/state/<B>/open_calls.json) that are OPEN, kind `fork`, and carry no `escalation`.
     An `act` is Andrew's to do and never nudges a CTO; an escalated row waits on its cross-adjudication or on Andrew.
  2. CLOSE-OUT = OPEN rows escalated to `xadj` whose cross-adjudication file now reads RULED (.tools/xadj.py).
  3. TO RULE = OPEN cross-adjudication files from every box, but only when B is the adjudicator of record (xadj.py
     adjudicator(): the laptop, or site Z when the laptop's heartbeat is stale or reads no live CTO).
  4. The TARGET is B's CTO (CTO_OF[B] if its MCP process is alive, else any live 1.0.0_SA_CTO lane on B); with no CTO
     live, B's MSTR (it spawns and unsticks seats) is told the CTO is absent; with neither, nothing is written and the
     heartbeat says so.
  5. One inbox file goes to the target when the three sets, together, differ from the last file sent, or RENUDGE_SEC
     after the last file while unchanged. Empty sets reset the memory and send nothing.
  6. The scan heartbeat goes to s3://opal-313476888478-globgrph/fabric/open-calls/v1/box=<B>/scan.json -- the
     measurement xadj.py reads to decide whether the laptop is up.
  0. THE SWITCH first: `open-calls.py mode` (s3 .../open-calls/v1/mode.json, skill /keep-driving). `scan` off for B ->
     the pass sends nothing (sent=no:mode-off) and the heartbeat carries mode=off, so paused never reads as dead.
LAST line: OPEN-CALLS-SCAN device=<B> due=<n> closeout=<n> to_rule=<n> target=<serial|none> sent=<yes|no:<why>> ... mode=<on|off>

Environment (tests only): OPAL_STATE_ROOT (open-calls lists), OPAL_XADJ_LOCAL (store + heartbeats), OPAL_LIVENESS_FILE,
OPAL_INBOX_ROOT, OPAL_SCAN_STATE, OPAL_SCAN_DEVICE. Exit 0 = a pass ran (either verdict), 2 = this box unresolved,
3 = this box's list unreadable.
"""
from __future__ import annotations

import argparse
import datetime
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
SCHEMA = "open-calls-scan/1"
RENUDGE_SEC = 1800
LIVE_MAX_AGE_SEC = 6 * 3600   # a liveness entry older than this is not trusted even if its PID resolves (PID reuse)
CTO_OF = {"laptop": "1.0.0_SA_CTO", "sitez": "1.0.0_SA_CTO~Z", "dell1": "1.0.0_SA_CTO~DELL1", "dell2": "1.0.0_SA_CTO~DELL2"}
MSTR_OF = {"laptop": "0.0.0_AB_MSTR", "sitez": "0.0.0_AB_MSTR~Z", "dell1": "0.0.0_AB_MSTR~DELL1", "dell2": "0.0.0_AB_MSTR~DELL2"}
LIST_CAP = 12
TIERS = ("tier0_exec", "tier0_utility", "tier1_exec", "tier2_senior", "tier3_junior")


def load_mod(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def now_dt() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)


def stamp(dt: datetime.datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def age_min(s: str, now: datetime.datetime) -> int:
    try:
        t = datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
    except (TypeError, ValueError):
        return -1
    return int((now - t).total_seconds() // 60)


# ---------------------------------------------------------------- seats on this box

def pid_alive(pid) -> bool:
    try:
        pid = int(pid)
    except (TypeError, ValueError):
        return False
    if pid <= 0:
        return False
    if sys.platform.startswith("win"):
        import ctypes
        handle = ctypes.windll.kernel32.OpenProcess(0x1000, False, pid)   # PROCESS_QUERY_LIMITED_INFORMATION, probe only
        if handle:
            ctypes.windll.kernel32.CloseHandle(handle)
            return True
        return False
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def liveness() -> dict:
    path = os.environ.get("OPAL_LIVENESS_FILE", "").strip() or os.path.join(ROOT, "org", "mcp", "liveness.json")
    try:
        data = json.load(open(path, encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def is_live(entry, now_epoch: float, probe=pid_alive) -> bool:
    if not isinstance(entry, dict):
        return False
    if now_epoch - float(entry.get("last_seen_epoch") or 0) > LIVE_MAX_AGE_SEC:
        return False
    return probe(entry.get("pid"))


def pick(live: dict, preferred: str, prefix: str, now_epoch: float, probe=pid_alive):
    if preferred and is_live(live.get(preferred), now_epoch, probe):
        return preferred
    for serial in sorted(live):
        if (serial == prefix or serial.startswith(prefix + "~")) and is_live(live[serial], now_epoch, probe):
            return serial
    return None


def inbox_dir(serial: str) -> str:
    root = os.environ.get("OPAL_INBOX_ROOT", "").strip() or os.path.join(ROOT, "org", "mcp", "inbox")
    base, _, lane = serial.partition("~")
    d = os.path.join(root, base)
    return os.path.join(d, "~" + lane) if lane else d


# ---------------------------------------------------------------- the pass

def state_path() -> str:
    p = os.environ.get("OPAL_SCAN_STATE", "").strip()
    if p:
        return p
    try:
        common = subprocess.run(["git", "-C", ROOT, "rev-parse", "--path-format=absolute", "--git-common-dir"],
                                capture_output=True, text=True, timeout=20,
                                creationflags=0x08000000 if sys.platform.startswith("win") else 0).stdout.strip()   # no console
    except (OSError, subprocess.SubprocessError):
        common = ""
    return os.path.join(common or os.path.join(ROOT, ".git"), "open-calls-scan", "state.json")


def read_state() -> dict:
    try:
        return json.load(open(state_path(), encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def write_state(st: dict) -> None:
    p = state_path()
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p + ".tmp", "w", encoding="utf-8") as fh:
        json.dump(st, fh, indent=1)
    os.replace(p + ".tmp", p)


def compose(device: str, target: str, cto_absent: bool, due: list, closeout: list, to_rule: list, now) -> tuple:
    n = len(due) + len(closeout) + len(to_rule)
    subj = "[OPEN-CALLS SCAN] %d item(s) to adjudicate on %s" % (n, device)
    lines = ["# Message from OPEN-CALLS-SCAN (box %s)" % device, "**To:** %s" % target,
             "**Date:** %s" % now.strftime("%Y%m%dT%H%M%SZ"), "**Subject:** %s" % subj, ""]
    if cto_absent:
        lines += ["NO CTO IS LIVE ON %s. These calls wait on a CTO: seat one (or unstick it) so it adjudicates." % device, ""]
    if due:
        lines += ["CALLS TO ADJUDICATE (this box's open forks; Andrew-direct 2026-10-09 ~00:0xZ: the CTO on the box has to "
                  "adjudicate). Per call, ONE of:",
                  "  RULE it: /open-calls --adjudicate <CODE>, then python .tools/open-calls.py close --id <id> --by <you> "
                  "--ruling <record>",
                  "  ESCALATE it (open-ended, architectural, out of pattern, or CROSS-BOX): write the submission (## Context, "
                  "## Position, ## Why it gave pause: ### Ambiguity / ### Out of pattern / ### Other solutions), then "
                  "python .tools/xadj.py open --call-id <id> --body <file> --by <you>",
                  "  HOLD it for Andrew (money, vendor, directive, his named hold): python .tools/open-calls.py hold --id <id> "
                  "--by <you> --reason \"<one line>\""]
        for r in due[:LIST_CAP]:
            lines.append("  - %s | %s | %s | age %dm | %s | source %s" % (r["id"], r["project"], r["scope"].get("verdict", "?"),
                                                                         age_min(r["opened_at"], now), r["subject"][:160],
                                                                         r["source"]))
            lines.append("      CONTEXT: %s" % (r.get("context") or "(none: written before the context field; read the source)"))
            lines.append("      REC: %s" % (r.get("rec") or "(none)"))
        if len(due) > LIST_CAP:
            lines.append("  ... and %d more: python .tools/open-calls.py list" % (len(due) - LIST_CAP))
        lines.append("")
    if closeout:
        lines.append("RULED CROSS-ADJUDICATIONS -- close the row on the ruling: python .tools/open-calls.py close --id <id> "
                     "--by <you> --ruling <record> --xadj <XA id>")
        for r, x in closeout:
            lines.append("  - %s <- %s ruled by %s on %s: %s" % (r["id"], x["id"], x["ruling"]["by"], x["ruling"]["device"],
                                                                  x["ruling"]["record"]))
        lines.append("")
    if to_rule:
        lines.append("CROSS-ADJUDICATIONS TO RULE (this box is the adjudicator of record): python .tools/xadj.py show --id <XA>, "
                     "then python .tools/xadj.py rule --id <XA> --by <you> --ruling \"(a) ... because ...\", and commit the record.")
        for x in to_rule[:LIST_CAP]:
            lines.append("  - %s | from %s %s | %s | %s | opened %s (%dm)" % (x["id"], x["from_device"], x["from_serial"],
                                                                             x["project"], x["subject"][:140], x["opened_at"],
                                                                             age_min(x["opened_at"], now)))
        lines.append("")
    lines.append("Re-sent every %d minutes while unchanged. Owner of this scan: 4.0.0_SA_CRO~B." % (RENUDGE_SEC // 60))
    return subj, "\n".join(lines) + "\n"


def deliver(target: str, subj: str, content: str, now) -> str:
    d = inbox_dir(target)
    if not os.path.isdir(d):
        raise OSError("no inbox directory %s (the seat's watcher creates it)" % d)
    name = "%s_OPEN-CALLS-SCAN_%s.md" % (now.strftime("%Y%m%dT%H%M%SZ"), re.sub(r"[^a-zA-Z0-9._-]", "_", subj)[:40])
    path = os.path.join(d, name)
    with open(path + ".tmp", "w", encoding="utf-8", newline="\n") as fh:
        fh.write(content)
    os.replace(path + ".tmp", path)
    return path


# ---------------------------------------------------------------- unblock files (Andrew-direct 2026-10-09 ~02:3xZ-02:4xZ)
# A COO's third empty tick writes to the CRO (.tools/unblock.py); the CRO proposes a new approach, the CTO folds it into the
# workflow, the CVO signs it off, the COO resumes. This pass drops each step's nudge in the inbox of the seat on THIS box that
# owns it. Record: org/tier1_exec/4.0.0_SA_CRO~B/deliverables/ANDREW_DIRECT_20261009_023xZ_THIRD_EMPTY_TICK_UNBLOCK_VIA_CRO_THEN_CTO.md

UB_ACTS = {
    "CRO": "find a new approach that is NOT blocked. Read: python .tools/unblock.py show --id {id}. Write ## New approach / "
           "## Why it is not blocked / ## What changes for the COO, then python .tools/unblock.py propose --id {id} --by <you> "
           "--body <file>. It goes to the CTO of box {box}.",
    "CTO": "synthesize the CRO's approach into the workflow (a PRD addendum, a round-N analysis or a ruling the COO's drive "
           "reads), then python .tools/unblock.py fold --id {id} --by <you> --ref <that file>. The CVO signs it off.",
    "CVO": "sign the CTO's fold off, or refuse it back. Read: python .tools/unblock.py show --id {id} and the fold's ref. Then "
           "python .tools/unblock.py sign --id {id} --by <you> [--note ...] (writes the record; commit it), or "
           "python .tools/unblock.py refuse --id {id} --by <you> --reason \"...\".",
    "COO": "your unblock is SIGNED: drive on the fold (python .tools/unblock.py show --id {id}), then "
           "python .tools/unblock.py resume --id {id} --by <you>.",
}


def unblock_items(device: str, docs: list, live: dict, ep: float, cto, mstr, probe) -> dict:
    """{target serial: [(role, doc, seat_absent)]} for every unblock file whose next act is on THIS box."""
    ub = load_mod("opal_unblock_for_scan", ".tools/unblock.py")
    out = {}
    for d in docs:
        role, seat = None, None
        if d["state"] == "OPEN" and d["cro_device"] == device:
            role, seat = "CRO", pick(live, ub.CRO_OF.get(device, ""), "4.0.0_SA_CRO", ep, probe)
        elif d["state"] == "PROPOSED" and d["from_device"] == device:
            role, seat = "CTO", cto
        elif d["state"] == "FOLDED" and d["fold"]["cvo_device"] == device:
            role, seat = "CVO", pick(live, ub.CVO_OF.get(device, ""), "3.0.0_SA_CVO", ep, probe)
        elif d["state"] == "SIGNED" and d["from_device"] == device:
            role, seat = "COO", d["from_serial"] if is_live(live.get(d["from_serial"]), ep, probe) else None
        if role is None:
            continue
        target = seat or mstr
        if target:
            out.setdefault(target, []).append((role, d, seat is None))
    return out


def compose_unblock(device: str, target: str, items: list, now) -> tuple:
    subj = "[UNBLOCK] %d step(s) for you on %s" % (len(items), device)
    lines = ["# Message from OPEN-CALLS-SCAN (box %s)" % device, "**To:** %s" % target,
             "**Date:** %s" % now.strftime("%Y%m%dT%H%M%SZ"), "**Subject:** %s" % subj, "",
             "A COO found nothing that advances its project for three ticks and wrote to the CRO (Andrew-direct 2026-10-09). "
             "The next step of each file below is yours:"]
    for role, d, absent in items:
        lines.append("  - %s [%s] project %s, COO %s on %s, opened %s" % (d["id"], d["state"], d["project"], d["from_serial"],
                                                                         d["from_device"], d["opened_at"]))
        if absent:
            lines.append("      NO %s IS LIVE ON %s: seat one (or unstick it) for this step." % (role, device))
        lines.append("      %s: %s" % (role, UB_ACTS[role].format(id=d["id"], box=d["from_device"])))
    lines.append("")
    lines.append("Re-sent every %d minutes while unchanged. Owner of this scan: 4.0.0_SA_CRO~B." % (RENUDGE_SEC // 60))
    return subj, "\n".join(lines) + "\n"


def unblock_pass(device: str, dry: bool, now, live: dict, cto, mstr, prev: dict, probe, notes: list) -> tuple:
    """(new memory {serial: {fp, sent_at}}, delivered count, item count)."""
    try:
        docs = load_mod("opal_unblock_for_scan", ".tools/unblock.py").list_all()
    except Exception as exc:  # noqa: BLE001
        notes.append("unblock store unreadable (%s)" % type(exc).__name__)
        return prev, 0, 0
    items = unblock_items(device, docs, live, now.timestamp(), cto, mstr, probe)
    mem, sent = {}, 0
    for target, its in sorted(items.items()):
        fp = json.dumps(sorted("%s:%s" % (d["id"], d["state"]) for _, d, _ in its))
        old = prev.get(target) or {}
        age = age_min(old.get("sent_at"), now)
        if old.get("fp") == fp and 0 <= age and age * 60 < RENUDGE_SEC:
            mem[target] = old
            continue
        subj, content = compose_unblock(device, target, its, now)
        if dry:
            print(content)
            mem[target] = old
            continue
        try:
            deliver(target, subj, content, now)
            mem[target] = {"fp": fp, "sent_at": stamp(now)}
            sent += 1
        except OSError as exc:
            notes.append("unblock nudge to %s not delivered (%s)" % (target, exc))
            mem[target] = old
    return mem, sent, sum(len(v) for v in items.values())


def run_pass(device: str, dry: bool, now=None, probe=pid_alive) -> tuple:
    now = now or now_dt()
    oc = load_mod("opal_open_calls", ".tools/open-calls.py")
    xa = load_mod("opal_xadj", ".tools/xadj.py")
    rows = []
    if os.path.exists(oc.list_path(device)):
        rows = oc.read_list(device)["rows"]
    due = [r for r in rows if r["state"] == "OPEN" and r.get("kind", "fork") == "fork" and not r.get("escalation")]
    notes = []
    try:
        xdocs = xa.list_all()
    except Exception as exc:  # noqa: BLE001 -- a store outage must not stop the box's own nudge
        xdocs = []
        notes.append("xadj store unreadable (%s)" % type(exc).__name__)
    by_id = {x["id"]: x for x in xdocs}
    closeout = []
    for r in rows:
        esc = r.get("escalation") or {}
        x = by_id.get(esc.get("ref") or "")
        if r["state"] == "OPEN" and esc.get("to") == "xadj" and x and x["state"] == "RULED":
            closeout.append((r, x))
    live = liveness()
    ep = now.timestamp()
    cto = pick(live, CTO_OF.get(device, ""), "1.0.0_SA_CTO", ep, probe)
    if device == xa.PRIMARY:   # the laptop's own pass IS the measurement its heartbeat carries
        adj, why = (xa.PRIMARY, "this pass reads the laptop CTO live") if cto else (xa.BACKUP, "this pass reads no live laptop CTO")
    else:
        try:
            adj, why = xa.adjudicator(now)
        except Exception as exc:  # noqa: BLE001
            adj, why = None, "adjudicator unmeasurable (%s)" % type(exc).__name__
    to_rule = [x for x in xdocs if x["state"] == "OPEN"] if adj == device else []
    target = cto or pick(live, MSTR_OF.get(device, ""), "0.0.0_AB_MSTR", ep, probe)
    fp = json.dumps([sorted(r["id"] for r in due), sorted(x["id"] for _, x in closeout), sorted(x["id"] for x in to_rule),
                     target], sort_keys=True)
    st = read_state()
    ub_prev = st.get("unblock") or {}
    n = len(due) + len(closeout) + len(to_rule)
    mdoc, msrc = oc.mode_read()
    mode = oc.mode_state(mdoc, device, "scan")
    if msrc.startswith("unreadable"):
        notes.append("keep-driving switch unreadable (%s); reads ON" % msrc)
    if mode == "off":
        sent = "no:mode-off"   # the switch (/keep-driving) holds the scan; the memory is kept for when it turns back on
    elif n == 0:
        sent, st = "no:nothing-due", {}
    elif target is None:
        sent = "no:no-cto-or-mstr-live"
    elif st.get("fp") == fp and age_min(st.get("sent_at"), now) * 60 < RENUDGE_SEC and age_min(st.get("sent_at"), now) >= 0:
        sent = "no:unchanged-sent-%dm-ago" % age_min(st.get("sent_at"), now)
    else:
        subj, content = compose(device, target, cto is None, due, closeout, to_rule, now)
        if dry:
            print(content)
            sent = "no:dry-run"
        else:
            try:
                path = deliver(target, subj, content, now)
                st = {"fp": fp, "sent_at": stamp(now), "to": target, "file": path}
                sent = "yes"
            except OSError as exc:
                sent = "no:deliver-failed(%s)" % exc
    mstr = pick(live, MSTR_OF.get(device, ""), "0.0.0_AB_MSTR", ep, probe)
    if mode == "off":
        ub_mem, ub_sent, ub_n = ub_prev, 0, 0
    else:
        ub_mem, ub_sent, ub_n = unblock_pass(device, dry, now, live, cto, mstr, ub_prev, probe, notes)
    st = dict(st, unblock=ub_mem)
    hb = {"schema": SCHEMA, "device": device, "scanned_at": stamp(now), "cto_serial": cto, "cto_live": cto is not None,
          "target": target, "due": len(due), "closeout": len(closeout), "to_rule": len(to_rule), "adjudicator": adj,
          "adjudicator_why": why, "sent": sent, "mode": mode, "unblock_items": ub_n, "unblock_sent": ub_sent}
    if not dry:
        write_state(st)
        try:
            xa.heartbeat_put(device, hb)
        except Exception as exc:  # noqa: BLE001
            notes.append("heartbeat not written (%s)" % type(exc).__name__)
    for note in notes:
        print("WARN: " + note)
    line = "OPEN-CALLS-SCAN device=%s due=%d closeout=%d to_rule=%d target=%s sent=%s adjudicator=%s mode=%s unblock=%d/%d" % (
        device, len(due), len(closeout), len(to_rule), target or "none", sent, adj or "?", mode, ub_sent, ub_n)
    return line, hb


# ---------------------------------------------------------------- selftest

def selftest() -> int:
    cases = []

    def rec(name, ok, detail=""):
        cases.append(bool(ok))
        print("%s %s%s" % ("PASS" if ok else "FAIL", name, (" -- " + str(detail)) if detail and not ok else ""))

    base = tempfile.mkdtemp(prefix="ocscan_selftest_")
    env_keys = ("OPAL_STATE_ROOT", "OPAL_XADJ_LOCAL", "OPAL_LIVENESS_FILE", "OPAL_INBOX_ROOT", "OPAL_SCAN_STATE",
                "OPAL_MODE_LOCAL")
    keep = {k: os.environ.get(k) for k in env_keys}
    try:
        os.environ["OPAL_STATE_ROOT"] = os.path.join(base, "state")
        os.environ["OPAL_XADJ_LOCAL"] = os.path.join(base, "xadj")
        os.environ["OPAL_LIVENESS_FILE"] = os.path.join(base, "liveness.json")
        os.environ["OPAL_INBOX_ROOT"] = os.path.join(base, "inbox")
        os.environ["OPAL_SCAN_STATE"] = os.path.join(base, "scan_state.json")
        os.environ["OPAL_MODE_LOCAL"] = os.path.join(base, "mode.json")
        dev = "dell1"
        now = now_dt()
        alive = {101, 202}
        probe = (lambda pid: int(pid) in alive)   # noqa: E731
        live = {"1.0.0_SA_CTO~DELL1": {"pid": 101, "last_seen_epoch": now.timestamp() - 60},
                "0.0.0_AB_MSTR~DELL1": {"pid": 202, "last_seen_epoch": now.timestamp() - 60}}
        json.dump(live, open(os.environ["OPAL_LIVENESS_FILE"], "w"))
        for s in live:
            os.makedirs(inbox_dir(s), exist_ok=True)
        oc = load_mod("opal_open_calls", ".tools/open-calls.py")

        def row(cid, **kw):
            r = {"id": cid, "project": "P", "subject": "s " + cid, "asked_by": "x", "source": "src", "orders": [], "roots": [],
                 "state": "OPEN", "opened_at": stamp(now), "kind": "fork", "scope": {"verdict": "OWN-BOX"}, "closed": None}
            r.update(kw)
            return r
        doc = {"schema": oc.SCHEMA, "device": dev, "written_at": stamp(now), "written_by": "t",
               "rows": [row("c-act", kind="act"), row("c-closed", state="CLOSED")]}
        oc.write_list(dev, doc, "t")
        line, _ = run_pass(dev, False, now, probe)
        rec("acts-and-closed-rows-nudge-nobody", "due=0" in line and "sent=no:nothing-due" in line, line)
        doc["rows"].append(row("c-fork", context="why c-fork exists and what it gates", rec="(a) c-fork, because"))
        oc.write_list(dev, doc, "t")
        line, hb = run_pass(dev, False, now, probe)
        files = os.listdir(inbox_dir("1.0.0_SA_CTO~DELL1"))
        rec("an-open-fork-nudges-the-box-cto", "due=1" in line and "sent=yes" in line and len(files) == 1, line)
        body = open(os.path.join(inbox_dir("1.0.0_SA_CTO~DELL1"), files[0]), encoding="utf-8").read()
        rec("the-file-names-the-call-and-the-three-outcomes", "c-fork" in body and "xadj.py open" in body and "hold" in body)
        rec("the-file-carries-context-and-rec", "CONTEXT: why c-fork" in body and "REC: (a) c-fork" in body, body[-300:])
        rec("heartbeat-says-cto-live", hb["cto_live"] and hb["cto_serial"] == "1.0.0_SA_CTO~DELL1")
        line, _ = run_pass(dev, False, now + datetime.timedelta(minutes=10), probe)
        rec("unchanged-within-30m-is-not-resent", "sent=no:unchanged" in line, line)
        line, _ = run_pass(dev, False, now + datetime.timedelta(minutes=31), probe)
        rec("unchanged-after-30m-is-resent", "sent=yes" in line, line)
        xa = load_mod("opal_xadj", ".tools/xadj.py")
        xid = "XA-20261009T000000Z-5e5e"
        x = {"schema": xa.SCHEMA, "id": xid, "call_id": "c-fork", "project": "P", "subject": "s", "scope_verdict": "CROSS-BOX",
             "from_device": dev, "from_serial": "1.0.0_SA_CTO~DELL1", "opened_at": stamp(now), "body": "b", "state": "OPEN",
             "ruling": None}
        xa._put(xa.key_of(xid), x)
        oc.set_escalation(dev, "c-fork", {"to": "xadj", "ref": xid, "at": stamp(now), "by": "t", "reason": None}, "t")
        line, _ = run_pass(dev, False, now + datetime.timedelta(minutes=40), probe)
        rec("an-escalated-row-stops-nudging", "due=0" in line and "closeout=0" in line, line)
        xa._put(xa.key_of(xid), dict(x, state="RULED", ruling={"at": stamp(now), "by": "1.0.0_SA_CTO", "device": "laptop",
                                                                "text": "(a)", "record": "r.md"}))
        line, _ = run_pass(dev, False, now + datetime.timedelta(minutes=50), probe)
        rec("a-ruled-xadj-nudges-the-close", "closeout=1" in line and "sent=yes" in line, line)
        alive.discard(101)
        line, hb = run_pass(dev, False, now + datetime.timedelta(minutes=60), probe)
        rec("no-live-cto-goes-to-the-box-mstr", "target=0.0.0_AB_MSTR~DELL1" in line and not hb["cto_live"], line)
        rec("dell1-is-never-the-adjudicator", "to_rule=0" in line)
        # the laptop as adjudicator sees every box's OPEN file
        lap_live = {"1.0.0_SA_CTO": {"pid": 202, "last_seen_epoch": now.timestamp()}}
        json.dump(lap_live, open(os.environ["OPAL_LIVENESS_FILE"], "w"))
        os.makedirs(inbox_dir("1.0.0_SA_CTO"), exist_ok=True)
        xa._put(xa.key_of("XA-20261009T000000Z-0001"), dict(x, id="XA-20261009T000000Z-0001", call_id="other"))
        xa.heartbeat_put("laptop", {"scanned_at": stamp(now), "cto_live": True, "cto_serial": "1.0.0_SA_CTO"})
        os.remove(os.environ["OPAL_SCAN_STATE"])
        line, _ = run_pass("laptop", False, now, probe)
        rec("the-laptop-gets-open-xadj-files-to-rule", "to_rule=1" in line and "sent=yes" in line, line)
        oc.mode_write({"schema": oc.MODE_SCHEMA, "scan": "on", "empty_tick": "on", "boxes": {"laptop": {"scan": "off"}},
                       "set_by": "t", "set_at": stamp(now), "reason": "r"})
        os.remove(os.environ["OPAL_SCAN_STATE"])
        line, hb = run_pass("laptop", False, now, probe)
        rec("the-switch-off-for-this-box-sends-nothing-and-says-so", "sent=no:mode-off" in line and hb["mode"] == "off", line)
        line, _ = run_pass(dev, False, now, probe)
        rec("another-box-still-reads-on", "mode=on" in line, line)
        # unblock routing: OPEN -> CRO on cro_device; PROPOSED -> CTO; FOLDED -> CVO on cvo_device; SIGNED -> the COO
        ub = load_mod("opal_unblock_for_scan", ".tools/unblock.py")
        oc.mode_write({"schema": oc.MODE_SCHEMA, "scan": "on", "empty_tick": "on", "boxes": {}, "set_by": "t",
                       "set_at": stamp(now), "reason": "r"})
        live2 = {"1.0.0_SA_CTO~DELL1": {"pid": 101, "last_seen_epoch": now.timestamp()},
                 "4.0.0_SA_CRO~D1": {"pid": 101, "last_seen_epoch": now.timestamp()},
                 "3.0.0_SA_CVO~D1": {"pid": 101, "last_seen_epoch": now.timestamp()},
                 "2.0.0_SA_COO~M1": {"pid": 101, "last_seen_epoch": now.timestamp()},
                 "0.0.0_AB_MSTR~DELL1": {"pid": 202, "last_seen_epoch": now.timestamp()}}
        alive.add(101)
        json.dump(live2, open(os.environ["OPAL_LIVENESS_FILE"], "w"))
        for s_ in live2:
            os.makedirs(inbox_dir(s_), exist_ok=True)
        base_doc = {"schema": ub.SCHEMA, "id": "UB-20261009T000000Z-0a0a", "project": "P", "from_device": dev,
                    "from_serial": "2.0.0_SA_COO~M1", "cro_device": dev, "opened_at": stamp(now), "body": "b",
                    "state": "OPEN", "proposal": None, "fold": None, "signoff": None, "refusals": [], "resumed": None}
        prop = {"at": stamp(now), "by": "4.0.0_SA_CRO~D1", "device": dev, "body": "x"}
        fold = {"at": stamp(now), "by": "1.0.0_SA_CTO~DELL1", "device": dev, "ref": "r.md", "cvo_device": dev}
        sign = {"at": stamp(now), "by": "3.0.0_SA_CVO~D1", "device": dev, "note": "", "record": "x.md"}
        for state, extra, who in (("OPEN", {}, "4.0.0_SA_CRO~D1"),
                                  ("PROPOSED", {"proposal": prop}, "1.0.0_SA_CTO~DELL1"),
                                  ("FOLDED", {"proposal": prop, "fold": fold}, "3.0.0_SA_CVO~D1"),
                                  ("SIGNED", {"proposal": prop, "fold": fold, "signoff": sign}, "2.0.0_SA_COO~M1")):
            xa._put(ub.key_of(base_doc["id"]), dict(base_doc, state=state, **extra))
            items = unblock_items(dev, ub.list_all(), live2, now.timestamp(), "1.0.0_SA_CTO~DELL1", "0.0.0_AB_MSTR~DELL1", probe)
            rec("unblock-%s-goes-to-%s" % (state.lower(), who), list(items) == [who], items)
        xa._put(ub.key_of(base_doc["id"]), dict(base_doc, cro_device="laptop"))
        items = unblock_items(dev, ub.list_all(), live2, now.timestamp(), "1.0.0_SA_CTO~DELL1", "0.0.0_AB_MSTR~DELL1", probe)
        rec("an-open-file-for-the-laptop-cro-is-not-this-boxs", items == {})
        xa._put(ub.key_of(base_doc["id"]), dict(base_doc))
        if os.path.exists(os.environ["OPAL_SCAN_STATE"]):
            os.remove(os.environ["OPAL_SCAN_STATE"])
        line, hb = run_pass(dev, False, now, probe)
        line2, _ = run_pass(dev, False, now + datetime.timedelta(minutes=10), probe)
        rec("the-pass-delivers-the-cro-step-once-then-holds", "unblock=1/1" in line and "unblock=0/1" in line2, line + " || " + line2)
    finally:
        for k, v in keep.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        import shutil
        shutil.rmtree(base, ignore_errors=True)
    ok = all(cases)
    print("OPEN-CALLS-SCAN-SELFTEST cases=%d/%d ok=%s" % (sum(cases), len(cases), ok))
    return 0 if ok else 1


def main(argv: list) -> int:
    ap = argparse.ArgumentParser(prog="open-calls-scan.py", description=__doc__.split("\n")[0])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--log", help="append this pass's output to this file (the scheduled task runs windowless under pythonw)")
    args = ap.parse_args(argv)
    if args.log:
        fh = open(args.log, "a", encoding="utf-8")
        sys.stdout = sys.stderr = fh
        print("=== %s open-calls scan" % stamp(now_dt()))
    if args.selftest:
        return selftest()
    device = os.environ.get("OPAL_SCAN_DEVICE", "").strip()
    if not device:
        dev = load_mod("opal_devices", "lib/devices.py")
        device, basis = dev.this_device(dev.load())
        if device is None:
            print("ERROR: this box is unresolved: %s" % basis, file=sys.stderr)
            return 2
    try:
        line, _ = run_pass(device, args.dry_run)
    except Exception as exc:
        if type(exc).__name__ == "BadFile":
            print("ERROR: this box's open-calls list is unreadable: %s" % exc, file=sys.stderr)
            return 3
        raise
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
