# TO ADVI_COTBKF.TO-CB-e-3 -- round 5 CB-e-3: the documents script holds back and counts every planned key under the C-RESTRICTED prefix

<to_id>ADVI_COTBKF.TO-CB-e-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~18</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-e-3` (`decompositions/ADVI_COTBKF_DECOMP.round5.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-e-3`, FWD-5: `data/assets/scripts/silver/commonwealth_documents.py` (round 4, CB-d-5) plans each of the 11,119 unique Commonwealth
documents to be unpacked once from the three bronze imaging archives into the silver documents store, and `--apply` writes them. Before
the issuer applies it, the script must guarantee it never writes a byte under the **C-RESTRICTED prefix** -- the firm bucket's prefix
that only Andrew's console user and one break-glass role may read or write (the policy is merged in
`infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf:177-275`, not yet applied).

**The prefix comes from the builder, never typed:** it is the key prefix `lib/opal_naming` builds for
`("commonwealth", <the cottonwood scope>, "bronze", "crm")`; at the cut it reads `commonwealth/cottonwood/bronze/crm/` (R20 register
entry X15). Resolve it the way the script already resolves its own addresses (`opal_naming`), in ONE function.

**The change.** In the plan (and therefore in `--apply`, which writes only what the plan admits): every planned object key that starts
with the restricted prefix is HELD BACK -- not written, listed in the plan output with its reason, and counted. The plan's last line
gains two fields, appended in this order after the existing ones: `held_restricted=<n> writable=<m>`, where `m` = planned objects less
held-back objects. Nothing else in the plan line changes. Expected on the real plan today: `held_restricted=0 writable=11119` (the
documents land under silver, not under bronze/crm) -- the guard exists so that a later change in the key builder or the input cannot
silently write into the restricted prefix.

**Tests** in `data/assets/scripts/silver/tests/test_commonwealth_documents.py`, each test name containing `restricted`: a stub plan with
one key under the prefix and two outside holds back exactly one and reports `held_restricted=1 writable=2`; the same stub with no
restricted key reports `held_restricted=0 writable=3` (the difference control); `--apply` against a stub S3 client makes zero put calls
under the prefix.

### ACCEPTANCE

<criterion id="CB5e3-AC1" cell_refs="CB-e-3"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_documents.py -k restricted</invocation><expect>passed</expect></criterion>
`CB5e3-AC1` -- the hold-back on stubs, with the difference control and the zero-put arm.

<criterion id="CB5e3-AC2" cell_refs="CB-e-3"><invocation>python data/assets/scripts/silver/commonwealth_documents.py --plan --out .scratch/advi_cotbkf/documents_plan_e3</invocation><expect>held_restricted=0 writable=11119</expect></criterion>
`CB5e3-AC2` -- the real plan over the bronze archives: every document still planned once, none under the restricted prefix.

<expected_criteria>CB5e3-AC1,CB5e3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scratch under `.scratch/`, uncommitted.
- **No `--apply`, no S3 write.** `--plan` reads bronze only. The apply is the issuer's act after the drain.
- **No typed bucket or key** in the script: the naming gate refuses them.
- **Rule 13:** a DS-lane script; your commit is a candidate.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W18-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_documents.py
data/assets/scripts/silver/tests/test_commonwealth_documents.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round5.md</decomp_doc> (round 5), cell `CB-e-3`.
<owned_cells>CB-e-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB5e3-AC1, CB5e3-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~18/ADVI_COTBKF.TO-CB-e-3.documents-hold-restricted.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB5e3-AC1,CB5e3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the DOCUMENTS-PLAN line, the test names and count, how the prefix is resolved (the builder call), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE code only; no schedule touched.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; denominator 0 principals; BLIND: none needed.
comp-adversary: RUN -- the prefix from the builder, never typed; the zero-put arm is counted by a stub client, not asserted; BLIND: the live bucket policy (not applied; CB-d-4).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-4 analysis @e363a194ed, E3 criterion (1); the apply half (criteria 2 and 3) is the issuer's act (decomposition round 5).
