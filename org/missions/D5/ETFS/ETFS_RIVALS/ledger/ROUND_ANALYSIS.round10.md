# ETFS_RIVALS -- ROUND 10 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-06 ~01:0xZ

**Input:** CVO~RV slug msg 29838. Compile `surprise-channel/adjudications/ADJUDICATION_v10.Z.md` @85301da213; there is no
REMEDIATION_v10. Review `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R10_REVIEW_20261006.md` (77 lines, read in full).

## 1. WHAT THE ROUND DELIVERED

| cell | state |
|---|---|
| RIV-eg-1, S25's guard (no all-empty or all-error G4) | **Live** on the Terminal vehicle from the shared tree (equal to 0997603f5d). There is no Lambda leg. AC1 re-run by the CVO: PASS 0 |
| RIV-iam-1, the round-9 table grants | **Applied** (CTO half @4e9b59ea50, ledger CLOSED). Simulate reads allow on the 4 grants and deny on both negative controls. My read: live equals AFTER on both roles |
| RIV-ok-1, one key per security | Drained, **not deployed** (round-9 addendum 2) |
| RIV-rp-2, the code-class replay tool | Drained. The dry run moves 1,323 rows in the 4 classes and 0 outside them. **The served replay is held** on `_g5_target` (rows Z-W3-S23 and Z-S42) |
| The Z-S31 repair | Live @409b855114 |
| D12 Step B | CLOSED 8/8 |

**Round 10 is CLOSED.** Nothing graduates.

## 2. GRADES (CVO~RV L9)

| item | grade |
|---|---|
| RIV-ok-1 J1 | **NOT_EVALUATED.** Moved to round 11 by addendum 2, because it is not served |
| Z-W3-S22, rp-2 AC1 (b): labels and fills | **CONFIRMED, with condition C-S42.** 4,950 rows (9,892 cells) of G1 revision labels and 5,287 filled cells move. Both are effects of the 4 classes, and 0 trade-fact or G3 label cells move outside them |

## 3. RULINGS

| # | item | ruling |
|---|---|---|
| 1 | **C-S42 and the review's s.5:** the dry census records no G5 keys, so a G5 written between the dry run and the served replay would change the base unseen | **Adopted as written.** The served replay's never-widen half lists, PER FUND, the relabelled rows and filled cells (4,950 and 5,287 in total) in its blast radius. At its own start it records the newest G5 key per planned date and re-runs `plan` against those keys. It **STOPs** if any key differs from the plan's. W6-S2's first-window precondition rides the same half. |
| 2 | **C-S38:** `g5_drift.json` still attributes the 9,467-row data-arrival class to cause commit `4fa3e25f5e` | **A round-11 record fix.** Re-label that class's cause as "data arrival (later G3 pulls)" in the drift record, per round-9 ruling 3. It moves no data. |
| 3 | **P2: the 2026-10-06 vehicle carries six proofs** (eg-1 live, nm-3 names, S24's budget, the D12 leg, iam-1's first data run, S31's disarm) | **One read grades all six,** at the CVO's 13:30Z read, after MSTR~Z's 10:45Z P0 probe (round-8 ruling 1). A capacity refusal is ONE cause, never six findings. A blocked Terminal falls back to the pre-signed interim restore (round-9 ruling 2). |
| 4 | **The NBIS label** ('NBIS US Equity' against 'NBIS_US_Equity') | Graded with ok-1's round-11 J1, as the review routes it. |

## 4. ENRICHMENT LIST (round 11, ONE issuance by `2.0.0_SA_COO~RV`)

1. **`_g5_target`, FIRST.** A same-input pass at a NEW code version writes a new revision; at the SAME code version it still writes
   nothing. Both arms are the criterion (round-9 addendum 2).
2. **The served replay** of the 4 code classes (1,323 rows), under a pair carrying ruling 1. Proof: a census in which only those 4
   classes, plus their labels and fills, move.
3. **The ok-1 deploy, AFTER the replay.** Its J1 includes the NBIS label.
4. **The C-S38 drift-record fix** (ruling 2).
5. **The six first-run reads** from the 2026-10-06 vehicle, graded once (ruling 3). This is a grade, not a build cell. S31's disarm is
   `2.0.0_SA_COO~RV`'s at that run.

## 5. ACTS FOR ANDREW (cited)

None. The vehicle's Bloomberg use runs under his existing word for the OPAL_BBGTML pull. The backfill ran under "Backfill is approved
for IDVZ/PFOE" (@4bd948e824).
