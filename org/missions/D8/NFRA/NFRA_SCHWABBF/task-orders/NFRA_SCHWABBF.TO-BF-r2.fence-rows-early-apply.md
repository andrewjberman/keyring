# TO NFRA_SCHWABBF.TO-BF-r2 -- apply the fence rows tonight (shared-infra, the two firm-bucket policies) and prove each principal's read, before 2026-10-21 06:00Z

<to_id>NFRA_SCHWABBF.TO-BF-r2</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.7.0_AE_CloudOps~NFRA2</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>release-fence</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-r-2` (`decompositions/NFRA_SCHWABBF_DECOMP_R6.md`) | **outcome_ref:** FWD-1, FWD-4, FWD-6 |
**GO:** written below; this order is `pending`.

---

## WORKER FACE

### GO

GO, written 2026-10-20 ~23:0xZ by `2.0.0_SA_COO~SB`: apply from `box/laptop` at commit `2258ed4f47` (it carries the three BF-h-5 rows, the Alongside row and the gateway row of `BF-h-6`; print `git rev-parse HEAD` and confirm `2258ed4f47` is an ancestor of it). DEADLINE: applied, verified and step 7 reported before 2026-10-21 06:00Z (the gateway release at 07:00Z depends on it). Lane `0.7.0_AE_CloudOps~NFRA2`. This order is NOT bound by the 12:00Z window: the CTO moved this act out of it (msg 110046).

### THE CELL

`BF-r-2`, release act(s) R3a (moved out of the window by the CTO, msg 110046) of the 0840 cutover on all three tiers (bronze, silver, state) of master `08403355` (Tax SMA 0840-3355). Andrew-direct (relayed by the CTO): one cutover, same-day rollback, no side-by-side, the old keys deleted only on his confirmation (act R7, NOT yours, never in this order). The pair that authorizes your acts: the COO half (the release plan, "COO half -- SIGNED") and the CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SCHWABBF_R5_0840_ALL_TIERS_CTO_HALF_20261020.md` @e7d8af9d1c (msg 110003, covers R0-R6 and R8). Fence rows: COO half `org/missions/D8/NFRA/NFRA_SCHWABBF/ledger/NEVER_WIDEN_BF5_STATE_FENCE_COO_HALF.md`, CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_BF5_STATE_FENCE_CTO_HALF.md` @4b0036c6cb. Read first: the release plan `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/2.0.0_SA_COO~SB/RELEASE_PLAN_R5_0840_ALL_TIERS.md` (sections 1-6), the decomposition `org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R6.md`, the CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SCHWABBF_R5_0840_ALL_TIERS_CTO_HALF_20261020.md` (its four conditions bind you), and the `/cloud-ops` skill (safe-apply, the ledger, the identity rules). The AWS CLI is `.tools/aws`.

### DO, IN ORDER

Work from a worktree of `box/laptop` at the commit the GO line names; print `git rev-parse HEAD`, `.tools/aws sts get-caller-identity`, and `date -u`.
1. OPEN A CHANGE-MANAGEMENT ENTRY first: `python .tools/deploy_ledger.py open --slug nfra-schwabbf-fence-rows-early-20261021 --title "NFRA_SCHWABBF fence rows applied ahead of the 0840 window" --author 0.7.0_AE_CloudOps~NFRA2 --window-hours 8` with one `--leg 'L1|tf-apply|shared-infra: the scoped exemption rows on the opal-data-49financial and opal-data-cottonwood bucket policies|get-bucket-policy shows the rows and the principal reads pass'`. Commit the entry and its sentinel `org/critical_paths/.open_deploys/<slug>.json` together with `safe-commit.sh`, paths-only.
2. READ the live policies BEFORE the apply (the rollback baseline): `aws s3api get-bucket-policy --bucket opal-data-49financial` and `--bucket opal-data-cottonwood`; save both JSON files to `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA2/r2/before_*.json`.
3. APPLY under `safe-apply` per `/cloud-ops`, root `infra/aws/terraform/shared-infra`, `-target` ONLY `aws_s3_bucket_policy.opal_data_49financial` and the cottonwood instance of `aws_s3_bucket_policy.lgic_firm` (read `s3-lgic-firm-buckets.tf` for its key). Print the whole plan first. EXPECTED: two in-place updates, and the policy diff adds ONLY (i) these principals' ARNs to the `ArnNotLike` lists: on 49financial `quartz-si2-spike-role`, `opal-assets-silver-schwab-role`, `gateway-schwab-catalog-read-role`; on cottonwood `opal-assets-silver-schwab-role` and `schwab-alongside-si2-box-role`; and (ii) the scoped Deny and Allow statements those five rows render. The five rows are signed: four by the pairs of this project (COO half `org/missions/D8/NFRA/NFRA_SCHWABBF/ledger/NEVER_WIDEN_BF5_STATE_FENCE_COO_HALF.md`; CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_BF5_STATE_FENCE_CTO_HALF.md` @4b0036c6cb, addendum 1 @8298aecd1f, addendum 2 @e79769e167) and the Alongside row by `2.0.0_SA_COO~SA`'s pair (CTO @a9bc898596, condition 1: it rides this apply and is never applied with a `-target` of its own row). If the diff shows ANY other principal, row or statement, or any other resource, STOP: no apply, report the plan.
4. READ the applied policies again (`after_*.json`) and print the statements of the five rows.
5. PROVE EACH PRINCIPAL (CTO: a live check from each). `date -u` before each.
   a. `gateway-schwab-catalog-read-role` (site Z's R3c gate): `aws sts assume-role --role-arn arn:aws:iam::313476888478:role/gateway-schwab-catalog-read-role --role-session-name nfra-schwabbf-fence-check` (never print the credentials; export them only into the child commands). If the trust policy admits you, with those credentials run (i) `aws s3api get-object --bucket opal-data-49financial --key schwab/49financial/state/complete/date=2026-10-20/08403355.complete.json /dev/null` and (ii) `aws s3api list-objects-v2 --bucket opal-data-49financial --prefix schwab/49financial/state/complete/ --max-keys 5`. PASS = (i) NoSuchKey (or the object, if one exists) and (ii) an empty listing or keys, and NEITHER says AccessDenied. Print both outputs verbatim. Negative control, same credentials: `get-object` of `schwab/49financial/state/pulls/date=2026-10-20/08403355.x` must say AccessDenied (the row reads the `complete` prefix only). If the assume-role is refused, say so and mark this principal NOT LIVE-TESTABLE: use `aws iam simulate-principal-policy --policy-source-arn <the role arn> --action-names s3:GetObject s3:ListBucket --resource-arns <the key arn and the bucket arn> --resource-policy file://after_49f.json` and mark it SIMULATED; site Z's gate needs a LIVE read, so report this at once.
   b. `quartz-si2-spike-role` (the box) and `opal-assets-silver-schwab-role` (the converter) and `schwab-alongside-si2-box-role` are service roles you cannot assume from here: read the applied statements (step 4) and, for the box role, `simulate-principal-policy` with `--resource-policy` for `s3:PutObject` on `arn:aws:s3:::opal-data-49financial/schwab/49financial/state/pulls/date=2026-10-20/08403355.x` (expect allowed) and on `.../state/complete/date=2026-10-20/08403355.x` (expect NOT allowed: the row allows the pulls and daily_pull tables only). For the converter, the bucket side is proven by the policy read ONLY: its identity-side explicit Deny (the shared fan-in fence, row NFRA_SCHWABBF-S4) is lifted later by `BF-r-3`; a simulation now would show that Deny and is not evidence about the fence rows. Say so.
6. CLOSE leg L1 (`deploy_ledger.py close-leg ... --proof <the proof file>`) and then the entry (`deploy_ledger.py close`). Save everything under `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA2/r2/`, commit paths-only.
7. THE MOMENT step 5a passes (or is found NOT LIVE-TESTABLE), message `2.0.0_SA_COO~SB` with the verbatim outputs; do not wait for the rest of the report.
ROLLBACK: re-apply the previous commit's shared-infra Terraform with the same `-target` set (the rows leave the policies), or restore the `before_*.json` policy with `put-bucket-policy` if `safe-apply` is unavailable; report before rolling back.

### ACCEPTANCE (read by the issuer from your committed files)

<criterion id="BF6-r2-AC1" cell_refs="BF-r-2"><invocation>python .tools/proof-of-spec-check.py org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA2/NFRA_SCHWABBF.TO-BF-r2.fence-rows-early-apply.proof_of_spec.json BF6-r2-AC1</invocation><expect>VALID</expect></criterion>
`BF6-r2-AC1` -- the five fence rows are applied to the two firm-bucket policies exactly as planned; the gateway role reads the 49financial complete prefix without AccessDenied (live or marked not testable), the negative control is denied, the other principals are proven by policy read and simulation as stated; the entry is closed.

<expected_criteria>BF6-r2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus this order's file.
- **Never:** `terraform apply` outside `safe-apply`; any apply, copy or write outside the legs this order names; deleting an S3 object or version; touching `08242234`, `08335338` or any other master's keys or grants; reading or printing a Schwab token or any secret value; a second concurrent Schwab session; enabling or editing an EventBridge rule; stopping an instance.
- **Window.** The CTO's window is 2026-10-21 12:00-20:00Z. Outside it you do nothing in this order except what its GO line allows. Any failure rolls back that order's legs in the same window (rollback per step below) and is reported at once.
- **Refusal clause.** If a step cannot be met as written, stop, write the reason and the output in your report and a surprise row (id `NFRA_SCHWABBF-R3-S<k>`; read the investigation file for the highest `R3-S<k>` and use the next; the gate may renumber it), commit the row AT ONCE with `safe-commit.sh` paths-only and tell the issuer its hash, and do not improvise. Append the row at the BYTE level (the file mixes CRLF and LF: do not use an editor that rewrites line endings).

<paths>
org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA2/
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R6.md</decomp_doc> (round 6), cell `BF-r-2`.
<owned_cells>BF-r-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: BF6-r2-AC1. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA2/NFRA_SCHWABBF.TO-BF-r2.fence-rows-early-apply.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF6-r2-AC1` BEFORE the flip. The instance records, as artifact rows, every printed output the steps ask for.
</proof_of_spec>

**REPORT (your final message and a message to `2.0.0_SA_COO~SB`):** the commit applied from, the before and after policy statements of the five rows, the plan summary, the step 5 outputs verbatim per principal with LIVE or SIMULATED marked, the closed entry, any stop, any row id.

---

## RECORD FACE

<preflight>
comp-schedule: RUN by reading -- the pull fires are 09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z; the window 12:00-20:00Z sits between the 10:45 and 21:45 fires; CTO condition: no pull fire between R4c and R5; BLIND: the live EventBridge rules (read at step 1 of `BF-r-1`).
comp-iam: RUN -- the apply adds five scoped exemption rows to two bucket policies (box PutObject on two tables, converter Get/Put/List on three, gateway Get/List on one, Alongside box PutObject on two); nothing is written into the prefixes (still empty); no delete; BLIND beforehand: the live bucket policies (read at step 2) and the live IAM plane.
comp-adversary: DECLARED-NOT-APPLICABLE as a lens run; findings inlined in the steps -- (1) the shared-infra root may carry other seats' pending changes, so the apply is `-target`ed and stops on anything unlisted; (2) the converter's identity-side Deny is a separate known blocker (row S4, BF-r-3), so its read is not simulated here; (3) the gateway's dual read treats AccessDenied as a hard error, so step 5a is the gate for site Z's 07:00Z release.
lane: the <paths> block IS the grant; CloudOps seats act on infrastructure under a task order (rule 34).
</preflight>

Source: PRD v1.0 C-TIERS, C-MOVE, C-DAILY; the release plan; the CTO half @e7d8af9d1c; decomposition round 6 cell BF-r-2.
