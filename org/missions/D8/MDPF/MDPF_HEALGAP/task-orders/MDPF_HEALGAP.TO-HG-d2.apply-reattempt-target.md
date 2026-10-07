# TO MDPF_HEALGAP.TO-HG-d2 -- round 1 apply of HG-t-2: the Rebalancer runner re-runs after the Cottonwood login chain succeeds (laptop)

<to_id>MDPF_HEALGAP.TO-HG-d2</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.7.0_AE_CloudOps~F</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>seat</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>DEPLOY-T2</workstream>

**Directive:** D8 | **Fabric:** laptop (project placement dell1; THIS act on the laptop) | **Decomp cell:** `HG-t-2`
(`decompositions/MDPF_HEALGAP_DECOMP.md`, the issuer's drain act 3) | **outcome_ref:** FWD-1 | **depends_on:**
`MDPF_HEALGAP.TO-HG-t2` (drained to CLOUD), `MDPF_HEALGAP.TO-HG-d1` (complete)

**GO condition (all three, read on the trunk):** (1) `cot_rebalancer_reattempt.tf` and `MDPF_HEALGAP.TO-HG-t2` reading `complete`
are on CLOUD; (2) the R20 entry for `cot-bronze-complete` is on CLOUD (`org/standards/NAMING_LEGACY_READS.json`, kind
`r20_exception`, landed by `1.0.0_SA_CTO~DELL1`); (3) both never-widen halves SIGNED in
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/NEVER_WIDEN_HALF_REQUEST_HEALGAP_HG_T2_REATTEMPT_APPLY_20261007.md`.
The issuer flips this order's `<status>` to `pending` when all three hold; until then it is `staged`.

---

## WORKER FACE

### THE CELL

`HG-t-2`'s apply. FWD-1: on a day the 06:00Z Cottonwood Rebalancer pull fails because the vendor login lapsed, a reader sees that
day's figures by the end of the same day with nobody acting. The runner's guard is live (your HG-d1); this order wires the second
attempt: a target on the EXISTING rule `cot-bronze-complete` invoking `cot-rebalancer-runner` with `{"mode":"pull"}`, and the invoke
permission for that rule. Andrew gave the standing vendor word for this re-run and the R20 naming exception for its rule-name literal
(`ANDREW_DIRECT_20261007_135xZ_HEALGAP_ACT1_YES_R20_YES_ACT2_NO_WORKTREE_DELETE_YES.md` @e5fb41862f).

**Preconditions (each a refusal if absent):**
1. The GO condition above reads true on your trunk.
2. `infra/aws/terraform/opal-assets/cot_rebalancer_reattempt.tf` declares exactly one `aws_cloudwatch_event_target` and one
   `aws_lambda_permission` (read the file; their resource addresses are the `-target`s below).
3. Live `cot-rebalancer-runner` CodeSha256 is `QxLvPLTMO5YSkS+vaRXEkhaA78ZAr1arTyS0ADOOMvk=` (the guard is live first, C-IDEMPOTENT).

**Act:**
0. **The SKIP probe, before anything else (CTO half condition 1, @a79f7ea1b7).** With today's UTC stamp
   `blackdiamond/cottonwood/meta/<today>-complete.json` listed in `opal-data-assets`, invoke `cot-rebalancer-runner` once with
   `{"mode":"pull"}` (RequestResponse). It must return `{"verdict": "SKIP-IDEMPOTENT", ...}` and no new key may appear under
   `blackdiamond/cottonwood/bronze/rebalancer_*/<today>/` (list before and after; print both counts). If it pulls instead, stop:
   there is no apply. Record the response and both counts in the ledger entry. (This is the guard's first live run; any vendor
   call it made would fall under Andrew's ACT 1 word, @e5fb41862f.)
1. Open a change-management ledger entry (`.tools/deploy_ledger.py`) naming this order, the laptop as the box, and the two resources.
2. With `CHECKPOINT_DISABLE=1` and WITHOUT `MSYS_NO_PATHCONV`: `terraform plan -target=<event_target address> -target=<permission
   address>` in `infra/aws/terraform/opal-assets`. The plan must read 2 to add, 0 to change, 0 to destroy, both on those two
   addresses. Any other line: stop and refuse. Print the plan's change lines in the ledger entry.
3. `.tools/safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply` with the same two `-target`s.
4. Close the ledger entry and commit it BEFORE the reads below (commit with an exact pathspec: the close also rewrites other seats'
   sentinels, row MDPF_HEALGAP-S6, which you never commit); then `record-terraform-deploy.sh` as for HG-d1.

### ACCEPTANCE

<criterion id="HG1-d2-AC1" cell_refs="HG-t-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R1_CHECKS/hg_d2_applied.py --wired</invocation><expect>WIRED-OK</expect></criterion>
`HG1-d2-AC1` -- `cot-bronze-complete` carries one runner target with `{"mode":"pull"}` beside its unchanged silver target, and the runner's policy admits that rule.

<criterion id="HG1-d2-AC2" cell_refs="HG-t-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R1_CHECKS/hg_d2_applied.py --unchanged</invocation><expect>UNCHANGED-OK</expect></criterion>
`HG1-d2-AC2` -- nothing else moved: runner code, retry/age/on_success, the 06:00Z rule and its input.

<expected_criteria>HG1-d2-AC1 HG1-d2-AC2</expected_criteria>

At the base (2026-10-07 ~14:1xZ, dell1): AC1 FAILS (`WIRED-BAD runner targets on cot-bronze-complete=0`), AC2 PASSES (a control).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- No change to the runner's code, IAM role, invoke-config, any schedule or rule definition, or any other function. One Lambda invoke
  only (the act 0 probe); no S3 data write. Every terraform call with `CHECKPOINT_DISABLE=1`.
- **Rollback** (if AC1 or AC2 fails after the apply): the half file's Rollback section.
- **Refusal clause.** If a precondition or criterion cannot be met as written, stop, write the reason and the row's `spec_asserts` /
  `world_is` in your report, and do not widen the act. Row ids for this project are minted on dell1; `0.0.0_AB_MSTR` carries
  the row and the issuer files it.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/terraform/opal-assets/CHANGELOG.json
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D8/MDPF/MDPF_HEALGAP/ledger/
</paths>

The block is your WRITE grant (it enumerates what `deploy_ledger.py` and `record-terraform-deploy.sh` write; row MDPF_HEALGAP-S5).
Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 1, the thread), cell `HG-t-2`
(the issuer's drain act 3: "Apply HG-t-2 (WORLD), held on ACT 1").
<owned_cells>HG-t-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG1-d2-AC1, HG1-d2-AC2. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.7.0_AE_CloudOps~F/MDPF_HEALGAP.TO-HG-d2.apply-reattempt-target.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG1-d2-AC1,HG1-d2-AC2 --governing-order <this file>` BEFORE the flip.
</proof_of_spec>

**REPORT:** the ledger entry path, the plan's change lines, the apply output tail, both checks' output, commits, push state.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule moves; an event target on an existing rule; AC2 reads the daily rule after the apply.
comp-iam: RUN at L5 (comp-iam service cot-rebalancer-runner, 2026-10-07); the new aws_lambda_permission is a resource policy on the runner, not a role grant; no role changes.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
risk: WORLD -- an apply that adds a recurring vendor-call path (Andrew's ACT 1 word @e5fb41862f). Never-widen halves CTO + COO (dell1) before the GO; change-management entry by the deploying seat; the CTO's exercised read after.
direct_act: false -- WORLD.
</preflight>

Workstream DEPLOY-T2: round 1's drain act 3, ordered to the laptop seat that deployed HG-d1 (laptop CTO rulings @31e91d2d1e s.2); its write
surface (ledger, sentinel, CHANGELOG, source map) is disjoint from the THREAD cells and from HG-d1, which is complete.

Source: PRD v0.1 @78db344481 section 2 hop 3, C-ONE-PIPELINE, C-VENDOR; decomposition round 1, drain act 3; Andrew-direct @e5fb41862f.
