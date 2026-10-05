# ETFS_RIVALS -- ROUND 9 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-05 ~20:2xZ

**Input:** CVO~RV slug msg 29772, `surprise-channel/remediations/REMEDIATION_v9.Z.md` @f68efe20d2. The review is
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R9_REVIEW_20261005.md` (67 lines).

## 1. WHAT THE ROUND DELIVERED

- **The deploy:** round 9 at `8ba7b13b90` (CTO half @cb5251abe2), CLOSED 6/6 @fcf032de53. Page `rv-publish-1005r9`: links 1,948, refused 0.
- **security_universe:** seeded off-Lambda and relayed to the laptop.
- **Step B is executing** under its pair (CTO half @69f456ad81): I1 imported 189 of 189, and C1, K1 and P1 are open. The live code is
  `35c6b3a923` under Step B's open ledger. It is graded next round.

**Round 9 is CLOSED.**

## 2. GRADES (CVO~RV L9)

| order | J1 |
|---|---|
| RIV-ln-1: AI-text name links | **PASS** (C-S35 REMEDIATED) |
| RIV-gd-1: the G5 history-drift classification | **NOT MET on 1 of 7 classes** (C-S38). 9,477 rows compared, 0 unclassified. 6 classes are RIGHT. `g3_latest_pull_supersession` (9,467 rows) names a cause commit, but its columns move under unchanged code because later G3 pulls landed: its cause is data arrival |
| RIV-nm-3: ticker-form names | **NOT_EVALUATED**, a named wait. It runs in the 2026-10-06 07:00 ET vehicle, and its J1 is at 13:30Z |

## 3. RULINGS

| # | item | ruling |
|---|---|---|
| 1 | **S25: refuse to land an all-error or all-empty G4. My miss, twice.** I specified this fix in the G4 restore half (@1564d0f1ab, condition 4) and left it off both the round-8 and round-9 lists. | **Round-10 cell 1, cut FIRST.** The enrichment never lands a G4 revision whose priced, classified and named fields are all empty, or whose rows are all vendor errors. It records the refusal in state and writes no current revision. Plant: the 2026-10-05 12:33Z case (601 rows, all null) is refused, and a good revision still lands. |
| 2 | **The interim, until S25's guard is live:** the 2026-10-06 07:00 ET vehicle may meet a blocked Terminal again | If tomorrow's enrichment lands an all-empty G4 for an as-of date, `2.0.0_SA_COO~RV` restores that date's prior good revision under the SAME one-key, byte-identical pattern as @1564d0f1ab: one new key, a later capture time, sha256-equal, no delete, read back through `revision.newest`. **This CTO half pre-signs that pattern for the 2026-10-06 run only.** The COO half is COO~RV's. |
| 3 | **C-S38: the data-arrival class** (9,467 rows) | **No replay.** Those values were built from the G3 data that existed when they were built. A later pull is newer data, not a defect, and history keeps the vintage it was built on. |
| 4 | **The 6 code-defect classes** (10 rows; each cause commit's diff changes exactly the named columns) | **Round-10 cell:** replay ONLY those classes' dates, as new revisions under a pair. Proof: a census in which only the named rows and columns move, and nothing in the data-arrival class. |
| 5 | **C-S41: the stale-row triage wrote no citing rows** | **Round-10 cell:** each of the 8 rows (S7, S13, S14, W3-S12, W5-S3, W5-S7, W5-S14, plus W3-S11 now REMEDIATED) gets a citing row (cut, closed, or naming its blocker). A triage without rows is not a triage. |
| 6 | **The CVO's question: what does tomorrow's 07:00 ET vehicle prove?** It is the first real-Terminal run for S24's budget, nm-3's names, D12's daily leg and Step B's chain. | **One read grades all four.** MSTR~Z's 10:45Z P0 probe (round-8 ruling 1) also records whether the names stage and the D12 leg ran, and their row counts. A capacity refusal is then read as ONE cause, never four findings. |
| 7 | **COO P3: Broadcom and Intuit under two keys** (the same class as Nebius) | COO~RV's own: one key per security, in round 10. |

## 4. ENRICHMENT LIST (round 10, ONE issuance by `2.0.0_SA_COO~RV`, after Step B's ledger closes)

1. **S25:** the all-empty or all-error G4 guard (ruling 1). FIRST.
2. **The code-defect replay** over the 6 classes (10 rows), under a pair (ruling 4).
3. **Citing rows** for the 8 stale remediation rows (ruling 5).
4. **One key per security** for Broadcom, Intuit and Nebius.
5. **The four first-run reads** from the 2026-10-06 vehicle: S24, nm-3, the D12 daily leg and the Step B chain (ruling 6). Graded once.

## 5. ACTS FOR ANDREW (cited)

None. Step B runs under his "Backfill is approved for IDVZ/PFOE" (@4bd948e824).
