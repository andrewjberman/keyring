# AMGT_CORPUS task order -- `CRPS-al-2` -- ROUND 36: the Model sheet renders the 49 V3 lines (FWD-20)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-al-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task, alarm or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the check reads a fixture file.
comp-adversary: RUN by the issuer at the cut on portal DEV ec65c5d637 -- al2_check.cjs build 0/3 control 1/1. Blind spot: the check grades the pure sheet builder on two captured names; the rendered page is the CVO's judgment (AC3) on the running build.
EGRESS CLASS, declared: NONE. Portal source only. NO push of any portal branch: the DEV push is Andrew's word after the CTO's review.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 36. This is the SECOND order of your queue; it reads the field your first
order (`CRPS-al-1`) added: `read_model(...)["fiscal_unresolved"]`, a list of `{mnemonic, fiscal_year, reason}`, served on the
`/thesis` payload as `data.model.fiscal_unresolved`.

**Your portal.** Your worktree's `portal/` is a nested git repository checked out at portal `DEV` @`ec65c5d637` on your own portal
branch. Portal files commit INSIDE `portal/` on that branch first, then the outer commit for the outer files. Never commit the
portal gitlink in the outer repository.

## 1. THE CELL -- `CRPS-al-2`

FWD-20 (PRD `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md` about line 560): "A viewer opens any name's Model tab and every
row the team's sheet carries shows a figure ... a row that still cannot show says why in words a PM reads, never 'ABSENT',
'REFUSED --' or 'not read'."

Round 34 added 52 mnemonics to every model block. The 49 V3 lines among them do not reach the page, because
`portal/src/pages/SecurityAnalysis/modelSheet.ts` names only 17 rows (`FINANCIAL_SUMMARY_ROWS` 13 + `MARGIN_HISTORY_ROWS` 4). Round
35 gave all 52 measured units, so 0 figures carry a pointer unit now. The 49 split, measured at the cut, into:
- **44 fiscal lines** (block scope `fiscal_year_line_item`): ARD_GOODWLL, ARD_OTHER_INTANGIBLE_ASSET, ARD_SHARES_OUTSTANDING,
  ARD_TOTAL_CURRENT_LIABILITIES, ARD_TOT_ASSETS, AVERAGE_DIVIDEND_YIELD, AVERAGE_EV_TO_T12M_EBIT, AVERAGE_EV_TO_T12M_SALES,
  AVERAGE_PRICE_EARNINGS_RATIO, AVERAGE_PRICE_TO_BOOK_RATIO, AVERAGE_PRICE_TO_FREE_CASH_FLOW, AVG_EV_TO_T12M_EBITDA,
  CAPEX_ABSOLUTE_VALUE, CASH_AND_MARKETABLE_SECURITIES, CF_CASH_FROM_OPER, DIVIDEND_YIELD, EARN_FOR_COMMON, EQY_FUND_YEAR,
  EV_TO_T12M_EBIT, EV_TO_T12M_EBITDA, EV_TO_T12M_SALES, FCF_MARGIN_AFTER_OPER_LEA_PYMT, FREE_CASH_FLOW_PER_SH,
  HIGH_CLOSING_PRICE_TO_BOOK_RATIO, HIGH_DIVIDEND_YIELD, HIGH_EV_TO_T12M_EBIT, HIGH_EV_TO_T12M_EBITDA, HIGH_EV_TO_T12M_SALES,
  HIGH_PRICE_TO_FREE_CASH_FLOW, HISTORICAL_MARKET_CAP, LOW_CLOSING_PRICE_TO_BOOK_RATIO, LOW_DIVIDEND_YIELD, LOW_EV_TO_T12M_EBIT,
  LOW_EV_TO_T12M_EBITDA, LOW_EV_TO_T12M_SALES, LOW_PRICE_TO_FREE_CASH_FLOW, MINORITY_NONCONTROLLING_INTEREST, NORMALIZED_ROA,
  NORMALIZED_ROE, PX_ERN_RATIO_WITH_HIGH_CLOS_PX, PX_ERN_RATIO_WITH_LOW_CLOS_PX, SHORT_AND_LONG_TERM_DEBT, TANG_BOOK_VAL_PER_SH,
  TOTAL_EQUITY;
- **1 forecast line**, `BEST_CPS` (scope `forecast`, E columns only);
- **4 header facts** (scope `header`): SHORT_NAME, COUNTRY_FULL_NAME, AVG_DAILY_VALUE_TRADED_3M, CRNCY_ADJ_MKT_CAP.

Served units on these figures (measured): `RATIO (dimensionless multiple)`, `MILLIONS`, `PERCENT`, `PER SHARE (local
trading/reporting currency)`, `MILLIONS (share count)`, `TEXT (string field)`, `DATE (ISO yyyy-mm-dd)`, `ABSOLUTE (full currency
units)`.

**The served reasons (measured over all 96 names at the cut: 6,796 fiscal entries, exactly 2 texts):**
- `not dated at the fiscal period end (non-December FYE, fye_join)` -- 6,771 entries. In PM words: the price-dated range is not
  reported at this company's fiscal year end, because its fiscal year does not end in December.
- `empty/no value returned` -- 25 entries. In PM words: Bloomberg returned no value for this line.
A row with NO figure and NO served reason (for example EQY_FUND_YEAR, which landed no value on any name) reads: Bloomberg returned
no value for this line for this company. Any other served text is shown as served, with internal tokens removed; never drop a
reason silently.

**Build, in `modelSheet.ts`, `tabs/ModelTab.tsx` and `types.ts` only:**
1. `buildModelSheet(figures, fiscalYears, servedLineNames, forecastFigures, fiscalUnresolved?, headerFigures?)`. The two new
   optional arguments are `{mnemonic, fiscal_year, reason}[]` and the header figures. Existing callers keep working unchanged.
2. Export `V3_LINES_TITLE` (a title in words). Append ONE group with that title AFTER the two existing groups: exactly one row
   per V3 sheet mnemonic (the 44 fiscal lines + `BEST_CPS`, the latter filling only the E columns from the forecast figures).
   Each row is labelled in words (a label map in the style of `LINE_NAMES`, written from Bloomberg's definitions; never the
   vendor code as the label) and typed from the served unit: `PERCENT` -> `percent`, `RATIO` -> `multiple`, `PER SHARE` ->
   `perShare`, `MILLIONS` / `ABSOLUTE` -> `amount`, anything else -> `other`.
3. A V3 row with no figure in any column carries `absentReason` in PM words, built from that row's served reasons as above.
   An `absentReason` on a V3 row never contains ABSENT, REFUSED, "not read", "mnemonic", fye_join, HELD_OFF or an UPPER_SNAKE
   vendor code.
4. Return `v3Facts`: the 4 header facts, each `{mnemonic, label, value}`, with the label in words and `value` exactly the
   served header figure's value.
5. The two existing groups and their 17 rows do not move: same titles, labels, mnemonics and cells.
6. In `ModelTab.tsx`, pass `data.model?.fiscal_unresolved` and `data.header_figures` to the `buildModelSheet` call(s) that build
   the sheet. Render the V3 group like the existing groups, show each fully-absent V3 row's reason ONCE in words, and render
   `v3Facts` as a short labelled line with the group. In `types.ts`, type `fiscal_unresolved` on the model slice.
7. **Colour law** (`portal/CLAUDE.md`): on the light canvas and on white panels, ink is navy. Never use `text-white*`,
   `text-{color}-100..300` or `bg-white/N` here; reuse the existing groups' classes.

## 2. BOUNDS

1. NO push of any branch, NO deploy, NO AWS call. Typecheck with `bun run typecheck` inside `portal/` (never bare `tsc
   --noEmit`, which checks nothing here).
2. Only the files in `<paths>` change. Never edit the issuer's check, fixture or snapshot.
3. Write code with the Edit/Write tools, never a shell heredoc. ASCII only.
4. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner
   2.0.0_SA_COO~X`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/modelSheet.ts
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/types.ts
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-al-2.model-sheet-v3-rows.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-al-2.model-sheet-v3-rows.md
</paths>

Read-only: the whole repository, in particular `portal/CLAUDE.md`, `portal/DESIGN.md`, the existing
`portal/src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs`, and the issuer's checks, fixture and snapshot under
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round36/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-al-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round36/al2_check.cjs" portal</invocation><expect>(?m)^al2 build 3/3 control 1/1$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-al-2"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs</invocation><expect>(?m)^CHECKS-OK ([0-9]+) of \1$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-al-2" judgment="true"/>
</proof_of_spec>

- AC1 (the real `modelSheet.ts` on the captured BA and 1299 HK payloads): build -- 45 of 45 V3 rows once each on both names;
  every fully-absent V3 row carries a reason in words, and 1299 HK has at least one; the 4 header facts with the served values;
  control -- the 17 existing rows unchanged against the base snapshot.
- AC2: the existing Model-sheet harness still passes on your build (the rendered ModelTab, real react-dom/server). At the base it
  prints `CHECKS-OK 12 of 12`. Its fixture `tabsFixture.BA_US_Equity.json` predates the 52 mnemonics and carries no
  `fiscal_unresolved`, so on it every V3 row is fully absent: the page must render that state cleanly (one reason line, no
  per-row noise), and the harness, the oracle, is never edited.
- AC3 (JUDGMENT, graded by the CVO at L9 on the running page): a PM reads the V3 lines on BA's and 1299 HK's Model tab, and each
  reason reads as plain words. Record it as `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO~Z`; no verdict.

## 5. WHEN YOU ARE DONE

1. Inside `portal/`, run `bun run typecheck`. It reads clean.
2. Write the instance at the proof path, then run `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order
   <this order>` AFTER your final commit. It must return rc 0.
3. Only if every mechanical criterion passes, append a new status tag reading complete at the END of this file, in the SAME
   outer commit as your proof instance.
4. Report ONCE: your label map and type map for the 45 rows, the reason wording you chose for each served text, every criterion's
   output line, the typecheck line, your portal commit hashes and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-35 analysis @`02bbbc0208` s.3 ruling 1 + s.4 item 1. Base portal DEV ec65c5d637: al2_check build 0/3
control 1/1. portal_ref ec65c5d637. A product-file candidate: `1.0.0_SA_CTO~Z` reviews it; the DEV push is on Andrew's word.
<risk>LOCAL</risk>
<status>pending</status>
<round>36</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<status>complete</status>
