# AMGT_CORPUS task order -- `CRPS-ak-1` -- ROUND 35: unit families for the 52 round-34 mnemonics

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ak-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task, alarm or cadence; the unit map is not written by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 list/get of the landed raw only, through build_unit_map's own client (the same reads its --dry-run makes, measured at the cut: 2.5 s for 3 names, 0 bytes written).
comp-adversary: RUN by the issuer at the cut on CLOUD bad41f3f91 -- ak1_check.py build 0/2 control 2/2; test_build_unit_map_families.py 1 failed. Blind spot: the check reads three landed names (BA, GOOGL, BP/ LN), not all 96; the issuer's ak-4 dry run reads every name.
EGRESS CLASS, declared: AWS-INTERNAL READ ONLY. NO Bloomberg call, NO vendor call, NO write to S3 or to field_map.json.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 35.

## 1. THE CELL -- `CRPS-ak-1`

Round 34 appended 52 mnemonics to the producer's field lists, `integrations/bloomberg/research/model_block_pull.py`:
- `HEADER_FIELDS[18:]`: 7 mnemonics;
- `HIST_FIELDS[39:]`: 44 mnemonics;
- `FORECAST_FIELDS[11:]`: 1 mnemonic.

Each of the 52 has a `FIELD_BASIS` entry, Bloomberg's own definition. None of them is in any unit family of
`integrations/bloomberg/research/build_unit_map.py`:
- `unfamilied_mnemonics()` returns all 52;
- `tests/test_build_unit_map_families.py::test_census_covers_every_pulled_mnemonic` is RED;
- a map rebuild could only write "not in any known field family".

On the served blocks, 32,826 figures of the 52 carry the pointer unit "SEE field_map.json ... not yet built". The page reads that
as NOT measured, so FWD-20's V3 rows cannot reach the page.

**Build, in `build_unit_map.py` only:**
1. Place each of the 52 in a unit family. Use the module's existing families where one fits: `TEXT_FIELDS`, `PERCENT_FIELDS`,
   `ABSOLUTE_OR_MILLIONS_FIELDS`, `PER_SHARE_FIELDS`, `RATIO_FIELDS`, `SHARE_COUNT_ABSOLUTE_FIELDS`, `SHARE_COUNT_MILLIONS_FIELDS`.
   Add a family only where none fits; a DATE family for `EXPECTED_REPORT_DT` and `ERN_ANN_DT_AND_PER` is the expected case.
   - The family is decided by Bloomberg's own definition, the producer's `FIELD_BASIS` text.
   - It must DISCRIMINATE on the landed values. Read them in-process through `load_raw_for_key` + `prepare_header` +
     `build_entries` with `remeasure=False`, over at least BA, GOOGL and BP/ LN, and never write the map.
   - A field whose landed values do not discriminate gets UNRESOLVED-ON-<security> with its reason, the module's existing
     path. It never gets a guessed unit.
2. A hypothesis by name only. It is NOT a ruling: test each placement on the landed values and report where the values
   disagree.
   - **text:** SHORT_NAME, COUNTRY_FULL_NAME, LONG_COMP_NAME.
   - **dates:** EXPECTED_REPORT_DT, ERN_ANN_DT_AND_PER (a LIST of `{announcement_date, period}` objects in the served block; the
     raw is a list of row dicts). EQY_FUND_YEAR is a year; it landed no value at all on 96 names.
   - **percent:** DIVIDEND_YIELD, AVERAGE_/HIGH_/LOW_DIVIDEND_YIELD, FCF_MARGIN_AFTER_OPER_LEA_PYMT, NORMALIZED_ROA,
     NORMALIZED_ROE.
   - **ratio (multiples):** EV_TO_T12M_EBIT/EBITDA/SALES with their AVERAGE_/AVG_/HIGH_/LOW_ variants,
     AVERAGE_PRICE_EARNINGS_RATIO, AVERAGE_/HIGH_CLOSING_/LOW_CLOSING_PRICE_TO_BOOK_RATIO,
     AVERAGE_/HIGH_/LOW_PRICE_TO_FREE_CASH_FLOW, PX_ERN_RATIO_WITH_HIGH/LOW_CLOS_PX.
   - **amounts:** ARD_GOODWLL, ARD_OTHER_INTANGIBLE_ASSET, ARD_TOTAL_CURRENT_LIABILITIES, ARD_TOT_ASSETS, CAPEX_ABSOLUTE_VALUE,
     CASH_AND_MARKETABLE_SECURITIES, CF_CASH_FROM_OPER, EARN_FOR_COMMON, HISTORICAL_MARKET_CAP, MINORITY_NONCONTROLLING_INTEREST,
     SHORT_AND_LONG_TERM_DEBT, TOTAL_EQUITY, CRNCY_ADJ_MKT_CAP, AVG_DAILY_VALUE_TRADED_3M.
   - **share count:** ARD_SHARES_OUTSTANDING.
   - **per share:** FREE_CASH_FLOW_PER_SH, TANG_BOOK_VAL_PER_SH, BEST_CPS.
3. A LIST value (`ERN_ANN_DT_AND_PER`) and a date string must not crash `classify_unit`, `classify_sign`, `sample_value` or
   `build_entries`. A list is classified by its family, never by magnitude.
4. Never move a base mnemonic's family or a base unit. The 68 base members keep their families, and `build_entries` over the
   landed names leaves every base per-security unit equal to the committed map's (additive merge).
5. Write `integrations/bloomberg/research/tests/test_build_unit_map_families_round35.py`. It is offline, with fixture values
   shaped like the landed ones: one case per family you placed or added, the list and date cases, and an UNRESOLVED case.

## 2. BOUNDS

1. NO Bloomberg call, NO vendor call, NO write to S3. NEVER write `field_map.json`: the map write is the issuer's served act
   (CRPS-ak-4), under a never-widen pair. Run `build_unit_map.py` only with `--dry-run` or in-process without writing.
2. Only the files in `<paths>` change. Never edit `tests/test_build_unit_map_families.py`; it is the oracle. Never edit
   `model_block_pull.py`.
3. Write code with the Edit/Write tools, never a shell heredoc or `python -c` (a heredoc on this machine turns `\b` into a 0x08
   byte). ASCII only.
4. Run python as `PYTHONPATH=<worktree root> python ...` (the modules import `lib.research`).
5. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner
   2.0.0_SA_COO~X`.

## 3. SURFACES

<paths>
integrations/bloomberg/research/build_unit_map.py
integrations/bloomberg/research/tests/test_build_unit_map_families_round35.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-ak-1.unit-families-for-the-52.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ak-1.unit-families-for-the-52.md
</paths>

Read-only: the whole repository, in particular `model_block_pull.py` (`FIELD_BASIS`, the field lists), the committed
`field_map.json`, the existing `tests/test_build_unit_map_*.py`, and the issuer's checks under
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round35/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ak-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round35/ak1_check.py"</invocation><expect>(?m)^ak1 build 2/2 control 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ak-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest integrations/bloomberg/research/tests/test_build_unit_map_families.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^[0-9]+ passed(, [0-9]+ warnings?)? in [0-9.]+s$</expect></criterion>
</proof_of_spec>

- AC1 (in memory, over BA, GOOGL and BP/ LN):
  - build: none of the 52 is unfamilied, and no landed entry of the 52 reads "not in any known field family";
  - control: no base family moved, and no base per-security unit moved.
- AC2: the census test, the oracle, passes with no failure.

## 5. WHEN YOU ARE DONE

1. Run your new test file and every `integrations/bloomberg/research/tests/test_build_unit_map_*.py` with
   `python -m pytest <files> -q`. Every test passes.
2. Write the instance at the proof path, then run `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order
   <this order>` AFTER your final commit. It must return rc 0.
3. Only if every mechanical criterion passes, append a new status tag reading complete at the END of this file, in the SAME
   commit as your proof instance.
4. Report ONCE:
   - the family each of the 52 landed in, and any family you added;
   - per mnemonic, over the names you read, the count MEASURED / UNRESOLVED, with each UNRESOLVED reason;
   - every criterion's output line, the pytest summary lines, your commit hashes and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-34 analysis @`83cd052a9c` s.2 ruling 2 + s.3 item 1. Base CLOUD `bad41f3f91`: ak1_check build 0/2
control 2/2; census test 1 failed. The served move is CRPS-ak-4 (decomposition s.1).
<risk>LOCAL</risk>
<status>pending</status>
<round>35</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<status>complete</status>
