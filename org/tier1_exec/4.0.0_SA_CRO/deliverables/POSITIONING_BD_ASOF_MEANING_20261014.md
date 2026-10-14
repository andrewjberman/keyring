# What Positioning's Black Diamond date means: the pull day of a model definition, not a market close

**archetype:** TRACE

From `4.0.0_SA_CRO~DELL1` to `1.0.0_SA_CTO~DELL1`, on msg 5693. Read-only, read on 2026-10-14 at ~18:5xZ.
Andrew's report: Positioning cited Black Diamond holdings "as of 5 PM ET, October 14" at 2:37 PM ET on Oct 14 (record
`ANDREW_DIRECT_20261014_183xZ_FIVE_CALLS_ANSWERED_AND_BD_ASOF_CITATION.md`). The 5 PM clock is dell2's fix
(`DataAsOf.tsx` / `dateUtils.create5pmETDate`). This note answers what the DATE is.

## Answer

**The date is the day the Black Diamond rebalancer was read: today in UTC at the producer's run. It is not a market
close.** The rows behind it are **model definitions**, the satellite models' target weights as configured in Black
Diamond's rebalancer. They are not account positions, so no market close applies to them at all.

The date that belongs to the content is **`hierarchy.updatedAt`** in each pulled model-detail object: the time the
model was last changed in Black Diamond. The serving chain drops it today.

## The chain, cited

1. **Page** (portal `origin/DEV` 97c66c93): `src/pages/Positioning/panels/PositioningSummary.tsx:1605-1606`, the
   Satellites footer, prints `Source: Black Diamond, holdings as of ${... positioningData.data_as_of}`. The per-book cell
   (`:1506`) reads `portfolios[code].as_of_date`. `HoldingsTab.tsx` carries no date of its own (0 matches for
   as_of / DataAsOf).
2. **Adapter:** `src/pages/Positioning/shared/satelliteAdapter.ts:321` (`holdingsAsOf = served.holdings_as_of`), `:440`
   (`as_of_date: served.holdings_as_of`) and `:476-477` (`data_as_of` and `data_date` = `holdingsAsOf`).
3. **Read seam:** `src/api/endpoints/satelliteRegistry.ts:295`, `holdings_as_of: holdings.as_of`, the top-level `as_of`
   of `s3://opal-data-cot/platinum/satellites/holdings.json`.
4. **Producer (the line that sets it):** `data/assets/scripts/gold/build_satellites_registry.py:588-612`
   `resolve_as_of()`. Its docstring says "The partition date. DEFAULTS to today-UTC", and the body returns
   `now.date().isoformat()`, with `now = datetime.datetime.now(datetime.timezone.utc)`.
   - The docstring records the choice: "as_of is SAME-DAY, not T-1".
   - `build_holdings_payload()` (`:505-519`) writes `"as_of": str(as_of)` and
     `"source": DETAIL_KEY % (as_of, "{model_id}")`.
   - `DETAIL_KEY` (`:122`) is `blackdiamond/cottonwood/bronze/rebalancer_model_detail/%s/%s.json` in `opal-data-assets`.
     So `as_of` names the **partition of the pull**.
5. **What the pulled object is:** `rebalancer_model_detail/2026-10-14/<model_id>.json`, 95 objects. Each is a
   rebalancer model with a target `hierarchy`. Its date fields: `hierarchy.updatedAt` (sample 2026-07-29T13:26:15Z),
   `hierarchy.children[].updatedAt` (sample 2026-06-15T17:54:09Z), `updatedBy` (a Cottonwood user). None is a price or
   close date.

## One served object, date beside pull time

| Object | Date it carries | Pull / write time (UTC) |
|---|---|---|
| `opal-data-assets/.../rebalancer_models/2026-10-14/page_000.json` (roster) | partition 2026-10-14 | LastModified 2026-10-14 11:32:13 |
| `.../rebalancer_model_detail/2026-10-14/*.json` (95 objects) | partition 2026-10-14; content `updatedAt` 2026-07-29 (sample) | LastModified 11:32:15 to 11:32:30 |
| `opal-data-cot/platinum/satellites/holdings.json` | `as_of` **2026-10-14** | LastModified **2026-10-14 13:15:49** |
| Page footer, rendered | "holdings as of 5 PM ET, October 14" | seen 18:37Z (2:37 PM ET) |

The page's "October 14" is the pull day; its "5 PM ET" is the shared 5 PM clock (dell2). The data was read at 07:32 ET
and published at 09:15 ET. It says nothing about any close.

## What the label should say (proposal for the owner; not done here)

- Honest as served today: "Source: Black Diamond rebalancer model definitions, read Oct 14".
- With the content's own date: carry `hierarchy.updatedAt` per model through `build_holdings_payload` (for example
  `model_updated_at` per satellite), and print "model last changed <date>".
- A "holdings as of <close>" wording is not available for these rows. They are targets, and Black Diamond's rebalancer
  gives them no close.

## Side readings (not asked; recorded so they are not lost)

- The pull landed at 11:32:13Z. The live rule `cot-rebalancer-runner-daily` reads cron(45 12 * * ? *) UTC, and the
  producer docstring quotes cron(0 6 * * ? *). Neither matches 11:32Z, so which trigger wrote today's partition was not
  read. Three clocks for one pull: a row for the rebalancer runner's owner.
- The characteristics producer stamps BBG and positioning inputs at T-1 (2026-10-13), beside a same-day holdings date
  (2026-10-14). The factsheet already prints both clocks through J359; this note does not change that.

## Not read

- Which scheduler fired the 11:32Z rebalancer pull.
- `DataAsOf.tsx` (dell2's).
- Any Black Diamond account-position date. Positioning's satellite rows do not come from positions.
