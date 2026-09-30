# AMGT_CORPUS task order -- `CRPS-v-1` -- ROUND 20: the Python 3.9 floor -- no `Path` text call passes `newline=`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-v-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 20. Serves **the code's stated Python 3.9 floor**.

## 1. THE CELL -- `CRPS-v-1`

**Where this came from.** `pathlib.Path.write_text` / `read_text` accept `newline=` only from Python 3.10. The code states a 3.9
floor, and ruff's py39 target cannot see a stdlib keyword added later. The issuer's AST census at the cut reads 10 such calls
over 95 files:
- `integrations/bloomberg/research/model_block_pull.py:846`, in `_ensure_unit_map` (the unit-map write);
- `integrations/bloomberg/research/tests/test_model_block_admit.py:101`, `:106`;
- `lib/research/corpus/tests/test_induction_planted_drive.py:106`, `:110`, `:112`;
- `lib/research/corpus/tests/test_induction_schedule.py:77`, `:79`, `:81`, `:164`.

**RULED -- what you build:**
1. Every one of the 10 calls becomes `open(path, "w" or "r", encoding=<the same encoding>, newline=<the same value>)` inside a
   `with`, writing or returning exactly the same text. No other change to those files.
2. `integrations/bloomberg/research/tests/test_model_block_unit_map_write.py` (new): run `_ensure_unit_map` against a stub S3
   and a temp field-map path (set `model_block_pull._FIELD_MAP_PATH` and the builder's `FIELD_MAP_PATH` to it; never the
   committed map), then read the written bytes: they contain no `b"\r"` and parse as JSON. No network, no vendor call.
3. The suites that hold the changed calls stay green.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_model_block_admit.py
integrations/bloomberg/research/tests/test_model_block_unit_map_write.py
lib/research/corpus/tests/test_induction_planted_drive.py
lib/research/corpus/tests/test_induction_schedule.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-v-1.py39-newline-floor.md
</paths>

READ-ONLY: every other file (including `field_map.json` -- NEVER write it), every S3 object. Scratch `.scratch/v1/`.

Your worktree is a SPARSE cone (`lib integrations .tools .claude org docs rcg infra/logic`); `data/`, `portal/` and the rest
of `infra/` are absent by design. If you need a path outside the cone, file a row and stop that criterion; never disable the
sparse checkout.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call, NO S3 read or write, NO write to `field_map.json`.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k),
  with `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-v-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round20/v1_AC1.sh</invocation><expect>(?m)^v1 newline_kw_calls 0 files_scanned (9[5-9]|1\d\d) parse_errors 0$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-v-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round20/v1_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: the census over `lib/research/corpus/` and `integrations/bloomberg/research/` reads 0 calls, with the file count
  printed (95 at the cut; your new test file adds one). AC2: your LF test with the three suites that hold changed calls.

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-v-1.py39-newline-floor.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you
   changed plus the instance.
4. Report ONCE: each AC line and the 10 call sites as changed.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-19 analysis s.4 cell 1 @`d5d806bc2e`, ruling 1. No 3.9 interpreter here (`py -0`: 3.14, 3.11), so the
AST branch. The census root is widened to the defect's own root (decomposition s.1a). Dry-run at base CLOUD `be851f21d2`
(worktree `C:/tmp/coox-crps20-issue`):
- v1_AC1 FAIL as expected: `v1 newline_kw_calls 10 files_scanned 95 parse_errors 0`.
- v1_AC2 FAIL as expected (no tests ran; the new file is absent).

`worker-light`: about 20 changed lines plus one small test (report 2 C7 trial size).
<risk>LOCAL</risk>
<status>pending</status>
<round>20</round>
<slot>~1</slot>
<fabric>site-z</fabric>

<status>complete</status>
