# DS~C 2026-05-12 — Distribution tab gap-closure (RD brief, 6 gaps -> 2 commits)

**Agent:** 0.4.0_DS_ClientPlatform~C
**Window:** ~17:48Z 2026-05-12 → ~18:07Z 2026-05-12 (~20 min)
**Trigger:** RD 0.4.2_RD_AdvisorIntelligence brief committed `b7b15c35` and Andrew-forwarded — Distribution tab gap-closure (Snapshot/Continuous × GEO/ADV × NNA/AUA). Six gaps enumerated.

## TL;DR

Brief enumerated 6 gaps (A-F). Diagnostic on live S3 artifacts showed **4 of 6 were already shipped in earlier waves** (Brief #3 Phase A/B/C + INF_D_00d). Two net-new commits cleared the actual gaps:

- **Phase 1 `97796c0ac`** — `_build_nna_view_period` field-name fix (Gap A). Was emitting `net`/`inflow`/`outflow`; FE reads `value`/`aua`/`period_inflows`/`period_outflows`.
- **Phase 2 `6967d27f7`** — new `build_advisor_nna_clients(...)` Step 9 emit (Gap E). Per-advisor `platinum/advisors/{key}/nna_clients.json`.

Both gates-clean, SHA-MATCH deployed via `safe-deploy.sh` pre-push hook. RAVC2 to RD with diagnostic findings + commit-by-commit detail.

## Brief gap inventory vs actual state

| Gap | Brief described | Live artifact diagnostic | Resolution |
|---|---|---|---|
| A (state NNA/AUA values N/A) | Aggregation broken | Segments populated (15 states, 4 advisors), `value`/`aua` field-name mismatch with FE | **Phase 1 fix** |
| B (cities[] L2 drill unpopulated) | Missing per-state cities | **Already populated**: WA→Everett/Snohomish/Seattle, MT→Missoula/Bonner, CA→Torrance/Encinitas | **No fix needed** (likely cascade from Gap A on FE side) |
| C (cumulative_chart.geo_drill missing) | Per-state city timeseries missing | **Already populated**: 8 states, full city categories, 106 weekly data pts each | **No fix needed** (`INF_D_00d.build_geo_drill_view` already emits) |
| D (4 ADV incl. IWM catchall not surfacing) | Catchall stripped | **Already populated**: all 4 advisors incl. `inflection_wealth_management` present from Brief #3 Phase B/C | Phase 1 lights up value field |
| E (per-advisor `nna_clients.json` missing) | New artifact needed | Path empty for all 4 advisors; 49F has it | **Phase 2 new emit** |
| F (`cumulative_chart.adv` + `nna_adv` missing) | New timeseries blocks | **Already populated**: 4 advisor categories + `_inflow`/`_outflow` per advisor per date | **No fix needed** |

Net new DS work: **Gap A + Gap E only**.

## Per-phase fix detail

### Phase 1 — Gap A NNA donut value-field (`97796c0ac`)

**Root cause:** `_build_nna_view_period` (line 2277) emitted segments with:
```
{key, label, inflow, outflow, net, net_pct, client_count, account_count, color}
```

FE `DistributionTab.tsx:3501`:
```typescript
const seg = cohortView.donut?.segments?.find((s: DonutSegment) => s.key === parentSegmentKey)
return seg?.value ?? seg?.aua ?? 0
```

Both `value` and `aua` absent → nullish-coalesce to 0 → N/A render. **Segments WERE populated; just the field name was wrong.**

49F shape (verified via `s3://opal-data-bd/platinum/firm/partner_analytics_quarterly.json` first segment):
```
{key:'tx', label:'TX', aua:21806530.38, aua_pct:28.5, value:21806530.38,
 client_count:1404, period_inflows:48877535.93, period_outflows:27071005.55, color:'#1E40AF'}
```

**Fix:**
- `_build_nna_view_period` signature extended with `aua_by_group=None` kwarg.
- Segment dict now emits: `aua`, `aua_pct`, `value`, `value_pct` (donut-slice-size fields per 49F) plus `period_inflows`, `period_outflows` (49F flow names) alongside legacy `inflow`/`outflow`/`net`/`net_pct` aliases.
- Sort switches to AUA descending when `aua_by_group` supplied (49F donut convention) vs `|net|` descending fallback.
- `donut.total` switches to sum of segment AUA when `aua_by_group` present.

**Plumbing in caller (line ~2728):**
```python
geo_cur_segs = views_geo.get('current', {}).get('donut', {}).get('segments', []) or []
adv_cur_segs = views_adv.get('current', {}).get('donut', {}).get('segments', []) or []
aua_by_state = {str(s.get('key')): float(s.get('aua') or 0.0) for s in geo_cur_segs}
aua_by_advisor = {str(s.get('key')): float(s.get('aua') or 0.0) for s in adv_cur_segs}
```

Single-sources the AUA computation rather than re-joining holdings inside the NNA helper.

### Phase 2 — Gap E build_advisor_nna_clients (`6967d27f7`)

**Schema (matches 49F `D_04.build_advisor_nna_clients`):**
```json
{
  "generated_at": "...",
  "data_as_of": "...",
  "advisor_id": "peter_lee",
  "total_nna": <float>,
  "client_count": <int>,
  "clients": [
    {"rel_id": "<household_id>", "display_name": "...", "nna": <float>, "pct_of_advisor_nna": <float>},
    ...up to 9...,
    {"rel_id": "other", "display_name": "Other Clients", "nna": <float>, "pct_of_advisor_nna": <float>}
  ]
}
```

**Methodology (INF simplifications vs BD path):**
- Window: current QTD (data_as_of's quarter start → data_as_of).
- Source: `canonical_nna` directly (`.advisor_key` on-source per Brief #3 Phase A finding; no `account_team` join needed for the split).
- `account_id → household_id + household_name` resolution via `household_dim.drop_duplicates('account_id')`. Int64 coerce on both sides defends against the dtype landmine class (chain #14 `b0add04cc`, INF_C_01 `880f6f938`, INF_C_05 `bd488e1b4`).
- Advisor key normalization: null/empty/'unknown'/'Unknown' → `inflection_wealth_management` catchall.
- Per-advisor: `groupby(household_id, household_name).sum(net_nna)`, sort `abs(nna)` desc, top 9 + Other rollup.
- PII: emits cleartext `household_name`; Lambda/FE applies `canSeeCleartext` at API layer (same model as 49F — gold artifact carries cleartext, API pseudonymizes when caller lacks the claim).

**vs BD lift differences:**
- BD reads per-advisor `book.json` + per-client `aua_timeseries.json` (200+ S3 reads). INF computes everything from one canonical_nna DataFrame + existing household_dim load — zero new S3 reads.
- BD computes QTD via `[latest row.nna] - [quarter-start row.nna]` diff-of-snapshots. INF uses `sum(net_nna)` directly since `canonical_nna` IS the per-day delta series.

**IWM catchall inclusion (Andrew explicit directive per brief):**
- Leaderboard convention strips catchall (`ADVI_LEADERBD`).
- For ADV-cohort artifacts (`views.adv` + `nna_clients.json`), catchall STAYS so the 4-advisor view is complete.
- Catchall HH count: 7 of 222 NNA-active (3%), 23 of 818 AUA-tagged (3%). Not dominant; safe to surface.

**Constants added:**
- `_MAX_NNA_CLIENTS = 9` (mirrors BD)
- `_INF_CATCHALL_ADV_KEY = 'inflection_wealth_management'`

Wired into `main()` as Step 9 between `build_clients_tab_slim` and the final log. No dispatch change (INF_D_04 already in `CHAIN_FULL` + `CHAIN_GOLD_D`).

## Files Modified

| File | Change | Commit |
|------|--------|--------|
| `data/orion/scripts/gold/INF_D_04.client_portal_summary.py` | `_build_nna_view_period` field rename + AUA plumbing (Gap A) | `97796c0ac` (+82/-22) |
| `data/orion/scripts/gold/INF_D_04.client_portal_summary.py` | `build_advisor_nna_clients` new Step 9 emit (Gap E) | `6967d27f7` (+169/-0) |

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `ds-commit-gate.sh INF_D_04` | 2× (one per commit) | Both PASS — py_compile + ds-precommit + ruff py39 clean |
| `safe-commit.sh --author 0.4.0_DS_ClientPlatform~C` | 2× | Phase 1 first attempt aborted on staged-index contamination (AE 0.7 session logs); cleaned via `git reset HEAD -- <extras>` and re-ran clean. Phase 2 clean first try. |
| `safe-deploy.sh` pre-push hook | 2× | Both DEPLOYED + SHA-MATCH verified |
| Manual `aws s3 cp` + `hashlib.sha256` SHA verify | 2× | Phase 1 MATCH `18f80aa698c1f537…ab3b`; Phase 2 MATCH `89097f74a9d49c651099…6000` |
| Live S3 diagnostic on `s3://opal-data-inf/platinum/firm/partner_analytics_quarterly.json` | 1× | Confirmed Gap A field-mismatch, Gaps B/C/D/F already populated |
| Live S3 diagnostic on `s3://opal-data-inf/platinum/firm/cumulative_chart.json` | 1× | Confirmed Gap C/F already populated |
| Live S3 diagnostic on `s3://opal-data-bd/platinum/firm/partner_analytics_quarterly.json` | 1× | Confirmed 49F NNA segment shape `{aua, aua_pct, value, period_inflows, period_outflows, client_count, color}` |
| Silver `s3://opal-data-inf/silver/api_dims/household/snapshot_date=2026-04-28/data.parquet` schema check | 1× | Confirmed `household_name` column for cleartext display_name; 852 rows, 12 cols |

No owned-paths blocks. No SHA mismatches. No pre-commit hook bypasses.

## Deploy Evidence

| Step | Phase 1 (`97796c0ac`) | Phase 2 (`6967d27f7`) |
|------|---------------------|---------------------|
| Pre-commit gate | PASS | PASS |
| Author | `0.4.0_DS_ClientPlatform~C` | `0.4.0_DS_ClientPlatform~C` |
| Push range | `b0d650be7..97796c0ac` (carrying a8996b27 RAVC + others) | `c7939d6f6..6967d27f7` |
| S3 upload | `s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py` | same key, second upload |
| S3 SHA-256 vs local | MATCH `18f80aa6…ab3b` | MATCH `89097f74…6000` |
| RAVC2 to RD | Diagnostic + Phase 1 SHIPPED message | Brief CLOSED message with full validation checklist |

## Sequencing handoffs

| Recipient | Item |
|---|---|
| **AE 0.6.1 / AE 0.7** | Next gold-d / full chain picks up both commits. Chain #18 was triggered at 16:47Z with prior bundle; Phase 1 + Phase 2 land at chain #19 or via solo INF_D_04 SSM. No dispatch wire change needed. |
| **DE 0.4.0_DE_ClientPlatform** | Post-chain smoke: confirm FE Snapshot-GEO-NNA + Snapshot-ADV-NNA donut slices light up (N/A → $$); confirm ADV-NNA L1 drill (click advisor → top-9+Other client breakdown) works. |
| **RD 0.4.2_RD_AdvisorIntelligence** | RAVC2 closeout delivered with diagnostic findings; flagged Gap B FE-render-path contingency: if cities still don't surface post-Gap-A-deploy, separate FE bug — RD to file. |
| **DS~C self** | Idle. Standing by for chain redeploy + smoke results. ADVI_ROLLUP.SL-P2 still awaits explicit COO GO. |

## Decision notes (worth keeping)

1. **Diagnose before pipe-change.** RD open Q #1 ("aws s3 cp of the current artifact would resolve whether the data is empty vs broken-FE-read in 30 seconds") was the right instinct. Saved building aggregation infrastructure for paths that were already populated. **Don't trust gap inventories without an S3 diagnostic first.**

2. **49F sample is the contract.** When in doubt about expected field names / shape, dump 49F's analogous artifact (`s3://opal-data-bd/platinum/firm/partner_analytics_quarterly.json`) and mirror byte-for-byte. The brief's text reference can drift from the actual on-disk shape (e.g., brief said `cities` have `value` field; 49F cities only have `aua`/`aua_pct`).

3. **FE source overrides brief.** `DistributionTab.tsx:3501` `seg?.value ?? seg?.aua ?? 0` was the definitive read pattern — knowing that, the Phase 1 fix could have emitted only `aua` (the legacy field) and FE would have rendered correctly. Emitting both `value` + `aua` is defensive (matches 49F exactly + no FE-side dependency on the ?? order).

4. **Field-name drift is invisible until artifact ships.** All 15 state segments + 4 advisor segments were structurally correct from Brief #3 Phase A/B/C — only the donut-slice-size field name diverged from 49F. **The class lesson: always run a 49F vs INF segment-shape diff after any new partner_analytics emit.** Worth adding to comp-validate sentinel pack.

5. **IWM catchall isn't a "behavior switch" — it's a cohort difference.** Brief framed it as "DS needs to make consciously" but the existing `_build_nna_view_period` already emits 4 segments including catchall — the catchall is just a regular advisor_key bucket. Leaderboard exclusion lives at a different artifact (`platinum/firm/architect_leaderboard.json`-equivalent). No catchall-aware branch needed in `nna_clients.json` emit.

## Pacing

20 min concentrated burn. Brief was overstated in inventory size (6 gaps → 2 actual commits) but the diagnostic upfront saved hours of redundant pipeline work. RD-front-loaded "investigate before changing pipelines" guidance was correct and worth amplifying as a memory pattern for future ADVI briefs.
