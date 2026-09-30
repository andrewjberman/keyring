# AMGT_CORPUS task order -- `CRPS-z-1` -- ROUND 24: the 602 still-UNRESOLVED served units by class, and the families that close them

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-z-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface (a map commit and re-derive are a later issuer act under a pair).
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 24. Serves **every served figure's unit**.

## 1. THE CELL -- `CRPS-z-1`

**Where this came from.** After round 23, the newest served model block of 98 keys carries **602 figures whose unit reads
`UNRESOLVED-ON-<security>: <reason>`**. That count excludes the slash-bearing keys `BP/_LN_Equity` and `NG/_LN_Equity`, which are
EXCLUDED under row `Z-S64` and must be named as EXCLUDED in your table.

The unit comes from `integrations/bloomberg/research/field_map.json`, built by `integrations/bloomberg/research/build_unit_map.py`:
- `classify_unit` and its families (`TEXT_FIELDS`, `PERCENT_FIELDS`, `ABSOLUTE_OR_MILLIONS_FIELDS`, `PER_SHARE_FIELDS`,
  `RATIO_FIELDS`, the share-count sets and `PRICE_FIELDS`);
- round 23's per-share cross-field band against `PX_LAST`, applied only when `CRNCY` equals `EQY_FUND_CRNCY`.

It is read per figure through `model_block_pull._resolved_unit`. About 199 of the 602 are per-share names outside their band; the
rest carry other reasons.

**RULED -- what you build:**
1. **The class table, BY CENSUS:** `deliverables/0.9.0_WK_AMGT_CORPUS~1/UNRESOLVED_CLASSES_ROUND24.json` (+ `.md`), covering every
   UNRESOLVED figure of the newest served block of each non-slash key.
   - Its shape: `{"denominator_keys": 98, "excluded": [{"key": "BP/_LN_Equity", "row": "Z-S64"}, {"key": "NG/_LN_Equity", "row":
     "Z-S64"}], "before_total": 602, "classes": [{"mnemonic", "reason_class", "securities": [...], "count", "disposition":
     "family"|"stays_unresolved", "reason"}], "remaining_after": <int>}`.
   - `reason_class` is the reason text with the numbers normalised. The class counts sum to `before_total`.
2. **The families that close a class.** Only where the census names a real, stated rule: a field-basis definition, or a
   cross-field read in the same currency. NEVER a default scale and never magnitude alone. Each change goes into
   `build_unit_map.py`'s classifier, with its ground in a code comment.
   - A class you cannot close stays UNRESOLVED, with its `reason` in the table (for example "reporting currency differs from
     listing currency; no same-currency PX_LAST").
3. `remaining_after` is the UNRESOLVED count your builder leaves. The issuer's checker recomputes it independently: it rebuilds a
   temp copy of the committed map over the crosswalk population and resolves every figure through the reader. The two must agree.
4. `integrations/bloomberg/research/tests/test_build_unit_map_families_round24.py` (new):
   - one test per family added;
   - one test that an unclosable class stays UNRESOLVED;
   - no network.
   Keep the builder's suites green.
5. Do NOT write the committed `field_map.json`, do NOT touch `model_block_pull.py` or `unit_anchor.py`, and do NOT derive.

## 3. SURFACES

<paths>
integrations/bloomberg/research/build_unit_map.py
integrations/bloomberg/research/tests/test_build_unit_map_families_round24.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/UNRESOLVED_CLASSES_ROUND24.json
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/UNRESOLVED_CLASSES_ROUND24.md
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-z-1.unresolved-classes.md
</paths>

READ-ONLY: every other file (`field_map.json` NEVER written), every S3 object. Scratch `.scratch/z1/`.

Your worktree is a SPARSE cone (`lib integrations .tools .claude org docs rcg infra/logic`). Never disable the sparse checkout.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call, NO S3 write, NO write to `field_map.json`, NO derive.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-z-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round24/z1_AC1.sh</invocation><expect>(?m)^z1 keys 98 excluded 2 measured_before 602 table_total 602 classes [1-9]\d* dispositions_complete True projected_after \d+ table_remaining \d+ consistent True$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-z-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round24/z1_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: your table sums to the checker's own served count (602 over 98 keys, 2 EXCLUDED); every class carries a disposition and a
  reason; and your `remaining_after` equals the checker's independent projection of your builder (about 70 s). How many you close
  is reported, not demanded.
- AC2: your family tests with the builder's suites.

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-z-1.unresolved-classes.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you changed
   plus the instance.
4. Report ONCE: each AC line, the class table's top classes, each family added with its ground, and what stays UNRESOLVED and why.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-23 analysis rulings 3-4 @`4cbd61daf8`. Dry-run at base CLOUD `da4fb630b5` (worktree `C:/tmp/coox-crps24-issue`):
- z1_AC1 FAIL as expected: `z1 keys 98 excluded 2 measured_before 602 table_total 0 classes 0 dispositions_complete False
  projected_after 602 table_remaining -1 consistent False`.
- z1_AC2 FAIL as expected (no tests ran).
<risk>LOCAL</risk>
<status>pending</status>
<round>24</round>
<slot>~1</slot>
<fabric>site-z</fabric>
