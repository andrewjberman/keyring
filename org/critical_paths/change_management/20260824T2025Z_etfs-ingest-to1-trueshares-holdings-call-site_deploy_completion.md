# Deploy Completion Record
**Date opened:** 2026-08-24T20:25:09.802046+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260824T220441Z
**Deploy:** ETFS_INGEST.TO-1 -- deploy the TrueShares holdings CALL SITE (@4e5800fde0) to etfs-netassets-daily; TF-only, zero new code. Closes PRD F2 / Z-S1.
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | lambda artifact zip -> s3://opal-313476888478-lambda-artifacts/etfs-netassets/etfs-netassets-daily.zip | build-and-upload write-verify: ContentLength + content-sha256 metadata match | build-and-upload.sh etfs-netassets etfs-netassets-daily -> s3://opal-313476888478-lambda-artifacts/etfs-netassets/etfs-netassets-daily.zip WRITE VERIFIED (size=19948, content-sha256 metadata match). New artifact sha256=BEITykjhmRlEvcM8p9cBUFmKX7doqEP+jHGRPhOprxo= (prior tHeVS53pKxV4hX9UXciJsigvO8t5v10T3CmN2VwQURI=). | CLOSED 20260824T202620Z |
| L2 | git | source-map commit: artifact_sha256 + last_deployed_commit + last_deployed_at (3 fields, Rule 4) | commit hash, landed LOCAL | Source map 3 fields (Rule 4/AC2): artifact_sha256 -> BEITykjhmRlEvcM8p9cBUFmKX7doqEP+jHGRPhOprxo=; last_deployed_commit e45606d461 -> 4e5800fde0; last_deployed_at 2026-07-15T23:35:40Z -> 2026-08-24T20:35:52Z (+_last_deploy_recorded). Commits aaec8e05c6 then d6e5fbe667 (fix-forward: my own recorder run flipped LF->CRLF and churned 8 other-lane serialization lines; rebuilt from parent after PROVING a lossless round-trip). NET diff pre-deploy-parent -> HEAD = 8 lines = exactly the 4 fields. LANDED LOCAL, rides integration -- NOT pushed. | CLOSED 20260824T204223Z |
| L3 | activation | terraform apply via .tools/safe-apply.sh in infra/aws/terraform/etfs-netassets/ (NEVER#4) | apply output + new live CodeSha256 | safe-apply.sh -chdir=infra/aws/terraform/etfs-netassets apply (HALT_ACK=1 after reviewing 2 routine pending msgs, neither a STOP). Apply complete: 0 added, 1 changed, 0 destroyed. Only aws_lambda_function.this in-place: source_code_hash tHeVS53p...URI= -> BEITykjhmRlEvcM8p9cBUFmKX7doqEP+jHGRPhOprxo=. No IAM/schedule/alarm change. | CLOSED 20260824T203207Z |
| L4 | verify | 0-diff re-plan -detailed-exitcode rc=0 in the OWNING root infra/aws/terraform/etfs-netassets/ | measured rc, not eyeballed | terraform plan -detailed-exitcode in OWNING root infra/aws/terraform/etfs-netassets/ -> rc=0 (No changes), rc captured directly with NO pipe. | CLOSED 20260824T203207Z |
| L5 | verify | AC3 post-deploy per-member CRLF-NORMALIZED package re-census, BOTH members, + explicit CRLF statement | member sha256 vs applied-commit blobs; fetch_trueshares_holdings >=3 | Re-downloaded from Code.Location; zip sha256=BEITykjhmRlEvcM8p9cBUFmKX7doqEP+jHGRPhOprxo= == live CodeSha256 (so these ARE the running bytes). PER MEMBER vs HEAD blobs resolved through source-map files[]: lambda_function.py 51885B RAW MATCH e6f9fe5391da...; landing_guard.py 5998B RAW MATCH a715b04be314.... AC3(d) CRLF STATEMENT: the NEW package is LF, NOT CRLF -- both members match RAW, so Z-S4 does not recur for this artifact. Call site PRESENT :550/:552, SKIP :559; fetch_trueshares_holdings 1->3; lines 1083->1126; control fetch_filepoint 3->4; negative control 0. | CLOSED 20260824T203421Z |
| L6 | verify | AC4 EXERCISED on the SCHEDULED cron(0 22) fire -- bronze DIVZ/IDVZ non-empty + silver gains DIVZ/IDVZ rows | scheduled-invocation CloudWatch log stream, NOT an ad-hoc run | EXERCISED on the SCHEDULED cron(0 22) fire. Log stream 2026/08/24/[$LATEST]25ae2df9e21247ff9868c0dcf1089251, first event 22:00:08.209Z (8s after cron time), RequestId 5ec70c09-1b87-4cb7-971c-6ae755ad2715, Duration 7800.26ms, 1024MB/252MB used. Pre-fire baseline had NO 2026/08/24 stream and this is the only one. Log carries the DEPLOYED code's own lines: 'OK: [divz] trueshares holdings captured: 29 row(s)' and '[idvz] ... 44 row(s)' -- absent from the old bytes by construction (no call site). BRONZE: DIVZ 0->1 (divz_holdings.csv 2705B 22:00:11Z), IDVZ 0->1 (idvz_holdings.csv 4026B 22:00:12Z), both INSIDE the invocation window; sibling control netassets 40->41 each; negative control ZZZNOFUND 0. SILVER: 2026-08-24.parquet 21073B 22:00:17Z, rows 114->187, DIVZ 0->29, IDVZ 0->44, PFDE 90->90 and PFOE 24->24 UNCHANGED (no regression to the working product). Arithmetic reconciles: 29+44=73, 114+73=187. NO ad-hoc invoke was fired at any point. | CLOSED 20260824T220416Z |
| L7 | git | tag etfs-netassets-v1.4.0 (Deployment Rule 6) | annotated tag, landed LOCAL, rides integration | Annotated tag etfs-netassets-v1.4.0 created (rc=0), predecessors v1.0.0-v1.3.0. LANDED LOCAL, rides MSTR~Z integration -- NOT pushed (LD-0367 integrator-only). | CLOSED 20260824T204223Z |

## Log

- 20260824T202509Z OPENED by 0.7.0_AE_CloudOps~Z with 7 leg(s)
- 20260824T202620Z LEG L1 closed: build-and-upload.sh etfs-netassets etfs-netassets-daily -> s3://opal-313476888478-lambda-artifacts/etfs-netassets/etfs-n
- 20260824T203207Z LEG L3 closed: safe-apply.sh -chdir=infra/aws/terraform/etfs-netassets apply (HALT_ACK=1 after reviewing 2 routine pending msgs, neithe
- 20260824T203207Z LEG L4 closed: terraform plan -detailed-exitcode in OWNING root infra/aws/terraform/etfs-netassets/ -> rc=0 (No changes), rc captured d
- 20260824T203421Z LEG L5 closed: Re-downloaded from Code.Location; zip sha256=BEITykjhmRlEvcM8p9cBUFmKX7doqEP+jHGRPhOprxo= == live CodeSha256 (so these A
- 20260824T204223Z LEG L2 closed: Source map 3 fields (Rule 4/AC2): artifact_sha256 -> BEITykjhmRlEvcM8p9cBUFmKX7doqEP+jHGRPhOprxo=; last_deployed_commit 
- 20260824T204223Z LEG L7 closed: Annotated tag etfs-netassets-v1.4.0 created (rc=0), predecessors v1.0.0-v1.3.0. LANDED LOCAL, rides MSTR~Z integration -
- 20260824T220416Z LEG L6 closed: EXERCISED on the SCHEDULED cron(0 22) fire. Log stream 2026/08/24/[$LATEST]25ae2df9e21247ff9868c0dcf1089251, first event
- 20260824T220441Z CLOSED -- all 7 legs proven
