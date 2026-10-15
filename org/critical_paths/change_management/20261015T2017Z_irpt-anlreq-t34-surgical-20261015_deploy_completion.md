# Deploy Completion Record
**Date opened:** 2026-10-15T20:17:08.496052+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261015T202824Z
**Deploy:** IRPT_ANLREQ TO-APPLY-t34 amendment_1 (route B): SURGICAL zip sha256 hUZY39qNcHdJf0fgQRHS4ckuFBT+8rU/K7VhGscaeYc= (the fetched live zip xC1GDXXp with exactly 3 commentary members from pin 5b438cd6c4; 92 members) applied by one targeted safe-apply to teams-global-transcripts-pull-lambda, outlook-global-transcripts-pull-lambda, outlook-global-commentary-draft-lambda; then ONE read-only draft_exists invoke
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | the three proofs (i) three of three byte-equal to the pin, (ii) exactly 3 members differ from live, (iii) clean -I imports, plus addr_equal ADDR-EQUAL-OK | the printed proof lines and the surgical sha | proof-i 3 of 3 replaced members byte-equal to git blob at 5b438cd6c4 (lambda_handler c3d837ee, drafter a93987d2, entry c0deb153); proof-ii 92 members, exactly 3 differ from live; proof-iii three python -I imports OK from the extract outside the repo; addr_equal ADDR-EQUAL-OK teams=14/14 mail=7/7 control=discriminates; surgical zip 904953 bytes 92 members hUZY39qNcHdJf0fgQRHS4ckuFBT+8rU/K7VhGscaeYc= | CLOSED 20261015T202823Z |
| V2 | verify | plan 0/3/0 source_code_hash only; after reads: three CodeSha256 equal the surgical zip, sizes, env values and mapping unchanged | the printed reads | plan 0 to add 3 to change 0 to destroy, source_code_hash and last_modified only on each; after reads 20:23Z: all three CodeSha256 hUZY39qN..., MemorySize 1024 1024 512, Timeout 300 600 300 as at step 1, env NAMES the same 8, mapping 1 Enabled; env values evidenced unchanged by the plan, not compared | CLOSED 20261015T202824Z |
| V3 | verify | get_ref non-null then ONE invoke: stage draft_exists, failed empty, the INFO line present | the parsed response and the log line | get_ref status OK commentary_ref NON-NULL 20:24Z; ONE invoke 20:25:15Z to 20:25:26Z StatusCode 200 no FunctionError; parsed results[0].stage draft_exists, failed empty, batchItemFailures empty; log INFO line commentary draft exists request_id=REQ-d47252fe... present 20:25:26Z; REPORT 4175 ms; body 92 chars sha256 a86119437c56 | CLOSED 20261015T202824Z |
| teams-global-transcripts-pull-lambda | tf-lambda | aws_lambda_function.pull | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | safe-apply 0 added 3 changed 0 destroyed at 20:22Z (comp-tagauthz passed); targeted re-plan No changes 20:27Z; CodeSha256 hUZY39qNcHdJf0fgQRHS4ckuFBT+8rU/K7VhGscaeYc= equals the surgical zip's base64 sha256; served read of get-function-configuration 20:23Z, size and timeout unchanged | CLOSED 20261015T202823Z |
| outlook-global-transcripts-pull-lambda | tf-lambda | aws_lambda_function.mail_pull | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | safe-apply 0 added 3 changed 0 destroyed at 20:22Z (comp-tagauthz passed); targeted re-plan No changes 20:27Z; CodeSha256 hUZY39qNcHdJf0fgQRHS4ckuFBT+8rU/K7VhGscaeYc= equals the surgical zip's base64 sha256; served read of get-function-configuration 20:23Z, size and timeout unchanged | CLOSED 20261015T202823Z |
| outlook-global-commentary-draft-lambda | tf-lambda | aws_lambda_function.commentary | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | safe-apply 0 added 3 changed 0 destroyed at 20:22Z (comp-tagauthz passed); targeted re-plan No changes 20:27Z; CodeSha256 hUZY39qNcHdJf0fgQRHS4ckuFBT+8rU/K7VhGscaeYc= equals the surgical zip's base64 sha256; served read of get-function-configuration 20:23Z, size and timeout unchanged | CLOSED 20261015T202823Z |

## Log

- 20261015T201708Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 6 leg(s)
- 20261015T202823Z LEG teams-global-transcripts-pull-lambda closed: safe-apply 0 added 3 changed 0 destroyed at 20:22Z (comp-tagauthz passed); targeted re-plan No changes 20:27Z; CodeSha25
- 20261015T202823Z LEG outlook-global-transcripts-pull-lambda closed: safe-apply 0 added 3 changed 0 destroyed at 20:22Z (comp-tagauthz passed); targeted re-plan No changes 20:27Z; CodeSha25
- 20261015T202823Z LEG outlook-global-commentary-draft-lambda closed: safe-apply 0 added 3 changed 0 destroyed at 20:22Z (comp-tagauthz passed); targeted re-plan No changes 20:27Z; CodeSha25
- 20261015T202823Z LEG V1 closed: proof-i 3 of 3 replaced members byte-equal to git blob at 5b438cd6c4 (lambda_handler c3d837ee, drafter a93987d2, entry c
- 20261015T202824Z LEG V2 closed: plan 0 to add 3 to change 0 to destroy, source_code_hash and last_modified only on each; after reads 20:23Z: all three C
- 20261015T202824Z LEG V3 closed: get_ref status OK commentary_ref NON-NULL 20:24Z; ONE invoke 20:25:15Z to 20:25:26Z StatusCode 200 no FunctionError; par
- 20261015T202824Z CLOSED -- all 6 legs proven
