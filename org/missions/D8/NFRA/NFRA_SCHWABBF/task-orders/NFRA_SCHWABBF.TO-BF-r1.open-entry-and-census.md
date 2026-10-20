# TO NFRA_SCHWABBF.TO-BF-r1 -- open the change entry for the 0840 cutover, take the live census, and confirm the copy identity before the window

<to_id>NFRA_SCHWABBF.TO-BF-r1</to_id>
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

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-r-1` (`decompositions/NFRA_SCHWABBF_DECOMP_R6.md`) | **outcome_ref:** FWD-1, FWD-4, FWD-6 |
**GO:** this order is `staged`. The issuer writes the GO line below and flips it to `pending`; do not act before that flip.

---

## WORKER FACE

### GO

(not yet written. It will read: on or after 2026-10-21 11:00Z; the gateway pair of `2.0.0_SA_COO~O` signed; cells `BF-k-6` and `BF-j-6` merged. The issuer writes the commit hash you work from.)

### THE CELL

`BF-r-1`, release act(s) R1 of the 0840 cutover on all three tiers (bronze, silver, state) of master `08403355` (Tax SMA 0840-3355). Andrew-direct (relayed by the CTO): one cutover, same-day rollback, no side-by-side, the old keys deleted only on his confirmation (act R7, NOT yours, never in this order). The pair that authorizes your acts: the COO half (the release plan, "COO half -- SIGNED") and the CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SCHWABBF_R5_0840_ALL_TIERS_CTO_HALF_20261020.md` @e7d8af9d1c (msg 110003, covers R0-R6 and R8). Fence rows: COO half `org/missions/D8/NFRA/NFRA_SCHWABBF/ledger/NEVER_WIDEN_BF5_STATE_FENCE_COO_HALF.md`, CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_BF5_STATE_FENCE_CTO_HALF.md` @4b0036c6cb. Read first: the release plan `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/2.0.0_SA_COO~SB/RELEASE_PLAN_R5_0840_ALL_TIERS.md` (sections 1-6), the decomposition `org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R6.md`, the CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SCHWABBF_R5_0840_ALL_TIERS_CTO_HALF_20261020.md` (its four conditions bind you), and the `/cloud-ops` skill (safe-apply, the ledger, the identity rules). The AWS CLI is `.tools/aws`.

### DO, IN ORDER

1. Work from a worktree of `box/laptop` at the commit the GO line names. Print `git rev-parse HEAD` of it and `.tools/aws sts get-caller-identity` (the identity that will run every copy and apply; never the box role).
2. LIVE CENSUS, read only, every output printed with its denominator:
   a. `aws iam list-entities-for-policy --policy-arn <arn of opal-assets-one-way-fan-in-fence> --query 'PolicyRoles[].RoleName'` (paginated: count client-side). Row `NFRA_SCHWABBF-S4` claims `opal-assets-silver-schwab-role` is attached (expect about 12 roles). Print the list and whether schwab is in it.
   b. `aws s3api get-bucket-notification-configuration --bucket opal-data-assets`: print the count of Lambda rules and each rule's id, prefix and suffix. Expect the three `schwab-<master>` rules among the others and NO `schwab-49financial` or `schwab-cottonwood` rule yet.
   c. `aws s3api get-bucket-versioning` for `opal-data-assets`, `opal-data-49financial`, `opal-data-cottonwood`: print Status (the rollback of the copies and of R7 depends on it).
   d. FENCE READ-ADMISSION of the copy identity: `aws s3api list-objects-v2 --bucket opal-data-49financial --prefix schwab/49financial/state/ --max-keys 5` and the same on `opal-data-cottonwood --prefix schwab/cottonwood/state/`: print key counts. An AccessDenied here STOPS the cutover (the fence does not admit the copy identity): report and file a row.
   e. The consumers of Schwab bronze: ONE sweep naming every Lambda function, ECS task definition and scheduled job whose environment, code or IAM read grant names the monolith Schwab bronze (`schwab/<master>/bronze` or `schwab/*/bronze`); use `comp-find --corpus aws` and `comp-iam` and one `aws lambda list-functions` plus `get-function-configuration` sweep; print the node denominator and the vintage. Name each family that READS bronze keys by master or by prefix (the Black Diamond converters read `_monolith_bronze.py`).
3. OPEN THE LEDGER ENTRY: `python .tools/deploy_ledger.py open --slug nfra-schwabbf-0840-all-tiers-cutover-20261021 --title "NFRA_SCHWABBF 0840 cutover on bronze, silver and state" --author 0.7.0_AE_CloudOps~NFRA1 --window-hours 12` with six `--leg` arguments `id|kind|target|proof_required`: `L1|tf-apply|shared-infra: the 3 fence rows on the opal-data-49financial and opal-data-cottonwood bucket policies|get-bucket-policy shows the rows` ; `L2|tf-apply|opal-assets: schwab fence variant, firm read/write/state grants, firm event rules, converter package|policy reads, notification config, function config` ; `L3|tf-apply|canonical-schwab-ec2: box MonolithSchwabStateWrite|get-role-policy` ; `L4|s3-copy|state tier 6930 keys to opal-data-49financial|move tool verify rc 0` ; `L5|s3-copy|silver tier 7581 keys|move tool verify rc 0` ; `L6|s3-copy|bronze tier 6074 keys, converter events drained|move tool verify rc 0, DLQ 0`. The entry names EVERY family from step 2e in its body. DO NOT name `data/black_diamond/scripts/bronze/_monolith_bronze.py` or the puller here (the deploy gate deploys a named file at the next push; that leg is the second entry of `BF-r-5`, opened only after the copies verify). Commit the entry and its sentinel `org/critical_paths/.open_deploys/<slug>.json` TOGETHER with `safe-commit.sh` paths-only (a staged sentinel does not survive a forced worktree removal).
4. Save every output under `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/r1/`, commit, and report.

### ACCEPTANCE (read by the issuer from your committed files)

<criterion id="BF6-r1-AC1" cell_refs="BF-r-1"><invocation>python .tools/proof-of-spec-check.py org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-BF-r1.open-entry-and-census.proof_of_spec.json BF6-r1-AC1</invocation><expect>VALID</expect></criterion>
`BF6-r1-AC1` -- the entry is open and committed with its sentinel; the census (fence attachment, notification rules, versioning, copy-identity read admission, the Schwab-bronze consumer families with the denominator) is recorded; nothing was applied, copied or pushed.

<expected_criteria>BF6-r1-AC1</expected_criteria>

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
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R6.md</decomp_doc> (round 6), cell `BF-r-1`.
<owned_cells>BF-r-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: BF6-r1-AC1. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-BF-r1.open-entry-and-census.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF6-r1-AC1` BEFORE the flip. The instance records, as artifact rows, every printed output the steps ask for.
</proof_of_spec>

**REPORT (your final message and a message to `2.0.0_SA_COO~SB`):** the caller identity, the HEAD commit, the six census outputs with denominators, the families named, the entry path and slug, any row id.

---

## RECORD FACE

<preflight>
comp-schedule: RUN by reading -- the pull fires are 09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z; the window 12:00-20:00Z sits between the 10:45 and 21:45 fires; CTO condition: no pull fire between R4c and R5; BLIND: the live EventBridge rules (read at step 1 of `BF-r-1`).
comp-iam: RUN -- the copy identity is CloudOps's own; the live attachment census in step 2a is the check of row NFRA_SCHWABBF-S4; BLIND beforehand: the live IAM plane (0 roles read). No grant is added by this order.
comp-adversary: DECLARED-NOT-APPLICABLE as a lens run; findings inlined in the steps -- (1) a push before the copies verify would deploy `_monolith_bronze.py` early, so the entry does not name it; (2) the census (2d) fails closed on a fence refusal of the copy identity.
lane: the <paths> block IS the grant; CloudOps seats act on infrastructure under a task order (rule 34).
</preflight>

Source: PRD v1.0 C-TIERS, C-MOVE, C-DAILY; the release plan; the CTO half @e7d8af9d1c; decomposition round 6 cell BF-r-1.
