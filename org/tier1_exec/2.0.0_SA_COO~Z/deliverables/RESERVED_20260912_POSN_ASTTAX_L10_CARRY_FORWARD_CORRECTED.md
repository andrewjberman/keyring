# RESERVED CARD, CORRECTED: POSN_ASTTAX round 3 at the LD-0521 L10 wall

**Seat:** `2.0.0_SA_COO~Z` · **For:** Andrew, via `0.0.0_AB_MSTR~Z` · **2026-09-12T21:3xZ**
**Supersedes the SCOPE of broker msg 21817** (same seat, ~2026-09-12T00:2xZ). That card is not
withdrawn; it named too little, and a card that understates the set Andrew is ruling on is worse
than no card, because the refuser will count the members the card never mentioned.

## What 21817 got wrong, measured

21817 asked whether round 3 may close **"at 5 of 7 terminal with `s-6`/`s-7` carried forward."**
Both numbers are wrong and the set is wrong.

```
MEASURED AT HEAD, 2026-09-12T21:33Z, org/missions/D4/POSN/POSN_ASTTAX/task-orders/
  DENOMINATOR: 15 task orders          (21817 said 7)
  terminal:    11
  OPEN:         4                      (21817 named 2)
     TO-S2-1  retag-the-hedge-bucket            staged   <- ROUND 2, never named by 21817
     TO-S3-1  is-hedge-reconciliation           staged   <- ROUND 2, never named by 21817
     TO-T6-1  the-retag-with-a-criterion...     staged
     TO-T7-1  is-hedge-reconciliation           staged
```

`3.0.0_SA_CVO~Z` independently reached the same set and said so in the verdict relayed at msg 21941:
a new named exception must state **all four**, *"not only T6/T7"*, and *"merely renaming or
prematurely terminating them is not a resolution."* `1.0.0_SA_CTO~Z` reports its own card named two
of four and is correcting it at Andrew's terminal. **This card is the third carrier of that same
two-of-four error and it is this seat's own.**

## Why the two round-2 orders are still open, and why the old exception cannot be reused

`TO-S2-1` and `TO-S3-1` have been open since round 2. They were left open deliberately, under the
**single named exception Andrew granted for round 2 only** (call 1 YES, relayed by `1.0.0_SA_CTO`
msg 21533). That exception is pinned in the gate itself and it is now **structurally unavailable**:

```
.tools/surprise-row-gate.py:827  _posn_round2_terminal_exception(...)
    if code != "POSN_ASTTAX" or not open_ids or total != 8:  return False
POSN total is now 15. The guard can never match again. Measured, not inferred.
```

So round 2's carry-forward did not retire those two orders; it stepped over them once. They are
back in the count, and they are two of the four.

## The wall itself, read at source rather than from the law's summary

```
.tools/surprise-row-gate.py:787  _open_tos_for_project(root, code, merging=False)
    git ls-files -- */task_orders/<CODE>.*.md
                     org/missions/D*/*/<CODE>/task-orders/*.md
    NO ROUND FILTER ANYWHERE -- the open count is PER PROJECT, never per round.
```

A new `REMEDIATION_v3` row (the L10 slug) is refused while any of the four is non-terminal, citing
LD-0521 / Andrew-direct 2026-09-03 @`716a9bc7ce` call 3: *"We do not route until the job is over."*

## THE CONSEQUENCE THAT IS NOT OBVIOUS, AND IT IS WHY THIS CARD IS URGENT RATHER THAN TIDY

Because the count is per PROJECT, **cutting round 4 before round 3 slugs would deadlock round 3's
L10 until round 4 fully drains.** Rule 27 banks this, measured on `AMGT_RESAPP` on 2026-09-11 by the
seat that did it: round 6 was cut straight off the L9 adjudication, the open count never reached
zero, and `3.0.0_SA_CVO~Z` — already correctly gated — silently acquired a different blocker. The
cost lands on another seat and is invisible to the one that caused it.

POSN's round-4 inputs are in hand as of msg 21941. **This seat is NOT cutting them, and the reason
is this card.** Round 4 would add a DEPLOY cell whose underlying act still needs a never-widen
sign-off that does not exist — so round 3's slug would sit behind a gate nobody can currently open.

## What is asked of Andrew, stated at the grain the refuser measures

**One question:** may `POSN_ASTTAX` route its round-3 L10 slug with these **four** orders
non-terminal — `TO-S2-1`, `TO-S3-1`, `TO-T6-1`, `TO-T7-1`, of 15 — carried forward with their
measured blockers named?

The measured blockers, so the question is not asked in the abstract:

| order | why it is not terminal |
|---|---|
| `TO-T6-1` | the retag is **NO-GO** (`AT3-s-5`, three instruments, three seats). Row `Z-S8`: its criterion `T6-AC4` reads an artifact production never writes, so it can return neither PASS nor FAIL. Ruling 21813: not re-pinned, not spawned, not re-cut. |
| `TO-T7-1` | depends on `AT3-s-6`, which is held by that NO-GO. Never spawned. |
| `TO-S2-1` | round-2 carry-forward; the retag it performs is the same act `TO-T6-1`'s NO-GO blocks. |
| `TO-S3-1` | round-2 carry-forward; reconciliation over the retagged bucket, so downstream of the same NO-GO. |

⛔ **Every one of the four is downstream of the same measured fact**: the deployed generator is
`LastModified 2026-08-18T18:34:43Z`, every repair is COMMITTED-NOT-DEPLOYED, and no cell in the cut
deploys. They are not four independent stalls; they are one gap seen four times.

## What this card does NOT ask, so nothing is read wider

- It does **not** ask for the `# surprise-row-override:` escape on the L10 precondition. That is a
  NEVER-class line (LD-0521, Andrew's word) and this seat will not use it under any answer.
- It does **not** ask for any order to be flipped terminal to release the gate.
- It does **not** ask for the deploy authorization, the portal freeze scope, or the LIMB 6 widening.
  Those are separate and stay where they are.
- It does **not** re-litigate the CVO's re-classes in 21941; those are about AUTHORITY and they are
  accepted. This card is about ORDER — slug before recut — which is the issuer's own call.

## Owner and unpark condition

```
OWNER    2.0.0_SA_COO~Z (this seat)
UNPARKS  Andrew's answer on the four-order question, relayed verbatim by 0.0.0_AB_MSTR~Z
         -- OR the four orders reaching terminal legitimately, which needs the deploy act
CARRIER  this file (21817 was a broker message with no durable carrier -- the silent-hole shape
         CLAUDE.md names, and it sat ~20 hours across a fabric-wide stall proving the point)
```

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QrY42PDSgAGLLtWHy1MNJy
