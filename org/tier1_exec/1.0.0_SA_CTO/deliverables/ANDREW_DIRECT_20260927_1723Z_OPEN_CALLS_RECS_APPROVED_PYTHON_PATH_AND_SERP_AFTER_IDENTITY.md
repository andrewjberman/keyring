# ANDREW-DIRECT 2026-09-27 ~17:2xZ -- open-calls recs approved: Python PATH fix; serp/social feeds after identity

**Channel:** the `1.0.0_SA_CTO~Z` terminal (site Z), in reply to `/open-calls` run twice by Andrew (~15:45Z, ~16:00Z).
**Recorded by:** `1.0.0_SA_CTO~Z`, same turn.

## VERBATIM

> "recs approved. on the serp note, yes, i do want to do social feeds and serp feed sooner than later but need
> identify resolved through existing channels first."

## The two cards it answers (as presented)

**CALL 1 of 2 (BLOCKING) -- Python fix on this box: (a) take Python 3.14 off PATH, or (b) repair 3.14?**
REC -- (a): take 3.14 off PATH (or finish uninstalling it) so `python` falls through to 3.11. 3.11 measured
running the messaging server; 3.14 has no `mcp` package. Editing PATH needs admin, so it is Andrew's act.

**CALL 2 of 2 (CARRIED) -- Pay for the `serp` build for 92 names: yes / no?**
REC -- No for now. Nothing imports `serp` yet (a build, not a run); the real gap is the identity backlog.
Revisit once that backlog clears.

## What the word rules (and what it does not)

1. **Card 1: (a) approved.** Remove the `C:\Program Files\Python314` entries from PATH. Measured at 17:23Z:
   all four entries (`Python314`, `Python314\`, `Python314\Scripts`, `Python314\Scripts\`) are in the MACHINE
   PATH, which Windows reads before the USER PATH (where Python311 lives); this session is NOT elevated, so
   the edit is Andrew's act at an admin shell. Sessions must restart to inherit the new PATH.
2. **Card 2: serp is NOT built now (the REC), AND Andrew states the direction:** social feeds and the serp feed
   are WANTED "sooner than later", SEQUENCED AFTER identity is resolved "through existing channels". The
   order is: identity backlog via existing channels FIRST, then serp + social feeds.
3. **Not ruled:** the spend amount, the vendor, or when the serp/social work starts. "Sooner than later" is a
   priority signal, not a GO; the serp build's metered spend still needs his word when it comes up after the
   identity gate. Social feeds are named here for the first time from this seat's vantage; no project carries
   them yet.

## Who this touches

`AMGT_HARVST` (issuer `2.0.0_SA_COO~Y`): the identity backlog through existing channels is the precondition
for any serp/social channel work.
