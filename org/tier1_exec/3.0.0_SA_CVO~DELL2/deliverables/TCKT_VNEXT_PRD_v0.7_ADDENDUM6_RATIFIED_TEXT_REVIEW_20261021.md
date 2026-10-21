# TCKT_VNEXT PRD v0.7 ADDENDUM 6 -- ratified-text half review: REFUSED (three "moved" outcomes have no graded carrier)

**Seat:** `3.0.0_SA_CVO~DELL2`, 2026-10-21 ~02:3xZ. **PRD:** `org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md` v0.7 @df3eb8dc43,
ADDENDUM 6. Asked by `1.0.0_SA_CTO~DELL2` msg 11762.

## What I read

- **ADDENDUM 6.** FWD-1, 3, 6, 8 and 9 and FWD-2's file arm are "MOVED to IRPT_ANLREQ, graded there and never here", and "No capability
  is dropped from the estate". TCKT_VNEXT closes on FWD-2 (ticket arm), 4, 5, 7, 10 and 11.
- **The moved outcomes' own text** in this PRD: FWD-1, 3, 6, 8 and 9.
- **IRPT_ANLREQ PRD v0.28** (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`): its ENDPOINT (FWD-1 to FWD-12), C-ABSORB items
  (c) and (e) (line 165), and the addenda where the moved items appear.

## Where each moved outcome actually lands

| TCKT_VNEXT outcome | promise | carrier in IRPT_ANLREQ | graded there? |
|---|---|---|---|
| FWD-1 | an Analysis Request filed, report opened from the ticket | IRPT_ANLREQ FWD-1 (four attachments on the open ticket) | YES |
| FWD-9 | the package on the open ticket | IRPT_ANLREQ FWD-1 (the four standalone attachments) | YES |
| FWD-2 file arm | another firm refused on the file and report ref | IRPT_ANLREQ ENDPOINT SOURCE line 78 ("TCKT_VNEXT FWD-2; C-PACKAGE firm check") | YES, as cited |
| **FWD-3** | a bad sheet (several accounts, a totals row, an unpriceable holding) turned back with what to fix | the unpriceable part: C-SWAP replaces it and never asks the filer (Andrew 10-15, v0.18). The sheet-shape part: C-STOREDINPUT and the reader's door checks, an enrichment item (lines 276-305) | **NO.** It is a contract and an enrichment list, not an outcome with a DONE WHEN |
| **FWD-6** | the commentary draft on the ticket, and who sent the final and when | the draft: the commentary attachment of IRPT_ANLREQ FWD-1. The sender record: "`commentary_sent` on the ticket page ... As parked" (line 308) | **Partly.** The sender record is parked, not graded |
| **FWD-8** | a client advisor files unaided and opens the report | "the partner organic arm ... waits on the Ticket Center being shown to client users" (lines 38, 161, 378) | **NO.** An organic arm, never the gate |

So "graded there and never here" is true for FWD-1, FWD-9 and FWD-2's file arm, and false for FWD-3, FWD-6's sender record and FWD-8.
"No capability is dropped from the estate" overstates it: three promises leave this ENDPOINT with no graded carrier. The close's
denominator would then be short by three without saying so. That is the defect this half exists to catch (Taxonomy Law, postulate i).

## The fix (ADDENDUM 6 text only; it changes no grade and needs no new work)

Replace the MOVED bullet and the "No capability is dropped" sentence with one line per outcome:

- **FWD-1, FWD-9:** MOVED; graded as IRPT_ANLREQ FWD-1.
- **FWD-2 file arm:** MOVED; graded under IRPT_ANLREQ C-PACKAGE (ENDPOINT SOURCE line 78).
- **FWD-3:** the unpriceable-holding part is SUPERSEDED by C-SWAP: the filer is never asked (Andrew-direct 2026-10-15, IRPT_ANLREQ
  v0.18). The sheet-shape part (several accounts, a totals row) is CARRIED BY IRPT_ANLREQ C-STOREDINPUT and the reader's door checks,
  as a contract with no outcome. Either name the IRPT_ANLREQ outcome that will grade it, or say it is ungraded and name who decides.
- **FWD-6:** the draft is MOVED, graded as IRPT_ANLREQ FWD-1's commentary attachment. The sender record is PARKED in IRPT_ANLREQ's
  enrichment list (`commentary_sent`, line 308), owner `2.0.0_SA_COO~Y2`; ungraded until cut.
- **FWD-8:** SUPERSEDED by Andrew-direct 2026-10-14 ~15:2xZ: the Ticket Center is shown to Opal users only, and the filer is Opal staff
  (IRPT_ANLREQ ADDENDUM v0.6). It is kept as IRPT_ANLREQ's organic arm, which waits on the Ticket Center being shown to client users. It
  is not a promise either project grades.

On that bump this seat signs the same hour. The grades of FWD-2 (ticket arm), FWD-4 and FWD-5 asked in msg 11762 are a separate act,
and do not wait on this text.

-- `3.0.0_SA_CVO~DELL2`

## Re-review at v0.8 @4bfe0b7f6 (2026-10-21 ~02:3xZ): SIGNED

- Half reviewed: ratified-text, half_hash `b756bd8f3e04d1795e73ea885e43770ac53ba1cf7122a8e5315b8d60455ce0d1`.
- I read the diff v0.7 to v0.8. ADDENDUM 6 now names each moved outcome's carrier, as this review asked:
  - FWD-1 and FWD-9 are MOVED to IRPT_ANLREQ FWD-1.
  - FWD-3 is split: the unpriceable part is SUPERSEDED by C-SWAP. The sheet-shape part is CARRIED by C-STOREDINPUT, UNGRADED, and the
    CTO decides at the next IRPT_ANLREQ analysis whether it becomes an outcome.
  - FWD-6: the draft is MOVED; the sender record is PARKED with owner `~Y2`.
  - FWD-8 is SUPERSEDED by Andrew-direct 2026-10-14 and kept as an organic arm.
  - FWD-2's file arm is MOVED to C-PACKAGE.
  - "No capability is dropped" is gone.
- The close's denominator is now stated: TCKT_VNEXT closes on FWD-2 (ticket arm), 4, 5, 7, 10 and 11. Three items are openly ungraded
  or parked, each with an owner. **SIGNED.**
