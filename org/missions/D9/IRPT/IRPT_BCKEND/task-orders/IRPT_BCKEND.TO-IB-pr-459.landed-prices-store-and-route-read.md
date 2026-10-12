# TO IRPT_BCKEND.TO-IB-pr-459 -- READ ONLY, two measurements: does the landed prices store hold the unadjusted Close (and when is it refreshed); and what the performance route's reader answers for a window with a non-OK day

<to_id>IRPT_BCKEND.TO-IB-pr-459</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~315</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>155</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6004 | **Decomp cell:** `IB-pr-459` (decomposition section 147) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-315/` (bash `/c/dev/wk-irpt-bckend-315`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit`. **READ ONLY.** No AWS write, no invoke of any function, NO SIGN-IN as a service or a person (the
service account's password is under an explicit deny for this box, row `IRPT_BCKEND-D2-S96`: do not try it and seek no grant),
no product file edited, nothing built or proposed. ONE external source, Yahoo Finance through the repo's reader, ONE PASS
(count the distinct tickers BEFORE fetching; they must be the 878 of the earlier reads; above 1,500 STOP; each ticker asked
once, at most 50 a call, paced, never in parallel; nothing re-asked). NO YCharts call, NO Bloomberg call. Counts only in every
output: no account id (not even a digest of one in the read file), no balance, no holding; write dates with dashes.

**Why.** Read `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~313/IB153-1_PRODUCER_DESIGN_READ.md` and its json
(`module_inputs`, `open_design_questions` 1 and 3, the consumer entry for the performance route reader). The date-basis rule's
second witness needs an unadjusted daily Close per ticker, and no scheduled, landed source of it is known: every measurement
fetched it at run time. A LANDED prices store with yahoo-labelled points exists; whether it holds the unadjusted Close, and
when it is refreshed, was not read. And the performance route's reader skips a non-OK day and chains over it; nobody has read
what it answers for such a window. The CTO writes the producer's addendum from these two facts and does not write it blind.

**Measurement 1 -- the landed prices store** (`landed_prices_store`, `tickers`, `ticker_days`):
- The store: the parquet the legacy-addresses row for `silver/prices/canonical_prices.parquet` names, read by
  `data/assets/scripts/silver/commonwealth_price_basis_census.py:159` (read that script's header, lines 1-60: it already
  classes tickers `dividend_adjusted`, `mixed` and carries `linear_interpolation` fills). State `address_built_by` (the
  file:line that builds or names the address; do not type the address from memory), its `last_modified_utc` (one
  `s3api head-object`), `rows`, its columns, and `how_a_point_is_labelled_yahoo` (the column and value that mark a point's
  source).
- Its refresh (`refresh`): WHO writes that object and on what schedule: find the writer by `comp-pipescript` (`io`,
  `postdeps`) and the native Grep tool for the object's key, then its trigger in Terraform or the schedule registry
  (`schedule_found`, `writer`, `schedule_or_trigger`, `searched`). Also `last_modified_history`: if the bucket keeps versions,
  the last-modified times of up to the 30 newest versions of that key (`s3api list-object-versions`, auto-paginated, counted
  client-side), so the cadence is read from the object itself; if it keeps none, say so.
- The comparison: the same 878 tickers and the same window as IB-pr-454 / IB-pr-457 (reuse the driver in
  `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~313/`; one Yahoo pass for the unadjusted Close through
  `fetch_yahoo` / `read_yahoo_close`; cache in `C:/dev/_scratch315/`, outside the worktree, deleted file by file at the end).
  Place EACH of the 878 tickers in exactly one of: `every_compared_day_equal`, `some_days_not_equal`,
  `no_yahoo_labelled_point_in_the_store`, `not_in_the_store`, `no_bar_from_the_reader` (`tickers.asked` 878, `tickers.outcomes`
  summing to it). Over ticker-days where both exist: `ticker_days.compared` = `equal` + `not_equal`, with `equality_rule`
  (relative 1e-4, the module's tolerance). `not_equal_by_cause` (cause to count, summing to `not_equal`): your best
  classification from the data, e.g. a constant ratio that changes at a dividend date (adjusted), an interpolated fill, a
  different day, other. Also: how many of the 85 graded days and of the 40 days before them the store COVERS per ticker
  (`store_coverage`: tickers with every needed day, with gaps, and the newest day the store holds against the newest the
  reader returns). Conclude with ONE word, `the_store_holds_the_unadjusted_close`: `YES_FOR_EVERY_COMPARED_TICKER`, `FOR_SOME`,
  `NO` or `CANNOT_BE_TOLD`.

**Measurement 2 -- one read through the performance route** (`route_read`):
- The deployed route needs a signed-in principal, which this box may not obtain. So make the read the box CAN make and say
  which it is: `arm: READER_CODE_OVER_SERVED_GOLD` = the route reader's OWN code
  (`infra/aws/lambda/investor-reporting/performance/holdings_gold.py`, `HoldingsGoldSource`; read it whole, and
  `performance/installed.py` for how the route composes its source and its window) imported from the repo and run locally
  over the SERVED holdings gold read from S3 (read only, the addresses the code itself builds, for one of the entries the
  route composes today; name the `sources.json` entry key). No network call but S3 reads; no Lambda invoked. `arm_in_words`
  says plainly that this is the reader's code at your base over served data, NOT the deployed function's answer, and what
  could differ (the deployed package's bytes; the route's authorization and envelope). If even that cannot be made, `arm:
  NOT_MADE` with `why_not_made`, and stop there.
- Pick, from the served gold, ONE account whose window holds one or more rows with a status other than OK
  (`with_a_non_ok_day`) and ONE control account whose window holds none (`control_all_ok`), the same window for both (the
  route's default window, or the longest one the code offers; state it). For each record: `window`, `days_in_window`,
  `non_ok_days`, `non_ok_status_values` (the distinct status tokens), and from the reader's answer exactly what the CTO named:
  `days_excluded`, `claim`, `absences` (as the reader returns them; counts and tokens, never a value), plus `answer_keys` (the
  key names of the answer). `chained_over_the_non_ok_day`: true if the returned period return spans the non-OK day by chaining
  the remaining days, false if the reader refuses or returns no figure, null if it cannot be told; cite `reader_code_line`.
  If no account in the served gold has a non-OK day, say so with the count of rows and statuses read, and plant ONE in a COPY
  in memory (never in S3) to read the reader's behaviour: then `planted: true` and the claim is `inferred`.

**AMENDMENT 1 (2026-10-11 ~23:5xZ, issuer, on CTO msg 6162).** Measurement 1 reports PER FUND CLASS, not one figure. Another
project measured this same store today against the price paid on trades: for funds whose stored close the build did NOT
replace, the close is more than 20 percent off the price paid on 3,205 of 3,614 trades (median ratio 0.742); for funds whose
close it DID replace, within 1 percent on 10,411 of 10,636. Read
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_76_L9_GRADE_20261011.md` and
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_77_20261011.md` (sections 1 and 2), and find
in the records they cite HOW a fund is marked replaced or not (the flag, and where it lives: a column of the store, a list,
or the build's own table; cite file:line; if you cannot find it, say so and do not guess). Then add to the json
`by_fund_class`: for each class you can form (`replaced`, `not_replaced`, `not_a_fund_or_unmarked`), the tickers of the 878
in it, and the SAME five ticker outcomes and the same ticker-days `compared` / `equal` / `not_equal` as the whole, each
summing with no remainder to the whole's; and the median ratio of the store's point to the reader's unadjusted Close on
unequal ticker-days per class. And `admitted_types_holding_not_replaced_funds`: for each of the NINE admitted type pairs
(PRD v0.39 and v0.42; the product module `date_basis_grading.py` lists them), how many of its securities among the 878 are
`not_replaced`, and how many of those show unequal ticker-days. The CTO's sentence governs the reading: an adjusted close
dates nothing. The one word `the_store_holds_the_unadjusted_close` is then given PER CLASS as well
(`the_store_holds_the_unadjusted_close_by_class`). The checks do not grade this amendment; the issuer reads it at the drain.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~315/`: `IB155-1_two_measurements.json` with the
members named above plus `base_commit`, `fetch:{call_count, distinct_tickers_asked, tickers_asked_more_than_once: 0,
counted_before_fetching}`, `not_established`, `aws_writes_made: 0`, `sign_ins_made: 0`, `functions_invoked: 0`,
`product_files_edited: 0`, `builds_proposed: 0`, `other_sources_asked: 0`; your driver; and a one-page
`IB155-1_TWO_MEASUREMENTS_READ.md` leading with the two answers.

<criterion id="IB155-1-AC1" cell_refs="IB-pr-459"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r155/p155_cells.py" . IB155-1-AC1</invocation><expect>IB155-1-AC1 PASS</expect></criterion>
<criterion id="IB155-1-AC2" cell_refs="IB-pr-459"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r155/p155_cells.py" . IB155-1-AC2</invocation><expect>IB155-1-AC2 PASS</expect></criterion>
<criterion id="IB155-1-AC3" cell_refs="IB-pr-459"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r155/p155_cells.py" . IB155-1-AC3</invocation><expect>IB155-1-AC3 PASS</expect></criterion>

<expected_criteria>IB155-1-AC1, IB155-1-AC2, IB155-1-AC3</expected_criteria>

The checks grade the denominators (878 tickers placed, ticker-days summing), the shape of the route read with its control, and
the six zeros. Every answer is UNMEASURED by the issuer; "none found", "cannot be told" and "not made" pass where true.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited; nothing is built.
- **Refusal clause:** an AWS read refused, a count of tickers that is not 878, or a criterion that cannot be met as written:
  stop, file a row and report. Never weaken a check; do not edit `p155_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W315-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~315" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~315@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~315 <0.9.0_WK_IRPT_BCKEND~315@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~315/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-459.landed-prices-store-and-route-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 147 (round 155, workstream ~P), cell `IB-pr-459`.
<owned_cells>IB-pr-459</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB155-1-AC1, IB155-1-AC2, IB155-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~315/IRPT_BCKEND.TO-IB-pr-459.landed-prices-store-and-route-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; the store's address source, last-modified, writer and schedule (or none found),
and the cadence read from its versions; the 878 tickers by outcome, the ticker-days equal and not, the causes, the coverage,
and the one word; the route read's arm in words, the window, the non-OK statuses, `days_excluded`, `claim`, `absences` for the
account and for the control, and whether the reader chained over the day; the fetch; what is not established; each criterion's
last line; the proof checker's result; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read-only measurement written to the worker's own deliverables folder; nothing is edited, built, served or invoked.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; S3 reads of a silver prices object and a served gold; the service password's deny (row IRPT_BCKEND-D2-S96) is named on the face as a wall.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; the deployed route is NOT called.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; one is read.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p155_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~23:0xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. ISSUER'S READING OF THE CTO'S SECOND ASK, stated: "one read through the performance route ... as served" is cut as the reader's own code over the served gold, because the deployed route needs a sign-in this box is denied and the CTO has ruled no served-read window for a single read (msgs 5200, 5770); the face makes the worker say which arm it made and what could differ. The facts on the face are IB-pr-457's merged record @01502183ee, read by the issuer in its json.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
