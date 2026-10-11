# TO IRPT_BCKEND.TO-IB-pr-427 -- Cottonwood's lagged closes graded BY ACCOUNT and by any custodian or source field: who is on their own date, who is a day behind, who is mixed (read only, counts only)

<to_id>IRPT_BCKEND.TO-IB-pr-427</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~286</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>125</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 4786, on IB-pr-425's read `deliverables/0.9.0_WK_IRPT_BCKEND~284/IB123-1_S252_READ.md` (drained @7aa373487b) | **Decomp cell:** `IB-pr-427` (decomposition section 118) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-286/` (bash `/c/dev/wk-irpt-bckend-286`). Work only there. **READ ONLY: S3 reads and local analysis. No
write to AWS, no deploy, no product source edit, no vendor call.**

**Where this stands.** IB-pr-425 graded every trading-day partition of Cottonwood's declared holdings source (`opal-data-assets`,
entry `blackdiamond_z09` of `data/assets/scripts/gold/irpt_holdings_performance/sources.json`) against the Schwab own-date anchor. Of
37,806 moved security-days, 2,514 read the PRIOR trading day's close and 361 read neither; per day the share at the prior close runs
from 0.0 to 59.0 percent, median 5.9. One CUSIP's rows disagree with each other on 50 of 85 days. So the date basis does not belong to
the security. The CTO ruled one more read before any basis is declared: by ACCOUNT, and by custodian or source field if the rows
carry one.

**Reuse IB-pr-425's work.** Read `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~284/` first: `IB123-1_S252_READ.md`,
`IB123-1_s252_all_partitions.json` and its instrument scripts. Copy what you need into your folder and extend the copy; leave that
folder untouched. Keep its tolerance, its anchor, its definition of "moved" and its ROW-level grading (every row graded, never one
price per CUSIP). Your row totals over the same 85 graded days should reconcile with its security-day totals; say how (a security-day
with several rows is several rows here), and if they do not reconcile, say by how much and why.

**Build:**
1. **Per account.** For every account in the partitions: over the graded days, its moved rows at the own close, at the prior close
   and at neither. Class each account: `always_own` (0 prior rows, at least one moved row), `always_prior` (every moved row that is
   own-or-prior is prior), `mixed` (both), `no_moved_rows`. Report the counts of accounts per class, the moved rows per class, and
   the distribution of the per-account share at the prior close (how many accounts at 0, up to 1, 1 to 10, 10 to 50, 50 to 99, and
   100 percent). For the `mixed` accounts say whether the mixing is BY DAY (the account is behind on some days and current on
   others) or WITHIN a day (some of its securities behind on the same day), with counts.
2. **Per field.** List the columns the partition rows carry. For every column that could name a custodian, a data source, a feed or
   an account type (name each you considered and why you took or left it), the same own / prior / neither split per value, with the
   number of accounts per value. A lag that follows a custodian is a feed's date. A value is a category label; if a column's values
   are account-specific, it is not a field split and is left out with that reason.
3. **The "neither" rows** (IB-pr-425 read 361 security-days): split by account class, and by each field of step 2.
4. **Time.** The per-day count of accounts that are behind, so a reader sees whether the same accounts are behind day after day or a
   set that changes; and whether the four heavy days IB-pr-425 named (2026-10-01, 2026-09-03, 2026-07-02, 2026-07-31) are many accounts
   at once.
5. **The planted control again:** a synthetic fixture with ONE planted lagged account (labelled, for example, `ACCT_PLANTED`) among
   clean ones, and a clean copy. The instrument reports the planted account alone, and nothing on the clean copy.
6. **Outputs**, both under `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~286/`:
   - `IB125-1_lag_by_account.json`: `{source, tolerance, days_graded, rows:{moved, own, prior, neither},
     accounts:{read, always_own, always_prior, mixed, no_moved_rows}, rows_by_account_class:{always_own:{moved, own, prior,
     neither}, always_prior:{...}, mixed:{...}}, account_share_distribution:{...}, mixed_accounts:{by_day, within_day, both},
     by_field:[{field, values:[{value, accounts, moved, own, prior, neither}]}], by_field_absent_reason,
     neither_by_account_class:{always_own, always_prior, mixed}, accounts_behind_per_day:[{date, accounts_behind, accounts_with_moved_rows}],
     control:{planted_account_label, reported:[...], clean_fixture_reported:[...]}, reconciliation_with_IB_pr_425}`.
     Every `{moved, own, prior, neither}` block satisfies `own + prior + neither == moved`; each field's values sum to `rows.moved`.
   - `IB125-1_LAG_BY_ACCOUNT_READ.md`: one page for the CTO. The account split in one table; the field split; what the mixing is;
     whether the lag is a property of the account, of a field value, of the day, or of none of these; and what you did NOT measure.
     Standard technical English, short sentences. Do not propose the basis declaration.

**NO ACCOUNT ID IN ANY OUTPUT.** Account ids are read in memory to group rows and are never written: not to a committed file, not to
a log you commit, not into your final message. Accounts appear only as counts. (Black Diamond's account ids carry the prefix `z09`;
the check greps both outputs for it.) Balances and position values never leave memory either. Downloaded partitions stay OUTSIDE the
worktree (for example `C:/dev/_scratch286/`) and are deleted file by file at the end.

<criterion id="IB125-1-AC1" cell_refs="IB-pr-427"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r125/p125_cells.py" . IB125-1-AC1</invocation><expect>IB125-1-AC1 PASS</expect></criterion>
<criterion id="IB125-1-AC2" cell_refs="IB-pr-427"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r125/p125_cells.py" . IB125-1-AC2</invocation><expect>IB125-1-AC2 PASS</expect></criterion>
<criterion id="IB125-1-AC3" cell_refs="IB-pr-427"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r125/p125_cells.py" . IB125-1-AC3</invocation><expect>IB125-1-AC3 PASS</expect></criterion>

<expected_criteria>IB125-1-AC1, IB125-1-AC2, IB125-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Read only on AWS. Do not edit `sources.json`, the gold script, or any other
  worker's folder.
- **Do not propose or make the basis declaration.** This cell measures; the CTO rules on its table.
- **Refusal clause:** a day or an account that cannot be graded is counted and reasoned, never dropped. If a criterion cannot be met
  as written, stop, file a row and report. Never weaken a check; do not edit `p125_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W286-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; check the id is free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~286" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~286@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~286 <0.9.0_WK_IRPT_BCKEND~286@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~286/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-427.cottonwood-lag-by-account.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 118 (round 125, workstream ~P), cell `IB-pr-427`.
<owned_cells>IB-pr-427</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB125-1-AC1, IB125-1-AC2, IB125-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~286/IRPT_BCKEND.TO-IB-pr-427.cottonwood-lag-by-account.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, counts only: accounts per class and the moved rows per class; the share distribution; what the
mixing is; each field you split by and whether the lag follows it; the neither rows' split; whether the heavy days are many accounts
at once; how your totals reconcile with IB-pr-425's; what you did NOT measure; each criterion's last line; the proof checker's
result; any row ids; what scratch remains.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only measurement; nothing is built, deployed or written to AWS.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p125_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~11:1xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no output file); commit-gate clean.
lane: the <paths> block IS the grant; ~P's holdings-basis thread.
</preflight>
