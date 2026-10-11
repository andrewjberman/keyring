# TO IRPT_BCKEND.TO-IB-pr-439 -- READ ONLY: the source's instrument type; both witnesses compared per type; the sizing under PRD v0.38; a count of priced fund transactions

<to_id>IRPT_BCKEND.TO-IB-pr-439</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~297</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>137</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5298, under PRD ADDENDUM v0.38 @83f1d66bd8 (ratified-text half signed by `3.0.0_SA_CVO` @8ae7b1a563) | **Decomp cell:** `IB-pr-439` (decomposition section 129) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-297/` (bash `/c/dev/wk-irpt-bckend-297`). Work only there. READ ONLY toward AWS. ONE external source
only: Yahoo Finance through the reader below, ONE PASS (each ticker asked exactly once, at most 50 a call, calls paced and never in
parallel; a ticker or a call that returns nothing is recorded and never asked again). NO YCharts call, NO Bloomberg call. Nothing
built into the product, nothing served, no claim re-graded in the product.

**Why.** Read PRD ADDENDUM v0.38 whole first: it is the LAST section of
`org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`. In short: a WITNESS is an independent close for one security on one date,
used only to decide whether an account-day is served or blank; there are two, `SCHWAB_ANCHOR` and `YAHOO_CLOSE` (the reader's
unadjusted Close). A witness can be wrong in price (that blanks a day) or in its DATE LABEL (that passes days systematically). So
`YAHOO_CLOSE` may grade only a class of security whose date labels have been measured; today one class is admitted,
`EXCHANGE_TRADED`, on thin evidence: one security, equal on 85 of 85 days. Mutual funds are NOT admitted. The earlier sizing (blank
37.0 percent) is withdrawn. This cell widens the evidence, states the class field, and re-sizes.

**Your instruments** are in your worktree (merged): `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~288/`
(claims), `~293/` (ranking, cash rule), `~294/` (mark against the reader's bar of the day and the prior day; the control),
`~296/` (all securities, the account-day outcomes, the sizing script; `IB136-1_all_securities_nav_effect.json`). Copy what you need
into YOUR folder; write nothing into another worker's folder. Keep unchanged: the source and anchor addresses, the price rule, the
tolerance (relative 1e-4), the trading-day axis, the one-way digest of the account key, the row kinds, the ordered claim rule with
the v0.36 names, the cash rule in force. The reader: `fetch_yahoo` in `data/assets/scripts/silver/commonwealth_price_basis_census.py`
and `read_yahoo_close` in `data/assets/scripts/silver/commonwealth_daily_valuation.py`, used as `~296` used them; your own cache
`C:/dev/_scratch297/yahoo/`; window 2026-06-08 to 2026-10-10. Scratch is OUTSIDE the worktree and deleted file by file at the end.

**Do, in this order:**

1. **The instrument-type field.** Does Cottonwood's silver holdings source carry a field that states what KIND of instrument a row
   is? Read the partition's column list (record every column name read, `columns_read`), name the field, and give its distinct
   values with row counts over the 85 partitions (summing to the rows read). A cash-equivalent flag alone is not an instrument
   type. If more than one column could serve, name each (`candidates_examined`) and say which is the type field and why. **If
   there is none: say so, set `stopped_no_type_field: true`, draw NO overlap table, and go straight to the sizing (with no class
   admitted, which is the rule in force) and to item 4.** Do not invent a type from names or tickers.

2. **Both witnesses, per type.** The securities both witnesses carry: held by a Cottonwood account in the window, carried by the
   Schwab anchor (`closing_price` by CUSIP), and with a ticker in the source to ask the reader with. Say how many securities that
   is before you fetch; if it is more than 1,500 tickers, STOP before fetching, report the number and file a row (the pass would
   be more than 30 calls and the CTO decides that). For each such security and each trading day in the window: the reader's bar
   for day t against the anchor's close for day t:
   - `equal`: they are equal within the tolerance;
   - `one_day_off`: not equal for day t, and the reader's bar for day t equals the anchor's close for the prior OR the next
     trading day;
   - `neither`;
   - `no_bar`: the reader has no bar for that date.
   Per instrument type (the value of the field of item 1 for that security; a security whose rows carry more than one value goes
   under `MIXED`): `securities`, `security_days`, and the four counts summing to `security_days`. Also, per type,
   `equal_on_days_the_close_moved`: the `equal` days on which the anchor's close differs from its prior day's (only those days
   can tell a correct date label from a shifted one), and `securities_with_any_one_day_off`. State `one_day_off_rule` and
   `unchanged_price_rule` in words. List `types_with_an_empty_one_day_off_column`: the types with `one_day_off` 0 and `equal`
   above 0. The reviewer's test, which is the point of the table: a class is safe when the one-day-off column is EMPTY across
   it, not when the equal column is large. For every type whose column is NOT empty, list the securities and dates behind it
   (up to 50 lines; tickers and dates are not client data).

3. **The sizing under v0.38** (`sizing_under_v038`). `SCHWAB_ANCHOR` grades every security it carries, as today. `YAHOO_CLOSE`
   grades a security the anchor does NOT carry only if its instrument type is in `classes_admitted`. MUTUAL FUNDS ARE NOT
   ADMITTED, whatever their column reads. `classes_admitted` is, for this sizing: the source's type values that are exchange-
   traded securities (stocks, exchange-traded funds; say which values you took and why) AND whose one-day-off column is empty in
   item 2. State that sentence in `what_is_assumed` and that it is a sizing the CTO rules on, not a stamp. Print the four claim
   counts, eligible, served, blank, blank share and accounts never served; beside them the rule in force (58.2 percent; 382 of
   999) and, for reference only, the withdrawn figure's basis (funds counted as graded: 37.0 percent). If no type field exists,
   `classes_admitted` is empty and the sizing equals the rule in force: print it and say so.
   Also print `fpnix_account_days`: the account-days the one fund with no data touches (the CTO ruled it is stated beside the
   blank share wherever that is shown).

4. **Fund transactions, counts only** (`fund_transactions`). The check that would admit mutual funds needs fund-dates on which
   the custodian executed a purchase or redemption at a price. Find Cottonwood's transactions in the estate: list the silver
   tables beside the holdings table (the holdings prefix comes from the instrument's own resolver; list its PARENT, one level,
   through `.tools/aws`; if a listing is denied by a hook, append `# rail-checked: IB-pr-439 lists one named silver prefix`), and
   read `data/assets/scripts/silver/commonwealth_daily_valuation.py` for the transaction source ADVI_COTBKF reads. If a
   transactions table exists: its name, first and last date, how many (fund, date) pairs carry a purchase or redemption with a
   price (`fund_dates_with_a_priced_purchase_or_redemption`), how many distinct funds, and how many of those pairs fall inside
   the 85 days. A "fund" here is a security of the mutual-fund type of item 1 (or, with no type field, one of the nine funds of
   IB-pr-436; say which basis). If none is found: `source_found: false` and `where_looked`. Do NOT compare any transaction price
   with any bar in this cell: counts only.

5. **Control** (`control.planted` must equal `control.read`): a small planted fixture of two witnesses over five days with one
   security whose reader series is shifted by one day and one that is not: the shifted one must read `one_day_off` on the days its
   price moved and the other `equal`.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~297/`: `IB137-1_witness_overlap_by_type.json` with
`{same_account_days_read, instrument_type_field:{present, name, values, rows_read, columns_read, candidates_examined},
stopped_no_type_field, securities_both_witnesses_carry, fetch:{calls:[{tickers}], distinct_tickers_asked,
tickers_asked_more_than_once:0}, overlap_by_type:{<type>:{securities, security_days, equal, one_day_off, neither, no_bar,
equal_on_days_the_close_moved, securities_with_any_one_day_off}}, one_day_off_rule, unchanged_price_rule,
types_with_an_empty_one_day_off_column, one_day_off_detail, sizing_under_v038:{what_is_assumed, classes_admitted,
mutual_funds_admitted:false, account_days:{present, UNGRADEABLE, ACCT_PRIOR_DATE, ACCT_OWN_DATE, NOTHING_TO_GRADE},
serving_rule:{eligible, served, blank, blank_share_percent, accounts_never_served}, fpnix_account_days}, fund_transactions:{...},
control:{planted, read}, claims_regraded_in_product:false, other_sources_asked:0}`; and a one-page
`IB137-1_WITNESS_OVERLAP_BY_TYPE_READ.md`. `same_account_days_read` is true only if your totals under the cash rule equal
IB-pr-438's (UNGRADEABLE 43,310; ACCT_PRIOR_DATE 55; ACCT_OWN_DATE 19,832; NOTHING_TO_GRADE 13,599; present 76,796); otherwise
explain in `source_difference_explained` and file a row. Counts only: no account id, no balance, no single account's holding.

<criterion id="IB137-1-AC1" cell_refs="IB-pr-439"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r137/p137_cells.py" . IB137-1-AC1</invocation><expect>IB137-1-AC1 PASS</expect></criterion>
<criterion id="IB137-1-AC2" cell_refs="IB-pr-439"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r137/p137_cells.py" . IB137-1-AC2</invocation><expect>IB137-1-AC2 PASS</expect></criterion>
<criterion id="IB137-1-AC3" cell_refs="IB-pr-439"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r137/p137_cells.py" . IB137-1-AC3</invocation><expect>IB137-1-AC3 PASS</expect></criterion>

<expected_criteria>IB137-1-AC1, IB137-1-AC2, IB137-1-AC3</expected_criteria>

The checks grade BOTH branches of item 1 (a type field exists, or none does), the sums, the one-pass bound, that the listed types
with an empty one-day-off column are exactly those the table shows, and the control. Every count is UNMEASURED by the issuer.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file, no PRD, no `sources.json`, no gold script, no ADVI_COTBKF file.
- **Refusal clause:** the 1,500-ticker stop of item 2; a whole fetch call that fails is recorded, not repeated. If a criterion
  cannot be met as written, stop, file a row and report. Never weaken a check; do not edit `p137_cells.py`. Do not make a number
  fit: the one-day-off column is what the data says.
- **Row ids** are `IRPT_BCKEND-D2-W297-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's existing line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~297" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~297@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~297 <0.9.0_WK_IRPT_BCKEND~297@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push. Write no firm name as a literal in any file.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~297/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-439.witness-overlap-by-instrument-type-and-resizing.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 129 (round 137, workstream ~P), cell `IB-pr-439`.
<owned_cells>IB-pr-439</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB137-1-AC1, IB137-1-AC2, IB137-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~297/IRPT_BCKEND.TO-IB-pr-439.witness-overlap-by-instrument-type-and-resizing.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the type field and its values with counts (or that none exists); the number of securities
both witnesses carry and the number of fetch calls; the per-type table with the one-day-off column, and for every non-empty
type the securities and dates behind it; the sizing beside 58.2 percent and 382 of 999, with the classes you admitted and why,
and FPNIX's account-days; the fund-transaction counts and window, or where you looked; the control; each criterion's last line;
the proof checker's result; scratch deleted; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read-only measurement written to the worker's own deliverables folder; no product file, route, function or served byte.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission change; S3 reads and public market-data fetches through a reader the estate already runs.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p137_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~16:1xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The checks grade both branches of the type-field question. Not measured by the issuer: whether the source carries a type field, how many securities both witnesses carry, where Cottonwood's transactions live (one listing by the issuer returned nothing and was not pursued); each is a branch, a stop or a where-looked member on the face. prd-signoff status: ratified-text SIGNED at v0.38 by the CTO's message 5298 (the tool's own reading does not cover an addendum).
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only). Egress: Yahoo Finance through ADVI_COTBKF's existing reader, one pass, bounded at 1,500 tickers.
</preflight>
