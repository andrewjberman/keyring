#!/usr/bin/env python3
"""broker_arg_guards -- the two D0_T1_BROKER call-boundary guards (settled spec MSTR 64327;
CTO ruling 64300/64325; COO seating 64310 + amendment 64318; CRO's class correction).

CHECK 1 (the CLASS-level fix): STRICT KWARGS at the tool boundary. The measured failure class is
AN UNKNOWN KWARG SILENTLY DROPPED -- `send_message(message=...)` validated clean because pydantic
ignores extras, `body` defaulted to "", and the tool returned a normal DELIVERED receipt. Nine
empty sends across two seats in one night, including three by the seat that had already diagnosed
the mechanism ("knowing a failure mode by name does not immunize you against writing it" --
discipline is not an available remedy; the receipt observes the envelope, never the content).
Refuse-on-empty alone catches only the instance where the mis-named parameter happens to be the
one that empties the body; the NEXT mis-named parameter drops something else and still looks fine.

CHECK 2 (the instance backstop): refuse an EMPTY body. STRUCTURAL, ZERO THRESHOLDS ANYWHERE --
no byte floor, no character count, no subject-length qualifier (four seats amended those OUT in 25
minutes: a byte-floor detector is ANTI-CORRELATED with its own target, because content typed into
the subject makes the file BIGGER as the misuse gets WORSE -- 0.7.0 measured 2-of-4 caught with
the misses the structurally worse cases, and the one instance MSTR received was 349 B against a
~350 B floor: caught by ONE byte, which is a coin, not a detector). Body-empty is EXACTLY
detectable: every measured instance was 0 characters after whitespace, not "small".

This module is PURE (stdlib difflib only, no I/O, no state) so a harness can exercise every guard
without importing the broker. NOT A GOVERNED GATE (CTO 64300: a parameter-validation refusal
approves nothing, holds nothing, routes nothing to a human) and NOT under the alarm moratorium
(a synchronous refusal on a call emits nothing and watches nothing).

Author: 0.8.0_AE_CloudComp (COO seating 64310, D0_T1_BROKER window).
"""
from __future__ import annotations

import difflib

# Cross-tool parameter confusions, SEMANTIC not string-similar (difflib cannot suggest `body` for
# `message` -- their ratio is ~0.36 -- yet that exact confusion produced all nine measured empty
# sends: `message` is the parameter name of the OTHER messaging tool in this environment). The
# alias map is consulted first; difflib remains the fallback for genuine typos (bodyy, subjct).
_KNOWN_CONFUSIONS = {"message": "body", "content": "body", "text": "body",
                     "recipient": "to_agent", "recipients": "to_agents", "to": "to_agent",
                     "sender": "from_agent", "from": "from_agent", "title": "subject"}


def unknown_kwargs(supplied: dict, known: set) -> list:
    """The supplied argument names that no declared parameter matches (sorted, deterministic)."""
    return sorted(k for k in (supplied or {}) if k not in known)


def strict_kwargs_message(tool_name: str, unknown: list, known: list) -> str:
    """The refusal text: names every unknown parameter, with a did-you-mean per parameter."""
    parts = []
    for k in unknown:
        hint = _KNOWN_CONFUSIONS.get(k)
        if hint not in known:
            close = difflib.get_close_matches(k, list(known), n=1)
            hint = close[0] if close else None
        parts.append("unknown parameter: %s%s" % (k, (" -- did you mean %s?" % hint) if hint else ""))
    return ("CALL REFUSED (%s): %s. Declared parameters: %s. Nothing was executed and nothing was "
            "written -- an unknown parameter used to be SILENTLY DROPPED (measured 2026-08-21: nine "
            "empty sends with normal DELIVERED receipts), and a malformed call must fail loudly at "
            "the boundary, not succeed at delivering something else."
            % (tool_name, "; ".join(parts), ", ".join(sorted(known))))


def empty_envelope_refusal(subject: str, body: str) -> str | None:
    """CHECK 2, structural, no thresholds: an empty body refuses. Returns the refusal text or None.

    Both directions ruled (COO A4): body empty + subject NON-empty -> the measured defect (content
    typed into the subject; the recipient sees a subject promising content and a body saying
    nothing, which is byte-identical to 'no changes needed'). body empty + subject empty -> ALSO
    refused, with its own reason: an entirely empty envelope has no fabric use -- a liveness ping
    is the heartbeat's job, and every real message carries content; delivering one would put a
    zero-information artifact in an inbox wearing a DELIVERED receipt."""
    if (body or "").strip():
        return None
    if (subject or "").strip():
        return ("SEND REFUSED: body is EMPTY while subject is non-empty. At the recipient an empty "
                "body and a body saying 'no changes needed' are BYTE-IDENTICAL -- if your content "
                "is in the subject, move it to body=. Nothing was sent.")
    return ("SEND REFUSED: subject AND body are both empty. An empty envelope has no fabric use "
            "(a liveness signal is heartbeat's job). Nothing was sent.")
