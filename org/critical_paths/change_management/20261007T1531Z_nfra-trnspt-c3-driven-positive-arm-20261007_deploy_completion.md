# Deploy Completion Record
**Date opened:** 2026-10-07T15:31:14.966984+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T233341Z
**Deploy:** NFRA_TRNSPT C3: mail pull code (C1+C2) + WINDOW_DAYS 7->60 for the 2026-10-07T23:30Z scheduled fire, then back to 7. Halves: COO @5eaf7966af, CTO @d450f6664b. APPLY 2 seat: 2.0.0_SA_COO~T2 at ~2026-10-07T23:50Z after grading; fallback 1.0.0_SA_CTO~DELL2 before 2026-10-08T23:00Z
**Authored by:** 2.0.0_SA_COO~T2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 36.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | aws_lambda_function.mail_pull APPLY 1 (code VGIq..., WINDOW_DAYS 60) | safe-apply plan 0/1/0 + rc | safe-apply rc=0 from clean worktree at 8f82af6281 applying saved plan c3-apply1.tfplan: Plan 0 to add, 1 to change, 0 to destroy (source_code_hash teSt...->VGIq..., WINDOW_DAYS 7->60); 2026-10-07T15:34:46Z | CLOSED 20261007T153721Z |
| L2 | verify | get-function-configuration | CodeSha256 VGIq85Xxm5KVLCnv16BASS63RsPMHScMEwZJP5SuMNY= and WINDOW_DAYS 60 | aws lambda get-function-configuration outlook-global-transcripts-pull-lambda read from dell2 after apply: CodeSha256 VGIq85Xxm5KVLCnv16BASS63RsPMHScMEwZJP5SuMNY=, CodeSize 478258, WINDOW_DAYS 60, LastModified 2026-10-07T15:34:46Z, LastUpdateStatus Successful | CLOSED 20261007T153721Z |
| L3 | verify | 2026-10-07T23:30Z scheduled fire | MAIL-PULL-FIRE line landed>=1 + EventBridge invocation; laptop fenced-read FILE | r4_c3_grade.py at 2026-10-07T23:38Z from dell2: C3-FIRE-OK run=20261007T233013Z window_days=60 listed=100 admitted=3 landed=12 skipped_known=1 list_refusals=0 silver_rows=3 held_out=3; C3-SCHEDULED-OK starts=1 at_cron_slot=1 invocations_metric=1; C3-BRONZE-OK messages=3 objects_checked=9 hashes_equal=9; C3-SILVER rows=3 held_out=3. landed_dates 2026-09-02, 2026-09-15, 2026-09-17 (the 2026-08-11 target did not land: row NFRA_TRNSPT-D2-S2) | CLOSED 20261008T000142Z |
| L4 | activation | aws_lambda_function.mail_pull APPLY 2 (WINDOW_DAYS 7) | safe-apply plan 0/1/0 + rc | safe-apply rc=0 at 2026-10-07T23:59:05Z by 2.0.0_SA_COO~T2: plan 0/1/0 (WINDOW_DAYS 60->7 only; main.tf taken from HEAD so the laptop's key policy 74320c91b2 is not reverted -- the first APPLY 2 plan read 0/2/0 including aws_kms_key.transcripts and was NOT applied); read back WINDOW_DAYS 7, CodeSha256 VGIq85Xxm5KVLCnv16BASS63RsPMHScMEwZJP5SuMNY= unchanged, Successful | CLOSED 20261008T000142Z |
| L5 | verify | get-function-configuration + 2026-10-08T23:30Z fire line | WINDOW_DAYS 7 and window_days=7 | get-function-configuration WINDOW_DAYS=7 CodeSha256 VGIq85Xx...MNY= (unchanged); CloudWatch 23:30:34Z MAIL-PULL-FIRE run=20261008T233013Z window_days=7 listed=12 admitted=0 landed=0; 1 invocation (EventBridge outlook-global-transcripts-pull-daily cron(30 23 * * ? *) ENABLED); read by 2.0.0_SA_COO~T2 2026-10-08T23:3xZ | CLOSED 20261008T233341Z |

## Log

- 20261007T153114Z OPENED by 2.0.0_SA_COO~T2 with 5 leg(s)
- 20261007T153721Z LEG L1 closed: safe-apply rc=0 from clean worktree at 8f82af6281 applying saved plan c3-apply1.tfplan: Plan 0 to add, 1 to change, 0 to
- 20261007T153721Z LEG L2 closed: aws lambda get-function-configuration outlook-global-transcripts-pull-lambda read from dell2 after apply: CodeSha256 VGI
- 20261008T000142Z LEG L3 closed: r4_c3_grade.py at 2026-10-07T23:38Z from dell2: C3-FIRE-OK run=20261007T233013Z window_days=60 listed=100 admitted=3 lan
- 20261008T000142Z LEG L4 closed: safe-apply rc=0 at 2026-10-07T23:59:05Z by 2.0.0_SA_COO~T2: plan 0/1/0 (WINDOW_DAYS 60->7 only; main.tf taken from HEAD 
- 20261008T233341Z LEG L5 closed: get-function-configuration WINDOW_DAYS=7 CodeSha256 VGIq85Xx...MNY= (unchanged); CloudWatch 23:30:34Z MAIL-PULL-FIRE run
- 20261008T233341Z CLOSED -- all 5 legs proven
