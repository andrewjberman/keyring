# AMGT_CORPUS task order -- `CRPS-t-2` -- ROUND 18: `build_unit_map` records a per-security exception and never downgrades a shared field (row `Z-S65`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-t-2</owned_cells>
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

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 18. Serves **the served unit map's integrity (row `Z-S65`)**.

## 1. THE CELL -- `CRPS-t-2`

**Where this came from.** Row `AMGT_CORPUS-Z-S65`: registering Hitachi 6501 JP's units through
`integrations/bloomberg/research/build_unit_map.py`'s merge (called by `model_block_pull.py`'s `_ensure_unit_map`, and by its
own CLI `main --securities`) changed SHARED field entries in `integrations/bloomberg/research/field_map.json`:
- 4 fields' `unit_status` / `sign_status` flipped from `MEASURED` to `UNRESOLVED-ON-6501 JP Equity: sampled magnitude
  11962163.4 does not discriminate absolute vs millions`;
- 1 field's `unit` / `sign` changed TYPE, from a scalar (`"MILLIONS"`) to a per-security dict;
- `finding` strings were recomputed.

The committed map at `ead621d685` carries Hitachi's per-security entries ONLY, 214 additions, by the CTO's ruling. The CTO
ruled (`org/missions/D5/AMGT/AMGT_CORPUS/ledger/ROUND_ANALYSIS.round17.md` s.2 ruling 2): when one name disagrees with a
MEASURED shared field, `build_unit_map` records a per-security EXCEPTION and never changes a shared field's status or type.

**RULED -- what you build:**
1. In `build_unit_map.py`'s merge: a new security whose unit or sign cannot be measured, or disagrees with a shared field
   already `MEASURED`, is recorded as a per-security exception under that field. The shape is yours; name it in your report,
   and it must be 6501-scoped for Hitachi. It never changes the field's `unit_status`, `sign_status`, `unit` / `sign` type or
   `finding`. A field whose entries are already per-security dicts keeps its current behaviour.
2. `integrations/bloomberg/research/tests/test_build_unit_map_exceptions.py` (new): a MEASURED scalar field plus a new name with
   an ambiguous magnitude gives an exception, with status and type unchanged. A MEASURED per-security field plus a new
   measured name adds that name's entry. Keep `test_build_unit_map_classification_split.py` green.
3. Run the replay (AC1) yourself: Hitachi's input through the CLI, against the pre-Hitachi map in a temp file.

## 3. SURFACES

<paths>
integrations/bloomberg/research/build_unit_map.py
integrations/bloomberg/research/tests/test_build_unit_map_exceptions.py
integrations/bloomberg/research/tests/test_build_unit_map_classification_split.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-t-2.unit-map-exceptions.md
</paths>

READ-ONLY: every other file (including `field_map.json` itself -- NEVER write it), every S3 object. Scratch `.scratch/t2/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call, NO S3 write, NO write to the committed `field_map.json`. The replay works on a temp copy.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W2-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-t-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round18/t2_AC1.sh</invocation><expect>(?m)^t2 replay rc 0 shared_changed 0 shared_removed 0 type_changed 0 hitachi_reproduced \d+ of 214 non6501_added 0$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-t-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round18/t2_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: Hitachi's replay at HEAD -- 0 shared changes, removals or type changes, and 0 non-6501 additions. `hitachi_reproduced` is
  reported; entries the committed map carries that the exception shape records differently are named in the report. AC2: the
  builder's tests with the new one.

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-t-2.unit-map-exceptions.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you
   changed plus the instance.
4. Report ONCE: each AC line, the exception shape, and which of the committed 214 Hitachi entries the replay does not reproduce,
   and why.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-17 analysis s.4 cell 2 @`50a4593cba`. The checks were dry-run at base CLOUD `9dc713f359`:
- t2_AC1 FAIL: `t2 replay rc 0 shared_changed 23 shared_removed 0 type_changed 4 hitachi_reproduced 209 of 214 non6501_added 0`.
  The list diff matches elements by identity; a positional diff read 2918 through the CLI's sorted insertion.
- t2_AC2 FAIL (no tests ran).

The CTO's "byte-equal" is graded as 0 shared/type change plus reproduction reported. An exception entry is by construction a
6501-scoped addition the committed map does not carry.
<risk>LOCAL</risk>
<status>pending</status>
<round>18</round>
<slot>~2</slot>
<fabric>site-z</fabric>
