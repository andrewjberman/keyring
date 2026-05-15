# DS~C Session 2 — P1 Snapshot-GEO-AUA percentile math fix (FE synthesizer grain-mismatch bypass)

**Date:** 2026-05-14
**Agent:** 0.4.0_DS_ClientPlatform~C
**Authorization:** CTO P1 dispatch (Andrew empirical from PROD/DEV smoke) — RAVC1 ACK 15:00:41Z
**TO:** none (P1 incident dispatch — CTO session-direct; no formal TO file)
**Commit:** `1d9848aab`
**Wall time:** ~15 min CTO dispatch → safe-deploy PASS (~8 min diagnosis + 7 min code + verify + push)

## TL;DR

CTO P1 (Andrew empirical): Snapshot-GEO-AUA "Account Sizes By State" displayed visually-wrong percentiles. Histogram peak at $83K-$187K range (~75 accounts in $125K-$187K bucket) but displayed P50=$30.5K — clearly on the left tail, not at the bell peak.

Diagnosis: **bug is FE-side**, not DS-side. DS emit at `views.geo.current.distribution.total` has correct flat stats (`p50: $101K`). But `percentiles.{p10..p90}` block is absent (null), triggering FE's `withSynthesizedPercentiles` fallback (RD `1574ba7d`). That helper's internal `pctile()` uses `target = count * q` where `count` is DS-emitted HH-grain (305) while `histogram.counts` are per-account-grain (~770) — grain mismatch sends all percentile markers to the left half of bins.

Empirical confirmation: P50 target = 305 * 0.5 = 152.5; cumulative bin counts cross 152.5 at bin 8; `sqrt(24978 * 37347) ≈ $30,541` — **exactly the displayed $30.5K**. All five displayed percentiles ($6.11K / $13.7K / $30.5K / $45.7K / $68.3K) map to bin geometric midpoints at the broken indices.

**Smallest-delta DS-side ship (1d9848aab):** emit `percentiles.{p10..p90}` block on `views.geo.current.distribution.{total, by_segment[*]}` in `_build_geo_view_inf` (line 2243-2272 area) — FE no-ops the synthesizer via DistributionTab.tsx:150 guard. Same pattern also applied to `_build_adv_view` for cohort shape consistency + future-grain-shift immunization. AUA cohort (`_build_aua_view`) not touched — emits no histogram so synthesizer short-circuits.

**FE structural fix needed (separate ship — FYI sent to DE 0.4):** `pctile()` should use `aggCounts.reduce((s, c) => s + c, 0)` (histogram count sum) as target divisor, NOT `count`. Eliminates the bug class regardless of count grain.

## Diagnostic walkthrough

**Step 1: empirical-verify the deployed emit.**

```bash
aws s3 cp s3://opal-data-inf/platinum/firm/partner_analytics_quarterly.json - \
  | jq '.views.geo.current.distribution.total'
```

```json
{
  "count": 305,
  "sum": 203183160.52,
  "mean": 253978.95,
  "p25": 31232.24,
  "p50": 101360.85,        // ← correct firm-AUA per-account quantile
  "p75": 280165.94,
  "min": 0.01,
  "max": 3118341.4,
  "percentiles": null,     // ← block absent — triggers FE synthesizer
  "histogram_bins_len": 21,
  "histogram_counts_len": 20,
  "counts_sum": 770        // ← per-account-grain (305 HH * ~2.6 accts/HH)
}
```

DS emit was emitting correct flat stats but the displayed values didn't match. Sniff: FE must be doing something with the `null` percentiles.

**Step 2: check the chart's actual data source.**

The "Account Sizes By State" chart's "Total Accounts: 799" label suggested the chart might read `header_metrics.json.account_distribution` (raw list of 800 `{account_id, aua}` pairs, sum ≈ 799 ignoring $0.01 outliers). Hand-computed true percentiles from that raw list:

| Percentile | True per-account | Displayed |
|---|---|---|
| P10 | $9,418 | $6,110 |
| P25 | $31,232 | $13,700 |
| P50 | $101,455 | $30,500 |
| P75 | $280,613 | $45,700 |
| P90 | $700,325 | $68,300 |

Truth ≠ display. So chart is NOT reading `account_distribution`; it's reading the partner_analytics emit and the FE is mangling percentiles.

**Step 3: read the FE helper.**

`portal/src/pages/AdvisorIntelligence/_shared/tabs/DistributionTab.tsx:142` (`withSynthesizedPercentiles`):

```typescript
function withSynthesizedPercentiles(d, overrideCount?) {
  if (!d) return null
  const projected = (overrideCount != null && overrideCount > 0)
    ? { ...d, count: overrideCount }
    : d
  if (projected.percentiles?.p50 != null) return projected   // ← line 150 guard
  if (!projected.histogram?.counts?.length) return projected
  const agg = aggregateDistributions([d], overrideCount ?? null)
  // ... merges agg.percentiles back into projected
}
```

Inside `aggregateDistributions.pctile()` (line 190-202):

```typescript
const pctile = (q: number): number | null => {
    const target = count * q                  // ← BUG: HH-grain count
    let cum = 0
    for (let i = 0; i < nbins; i++) {
      cum += aggCounts[i]                     // per-account-grain counts
      if (cum >= target) {
        const lo = ref.histogram.bins[i] ?? 0
        const hi = ref.histogram.bins[i + 1] ?? lo
        return lo > 0 && hi > lo ? Math.sqrt(lo * hi) : lo
      }
    }
    return ref.histogram.bins[nbins - 1] ?? null
}
```

`count = d.count = 305`. Target for P50 = 152.5. Cumulative histogram counts: [6, 10, 17, 27, 35, 67, 96, 143, 199, ...] — crosses 152.5 at bin 8. Bin 8 edges = $24,978 and $37,347. `sqrt(24978 * 37347) ≈ $30,541` — **exactly the displayed $30.5K**.

Verified all five displayed values map to bin geometric midpoints at indices the broken target produces.

**Step 4: pick the fix.**

Two valid fixes:

| Fix | Location | Effect | Cost |
|---|---|---|---|
| Emit `percentiles.{p10..p90}` block | DS (`_build_geo_view_inf` + `_build_adv_view`) | FE no-ops synthesizer via line-150 guard | +50 LOC, single ship, immediate unblock |
| Use `aggCounts.reduce((s,c)=>s+c,0)` as target divisor | FE (`aggregateDistributions.pctile`) | Eliminates bug class regardless of count grain | requires DT push + portal cycle |

Chose DS-side ship (immediate) + flag FE structural fix as separate to DE 0.4. Same pattern as INFFIN.014's NNA emit + INFGRO.004's NaN strip — defense-in-depth at the DS boundary.

## Files Modified

| File | Change | Commit |
|---|---|---|
| `data/orion/scripts/gold/INF_D_04.client_portal_summary.py` | +50/-0: emit `percentiles.{p10..p90}` block on `views.geo.current.distribution.{total, by_segment[*]}` (lines 2243-2289 area, `_build_geo_view_inf`) AND `views.adv.current.distribution.{total, by_segment[*]}` (line 2407-2454 area, `_build_adv_view`). Computed via existing `aua_series.quantile(0.10/0.25/0.50/0.75/0.90)` calls — same source data as the flat stats already emit. | `1d9848aab` |

## Deploy Evidence

| Step | Result |
|---|---|
| `.tools/ds-commit-gate.sh INF_D_04.client_portal_summary.py` | All checks passed (py_compile + AST + ruff py39 0.15.11) |
| `git status data/orion/scripts/gold/` | Only target file dirty |
| Author | `0.4.0_DS_ClientPlatform~C <0.4.0_DS_ClientPlatform_C@opal.agent>` |
| Commit | `1d9848aab` |
| Push | `94e523a4f..1d9848aab` (other agents pushed between my a731e8461 and this; clean FF) |
| safe-deploy.sh (pre-push) | `DEPLOYED [inf] data/orion/scripts/gold/INF_D_04.client_portal_summary.py` PASS |
| S3 path | `s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py` |
| S3 ETag | `a38103cfae642cb07ecf1e203c330bcd` |
| S3 LastModified | 2026-05-14T15:08:10Z |
| S3 ContentLength | 191,486 bytes |

## Compiler Tools

| Tool | Runs | Findings |
|---|---|---|
| `aws s3 cp .../partner_analytics_quarterly.json - \| jq` (deployed emit shape) | 4 runs | Confirmed `percentiles: null` block + `count=305` HH-grain + `histogram.counts.sum=770` per-account-grain mismatch |
| `aws s3 cp .../header_metrics.json - \| jq` (alternative source check) | 1 run | Confirmed `account_distribution` has 800 raw `{account_id, aua}` pairs — not the chart source |
| `aws s3 cp .../partner_analytics_quarterly.json - \| jq '.account_distribution \| sort \| percentiles'` (true-value hand-recompute) | 1 run | Empirical: P10=$9.4K / P50=$101K / P90=$700K (matches DS-emit flat stats, NOT displayed) |
| `Grep withSynthesizedPercentiles\|synthesizePercentiles` on portal/src | 1 run | Located bug site at DistributionTab.tsx:142 + aggregateDistributions at line 170 + pctile at line 190 |
| Hand-trace `pctile(0.5)` against deployed data | 1 run | Target = 305 * 0.5 = 152.5 → cum crosses at bin 8 → `sqrt(24978*37347) ≈ $30,541` — matches displayed P50=$30.5K exactly |
| `.tools/ds-commit-gate.sh` | 1 run | PASS |
| `.tools/safe-commit.sh --author=...` | 1 run | Clean commit `1d9848aab` |
| `.tools/safe-deploy.sh` (pre-push hook) | 1 run | DEPLOYED [inf] PASS |
| `aws s3api head-object` | 1 run | ETag `a38103cfae642cb07ecf1e203c330bcd` @ 15:08:10Z, 191,486 bytes |

**Compiler-tool gaps reaffirmed (no new findings):**
- `comp-pipescript deployed` bucket-scope for INF — verified via direct head-object instead
- `comp-platinum reverse` skipped — single consumer is known (DistributionTab.tsx)

## MCPs Sent

| To | At (Z) | Subject |
|---|---|---|
| 1.0.0_SA_CTO | 15:00:41 | RAVC1 ACK — GEO-AUA percentile math investigation starting |
| 1.0.0_SA_CTO | 15:08:39 | RAVC2 — P1 GEO-AUA percentile fix SHIPPED — 1d9848aab — bug is FE synthesizer grain mismatch |
| 0.4.0_DE_ClientPlatform | 15:08:53 | FYI — FE synthesizer grain-mismatch bug surfaced + surgical patch sketch |

## MCPs Received

| From | Subject | Disposition |
|---|---|---|
| 1.0.0_SA_CTO (~15:00Z) | P1 — Snapshot-GEO-AUA percentiles math empirically wrong (Andrew direct) | ACKed + diagnosed + shipped |

## Next Steps

| Recipient | Item |
|---|---|
| **AE 0.6.1** | Three INF_D_04 ships stacked on origin/CLOUD now (`a731e8461` INFFIN.014 + ?intermediate? + `1d9848aab`). All materialize together on next chain. No fresh trigger from me. |
| **DE 0.4** | FE structural fix per the surgical patch sketch I sent — `aggCounts.reduce((s,c)=>s+c,0)` as target divisor in `pctile()`. Bug-class elimination; correctness-hardening for future histograms emitted without percentiles. No urgency — my DS ship unblocks the immediate symptom. |
| **RD 0.4.2** | Visual confirm post-chain: P10/P25/Median/P75/P90 chip strip on Snapshot/GEO/AUA "Account Sizes By State" should now display $9.4K / $31K / $101K / $280K / $700K (or close) — matching the histogram peak position. |
| **Self — passive** | Standing by for chain materialize. Sentinel check `jq '.views.geo.current.distribution.total.percentiles.p50'` on `partner_analytics_quarterly.json` post-chain — expect ≈ $101K, not null. |
| **Andrew** | Direct visual sign-off post-chain. |

## Decision Notes

1. **DS-side defense-in-depth vs FE structural fix tradeoff.** Both fixes are valid; FE structural fix is the cleaner long-term shape but requires DT push + portal cycle. DS-side ship is immediate, single-file, low-risk. The two compose — emit percentiles block AND fix the FE algorithm. Pursuing both in parallel (FE-side via DE 0.4) follows the same "two structural layers" pattern as INFGRO.004 NaN cleanup (gold strip + FE strip both live).

2. **Why ADV cohort got the same fix even though it wouldn't trigger the bug.** `_build_adv_view` uses per-account count grain (`acct_aua['account_id'].nunique()`) — matches histogram grain. FE synthesizer would compute correct percentiles there. But emitting the percentiles block is near-zero risk + keeps cohort shape consistent + immunizes against future grain shifts. Same logic applied at the INFFIN.014 ship (defense-in-depth across cohorts).

3. **Why AUA cohort (`_build_aua_view`) NOT touched.** It emits no histogram → FE synthesizer short-circuits at line-151 guard (`if (!projected.histogram?.counts?.length) return projected`). No bell-curve render on that surface, no bug to fix. Out of scope.

4. **Hypothesis match against CTO's three suspects.**
   - (1) Bin-index instead of midpoint: ACTUALLY using midpoints (`sqrt(lo*hi)`), but at wrong INDICES — partial match
   - (2) Percentiles on count distribution instead of value distribution: CLOSER — uses cumulative bin counts as the lookup mechanism, but the bug is the TARGET divisor not the lookup method
   - (3) Wrong field selection: not the case — `d.histogram` and `d.count` are the right fields, just at incompatible grains

   The actual bug is a **grain mismatch** between two fields the synthesizer treats as compatible. None of the three hypotheses caught it cleanly, but (2) was closest.

5. **Stacked ship coordination.** Three INF_D_04 commits today (INFFIN.014 NNA histogram + this P1 GEO-AUA percentile + ?intermediate?). They're all additive (new fields on existing artifacts, no field renames or removals); no merge conflict expected; all materialize together. Chain #30 recovery sequencing per COO 14:13Z msg + AE 0.6.1's signal queue manages ordering.

## Session Telemetry

- Wall time: ~15 min RAVC1 → safe-deploy PASS
- 1 substantive commit (1d9848aab)
- 1 file modified (+50/-0)
- 1 MCP sent pre-ship (RAVC1 ACK)
- 1 MCP sent post-ship (RAVC2 CTO)
- 1 MCP sent post-ship (DE FYI with surgical patch sketch)
- safe-deploy gate PASS on first try
- Empirical hand-trace pre-commit confirmed bug location + fix shape
- 8-min diagnosis + 7-min ship — diagnosis-heavy, edit-light
