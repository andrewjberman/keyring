# TO IRPT_DASHBD.TO-DB-b-86 -- E4: the first real retained Performance client statement -- one Cottonwood household's submission retained and its document persisted through the live writer as svc-custody-statement, both read back LIVE, and the other-firm refusals (49financial, inflection) read

<to_id>IRPT_DASHBD.TO-DB-b-86</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~DB2</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>41</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 9.1 (msg 3011; the IRPT_CUSTDY handover @185805a565), enrichment item E4 | **Decomp cell:** `DB-b-86` (decomposition section 43) | **outcome_ref:** FWD-12 | **depends_on:** DB-b-84 (the token) and DB-b-85 (the runner), both drained.

---

## WORKER FACE

You are the seat `0.7.0_AE_CloudOps~DB2` (seated for IRPT_DASHBD, MSTR msg 2572). Work in your own linked worktree, cut from box/dell2. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/`.

**The cell (`DB-b-86`).** It starts after DB-b-84 (the token) and DB-b-85 (the runner) have drained. This is IRPT_CUSTDY's CU-g-5 (E2a), now
IRPT_DASHBD FWD-12. It is the pair's positive and negative arms (steps 4-6 of the pair `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/NEVER_WIDEN_PAIR_SVC_CUSTODY_STATEMENT_MINT.md`), and it carries E-P9's persist reads
(the ~P handover @4bfb22b033).

1. **The run.**
   - Read the token from `opal/investor-reporting/svc-custody-statement` into the environment for the call only; never print or write it.
   - Run `python data/assets/scripts/gold/irpt_custody/e2a_real_statement.py run --refs org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/E2A_REFS.json`: ONE submission for ONE
     Cottonwood household (the project's existing pick), and ONE persist with `selected_tenant=cottonwood`.
   - Expect 2xx and a retained `CUSTODY_REPORT` reference.
   - Commit the ledger leg.
2. **The negative arms.** With the same token:
   - persist with `selected_tenant=49financial`, and again with `selected_tenant=inflection`. Each must be refused (401/403 or NOT_AUTHORIZED /
     OBJECT_NOT_COVERED) with nothing written. Record `other_firm` [{firm, refused, status, written}] in the refs file.
   - Make one unrelated scoped read, named in the ledger, which must be refused or return zero rows.
3. **The read-backs** are the criteria below. They re-read the LIVE store, never the run's own output.

**Opal-internal only.** No client-facing page is pushed; a PROD render is Andrew's word (row 0347, CU-g-6). The CVO grades the real
artifact.

<criterion id="DB41-3-AC1" cell_refs="DB-b-86"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r41/p41_round41.py" . DB41-3-AC1</invocation><expect>DB41-3-AC1 PASS</expect></criterion>
`DB41-3-AC1` -- the real submission is retained under irpt-custody-x10-v1, read live. Base: FAIL.

<criterion id="DB41-3-AC2" cell_refs="DB-b-86"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r41/p41_round41.py" . DB41-3-AC2</invocation><expect>DB41-3-AC2 PASS</expect></criterion>
`DB41-3-AC2` -- the household document is persisted as CUSTODY_REPORT through the live writer, read live. Base: FAIL.

<criterion id="DB41-3-AC3" cell_refs="DB-b-86"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r41/p41_round41.py" . DB41-3-AC3</invocation><expect>DB41-3-AC3 PASS</expect></criterion>
`DB41-3-AC3` -- the same token is refused for 49financial and inflection with nothing written. Base: FAIL.

<expected_criteria>DB41-3-AC1,DB41-3-AC2,DB41-3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's acts:** ONE submission and ONE persist through the live product path, plus two refused persists and one refused read. No
  apply, no IAM change, no direct table or S3 put.
- Figures stay in the retained store: files and messages carry refs and counts only.
- A refusal on the Cottonwood path is a finding: file a row and stop. Never work around it.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-86.e2a-real-statement-apply.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 43 (round 41), cell `DB-b-86`.
<owned_cells>DB-b-86</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB41-3-AC1, DB41-3-AC2, DB41-3-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/IRPT_DASHBD.TO-DB-b-86.e2a-real-statement-apply.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB41-3-AC1,DB41-3-AC2,DB41-3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the household's opaque id, the two refs and revisions, each call's status, the other-firm refusals, and the ledger, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- two writes through the live product path (one retained submission, one persisted CUSTODY_REPORT) for one Cottonwood household; the other-firm arms prove the radius does not widen.
comp-iam: RUN -- the run exercises svc-custody-statement's admission (IB-pr-385) and the reader grant; it changes no IAM.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes; the route is IRPT_BCKEND's, already live.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: a one-off act; no schedule.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB41-3-AC1/AC2/AC3 FAIL at base (no runner, no refs). Pair steps 4-6; CTO ADDENDUM 9.1.
lane: the <paths> block IS the grant.
</preflight>
