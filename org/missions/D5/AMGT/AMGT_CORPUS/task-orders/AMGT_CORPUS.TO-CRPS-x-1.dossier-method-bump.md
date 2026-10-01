# AMGT_CORPUS task order -- `CRPS-x-1` -- ROUND 22: bump the dossier `METHOD_VERSION` to `/5` so `write_one` writes `pack_shape`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-x-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface (the served rewrite is the issuer's act under a pair).
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only in the check.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 22. Serves **FWD-16** (the dossier states its pack shape).

## 1. THE CELL -- `CRPS-x-1`

**Where this came from.** `lib/research/corpus/dossier.py` now builds `fields["pack_shape"]` (round 21). But `write_one` writes
NOTHING when the newest stored object's `inputs` equal the fresh ones AND its `method_version` equals the module's
`METHOD_VERSION`, currently `"amgt-corpus-dossier/4"` (line 144). Every stored object is `/4`, so no rewrite can serve the new
field. The module's own rule (CRPS-j-1) is that a method bump is never a no-op: a stored object naming a different method is
never "unchanged".

**RULED -- what you build:**
1. `METHOD_VERSION = "amgt-corpus-dossier/5"` in `dossier.py`. Change no other line of `dossier.py`.
2. The three tests that assert the literal `/4` (`tests/test_dossier_case_positional.py:189`, `tests/test_dossier_case_body.py:159`,
   `tests/test_dossier_case_unit.py:110`) assert `/5`. No other change to them.
3. `lib/research/corpus/tests/test_dossier_method_bump.py` (new), with stubs and no network:
   - a stored `/4` object with inputs equal to the fresh ones -> `write_one` WRITES (the method differs);
   - a stored `/5` object with equal inputs -> `write_one` writes nothing;
   - the written document carries `method_version` `/5` and a `pack_shape` field.
4. Do NOT run `--write`, and write nothing to S3. The 95-name rewrite is the issuer's act under a pair.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_method_bump.py
lib/research/corpus/tests/test_dossier_case_positional.py
lib/research/corpus/tests/test_dossier_case_body.py
lib/research/corpus/tests/test_dossier_case_unit.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-x-1.dossier-method-bump.md
</paths>

READ-ONLY: every other file, every S3 object. Scratch `.scratch/x1/`.

Your worktree is a SPARSE cone (`lib integrations .tools .claude org docs rcg infra/logic`); `data/`, `portal/` and the rest of
`infra/` are absent by design. If you need a path outside the cone, file a row and stop that criterion; never disable the sparse
checkout.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call, NO S3 write, NO `--write` run.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-x-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round22/x1_AC1.sh</invocation><expect>(?m)^x1 code_method amgt-corpus-dossier/5 stored_differs 3 of 3$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-x-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round22/x1_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: the code's method against the stored method on three served names (IMB, ADBE, AZN). All three differ, so `write_one`
  would write.
- AC2: your test with the dossier suites that touch the method (pack_shape, canonical address, case positional / body / unit,
  reader method, newest).

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-x-1.dossier-method-bump.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you changed
   plus the instance.
4. Report ONCE: each AC line and the lines you changed.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-21 analysis ruling 2 @`0bf907bee8`. Dry-run at base CLOUD `2a4c7f5451` (worktree `C:/tmp/coox-crps22-issue`):
- x1_AC1 FAIL as expected: `x1 code_method amgt-corpus-dossier/4 stored_differs 0 of 3`.
- x1_AC2 FAIL as expected (no tests ran; the new file is absent). The five existing suites read 47 passed at base.

The rewrite's expected diff is measured: 95 of 95 pack_shape-only, 0 other moves (decomposition s.1a).
<risk>LOCAL</risk>
<status>pending</status>
<round>22</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<status>complete</status>
