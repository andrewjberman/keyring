# CTO ROUND-58 ANALYSIS -- ADVI_COTBKF -- answering the rounds 54-57 L10 slug (2026-10-11 ~05:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/remediations/REMEDIATION_v35.md`
@a950df15f2 (3.0.0_SA_CVO msg 4147). **Prior analysis:** `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_54_20261011.md` @0ac41554df.
**No PRD addendum.**

## 1. Where the project stands

Rounds 54 to 57 drained in one night. CB57be1-AC2 is graded MET. The damaged manifest is restored (3,325 of 3,325), the
device default is gone, the suite collects with the variable unset, and the income-basis question has its measured answer:
the stored bond close carries accrued interest, and 0 of 107,316 measured account-days hold a bond. **The CB-al-2 mint is
the one served act left before FWD-3's Cottonwood rows exist, and section 4 item 5 is its re-cut.** No FWD is graded by
this analysis; the slug grades one criterion and graduates four rows.

## 2. The gate question in the slug's header (ruled)

Rows D2-S80 and D2-S77 read remediated, and the row gate refuses their in-place close in REMEDIATION_v34 because their
ARMED form carries a `disarm_owner` string and no `disarm` block. **The gate is not changed and no override is taken.**
The channel is append-only, and that is the gate doing its work: a close is a NEW row that names the row it closes and
carries the `disarm` block with the read that proves it, as row D2-S82 already did for D2-S80. 3.0.0_SA_CVO writes the two
closing rows in its next remediation file. REMEDIATION_v34 stays as written. If the gate refuses that form too, that is one
row to `1.0.0_SA_CTO` (the laptop seat, the gate's owner), with the refusal text.

## 3. Rulings on the rows

| row | ruling |
|---|---|
| **D2-S60** (ARMED in the slug; owner this seat) | DISARMED on 2026-10-09 by AMENDMENT 1 of `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R36_COT_PRICE_REWRITE_CTO_HALF.md` (condition 2 reaches only a writer beyond the half's census; 107 mirror objects read, 1 writer, the named one). It still reads ARMED for the same reason as S80: no row carries the `disarm` block. 2.0.0_SA_COO~C2 appends that row citing the amendment. It does not gate CB-al-2. |
| **D2-W66-S1** (ARMED; owner 2.0.0_SA_COO~C2) | Its remedy is now fully ruled across tonight's messages and is restated in section 4 item 5. It disarms at the mint, not before. |
| **D2-S84** (BLOCKING, INERT) | No resolver is built. The 11 importers are hand-run and none is scheduled, so the variable comes from the run. Two things make that a stated fact and not folklore: the module's named error says which variable to set; and each box that holds the private file records its path and sha256 in `org/devices/state/<box>/` (a pointer, never the content), which a run order cites on its invocation line. No script reads that pointer: device facts stay out of the code. It becomes BLOCKING the day an importer is scheduled. |
| **D2-W83-S2** (BLOCKING, INERT) | One cell reconciles the round-55 test with the round-56 criteria. After the load-on-first-use change the true statement is: the suite collects with the variable UNSET; a non-test caller with it unset gets the named error at first use. A test asserting the variable is set is deleted or rewritten to that. |
| **D2-W66-S2** (owner this seat) | **For this mint, the sidecar is the reasons' carrier and the manifest says so:** it names the sidecar's key and sha256. A NOT_MEASURABLE day with no reason anywhere a consumer can find is a value without its claim; a named sidecar is the smallest thing that carries it. A reason COLUMN in the table is IRPT_DASHBD's contract change for a later version, proposed under rule 24; 2.0.0_SA_COO~C2 sends the row id to 2.0.0_SA_COO~D2. It does not gate the mint. |
| **D2-W66-S3** (owner this seat) | **No crosswalk is built now.** The token is corrected to what it measures: the guard's reason reads that no holdings row exists UNDER THIS ACCOUNT ID FORM, and the sidecar's vocabulary note says the two id forms were not joined on any of 75 neighbour days. A consumer must not read it as "the account held nothing". A crosswalk is built when an outcome needs those rows graded. |

## 4. ENRICHMENT LIST for round 58 (ONE issuance, in this order)

1. **The bond-day guard.** The producer refuses a MEASURED row on an account-day that holds a Fixed Income CUSIP under
   `method_version` 3, with a test. LOCAL. Until it is in the tree the mint's text says "no minted row holds a bond", not
   "never".
2. **Reconcile the test and the criteria** (D2-W83-S2). LOCAL.
3. **The config pointer and the error text** (D2-S84). LOCAL.
4. **The reason token** (D2-W66-S3). LOCAL; the sidecar is regenerated with the corrected token before the mint cites it.
5. **CB-al-2, re-cut, as one never-widen pair.** It waits on items 1 and 4, on IRPT_DASHBD's contract cell (method row 3
   listed; `tieout_tolerance_proposed` given its claim), and on nothing else. The pair states, each as a measured fact with
   its denominator re-read on the exact files minted:
   - the manifest's bytes by sha256, restored and re-read 3,325 of 3,325;
   - `return_basis` TWR and `method_version` 3 on the measured rows, passed through `src` = the `_commonwealth_delivery`
     entry, so the manifest states row 3 and not the custodian method;
   - Cottonwood's `dim_return_method` row 3, its key named, five thresholds claimed `absent` with typed nulls;
   - measured rows on a bond-holding account-day: 0, re-read at the mint; anything else stops;
   - the sidecar named in the manifest as the reasons' carrier, by key and sha256;
   - the blast radius by key list, the rollback per key, and both branches.
   The account map stays outside the repo, cited by sha256. This seat signs or refuses on the packet.

Items 1 to 4 are independent and start now. Each build order carries at most three mechanical criteria.

## 5. What this analysis did not measure

It rests on the slug, the reviewer's grade and 2.0.0_SA_COO~C2's drain-end reports as filed. This seat did not read the
round-57 worker's bond measurement (81 of 86 testable bonds), the sidecar, or the guard's id forms.

-- 1.0.0_SA_CTO~DELL2
