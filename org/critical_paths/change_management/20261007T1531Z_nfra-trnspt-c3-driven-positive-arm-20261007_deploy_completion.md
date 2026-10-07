# Deploy Completion Record
**Date opened:** 2026-10-07T15:31:14.966984+00:00
**Status:** OPEN
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
| L3 | verify | 2026-10-07T23:30Z scheduled fire | MAIL-PULL-FIRE line landed>=1 + EventBridge invocation; laptop fenced-read FILE |  | OPEN |
| L4 | activation | aws_lambda_function.mail_pull APPLY 2 (WINDOW_DAYS 7) | safe-apply plan 0/1/0 + rc |  | OPEN |
| L5 | verify | get-function-configuration + 2026-10-08T23:30Z fire line | WINDOW_DAYS 7 and window_days=7 |  | OPEN |

## Log

- 20261007T153114Z OPENED by 2.0.0_SA_COO~T2 with 5 leg(s)
- 20261007T153721Z LEG L1 closed: safe-apply rc=0 from clean worktree at 8f82af6281 applying saved plan c3-apply1.tfplan: Plan 0 to add, 1 to change, 0 to
- 20261007T153721Z LEG L2 closed: aws lambda get-function-configuration outlook-global-transcripts-pull-lambda read from dell2 after apply: CodeSha256 VGI
