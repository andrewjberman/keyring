# TO IRPT_BCKEND.TO-IB-pr-438 -- READ ONLY: the same reader over ALL the securities the anchor does not carry, one pass, and the ACCOUNT-DAYS freed

<to_id>IRPT_BCKEND.TO-IB-pr-438</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~296</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>136</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5211 (ruling on IB-pr-436's read) | **Decomp cell:** `IB-pr-438` (decomposition section 128) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-296/` (bash `/c/dev/wk-irpt-bckend-296`). Work only there. READ ONLY toward AWS (S3 reads through
`.tools/aws` and the inherited scripts' own calls). ONE external source and only one: Yahoo Finance through the reader below, ONE
PASS: every ticker is asked exactly once; a ticker that returns nothing is recorded, never asked again, and no other source is
tried. NO YCharts call, NO Bloomberg call. Nothing is built into the product, nothing served, no claim re-graded in the product.

**Why.** Under PRD ADDENDUM v0.35/v0.36 an account-day that holds one priced security the instrument cannot place at a close is
`UNGRADEABLE` and blank: 58.2 percent of Cottonwood's eligible account-days, 382 of 999 accounts never served. IB-pr-435 found 734
securities behind `OUTSIDE_ANCHOR`. IB-pr-436 read an independent daily NAV for nine of them: on eight funds the custodian's mark
equals the DAY's NAV on every fund-day measured and the prior day's on none. But those nine free only 563 account-days, because an
account-day is freed only when EVERY security it holds is graded. The CTO ruled the unit is the account-day, and this cell sizes
it over all 734, once. Whether an unofficial reader may be a production anchor is a PRD question the CTO rules on this cell's
table, not before.

**Your instruments.** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~288/` and `~293/` are in your worktree
(merged). IB-pr-436's folder `.../0.9.0_WK_IRPT_BCKEND~294/` is on branch `wk-IRPT_BCKEND-294` (commit d1adf5102e) and may or may
not be in your worktree's files: if absent, read it with `MSYS_NO_PATHCONV=1 git show wk-IRPT_BCKEND-294:<path>` (list with
`git ls-tree --name-only wk-IRPT_BCKEND-294 "<folder>/"`; run a positive control beside any "absent" reading). It holds the
measure script that compares a mark with the NAV of the day and of the prior trading day, the row-level grading, the control and
`IB134-1_fund_nav_basis.json`. `~293/IB133-1_outside_anchor_coverage.json` holds the ranking: each security's CUSIP, its ticker
where the source carries one, and its account-days. Copy what you need into YOUR folder; write nothing into another worker's
folder. Keep unchanged: the source address, the price rule (Market Value / Units), the tolerance, the trading-day axis, the
one-way digest of the account key, the row-kind definitions, the ordered claim rule with the v0.36 names, and the CASH RULE in
force (a cash-flagged priced row outside the anchor is cash only where its own price is equal on the day and the prior trading
day; a row that cannot be compared is `OUTSIDE_ANCHOR`). Scratch goes OUTSIDE the worktree in `C:/dev/_scratch296/` and is
deleted file by file at the end.

**The reader (ADVI_COTBKF's; do not write a new one).** Fetch: `data/assets/scripts/silver/commonwealth_price_basis_census.py`,
`fetch_yahoo(tickers, start, end, cache_dir)` (at most 50 tickers a call, `auto_adjust=False`, one cache file per ticker). Read:
`data/assets/scripts/silver/commonwealth_daily_valuation.py`, `read_yahoo_close(cache_dir, ticker)` (unadjusted Close). Your own
cache directory: `C:/dev/_scratch296/yahoo/`. Window 2026-06-08 to 2026-10-10. The nine funds of IB-pr-436 are asked again in this
one pass with the rest (your cache is new); FPNIX returned no data there and is NOT asked a second time WITHIN this pass.

**Do, in this order:**
1. **The securities.** Every security behind an `OUTSIDE_ANCHOR` row under the cash rule in force (IB-pr-435 counted 734 before
   the cash rule's three additions; count yours and say which basis). Each is in exactly one class: `no_ticker_to_ask_with` (the
   source carries no ticker for it and the reader keys by ticker; do not invent or look up a ticker: a CUSIP-only bond stays
   unasked, and say how many account-days such securities sit on), `asked_data_returned`, `asked_no_data`. Record every fetch
   call with its ticker count; list every asked security that returned no data, by ticker and name.
2. **Grade each row** of each security that returned data, as IB-pr-436 did: the row's own mark against the NAV of the day and
   of the prior trading day: day only, prior day only, both (NAV unchanged), neither; a date with no bar is no NAV.
3. **The account-days.** Every account-day that holds one or more outside-anchor rows is in exactly ONE outcome, the first that
   applies in this order: `one_or_more_with_no_nav` (it holds an outside-anchor security with no ticker, no data, or no bar on a
   needed date), `one_or_more_at_neither`, `one_or_more_at_prior_day_nav_only`, `every_security_at_day_nav_or_unchanged`. The last
   is the FREED set. Also `freed_and_holding_no_other_ungradeable_kind` (no `NO_CUSIP`, `NEITHER_CLOSE`, `NEGATIVE_POSITION` row
   and no sixth-reason row on that account-day).
4. **The sizing under v0.36** (`sizing_under_v036`): IF every freed account-day with no other ungradeable kind took the claim its
   graded rows give (its anchor-graded rows by the anchor as today, its outside-anchor rows at the day's NAV: so `ACCT_OWN_DATE`
   unless an anchor-graded row says `ACCT_PRIOR_DATE`), and an account-day with a prior-day-only row and nothing worse read
   `ACCT_PRIOR_DATE`, what are the four claim counts, and the serving rule's eligible, served, blank, blank share and accounts
   never served. Say in `what_is_assumed` exactly that sentence and that it is a sizing, not a claim anybody stamped. Print it
   beside the rule in force (58.2 percent; 382 of 999).
5. **The prior-day rows.** IB-pr-436 found 497 rows of the nine funds equal only to the prior day's NAV, on 33 of 85 days. Over
   all securities with data: how many rows, on how many days, and HOW MANY ACCOUNT-DAYS THEY BLANK (account-days whose only
   obstacle to being freed is one or more prior-day-only rows). Say whether the days cluster (by date, by security family, by the
   partition's landing time IB-pr-429 read) or do not.
6. **Control:** one security the Schwab anchor carries every day (IB-pr-436 used VTI): the reader's Close against the anchor's
   `closing_price` over the window.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~296/`: `IB136-1_all_securities_nav_effect.json`
with `{same_account_days_read, securities:{total, no_ticker_to_ask_with, asked_data_returned, asked_no_data,
account_days_touched_by_no_ticker_securities}, fetch:{calls:[{tickers}], distinct_tickers_asked, tickers_asked_more_than_once:0},
no_data_securities:[{ticker, name, account_days_carried}], account_day_effect:{account_days_holding_an_outside_anchor_row,
one_or_more_with_no_nav, one_or_more_at_neither, one_or_more_at_prior_day_nav_only, every_security_at_day_nav_or_unchanged,
freed_and_holding_no_other_ungradeable_kind}, sizing_under_v036:{what_is_assumed, account_days:{present, UNGRADEABLE,
ACCT_PRIOR_DATE, ACCT_OWN_DATE, NOTHING_TO_GRADE}, serving_rule:{eligible, served, blank, blank_share_percent,
accounts_never_served}}, prior_day_rows:{rows_with_a_nav, rows_equal_only_to_prior_day_nav, rows_equal_neither, days_they_fall_on,
account_days_they_blank, clustering}, control:{security, carried_by_anchor, days_compared, days_equal, difference_explained},
claims_regraded_in_product:false, other_sources_asked:0}`; and a one-page `IB136-1_ALL_SECURITIES_NAV_EFFECT_READ.md`.
`same_account_days_read` is true only if your v0.35/cash-rule totals equal IB-pr-435's (`~293` json: claims UNGRADEABLE 43,310;
ACCT_PRIOR_DATE 55; ACCT_OWN_DATE 19,832; NOTHING_TO_GRADE 13,599; present 76,796); otherwise explain in
`source_difference_explained` and file a row. Counts only: no account id, no balance, no single account's holding.

<criterion id="IB136-1-AC1" cell_refs="IB-pr-438"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r136/p136_cells.py" . IB136-1-AC1</invocation><expect>IB136-1-AC1 PASS</expect></criterion>
<criterion id="IB136-1-AC2" cell_refs="IB-pr-438"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r136/p136_cells.py" . IB136-1-AC2</invocation><expect>IB136-1-AC2 PASS</expect></criterion>
<criterion id="IB136-1-AC3" cell_refs="IB-pr-438"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r136/p136_cells.py" . IB136-1-AC3</invocation><expect>IB136-1-AC3 PASS</expect></criterion>

<expected_criteria>IB136-1-AC1, IB136-1-AC2, IB136-1-AC3</expected_criteria>

The checks grade sums, the one-pass bound (the calls' ticker counts sum to the distinct tickers asked; none asked twice; no call
over 50) and the control's shape. Every count is UNMEASURED by the issuer.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file, no PRD, no `sources.json`, no gold script, no ADVI_COTBKF file.
- **Refusal clause:** if the reader fails for a whole call (not one ticker), record what it returned, do NOT repeat the call, mark
  those tickers `asked_no_data`, file a row and go on. If a criterion cannot be met as written, stop, file a row and report.
  Never weaken a check; do not edit `p136_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W296-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's existing line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~296" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~296@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~296 <0.9.0_WK_IRPT_BCKEND~296@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push. Write no firm name as a literal in any file.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~296/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-438.all-outside-anchor-securities-one-pass-and-the-account-days-freed.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 128 (round 136, workstream ~P), cell `IB-pr-438`.
<owned_cells>IB-pr-438</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB136-1-AC1, IB136-1-AC2, IB136-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~296/IRPT_BCKEND.TO-IB-pr-438.all-outside-anchor-securities-one-pass-and-the-account-days-freed.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the securities' three classes and the account-days the no-ticker ones touch; the no-data
securities by name; the four account-day outcomes and the freed count; the sizing beside 58.2 percent and 382 of 999; the
prior-day rows, the account-days they blank and whether they cluster; the control; the number of fetch calls; each criterion's
last line; the proof checker's result; scratch deleted; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read-only sizing written to the worker's own deliverables folder; no product file, route, function or served byte.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission change; S3 reads and public market-data fetches through a reader the estate already runs.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p136_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~15:2xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The bound figures (734 securities; 76,796 present) are earlier cells' and bind only when the same account-days are read. Not measured by the issuer: how many of the 734 carry a ticker, how the reader behaves on about 700 tickers in about 15 calls, and whether its Close is a NAV of its date for non-fund securities; each is a class, a refusal clause or a claim on the face.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only). Egress: Yahoo Finance through ADVI_COTBKF's existing reader, one pass; no vendor needing a per-use word.
</preflight>
