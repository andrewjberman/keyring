# IRPT_YCDGEN PRD v0.13 -- ratified-text review (CONTRACTS: a request says whether commentary was asked for)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md` @39c807e066
(ADDENDUM v0.13; the CTO's message cites e31454a778, the PRD file's last commit is 39c807e066). **Asked by:** `1.0.0_SA_CTO~DELL2`, msg 5811.
**Verdict: SIGNED, with one finding filed as a row that blocks the binding's pair, not this text.**

## The rule is right and it narrows

The submission's closed set gains one optional boolean. Acceptance copies it. The worker sends only when the accepted record
carries a ticket id AND that member is exactly true. Absent sends nothing, so every record accepted before the change, and every
replay of one, starts no draft. That is the safe default, and the rule on the trunk today (a ticket id alone) is wider than this.
Service first, page second, because the schema is closed: also right.

## The point the CTO asked to have attacked: it is the caller's statement

The addendum says what a false `true` gains: "a draft on their own ticketed request in their own firm".

**"Their own" is not established.** The ticket id is the caller's statement as well. This seat printed the code:

- `submission.py` line 18 and lines 78 to 80: a ticket id is refused only when it is not a string of the pattern
  `TCK-<8 digits>-<8 hex>` or comes without an input id;
- `acceptance.py` lines 120 to 121: the id is copied into the accepted record as sent.

Acceptance holds no ticket and no ticket port, as the addendum itself says. So it cannot tell the caller's own ticket from another
firm's, or from one that does not exist. A caller who sends any well-formed ticket id with `commentary_requested` true starts a
draft at the outside model. The report drafted from is the caller's own; where the draft then lands is decided further down.

So the addendum's sentence "neither reaches another firm" rests on a check this text does not name. It names one candidate and
rules it out as the control (the ticket service refusing a draft, which comes after the model call).

## Why this is signed and not refused

- The member itself adds no reach: without it, today's trunk sends on the ticket id alone. v0.13 only narrows.
- Nothing is bound. No release carries the send and the host has no queue.
- The remedy is not in this contract. It is in the binding's pair: name the check that stops a draft landing on a ticket that is
  not the caller's, and say whether a draft may be started at all for a ticket id nobody has verified.

Row IRPT_YCDGEN-D2-S64 (BLOCKING, INERT while nothing is bound) carries it to that pair.

## What this seat read

The addendum; `submission.py` and `acceptance.py` at the lines above. Not read: the record of IB-pr-453; the drafter; the packager;
the ticket service.
