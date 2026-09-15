# Deploy Completion Record
**Date opened:** 2026-09-15T03:43:51.686945+00:00
**Status:** OPEN
**Deploy:** POSN_ASTTAX B6: characteristics.json gains the tickers block; rule to cron(30 12 * * ? *); driven run
**Authored by:** 0.9.0_WK_POSN_ASTTAX~24
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | SITEZ commit of producer + build_package + tf | hash | git commit 2a62019b637d17dfcc100763030a2d530a18235e on wk-posn_asttax-6-24 (LOCAL): producer + build_package + .tf + 10 rows + deliverables; verified by git log -1 --format=%h~%an~%s 2a62019b63 with a bogus-hash negative control | CLOSED 20260915T044414Z |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts cot-pipeline/cot-satellites-characteristics-producer.zip | VersionId + content-sha256 read back | s3api head-object READ BACK (not the put response): opal-313476888478-lambda-artifacts/cot-pipeline/cot-satellites-characteristics-producer.zip VersionId ZM8X7mpXR6zBymgcjMx_hO.Dw9FBzyIw, ContentLength 180046 == local zip bytes, Metadata content-sha256 rN/jcmeQk4F/HJsQHfasjdWFgIjWXOrYHeBPkf5TbOU= == locally computed base64 sha256; PRIOR version sZ0o.m4CGbylNMV7KPN1oR9bgRZnlEml (36184 B) kept as the rollback | CLOSED 20260915T044414Z |
| L3 | verify | targeted plan | 0 add / 3 change / 0 destroy | targeted plan saved to C:/tmp/wk-posn-6-24/.scratch/b6.tfplan: 'Plan: 0 to add, 3 to change, 0 to destroy' -- rule schedule_expression cron(20 7 * * ? *) -> cron(30 12 * * ? *); policy +3 Sids (ListBloombergHistoryPrefixes conditioned to bbg/* and bbg-testpull/tickers/*, ReadBloombergReturnHistory, ReadEtfClassifications dynamodb:GetItem only) with 2 unchanged elements hidden + ReadBloombergEtfDaily + WriteSatellitesCharacteristics unchanged; function s3_object_version sZ0o... -> ZM8X7mpXR6zBymgcjMx_hO.Dw9FBzyIw and source_code_hash -> rN/jcmeQk4F/HJsQHfasjdWFgIjWXOrYHeBPkf5TbOU= | CLOSED 20260915T045215Z |
| L4 | activation | safe-apply | summary + HALTGT | safe-apply.sh: 'Apply complete! Resources: 0 added, 3 changed, 0 destroyed'; HALTGT line 1 'HALT-GATE: worker 0.9.0_WK_POSN_ASTTAX~24 has no inbox; scanning its issuer 2.0.0_SA_COO~Z'; comp-tagauthz gate PASSED (0 candidates carry an authorization tag); tombstone-gate CLEAN (0 creates vs 7 tombstones); LIVE PLANE (second instrument) lambda get-function-configuration CodeSha256 rN/jcmeQk4F/HJsQHfasjdWFgIjWXOrYHeBPkf5TbOU= == the uploaded content-sha256, LastModified 2026-09-15T04:50:51Z, memory 512, timeout 120 | CLOSED 20260915T045216Z |
| L5 | verify | unscoped 0-diff | No changes | unscoped terraform plan on the whole cot-pipeline root: 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260915T045551Z |
| L6 | verify | driven invoke with explicit bbg_as_of lands the tickers block | VersionId moved + block read back | driven invoke {bbg_as_of: 2026-09-11}: StatusCode 200, no FunctionError, body rc 0; served VersionId MOVED rt61ogajZQy79meUlsY1X_mIdPngxJTZ -> 74d9.pGWF16Ox7cXKGax.zQw.lhwi5yI (54825 -> 67782 B) at 2026-09-15T04:53:42Z; served tickers block DEEP-EQUAL to the local dry run (25 of 25, identity pair 25 of 25, identity_missing 0) and the WHOLE served document DEEP-EQUAL to the local dry run minus as_of; in-Lambda REPORT Duration 39407 ms of 120000 ms, Max Memory Used 270 MB of 512 MB | CLOSED 20260915T045552Z |
| L7 | verify | rule cron(30 12 * * ? *) ENABLED with the function as target | describe-rule + list-targets | events describe-rule cot-satellites-characteristics-producer-daily: {state: ENABLED, expr: cron(30 12 * * ? *)}; list-targets-by-rule: ONE target CotSatellitesCharacteristicsProducerDaily -> arn:aws:lambda:us-east-1:313476888478:function:cot-satellites-characteristics-producer | CLOSED 20260915T045618Z |
| L8 | verify | first scheduled 12:30Z fire lands organically (the negative arm; recorded by the COO, not waited on here) | s3api head after the fire |  | OPEN |
| L9 | git | deploy recorded: source map + CHANGELOG entry by hand | git show --stat | deploy recorded and git-VERIFIED: git show --stat 9633bb9e7e lists infra/aws/lambda/ci/lambda-source-map.json (last_deployed_commit 2a62019b63, deployed_code_sha256 rN/jcmeQk4F/HJsQHfasjdWFgIjWXOrYHeBPkf5TbOU=, deploy_ledger posn-round6-b6-characteristics-tickers; the earlier a031c56c74 left the sha stale and was corrected by a re-run with --code-sha256); the CHANGELOG.json entry written BY HAND in the helper's 10-key shape at commit 3c5c3bba93 (entries 12 -> 13, non-ASCII 18 before and 18 after, trailing newline kept) -- the recorder's own CHANGELOG limb raised SyntaxError because JSON_TOOL fell through to python and was handed its .js | CLOSED 20260915T051903Z |

## Log

- 20260915T034351Z OPENED by 0.9.0_WK_POSN_ASTTAX~24 with 9 leg(s)
- 20260915T044414Z LEG L1 closed: git commit 2a62019b637d17dfcc100763030a2d530a18235e on wk-posn_asttax-6-24 (LOCAL): producer + build_package + .tf + 10 
- 20260915T044414Z LEG L2 closed: s3api head-object READ BACK (not the put response): opal-313476888478-lambda-artifacts/cot-pipeline/cot-satellites-chara
- 20260915T045215Z LEG L3 closed: targeted plan saved to C:/tmp/wk-posn-6-24/.scratch/b6.tfplan: 'Plan: 0 to add, 3 to change, 0 to destroy' -- rule sched
- 20260915T045216Z LEG L4 closed: safe-apply.sh: 'Apply complete! Resources: 0 added, 3 changed, 0 destroyed'; HALTGT line 1 'HALT-GATE: worker 0.9.0_WK_P
- 20260915T045551Z LEG L5 closed: unscoped terraform plan on the whole cot-pipeline root: 'No changes. Your infrastructure matches the configuration.'
- 20260915T045552Z LEG L6 closed: driven invoke {bbg_as_of: 2026-09-11}: StatusCode 200, no FunctionError, body rc 0; served VersionId MOVED rt61ogajZQy79
- 20260915T045618Z LEG L7 closed: events describe-rule cot-satellites-characteristics-producer-daily: {state: ENABLED, expr: cron(30 12 * * ? *)}; list-ta
- 20260915T051903Z LEG L9 closed: deploy recorded and git-VERIFIED: git show --stat 9633bb9e7e lists infra/aws/lambda/ci/lambda-source-map.json (last_depl
