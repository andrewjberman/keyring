# TO IRPT_BCKEND.TO-IB-pr-442 -- READ ONLY: the sizing under PRD ADDENDUM v0.39 -- account-days freed when only ADMITTED types are graded by the second witness

<to_id>IRPT_BCKEND.TO-IB-pr-442</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~300</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>139</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msgs 5453 and 5460 and PRD ADDENDUM v0.39 @90bfa5fc4f (its cost bullet; ratified-text half signed by `3.0.0_SA_CVO` @5d8db9acaf) | **Decomp cell:** `IB-pr-442` (decomposition section 131) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-300/` (bash `/c/dev/wk-irpt-bckend-300`). Work only there. READ ONLY toward AWS. ONE external source
only: Yahoo Finance through the reader below, ONE PASS (each ticker asked exactly once, at most 50 a call, calls paced and never in
parallel; a ticker or a call that returns nothing is recorded and never asked again). NO YCharts call, NO Bloomberg call. Nothing
built into the product, nothing served, no claim re-graded in the product: this is a SIZING.

**Why.** Read PRD ADDENDA v0.38 and v0.39 whole first (the last two sections of
`org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`). A second witness of the date basis (the reader's unadjusted Close) may
grade a security the first witness (the Schwab anchor) does not carry, but only if the security's TYPE is admitted. A security's
type is the pair (`SEC Asset Type`, `Share Class Type`) the transactions table states for its CUSIP; a security with exactly ONE
pair over all its transaction rows has that type; one with no transaction row or more than one pair has NO type. v0.39 admits
seven pairs and leaves out the rest. The cost is not known: 58.2 percent of Cottonwood's eligible account-days are blank today
and 382 of 999 accounts are never served. This cell sizes it.

**The seven admitted pairs** (the source's own strings; `RIC/BDC` abbreviates the source's value `Securities Issued by Registered
Investment Companies or Business Development Companies`; read the exact strings from the transactions table, do not retype them
from here): `Exchange-Traded Equity Securities / Not Available`; `RIC/BDC / ETF`; `RIC/BDC / A`; `RIC/BDC / No Load`;
`RIC/BDC / Other`; `RIC/BDC / Retirement`; `RIC/BDC / Inv`. **Left out, by name:** `RIC/BDC / Inst` and `RIC/BDC / Not Available`.
Every other pair, and NO TYPE, is not admitted.

**Your instruments** are all in your worktree (merged): `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~299/`
(the type join by CUSIP from the transactions table, the one-day-off classifier, the one-pass fetch of 948 tickers, the control);
`~296/` (every outside-anchor security graded row by row against the reader's bar for the day and the prior day, the four
account-day outcomes, the sizing script); `~297/`, `~294/`, `~293/`, `~288/`. Copy what you need into YOUR folder; write nothing
into another worker's folder. Keep unchanged: the source and anchor addresses, the price rule (Market Value / Units), the
tolerance (relative 1e-4), the trading-day axis, the one-way digest of the account key, the row kinds, the ordered claim rule with
the v0.36 names, the cash rule in force. The reader: `fetch_yahoo` in
`data/assets/scripts/silver/commonwealth_price_basis_census.py` and `read_yahoo_close` in
`data/assets/scripts/silver/commonwealth_daily_valuation.py`; your own cache `C:/dev/_scratch300/yahoo/`; window 2026-06-05 to
2026-10-13. Scratch is OUTSIDE the worktree and deleted file by file at the end.

**Do, in this order:**

1. **Class every security the first witness does not carry** (the securities behind an `OUTSIDE_ANCHOR` row under the cash rule
   in force; IB-pr-438 counted 737). Each is in exactly ONE class, by this precedence (state it as `class_precedence`):
   `no_ticker_to_ask_with` (the holdings source carries no ticker: the reader cannot be asked, whatever its type);
   then by its type: `no_type_or_mixed`; `left_out_type_inst`; `left_out_type_ric_not_available`;
   `another_type_not_admitted` (any other pair that is not one of the seven; list the pairs and counts);
   then, for an admitted type: `no_bar` (its ticker returned no bar in your pass) or `admitted_type_with_bars`.
   Print `admitted_by_type` (the seven pairs with their security counts, summing to `admitted_type_with_bars`). Ask the reader
   ONLY for securities of an admitted type, plus the fund tickers item 6 needs (that is the pass); say how many tickers that is
   before fetching.
   NOTE the type join's domain: IB-pr-441 joined the 894 securities BOTH witnesses carry; these are the securities the first
   witness does NOT carry, a different set. Join them the same way and print how many find a type.

2. **Grade and place the account-days.** For each security of class `admitted_type_with_bars`, grade each of its rows as
   IB-pr-438 did (the row's mark against the reader's bar for the day and for the prior trading day: day only, both, prior day
   only, neither; a date with no bar is no bar). Every account-day that holds one or more outside-first-witness securities is in
   exactly ONE outcome, the first that applies:
   `holds_a_security_no_witness_may_grade` (any such security not in `admitted_type_with_bars`, or a row on a date with no bar);
   `admitted_but_one_or_more_at_neither`; `admitted_but_one_or_more_at_prior_day_only`;
   `freed_every_security_admitted_and_at_the_day_close`. Also `freed_and_holding_no_other_ungradeable_kind` (no `NO_CUSIP`,
   `NEITHER_CLOSE`, `NEGATIVE_POSITION` row and no sixth-reason row on that account-day).

3. **The sizing** (`sizing_under_v039`): if every freed account-day with no other ungradeable kind took the claim its graded rows
   give (`ACCT_OWN_DATE` unless an anchor-graded row says `ACCT_PRIOR_DATE`), and an account-day whose only obstacle is one or
   more prior-day-only rows read `ACCT_PRIOR_DATE`: the four claim counts, eligible, served, blank, blank share, accounts never
   served. Say exactly that in `what_is_assumed`, and that it is a sizing, not a stamp. Print it beside the rule in force (58.157
   percent; 382 of 999) and, for reference only, the withdrawn sizing that counted every fund (36.989 percent; 181).

4. **What the rest waits on, counts only** (`still_waiting`), for each of: `left_out_type_inst`,
   `left_out_type_ric_not_available`, `no_type_or_mixed`, `another_type_not_admitted`, `no_ticker_to_ask_with`, `no_bar`:
   `account_days_holding_any` (account-days that hold one or more securities of that class; an account-day counts under every
   class it holds) and `account_days_waiting_only_on` (account-days that would be freed if that ONE class were admitted and
   graded at the day's close, everything else unchanged: an upper bound, say so). Name the single fund with no bar that carries
   the most account-days and print them (IB-pr-438 read FPNIX, 12,115).

6. **The reviewer's two points on PRD v0.39** (`reviewer_points`; neither is a condition; both come from IB-pr-441's fund-trade
   table, whose script and inputs are in `~299/`; re-read the transactions table, ask the reader nothing beyond your one pass:
   the funds' bars you need are those of the fund tickers, so include the 103 fund tickers of that table in your one pass):
   - "Next day only" is 0 of 6,149 at the relative tolerance and 3 to the cent. Name those three trades: the fund's ticker,
     the trade date, the transaction kind, the trade price and the three bars beside it (prices of a public fund are not
     client data; no account, no quantity, no amount). `next_day_only_to_the_cent: [{ticker, trade_date, kind, price,
     bar_prior, bar_day, bar_next}]` and `next_day_only_to_the_cent_count`. If your count is not 3, say so and why.
   - The admitted fund pairs `RIC/BDC / Inv`, `RIC/BDC / Retirement` and `RIC/BDC / A` rest on 2, 4 and 6 securities in the
     overlap table. Print how the 6,149 priced fund trades split by the fund's type pair: `trades_by_fund_pair: {<pair>:
     trades}` over EVERY pair present (and `NO_TYPE`/`MIXED` if any), summing to `trades_total`; beside each pair its funds, and
     its six outcomes (same day only, prior day only, next day only, more than one, none, no bar) in `outcomes_by_fund_pair`.
5. **Control** (`control.planted` must equal `control.read`): a planted fixture of three account-days: one holding only an
   admitted-type security at the day's close (it is freed: `admitted_security_at_the_day_close_frees_its_day: true`); one holding
   the same plus a left-out-type security at the day's close (not freed: `left_out_type_does_not_free_its_day: true`); one
   holding an admitted security at the prior day's close.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~300/`: `IB139-1_sizing_under_v039.json` with
`{same_account_days_read, admitted_types:[the seven pairs as the source writes them], class_precedence,
securities_outside_the_first_witness:{total, admitted_type_with_bars, left_out_type_inst, left_out_type_ric_not_available,
no_type_or_mixed, another_type_not_admitted, no_ticker_to_ask_with, no_bar}, admitted_by_type:{...}, other_pairs_not_admitted:{...},
type_join:{found_one_pair, found_no_row, found_more_than_one_pair}, fetch:{calls:[{tickers}], distinct_tickers_asked,
tickers_asked_more_than_once:0}, account_day_effect:{account_days_holding_such_a_security,
holds_a_security_no_witness_may_grade, admitted_but_one_or_more_at_neither, admitted_but_one_or_more_at_prior_day_only,
freed_every_security_admitted_and_at_the_day_close, freed_and_holding_no_other_ungradeable_kind},
sizing_under_v039:{what_is_assumed, account_days:{present, UNGRADEABLE, ACCT_PRIOR_DATE, ACCT_OWN_DATE, NOTHING_TO_GRADE},
serving_rule:{eligible, served, blank, blank_share_percent, accounts_never_served}}, still_waiting:{account_days_holding_any:{...},
account_days_waiting_only_on:{...}, largest_no_bar_fund:{ticker, account_days}}, reviewer_points:{next_day_only_to_the_cent, next_day_only_to_the_cent_count, trades_total, trades_by_fund_pair,
outcomes_by_fund_pair}, control:{planted, read}, claims_regraded_in_product:false, other_sources_asked:0}`; and a one-page
`IB139-1_SIZING_UNDER_V039_READ.md`.
`same_account_days_read` is true only if your totals under the cash rule equal IB-pr-438's (UNGRADEABLE 43,310; ACCT_PRIOR_DATE
55; ACCT_OWN_DATE 19,832; NOTHING_TO_GRADE 13,599; present 76,796); otherwise explain in `source_difference_explained` and file
a row. Counts only: no account id, no balance, no single account's holding.

<criterion id="IB139-1-AC1" cell_refs="IB-pr-442"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r139/p139_cells.py" . IB139-1-AC1</invocation><expect>IB139-1-AC1 PASS</expect></criterion>
<criterion id="IB139-1-AC2" cell_refs="IB-pr-442"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r139/p139_cells.py" . IB139-1-AC2</invocation><expect>IB139-1-AC2 PASS</expect></criterion>
<criterion id="IB139-1-AC3" cell_refs="IB-pr-442"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r139/p139_cells.py" . IB139-1-AC3</invocation><expect>IB139-1-AC3 PASS</expect></criterion>

<expected_criteria>IB139-1-AC1, IB139-1-AC2, IB139-1-AC3</expected_criteria>

The checks grade sums, the seven-pair list's length, that each waiting-only count is not above its holding-any count, the
one-pass bound and the control. Every count is UNMEASURED by the issuer.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file, no PRD, no `sources.json`, no gold script, no ADVI_COTBKF file.
- **Refusal clause:** a whole fetch call that fails is recorded, not repeated. If one of the seven pairs' exact strings is not
  found in the transactions table as the addendum abbreviates it, STOP on that pair, say which string you did find, and file a
  row; do not match by resemblance. If a criterion cannot be met as written, stop, file a row and report. Never weaken a check;
  do not edit `p139_cells.py`. Do not make a number fit.
- **Row ids** are `IRPT_BCKEND-D2-W300-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's existing line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~300" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~300@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~300 <0.9.0_WK_IRPT_BCKEND~300@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push. Write no firm name as a literal in any file, and no token beginning `z09` in the two outputs.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~300/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-442.sizing-under-the-admitted-types.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 131 (round 139, workstream ~P), cell `IB-pr-442`.
<owned_cells>IB-pr-442</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB139-1-AC1, IB139-1-AC2, IB139-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~300/IRPT_BCKEND.TO-IB-pr-442.sizing-under-the-admitted-types.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the seven classes with their counts and the admitted securities per pair; the type join over
this set; the number of fetch calls and tickers; the four account-day outcomes and the freed count; the sizing beside 58.157
percent and 382 of 999 (and the withdrawn 36.989 and 181 for reference); what the rest waits on, both ways, per class, and the
largest no-bar fund; the three to-the-cent next-day trades by fund and date; the trades per fund pair; the control; each criterion's last line; the proof checker's result; scratch deleted; commit hashes; any
row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read-only sizing written to the worker's own deliverables folder; no product file, route, function or served byte.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission change; S3 reads and public market-data fetches through a reader the estate already runs.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p139_cells.py dry-run at base box/dell2 on dell2 2026-10-11: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. Issued only after IB-pr-441 merged and its three criteria and proof were re-run by the issuer at box HEAD (the addendum: nothing is cut before that record is on the trunk and its numbers are read there unchanged), and after the ratified-text half on v0.39 was signed. Every count is unmeasured by the issuer.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only). Egress: Yahoo Finance through ADVI_COTBKF's existing reader, one pass over the admitted-type securities only.
</preflight>
