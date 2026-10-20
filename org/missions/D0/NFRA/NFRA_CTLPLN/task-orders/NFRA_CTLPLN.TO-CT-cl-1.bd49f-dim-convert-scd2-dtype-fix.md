# TO NFRA_CTLPLN.TO-CT-cl-1.bd49f-dim-convert-scd2-dtype-fix -- workstream OUTCOME round 39 (cell CT-cl-1): the 49F dim converter's SCD2 fold compares each tuple column at its schema type, so an unchanged account stays unchanged

<to_id>NFRA_CTLPLN.TO-CT-cl-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~153</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<status_reason>Complete, 2026-10-20. Worker 0.9.0_WK_NFRA_CTLPLN~153 built it (branch wk-NFRA_CTLPLN-153, head 625541626f; the first run was blocked by the issuer's sparse checkout omitting data/assets/scripts/lib, row W153-S1, fixed by the issuer). CTcl1-AC1: `29 passed` (base 26); the issuer re-ran in the worker tree (29 passed) and ran the seam probe on the REAL stored dim (date=2026-09-28, 282,857 rows, 5,338 open, read-only): the unfixed file closes 5338 of 5338 open accounts against a today frame with flat_fee int64; the fixed file closes 0 of 5338, total rows 282,857 unchanged; control with one real flat_fee change closes 1. The two converter copies are byte-equal; sha256 bc3019570d49...00d503 equals the BUILD_MANIFEST value. Nothing deployed: the apply leg is CT-cm-1.</status_reason>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>39</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-cl-1` (`decompositions/NFRA_CTLPLN_DECOMP.round30.md`, amendment 12) | **outcome_ref:** an inbound ask, no FWD (the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/DIAG_BD49F_DIM_CONVERT_OOM_XREF_STALE_20261020.md` @e99ca8caa4, part 1 of three; msg 109983) |
**depends_on:** none (its apply leg `CT-cm-1` follows its merge)

---

## WORKER FACE

### THE CELL

`data/assets/scripts/silver/bd49f_dim_conversion.py` (the 49F dim converter) keeps an SCD2 dim: `scd2_fold(prev, today, as_of)` compares, per account, the tuple `SCD2_TUPLE` of the prior open row with today's row, and a changed tuple closes the open period and opens a new one.

THE DEFECT (MEASURED by the CTO, 2026-10-20): the comparison is `_tuple_frame` (inside `scd2_fold`, about line 478): `df[list(SCD2_TUPLE)].fillna("<NA>").astype(str)`. It compares the columns AS STRINGS, so the string depends on the dtype each frame happens to carry. The prior partition is read from parquet, where `flat_fee` is float64, so a zero prints `"0.0"`. Today's frame is built in `build_dim` (about line 343) as `dim["flat_fee"] = pd.to_numeric(d["Flat Fee.1"], errors="coerce")`, which for an all-integer column yields int64, so the same zero prints `"0"`. The tuples differ for EVERY account on EVERY run: all 5,338 accounts close and reopen daily (only 3 really changed between the 09-25 and 09-28 periods), the stored history grew to 282,857 rows, and the converter's Lambda (1024 MB) ran out of memory every trading day since 2026-09-29.

THE FIX (the CTO's part 1): in the fold's comparison, cast every tuple column to its `DIM_SCHEMA` type before stringifying, so a float column is float64 on both sides, a bool column is bool, a string column is string. Or equivalently cast `flat_fee` to float64 where it is built. Prefer the cast in the comparison (it covers every numeric tuple column and a prior partition read with another dtype), keep the `<NA>` handling for nulls, and change nothing else: the SCD2 rules in the docstring of `scd2_fold` hold exactly as they are.

BUILD:
1. Edit `data/assets/scripts/silver/bd49f_dim_conversion.py` as above. Make the same change byte-for-byte in the vendored copy `infra/aws/lambda/opal-assets/opal-assets-bd49f-dim-convert/bd49f_dim_conversion.py` (the two files are byte-identical at the base; copy the edited repo file over it).
2. Add THREE tests to `data/assets/scripts/silver/tests/test_bd49f_dim_conversion.py`, in the style of the existing `test_scd2_*` tests (use its `_today` helper and its D1/D2 constants):
   - `test_scd2_dtype_float_zero_vs_int_zero_is_unchanged`: a prior frame whose `flat_fee` is float64 `0.0` and a today frame whose `flat_fee` is int64 `0` for the same account and otherwise identical: the fold leaves ONE row for the account, `is_current` True, `effective_from` still the prior vintage, no closed row.
   - `test_scd2_dtype_real_flat_fee_change_still_closes_and_opens` (the difference control): the same shape with today's `flat_fee` `25.0` (a real change): the fold returns TWO rows for the account, one closed (`effective_to` = the fold date, `is_current` False) and one open.
   - `test_scd2_dtype_vendored_copy_is_byte_identical`: reads both files named in step 1 as bytes and asserts they are equal.
3. In `infra/aws/lambda/opal-assets/opal-assets-bd49f-dim-convert/BUILD_MANIFEST.json` set `vendor_sha256["bd49f_dim_conversion.py"]` to the sha256 (lowercase hex) of the edited file and set `memory_mb` to `3008` (the memory bump itself is applied by another order; this file only records it). Change no other field.
4. Run `python -m pytest data/assets/scripts/silver/tests/test_bd49f_dim_conversion.py -q` under `timeout 120`. The base reads `26 passed`; after your change it reads `29 passed`.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~153/`. THIS IS A WORLD-CLASS CELL BY ITS PATH (the gate infers the class from `infra/aws/lambda/`): you run NO `terraform`, NO `aws`, NO deploy, NO zip build, and you do NOT invoke the Lambda; the build of the zip, the apply and the real run against the stored dim are the issuer's and a CloudOps seat's. You do not touch `infra/aws/terraform/`, the `function-map` folder, or any other Lambda. The tests use in-memory frames only (no S3). ASCII only in every file you write. If a test you add cannot be made to fail at the base for the reason above, that is a surprise row, not a weaker test.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTcl1-AC1" cell_refs="CT-cl-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_bd49f_dim_conversion.py -q</invocation><expect>29 passed</expect></criterion>
`CTcl1-AC1` -- the three new tests pass beside the 26 existing ones: the float-zero versus int-zero tuple is unchanged, a real `flat_fee` change still closes and opens (the difference control), and the vendored copy is byte-identical (base: `26 passed`, so this reads FAIL at the base as expected). Report the whole last line.
</proof_of_spec>

<expected_criteria>CTcl1-AC1</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~153/NFRA_CTLPLN.TO-CT-cl-1.bd49f-dim-convert-scd2-dtype-fix.proof_of_spec.json`, validate it with the checker `.claude/agents/worker.md` names, and flip this order `complete` only when the criterion passes.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round30.md</decomp_doc>
<owned_cells>CT-cl-1</owned_cells>
</decomp_ref>

<paths>
data/assets/scripts/silver/bd49f_dim_conversion.py
data/assets/scripts/silver/tests/test_bd49f_dim_conversion.py
infra/aws/lambda/opal-assets/opal-assets-bd49f-dim-convert/bd49f_dim_conversion.py
infra/aws/lambda/opal-assets/opal-assets-bd49f-dim-convert/BUILD_MANIFEST.json
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE (never travels to the worker)

Issued 2026-10-20 by `2.0.0_SA_COO~C` on the CTO's msg 109983 (record `DIAG_BD49F_DIM_CONVERT_OOM_XREF_STALE_20261020.md` @e99ca8caa4, part 1 of three). Parts 2 (memory, restores today) and 3 (one-time compaction under a never-widen pair) are `CT-ck-1` (TO-APPLY-34) and a later amendment. One criterion: the build, plus the byte-identical copy and the difference control inside it (the verification diet). Seam probe against the real neighbour (the stored dim at `date=2026-09-28`, read-only) is the issuer's at the drain, with a negative control.

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is read or changed by this cell (the daily scheduler is untouched).
comp-iam: DECLARED-NOT-APPLICABLE no IAM or policy change, no boto3 call added.
comp-adversary: RUN -- a test that passes at the base (the float/int zero test must FAIL on the unfixed fold; the issuer re-runs the new tests against the base file as the mutant); a cast that hides a real change (the control test: flat_fee 0.0 to 25.0 still closes); a cast that drops the null marker (an all-null column stays unchanged against an all-null column); a copy that drifts (the byte-identity test); a manifest hash left stale (the issuer recomputes it at the merge).
risk: WORLD by path class (a Lambda source file), no deploy from the cell; the apply leg is `CT-cm-1` after the merge.
</preflight>
