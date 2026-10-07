# TO MDPF_HEALGAP.TO-HG-d1 -- round 1 deploy of HG-t-1: the Rebalancer runner's guard-by-listing reaches the live Lambda (laptop)

<to_id>MDPF_HEALGAP.TO-HG-d1</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.7.0_AE_CloudOps~F</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>seat</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>DEPLOY</workstream>

**Directive:** D8 | **Fabric:** laptop (project placement dell1; THIS act on the laptop) | **Decomp cell:** `HG-t-1`
(`decompositions/MDPF_HEALGAP_DECOMP.md`, the issuer's drain act 1) | **outcome_ref:** FWD-1 | **depends_on:** `MDPF_HEALGAP.TO-HG-t1`
(complete, drained @ca914096d7)

**GO condition:** both never-widen halves SIGNED in
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/NEVER_WIDEN_HALF_REQUEST_HEALGAP_HG_T1_RUNNER_DEPLOY_20261007.md`
(COO half signed; CTO half `1.0.0_SA_CTO~DELL1`). Until then this order is `staged`; flip it to `pending` when you start.

---

## WORKER FACE

### THE CELL

`HG-t-1`'s deploy. FWD-1: on a day the 06:00Z Cottonwood Rebalancer pull fails because the vendor login lapsed, the day's three bronze
feeds land the same day with nobody acting. The runner code that makes a second same-day invocation safe is merged; this order puts it
on the live Lambda `cot-rebalancer-runner`. Nothing else moves.

**Ruling:** laptop `1.0.0_SA_CTO` `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_FOR_THE_DELLS_20261007_0930Z.md` @31e91d2d1e
section 2: the laptop deploys it through you; read its three refusal conditions before you build.

**Preconditions (each a refusal if absent):**
1. `python .tools/prd-signoff.py status MDPF_HEALGAP` reads `ADMITTED`; the brief
   `docs/briefs/mdpf-healgap-midstream-brief-20261007.md`, the PRD `org/missions/D8/MDPF/MDPF_HEALGAP/prd/MDPF_HEALGAP_PRD.md` and the
   decomposition `org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md` are on your trunk.
2. Your trunk carries `ca914096d7` (`git merge-base --is-ancestor ca914096d7 HEAD`).
3. `infra/aws/terraform/opal-assets/cot_rebalancer_reattempt.tf` does NOT exist on your trunk. If it does, refuse: it is held.

**Act (the sequence in `infra/aws/lambda/ci/build-and-upload.sh`'s header):**
1. Open a change-management ledger entry under `org/critical_paths/change_management/` naming this order, the laptop as the box, the
   function and the expected sha.
2. `bash infra/aws/lambda/ci/build-and-upload.sh opal-assets cot-rebalancer-runner`. The printed sha must be
   `QxLvPLTMO5YSkS+vaRXEkhaA78ZAr1arTyS0ADOOMvk=`; if not, stop and refuse (do not apply).
3. `terraform plan -target=module.cot_rebalancer_runner` in `infra/aws/terraform/opal-assets`: the only change is the function's code
   (source hash / S3 object version). Any other change: stop and refuse.
4. `.tools/safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply -target=module.cot_rebalancer_runner`.
5. Close the ledger entry and commit it BEFORE the reads below; then `record-terraform-deploy.sh` as the script header says.

### ACCEPTANCE

<criterion id="HG1-d1-AC1" cell_refs="HG-t-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R1_CHECKS/hg_d1_deployed.py --code</invocation><expect>DEPLOYED-OK</expect></criterion>
`HG1-d1-AC1` -- the live function's CodeSha256 is the HG-t-1 build.

<criterion id="HG1-d1-AC2" cell_refs="HG-t-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R1_CHECKS/hg_d1_deployed.py --unchanged</invocation><expect>UNCHANGED-OK</expect></criterion>
`HG1-d1-AC2` -- the deploy moved code only: retry 2, age 21600, on_success to the silver converter, the 06:00Z rule and its `{"mode":"pull"}` input, and one target on `cot-bronze-complete`.

<expected_criteria>HG1-d1-AC1 HG1-d1-AC2</expected_criteria>

At the base (2026-10-07, dell1): AC1 FAILS (`DEPLOYED-BAD CodeSha256=b1m7jUh6...Fw=`), AC2 PASSES (a control).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- No change to IAM, the invoke-config, any schedule or rule, any other function, or any S3 data key. No Lambda invoke, no Black Diamond
  call. No `apply` without `-target=module.cot_rebalancer_runner`.
- **Rollback** (if AC1 or AC2 fails after the apply): the half file's Rollback section, prior artifact version
  `XeSy4IKGvKXGsEwBQRpeXUekk5qb.TYp`; read back CodeSha256 `b1m7jUh6jC55tBfoUX20xRmmKAjB4P1Wvxnwvn2N/Fw=`.
- **Refusal clause.** If a precondition or criterion cannot be met as written, stop, write the reason and the row's `spec_asserts` /
  `world_is` in your report, and do not widen the act. Row ids for this project are minted on dell1 (interim rule,
  `0.0.0_AB_MSTR~DELL1` msg 89), so `0.0.0_AB_MSTR` carries the row to dell1 and the issuer files it.

<paths>
org/critical_paths/change_management/
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D8/MDPF/MDPF_HEALGAP/ledger/
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 1, the thread), cell `HG-t-1`
(the issuer's drain act 1: "Deploy HG-t-1 (WORLD)").
<owned_cells>HG-t-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG1-d1-AC1, HG1-d1-AC2. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.7.0_AE_CloudOps~F/MDPF_HEALGAP.TO-HG-d1.deploy-runner-guard.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG1-d1-AC1,HG1-d1-AC2 --governing-order <this file>` BEFORE the flip.
</proof_of_spec>

**REPORT:** the ledger entry path, the build sha, the plan's change list, the apply output tail, both checks' output, commits, push state.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule moves; AC2 reads the daily rule after the apply.
comp-iam: RUN at L5 (comp-iam service cot-rebalancer-runner, 2026-10-07); the new code uses s3:ListBucket (GRANTED) and drops the s3:GetObject call (UNGRANTED); no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
risk: WORLD -- a deploy. Never-widen halves CTO + COO (dell1) before the GO; change-management entry by the deploying seat; the CTO's exercised read after.
direct_act: false -- WORLD.
</preflight>

Workstream DEPLOY: round 1's drain act 1, ordered to a laptop seat by the laptop CTO; its write surface (ledger, source map) is disjoint from the THREAD workstream's cells.

Source: laptop 1.0.0_SA_CTO rulings @31e91d2d1e section 2; PRD v0.1 @78db344481 C-IDEMPOTENT; decomposition round 1, drain act 1.
