# Deploy Completion Record
**Date opened:** 2026-06-26T16:48:12.877305+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260626T222254Z
**Deploy:** NFRA_MSGRAPH.S2 MS doc-cloud ingest GO-LIVE: gateway /ms/* read-only endpoint + /ms/health probe + derive extract_ms_cloud enable (CTO deploy-go 164447Z, COO window 164439Z)
**Authored by:** 0.8.0_AE_CloudComp
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 10.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | code+IaC committed+pushed CLOUD (extractor/cert/gateway/TF/readonly) | commit hashes pushed | commits fb625d0f5 (extractor+SS4 cert 11/11) + 5fd78e01e (gateway /ms/* + caller) + 1a23a3ed4 (gateway TF liveness) + cac16138a (read-only GET-pin) + fd4894fe4 (deploy plan), all pushed CLOUD | CLOSED 20260626T164936Z |
| L2 | activation | mint opal/mcp/ms-ingest-token secret out-of-band (value never in TF state) | secret ARN created | secret arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/mcp/ms-ingest-token-mXFTKk created out-of-band (boto3); retrievable (45-char value, never in TF state/logs) | CLOSED 20260626T164937Z |
| L3 | activation | gateway TF safe-apply: /ms/health liveness Lambda + IAM grant + bearer read | 0-diff plan + apply counts | safe-apply gateway TF: 6 added (ms-ingest liveness Lambda+IAM role/policy+EventBridge rule/target/permission), 1 changed (gw_golive policy +ms_ingest_bearer read), 0 destroyed -- live gateway untouched | CLOSED 20260626T165129Z |
| L4 | ec2-baked-asset | gateway code redeploy (ms_ingest.py + server/config) + .env MS_INGEST_BEARER/IDENTITY | /ms/health {ok:true} via bearer (token mints) | gateway redeployed (safe-ec2-deploy i-07dccb1615503ac99): on-box smoke active/health{ok:true}/AS-200/mcp-401. LIVE EXTERNAL PROOF: GET /ms/health+bearer={ok:true} (Andrew server-held delegated token MINTS), no-bearer=401, /ms/sites?q=opal=6 sites structure-only (no content/body key). ALB /ms/* OIDC-exempt rule applied (proven by the 200). | CLOSED 20260626T165808Z |
| L5 | activation | derive task-def env GLOBGRPH_MS_ENABLED=1 + MS_GATEWAY_BASE_URL + MS_INGEST_BEARER + image carries ms_cloud_extract | task-def revision + image digest | task-def globgrph-derive-runner:4 registered: GLOBGRPH_MS_ENABLED=1 + MS_GATEWAY_BASE_URL=https://mcp.opalinvest.dev (env) + MS_INGEST_BEARER (secret valueFrom) + execution-role GetSecretValue grant; nightly EventBridge target -> :4; :latest ECR image rebuilt via CodeBuild (carries ms_cloud_extract.py). safe-apply 2 added/2 changed/1 destroyed (task-def revision). | CLOSED 20260626T170457Z |
| L6 | verify | next SCHEDULED nightly (02:00 UTC) first MS-enabled run -> comp-kuzu n.source=ms first-class + AWS-count-unchanged superset (CTO step-6: validate on nightly artifacts, NOT ad-hoc) | comp-kuzu output post-nightly | MS estate LANDED via the off-cycle re-target derive e20c1250 (supersedes the nightly): comp-kuzu snapshot 3929343047371898635 ms=5422 first-class (MS_FILE 4399/FOLDER 1007/USER 14/SITE 1/LIBRARY 1, 0 UNCATEGORIZED, SS4 0-leak) + AWS-RESOURCE subset byte-identical (corrected COND-A, CVO 638ee9bc3). The /sites/Shared estate is queryable in Nessie/Iceberg/Kuzu | CLOSED 20260626T222253Z |

## Log

- 20260626T164812Z OPENED by 0.8.0_AE_CloudComp with 6 leg(s)
- 20260626T164936Z LEG L1 closed: commits fb625d0f5 (extractor+SS4 cert 11/11) + 5fd78e01e (gateway /ms/* + caller) + 1a23a3ed4 (gateway TF liveness) + ca
- 20260626T164937Z LEG L2 closed: secret arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/mcp/ms-ingest-token-mXFTKk created out-of-band (boto3);
- 20260626T165129Z LEG L3 closed: safe-apply gateway TF: 6 added (ms-ingest liveness Lambda+IAM role/policy+EventBridge rule/target/permission), 1 changed
- 20260626T165808Z LEG L4 closed: gateway redeployed (safe-ec2-deploy i-07dccb1615503ac99): on-box smoke active/health{ok:true}/AS-200/mcp-401. LIVE EXTER
- 20260626T170457Z LEG L5 closed: task-def globgrph-derive-runner:4 registered: GLOBGRPH_MS_ENABLED=1 + MS_GATEWAY_BASE_URL=https://mcp.opalinvest.dev (en
- 20260626T222253Z LEG L6 closed: MS estate LANDED via the off-cycle re-target derive e20c1250 (supersedes the nightly): comp-kuzu snapshot 39293430473718
- 20260626T222254Z CLOSED -- all 6 legs proven
