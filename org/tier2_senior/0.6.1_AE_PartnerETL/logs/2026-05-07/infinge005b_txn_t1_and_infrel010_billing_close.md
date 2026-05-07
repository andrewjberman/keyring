# Session Log: INFINGE.005b T-1 Fix + INFREL.010 Billing Complete + Billing Builder Fix

**Agent:** 0.6.1_AE_PartnerETL
**Date:** 2026-05-07
**Session window:** ~15:00Z – 15:30Z
**Branch:** CLOUD

---

## Summary

Deployed inf-api-txn T-1 default (v1.7.30), completed billing Wave C 4-date retry (all sentinels triggered + silver confirmed), diagnosed and fixed systemic billing silver blocker in build_billing_dim.py (v1.7.31), confirmed all 4 billing silver parquets at correct path. RAVC6 + RAVC8 sent to COO.

---

## 1. inf-pipeline-v1.7.30 — T-1 Default (INFINGE.005b)

COO ruling 20260507: inf-api-txn Lambda must default to T-1 (yesterday) when no date override in event. Orion Custom Reports has no same-day data at 13:00 UTC cron time.

**Change:**
```python
# lambda_function.py
_default_date = (
    dt.datetime.now(dt.timezone.utc).date() - dt.timedelta(days=1)
).isoformat()
snap_date = event.get("date") or _default_date
```

**Deploy sequence:**
1. `build-and-upload.sh inf-pipeline inf-api-txn` -> SHA `5noxDRvexYkLQ2YKa7xT+zFRGbHtd2Bmuu3veth880Y=`
2. Commit `fd4105bec` (lambda_function.py + source-map)
3. `terraform apply` -> 1 change (source_code_hash)
4. 0-diff verified
5. `record-terraform-deploy.sh inf-pipeline --version inf-pipeline-v1.7.30` -> `b222fa687`
6. Tag `inf-pipeline-v1.7.30`, pushed CLOUD + --follow-tags

---

## 2. INFREL.010 Billing Wave C — 4-Date Retry

### Failure Root Cause Diagnosis

First retry attempt (SSM 362...) failed because retry script used wrong path `/home/ec2-user/manual_api/orion_billing_dim.py`. EC2 is a fresh instance; scripts are at `/opt/inf-bronze-runner/repo/data/orion/manual_api/`. Corrected script uploaded to S3 and re-dispatched.

Second retry (SSM 862da701):
- 2020-10-31: OK (ReadTimeout was transient; retry succeeded)
- 2022-12-31: OK (exit=3 was transient; retry succeeded)
- 2020-02-29: FAIL rc=5 — `ValueError: day is out of range for month` at line 153 `today.replace(year=today.year-5)` when today=2020-02-29 (EC2 repo has old billing script, pre-DS~B fix a70eadd04)
- 2024-02-29: Same leap-day ValueError

Third retry (SSM 41ff27bd) — downloaded S3 fixed script (has DS~B a70eadd04):
- 2020-02-29: OK
- 2024-02-29: OK

All 4 sentinels written. All 4 bronze CSVs verified in S3.

### Billing Silver Blocker — Systemic (v1.7.31 Fix)

After all 4 sentinels written, CloudWatch showed inf-silver-chain Lambda repeatedly failing:
```
[billing] FAILED: NoSuchKey on GetObject ... billing.csv
```

Investigation: Lambda was also being triggered by ongoing Wave C1 historical backfill (daily May 2020 dates — billing.csv doesn't exist for non-month-end dates → expected).

For the 4 retry dates, billing.csv WAS in S3. Root cause was that `_attach_rep_id_via_tax_unrealized` calls `read_bronze_csv(snapshot_date, "tax_unrealized")` unconditionally, and tax_unrealized.csv doesn't exist for these month-end dates (tax backfill covered different dates). This caused ALL billing silver conversions to fail — 0 billing parquets existed.

**Fix (build_billing_dim.py):**
```python
from botocore.exceptions import ClientError
try:
    tax_bronze = read_bronze_csv(snapshot_date, "tax_unrealized")
except ClientError:
    df = df.copy()
    df["rep_id"] = None
    return df  # INFGRD filter will produce 0 rows
```

**Deploy:**
1. `build-and-upload.sh inf-pipeline inf-silver-chain`
2. Commit `f427c6aed`
3. `terraform apply` -> 1 change
4. 0-diff verified
5. `record-terraform-deploy.sh inf-pipeline --version inf-pipeline-v1.7.31` -> `8ed19aebc`
6. Tag `inf-pipeline-v1.7.31`, pushed CLOUD + --follow-tags

### Billing Silver Confirmation

Re-triggered 4 sentinels. Lambda fired (v1.7.31) for each date. CW logs showed:
- "DIM billing: 0 rows after INFGRD filter -- pre-onboarding date, SKIP partition" (expected)
- "[billing] OK: 0 rows -> silver/api_dims/billing/snapshot_date={date}/data.parquet"

Note: Silver path is `silver/api_dims/billing/` (NOT `billing_unrealized/` as COO initially assumed).

S3 verification (all 4 at 15:23:44-49Z):
| Date | Bytes |
|---|---|
| 2020-02-29 | 5,027 |
| 2020-10-31 | 5,027 |
| 2022-12-31 | 5,027 |
| 2024-02-29 | 5,027 |

---

## 3. DS~B Reply — Failure Mode Clarification

DS~B asked about failure modes for 2020-10-31 and 2022-12-31. Replied:
- 2020-10-31: ReadTimeout (transient) — NOT leap-day ValueError
- 2022-12-31: exit=3 (transient API error) — NOT leap-day ValueError
- Only 2020-02-29 and 2024-02-29 were leap-day failures

---

## 4. RAVC Chain

| Message | Subject | Timestamp |
|---|---|---|
| RAVC6 | T-1 deployed + billing 4-date retry complete | 20260507T151521Z |
| RAVC6 ADDENDUM | Billing silver confirmed + v1.7.31 systemic fix | 20260507T152601Z |
| RAVC7 ACK (COO) | INFINGE.005b CLOSED. INFREL.010 billing CLOSED. | received |
| RAVC8 | Billing silver all confirmed + path correction + 71-date sweep request | 20260507T152627Z |

---

## 5. Open Items

1. **inf-api-txn first cron fire**: 2026-05-08T13:00Z. Monitor CW logs. RAVC11 after first successful pull.
2. **Wave C2 (performance skip-400)**: DS~B session down; passive item. DS~B must restart before 2026-05-08T23:00Z.
3. **RPBKTPI TO-2**: DS~B to RAVC1 plan + chain cost estimate for INF_B_00 historical re-run.
4. **INFREL.010 Phase 1 GO**: Pending COO + Andrew approval for billing+tax+performance historical backfill (2020-01-01 to present). RAVC3 sent 20260507T181910Z.

---

## 6. Commits This Session

| Commit | Message |
|---|---|
| `fd4105bec` | fix(ADVI_INFINGE.005b): inf-api-txn T-1 default date + resync Lambda |
| `b222fa687` | ci: record deploy inf-pipeline @ fd4105be [skip ci] |
| `075a61728` | feat(ADVI_INFREL.010): billing Wave C retry script (inf_backfill_billing_c3_retry.py) |
| `e8a6efdd7` | fix(ADVI_INFREL.010): billing retry script -- correct repo path + boto3 pattern |
| `09b1b22b5` | fix(ADVI_INFREL.010): billing leap-day retry -- download fixed S3 script |
| `f427c6aed` | fix(ADVI_INFREL.010): build_billing_dim -- catch NoSuchKey on tax_unrealized |
| `8ed19aebc` | ci: record deploy inf-pipeline @ f427c6ae [skip ci] |

**Tags:** `inf-pipeline-v1.7.30`, `inf-pipeline-v1.7.31`
**Push:** CLOUD + --follow-tags (all commits live)

---

## Addendum: v1.7.32 — 2020-05-31 $0 AUA Guard (INFREL.010 Final)

**Root cause:** `2020-05-31` has BOTH `billing.csv` (87,508b) AND `tax_unrealized.csv` in bronze. The rep_id lookup via tax_unrealized succeeded and matched Inflection accounts, but those accounts had `ending_mv = $0` (pre-onboarding noise). Guard B fired: `$0 outside [$50M, $400M]`.

**Fix (build_billing_dim.py):**
```python
if df["ending_mv"].sum() == 0:
    print("DIM billing: $0 AUA after INFGRD filter -- pre-onboarding noise, SKIP partition")
    return df.iloc[0:0]
```

**Deploy:** inf-pipeline-v1.7.32 (commit b2e634a12, 0-diff). Directly invoked Lambda (EventBridge delivery gap during Wave C1 high-concurrency period — 3 sentinel retries all dropped).

**Result:** 2020-05-31 billing OK, 0 rows, 5,027b @ 16:49Z. **83/83 billing silver COMPLETE.**

**RAVC10 sent to COO at 20260507T164922Z.**

| Tag | Change | Commit |
|---|---|---|
| v1.7.32 | build_billing_dim $0 AUA guard | b2e634a12 |

---

## Addendum 2: INFREL.010 Phase 0 Audit (20260507T~18:30Z)

Context-compacted restart. Completed INFREL.010 Phase 0 (per-dim lookback audit).

### Phase 0 Audit Matrix

| Dim | Endpoint | Date-Range Capable | Date Mechanism | Backfill Viable |
|---|---|---|---|---|
| billing | Envision ExcelReport | YES | ORION_PULL_DATE env (`_pull_date()`) | YES |
| tax | Envision ExcelReport | YES | ORION_PULL_DATE env (`_pull_date()`) | YES |
| performance | ExcelReport | PARTIAL | `--snapshot-date` argparse (orchestrator NOT passing it) | YES with fix |
| unified_account_dim | ExcelReport | NO (snapshot) | Hardcodes `today` | NO |
| accounts_v2 | Portfolio snapshot | NO (snapshot) | `--date` argparse; env mismatch | NO |
| assets | Orion REST | NO (snapshot) | Hardcodes `today` | NO |
| transactions | Custom Reports | DECOMMISSIONED | Lambda (inf-api-txn) | INFNNA.001 |
| geo | N/A | SKIP | N/A | N/A |

### Key Findings

1. **expected_fail on assets**: Already removed (orchestrator.py line 22 docstring + DimSpec confirmed). No action needed.
2. **Orchestrator date propagation**: Correct via ORION_PULL_DATE env var. billing + tax honor it. Snapshot-only dims (unified_account_dim, accounts_v2, assets) hardcode today — not a bug for daily cron (snapshot is correct); just not backfillable.
3. **Performance gap**: `pull_inflection_performance_dim.py` has `--snapshot-date` argparse arg (added by INFREL.001b) but orchestrator DimSpec doesn't include it in extra_args. Daily cron writes to today's partition. Phase 1.1 fix needed.
4. **INFREL.002 Fix4 "wrong partition" root cause**: NOT a structural orchestrator bug. billing/tax scripts correctly use ORION_PULL_DATE. Fix4 likely had pre-DS~B leap-day bug or wrong dispatch date.
5. **Backfill scope**: billing + tax viable (2020-01-01 to present). performance viable after fix. Others not viable.

### RAVC3 Sent

RAVC3 sent to COO at 20260507T181910Z with Phase 0 matrix + Phase 1 GO request. Awaiting COO + Andrew approval for large-scale S3 backfill operations.
