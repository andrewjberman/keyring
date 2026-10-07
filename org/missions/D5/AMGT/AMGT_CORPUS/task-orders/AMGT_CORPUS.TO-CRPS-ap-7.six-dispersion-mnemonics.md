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

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-39 analysis @`5ccdc90368` ruling 10 + s.4 item 4; CTO msg 30490 (AMGT_RESAPP ROUND_ANALYSIS.round76 ADDENDUM 1 item 2 @a7b2c3e0ba). Base: ap7 build 0/1 control 2/2; the six files 51 passed. Calls per fire: 768 before, 768 after. A 2026-09-15 probe instrument spells `BEST_CPS_STDDEV`; the issuer's one-name scripted probe (CRPS-ap-10) settles the spelling before the re-pin.
<risk>LOCAL</risk>
<status>pending</status>
<round>40</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<status>complete</status>
