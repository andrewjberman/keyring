# MDPF_CANON task order -- `CN-i-2` RE-CUT AS `CN-i-3` -- THE GLOBAL AUA TREND GOES BACK TO PROD'S TEXT; EVERY OTHER SCOPE KEEPS THE CANDIDATE'S (FWD-9; PORTAL CANDIDATE, HELD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-i-2, CN-i-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~25</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; one portal page file.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS contact at all (the checks read git objects only).
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 -- `r8_cn_i_3.py sites` reads 1 of 2 at base (P1 fails: 22 of 24 PROD lines missing; P2 is a control) and `scope` 1 of 2 (S1 fails; S2 is a control); the selftest prints OK.
EGRESS CLASS, declared: none.
</preflight>

**Your worktree:** the spawn names it (outer branch `wk-MDPF_CANON-25`, cut from the issuance commit). The portal is a NESTED repository at `<worktree>/portal`, provisioned on its own branch `wk-MDPF_CANON-25-portal`
cut from a base that is the CURRENT portal PROD head (`5ab67a65`) plus the three feature commits (so `git -C portal diff 5ab67a65 HEAD` is the whole feature). `node_modules` is linked. Start every shell call with `cd` into the outer worktree path.
`src/pages/ModelPortfolios.tsx` uses CRLF line endings: keep them.

## 1. THE ACT -- `CN-i-3`

THE REQUIREMENT (Andrew-direct, ~20:1xZ today, as the issuer was told it). The Global AUA Trend as built by the feature is declined: at the **Global** scope the Trend must be exactly PROD's. Everything else the feature does stays, including the 49 Financial view as it is. So `src/pages/ModelPortfolios.tsx`
must choose, per scope, between two texts that are both already written: PROD's text (for Global) and the feature's text (for every other scope). You write NO new Trend behaviour: you only add the choice. You touch ONE file.

THE RECIPE (uniform; every site below uses it).
- Once, in the component body where `effectiveFirmId` is already in scope and before its first use below, on its own line: `const isGlobalTrend = effectiveFirmId === 'global'`.
- At each site, keep BOTH texts verbatim, each text on its OWN lines (the checks compare trimmed lines), and select with a conditional whose `?` and `:` are on lines of their own: `isGlobalTrend` then `? <PROD text>` then `: <feature text>`. Do not reword, reflow or merge either text.
- The PROD text of every site is what the feature REMOVED: run `git -C "<worktree>/portal" diff 5ab67a65 HEAD -- src/pages/ModelPortfolios.tsx` and read every hunk; each `-` line is PROD's text, each `+` line is the feature's. (HEAD at the start of your task is that base.)

THE SITES (in ModelPortfolios.tsx; read each hunk in the diff above before editing it):
1. `STACK_SERIES` (module constant): keep it as it is (the feature's list). Add, right above it, `const STACK_SERIES_PROD` holding PROD's whole list, copied verbatim from `git -C portal show 5ab67a65:src/pages/ModelPortfolios.tsx`. Inside the component add `const stackSeries = isGlobalTrend ? STACK_SERIES_PROD : STACK_SERIES` (with the `?`/`:` rule) and use `stackSeries` at EVERY place the component's Trend code reads `STACK_SERIES`.
2. `trendModelOrderWithNonModel`: Global gets `[...trendModelOrder, 'Non-Model']`; other scopes keep the feature's list.
3. The memo that returns `{ ...timeSeriesDataRaw, by_model: ... }`: Global gets `rollBlendsIntoArchetypeSeries(timeSeriesDataRaw.by_model)` alone (no custom grouping); other scopes keep `groupCustomModelsSeries(rolled, new Set(MODEL_ORDER))`.
4. The tooltip `buckets`: Global gets `payload.filter((entry) => entry.dataKey !== 'interp_total')`; others keep `presentTrendEntries(...)`.
5. The colour at the tooltip/legend row (`color: trendColorOf(modelName) || modelColor?.primary || PALETTE.blue400`): Global gets `color: modelColor?.primary || PALETTE.blue400`.
6. The legend extras (Client Supervised, Client Unsupervised, ETF Strategies, ALT Strategies): Global gets PROD's entries (`Additive SMA sleeves`, `Tax-Managed SMA`, no Client entries).
7. The boundary note: DELETE it. Remove the `detailNote` constant, its `<p data-trend-detail-note>` paragraph, and the name `trendDetailNote` from the import (the note existed only at Global; elsewhere it was always null). This is the one site where the feature's text is dropped, and the checks exempt exactly the lines that name it.
8. The data points of the quarterly bars AND of the daily area (`nmKey`, `sma_additive`, the Client keys): Global gets PROD's lines; others keep the feature's.
9. The mount filter `(s.key === 'client_supervised' || s.key === 'client_unsupervised') ? ... : trendModelOrder.includes(s.label)`: Global gets PROD's `: trendModelOrder.includes(s.label)` form; others keep the feature's.
10. `fill={trendSeriesColor(s.key, s.label) || modelColor?.primary || PALETTE.gray300}`: Global gets `fill={modelColor?.primary || PALETTE.gray300}`.
Leave every OTHER hunk of the diff alone: the imports for `carriedAsOf`/`asOfLabel`, the `carriedAsOf` field, the `carriedAsOf:` mapping, the `[scopeAumMetrics, dataAsOf]` dependency, the `selectedPortfolio.carriedAsOf` span (the Other Models "as of"), `globalCarveOutByPeriod`, the Client-chip constants and `globalTrendBands` (they stay, used by the feature's text).

## 2. BOUNDS

1. You change `portal/src/pages/ModelPortfolios.tsx` and nothing else in the portal. `CategoryViewTree.tsx` (the lime colour), `trendGrouping.ts`, `portal-proxy.ts`, `otherModelsAsOf.ts` and `aum.ts` stay byte-equal to the base.
2. No new Trend behaviour, no new colour, no reworded text. If a site cannot take the recipe, file a row naming the site and stop on that site.
3. No AWS contact, no deploy, no push, no `bun install`, no browser launch.
4. **CLIENT DATA:** never print a client figure or an account id in your report, a row or a file.
5. No non-ASCII character in any line you add. Use the Edit tool; keep CRLF.
6. Do not edit the issuer's checks. Do not run repo-wide hygiene as a criterion (the issuer runs the type check and the real run at the drain).

## 3. SURFACES

<paths>
portal/src/pages/ModelPortfolios.tsx
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-i-2.aua-trend-repair-colour-tooltip-note.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~25/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular the issuer's check `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r8_cn_i_3.py` (never edit it; read what each arm asserts).

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-i-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r8_cn_i_3.py" sites; echo "exit=$?"</invocation><expect>ROUND 8 CN-I-3 SITES: 2 of 2 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-i-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r8_cn_i_3.py" scope; echo "exit=$?"</invocation><expect>ROUND 8 CN-I-3 SCOPE: 2 of 2 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-i-3" judgment="true"/>
</proof_of_spec>

AC1 and AC2 are source-level: they prove both texts exist and that nothing outside the one file moved; they cannot prove WHICH text each scope draws. AC3 is JUDGMENT, graded at the round close (never self-graded): the issuer renders the Global Trend at a STATED portal commit on `bun run dev:live --port 5174` and compares it with PROD's. You do not render.

## 5. WHEN YOU ARE DONE

1. Commit the one portal file INSIDE the nested repo: `git -C "<worktree>/portal" add -- src/pages/ModelPortfolios.tsx` then `git -C "<worktree>/portal" commit --author "0.9.0_WK_MDPF_CANON~25 <0.9.0_WK_MDPF_CANON~25@opal.agent>" -F <msgfile>` (message file written with the Write tool). If a portal hook refuses, file a row with its text and stop: do not bypass it.
2. Write the proof instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~25/MDPF_CANON.TO-CN-i-2.aua-trend-repair-colour-tooltip-note.proof_of_spec.json`, AC3 UNVERIFIABLE-BY-INSTRUMENT with status_reason "graded at the round close". **Flip this order's `<status>` to `complete` in the SAME commit as the instance**, and only when AC1 and AC2 both pass.
3. Commit the OUTER files via `.tools/safe-commit.sh --author "0.9.0_WK_MDPF_CANON~25 <0.9.0_WK_MDPF_CANON~25@opal.agent>" -F <msgfile> -- <paths>` (outer paths only; do not stage `portal`). Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.

Report once: the portal branch and commit hash, the diff stat (one line), the output lines of AC1 and AC2, the outer commit hash, and any row (name any site you could not fit to the recipe).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** THIS FILE IS THE CN-i-2 ORDER, MODIFIED (the TO issuance gate's one-issuer-per-round limb refuses a second order file in round 8 and reads no override: a re-cut into the first issuance MODIFIES its orders). Its prior act (the Client Unsupervised colour, the tooltip filter, the boundary note) was delivered by worker ~24 (outer `9e1e72997d`, portal `71ed7393`; instance VALID, recorded under `deliverables/0.9.0_WK_MDPF_CANON~24/`); Andrew declined the Trend parts; the colour stays; this act replaces the rest. The status goes complete to pending. Andrew declined the Trend as built (row 19ae CLOSED declined; record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_201xZ_PORTFOLIOS_SMOKE_TREND_FULL_HISTORY_COTTONWOOD_SPEC.md` @caf5dc7d73) and approved the other popup edits, the lime repaint and the 49 Financial view; the CTO's direction (msg 5831): ONE candidate branch, fd5433a3's changes with the Global AUA Trend
byte-equal to PROD 5ab67a651a's Trend, the 49F view unchanged; render the Trend on 5174 and diff it against PROD; register a fresh client-facing row and HOLD it (Andrew is deciding whether to ship now or wait for the full-history Trend the CRO is speccing). Stop at 20:45Z if not done and hand off for the re-seat (the 21:00Z dell1 restart).
The base (`scratch/canon-i3-base` in the portal repo) is current PROD plus the three feature commits, the same patches as fd5433a3 (patch-ids equal). The issuer's real run: `/ui-walk` at the stated commit, Global, Trend, and a pixel or DOM comparison with a PROD build of the same data.
**OPEN, put to the CTO:** the Inflection and Cottonwood Trend views in the feature also carry the custom grouping and the label changes (the recipe keeps them as the feature has them, per "the 49F view is unchanged"); Andrew said of Inflection "No need to touch these". **RISK CLASS:** `LOCAL`, `worker` (one file, ten sites, a recipe). LANDING (CLAUDE.md Portal): DEV only by `portal-merge-forward.sh` on an approved row, Andrew approving; PROD only by a chosen-set promote.
DEV already carries the declined Trend as `9e637fe51e` (landed before the CTO's "do not promote"); fixing DEV is a follow-up the CTO owns.

**Fanout:** 1 of 1 chains; no shared file with another open cell. `portal_ref:` `scratch/canon-i3-base` (PROD 5ab67a65 plus the three feature commits).

**CLOSED 2026-10-14 ~21:4xZ (2.0.0_SA_COO~D1): SUPERSEDED.** CN-i-2 delivered (merged, candidate `f8c7d310`); CN-i-3, which this order carried, is WITHDRAWN (CTO msg 5877, Andrew-direct "whatever CRO~DELL1 and I agreed on"); the Global Trend is rebuilt by round 9 cell CN-p-2. Slot ~25 is released; no further work is owed on this file.

<status>superseded</status>
<round>8</round>
<to_id>MDPF_CANON.TO-CN-i-2</to_id>
<slot>~25</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
