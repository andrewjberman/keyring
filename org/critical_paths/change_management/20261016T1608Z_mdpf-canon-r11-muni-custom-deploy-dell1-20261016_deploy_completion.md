# Deploy Completion Record
**Date opened:** 2026-10-16T16:08:23.935935+00:00
**Status:** OPEN
**Deploy:** MDPF_CANON CN-s-1: Opal_Muni_Income becomes the custom model Opal Municipal Bonds -- gold scripts to code/ (conditional D1), mdpf-gold-lambda package at pin 66ae82d62d with MDPF_GOLD_COMMIT stamp, one qa_local+qa_return_bodies dry run, issuer D4-PASS/STOP; emitter+publisher NOT touched (TO ADHOC.canon-r11-muni-custom-deploy, GO msg 6799, risk WORLD)
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 20.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | preconditions 2a-2i: GO, pin ancestry+content, pair halves, clock, sentinels, one-change-per-fire, runner layout (g), SMArtX partitions (h), identity flag (i) | printed reads |  | OPEN |
| L1 | verify | before print: whole-tree equality, D1 key ETag/VersionId, function CodeSha256/env, deployed manifest commit, package VersionId, schedule input, 16 served objects saved to C:/dev/_deploy_artifacts/canon_r11_muni/baseline, overwrite keys + control key, tax stores, workbook listing, emitter CodeSha256 | before-print json under org/tier2_senior/0.7.0_AE_CloudOps~DELL1/deliverables/canon_r11_muni/ |  | OPEN |
| L2 | s3-prefix | D1: build_cottonwood_mdpf_slice.py + mdpf_revamp_model_crosswalk.py to s3://opal-data-mdpf/code/scripts/gold/ via named safe-deploy -- ONLY if 2.g (iii) | mdpf-code-equality --files named_not_equal 0, or the ledger states D1 NOT DONE under 2.g |  | OPEN |
| L3 | activation | D2: build_package --pin 66ae82d62d, upload zip, .tf MDPF_GOLD_COMMIT to full pin SHA, ONE targeted safe-apply on mdpf-gold-lambda, read back env and manifest | MDPF_GOLD_COMMIT == pin == manifest commit, CodeSha256 differs from before |  | OPEN |
| L4 | verify | D4: ONE invoke with schedule input + qa_local + qa_return_bodies; 200, no FunctionError, errors empty, a4_objects_built 16; response saved + sha256; 16+overwrite keys unchanged in S3 | after print json + d4_response sha256 |  | OPEN |
| L5 | verify | issuer D4-PASS or D4-STOP (on STOP section-4 rollback read back) | the issuer's message id |  | OPEN |
| L6 | verify | after print, changed-name report, emitter control, deploy_ledger check; reported to 2.0.0_SA_COO~D1 and 0.0.0_AB_MSTR~DELL1 | equality AFTER out |  | OPEN |

## Log

- 20261016T160823Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 7 leg(s)
