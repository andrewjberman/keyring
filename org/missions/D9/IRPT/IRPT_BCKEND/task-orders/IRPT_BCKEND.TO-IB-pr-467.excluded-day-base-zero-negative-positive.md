# TO IRPT_BCKEND.TO-IB-pr-467 -- READ ONLY: for the reader's INTERIOR and LAST-ROW excluded days, what the base was -- zero, negative or positive -- and how long the zero run

<to_id>IRPT_BCKEND.TO-IB-pr-467</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~322</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>161</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6315 (on IB-pr-464's result) | **Decomp cell:** `IB-pr-467` (decomposition section 153) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-322/` (bash `/c/dev/wk-irpt-bckend-322`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it). **A READ, NOT A BUILD.** You edit no product file and propose no fix.

**Why.** Read `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~319/IB160-1_READER_EXCLUDED_DAYS_READ.md`, its json
and its two drivers (`ib160_measure.py`, `ib160_assemble.py`): IB-pr-464 counted, per firm entry and window, the accounts for
which the performance route's reader skips a non-OK day and still returns a figure. The CTO ruled the FIRST-DAY cases right
(no base to measure a return on). The INTERIOR and LAST-ROW cases are not ruled blind, because a non-positive base is one of
two things that need opposite rulings:
- the account's value the day before was exactly ZERO: it was empty and re-funded; linking the periods either side is the
  standard treatment and the figure is right;
- the base was NEGATIVE, or POSITIVE and flagged: the reader skips a day that HAD a return, and the figure is wrong by it
  while the claim says `measured`.
This cell counts which.

**HARD BOUNDS.** READ ONLY. The arm is IB-pr-464's, unchanged: the reader's OWN code imported from your worktree and run locally
over the SERVED holdings gold read from S3 (gets and lists of the addresses the code itself builds). No Lambda is invoked, the
deployed route is not called, nobody signs in, nothing is written to AWS. NO account id is written in any form, and NO VALUE
of an account (no balance, no return): counts and status tokens only. Name the entry whose key carries a custodian master
number `the 49F entry`; name the other by its key.

**Measure, for the SAME eight cells** (two entries x SI, YTD, QTD, 1Y at the latest landed day; reuse IB-pr-464's driver and
window rule exactly, and say if the latest landed day has moved since its read):
1. **Reproduce first:** `accounts_with_an_interior_or_last_row_excluded_day` per cell must equal IB-pr-464's `interior_only` +
   `first_and_interior` + `last_day_involved` for that cell. If it does not (and the latest day has not moved), stop and file
   a row.
2. **The days.** For those accounts, list every excluded DAY that is INTERIOR (it lies between two OK days of that account
   in the window) or is the account's LAST ROW in the window (`interior_days`, `last_row_days`, `days_counted` = their sum;
   a first-day exclusion, before the account's first OK day, is NOT counted here; state `day_rule_in_words`).
3. **For each such day, two facts:** the row's `status` token, and the PRIOR DAY'S ENDING VALUE class: the account's
   `account_value` on its previous row in the gold (the previous partition in which the account has a row; say whether that
   is always the previous trading day, and count where it is not): `zero` (state `zero_rule_tolerance`: exactly 0.0, or
   within what tolerance, and how many fall within a cent of zero without being exactly zero), `negative`, `positive`, or
   `no_prior_row`. Read from the producer's code what "base" a `NON-POSITIVE-BASE` row tests
   (`data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py`, about lines 860-890) and say whether the
   prior row's `account_value` IS that base or a proxy for it (`prior_value_rule_in_words`, with file:line); if the gold
   carries the base itself in a column, use that column and say so.
   Output per cell: `interior_by_status_and_prior_value` and `last_row_by_status_and_prior_value`: status token ->
   `{zero, negative, positive, no_prior_row}` counts of DAYS, each table summing to its days.
4. **The zero run** (`zero_run_rule_in_words`): for each counted day whose prior value is `zero`, the length of the run of
   consecutive rows of that account, ending at the prior row, whose value is zero (1 = only the prior day). Per cell:
   `interior_zero_run_lengths` and `last_row_zero_run_lengths`: a distribution over `1`, `2`, `3-5`, `6-20`, `21-60`, `more`,
   summing to the days whose prior value is zero.
5. Per cell also, in ACCOUNTS: how many of the accounts of step 1 have EVERY counted day on a zero prior value
   (`accounts_all_zero_base`), how many have one or more on a negative prior value (`accounts_with_a_negative_base`), and how
   many have one or more on a positive prior value (`accounts_with_a_positive_flagged_base`).
6. `control`: plant, in memory only, an account with a positive, then zero, then positive value over three days; your
   classifier reads the third day's prior value as `zero` with run length 1.

Read each partition ONCE into memory (cache in `C:/dev/_scratch322/`, outside the worktree; one entry has about 1,600 daily
partitions: bound every step with its own timeout and state the denominator of partitions read; never silently truncate).
Remove the scratch at the very end with a short bounded python script; if the cleanup hangs or errors, stop cleaning, say so,
and still report.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~322/`: `IB161-1_excluded_day_base.json` with
`{base_commit, arm: "READER_CODE_OVER_SERVED_GOLD", arm_in_words, latest_landed_day, per_entry_and_window:[{entry, window,
accounts_with_an_interior_or_last_row_excluded_day, interior_days, last_row_days, days_counted,
interior_by_status_and_prior_value, last_row_by_status_and_prior_value, interior_zero_run_lengths, last_row_zero_run_lengths,
accounts_all_zero_base, accounts_with_a_negative_base, accounts_with_a_positive_flagged_base}], day_rule_in_words,
prior_value_rule_in_words, zero_rule_tolerance, zero_run_rule_in_words, control:{what, reading}, not_established,
functions_invoked:0, sign_ins_made:0, aws_writes_made:0, accounts_written:0, values_written:0}`; your driver; and a one-page
`IB161-1_EXCLUDED_DAY_BASE_READ.md`: one table per entry, leading with the negative and positive-flagged counts.

<criterion id="IB161-1-AC1" cell_refs="IB-pr-467"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r161/p161_cells.py" . IB161-1-AC1</invocation><expect>IB161-1-AC1 PASS</expect></criterion>
<criterion id="IB161-1-AC2" cell_refs="IB-pr-467"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r161/p161_cells.py" . IB161-1-AC2</invocation><expect>IB161-1-AC2 PASS</expect></criterion>
<criterion id="IB161-1-AC3" cell_refs="IB-pr-467"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r161/p161_cells.py" . IB161-1-AC3</invocation><expect>IB161-1-AC3 PASS</expect></criterion>

<expected_criteria>IB161-1-AC1, IB161-1-AC2, IB161-1-AC3</expected_criteria>

The checks grade the reproduction against IB-pr-464's record, the sums and the bounds. Every new count is UNMEASURED by the
issuer. If the latest landed day has moved since IB-pr-464's read, AC1 cannot hold on the new day: read the SAME latest day
IB-pr-464 read (2026-10-08) and say so.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited.
- **Refusal clause:** a reproduction that fails, an AWS read refused, or a criterion that cannot be met as written: file a row
  and report. Never weaken a check; do not edit `p161_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W322-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~322" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~322@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~322 <0.9.0_WK_IRPT_BCKEND~322@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~322/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-467.excluded-day-base-zero-negative-positive.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 153 (round 161, workstream ~P), cell `IB-pr-467`.
<owned_cells>IB-pr-467</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB161-1-AC1, IB161-1-AC2, IB161-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~322/IRPT_BCKEND.TO-IB-pr-467.excluded-day-base-zero-negative-positive.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base and the latest landed day read; the reproduction; per entry and window the
interior and last-row days by status token and prior-value class; the zero-run distributions; the three account counts;
what the producer's base is and whether the prior row's value is it; the control; what is not established; each criterion's
last line; the proof checker's result; commit hashes; row ids; whether the scratch was cleaned.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read written to the worker's own deliverables folder; nothing is edited, built, invoked or served.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; S3 reads the earlier cell already made.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; the deployed route is not called.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p161_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~02:2xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The reproduction target is read by the check from IB-pr-464's merged record @03e9d0d4c2. The two readings of a non-positive base are the CTO's (msg 6315), stated on the face as the reason for the split. No account-id text test is in this check; the bounds keep ids and values out.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
