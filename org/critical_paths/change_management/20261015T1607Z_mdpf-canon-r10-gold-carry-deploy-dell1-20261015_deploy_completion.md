# Deploy Completion Record
**Date opened:** 2026-10-15T16:07:47.783386+00:00
**Status:** OPEN
**Deploy:** MDPF_CANON CN-r-1: Global Trend groups carry a missing leg only where the carried row still partitions the Total -- gold consolidator to code/ (conditional D1), mdpf-gold-lambda package at pin b6352de8f8 with MDPF_GOLD_COMMIT stamp, one qa_local dry run (TO ADHOC.canon-r10-gold-carry-deploy, GO msg 6065, risk WORLD)
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 21.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | preconditions 2a-2h: GO, pin ancestry+content, pair halves, clock, FIRMBKTS, one-change-per-fire, runner layout (g), SMArtX partitions (h) | printed reads |  | OPEN |
| L1 | verify | before print: whole-tree equality, D1 key prior ETag/VersionId, function CodeSha256/env, deployed manifest commit, package VersionId, schedule input, 16 served objects, 5 overwrite keys + control key, tax stores, workbook listing, emitter CodeSha256 | org/tier2_senior/0.7.0_AE_CloudOps~DELL1/deliverables/canon_r10_gold/before_print json + equality out |  | OPEN |
| L2 | s3-prefix | D1: code/scripts/gold/mdpf_gold_consolidator.py on s3://opal-data-mdpf via named safe-deploy -- ONLY if 2.g (iii) | mdpf-code-equality --files named_not_equal 0, or the ledger states D1 NOT DONE under 2.g |  | OPEN |
| L3 | activation | D2: build_package --pin b6352de8f8, upload zip, .tf MDPF_GOLD_COMMIT to full pin SHA, ONE targeted safe-apply on mdpf-gold-lambda, read back env and manifest | MDPF_GOLD_COMMIT == pin == manifest commit, CodeSha256 differs from before |  | OPEN |
| L4 | verify | D4: ONE invoke with schedule input + qa_local true; 200, no FunctionError, errors empty, a4_objects_built 16; 16+5 objects byte-equal, control key and stores same VersionId, emitter unchanged | after print json |  | OPEN |
| L5 | verify | after print, changed-name report, emitter control, deploy_ledger check; reported to 2.0.0_SA_COO~D1 and 0.0.0_AB_MSTR~DELL1 | equality AFTER out |  | OPEN |

## Log

- 20261015T160747Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 6 leg(s)
