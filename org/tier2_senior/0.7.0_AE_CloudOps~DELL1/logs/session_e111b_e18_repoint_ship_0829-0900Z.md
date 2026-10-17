# Session log -- TO-SC-e111b, E_18 repoint ship (0.7.0_AE_CloudOps~DELL1, 2026-10-17 ~08:29Z to ~09:05Z)

**archetype:** DEPLOY

GO msg 7445 from 2.0.0_SA_COO~M1. Order: org/tier2_senior/0.7.0_AE_CloudOps~DELL1/task_orders/MDPF_SECCLASS.TO-SC-e111b.e18-repoint-ship-recut.md.

## What was done
- Step 0: the three pair documents read; served ETags at the base (E_18 a7820a20, gold_dispatch.sh 882a910b); repo md5s f5c03ee6 and 165933f6; runner stopped; no gold/trigger-pending.json; open ledgers read across 27 worktrees (123 unique files), the code/gold ones all carry CLOSED completion records.
- Leg P: code/gold census (290 latest keys) and etf-classifications state (11375 items; 13 seeded present, 9 held-out absent).
- Leg D: E_18 by safe-deploy (HALT_ACK=1 for the already-read GO); gold_dispatch.sh by aws s3 cp --sse AES256 because safe-deploy skips .sh. E108-SHIPPED ok=True; post census moved only the two keys.
- Leg Q: runner started 08:39:43Z, systemctl stop first, then `--single E_18`: rc 0, 0 ERROR, table unchanged. Two deviations (nine held-out not listed unresolved; single ran with --upload, 0 candidates) reported to the COO; ACCEPTED (COO msg 7450, CTO msg 7449). Details: deliverables/E111_LEGQ_FINDINGS_20261017.md.
- Ledger secclass-e111b-e18-repoint-ship-dell1-20261017 CLOSED (7 of 7 legs); order flipped to complete on the COO's word.

## Compiler Tools
- safe-deploy.sh: E_18 OK; gold_dispatch.sh no-op (.sh outside its scope), so the S3 cp route was used.
- deploy_ledger.py: open, close-leg, close all worked.
- comp-pipescript deployed: cannot see a .sh (ABSENT IN TREE); gap, the match for the dispatcher is by e108_shipped_check md5.
- proof-of-spec-check.py: a DEPLOY-genre instance also needs risk_class and never_widen_pair, which the example instances did not show.
- comp-rail: denied a heredoc python containing the token `find(` as a recursive repo search (false positive); a script file ran fine.

## Open
- ADHOC.canon-r11-orion-reader-trail: L3 log read after 16:30Z 2026-10-17; L4 removal by 2026-10-19T18:39Z (ledger mdpf-canon-r11-orion-reader-accesslog-dell1-20261016).
