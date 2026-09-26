# COT gold: admitting `other` -- the consumer census (CTO order 101022, step 1)

`2.0.0_SA_COO~M`, 2026-09-25 ~20:1xZ. Order: 1.0.0_SA_CTO msg 101022. ~M owns it: census first, then the code, then
one never-widen half. The census was a read-only sweep of the repo and portal DEV (Explore agent). Every row below is
path:line evidence.

## What the three scripts write

- **C_06** `data/cot/scripts/gold/C_06.client_mix_timeseries.py` writes:
  - `gold/entities/clients/{rel_id}.json`, with `mix[]` `{date, equity, fixed_income, alternatives, total_mv}` keyed by
    MIX_ASSET_CLASSES (:169);
  - `{rel_id}_views.json`;
  - `gold/views/mix_daily_summary.json`, which feeds D_03.
  - Today an unclassified security falls back to `equity` (:182), and a real `other` would be DROPPED from `mix`.
- **D_03** `D_03.composition_artifacts.py` writes firm, advisor and client `composition.json`
  (`mix[]:{asset_class,label,...}`, root `other{}` and `unclassified{}`) and the mix views.
  - `classify_series` (:117-137) returns `'other'` for any unknown, non-cash security.
  - `_ASSET_CLASS_LABELS` already has `'other':'Other'`.
- **D_04** `D_04.client_portal_summary.py` writes the platinum firm, advisor and client summaries.
  - Its own classify copies (:1344, :2912/2971) return `'other'` for unknowns.

## Consumers (verdict for a new `other` class value / mix key)

| Consumer | Verdict | Evidence |
|---|---|---|
| `data/cot/scripts/gold/lib/mix_views.py:19,84` | tolerated (own 3-class list; skips `other`) | `MIX_ASSET_CLASSES = [...]` |
| `D_04.client_portal_summary.py:525` | tolerated | `for ac in ('equity','fixed_income','alternatives','cash')` |
| `D_04.client_portal_summary.py:568` | tolerated | `# asset classes not in C_06 (e.g. 'other') are excluded` |
| `D_04.client_portal_summary.py:1261-1271` | tolerated (verbatim passthrough) | `mix_list = data.get('mix', [])` |
| `portal/.../AdvisorIntelligence/_shared/types.ts:1561-1569` | tolerated (type unused) | `MixTimeseriesPoint` |
| `portal/.../_shared/lib/composition.ts:32,100` | **tolerated by FILTERING** (every donut) | `if (!classes.includes(item.asset_class)) continue` |
| `portal/.../_shared/lib/composition.ts:54-60,168-175` | rendered, then filtered by the row above | `other: 'Other'` in PLATINUM_LABEL_MAP |
| `portal/.../_partners/cottonwood/layout.ts:113` | **tolerated by FILTERING** (firm/advisor bars) | `ordered: ['fixed_income','equity','alternatives']` |
| `portal/.../PartnerAnalytics.tsx:556-561` | tolerated (fixed keys) | `fixed_income: pt.fixed_income?.value ?? 0` |
| `portal/.../ConsolidatedOverviewPanel.tsx:68-72` | rendered if reachable | generic accessor |
| `portal/src/lib/chartColors.ts:449-464` | colour already exists | `other: PALETTE.gray500` |
| `opal-partners-data/lambda_function.py:1439-1555` | tolerated (pure S3 proxy) | `serve_s3_json(...)` |
| `opal-partners-data/lambda_function.py:1015-1022,1270-1279` | rendered (own `'other'` label) | local `_ASSET_CLASS_LABELS` |
| `validate_platinum_consistency.py:596-630` | tolerated (reads `date` only) | `ts.get('mix', ...)` |
| `runners_cot/d08_cot_mix_summary.py:51-54` | breaks, but reads its OWN classifier and not these artifacts | `CLASS-DOMAIN FAIL` |

Counts:
- 10 tolerated;
- 4 rendered: 2 behind the filters, 2 with their own label;
- 1 breaking, and it is not a reader of these artifacts.
No schema or validator in the served path changes, and no portal test pins the mix key set.

## What this means for the served move

1. **C_06 admits `other`** (MIX_ASSET_CLASSES += `other`). The published `mix` then carries the `other` fraction and
   stops dropping it. The Advisor Intelligence views, however, FILTER to three classes (`composition.ts:32,100`;
   `cottonwood/layout.ts:113`), so `other` stays invisible on screen. For an affected client, what CHANGES on screen
   after batch B is that the $48.5M leaves the `equity` slice, where C_06's fallback puts it today.
2. **D_03/D_04 sentinel:** their unknown value `'other'` is already labelled "Other" and is already filtered from every
   donut and bar. It becomes `'unclassified'`, which matches the root `unclassified{}` field's meaning (D_03:447-465),
   so a real `other` (held-away, personal) is no longer merged with "unknown". The concentration residual `other{}`
   ("beyond the top N") is a different key and is untouched.
3. **To RENDER `other` on the COT portal,** two files outside ~D's IR order change: `composition.ts` CANONICAL_CLASSES
   and `cottonwood/layout.ts` ordered. The label and colour already exist. Owner: the Advisor Intelligence portal
   lane. This is a question for the half, not a prerequisite of it: without it, `other` is correct in the data and
   hidden on screen.

## Pre-existing, found on the way (not caused by this change)

C_06's MIX_ASSET_CLASSES also lacks `cash`. The table has `cash` items, so cash money already drops out of the
published `mix` today, and the fractions sum below 1 for clients holding table-`cash` securities. This is noted for
the half; it is not fixed here.
