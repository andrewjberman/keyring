# TO IRPT_BCKEND.TO-IB-pr-436 -- READ ONLY: nine mutual funds by 85 days, an independent daily NAV against the custodian's mark

<to_id>IRPT_BCKEND.TO-IB-pr-436</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~294</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>134</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5157 (ruling on IB-pr-435's read); reader named by `2.0.0_SA_COO~C2` msg 5159 | **Decomp cell:** `IB-pr-436` (decomposition section 126) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-294/` (bash `/c/dev/wk-irpt-bckend-294`). Work only there. READ ONLY toward AWS (S3 reads through
`.tools/aws`); nothing built into the product; nothing served. ONE external source is permitted and only one: Yahoo Finance, through
the reader named below. NO YCharts call of any kind and NO Bloomberg call (the issuer made the three gateway calls the CTO allowed on
2026-10-11: the time-series tool answered 403 twice and the fund-series tool 400 once; source one is closed for funds and is not to be tried again by this cell).

**Why.** Under PRD ADDENDUM v0.35/v0.36 an account-day holding one priced security the instrument cannot place at a close is
`UNGRADEABLE` and blank: 58.2 percent of Cottonwood's eligible account-days. IB-pr-435 found that nine mutual funds carry half of
it, and that the estate holds no independent close for them: only the custodian's own mark. The CTO ruled the custodian's mark
cannot grade itself, and that a mutual fund is exactly the case the date basis exists for: one NAV a day, struck after the close,
so a positions file can carry yesterday's. An independent NAV answers it per fund-day. This cell reads it; it re-grades nothing.

**The nine funds:** FLCOX, MFEIX, CEMIX, FSGGX, FSMAX, FXNAX, FSPGX, CDSIX, FPNIX. Their CUSIPs are in IB-pr-435's ranking.

**Your instruments are on other branches.** Read them with `MSYS_NO_PATHCONV=1 git show <branch>:<path>` (run a positive control
beside any "absent" reading) and copy what you need into YOUR folder; write nothing into another worker's folder.
- `wk-IRPT_BCKEND-293` (commit 497c7628fd), folder `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~293/`: the
  fetch and claim scripts as last extended, `IB133-1_outside_anchor_coverage.json` (the ranking with each security's CUSIP and
  ticker), `IB133-1_OUTSIDE_ANCHOR_COVERAGE_READ.md`.
- If the merged tree already holds `deliverables/0.9.0_WK_IRPT_BCKEND~288/` or `~293/`, the files there are the same; either is fine.
Keep unchanged: the source address, the price rule (Market Value / Units), the tolerance, the trading-day axis
(`lib/trading_calendar.py`), the one-way digest of the account key. Scratch goes OUTSIDE the worktree in `C:/dev/_scratch294/` and
is deleted file by file at the end.

**The NAV reader (ADVI_COTBKF's, do not write a new one).** Fetch: `data/assets/scripts/silver/commonwealth_price_basis_census.py`,
`fetch_yahoo(tickers, start, end, cache_dir)` (about line 200: `yfinance.download`, at most 50 tickers a call, `auto_adjust=False`,
one cache file per ticker). Read: `data/assets/scripts/silver/commonwealth_daily_valuation.py`, `read_yahoo_close(cache_dir, ticker)`
(about line 227; it returns the UNADJUSTED Close). Use your OWN cache directory under `C:/dev/_scratch294/yahoo/`; do not write into
ADVI_COTBKF's cache (`<root>/.scratch/advi_cotbkf/yahoo_census`), though you may READ it first and say what it already holds for
the nine. ONE fetch call for the nine funds plus the control security, window 2026-06-08 to 2026-10-10; if it fails or returns
nothing for a fund, do not loop: record `no_nav_found` for that fund's days, say what the call returned, and file a row. If
`yfinance` is not importable on this box, STOP and file a row; do not install anything.

**Count, for each fund and each trading day in 2026-06-10 to 2026-10-09 on which any Cottonwood account holds it with a priced row:**
- the custodian's MARK that day: Market Value / Units of the fund's rows in that day's partition. If the accounts' marks for one
  fund-day differ beyond the tolerance, say how you chose (state `many_marks_rule`; the natural rule is the mark held by the most
  rows, with `fund_days_with_more_than_one_mark` counted);
- the independent NAV of that day and of the prior trading day;
- exactly one outcome per fund-day: `equals_day_nav_only`, `equals_prior_day_nav_only`, `equals_both_nav_unchanged` (the NAV did
  not move between the two days, so the mark cannot say which), `equals_neither`, `no_nav_found`.
The comparison tolerance: the instrument's own relative tolerance, and ALSO report how many `equals_neither` fund-days are within
one cent of either NAV (a fund NAV is quoted to the cent; a mark derived from a rounded Market Value can sit a fraction off).
State both; the five outcomes use the instrument's tolerance unless you show it cannot work for cent-quoted NAVs, in which case
say so, use the one-cent rule, and print the count under each.

**Is Yahoo's fund Close the NAV of that day?** `2.0.0_SA_COO~C2` did not establish it. Answer it with what you can measure: for a
fund on a day its NAV moved, does the date Yahoo attaches to a value agree with the date a second public statement of the fund's
NAV would attach? You have no second source by bound, so: state the claim as `inferred` or `absent`, and give the internal
evidence you do have (for example whether, on days the custodian's mark equals exactly one of the two NAVs, the split between
"day" and "prior day" is stable across funds and accounts, or flips by day in a way that tracks the partition's landing time).
Put the answer and its claim in `is_fund_close_the_nav_of_that_day: {answer, claim, evidence}`.

**Control.** Pick ONE security the Schwab anchor DOES carry on every day (an exchange-traded fund or stock held by Cottonwood
accounts; name it), fetch it in the same call, and compare the reader's Close with the anchor's `closing_price` on every trading
day in the window: `control: {security, carried_by_anchor: true, days_compared, days_equal, difference_explained}`. This shows the
reader, the date alignment and the tolerance on a case where the answer is known.

**The account-day effect (an upper bound; nothing is re-graded).** Of the account-days whose ONLY outside-anchor rows are among
these nine funds: on how many does every such fund's mark equal the day's NAV (or both), on how many does one or more equal only
the prior day's, on how many is one or more `equals_neither` or `no_nav_found`; and of the first group, how many hold no other
ungradeable kind. `claims_regraded: false`.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~294/`: `IB134-1_fund_nav_basis.json` with
`{funds:[{ticker, cusip, fund_days_with_a_mark, fund_days_with_more_than_one_mark, nav_days_needed, nav_days_found,
equals_day_nav_only, equals_prior_day_nav_only, equals_both_nav_unchanged, equals_neither, no_nav_found,
equals_neither_within_one_cent}], totals:{the five outcomes summed over the nine}, many_marks_rule, tolerance,
nav_source:{name, read_by, adjusted:false, first_date, last_date, cache_already_held}, is_fund_close_the_nav_of_that_day,
by_day:{<date>: {day, prior, both, neither, none}}, control, account_day_effect:{
account_days_whose_only_outside_anchor_rows_are_these_funds, every_mark_equals_day_nav_or_both,
one_or_more_equals_prior_day_only, one_or_more_neither_or_no_nav, of_those_holding_no_other_ungradeable_kind},
claims_regraded:false}`; and a one-page `IB134-1_FUND_NAV_BASIS_READ.md`: a nine-row table of the five outcomes; whether the
prior-day marks cluster on particular days or particular funds (read `by_day`); the control; the account-day effect; what was not
measured. Counts only: no account id, no balance, no single account's holding.

<criterion id="IB134-1-AC1" cell_refs="IB-pr-436"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r134/p134_cells.py" . IB134-1-AC1</invocation><expect>IB134-1-AC1 PASS</expect></criterion>
<criterion id="IB134-1-AC2" cell_refs="IB-pr-436"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r134/p134_cells.py" . IB134-1-AC2</invocation><expect>IB134-1-AC2 PASS</expect></criterion>
<criterion id="IB134-1-AC3" cell_refs="IB-pr-436"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r134/p134_cells.py" . IB134-1-AC3</invocation><expect>IB134-1-AC3 PASS</expect></criterion>

<expected_criteria>IB134-1-AC1, IB134-1-AC2, IB134-1-AC3</expected_criteria>

The checks grade the fund set, the sums and the control's shape (at least 20 days compared; if fewer than nine in ten are equal,
`difference_explained` is required). Every count is UNMEASURED by the issuer.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file, no PRD, no `sources.json`, no gold script, no ADVI_COTBKF file.
- **Refusal clause:** if the reader cannot return a fund's NAV, record it; do not try another source. If a criterion cannot be met
  as written, stop, file a row and report. Never weaken a check; do not edit `p134_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W294-S<k>` (the worker form; the row gate refuses the bare form from a worker); `surfaced_at` is
  `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or `INFERRED`; append only, keeping the channel file's existing
  line endings byte for byte; check the id is free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~294" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~294@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~294 <0.9.0_WK_IRPT_BCKEND~294@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push. Write no firm name as a literal in any file (the naming gate refuses it); take a firm key from the modules' own lookup at run time.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~294/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-436.nine-funds-independent-nav-against-the-custodian-mark.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 126 (round 134, workstream ~P), cell `IB-pr-436`.
<owned_cells>IB-pr-436</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB134-1-AC1, IB134-1-AC2, IB134-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~294/IRPT_BCKEND.TO-IB-pr-436.nine-funds-independent-nav-against-the-custodian-mark.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the nine-row table; the totals; whether prior-day marks cluster by day or by fund; the answer
and claim on whether the reader's fund Close is that day's NAV; the control; the account-day effect; what the one fetch returned;
each criterion's last line; the proof checker's result; scratch deleted; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read-only count written to the worker's own deliverables folder; no product file, route, function or served byte.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission change; S3 reads and one public market-data fetch through a reader the estate already runs.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p134_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~14:5xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. Not measured by the issuer: that the reader returns these nine funds, and that its fund Close is the NAV of its date; each is a named stop or a claim on the face. Measured by the issuer: ycharts_time_series returned 403 twice and, on the CTO's one further call (msg 5161), ycharts_fund_series returned 400 for FLCOX; source one is closed for funds. yfinance 1.2.0 imports on this box.
lane: the <paths> block IS the grant: the worker's own folder, the channel, the order. DIRECT-ACT (one read-only cell, LOCAL: records only). Egress: Yahoo Finance through ADVI_COTBKF's existing reader; no vendor needing a per-use word.
</preflight>
