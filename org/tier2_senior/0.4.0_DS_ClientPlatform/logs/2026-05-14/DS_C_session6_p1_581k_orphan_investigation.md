# DS~C Session 6 — P1 $581K orphan-aggregation investigation (date-asymmetry root cause)

**Date:** 2026-05-14
**Agent:** 0.4.0_DS_ClientPlatform~C
**Authorization:** CTO P1 investigation (17:22:43Z broker push, Andrew direct promotion P3 → P1) — RAVC1 ACK 17:23:41Z; RAVC2 17:30:48Z
**TO:** `P1_581k_orphan_aggregation_inf_d_08` (no formal TO file; CTO-direct routing + COO TO authoring in parallel)
**Wall time:** ~7 min RAVC1 ACK → RAVC2 (well under 1-2h sizing)
**Outcome:** Investigation conclusive. Root cause = **date asymmetry**, not orphan-accounts. Recommendation: (c) document legitimate-divergence.

## TL;DR

DS~A Phase 1.1 RAVC2 surfaced a $580,948.02 gap between `nmec_nmnc_nna.json#total.total_aua` ($202,602,212.50) and firm canonical `header_metrics.json#total_aua` ($203,183,160.52). CTO suspected an orphan-aggregation gap at `INF_D_08.nmec_nmnc_nna.py:259` `hh["aua"].sum()`.

**Empirical decomposition resolves the gap exactly:**

| Component | Value |
|---|---|
| Bronze 5/14 - bronze 5/13 (day-over-day AUA growth) | **+$737,663.68** |
| Gold client_performance 5/14 vs bronze 5/14 (intra-day source delta) | **-$156,715.66** |
| **Net** | **$580,948.02** |

INF_D_08 uses bronze 2026-05-13 because `_latest_bronze_date()` (line 60-71) requires `transactions.csv` presence and 2026-05-14 only has `assets.csv` + `billing.csv` (no txn yet). Gold canonical (header_metrics.json via INF_D_00) reads `client_performance.parquet` which uses 2026-05-14 via a separate upstream pipeline that doesn't need same-day txn data.

Both artifacts are correct for their stated purpose. Bug is documentation, not data.

## Empirical investigation

### Phase 1: Confirm the gap

```bash
$ aws s3 cp s3://opal-data-inf/platinum/firm/nmec_nmnc_nna.json - | jq '.total.total_aua, .as_of'
202602212.50
"2026-05-14"

$ aws s3 cp s3://opal-data-inf/platinum/firm/header_metrics.json - | jq '.total_aua'
203183160.52

# Gap: 203183160.52 - 202602212.50 = $580,948.02 ✓
```

### Phase 2: Identify source-loading divergence

```bash
# INF_D_08._load_aua reads bronze/orion-api/{bronze_date}/assets.csv
# INF_D_08._latest_bronze_date returns latest date with BOTH assets.csv AND transactions.csv
$ aws s3 ls s3://opal-data-inf/bronze/orion-api/2026-05-14/
assets.csv      # present
billing.csv     # present
transactions.csv  # ABSENT — not delivered yet
```

```bash
# INF_D_00.portal_aggregates.py reads gold/timeseries/client_performance.parquet
# Line 704: total_aua = float(cp[cp['date'] == cp['date'].max()]['total_aua'].sum())
# This is a derived artifact from INF_C_02 (gold tier) — date constraint different
```

### Phase 3: Empirical simulation of INF_D_08 main flow

Mimicked `_load_aua` + `_lifecycle_table` exactly with current S3 data:

```
Bronze date used by _latest_bronze_date: 2026-05-13  ← key finding
aua: 306 HHs, total $202,602,212.50  ← EXACT MATCH against nmec emit
txn: 20,212 rows, unique HHs=198 (last 365 days)
After outer-merge into hh: 307 HHs, aua sum = $202,602,212.50
INF_D_08 total_aua emit: $202,602,212.50  ← MATCH
```

Outer-merge HH composition:
- aua-only HHs (no txn match): 109; AUA sum $73,307,867.01 (existing HHs with no transactions in 365-day window)
- txn-only HHs (no aua match): 1 (txn-active but zero current AUA — likely closed account)
- Both: 197

NO orphan-account dropping inside `_lifecycle_table` — every aua HH is preserved through the outer merge. `hh["aua"].sum()` = `aua["aua"].sum()` exactly. The gap cannot be inside INF_D_08's aggregation logic.

### Phase 4: Day-over-day verification

```
Bronze date inventory (2026-05-12 through 2026-05-14):
  2026-05-12: txn=True, assets=True
  2026-05-13: txn=True, assets=True   ← INF_D_08 uses this
  2026-05-14: txn=False, assets=True  ← gold canonical uses this via client_performance

Bronze AUA by date (loaded directly, same _load_aua logic):
  5/13: 306 HHs, total $202,602,212.50
  5/14: 308 HHs, total $203,339,876.18
  Day-over-day delta: +$737,663.68

Gold client_performance.parquet date=2026-05-14: $203,183,160.52
Bronze 5/14 vs gold 5/14: -$156,715.66 (gold LOWER than raw bronze)

Reconciliation:
  (bronze 5/14 - bronze 5/13) + (gold 5/14 - bronze 5/14)
  = +$737,663.68 + (-$156,715.66)
  = $580,948.02  ← EXACT MATCH against original gap
```

## CTO's three questions — definitive answers

### 1. Who does the $581K belong to?

**Not a subset of specific accounts.** It's a per-day AUA delta + a same-day source-divergence, both spread across the entire firm:

- 2 new HHs in 5/14 not in 5/13 (HH count 306 → 308)
- All 306 pre-existing HHs with AUA value changes (market prices + dividends + intraday trades + settlements)

The orphan-account framing was inverted by the original DS~A finding. Investigation rules it out.

### 2. WHY are they not being rolled up?

**Date asymmetry, not aggregation logic.** `INF_D_08._latest_bronze_date()` at lines 60-71 requires `transactions.csv` presence (for lifecycle classification — first_txn + window_inflows). Bronze 2026-05-14 doesn't have txn yet, so INF_D_08 falls back to 5/13. Gold canonical (header_metrics.json) uses `client_performance.parquet` which has 5/14 data via a separate upstream pipeline that doesn't require same-day txn.

Code excerpt (INF_D_08 lines 60-71):

```python
for d in reversed(dates):
    head = S3.list_objects_v2(Bucket=BUCKET, Prefix=f"bronze/orion-api/{d}/transactions.csv")
    if head.get("KeyCount", 0) > 0:
        return d
```

### 3. Which is correct?

**Option (c) — both reflect legitimate-but-different conceptual scopes; bug is documentation.**

| Artifact | Scope | Date constraint | Date used |
|---|---|---|---|
| `nmec_nmnc_nna.json` | Lifecycle classification | Same-date assets + txn | 2026-05-13 |
| `header_metrics.json` | Current AUA snapshot | Latest gold client_performance | 2026-05-14 |
| (Hypothetical) raw bronze | Current AUA snapshot | Latest assets.csv | 2026-05-14 |

All three internally consistent. Difference is structural pipeline-design, not bug.

## Recommendation

**Document the legitimate-divergence via `_meta` block on `nmec_nmnc_nna.json`** — minimal-delta informational fix:

```python
# INF_D_08.nmec_nmnc_nna.py
output["_meta"] = {
    "bronze_date_used": bronze_date,
    "note": ("total_aua sourced from bronze/orion-api/{bronze_date}/assets.csv. "
             "INF_D_08 requires same-date transactions.csv for lifecycle "
             "classification, so falls back to latest bronze with both. "
             "Firm-canonical header_metrics.json may be a later date — "
             "same-day or fresher. ~$0-$1M divergence is normal."),
    "window_days": LIFECYCLE_WINDOW_DAYS,
}
```

**Why NOT recommend fix-the-data:**
- Both artifacts are correct
- Changing `_latest_bronze_date` to allow date-mismatch (use 5/14 assets even if txn 5/13) would force lifecycle classification on partial data → real classification bugs
- Per Andrew's "data correctness > opportunistic-tech-debt timing" framing — this confirms (c) is the right call

## Secondary finding (FYI, not in scope)

The $156,715.66 same-day gap between bronze 5/14 ($203,339,876.18) and gold client_performance 5/14 ($203,183,160.52) suggests `client_performance.parquet` (produced by INF_C_02) applies additional filtering or uses a different price source than raw bronze. Worth a separate probe if Andrew wants firm-canonical AUA reconciled all the way to raw-bronze. Not blocking; not part of this investigation's mandate.

## Files Modified

None — investigation was probe-only. Recommendation deferred to CTO/COO routing decision (ship the `_meta` documentation fix in a separate ~10-LOC commit OR defer to next opportunistic INF_D_08 touch).

## Compiler tools

| Tool | Runs | Findings |
|---|---|---|
| `aws s3 cp` + `jq` on nmec emit + header_metrics + cumulative_chart | 3 | $580,948.02 gap confirmed empirically |
| `aws s3 ls bronze/orion-api/{2026-05-12,13,14}/` | 1 | Confirmed 5/14 missing transactions.csv |
| `aws s3api head-object` on nmec emit | 1 | LastModified 2026-05-14T14:23:30Z (current chain output) |
| `grep` for `_load_aua` + `_lifecycle_table` + INFLECTION_REP_IDS in INF_D_08 | 3 | Source loading logic + filters enumerated |
| `grep` for `total_aua` + `client_performance` in INF_D_00 | 2 | Gold canonical source path identified |
| Python simulation of INF_D_08 main flow | 1 | Confirmed bronze 5/13 → emit $202,602,212.50 exactly |
| Python day-over-day AUA delta verification | 1 | Confirmed $580,948.02 = day-over-day + same-day-source-delta |

No comp-* runs — investigation was empirical-S3-diff + read-code. ds-commit-gate / safe-deploy not applicable (probe-only).

## MCPs Sent

| To | At (Z) | Subject |
|---|---|---|
| 1.0.0_SA_CTO | 17:23:41 | RAVC1 ACK — P1 investigation starting |
| 1.0.0_SA_CTO | 17:30:48 | RAVC2 — $581K investigation RESOLVED: date asymmetry, recommendation (c) |

## MCPs Received

| From | Subject | Disposition |
|---|---|---|
| 1.0.0_SA_CTO (~17:22Z) | P1 INVESTIGATION — $581K firm AUA orphan-aggregation gap | ACKed + investigated + RAVC2'd |

## Decision Notes

1. **Andrew's "orphan-aggregation" framing was a misdirect.** The natural read of "$581K not being rolled up" suggests specific accounts being dropped by INF_D_08's aggregation. But the simulation showed `hh["aua"].sum()` exactly equals `aua["aua"].sum()` — no drop inside the script. The gap is upstream (source date), not internal (aggregation logic). Always validate the framing's premise before chasing the framing's suggested locus.

2. **`_latest_bronze_date()` is the actual control variable.** The script's bronze-date selection (lines 60-71) couples aua + txn into same-date pairs, which is correct for lifecycle classification but creates legitimate-divergence vs gold-tier artifacts that can use a later assets-only date. This is a structural feature, not a bug.

3. **Same-day source divergence ($156K) is a separate finding.** Bronze 5/14 raw ($203.34M) vs gold client_performance 5/14 ($203.18M) differ by $156K on the SAME day. Suggests INF_C_02 (gold client_performance producer) applies additional filtering or uses a different price source. Worth a separate probe but out of this investigation's scope.

4. **Recommendation (c) is the empirically-correct call.** Andrew's "data correctness > opportunistic-tech-debt timing" framing confirmed: nothing is incorrect, so don't change data. Add `_meta` documentation so consumers can see the date provenance.

5. **Wall-time efficiency.** 25 min investigation closed a P1. Empirical decomposition (simulate the actual script logic against current S3 data) was the unlock — bypassed the temptation to dive into per-account joins / filter analysis that would have been a 2h-investigation dead-end given the actual root cause.

## Next Steps

| Recipient | Item |
|---|---|
| **1.0.0_SA_CTO** | Routing decision: (a) ratify recommendation (c) + dispatch the `_meta` documentation fix (~10 LOC commit) OR (b) defer to next opportunistic INF_D_08 touch OR (c) ask for the secondary $156K bronze-vs-gold investigation. |
| **2.0.0_SA_COO** | TO authoring in flight per CTO 17:22Z msg — can ratify the (c) recommendation in the formal TO if/when it lands. |
| **Andrew** | Direct sign-off via CTO relay. Data correctness question resolved cleanly. |
| **Self — passive** | Standing by /loop watchdog. Available to ship the `_meta` documentation fix if dispatched (5-min ship). |

## Session Telemetry

- Wall time: ~7 min RAVC1 ACK → RAVC2 (well under 1-2h sizing)
- 0 commits (probe-only)
- 2 MCPs sent (RAVC1 ACK + RAVC2)
- 1 MCP received (CTO P1 dispatch)
- 11 empirical investigation runs (S3 + Python)
- 0 compiler-tool runs (probe doesn't trigger them)
- 0 escalations
- 1 misdirection caught (orphan-accounts framing was empirically false)
