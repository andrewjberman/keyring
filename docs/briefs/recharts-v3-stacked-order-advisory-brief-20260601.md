# Advisory brief: forcing stacked-series order in recharts v3 (stack ignores my order for sparse/late series)

## TL;DR
In a **recharts v3.7.0** stacked `BarChart` and stacked `AreaChart`, I cannot get the stacked series to render in a fixed, explicit order. I provide the series in the exact order I want (verified — the chart's own legend, which maps the same array, renders correctly), but recharts places two **newly-added series whose underlying data is `null` until very recently** at the *end* of the stack group instead of in their intended interleaved ("sandwiched") positions. I need to force the stack order deterministically regardless of the data sparsity.

## Goal (the exact desired stack order, bottom → top)
A per-firm "AUA Trend Analysis" view with these stacked series:
```
Ultra-Short Term
Short Term
50/50 ST/INT        <- blend, must sit between Short Term and Intermediate Term
Intermediate Term
50/50 INT/LT        <- blend, must sit between Intermediate Term and Long Term
Long Term
Ultra-Long Term
Non-Model           <- must always be the topmost band
```
The two `50/50 *` series are blended model portfolios that must be "sandwiched" between the two models they're composed of. Non-Model must always be last (top).

## Stack: tech + data
- **recharts**: `^3.7.0`. React 18, TypeScript, Vite.
- Two charts, both stacked: a `BarChart` (`stackId="aum"`) and an `AreaChart` (`stackId="models"`). Same problem in both.
- **Data shape** (per-firm, e.g. one firm has 7 model series + Non-Model). Each model series is a per-date array of length 401 (dates 2024-11-01 … 2026-05-29):
  - **All 7 model series** (the 5 base models AND the 2 blends) are `null` for the first **391** entries and have real numbers only from index 391 (2026-05-18) onward — i.e. per-model tracking only began 5/18.
  - **Non-Model** has real (non-null) values across **all 401** dates.
- The chart-data builder converts each model value with `value ?? 0`, so the series fed to recharts contain **`0` for the leading 391 points** and real numbers after. Non-Model is real throughout. (So from recharts' perspective the model series are `0`-then-value; they are not `null` in the chart data.)

## What renders CORRECTLY (same order source)
- A **Pie/donut** of the same models renders slices in the exact desired sandwiched order (Pie honors the explicit array order I pass).
- A **custom `<Legend content={...}>`** maps over the same `trendModelOrder` array and renders the sandwiched order correctly.

So the order array itself is correct; the divergence is only in the **stacked** Bar/Area.

## What recharts renders (WRONG)
Stacked order (bottom → top), identical in both Bar and Area:
```
Ultra-Short Term, Short Term, Intermediate Term, Long Term, Ultra-Long Term,
50/50 ST/INT, 50/50 INT/LT,        <- both blends shoved to the END of the model group
Non-Model
```
The two blend series are moved to the end of the model block (after Ultra-Long Term), NOT sandwiched. (In an earlier variant they were even placed *after* Non-Model.) Non-Model itself sits where I want (top).

Crucially: the base models have the **same** `null`-until-5/18 → `0`-then-value data pattern as the blends, yet the base models keep their positions and only the **blends** get relocated.

## Relevant code (simplified, accurate)

Order array (verified to produce the sandwiched order; the legend proves it):
```ts
const MODEL_ORDER = ['Ultra-Short Term','Short Term','Intermediate Term','Long Term','Ultra-Long Term']
const BLEND_AFTER: Record<string,string> = {
  'Short Term': '50/50 ST/INT',
  'Intermediate Term': '50/50 INT/LT',
}
const orderModelsWithBlends = (names: string[]): string[] => {
  const present = new Set(names)
  const ordered: string[] = []
  for (const m of MODEL_ORDER) {
    if (present.has(m)) ordered.push(m)
    const blend = BLEND_AFTER[m]
    if (blend && present.has(blend)) ordered.push(blend)
  }
  for (const n of names) if (!ordered.includes(n)) ordered.push(n)
  return ordered
}
// => ['Ultra-Short Term','Short Term','50/50 ST/INT','Intermediate Term','50/50 INT/LT','Long Term','Ultra-Long Term']
const trendModelOrder = useMemo(() => orderModelsWithBlends(Object.keys(timeSeriesData.by_model)), [timeSeriesData])
```

Bar chart data builder (object key insertion order == trendModelOrder, Non-Model last):
```ts
const chartData = filteredPeriods.map((aggItem) => {
  const dataPoint: Record<string, string|number> = { period: label, fullDate: aggItem.period }
  for (const modelName of trendModelOrder) {
    const md = filteredByModel[modelName]
    const pd = md?.find(x => x.period === aggItem.period)
    dataPoint[modelName] = pd ? (pd.aum) : 0      // always set (0 fallback)
  }
  dataPoint['Non-Model'] = /* per-firm combined or global */ ...
  return dataPoint
})
```

Series rendered from a SINGLE explicitly-ordered children array (this is what finally moved Non-Model to the top — proving recharts honors child order for Non-Model):
```tsx
{[
  ...trendModelOrder,
  ...(isValueMode && hasNonModel ? ['Non-Model'] : []),
].map((modelName) => (
  <Bar key={modelName} dataKey={modelName} stackId="aum" fill={colorFor(modelName)} isAnimationActive />
))}
```
(Area is identical with `<Area stackId="models" .../>`.)

## What I've tried (none fixed the stack)
1. **Made the order array interleave the blends** (sandwich). Legend + donut became correct; the stacked Bar/Area still append the blends at the end of the model group.
2. **Built the AreaChart `combinedData` object keys in `trendModelOrder` order** (so data-object key insertion order == desired order, matching the BarChart). No change to the stack.
3. **Collapsed "map(models) + a separate conditional `<Non-Model>` sibling" into ONE ordered children array** `[...trendModelOrder, 'Non-Model'].map(...)`. This DID move Non-Model from mid-stack to the top (so recharts clearly respects child order for *that* series) — but the two blend series remain at the end of the model group.
4. Confirmed the blends and base models have **identical** first-non-null index (391 / 2026-05-18), so it isn't a per-series recency difference I can tweak.

## The paradox I can't resolve
- The legend and the stacked series are generated from the **same** `trendModelOrder` array. The legend renders sandwiched. recharts demonstrably honors child order (Non-Model relocated to top when I made it the last child).
- Yet the two blend series — which have the **same** leading-`null`→`0` data pattern as the base models — are the only ones reordered (to the end of the model group). The base models are not reordered.
- So something about recharts v3's stack-order computation is treating these two series differently and overriding my child/data order for them specifically.

## Questions
1. In **recharts v3.x**, what exactly determines the stacking order of `<Bar>`/`<Area>` that share a `stackId`? Strictly the order of child components? Or does it derive/sort the stack keys from the data — e.g. order of dataKey first-appearance, or first non-null / first non-zero value across the dataset?
2. Does recharts v3 place a series whose **leading values are `0` (or `null`)** later in the stack regardless of child order — i.e. does a "late-starting" series get pushed to the end? Does `0` vs `null` vs `undefined` in the leading points change stack-order behavior?
3. If recharts honors child/dataKey order, why would **only** two series (the blends) be relocated while sibling series with an **identical** leading-null/zero pattern keep position? What property could distinguish them (dataKey string containing `/` or `50/50`; being inserted into the data object after others; being passed via a spread in the children array)?
4. Is there a **recharts v3 API to explicitly set stack order** — a `stackOrder` prop, or a way to pass a d3-shape stack `order`/`offset` (like `d3.stack().order(stackOrderNone)` / `stackOrderReverse`)? recharts v3 supports `stackOffset` on the chart; is there an equivalent for order?
5. Would forcing **every** series (including the blends) to an explicit numeric `0` at **every** point (including the 391 leading points) change the stack order? (The BarChart already does this and it did NOT help; the AreaChart builder currently only sets a key when `periodData` exists — does that gap matter even though `periodData` is found for all in-window dates?)
6. Is there a **known recharts v3 issue/regression** where stacked series with sparse/late data get auto-sorted to the end of the stack? Is there a version where child order is strictly honored for stacks?
7. Recommended robust pattern to **guarantee a fixed stack order** in recharts v3 regardless of data sparsity?

## Where I think the fix is (hypotheses)
- **Most likely:** recharts v3 derives stack order from the data — probably by the order each series' dataKey first appears with a **non-null/non-zero** value (or the order keys are encountered while scanning data). Because the blends' underlying `model_value` is `null` for the leading 391 points, recharts treats them as "introduced late" and appends them — even though I map them to `0`. (Why the base models with the same pattern aren't relocated is the part I can't explain — possibly the conversion to `0` isn't uniform, or recharts ties-break by something else.)
- **Candidate fixes to validate:** (a) a recharts v3 `stackOrder`/d3-stack-order escape hatch to force key order; (b) ensure all series are explicit `0` (never null/undefined) at every datapoint so none is "late"; (c) trim the chart window to start at the first date any model has data (5/18) so all model series begin together; (d) confirm whether the `'50/50 …'` dataKey string format triggers special handling; (e) if recharts genuinely won't honor it, restructure to control the stack manually.

## What a good answer gives me
A concrete way to **pin the stacked render order** to my explicit array `[UST, ST, 50/50 ST/INT, INT, 50/50 INT/LT, LT, ULT, Non-Model]` in recharts v3 — ideally a prop/config, otherwise the minimal data/markup change that makes recharts honor it.
