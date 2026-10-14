# MDPF_CANON task order -- `CN-i-1` -- THE AUA TREND GROUPS ITS CUSTOM MODELS INTO ONE SERIES AND DRAWS THE STRATEGY GROUPS AS CHIPS IN THE TOTAL ASSETS COLOURS (FWD-9; PORTAL DEV CANDIDATE)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-i-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~18</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; one page, one exported palette and one pure module.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS; the page reads series and a category-views object it already fetches.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at the shared tree -- `r7_cn_i_1.py module` reads 0 of 1 (the module is absent) and `page` 2 of 8 at base (P6 and P8 are controls that hold); `data` reads 5 of 5 at base by design (it grades the SERVED inputs the rules stand on, the cent-exact stack and the 21-of-21 carve-out equality, and is the proof the rule is implementable, not a build test); the reference patch reads module 9 of 9 and page 8 of 8; four mutants (a null coalesced to 0; a hex literal beside a group label; the grouping gated on Global; ALT recoloured from Total Assets) turn M2, P5, P4 and P6 red; `selftest` prints OK.
EGRESS CLASS, declared: NONE (the worker reads no AWS and writes none).
</preflight>

**Your worktree:** the spawn names it (outer branch `wk-MDPF_CANON-18`, cut from the issuance commit). The portal is a NESTED repository at
`<worktree>/portal`, provisioned on its own branch `wk-MDPF_CANON-18-portal` cut from portal `DEV` (the issuance names the ref) with `node_modules`
linked. Start every shell call with `cd` into the outer worktree path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base
checkout. The existing files use CRLF line endings: keep them, and confirm with `git -C portal diff --stat` that the diff is about 150 lines.

## 1. THE ACT -- `CN-i-1` (round 7)

THE REQUIREMENT (Andrew, 2026-10-13 ~18:4xZ; PRD v2.15 FWD-9, the CTO's rulings msgs 5071 and 5086-5088). On Model Portfolios > AUA TREND ANALYSIS the trend
lists about 17 series. He wants the custom models as ONE series "Custom Models", and the strategy groups as chips, in the colours the Total Assets card
already uses; the five canonical Opal models stay one series each. Group IN THE COMPONENT through the ONE Total Assets colour export; no back-cast, no
interpolation, no new served key, no served-object change.

THE SERIES SET (Global is the measured scope; the `data` arm proves each rule on the real served objects):
1. The five canonical models: unchanged, one series each.
2. "Custom Models": the per-date sum of every served model line that is not canonical, INCLUDING the fold's pooled `other_models` line, which it REPLACES
   (no "Other Models" series remains). Applies at EVERY scope the page offers (the PRD reads "at Global and at each firm scope").
3. "ETF Strategies" (Global): `sma_additive_aua` (pfde) PLUS the two carve-out SMA lines `opal_div_sma` and `opal_growth_sma`, read from the served
   `by_model` by date. Those two sit INSIDE `non_model_aua`, so they are CARVED OUT of it: drawn once, here, never also in Other AUA.
4. "ALT Strategies" (Global): `tax_additive_aua` ONLY (the `tax` by_model line is the same dollars and is not stacked). Its colour on the Trend STAYS
   `vermilion500` (Andrew-direct 2026-10-01, "we canonically use vermillion for alts"); the pin test stands (section 1d).
5. Non-model AUA (Global):
   - on the one date the page holds a category-views object for (its `as_of`): "Client Supervised" (`Client - Opal Supervised`), "Client Unsupervised"
     (`Client - Opal Unsupervised`) and "Other AUA" = `non_model_aua` minus the two Client chips minus the two carve-outs, drawn only when not zero;
   - on every other date: ONE series "Other AUA" = `non_model_aua` minus the two carve-outs, and the two Client chips draw NOTHING.
   The Client chips are AS-OF ONLY in this cell: they read the page's EXISTING category-views query (`categoryViews`, one fetch, the latest served object).
   The dated history route is its own cell; this cell must not fetch a second object, back-cast or interpolate.
6. The whole stack sums to `opal_aggregate_aua` to the cent (the carve-outs drawn once), EXCEPT on a date FWD-3's fold suppressed the pooled line, where
   it is below the total by exactly that amount and is never drawn.

WHAT THE PAGE DOES TODAY (`portal/src/pages/ModelPortfolios.tsx`, anchors at HEAD; verify each before you edit):
- Global series are built client-side from the served `by_model` at `:782-856` (`nonSmaKeys` = every key whose `cohort_class !== 'sma'`; the SMA-class keys,
  the carve-outs among them, are NOT in that map). Add a small memo beside `globalEnterpriseByPeriod` that reads, per date index, the two carve-out lines
  from `globalMdpfData.by_model.opal_div_sma` / `.opal_growth_sma` `model_value` and exposes them by `period`; do no arithmetic there.
- blends are rolled into their archetypes by `rollBlendsIntoArchetypeSeries` (`:171`, applied in the `timeSeriesData` memo `:854-857`). Leave it alone.
- mount list `STACK_SERIES` (`:146-157`), a closed literal mounted in registration order; extras are appended before `non_model` by `trendStackSeries`
  (`:888-896`). Keys are recharts dataKeys: do not rename existing keys.
- the data-point builds for the period-end bars (`:1862-1915`) and the daily area (`:2060-2110`) fill `dataPoint[nmKey]` from
  `globalEnterpriseByPeriod.get(period)?.nonModelAua` and `dataPoint['sma_additive']` / `['tax_additive']` from `addPt?.smaAdditiveAua` /
  `?.taxAdditiveAua`. `categoryViews` is fetched at `:528-532` (`['mdpf-category-views', effectiveFirmId]`) for the Total Assets card (`:1306`).
- colours: `getModelColor(label)` (`src/lib/modelPortfolioColors.ts`) at the legend (`:1146-1160`), the bars (`:2003`) and the areas (`:2239`). The Total
  Assets card colours by NAME from `L1_COLOR` in `src/components/CategoryViewTree.tsx:87-95` (`Custom` fuchsia500, `ETF Strategies` cyan400,
  `ALT Strategies` green400, the two `Client - Opal ...` keys amber/orange); `L1_COLOR` and `l1ColorOf` (`:96`) are module-private today.

THE EDIT, three files:

### 1a. `portal/src/components/CategoryViewTree.tsx` -- export the palette, change nothing else

`const L1_COLOR` becomes `export const L1_COLOR`, `const l1ColorOf` becomes `export const l1ColorOf`. No logic, no value, no other line moves. The page imports
`l1ColorOf`; it must NOT copy the table.

### 1b. NEW `portal/src/lib/trendGrouping.ts` -- a pure module, imports nothing

```ts
export interface TrendPoint { period: string; aum: number | null; pointClass?: string }
export const CUSTOM_MODELS_LABEL = 'Custom Models'
export function groupCustomModelsSeries(byModel: Record<string, TrendPoint[]>, canonical: ReadonlySet<string>): Record<string, TrendPoint[]>
export function etfStrategiesAua(smaAdditive: number | null, carveOuts: ReadonlyArray<number | null>): number | null
export function otherAua(nonModelAua: number | null, carveOuts: ReadonlyArray<number | null>, clients: ReadonlyArray<number | null> | null): number | null
export function clientChipAt(period: string, asOf: string | null | undefined, value: number | null | undefined): number | null
```

Behaviour, exactly (the issuer's `module` arm exercises each):
- `groupCustomModelsSeries`: keys in `canonical` pass through UNCHANGED (the same array object); every other key is a member; with no members the result is the
  canonical keys only (no group key invented); otherwise ONE key `'Custom Models'` whose points are, per `period` (first-seen order), the sum of the members'
  `aum` rounded to cents, `null` only where EVERY member is null (absent is not zero); `pointClass` is `interpolated_estimate` if any member carries it, else
  the first defined member value. The input is never mutated; the member series do not appear in the result.
- `etfStrategiesAua`: the cents-rounded sum of the non-null arguments (`smaAdditive` and the carve-outs); `null` only when all of them are null.
- `otherAua`: `null` when `nonModelAua` is null; else `nonModelAua` minus the sum of the non-null carve-outs minus (when `clients` is not null) the sum of the
  non-null client values, rounded to cents; a result whose absolute value is under 0.005 is returned as `null` (nothing to draw, and never `-0`); a real
  negative result is returned as is (it is a finding, never hidden).
- `clientChipAt`: `value` only when `asOf` is set and equals `period`, else `null`; a measured `0` stays `0`.
Comment the module with the FWD-9 reference and the field-read law (it sums served series and never composes an artifact total).

### 1c. `portal/src/pages/ModelPortfolios.tsx`

1. Imports: add `l1ColorOf` to the `CategoryViewTree` import and `import { groupCustomModelsSeries, etfStrategiesAua, otherAua, clientChipAt } from '@/lib/trendGrouping'`.
2. Above `keyForModel` (`:136`): `const TREND_GROUP_L1: Record<string, string> = { 'Custom Models': 'Custom', 'ETF Strategies': 'ETF Strategies',
   'Client Supervised': 'Client - Opal Supervised', 'Client Unsupervised': 'Client - Opal Unsupervised' }` (NO ALT entry),
   `const trendColorOf = (label: string): string | undefined => (label in TREND_GROUP_L1 ? l1ColorOf(TREND_GROUP_L1[label]) : undefined)` and
   `const ALT_TREND_COLOR = getModelColor('Tax-Managed SMA')?.primary ?? PALETTE.gray300` with a comment citing Andrew's 2026-10-01 word and the pin test.
   These are the ONLY colour lines for the six labels: no hex literal and no `PALETTE.fuchsia/cyan/amber/orange` pick beside any of them.
3. `STACK_SERIES`: keep every existing entry; insert `{ key: 'custom_models', label: 'Custom Models' }` and the two Client entries
   (`client_supervised` / `Client Supervised`, `client_unsupervised` / `Client Unsupervised`) immediately BEFORE the `non_model` entry; relabel
   `non_model` to `'Other AUA'`, `sma_additive` to `'ETF Strategies'`, `tax_additive` to `'ALT Strategies'`. Add the three new labels to `MODEL_KEY`
   so `keyForModel` resolves them to those keys.
4. The `timeSeriesData` memo (`:854-857`): after the blend roll, pass the rolled `by_model` through
   `groupCustomModelsSeries(rolled, new Set(['Ultra-Short Term','Short Term','Intermediate Term','Long Term','Ultra-Long Term']))` at EVERY scope (no
   `effectiveFirmId` gate).
5. Both data-point builds (period-end bars and daily area), Global branch only: `dataPoint['sma_additive'] = etfStrategiesAua(addPt?.smaAdditiveAua ?? null, [divSma, growthSma])`;
   the two Client keys from `clientChipAt(period, categoryViews?.as_of, categoryViews?.nodes?.Client?.children?.['Client - Opal Supervised']?.aum)` and the
   Unsupervised twin; `dataPoint[nmKey] = otherAua(nonModelAua, [divSma, growthSma], [clientSup, clientUnsup])` when a Client chip is present on that period,
   else `otherAua(nonModelAua, [divSma, growthSma], null)`. The per-firm branches keep their existing `nonModel` value path unchanged (they carry no carve-out
   arithmetic and no Client chips: not measured, section 2 bound 7). `dataPoint['tax_additive']` is unchanged (the `tax_additive_aua` field read).
6. Colours: the legend model entries, the two band legend entries and the three new chips use `trendColorOf(label)`; the ALT band uses `ALT_TREND_COLOR`; the
   bars (`:2003`) and areas (`:2239`) prefer `trendColorOf(s.label)` (and `ALT_TREND_COLOR` for `tax_additive`) over `getModelColor(s.label)?.primary`. Every
   other label keeps `getModelColor`.
7. The absent observable: a Client chip with a `null` value draws no bar or area segment and no tooltip row (read how the tooltip filters nulls and confirm; if
   it prints `$0` for a null, file a row), and a series value that rounds to zero is never printed `-$0`.
8. Leave alone: `rollBlendsIntoArchetypeSeries`, the donut and Total Holdings rollup, the per-firm paths, `src/lib/modelPortfolioColors.ts` and its tests.

### 1d. the existing colour test

`portal/src/pages/ModelPortfolios.taxsma-color.test.ts` pins `getModelColor` for 'Tax-Managed SMA' (vermilion500) and 'ETF Strategies' (#6366f1). Both resolve
through `modelPortfolioColors.ts`, which you do not touch, so the test stays green unchanged. Run it once and say so. DO NOT EDIT IT (the issuer's `page` arm
P6 reads it).

LAWS THAT BIND THIS EDIT. (i) FIELD READ: every group is a per-date sum or difference of SERVED fields through the pure functions, never an artifact total
recomposed. (ii) Absent is not zero: a date with no member value draws no point. (iii) No back-cast, no interpolation, no new key, no served-object change,
no second fetch. (iv) The provenance read guard stays green (`node scripts/provenance-read-guard.mjs` in the portal prints `OK:`). (v) The chips are
as-of only until the history route cell lands: the label states nothing about dates the page does not hold.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ`. Row id form `MDPF_CANON-D1-W18-S<k>`, `disarm_owner` `2.0.0_SA_COO~D1`. If a series' resolved
colour equals another series' colour, file an OBSERVATION row naming both hex values: do not edit the colour registry.

## 2. BOUNDS

1. Portal repository only, on branch `wk-MDPF_CANON-18-portal`; never push; never touch `DEV` or `PROD`; no merge.
2. Edit only the files in section 3 (plus your deliverables and the surprise channel). No token change, no new dependency, no new component.
3. No AWS call of any kind, no deploy, no store write. No `bun install` (the modules are linked). No browser launch.
4. **CLIENT DATA:** never print a client figure or an account id in your report, a row or a file; tests use synthetic numbers.
5. No non-ASCII character in any line you add. Use the Edit tool; keep CRLF in the two existing files.
6. If an item cannot be met inside your paths, file a row and stop on that criterion: the issuer rules it.
7. Scope of the measured rules: ETF, ALT, Other AUA and the Client chips are Global-only in this cell; every firm scope keeps its existing non-model band
   value path and gets only the Custom Models grouping and the relabelled band names.

## 3. SURFACES

<paths>
portal/src/components/CategoryViewTree.tsx
portal/src/lib/trendGrouping.ts
portal/src/pages/ModelPortfolios.tsx
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-i-1.aua-trend-grouping.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~18/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `portal/CLAUDE.md`, `portal/DESIGN.md`, `portal/src/lib/modelPortfolioColors.ts`,
`portal/src/pages/ModelPortfolios.taxsma-color.test.ts` and the issuer's check
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_i_1.py` (never edit it; read its subcommands to see exactly what each
arm asserts).

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-i-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_i_1.py" module; echo "exit=$?"</invocation><expect>ROUND 7 GROUP-MODULE: 9 of 9 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-i-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_i_1.py" page; echo "exit=$?"</invocation><expect>ROUND 7 GROUP-PAGE: 8 of 8 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-i-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_i_1.py" data; echo "exit=$?"</invocation><expect>ROUND 7 GROUP-DATA: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="CN-i-1" judgment="true"/>
</proof_of_spec>

AC3 reads the SERVED inputs (read-only AWS gets); it must still read 5 of 5 after your edit, and prints the per-arm denominators in the proof.

AC4 is JUDGMENT, graded at the round-7 close (never self-graded): the issuer renders the Global AUA Trend on `bun run dev:live --port 5174` at a STATED portal
commit (`/frontend-dev`, `scripts/ui-smoke.mjs`) and the CVO reads it against PRD FWD-9 (3) and (4) and `DESIGN.md`: the five canonical series unchanged; ONE
"Custom Models" series in the Total Assets Custom colour and no "Other Models"; "ETF Strategies" and "ALT Strategies" named, ETF in the Total Assets colour and
ALT in vermilion500; on the as-of date (date A) the Client chips and a true-remainder "Other AUA"; on dates C and D no Client segment, no Client tooltip row, and
one "Other AUA"; no "-$0"; the stack adds to the Total on a sampled date. Date B (2026-08-27) is NOT drawable by this cell: it needs the history route
cell, so FWD-9's grade waits for it. You do not render.

## 5. WHEN YOU ARE DONE

1. Commit the three portal files INSIDE the nested repo: `git -C "<worktree>/portal" add -- src/components/CategoryViewTree.tsx src/lib/trendGrouping.ts
   src/pages/ModelPortfolios.tsx` then `git -C "<worktree>/portal" commit --author "0.9.0_WK_MDPF_CANON~18 <0.9.0_WK_MDPF_CANON~18@opal.agent>" -F <msgfile>`
   (message file written with the Write tool). If a portal hook refuses, file a row with its text and stop: do not bypass it.
2. Write the proof instance at
   `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~18/MDPF_CANON.TO-CN-i-1.aua-trend-grouping.proof_of_spec.json`, AC4
   UNVERIFIABLE-BY-INSTRUMENT with status_reason "graded at the round-7 close". **Flip this order's `<status>` to `complete` in the SAME commit as the
   instance**, and only when AC1, AC2 and AC3 all pass.
3. Commit the OUTER files via `.tools/safe-commit.sh --author "0.9.0_WK_MDPF_CANON~18 <0.9.0_WK_MDPF_CANON~18@opal.agent>" -F <msgfile> -- <paths>` (outer
   paths only; do not stage `portal`). Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.

Report once: the portal branch and commit hash, the diff (one line per file), the output line of AC1-AC3, the outer commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 7, from the CTO's round-6 analysis (FWD-9 enters beside CN-h-1; rulings msgs 5071, 5086-5088; PRD v2.13 @fed23ff9ff, v2.15
@567018c9e5). Design: `round7/FWD9_GROUPING_READ.md` @1c9f519b6f. DRAIN CHECKS (the issuer's, not criteria): `bun run typecheck` and
`node scripts/provenance-read-guard.mjs` in the portal worktree, once, after the commit; the `ui-smoke` render for AC4. A portal candidate touching product
files comes to `1.0.0_SA_CTO~DELL1` for review BEFORE any DEV landing, with the render beside it; the PROD push of Model Portfolios is client-facing and is
Andrew's card with the before/after, beside the FWD-3 `/portfolios` card, which carries "Client chips: 21 of 495 dates, from 2026-08-27" and the Other AUA
remainder at the frontier. The `--portal-ref` the issuance names is portal `DEV` HEAD at the cut (the `fanout:` line carries `portal_ref:`).

**RISK CLASS:** `LOCAL` for this cell (portal/src is the LOCAL floor, GATE xii). LANDING (CLAUDE.md Portal, fcdfc34843, 2026-10-14): DEV is written only by `.tools/portal-merge-forward.sh cand/<box>/<slug>` on an approved row, never by this order; a client-facing candidate's approver is Andrew, an Opal-internal one's the building box's CTO; PROD only by a chosen-set promote.
`worker` (not light): about 150 product lines over three files (one new, about 70), several anchors, two data-point sites and a colour contract.

**WHAT CHANGED SINCE THE FIRST DRAFT (the CTO's rulings, measured):** Fork 2 ruled on the issuer's REC: ETF = pfde + carve-outs, Other AUA the true remainder,
the stack sums to the Total (reverses v2.14 (a)). Fork 1: the dated-history route is its own cell and pair; the chips ship as-of first and the grade waits.
Fork 3: ALT stays vermilion500 (Andrew 2026-10-01), the pin test stands; the first draft's recolour is removed.

**FOR THE ISSUER (measured, not decided here):**
1. **The cent-exact sum on a DATED Client chip holds against the SAME-DATE ts object, not the newest one.** Measured: the Client gap
   (`non_model_aua` - Supervised - Unsupervised) equals `opal_div_sma + opal_growth_sma` on 21 of 21 dated category-views objects to the cent when each is
   compared with the time series OF ITS OWN DATE, and on 3 of 21 when compared with the newest ts object (a newer object restates its history: against the newest ts the
   residual (gap minus carve-outs) is 190.77 on 2026-10-09 and 301,207.84 on 2026-10-05, and is exactly 0 on 3 dates). Once the history route serves dated chips, the
   page draws them beside the CURRENT ts history, so FWD-9 (2)'s "equals the sum of its served members to the cent" cannot hold on a historical dated chip
   unless the route also serves that date's `non_model_aua` or the sum arm is stated against the same-date object. The route cell's pair must say which.
2. **Firm scopes are unmeasured.** FWD-9's exercised read names "each firm scope the page offers", but ETF, ALT, the carve-outs and the Client gap were measured
   only at Global (the per-firm non-model band is `non_model_aua + sma_aua` from a different path). This cell groups Custom Models at every scope and
   relabels the bands; it leaves the per-firm non-model values alone. The exercised read at firm scopes will show a relabelled single band.
3. **The label 'Other AUA' replaces 'Non-Model' at every scope** (one `STACK_SERIES` entry). PRD names it at Global only; a per-scope label would need a
   conditional label. Raise it if Andrew's card should keep 'Non-Model' at firm scopes.
4. **`getModelColor('ETF Strategies')` is #6366f1 (indigo), pinned by the test, while Total Assets colours ETF cyan400.** The page's series colours come from
   `trendColorOf`, so the Trend takes cyan400; the indigo remains wherever else the page calls `getModelColor('ETF Strategies')` (tooltip row swatches may):
   the worker checks every call site and files a row for any that remain.
5. **The fold's suppressed dates:** Custom Models has gaps wherever `other_models` is suppressed (2026-05-15 .. 2026-09-09) and before 2026-05-15, by accepted
   ruling; FWD-9 (2)'s exception reads the fold's own record, which a component cannot read: it draws what is served and the issuer's `r6_fold_readback.py` R5
   carries the suppressed amount.
6. **The history route (fork 1) is a separate cell and pair**, read-only over `opal-data-assets/portal/gold/mdpf/global/category-views/`; not drafted here.

**Fanout:** 1 of 1 chains, cap 8 beside CN-h-1 (no shared file: CN-h-1 owns `dim_mdpf_aggregate_aua_timeseries.py` and tests, this owns portal files); 2 of 2
independent chains if both are issued in one round. `portal_ref:` the portal `DEV` HEAD at the cut.

<status>pending</status>
<round>7</round>
<to_id>MDPF_CANON.TO-CN-i-1</to_id>
<slot>~18</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
