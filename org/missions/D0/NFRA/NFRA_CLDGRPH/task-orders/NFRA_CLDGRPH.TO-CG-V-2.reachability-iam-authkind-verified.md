# TO NFRA_CLDGRPH.TO-CG-V-2 -- three VERIFY rows before anything is built: gateway -> cluster network REACHABILITY measured from both ends (S11), the IAM DELTA for the new worker and the new service read on the APPLIED plane and written as a proposal, never applied (S12), and the AuthKind an agent traversal fits, named with its line (S13)

<to_id>NFRA_CLDGRPH.TO-CG-V-2</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.7.0_AE_CloudOps~P</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-03</issued_date>
<status>pending -- GO paired at cut (2026-09-03 ~06:3xZ). AMENDED BY THE ISSUER 2026-09-03 ~07:4xZ, encoding only: V2-AC7's cell_refs re-written comma-separated (was space-separated, the ONE such attribute in 842 estate-wide; proof-of-spec-check.py:562 splits on commas) -- the DISARM of surprise row NFRA_CLDGRPH-S5 (BLOCKING, disarm_owner 2.0.0_SA_COO~A); the declared cell set CG-s-11/12/13 is unchanged, no criterion text changed, the spec stays frozen. ROUND 1 of NFRA_CLDGRPH, in parallel with TO-CG-V-1 at 0.7.0_AE_CloudOps~Q (a different seat; do not share a temp path or a lock). Authority: Andrew-direct at the 1.0.0_SA_CTO~A terminal ~05:1xZ (@8e134cc126) + his ruling (a) ~06:1xZ (@858fc08951: 2.0.0_SA_COO~A spawns Tier-2 workers at L6). The assignee commits its own status flip (task-orders/** is lane ANY @f9c97a52ce) after a VALID proof-of-spec instance; the L8 seat reads the record.</status>

**Directive:** D0 · **Fabric:** laptop · **PRD:** `../prd/NFRA_CLDGRPH_PRD.md` v0.4 @`25c66d3358` (s.6 "Open for the decomp": reachability, IAM, AuthKind are measurement-resolved inputs, never decide-first; s.7 rows S11, S12, S13; R3 the gateway is a THIN PROXY and never the host; R11 the read path is the agent default) · **Decomp cells:** `CG-s-11`, `CG-s-12`, `CG-s-13` (`../decompositions/NFRA_CLDGRPH_DECOMP.md` v0.1 @`994c9381d0`, s.1a; ROUND 1 "measure first" -- CG-s-11 can INVALIDATE CG-s-5's shape, CG-s-13 is a precondition of CG-s-5, CG-s-12 feeds CG-s-1/4/5) · **Lane:** the deliverable at `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~P/` (owner by path); NO Terraform, IAM, security group, route or repo source is changed by this task order. **Rule 27 seating:** `0.7.0_AE_CloudOps~P` is seated for NFRA_CLDGRPH only (pre-flight at cut: no process, no marker, not registered, no open task order; its one prior record is ETFS_POSITIONING.TO-5, CLOSED 2026-08-29 -- world-done, nothing owed). The lane's agent folder `org/tier2_senior/0.7.0_AE_CloudOps~P/` may not exist; the base folder's README + prompt apply; create the lane folder for your logs.

---

## THE CELLS -- three questions the PRD names as inputs, each answered by a measurement or a read, none by a decision

Before the serving plane (S4) and the gateway integration (S5) are built, three things are unknown and each can change what gets built: whether the gateway host can reach a service on the `opal-globgrph` cluster at all (if not, S5's whole shape changes); what IAM the NEW worker and the NEW service will need, read on the APPLIED plane and not from Terraform text (comp-iam cannot answer "is this denied?" -- silence is not "allowed"); and which existing `AuthKind` in the gateway's integration framework an agent traversal fits (a precondition for S5, not a detail of it). This task order answers all three and changes nothing.

## DELIVERABLE -- one file, three sections, one verdict each in the manifest's own vocabulary

`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~P/CG-s-11-12-13.reachability-iam-authkind.result.md`, one fenced JSON block + prose:

**A. CG-s-11 -- REACHABILITY, from both ends.**
1. The TOPOLOGY read: the gateway instance `i-07dccb1615503ac99` (t4g.nano) -- its VPC, subnet, security group(s), route table; the cluster side -- the VPC/subnets the `opal-globgrph` services run in and the four DECLARED security groups (`sg-0f27eda3ce895395d` nessie, `sg-0715c43654a151f69` trino, `sg-0f6cedf53107c6f8c` derive-runner, `sg-0191bda6ae427c0bb` incremental-updater) with their ingress rules. Instruments: `comp-find --corpus aws` on the node props (its `built:` vintage quoted) AND the live `aws ec2 describe-*` reads (the two must agree; a disagreement is a row).
2. The PROBE, both ends: from the gateway host (SSM `send-command`, a `curl`/TCP connect with a timeout -- no package install, no service restart, the `--workers 1` pin untouched) to an EXISTING in-cluster listener as the positive control (a Nessie or Trino task's private IP + port, read from `ecs describe-tasks`), and to a port/IP that MUST be closed as the negative control; and from the cluster side, the SG rule that would admit the gateway's SG or CIDR, present or absent.
3. The VERDICT, one of three: `REACHABLE` (positive control connects, negative refuses/times out) · `NOT-REACHABLE` (positive control fails; the blocking layer named: SG, NACL, route, subnet) · `REACHABLE-WITH-CHANGE` (the exact SG rule or route that would admit it, written as the Terraform resource text CG-s-4's task order would apply -- NOT applied here). Under `NOT-REACHABLE` with no single admitting change, state that CG-s-5's shape is invalidated and file the row.

**B. CG-s-12 -- IAM on the APPLIED plane, and the delta as a PROPOSAL.**
1. `comp-iam refresh-census` FIRST (the APPLIED census has a 24 h TTL and nothing refreshes it on a schedule; it was measured 664 h stale on 2026-09-01); quote the census vintage.
2. The APPLIED policies of the three principals the new ones will resemble: `opal-globgrph-incremental-updater` (the item2b Lambda: sqs 4 actions + s3 5 actions on `opal-313476888478-globgrph`), `opal-globgrph-nessie-task` (dynamodb 12 + s3 5), `opal-gateway-role` (10 statements; NONE on the globgrph bucket, no ECS or service-discovery action) -- DESIRED (Terraform, `comp-iam role <name>`) beside APPLIED (the census), and any drift named.
3. THE DELTA, as DESIRED text in the deliverable and nowhere else: for the NEW worker (read the warehouse + marker; write the versioned artifact, `_build_manifest` and the ONE pointer; consume the NEW queue S1 creates); for the NEW serving service (read the artifact + pointer); for the gateway (nothing, if the proxy is HTTP inside the VPC -- state it as a finding of A, or the one grant if not). Each statement with its action list and resource ARNs, least-privilege, and the name of the task order that will apply it (CG-s-1 / CG-s-4 / CG-s-5). Then `comp-iam gaps` before and after with its denominator unchanged (the control: nothing was applied).
4. `comp-iam simulate`, ONE ARN PER CALL (a batched multi-ARN simulate poisons verdicts; an `implicitDeny` on a CONDITIONED grant is a FALSE DENY -- read the condition before recording a deny), on two existing pairs that bound the new ones: the updater role on `s3:GetObject` of the marker key, and the gateway role on `s3:GetObject` of any globgrph key (expected DENIED: the negative control).

**C. CG-s-13 -- the AuthKind, named.**
Read `infra/aws/ec2/opal-gateway/app/integrations/registry.py` (67 @`2781aac326`; `ENABLED_INTEGRATIONS` at `:34` is CTO-arch-gated and NOT flipped here) and `docs/architecture/NFRA_INTEGRATIONS_STANDARD.md`; the two live integrations (`opal_portal`, `ycharts`) are the worked examples. Name the `AuthKind` an agent's Cypher traversal fits, with the framework line that defines it; name the one it does NOT fit and why; state whether the 5-step checklist admits a read-only proxy integration without a framework change (R3: the framework is NOT modified).

**D. The three verdicts in the manifest's `claim` vocabulary:** S11 `absent` -> the reachability verdict; S12 `unmeasured` -> `measured` with the census vintage; S13 `unmeasured` -> `measured` with the AuthKind. Each with the instrument and the vintage. These lines are what CG-s-1/4/5's task orders cite.

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the proof instance

<criterion id="V2-AC1" cell_refs="CG-s-11"/> `V2-AC1` -- TOPOLOGY READ on two instruments (aws corpus node props with `built:` vintage; live `describe-*`) for the gateway instance and the four cluster SGs: VPC, subnet, SG ids, ingress rules, route; the two instruments agree or the disagreement is a filed row.
<criterion id="V2-AC2" cell_refs="CG-s-11"/> `V2-AC2` -- THE PROBE from the gateway host to an existing in-cluster listener (positive control) and to a must-be-closed target (negative control), both results quoted with the command and its timeout; no install, no restart, `--workers 1` untouched (the gateway's process table before/after quoted).
<criterion id="V2-AC3" cell_refs="CG-s-11"/> `V2-AC3` -- THE VERDICT, exactly one of REACHABLE / NOT-REACHABLE / REACHABLE-WITH-CHANGE, with the blocking or admitting layer named and, for the third, the Terraform text NOT applied (the control: `terraform plan` on the untouched tree shows no change, or the plan is not run and the working tree is shown clean).
<criterion id="V2-AC4" cell_refs="CG-s-12"/> `V2-AC4` -- `comp-iam refresh-census` RUN FIRST with its vintage < 24 h at every APPLIED read; the three principals' APPLIED policies beside their DESIRED text; drift named or "0 drift on N statements".
<criterion id="V2-AC5" cell_refs="CG-s-12"/> `V2-AC5` -- THE DELTA as DESIRED text only (worker / service / gateway), each statement with actions + resource ARNs + the applying task order named; `comp-iam gaps` denominator identical before and after (nothing applied); two `simulate` calls, one ARN each, the gateway-role read of a globgrph key reading DENIED (the negative control), any conditioned deny read with its condition.
<criterion id="V2-AC6" cell_refs="CG-s-13"/> `V2-AC6` -- THE AUTHKIND NAMED at `file:line @ commit` with the one it does not fit and why; whether the 5-step checklist admits a read-only proxy integration with the framework unmodified; `ENABLED_INTEGRATIONS` untouched (the file's diff is empty -- quoted).
<criterion id="V2-AC7" cell_refs="CG-s-11, CG-s-12, CG-s-13"/> `V2-AC7` -- the three verdict lines in section D in the manifest's `claim` vocabulary with instrument + vintage; PUSH STATE MEASURED at report (`ls-remote` + `is-ancestor`; LOCAL expected -- say which state was read); the proof instance VALID (`.tools/proof-of-spec-check.py` rc 0) with every `surprises` entry resolving to a row BEFORE the complete flip, which this seat commits itself.

<expected_criteria>V2-AC1, V2-AC2, V2-AC3, V2-AC4, V2-AC5, V2-AC6, V2-AC7</expected_criteria>

## SURFACES

Gateway `i-07dccb1615503ac99` (t4g.nano, `--workers 1` MANDATORY) · `infra/aws/terraform/opal-gateway/main.tf` (`opal-gateway-role`) · `infra/aws/ec2/opal-gateway/app/integrations/registry.py` 67 @`2781aac326` · `docs/architecture/NFRA_INTEGRATIONS_STANDARD.md` · cluster `opal-globgrph` (`infra/aws/terraform/globgrph/nessie.tf:14`, 215 @`d8d0d7d26d`; 2 active services, 7 task definitions at the 2026-09-03T00:36Z corpus build) · the four SGs above (all DECLARED; `comp-find --corpus aws 'opal-globgrph'` band SECURITY_GROUP) · `infra/aws/terraform/globgrph/iam.tf` (`globgrph_incremental_updater`, `nessie_task`, `nessie_execution`) · `infra/aws/terraform/globgrph/item2b.tf` 199 @`e0a3d7fd87` (the existing queue + DLQ + Lambda event source -- the pattern S1 copies, NOT the queue S1 uses) · S3 `opal-313476888478-globgrph`, marker key `warehouse/_branch_head.main.json`.

## BOUNDS

- **READ-ONLY plus one network probe.** No `terraform apply`, no IAM grant or policy edit, no SG or route change, no ECS service change, nothing installed on the gateway host, no gateway restart. A change this task order finds necessary is written as Terraform TEXT in the deliverable for the task order that will apply it (CG-s-1 / CG-s-4 / CG-s-5), with its exact resource named.
- **comp-iam traps, stated because each has drawn blood:** run `refresh-census` before any APPLIED read; `simulate` one ARN per call; an `implicitDeny` on a conditioned grant is a false deny; "no parsed deny" is never "allowed".
- **No monitor, alarm, checker or SNS** (CLAUDE.md s.5; PRD R4).
- **Do not collide with TO-CG-V-1 at `0.7.0_AE_CloudOps~Q`:** that seat runs full loads to a temp path; this seat reads IAM and network. Neither touches the canonical local DB or its lock.
- **A spec-vs-world divergence is a ROW** at `org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md` (create the folder on the first row; lane ANY; schema at `org/surprise_channel/schemas/`), then keep working; never a message. `3.0.0_SA_CVO~A` reads the file at L8. A BLOCKING row also goes to the issuer in the same turn; NOT-REACHABLE with no admitting change is BLOCKING for CG-s-5 and is filed as such.
- **Certifier != author:** this seat measures and files; the grade is the L8-L10 seat's on the record.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> @994c9381d0 (v0.1), cells CG-s-11, CG-s-12, CG-s-13 (s.1a, ROUND 1 "measure first").
<owned_cells>CG-s-11, CG-s-12, CG-s-13</owned_cells>
Read-dependencies, NOT claimed: CG-s-1 (the queue policy S12's delta names), CG-s-4 and CG-s-5 (the builds these verdicts shape), CG-s-10 (the parallel measurement at the other seat).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 19 across 5 carriers (C1 sentinel denominator 21 -> 5, C2 deploy-ledger 2 -> 2, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 336 NOT-DECIDABLE -> 0); 138 prose blocking fields NEEDS-READ; 0 armed gates name NFRA_CLDGRPH, globgrph, kuzu, opal-gateway, IntegrationSpec, comp-graph or KUZUSPLIT (read at 2026-09-03 06:29:48Z).
comp-iam: RUN -- DESIRED plane at cut: 180 roles parsed / 187 services / 1,074 operations / 306 gaps estate-wide; the three principals this task order reads enumerated by name (`opal-globgrph-incremental-updater` 6 statements, `opal-globgrph-nessie-task` 2, `opal-gateway-role` 10; 15 globgrph-family roles of 180). BLIND at cut on the APPLIED plane and on the two NEW principals by construction -- that blindness is exactly what CG-s-12 measures (refresh-census, then the APPLIED reads, then simulate one ARN per call).
comp-adversary: RUN -- rc 0 at read-vintage @a1af5d70c2 (2026-09-03T06:34:47Z, --no-packet: stage 4 disabled by the caller, disclosed); pins found 8 commits, 10 repo paths, 0 file:line cites (the `:NN` pins sit inside backticks), 6 tool mentions; cited commits 8 attempted / 8 verified / 0 UNVERIFIABLE; cited paths 10 attempted / 7 stable / 3 flagged (all three flagged = GONE at read-vintage: the deliverable file, the proof instance and the investigation file this TO CREATES -- expected, not stale); uncited siblings 516 with the cap (25) declared; 6 hex runs not parsed as pins by design (four SG ids, the gateway instance id, the account id); complement sources 4 run / 0 deferred / 5 declared-excluded (v1 contract). Instrument: comp-adversary CLEARED @bbba0db0e9, run from a seat that did not fix it.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `V2-AC1`..`V2-AC7`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~P/NFRA_CLDGRPH.TO-CG-V-2.reachability-iam-authkind-verified.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the assignee commits itself. V2-AC2's negative-control
probe, V2-AC5's DENIED simulate and the unchanged `gaps` denominator are the arms that must be able to FAIL; every `surprises` entry opens with
a row id that resolves in the project's channel (the SURPRISES limb refuses the flip otherwise).
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-find --corpus aws 'opal-globgrph' --all --budget 300` (SECURITY_GROUP + ECS bands; quote `built:`), `comp-find --corpus aws 'opal-gateway' --budget 300` (the instance + its SG), `comp-iam refresh-census`, `comp-iam role opal-globgrph-incremental-updater` / `opal-globgrph-nessie-task` / `opal-gateway-role`, `comp-read infra/aws/ec2/opal-gateway/app/integrations/registry.py --for "the AuthKind enum, what each kind requires, and how ENABLED_INTEGRATIONS gates a new integration"`. DURING: `comp-iam simulate` one ARN per call; live `aws ec2 describe-instances` / `describe-security-groups` / `aws ecs describe-tasks` via the `.tools/aws` shim. AFTER: `comp-iam gaps` (denominator unchanged); `.tools/proof-of-spec-check.py` on the instance; `git ls-remote origin CLOUD` + `git merge-base --is-ancestor` for V2-AC7.
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO~A` (the sequencer; the L8 seat `3.0.0_SA_CVO~A` reads the record, not a message; never message that seat) with per-criterion evidence, the three verdict lines, the delta text, and push state as MEASURED. GO = this TO + the dispatch message.
