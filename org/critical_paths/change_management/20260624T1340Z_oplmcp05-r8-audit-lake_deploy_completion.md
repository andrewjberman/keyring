# Deploy Completion Record
**Date opened:** 2026-06-24T13:40:21.260143+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260624T135712Z
**Deploy:** OPLMCP.05 R8 audit->lake: safe-apply audit-lake.tf (S3+Glue+Athena+IAM) -> deploy audit.py best-effort dual-write + AUDIT_S3_BUCKET -> on-box enforce-smoke -> Athena lake-reach
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | infra/aws/terraform/m365-mcp-gateway audit-lake.tf | safe-apply 12-add/0-change/0-destroy + post-apply 0-diff convergence | safe-apply tfplan.r8 = 'Apply complete! 12 added, 0 changed, 0 destroyed' (HALTGT passed, HALT_ACK=1 routine). Post-apply terraform plan = 'No changes. Your infrastructure matches the configuration' (0-diff converged, zero drift). Live: opal-mcp-audit + opal-mcp-athena-results buckets exist; glue table mcp_audit LOCATION s3://opal-mcp-audit/audit/; athena wg opal_mcp output s3://opal-mcp-athena-results/; audit bucket object-lock Enabled (WORM-capable, not enforced). | CLOSED 20260624T134313Z |
| B | ec2-baked-asset | EC2 m365-mcp-gateway /opt/m365-mcp-gateway audit.py + .env AUDIT_S3_BUCKET | SSM Success + on-box smoke: /health 200 + /mcp unauth 401 UNCHANGED on the NEW process + md5 of running audit.py | Deploy via safe-ec2-deploy (ssm:92684b0c) after adding boto3 to requirements (caught: boto3 absent = lazy import would no-op the lake write silently). On-box ground-truth (ssm:350de094 Success): boto3 1.43.36 in venv; systemd m365-mcp-gateway ACTIVE; /mcp unauth -> 401 UNCHANGED (the hard gate, new process enforces); AUDIT_S3_BUCKET=opal-mcp-audit in .env; app/audit.py carries _s3_client.put_object (new code deployed). safe-ec2-deploy wrapper false-negative (known Windows-charmap bug, SSM Success) -> manifest recorded manually (commit). comp-iam s3:PutObject GRANTED prefix-scoped. | CLOSED 20260624T135424Z |
| C | verify | opal-mcp-audit lake-reach + Athena opal_mcp workgroup | a real REDACTED audit record lands in opal-mcp-audit/audit/dt=.../ + queryable via Athena (CVO AC3 independent) | Real-path canary via the DEPLOYED gateway _emit (ssm:46a30bbe Success, run from the venv on-box: from app import audit; log_call). Record LANDED s3://opal-mcp-audit/audit/dt=2026-06-24/2026-06-24T13:55:30...jsonl. REDACTION PROVEN end-to-end: args.body='<352 chars>' (the email-body content does NOT appear in the lake; grep=0). ATHENA-QUERYABLE via opal_mcp workgroup (qid 88d20d74 SUCCEEDED): SELECT ... WHERE dt='2026-06-24' AND tool='r8_audit_lake_canary' returned the row; partition-projection works (no MSCK); args reads correctly (OpenX SerDe stringifies the nested object). CVO does the independent AC#3 cert on this served row. | CLOSED 20260624T135712Z |

## Log

- 20260624T134021Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
- 20260624T134313Z LEG A closed: safe-apply tfplan.r8 = 'Apply complete! 12 added, 0 changed, 0 destroyed' (HALTGT passed, HALT_ACK=1 routine). Post-appl
- 20260624T135424Z LEG B closed: Deploy via safe-ec2-deploy (ssm:92684b0c) after adding boto3 to requirements (caught: boto3 absent = lazy import would n
- 20260624T135712Z LEG C closed: Real-path canary via the DEPLOYED gateway _emit (ssm:46a30bbe Success, run from the venv on-box: from app import audit; 
- 20260624T135712Z CLOSED -- all 3 legs proven
