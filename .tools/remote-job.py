#!/usr/bin/env python
"""remote-job.py -- the device side of remote jobs: a machine's MSTR bids for, accepts, completes and closes an ad hoc
job that LDO-001 offered on the agent bus.

Contract: org/tier1_exec/4.0.0_SA_CRO/deliverables/REMOTE_JOBS_PROTOCOL_20261002.md. Authority: Andrew-direct
2026-10-02 ~16:4xZ-17:0xZ, verbatim in org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261002_020xZ_EOD_UPDATE_AUTOMATION.md
("If there are multiple, then they check their boxes, write back to sqs their stats, and the one with the lowest
cpu/memory usage gets the job").

    python .tools/remote-job.py bid J042                                   # availability + CPU/memory -> job.bid
    python .tools/remote-job.py accept J042 --coo 2.0.0_SA_COO~R --brief-file PATH   # lock this device -> job.accepted
    python .tools/remote-job.py grade J042 --as 3.0.0_SA_CVO --verdict PASS|FAIL --record PATH   # the reviewer's grade
    python .tools/remote-job.py complete J042 --summary TEXT [--deployed] [--evidence TEXT] [--attempt N]
    python .tools/remote-job.py fail J042 --reason TEXT                    # job.failed, lock cleared
    python .tools/remote-job.py close J042                                 # lock cleared (after the bus CLOSE + reap)
    python .tools/remote-job.py show J042 --json '<REMOTE-JOB-JSON line>' | --from-file PATH   # brief -> a file

Every sending subcommand takes --dry-run (print the envelope, send nothing, touch no lock). Each event id is fixed
per act (bid-J042-<device>, accept-J042, complete-J042-<attempt>), so a re-run is a no-op at LDO-001; fail carries
its time. One ASCII line per act; nothing secret is printed.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
LOCK = os.path.join(HERE, ".remote-job.json")   # gitignored: this device's open job, if any
LDO_RUNTIME = os.path.join(ROOT, "infra", "aws", "terraform", "modules", "ldo", "runtime")
LDO_ID = "LDO-001"
REGION = "us-east-1"
def device_names() -> tuple:
    """The boxes in the device register org/devices/DEVICES.json (NFRA_CTLPLN FWD-2), read through lib/devices.py.
    No device list is kept in this file: a box added to the register can bid with no edit here."""
    # Loaded by FILE PATH: .tools/lib is a package too, and with .tools first on sys.path `from lib import` finds it.
    import importlib.util
    spec = importlib.util.spec_from_file_location("opal_devices", os.path.join(ROOT, "lib", "devices.py"))
    devices = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(devices)
    return tuple(devices.names())
JOB_RE = re.compile(r"^J\d{3}$")
COO_RE = re.compile(r"^2\.0\.0_SA_COO~[A-Za-z0-9_]+$")
REVIEWER_RE = re.compile(r"^3\.0\.0_SA_CVO(~[A-Za-z0-9_]+)?$")
LIVE_SECONDS = 120   # the estate reads a seat as live when it was seen within this many seconds
LIVENESS = os.path.join(ROOT, "org", "mcp", "liveness.json")   # per box, gitignored; OPAL_LIVENESS_FILE overrides
JSON_PREFIX = "REMOTE-JOB-JSON"


def now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def out(line: str) -> None:
    print(line.encode("ascii", "replace").decode("ascii"), flush=True)


def job_id(value: str) -> str:
    j = (value or "").strip().lstrip("#").upper()
    if not JOB_RE.match(j):
        raise SystemExit("ERROR: %r is not a job id (J plus three digits, e.g. J042)" % value)
    return j


# -- which machine is this: the agent bus's own resolver, never a second copy of its rule ----------------------------
def parse_device(output: str, rc: int) -> str:
    """`agentbus-sqs.sh device` prints `device: <a register device | UNKNOWN>`. Anything but a device in the register
    is refused: a bid under the wrong device name would win jobs for the other machine."""
    m = re.search(r"^device:\s*(\S+)", output or "", re.M)
    dev = m.group(1) if m else ""
    known = device_names()
    if rc != 0 or dev not in known:
        raise SystemExit("ERROR: this device is UNRESOLVED (%r, rc=%s); set AGENTBUS_DEVICE to one of %s -- "
                         "refusing to guess" % (dev or "no answer", rc, "|".join(known)))
    return dev


def device_name() -> str:
    sys.path.insert(0, HERE)
    import git_bash_resolver  # noqa: E402 -- the estate's canonical Git Bash, never a bare `bash`
    r = subprocess.run(git_bash_resolver.bash_argv(os.path.join(HERE, "agentbus-sqs.sh"), "device"),
                       capture_output=True, text=True, timeout=60)
    return parse_device(r.stdout, r.returncode)


def measure() -> tuple:
    """(cpu_pct, mem_pct) as the contract fixes them."""
    import psutil
    return float(psutil.cpu_percent(interval=1)), float(psutil.virtual_memory().percent)


# -- the lock: this device's open job ---------------------------------------------------------------------------------
def read_lock(path: str = None):
    path = path or LOCK
    try:
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
        return doc if isinstance(doc, dict) and doc.get("job") else None
    except FileNotFoundError:
        return None


def write_lock(doc: dict, path: str = None) -> None:
    with open(path or LOCK, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(doc, fh, indent=1, sort_keys=True)


def clear_lock(job: str, path: str = None) -> bool:
    """Remove the lock if it is this job's. False when there was nothing of this job's to clear."""
    path = path or LOCK
    lock = read_lock(path)
    if not lock or lock.get("job") != job:
        return False
    os.remove(path)
    return True


def live_reviewer(path: str = None, now: float = None):
    """The reviewer seat (3.0.0_SA_CVO, with or without ~lane) seen most recently within LIVE_SECONDS on this box
    according to the liveness file (serial -> entry with last_seen_epoch / last_seen), or None."""
    path = path or os.environ.get("OPAL_LIVENESS_FILE") or LIVENESS
    now = time.time() if now is None else now
    try:
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
    except (OSError, ValueError):
        return None
    best, best_seen = None, None
    for serial, entry in (doc.items() if isinstance(doc, dict) else ()):
        if not REVIEWER_RE.match(str(serial)) or not isinstance(entry, dict):
            continue
        seen = entry.get("last_seen_epoch")
        if not isinstance(seen, (int, float)):
            try:
                seen = datetime.datetime.fromisoformat(str(entry.get("last_seen"))).timestamp()
            except ValueError:
                continue
        if 0 <= now - seen <= LIVE_SECONDS and (best_seen is None or seen > best_seen):
            best, best_seen = serial, seen
    return best


def sha256_file(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


# -- sending to LDO-001 ------------------------------------------------------------------------------------------------
def make_runtime():
    """An LDO runtime aimed at LDO-001's mailbox. Queue and table names are NAMES.json's (name() output)."""
    import boto3
    sys.path.insert(0, LDO_RUNTIME)
    sys.path.insert(0, ROOT)
    import ldo  # noqa: E402
    from data.transcripts.scripts import teams_chat  # noqa: E402 -- NAMES.json lives beside LDO-001's tenant
    with open(os.path.join(os.path.dirname(teams_chat.__file__), "NAMES.json"), encoding="utf-8") as fh:
        names = json.load(fh)
    sqs = boto3.client("sqs", region_name=REGION)
    url = sqs.get_queue_url(QueueName=names["queue"]["name"] + ".fifo")["QueueUrl"]
    arn = sqs.get_queue_attributes(QueueUrl=url, AttributeNames=["QueueArn"])["Attributes"]["QueueArn"]
    return ldo.Runtime(env={"LDO_ID": LDO_ID, "LDO_TABLE": names["table"]["name"], "LDO_MAILBOX_URL": url,
                            "LDO_MAILBOX_ARN": arn}, sqs=sqs)


def emit(job: str, kind: str, payload: dict, event_id: str, dry_run: bool) -> dict:
    envelope = {"object_id": "job:%s" % job, "kind": kind, "payload": payload, "event_id": event_id}
    if dry_run:
        out("DRY-RUN: would send %s" % json.dumps(envelope, sort_keys=True))
        return envelope
    make_runtime().send(envelope["object_id"], kind, payload, event_id=event_id)
    out("OK: sent %s to %s (%s), event %s" % (kind, envelope["object_id"], LDO_ID, event_id))
    return envelope


def who(args) -> tuple:
    return device_name(), (args.serial or os.environ.get("OPAL_AGENT_SERIAL") or "0.0.0_AB_MSTR")


# -- subcommands ------------------------------------------------------------------------------------------------------
def cmd_bid(args) -> int:
    j = job_id(args.job)
    dev, serial = who(args)
    lock = read_lock()
    reviewer = live_reviewer()
    cpu, mem = measure()
    payload = {"device": dev, "serial": serial, "available": lock is None and reviewer is not None,
               "reviewer": reviewer, "cpu_pct": cpu, "mem_pct": mem, "at": now_iso()}
    if lock is not None:
        payload["unavailable_reason"] = "job_open"
        out("WARN: this device already runs %s, so the bid says available=false" % lock.get("job"))
    elif reviewer is None:
        payload["unavailable_reason"] = "no_reviewer"
        out("WARN: no reviewer seat (3.0.0_SA_CVO) is live on this device, so the bid says available=false")
    emit(j, "job.bid", payload, "bid-%s-%s" % (j, dev), args.dry_run)
    return 0


def cmd_accept(args) -> int:
    j = job_id(args.job)
    if not COO_RE.match(args.coo or ""):
        out("ERROR: --coo %r is not a 2.0.0_SA_COO~<lane> serial; %s not accepted" % (args.coo, j))
        return 2
    brief = args.brief_file
    if not brief or not os.path.isfile(brief) or os.path.getsize(brief) == 0:
        out("ERROR: --brief-file %r is not an existing, non-empty file; %s not accepted" % (brief, j))
        return 2
    dev, serial = who(args)
    lock = read_lock()
    if lock is not None and lock.get("job") != j:
        out("ERROR: this device already runs %s; %s not accepted" % (lock.get("job"), j))
        return 2
    digest = sha256_file(brief)
    payload = {"device": dev, "serial": serial, "coo": args.coo, "brief_sha256": digest}
    if args.dry_run:
        emit(j, "job.accepted", payload, "accept-%s" % j, True)
        return 0
    write_lock({"job": j, "coo": args.coo, "accepted_at": now_iso(), "device": dev, "serial": serial,
                "brief": brief, "brief_sha256": digest})
    emit(j, "job.accepted", payload, "accept-%s" % j, False)
    return 0


def cmd_grade(args) -> int:
    """The reviewer's grade, written into the lock. Sends nothing."""
    j = job_id(args.job)
    reviewer = args.as_serial
    lock = read_lock()
    env_serial = os.environ.get("OPAL_AGENT_SERIAL")
    record = args.record
    why = None
    if not REVIEWER_RE.match(reviewer or ""):
        why = "%r is not a reviewer serial (3.0.0_SA_CVO, with or without ~lane)" % reviewer
    elif not lock or lock.get("job") != j:
        why = "this device's lock does not name %s" % j
    elif reviewer == lock.get("coo"):
        why = "the seat that did the work cannot grade it"
    elif env_serial and env_serial != reviewer:
        why = "OPAL_AGENT_SERIAL is %r, not %r" % (env_serial, reviewer)
    elif not record or not (os.path.isfile(record) or os.path.isfile(os.path.join(ROOT, record))):
        why = "--record %r is not an existing file" % record
    if why:
        out("ERROR: %s not graded: %s" % (j, why))
        return 2
    lock["grade"] = {"by": reviewer, "verdict": args.verdict, "record": record, "at": now_iso()}
    write_lock(lock)
    out("OK: %s graded %s by %s" % (j, args.verdict, reviewer))
    return 0


def cmd_complete(args) -> int:
    j = job_id(args.job)
    lock = read_lock()
    grade = (lock or {}).get("grade") or {}
    if (not lock or lock.get("job") != j or grade.get("verdict") != "PASS" or not grade.get("by")
            or grade.get("by") == lock.get("coo")):
        out("ERROR: %s has no passing reviewer grade on this box; nothing sent" % j)
        return 2
    dev, serial = who(args)
    payload = {"device": dev, "serial": serial, "summary": args.summary, "deployed": bool(args.deployed),
               "evidence": args.evidence or "", "coo": lock.get("coo"), "grade": grade}
    emit(j, "job.complete", payload, "complete-%s-%d" % (j, args.attempt), args.dry_run)
    return 0


def cmd_fail(args) -> int:
    j = job_id(args.job)
    dev, serial = who(args)
    payload = {"device": dev, "serial": serial, "reason": args.reason}
    emit(j, "job.failed", payload, "fail-%s-%s" % (j, now_iso()), args.dry_run)
    if not args.dry_run and clear_lock(j):
        out("OK: lock for %s cleared" % j)
    return 0


def cmd_close(args) -> int:
    j = job_id(args.job)
    out("OK: lock for %s cleared" % j if clear_lock(j) else "OK: no open lock for %s on this device" % j)
    return 0


def find_job_json(text: str, job: str):
    """The REMOTE-JOB-JSON document for `job` in a listener's captured text (the last one wins), or a bare JSON."""
    found = None
    for line in (text or "").splitlines():
        i = line.find(JSON_PREFIX)
        raw = line[i + len(JSON_PREFIX):].strip() if i >= 0 else line.strip()
        if not raw.startswith("{"):
            continue
        try:
            doc = json.loads(raw)
        except ValueError:
            continue
        if isinstance(doc, dict) and doc.get("job") == job:
            found = doc
    return found


def cmd_show(args) -> int:
    j = job_id(args.job)
    if args.from_file:
        with open(args.from_file, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    elif args.json:
        text = args.json
    else:
        out("ERROR: give --json '<REMOTE-JOB-JSON line>' or --from-file <listener output>")
        return 2
    doc = find_job_json(text, j)
    if not doc or not doc.get("brief"):
        out("ERROR: no REMOTE-JOB-JSON with a brief for %s in the input" % j)
        return 2
    path = os.path.join(args.out_dir or tempfile.gettempdir(), "remote-job-%s-brief.md" % j)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("# Remote job %s\n\n" % j)
        fh.write("- Requester: %s\n- Chat: %s\n- Offered: %s\n\n" % (doc.get("requester") or "unknown",
                                                                  doc.get("chat_title") or "unknown",
                                                                  doc.get("sent_at") or "unknown"))
        fh.write(str(doc["brief"]).rstrip() + "\n")
    out("OK: brief for %s written to %s" % (j, path))
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    def add(name, fn, send=True):
        p = sub.add_parser(name)
        p.add_argument("job")
        p.add_argument("--serial", default=None, help="this MSTR's full serial (default $OPAL_AGENT_SERIAL, then 0.0.0_AB_MSTR)")
        if send:
            p.add_argument("--dry-run", action="store_true", help="print the envelope; send nothing; touch no lock")
        p.set_defaults(fn=fn)
        return p

    add("bid", cmd_bid)
    p = add("accept", cmd_accept)
    p.add_argument("--coo", required=True, help="the 2.0.0_SA_COO~<N> serial spawned for the job")
    p.add_argument("--brief-file", default=None, help="REQUIRED: the existing, non-empty file `show` wrote (kept in the lock)")
    p = add("grade", cmd_grade, send=False)
    p.add_argument("--as", dest="as_serial", required=True, help="the reviewer's serial (3.0.0_SA_CVO[~lane])")
    p.add_argument("--verdict", required=True, choices=("PASS", "FAIL"))
    p.add_argument("--record", required=True, help="repo path of the reviewer's grade record (must exist)")
    p = add("complete", cmd_complete)
    p.add_argument("--summary", required=True)
    p.add_argument("--deployed", action="store_true")
    p.add_argument("--evidence", default="")
    p.add_argument("--attempt", type=int, default=1, help="1 for the first completion, 2 after a re-open, ...")
    p = add("fail", cmd_fail)
    p.add_argument("--reason", required=True)
    add("close", cmd_close, send=False)
    p = add("show", cmd_show, send=False)
    p.add_argument("--json", default=None)
    p.add_argument("--from-file", default=None)
    p.add_argument("--out-dir", default=None)
    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
