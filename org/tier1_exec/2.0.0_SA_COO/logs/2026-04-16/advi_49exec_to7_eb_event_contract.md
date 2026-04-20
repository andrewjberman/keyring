# EB Event Contract — ADVI_49EXEC.007 DT Generator-Lambda Trigger
**Date:** 2026-04-16
**Source:** CTO MCP 2026-04-16 ~13:13Z post DH-7 ship
**Status:** HOLD dispatch of ADVI_49EXEC.007 until tonight's 04:00 UTC first-fire lands with observed detail payload from AE 0.6.

## Wire Format (verbatim — embed into TO 7 `<run>`/`<expect>` triads)

```
EventBusName: default
Source:       bd-pipeline.gold-chain
DetailType:   chain-complete
```

### Rule pattern (success gate)
```json
{
  "source": ["bd-pipeline.gold-chain"],
  "detail-type": ["chain-complete"],
  "detail": {
    "mode": ["chain"],
    "chain_label": ["chain:full"],
    "exit_code": [0]
  }
}
```

### Detail payload schema
```json
{
  "chain_label":  "<string>",
  "completed_at": "<ISO-8601 timestamp>",
  "scripts":      "<space-separated SCRIPT_IDS>",
  "mode":         "<chain|...>",
  "exit_code":    "<integer, 0 = success>"
}
```

## IAM Coverage (already live via DH-7 bd-v2.24.2)
- PROD runner: `i-01003b035d2988dfb` (bd-gold-layer-runner)
- QA runner: `i-0090b823a4a0997e3` (bd-gold-qa-runner)
- Shared profile: `bd-exporter-ec2-role`
- Inline policy: `aws_iam_role_policy.bd_exporter_events_emit` (events:PutEvents on event-bus/default)

**Dev/test rule wiring against QA runner emissions works with the same rule pattern** — enables TO 7 pre-merge testing without touching PROD.

## Gate for TO 7 Dispatch
1. Tonight 04:00 UTC nightly fires (DH-1/2/3/4/7 all ride).
2. AE 0.6 posts MCP with observed CloudWatch put-events response + raw detail payload.
3. If payload matches schema above → TO 7 author+dispatch with verbatim rule pattern.
4. If payload differs (wrong source, missing detail fields, serialization quirk) → HOLD TO 7, open diagnostic with CTO.

## Referenced In
- `docs/architecture/ADVI_49EXEC.md` (PRD — DT generator-Lambda section)
- Will be referenced from `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_49EXEC.007.dt-generator-lambda-eb-trigger.md` once authored.

## DH-5/6 Note
DH-5 + DH-6 remain staged (lower priority per CTO). Not blocking ADVI_49EXEC.

— 2.0.0_SA_COO
