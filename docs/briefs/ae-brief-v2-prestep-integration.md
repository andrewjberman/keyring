# AE Brief — build_canonical_prices_v2 Pre-Step on Gold Runner

**Audience:** 0.6.0_AE_PartnerETL
**Issued by:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-10
**Related TOs:** ADVI_GLDRST.021 (source tag shipped), ADVI_GLDRST.021b (exemptions + min-sample guard shipped), ADVI_GLDRST.022 (this work)
**Ground truth trace:** `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-10/gold_trigger_chain_trace_and_d00c_role_split_fix.md`

---

## Why this brief exists

DS has done the end-to-end integration of `build_canonical_prices_v2.py` as a silver-prep pre-step on the `bd-gold-layer-runner` EC2. The script is registered as `S_00` in `gold_dispatch.sh` CATALOG and runs automatically ahead of `--chain full` / `--chain rebuild` invocations, before the freshness gate check. When DS's commits ship to S3, the next gold runner boot that runs the full chain will invoke v2 first, rebuild `silver/prices/canonical_prices.parquet` with the 4-tier hierarchy (T1 transaction_observed, T2 yahoo_finance, T3 linear_interpolation, T4 carry_forward), and then the existing A/B/C/D chain runs against the refreshed canonical_prices.

DS's scope stops at the code. AE owns everything downstream: the new EventBridge rule that gives v2 7-day coverage, the IAM sanity check, the diff protocol for the first week of parallel operation, and the eventual deprecation of `bd-price-update` Lambda's Job 1.

Everything below is sequenced. Don't skip ahead — the diff protocol in phase 3 is the gate on the Job 1 deprecation in phase 4.

---

## What DS shipped (context for the AE work)

- `data/black_diamond/scripts/gold/build_canonical_prices_v2.py` — moved from `silver/` to `gold/`. Uploaded to `s3://opal-data-bd/code/gold/build_canonical_prices_v2.py`.
- `data/black_diamond/scripts/gold/lib/ticker_overrides.py` — copied from `silver/lib/` (the silver copy is retained for the orphaned `silver/bd_price_update.py` host version and `inject_scoped_overrides.py`; duplication is tolerated as a known follow-up). Uploaded to `s3://opal-data-bd/code/gold/lib/ticker_overrides.py`. Side benefit: this also fixes the latent import bug in `E_06`, `E_08`, `E_11`, `E_15` which previously referenced `lib.ticker_overrides` without it being present in `gold/lib/`.
- `data/black_diamond/scripts/gold/gold_dispatch.sh`:
  - New CATALOG entry: `S_00|build_canonical_prices_v2.py|--upload`
  - New chain definition: `CHAIN_SILVER_PREP="S_00"`
  - New target in the case statement: `--chain silver-prep` runs v2 standalone
  - New pre-gate execution block: when MODE=chain and TARGET in `{full, rebuild}`, run `run_chain "silver-prep-pre" "$CHAIN_SILVER_PREP" ""` BEFORE the freshness gate
  - Execution-block reorder: BG re-invoke moved to fire BEFORE silver-prep + freshness gate so silver-prep runs exactly once per real execution (not once for the initial `--bg` process and once for the nohup'd re-invoke)
  - `CHAIN_FULL` and `CHAIN_REBUILD` do NOT include `S_00` — silver-prep is a separate run_chain invocation before the gate; including it in CHAIN_FULL would mean it runs AFTER the gate via the main run_chain, which defeats the whole purpose on no-new-data days
- `infra/aws/ec2/bd-gold-layer-runner/deploy-to-ec2.sh` — stale comment at line 11 updated to reflect the current reality: the runner's boot sync pulls from `code/gold/` only, and v2 is now there as a first-class gold script.

---

## What AE needs to do — sequenced

### Phase 1 (ship in one terraform apply) — New daily EventBridge cron rule

The gold runner's current daily coverage is:

- `bd-allocation-pipeline-trigger` at 22:00 UTC Mon-Fri (fires `bd-gold-trigger` via the bd-allocation-processor → bd-price-update → silver/prices/20*.parquet → S3 event chain)
- `bd-gold-nightly-fallback` at 23:00 UTC Mon-Fri (unconditional `bd-gold-trigger` safety net)
- `bd-gold-layer-monthly-trigger` at 08:00 UTC on the 1st (mode=full)

The gap this work closes: weekends and US market holidays. On a Saturday / Sunday / Good Friday / Memorial Day / July 4 / Labor Day / etc., bd-allocation-processor doesn't run (no new allocation file), bd-price-update doesn't run, no `silver/prices/<date>.parquet` lands, no S3 event fires, and the runner doesn't boot. That's by design for the old world where canonical_prices was only for trading days. But now that v2 is the silver-prep step and needs to run every day to T3-interpolate / T4-carry-forward the weekend and holiday gap dates, we need an unconditional daily trigger.

**Rule to add in `infra/aws/terraform/bd-pipeline/eventbridge.tf`:**

```hcl
resource "aws_cloudwatch_event_rule" "bd_canonical_prices_daily" {
  name                = "bd-canonical-prices-daily"
  description         = "Daily 22:00 UTC trigger for v2 canonical_prices rebuild (all days incl. weekends/holidays). Fires bd-gold-trigger which starts the gold runner; gold_dispatch.sh runs silver-prep (S_00 = build_canonical_prices_v2.py) before the freshness gate."
  schedule_expression = "cron(0 22 * * ? *)"  # every day, all days
  state               = "ENABLED"

  tags = {
    Name   = "bd-canonical-prices-daily"
    System = "BDPipeline"
  }
}

resource "aws_cloudwatch_event_target" "bd_canonical_prices_daily_target" {
  rule      = aws_cloudwatch_event_rule.bd_canonical_prices_daily.name
  target_id = "1"
  arn       = module.gold_trigger.function_arn
  input     = jsonencode({ mode = "incremental" })  # runs --chain full --incremental on the runner
}

resource "aws_lambda_permission" "eventbridge_canonical_prices_daily" {
  statement_id  = "allow-canonical-prices-daily-trigger"
  action        = "lambda:InvokeFunction"
  function_name = module.gold_trigger.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.bd_canonical_prices_daily.arn
}
```

**Why `cron(0 22 * * ? *)` and not `cron(0 22 ? * * *)`:** AWS EventBridge cron expects either day-of-month OR day-of-week to be `?` (not both). `* * ? *` = every day-of-month, every month, any day-of-week, every year — matches "every day". Reference: `eventbridge.tf:258` where `historical-prices-daily` uses the same pattern.

**Why `mode = "incremental"`:** the runner's wrapper `run_gold_layer.sh` delegates `incremental` → `gold_dispatch.sh --chain full --incremental`. That runs silver-prep first (auto) via the new pre-gate block, then the freshness gate, then the full chain. On weekdays, silver-prep runs, freshness gate passes (new allocations landed), chain runs. On weekends/holidays, silver-prep runs, freshness gate trips, A/B/C/D skips, instance shuts down — canonical_prices is still updated for the weekend/holiday date.

**Why keep the existing 22:00 weekday allocation trigger:** on weekdays, both the new `bd-canonical-prices-daily` AND the existing `bd-allocation-pipeline-trigger` chain fire. The runner's pending-marker mechanism (`gold/trigger-pending.json`) and existing race-safety in `run-gold-layer.sh:114-130` handles the overlap. Worst case: one extra boot + immediate pending-check re-run on weekdays. In practice, a single boot should satisfy both triggers because the second fire within the same boot window is absorbed by the pending marker. **Do not delete the existing weekday allocation trigger** — it still drives the allocation ingest path and is load-bearing for the silver/allocations layer.

**Why keep the existing `bd-gold-nightly-fallback`:** it's still needed as a safety net when the S3 prices trigger or the new canonical-prices-daily trigger silently drop. Redundant defense is fine.

### Phase 2 — IAM sanity check

The gold runner's instance profile needs read access to silver inputs that v2 reads, and write access to `silver/prices/canonical_prices.parquet` which v2 writes. The existing profile should already have these (the runner writes to `silver/canonical_holdings/` via B_00 and reads broadly from `silver/*`), but please verify before the first scheduled run:

```bash
# What v2 reads:
aws s3 ls s3://opal-data-bd/silver/transactions/ | head  # should not error
aws s3 ls s3://opal-data-bd/silver/historical_prices.parquet  # should exist
aws s3 ls s3://opal-data-bd/silver/prices/canonical_prices.parquet  # should exist

# What v2 writes:
# Run this on the instance itself via SSM with the runner's instance profile,
# against a test key to confirm write is allowed without touching the real file:
aws s3 cp /tmp/test.txt s3://opal-data-bd/silver/prices/test-write-$(date +%s).txt
aws s3 rm s3://opal-data-bd/silver/prices/test-write-*.txt
```

If any of these fails, add the missing S3 action to the runner's IAM role in `infra/aws/terraform/bd-pipeline/iam.tf` or `infra/aws/terraform/shared-infra/` depending on where the `bd-gold-layer-runner` instance profile is defined.

### Phase 3 — Diff protocol for the first week

**Do NOT disable `bd-price-update` Job 1 yet.** Let both v2 (scheduled nightly via the new cron) AND `bd-price-update` (triggered weekdays via the bd-allocation-processor chain) run in parallel for at least 5 business days. Both write `silver/prices/canonical_prices.parquet`; v2 runs after bd-price-update in the daily sequence (22:00 UTC both), so v2's output wins on every run where both fire. That's the intended transition state.

Every weekday during the parallel-run week, compare the two outputs:

1. Snapshot `canonical_prices.parquet` immediately after bd-price-update finishes (before v2 runs). The Lambda's CloudWatch log line "Job 1 complete" is the marker; grab the parquet at that point via an SSM doc or a one-off `aws s3 cp` on a fresh timestamp.
2. Let v2 run via the gold runner's silver-prep step.
3. Snapshot `canonical_prices.parquet` again after v2 finishes.
4. Diff the two parquets on `(date, asset_name)` pairs. Compare `price` and `source` columns.

**Expected weekday diff:**
- v2 should have strictly MORE rows than bd-price-update on any given day (v2 includes gap-date fills, bd-price-update only writes the target date)
- For rows present in both, `price` should match within $0.001 (both use the same T1/T2 sources; only difference is v2 applies the 4-tier hierarchy across the full date range whereas bd-price-update only writes per-asset rows for `target_date`)
- `source` values should match for rows where both wrote: `transaction_observed`, `yahoo_finance`, `carry_forward`
- v2 adds `linear_interpolation` as a new source value on gap dates (bd-price-update doesn't produce this)

**Stop-ship signals** during the parallel week:
- Any price delta > $0.001 on an overlapping (date, asset_name) row → investigation required
- Any row where bd-price-update has a value but v2 has nothing → v2 is losing data, investigate
- Any row where the `source` tag disagrees (e.g. bd-price-update says `transaction_observed` but v2 says `yahoo_finance` on the same row) → tier resolution divergence, investigate

If the first week is clean, proceed to Phase 4. If not, open a new TO to investigate the divergence before proceeding.

### Phase 4 — Disable bd-price-update Job 1

Once the parallel-run diff is clean for 5 business days:

1. In `infra/aws/lambda/bd-pipeline/bd-price-update/lambda_function.py`, wrap the Job 1 block (the canonical_prices write path) in an `if os.environ.get('ENABLE_JOB_1', 'false') == 'true':` guard. Default to false. Keep Job 2 (the `silver/interpolated_prices.parquet` write) unchanged — v2 still reads `interpolated_prices.parquet` in the future-rebuild emergency path per v2's current docstring, so that artifact must keep updating daily.
2. Deploy the Lambda via the standard pipeline (`build-and-upload.sh` + terraform apply).
3. Verify the next weekday run: the Lambda CloudWatch logs should show "Job 1 disabled via env var, skipping" (or similar), and v2's canonical_prices output should be the only writer.
4. Tag the commit: `bd-v{X.Y.Z}` per the pipeline versioning convention.
5. Monitor for 1 more business week. If anything breaks, flip the env var back to `true` in terraform and redeploy — that's the rollback.

After 2 weeks of clean operation, Job 1 can be deleted from the Lambda source entirely in a subsequent cleanup commit.

### Phase 5 — Rollback plan (keep accessible for 2 weeks post-shipping)

If v2 on the gold runner fails or corrupts canonical_prices at any point:

1. **Fastest rollback** (< 5 minutes): re-enable bd-price-update Job 1 via the env var (Phase 4 made it configurable). v2 keeps running but its output gets overwritten by the Lambda on the next weekday run. Weekends regress to the pre-022 dropout behavior during the rollback window. Acceptable as a short-term bridge while investigating v2.
2. **Full rollback**: revert the gold_dispatch.sh change, push, S3 upload — the runner stops invoking v2 on the next boot. Combined with (1), this is the no-v2 state. Use if v2 is producing actively-bad data, not just thin data.
3. **Terraform rollback**: disable `bd-canonical-prices-daily` event rule (set `state = "DISABLED"`) and terraform apply. Kills the weekend/holiday trigger entirely. Use if the cron itself is misbehaving (storm of triggers, AWS-side issue).

---

## What AE should NOT do

- Do NOT delete `bd-price-update` from terraform. Even after Job 1 is disabled, Job 2 still writes `silver/interpolated_prices.parquet` which v2 reads for emergency full rebuilds.
- Do NOT delete `bd-gold-nightly-fallback`. It's still the safety net when the S3 trigger chain drops.
- Do NOT delete `bd-allocation-pipeline-trigger` or the allocation chain. That's the live ingest path for `silver/daily_allocations/` — unrelated to canonical_prices.
- Do NOT skip the Phase 3 parallel-run diff. Shipping v2 as authoritative without confirming it matches the Lambda on overlapping dates is the same failure mode the ADVI_49PUSH postmortem flagged: "no crash ≠ correct".
- Do NOT move `v2` from `code/gold/` to somewhere else. Its location is load-bearing for the runner's sync path.

---

## Verification after Phase 1 lands

After the terraform apply for the new EventBridge rule:

```bash
# Confirm the rule exists and is enabled
aws events describe-rule --name bd-canonical-prices-daily

# Confirm the target is bd-gold-trigger
aws events list-targets-by-rule --rule bd-canonical-prices-daily

# Confirm the Lambda permission exists (S3InvokeGoldTrigger and
# allow-canonical-prices-daily-trigger should both be listed)
aws lambda get-policy --function-name bd-gold-trigger | jq -r '.Policy | fromjson | .Statement[].Sid'
```

First scheduled run will fire at the next `cron(0 22 * * ? *)` boundary (22:00 UTC = 6 PM ET / 5 PM EDT daily). Watch the runner via:

```bash
aws ec2 describe-instances --instance-ids i-01003b035d2988dfb \
  --query 'Reservations[0].Instances[0].[State.Name,LaunchTime]'
```

and the CloudWatch logs for `bd-gold-trigger` Lambda + the runner's own systemd logs at `s3://opal-data-bd/logs/gold-layer/`.

---

## Open questions for AE (flag back to Andrew if unclear)

1. **Instance profile IAM coverage** — Phase 2 is a best-effort verification on my end. If the sanity check reveals missing permissions, you own the terraform edit to add them.
2. **Monthly full run interaction** — `bd-gold-layer-monthly-trigger` on the 1st at 08:00 UTC already fires the runner with `mode=full`. That will now auto-invoke silver-prep (because `--chain full` runs silver-prep first via the new pre-gate block), which is redundant with the 22:00 UTC daily run on the 1st but not harmful. If you want to save 10-20 min on the 1st, you could conditionally skip silver-prep in the dispatcher when `MODE_TMP == full` — but I'd recommend NOT doing that optimization. Redundant full rebuilds are a safety net and the extra compute is cheap.
3. **Weekday vs weekend cron collision** — `bd-allocation-pipeline-trigger` fires at 22:00 UTC Mon-Fri and the new `bd-canonical-prices-daily` also fires at 22:00 UTC every day. On weekdays, both fire at the same minute. The pending-marker mechanism should handle the overlap cleanly, but if you see any double-boot symptoms in the first week, consider shifting `bd-canonical-prices-daily` to `cron(5 22 * * ? *)` (22:05 UTC) so the allocations chain lands first on weekdays and the canonical-prices trigger arrives after.
