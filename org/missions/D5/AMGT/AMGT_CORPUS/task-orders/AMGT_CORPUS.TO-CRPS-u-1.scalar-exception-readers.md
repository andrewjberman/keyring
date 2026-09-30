# AMGT_CORPUS task order -- `CRPS-u-1` -- ROUND 19: the unit/sign readers honour a scalar field's per-security exception (row `Z-W2-S13`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-u-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface.
comp-iam: DECLARED-NOT-APPLICABLE -- one S3 GET of a served block, read-only, inside the issuer's probe.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 19. Serves **the served unit on a name whose unit the map could not
measure (row `Z-W2-S13`)**.

## 1. THE CELL -- `CRPS-u-1`

**Where this came from.** `integrations/bloomberg/research/field_map.json` records a field's unit and sign either as a SCALAR
shared by every security (e.g. BEST_SALES: `unit "MILLIONS"`, `unit_status "MEASURED"`) or as a per-security dict. Round 18
(`build_unit_map.py`) froze a shared field: a security that cannot be measured, or disagrees, is recorded under
`per_security_detail[<security>]["exception"]` (a dict with `scope` and a `unit` and/or `sign` reason), and the scalar stays.
The readers in `integrations/bloomberg/research/model_block_pull.py`, `_resolved_unit(mnemonic, security)` and
`_resolved_sign(mnemonic, security, observed_value)` (about lines 690-725), return the scalar for ANY security and never read
`per_security_detail`. So a re-derive of Hitachi (`6501 JP Equity`) would serve BEST_SALES as MEASURED `MILLIONS`, although
its own map entry says the magnitude did not discriminate.

**Measured by the issuer at the cut:** in the committed map, BEST_SALES is the only scalar-unit field with a non-MEASURED
6501 entry. That entry predates the `exception` shape: it carries `unit_status` and `sign_status` strings starting
`UNRESOLVED-ON-6501 JP Equity: ...` and **no `exception` key**.

**RULED -- what you build:**
1. In `_resolved_unit` and `_resolved_sign`, when the field's unit (or sign) is a SCALAR: if
   `per_security_detail[security]` exists and EITHER carries an `exception` with a `unit` (or `sign`) reason, OR its
   `unit_status` (or `sign_status`) is not `"MEASURED"`, return a text starting `UNRESOLVED-ON-<security>: ` with the reason
   (the entry's own status text is acceptable). Otherwise the current behaviour. A dict-valued field keeps its current
   behaviour. A security with no entry, or a MEASURED entry with no exception, still gets the scalar.
2. `integrations/bloomberg/research/tests/test_model_block_resolved_exception.py` (new), on a temp map (never the committed
   one): the `exception` form, the pre-exception status form, a MEASURED security under the same scalar field (the control:
   still the scalar), and a dict-valued field (unchanged). Keep `test_build_unit_map_classification_split.py` green.
3. Change nothing else in `model_block_pull.py`. In particular do NOT touch `_ensure_unit_map`: another cell of this round
   owns its header preparation, and the issuer rewires it at the merge.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_model_block_resolved_exception.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-u-1.scalar-exception-readers.md
</paths>

READ-ONLY: every other file (including `field_map.json` -- NEVER write it -- and
`tests/test_build_unit_map_classification_split.py`), every S3 object. Scratch `.scratch/u1/`.

Your worktree is a SPARSE cone (`lib integrations .tools .claude org docs rcg infra/logic`); `data/`, `portal/` and the rest
of `infra/` are absent by design. If you need a path outside the cone, file a row and stop that criterion; never disable the
sparse checkout.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call, NO S3 write, NO write to `field_map.json`, NO derive.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k),
  with `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-u-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round19/u1_AC1.sh</invocation><expect>(?m)^u1 reader best_sales_6501 unit UNRESOLVED sign UNRESOLVED control_8035 unit MILLIONS sign POSITIVE module_in_toplevel yes$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-u-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round19/u1_AC2.sh</invocation><expect>(?m)^u1 served best_sales_6501 FY1 value 11962163\.4 served_unit_class UNRESOLVED reader_unit_class UNRESOLVED agree yes$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-u-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round19/u1_AC3.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: the fixed readers on the REAL committed map. 6501 reads UNRESOLVED; the control, 8035 (MEASURED on the same scalar
  field), still reads `MILLIONS` / `POSITIVE`; the module graded is this tree's file. AC2: ruling 1's print -- the served
  Hitachi block's FY1 BEST_SALES unit class against the fixed reader's (one S3 GET). AC3: your tests with the split suite.
  A fourth line of evidence is not a criterion: AC2 is the analysis's required measurement.

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-u-1.scalar-exception-readers.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you
   changed plus the instance.
4. Report ONCE: each AC line, the text the readers now return for 6501, and the line range you changed.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-18 analysis s.4 cell 1 @`62ccfcb8d2`, ruling 1. The checks were dry-run at base CLOUD `d357a9e247`
(worktree `C:/tmp/coox-crps19-issue`, sparse cone plus `infra/logic`, which `lib/opal_naming.py` reads at import):
- u1_AC1 FAIL as expected: `u1 reader best_sales_6501 unit MEASURED sign MEASURED control_8035 unit MILLIONS sign POSITIVE
  module_in_toplevel yes` (the control half already PASSes).
- u1_AC2 FAIL as expected: `u1 served best_sales_6501 FY1 value 11962163.4 served_unit_class UNRESOLVED reader_unit_class
  MEASURED agree no`.
- u1_AC3 FAIL as expected (no tests ran).

Ruling 1's branch is settled by the base read: the served block already reads UNRESOLVED; after the fix the two agree, so
the served block stands and no re-derive is cut.
<risk>LOCAL</risk>
<status>pending</status>
<round>19</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<status>complete</status>
