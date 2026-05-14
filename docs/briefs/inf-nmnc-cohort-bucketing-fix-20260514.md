# INF NMNC Cohort Bucketing Fix — Per-HH Inception Emit Model

**Author:** 0.4.0_DS_ClientPlatform~D
**Date:** 2026-05-14
**Audience:** 2.0.0_SA_COO (for distribution to 0.4.0_DE_ClientPlatform)
**Status:** Design proposal — DS+DE coord required
**Trigger:** Andrew 2026-05-14 spot-check on IWM NMNC ($20M current quarter vs ~$5M historical baseline) surfaced that the NMNC model is structurally wrong for the portal's view-mode bucketing.

---

## TL;DR

The portal's "NMNC by quarter / month / year" view is computed off a **single rolling-365-day lifecycle window**. That's the wrong shape: every period block (Q1 / Q4 / Q3 / current) anchors its 365d cutoff to that period's end date and re-classifies the same population, so adjacent quarters show overlapping cohorts and the numbers drift monotonically rather than reflecting "clients who entered IN that quarter."

The intended model (Andrew direct 2026-05-14): NMNC is a **per-HH cohort attribute** keyed off inception date (first_trade_date / first_txn_date). Each view mode (monthly / quarterly / annual) buckets clients dynamically by whether their inception falls within the bucket's date range. Same client appears in exactly one bucket per view mode; no overlap; numbers reflect real per-period acquisition.

Fix is small at the data layer — per-HH inception is already computed at gold (`INF_D_04._compute_hh_lifecycle()` line 992-1107 and `INF_D_08._lifecycle_table()` line 213-217) — just isn't *emitted*. Aggregator + FE need the per-HH list to do the bucketing.

---

## 1. Empirical confirmation (from chain `chain_full_20260514_131842` output)

`s3://opal-data-inf/platinum/firm/partner_analytics_quarterly.json` `views.aua.{period}.donut.segments[nmnc]`:

| Period | Anchor date | Rolling-365d cutoff | NMNC AUA reported |
|---|---|---|---|
| `current` | 2026-05-14 | 2025-05-14 | **$19,979,134** |
| `q1` | 2026-03-31 (Q1 '26) | 2025-03-31 | $16,271,487 |
| `q2` | 2025-12-31 (Q4 '25) | 2024-12-31 | $12,604,363 |
| `q3` | 2025-09-30 (Q3 '25) | 2024-09-30 | $11,847,354 |

Same client population overlaps across all four periods — a client who onboarded in 2025-10 appears as NMNC in q2/q1/current AND in q3 (just past the q3 cutoff). The growth is therefore not "per-quarter inception," it's "rolling 12-month onboarding lookback from a different anchor each time."

Andrew's mental model: "$5M typical, $20M this quarter" maps to **per-quarter inception AUA** — i.e., AUA brought in by clients whose first_trade_date fell IN that calendar quarter. Today's chain output cannot answer that question without changing the artifact shape.

---

## 2. Current implementation (the load-bearing surfaces)

### 2a. `INF_D_04.client_portal_summary.py` — produces `partner_analytics_quarterly.json` (and monthly + annual siblings)

- Line 992: `_compute_hh_lifecycle(accounts_dim, holdings, nna, data_as_of, window_days=365, ...)`
- Line 1023: `cutoff = pd.Timestamp(data_as_of) - pd.Timedelta(days=window_days)`
- Line 1097-1100: `nmnc_mask = hh['first_trade_date'] >= cutoff; hh['lifecycle'] = 'nmec' + nmnc_mask -> 'nmnc'`
- The function is CALLED multiple times per artifact, once per view-mode period — but each call uses the same 365d span anchored at that period's end. The bucketing is "trailing-window-from-anchor," not "inception-in-period."
- Andrew directive cited inline at line 1000: "nmnc + nmec = total_aua, binary split" — *that* invariant stays; what changes is the cutoff semantic.

### 2b. `INF_D_08.nmec_nmnc_nna.py` — produces `platinum/firm/nmec_nmnc_nna.json` (firm + per-advisor aggregates)

- Line 18: `LIFECYCLE_WINDOW_DAYS = 365`
- Line 213-217: `first_txn = txn.groupby("household_id")["TransDate"].min()` — inception IS computed
- Line 232: `nmnc_mask = hh["first_txn_date"] >= cutoff` — classified, aggregated, per-HH inception discarded
- Side-artifact for the firm-level overview; not load-bearing for the quarterly view.

### 2c. Portal frontend

- Consumes `partner_analytics_quarterly.json` `views.aua.{period}.donut.segments[nmnc]` directly as cumulative-AUA numbers.
- View-mode toggle (monthly / quarterly / annual) picks the right sibling artifact, but each sibling has the same rolling-window model baked in by INF_D_04.
- DE owns FE consumption.

---

## 3. Proposed model

**Data shape:** emit a per-HH lifecycle list as part of the platinum payload. Suggested key: `platinum/firm/hh_lifecycle.json` (new artifact) OR augment `partner_analytics_quarterly.json` with a top-level `hh_lifecycle` array. Each record:

```json
{
  "household_id": 49342,
  "advisor_key": "patrick_scanlan",
  "rep_id": 11,
  "first_trade_date": "2025-08-14",
  "aua": 1247392.55,
  "window_net_nna": 982140.00
}
```

`window_net_nna` is the net inflow in trailing 365d from data_as_of — keep for back-compat with the existing NMEC `window_inflows` aggregation pattern (D_04 line 1098+). Can be dropped once FE is fully on the new model.

**Bucketing logic (FE OR aggregator, depending on where we settle):**

- Quarterly view, bucket = `2026-Q2`: NMNC = sum(aua) where `first_trade_date in [2026-04-01, 2026-06-30]`
- Monthly view, bucket = `2026-05`: NMNC = sum(aua) where `first_trade_date in [2026-05-01, 2026-05-31]`
- Annual view, bucket = `2025`: NMNC = sum(aua) where `first_trade_date in [2025-01-01, 2025-12-31]`

NMEC for the same bucket = `total_aua - NMNC` (preserves the Andrew 2026-05-06 binary split invariant: `nmnc + nmec = total_aua`).

**Where bucketing lives:**

- **Option A (FE buckets):** ship per-HH list as-is; FE filters by view-mode period. Cleaner separation, dynamic bucketing without artifact regeneration. Andrew's stated preference ("frontend can bucket them depending on view mode").
- **Option B (aggregator pre-buckets):** INF_D_04 emits pre-computed NMNC per period under the new model. Larger artifact diff, but FE stays simple. Worse cache invalidation: any new client requires aggregator rerun.

Recommend Option A. INF_D_04 still emits the totals + per-period AUA totals it produces today (those are unaffected — only the NMNC/NMEC split changes), plus the new per-HH inception array.

---

## 4. Scope split

| Lane | Responsibility | Effort |
|---|---|---|
| DS~D | INF_D_04: emit per-HH `hh_lifecycle` array (with `household_id`, `advisor_key`, `rep_id`, `first_trade_date`, `aua`, `window_net_nna`) alongside existing `views.aua` blocks; keep rolling-window aggregates as legacy fields for back-compat during cutover | ~3-4h |
| DS~D | INF_D_08: same emit pattern on the firm + per-advisor side; keep current `nmnc_aua / nmec_aua` aggregates as legacy fields | ~1h |
| DE 0.4.0 | FE: consume per-HH array; in the view-mode toggle, dynamically bucket by inception date; replace donut/distribution NMNC reads from `views.aua.{period}.donut.segments[nmnc]` with FE-side computed bucket | ~3-5h (depends on how many components hit the NMNC segment) |
| DE 0.4.0 | FE: TypeScript schema for the new array (`HhLifecycleRow`); component tests | ~1h |

Total ~9-11h. Coordination cost: one DS-DE check-in mid-flight to lock the array shape before DS commits (45min slot).

---

## 5. Validation plan

After Andrew's "$5M typical, $20M current" surface, we need to know whether the per-quarter-inception NMNC AUA actually shows:

- A typical baseline of ~$5M
- A current-quarter spike to ~$20M
- And if so, **what drove the spike** (is it real new-client onboarding or a data issue — e.g. an Orion dim refresh re-keyed legacy HH_IDs so they look "new")

Recommend a 5-minute empirical probe BEFORE the DS edit: pull `gold/dimensions/accounts_dimension_latest.parquet` + the bronze transactions for trailing 4 quarters; group by HH first_txn_date bucketed into calendar quarters; report per-quarter inception AUA sums. This is a read-only data spot-check that confirms (or refutes) Andrew's intuition. If the spike is real, ship the fix and Andrew sees it. If the spike is a data artifact, surface to AE/COO before the fix because the underlying bronze/silver has a problem.

---

## 6. Compatibility / cutover

- Existing `views.aua.{period}.donut.segments[nmnc]` fields STAY in the artifact during cutover — FE switches to FE-computed buckets first, then we deprecate the rolling-window fields once the legacy view is gone.
- The Andrew 2026-05-06 binary invariant (`nmnc + nmec = total_aua`, no "existing" residual) is preserved.
- No PROD chain re-fire needed for the fix to materialize beyond the normal nightly run — artifact regenerates with both old + new fields; FE switches when DE ships.
- Reversible: if the new model surfaces an unexpected issue, FE can revert to consuming the legacy rolling-window field while DS/DE iterate.

---

## 7. Open questions for COO routing

1. **Project code:** does this fit under an existing project (ADVI_INFLEC? ADVI_INFGRO?) or warrant a new short code (e.g. ADVI_NMCOHT for "NMNC cohort fix")? Andrew's stated intent suggests this is a single tight scope, not a multi-phase initiative — probably a single TO.
2. **Brief #5 probe — DS~D self-execute or route?** I have the bandwidth and the bronze access; happy to run it in-flight before the code edit. Flag if another lane should pick it up.
3. **DE alignment:** DE 0.4.0 needs the proposed array shape locked before commit. Recommend you forward this brief + I MCP DE 0.4.0 directly for the 45min schema-lock check-in.
4. **Phase 1 INFINC interaction:** none. NMNC bucketing fix is in the D-stage (latest-state Pattern D per AE brief §2.4) — orthogonal to the per-partition skip-gate work shipped today (`d88b7a7a4`). No coordination block needed with ADVI_INFINC.

---

## 8. Concrete next steps

1. **COO:** forward this brief to DE 0.4.0; either author a single-TO scope (recommend) or assign me to draft one.
2. **DS~D (me):** in parallel, run the §5 empirical probe (5 min wall) so we know if the $20M is a real spike or a data artifact before the edit lands. Will MCP findings to you + DE + Andrew.
3. **DS~D:** open the INF_D_04 + INF_D_08 edits as soon as DE lock on `HhLifecycleRow` shape lands. ds-commit-gate + safe-deploy per CLAUDE.md Rule 13 + 14.

— DS~D
