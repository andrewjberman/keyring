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
import os
import sys
import time


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

    while True:
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
            time.sleep(60)
            continue

        for msg in resp.get("Messages", []):
            mid = msg.get("MessageId", "?")
            body = msg.get("Body", "")
            emitted = False
            try:
                print(f"[AGENTBUS -> {args.device}] [id {mid}] {body}", flush=True)
                emitted = True
            except Exception:  # noqa: BLE001 -- emit failed: DO NOT DELETE
                pass
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
