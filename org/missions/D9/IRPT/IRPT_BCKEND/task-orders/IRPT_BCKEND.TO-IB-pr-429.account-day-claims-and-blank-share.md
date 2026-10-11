# TO IRPT_BCKEND.TO-IB-pr-429 -- the per account-day date-basis claim, counted: OWN_DATE, PRIOR_CLOSE, NOT_GRADED, and the share of account-days the serving rule blanks (read only, counts only)

<to_id>IRPT_BCKEND.TO-IB-pr-429</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~288</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>127</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 4825 (the basis is declared per account-day as a measured claim; "Before the addendum, one paragraph: what the instrument needs daily to grade, and the share of account-days this blanks"), on IB-pr-427's read `deliverables/0.9.0_WK_IRPT_BCKEND~286/IB125-1_LAG_BY_ACCOUNT_READ.md` (drained @ea10544bdf) | **Decomp cell:** `IB-pr-429` (decomposition section 120) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-288/` (bash `/c/dev/wk-irpt-bckend-288`). Work only there. **READ ONLY: S3 reads and local analysis. No
write to AWS, no deploy, no product source edit, no vendor call.**

**The ruling you are counting (CTO msg 4825).** Cottonwood's holdings gold will carry, per ACCOUNT-DAY, a date-basis claim that the
grading instrument measured:
- `OWN_DATE`: the account's moved, priced rows that day are at the day's own close;
- `PRIOR_CLOSE`: they are at the prior trading day's close;
- `NOT_GRADED`: no moved security to grade that day, or a "neither" row.
A return is SERVED for an account-day only when that account-day AND the same account's prior trading day both read `OWN_DATE`.
Otherwise the day is BLANK, with the reason. Nothing is shifted or repaired. The CTO does not key on the `Account Supervised` column.

The CTO asks two things before the PRD addendum: what the instrument needs every day to grade, and the share of account-days this
rule blanks. You answer both with counts.

**Reuse.** Read `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~286/` first (the read, the JSON, the instrument
scripts) and `deliverables/0.9.0_WK_IRPT_BCKEND~284/`. Copy what you need into your own folder and extend the copy; leave those folders
untouched. Same source (`blackdiamond_z09` of `data/assets/scripts/gold/irpt_holdings_performance/sources.json`), same anchor, same
tolerance, same definition of "moved", same row-level grading, same 85 graded days. Your row totals must reconcile with IB-pr-427's
(583,996 moved rows, 3,278 prior, 1,903 neither); say so, or say by how much they differ and why.

**Build:**
1. **One claim per account-day.** For every account present in a graded day's partition, one claim. State your rule for an
   account-day that holds a mix, and apply the CTO's words literally where they decide it: a "neither" row makes the account-day
   `NOT_GRADED`; an account-day with at least one prior-close row and no neither row is `PRIOR_CLOSE`; an account-day whose moved,
   priced rows are all at the own close is `OWN_DATE`; an account-day with no moved, priced row is `NOT_GRADED`. Split `NOT_GRADED` by
   reason: `no_moved_security`, `neither_row`, and any other reason you meet, each named.
2. **The serving rule.** An account-day is ELIGIBLE when the account is present that day and on the prior trading day (the first
   graded day of the range has its prior partition, 2026-06-09, which is itself ungraded: count how you treat it and say so). Count
   eligible account-days, those SERVED (today and the prior trading day both `OWN_DATE`) and those BLANK, the blanks split by reason:
   `today_PRIOR_CLOSE`, `today_NOT_GRADED`, `yesterday_PRIOR_CLOSE`, `yesterday_NOT_GRADED` (when two apply, take the first in that
   order and say so). State `blank_share_percent`. Then per ACCOUNT: how many accounts have eligible days; how many are never served,
   always served, sometimes served; and the distribution of the per-account served share.
3. **Why so many NOT_GRADED, if it is so.** IB-pr-427 read 386 of 1,000 accounts with no moved row on any day. For the accounts and
   account-days that are `NOT_GRADED` for `no_moved_security`, say by counts what they hold instead: no priced row at all, only cash
   or cash-equivalent rows, only securities the anchor does not carry, or securities that did not move that day. This is the number
   the CTO needs most: an account whose days are never graded is never served under this rule.
4. **What the instrument needs daily.** For the gold to stamp a claim on day D, list each input it needs, where it comes from and by
   when it exists: the account's partition for D and for the prior trading day; the anchor's close for D and for the prior trading
   day (name the anchor source and read when its D partition lands relative to the Cottonwood partition for D, from object
   timestamps on a handful of recent days, counts and times only); the trading calendar. Say which of these is the binding one, that
   is, the one that arrives last.
5. **A control.** A small synthetic fixture where the correct counts are known by construction (for example 3 accounts over 4 days
   with one planted prior-close day and one planted neither row): `control: {planted: {served, blank, OWN_DATE, PRIOR_CLOSE,
   NOT_GRADED}, read: {the same keys}}`, and the two are equal.
6. **Outputs**, under `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~288/`:
   - `IB127-1_account_day_claims.json`: `{source, tolerance, days, accounts, claim_rule, account_days:{present, OWN_DATE, PRIOR_CLOSE,
     NOT_GRADED}, not_graded_by_reason:{...}, not_graded_holdings_breakdown:{...}, serving_rule:{eligible, served, blank,
     blank_by_reason:{...}, blank_share_percent, first_day_treatment, accounts:{with_eligible_days, never_served, always_served,
     sometimes_served}, per_account_served_share_distribution:{...}}, instrument_daily_needs:[{need, where_from, by_when}],
     binding_need, control:{planted:{...}, read:{...}}, reconciliation_with_IB_pr_427}`.
   - `IB127-1_ACCOUNT_DAY_CLAIMS_READ.md`: ONE PAGE for the CTO. Its first paragraph is the paragraph he asked for: what the instrument
     needs daily, and the share of account-days the rule blanks, in plain sentences with the two or three numbers that matter. Then
     the tables. Then what you did NOT measure. Standard technical English, short sentences. Do not propose a change to the ruling.

**NO ACCOUNT ID IN ANY OUTPUT.** Account ids are read in memory to group rows (digest them at read time, as IB-pr-427 did) and are never
written anywhere. Accounts appear only as counts. Balances and position values never leave memory. Downloaded partitions and any
intermediate file stay OUTSIDE the worktree (for example `C:/dev/_scratch288/`) and are deleted file by file at the end.

<criterion id="IB127-1-AC1" cell_refs="IB-pr-429"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r127/p127_cells.py" . IB127-1-AC1</invocation><expect>IB127-1-AC1 PASS</expect></criterion>
<criterion id="IB127-1-AC2" cell_refs="IB-pr-429"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r127/p127_cells.py" . IB127-1-AC2</invocation><expect>IB127-1-AC2 PASS</expect></criterion>
<criterion id="IB127-1-AC3" cell_refs="IB-pr-429"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r127/p127_cells.py" . IB127-1-AC3</invocation><expect>IB127-1-AC3 PASS</expect></criterion>

<expected_criteria>IB127-1-AC1, IB127-1-AC2, IB127-1-AC3</expected_criteria>

## AMENDMENT 1 (2026-10-11 ~11:4xZ, issuer 2.0.0_SA_COO~P2, on CTO msg 4833): NOT_GRADED is two different things; the ruling of msg 4825 is HELD

The CTO read the 386 of 1,000 accounts with no moved row and HELD his ruling: it is not in force and nothing is built on it. His rule
folded two cases into `NOT_GRADED`. This cell is still the right read. It keeps counting the rule AS WRITTEN (steps 1 and 2 are
unchanged, so the CTO sees what msg 4825 would have done) and ADDS one split, which is the table he rules on:
- **Every `NOT_GRADED` account-day is classed as exactly one of:**
  - `nothing_to_grade`: nothing in the account that day could be on the wrong date. Its value is the same on either basis. Holdings
    classes: `cash_only` (only cash or cash-equivalent rows), `did_not_move` (priced securities the anchor carries, none of which
    moved that day), `no_priced_row` (no row with a price at all), or a mix of only these.
  - `ungradeable`: the account-day holds at least one priced security the instrument cannot grade. Holdings classes:
    `outside_anchor` (a priced security the anchor does not carry), `neither_row` (a moved row at neither close), or any other
    reason you meet, each named.
  An account-day that holds both kinds is `ungradeable`, under the class of what makes it so. State that rule.
- **Output field** `not_graded_split: {nothing_to_grade: {account_days, by_holdings_class:{...}}, ungradeable: {account_days,
  by_holdings_class:{...}}}`. Each `by_holdings_class` sums to its `account_days`; the two `account_days` sum to
  `account_days.NOT_GRADED`.
- **Also count the alternative the CTO describes**, beside the rule as written and clearly labelled as NOT the rule in force:
  `serving_rule_alternative: {description, eligible, served, blank, blank_by_reason, blank_share_percent, accounts:{...}}`, where an
  account-day is good when it reads `OWN_DATE` or is `nothing_to_grade`, and a return is served when today and the prior trading day
  are both good. The read's first paragraph gives BOTH blank shares.
- The read does not say which rule is right.

Gate limb: GATE (viii) grades this modified order (placeholders NONE).

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Read only on AWS. Do not edit `sources.json`, the gold script, or another worker's
  folder.
- **Do not change or second-guess the ruling.** You count what it does. If the count shows something the CTO should see (for example a
  large share of accounts never served), it goes in the first paragraph of the read as a number, not as a proposal.
- **Refusal clause:** an account-day you cannot claim is counted under a named `NOT_GRADED` reason, never dropped. If a criterion
  cannot be met as written, stop, file a row and report. Never weaken a check; do not edit `p127_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W288-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; check the id is free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~288" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~288@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~288 <0.9.0_WK_IRPT_BCKEND~288@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~288/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-429.account-day-claims-and-blank-share.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 120 (round 127, workstream ~P), cell `IB-pr-429`.
<owned_cells>IB-pr-429</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB127-1-AC1, IB127-1-AC2, IB127-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~288/IRPT_BCKEND.TO-IB-pr-429.account-day-claims-and-blank-share.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, counts only: the account-day claims; NOT_GRADED by reason and what those accounts hold; eligible,
served and blank with the blank share and the blanks by reason; accounts never / always / sometimes served; the instrument's daily
needs and the binding one; how you treated the first day and mixed account-days; the reconciliation; what you did NOT measure; each
criterion's last line; the proof checker's result; any row ids; what scratch remains.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only measurement; nothing is built, deployed or written to AWS.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the cell reads object timestamps to say when the instrument's inputs exist.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p127_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~11:4xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no output file); commit-gate clean.
lane: the <paths> block IS the grant; ~P's holdings-basis thread.
</preflight>
