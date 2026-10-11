# TO ADVI_COTBKF.TO-CB-bi-2.shared-infra-plan-proof -- round 61 CB-bi-2: `init` and `plan` of `shared-infra` succeed with 0 changes to the CRM statements; no apply

<to_id>ADVI_COTBKF.TO-CB-bi-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.7.0_AE_CloudOps~CB2</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>61</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bi-2` (`decompositions/ADVI_COTBKF_DECOMP.round61.md`) |
**outcome_ref:** FWD-7 | **depends_on:** `CB-bi-1`

---

## WORKER FACE

### THE CELL

**Do not start until this order's AMENDMENT names the commit of `CB-bi-1` and the worktree to plan in.**

**Read first:** the ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_CROSSBOX_XB-20261011T055236Z-0989_SHARED_INFRA_CRM_SCOPE_SELECTOR_20261011.md` (item 5 is your proof), and `/cloud-ops`.

**Your item. A PLAN ONLY. No `terraform apply`, no state verb (`import`, `mv`, `rm`, `taint`), no AWS write.**

1. In the worktree the amendment names (the branch that carries `CB-bi-1`), run `init` and `plan` of the root
   `infra/aws/terraform/shared-infra`, saving the plan to a file outside the repo and its JSON (`terraform show -json`) to
   `C:/dev/_cotbkf_private_evidence_20261009/r61/shared_infra_plan.json`. If `init` needs a provider download that the box's download
   rules do not allow, STOP and report; do not work around it.
2. As a control, show that the SAME root fails to plan at the base commit of that branch with the `one()` error (the defect), or
   cite site Z's measured failure if running it twice is not possible; say which.
3. Run the acceptance invocation and report its line.
4. **A resource this change moved is a STOP:** any create, update, delete or replace on a resource whose address matches the pattern
   in the criterion goes to `1.0.0_SA_CTO~DELL2` as a never-widen act; you do not apply it.
5. Other planned changes on this root (drift unrelated to this change) are REPORTED by count and address, not acted on.

### ACCEPTANCE

<criterion id="CB61bi2-AC1" cell_refs="CB-bi-2"><invocation>python -c "import json,re;d=json.load(open('C:/dev/_cotbkf_private_evidence_20261009/r61/shared_infra_plan.json',encoding='utf-8'));rc=d.get('resource_changes',[]);pat=re.compile(r'lgic_firm|restricted|breakglass|crm',re.I);w=[x for x in rc if pat.search(x['address'])];mv=[x for x in w if x['change']['actions']!=['no-op']];oth=[x for x in rc if not pat.search(x['address']) and x['change']['actions']!=['no-op']];print('CRM-PLAN resources=%d watched=%d watched_changed=%d other_changed=%d'%(len(rc),len(w),len(mv),len(oth)))"</invocation><expect>watched_changed=0</expect></criterion>
`CB61bi2-AC1` -- the plan succeeded (the JSON exists), the watched set is not empty, and 0 watched resources change. Report the
watched count: a watched count of 0 is a failed read, not a pass.

<criterion id="CB61bi2-AC2" cell_refs="CB-bi-2" judgment="true"/>
`CB61bi2-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the watched pattern covers the CRM restricted-prefix
statements, the break-glass role and the firm bucket policies (each named by address in the report); the control of step 2 is real.

<expected_criteria>CB61bi2-AC1,CB61bi2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and the file of this order. The plan file and its JSON live OUTSIDE the repo.
- **No apply. No state verb. No AWS write. No push. No merge of the worker's branch.**
- **Refusal clause.** If the plan fails for another reason, or a watched resource changes, stop. Write the exact error or the
  changed addresses in your report and a NEW surprise row (id `ADVI_COTBKF-D2-WCB2-S<k>`, `"fabric": "dell2"`, `surfaced_at` from
  the clock).

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round61.md</decomp_doc> (round 61), cell `CB-bi-2`.
<owned_cells>CB-bi-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB61bi2-AC1, CB61bi2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB2/ADVI_COTBKF.TO-CB-bi-2.shared-infra-plan-proof.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB61bi2-AC1,CB61bi2-AC2` BEFORE the flip. Mechanical: CB61bi2-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the `CRM-PLAN` line; the watched addresses; the plan's own summary line; the control of step 2; every other planned
change by address; whether `init` downloaded anything.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a plan; nothing is applied and no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE a plan with no IAM edit in this cell; the bucket policy statements the selector feeds are the plan's watched set and must read no-op; BLIND: comp-iam was not run on this root by the issuer.
comp-adversary: RUN -- the criterion fails on an empty watched set as well as on a changed one; a control shows the defect at the base; unrelated drift is counted separately so it cannot hide a watched change; BLIND: a resource the selector feeds whose address matches none of the four pattern words (the judgment criterion asks the CVO to check the coverage by address).
lane: 0.7.0_AE_CloudOps, plan only; no apply under this order.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ruling @27ba4d3769 (msg 4216), item 5; cross-box call XB-20261011T055236Z-0989; NFRA_IAMROLES202609 row 6 at site Z waits on this proof.
