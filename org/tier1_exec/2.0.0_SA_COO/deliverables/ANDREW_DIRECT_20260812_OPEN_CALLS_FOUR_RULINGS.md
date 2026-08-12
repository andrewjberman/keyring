# ANDREW-DIRECT 2026-08-12 — `/open-calls` rulings, all six calls answered

**Recorded by `2.0.0_SA_COO` at the COO terminal, same turn as receipt.** Broadcast per `org/XXX.md`.

## VERBATIM

> *"all recs approved, for securities im looking into it with CVO now, for edit rights yes i would
> like to make that text editable just want it to be extremely light and client-facing do not want
> overwrought process architecture around this should be extremely simple setup, for ETFS canonical
> location its opal-data-etfs"*

## THE SIX CALLS, AS RULED

| # | call | ruling |
|---|---|---|
| 1 | 49F bar: accept 9-of-17 or drive P3? | **REC APPROVED = (b) AUTHORIZE P3.** Minting `portal/gold/advi/49financial` has its sovereign confirmation. |
| 2 | Which DDB table / S3 location is canonical for ETFS? | **`opal-data-etfs`.** ⭐ The P0 that gated two live items is ANSWERED. |
| 3 | $113.2M UNCLASSIFIED — curate, rules, or leave loud? | **REC APPROVED = leave UNCLASSIFIED-LOUD** — *and he is working the securities question with CVO himself, now.* **NOT a COO workstream.** |
| 4 | Yang/Manav editable pillar text? | **YES, MAKE IT EDITABLE** — with a binding constraint, below. |
| 5 | estate-pull backlog — sign or drop? | **REC APPROVED = DROP the backlog, keep forward days.** |
| 6 | ETFS month-end email recipients? | **REC APPROVED = Andrew only** until he says otherwise. |

## ⚠ CALL 4 CARRIES A CONSTRAINT, AND IT IS THE LOAD-BEARING PART OF THE RULING

His words: ***"extremely light and client-facing … do not want overwrought process architecture
around this … should be extremely simple setup."***

**This is a scope CEILING, not a green light to build a content system.** It composes exactly with the
rec he approved in the same breath (*"no CMS; the cheap intermediate is a served JSON the publishers
already own"*), so the sanctioned shape is:
- ⛔ **NO CMS. NO admin console. NO auth layer. NO approval workflow. NO draft/publish states. NO
  new Lambda, NO new bucket, NO new table.** Every one of those is the "overwrought process
  architecture" he named.
- ✅ **Content moves out of the component into data a publisher already owns**, so wording changes
  do not require a code edit + promote.
- **The BUILD LADDER applies at full force here** (rung 2: the estate already has it). A publisher
  that already emits served JSON is the mechanism; **if this needs a new component to exist, the
  design is wrong.**

> **Why the constraint is recorded as prominently as the approval: "make it editable" is the kind of
> ask an agent expands into a content-management project.** He pre-empted that in the same sentence,
> and the pre-emption is the instruction.

## WHAT EACH RULING UNBLOCKS

**Call 2 is the highest-leverage word in the message.** `opal-data-etfs` closes the ETFS CANON P0 and
releases **two items that were one cluster, not two deferrables**:
1. **AVGCAP `partial`-flag defect** — a **partner-REBATE basis**. `partial` keys off CALENDAR
   coverage, which carry-forward satisfies by construction (June shipped `partial=false` on 17/30
   written days, ~13% carried). **No estate instrument reports this.** Fix = graded written/carried
   days + re-key `partial` to **WRITTEN** coverage. **DS owns, CTO gates.**
2. **INF gold-floor derivation figure** — under his 07-31 DO-NOT-QUOTE-A-FIGURE order pending canon.
   **Canon is now given, so the magnitude can be derived and quoted.**

**Call 1 releases the last 8 of 17 keys** — their parity was *inexpressible* pre-cutover, not missing.

## ⛔ SCOPE DISCIPLINE ON CALL 3
He is working the securities/classification question **with CVO, himself, right now.** ⛔ **Do not
open a parallel curation workstream, do not dispatch on it, do not "help" by pre-building rules.**
The COO position is: the loud token stays honest meanwhile, and the next word on it is his or CVO's.

## CALL 5 — the DROP is a disposition, not a delete
**Stop treating the un-signed 08-05..08-12 manifest days as owed work.** ⛔ It does **not** authorize
deleting manifests or touching `s3://opal-estate-report/`. The producer is healthy (daily emissions
verified through 2026-08-12) and the forward path is unchanged. **The backstop trip-condition for
NEW days stands.**
