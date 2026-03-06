# DevOps Brief: ADVI_NNAVAR Phase 4 — Volume Gap EC2 Run

**To:** 0.4.0_DT_ClientPlatform
**From:** 0.4.0_DS_ClientPlatform
**Date:** 2026-03-06
**Script:** `data/black_diamond/scripts/diagnostics/diag_nnavar_volume_gap.py`

---

## Context

The NNAVAR timing investigation is complete. The persistent -$119M total NNA volume gap vs
Schwab is independent of timing and remains open. This script tests the hypothesis that
transaction types present in the original BD silver NNA logic (Wire In, Wire Out, Transfer)
were dropped from production script 05 and account for the missing volume.

Three suites — run in this order:

1. `taxonomy` (~5-10 min) — gates everything else
2. `sign_audit` (~2-5 min) — fast, can run in parallel with type_extension
3. `type_extension` (~30-60 min) — conditional on taxonomy finding candidate types

---

## Upload

```bash
aws s3 cp data/black_diamond/scripts/diagnostics/diag_nnavar_volume_gap.py \
  s3://opal-data-bd/scripts/diagnostics/diag_nnavar_volume_gap.py
```

---

## EC2 Instance

`bd-gold-layer-runner` (`i-01003b035d2988dfb`)

---

## Execution (SSM, file-based params — same pattern as all NNAVAR scripts)

Prepare `.tmp_ssm_params.json` for each suite invocation:

```json
{
  "DocumentName": "AWS-RunShellScript",
  "InstanceIds": ["i-01003b035d2988dfb"],
  "Parameters": {
    "commands": [
      "aws s3 cp s3://opal-data-bd/scripts/diagnostics/diag_nnavar_volume_gap.py /tmp/diag_nnavar_volume_gap.py",
      "python3 /tmp/diag_nnavar_volume_gap.py --suite taxonomy --run-date 20260306 --instance-id i-01003b035d2988dfb 2>&1 | tee /tmp/nnavar_volgap_taxonomy_stdout.txt",
      "aws s3 cp /tmp/nnavar_volgap_taxonomy_stdout.txt s3://opal-data-bd/diagnostics/nnavar_volume_gap/20260306/taxonomy/stdout.txt"
    ]
  }
}
```

Change `--suite taxonomy` to `--suite sign_audit` or `--suite type_extension` for subsequent runs.

```bash
export MSYS_NO_PATHCONV=1
aws ssm send-command --cli-input-json file://.tmp_ssm_params.json
```

---

## Run Order and Decision Gates

### Step 1: `taxonomy` (~5-10 min)

Run this first. Read `s3://opal-data-bd/diagnostics/nnavar_volume_gap/20260306/taxonomy/taxonomy_summary.json`.

The key field is `type_extension_warranted`:
- **`true`** → candidate types (Wire In, Wire Out, etc.) have >$1M volume in the window → proceed to Step 3
- **`false`** → no material candidate types found → report to DS before proceeding

Also check `txn_type_taxonomy.csv` — share with DS so they can see the full type landscape.

### Step 2: `sign_audit` (~2-5 min)

Can run immediately after taxonomy (does not depend on taxonomy result). Check stdout and
`sign_mismatches.csv`. If `total_wrong_sign_exposure_dollars` > $10M, share with DS before
running type_extension.

### Step 3: `type_extension` (~30-60 min, conditional)

Only run if `type_extension_warranted=true` in taxonomy_summary.json.

The script internally re-runs taxonomy inline if run standalone, but since you already have
it, the `type_extension` suite will use the gating logic automatically. Just run it.

Expected variants: `base_prod`, `plus_wire_in`, `plus_wire_out`, `plus_all_candidates`,
`cash_only` (exact variant list depends on which types have material volume from taxonomy).

Share `summary.csv` with DS immediately on completion.

---

## Expected Runtimes

| Suite | Expected Runtime | Notes |
|-------|-----------------|-------|
| `taxonomy` | 5-10 min | Scans all silver partitions once, no caps |
| `sign_audit` | 2-5 min | Fast, no caps, just sign checks |
| `type_extension` | 30-60 min | Depends on how many candidate variants. Each variant runs full cap pipeline. |

---

## Outputs

All outputs write to `s3://opal-data-bd/diagnostics/nnavar_volume_gap/20260306/`:

```
taxonomy/
  txn_type_taxonomy.csv     <- full type audit (share with DS)
  taxonomy_summary.json     <- gating flags
  stdout.txt

sign_audit/
  sign_mismatches.csv       <- sign convention audit (share with DS)
  sign_audit_summary.json
  stdout.txt

type_extension/
  summary.csv               <- one row per variant (PRIMARY DELIVERABLE — share with DS)
  {variant}/monthly_nna.csv
  {variant}/metrics.json
  stdout.txt

run_manifest.json
```

---

## Error Handling

- If OOM or script error on any suite: capture stdout, report to DS before retry
- If `type_extension_warranted=false`: stop after taxonomy + sign_audit, report to DS
- If `taxonomy` finds no `transaction_type` column: report immediately to DS — schema change

---

## Reference

`docs/deployment/EC2_CODE_DEPLOYMENT_STANDARD.md` applies.
No inline code. Script must be in S3 before EC2 pull.
