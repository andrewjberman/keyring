# DevOps Brief — ADVI_MIXV2.001: pct fix + AP gate insurance override

**Author:** 0.4.0_DS_ClientPlatform
**Date:** 2026-03-18
**Branch:** CLOUD
**Task order:** ADVI_MIXV2.001

---

## Part 1 — Lambda pct fix (WS1)

### What changed

**File:** `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py`
**Function:** `handle_books_composition`

Three lines changed in the `handle_books_composition` response builder:

```python
# Before (incorrect — 0-100 scale)
'pct': round(float(mv) / total_mv * 100, 2)

# After (correct — 0-1 scale, consistent with all other pct fields)
'pct': round(float(mv) / total_mv, 6)
```

All three `pct` fields updated: mix_items loop, top_items loop, other bucket.

A comment was added above the mix loop confirming the 0-1 convention for future maintainers.

### Why this matters

The frontend multiplies pct by 100 before display (`{(item.pct * 100).toFixed(1)}%`).
With the old scale (pct=62.5), equity showed as 6250.0%. With the fix (pct=0.625), it
renders correctly as 62.5%.

### Deploy sequence (DT owns this — task order ADVI_MIXV2.004)

1. Build and upload the Lambda zip to S3:
   ```
   # From repo root in Git Bash
   cd infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/
   # Build zip (see build-and-upload.sh or PowerShell equivalent)
   # Upload to s3://opal-313476888478-lambda-artifacts/partners-api/opal-partners-data.zip
   ```

2. Terraform plan/apply:
   ```
   cd infra/aws/terraform/partners-api/
   .tools/terraform.exe plan
   # Expect: aws_lambda_function.opal_partners_data -- update in place (s3_object_version)
   .tools/terraform.exe apply
   ```

3. Verify 0-diff plan after apply.

4. Tag and push:
   ```
   git tag -a partners-api-v1.1.0 -m "fix pct scale in handle_books_composition"
   git push --follow-tags
   ```

5. Smoke test: hit `/api/scoped/partners/books/account/{id}/composition` for any account.
   Confirm mix items show pct values in 0-1 range (e.g., 0.625 not 62.5).

---

## Part 2 — 06b AP gate insurance override (WS2)

### What changed

**Files modified:**
- `data/black_diamond/scripts/gold/06b_build_client_mix_timeseries.py`
- `data/black_diamond/scripts/gold/insurance_accounts.json` (new)

### Summary of changes

1. Added `_load_insurance_config()` — reads `insurance_accounts.json` at startup.
2. `load_static_tables()` now returns `(acct_rel_dict, prices_grouped, ap_last_seen, insurance_account_ids, insurance_gate_days)`.
3. `process_date()` applies a per-account AP gate: standard accounts use 45 days, accounts
   listed in `insurance_accounts.json` use `ap_gate_days_override` (default 180 days).
4. `insurance_accounts.json` starts empty. Populate it after running `.tmp_insurance_ap_gate.py`.

### Why this matters

Insurance/annuity accounts (SHIELD, BUFFER, variable annuities) update `account_performance`
on monthly or quarterly statement cycles. The standard 45-day gate incorrectly excludes them
during inter-statement gaps, causing ~$60M of structured_notes to appear and disappear from
the firm-level mix view. The targeted override keeps them in snapshots throughout their full
statement cycle without affecting the $371M stale-positions protection for standard accounts.

### Populating insurance_accounts.json

Run the diagnostic before the next full rebuild:

```bash
# On the EC2 instance or locally with AWS credentials
python3 .tmp_insurance_ap_gate.py
```

The script prints a `suggested insurance_accounts.json content` block. Copy the
`insurance_account_ids` list into:
`data/black_diamond/scripts/gold/insurance_accounts.json`

Then commit and re-deploy 06b before running the full rebuild.

### Deploy sequence (AE owns this — task order ADVI_MIXV2.003)

1. Upload 06b script and insurance_accounts.json to S3:
   ```
   aws s3 cp data/black_diamond/scripts/gold/06b_build_client_mix_timeseries.py \
       s3://opal-data-bd/scripts/gold/06b_build_client_mix_timeseries.py
   aws s3 cp data/black_diamond/scripts/gold/insurance_accounts.json \
       s3://opal-data-bd/scripts/gold/insurance_accounts.json
   ```

2. On EC2 (via safe-ec2-deploy.sh or SSM), pull both files from S3 to the working directory.

3. Run incremental to pick up the gate fix for recent dates:
   ```
   python3 06b_build_client_mix_timeseries.py --upload --incremental
   ```

4. If insurance_accounts.json has been populated (after diagnostic run), do a full rebuild
   so all historical dates reflect the extended gate:
   ```
   python3 06b_build_client_mix_timeseries.py --upload
   ```

5. Verify: check a known insurance account_id in the output JSONs at
   `gold/client_timeseries/{relationship_id}.json` and confirm it is present across the
   inter-statement gap dates where it was previously excluded.

---

## Acceptance criteria

| # | Check | Owner |
|---|-------|-------|
| 1 | Lambda: mix item pct values 0-1 on composition endpoints | DT |
| 2 | Diagnostic run, insurance account_ids identified | DS |
| 3 | insurance_accounts.json populated and committed | DS |
| 4 | 06b incremental run picks up extended gate without errors | AE |
| 5 | Full rebuild with populated insurance_accounts.json done | AE |
| 6 | $60M structured_notes no longer oscillates in firm-level mix views | RD |
