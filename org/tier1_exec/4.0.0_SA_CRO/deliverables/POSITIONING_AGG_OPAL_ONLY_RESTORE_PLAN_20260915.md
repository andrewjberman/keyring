# Positioning "AGG" view — restoring it as an Opal-only view: findings and draft plan

**Author:** 4.0.0_SA_CRO (Chief Research Officer) · **Home:** org/tier1_exec/4.0.0_SA_CRO/
**Date:** 2026-09-15 · **Status:** DRAFT PLAN for Andrew's decision. Not a task order and not a brief.
**Asked by Andrew, 2026-09-15:** find the old AGG implementation on Positioning, check whether the wiring still
exists, and draft how to bring it back as an Opal-only view on the Portfolio Composition and Holdings Breakdown
panels.

---

## The answer first

- **It is almost all still there.** The view was removed from the portal only, in portal commit `d53049a0`
  (2026-08-24, on DEV and PROD). The data was deliberately left alone. Today's served Positioning file still carries
  the `AGG` block: 30 holdings, each with its per-model breakdown, rewritten this morning.
- **What came out was small.** The removal took out:
  - a selector button;
  - a five-column "Model Breakdown" group in the holdings table;
  - the default selection;
  - some client-side code that had already stopped being reachable.
  Both panels you named read the same selected book, so bringing back the selector brings back both.
- **A straight revert would restore a stale number.** AGG's model weights come from a file last written
  **2026-07-23**, so AGG today is today's holdings mixed with July's model AUM. It also still drops the two 50/50
  "Opal Blend" models.
- **The fix exists.** A canonical Opal-wide AUM-by-model file is current (written today) and carries all seven
  models.
- **Recommendation:** restore the UI for Opal users only, and in the same change re-point the weights to that
  current file. A third, optional step would also stop sending the AGG data to clients. Details and decisions
  below.

---

## 1. What the old implementation was (from the removal commit `d53049a0`)

Why it came out, in Andrew's words on 2026-08-24: *"pulling 'Agg' toggle view from those three pages ... nobody
cares about this view and its more trouble than its worth."* The record is
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260824_PULL_AGG_VIEW_THREE_PAGES_AND_TOGGLE_PERSISTENCE_PATTERN.md`.
The measured reason: it weighted each model by Opal's firm-wide AUM, pooled across 49 Financial, Inflection and
Cottonwood, with no advisor dimension. That put Long-Term at 49.15% of every AGG weight, on a page advisors read as
their own positioning.

On the Positioning page, the removal took out these pieces. The first two live in
`portal/src/pages/Positioning/tabs/HoldingsTab.tsx`, and all line numbers are from the diff.
- **The selector entry.** `AGG_PORTFOLIO = { id: 'AGG', name: 'Aggregate', color: PALETTE.opalIndigo }`, placed
  first in the book selector whenever the mode supported it (`caps.aggregate`).
- **The data path.** In the page's only live period (Current), both the **Portfolio Composition** treemap and the
  **Holdings Breakdown** table rendered `positioningData.current_holdings[selectedPortfolio]`. With AGG selected,
  that is the served `current_holdings.AGG` block. No client-side computation was involved.
- **The Model Breakdown column group.** Five columns, UST / ST / INT / LT / ULT, reading
  `holding.model_breakdown.<code>`, shown only when AGG was selected.
- **The default selection.** The first render landed on `'AGG'`. Removing it exposed a first-render bug that is now
  handled explicitly at `HoldingsTab.tsx` (the FIRST-RENDER LANDING block).
- **Dead code.** A client-side AUM-weighted builder (`aggregateWeighting`), plus a fetch of
  `/api/general/portfolios/aum-metrics.json` whose result was never read. Both sat behind a period that can never
  be selected.
- **The capability flag.** `bookSet.ts` dropped `aggregate` from `BookSetCapabilities` and replaced it with a long
  explanation of why (`bookSet.ts:238-257`).

The same commit also removed AGG from Attribution and Factor Tilts, where it was computed client-side. This plan
does not touch those pages; your request names only the Positioning panels.

## 2. What is still wired today (measured 2026-09-15)

| Piece | State | Evidence |
|---|---|---|
| Served AGG data | **Present and refreshed daily.** `current_holdings` keys are UST, ST, INT, LT, ULT, AGG. AGG has 30 holdings, weights summing to 1.0001, and each holding carries `model_breakdown` | `s3://opal-data-portal-v2/json/positioning/positioning_data.json`, LastModified 2026-09-15 11:06:20 GMT, `generated_at` 2026-09-15T11:06:19Z, `data_as_of` 2026-09-14 |
| Producer | **Still builds AGG.** `load_aum_data` `:1395`, name-to-code map `:1411`, reads `json/portfolios/aum-metrics.json` `:1435`, `calculate_aggregated_holdings` `:1499`, writes `current_holdings['AGG']` `:1785` | `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` at HEAD |
| Portal read seam | `getPositioningData()` already canonicalizes `current_holdings` and each holding's per-model breakdown | `portal/src/api/portal-proxy.ts:1177-1182` |
| Opal-user check | Already on the page: `const internal = isInternal() || isDev()`. It is not passed down to `HoldingsTab` today, which does not use `useAuth` | `portal/src/pages/Positioning/Positioning.tsx:260-267` |
| Panels | "Portfolio Composition" (treemap) and "Holdings Breakdown" are both in `HoldingsTab` and both follow `selectedPortfolio` | `HoldingsTab.tsx:1105`, `:1153`, `:1197` |

## 3. Why a straight revert is not enough

1. **Stale weights.** The producer weights models from `json/portfolios/aum-metrics.json`, which was **last
   written 2026-07-23 20:57:17 GMT**. AGG's `total_aum` is still exactly **$1,637,144,180.01**, the same figure
   measured on 2026-08-24. So every day's AGG uses July's model mix.
2. **Two models dropped.** The producer's name-to-code map covers five models. The two "Opal Blend 5050" models
   carry no code, so they fall out of both the numerator and the denominator. The survivors still sum to 100%, so
   nothing on screen shows the gap. The two blends hold $35.7M and $7.2M today.
3. **Legacy source.** Your 2026-09-09 ruling was that Attribution and Factor Tilts should have no reliance on
   `json/portfolios/`. The AGG producer is the remaining reader of that legacy path. Re-pointing it closes that.
4. **The data reaches clients already.** `positioning_data.json` requires a signed-in user
   (`portal-proxy.ts:1129-1131`), but every signed-in user, clients included, receives the same file. That file
   includes the AGG block, which is Opal's firm-wide model mix and total. A UI gate makes AGG Opal-only **on
   screen**, not in the data. This has been true all along.
5. **The old markup breaks today's colour rules.** The removed columns used dark-theme classes (`text-white`,
   `text-orange-300`, `bg-white/10`, `bg-orange-500/5`). The canvas is now light (`portal/CLAUDE.md`,
   `DESIGN.md` C3/C5), so those classes render near-invisible. The columns need re-authoring in current tokens,
   not a revert.

## 4. The current canonical weight source

`s3://opal-data-portal-v2/platinum/mdpf/global/aum-metrics.json`: LastModified 2026-09-15 13:50:50 GMT,
`period` 2026-09-14, scope Opal-wide. It carries seven models in `by_model`:

| Model (`model_name` as served) | Code | AUM | Accounts |
|---|---|---|---|
| Ultra Short-Term | UST | 65,550,660.50 | 192 |
| Short-Term | ST | 133,205,460.44 | 841 |
| Intermediate | INT | 456,971,348.29 | 2,034 |
| Long-Term Conservative | LT | 883,977,496.68 | 3,476 |
| Long-Term Aggressive | ULT | 209,446,529.75 | 1,431 |
| Opal Blend 5050 Int Ltc | 50/50 INT + LT | 35,744,571.59 | 160 |
| Opal Blend 5050 St Int | 50/50 ST + INT | 7,217,454.65 | 23 |

The model names still use pre-rename labels ("Long-Term Conservative" and "Long-Term Aggressive" for LT and ULT),
so the name-to-code map needs both.

**Reconcile before relying:** the seven `by_model` rows sum to $1,792,113,521.90, but the file's own
`total.model_aum` is $1,800,437,987.06. The gap is $8,324,465.16 and is not explained by anything read here.

**The effect of switching:**

| Weights | UST | ST | INT | LT | ULT |
|---|---|---|---|---|---|
| Served AGG today (July AUM) | 3.20% | 7.89% | 27.14% | 49.15% | 12.62% |
| Canonical file, 5 models, blends excluded | 3.75% | 7.62% | 26.13% | 50.54% | 11.97% |

Folding the blends into their constituents would move INT and LT up slightly further.

## 5. Draft plan

### Phase 1 — Opal-only view in the portal (frontend; can be built behind the freeze)

1. `Positioning.tsx` passes `internal` (already computed at `:267`) into `HoldingsTab`.
2. Models mode gets AGG only when the viewer is internal. Gate it by viewer, the same way `visibleModes` gates
   modes. Do **not** re-add `aggregate` to `capabilitiesFor(mode)`: that function is mode-only, and a mode-level
   flag would show AGG to clients again.
3. Put AGG back first in the book selector, for internal viewers only. Composition and Breakdown then read the
   served `current_holdings.AGG` through the existing path, with no new fetch.
4. Restore the Model Breakdown column group (UST to ULT from `model_breakdown`) using current light-canvas tokens:
   navy ink on the white panel, with no orange-on-dark. Label it as Opal-wide, not advisor exposure.
5. Remembered selection: the stored book is validated against the viewer's own book set. So `'AGG'` is valid only
   for internal viewers, and a client's hand-edited stored value falls back to the default. This mirrors the
   existing `visibleModes` check on remembered mode.
6. Keep the current default landing (the first real model). Making AGG the default for Opal users is decision D4.
7. Update the "no aggregate" explanations in `bookSet.ts:238-257`, `HoldingsTab.tsx:39-48` and the Positioning
   `README.md` to cite the new ruling.
8. Verification (portal verification law):
   - `/frontend-dev` screenshots as an internal viewer (AGG present, labelled) and as a client (no AGG button);
   - a stored-value check with a client viewer;
   - `bun run typecheck`, shown able to fail;
   - lint.

### Phase 2 — current weights at the producer (changes served output: CTO + COO sign-off)

1. Re-point `load_aum_data` from `json/portfolios/aum-metrics.json` to
   `platinum/mdpf/global/aum-metrics.json` `by_model`.
2. Cover both old and new model names, and handle the two blends (decision D2). Reconcile the $8.3M gap first.
3. Add `weights_as_of`, `weights_source` and the per-model weights to the AGG block, so the UI can print the date
   instead of implying freshness.
4. This retires the last reader of the legacy `json/portfolios/aum-metrics.json`.
5. Deploy through the producer's normal Terraform path. Sign-off covers `current_holdings.AGG` only: the five model
   books must be byte-unchanged, checked by comparing before and after.

### Phase 3 (optional) — make the data Opal-only too

Move AGG out of the shared payload into an internal-only file behind a route that refuses client users, following
the existing `/api/general/positioning/model.json` route that blocks the client tier (`portal-proxy.ts:1420-1432`).
Then drop `current_holdings.AGG` from the payload clients receive. This also changes served output and needs
sign-off.

## 6. Decisions for Andrew

| # | Decision | Recommendation |
|---|---|---|
| D1 | Phase 1 alone (showing July weights), or Phases 1 and 2 together | **Together.** Phase 1 alone puts a known-stale mix on screen, and nothing in today's data could label its date. |
| D2 | The two 50/50 blends: fold them 50/50 into their constituent models, or exclude them with a note | **Fold them in.** That makes AGG the whole Opal model book rather than a five-model subset. |
| D3 | Leave AGG in the file every client receives, or move it to an Opal-only file (Phase 3) | **Move it,** since the point is Opal-only. It can follow Phases 1 and 2. |
| D4 | Default book for Opal users: AGG, or the first model as today | Your preference. AGG as the default suits an Opal-first reading of the page. |

**Process.** Canonical flow runs new work through L1 (a CRO brief) and onward. Your 2026-08-24 removal was exempted
("just clean it up"). If you want the same exemption here, say so. Otherwise this seat can turn the plan into the
L1 brief now.

## 7. Not in scope

- Attribution and Factor Tilts AGG.
- The AGG ETF ticker (iShares Core U.S. Aggregate Bond). It shares the string and appears in benchmark
  composition; any change must discriminate per call site.
- The per-advisor aggregate the 2026-08-24 finding said would need an advisor-scoped AUM source. This plan is the
  Opal-wide aggregate, for Opal users.

## 8. Evidence and limits

- Removal diff: `git -C portal show d53049a0 -- src/pages/Positioning` (740 lines, read in full). Ancestry
  confirmed on DEV and on origin/PROD.
- Live reads with the `.tools/aws` shim (`s3api head-object` and `s3 cp`), 2026-09-15 about 13:5xZ:
  - `positioning_data.json`
  - `json/portfolios/aum-metrics.json`
  - `platinum/mdpf/global/aum-metrics.json`
- Source reads at HEAD: `HoldingsTab.tsx`, `Positioning.tsx`, `bookSet.ts`, `portal-proxy.ts`, `aum.ts`, and the
  producer `lambda_function.py`.
- **Not done:**
  - no build, render or deploy;
  - no reading of the deployed producer bytes (source only);
  - the $8.3M gap in the canonical file is unexplained;
  - the served AGG's per-holding values were not re-derived by hand.
