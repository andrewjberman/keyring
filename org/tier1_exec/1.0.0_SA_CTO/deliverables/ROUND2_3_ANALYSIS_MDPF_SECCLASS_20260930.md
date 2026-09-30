# MDPF_SECCLASS rounds 2 and 3 -- the CTO's L10 analysis

**Author:** 1.0.0_SA_CTO, 2026-09-30 ~13:5xZ (post-crash relaunch; owed since the CVO's slug of 07:28Z).
**Inputs, read at HEAD cc277564c0:**
- The CVO's slug 103223: `org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R2_R3_REVIEW_20260930.md`
  @`5ab8f37be7`; carriers `ADJUDICATION_v2.md` (C-S4..C-S7) and `REMEDIATION_v2.md` (S3, W6-S2, W5-S3, W5-S2).
- `2.0.0_SA_COO~M`'s packet `DRAIN_END_R2_R3_20260930.md` @`6d22aa7388` (SC-e1..e8 round 2, SC-e9 round 3, all
  `complete`, all WORLD, proofs re-run VALID). Round 4 (`MDPF_SECCLASS_DECOMP_R4.md`, one cell SC-e-10) is already
  issued on Andrew's Kimi word and is outside this compile; GATE (x) admits it.
- PRD v0.2 @`301332beb4` (ADMITTED; ratified-text half current by ENDPOINT hash, text changed since signed, which is
  the proportionate rule's expected reading).
- The seven never-widen halves: legacy label and instrument_kind signed `3bca6b55e6` and CLOSED by ~M `7e171f5510`
  (238 of 238, 156 of 156, 0 refused, table 2,309 -> 2,309); FWD3 (VNQI) and E18_IAM signed `a7a6d286f2` with the
  steps separate; BD_THREAD_R2, CUSIP rows and MODEL rows requested and not yet signed by this seat.

## 1. The decision the slug asked: the contract move is CONTRACTS wording, no re-sign (103225, stands)

`MDPF_SECCLASS_CONTRACT.json` v0.1.0 -> v0.2.0 added `identifier_namespace` {TICKER, CUSIP} and two `classified_by`
values. Under CLAUDE.md rule 27's proportionate sign-off (Andrew-direct 2026-09-24) only an ENDPOINT change re-signs;
a wording change under the section hash re-opens nothing and withholds no delivery. Neither change alters what the
project promises (the FWD lines are unchanged); both alter how a row says who classified it and which key space it
sits in. The L10 addendum is landed as PRD v0.2 (`301332beb4`, C-WRITER four values, C-FIELD identifier_namespace),
so the ratified text in force describes the contract in force. The CVO's disagreement is on the record and executed
as ruled; if `prd_signoff_lib.py` later binds the ENDPOINT hash alone, this case is the one it is for.

## 2. The rows

| row | ruling | owner |
|---|---|---|
| S3 (ARMED) | The thread drain broke IRPT_BCKEND's Holdings producer import on CLOUD. BD_THREAD_R2's release and IRPT_BCKEND's IB-mr-291 land in ONE window under one ledger entry; this seat signs BD_THREAD_R2's half only on a packet that names IB-mr-291's commit as a precondition. The same seat holds both orders. | 2.0.0_SA_COO~M |
| W6-S2 (ARMED) | The unconditional `bd-securities` PutItem grant lives in `shared-infra/main.tf:402-407`, shared with `partners-lambda-role`. E18_IAM's signed half is true of `bd-pipeline/iam.tf` alone and says so (a7a6d286f2). The shared-infra narrowing is a separate AE-lane order in a later round; its packet first prints EVERY consumer of `partners-lambda-role` (N writers = N rules read, N printed) and covers both branches. Not this round. | 2.0.0_SA_COO~M issues; 0.7.0_AE_CloudOps lane executes (dark today: the order is cut and parks on the seat's relaunch) |
| W5-S3 (ARMED, 0.0.0_AB_MSTR) | RESOLVED in the world: the pull-push landed, origin/CLOUD c5d944f680 (MSTR 103240, ls-remote 13:1xZ). Disarm on MSTR's ledger line (LD-0613 Progress 37), by the CVO at its next compile. | 0.0.0_AB_MSTR (disarm evidence), 3.0.0_SA_CVO (the row) |
| W5-S2 (INERT, this seat) | One token, two enums, two schemas: the contract's `classified_by` enum is canonical; the second schema's copy imports or cites the contract and carries no value of its own. A hygiene cell at the next drain, not a round cell. Rule 24 (iii): one axis, one intent. | 2.0.0_SA_COO~M (drain hygiene) |
| S2 (v1, OPEN) | Inflection's ticker-keyed source is still 2026-08-07. That is IRPT_BCKEND's S152/S216 snapshot lag, not a SECCLASS act; carried, cross-referenced in the IRPT_BCKEND round-25 analysis (section 1, the INF raw chain). | 2.0.0_SA_COO~P (IRPT_BCKEND) |
| W4-S1, W4-S2, W5-S1, W5-S4, W6-S1 | dismissed as compiled; accepted | -- |

The CVO's third unasked question (e9's `seed_bd_securities.py` copies every etf-classifications row unconditionally, so
CUSIP-keyed rows landing first would add 349 rows the fork never had) is adopted: the issuer's release-sequencing item 1
guards it, and this seat signs the CUSIP-rows half only on a packet whose dry-run prints the bd-securities delta as 0
new rows from CUSIP keys.

## 3. Outcome read

No act served in rounds 2-3 (the live table reads 2,309 rows, 0 `CUSIP:`-keyed, the CVO's scan 07:1xZ agreeing with
the packet). The two writes that HAVE served since (legacy label 238, instrument_kind 156, `7e171f5510`) move the
C-WRITER contract from APPLIED to EXERCISED on the legacy population. Every FWD stands at its round-1 grade
(`ROUND1_ANALYSIS_MDPF_SECCLASS_20260930.md`, `151c890591`); none is REALIZED. FWD-3 (VNQI seed) moves when its
signed act runs; FWD-4 and FWD-7 move on the scheduled classifier's first real fire and the model census (round 4).

## 4. Enrichment for round 5 (~M cuts; round 4 is already issued and is not reopened)

1. The signed acts in their sequenced order: FWD3 seed with `--accept-module-truth` (refused on any conflict but
   VNQI); E18_IAM step 1 then step 2, ledger entry open across both; CUSIP rows under the section-2 guard; MODEL rows
   after SC-e-10's census; BD_THREAD_R2 with IB-mr-291 in one window.
2. W5-S2 enum consolidation at the drain.
3. The W6-S2 AE-lane order, cut and parked with its consumer census as criterion 1.
4. FWD-7's scheduled classifier: one real scheduled fire read from the log, not the build.

-- 1.0.0_SA_CTO
