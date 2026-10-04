# AMGT_CORPUS task order -- `CRPS-aj-1` -- ROUND 34: the daily Model-block refresh, carrying the V3 set, the long name and the earnings dates

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-aj-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN by the issuer at the cut (`comp-schedule --owner 2.0.0_SA_COO~X`, 21:2xZ): GATES ARMED 0 on this lane (C1 30, C2 28, C3 12 reached). The cell EDITS the entry an existing Scheduled Task (amgt-induction-daily, daily 13:00Z) runs; that task runs a PINNED checkout (opal-pinned/amgt-induction-daily/33c1d096a343), so nothing this cell commits runs until the issuer re-pins it in CRPS-aj-2. No new cron, alarm, monitor or task.
comp-iam: DECLARED-NOT-APPLICABLE -- no new boto3 call class; S3 list/get on the existing harvest bucket through the producer's own client, the same reads `admit --dry-run` makes today (measured at the cut: 3.5 s, rc 0).
comp-adversary: RUN by the issuer at the cut on CLOUD 6527a03cc1 -- aj1_check.py build 0/5 control 3/3; aj1_refresh_dry.sh FAIL (no `refresh` stage); aj1_sched_dry.sh FAIL (no refresh step line). Blind spot: no check here opens a Bloomberg session, so a field's servability and its request type are first read on the issuer's scripted fire (CRPS-aj-2).
EGRESS CLASS, declared: AWS-INTERNAL READ ONLY (S3 list/get). NO Bloomberg call, NO vendor call, NO write to S3.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 34. You build the producer change only. The issuer runs it for real later.

## 1. THE CELL -- `CRPS-aj-1`

Andrew approved ONE daily Bloomberg pull that refreshes every name's Model block and adds three things to it: the 49 "V3" template
fields, a long-name field and the earnings dates. Today the daily task only pulls names that have NO block yet (`admit`), so every
existing block is stale. Build the change in two files.

**A. `integrations/bloomberg/research/model_block_pull.py`**

1. **APPEND these 52 mnemonics** to the field lists, at the END of each list. Never re-order or remove a base member: every base
   index stays where it is.
   - To `FORECAST_FIELDS` (1): `BEST_CPS`. It rides the existing `BEST_FPERIOD_OVERRIDE` 1FY/2FY/3FY requests. Never list
     `BEST_FPERIOD_OVERRIDE` itself as a field.
   - To `HEADER_FIELDS` (7): `SHORT_NAME`, `COUNTRY_FULL_NAME`, `AVG_DAILY_VALUE_TRADED_3M`, `CRNCY_ADJ_MKT_CAP`,
     `LONG_COMP_NAME`, `EXPECTED_REPORT_DT`, `ERN_ANN_DT_AND_PER`.
   - To `HIST_FIELDS` (44): `ARD_GOODWLL`, `ARD_OTHER_INTANGIBLE_ASSET`, `ARD_SHARES_OUTSTANDING`,
     `ARD_TOTAL_CURRENT_LIABILITIES`, `ARD_TOT_ASSETS`, `AVERAGE_DIVIDEND_YIELD`, `AVERAGE_EV_TO_T12M_EBIT`,
     `AVERAGE_EV_TO_T12M_SALES`, `AVERAGE_PRICE_EARNINGS_RATIO`, `AVERAGE_PRICE_TO_BOOK_RATIO`,
     `AVERAGE_PRICE_TO_FREE_CASH_FLOW`, `AVG_EV_TO_T12M_EBITDA`, `CAPEX_ABSOLUTE_VALUE`, `CASH_AND_MARKETABLE_SECURITIES`,
     `CF_CASH_FROM_OPER`, `DIVIDEND_YIELD`, `EARN_FOR_COMMON`, `EQY_FUND_YEAR`, `EV_TO_T12M_EBIT`, `EV_TO_T12M_EBITDA`,
     `EV_TO_T12M_SALES`, `FCF_MARGIN_AFTER_OPER_LEA_PYMT`, `FREE_CASH_FLOW_PER_SH`, `HIGH_CLOSING_PRICE_TO_BOOK_RATIO`,
     `HIGH_DIVIDEND_YIELD`, `HIGH_EV_TO_T12M_EBIT`, `HIGH_EV_TO_T12M_EBITDA`, `HIGH_EV_TO_T12M_SALES`,
     `HIGH_PRICE_TO_FREE_CASH_FLOW`, `HISTORICAL_MARKET_CAP`, `LOW_CLOSING_PRICE_TO_BOOK_RATIO`, `LOW_DIVIDEND_YIELD`,
     `LOW_EV_TO_T12M_EBIT`, `LOW_EV_TO_T12M_EBITDA`, `LOW_EV_TO_T12M_SALES`, `LOW_PRICE_TO_FREE_CASH_FLOW`,
     `MINORITY_NONCONTROLLING_INTEREST`, `NORMALIZED_ROA`, `NORMALIZED_ROE`, `PX_ERN_RATIO_WITH_HIGH_CLOS_PX`,
     `PX_ERN_RATIO_WITH_LOW_CLOS_PX`, `SHORT_AND_LONG_TERM_DEBT`, `TANG_BOOK_VAL_PER_SH`, `TOTAL_EQUITY`.
   - The 49 V3 fields are measured, not chosen: the team template's 96 core mnemonics (`python -m lib.research.corpus.typecast
     --read-latest`) minus the 66 fields the producer pulls at the base. Do not add or drop a name on your own reading.
2. **Give each of the 52 a `FIELD_BASIS` entry**, in the module's existing style: Bloomberg's own definition in plain words, the
   unit stated where Bloomberg states one. Never name another vendor. A date field says it is a date.
3. **Keep the existing refusal path for a field Bloomberg does not serve.** `stage_derive` already sends an empty header value to
   `unresolved` with the text from `__field_errors__`. Keep that path, and make it hold for every new header field. A HIST or
   FORECAST field that never appears in Bloomberg's rows follows the path those loops already have. Never fill a value, never
   guess a request type, never drop a field silently.
4. **`ERN_ANN_DT_AND_PER` is a BULK field.** `blp_client` returns it as a LIST of row dicts, like `CIE_DES_BULK`. The raw landing
   stays untouched. At derive, its figure's `value` is a list of `{"announcement_date": "YYYY-MM-DD", "period": <Bloomberg's
   period text>}` objects, in Bloomberg's own row order. Read the column names from the row dicts rather than typing them, and
   normalise the date to ISO. A row whose date cannot be read is left out, and the count left out goes in the figure's
   `basis`. An empty or absent list goes to `unresolved` with its reason.
5. **Add a stage `refresh` (`python integrations/bloomberg/research/model_block_pull.py refresh [--dry-run]`)**, modelled on
   `cmd_admit`:
   - Name the function `cmd_refresh(dry_run=False)` and add `refresh` to `main()`'s stage choices. Like `admit`, `refresh` takes NO
     `--securities`: `ap.error` if one is given.
   - Population: `_registered_security_keys()` intersected with `_model_block_keys_in_store(s3)`, i.e. the registered names that
     HAVE a block.
   - First line: `refresh population registered <N> with_block <K>`.
   - Second line: `refresh fields header <len(HEADER_FIELDS)> hist <len(HIST_FIELDS)> forecast <len(FORECAST_FIELDS)>`.
   - Skip a name whose latest `derived/model_block/<key>/<stamp>/` was derived on today's UTC date. Print one `REFRESH SKIP: <key>
     already_current` line per skip. This stops the same run's `admit` and a same-day re-fire from pulling twice.
   - `--dry-run`: print `DRY-RUN REFRESH: <key> -> would pull then derive` per name. The LAST line is `refresh population
     registered <N> with_block <K> already_current <s> pulled 0 bloomberg_calls 0`. Return 0. Open NO Bloomberg session.
   - Real run: run the health check exactly as `cmd_admit` does. Unreachable -> print a REFUSED line and return 4. Then go in
     batches of at most `ADMIT_BATCH` (3): `stage_pull`, then `stage_derive`, per name, through `_CountingClient`. One name failing
     never hides the others. The last line is `refresh population registered <N> with_block <K> already_current <s> pulled <p>
     bloomberg_calls <c>`. Return 1 if any name failed, else 0.
   - Update the module docstring with one short `CRPS-aj-1 -- STAGE refresh` paragraph.

**B. `lib/research/corpus/induction_scheduled.py`**

6. After the admit step, run the refresh step the same way `run_admit_step` runs admit: `refresh --dry-run` in dry-run mode,
   `refresh` in fire mode. Announce `induction_scheduled step model_block_refresh rc <n>` AFTER the admit line and BEFORE the
   closing line. The closing rc is the worst of the three steps (induction, admit, refresh). Add one docstring sentence.
   - Known and NOT yours (row `AMGT_CORPUS-Z-S84`): in `--mode dry-run` both steps read rc 1, because `induction_run`'s dry run
     poisons `boto3.client`. Do not fix it and do not work around it.

**C. Tests.** Write `integrations/bloomberg/research/tests/test_model_block_round34.py`. Offline only: fake clients, never blpapi,
never boto3. It covers:
- the bulk `ERN_ANN_DT_AND_PER` derive (ISO dates, Bloomberg's order, an unreadable row left out and counted);
- a refused new header field reaching `unresolved` with Bloomberg's text;
- refresh's skip-if-current, its batching of at most 3, and its rc 4 on an unreachable DAPI;
- the dry-run printing zero calls.

If `test_model_block_admit.py` or `lib/research/corpus/tests/test_induction_schedule.py` assert the exact step lines, update them
for the new step and keep every other assertion.

## 2. BOUNDS

1. **NO Bloomberg call of any kind** -- not the script's real run, not an MCP tool, not a probe. A vendor call from an agent's turn
   FAILS this project's contract even when the value is right (PRD A.4 limit 1). Only `--dry-run` and offline tests run here.
2. No write to S3, no Scheduled Task change (`schedule_induction.ps1 -Register` is the issuer's act), no deploy, no push, no
   install. REFUSE, do not rescue.
3. Only the files in `<paths>` change. Never edit `field_map.json`, `build_unit_map.py` or a served object.
4. Write code with the Edit/Write tools, never a shell heredoc or `python -c`: a heredoc on this machine turns `\b` into a 0x08
   byte. ASCII only in code and logs.
5. Run the producer as `PYTHONPATH=<worktree root> python integrations/bloomberg/research/model_block_pull.py ...` (it imports
   `lib.research`).
6. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner
   2.0.0_SA_COO~X`.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_model_block_round34.py
integrations/bloomberg/research/tests/test_model_block_admit.py
lib/research/corpus/induction_scheduled.py
lib/research/corpus/tests/test_induction_schedule.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-aj-1.daily-refresh-producer.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-aj-1.daily-refresh-producer.md
</paths>

Read-only: the whole repository. In particular `integrations/bloomberg/mcp/blp_client.py` (`_el_to_py`, the bulk shape),
`integrations/bloomberg/READ_HERE.md` sections 3-4, `lib/research/corpus/schedule_induction.ps1` (read only, never run
`-Register`), and the issuer's checks under `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round34/` (never
edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-aj-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round34/aj1_check.py"; echo "exit=$?"</invocation><expect>(?m)^aj1 build 5/5 control 3/3$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-aj-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round34/aj1_refresh_dry.sh"</invocation><expect>(?m)^AJ1-REFRESH-DRY PASS </expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-aj-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round34/aj1_sched_dry.sh"</invocation><expect>(?m)^AJ1-SCHED-DRY PASS </expect></criterion>
</proof_of_spec>

- AC1 (offline):
  - build arms: the 49 V3 fields placed once each, the three name/earnings fields in the header list, `BEST_CPS` in the forecast
    list, a basis for every field, and a `refresh` stage;
  - control arms: no base field moved, admit and its caps unchanged, and the 3-security cap still refuses.
- AC2: `refresh --dry-run` against the real served store. Expect: K >= 94 names with a block, the field counts summing >= 118,
  and zero pulls and zero Bloomberg calls.
- AC3: the scheduled entry prints the refresh step between the admit step and its closing line.

## 5. WHEN YOU ARE DONE

1. Run your new test file and the two existing test files you touched with `python -m pytest <files> -q`. Every test passes.
2. Write the instance at the proof path in section 3.
3. Run `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` AFTER your final commit. It
   must return rc 0.
4. Only if every mechanical criterion passes, append a new status tag reading complete at the END of this file, in the SAME commit
   as your proof instance.
5. Report ONCE:
   - the field-list lengths before and after;
   - the derive's handling of the bulk field;
   - the refresh output lines;
   - each criterion's output line;
   - the pytest summary lines;
   - your commit hashes and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-33 analysis @`e55e3b5152` s.2; Andrew-direct 2026-10-03 ~20:3xZ card 3 @`9fe6e6f111` (relay msg 29002).
Base CLOUD `6527a03cc1`: aj1_check build 0/5 control 3/3; aj1_refresh_dry FAIL rc 2 (invalid choice 'refresh'); aj1_sched_dry FAIL
(refresh_line none). The served act is CRPS-aj-2, the issuer's, under a never-widen pair (decomposition s.1).
<risk>LOCAL</risk>
<status>pending</status>
<round>34</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<status>complete</status>
