# TO IRPT_DASHBD.TO-DB-b-33 -- E1: build `account_class_daily` (the class contribution) for 49 Financial and its contract, run it locally over a bounded sample; the served release is a separate act (FWD-3)

<to_id>IRPT_DASHBD.TO-DB-b-33</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~18</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-20 analysis @58f3ed0501 item E1 ("(1) the
per-class daily contributions sum to the account's daily return within 1e-9 on every account-day; (2) unclassified holdings are their own
class, never folded into another; (3) only the six-class vocabulary appears (cash, fixed income, equity, structured, alternatives,
commodities)"; risk SERVED, "a gold producer under rule 13; its release carries its own halves") | **Decomp cell:** `DB-b-33`
(decomposition section 21) | **outcome_ref:** FWD-3 | **depends_on:** the six-class values in `_shared/etf_classification.py`
(@63fa1a2e32, the gate the analysis names as open).

This order BUILDS and RUNS LOCALLY. It writes nothing to S3, deploys nothing and schedules nothing. The served release (upload of the
producer, its first gold write, its schedule) is the next cell, under never-widen halves, once this one drains.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-18`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~18/`.

**The cell (`DB-b-33`).** PRD C-SHAPE names `account_class_daily` as one of the eight account-grain gold tables; C-CLASSES says
`class_return_daily` is the class's contribution to the account's daily return, "so classes sum to the account", and "No row means
UNCLASSIFIED; nothing is guessed." Build it for 49 Financial.

**Where the figures come from.**
- The account's daily return is the served producer's: `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (1,953 lines;
  read it, DO NOT EDIT it -- it is packaged unedited into the live `irpt-49f-reporting-gold-lambda`). Its handler,
  `infra/aws/lambda/investor-reporting/reporting-gold/handler.py`, shows how to compose its functions without calling `main()`
  (`load_declaration`, `firm_scope`, `first_data_dates`, `prefetch`, `compute_range`). Find, in that producer, the position-level market
  values it reads (its comments cite `dim_position`) and the account's numerator and denominator for each day.
- Classes come from `infra/aws/lambda/v2_portal/_shared/etf_classification.py` (six-class values since @63fa1a2e32). **Two traps in
  that module, both forbidden by the cell:** `get_asset_class(ticker, default='equity')` returns `'equity'` for a ticker it does not
  know, which is a GUESS; and it maps `CASH_USD` to `'fixed_income'`. So: look the ticker up with a sentinel default (or read its
  dictionaries) and send any ticker it does not name to `unclassified`; send every cash position to `cash`.

**The method (so the classes sum to the account EXACTLY).** For each account-day the producer measures, with `D_t` the account's own
return denominator from the producer and `MV_c` the class's summed position market value:
`class_return_daily_c,t = (MV_c,t - MV_c,t-1 - NF_c,t) / D_t`, where `NF_c,t` is the net trade flow into class c on day t (buys minus
sells, from the producer's transaction source) for every non-cash class, and for `cash` `NF_cash,t = external_flow_t - sum of the other
classes' NF`. The class market values must sum to the account's market value on each day; where they do not, the day is not measurable
for classes and carries null with a `coverage` reason. Income lands in cash under this method: say so in the contract as a limit of
`method_version` 1. If the producer's numerator differs from `MV_t - MV_t-1 - external_flow_t`, adapt the class numerator so the identity
holds, and write the adaptation in the contract.

**What you build:**
1. `data/assets/scripts/gold/irpt_reporting/account_class_daily.py`: a producer beside `account_return_daily.py` that imports it
   read-only. It has a `--local` mode that computes a sample and writes local parquet plus the record below, and it never writes S3.
   Columns at least: `firm`, `account_id`, `business_date`, `asset_class`, `market_value_eod`, `class_return_daily`, `method_version`,
   `coverage`.
2. `data/assets/scripts/gold/irpt_reporting/tests/test_account_class_daily.py`: offline tests on synthetic positions: the identity holds;
   an unknown ticker goes to `unclassified`; a cash position goes to `cash`; a day whose class values do not sum to the account is null
   with a coverage reason.
3. `org/standards/IRPT_DASHBD_ACCOUNT_CLASS_DAILY_CONTRACT.json`, in the shape of
   `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json`: `columns` (the produced order), `class_enum` (exactly cash,
   fixed_income, equity, structured, alternatives, commodities, unclassified), the source of the classes and its pin, the method and its
   limits. It supersedes the portal-type authority of PRD ruling 13 by citing `@63fa1a2e32`.
4. One local run over a bounded sample: account `acct#737d1020` (the PRD's C-NAMES example) plus at least 49 other accounts from the producer's population,
   over the five trading days 2026-09-29 to 2026-10-05. Write `CLASS_DAILY_LOCAL_RUN.json` in your folder with `columns` (the parquet's
   column list), `account_days` (`{account_id, business_date, account_daily_return}` for every MEASURED account-day, the producer's own
   figure), `class_rows` (`{account_id, business_date, class, class_return_daily}`) and `holding_map` (`{ticker, module_class (null when
   the module does not name it), is_cash, class}` for every distinct holding seen). Write a summary `CLASS_DAILY_LOCAL_RUN.md`, COUNTS
   ONLY. The JSON may carry figures; keep it under 5 MB.

<criterion id="DB21-1-AC1" cell_refs="DB-b-33"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r21/p21_class_daily.py" . DB21-1-AC1</invocation><expect>DB21-1-AC1 PASS</expect></criterion>
`DB21-1-AC1` -- on every measured account-day of the run (at least 50), the classes sum to the account's daily return within 1e-9.
Base: FAIL.

<criterion id="DB21-1-AC2" cell_refs="DB-b-33"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r21/p21_class_daily.py" . DB21-1-AC2</invocation><expect>DB21-1-AC2 PASS</expect></criterion>
`DB21-1-AC2` -- the seven-value vocabulary only; an unnamed ticker is `unclassified`, a cash position is `cash`, nothing else is
reassigned. Base: FAIL.

<criterion id="DB21-1-AC3" cell_refs="DB-b-33"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r21/p21_class_daily.py" . DB21-1-AC3</invocation><expect>DB21-1-AC3 PASS</expect></criterion>
`DB21-1-AC3` -- the contract file's enum is the seven values and its columns equal the produced table's, including firm, account_id,
method_version and coverage. Base: FAIL.

<expected_criteria>DB21-1-AC1,DB21-1-AC2,DB21-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Do not edit `account_return_daily.py`, its handler, or `_shared/etf_classification.py`.
- **AWS:** S3 reads only (the producer's own sources; all read from this box). No write, no upload, no Lambda, no schedule, no
  vendor call.
- **Refusal clause.** An S3 write, an edit to the served producer, a guessed class, or a client figure in a committed `.md` is a defect:
  stop and file a row.

<paths>
data/assets/scripts/gold/irpt_reporting/account_class_daily.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_class_daily.py
org/standards/IRPT_DASHBD_ACCOUNT_CLASS_DAILY_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~18/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-33.account-class-daily-build.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 21 (round 21, workstream B), cell `DB-b-33`.
<owned_cells>DB-b-33</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB21-1-AC1, DB21-1-AC2, DB21-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~18/IRPT_DASHBD.TO-DB-b-33.account-class-daily-build.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB21-1-AC1,DB21-1-AC2,DB21-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the sample (accounts, days, measured account-days, not-measurable account-days by
reason), the class counts, the unclassified tickers, the method adaptation if any, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED -- a new producer file beside the served one; the served producer, its handler and its Lambda are not touched; 0 served bytes move in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only from dell2 (both firm buckets read since the fence join @aefcf32c11); no role change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the release cell adds one under its halves.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB21-1-AC1, AC2 and AC3 base FAIL (no record, no contract), dry-run at base 09f7e2ab87 2026-10-07 ~11:4xZ.
lane: the <paths> block IS the grant; rule 13 (DS owns commit -> QA-deploy for gold scripts) binds the release cell, not this build.
</preflight>
