# AMGT_CORPUS task order -- `CRPS-u-2` -- ROUND 19: the `build_unit_map` CLI builds from the producer's header preparation (row `Z-W2-S14`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-u-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 raw reads only (the replay reads Hitachi's bronze).
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 19. Serves **one unit-map build, whichever entry point runs it (row
`Z-W2-S14`)**.

## 1. THE CELL -- `CRPS-u-2`

**Where this came from.** `integrations/bloomberg/research/build_unit_map.py` builds the unit map
(`integrations/bloomberg/research/field_map.json`) through `build_entries(resolved, remeasure)`. Two entry points feed it
different headers:
- the PRODUCER, `model_block_pull._ensure_unit_map` (`integrations/bloomberg/research/model_block_pull.py`, about lines
  796-845), copies the refdata header, joins every `_BULK_TEXT_HEADER_FIELDS` member (`CIE_DES_BULK`) to a string with
  `_bulk_text_value`, and merges the bestdata `1FY` row's `FORECAST_FIELDS` values (read from
  `_bronze_key("bestdata", sec_key, raw_stamp)` with `_read_json_from_s3`; a missing object is a no-op);
- the CLI, `build_unit_map.main --securities`, passes `load_raw_for_key`'s raw header as landed: CIE_DES_BULK is still a
  row-dict list and no BEST_ value is present.

So the CLI replay of Hitachi (`6501 JP Equity`) reproduces 209 of the 214 committed Hitachi additions: the `measured_on`
appends for BEST_DPS, BEST_EBITDA, BEST_EPS, BEST_PE_RATIO and CIE_DES_BULK come out as exceptions instead.

**RULED -- what you build:**
1. In `build_unit_map.py`: ONE public function (name yours; e.g. `prepare_header(s3, security, sec_key, header, raw_stamp)`)
   that returns a COPY of the header with exactly the producer's preparation above, reading every constant and helper from
   the producer module it already imports as `_mbp` (never re-typed). `main` uses it for every resolved name, dry run
   included. Never mutate the raw header.
2. Do NOT edit `model_block_pull.py` (another cell of this round owns it). The producer switching to your function is a
   one-line hookup the issuer adds at the merge: name the exact replacement in your report.
3. The CLI's real write uses `newline="\n"`, as the producer's does, so the map stays LF on this device.
4. `integrations/bloomberg/research/tests/test_build_unit_map_cli_header.py` (new), with a stub S3 (no network): the
   function joins a CIE_DES_BULK row-dict list, merges a bestdata `1FY` value, leaves the input header unchanged, and is a
   no-op on a missing bestdata object. Keep `test_build_unit_map_exceptions.py` and
   `test_build_unit_map_classification_split.py` green.

## 3. SURFACES

<paths>
integrations/bloomberg/research/build_unit_map.py
integrations/bloomberg/research/tests/test_build_unit_map_cli_header.py
integrations/bloomberg/research/tests/test_build_unit_map_exceptions.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-u-2.cli-producer-header.md
</paths>

READ-ONLY: every other file (including `field_map.json` -- NEVER write it -- `model_block_pull.py` and
`tests/test_build_unit_map_classification_split.py`), every S3 object. Scratch `.scratch/u2/`.

Your worktree is a SPARSE cone (`lib integrations .tools .claude org docs rcg infra/logic`); `data/`, `portal/` and the rest
of `infra/` are absent by design. If you need a path outside the cone, file a row and stop that criterion; never disable the
sparse checkout.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call, NO S3 write, NO write to the committed `field_map.json`. The replay works on a temp copy.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W2-S<k>` (next free k),
  with `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-u-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round19/u2_AC1.sh</invocation><expect>(?m)^u2 replay rc 0 shared_changed 0 shared_removed 0 type_changed 0 hitachi_reproduced 214 of 214 non6501_added 0$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-u-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round19/u2_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: Hitachi's replay through the CLI at HEAD, against the pre-Hitachi map in a temp file: every committed Hitachi addition
  reproduced, 0 shared or type change, 0 non-6501 addition. AC2: your test with the builder's two suites.

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-u-2.cli-producer-header.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you
   changed plus the instance.
4. Report ONCE: each AC line, the function's name and signature, and the exact producer hookup (old lines, new line).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-18 analysis s.4 cell 2 @`62ccfcb8d2`, ruling 2 ("byte-equal then means byte-equal"). The checks were
dry-run at base CLOUD `d357a9e247` (worktree `C:/tmp/coox-crps19-issue`):
- u2_AC1 FAIL as expected: `u2 replay rc 0 shared_changed 0 shared_removed 0 type_changed 0 hitachi_reproduced 209 of 214
  non6501_added 0` (the bound halves already PASS).
- u2_AC2 FAIL as expected (no tests ran).

The hookup in `_ensure_unit_map` is the issuer's, at the merge, after u-1 drains (u-1 owns the file).
<risk>LOCAL</risk>
<status>pending</status>
<round>19</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<status>complete</status>
