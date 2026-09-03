# TO NFRA_OPSEC202609.TO-OP-S-29 -- THE LOG DESTINATION'S TWO SERVICE GRANTS GET THE SOURCE CONDITIONS C-16 ALREADY CLAIMS THEY HAVE: `aws:SourceAccount` on BOTH, `aws:SourceArn` only where the service supports it and MEASURED per service, with delivery proven to CONTINUE across the change (OP-s-29, FWD-5)

<to_id>NFRA_OPSEC202609.TO-OP-S-29</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~S</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete</status>

**BLOCKER: NONE REMAINING.** It was `OP-s-28`, which went COMPLETE at 19:2xZ when `TO-OP-S-17R-28` flipped. **GO after `TO-OP-S-4-18` goes terminal** -- one task order at a time, not a dependency.

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (ENDPOINT FWD-5; **C-16 as amended at v0.11/v0.12**, :531-546 the in-scope ruling and the floor) - **Decomp cell:** `OP-s-29` (v0.1.11, s.1a; mirrors manifest **S28** as a SECOND ACT on that surface) - **Lane:** `infra/aws/terraform/opsec/`, AE lane - **Round:** 3.

---

## THE CELL -- a PRD text that claimed a control the world does not have

Row **Z-S60** (`0.7.0_AE_CloudOps~S`, during `TO-OP-S-17R-28`'s ALIGN limb) found that C-16 describes the log destination's two service grants as *"each with SourceAccount + SourceArn"*. **Verified independently at the issuer's seat at `s3.tf:117-160`: one of the four asserted condition slots exists.**

| grant | principal | `aws:SourceAccount` | `aws:SourceArn` |
|---|---|---|---|
| `AllowCloudFrontAccessLogDelivery` | `delivery.logs.amazonaws.com` | **present** | **ABSENT** |
| `AllowALBAccessLogDelivery` | `logdelivery.elasticloadbalancing.amazonaws.com` | **ABSENT** | **ABSENT** |

**The declaration and the live world AGREE. The PRD's text was the outlier**, which is why `TO-OP-S-17R-28`'s zero-change plan and its non-firing STOP were both correct. C-16 is corrected at v0.11/v0.12 and the remediation is ruled IN SCOPE at L4.

**SEVERITY, BOUNDED AND NOT TO BE RAISED IN THE PROOF:** both grants are `s3:PutObject` scoped to a **specific prefix**, so the exposure is foreign **WRITES** into two `waf-logs/` prefixes and **never reads**. An INTEGRITY risk on a security-evidence bucket, not a confidentiality one. **Do not write "data leak" or "exfiltration" into this proof** -- the bound is the finding's own measurement and it travels with it.

> ⛔ **WHY THE GAP SURVIVED A CAREFUL READER, and it is worth knowing before you edit:** the ALB grant's own comment argues *"THE ENABLEMENT IS THE ORACLE"* -- that `elbv2 modify-load-balancer-attributes` performs a test write and fails loudly on a wrong principal. **That is a sound defence of the PRINCIPAL being correct and it is silent on SOURCE SCOPING.** A correct answer to the neighbouring question is what made this invisible. **Do not delete that comment; extend it.**

## THE FLOOR -- ruled at L4, carried verbatim, NOT to be widened by this cut

1. **`aws:SourceAccount` on BOTH grants.** Non-negotiable, both.
2. **`aws:SourceArn` ONLY where the service supports it, MEASURED per service and NEVER ASSUMED.** ⛔ **An asserted SourceArn is exactly how C-16 reached its wrong state, and the remedy must not repeat the method that caused the defect.** For each of the two service principals, establish from AWS's own documented behaviour or from a live read whether it sends a `SourceArn` for this delivery type; **if it does not, say so and add only `SourceAccount`, and record that as a MEASURED negative rather than an omission.**
3. **DELIVERY-CONTINUITY EVIDENCE ACROSS THE CHANGE, never merely a clean plan.** Both live legs must be observed still delivering AFTER the apply, against a pre-apply denominator.

## DELIVERABLE

1. **Amend `aws_s3_bucket_policy` on `opal-data-security` in `infra/aws/terraform/opsec/`** so both statements carry the floor above. **Nothing else on that bucket changes** -- not its encryption (C-16 forbids the CMK flip and that limb is retired), not its lifecycle, not its public-access blocks, not the prefixes.
2. **PRE-APPLY DENOMINATOR, captured BEFORE the edit:** object counts and newest `LastModified` under **both** `waf-logs/cloudfront-access/` and `waf-logs/alb-opal-gateway/`. Without this the continuity criterion has nothing to compare against.
3. **A deploy-ledger entry** (`safe-apply`, never bare), opened before and closed after, with the module's UNSCOPED baseline quoted BEFORE the first edit and the rollback named -- **the rollback is the prior policy document, captured verbatim before the edit.**
4. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~S/NFRA_OPSEC202609.TO-OP-S-29.log-destination-source-conditions.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

**BROKER DRAIN IMMEDIATELY BEFORE THE APPLY.** A policy edit under live delivery has row Z-S49's exact silent-failure shape: a refused delivery presents as an EMPTY PREFIX, not an error.

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S29-AC1" cell_refs="OP-s-29"/> `S29-AC1` -- BOTH GRANTS CARRY `SourceAccount`, READ ON THE APPLIED PLANE: `get-bucket-policy` after, with both statements quoted in full, showing `aws:SourceAccount` present on each. The BEFORE state is quoted from this face (CloudFront: present; ALB: absent) as the comparison. Denominator: 2 of 2 grants.
<criterion id="S29-AC2" cell_refs="OP-s-29"/> `S29-AC2` -- THE `SourceArn` DECISION IS MEASURED PER SERVICE, NOT ASSERTED: for EACH principal, a stated finding on whether it sends a `SourceArn` for this delivery type, **with the source of that finding cited**, and the resulting condition present or deliberately absent. **A `SourceArn` added without that finding is a FAIL even if the policy applies cleanly** -- that is the exact method that produced the defect. A measured negative is a PASS.
<criterion id="S29-AC3" cell_refs="OP-s-29"/> `S29-AC3` -- BOTH LIVE LEGS STILL DELIVER AFTER THE CHANGE: for `waf-logs/cloudfront-access/` and `waf-logs/alb-opal-gateway/`, at least one object with `LastModified` **strictly AFTER the apply timestamp**, against the pre-apply counts captured in deliverable 2. **This limb does NOT get the UNCOMPUTABLE branch for the ALB leg, which was measured delivering continuously** -- a stop there is a regression this task order caused. **The CloudFront leg MAY file `UNCOMPUTABLE` with its window if that source is genuinely idle**, stated as such with the pre-apply count as evidence of its normal rate.
<criterion id="S29-AC4" cell_refs="OP-s-29"/> `S29-AC4` -- NOTHING ELSE ON THE BUCKET MOVED: the apply's changed-resource list enumerated with its count, containing ONLY `aws_s3_bucket_policy` for this bucket; the UNSCOPED re-plan 0-diff after; and a re-read confirming encryption is still `AES256` (**not** the project CMK), versioning still ON, the four public-access blocks still true, and the `waf-logs/` lifecycle unchanged. `0 to destroy` and `0 forces-replacement` bind PLAN-WIDE.
<criterion id="S29-AC5" cell_refs="OP-s-29"/> `S29-AC5` -- THE LEDGER CLOSES ON THE ARTIFACT AND PUSH STATE IS MEASURED: ledger entry CLOSED with its proof and the prior policy document named as the rollback; push state read by `ls-remote` + `is-ancestor` and stated as MEASURED.

<expected_criteria>S29-AC1, S29-AC2, S29-AC3, S29-AC4, S29-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> (v0.1.11), cell `OP-s-29` -- mirrors manifest **S28** as a SECOND ACT on the same surface; no S29 manifest row exists and none is to be minted (L4 ruling 18:5xZ: section 8's contract is one row per ENGINE and this hardening introduces none).
<owned_cells>OP-s-29</owned_cells>
Read-dependencies, NOT claimed: `OP-s-28` (COMPLETE -- its ALIGN limb is what found this), `OP-s-5` (COMPLETE -- the ALB leg it established is the one that must keep delivering).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED 21 over 5 carriers (C1 SENTINEL denominator 21 -> 5 gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0). The DEPLOY-LEDGER carrier binds: this is a ledgered apply on a bucket receiving live deliveries.
comp-iam: DECLARED-NOT-APPLICABLE -- this face edits an S3 RESOURCE policy, not an IAM identity policy, and creates no principal. comp-iam is a DESIRED-plane lens over IAM policy documents; the claim here lives on the APPLIED bucket policy and on actual delivery, which S29-AC1 and S29-AC3 read directly.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim; its `s3.tf:117-160` reading was taken at the issuer's seat at 19:0xZ and the assignee re-takes it in phase 1, STOPPING on any difference.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S29-AC1`, `S29-AC2`, `S29-AC3`, `S29-AC4`, `S29-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~S/NFRA_OPSEC202609.TO-OP-S-29.log-destination-source-conditions.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S29-AC1,S29-AC2,S29-AC3,S29-AC4,S29-AC5"` BEFORE the complete flip. **The control that must be able to FAIL is `S29-AC3`'s post-apply ALB delivery: if tightening the conditions refuses the very principal they were meant to admit, the prefix goes quiet and nothing else in this face would show it.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">Re-read the bucket policy at `s3.tf:117-160` and on the applied plane, and capture BOTH prefixes' pre-apply denominators. STOP on any difference from the table above.</phase>
  <phase id="2" when="before the apply">A broker drain, the unscoped baseline plan, the ledger opened, the prior policy document captured verbatim as the rollback.</phase>
  <phase id="3" when="after the apply">Both prefixes re-read for objects newer than the apply timestamp, then the unscoped re-plan, then the ledger closed on that evidence.</phase>
</compiler_tools_mandate>
