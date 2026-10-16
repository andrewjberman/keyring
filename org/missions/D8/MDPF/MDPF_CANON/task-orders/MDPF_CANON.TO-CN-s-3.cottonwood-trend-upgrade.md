# MDPF_CANON task order -- `CN-s-3` -- THE COTTONWOOD AUM TREND STARTS AT ITS FIRST MEASURED TOTAL, FILLS OTHER AUM, AND CARRIES THE 12 ABSENT MODEL LEGS (FWD-9 head f; PORTAL CANDIDATE, CLIENT-FACING AT THE LANDING)


<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-s-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~31</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; one new portal module and the page's Cottonwood Trend wiring.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS contact at all (the check runs `bun` on a pure module and on a committed copy of a served object).
comp-adversary: RUN by the issuer on DELL1 at the base (portal DEV 39dab87f3b) -- `r11_cn_s_3.py pure` 0 of 7 arms (every arm red at the base: the module does not exist); a scratch reference module reads 7 of 7 (the arms can pass); planted mutants (Other taken as `non_model_aua`; the 12 dates left absent; the window starting at the first model date; a negative group; the input mutated) each turn their named arm red; `selftest` prints OK.
EGRESS CLASS, declared: none.
</preflight>

**Your worktree:** you are already in it (slot ~31, outer branch `wk-MDPF_CANON-31`, portal branch `wk-MDPF_CANON-31-portal`); this order is handed to you after CN-s-5. The earlier commits on the branch stay as they are. Start every shell call with `cd` into the outer worktree path.
**Line endings: `src/pages/ModelPortfolios.tsx` is CRLF in EVERY line, keep it; the new `src/lib/cottonwoodTrend.ts` takes the same CRLF as its sibling `src/lib/trendGrouping.ts`.** After your edits run `git -C "<worktree>/portal" diff --stat` and check that no line of a CRLF file is LF-only.

## 0. AMENDMENT 1 -- READ THIS FIRST (the issuer's real run found one marking gap; the order is reopened)

You inherit your built and committed CN-s-3 (portal `34a15de1`, and its copy on the issuer's landing candidate `1e39adc9` + `978da061`); it stays as it is except this one repair. The issuer rendered the Cottonwood Trend (Monthly view) and hovered the 2026-08-31 bar, a carried date: the bar draws, its Total is right and every leg equals the CRO oracle, and the tooltip marks `Custom Models (carried)` and `Other AUA (carried)`, but the five primary lines read without the `(carried)` suffix. Cause, read from the page: the tooltip row label is `carriedTooltipLabel(entry.name, carried_keys)` (`ModelPortfolios.tsx` near L1311), which marks a row only when its `entry.name` is IN the `carried_keys` list; your `cottonwoodCarriedByPeriod` builds that list from `GLOBAL_PRIMARY_LABELS` (`Ultra-Short Term`, `Short Term`, `Intermediate Term`, `Long Term`, `Ultra-Long Term`), while the tooltip entries' names for those five series read (from the render) `Ultra Short-Term`, `Short-Term`, `Intermediate-Term`, `Long-Term`, `Ultra Long-Term`. THE REPAIR: make the Cottonwood carried keys for the five primary series equal the names the tooltip entries carry. Find where those five series get their `name` (the chart series for the Cottonwood view, for example via `modelPortfolioColors.ts` or the page's display-name helper) and derive the keys from the SAME source, so the two cannot drift; only if no single source exists, use the five strings above. Do not touch `Custom Models` or `Other AUA` (they already match), the Global path, `trendGrouping.ts`, `cottonwoodTrend.ts` or any other firm. The pure check does not see the page (AC1 stays 7 of 7); the judgment AC2 is re-graded on a re-render. Commit it as ONE more portal commit on the branch you are on, flip this order to `complete` again in your outer proof commit (update the proof instance's commit reference), and report as before.
## 1. THE CELL -- `CN-s-3` (round 11)

**The cell, verbatim from the decomposition:** the Cottonwood AUM Trend upgrade (CRO spec): a new pure module `cottonwoodTrend.ts` builds one row per total-bearing served date from the first one (2026-06-09) to the as-of: Total = `partner_custody_total`, the five primary lines = the models' `model_value`, Custom = `model_aua` minus the five, Other AUM = `partner_custody_total` minus `model_aua` on EVERY row with a total (today drawn only from 2026-07-20), the 12 absent-model-leg dates listed in `meta.channel_participation.exceptions` take the last measured model leg and are marked carried with their measured Total, the sanctioned backfill window keeps its interpolated marking; the page's Cottonwood Trend draws from it, no 2026-04-22 extension.

**Read first:** the CRO spec `org/tier1_exec/4.0.0_SA_CRO/deliverables/MDPF_CANON_COTTONWOOD_AUM_TREND_UPGRADE_SPEC_20261015.md` (the rule per group, the month-end oracle, why the empty months are NOT filled with the Commonwealth slice) and the issuer's reference oracle `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/draft/checks/r11_cn_s_3_oracle.py` (the rule in Python, derived from the served object).

**What it is:** on the page's Cottonwood view (`effectiveFirmId === 'cottonwood'`) the AUM Trend today draws a rolling one-year window from October 2025, but Cottonwood's measured coverage begins in 2026; the Other AUM band is drawn only from 2026-07-20; the month-end bars of 12 dates (2026-07-28, 07-29, 07-30, 08-04, 08-12, 08-31, 09-01..09-04, 09-08, 09-09) draw nothing because their model leg is absent although their Total is measured. The upgrade fixes all three from the served object alone, with no new pull.

**THE MODULE CONTRACT (fixed by the issuer; the check tests exactly this):** a NEW pure file `portal/src/lib/cottonwoodTrend.ts` (no imports from the page; it may import types) exporting `buildCottonwoodTrendRows(raw: any): CottonwoodTrendRow[]`, where `raw` is the served Cottonwood `aggregate-aua-timeseries` object exactly as the page holds it (`perFirmMdpfData` for the Cottonwood view), and

`CottonwoodTrendRow = { period: string; total: number | null; primary: { 'Ultra-Short Term': number | null; 'Short Term': number | null; 'Intermediate Term': number | null; 'Long Term': number | null; 'Ultra-Long Term': number | null }; custom: number | null; other: number | null; cls: 'measured' | 'interpolated' | 'carried' }`

Values are DOLLARS. One row per TOTAL-BEARING served date, from the first total-bearing date through the as-of date (a served date with no total, such as the weekend dates 2026-06-13, 06-14, 06-19, 06-20, 06-21, gets no row; no row before the first total; 90 rows on the 2026-10-15 object, 89 on the CRO spec's 10-14 read). The rule: `total` = `partner_custody_total`; the five primaries = each model's `model_value` (keys as the oracle's PRIMARY list); `custom` = `model_aua` minus the five primaries; `other` = `partner_custody_total` minus `model_aua` on EVERY row that has a total; the dates listed under `meta.channel_participation.exceptions` (model leg absent, Total measured) take the LAST measured model leg (the five primaries and `model_aua` rolled forward), keep their measured `total`, and are `cls: 'carried'`; rows in the sanctioned interpolated-backfill window (before the first measured model date, `meta.composed_backfill`) are `cls: 'interpolated'`; the rest `'measured'`. The function must not mutate `raw`, must not write 0 for a value the object serves as null, and must read the Total, never recompose it.

**The page:** wire the Cottonwood Trend's data (the Trend bar chart and its daily area, in `src/pages/ModelPortfolios.tsx`; find them where the Cottonwood view draws the AUM Trend, near the chart whose tooltip sets `cursor={{ fill: 'rgba(255,255,255,0.05)' }}`, L2145 at the CRO's read) to draw from `buildCottonwoodTrendRows(perFirmMdpfData)` on the Cottonwood view only; every other firm's Trend stays byte-equal. The window starts at the first row (2026-06-09), not at a rolling year; the "Interpolated model mix (estimate)" marking stays on `cls: 'interpolated'` rows; a `carried` row draws with the existing carried marking and tooltip text the Global Trend uses (`carriedTooltipLabel`, `CARRIED_LEGEND_LABEL` from `trendGrouping.ts`). Do not extend the window back to 2026-04-22 (the optional extension is not in this cell). If the page's structure needs more than the Cottonwood branch of the Trend wiring changed, file a row naming what, and stop on that step.

## 2. BOUNDS

1. You change `portal/src/lib/cottonwoodTrend.ts` (new), `portal/src/pages/ModelPortfolios.tsx` (the Cottonwood Trend wiring only) and nothing else in the portal (a new `src/lib/cottonwoodTrend*.test.ts` is allowed). `trendGrouping.ts` is NOT yours in this order.
2. The page does NO arithmetic on a served value outside the module; the module's only arithmetic is the two differences stated above. Do not round a served value, do not fill a null with 0, do not interpolate or back-fill an assignment before 2026-07-21.
3. Do not draw the Commonwealth custody slice or any series the object does not serve; do not extend the window before the first total.
4. No AWS contact, no deploy, no push, no `bun install`, no browser launch.
5. **CLIENT DATA:** never print a client figure or an account id in your report, a row or a file.
6. No non-ASCII character in any line you add. Use the Edit tool; keep line endings.
7. Do not edit the issuer's checks, the draft oracle or the committed fixtures. If a step cannot be done as written, file a row naming the step and stop on that step.
8. Do not run repo-wide hygiene as a criterion (the issuer runs the type check and the real run at the drain).

## 3. SURFACES

<paths>
portal/src/lib/cottonwoodTrend.ts
portal/src/pages/ModelPortfolios.tsx
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-s-3.cottonwood-trend-upgrade.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~31/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/` (the check and `ref/`) and the CRO spec `org/tier1_exec/4.0.0_SA_CRO/deliverables/MDPF_CANON_COTTONWOOD_AUM_TREND_UPGRADE_SPEC_20261015.md` (the check reads its month-end oracle table at run time; your sparse worktree carries that folder).

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-s-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 120 python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/r11_cn_s_3.py" pure; echo "exit=$?"</invocation><expect>ROUND 11 CN-S-3 PURE: 7 of 7 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-s-3" judgment="true"/>
</proof_of_spec>

AC1 runs the new pure module under `bun` on the committed copy of the real served Cottonwood object (as served 2026-10-15; the check holds the CRO spec's month-end oracle). It cannot prove what the page DRAWS. AC2 is JUDGMENT, graded at the round close (never self-graded): the issuer renders the Cottonwood Trend at a STATED portal commit on `bun run dev:live --port 5174` and looks at the window start, the Other AUM band, the interpolated and carried marking and the Aug 31 bar. You do not render.

## 5. WHEN YOU ARE DONE

1. Commit the portal files INSIDE the nested repo as ONE portal commit, separate from the earlier ones: `git -C "<worktree>/portal" add -- src/lib/cottonwoodTrend.ts src/pages/ModelPortfolios.tsx` (plus a test file if you wrote one), then `git -C "<worktree>/portal" commit --author "0.9.0_WK_MDPF_CANON~31 <0.9.0_WK_MDPF_CANON~31@opal.agent>" -F <msgfile>` (message file written with the Write tool). If a portal hook refuses, file a row with its text and stop: do not bypass it.
2. Write the proof instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~31/MDPF_CANON.TO-CN-s-3.cottonwood-trend-upgrade.proof_of_spec.json`, AC2 UNVERIFIABLE-BY-INSTRUMENT with status_reason "graded at the round close". **Flip this order's `<status>` to `complete` in the SAME commit as the instance**, and only when AC1 passes.
3. Commit the OUTER files via `.tools/safe-commit.sh --author "0.9.0_WK_MDPF_CANON~31 <0.9.0_WK_MDPF_CANON~31@opal.agent>" -F <msgfile> -- <paths>` (outer paths only; do not stage `portal`). Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.

A row id carries the dell1 infix: `MDPF_CANON-D1-W31-S<k>`, with `surfaced_at` from `date -u +%FT%TZ`.
Report once: the portal commit hash, the diff stat (one line), the output line of AC1, the outer commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 11, issuer 2.0.0_SA_COO~D1, on the CTO's round-10 analysis (msg 6731) item 3 head (f), PRD v2.23 @1fb9ac96ab, the CRO spec @21caa664be (Verdict: DOABLE from MDPF's own served Cottonwood object, with no new pull). The draft's CN-s-2 (producer emission of the carried legs) is DISSOLVED into this cell by ruling 1 of the v11 section: `apply_global_trend_groups` resets `carried_dates` to `[]` on every scope, so a producer emission would be overwritten, while the object already lists its own absent-leg dates in `meta.channel_participation.exceptions`; the carry therefore rolls read-side, keyed on that served list.
- **Oracle rebasing:** the check grades the object as served 2026-10-15 (Muni still in Other). After CN-s-1's deploy (no earlier than the 2026-10-17 13:30Z fire) Custom rises and Other falls by the `Opal_Muni_Income` account on every date it holds a value, so the issuer re-bases the month-end oracle at the real run; the rule does not change.
- **The chart's cursor band (the CRO's item 4)** is not data and is claimed inferred; it disappears with the window start. Not a criterion.
- **Staged:** this order stays `staged` until CN-s-5 is terminal, then the issuer flips it to `pending` and continues the worker.
- **LANDING (CLAUDE.md Portal):** client-facing row for Andrew (Cottonwood partner page); the approval row is cut FROM PROD with a cherry-pick of this ONE commit.

**Fanout:** chain 1 of 2: `CN-s-4` -> `CN-s-5` -> `CN-s-3`, one worker, slot ~31. `portal_ref:` 39dab87f3b.

**AMENDMENT 1 (issuer, 2.0.0_SA_COO~D1, 2026-10-16 ~15:2xZ; the order is reopened):** on the CVO's C-S95 (ADJUDICATION_v20: render the Monthly view and one carried-date tooltip) the issuer rendered both (PNGs outside the repo, per C-S96) and found the five primary lines unmarked `(carried)` on 2026-08-31, a key-versus-display-name mismatch inside the worker's carried-key list (section 0 of the face). The modification is not graded by any gate limb (`to-pipeline-gate.py` grades newly-added orders and a modified order only for GATE (viii) placeholders, which read NONE); the CTO reads it at the round-N analysis. The mismatch may also exist on the Global Trend's carried rows (the same `carriedTooltipLabel` comparison); NOT checked, and outside this order.

<status>in_progress</status>
<round>11</round>
<to_id>MDPF_CANON.TO-CN-s-3</to_id>
<slot>~31</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
