#!/usr/bin/env python3
"""Canonical single-command outbound message for Codex seats.

    python org/mcp/codex-send.py --from-serial 4.0.0_SA_CRO~A \
        --to 2.0.0_SA_COO --subject "..." (--body "..." | --body-file f.md)

WHY THIS EXISTS (2026-08-26): told to "write to CRO~A to confirm readiness",
a Codex seat reclassified the ask as governance, proposed a broadcast, ran
comp-which twice through two shells, fell back to hand-written Python, and
still had not sent after a minute. There was no checked-in, single-command
send surface, so every routine message was an inference hole. This is that
surface. It performs, deterministically and in order:

  1. CALLER IDENTITY -- OPAL_AGENT_SERIAL must equal --from-serial. The env
     var is exported by ajb2 into every process of the seat's tree, so it is
     the one in-process signal of who is invoking. A mismatch REFUSES before
     anything is read or written (rc 2).
  2. SEAT PRESENCE -- the claimed serial must have a LIVE liveness entry on
     this box. Refuses a serial nobody registered (typo class), rc 2.
  3. DELIVERY -- exactly the broker library's own send_message: canonical
     nested inbox routing (base vs ~lane -- the flat form is inexpressible
     here because the library derives the path, never the caller), filesystem
     persistence, broker push to a live recipient, structured receipt.
  4. RECEIPT -- preserve the delivery result and sender-unverified warning,
     but explain the process/seat distinction instead of advising a second
     registration. rc 0 only if the library reports delivery
     (DELIVERED or QUEUED-for-dead-recipient), rc 1 on any REFUSED.

HONEST LIMIT, stated rather than papered over: the broker stamps sends from
an unregistered PROCESS "Sender-unverified" (the registered process is the
heartbeat, not this command). The stamp is TRUE -- this process is not the
registered one -- and steps 1-2 are the local identity control. Removing the
stamp would need a seat-token protocol in server.py; deliberately NOT built
tonight (build-ladder: the stamp is honest, the control is real). The CLI's
receipt explains this expected advisory; it does not upgrade sender trust.
"""

from __future__ import annotations

import argparse
import asyncio
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import server as comms  # noqa: E402  (the broker library; guarded send lives there)

SERIAL_RE = r"^[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9]+(~[A-Za-z0-9]+)?$"


def explain_receipt(receipt: str) -> str:
    """Clarify the advisory only after main's identity and presence checks."""
    return receipt.replace(
        " [sender unverified -- register_agent to send verified]",
        " [sender unverified: this one-shot process is unregistered; "
        "seat identity and fresh launcher liveness checked by codex-send. "
        "Expected advisory; do not register a second process]",
    )


def main(argv: list[str] | None = None) -> int:
    import re

    parser = argparse.ArgumentParser(
        description="Send one broker message as a Codex seat. No routing "
        "logic, no comp-which, no governance classification -- one send."
    )
    parser.add_argument("--from-serial", required=True)
    parser.add_argument("--to", required=True)
    parser.add_argument("--subject", required=True)
    body_group = parser.add_mutually_exclusive_group(required=True)
    body_group.add_argument("--body")
    body_group.add_argument("--body-file", type=Path)
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)

    for name, value in (("--from-serial", args.from_serial), ("--to", args.to)):
        if not re.fullmatch(SERIAL_RE, value):
            print(f"codex-send REFUSED: {name} {value!r} is not a serial "
                  f"(N.N.N_ROLE_Name[~Lane]).", file=sys.stderr)
            return 2

    # 1. caller identity: the seat's own exported serial must match the claim.
    caller = (os.environ.get("OPAL_AGENT_SERIAL") or "").strip()
    if caller != args.from_serial:
        print(
            f"codex-send REFUSED: OPAL_AGENT_SERIAL={caller!r} does not match "
            f"--from-serial {args.from_serial!r}. You may only send as the "
            f"seat you are. (A relay on another seat's behalf is a broker "
            f"identity_override act, deliberately not exposed here.)",
            file=sys.stderr,
        )
        return 2

    # 2. seat presence: the claimed serial is LIVE on this box.
    import json
    import time
    liveness_path = Path(__file__).resolve().parent / "liveness.json"
    try:
        liveness = json.loads(liveness_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        liveness = {}
    entry = liveness.get(args.from_serial) or {}
    age = time.time() - float(entry.get("last_seen_epoch") or 0)
    if not entry or age > 120:
        print(
            f"codex-send REFUSED: {args.from_serial} has no fresh liveness "
            f"entry (age={'ABSENT' if not entry else int(age)}s). Register the "
            f"seat (the ajb2 heartbeat does this) before sending.",
            file=sys.stderr,
        )
        return 2

    body = args.body if args.body is not None else args.body_file.read_text(
        encoding="utf-8"
    )

    # 3. delivery via the broker library's own guarded send.
    receipt = asyncio.run(
        comms.send_message(
            from_agent=args.from_serial,
            to_agent=args.to,
            subject=args.subject,
            body=body,
        )
    )
    print(explain_receipt(receipt))
    # 4. structured verdict: REFUSED anywhere in the receipt = failure.
    return 1 if "REFUSED" in receipt else 0


if __name__ == "__main__":
    raise SystemExit(main())
