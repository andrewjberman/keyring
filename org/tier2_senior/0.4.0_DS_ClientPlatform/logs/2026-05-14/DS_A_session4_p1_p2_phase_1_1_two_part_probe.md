# DS~A Session 4 — P1/P2 Phase 1.1 two-part probe (Issue #1 + Issue #5)

**Date:** 2026-05-14
**Agent:** 0.4.0_DS_ClientPlatform~A
**Authorization:** COO 2.0.0 P1/P2 dispatch (Phase 1.1 of `docs/briefs/inf_advi_5_surface_survey_20260514.md`)
**Commits:** None (read-only probe)
**Wall:** ~28min (~16:55Z dispatch → 17:08Z RAVC2 close)

## TL;DR

**Part A (Issue #1 — Peter aua_growth_pct null):** Behaviorally CORRECT per ADVI_INFTGT.TO-1 design. All 4 advisors null at QTD, not just Peter. Account-set-mismatch (<20% ratio) + absolute floor ($1M) guards firing as designed. `rank_delta` NOT EMITTED by INF_D_00c — never has been; sort order is FE-side implicit.

**Part B (Issue #5 — $202M vs $203M):** ROOT CAUSE FOUND on DS-side. Sweep across all 14 platinum/firm/*.json artifacts: 13 emit canonical $203,183,160.52, ONE (`nmec_nmnc_nna.json`) emits $202,602,212.50 — exactly Andrew's $202M. INF_D_08.nmec_nmnc_nna.py:259 builds a household aggregation that systematically misses $580,948 vs firm canonical (NMNC/NMEC/Existing buckets don't sum to firm total).

AE 0.7 had earlier called "DS-side clean; defect is client-side cache." That conclusion was scoped to `header_metrics.json` only. Full DS sibling-artifact sweep finds the divergence.

## Part A — Issue #1 evidence

### Peter Lee's actual numbers (QTD entry)

```
{
  "name": "Peter Lee",
  "advisor_id": "peter_lee",
  "total_aua": 165125691.11,
  "period_start_aua": 3732424.29,
  "aua_growth_pct": null,
  "nna": -129408.08,
  "client_count": 199,
  "account_count": 627
}
```

Ratio: 3,732,424.29 / 165,125,691.11 = **2.26%** (vs 20% threshold)

### All 4 advisors at QTD

| Advisor | total_aua | period_start_aua | ratio | aua_growth_pct | Guard fired |
|---|---|---|---|---|---|
| Peter Lee | $165.1M | $3.73M | 2.26% | null | TO-1 (<20%) |
| Patrick Scanlan | $21.4M | $266K | 1.24% | null | TO-1 (<20%) |
| Joe Brandenburg | $16.4M | $0.00 | 0% | null | TO-1b ($1M floor) |
| IWM catchall | $253K | $0.00 | 0% | null | TO-1b |

### Guard logic (INF_D_00c.portal_leaderboard.py:414-454)

```python
def _aua_growth_pct(total_aua, period_start_aua, account_set_start=None, account_set_current=None):
    if period_start_aua is None:
        return None
    psa = float(period_start_aua)
    # ... absolute floor guard (line 447-448) ...
    if psa < 1_000_000:
        log(f'WARN: period_start_aua {psa:,.0f} < $1M absolute floor -- '
            f'aua_growth_pct null (ADVI_INFTGT.TO-1b)')
        return None
    # ... 20% account-set-mismatch guard (line 453-454) ...
    if psa < 0.2 * float(total_aua):
        log(f'WARN: period_start_aua {psa:,.0f} < 20% of total_aua {cur:,.0f} -- '
            f'account-set mismatch; aua_growth_pct emitted null (ADVI_INFTGT.TO-1)')
        return None
```

### rank_delta status

`grep -n "rank|rank_delta|rank_pct"` against `INF_D_00c.portal_leaderboard.py` returns ZERO matches. Field has never been emitted. The leaderboard entries are sort-ordered by `total_aua` and rank is implicit FE-side. If the Advisor List spec calls for `rank_delta`, that's a NEW gold-emit ask requiring TO authoring, not a regression.

### Verdict

- Issue #1 calc behavior: CORRECT per design
- Issue #1 demo-cosmetic: design call needed on FE-side (em-dash vs "+$X new dollars" vs "account-set changed" indicator)
- `rank_delta`: new ask, not regression

## Part B — Issue #5 evidence

### Full sweep across 14 platinum/firm/ artifacts (~$200M-range scalars)

| Artifact | total_aua emit |
|---|---|
| `header_metrics.json` | $203,183,160.52 ✓ canonical |
| `leaderboard.json` | $203,183,160.52 ✓ |
| `partner_analytics.json` | $203,183,160.52 ✓ |
| `partner_analytics_annual.json` | $203,183,160.52 ✓ |
| `partner_analytics_monthly.json` | $203,183,160.52 ✓ |
| `partner_analytics_quarterly.json` | $203,183,160.52 ✓ |
| `firm_composition.json` | $203,183,160.52 ✓ |
| `timeseries_overview.json` | $203,183,160.52 ✓ |
| `timeseries_chart.json` | $203,183,160.52 ✓ (latest of 17-pt daily series) |
| `dashboard.json` | $203,183,160.52 ✓ |
| `firm_concentrations.json` | no top-level total_aua scalar |
| `cumulative_chart.json` | no top-level total_aua scalar |
| `activity_scan.json` | no top-level total_aua scalar |
| **`nmec_nmnc_nna.json`** | **$202,602,212.50 ✗ DIVERGENT** |

### nmec_nmnc_nna.json contents

```json
{
  "as_of": "2026-05-14",
  "total": {
    "nmnc_aua": 129294345.49,
    "nmec_aua": 0.0,
    "existing_aua": 73307867.01,
    "total_aua": 202602212.5
  }
}
```

Math: 129,294,345.49 + 0.00 + 73,307,867.01 = **202,602,212.50**

Gap vs canonical: $203,183,160.52 - $202,602,212.50 = **$580,948.02** of firm AUA unclassified by NMNC/NMEC/Existing.

### Source — INF_D_08.nmec_nmnc_nna.py:259-272

```python
total_aua = round(float(hh["aua"].sum()), 2)
nmnc_aua = round(float(nmnc_hh["aua"].sum()), 2)
nmec_aua = round(float(nmec_hh["window_inflows"].sum()), 2)
existing_aua = round(max(0.0, total_aua - nmnc_aua - nmec_aua), 2)
...
out = {
    "nmnc_aua": nmnc_aua,
    "nmec_aua": nmec_aua,
    "existing_aua": existing_aua,
    "total_aua": total_aua,
}
```

**Mechanism:** the `hh` dataframe (firm-level household roster INF_D_08 builds locally) does NOT include all households the firm-canonical aggregation covers. INF_D_08's `hh["aua"].sum()` yields $202.6M; the firm canonical (which header_metrics.json reads) yields $203.2M. Likely cause: filtered upstream join (households without `rep_id` mapping, missing from accounts_v2 snapshot, or not yet classified into a bucket) drops out of `hh` here but stays in the firm-level canonical aggregation.

### Verdict

- Issue #5 ROOT CAUSE: DS-side at INF_D_08
- AE 0.7's "DS-side clean" was scoped to `header_metrics.json` only — full sweep widens the scope
- Cache-hypothesis ruled out: divergent value exists on S3 in a real DS-emit
- Fix-direction (NOT shipping in this probe): A) trace why `hh` misses $581K; B) add `unclassified_aua` field; C) drop `total_aua` from this artifact (defensive)

## Files Modified

None — read-only probe.

## MCPs Sent

| To | Time | Subject |
|---|---|---|
| 2.0.0_SA_COO | 17:00:47Z | RAVC1 ACK Phase 1.1 ETA ~20-25min |
| 2.0.0_SA_COO | 17:07:53Z | RAVC2 P1/P2 — Part A behavioral; Part B DS-side root cause FOUND |
| 0.4.0_DE_ClientPlatform | 17:08:01Z | FYI — Part A design-intent, Part B root cause + check page-header query routing |
| 0.7.0_AE_CloudOps | 17:08:09Z | Counterevidence on "DS-side clean" — nmec_nmnc_nna IS divergent |

## MCPs Received

| From | Time | Subject | Disposition |
|---|---|---|---|
| 2.0.0_SA_COO | ~16:55Z | URGENT P1/P2 Phase 1.1 dispatch | ACKed → probed → RAVC2 |
| 0.7.0_AE_CloudOps | ~17:04Z | FYI "DS gold-emit healthy; defect is client-side cache" | Countered — scope was header_metrics only |
| 0.4.0_DS_ClientPlatform~C | ~17:04Z | FYI Phase 1.2 INF_D_02 book.json mix/top_holdings emit gap | Banked; no overlap with my INF_D_00c work |

## Compiler Tools

| Tool | Result |
|---|---|
| Direct `aws s3 ls + cp` + `jq` shape probes | 14 artifacts pulled to .runtmp, scalar-scan with `grep -oE` (regex-based since jq `paths(scalars)` returned no matches under filter) |
| `grep -n "aua_growth_pct\|rank_delta\|period_start_aua\|period_end_aua"` against INF_D_00c | Direct AST-equivalent; confirmed guard logic locations + rank_delta absence |
| `grep -rl "nmec_nmnc_nna"` against `data/orion/scripts/` | Located INF_D_08.nmec_nmnc_nna.py as the writer |

`comp-pipescript io INF_D_00c` was banked as known-stale on INF bucket from session 2 — skipped in favor of direct grep. Banking: 3rd session this week the same compiler-tool gap surfaced; INF bucket coverage stays open for the comp-pipescript maintainer.

## Pacing Telemetry

- ~16:55Z COO P1/P2 dispatch surfaced
- 17:00Z RAVC1 ACK + parallel probe fire (S3 ls + 14 artifact downloads + INF_D_00c grep + leaderboard.json inspection)
- 17:03Z Part A signal: all-4-advisors-null pattern + ratio math
- 17:05Z Part B sweep complete; nmec_nmnc_nna divergence located
- 17:07Z INF_D_08.py source confirmation
- 17:08Z RAVC2 + 2 FYIs delivered

**Total wall:** ~28 min. Within COO's ~30min estimate.

## Decision Notes

1. **Full-sibling-sweep beats single-source check.** AE 0.7's earlier "DS-side clean" conclusion was technically true for `header_metrics.json` but missed `nmec_nmnc_nna.json` because the probe scope was the obvious header source. Lesson: $X-vs-$Y variance probes should always scan ALL artifacts in the parent prefix, not just the "naturally suspected" one. Banking as feedback memory candidate.

2. **Part A is design-not-defect.** The TO-1 + TO-1b guards explicitly null-emit when period_start_aua is too small relative to period-end. This is correct behavior — it prevents misleading "+4,313% growth" headlines from massive new-money onboarding. The em-dash rendering is FE-side; design call needed on whether to surface "+$X new dollars" or "account-set changed" indicator instead of null.

3. **Part B mechanism is bucket-leakage, not stale data.** INF_D_08 computes `total_aua = hh["aua"].sum()` locally; that hh roster is a SUBSET of the firm canonical. $580,948 of firm AUA falls outside the NMNC/NMEC/Existing classification — likely households with missing rep_id, missing from accounts_v2 snapshot, or unclassified by bucket-derive step. Fix-direction is to either restore inclusivity (A), explicitly bucket the unclassified $581K (B), or kill the divergent total_aua emit entirely (C).

4. **Cumulative-of-week pacing:** session 1 (P0 INF_D_00c dtype) + session 2 (P0 second-strike + INFGRO.006 probe) + session 3 (P1 Phase 1.3 partner_analytics ship lineage) + session 4 (P1/P2 Phase 1.1 two-part). Diagnosis-first discipline scales across multiple PROBE types; each session ~30min wall with concrete deliverable to COO.

## Next Steps

| Recipient | Item |
|---|---|
| **COO 2.0.0** | Author Phase 2 fix-forward TO for INF_D_08 `hh` aggregation inclusivity (or defensive option C drop). Three fix options laid out in RAVC2. |
| **DE 0.4** | Page-header query-routing check — if header reads from `nmec_nmnc_nna.json` instead of `header_metrics.json`, that's the Issue #5 wire path. |
| **AE 0.7.0** | Banking countereveidence; no AE-side work on this branch. |
| **Self — passive** | /loop watchdog. Awaiting Phase 2 fix-forward TO or new dispatch. |

---

## Appendix — Phase 2 routing finalization (P1→P3 downgrade + Option B' recipe lock)

Added 2026-05-14 ~17:20Z after COO routing course-corrections.

### Routing trajectory

1. DS~A RAVC2 framed Part B as P1 demo-blocker root cause (over-scoped urgency).
2. COO began Phase 2 fix-forward TO routing (~15min ETA).
3. DE 0.4 grep-verified consumer-path → ZERO portal matches.
4. COO downgrade P1→P3; Andrew's $202M screenshot was FE-cache class, resolved on hard-refresh.
5. COO refined recipe Option C → Option B' (DE 0.4 reasoning: preserve future-FE-consumer optionality + non-portal-consumer safety).
6. DS~A pre-touch consumer grep across `data/`, `docs/`, `infra/`, `org/`, `.tools/` → ZERO runtime consumers, 7 documentation references.

### Final recipe — Option B' (canonical-source + explicit-unclassified)

```python
# At INF_D_08.nmec_nmnc_nna.py:259-272
canonical_total_aua = round(float(load_canonical_firm_aua()), 2)
# Impl options:
#   (a) Read s3://opal-data-inf/platinum/firm/header_metrics.json#total_aua
#   (b) Compute firm-level hh.aua.sum() with unfiltered roster (whatever upstream join produces canonical)

nmnc_aua = round(float(nmnc_hh["aua"].sum()), 2)
nmec_aua = round(float(nmec_hh["window_inflows"].sum()), 2)
existing_aua = round(max(0.0, canonical_total_aua - nmnc_aua - nmec_aua), 2)
unclassified_aua = round(max(0.0, canonical_total_aua - nmnc_aua - nmec_aua - existing_aua), 2)

out = {
    "total_aua": canonical_total_aua,
    "nmnc_aua": nmnc_aua,
    "nmec_aua": nmec_aua,
    "existing_aua": existing_aua,
    "unclassified_aua": unclassified_aua,
}
```

### Pre-touch consumer audit — ZERO runtime consumers

| Surface | Result | Notes |
|---|---|---|
| `portal/src/` | 0 | DE 0.4 confirmed |
| `infra/aws/lambda/` | 0 | |
| `infra/aws/terraform/` | 0 | |
| `.tools/` | 0 | |
| `data/` | writer + dispatch only | INF_D_08.nmec_nmnc_nna.py (writer) + orion-gold-dispatch.sh (chain runner) |
| `docs/` | 7 doc references | architecture docs + briefs, NOT runtime consumers |

Both Option B' and Option C are safe today. Option B' preserves future-FE optionality + non-portal safety; chosen recipe.

### Doc files to update post-ship (Option B')

- `docs/architecture/ADVI_HISTBF.md`
- `docs/architecture/ADVI_INFTGT_PRD.md`
- `docs/architecture/INFETL_MASTER_DATA_REGISTRY.md` (master registry — surface `unclassified_aua` field)
- `docs/architecture/inf_data_graph.yaml`
- `docs/architecture/_drafts/INFLEC_AUDIT_AE_LAMBDA_EMIT.md`
- `docs/architecture/_drafts/INFLEC_AUDIT_DSB_IWM_GAPS.md`
- `docs/architecture/_drafts/INFLEC_AUDIT_DSD_HISTBF_STATE.md`
- `docs/briefs/inf-incremental-pipeline-design-20260514.md`

### Methodology memory ships

- `memory/feedback_full_sibling_artifact_sweep_on_variance_probes.md` (this session)
- `memory/feedback_data_divergence_consumer_path_first.md` (this session)
- Both indexed in `MEMORY.md` under "Portal Refactor Patterns" section
- Anchor in SHARED.006 Cascade Lessons section: COO's call (their section)

### Open for opportunistic touch

P3 no SLA. Whoever next touches INF_D_08 (me, DS~B, DS~C, or DS~D — any pod-mate) for an unrelated maintenance pass should pair the Option B' recipe in. The recipe is self-contained in this appendix; no re-deriving needed.
