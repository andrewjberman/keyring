# TO IRPT_BCKEND.TO-IB-pr-309 -- three AE roles read the Kimi API key through the exact secret, not a wildcard

<to_id>IRPT_BCKEND.TO-IB-pr-309</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~112</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-03</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>44</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 234 item 2 (msg 104804, @a5c484c7cb): "S299: narrow
astn/kimi/api-key-* to api-key-?????? in three AE iam.tf lines, one targeted safe-apply each; close on get-role-policy." |
**Decomp cell:** `IB-pr-309` (decomposition section 37) | **outcome_ref:** row S299 (least privilege on the Kimi key) |
**depends_on:** none. BUILT now; the three applies are the issuer's.

---

## WORKER FACE

**What is wrong.** Three IAM policies grant `secretsmanager` reads on `astn/kimi/api-key-*`. The trailing `*` admits any secret
whose name starts with `astn/kimi/api-key-`, not only the one key. Secrets Manager appends a hyphen and exactly six characters to
a secret's name in its ARN, so `astn/kimi/api-key-??????` admits exactly the secret `astn/kimi/api-key`. That is the form
`infra/aws/terraform/investor-reporting/ycharts/iam.tf:63` already uses.

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-112`. The three lines, at the base:
- `infra/aws/terraform/estate-report/iam.tf:283`
- `infra/aws/terraform/cot-pipeline/iam.tf:325`
- `infra/aws/terraform/bd-49f-auto-login/iam.tf:57`

**What you build.** In each of those three lines, replace `astn/kimi/api-key-*` with `astn/kimi/api-key-??????`. Change nothing
else on the line or in the file: no reformatting, no other ARN, no comment.

<criterion id="IB44-1-AC1" cell_refs="IB-pr-309"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r44/p44_kimi_secret_narrow.py" . IB44-1-AC1</invocation><expect>IB44-1-AC1 PASS</expect></criterion>
`IB44-1-AC1` -- in all three files, every `astn/kimi/api-key` ARN reads `-??????` and none reads `-*`. Base: FAIL.

<criterion id="IB44-1-AC2" cell_refs="IB-pr-309"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r44/p44_kimi_secret_narrow.py" . IB44-1-AC2</invocation><expect>IB44-1-AC2 PASS</expect></criterion>
`IB44-1-AC2` -- a GUARD: against base 80ba60328c, only the `astn/kimi/api-key` lines change, each only by `-*` -> `-??????`, and
no line is added or removed. Base: PASS.

<expected_criteria>IB44-1-AC1,IB44-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** none. No `terraform plan` or `apply`, no IAM call. The three targeted applies are the issuer's.
- **Refusal clause.** A change to any other line, or to any other secret's ARN, is a defect: stop and file a row.

<paths>
infra/aws/terraform/estate-report/iam.tf
infra/aws/terraform/cot-pipeline/iam.tf
infra/aws/terraform/bd-49f-auto-login/iam.tf
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~112/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 37 (round 44, workstream ~P), cell `IB-pr-309`.
<owned_cells>IB-pr-309</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB44-1-AC1, IB44-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~112/IRPT_BCKEND.TO-IB-pr-309.kimi-secret-arn-narrowed.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB44-1-AC1,IB44-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, and any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- three IAM inline policies (estate-report, cot-pipeline and bd-49f-auto-login roots, lane 0.7.0_AE_CloudOps, routed to this seat by CTO batch 234); the change narrows one secret ARN in each; 0 served bytes move; the issuer applies each root with one targeted safe-apply and closes on get-role-policy.
comp-iam: RUN -- narrowing only: the granted set shrinks from astn/kimi/api-key-* to the one secret astn/kimi/api-key (six-character suffix); the runner already conforms (CTO batches 208-209).
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB44-1-AC1 base FAIL (three wildcards), IB44-1-AC2 base PASS (guard), dry-run at base 80ba60328c 2026-10-03 ~22:5xZ.
lane: the <paths> block IS the grant.
</preflight>
