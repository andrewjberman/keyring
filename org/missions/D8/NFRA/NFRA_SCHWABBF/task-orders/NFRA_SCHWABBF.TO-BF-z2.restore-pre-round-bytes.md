# TO NFRA_SCHWABBF.TO-BF-z2 -- restore the five round-1 master-form files to their pre-round bytes

<to_id>NFRA_SCHWABBF.TO-BF-z2</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~1</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-z-2` (`decompositions/NFRA_SCHWABBF_DECOMP_R2.md`) |
**outcome_ref:** FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-z-2`. CTO ruling 3 of the round-1 analysis (msg 109909): the round-1 key-function work was built on the MASTER form (`schwab/<master>/bronze/...`) and PRD v0.5 moved C-KEYFORM to the FIRM form (`schwab/<firm>/bronze/...`), by Andrew-direct 2026-10-20 ~14:3xZ
("abiding by the path structure that already exists in that bucket"). One of the round-1 files, `data/black_diamond/scripts/bronze/_monolith_bronze.py`, is mapped by the deploy gate to `s3://opal-data-bd/code/`, so the master-form bytes must not stay on the shared branch.
Put these FIVE files back to their pre-round bytes, byte for byte, in ONE commit:

1. `data/black_diamond/scripts/bronze/_monolith_bronze.py`
2. `data/canonical/schwab/silver/_canonical_silver_lib.py`
3. `data/canonical/schwab/build_canonical_daily.py`
4. `data/canonical/schwab/silver/build_fact_tax_1099div.py`
5. `data/canonical/schwab/tests/test_canonical_daily_date_axis.py`

The pre-round bytes are the blobs at commit `5f1ad506a4` (the round-1 issuance commit; the round-1 chain-A merge `293346aff1` has the same blobs for these five files at its first parent). Do it with `git show 5f1ad506a4:<path> > <path>` for each, never by retyping. Do not touch any other file.
The round-1 tests `data/canonical/schwab/tests/test_bronze_key_form.py` and `test_move_bronze_key_form.py` and the tool `data/canonical/schwab/keyform/move_bronze_key_form.py` stay as they are; they will fail or sit dormant until round 2's later cells rework them. The master-form work stays recoverable at `293346aff1`. Do not run those tests as a criterion.

### ACCEPTANCE

<criterion id="BF2-z2-AC1" cell_refs="BF-z-2"><invocation>python org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/2.0.0_SA_COO~SB/R2_CHECKS/restore_check.py</invocation><expect>^RESTORE-OK files=5$</expect></criterion>
`BF2-z2-AC1` -- the five blobs at HEAD equal the five blobs at `5f1ad506a4`.

<criterion id="BF2-z2-AC2" cell_refs="BF-z-2"><invocation>python -m pytest data/canonical/schwab/tests/test_canonical_daily_date_axis.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF2-z2-AC2` -- the control: the restored daily-builder test file passes against the restored builder (16 passed at the base).

<expected_criteria>BF2-z2-AC1,BF2-z2-AC2</expected_criteria>

Dry-run at the base 2026-10-20: AC1 `RESTORE-FAIL differing=5 of 5` (rc 1) -- FAIL as expected; AC2 PASS as expected (a control: at `5f1ad506a4` the file reads 16 passed; at the current head the new-layout file runs 20 passed, so read the count you get).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. LOCAL: no S3, no network, no deploy.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the check.

<paths>
data/black_diamond/scripts/bronze/_monolith_bronze.py
data/canonical/schwab/silver/_canonical_silver_lib.py
data/canonical/schwab/build_canonical_daily.py
data/canonical/schwab/silver/build_fact_tax_1099div.py
data/canonical/schwab/tests/test_canonical_daily_date_axis.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R2.md</decomp_doc> (round 2), cell `BF-z-2`.
<owned_cells>BF-z-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF2-z2-AC1, BF2-z2-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~1/NFRA_SCHWABBF.TO-BF-z2.restore-pre-round-bytes.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF2-z2-AC1,BF2-z2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the RESTORE-OK line, the pytest summary line, the one commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- restore of five files.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters; this cell touches no IAM and no network; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- the deploy-gate mapping of `data/black_diamond/scripts/bronze/*.py` to `opal-data-bd` is the reason for the order and is stated in the face.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-1 analysis ruling 3 (msg 109909); decomposition round 2 cell BF-z-2.
