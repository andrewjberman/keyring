# TO IRPT_BCKEND.TO-IB-pr-470 -- READ ONLY, the read before the C-CHAINCLAIM cell: the closed status set with counts; the NON-POSITIVE-BASE days by prior-day holdings; the assignment order; the accounts whose claim moves

<to_id>IRPT_BCKEND.TO-IB-pr-470</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~325</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>164</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msgs 6414 and 6420 (PRD v0.48, signed @a94db569fc) | **Decomp cell:** `IB-pr-470` (decomposition section 156) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-325/` (bash `/c/dev/wk-irpt-bckend-325`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it). **A READ, NOT A BUILD.** You edit no product file and propose no fix.

**Why.** Read `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`, `## ADDENDUM v0.48` (contract C-CHAINCLAIM, about 45
lines). The performance route's reader drops every day whose status is not `OK`, chains the rest and says `measured`. The
contract will make the claim follow the excluded day's STATUS: `NO-PRIOR-HOLDINGS` and `NON-POSITIVE-BASE` (no base to earn on)
keep `measured`; every other non-OK status, named or not yet seen, turns the claim `inferred`. Before any cell is built, the
CTO needs four facts. The weak place is `NON-POSITIVE-BASE`: it sits on the measured side by the definition of the base (the
included basket plus positive cash), not by a count. If such a day belongs to an account that HELD positions the day before,
a return was left out and the status moves to the other side.

Start from the previous two cells, merged in your worktree: `deliverables/0.9.0_WK_IRPT_BCKEND~322/` (`ib161_measure.py`,
`ib161_assemble.py`, the json and the READ file) and `~319/`. Reuse their partition cache step, window rule and day
classifier exactly (copy what you need into YOUR folder). Read the SAME latest landed day they read, 2026-10-08.

**HARD BOUNDS.** READ ONLY. The arm is theirs: the reader's own code (`infra/aws/lambda/investor-reporting/performance/
holdings_gold.py`) and the producer's code read from your worktree, run locally over the SERVED holdings gold read from S3
(gets and lists of the addresses the code itself builds). No Lambda is invoked, the deployed route is not called, nobody
signs in, nothing is written to AWS. NO account id in any form and NO value of an account: counts and status tokens only.
Name the entry whose key carries a custodian master number `the 49F entry`; name the other by its key.

**Measure.**
1. **The closed status set, from code** (`status_tokens_in_code`): every status token the gold's producer can write
   (`data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py`: the constants about lines 219-228 and
   EVERY place a status is assigned, the `np.select` about lines 860-876 and any later overwrite such as the implausible-
   return and follows-discontinuity steps; search the whole producer package for other writers of the column). Each:
   `{token, defined_at: "path:line", assigned_at: "path:line", condition_in_words}`. Say whether any code path can write a
   token outside the constants (`can_a_token_outside_the_constants_be_written`, with the line).
2. **Each token's count over the served gold** (`status_counts_over_the_served_gold`: per entry `{partitions_read, rows_read,
   by_token: {token: rows}, tokens_in_the_gold_not_in_the_code: [...]}`), over EVERY landed partition up to 2026-10-08.
3. **The NON-POSITIVE-BASE days, per entry and window** (the same eight cells: two entries x SI, YTD, QTD, 1Y).
   `non_positive_base_days: {interior, all_positions}`: `interior` by the previous cell's day rule (it must reproduce that
   cell's interior NON-POSITIVE-BASE count, e.g. 637 for the 49F entry SI); `all_positions` = every such day of the window
   wherever it sits (first, interior, last, after the last OK day). For each of the two, place every day by WHAT THE ACCOUNT
   HELD THE PRIOR DAY, into exactly these six classes (`non_positive_base_interior_by_prior_day_holdings`,
   `non_positive_base_all_positions_by_prior_day_holdings`):
   `held_none` (no position row, included or excluded), `held_only_negative` (every position row negative),
   `held_only_excluded` (position rows, none included, none negative), `held_included_only_or_mixed` (one or more included
   position rows), `held_other`, `not_determinable`. Use the gold's own columns if it carries them (`held_count`,
   `included_count`, `negative_count`, `cash_value` or their served names; say which, and that they describe the prior
   trading day's positions, with the producer line); if the gold does not carry them, say so, put the days in
   `not_determinable`, and do NOT go to another source. State `prior_day_holdings_rule_in_words`. Also give, per cell,
   `non_positive_base_all_positions_with_nonzero_cash` (days where the row's cash is not zero).
4. **The assignment order** (`assignment_order`): from the producer's code, the order in which `NON-POSITIVE-BASE` and
   `ALL-HOLDINGS-EXCLUDED` are assigned, with `cites`; `only_excluded_holdings_can_be_stamped_non_positive_base`: `YES` or
   `NO` (can an account holding only excluded, non-negative positions receive `NON-POSITIVE-BASE`), and `in_words` naming
   every case that DOES receive `NON-POSITIVE-BASE`.
5. **The accounts whose claim moves** (`accounts_whose_claim_moves`, per cell, in ACCOUNTS):
   `accounts_with_a_figure_saying_measured` (the reader returns a figure and the claim `measured` today);
   `under_the_contract_as_written` (of those, the accounts with one or more excluded days in the window, at ANY position,
   whose status is neither `NO-PRIOR-HOLDINGS` nor `NON-POSITIVE-BASE`);
   `if_non_positive_base_with_a_prior_position_also_moves` (the same, also counting a `NON-POSITIVE-BASE` day whose class in
   step 3 is none of `held_none`, `not_determinable`).
6. `control`: `{what, reading}`: plant in memory one account with a single `ALL-HOLDINGS-EXCLUDED` day and one with a single
   `NO-PRIOR-HOLDINGS` day; your step-5 counter moves the first and not the second.

Cache partitions in `C:/dev/_scratch325/` (outside the worktree; one entry has about 1,600 daily partitions: bound every
step with its own timeout, state the denominator of partitions read, never silently truncate). Remove the scratch at the
very end with a short bounded python script; if the cleanup hangs or errors, stop cleaning, say so, and still report.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~325/`: `IB164-1_status_set_and_base.json`
with the keys above plus `base_commit`, `latest_landed_day`, `per_entry_and_window` (each cell: `entry`, `window`, and the
step 3 and step 5 keys), `not_established` (a list), and `functions_invoked`, `sign_ins_made`, `aws_writes_made`,
`accounts_written`, `values_written`, `product_files_edited` each 0; your driver; and a one-page
`IB164-1_STATUS_SET_AND_BASE_READ.md` leading with the count of NON-POSITIVE-BASE days in an account that held a position.

<criterion id="IB164-1-AC1" cell_refs="IB-pr-470"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r164/p164_cells.py" . IB164-1-AC1</invocation><expect>IB164-1-AC1 PASS</expect></criterion>
<criterion id="IB164-1-AC2" cell_refs="IB-pr-470"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r164/p164_cells.py" . IB164-1-AC2</invocation><expect>IB164-1-AC2 PASS</expect></criterion>
<criterion id="IB164-1-AC3" cell_refs="IB-pr-470"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r164/p164_cells.py" . IB164-1-AC3</invocation><expect>IB164-1-AC3 PASS</expect></criterion>

<expected_criteria>IB164-1-AC1, IB164-1-AC2, IB164-1-AC3</expected_criteria>

The checks grade the reproduction against IB-pr-467's record, the sums, that each cite exists, and the bounds. Every new
count and the order verdict are UNMEASURED by the issuer.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited.
- **Refusal clause:** a reproduction that fails, an AWS read refused, or a criterion that cannot be met as written: file a row
  and report. Never weaken a check; do not edit `p164_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W325-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~325" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~325@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~325 <0.9.0_WK_IRPT_BCKEND~325@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~325/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-470.status-set-and-non-positive-base-prior-holdings.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 156 (round 164, workstream ~P), cell `IB-pr-470`.
<owned_cells>IB-pr-470</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB164-1-AC1, IB164-1-AC2, IB164-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~325/IRPT_BCKEND.TO-IB-pr-470.status-set-and-non-positive-base-prior-holdings.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base and the day read; the status tokens in code with their lines, and whether any
other can be written; each token's count per entry and any token met only in the gold; per entry and window the
NON-POSITIVE-BASE days (interior and all positions) by the six prior-day-holdings classes, and which columns gave them; the
assignment order and its YES or NO; the three claim-move counts per cell; the control; what is not established; each
criterion's last line; the proof checker's result; commit hashes; row ids; whether the scratch was cleaned.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read written to the worker's own deliverables folder; nothing is edited, built, invoked or served.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; S3 reads the two earlier cells already made.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; the deployed route is not called.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p164_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~03:2xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. Read by the issuer at holdings_performance.py:219-224 and :862-872: six constants; ALL-HOLDINGS-EXCLUDED is tested before the non-positive basket and requires negative_count == 0, and the code's own comment gives NON-POSITIVE-BASE the account whose only holdings are negative. So the issuer EXPECTS count 1 of CTO msg 6420 to be non-zero; that expectation is not on the worker face. PRD v0.48's ratified-text half reads signed @a94db569fc by the CTO's word (msg 6420); this is a read and adds no build order against it.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
