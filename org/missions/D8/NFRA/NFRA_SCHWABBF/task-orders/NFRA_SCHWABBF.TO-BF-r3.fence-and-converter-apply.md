# TO NFRA_SCHWABBF.TO-BF-r3 -- apply the three fence rows, then the converter fence variant, grants, event rules and package, then the box state statement, under safe-apply

<to_id>NFRA_SCHWABBF.TO-BF-r3</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>release-0840</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-r-3` (`decompositions/NFRA_SCHWABBF_DECOMP_R6.md`) | **outcome_ref:** FWD-1, FWD-4, FWD-6 |
**GO:** this order is `staged`. The issuer writes the GO line below and flips it to `pending`; do not act before that flip.

---

## WORKER FACE

### GO

(not yet written. It will read: inside 2026-10-21 12:00-20:00Z; `TO-BF-r1` complete; the gateway pair signed and ready (R3c); the CTO's addendum on the fence variant (row `NFRA_SCHWABBF-S4`) signed; the exact commit to apply from.)

### THE CELL

`BF-r-3`, release act(s) R3a and R3b of the 0840 cutover on all three tiers (bronze, silver, state) of master `08403355` (Tax SMA 0840-3355). Andrew-direct (relayed by the CTO): one cutover, same-day rollback, no side-by-side, the old keys deleted only on his confirmation (act R7, NOT yours, never in this order). The pair that authorizes your acts: the COO half (the release plan, "COO half -- SIGNED") and the CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SCHWABBF_R5_0840_ALL_TIERS_CTO_HALF_20261020.md` @e7d8af9d1c (msg 110003, covers R0-R6 and R8). Fence rows: COO half `org/missions/D8/NFRA/NFRA_SCHWABBF/ledger/NEVER_WIDEN_BF5_STATE_FENCE_COO_HALF.md`, CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_BF5_STATE_FENCE_CTO_HALF.md` @4b0036c6cb. Read first: the release plan `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/2.0.0_SA_COO~SB/RELEASE_PLAN_R5_0840_ALL_TIERS.md` (sections 1-6), the decomposition `org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R6.md`, the CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SCHWABBF_R5_0840_ALL_TIERS_CTO_HALF_20261020.md` (its four conditions bind you), and the `/cloud-ops` skill (safe-apply, the ledger, the identity rules). The AWS CLI is `.tools/aws`.

### DO, IN ORDER

Order is fixed by the CTO: the fence apply first (A), then the converter (B), then the box (C). Work from a worktree at the commit the GO line names; print `git rev-parse HEAD`. For each apply use `safe-apply` per `/cloud-ops`, print the whole plan, compare it with the EXPECTED list below, and STOP (no apply, report the plan) if the plan holds anything not on the list: the roots hold other seats' pending changes, so every apply is `-target`ed to the addresses named.
A. `infra/aws/terraform/shared-infra` (leg L1). EXPECTED: in-place update of `aws_s3_bucket_policy.opal_data_49financial` and of the cottonwood instance of `aws_s3_bucket_policy.lgic_firm`, each adding ONLY (i) the ARNs of the rows `quartz-si2-spike-role` (49financial only) and `opal-assets-silver-schwab-role` (both buckets) to the `DenyForeignFirmPrincipals` ArnNotLike list and (ii) the scoped Deny and Allow statements those rows render. ONE further row is expected and signed: `schwab-alongside-si2-box-role` on `opal-data-cottonwood` (PutObject on `state/pulls` and `state/daily_pull`; `2.0.0_SA_COO~SA`'s cell AL-i-2, CTO signed @a9bc898596, condition 1: it rides this apply and is never applied with `-target` of its own). If the diff shows any OTHER principal, row or statement (another seat's unapplied exemption row), STOP and report: the pairs cover four rows only. After the apply: `aws s3api get-bucket-policy` for both buckets; print the statements of the three rows (leg L1 proof).
B. `infra/aws/terraform/opal-assets` (leg L2), in this sequence, each a `-target` apply with its plan printed first:
   B1. `aws_iam_policy.one_way_fan_in_fence_schwab` and `aws_iam_role_policy_attachment.silver_fence_schwab` (creates only). EXPECTED: 2 to add.
   B2. `aws_iam_role_policy.silver_read_schwab_firm_prefix`, `aws_iam_role_policy.silver_write_schwab_firm_silver`, `aws_iam_role_policy.silver_state_write_schwab_firm`. EXPECTED: 3 to add.
   B3. the schwab converter Lambda (read `silver.tf` about lines 770-900 for the module or resource address of the `schwab` instance) with its package and its `OPAL_BUILD_COMMIT` row. EXPECTED: in-place update of that one function: code hash and the `OPAL_BUILD_COMMIT` environment value (the new pin, from `TO-BF-k6`) only. Also `aws_lambda_permission.silver_s3_invoke["schwab"]` if the plan lists it.
   B4. `aws_s3_bucket_notification.monolith_bronze`. EXPECTED: in-place update adding exactly two Lambda rules, `schwab-49financial` (prefix `schwab/49financial/bronze/`, suffix `.zip`) and `schwab-cottonwood` (prefix `schwab/cottonwood/bronze/`, suffix `.zip`); every other rule unchanged. Do this step LAST so no copy event fires before the new code runs.
   B5. `aws_iam_role_policy_attachment.silver_fence["schwab"]`, a DESTROY of the shared-fence attachment of the schwab role ONLY (the for_each now excludes it). EXPECTED: 1 to destroy; the five other families keep it.
   Verify (leg L2 proof): `get-function-configuration` (OPAL_BUILD_COMMIT equals the pin; print CodeSha256); `list-attached-role-policies` for `opal-assets-silver-schwab-role` (variant attached, shared one not) and for `opal-assets-silver-etf-role` (shared still attached); `get-bucket-notification-configuration` (the 2 new rules plus the previous rules intact, count before and after); `get-role-policy` for the three new inline policies.
C. `infra/aws/terraform/canonical-schwab-ec2` (leg L3): `-target=aws_iam_role_policy.schwab_si2_monolith_write`. EXPECTED: in-place update adding statements for the firm-form masters and `MonolithSchwabStateWrite`; nothing removed (the old `_ops` and `meta/pulls` grants stay until R7). Verify with `get-role-policy` (role `quartz-si2-spike-role`, policy `quartz-si2-monolith-write`).
D. Close legs L1, L2, L3 with `deploy_ledger.py close-leg --slug nfra-schwabbf-0840-all-tiers-cutover-20261021 --leg-id <Lk> --proof "<the output file path>"`. Do NOT close the entry. Save outputs under `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/r3/`, commit paths-only, report.
ROLLBACK (same window): revert nothing by hand; re-apply the previous commit's Terraform text for the touched root with the same `-target` set (old rules, old grants and the shared-fence attachment are restored); for B5 the rollback is re-creating `silver_fence["schwab"]` by reverting the `for_each` change. Report before rolling back.

### ACCEPTANCE (read by the issuer from your committed files)

<criterion id="BF6-r3-AC1" cell_refs="BF-r-3"><invocation>python .tools/proof-of-spec-check.py org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-BF-r3.fence-and-converter-apply.proof_of_spec.json BF6-r3-AC1</invocation><expect>VALID</expect></criterion>
`BF6-r3-AC1` -- the three fence rows, the schwab converter's variant fence, firm grants, two firm event rules and the new package, and the box's state statement are applied exactly as planned; legs L1-L3 closed with proof; nothing copied.

<expected_criteria>BF6-r3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus this order's file.
- **Never:** `terraform apply` outside `safe-apply`; any apply, copy or write outside the legs this order names; deleting an S3 object or version; touching `08242234`, `08335338` or any other master's keys or grants; reading or printing a Schwab token or any secret value; a second concurrent Schwab session; enabling or editing an EventBridge rule; stopping an instance.
- **Window.** The CTO's window is 2026-10-21 12:00-20:00Z. Outside it you do nothing in this order except what its GO line allows. Any failure rolls back that order's legs in the same window (rollback per step below) and is reported at once.
- **Refusal clause.** If a step cannot be met as written, stop, write the reason and the output in your report and a surprise row (id `NFRA_SCHWABBF-R3-S<k>`; read the investigation file for the highest `R3-S<k>` and use the next; the gate may renumber it), commit the row AT ONCE with `safe-commit.sh` paths-only and tell the issuer its hash, and do not improvise. Append the row at the BYTE level (the file mixes CRLF and LF: do not use an editor that rewrites line endings).

<paths>
org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R6.md</decomp_doc> (round 6), cell `BF-r-3`.
<owned_cells>BF-r-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: BF6-r3-AC1. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-BF-r3.fence-and-converter-apply.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF6-r3-AC1` BEFORE the flip. The instance records, as artifact rows, every printed output the steps ask for.
</proof_of_spec>

**REPORT (your final message and a message to `2.0.0_SA_COO~SB`):** per root: the plan summary, the apply result, the verification outputs, the closed legs, any stop and its plan, any row id.

---

## RECORD FACE

<preflight>
comp-schedule: RUN by reading -- the pull fires are 09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z; the window 12:00-20:00Z sits between the 10:45 and 21:45 fires; CTO condition: no pull fire between R4c and R5; BLIND: the live EventBridge rules (read at step 1 of `BF-r-1`).
comp-iam: RUN -- the apply adds the box role's PutObject on two state tables and the converter role's Get/Put/List on three tables per master in the firm buckets, the three bucket-side rows, and the variant fence leaving the 15 enumerated resources outside the Deny; no delete, no folder wildcard; plan of each root printed; BLIND beforehand: the live IAM plane.
comp-adversary: DECLARED-NOT-APPLICABLE as a lens run; findings inlined in the steps -- (1) other seats' pending changes in `opal-assets` and `shared-infra` (every apply is `-target`ed and stops on anything unlisted); (2) the notification resource is the whole bucket's config, so B4 comes last and its plan must show only the two added rules; (3) detaching the shared fence last (B5) leaves no unfenced gap.
lane: the <paths> block IS the grant; CloudOps seats act on infrastructure under a task order (rule 34).
</preflight>

Source: PRD v1.0 C-TIERS, C-MOVE, C-DAILY; the release plan; the CTO half @e7d8af9d1c; decomposition round 6 cell BF-r-3.
