# TO IRPT_BCKEND.TO-IB-pr-452 -- READ ONLY, counts only: nine admitted pairs sized under both guard sentences, the same with five securities not graded, and the count of securities that mostly repeat

<to_id>IRPT_BCKEND.TO-IB-pr-452</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~308</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>148</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5724 (PRD v0.42 @73d4348a31, ratified-text half SIGNED @b05e8baee2) | **Decomp cell:** `IB-pr-452` (decomposition section 140) | **outcome_ref:** FWD-13

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-308/` (bash `/c/dev/wk-irpt-bckend-308`). Work only there. READ ONLY toward AWS. ONE external source
only: Yahoo Finance through the reader below, ONE PASS (each ticker asked exactly once, at most 50 a call, calls paced and never
in parallel; a ticker or a call that returns nothing is recorded and never asked again). Count the distinct tickers BEFORE
fetching; above 1,500, STOP, report the number and file a row. NO YCharts call, NO Bloomberg call. Nothing built into the product,
nothing served, no claim re-graded in the product. **This cell admits no class and excludes no security: it sizes.** Counts
only; no account id, balance or holding of an account in any output (write dates with dashes).

**Why.** Read PRD ADDENDA v0.40, v0.41 and v0.42 (the last three sections of
`org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`). The second witness (the reader's unadjusted Close) now carries two
guard sentences: (1) no grade on a day its bar equals its bar for the prior trading day (relative 1e-4); (2) no grade where it
has no bar for the calendar's prior trading day. v0.42 admits NINE type pairs under that guard: the seven of v0.39 plus
`Securities Issued by Registered Investment Companies or Business Development Companies / Inst` and `... / Not Available`
(the source's exact strings; take all nine from the PRD and from IB-pr-445's record, and list them as `pairs_admitted`).
The reviewer's note: for five institutional securities with no anchor (ADLYX, BISOX, EIBLX, GPPIX, OLCYX) nothing shows their
moved days are dated right. The CTO will rule on a per-security exclusion with three numbers. This cell prints them.

**Your instruments** are in your worktree (merged): `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~303/`
(`ib445_measure.py`: the sizing under a set of admitted pairs with the guard, the four account-day claims, the serving rule,
`freed_and_holding_no_other_ungradeable_kind`, the fetch, the per-security un-graded days; its record
`IB142-1_unmoved_bar_guard.json`) and `~306/` (the no-prior-bar sentence as measured; `IB145-1_first_moved_bar.json`). Copy what
you need into YOUR folder; write nothing into another worker's folder. Keep unchanged: source and anchor addresses, price rule,
tolerance, trading-day axis, the one-way digest of the account key, the row kinds, the ordered claim rule, the cash rule, the
type rule (exactly one pair = that type). The guard is now product code: `second_witness_grades(bars, t)` in
`data/assets/scripts/gold/irpt_reporting/second_witness_guard.py` (read it); use it or reproduce its three conditions exactly,
and say which. The reader: `fetch_yahoo` in `data/assets/scripts/silver/commonwealth_price_basis_census.py` and
`read_yahoo_close` in `data/assets/scripts/silver/commonwealth_daily_valuation.py`; your own cache `C:/dev/_scratch308/yahoo/`;
window 2026-06-05 to 2026-10-13. Scratch is OUTSIDE the worktree and deleted file by file at the end.

**Do, in this order:**
1. **Reproduce first** (`reproduces_ib_pr_445_seven_and_inst_first_sentence_only`): the seven pairs plus Inst under guard
   sentence (1) ALONE must give IB-pr-445's `seven_types_and_inst_under_the_guard` exactly (blank 46.298 percent, never served
   283, freed 10,164; `account_days` equal member for member). `{reproduces, read:{account_days, serving_rule,
   freed_and_holding_no_other_ungradeable_kind}}`. If it does not reproduce, stop and file a row.
2. **`sizings.nine_pairs_under_both_guard_sentences`:** all nine pairs, both sentences. `account_days:{present, UNGRADEABLE,
   ACCT_PRIOR_DATE, ACCT_OWN_DATE, NOTHING_TO_GRADE}`, `serving_rule:{eligible, served, blank, blank_share_percent,
   accounts_never_served}`, `freed_and_holding_no_other_ungradeable_kind`. Beside it, outside the sizing: how many account-days
   the SECOND sentence alone costs (`second_sentence_cost_in_freed_account_days`: nine pairs under sentence (1) alone, less nine
   pairs under both).
3. **`sizings.nine_pairs_with_the_five_not_graded`:** the same, but the second witness gives NO grade on any day for ADLYX,
   BISOX, EIBLX, GPPIX and OLCYX (`the_five_not_graded`, exactly those five in that order). Beside it:
   `the_five_cost:{account_days_no_longer_freed, accounts_no_longer_ever_served, row_days_of_the_five, by_ticker:{<t>:{row_days,
   accounts_holding_it}}}` (accounts as a count only).
4. **`repeating_on_more_than_half_their_days`:** over the securities of the nine pairs OUTSIDE the first witness that have bars:
   a security repeats on more than half its days when the guard (both sentences) leaves it un-graded on more than half the days
   it has a bar in the 85 graded days (state `rule_in_words`). `by_pair` (each of the nine: `securities_outside_the_first_witness_with_bars`,
   `repeating_on_more_than_half`), `total`, and `securities` (each: `ticker`, `pair`, `days_with_a_bar`, `days_not_graded`,
   `row_days`). If any of the five is not in that list, explain in `of_the_five_not_listed_explained`. Note JSOSX: the anchor
   carries it on most days (row `IRPT_BCKEND-D2-W306-S1`), so say whether it counts as outside the first witness on your rule.
5. **Control** (`control`): plant an account-day holding one security of an admitted pair whose bar moves: it is freed with
   the security graded, and NOT freed when that security is in the not-graded list; `planted` equals `read`.
6. `what_is_assumed` (one sentence; these are sizings, not stamps) and `not_established`. Recommend nothing on the exclusion.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~308/`: `IB148-1_nine_pair_sizing.json` with the
members named above plus `pairs_admitted`, `guard_used` (the product function, or its conditions reproduced), `fetch:{call_count,
distinct_tickers_asked, tickers_asked_more_than_once, tickers_with_no_bars, counted_before_fetching}`,
`claims_regraded_in_product:0`, `classes_admitted_by_this_cell:0`, `securities_excluded_by_this_cell:0`, `other_sources_asked:0`;
your scripts; and a one-page `IB148-1_NINE_PAIR_SIZING_READ.md` leading with the three numbers the CTO asked for.

<criterion id="IB148-1-AC1" cell_refs="IB-pr-452"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r148/p148_cells.py" . IB148-1-AC1</invocation><expect>IB148-1-AC1 PASS</expect></criterion>
<criterion id="IB148-1-AC2" cell_refs="IB-pr-452"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r148/p148_cells.py" . IB148-1-AC2</invocation><expect>IB148-1-AC2 PASS</expect></criterion>
<criterion id="IB148-1-AC3" cell_refs="IB-pr-452"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r148/p148_cells.py" . IB148-1-AC3</invocation><expect>IB148-1-AC3 PASS</expect></criterion>

<expected_criteria>IB148-1-AC1, IB148-1-AC2, IB148-1-AC3</expected_criteria>

The checks grade the reproduction against IB-pr-445's record, the sums, that not grading five never frees more, the repeat
list's arithmetic, the control and the bounds. Every new count is UNMEASURED by the issuer.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited.
- **Refusal clause:** if the reproduction fails or a criterion cannot be met as written: stop, file a row and report. Never
  weaken a check; do not edit `p148_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W308-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~308" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~308@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~308 <0.9.0_WK_IRPT_BCKEND~308@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~308/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-452.nine-pair-sizing-under-both-guard-sentences.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 140 (round 148, workstream ~P), cell `IB-pr-452`.
<owned_cells>IB-pr-452</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB148-1-AC1, IB148-1-AC2, IB148-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~308/IRPT_BCKEND.TO-IB-pr-452.nine-pair-sizing-under-both-guard-sentences.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the reproduction; the nine-pair sizing (blank share, never served, freed) and the second
sentence's cost; the same with the five not graded, and the five's cost by ticker; the repeat count by pair with the list;
JSOSX's standing; the fetch; the control; what is not established; each criterion's last line; the proof checker's result;
commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read-only measurement written to the worker's own deliverables folder; nothing is edited or served.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; S3 reads the earlier cells of this chain already made.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p148_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~20:1xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. prd-signoff status read by the issuer: v0.42, both halves current. The reproduction target is read by the check from IB-pr-445's merged record. The five tickers are the CTO's (msg 5724).
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
