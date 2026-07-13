# Deploy Completion Record
**Date opened:** 2026-07-13T22:35:06.336013+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260713T224721Z
**Deploy:** ETF net-assets LAPTOP -> CLOUD: etfs-netassets-daily Lambda (bronze-first, Rule 17a) + IAM + EventBridge 22:00Z + error/absence alarms. PARITY PHASE: silver -> _cloudprobe/ scratch; laptop task STAYS ON.
**Authored by:** 0.5.0_AE_OpalETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of lambda_function.py + terraform + source-map | commit hash pushed | 00484e0f5 pushed to origin/CLOUD (verified: git branch -r --contains HEAD -> origin/CLOUD) | CLOSED 20260713T224720Z |
| L2 | s3-prefix | artifact zip -> s3://opal-313476888478-lambda-artifacts/etfs-netassets/etfs-netassets-daily.zip | upload verified by head-object size+etag | head-object s3://opal-313476888478-lambda-artifacts/etfs-netassets/etfs-netassets-daily.zip = 11482 bytes + metadata content-sha256=f1WQyBKDj1Nym44j8bPnd05klSTF36/HIKBdGZsiaR8= (built by canonical ci/build-and-upload.sh). NOTE: a first hand-rolled cp printed rc=0 while the upload had FAILED (pipe masked aws's rc); the head-object gate caught the 404 -- rc was never the proof. | CLOSED 20260713T224721Z |
| L3 | activation | terraform apply via safe-apply -> Lambda + role + EventBridge rule + 2 alarms | 0-diff plan after apply | safe-apply: Apply complete! 10 added, 0 changed, 0 destroyed. Follow-up terraform plan = 'No changes. Your infrastructure matches the configuration.' (0-diff) | CLOSED 20260713T224721Z |
| L4 | verify | LIVE INVOKE: function imports the py311 pandas/pyarrow layer AND writes bronze raw + silver scratch (DEPLOYED = DOWNLOADED *AND IMPORTED*) | invoke rc=0 + head-object on a bronze key + a _cloudprobe silver key | LIVE INVOKE StatusCode=200, no FunctionError -> py311 pandas/pyarrow layer IMPORTED (it wrote parquet). Verified ON S3, not on the self-report: bronze/ = 4 RAW objects (divz.html 451.2KiB, idvz.html 246.5KiB, ETF_Holdings.csv 13.7KiB, DailyNAV.csv 539B; no .parquet under bronze/); _cloudprobe/ = 5 silver objects. CONTROL: live silver/netassets/2026-07-13.parquet still carries the LAPTOP's 18:00:09 stamp, NOT the 18:44 invoke -- quarantine holds, laptop still the producer. PARITY DAY 1/3 on the artifact: 52 fields, 0 mismatches, sum(net_assets) delta 0.00; 0 columns dropped, +staleness_days. AC10 (bronze-alone re-derive, network cut): 32 fields 0 diff; mutant control FAILS correctly. | CLOSED 20260713T224721Z |

## Log

- 20260713T223506Z OPENED by 0.5.0_AE_OpalETL with 4 leg(s)
- 20260713T224720Z LEG L1 closed: 00484e0f5 pushed to origin/CLOUD (verified: git branch -r --contains HEAD -> origin/CLOUD)
- 20260713T224721Z LEG L2 closed: head-object s3://opal-313476888478-lambda-artifacts/etfs-netassets/etfs-netassets-daily.zip = 11482 bytes + metadata con
- 20260713T224721Z LEG L3 closed: safe-apply: Apply complete! 10 added, 0 changed, 0 destroyed. Follow-up terraform plan = 'No changes. Your infrastructur
- 20260713T224721Z LEG L4 closed: LIVE INVOKE StatusCode=200, no FunctionError -> py311 pandas/pyarrow layer IMPORTED (it wrote parquet). Verified ON S3, 
- 20260713T224721Z CLOSED -- all 4 legs proven
