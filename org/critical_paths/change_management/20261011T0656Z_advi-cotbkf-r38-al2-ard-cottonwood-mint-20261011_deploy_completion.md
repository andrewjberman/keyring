# Deploy Completion Record
**Date opened:** 2026-10-11T06:56:18.360447+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T072305Z
**Deploy:** ADVI_COTBKF CB-al-2: mint Cottonwood account_return_daily (3,325 days) under the R59 never-widen pair
**Authored by:** 0.7.0_AE_CloudOps~CB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | condition 1: list-object-versions on the three gold prefixes, all pages | versions + delete-marker counts per prefix, printed | condition 1 MET. list-object-versions, auto-paginated, IsTruncated=None on all three: irpt/cottonwood/gold/account_return_daily/ versions=0 delete_markers=0; account_return_daily_blank_reasons/ versions=0 delete_markers=0; dim_return_method/ versions=0 delete_markers=0. POSITIVE CONTROL on the parent prefix irpt/cottonwood/ reads versions=862 delete_markers=1, so the three zeros are real absence and not a failed read. Both counts 0 => the pair's 'no prior version exists' is TRUE and its rollback sentence stands uncorrected. | CLOSED 20261011T065806Z |
| L2 | verify | step 3: --stamp-manifest | ARD-COTTONWOOD-MANIFEST-STAMP line + manifest sha256 unchanged | step 3 rc=0, last line EXACTLY as the amendment specifies: 'ARD-COTTONWOOD-MANIFEST-STAMP days=3325 day_hashes_equal=3325/3325 note=present sidecar_rows=1584413 method_version=3'. Manifest sha256 d2d99d5c4a127635170f77516b52fdfc0c163e151e39649e35569a601ce47b36 measured before AND after the stamp: unchanged, as the step requires. | CLOSED 20261011T065859Z |
| L3 | verify | step 4 / condition 4: --bond-check | line carrying measured_rows=107316 measured_rows_on_bond_days=0 | step 4 / condition 4 MET, rc=0: 'ARD-COTTONWOOD-BOND-CHECK days=3325 rows=1691729 measured_rows=107316 measured_rows_on_bond_days=0 fixed_income_cusips=778'. The two figures the condition names are present and exact: measured_rows=107316, measured_rows_on_bond_days=0. The tool refuses on anything but 0 and did not refuse. | CLOSED 20261011T065948Z |
| L4 | verify | step 5 / condition 2: --show-day-manifest --date 2026-06-22 | the ARD-COTTONWOOD-DAY-MANIFEST line, exit 0 | step 5 / condition 2 MET, rc=0. Last line: 'ARD-COTTONWOOD-DAY-MANIFEST date=2026-06-22 method_version=3 valuation_source=positions_x_as_traded_close fee_treatment=net_of_fees price_basis=as_traded custodian_text=absent'. The shown manifest body carries method_version 3, the three row-3 fields, and the row-3 method sentence ('r_t = (V_t - F_t) / V_(t-1) - 1; ... GIPS-ALIGNED, not GIPS-compliant.'), address s3://opal-data-cottonwood/irpt/cottonwood/gold/account_return_daily/date=2026-06-22. Custodian scan over the WHOLE output: 1 occurrence, which is the token custodian_text=absent itself -- no custodian method text anywhere, so the condition's STOP did not fire. LIMIT accepted by name in the CTO half: show mode mirrors apply_days rather than being called by it, which is why condition 3 (L6) is the control. | CLOSED 20261011T070032Z |
| L5 | s3-prefix | step 6: --apply under both pair halves (THE MINT) | count of LANDED lines + ARD-COTTONWOOD-APPLY last line | step 6 THE MINT: rc=0, 07:01:01Z-07:17:06Z. Last line EXACTLY as the amendment specifies: 'ARD-COTTONWOOD-APPLY days=3325 landed=3325 sidecar=landed method_row=landed'. LANDED lines=3328, reconciled in full against days=3325: 3325 day lines with 3325 DISTINCT dates and zero duplicates, +1 sidecar (account_return_daily_blank_reasons/source_date=2026-06-23/ard_cottonwood_blank_reasons.parquet sha256=589f72cc... bytes=763053), +2 for method_row, which is TWO objects not one (dim_return_method/method_version=3/data.parquet etag=7b70c246... and its manifest.json). 3325+1+2=3328, nothing unexplained. First day key date=2013-04-03, last day key date=2026-06-22. Every object lies inside the three granted prefixes; no key outside them. The apply re-ran the bond check as its own first act and printed measured_rows=107316 measured_rows_on_bond_days=0 at write time, so condition 4 holds on the writing run and not only on the earlier read. | CLOSED 20261011T071921Z |
| L6 | verify | step 7 / condition 3: --verify-served | ARD-COTTONWOOD-VERIFY days=3325 match=3325/3325 ... manifests=3325/3325 | step 7 / condition 3 MET, rc=0, 07:20:07Z-07:20:52Z. Last line EXACTLY as the amendment specifies: 'ARD-COTTONWOOD-VERIFY days=3325 match=3325/3325 sidecar=match method_row=match manifests=3325/3325'. Preceding line 'ARD-VERIFY mismatches=0 first=[]' -- zero mismatches with an EMPTY first-mismatch list. manifests=3325/3325 is the control the CTO half named for condition 2's accepted limit: every served manifest.json was read back for the five fields, so apply_days demonstrably handed the producer the right input and not merely the show-mode mirror. Row ADVI_COTBKF-D2-W66-S1 disarms on this line per condition 3. INDEPENDENT corroboration, not the tool's self-report: aws s3api list-objects-v2 auto-paginated, IsTruncated=None, counted client-side -- account_return_daily/ 6650 objects = 3325 data.parquet + 3325 manifest.json (both objects of every day), account_return_daily_blank_reasons/ 1, dim_return_method/ 2. 6653 served objects, matching the apply's 3325 days x2 +1 +2 exactly. | CLOSED 20261011T072305Z |

## Log

- 20261011T065618Z OPENED by 0.7.0_AE_CloudOps~CB2 with 6 leg(s)
- 20261011T065806Z LEG L1 closed: condition 1 MET. list-object-versions, auto-paginated, IsTruncated=None on all three: irpt/cottonwood/gold/account_retur
- 20261011T065859Z LEG L2 closed: step 3 rc=0, last line EXACTLY as the amendment specifies: 'ARD-COTTONWOOD-MANIFEST-STAMP days=3325 day_hashes_equal=332
- 20261011T065948Z LEG L3 closed: step 4 / condition 4 MET, rc=0: 'ARD-COTTONWOOD-BOND-CHECK days=3325 rows=1691729 measured_rows=107316 measured_rows_on_
- 20261011T070032Z LEG L4 closed: step 5 / condition 2 MET, rc=0. Last line: 'ARD-COTTONWOOD-DAY-MANIFEST date=2026-06-22 method_version=3 valuation_sourc
- 20261011T071921Z LEG L5 closed: step 6 THE MINT: rc=0, 07:01:01Z-07:17:06Z. Last line EXACTLY as the amendment specifies: 'ARD-COTTONWOOD-APPLY days=332
- 20261011T072305Z LEG L6 closed: step 7 / condition 3 MET, rc=0, 07:20:07Z-07:20:52Z. Last line EXACTLY as the amendment specifies: 'ARD-COTTONWOOD-VERIF
- 20261011T072305Z CLOSED -- all 6 legs proven

## CLOSE DISPOSITION -- APPLIED, UNREAD (CTO half condition 6)

**APPLIED, UNREAD.** All 6 legs proven and the entry CLOSED at 20261011T072305Z. The keys are minted and
served; they stay UNREAD. No reader of `account_return_daily` for Cottonwood exists, and none is created by
this act -- a reader waits on its own pair (ADDENDUM 11.1). This act built no reader, no schedule and no
trigger.

**What landed, 6,653 objects inside the three granted prefixes and nothing outside them:**

- `s3://opal-data-cottonwood/irpt/cottonwood/gold/account_return_daily/` -- 6,650 objects:
  3,325 `data.parquet` + 3,325 `manifest.json`, first `date=2013-04-03`, last `date=2026-06-22`.
- `.../account_return_daily_blank_reasons/source_date=2026-06-23/ard_cottonwood_blank_reasons.parquet` -- 1.
- `.../dim_return_method/method_version=3/` -- 2 (`data.parquet` + `manifest.json`).

**Rollback is NOT a delete** (AMENDMENT 4, kept by AMENDMENT 5, and the CTO half's section 4 with section 2's
third point). The minted keys stay unread behind the reader gate; a partial mint is RESUMED under an amendment
to this pair; a delete is Andrew's and is not this order's act. The versions census at L1 read 0 versions and 0
delete markers on all three prefixes against an 862-version positive control, so the pair's "no prior version
exists" sentence was true at write time and needed no correction here.

**Condition 7, not covered by the pair and not done:** no delete, no overwrite, no re-run of `build()`, no key
outside the three prefixes, no reader.

**Row `ADVI_COTBKF-D2-W66-S1` disarms** on L6's `manifests=3325/3325` per condition 3 -- the disarm is the
row's own, recorded here as the evidence that discharges it rather than claimed as this entry's act.
