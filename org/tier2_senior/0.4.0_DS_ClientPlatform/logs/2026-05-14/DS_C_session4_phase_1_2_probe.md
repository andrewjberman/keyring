# DS~C Session 4 — Phase 1.2 P1/P3 Probe (Peter Lee BookView + cumulative_chart new_clients)

**Date:** 2026-05-14
**Agent:** 0.4.0_DS_ClientPlatform~C
**Authorization:** COO Phase 1.2 probe routing (17:00:42Z broker push) — RAVC1 ACK 17:01:09Z
**TO:** none (read-only diagnostic probe, ~30min wall; not a formal TO file)
**Probe report:** sent to COO + DE 0.4 + DS~A at 17:06:09Z-17:06:27Z
**Wall time:** ~7 min broker GO → probe report

## TL;DR

Two-part probe per COO 5-surface-survey brief follow-on.

**Part A (P1 demo-blocker): Peter Lee BookView empty Asset Mix / Top Holdings / Cost Basis** — root cause = DS book.json emit gap. Top-level `mix` is null + `top_holdings` / `concentration` / `mix_periods` keys ABSENT, but sibling artifacts (summary.json + composition.json + top_holdings.json) have the data fully populated. System-wide INF_D_02 issue, not Peter-Lee-specific. Cost Basis is actually populated at `tax_exposure.cost_basis_by_year` — that part is a FE-path bug, not a DS-data bug.

**Part B (P3 enhancement): "0 New Clients" on Continuous Segment Analytics** — root cause = `new_clients` field doesn't exist in cumulative_chart.json. Writer INF_D_00d already loads `accounts_v2` which has `first_trade_date` — feasible additive emit, ~30-60min fix-forward effort if prioritized.

No fix-forward in this probe per COO scope; Phase 2 dispatch decision belongs to COO.

## Part A — Peter Lee BookView empty fields

### Empirical S3 inspection

**`platinum/advisors/peter_lee/book.json`** (161,480 bytes, gen 14:20:44Z, data_as_of 2026-05-14):

```json
{
  "top_keys": [
    "active_since", "advisor_key", "book", "book_name", "clients",
    "data_as_of", "fee_summary", "firm_id", "generated_at",
    "relationship_stacked_periods", "role_breakdown", "summary",
    "tax_exposure"
  ],
  "book.total_aua": 165125691.11,
  "book.client_count": 199,
  "book.nna_ytd": 2225373.10,
  "mix (top-level)": null,
  "top_holdings (top-level)": MISSING,
  "concentration (top-level)": MISSING,
  "mix_periods (top-level)": MISSING,
  "fee_summary": populated,
  "tax_exposure.cost_basis_by_year": populated,
  "tax_exposure.taxable_pct": populated,
  "tax_exposure (11 keys total)": fully populated,
  "summary.tax": null,
  "summary.performance": null,
  "summary.total_aua": null
}
```

**`platinum/advisors/peter_lee/summary.json`** (46,588 bytes, gen 14:21Z) — separately emitted, FULLY POPULATED:

```json
{
  "top_keys": [
    "active_since", "advisor_id", "book", "concentration", "data_as_of",
    "distribution", "fee_summary", "generated_at", "mix", "mix_periods",
    "role_breakdown", "tax_exposure"
  ],
  "book.total_aua": 165125691.11,
  "book.client_count": 199,
  "mix (top-level)": object with 4 keys,
  "mix_periods": present,
  "concentration": present,
  "distribution": present,
  "tax_exposure.cost_basis_by_year": populated
}
```

**`platinum/advisors/peter_lee/composition.json`** (6,404 bytes, gen 14:21:52Z) — separately emitted:

```json
{
  "top_keys": [
    "_meta", "classification_caveats", "classification_method",
    "data_as_of", "generated_at", "mix", "other", "scope",
    "top_holdings", "total_market_value", "unclassified"
  ],
  "mix": array of 4 entries,
  "top_holdings": 9 entries,
  "total_market_value": 165125691.11,
  "classification_method": "orion_native_v1"
}
```

**`platinum/advisors/peter_lee/top_holdings.json`** (1,792 bytes) — separately emitted:

```json
{
  "top_keys": [
    "data_as_of", "generated_at", "holding_count", "other",
    "scope", "top_holdings", "total_market_value"
  ],
  "top_holdings": populated,
  "holding_count": present
}
```

### Cross-advisor verification

| Advisor | composition.json mix | top_holdings.json | total_market_value |
|---|---|---|---|
| joe_brandenburg | array, 4 entries | 9 entries | $16.4M |
| patrick_scanlan | array, 4 entries | 9 entries | $21.4M |
| peter_lee | array, 4 entries | 9 entries | $165M |

**All advisors have the same shape pattern** — sibling artifacts healthy, book.json gap is system-wide.

### Writer identification

| Artifact | Writer Script | Status |
|---|---|---|
| `book.json` | `INF_D_02.advisor_client_detail.py:1894` | grep for `'mix'` / `mix_snapshot` returned no matches in INF_D_02 — confirms it doesn't populate the top-level mix |
| `summary.json` | `INF_D_04.client_portal_summary.py:3546` (in `write_advisor_summaries`) | Lines 3489-3498 build `mix_snapshot` from composition.json data → embeds in summary.json |
| `composition.json` | `INF_I_D03.composition_artifacts.py` (sibling, per INF_D_02b.top_holdings.py:9 docstring "INF_I_D03's composition.json which is owned [there]") | Healthy across firm |
| `top_holdings.json` | `INF_D_02b.top_holdings.py` | Healthy across firm |

### FE consumer

`portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx:85`:

```typescript
const requiredKeys = ['book', 'mix', 'fee_summary', 'tax_exposure']
```

FE asserts presence of these top-level keys. With `mix: null`, the assertion fails → renders empty / placeholder for Asset Mix panel. `top_holdings` / `concentration` panels read separate fields that aren't in book.json either.

### Cost Basis — separate finding

`tax_exposure.cost_basis_by_year` IS PRESENT and populated in book.json. FE wiring at AdvisorBookView.tsx:570 reads `bookData.tax_exposure.cost_basis_by_year` — the data path is correct. So Andrew's "Cost Basis empty" observation is either:
1. A FE-side rendering bug (panel reads wrong field name or sub-key)
2. A different artifact path consumer (e.g., a separate `TaxCostBasisPanel.tsx` reading a different file)

DE 0.4 dispatched in probe-FYI to verify the FE-side rendering separately. Not a DS gap.

### Fix shape recommendations

| Option | Approach | Effort | Pros | Cons |
|---|---|---|---|---|
| **DS-1** (recommended) | INF_D_02 reads composition.json (or its precursor) post-INF_I_D03-emit and fans `mix` / `top_holdings` / `concentration` into book.json top-level | Single-LOC delta in INF_D_02 + 1 cross-script read | Preserves book.json canonical-payload semantic; book.json stays the single FE entry point | Cross-script read coupling; requires INF_I_D03 to run before INF_D_02 (already true per chain order) |
| **DS-2** | Move book.json emit AFTER summary.json + read summary.json fields | Larger refactor | Single source of truth (summary.json) | Deeper cross-script coupling + reorder existing chain |
| **FE** | AdvisorBookView reads summary.json instead of book.json for mix/top_holdings/concentration | FE patch only | No DS change | Breaks "book.json = canonical advisor payload" semantic; FE has to manage 2 paths |

**Recommended: DS-1.** Phase 2 dispatch decision belongs to COO.

## Part B — cumulative_chart "0 New Clients"

### Empirical S3 inspection

**`platinum/firm/cumulative_chart.json`:**

```json
{
  "top_keys": [
    "adv", "data_as_of", "date_range", "firm_id", "generated_at",
    "geo", "geo_aua_grain", "geo_drill", "nna_adv", "nna_geo"
  ],
  "new_clients (anywhere in tree)": NOT FOUND
}
```

`new_clients` field is entirely absent — confirming the FE's "0 New Clients" display is a missing-emit, not a stale-emit.

### Writer identification

`INF_D_00d.cumulative_chart.py` (CUMULATIVE_CHART_KEY at line 72). Grep for `new_clients` / `first_trade_date` in this script returned no matches — confirms no current computation or emit.

### Upstream source data candidates

- `silver/accounts_dim/latest.parquet` has `first_trade_date` per account
- `silver/api_dims/accounts_v2/*` has same
- `INF_D_00d` ALREADY loads accounts_v2 (line 158 `load_accounts_v2()`) — data is in-scope

### Implementation sketch (for Phase 2 if prioritized)

```python
def build_new_clients_accumulation(accounts_v2, hh_dim, data_as_of):
    """Per-state cumulative new-client count over the date range.

    Group accounts by first_trade_date period (e.g., monthly) + state, then
    cumulative-count per state across the date range. Schema-additive emit
    at cumulative_chart.json top-level under `new_clients` key.
    """
    # group accounts_v2 by first_trade_date.dt.to_period('M') + state
    # accumulate counts per (state, period)
    # emit {state: [{date, cumulative_new_clients}, ...]}
```

**Effort:** ~30-60min implementation + chain-fire to materialize. Schema-additive (no breaking changes). P3 priority + new-feature work; COO decides timing.

## Compiler tools

| Tool | Runs | Findings |
|---|---|---|
| `aws s3 cp ... \| jq` on book.json (Peter Lee) | 4 | Initial probe at wrong paths (top-level `.total_aua` instead of `.book.total_aua`); corrected on second pass |
| `aws s3 cp ... \| jq` on summary.json + composition.json + top_holdings.json (Peter Lee) | 3 | Found sibling artifacts have populated data |
| `aws s3 cp ... \| jq` cross-advisor baseline (Joe + Patrick + Jeremy + Peter) | 4 | Confirmed system-wide pattern |
| `aws s3 cp ... \| jq` cumulative_chart.json | 1 | Confirmed new_clients absent |
| `grep` for writer-script identification | 4 | INF_D_02 + INF_D_04 + INF_D_02b + INF_D_00d roles enumerated |
| `grep` for FE consumer (AdvisorBookView.tsx) | 2 | Required-keys assertion + tax_exposure wiring located |
| `grep` for `mix_snapshot` / `'mix'` in INF_D_02 | 1 | No matches — confirms emit gap |

**No comp-* tool runs** — probe was read-only S3 + grep + jq diagnostic; ds-commit-gate / safe-deploy / safe-commit not applicable to probe-only work.

## MCPs sent

| To | At (Z) | Subject |
|---|---|---|
| 2.0.0_SA_COO | 17:01:09 | RAVC1 ACK — Phase 1.2 probe starting |
| 2.0.0_SA_COO | 17:06:09 | RAVC2 PROBE REPORT — Phase 1.2 P1 + P3 findings |
| 0.4.0_DE_ClientPlatform | 17:06:19 | FYI — book.json mix=null gap + Cost Basis is actually populated (FE-path bug?) |
| 0.4.0_DS_ClientPlatform~A | 17:06:27 | FYI — INF_D_02 emit gap; Option DS-1 fix-shape sketch |

## MCPs received

| From | Subject | Disposition |
|---|---|---|
| 2.0.0_SA_COO (~17:00Z) | P1/P3 PROBE — Phase 1.2 routing | ACKed + executed |

## Decision notes

1. **Initial probe used wrong query paths.** First jq pass queried top-level `.total_aua` / `.tax` / `.performance` on book.json — all returned null. Could have been misread as "Peter Lee data missing entirely." Re-probe with correct paths (`.book.total_aua` / `.tax_exposure.cost_basis_by_year`) revealed data IS present, just at different shape than expected. **Discipline observation:** when probing artifact shape, always start with `jq 'keys'` at each level before assuming field locations. Memory candidate.

2. **Sibling-artifact discovery via S3 directory listing was the unlock.** `aws s3 ls .../peter_lee/` revealed composition.json + top_holdings.json + summary.json as separate files. Without that step, "book.json is missing X" would have been the wrong conclusion. The memory entry on advisor book.json paths flagged this exact pattern.

3. **"Used to work, lately not displaying" framing was misleading.** Suggested a regression. But empirical investigation shows the gap is structural (INF_D_02 has NEVER populated top-level `mix` in book.json per grep). Either:
   - Andrew's "used to work" memory is conflating with a different surface (e.g., a previous version of the FE that read summary.json)
   - The FE was recently updated to read book.json instead of summary.json (regression on FE side, not DS)
   - DS book.json shape was recently slimmed down (less likely; grep would have surfaced removed code)

   FE-side audit by DE 0.4 should resolve this framing question.

4. **Cost Basis NOT a real DS bug.** `tax_exposure.cost_basis_by_year` is populated in book.json. If the panel renders empty, it's FE-side. Routing this finding to DE explicitly in the FYI MCP.

5. **Part B feasibility is high.** All required data (`accounts_v2.first_trade_date` + state mapping) is already loaded by INF_D_00d. Fix-forward is a small additive function. COO can dispatch immediately if Phase 2 prioritizes; effort matches the P3 enhancement framing.

## Next Steps

| Recipient | Item |
|---|---|
| **2.0.0_SA_COO** | Phase 2 dispatch decision: route Part A (Option DS-1 implementation, ~15-30min) + Part B (new_clients additive emit, ~30-60min) to me or DS~A or split. |
| **0.4.0_DE_ClientPlatform** | FE audit of Cost Basis panel — confirm wiring at AdvisorBookView.tsx:570 actually consumes `bookData.tax_exposure.cost_basis_by_year` correctly OR identify a different panel reading a different path. |
| **0.4.0_DS_ClientPlatform~A** | FYI noted; available to take Phase 2 Part A if COO routes (no merge conflict with your INF_D_00c work). |
| **Self — passive** | Standing by /loop watchdog for Phase 2 dispatch decision OR for new TO. |

## Session telemetry

- Wall time: ~7 min RAVC1 ACK → probe report
- 0 commits (probe-only)
- 4 MCPs sent
- 1 MCP received
- ~14 S3+grep diagnostic runs
- 0 compiler-tool runs (probe doesn't trigger them)
- 0 escalations
- 1 self-correction (wrong-path initial probe → correct-path re-probe)
