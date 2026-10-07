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

    return {d["tailnet_name"] for d in devices.devices(devices.load()) if d.get("tailnet_name")}


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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--queue-url", required=True)
    ap.add_argument("--device", required=True)
    ap.add_argument("--region", default="us-east-1")
    ap.add_argument("--lock", default="")
    ap.add_argument("--lock-pid", default="")
    args = ap.parse_args()

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

    import boto3  # deferred so a missing boto3 fails loud at start, not mid-loop

    sqs = boto3.client("sqs", region_name=args.region)
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

    while True:
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
            time.sleep(min(60, max(1, max_s - (time.monotonic() - t0))) if max_s else 60)
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
