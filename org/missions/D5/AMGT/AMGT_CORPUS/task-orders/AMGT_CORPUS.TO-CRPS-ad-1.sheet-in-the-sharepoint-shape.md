# AMGT_CORPUS task order -- `CRPS-ad-1` -- ROUND 28: the Model sheet in the SharePoint shape, with its forecasts

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ad-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures and an issuer capture.
comp-adversary: RUN by the issuer at the cut on portal DEV a41cf763 -- sheet.cjs 2 of 6 (FAIL as designed: arms 3 and 5 are the history and no-forecast controls and pass at base); CENSUS keys 100 rows 1700 shown 1055 absent 145 unmapped 500; bound 4 of 4 green at base. Blind spots: one name (BA) for rows, history and forecasts; the census reads mnemonic sets, not rendered rows; static render only.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 28. Serves FWD-20 (a figure on every row the team's sheet carries), FWD-12
(the sheet is the team's SharePoint shape) and FWD-21 (the served 2026E-2028E forecasts).

## 1. THE CELL -- `CRPS-ad-1`

The Model tab's row shape is `portal/src/pages/SecurityAnalysis/modelSheet.ts` (`FINANCIAL_SUMMARY_ROWS`, `MARGIN_HISTORY_ROWS`,
`buildModelSheet`). Today five rows are hard-coded to no field (`mnemonic: null`), so they render as "not on the model block" on every
name -- 500 rows over 100 names -- although the block already pulls their fields; those fields show lower down under "Other lines the
block carries", a group the team's sheet does not have. And the block serves FY1-FY3 forecasts that no portal code reads.

**Build, in `modelSheet.ts` only:**
1. **Map the five rows** to the fields the block already pulls: Revenue/Sh `REVENUE_PER_SH`; FCF yield `FREE_CASH_FLOW_YIELD`; FCF
   margin `FREE_CASH_FLOW_MARGIN`; RoTA `RETURN_ON_TANGIBLE_ASSETS`; Earnings margin `PROF_MARGIN`. Keep every label and the row
   order exactly as they are.
2. **No Other-lines group.** `buildModelSheet` returns the two groups (Financial Summary; EBITDA and margin history) only. Lines the
   team's sheet does not carry are not rendered. Keep exporting the row specs.
3. **Forecast columns.** `buildModelSheet(figures, fiscalYears?, servedLineNames?, forecastFigures?)` -- a new OPTIONAL fourth
   parameter, the served `model.forecast_figures` list. When it carries figures, the sheet's `years` gain `<fiscal_year>E` columns
   (e.g. `2026E`, `2027E`, `2028E`) after the history years, in ascending order, and these rows carry the served forecast figure at
   that year, value for value: EPS `BEST_EPS`, BVPS `BEST_BPS`, DPS `BEST_DPS`, Dividend yield `BEST_DIV_YLD`, P/E `BEST_PE_RATIO`,
   EBITDA `BEST_EBITDA`. A row with no forecast at a year has an empty cell there. Rows without a forecast mnemonic have empty E cells.
   With no forecast figures (absent, null or empty) the sheet is exactly today's: no E column, and `estimateYearsAbsent` still names
   the estimate years the block lacks. When forecasts fill the E columns, `estimateYearsAbsent` names only the years still missing.
4. **Every history cell is byte-unchanged** (same figure object at the same row and year), with and without forecasts.
5. Do NOT edit `ModelTab.tsx` -- it passes the forecasts in a later cell (`CRPS-ad-3`). It must keep compiling against your
   signature, which it does if the new parameter is optional.

**The rules every cell keeps (PRD CONTRACTS):** C-PRESENTATION-ONLY -- the sheet places served figures, it computes none. **Design law
(portal `DESIGN.md`):** a code, field name or path may sit in a data attribute or in code, never in visible text.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`; a heredoc on this machine turns `\b` into a
   0x08 byte.
5. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k), with `disarm_owner 2.0.0_SA_COO~X`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/modelSheet.ts
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-ad-1.sheet-in-the-sharepoint-shape.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ad-1.sheet-in-the-sharepoint-shape.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md`, `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx`, the issuer's
checks under `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round28/` and DSGN's loader and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 300)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ad-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round28/sheet.cjs"; echo "exit=$?"</invocation><expect>THE SHEET IN THE SHAREPOINT SHAPE: 6 of 6 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ad-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bound.cjs" AD1 modelPattern.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10 errorEmpty.harness.cjs:12; echo "exit=$?"</invocation><expect>AD1 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-ad-1"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node_modules/.bin/tsc -b --noEmit; echo "exit=$?"</invocation><expect>(?m)^exit=0$</expect></criterion>
</proof_of_spec>

- AC1 (`sheet.cjs`, six arms on BA's served `/thesis` capture): the five rows read their fields with a figure; no Other-lines group
  and the team sheet's rows in their order; the twelve mapped rows' history cells equal the base snapshot; with BA's served
  `model.forecast_figures` the last columns are `2026E, 2027E, 2028E` and the six forecast rows carry the served values; with an empty
  forecast list no E column and the missing estimate years still named; over 100 names (the issuer's capture) 0 rows hard-coded to no
  field.
- AC2: the page's own harnesses that load the Model tab stay green at their floors.
- AC3: the portal typechecks.

## 5. WHEN YOU ARE DONE

1. Write the instance at the proof path in section 3.
2. Run `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` AFTER your final commit, and pin
   each artifact row to the commit whose BYTES you graded (verify with `git show <pin>:<path>`). It must return rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file, in the SAME commit as your proof
   instance.
4. Report ONCE: what changed (the five mappings, the signature), the output line of every criterion, the portal and outer commit
   hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-27 analysis s.3 item 1 @`99b83b495a`; PRD v0.7 FWD-12/20/21. Base CLOUD `bd29533457`, portal DEV `a41cf763`:
sheet.cjs 2 of 6; bound 4 of 4. The forecast parameter is placed here (not in ad-3) so the row logic stays in the row-shape file
(CONTRACT s.0); ad-3 consumes it. BEST_DIV_YLD is served in percent like EQY_DVD_YLD_IND.
<risk>LOCAL</risk>
<status>pending</status>
<round>28</round>
<slot>~1</slot>
<fabric>site-z</fabric>
