# NFRA_CTLPLN decomposition -- round 26: the CVO's grade of FWD-15, 16 and 17, the dell1 scratch delete, FWD-14 (issuer 2.0.0_SA_COO~C; cut 2026-10-16)

**Status: ISSUED in one issuance. FROZEN at the cut.** (A cell cut later in the round, once its dependency clears, is an AMENDMENT of this document stating its gate limb, as in rounds 22, 24 and 25.)

**Input.** `ledger/ROUND_ANALYSIS.round25.md` (1.0.0_SA_CTO) @b2a2d5145a section 3 and msg 109591; the issuer's `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND25.md` and `ROUND25_INPUTS_FOR_ROUND_ANALYSIS.md` @a14976a438. **PRD:** v0.31. **Coverage entering the round (CTO table):** REALIZED 1, 3, 5, 24, 28; ADVANCED 2, 4, 6, 7, 8, 10, 11, 12, 14-19, 21, 22, 23, 25, 27; PARKED 9; MOVED 13, 20, 26. **Cadence:** `/canonical-drive` 30m.

## Cells

| cell | what | serves | risk | issued to |
|---|---|---|---|---|
| `CT-ap-1` | **Cut as an amendment, only if the CVO grades any of FWD-15, FWD-16, FWD-17 short of REALIZED; ONE cell naming the missing act.** Not cut now: no grade exists, and a cell cut ahead of its grade would name an act nobody has found missing. | FWD-15, 16, 17 | set by the amendment | a worker, at the amendment |

No order is cut at the issuance.

## Amendments

1. **`CT-ap-1` cut, 2026-10-16 ~04:3xZ, as a CROSSBOX CALL and not a laptop task order.** Dependency cleared: the CVO's `ADJUDICATION_v29.md` @6b85624313 graded FWD-16 and FWD-17 REALIZED and FWD-15 ADVANCED, one act short (C-S81); the CTO's round-25 addendum 1 @69d2a8dc22 REPLACES the enrichment list with ONE dell1 cell: a dell1 lane imports `tabulate` only from `SCRATCH_TARGET`, renders the one read-only table and commits the output and `tabulate.__file__` on `box/dell1`; "ask dell1 for it as a crossbox call". The act runs on dell1 under dell1's seats, so no laptop worker is spawned and no order file is added; the call body is `deliverables/2.0.0_SA_COO~C/XB_JOURNEY_R26_DELL1_RUN_ON_SCRATCH.md`. Risk class `LOCAL` on dell1 (read-only, no network, no install). **Gate limb that graded the amendment:** none (no task order is added or modified). Ruling 1 of round 25 is re-ordered by the CTO: the scratch delete goes to Andrew only after the output is committed.

## Driven by the issuer in this round (not cells)

1. **The CVO's read.** The L8 packets of rounds 24 and 25 are at `3.0.0_SA_CVO~L` (live; its summary read "awaiting NFRA_CTLPLN r24 L8"); the issuer nudged once with both paths and hashes (this tick). No READ ack yet; a second silent tick goes to `0.0.0_AB_MSTR` as `[STUCK]`.
2. **dell1's scratch folders.** `SCRATCH2` and `SCRATCH_TARGET` under `C:\dev\_intake_tabulate_20261016\` on dell1: the CTO puts the recursive delete to Andrew (round-25 ruling 1, REC delete). One act by dell1's seats if he says yes; recorded as accepted leftover if he declines. The issuer reads the answer.
3. **Call `XB-20261016T034630Z-a0a3`** (ACKED): closed from the issuing side after the CVO reads.

## FWD-14 (no cell)

Waits on Andrew's sitting (`c9a4`, `b87f`; the Security-log read joins `b87f`). FWD-9 PARKED; FWD-2 a qualified wait; FWD-27's person arms Andrew's. `W8-S7` waits behind the outcome cells.

## Carried with an OWNER and the CONDITION that un-parks each

As in the round-24 and round-25 decompositions: `W8-S7`, `S9103`, `S9120`, `W89-S3`, `W12-S1`, `Z-S3` (before 2027-12-01), `S9125` (dell1, before 2026-12-31), `S9119`, `S9128`, `W121-S3`/`S4`. `W126-S1` closed by the CTO's acceptance; `W128-S1` INERT and accepted (round-25 ruling 3).

## Rule 24

**Domain:** the CTO's round-25 section 3 enrichment list (3 items) against the open FWD chain; denominator in the CTO's section 1 table (28 FWDs). **Same grain; one intent; disjoint write surface:** no cell is cut now; `CT-ap-1`, if cut, writes only what its missing act names. **State coherence:** nothing in this round deploys, pushes or calls AWS.

## Dependency chains and fan-out

Three chains: (1) the CVO's grade, then `CT-ap-1` if any FWD reads short; (2) the scratch delete (Andrew's word, then dell1's seats); (3) FWD-14 (Andrew's sitting). `fanout: 0 of 3 chains, cap 8, reason: every chain waits on the CVO's grade or on Andrew's word; no cell can be cut honestly before either`
