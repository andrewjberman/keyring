# TO IRPT_BCKEND.TO-IB-pr-464 -- READ ONLY: the performance route's reader, per window and per composed firm: accounts with an excluded day, and whether those days are first or interior

<to_id>IRPT_BCKEND.TO-IB-pr-464</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~319</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>160</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6245 (PRD v0.46 @3f577ef37f: "three reads before any cell, no build") | **Decomp cell:** `IB-pr-464` (decomposition section 152) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-319/` (bash `/c/dev/wk-irpt-bckend-319`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it). **A READ, NOT A BUILD.** You edit no product file and propose no build or fix.

**Why.** Read PRD ADDENDUM v0.46 (the last section of `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`), its closing
bullet, and `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~315/IB155-1_TWO_MEASUREMENTS_READ.md` (Measurement 2)
with its driver `ib155_measure.py`. The performance route's reader (`infra/aws/lambda/investor-reporting/performance/holdings_gold.py`:
non-OK rows dropped at about line 246, the chain over the remaining rows at about 254, `days_excluded` at about 274) skips a
non-OK day, chains the rest, and still gives the claim `measured`: a figure over 248 of 249 days for one account. That is a
served claim that may say more than it knows, for the two firms the route composes today (`performance/installed.py`, about
line 68). The CTO rules on it with COUNTS: how common is it, and where in an account's window do the excluded days fall. A
first-day exclusion (an account not yet funded) is a different thing from an interior one (a gap chained across).

**HARD BOUNDS.** READ ONLY. The arm is the one IB-pr-459 used: the reader's OWN code imported from your worktree and run
locally over the SERVED holdings gold read from S3 (gets and lists of the addresses the code itself builds; nothing else). No
Lambda is invoked, the deployed route is not called, nobody signs in, nothing is written to AWS. NO account id is written in
any form (no digest of one either): counts only. Do not write the entry key that carries a custodian master number; name that
entry `the 49F entry` and the other by its key.

**Measure, for EACH entry the route composes (both firms) and EACH window the reader offers** (name them from the code:
`windows_from_code`, `windows_code_line`; the ruled periods and Since Inception, each at the latest landed day):
- `accounts_read` (every account with one or more rows in the window), split with no remainder into
  `accounts_with_an_excluded_day` (the reader returns a figure and `days_excluded` is 1 or more), `accounts_with_none`
  (`days_excluded` 0), and `accounts_the_reader_refuses` (no figure; give the refusal codes with counts in `refusals`).
- For the accounts with an excluded day: `position_of_the_excluded_days`, each account in EXACTLY one of `first_day_only`
  (every excluded day precedes the account's first OK day in the window), `interior_only` (every excluded day lies between two
  OK days), `first_and_interior`, `last_day_involved` (an excluded day is the account's last row in the window, whatever else);
  state `position_rule_in_words`. `excluded_days_per_account_distribution` (excluded-day count to accounts: 1, 2, 3-5, 6-20,
  more). `claim_the_reader_gives` (the reader's claim value to accounts, summing to the accounts with an excluded day) and
  `absences_named` (each absence fact and status the reader attaches, with counts).
- `status_values`: each status token in the served gold with its row count, per entry.
- One sentence per entry on what the non-OK status MEANS as the producer writes it (find where the holdings-performance
  producer sets it: `data/assets/scripts/gold/irpt_holdings_performance/`; cite file:line): is a non-OK row a day with no
  return by construction (the first day, a zero base), or a day whose return could not be computed.
- `control`: one account with no excluded day read the same way returns `days_excluded` 0 and the same claim value.
Running the reader once per account per window may be slow: read each partition ONCE into memory and feed the reader's own
functions from that cache (say exactly how you did it and that the reader's code, not a re-implementation, produced every
figure; if you had to re-implement a step, say which and check it against the reader on a sample of 50 accounts).

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~319/`: `IB160-1_reader_excluded_days.json` with
`{base_commit, arm: "READER_CODE_OVER_SERVED_GOLD", arm_in_words, windows_from_code, windows_code_line, per_entry_and_window:[{entry,
window, start, end, accounts_read, accounts_with_an_excluded_day, accounts_with_none, accounts_the_reader_refuses, refusals,
position_of_the_excluded_days:{four classes}, excluded_days_per_account_distribution, claim_the_reader_gives, absences_named}],
position_rule_in_words, status_values, what_a_non_ok_row_means, control:{what, reading}, not_established, functions_invoked:0,
sign_ins_made:0, aws_writes_made:0, accounts_written:0}`; your driver; and a one-page `IB160-1_READER_EXCLUDED_DAYS_READ.md`
with one table per entry, leading with the interior counts.

<criterion id="IB160-1-AC1" cell_refs="IB-pr-464"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r160/p160_cells.py" . IB160-1-AC1</invocation><expect>IB160-1-AC1 PASS</expect></criterion>
<criterion id="IB160-1-AC2" cell_refs="IB-pr-464"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r160/p160_cells.py" . IB160-1-AC2</invocation><expect>IB160-1-AC2 PASS</expect></criterion>
<criterion id="IB160-1-AC3" cell_refs="IB-pr-464"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r160/p160_cells.py" . IB160-1-AC3</invocation><expect>IB160-1-AC3 PASS</expect></criterion>

<expected_criteria>IB160-1-AC1, IB160-1-AC2, IB160-1-AC3</expected_criteria>

The checks grade the shape, the sums and the bounds. Every count and answer is UNMEASURED by the issuer; "none found" and
"cannot be told" pass where true.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited.
- **Refusal clause:** an AWS read refused (record it as a reading; never retry another way; seek no grant) or a criterion that
  cannot be met as written: file a row and report. Never weaken a check; do not edit `p160_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W319-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Scratch** in `C:/dev/_scratch319/`, outside the worktree, removed at the very end by a short bounded python script; if the
  cleanup hangs or errors, stop cleaning, say so, and still report.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~319" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~319@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~319 <0.9.0_WK_IRPT_BCKEND~319@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~319/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-464.route-reader-excluded-days-per-window.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 152 (round 160, workstream ~P), cell `IB-pr-464`.
<owned_cells>IB-pr-464</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB160-1-AC1, IB160-1-AC2, IB160-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~319/IRPT_BCKEND.TO-IB-pr-464.route-reader-excluded-days-per-window.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; the windows; per entry and window the account counts, the position classes, the claim the reader gives, the distribution; what a non-OK row means with its line; the control; what is not established; each criterion's last line; the proof checker's result; commit hashes; row ids; whether the scratch was cleaned.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read written to the worker's own deliverables folder; nothing is edited, built, invoked or served.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; reads only; a refused read is a reading.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; no deployed route is called.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p160_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~01:4xZ: every criterion of this order FAIL (no file); commit-gate clean. The issuer read IB-pr-459's merged record for Measurement 2 (the arm, the two status tokens, the 1Y window) and PRD v0.46's closing bullet. The account-id text test is not in this check (three false failures of that pattern on 2026-10-11); the bounds keep values out.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
