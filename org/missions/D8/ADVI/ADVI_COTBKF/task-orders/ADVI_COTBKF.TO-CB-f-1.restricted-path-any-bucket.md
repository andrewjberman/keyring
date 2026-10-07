# TO ADVI_COTBKF.TO-CB-f-1 -- round 6 CB-f-1: the documents hold-back matches the restricted key path in any bucket; the plan counts crm source keys

<to_id>ADVI_COTBKF.TO-CB-f-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~20</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-f-1` (`decompositions/ADVI_COTBKF_DECOMP.round6.md`) |
**outcome_ref:** FWD-5 (row S14) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-f-1`: `data/assets/scripts/silver/commonwealth_documents.py` plans the 11,119 unique Commonwealth documents (read from bronze imaging
archives) and `--apply` writes them to the silver documents store. Round 5 gave it a hold-back: any planned key under the **C-RESTRICTED
prefix** is not written and is counted (`held_restricted=<n> writable=<m>` on the plan's last line). That hold-back is aimed at the wrong
place. `restricted_prefix()` (lines 80-83) builds the prefix with `opal_naming.address(...)`, which returns
`s3://opal-data-assets/commonwealth/cottonwood/bronze/crm/`, and compares full URIs. But the restricted prefix actually lives in a
DIFFERENT bucket: by the estate's register entry X15 (`infra/logic/06_CONFORMANCE_LEDGER.md` line 149), the CRM zip and its restricted
prefix `commonwealth/cottonwood/bronze/crm/` sit in `opal-data-cottonwood`, and `address()` has no route there. So today the guard
watches a prefix in the wrong bucket.

**Change 1 -- match the PATH in any bucket.** Build the restricted path from `opal_naming.key("commonwealth", <the cottonwood scope>,
"bronze", "crm", "date=<d>")` (the same arguments, `key()` instead of `address()`), drop the partition segment, and hold back any planned
object whose KEY (the part after the bucket) starts with that path, **whatever its bucket**. Never type the path or a bucket name.

**Change 2 -- count the crm SOURCE keys.** The plan reads its source documents from bronze. Count the planned source keys (the objects
the plan reads from) whose key starts with the same restricted path, and append to the plan's last line, after the existing fields:
`crm_source_keys=<n>`. Expected today: `crm_source_keys=0` (the documents come from the imaging archives, not the CRM zip). If any
source key is under the path, the plan still prints the line, and `--apply` writes nothing at all (refuse the whole apply with rc 1),
because a restricted source must never be unpacked into silver.

**Tests** in `data/assets/scripts/silver/tests/test_commonwealth_documents.py`, each name containing BOTH `restricted` and `any_bucket`:
the same restricted key planned under `opal-data-assets` and under `opal-data-cottonwood` is held back in both (two arms, one per
bucket); a key outside the path is written in both buckets (the difference control); a plan with one crm source key prints
`crm_source_keys=1` and its `--apply` against a stub client makes zero puts. Keep the round-5 `restricted` tests passing.

### ACCEPTANCE

<criterion id="CB6f1-AC1" cell_refs="CB-f-1"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_documents.py -k "restricted and any_bucket"</invocation><expect>passed</expect></criterion>
`CB6f1-AC1` -- the path held back in both buckets, with the difference control and the zero-put arm.

<criterion id="CB6f1-AC2" cell_refs="CB-f-1"><invocation>python data/assets/scripts/silver/commonwealth_documents.py --plan --out .scratch/advi_cotbkf/documents_plan_f1</invocation><expect>held_restricted=0 writable=11119 crm_source_keys=0</expect></criterion>
`CB6f1-AC2` -- the real plan: every document still planned once, none held, no crm source key.

<expected_criteria>CB6f1-AC1,CB6f1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scratch under `.scratch/`, uncommitted.
- **No `--apply`, no S3 write.** `--plan` reads bronze only.
- **No typed bucket or key** in the script.
- **Rule 13:** a DS-lane script; your commit is a candidate.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W20-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_documents.py
data/assets/scripts/silver/tests/test_commonwealth_documents.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round6.md</decomp_doc> (round 6), cell `CB-f-1`.
<owned_cells>CB-f-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB6f1-AC1, CB6f1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~20/ADVI_COTBKF.TO-CB-f-1.restricted-path-any-bucket.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB6f1-AC1,CB6f1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the DOCUMENTS-PLAN line, the test names and count, how the path is built (the `key()` call), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE code only; no schedule touched.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; denominator 0 principals; BLIND: none needed.
comp-adversary: RUN -- the path from key(), never typed; bucket-agnostic match tested in both buckets with a difference control; a crm source refuses the whole apply; BLIND: the live C-RESTRICTED policy (not applied).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: row S14; `1.0.0_SA_CTO~DELL2` re-ruling msg 264 (E3's CTO half, conditions 1-2); round-5 analysis @21843491cd section 3.
