# AMGT_CORPUS task order -- `CRPS-x-2` -- ROUND 22: the unit apply writer -- resolved units into the map, each with its evidence and read count

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-x-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface (the map commit and re-derive are the issuer's act under a pair).
comp-iam: DECLARED-NOT-APPLICABLE -- S3 raw reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 22. Serves **the served unit on the names whose units the map could not
measure**.

## 1. THE CELL -- `CRPS-x-2`

**Where this came from.** `integrations/bloomberg/research/build_unit_map.py` has `discriminate_facts(facts, s3=None)` (round 21).
It returns, per `(security, mnemonic)`, `{"state": "RESOLVED"|"UNRESOLVED", "unit", "evidence"` (with a `reads` list)`, "reason"}`
from a cross-field read that never guesses. On the nine facts below, 8 resolve to `MILLIONS`, each on 1 read, and
`TSM US Equity` `CURR_ENTP_VAL` stays UNRESOLVED. Nothing yet writes a resolved unit into
`integrations/bloomberg/research/field_map.json`.

The map's shape per field:
- `unit` / `sign`: a scalar shared by all securities, or a per-security dict;
- `per_security_detail[<security>]`: `value_sampled`, `unit_status`, `sign_status`, `raw_stamp`, `derived_by`, and optionally
  `exception`;
- `measured_on`: the securities MEASURED on both.

The readers `model_block_pull._resolved_unit` / `_resolved_sign` honour a per-security non-MEASURED status or `exception` under a
scalar field (round 19).

**RULED -- what you build:**
1. `apply_discriminated(facts, field_map_path, s3=None) -> list[dict]` in `build_unit_map.py`. It calls `discriminate_facts(facts,
   s3)` and returns one dict per fact: `{"security", "mnemonic", "applied": bool, "reads": int, "reason"}`. For each RESOLVED fact
   ONLY, it writes into the map at `field_map_path`:
   - `per_security_detail[sec]["unit_status"] = "MEASURED"`;
   - `per_security_detail[sec]["unit_evidence"] = {"method": "cross_field_discriminator", "reads": <len of the evidence reads>,
     "detail": <the evidence>}`;
   - `sign_status`: classified afresh with the module's own `classify_sign` on `value_sampled`. MEASURED if it classifies, else
     it stays UNRESOLVED with its reason;
   - remove that security's `exception` if the unit was its only reason;
   - for a DICT-valued `unit` (or `sign`): set `unit[sec] = <resolved unit>` (and `sign[sec]` when MEASURED);
   - for a SCALAR `unit`: leave the scalar; the reader then returns it for that security because its status is MEASURED;
   - add `sec` to `measured_on` when unit and sign are both MEASURED and no exception remains.
2. It never writes an UNRESOLVED fact and never changes any other security's entry, any field-level shared key, or the top-level
   keys. It writes with `open(path, "w", encoding="utf-8", newline="\n")`.
3. `integrations/bloomberg/research/tests/test_build_unit_map_apply.py` (new), with stub raw and no network:
   - a RESOLVED fact on a dict field writes unit, status, evidence and read count;
   - a RESOLVED fact under a scalar field makes the reader return the scalar;
   - an UNRESOLVED fact writes nothing;
   - no other entry changes.
   Keep the builder's suites green.
4. Run the apply ONLY on a temp copy. Do NOT write the committed `field_map.json`. The commit and the re-derive of the moved
   blocks are the issuer's act under a pair.

## 3. SURFACES

<paths>
integrations/bloomberg/research/build_unit_map.py
integrations/bloomberg/research/tests/test_build_unit_map_apply.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-x-2.unit-apply-writer.md
</paths>

READ-ONLY: every other file (`field_map.json` NEVER written; `model_block_pull.py` read-only), every S3 object. Scratch `.scratch/x2/`.

Your worktree is a SPARSE cone (`lib integrations .tools .claude org docs rcg infra/logic`); `data/`, `portal/` and the rest of
`infra/` are absent by design. If you need a path outside the cone, file a row and stop that criterion; never disable the sparse
checkout.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible (no `newline=` on a `Path` text call).
- NO vendor call, NO S3 write, NO write to the committed `field_map.json`.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W2-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-x-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round22/x2_AC1.sh</invocation><expect>(?m)^x2 applied 8 of 9 skipped 1 changed_entries 8 other_changed 0 expected_set True reads_stated 8 tsm_unchanged True reader_6501_best_sales MILLIONS$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-x-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round22/x2_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: the apply on a temp copy of the committed map, diffed entry by entry against it:
  - exactly the 8 RESOLVED `(security, mnemonic)` entries change, each stating its read count;
  - 0 other changes, and TSM is unchanged;
  - the round-19 reader on the temp map now returns `MILLIONS` for 6501 BEST_SALES (UNRESOLVED on the committed map).
- AC2: your tests with the builder's suites (discriminate, exceptions, classification split).

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-x-2.unit-apply-writer.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you changed
   plus the instance.
4. Report ONCE: each AC line, the function's signature, and per fact the sign status after the apply.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-21 analysis ruling 3 @`0bf907bee8`. Dry-run at base CLOUD `2a4c7f5451`:
- x2_AC1 FAIL as expected (AttributeError: no `apply_discriminated`; no x2 line).
- x2_AC2 FAIL as expected (no tests ran).

Ruling 3's "2 reads for six" is superseded by the measurement: all 8 rest on 1 read (decomposition s.1a). The AC demands the
count be STATED, not a value.
<risk>LOCAL</risk>
<status>pending</status>
<round>22</round>
<slot>~2</slot>
<fabric>site-z</fabric>
