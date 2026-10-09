# Deploy Completion Record
**Date opened:** 2026-10-09T10:35:43.860408+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T104101Z
**Deploy:** NFRA_TRNSPT TR-w-20: re-wipe 30 Teams silver keys in place (monday_meeting 15, ocio_ic 7, asset_management_ic 8) at pin 776d8300716e572ea95f13ecd8281e594c0443cb; research_meeting EXCLUDED; pair COO @051003d7af + CTO @7a2e7199ed
**Authored by:** 0.7.0_AE_CloudOps~TR2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | step-0 prior-VersionId equality, 30 keys | live list_object_versions IsLatest per key equals R20_REWIPE_PRIOR_VERSIONS.json for all 30; any difference = STOP | STEP0 EQUAL: live list_object_versions IsLatest over the 3 silver prefixes (3 pages, denominator live_keys_scanned=30) -> only_live=0 only_prior=0 intersect=30, equal_to_prior=30 differ_from_prior=0 against R20_REWIPE_PRIOR_VERSIONS.json (total_keys=30). No key moved; no STOP. Evidence org/tier2_senior/0.7.0_AE_CloudOps/deliverables/NFRA_TRNSPT_TR2/W20_STEP0_PRE_VERSIONS.json | CLOSED 20261009T103723Z |
| L2 | verify | dry-run BEFORE from the clean extract of the pin | rewipe_silver --series monday_meeting,ocio_ic,asset_management_ic --dry-run prints keys=30 and per-key row counts | AC1 PASS from the clean extract at pin 776d8300716e572ea95f13ecd8281e594c0443cb (tool blob cd3bf1f39c == 4eb7ed184c:rewipe_silver.py, content-resolved): 'REWIPE-SILVER series=monday_meeting,ocio_ic,asset_management_ic keys=30 rows=8873 written=0 failed=0'. Key-set equality with the prior JSON: only_dry=0 only_prior=0; research_meeting absent from the output. Per-key BEFORE row counts in org/tier2_senior/0.7.0_AE_CloudOps/deliverables/NFRA_TRNSPT_TR2/W20_ROWCOUNTS_BEFORE.json | CLOSED 20261009T103832Z |
| L3 | activation | rewipe_silver --apply writes the 30 keys in place (KMS) | REWIPE-SILVER keys=30 written=30 failed=0 | APPLY rc=0 from the clean extract at pin 776d8300716e572ea95f13ecd8281e594c0443cb: 'REWIPE-SILVER series=monday_meeting,ocio_ic,asset_management_ic keys=30 rows=8873 written=30 failed=0'. 30 of 30 keys action=WRITTEN (KMS alias/opal-data-transcripts), held_out total 2271. No delete, no other series, prefix or bucket touched; research_meeting never passed. | CLOSED 20261009T104048Z |
| L4 | verify | post-run re-list: 30 NEW VersionIds + per-key row counts equal to L2 | 30 of 30 VersionIds differ from prior AND per-key rows before==after | POST-RUN re-list (live list_object_versions IsLatest, 3 pages, denominator live_keys_scanned=30): keyset only_live=0 only_prior=0; VersionIds equal_to_prior=0 differ_from_prior=30 -- all 30 keys carry a NEW VersionId. Per-key row counts before==after, mismatches=0 of 30 (rows_total 8873 both sides). Evidence: deliverables/NFRA_TRNSPT_TR2/W20_STEP2_POST_VERSIONS.json + W20_ROWCOUNTS_BEFORE_AFTER.json. NOT claimed here: the post-run re-wipe residual sweep with its planted positive control (CTO half condition 2) -- that proof is the issuer's. | CLOSED 20261009T104048Z |

## Log

- 20261009T103543Z OPENED by 0.7.0_AE_CloudOps~TR2 with 4 leg(s)
- 20261009T103723Z LEG L1 closed: STEP0 EQUAL: live list_object_versions IsLatest over the 3 silver prefixes (3 pages, denominator live_keys_scanned=30) -
- 20261009T103832Z LEG L2 closed: AC1 PASS from the clean extract at pin 776d8300716e572ea95f13ecd8281e594c0443cb (tool blob cd3bf1f39c == 4eb7ed184c:rewi
- 20261009T104048Z LEG L3 closed: APPLY rc=0 from the clean extract at pin 776d8300716e572ea95f13ecd8281e594c0443cb: 'REWIPE-SILVER series=monday_meeting,
- 20261009T104048Z LEG L4 closed: POST-RUN re-list (live list_object_versions IsLatest, 3 pages, denominator live_keys_scanned=30): keyset only_live=0 onl
- 20261009T104101Z CLOSED -- all 4 legs proven
