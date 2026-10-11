# TO IRPT_DASHBD.TO-DB-b-116 -- one measurement: does method row 3 describe the Cottonwood rows -- its income treatment read against row 3's text field by field -- and does a dim row 3 partition exist at the builder address

<to_id>IRPT_DASHBD.TO-DB-b-116</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~91</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ruling msg 4036 on row IRPT_DASHBD-D2-W89-S1 | **Decomp cell:** `DB-b-116` (decomposition section 62) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-114 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-91`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~91/`.

**THE CLIENT-DATA RULE (binding):** never print an account number or a client figure in a commit message, a record, a row or a report.

**The cell (`DB-b-116`).** DB-b-114's record (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~89/COTTONWOOD_VALUE_RULE24.json`) concluded
that the 107,316 Cottonwood rows are stamped `method_version` 3. The CTO ruled (msg 4036) that stamping 3 asserts EVERYTHING method row 3 states,
including its income basis, and the record left that unestablished (row `IRPT_DASHBD-D2-W89-S1`). This cell measures it. True: the stamp is 3. False:
row 3 does not describe these rows and a new method row is proposed later under rule 24. You do not propose it and you edit no producer.

In `C:/dev/wk-irpt-dashbd-91`:
1. **What row 3 states.** Read `METHOD_ROWS` row 3 in `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`, the function that writes the
   `dim_return_method` row (search `TABLE_METHOD`), and every field that written row carries for `method_version` 3 -- including the fields it
   INHERITS from module constants or from row 2's path (income basis, flow timing, fee basis, value basis, tolerance, anything else). List every
   field with file and line. Print the denominator: fields in the written row.
2. **What Cottonwood does.** Read the adapter `commonwealth_account_return_daily.py` (find it with `comp-find`), the `_commonwealth_delivery` entry
   in `data/assets/scripts/gold/irpt_reporting/sources.json`, and ADVI_COTBKF's records of how the 107,316 rows were computed (start from row
   `ADVI_COTBKF-D2-W66-S1` in `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md`). For EACH field from step 1, say what
   Cottonwood's computation actually does, with file and line.
3. **`fields`**: [{field, row3_states, cottonwood_does, verdict, evidence: [{file, line}]}] with verdict `TRUE` (row 3's statement is true of these
   rows), `FALSE` (it is not), or `NOT_STATED` (row 3 leaves it to the entry's fields, and you name the entry field that carries it). The income
   basis MUST be one of the fields. **`verdict`**: `ROW3_TRUE` only if no field is `FALSE`; otherwise `ROW3_FALSE`, naming the fields.
4. **`dim_partition`**: build the address with the builder exactly as the producer does (`opal_naming.address("irpt", <firm>, "gold",
   "dim_return_method", "method_version=3")` for the firm scope the Cottonwood entry resolves to; print the address, never type it). Read it with ONE
   S3 list or head through the `.tools/aws` shim and record {address, exists, read: {call, result}}. A read that fails is not an absence: record the
   failure as it is. **`positive_control`**: the same read on `method_version=2` for the 49F firm scope, which exists.
5. Write `ROW3_VS_COTTONWOOD.json` and a one-page `ROW3_VS_COTTONWOOD.md`.

<criterion id="DB60-1-AC1" cell_refs="DB-b-116"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r60/p60_round60.py" . DB60-1-AC1</invocation><expect>DB60-1-AC1 PASS</expect></criterion>
`DB60-1-AC1` -- every field of the written row 3 is read against Cottonwood's computation with file-and-line evidence, the verdict follows from the fields, and the dim row 3 partition read carries a positive control. Base: FAIL.

<expected_criteria>DB60-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/`, `portal/` or `org/standards/`.
- **This order's exception:** two S3 READS (the dim row 3 address and its positive control). No object body is downloaded.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~91/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~91/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-116.row3-vs-cottonwood.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 62 (round 60), cell `DB-b-116`.
<owned_cells>DB-b-116</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB60-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~91/IRPT_DASHBD.TO-DB-b-116.row3-vs-cottonwood.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB60-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, the criterion's last line, the verdict, each field's verdict in one line, the dim row 3 address and whether it exists with the positive control, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a measurement record only; no producer, contract or infra edit.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: two S3 reads inside the existing read set; no role change.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB60-1-AC1 FAIL at base (no record). CTO ruling msg 4036; row IRPT_DASHBD-D2-W89-S1.
lane: the <paths> block IS the grant.
</preflight>
