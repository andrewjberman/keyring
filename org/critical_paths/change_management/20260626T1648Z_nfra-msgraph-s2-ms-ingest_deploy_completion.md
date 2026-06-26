# Deploy Completion Record
**Date opened:** 2026-06-26T16:48:12.877305+00:00
**Status:** OPEN
**Deploy:** NFRA_MSGRAPH.S2 MS doc-cloud ingest GO-LIVE: gateway /ms/* read-only endpoint + /ms/health probe + derive extract_ms_cloud enable (CTO deploy-go 164447Z, COO window 164439Z)
**Authored by:** 0.8.0_AE_CloudComp
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 10.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

> **BY-DESIGN SPANNING NOTE (COO-confirmed 165226Z + CTO 165007Z):** the L6 validation leg is GATED ON THE 02:00 UTC SCHEDULED NIGHTLY by design -- this is the ONE legit exception to close-in-session. Steps 1-5 (deploy activation) land MS-ENABLED tonight; the nightly is the FIRST MS-enabled derive (NO ad-hoc manual run -- NEVER#4 validate-on-scheduled-nightly). L6 + close happen post-nightly-validate ~tomorrow AM. **NOT stranded** -- the deploy is fully landed; only the scheduled-nightly content-validation is pending. COO flags this in /drive so `--red` reads it as by-design-spanning, not a half-landed alarm.

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | code+IaC committed+pushed CLOUD (extractor/cert/gateway/TF/readonly) | commit hashes pushed | commits fb625d0f5 (extractor+SS4 cert 11/11) + 5fd78e01e (gateway /ms/* + caller) + 1a23a3ed4 (gateway TF liveness) + cac16138a (read-only GET-pin) + fd4894fe4 (deploy plan), all pushed CLOUD | CLOSED 20260626T164936Z |
| L2 | activation | mint opal/mcp/ms-ingest-token secret out-of-band (value never in TF state) | secret ARN created | secret arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/mcp/ms-ingest-token-mXFTKk created out-of-band (boto3); retrievable (45-char value, never in TF state/logs) | CLOSED 20260626T164937Z |
| L3 | activation | gateway TF safe-apply: /ms/health liveness Lambda + IAM grant + bearer read | 0-diff plan + apply counts | safe-apply gateway TF: 6 added (ms-ingest liveness Lambda+IAM role/policy+EventBridge rule/target/permission), 1 changed (gw_golive policy +ms_ingest_bearer read), 0 destroyed -- live gateway untouched | CLOSED 20260626T165129Z |
| L4 | ec2-baked-asset | gateway code redeploy (ms_ingest.py + server/config) + .env MS_INGEST_BEARER/IDENTITY | /ms/health {ok:true} via bearer (token mints) |  | OPEN |
| L5 | activation | derive task-def env GLOBGRPH_MS_ENABLED=1 + MS_GATEWAY_BASE_URL + MS_INGEST_BEARER + image carries ms_cloud_extract | task-def revision + image digest |  | OPEN |
| L6 | verify | next SCHEDULED nightly (02:00 UTC) first MS-enabled run -> comp-kuzu n.source=ms first-class + AWS-count-unchanged superset (CTO step-6: validate on nightly artifacts, NOT ad-hoc) | comp-kuzu output post-nightly |  | OPEN |

## Log

- 20260626T164812Z OPENED by 0.8.0_AE_CloudComp with 6 leg(s)
- 20260626T164936Z LEG L1 closed: commits fb625d0f5 (extractor+SS4 cert 11/11) + 5fd78e01e (gateway /ms/* + caller) + 1a23a3ed4 (gateway TF liveness) + ca
- 20260626T164937Z LEG L2 closed: secret arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/mcp/ms-ingest-token-mXFTKk created out-of-band (boto3);
- 20260626T165129Z LEG L3 closed: safe-apply gateway TF: 6 added (ms-ingest liveness Lambda+IAM role/policy+EventBridge rule/target/permission), 1 changed
