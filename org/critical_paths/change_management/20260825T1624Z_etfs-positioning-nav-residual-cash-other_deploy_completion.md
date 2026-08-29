# Deploy Completion Record
**Date opened:** 2026-08-25T16:24:49.106684+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260825T163150Z
**Deploy:** ETFS_POSITIONING: itemize the unaccounted NAV residual (CASH_OTHER row) on DIVZ/IDVZ -- Andrew-direct 2026-08-25, deploy + ad-hoc republish authorized
**Authored by:** 1.0.0_SA_CTO~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | SITEZ commit 83d3ca4592 (rides integrator push) | hash + branch | SITEZ 83d3ca4592 author 1.0.0_SA_CTO~Z, commit-gate clean, msg-verify MATCH len=5310. LANDED LOCAL -- push is integrator-only (LD-0367), rides 0.0.0_AB_MSTR~Z's window. Not claimed as on-origin. | CLOSED 20260825T163150Z |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts etfs-positioning/etf-positioning-producer.zip | uploaded sha256 + content-sha256 metadata | PUT opal-313476888478-lambda-artifacts/etfs-positioning/etf-positioning-producer.zip VersionId S0WElFWL5rpz1iZbW5T9QHU7q58DcvyJ, 34880 B. head-object Metadata content-sha256=4t99XarK6THSEdSFjSIeNlRk6SxgQVK+VfAjvqRLv7g= (verified on the live primitive, not assumed from the put). Zip is DETERMINISTIC -- in-memory rebuild digest identical. | CLOSED 20260825T163150Z |
| L3 | activation | module.etf_positioning_producer TF apply | apply 0-destroy + 0-diff replan + deployed CodeSha256 == uploaded sha | safe-apply (terraform 1.15.8 resolved on PATH -- no .tools/terraform.exe on site Z, Rule 26). Plan 0 add / 1 change / 0 destroy, code-only: source_code_hash p/mc7hvScGyYxxMK9QY7qWQQ3gZqsWvH/GbJQVIbnvY= -> 4t99XarK6THSEdSFjSIeNlRk6SxgQVK+VfAjvqRLv7g=, s3_object_version d2hwnUDf -> S0WElFWL, 28 attrs unchanged (Rule 5 untouched). Apply rc=0 'Resources: 0 added, 1 changed, 0 destroyed'. RE-PLAN -detailed-exitcode rc=0 (rc captured BEFORE any pipe) = No changes. | CLOSED 20260825T163150Z |
| L4 | verify | deployed package member carries CASH_OTHER (token controls) | download package, sha==live CodeSha256, positive+negative token controls | ACCEPTANCE ON DEPLOYED BYTES: package downloaded from Code.Location, zip sha256 b64 == live CodeSha256 == uploaded b64 (4t99XarK...), so it IS the running artifact. Member etf_positioning_gold.py 60899 -> 68875 B. TOKEN CONTROLS 6/6: CASH_OTHER, 'Cash & Other Assets', synthesized_residual, fund_net_assets, ULTRA_SHORT_SUB_ASSET_CLASS all PRESENT; negative control zzz_no_such_token_9999 ABSENT. PRE-DEPLOY DRIFT CHECK: live bytes were byte-identical (sha256) to tree HEAD~1, so no other seat's work was clobbered. | CLOSED 20260825T163150Z |
| L5 | activation | ad-hoc producer run (publish) -- ANDREW-AUTHORIZED republish | invoke rc + run manifest | ANDREW-AUTHORIZED republish ('yes i want it republished'). invoke RequestResponse StatusCode=200 FunctionError=null. run_class=adhoc (honest -- classify_run returns adhoc for a non-aws.events event). gold: objects_written=2, holding_rows=189, synthesized_residual_rows=2. platinum: status=published. as_of 2026-08-24, trading_days_behind=1 (healthy T-1, NEVER#1). | CLOSED 20260825T163150Z |
| L6 | verify | served platinum/etfs/positioning_data.json shows DIVZ/IDVZ summing 100.00 | live S3 read of the served artifact, both panels' figures | SERVED platinum/etfs/positioning_data.json 13:01:23Z/126788B/ETag b3e1ad04 -> 16:30:30Z/128027B/ETag 5a7b7a47, generated_at 2026-08-25T16:30:28Z. TIE-OUT ON SERVED BYTES, 4/4 books tie: DIVZ FI 0.78 EQ 99.22 TOT 100.00; IDVZ FI 1.38 EQ 98.62 TOT 100.00; PFDE 100.01; PFOE 99.99 (issuer's own +-1bp, unchanged by design). Residual rows served: DIVZ CASH_OTHER 0.20pct, IDVZ 0.49pct, both Fixed Income / Ultra Short Duration. NEGATIVE CONTROL: 0 CASH_OTHER rows on PFDE/PFOE (they carry issuer cash lines). | CLOSED 20260825T163150Z |

## Log

- 20260825T162449Z OPENED by 1.0.0_SA_CTO~Z with 6 leg(s)
- 20260825T163150Z LEG L1 closed: SITEZ 83d3ca4592 author 1.0.0_SA_CTO~Z, commit-gate clean, msg-verify MATCH len=5310. LANDED LOCAL -- push is integrator
- 20260825T163150Z LEG L2 closed: PUT opal-313476888478-lambda-artifacts/etfs-positioning/etf-positioning-producer.zip VersionId S0WElFWL5rpz1iZbW5T9QHU7q
- 20260825T163150Z LEG L3 closed: safe-apply (terraform 1.15.8 resolved on PATH -- no .tools/terraform.exe on site Z, Rule 26). Plan 0 add / 1 change / 0 
- 20260825T163150Z LEG L4 closed: ACCEPTANCE ON DEPLOYED BYTES: package downloaded from Code.Location, zip sha256 b64 == live CodeSha256 == uploaded b64 (
- 20260825T163150Z LEG L5 closed: ANDREW-AUTHORIZED republish ('yes i want it republished'). invoke RequestResponse StatusCode=200 FunctionError=null. run
- 20260825T163150Z LEG L6 closed: SERVED platinum/etfs/positioning_data.json 13:01:23Z/126788B/ETag b3e1ad04 -> 16:30:30Z/128027B/ETag 5a7b7a47, generated
- 20260825T163150Z CLOSED -- all 6 legs proven
