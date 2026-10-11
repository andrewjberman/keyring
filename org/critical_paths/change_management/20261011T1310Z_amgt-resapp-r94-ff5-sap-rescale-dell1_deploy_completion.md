# Deploy Completion Record
**Date opened:** 2026-10-11T13:10:52.863440+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-ff-5: two ordered STORE writes for SAP_GY_Equity ONLY -- (1) analyze.reverify_stored_thesis_driver rewrites filings/v1/SAP_GY_Equity/000110465926020058.analysis.json at its own key (ETag-conditional overwrite, versioning keeps the VersionId): 0 -> 3 points shown on the series unit's scale (2023 = 13.745, 2024 = 18.078, 2025 = 21.05 EUR billions, each keeping stated_value, stated_scale and rescaled_to), the conversion STATED by the filing (18,078 million in 2024 and 18.08 billion in the same passage); (2) drafting_build --splice-driver overwrites drafting/v1/SAP_GY_Equity.json with only thesis_driver and thesis_driver_provenance moving (risk WORLD; GO 2.0.0_SA_COO~R1 msg 3868, CTO signature msg 3867). BOTH NEVER-WIDEN HALVES READ WHOLE: COO half NEVER_WIDEN_ROUND94_SAP_RESCALE_COO_HALF.md (msg 3866), CTO half. Run from a detached checkout at ae728f0680 (analyze.py 4d1f93c978f0, drafting_build.py fd51d3dd7ffa, crosswalk.py 3603be4be89a; ff-3 @ae14fab6f5 an ancestor). ASML and BABA are NOT touched. A key other than SAP, served_validator=False, or a moved key beyond the two is a STOP and the recorded VersionIds are restored in the hour unless the CTO names KEEP. Rollback: copy each recorded prior VersionId back to the same key, drafting first, never a delete.
**Authored by:** 0.7.0_AE_CloudOps~RA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | PRE-ACT STATE read by this seat: the pin and its three blobs; ff-3 ancestry; the open-deploy sweep of every live worktree for filings/v1 or drafting/v1 | ancestry reads, blob compares, the sweep denominators |  | OPEN |
| L2 | verify | ROLLBACK LIST: the VersionId of every analysis and drafting object of the 12 names recorded BEFORE step 1, SAP's two marked and equal to the half's | the VersionIds file path and SAP's two rows |  | OPEN |
| L3 | verify | the pair's table re-run on the GO day: r94_rescale_table.py and the dry re-verification of all 12 objects (changed set exactly {SAP 0 -> 3}); the three points printed with stated value, scale and the scale shown; the dry splice's served_validator and moved keys | the 12-row comparison, the rescale-table verdict, the points and the dry-splice line |  | OPEN |
| L4 | activation | STEP 1 for SAP_GY_Equity only: analyze.reverify_stored_thesis_driver dry_run=False; the write read back; new VersionId; points before and after | the receipt and the points |  | OPEN |
| L5 | verify | STEP 2 dry run after step 1: drafting_build --splice-driver --dry-run --only-keys SAP_GY_Equity reads served_validator=True and moved keys exactly thesis_driver and thesis_driver_provenance | the dry-run line verbatim |  | OPEN |
| L6 | activation | STEP 2 write: the same with --pre-act-dir and without --dry-run; the ONE writer overwrites drafting/v1/SAP_GY_Equity.json | SPLICED 1 of 1 and the post_act sha256 |  | OPEN |
| L7 | verify | no other key moved: all 24 objects of the 12 names re-headed, exactly two VersionIds changed (SAP analysis and drafting), ASML and BABA unchanged; drafting diff only the two keys; the served thesis_driver for SAP, ASML and BABA before and after, SAP's three points printed with their units | the 24-row compare and the served points |  | OPEN |
| L8 | verify | AC1 r92_driver_reverified.py --write-set SAP_GY_Equity YES; r94_locator.py YES; AC2 the no-regression arm YES with the function CodeSha256 unchanged | the verdict lines |  | OPEN |

## Log

- 20261011T131052Z OPENED by 0.7.0_AE_CloudOps~RA1 with 8 leg(s)
