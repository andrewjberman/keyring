# DevOps Brief: ADVI-005 — stacked_bar + rolling_1y Deploy (script 10 EC2)

**From:** 0.4.0_DS_ClientPlatform
**To:** 0.4.0_DT_ClientPlatform
**Date:** 2026-03-04
**Commit:** `c9b3ab76`
**Pipeline:** bd-pipeline EC2 gold layer
**Service:** `bd-gold-layer-runner` (`i-01003b035d2988dfb`)
**Current deployed commit:** `9216c922`

---

## What Changed

One EC2 gold script changed. No infrastructure changes (no new IAM, S3 buckets, or instance changes).

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/10_generate_advisor_rolling_flows.py` | Added `stacked_bar` and `rolling_1y` keys to `advisor_rolling_flows.json` output. Added `STACKED_BAR_PERIODS` constant and `compute_stacked_bar()` function. |

### New output keys in `gold/advisor_rolling_flows.json`

Both keys are **additive**. All existing keys (`generated_at`, `data_as_of`, `firm_id`, `summary`,
`architects`, `implementors` with 30d/90d/1Y windows) are unchanged.

**`stacked_bar`** — period-aggregated inflows/outflows/nna_net per advisor (5 periods x 2 role types)
- Structure: `{ "qtd"|"ytd"|"1y"|"3y"|"max": { "architects": AdvisorBarEntry[], "implementors": AdvisorBarEntry[] } }`
- `AdvisorBarEntry = { advisor_name, advisor_id, inflows, outflows, nna_net }`
- `outflows`: positive magnitude; `nna_net`: signed
- Period boundaries: qtd/ytd calendar-anchored; 1y/3y trailing 365/1095 days; max = inception (2020-06-30)

**`rolling_1y`** — fixed 1Y rolling window daily timeseries for all advisors
- Structure: `{ "architects": AdvisorRolling1YSeries[], "implementors": AdvisorRolling1YSeries[] }`
- `AdvisorRolling1YSeries = { advisor_name, advisor_id, series: [{ date, nna, inflows, outflows }] }`
- Full history emitted (2021-07-01 to present); frontend slices by period toggle
- `outflows`: positive magnitude

---

## Deploy Steps

### 1. Export PATH for jq

```bash
export PATH="/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools:$PATH"
```

### 2. Run safe-ec2-deploy.sh to sync scripts to S3

```bash
export AGENT_NAME="0.4.0_DT_ClientPlatform"
bash infra/aws/ec2/safe-ec2-deploy.sh bd-gold-layer-runner \
    infra/aws/ec2/bd-gold-layer-runner/deploy-to-ec2.sh
```

Expected output:
- Bronze, silver, and gold scripts synced to `s3://opal-data-bd/code/{bronze,silver,gold}/`
- `EC2_MANIFEST.json` updated with new `deployed_commit` (current CLOUD HEAD)
- Manifest committed automatically by the wrapper

### 3. Commit the manifest update

The wrapper auto-commits EC2_MANIFEST.json. Verify:

```bash
git log --oneline -2
```

Expected: top commit is the auto-generated manifest commit from safe-ec2-deploy.sh.

### 4. Start the EC2 instance for incremental run

```bash
aws ec2 start-instances --instance-ids i-01003b035d2988dfb --region us-east-1
```

The instance boots, syncs scripts from S3, and runs `run_gold_layer.sh incremental`.
Incremental mode sequence: `02 -> 05 -> 07 -> 08 -> 09 -> 10`.
Only script 10 output changes; upstream scripts pass through quickly on current data.
Instance shuts down automatically after completion.

### 5. Monitor run progress

```bash
# Watch for new log file in S3 (appears when run completes)
aws s3 ls s3://opal-data-bd/logs/gold-layer/ --recursive | sort | tail -5
```

### 6. Verify output

```bash
aws s3 cp s3://opal-data-bd/gold/advisor_rolling_flows.json - | python3 -c \
  "import json,sys; d=json.load(sys.stdin); print('top-level keys:', list(d.keys()))"
```

Expected keys include: `stacked_bar`, `rolling_1y`.

```bash
aws s3 cp s3://opal-data-bd/gold/advisor_rolling_flows.json - | python3 -c \
  "import json,sys; d=json.load(sys.stdin); sb=d.get('stacked_bar',{}); \
   print('stacked_bar periods:', list(sb.keys())); \
   print('first period roles:', list(sb.get('qtd',{}).keys()))"
```

Expected:
```
stacked_bar periods: ['qtd', 'ytd', '1y', '3y', 'max']
first period roles: ['architects', 'implementors']
```

### 7. Tag and push

```bash
git tag -a bd-v2.15.1 -m "feat(bd-gold-10): stacked_bar + rolling_1y advisor flows (ADVI-005)"
git push --follow-tags
```

Note: tag `bd-v2.15.0` is reserved for the bd-portal-publisher Lambda deploy (Stream B1).
Script 10 EC2 is `bd-v2.15.1` (incremented from B1).

---

## Verification

After the run completes, confirm in the S3 log (`logs/gold-layer/gold_incremental_YYYY-MM-DD.log`):

```
COMPLETE -- INCREMENTAL
```

No errors from script 10. The pipeline-complete sentinel is written at
`s3://opal-data-bd/gold/pipeline-complete.json` which triggers bd-portal-publisher and
bd-portal-advisor-publisher Lambdas. This is normal and expected — they will re-run with
current data.

---

## What This Unlocks

- Portal advisor intelligence rolling flows charts will have `stacked_bar` data for all 5 periods.
- `rolling_1y` timeseries enables the 1Y rolling NNA chart for each architect/implementor.
- RD (0.4.2_RD_AdvisorIntelligence) is ready to implement portal rendering once this lands.

---

## Do NOT

- Run `02_build_positions_cube.py --start-date` manually or via SSM — corrupts data. Full rebuild only if needed.
- Skip the `safe-ec2-deploy.sh` wrapper — manifest tracing depends on it.
- Modify the existing `architects`/`implementors` legacy keys in the output (backward compat required).
- Run in `full` mode unless explicitly requested — full mode rebuilds all parquets from scratch.
