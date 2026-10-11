# TO IRPT_BCKEND.TO-IB-pr-445 -- READ ONLY: the unmoved-bar guard -- the overlap table again under it, the sizing with the institutional class under it, and what it un-grades

<to_id>IRPT_BCKEND.TO-IB-pr-445</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~303</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>142</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5549 (ruling on IB-pr-443's read) | **Decomp cell:** `IB-pr-445` (decomposition section 134) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-303/` (bash `/c/dev/wk-irpt-bckend-303`). Work only there. READ ONLY toward AWS. ONE external source
only: Yahoo Finance through the reader below, ONE PASS (each ticker asked exactly once, at most 50 a call, calls paced and never in
parallel; a ticker or a call that returns nothing is recorded and never asked again). If the distinct tickers come to more than
1,500, STOP before fetching, report the number and file a row. NO YCharts call, NO Bloomberg call. Nothing built into the product,
nothing served, no claim re-graded in the product, and NO CLASS IS ADMITTED by this cell. Counts only.

**Why.** Read PRD ADDENDA v0.38 and v0.39 (the last two sections of `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`).
The second witness of the date basis (the reader's unadjusted Close) may grade a security the first witness (the Schwab anchor)
does not carry, if the security's type is admitted. Seven type pairs are admitted; the institutional fund share class is left
out on two one-day-off security-days. IB-pr-443 looked at those two: on both, the READER repeats the prior trading day's bar
while the first witness moves. The CTO ruled that this is the dangerous direction (a custodian's mark that truly sat at the
prior close would equal the repeated bar and be stamped own-date), that the institutional class stays out on that finding, and
that the same staleness could reach an admitted class on a day nobody compared. What would close it for every class is a GUARD:

> **The second witness does not grade a security-day on which its own bar equals its bar for the prior trading day. An unmoved
> bar cannot tell one day from the next.**

This cell measures the guard. It rules nothing.

**The guard, exactly** (state it as `guard_rule_in_words`): for a security and a trading day t, if the reader's bar for t equals
its bar for the prior trading day (within the instrument's relative tolerance 1e-4; say also how many more security-days an
"equal to the cent" reading would un-grade), then the second witness gives NO grade for that security on day t. A security-day
with no grade from any witness is ungradeable, as a security with no bar is today. The guard applies to the SECOND witness
only; the first witness grades every security it carries, as today.

**Your instruments** are in your worktree (merged): `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~299/`
(Table 1: the 894 securities both witnesses carry, the type join by CUSIP from the transactions table, the one-day-off
classifier, the one-pass fetch); `~300/` (the seven classes, the row grading against the reader's bar, the four account-day
outcomes, the sizing under the seven admitted types, `IB139-1_sizing_under_v039.json`); `~301/` (the five security-days);
`~296/`, `~294/`, `~288/`. Copy what you need into YOUR folder; write nothing into another worker's folder. Keep unchanged: the
source and anchor addresses, the price rule, the tolerance, the trading-day axis, the one-way digest of the account key, the row
kinds, the ordered claim rule with the v0.36 names, the cash rule in force, the type rule of v0.39 (exactly one pair = that
type), the seven admitted pairs as the transactions table writes them. The reader: `fetch_yahoo` in
`data/assets/scripts/silver/commonwealth_price_basis_census.py` and `read_yahoo_close` in
`data/assets/scripts/silver/commonwealth_daily_valuation.py`; your own cache `C:/dev/_scratch303/yahoo/`; window 2026-06-05 to
2026-10-13. Scratch is OUTSIDE the worktree and deleted file by file at the end.

**Do, in this order:**

1. **Table 1 again, under the guard** (`overlap_by_type_under_the_guard`). The same 894 securities and 85 days as IB-pr-441, the
   same type key. For each security-day, ONE of five columns: `not_graded_under_the_guard` (the reader's bar for t equals its bar
   for the prior trading day); otherwise as before: `equal`, `one_day_off`, `neither`, `no_bar`. Per type: `securities`,
   `security_days`, the five counts summing to `security_days`, and `equal_on_days_the_close_moved`. List
   `types_with_an_empty_one_day_off_column_under_the_guard` (those with `one_day_off` 0 and `equal` above 0). Say where each of
   IB-pr-441's five one-day-off security-days lands under the guard (`the_five_earlier_one_day_off_security_days`: ticker, date,
   `under_the_guard` = one of the five columns). If any one-day-off entry REMAINS under the guard, list it with both witnesses'
   three-day values. Also print, per type, how many `neither` days remain and whether the guard moved any.
   CHECK your re-run against IB-pr-441 first: with the guard switched off your table must equal its Table 1 exactly (894
   securities, 64,536 security-days, equal 63,720, one day off 5, neither 499, no bar 312); if it does not, stop and say why.

2. **Three sizings** (`sizings`), each with the four claim counts, eligible, served, blank, blank share, accounts never served,
   and `freed_and_holding_no_other_ungradeable_kind`, computed exactly as IB-pr-442 computed its sizing:
   - `seven_types_no_guard`: IB-pr-442's sizing again (it read blank 50.305 percent, never served 357, freed 5,666): yours must
     reproduce it, or say why not;
   - `seven_types_under_the_guard`: the same seven pairs, the second witness not grading an unmoved-bar security-day;
   - `seven_types_and_inst_under_the_guard`: the seven pairs PLUS the institutional share class
     (`RIC/BDC / Inst`, the source's exact string), all under the guard.
   An account-day is freed only when EVERY security it holds outside the first witness is graded by the second witness at the
   day's close; a security-day the guard leaves ungraded blocks its account-day. State `what_is_assumed` in one sentence and that
   these are sizings, not stamps.

3. **What the guard costs in the seven admitted types** (`guard_cost_in_the_seven_types`): `row_days_not_graded` (rows of
   admitted-type securities outside the first witness that fall on an unmoved-bar day), `security_days_not_graded`, and
   `account_days_no_longer_freed` (the first sizing's freed-with-no-other-kind less the second's). Say which securities carry
   most of it (up to ten, by ticker; a money-market or stable-value fund whose price never moves would be un-graded every day:
   name any security un-graded on more than half its days, with its type pair). Also `inst_under_the_guard`: for the
   institutional class, securities, row-days graded, row-days the guard leaves ungraded, and account-days freed by adding it.

4. **Control** (`control.planted` must equal `control.read`): a planted fixture of one security over five days whose reader bar
   repeats on day 3: day 3 is `not_graded_under_the_guard` (`unmoved_bar_is_not_graded: true`), the other days are graded
   (`moved_bar_is_graded: true`); and an account-day holding that security on day 3 is not freed.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~303/`: `IB142-1_unmoved_bar_guard.json` with
`{same_account_days_read, guard_rule_in_words, guard_off_reproduces_ib_pr_441, overlap_by_type_under_the_guard:{<type>:{securities,
security_days, equal, one_day_off, neither, no_bar, not_graded_under_the_guard, equal_on_days_the_close_moved}},
types_with_an_empty_one_day_off_column_under_the_guard, the_five_earlier_one_day_off_security_days:[{ticker, date,
under_the_guard}], one_day_off_remaining_under_the_guard:[...], to_the_cent_variant:{...}, sizings:{seven_types_no_guard:{...},
seven_types_under_the_guard:{...}, seven_types_and_inst_under_the_guard:{...}} (each: account_days:{present, UNGRADEABLE,
ACCT_PRIOR_DATE, ACCT_OWN_DATE, NOTHING_TO_GRADE}, serving_rule:{eligible, served, blank, blank_share_percent,
accounts_never_served}, freed_and_holding_no_other_ungradeable_kind), what_is_assumed, guard_cost_in_the_seven_types:{row_days_not_graded,
security_days_not_graded, account_days_no_longer_freed, securities_carrying_most, securities_ungraded_on_more_than_half_their_days},
inst_under_the_guard:{...}, fetch:{calls:[{tickers}], distinct_tickers_asked, tickers_asked_more_than_once:0}, control:{planted,
read}, claims_regraded_in_product:false, other_sources_asked:0, classes_admitted_by_this_cell:0}`; and a one-page
`IB142-1_UNMOVED_BAR_GUARD_READ.md`. `same_account_days_read` is true only if your totals under the cash rule equal IB-pr-442's
(UNGRADEABLE 43,310; ACCT_PRIOR_DATE 55; ACCT_OWN_DATE 19,832; NOTHING_TO_GRADE 13,599; present 76,796); otherwise explain in
`source_difference_explained` and file a row. Counts only: no account id, no balance, no single account's holding.

<criterion id="IB142-1-AC1" cell_refs="IB-pr-445"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r142/p142_cells.py" . IB142-1-AC1</invocation><expect>IB142-1-AC1 PASS</expect></criterion>
<criterion id="IB142-1-AC2" cell_refs="IB-pr-445"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r142/p142_cells.py" . IB142-1-AC2</invocation><expect>IB142-1-AC2 PASS</expect></criterion>
<criterion id="IB142-1-AC3" cell_refs="IB-pr-445"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r142/p142_cells.py" . IB142-1-AC3</invocation><expect>IB142-1-AC3 PASS</expect></criterion>

<expected_criteria>IB142-1-AC1, IB142-1-AC2, IB142-1-AC3</expected_criteria>

The checks grade sums, that the listed empty-column types are those the table shows, that each of the five earlier days is
placed, that the guard's cost is the difference of two sizings and not negative, the one-pass bound and the control. Every count
is UNMEASURED by the issuer. A one-day-off entry that REMAINS under the guard is a finding, not a failure.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file, no PRD, no `sources.json`, no gold script, no ADVI_COTBKF file.
- **Refusal clause:** the 1,500-ticker stop; a whole fetch call that fails is recorded, not repeated; the two reproductions
  (Table 1 with the guard off; IB-pr-442's sizing) must hold or you stop and say why. If a criterion cannot be met as written,
  stop, file a row and report. Never weaken a check; do not edit `p142_cells.py`. Do not make a number fit.
- **Row ids** are `IRPT_BCKEND-D2-W303-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's existing line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~303" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~303@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~303 <0.9.0_WK_IRPT_BCKEND~303@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push. Write no firm name as a literal in any file, and no token beginning `z09` in the two outputs.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~303/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-445.unmoved-bar-guard-table-and-sizing.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 134 (round 142, workstream ~P), cell `IB-pr-445`.
<owned_cells>IB-pr-445</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB142-1-AC1, IB142-1-AC2, IB142-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~303/IRPT_BCKEND.TO-IB-pr-445.unmoved-bar-guard-table-and-sizing.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the two reproductions (guard off equals Table 1; the seven-type sizing equals IB-pr-442's);
the table under the guard with the one-day-off and not-graded columns per type, and where the five earlier days land; any
one-day-off entry that remains; the three sizings side by side; the guard's cost in the seven types and the securities that
carry it; the institutional class under the guard; the to-the-cent variant; the number of fetch calls and tickers; the
control; each criterion's last line; the proof checker's result; scratch deleted; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read-only measurement written to the worker's own deliverables folder; no product file, route, function or served byte.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission change; S3 reads and public market-data fetches through a reader the estate already runs.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p142_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~18:3xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The reproduction figures on the face (Table 1: 894, 64,536, 63,720, 5, 499, 312; the sizing: 50.305 percent, 357, 5,666) were read by the issuer from the merged outputs of IB-pr-441 and IB-pr-442; everything under the guard is unmeasured. The guard is the CTO's wording (msg 5549), quoted on the face.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only). Egress: Yahoo Finance through ADVI_COTBKF's existing reader, one pass, bounded at 1,500 tickers.
</preflight>
