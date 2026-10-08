# AMGT_CORPUS task order -- `CRPS-ap-7` -- ROUND 40: the six consensus-dispersion mnemonics ride the model-block pull

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ap-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE for this cell -- the scheduled task's re-pin is the issuer's CRPS-ap-10.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the check imports two modules and reads their constants.
comp-adversary: RUN by the issuer at the cut -- ap7_check.py build 0/1 control 2/2 (0 of 6 present; 8 calls per name; 12 forecast fields).
EGRESS CLASS, declared: NONE. NO Bloomberg call: the one-name probe is the issuer's scripted act, after your drain.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 40.

## 1. THE CELL -- `CRPS-ap-7`

`integrations/bloomberg/research/model_block_pull.py` pulls each covered name's model block from Bloomberg: one header call
(`HEADER_FIELDS`), the history in chunks (`HIST_FIELDS`, 25 per request), and three forecast calls, one per override in
`FORECAST_OVERRIDES` ("1FY", "2FY", "3FY"), each asking for `FORECAST_FIELDS` plus the period-end date (`stage_pull`, about lines
785-822). That is 8 calls per name, 768 for the 96 names of the daily fire.

`lib/research/scores/divergence.py` (about lines 64-65) divides by six consensus statistics that no block carries yet:
`CFPS_FIELDS = ("BEST_CPS_STANDARD_DEV", "BEST_CPS_AVG", "BEST_CPS_NUMEST")` and `EPS_FIELDS = ("BEST_EPS_STANDARD_DEV",
"BEST_EPS_AVG", "BEST_EPS_NUMEST")`. Its reader (`lib/research/scores/run_scores.py`, about 205-225) takes model-block figures
whose `mnemonic` is one of the six and whose `fiscal_period` is None or "FY1".

**Build:**
1. Append the six to `FORECAST_FIELDS` (about lines 330-334), after `BEST_CPS`, in the order above, with an `AMENDMENT (CRPS-ap-7,
   round 40):` comment. They ride the same three forecast requests: the call count per name stays 8. Import nothing from
   `divergence.py` into the pull; type the six names and let the issuer's check hold them equal to the consumer's.
2. Give each of the six what every forecast field already has, wherever the module keys on forecast membership: its `FIELD_BASIS`
   entry (about 395-458), and its unit and currency treatment. `_AVG` and `_STANDARD_DEV` are money per share in the reporting
   currency, like `BEST_CPS` and `BEST_EPS`. `_NUMEST` is a COUNT of estimates: it carries no currency and no per-share unit
   (see `_MONEY_REPORTING_FIELDS`, about 1159-1167, and how counts are handled since round 38).
3. The derive loops (about 1397-1409) emit a figure, or an unresolved record with its reason, for each forecast field and period.
   The six follow the same rule: a statistic Bloomberg does not return for a name is a recorded absence with its reason, never a
   zero and never a silent skip.
4. If the unit map needs a family for the new fields (`integrations/bloomberg/research/build_unit_map.py`;
   `test_build_unit_map_families.py` builds its producer set from all three lists), add it there, the way round 35's fields were
   added.
5. Tests: update the count assertions that enumerate `FORECAST_FIELDS` (`test_model_block_22_fields.py`, about lines 86 and 88).
   Three tests slice `FORECAST_FIELDS[11:]` as "the round-34 field" (`test_build_unit_map_families_round35.py` about 29,
   `test_currency_labels.py` about 364, `test_stage_derive_fye.py` about 277): bound each slice to `[11:12]` so it still means
   `BEST_CPS` alone. Mark every edit `AMENDMENT (CRPS-ap-7, round 40):`. Change no other assertion.
6. Add `integrations/bloomberg/research/tests/test_dispersion_fields_round40.py`: offline, a stub client; the three forecast
   requests each carry the six names; a derive over a stub response yields a figure for each of the six at FY1 with the right
   unit and currency treatment; a response missing one statistic yields its unresolved record with a reason.

## 2. BOUNDS

1. Never run `pull`, `admit`, `refresh` or `derive` except with `--dry-run` or against a stub; you do not need to run them.
2. Do not edit `HEADER_FIELDS`, `HIST_FIELDS`, `FORECAST_OVERRIDES`, `stage_pull`'s request shape, `cmd_refresh` or `cmd_admit`.
3. If you find that one of the six cannot be given a unit treatment without a rule this order does not state, file a row and stop on that field; do not guess.
4. NO push of any branch, NO deploy, NO AWS call, NO Bloomberg call, NO vendor call.
5. Only the files in `<paths>` change. Never edit the issuer's checks, fixtures or snapshots.
6. Write code with the Edit/Write tools, never a shell heredoc or `python -c`. ASCII only.
7. Rows are `AMGT_CORPUS-Z-W3-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner 2.0.0_SA_COO~X` and `surfaced_at` from `date -u +%FT%TZ` at filing.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/build_unit_map.py
integrations/bloomberg/research/tests/test_dispersion_fields_round40.py
integrations/bloomberg/research/tests/test_fire_budget_record_round40.py
integrations/bloomberg/research/tests/test_model_block_22_fields.py
integrations/bloomberg/research/tests/test_build_unit_map_families.py
integrations/bloomberg/research/tests/test_build_unit_map_families_round35.py
integrations/bloomberg/research/tests/test_currency_labels.py
integrations/bloomberg/research/tests/test_stage_derive_fye.py
integrations/bloomberg/research/tests/test_model_block_round34.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-ap-7.six-dispersion-mnemonics.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ap-7.six-dispersion-mnemonics.md
</paths>

Read-only: the whole repository, in particular `lib/research/scores/divergence.py`, `lib/research/scores/run_scores.py` and the issuer's check `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/ap7_check.py` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ap-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/ap7_check.py"</invocation><expect>(?m)^ap7 build 1/1 control 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ap-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python -m pytest integrations/bloomberg/research/tests/test_model_block_22_fields.py integrations/bloomberg/research/tests/test_build_unit_map_families.py integrations/bloomberg/research/tests/test_build_unit_map_families_round35.py integrations/bloomberg/research/tests/test_currency_labels.py integrations/bloomberg/research/tests/test_stage_derive_fye.py integrations/bloomberg/research/tests/test_model_block_round34.py integrations/bloomberg/research/tests/test_dispersion_fields_round40.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^[0-9]+ passed(, [0-9]+ warnings?)? in [0-9.]+s$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-ap-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/ap7_budget_check.py"</invocation><expect>(?m)^ap7b build 2/2 control 2/2$</expect></criterion>
</proof_of_spec>

- AC1 (the two real modules' constants): build -- each of the six the consumer divides by is in `FORECAST_FIELDS` exactly once;
  control -- round 39's twelve forecast fields are still first and in order, and the calls per name are still 8.
- AC2: the six named test files and your new file pass.

## 5. WHEN YOU ARE DONE

1. Run the pytest files named in AC2 once more after your last edit. Every test passes.
2. Write the instance at the proof path, with its mutant control from the start. Then run `python .tools/proof-of-spec-check.py
   <instance> AC1,AC2 --governing-order <this order>` AFTER your final commit. It must return rc 0.
3. Only if every mechanical criterion passes, append a new status tag reading complete at the END of this file, in the SAME commit
   as your instance.
4. Report ONCE: what you changed and where, every criterion's output line, the pytest summary line, your commit hashes and any row.

## 6. AMENDMENT 1 (2026-10-07, the issuer's own; the one-name probe and the CTO's ruling)

The build of section 1 is merged (drain `9b16c0cc86`): `FORECAST_FIELDS` carries the six names the consumer listed. The issuer
then probed ONE name at Bloomberg (`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/evidence/
r40_ap10_probe_BA_20261007.txt`, read it). Four of the six are not Bloomberg fields: `BEST_CPS_STANDARD_DEV`, `BEST_CPS_AVG`,
`BEST_EPS_STANDARD_DEV` and `BEST_EPS_AVG` each returned `BAD_FLD/INVALID_FIELD` on every override. `BEST_CPS_NUMEST` and
`BEST_EPS_NUMEST` returned, and so did the other spelling of the standard deviation, `BEST_CPS_STDDEV` and `BEST_EPS_STDDEV`.
Ruled by `1.0.0_SA_CTO~Z`: pull the four that exist; the mean is `BEST_CPS` / `BEST_EPS`, already pulled; no new mean field.

**Do, and only this:**
1. `FORECAST_FIELDS` ends, after `BEST_CPS`, with exactly `BEST_CPS_STDDEV`, `BEST_CPS_NUMEST`, `BEST_EPS_STDDEV`,
   `BEST_EPS_NUMEST` (16 fields, still 8 calls per name). Remove the four refused names from every list, basis map, money or
   count set and unit-map family they were added to (this module keeps an invalid field out of its lists: see its comments at
   about lines 97 and 218). Give the two `_STDDEV` names what the two `_STANDARD_DEV` names had (money per share, reporting
   currency). The two `_NUMEST` names keep what they have (a count, no currency). Mark each edit `AMENDMENT 1 (CRPS-ap-7, round
   40):` and cite the probe evidence file in the comment at `FORECAST_FIELDS`.
2. **The period term (the CTO's).** A standard deviation and its mean must be for the SAME forecast period. State in the comment
   at `FORECAST_FIELDS` which override each of the four is asked under: the same `BEST_FPERIOD_OVERRIDE` request as `BEST_CPS`
   and `BEST_EPS`, one request per override in `FORECAST_OVERRIDES`. In `test_dispersion_fields_round40.py` add a test that, for
   a stub pull of `BA US Equity`, PRINTS (and asserts equal) for each override the override the request carrying `BEST_CPS` and
   `BEST_EPS` was sent under beside the override the request carrying each of the four was sent under, and that the derived
   figures for a mean and its standard deviation carry the same `fiscal_period`. Paste that printed table into your report.
3. Update the tests you touched in the build to the four names and the new counts (16 forecast fields; the total in
   `test_model_block_22_fields.py`). Change no other assertion.
4. Do not edit `lib/research/scores/divergence.py` (its rename is an AMGT_RESAPP cell).

**Prove** AC1 and AC2 by their invocations in section 4 (the issuer's `ap7_check.py` now holds the four ruled names and the
absence of the four refused ones). Then section 5 again: the proof instance updated, the checker after your final commit, and the
status tag reading complete appended at the END of this file only if AC1 and AC2 pass.

## 7. AMENDMENT 2 (2026-10-07, the issuer's own; the CTO's rulings msg 31290 and msg 31295)

The build and AMENDMENT 1 are merged and are your INHERITED STATE. A shared ledger of the Terminal's daily capacity exists:
`data/etfs/scripts/rivalfunds/bbg_budget.py` (read it whole: `record(mode, rows, batch_id)` appends one JSON line to the day's
file under the directory `RIVALFUNDS_BBG_BUDGET_DIR` names, returns False on a write failure and never raises; `spent(day)` sums
`rows`). The model-block fire writes no line to it, so a backfill that checks the ledger before it draws cannot see this pull.
Measured on the 2026-10-07 fire: 768 calls, 13,824 security-field requests, 66,879 returned figures.

**Do, and only this, in `model_block_pull.py` (plus one new test file):**
1. Add `record_fire_budget(calls, security_fields, figures, records, stamp)` (keyword arguments, whole numbers and the fire's
   stamp). It
   loads `bbg_budget.py` BY PATH from the repository this file sits in (the way this module already loads `build_unit_map.py`:
   `_load_build_unit_map`), and appends ONE line: `mode` = `amgt-model-block`; `rows` = `figures` (the largest of the three, the
   CTO's ruling until the daily collector's unit is named); `batch_id` =
   `amgt-model-block:<stamp>:calls=<c>:security_fields=<s>:figures=<f>:records=<r>:rows_unit=returned-figures`. It returns what `record`
   returns. It never raises: a missing module, an unreadable path or a failed write returns False. A fire is never blocked or
   failed by bookkeeping, and the fire's rc does not change.
2. Call it ONCE at the end of a real (non dry-run) `cmd_refresh` and ONCE at the end of a real `cmd_admit` that pulled at least
   one name, with: `calls` = the run's own Bloomberg call count (the number its summary line already prints);
   `security_fields` = names pulled x (`len(HEADER_FIELDS)` + `len(HIST_FIELDS)` + `len(FORECAST_FIELDS)` x
   `len(FORECAST_OVERRIDES)`); `figures` = the count of figures in the blocks the run derived (sum of each derived block's
   figures; 0 when none derived); `records` = the RETURNED RECORDS, the ledger's own unit (ruled, msg 31310: the daily
   collector records returned data rows): one per security row a reference request returns (the header call and each forecast
   override call) plus one per dated row each history request returns, counted from the responses the run actually received,
   never estimated. A dry run records nothing. Print one line after it: `budget_record amgt-model-block rows <n>
   records <r> calls <c> security_fields <s> written <0|1>`.
3. Add `integrations/bloomberg/research/tests/test_fire_budget_record_round40.py`: offline, with `RIVALFUNDS_BBG_BUDGET_DIR` set
   to a temp directory: the helper writes the one line; an unwritable directory returns False and raises nothing; a dry-run
   refresh over a stub writes no line; a real refresh over a stub client writes exactly one line whose three numbers equal the
   stub's.

**Prove** AC1, AC2 and AC3 by their invocations in section 4 (AC3 is `ap7_budget_check.py`: `ap7b build 2/2 control 2/2`), and
run your new test file with pytest and report its last line. Then section 5 again: the proof instance updated (AC3 added), the
checker after your final commit, and the status tag reading complete appended at the END of this file only if AC1, AC2 and AC3
pass.

## 8. AMENDMENT 3 (2026-10-08, the issuer's own; the CTO's ruling msg 31815)

AMENDMENT 2 is merged and is your INHERITED STATE: `record_fire_budget` in
`integrations/bloomberg/research/model_block_pull.py` appends one line per fire to the shared Bloomberg budget ledger, with
`rows` = `figures` (about 67,000 for a fire) and `rows_unit=returned-figures` in the batch id. That was the earlier ruling
("the largest of the three, until the collector's unit is named"). No fire has run with it: the scheduled task is pinned to
a commit that does not hold it.

**The ruling now: the ledger holds ONE unit, RETURNED RECORDS.** The ledger's other writers record rows returned (the
2026-10-08 backfill line is 2,929). A line of about 67,000 would tell every later leg that 56 percent of the day's limit is
gone when 3.5 percent is, and another product could be refused capacity by a unit error.

**Build, and only this:**
1. In `record_fire_budget`, `rows` is `records` (the value passed to `bbg_budget.record`), and the batch id ends
   `:rows_unit=returned-records`. `calls`, `security_fields`, `figures` and `records` all stay in the batch id as they are.
   Update the docstring: the unit, the ruling (msg 31815) and why. Nothing else in the function changes; it still never
   raises.
2. `_close_fire_budget` and its printed line: if the line names which count was recorded, it names records. Do not change
   what is counted.
3. Update `integrations/bloomberg/research/tests/test_fire_budget_record_round40.py` (line 92 asserts `rows == 66879`, line 95
   the old unit word) to the new rule, and add one test that `rows` equals `records` and not `figures` when the two differ.
   Mark edits `AMENDMENT 3 (CRPS-ap-7, round 40):`.

**Prove** AC1, AC2 and AC3 by their invocations in section 4. AC3 (`ap7_budget_check.py`) now expects rows 4224, a rise in
`spent()` of 4224 and `rows_unit=returned-records`; on the inherited code it reads `ap7b build 0/2 control 2/2`, and after
your change `ap7b build 2/2 control 2/2`. Then section 5 again: the proof instance updated and pinned to your code commit,
the checker run after your final commit, and the status tag reading complete appended at the END of this file only if AC1,
AC2 and AC3 pass.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-39 analysis @`5ccdc90368` ruling 10 + s.4 item 4; CTO msg 30490 (AMGT_RESAPP ROUND_ANALYSIS.round76 ADDENDUM 1 item 2 @a7b2c3e0ba). Base: ap7 build 0/1 control 2/2; the six files 51 passed. Calls per fire: 768 before, 768 after. A 2026-09-15 probe instrument spells `BEST_CPS_STDDEV`; the issuer's one-name scripted probe (CRPS-ap-10) settles the spelling before the re-pin.
<risk>LOCAL</risk>
<status>pending</status>
<round>40</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<status>complete</status>
<status>in_progress</status>
<status>complete</status>
<status>in_progress</status>
<status>complete</status>
<status>in_progress</status>
<status>complete</status>
