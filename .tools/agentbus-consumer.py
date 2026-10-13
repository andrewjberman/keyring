#!/usr/bin/env python3
"""agentbus-consumer.py -- long-lived SQS consumer for the agent bus (Port 2).

NO-SPAWN CONSUMER (Andrew cleanup 2026-07-30, MSTR low-level audit): the aws-CLI
watch loop in agentbus-sqs.sh launched a FULL python interpreter per 20s long-poll
(~4,320/day/device, each ~1-2s CPU plus the heaviest per-event EDR import scans on
the box). This daemon holds ONE process and ONE boto3 client for the session.

CONTRACT -- identical to the shell loop it replaces (agentbus-sqs.sh `watch)`):
  - one stdout line per message:  [AGENTBUS -> <device>] [id <MessageId>] <Body>
    (the Monitor tool turns each line into a chat notification; the MessageId is
    emitted because Rule 22b's only delivery oracle is an ack NAMING it)
  - EMIT THEN DELETE, delete gated on a successful emit -- a death between the two
    redelivers a DUPLICATE after the visibility timeout, never a loss
  - receive errors are LOUD and never rendered as an empty queue
  - the PID lockfile written by the bash wrapper is removed on clean exit ONLY if
    it still holds the wrapper's MSYS pid (passed via --lock-pid; the wrapper
    exec()s into this process, so that pid IS this process on the MSYS side and
    `kill -0` liveness keeps resolving; a crash leaves the lock to self-clear)

Run only via `agentbus-sqs.sh watch` under the Monitor tool -- the wrapper does
device measurement, wrong-device refusal, and single-consumer locking BEFORE the
exec, and those guards must not be bypassed.
"""
from __future__ import annotations

import argparse
import atexit
import datetime
import json
import os
import pathlib
import sys
import time

_ROOT = pathlib.Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# STDOUT/STDERR MUST NOT BE ABLE TO KILL THIS PROCESS. (measured 2026-08-13)
#
# On Windows, python's stdout defaults to the ANSI codepage (cp1252). The emit at
# :83 prints the RAW MESSAGE BODY, so a single non-ASCII character in a peer's
# message -- U+26A0 (warning sign) was the live one -- raised UnicodeEncodeError,
# KILLED THE CONSUMER, and left the message in flight because the emit precedes
# the delete.
#
# >> AND THE EMIT-THEN-DELETE CONTRACT TURNS THAT INTO A POISON PILL, NOT A BLIP. <<
# The docstring above is right that a death between emit and delete redelivers
# rather than loses. But the redelivered DUPLICATE CARRIES THE SAME BYTES, so it
# kills the next consumer too, forever. The safety property becomes the trap: the
# queue head is un-consumable and every re-arm dies on it within one poll.
#
# MEASURED COST: two deafness windows in one session (3h08m and ~29m) on the ONLY
# live cross-device channel, while TaskOutput reported the Monitor "running" the
# whole time -- the consumer is a separate process from the wrapper the harness
# tracks, so its death is invisible to the check the /agentbus skill prescribes.
#
# CLAUDE.md already bans the INPUT ("No emojis (no non-ASCII) ... breaks
# CloudWatch/charmap") and we still shipped it into bus bodies. A rule that needs
# every sender to remember is not a control; THIS is the control. Senders should
# still keep bodies ASCII -- that is the rule -- but a peer that violates it must
# degrade one character, never take down the channel.
# ---------------------------------------------------------------------------
for _stream in ("stdout", "stderr"):
    try:  # py3.7+; never let the guard itself raise
        getattr(sys, _stream).reconfigure(encoding="utf-8", errors="backslashreplace")
    except Exception:  # pragma: no cover - older/odd interpreters keep prior behavior
        pass


# ---------------------------------------------------------------------------
# THE SENDER CHECK (NFRA_CTLPLN TO-CT-b-3, AMENDMENT 2; same rule as `recv` in agentbus-sqs.sh).
# The sender's TAILNET NAME is the message attribute `from_tailnet`; the register (org/devices/DEVICES.json,
# read through lib/devices.py -- the one reader agentbus-sqs.sh's _tailnet also uses) says which names are held.
#   held name      -> deliver
#   no stamp       -> deliver with one line  WARN agentbus unstamped sender=<serial>  (old-script boxes; strict later)
#   unheld name    -> REFUSED: the whole message is written to <refused dir>/<UTC stamp>_<message id>.json, one line
#                     REFUSED agentbus sender_tailnet=<name> reason=<why> record=<path>  is printed, and the message
#                     is DELETED so it cannot block the one-group FIFO queue. A record that cannot be written leaves
#                     the message on the queue (recorded, never silently dropped).
# ---------------------------------------------------------------------------
REFUSED_REASON = "not-held-by-the-device-register"


def held_tailnet_names() -> set:
    """Every tailnet name the register holds; raises devices.RegisterError when it cannot be read (fail closed)."""
    sys.path.insert(0, str(_ROOT / "lib"))
    import devices  # noqa: PLC0415 -- deferred, the register path is read per call (OPAL_DEVICE_REGISTER honoured)

    return set(devices.held_tailnet_names(devices.load()))


def refused_dir() -> pathlib.Path:
    return pathlib.Path(os.environ.get("AGENTBUS_REFUSED_DIR") or (_ROOT / "org" / "mcp" / "inbox" / "_agentbus_refused"))


def classify(msg: dict, held: set) -> str:
    stamp = ((msg.get("MessageAttributes") or {}).get("from_tailnet") or {}).get("StringValue") or ""
    if not stamp:
        return "unstamped"
    return "deliver" if stamp in held else "refused"


def refuse(sqs, queue_url: str, msg: dict) -> None:
    """Record the whole message, print the REFUSED line, then delete it from the queue."""
    mid = msg.get("MessageId", "?")
    tn = msg["MessageAttributes"]["from_tailnet"]["StringValue"]
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rec = refused_dir() / f"{now}_{mid}.json"
    try:
        rec.parent.mkdir(parents=True, exist_ok=True)
        rec.write_text(json.dumps({"refused_at": now, "sender_tailnet": tn, "reason": REFUSED_REASON, "message": msg},
                                  indent=2), encoding="utf-8")
    except OSError as exc:
        print(f"[agentbus] REFUSED [id {mid}] sender tailnet name [{tn}] but the record could not be written "
              f"({type(exc).__name__}) -- NOT deleted; it remains on the queue.", flush=True)
        return
    print(f"REFUSED agentbus sender_tailnet={tn} reason={REFUSED_REASON} record={rec}", flush=True)
    try:
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg["ReceiptHandle"])
    except Exception as exc:  # noqa: BLE001
        print(f"[agentbus] WARN: the refused message {mid} was recorded but its delete FAILED "
              f"({type(exc).__name__}); it will redeliver and be refused again.", flush=True)


def deliverable(sqs, queue_url: str, messages: list) -> list:
    """Apply the sender check to one received batch; return the messages to emit (refused ones are handled here)."""
    try:
        held = held_tailnet_names()
    except Exception as exc:  # noqa: BLE001 -- register unreadable: cannot judge, so withhold EVERYTHING, delete nothing
        print(f"[agentbus] WITHHELD {len(messages)} message(s): the device register's tailnet names could not be read "
              f"({type(exc).__name__}) -- NOT delivered, NOT deleted; they remain on the queue.", flush=True)
        return []
    out = []
    for msg in messages:
        kind = classify(msg, held)
        if kind == "refused":
            refuse(sqs, queue_url, msg)
            continue
        if kind == "unstamped":
            serial = ((msg.get("MessageAttributes") or {}).get("from") or {}).get("StringValue") or "unknown"
            print(f"WARN agentbus unstamped sender={serial}", flush=True)
        out.append(msg)
    return out


# ---------------------------------------------------------------------------
# OWNER TIE (P1 process GC, 4.0.0_SA_CRO~B). The harness stops a Monitor by killing the TOP of its bash chain
# (claude.exe -> Git\bin\bash.exe shim -> usr\bin\bash -c -> exec'd bash -> exec'd python). Measured: killing that
# shim leaves every process below it alive, so this consumer kept the lock and refused every re-arm (rc 3) until its
# 1700 s cap. Inside the script $PPID is 1 (the shim is not an MSYS process), so the owner is found on the WINDOWS
# parent chain: OWNER = the topmost consecutive bash.exe/sh.exe ancestor, SESSION = that process's parent.
# One handle per owner is opened at start and held (a held handle defeats PID reuse); each loop pass polls it.
# FAIL OPEN: no owner given, a handle that cannot be opened, or one already signalled -> cap only, said on stderr.
# ---------------------------------------------------------------------------
_SYNCHRONIZE = 0x00100000
_PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
_WAIT_OBJECT_0 = 0
_BASH_NAMES = {"bash.exe", "sh.exe"}


def _windows_parents() -> dict:
    """{pid: (parent_pid, exe_name)} from one Toolhelp snapshot (Windows only)."""
    import ctypes  # noqa: PLC0415
    from ctypes import wintypes  # noqa: PLC0415

    class _PE(ctypes.Structure):
        _fields_ = [("dwSize", wintypes.DWORD), ("cntUsage", wintypes.DWORD), ("th32ProcessID", wintypes.DWORD),
                    ("th32DefaultHeapID", ctypes.c_void_p), ("th32ModuleID", wintypes.DWORD),
                    ("cntThreads", wintypes.DWORD), ("th32ParentProcessID", wintypes.DWORD),
                    ("pcPriClassBase", ctypes.c_long), ("dwFlags", wintypes.DWORD),
                    ("szExeFile", ctypes.c_char * 260)]

    k32 = ctypes.WinDLL("kernel32", use_last_error=True)
    k32.CreateToolhelp32Snapshot.restype = wintypes.HANDLE
    snap = k32.CreateToolhelp32Snapshot(0x2, 0)  # TH32CS_SNAPPROCESS
    if not snap or snap == wintypes.HANDLE(-1).value:
        return {}
    out = {}
    try:
        ent = _PE()
        ent.dwSize = ctypes.sizeof(_PE)
        ok = k32.Process32First(wintypes.HANDLE(snap), ctypes.byref(ent))
        while ok:
            out[int(ent.th32ProcessID)] = (int(ent.th32ParentProcessID), ent.szExeFile.decode("ascii", "replace"))
            ok = k32.Process32Next(wintypes.HANDLE(snap), ctypes.byref(ent))
    finally:
        k32.CloseHandle(wintypes.HANDLE(snap))
    return out


def resolve_owners(start_winpid: int) -> list:
    """[owner, session]: owner = topmost consecutive bash/sh at or above start; session = its parent (if live)."""
    procs = _windows_parents()
    if start_winpid not in procs:
        return []
    owner = start_winpid
    seen = {owner}
    while True:
        parent = procs[owner][0]
        if parent in seen or parent not in procs or procs[parent][1].lower() not in _BASH_NAMES:
            break
        owner = parent
        seen.add(owner)
    session = procs[owner][0]
    return [owner] + ([session] if session in procs and session not in seen else [])


def open_owner_handles(pids: list) -> list:
    """[(pid, handle)] for each live owner; fail open (empty list) with one stderr line per refusal."""
    if not pids:
        print("agentbus-consumer: owner-tie OFF (no --owner-winpid) -- exits only at its cap.", file=sys.stderr,
              flush=True)
        return []
    if os.name != "nt":
        print("agentbus-consumer: owner-tie OFF (not Windows) -- exits only at its cap.", file=sys.stderr, flush=True)
        return []
    import ctypes  # noqa: PLC0415
    from ctypes import wintypes  # noqa: PLC0415

    k32 = ctypes.WinDLL("kernel32", use_last_error=True)
    k32.OpenProcess.restype = wintypes.HANDLE
    k32.WaitForSingleObject.restype = wintypes.DWORD
    held = []
    for pid in pids:
        if pid <= 0:
            print(f"agentbus-consumer: owner-tie OFF for pid {pid} (not a pid) -- ignored.", file=sys.stderr,
                  flush=True)
            continue
        h = k32.OpenProcess(_SYNCHRONIZE | _PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
        if not h:
            print(f"agentbus-consumer: owner-tie OFF for winpid {pid} (OpenProcess failed, "
                  f"err {ctypes.get_last_error()}) -- ignored.", file=sys.stderr, flush=True)
            continue
        if k32.WaitForSingleObject(wintypes.HANDLE(h), 0) == _WAIT_OBJECT_0:
            print(f"agentbus-consumer: owner-tie OFF for winpid {pid} (already exited at start) -- ignored.",
                  file=sys.stderr, flush=True)
            k32.CloseHandle(wintypes.HANDLE(h))
            continue
        held.append((pid, h))
    if held:
        print(f"agentbus-consumer: owner-tie ON -- exits when winpid {', '.join(str(p) for p, _ in held)} exits.",
              file=sys.stderr, flush=True)
    else:
        print("agentbus-consumer: owner-tie OFF (no owner handle held) -- exits only at its cap.", file=sys.stderr,
              flush=True)
    return held


def owner_gone(held: list):
    """The pid of the first owner whose handle is signalled (it exited), else None."""
    if not held:
        return None
    import ctypes  # noqa: PLC0415
    from ctypes import wintypes  # noqa: PLC0415

    k32 = ctypes.WinDLL("kernel32", use_last_error=True)
    k32.WaitForSingleObject.restype = wintypes.DWORD
    for pid, h in held:
        if k32.WaitForSingleObject(wintypes.HANDLE(h), 0) == _WAIT_OBJECT_0:
            return pid
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--resolve-owners", type=int, default=0, metavar="WINPID",
                    help="print the owner and session Windows pids above WINPID, then exit (used by the wrapper)")
    ap.add_argument("--queue-url", default="")
    ap.add_argument("--device", default="")
    ap.add_argument("--region", default="us-east-1")
    ap.add_argument("--lock", default="")
    ap.add_argument("--lock-pid", default="")
    ap.add_argument("--owner-winpid", type=int, action="append", default=[],
                    help="Windows pid whose exit ends this consumer (repeatable; absent or 0 = cap only)")
    args = ap.parse_args()

    if args.resolve_owners:
        try:
            print(" ".join(str(p) for p in resolve_owners(args.resolve_owners)))
        except Exception as exc:  # noqa: BLE001 -- fail open: the wrapper passes no owner
            print(f"agentbus-consumer: owner resolve failed ({type(exc).__name__})", file=sys.stderr)
        return 0
    if not args.queue_url or not args.device:
        ap.error("--queue-url and --device are required")

    def _release_lock() -> None:
        if not args.lock:
            return
        try:
            with open(args.lock, "r", encoding="utf-8") as fh:
                mine = fh.read().strip() == str(args.lock_pid)
            if mine:
                os.remove(args.lock)
        except OSError:
            pass

    atexit.register(_release_lock)

    try:
        owners = open_owner_handles([p for p in args.owner_winpid if p is not None])
    except Exception as exc:  # noqa: BLE001 -- fail open
        print(f"agentbus-consumer: owner-tie OFF ({type(exc).__name__}) -- exits only at its cap.", file=sys.stderr,
              flush=True)
        owners = []

    import boto3  # deferred so a missing boto3 fails loud at start, not mid-loop
    from botocore.config import Config  # noqa: PLC0415

    # Bounded blocking: the owner is polled between calls, so a hung connect must not outlast the 20 s long-poll by
    # much. read_timeout stays above WaitTimeSeconds=20.
    sqs = boto3.client("sqs", region_name=args.region,
                       config=Config(connect_timeout=5, read_timeout=30,
                                     retries={"max_attempts": 2, "mode": "standard"}))
    print(f"agentbus-consumer: watching {args.device} inbound (long-poll 20s, "
          "single-process boto3). Emits one line per message; silent otherwise.",
          file=sys.stderr, flush=True)

    # SELF-EXPIRY (0.0.0_AB_MSTR~Z, 2026-09-30). The harness kills a Monitor at 30 min, but it kills the bash
    # WRAPPER: this exec'd native python survived as an orphan, kept the lock (every re-arm refused, rc=3), and
    # wrote to a pipe nobody read -- site Z was deaf until the orphan was killed by hand (measured: pid 2116617,
    # alive after its Monitor b0vrs6jhl expired). Exit just before the cap, like inbox-watch.sh (1770 s), so the
    # Monitor ends normally and atexit frees the lock. 1700 s, not 1770: the Monitor clock starts before the bash
    # preamble (device resolve, lock, AWS checks), and at 1770 the harness killed the first live run first.
    # AGENTBUS_MAX_SECONDS overrides; 0 disables.
    max_s = int(os.environ.get("AGENTBUS_MAX_SECONDS", "1700") or 0)
    t0 = time.monotonic()

    def _expired() -> bool:
        return bool(max_s) and time.monotonic() - t0 >= max_s

    def _check_owner() -> bool:
        gone = owner_gone(owners)
        if gone is None:
            return False
        try:
            print(f"agentbus-consumer: owner winpid {gone} exited -- releasing the lock and exiting.",
                  file=sys.stderr, flush=True)
        except Exception:  # noqa: BLE001
            pass
        return True

    def _sleep(seconds: float) -> bool:
        """Sleep in 1 s slices; True if the owner exited meanwhile."""
        end = time.monotonic() + seconds
        while time.monotonic() < end:
            if _check_owner():
                return True
            time.sleep(min(1.0, max(0.0, end - time.monotonic())))
        return _check_owner()

    while True:
        if _check_owner():
            return 0
        if _expired():
            try:
                print(f"[AGENTBUS-EXPIRED] consumer for {args.device} ended after {max_s}s (Monitors die at 30 min). "
                      "RE-ARM with ONE Monitor call: cd <workspace-root> && exec bash .tools/agentbus-sqs.sh watch",
                      flush=True)
            except Exception:  # noqa: BLE001
                pass
            return 0
        try:
            resp = sqs.receive_message(
                QueueUrl=args.queue_url,
                WaitTimeSeconds=20,
                MaxNumberOfMessages=10,
                MessageAttributeNames=["All"],
            )
        except Exception as exc:  # noqa: BLE001 -- LOUD, never an empty-queue render
            detail = f"{type(exc).__name__}: {exc}"[:160]
            print(f"[agentbus] RECV ERROR -- this is NOT an empty queue: {detail}",
                  flush=True)
            if _sleep(min(60, max(1, max_s - (time.monotonic() - t0))) if max_s else 60):
                return 0
            continue

        for msg in deliverable(sqs, args.queue_url, resp.get("Messages", [])):
            mid = msg.get("MessageId", "?")
            body = msg.get("Body", "")
            emitted = False
            try:
                print(f"[AGENTBUS -> {args.device}] [id {mid}] {body}", flush=True)
                emitted = True
            except Exception:  # noqa: BLE001 -- emit failed: DO NOT DELETE
                # With stdout re-encoded above, a failed emit means the READER IS GONE (the orphan case). Exit so the
                # lock frees and the undeleted message redelivers to a consumer someone is reading.
                return 4
            if emitted:
                try:
                    sqs.delete_message(QueueUrl=args.queue_url,
                                       ReceiptHandle=msg["ReceiptHandle"])
                except Exception as exc:  # noqa: BLE001
                    # Failed delete = future DUPLICATE, never a loss. Say so.
                    print(f"[agentbus] DELETE FAILED for id {mid} -- expect a "
                          f"redelivery duplicate: {type(exc).__name__}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
