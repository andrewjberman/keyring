# MDPF_CANON task order -- `CN-p-2` -- THE GLOBAL AUA TREND OVER FULL HISTORY, VARIANT 1 FOR AN INTERNAL SESSION, VARIANT 2 FOR EVERY OTHER (FWD-9; PORTAL CANDIDATE, CLIENT-FACING AT THE LANDING)


<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-p-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~27</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; three portal source files.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS contact at all (the checks run `bun` on a pure module and read source text).
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 -- at the base `oracle` reads 1 of 7 (C1, a control), `variants` 0 of 10, `wiring` 2 of 9 (C2 and W8, controls); a scratch reference reads 26 of 26 and eighteen planted mutants each turn their named arm red; the selftest prints OK.
EGRESS CLASS, declared: none.
</preflight>

**Your worktree:** the spawn names it (outer branch `wk-MDPF_CANON-27`, cut from the issuance commit). The portal is a NESTED repository at `<worktree>/portal`, provisioned on its own branch `wk-MDPF_CANON-27-portal` cut from `scratch/canon-i3-base` (`f8c7d310`: current portal PROD `5ab67a65` plus the three feature commits CN-i-1, CN-l-2, CN-i-2: the lime Client Unsupervised, the Other Models "as of", the 49 Financial view, and the grouped Trend this order replaces at Global). `node_modules` is linked. Start every shell call with `cd` into the outer worktree path.
**Line endings: `src/pages/ModelPortfolios.tsx`, `src/lib/trendGrouping.ts` and `src/api/portal-proxy.ts` are CRLF in EVERY line. Keep it.** A multi-line text you insert must end each line with CRLF (after your edits run `git -C "<worktree>/portal" diff --stat` and check that no line is LF-only; the check W8 refuses a mixed file).

## 0. AMENDMENT 1 -- READ THIS FIRST (you inherit built work)

Your first pass is committed on the branches you were seated on: portal `wk-MDPF_CANON-27-portal` @0d83ee04 and outer `wk-MDPF_CANON-27` (the merged trunk is in it). Items 1 to 12 below are BUILT and stay as they are: do not redo them, do not re-run an edit that already stands. ONE thing changes, from your own row MDPF_CANON-D1-W27-S2: the composition footnote of item 11 is unscoped, so it also renders on an internal session's per-firm views (49 Financial, Inflection, Cottonwood), where its text about Inflection and Cottonwood is wrong. Item 13 is the repair. Then re-run AC1 to AC3 (they must still read 7, 10 and 9 of their arms), commit inside the nested portal repo (a second portal commit on top of 0d83ee04), rewrite the proof instance over the first one and flip this order's `<status>` to `complete` in the SAME outer commit.

## 1. THE ACT -- `CN-p-2`

THE REQUIREMENT (Andrew-direct, ~20:4xZ and ~20:5xZ today; PRD v2.19 to v2.21; the CRO's spec amendment 1). The Global AUA Trend draws the WHOLE history, 2024-11-01 to the as-of, with every group a served field or ONE served difference. Read these, in this order, before you edit: the pure reference module `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/ref/cn_p_2_helpers.ts` (the whole of the module logic; read-only), then the issuer's check `.../round9/checks/r9_cn_p_2.py` (read-only; what each arm asserts), then the spec table at `org/tier1_exec/4.0.0_SA_CRO/deliverables/MDPF_CANON_GLOBAL_AUA_TREND_FULL_HISTORY_SPEC_20261014.md` (the rule table with the amendment 1 rows, and the amended period-end oracle).

A. THE PURE MODULE (`src/lib/trendGrouping.ts`). Append the contents of `cn_p_2_helpers.ts` after the existing code, converting every line to CRLF. You may copy it verbatim; it uses `toCents`, `sumPresent`, `trendDetailNote` and `CUSTOM_MODELS_LABEL` that the file already holds. Do not edit or remove an existing export. It must keep importing nothing. The exported interface (the checks call exactly these):
`GLOBAL_PRIMARY_LABELS`, `MODELS_BAND_LABEL` ('Models'), `SUPPRESSED_FOOTNOTE`, `CARRIED_LEGEND_LABEL`, `type TrendMode = 'variant1' | 'variant2'`, `trendModeFor(internal: boolean): TrendMode`, `buildGlobalTrendRows(served, stitch, mode, detailBegins): GlobalTrendRow[]`, `globalTrendFootnote(rows, mode): string | null`, `trendDetailNoteFor(mode, begins, firstPeriod): string | null`, `compositionFootnote(mode): string | null`, `trendPointClass(existing, carriedKeys)`, `carriedTooltipLabel(label, carried)`.
THE RULES the module implements (so you can read it): before `begins` (the served `meta.by_model_fold.per_model_detail_begins`, 2026-05-15) Variant 1 takes the five model lines from the 49 Financial series passed as `stitch.firm49` and Variant 2 draws ONE `Models` band equal to the served `model_aua`; on and after `begins` the five lines are the Global series'; Custom Models is `model_aua` minus the five lines whenever the fold's pooled line `other_models` is served that day, else Inflection's own Custom series (Variant 1) or nothing, flagged `customSuppressed` (Variant 2); the Total, Client Supervised, ETF Strategies and ALT Strategies are read as served, unrounded; a null on a date listed in `carried_dates` takes the last known value (forward only, after the series' first value) and the group is named in `row.carried`.

B. THE TYPES (`src/api/portal-proxy.ts`). On `MdpfPerFirmTimeSeries` add four OPTIONAL fields, each with a one-line comment naming CN-p-2: `client_supervised_aua?: Array<number | null>`, `etf_strategies_aua?: Array<number | null>`, `alt_strategies_aua?: Array<number | null>`, `carried_dates?: string[]`.

C. THE PAGE (`src/pages/ModelPortfolios.tsx`). Every edit below is UNCONDITIONAL (no per-scope choice between two texts): find the named identifier, make the stated change. Per-firm views must not change; the per-firm branch of `timeSeriesDataRaw` and every per-firm code path stay as they are. In order:
1. Import: from `'@/lib/trendGrouping'` add the new names the page uses and drop `etfStrategiesAua`, `otherAua`, `clientChipAt` from the import (they stay exported by the module).
2. Mode: right after `internal` is defined add `const trendMode = trendModeFor(internal)` (the page's own `internal = isInternal() || isDev()`; do not derive the mode from anything else).
3. The two single-firm reads, next to the existing per-firm query, SAME query keys as it (`['mdpf-per-firm-timeseries', '49financial']` and `[... , 'inflection']`), `queryFn: () => getMdpfAggregateAUATimeSeriesByFirm('<id>')`, `enabled: effectiveFirmId === 'global' && internal`, `staleTime: 5 * 60 * 1000`. A non-internal session must not fetch them.
4. The stitch memo (null unless `internal`): `firm49` = for each model of the 49 Financial series whose `cohort_class` is not `'sma'`, the label `getCanonicalModelName(display_name)` kept only if it is one of `GLOBAL_PRIMARY_LABELS`, the points `readModelSeries(data, key)` mapped to `{ period, aum: value }` (never read a `by_model` value array directly: the provenance-read-guard test fails on it); `inflectionCustom` = the same mapping for the Inflection series, then `rollBlendsIntoArchetypeSeries`, then `groupCustomModelsSeries(rolled, new Set(MODEL_ORDER))[CUSTOM_MODELS_LABEL] ?? []`.
5. The served memo, from `globalMdpfData`: `dates`; `total` and `modelAua` from `readGlobalEnterpriseSeries(globalMdpfData)` (`totalAua`, `modelAua`, aligned to `dates`); `primary[label]` = `readModelSeries(globalMdpfData, key).map((p) => p.value)` for each non-`sma` key whose canonical label is in `GLOBAL_PRIMARY_LABELS`; `otherModels` = the same for the key `other_models` or `null` when the key is absent; `clientSupervised`, `etfStrategies`, `altStrategies` = the three new arrays or `null` when absent; `carriedDates` = `carried_dates ?? null`.
6. The rows memo: `buildGlobalTrendRows(served, stitch, trendMode, globalMdpfData?.meta?.by_model_fold?.per_model_detail_begins)`, then dropped past `globalCompleteFrontier` exactly as the existing Global aggregate is. Empty array when there is no Global data.
7. In the `timeSeriesData` memo, when `effectiveFirmId === 'global'` and the rows are not empty, return `{ ...timeSeriesDataRaw, aggregate, by_model }` built from the rows: `aggregate` = `{ period, aum: row.total, pointClass: trendPointClass(<the class the raw aggregate holds for that period>, row.carried) }`; `by_model` = the five labels (their `row.models` values), `CUSTOM_MODELS_LABEL` only if some row has a non-null `custom`, `MODELS_BAND_LABEL` only if `trendMode === 'variant2'` and some row has a non-null `modelsBand`; every point `{ period, aum, pointClass }` with nulls kept as null. Per-firm and any other path stays as it is.
8. `globalTrendBands(period)`: rewrite its body to look the period up in the rows and return `{ total, nonModel: null, sma, clientSup, clientUnsup: null, alt, carriedKeys }` (`sma` = `etfStrategies`, `clientSup` = `clientSupervised`, `alt` = `altStrategies`, `carriedKeys` = `row.carried.join('|')`). Keep its name and its callers. At the two places that read the ALT band from `globalEnterpriseByPeriod.get(...)?.taxAdditiveAua` read `globalBands?.alt` instead; at the daily area's Global total anchor read `globalBands?.total`; in both chart data points add `dataPoint['carried_keys'] = globalBands?.carriedKeys ?? ''`.
9. Retire at Global: delete the constants and memos that only fed the as-of chips and the old Other AUA (`hasGlobalEnterprise`, the `categoryBlock`/`clientAsOf`/`clientSupAsOf`/`clientUnsupAsOf`/`hasClientChips` group) and every use of them; the Bar and Area `show` gates become: `non_model` shown only when `timeSeriesData.isPerFirm`; `sma_additive`, `tax_additive` and `client_supervised` shown at Global when some row has a non-null `etfStrategies`, `altStrategies`, `clientSupervised` (name three small memos for it); `client_unsupervised` never shown. The legend: delete the Client Unsupervised entry and the chip condition, keep Client Supervised, ETF Strategies and ALT Strategies on the same row-derived conditions, drop the Other AUA entry at Global, and add `{ label: CARRIED_LEGEND_LABEL, color: PALETTE.gray300, shape: 'dash' as const }` when some plotted row has a non-empty `carried`.
10. Colour: add `'Models': 'Primary'` to `TREND_GROUP_L1` so the Variant 2 band draws in the Total Assets Primary colour. No other colour changes.
11. Notes: the call that builds `detailNote` becomes `trendDetailNoteFor(trendMode, <same arguments>)`; directly under the existing note paragraph add `<p data-trend-footnote="true" ...>{globalTrendFootnote(rows, trendMode)}</p>` and `<p data-trend-composition="true" ...>{compositionFootnote(trendMode)}</p>`, each rendered only when its text is non-null, in the same small white/60 style as the note.
12. Carried marking: in the tooltip, the row label passes through `carriedTooltipLabel(label, <the hovered row's carried_keys>)`; a period-end bar whose `carried_keys` contains the series label draws at `fillOpacity` 0.55 (the interpolated outline stays as it is).
13. Scope the composition footnote (AMENDMENT 1). Where the page computes `compositionNote` from `compositionFootnote(trendMode)`, make it `null` unless `effectiveFirmId === 'global'`: change that one statement to select by the flag (`effectiveFirmId === 'global' ? compositionFootnote(trendMode) : null`). The `data-trend-composition` paragraph and everything else about it stay as built. No other line of the page changes.

## 2. BOUNDS

1. You change `portal/src/lib/trendGrouping.ts`, `portal/src/pages/ModelPortfolios.tsx` and `portal/src/api/portal-proxy.ts` and nothing else in the portal (a new `src/lib/trendGrouping*.test.ts` is allowed). `CategoryViewTree.tsx` (the lime colour), `otherModelsAsOf.ts` and `aum.ts` stay byte-equal to the base. The approved edits (lime Client Unsupervised, the Other Models "as of", the 49 Financial view, Inflection and Cottonwood as built) ride unchanged.
2. The page does NO arithmetic on a served group: the Total and the three arrays are read as they come; Custom Models is the module's one difference. Do not recompute a group in the page, do not round a served value, do not fill a null with 0.
3. A non-internal session must not receive a single-firm value by any route: the stitch is null for it, the two reads are disabled for it, and the builder ignores a stitch it is handed in Variant 2.
4. No AWS contact, no deploy, no push, no `bun install`, no browser launch.
5. **CLIENT DATA:** never print a client figure or an account id in your report, a row or a file.
6. No non-ASCII character in any line you add. Use the Edit tool; keep CRLF.
7. Do not edit the issuer's checks or the reference. If a step cannot be done as written, file a row naming the step and stop on that step; do not improvise a per-scope fork of the old text.
8. Do not run repo-wide hygiene as a criterion (the issuer runs the type check and the real run at the drain). Write the page so it type-checks: the module's interfaces are strict.

## 3. SURFACES

<paths>
portal/src/lib/trendGrouping.ts
portal/src/pages/ModelPortfolios.tsx
portal/src/api/portal-proxy.ts
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-p-2.portal-variant1-trend-stitch-and-approved-edits.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~27/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/` (the check and `ref/`).

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-p-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/r9_cn_p_2.py" oracle; echo "exit=$?"</invocation><expect>ROUND 9 CN-P-2 ORACLE: 7 of 7 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-p-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/r9_cn_p_2.py" variants; echo "exit=$?"</invocation><expect>ROUND 9 CN-P-2 VARIANTS: 10 of 10 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-p-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/r9_cn_p_2.py" wiring; echo "exit=$?"</invocation><expect>ROUND 9 CN-P-2 WIRING: 9 of 9 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="CN-p-2" judgment="true"/>
</proof_of_spec>

AC1 and AC2 run the pure module under `bun` on contract-shaped fixtures (the producer is not deployed): AC1 against the CRO spec's amended period-end oracle for an internal session, AC2 for Variant 2, the demo tenant (a session that is not `opal-capital` and not `Dev` must draw Variant 2 and the stitch must be OFF), carried points and the notes. AC3 reads the page, the types and the scope as normalised text. They cannot prove what the two sessions DRAW. AC4 is JUDGMENT, graded at the round close (never self-graded): the issuer renders the Global Trend at a STATED portal commit on `bun run dev:live --port 5174` for an internal session and for a demo-tenant claim set, against the producer's deployed arrays and the spec's oracle. You do not render.

## 5. WHEN YOU ARE DONE

1. Commit the three portal files (and a test file if you wrote one) INSIDE the nested repo: `git -C "<worktree>/portal" add -- <those paths>` then `git -C "<worktree>/portal" commit --author "0.9.0_WK_MDPF_CANON~27 <0.9.0_WK_MDPF_CANON~27@opal.agent>" -F <msgfile>` (message file written with the Write tool). If a portal hook refuses, file a row with its text and stop: do not bypass it.
2. Write the proof instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~27/MDPF_CANON.TO-CN-p-2.portal-variant1-trend-stitch-and-approved-edits.proof_of_spec.json`, AC4 UNVERIFIABLE-BY-INSTRUMENT with status_reason "graded at the round close". **Flip this order's `<status>` to `complete` in the SAME commit as the instance**, and only when AC1, AC2 and AC3 all pass.
3. Commit the OUTER files via `.tools/safe-commit.sh --author "0.9.0_WK_MDPF_CANON~27 <0.9.0_WK_MDPF_CANON~27@opal.agent>" -F <msgfile> -- <paths>` (outer paths only; do not stage `portal`). Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.

Report once: the portal branch and commit hash, the diff stat (one line), the output lines of AC1, AC2 and AC3, the outer commit hash, and any row (name any step you could not do as written).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (issuer, 2.0.0_SA_COO~D1, after the worker's row MDPF_CANON-D1-W27-S2; the order is reopened):** item 13 scopes the composition footnote to the Global view. No mechanical arm is added (the footnote's scope is a rendering fact; the issuer's real run at AC4 reads it on a per-firm view and on Global). The modification is not graded by any gate limb (to-pipeline-gate grades newly-added orders; placeholders NONE); the CTO reads it at the round-N analysis. Base for the re-run: AC1 to AC3 stay green at the built head.

**ISSUER NOTES:** Cut of the Variant 1 round (CTO msgs 5868, 5873, 5877, 5886). PRD v2.19 (@02852d9d16) chose Variant 1; v2.20 (@038b2173f3) made the pre-05-15 lines and the 05-15 .. 07-19 Custom a READ-SIDE stitch for an internal session only, because the external demo tenant opens Global (CVO, `ModelPortfolios.tsx:271`, `:375-379`); v2.21 (@3826492d9c) put the SMA strategies in for every session. This cell is the portal half; `CN-p-1` is the producer half and owes the arrays. The CN-i-3 revert-by-scope order is WITHDRAWN; the CN-i-2 order file stays as delivered. The base `scratch/canon-i3-base` is PROD 5ab67a65 plus the three feature commits (patch-ids equal to `fd5433a3`); re-derive from the then-current PROD at the cut if PROD moved. LANDING (CLAUDE.md Portal): client-facing row for Andrew (approval row cut FROM PROD with cherry-picks; the tool refuses a branch that overlaps DEV), DEV only by `portal-merge-forward.sh`, PROD only by a chosen-set promote. The CRO asked for one line (branch and head hash) when the full-history Trend is ready to smoke on 5174 (msgs 5872, 5878). **RISK CLASS:** `LOCAL`, `worker` (three files, a copyable pure module, twelve named page steps). The issuer's real run: `/ui-walk` at the stated commit, Global, Trend, as an internal session and as a demo-tenant claim set (stitch OFF, Variant 2), compared to the spec's amended oracle.
**OPEN for the issuer (see the fork report):** (1) whether `CN-p-1` carries the Total and the five model arrays on the `carried_dates` as well (the module tolerates both: it rolls a null forward on a listed date); (2) the Custom pre-05-15 sliver; (3) v2.18 said "NO band" while v2.20 and the spec's Variant 2 say one `Models` band -- this order follows the spec and the cut brief; (4) the composition footnote names two partner firms and so shows to internal sessions only.

**Fanout:** 2 of 2 chains with `CN-p-1`; no shared file with another open cell. `portal_ref:` `scratch/canon-i3-base` (f8c7d310).

<status>complete</status>
<round>9</round>
<to_id>MDPF_CANON.TO-CN-p-2</to_id>
<slot>~27</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
