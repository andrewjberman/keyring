# TO IRPT_BCKEND.TO-IB-pr-435 -- READ ONLY: the securities the anchor does not carry, ranked; the cash rule counted; and whether a price store the estate already holds carries their closes

<to_id>IRPT_BCKEND.TO-IB-pr-435</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~293</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>133</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5082 (ruling on the re-count of IB-pr-429 AMENDMENT 2) | **Decomp cell:** `IB-pr-435` (decomposition section 125) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-293/` (bash `/c/dev/wk-irpt-bckend-293`). Work only there. READ ONLY: S3 reads through `.tools/aws`; no
write to any AWS resource; no vendor is asked for anything; nothing is built into the product; nothing is served.

**Why.** Under PRD ADDENDUM v0.35/v0.36 (`org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`, the last three sections) an
account-day that holds one priced security the instrument cannot place at a close is `UNGRADEABLE` and blank. The re-count read
57.3 percent of 75,796 eligible Cottonwood account-days blank and 382 of 999 accounts never served. One kind carries it:
`OUTSIDE_ANCHOR`, a priced security the Schwab anchor does not carry, on 34,437 account-days. The CTO ruled the serving rule
stands, and that the next read is the anchor's coverage, from what the estate already holds. No gold producer is cut before it.

**Your instrument is on another branch.** The re-count's scripts and outputs are committed on branch `wk-IRPT_BCKEND-288b`
(commit 4f263f004c), not yet merged into your base. Read them with `git show wk-IRPT_BCKEND-288b:<path>`; the folder is
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~288/` and holds `ib429_fetch.py`, `ib429_claims.py`,
`ib429_claims_v035.py`, `IB127-2_account_day_claims_v035.json` and `IB127-2_ACCOUNT_DAY_CLAIMS_V035_READ.md`. Copy the scripts
into YOUR folder and extend the copies; do not write into `~288`'s folder. Keep unchanged: the source and anchor addresses, the
price rule, the tolerance, the trading-day axis, the one-way digest of the account key, the row-kind definitions, the ordered
claim rule with the v0.36 names (`UNGRADEABLE`, `ACCT_PRIOR_DATE`, `ACCT_OWN_DATE`, `NOTHING_TO_GRADE`). Scratch goes OUTSIDE the
worktree in `C:/dev/_scratch293/` and is deleted file by file at the end.

**Three things to count, on the same 85 partitions (2026-06-10 to 2026-10-09):**

1. **The ranking.** Every security behind an `OUTSIDE_ANCHOR` row (a priced, non-cash row whose security the anchor carries on
   neither day), identified as the instrument identifies it (CUSIP; the ticker beside it where the source carries one), ranked by
   the account-days it carries (an account-day holding two such securities counts once under each). Print the count of
   securities, the total of those security-account-days, how many securities cover HALF of it and how many cover NINETY PERCENT,
   and the number of distinct account-days that hold one or more outside-anchor rows (the re-count read 34,437).
   `same_account_days_read` is true only if this run's v0.35 totals equal the re-count's file exactly (UNGRADEABLE 42,967;
   ACCT_OWN_DATE 20,138; NOTHING_TO_GRADE 13,636; ACCT_PRIOR_DATE 55); otherwise say what moved in `source_difference_explained`
   and file a row. A security identifier (a CUSIP, a ticker, a fund name) is not client data and is listed; an account id, a
   balance or any one account's holding is never written.

2. **The cash rule, as ruled.** The re-count treated a cash-flagged priced row outside the anchor as cash, on 31,307 account-days,
   and said 19,809 of them would turn `UNGRADEABLE` if such a row were not cash. Ruling: such a row is cash ONLY WHERE MEASURED --
   the source's own price for that row (Market Value / Units, by the instrument's price rule and tolerance) is EQUAL in the day's
   partition and in the prior trading day's. Otherwise it is `UNGRADEABLE`, kind `OUTSIDE_ANCHOR`. For the 19,809 account-days:
   how many keep every such row as cash (`price_equal_both_days_stays_cash`), how many have one or more whose price differs
   (`price_differs_becomes_OUTSIDE_ANCHOR`), how many cannot be compared because the row is absent from the prior trading day's
   partition (`not_comparable`; state how you treat it in `not_comparable_treated_as` -- the ruling's word is "only where
   measured", so an unmeasured row is not cash -- and print it separately so the CTO can see it). Then re-state the four claim
   counts and the serving rule (eligible, served, blank, blank share, accounts never served) under this rule, beside the
   re-count's. The securities that become `OUTSIDE_ANCHOR` by this rule join the ranking of item 1; say how many security-account-
   days they add, in `ranking.added_by_the_cash_rule`.
   The sixth reason (a non-cash row with Units zero and Market Value positive) stays a refusal of the stamp: count its rows and
   account-days in `sixth_reason`, as the re-count did, and change nothing for it.

3. **What the estate already holds.** For each ranked security and each date it is needed on (the day AND the prior trading day of
   every account-day it makes ungradeable), is its close in a price store the estate already holds? The stores are the six
   declared in `data/assets/scripts/analysis/commonwealth_price_census.py`, `STORES` (about lines 55-73), each an exact
   `legacy_address()` call; read them through that module's own readers (`read_store`, about line 448; `load_store_cached`, about
   line 489) and its own key and column declarations; do not hand-type an address. Per `2.0.0_SA_COO~C2` (msg 5084): two of them
   are Cottonwood's own (`...-gold-canonical-holdings`, keyed by cusip and ticker, a CUSTODIAN MARK on a held position, last read
   to 2026-10-06; `...-silver-canonical-prices`, ticker only, last read to 2026-06-09); the other four are market stores.
   ADVI_COTBKF also derives a local table `after/security_day_price.parquet` in its build's data directory: it is local only and
   not served; if a copy is readable on this box say where and count against it as a seventh, clearly marked LOCAL; if not, say it
   was not found and do not build it.
   The module BARS every other firm's stores by name; keep that bar: open no store of another firm.
   For each store: `opened`, its first and last date in your window, `price_kind` (`custodian_mark` -- the same custodian's value
   of the same holding, which is NOT an independent close -- or `market_close`), how many needed security-days it could answer
   (`security_days_needed`) and how many it does (`security_days_found`); a store you could not open carries `not_opened_reason`.
   For each ranked security: `coverage` (`every_needed_day`, `some_needed_days`, `no_needed_day`), `best_store`, and the share of
   its needed days found. Then, the number the CTO needs: if every security with `every_needed_day` coverage from a
   `market_close` store were treated as gradeable, how many account-days would stop being `OUTSIDE_ANCHOR` -- an UPPER BOUND, said
   as one (a found close does not say the holding sits at it), in `upper_bound_if_market_close_stores_used`; and the same with
   `custodian_mark` stores admitted, separately. Do not re-grade any claim with a store's price.
   **Control:** plant two security-days against a small fixture store (one present, one absent) and show the reader reports found
   and not found; `control.planted` must equal `control.read`.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~293/`: `IB133-1_outside_anchor_coverage.json` with
`{same_account_days_read, ranking:{securities:[{security, ticker, account_days_carried, coverage, best_store, needed_days,
found_days}], securities_count, security_account_days_total, securities_covering_half, securities_covering_ninety_percent,
account_days_holding_an_outside_anchor_row, added_by_the_cash_rule}, cash_rule:{account_days_examined,
price_equal_both_days_stays_cash, price_differs_becomes_OUTSIDE_ANCHOR, not_comparable, not_comparable_treated_as},
account_days_under_the_cash_rule:{present, UNGRADEABLE, ACCT_PRIOR_DATE, ACCT_OWN_DATE, NOTHING_TO_GRADE},
serving_rule_under_the_cash_rule:{eligible, served, blank, blank_share_percent, accounts_never_served}, sixth_reason:{rows,
account_days}, stores:[...], coverage_by_security:{every_needed_day, some_needed_days, no_needed_day},
upper_bound_if_market_close_stores_used, upper_bound_if_custodian_mark_stores_also_used, control:{planted, read}}`; and a one-page
`IB133-1_OUTSIDE_ANCHOR_COVERAGE_READ.md` (the top twenty securities by name with their account-days and coverage; the half and
ninety-percent counts; the cash rule's three numbers; the blank share beside 57.3 percent; each store in one line; what was not
measured).

<criterion id="IB133-1-AC1" cell_refs="IB-pr-435"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r133/p133_cells.py" . IB133-1-AC1</invocation><expect>IB133-1-AC1 PASS</expect></criterion>
<criterion id="IB133-1-AC2" cell_refs="IB-pr-435"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r133/p133_cells.py" . IB133-1-AC2</invocation><expect>IB133-1-AC2 PASS</expect></criterion>
<criterion id="IB133-1-AC3" cell_refs="IB-pr-435"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r133/p133_cells.py" . IB133-1-AC3</invocation><expect>IB133-1-AC3 PASS</expect></criterion>

<expected_criteria>IB133-1-AC1, IB133-1-AC2, IB133-1-AC3</expected_criteria>

What the checks need that is easy to miss: in `ranking.securities` every entry has a unique `security`, a positive integer
`account_days_carried`, the list sorted from the largest, `coverage` one of the three classes and a `best_store` key (null when
none); `securities_covering_half` is the smallest number of top entries whose carried account-days reach half of the total, and
likewise ninety percent; `stores` has exactly one entry whose `id` ends with each of the six store names; the three coverage
classes sum to the number of ranked securities. If the ranking is counted BEFORE the cash rule's additions, say so in the read and
keep the list, its total and its two cover counts on that one basis.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file, no PRD, no `sources.json`, no gold script, no ADVI_COTBKF file.
- **Refusal clause:** if a store cannot be read through the census module's own readers, do not hand-build its address: record it
  as not opened with the reason. If a criterion cannot be met as written, stop, file a row and report. Never weaken a check; do
  not edit `p133_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-S<n>`, the next free number in the channel at filing (read the file just before you commit; the
  proof gate resolves only this form); `surfaced_by` is your serial; `surfaced_at` is `date -u +%FT%TZ`; append only, keeping the
  channel file's existing line endings byte for byte.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~293" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~293@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~293 <0.9.0_WK_IRPT_BCKEND~293@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~293/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-435.outside-anchor-securities-and-held-price-coverage.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 125 (round 133, workstream ~P), cell `IB-pr-435`.
<owned_cells>IB-pr-435</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB133-1-AC1, IB133-1-AC2, IB133-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~293/IRPT_BCKEND.TO-IB-pr-435.outside-anchor-securities-and-held-price-coverage.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the number of securities, the half and ninety-percent counts and the top ten by name with
their account-days and coverage; the cash rule's three numbers and the blank share and never-served accounts under it; each
store in one line (opened, window, price kind, found of needed); the two upper bounds; the control; each criterion's last line;
the proof checker's result; scratch deleted; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read-only count written to the worker's own deliverables folder; no product file, route, function or served byte.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission change; S3 reads only, through the readers ADVI_COTBKF's census already uses; a refusal is recorded as a store not opened.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p133_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~14:1xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The two bound figures (34,437; 19,809) are the re-count's, read by the issuer in the worker's tree, and bind only when the same account-days are read; every other count is unmeasured. The six store names were read by the issuer at commonwealth_price_census.py lines 55-73; the stores' windows are 2.0.0_SA_COO~C2's reading (msg 5084), not the issuer's.
lane: the <paths> block IS the grant: the worker's own folder, the channel, the order. DIRECT-ACT (one read-only cell, LOCAL: records only). The instrument is read from branch wk-IRPT_BCKEND-288b, whose merge waits on another seat's uncommitted channel rows.
</preflight>
