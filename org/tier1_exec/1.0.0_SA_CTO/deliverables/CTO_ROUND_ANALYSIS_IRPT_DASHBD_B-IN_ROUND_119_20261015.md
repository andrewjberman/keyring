# CTO ROUND-119 ANALYSIS -- IRPT_DASHBD workstream B-IN (Inflection) -- fee basis NET; the missing account is read at Orion's own account record (2026-10-15 ~04:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `2.0.0_SA_COO~I2` msg 8045, packet
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND118_BIN_DRAIN_END_20261015.md` @a75f9982df: 1 of 1 PASS, 0
judgment criteria. The CVO~IRPT slug closes the books behind this round. **No PRD addendum.** Issuer: `~I2`, ONE issuance.

## Rulings

1. **Fee basis: NET.** Ruling 3 of round 118 said a tie makes it NET, and it tied: 2 of 2 fee-bearing accounts in Q3, 0 untied, 0 reversed.
   - `~P2`'s feed records `fee_basis: NET` with the note "calcGrossOfFees false; tied on 1 household, 2 fee-bearing accounts, Q3 2026".
   - The page states "net of fees". It is never stated without that record behind it.
   - Every request the feed sends keeps `calcGrossOfFees` false, so the basis cannot drift by request.
   - The issuer's sign error is accepted as disclosed. W306-S1 is disarmed by D2-S57.
2. **The missing account is a coverage fact the feed carries:** `ABSENT` with `NO_GROUP`, never zero, never an Opal fill. Before anyone asks
   Orion as a person, the estate reads what Orion's API already says about that account. This is a read through the open egress, not a vendor
   contact:
   - **One cell (`~I2`, WORLD read, cap 3 GETs, paced, no retry):** read Orion's own account record for the missing account and for one
     account that does appear, over the endpoint the estate's pull already uses for accounts. Compare every performance-relevant flag
     (inclusion or exclusion from performance or reporting, status, inception and start dates, the model or managed flag).
   - Record the flag names and which ones differ, as verdict words only.
   - If a flag explains the omission, the feed's reason class gains it (for example `EXCLUDED_AT_SOURCE`) and the page words follow.
   - If nothing differs, the cause stays `NOT_DETERMINED`. A question to Orion's support is then a draft this seat files as an act for
     Andrew, because a human vendor contact is his. It is not filed before the read.
3. **The adapter cell waits on `~P2`'s feed** landing its first bronze and silver. The issuer's sequencing is accepted: an adapter with
   nothing to read is not cut.

## Round-119 cell (ONE issuance by `~I2`)

1. The Orion account-record read (ruling 2).

-- 1.0.0_SA_CTO~DELL2
