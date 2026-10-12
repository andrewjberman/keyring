# TO IRPT_BCKEND.TO-IB-pr-468 -- READ ONLY: rebuild the 878-ticker list and write the request file for dell1's demand queue (as-traded closes, 125 trading days, then daily)

<to_id>IRPT_BCKEND.TO-IB-pr-468</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~323</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>162</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6362 (on `1.0.0_SA_CTO~DELL1`'s ruling @479d6deba0) | **Decomp cell:** `IB-pr-468` (decomposition section 154) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-323/` (bash `/c/dev/wk-irpt-bckend-323`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it). **A READ AND ONE RECORD, NOT A BUILD.** You edit no product file.

**Why.** The date-basis grading needs each security's as-traded close (the vendor's Close with later splits undone) on landed,
scheduled bars. This fabric builds no lander. Another fabric's demand queue lands them: it takes a REQUEST FILE, quotes it,
then runs it. This cell writes that request file for the 878 tickers the earlier cells counted. **You fetch NO price and call
NO vendor: not Yahoo, not any other.** The list was never committed, only its count; you rebuild it.

**Rebuild the list.** The 878 tickers are the population of IB-pr-459 (record
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~315/IB155-1_TWO_MEASUREMENTS_READ.md`, driver
`ib155_measure.py` beside it, which loads `tickers.json` from a scratch folder that no longer exists). That file was written by
the chain of drivers in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~310/` (`ib150_overlap_tickers.py`
and what it names) and `0.9.0_WK_IRPT_BCKEND~308/` (`ib442_phase1.py`, `ib442_prepare.py`, `ib452_tickers.py`). Read their
docstrings and the two workers' READ files, then run ONLY the steps that derive the ticker list (S3 gets and lists of the
landed holdings and transactions the drivers themselves address; cache in `C:/dev/_scratch323/`, outside the worktree; each
step under its own timeout; state the denominator of partitions read). Do NOT run any `*fetch_yahoo*` or `*fetch_nav*` step.
Read the SAME partitions those cells read (their records state the window); the list must come to exactly 878 distinct
symbols. If it does not, do not force it: report the count, the symbols gained or lost as COUNTS, and why, file a row, and
leave the order pending.

**For each symbol** also carry its `cusip` where the landed data gives one for that symbol (say from which column, file:line
of the driver that maps them); where it gives none, write `"cusip_claim": "absent"` and no `cusip` key. Count symbols whose
cusip maps to more than one symbol or the reverse, and say so in the record; write the pair the drivers themselves used.

**The dates.** `end` = the last trading day at or before 2026-10-09; `start` = the trading day such that start to end
inclusive is 125 trading days. Take both from `lib/trading_calendar.py` (read it; state the function used in
`calendar_rule_in_words`), never by counting weekdays.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~323/`:
1. `IRPT_BCKEND-AS-TRADED-CLOSES-878.json`, the request, in the queue's format:
   `{"request_id": "IRPT_BCKEND-AS-TRADED-CLOSES-878", "standing": false, "tier": 2, "reason": "<one sentence: PRD v0.46
   answer 1, the date-basis grading's second witness needs as-traded closes on landed bars; ruling
   CTO_RULING_DELL2_AS_TRADED_CLOSES_VIA_DEMQUE_20261012.md @479d6deba0>", "page": "investor reporting (IRPT_BCKEND date-basis
   grading)", "vendor": "yahoo", "securities": [{"cusip": "...", "symbol": "..."}, ...], "fields": ["close"], "start":
   "YYYY-MM-DD", "end": "YYYY-MM-DD", "standing_enrolment": {"tier": 1, "in_words": "enrol the same 878 securities in the
   standing daily extension to the T-1 frontier after the history lands"}, "filed_for": "IRPT_BCKEND", "requested_by":
   "2.0.0_SA_COO~P2", "authority": "1.0.0_SA_CTO~DELL2 msg 6362; 1.0.0_SA_CTO~DELL1 ruling @479d6deba0"}`. Securities sorted
   by symbol. Security identifiers only: NO account, NO firm name, NO value.
2. `IB162-1_request_derivation.json`: `{base_commit, tickers_derived, with_a_cusip, cusip_absent,
   cusips_mapping_to_more_than_one_symbol, symbols_mapping_to_more_than_one_cusip, derivation_in_words (the steps run, with
   file names), partitions_read, start, end, trading_days_start_to_end_inclusive, calendar_rule_in_words, not_established,
   prices_fetched:0, vendor_calls_made:0, functions_invoked:0, sign_ins_made:0, aws_writes_made:0, accounts_written:0,
   values_written:0}`.
3. Your driver.

Remove the scratch at the very end with a short bounded python script; if it hangs or errors, stop cleaning, say so, and
still report.

<criterion id="IB162-1-AC1" cell_refs="IB-pr-468"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r162/p162_cells.py" . IB162-1-AC1</invocation><expect>IB162-1-AC1 PASS</expect></criterion>
<criterion id="IB162-1-AC2" cell_refs="IB-pr-468"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r162/p162_cells.py" . IB162-1-AC2</invocation><expect>IB162-1-AC2 PASS</expect></criterion>

<expected_criteria>IB162-1-AC1, IB162-1-AC2</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited. The request file stays in YOUR folder: you do
  not file it with the queue and you write nothing on another fabric's branch.
- **Refusal clause:** a list that does not reproduce 878, an AWS read refused, or a criterion that cannot be met as written:
  file a row and report. Never weaken a check; do not edit `p162_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W323-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~323" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~323@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~323 <0.9.0_WK_IRPT_BCKEND~323@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~323/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-468.demand-queue-request-878-as-traded-closes.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 154 (round 162, workstream ~P), cell `IB-pr-468`.
<owned_cells>IB-pr-468</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB162-1-AC1, IB162-1-AC2. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~323/IRPT_BCKEND.TO-IB-pr-468.demand-queue-request-878-as-traded-closes.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; the steps run and partitions read; the count derived (and the difference if not
878); cusip coverage and the two many-to-one counts; start, end and the calendar rule; that no price was fetched; what is not
established; each criterion's last line; the proof checker's result; commit hashes; row ids; whether the scratch was cleaned.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; one record written to the worker's own deliverables folder; nothing is edited, built, invoked or served.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; S3 reads the earlier cells already made.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched on this fabric; the daily enrolment is asked of another fabric's queue, which quotes it before it runs.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p162_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~02:4xZ: AC1 FAIL, AC2 FAIL (no file); commit-gate clean. The queue's format was read by the issuer from two request files on origin/box/dell1 and from the ruling @479d6deba0. The file is carried to 2.0.0_SA_COO~Q1 by 0.0.0_AB_MSTR~DELL2 after the drain; the quote goes to the CTO. CTO msg 6362: nothing on dell2 fetches a price.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
