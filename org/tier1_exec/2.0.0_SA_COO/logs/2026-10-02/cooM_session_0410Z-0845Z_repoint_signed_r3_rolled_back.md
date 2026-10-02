# Re-point signed (conditional) and leg P on DEV; BD r3 served regression rolled back — 2.0.0_SA_COO~M

**archetype:** MIXED
**Date:** 2026-10-02
**Task Order:** ad-hoc (MDPF_SECCLASS Cottonwood re-point; BD thread r3 rollback under NEVER-2)
**Status:** IN PROGRESS (every open item waits on a scheduled run or on Andrew's portal PROD promote)

---

## Objective

Resume after MSTR msg 104038 withdrew the laptop wind-down: finish the Cottonwood re-point's signing, read the 04:00Z Black
Diamond gold fire for r3's closing legs, and act on what that read found.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-clobber | --sweep opal-data-cot over 7 prefixes | PASS | 871 keys, 0 interleaved lineages |
| comp-clobber | scan --path data/cot | PARTIAL | missed d08's writer: the key is a constant passed to a helper |
| comp-iam | --help (live / reconcile) | SKIPPED | leg I's role read deferred to the act |
| comp-pipescript io | C_06 / D_03 / D_04 --pipeline bd (earlier this session) | PASS | named the served keys read for A1 |

**What worked:** live etag lineage for writers per key; the S3 version history to prove the regression began with the r3 code.
**What failed:** the static writer scan cannot see a key held in a constant (d08); a ledger HOLD refuses while apply legs are open.
**Gap found:** none new; the d08 miss is a known static-analysis limit.

---

## Work Completed

1. **Carrier branch merge trap fixed:** CLOUD merged into `coo-m-cot-carrier` (12a364a4fd), B_00 + its test restored from
   dda373cbd3 (affbc33e2b), 22 tests, negative control, dry merge = the ten files.
2. **Re-point packet:** re-measured (unclassified 97.72 M, 17.6%), writers counted, COO half signed @40cc2e2108; CTO half
   CONDITIONAL (batch 113): G, R, S wait for the readers on portal PROD. Correction for d08 (@10399a923f), CTO re-bound.
3. **Leg P:** portal readers rebased and pushed to DEV (455ca18d..eb90f2ad), CI success. Ledger opened late (stated).
4. **r3 leg B4 FAILED** on the 04:00Z fire: 49F firm mix 445.7 M of 1,843.1 M in no class line; client mixes short since 10-01
   07:46Z. Escalated; rolled back C_06/D_03/D_04/lib to pre-r3 versions 06:19Z; CTO batches 117-118: watermark reset + ONE ad hoc
   restore run 06:25Z; V1 green 08:2xZ; run exit 0 08:31Z; ledger CLOSED ROLLED-BACK (batch 129).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Defer re-point legs M, I, A to just before G | M unheld on CLOUD would let C_06/D_03/D_04 ship without their held library; I needs a 600 MB provider copy on a 96% disk |
| Roll back only the four mix producers | E_18 does not import lib/etf_classifier and runs clean under the dispatcher; CTO batch 129 accepted |
| Restore by one ad hoc run, not per-key versions | CTO batch 118: serves the 09-30 picture, not the day-older 09-29 one |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `NEVER_WIDEN_HALF_REQUEST_COT_REPOINT_20261001.md` | restated, signed, corrected | Yes -- f777231240, 40cc2e2108, 10399a923f |
| carrier branch (B_00, test) | trap fixed | Yes -- 12a364a4fd, affbc33e2b (branch only) |
| portal `coo-m-cot-mix-readers` | rebased, pushed to DEV | Yes -- eb90f2ad on origin/DEV |
| ledgers (re-point, r3, r3 rollback) | opened / legs / closed | Yes -- 34f4d61e67, a741b8e3d1, d3760cc1c0 |

Note: commit 34f4d61e67's subject says the re-point entry is HELD; the hold was refused (apply legs open) and the entry is OPEN.

---

## Blockers

- BLOCKED-SOVEREIGN on Andrew: portal PROD promote carrying eb90f2ad releases the re-point's legs G, R, S (CTO batch 113).

---

## Current State

49 Financial's served mix is restored (firm 100 percent at 1,843.1 M as of 09-30); BD's mix producers run the pre-r3 code while
E_18, the silver builder, lib/_shared and SSM v5 stay on r3. The Cottonwood re-point has both halves (CTO conditional), leg P on DEV,
everything else waiting on the PROD promote. Owed reads and the forward fix are listed in `REBOOT_BRIEF_20261001_2.0.0_SA_COO_M.md`.

---

## Next Steps

1. **Read the 14:15Z irpt-holdings-snapshot publication** -- split-account leg S and seed-rows leg S.
2. **Read the 22:10Z silver and 23:00Z gold fires** -- firm mix 100 percent, bd_assets_dim classes as the old library (batch 129),
   seed-rows leg G; roll the r3 silver builder back if either moves.
3. **Start the r3 forward fix after those reads** (batch 117 item 4).
4. **[Andrew] portal PROD promote** carrying eb90f2ad -- then re-point legs M, I, A, G, R, S.
