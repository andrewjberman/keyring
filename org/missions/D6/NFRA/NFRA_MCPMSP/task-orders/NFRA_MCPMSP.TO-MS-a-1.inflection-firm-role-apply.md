# NFRA_MCPMSP task order -- `MS-a-1` -- ROUND 1, hop 2 apply: the Inflection firm role goes live, A1n arms read live

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-a-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~2</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: RUN -- this cell IS the lens's instrument: AC2 and AC3 simulate the applied role and the gateway role. Blindness: the two roles and the named resources only, not the rest of the account.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the negative arms are the adversary read.
EGRESS CLASS, declared: none (Opal's own AWS account).
</preflight>

## 1. THE CELL -- `MS-a-1` (decomposition section 2)

Apply the Terraform the previous order in your queue (`MS-t-2`) built -- `infra/aws/terraform/opal-gateway/mcpmsp_firm_roles.tf`
at CLOUD HEAD after its merge -- and read the negative arms live.

1. **Open the ledger FIRST** (NEVER-2, PRD C12): `python .tools/deploy_ledger.py open --slug nfra-mcpmsp-r1-firm-role
   --title "NFRA_MCPMSP r1: Inflection firm role + gateway AssumeRole grant" --author 0.9.0_WK_NFRA_MCPMSP~2 --leg
   "L1|activation|terraform apply targeted to mcpmsp_firm_roles.tf|apply output line" --leg "L2|verify|simulate-principal-policy
   arms|AC2+AC3 lines"`, and name the BLAST RADIUS in the entry: one role, its policy, one `sts:AssumeRole` grant on
   the gateway role; the rollback is `terraform destroy -target` of exactly those addresses. Commit the entry AND its
   sentinel `org/critical_paths/.open_deploys/nfra-mcpmsp-r1-firm-role.json` before the apply.
2. **Plan, then apply, targeted** to every resource `mcpmsp_firm_roles.tf` declares (and nothing else), through
   `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply -target=... ` (never bare `terraform apply`).
   The directory needs (measured at the cut): NFRA_MCPORTAL's gitignored layer zip at
   `infra/aws/lambda/layers/mcportal-grant-writer-deps/.build/mcportal-grant-writer-deps.zip` (copy it from the MAIN
   worktree, where the issuer restored the deployed bytes) and the main tree's `.terraform` via `TF_DATA_DIR` (no
   `init`). It also requires `mcportal_owner_key_claim` / `mcportal_owner_key`: read BOTH from the LIVE writer
   function's environment (`aws lambda get-function-configuration --function-name mcportal-grant-writer-lambda`,
   keys `MCPORTAL_OWNER_KEY_CLAIM` / `MCPORTAL_OWNER_KEY`) into shell variables and pass them as `-var`, **never
   printing, logging or committing the key value**. The plan before the apply must read only additions for your
   targets (`N to add, 0 to change, 0 to destroy`); anything else is a BLOCKING row and no apply.
3. **Read the live arms** (AC2, AC3), then close each leg and the entry (`deploy_ledger.py close-leg` / `close`),
   committing the closed entry with the sentinel removed.

**AMENDMENT 1 (issuer, 2026-09-30, following MS-t-2's AMENDMENT 1).** `mcpmsp_firm_roles.tf` now names through the
local module `opal_name` and reads ONLY `opal-data-portal-v2/platinum/mdpf/inflection/*` in round 1 (no firm-bucket
read; the firm buckets' own `DenyForeignFirmPrincipals` policies refuse foreign principals). Two consequences here:
- **Use a PRIVATE Terraform data dir, never the main tree's:** copy `<main tree>/infra/aws/terraform/opal-gateway/.terraform/providers`
  and its `terraform.tfstate` (the backend pointer) into a temp dir, `export TF_DATA_DIR=<it>`, run `terraform get`
  (registers the LOCAL module; no network), then plan and `safe-apply` with the same `TF_DATA_DIR`. The state itself
  stays in the remote backend; nothing is written to the main tree's `.terraform`.
- AC2 no longer reads an own-bucket arm; it reads own prefix ALLOWED, the other firm's prefix and bucket NOT allowed.
  The ledger's blast radius names the module-named role, its policy, and the gateway's one AssumeRole policy.

## 2. BOUNDS

1. Blast radius: the addresses in `mcpmsp_firm_roles.tf` only. The writer, the gateway role's existing policies and
   every other resource are untouched; if a targeted plan shows any change outside them, STOP with a BLOCKING row.
2. No push, no vendor call. REFUSE a criterion you cannot meet as written, with its measurement.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpmsp-r1-firm-role.json
infra/aws/lambda/layers/mcportal-grant-writer-deps/.build/mcportal-grant-writer-deps.zip
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~2/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `infra/aws/terraform/opal-gateway/*.tf`, `.tools/safe-apply.sh`, `.tools/deploy_ledger.py`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/`.

Rows: `INVESTIGATION_v1.Z.md`, id `NFRA_MCPMSP-Z-W2-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your last commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-a-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/a1.AC1.sh; echo "exit=$?"</invocation><expect>slug nfra-mcpmsp-r1-firm-role: entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR present -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-a-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/a1.AC2.sh; echo "exit=$?"</invocation><expect>role gateway-inf-firm-reader-role: own-prefix=allowed cot-prefix=(implicitDeny|explicitDeny) cot-bucket=(implicitDeny|explicitDeny) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MS-a-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/a1.AC3.sh; echo "exit=$?"</invocation><expect>gateway role opal-gateway-role: AssumeRole(gateway-inf-firm-reader-role)=allowed; GetObject opal-data-inf=(implicitDeny|explicitDeny) opal-data-cot=(implicitDeny|explicitDeny) -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~2/NFRA_MCPMSP.TO-MS-a-1.inflection-firm-role-apply.proof_of_spec.json`.
Report once, with: the role ARN (the issuer puts it in the release's `.env` line); the plan and apply lines; the three
check lines; the ledger entry path; the commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 issuance (CTO msg 26985); WORLD: a grant. Checks dry-run at base: AC1 FAIL as expected (no
entry); AC2 FAIL as expected (`NoSuchEntity`, no role); AC3 FAIL as expected (`AssumeRole=implicitDeny`;
the two S3 arms already read `implicitDeny` at base -- A1n arm 3 holds today, so AC3's FAIL is carried by the grant
arm, which is the build). The owner-key vars are read from live config so a mistargeted apply could not move the
writer's environment. Spawn: the slot continues here after MS-t-2 is merged.

**AMENDMENT 1 (issuer):** follows MS-t-2's AMENDMENT 1 (module names, portal-prefix-only read). The private TF data
dir + `terraform get` procedure is added; AC2's own-bucket arm is removed (round 1 grants no firm-bucket read; row
Z-S2). AC2 still FAILs at base (`NoSuchEntity`). Graded by: no gate limb grades a modification's criteria.

<status>complete -- drained by 2.0.0_SA_COO~MS 2026-09-30: applied 3 added / 0 changed / 0 destroyed (arn:aws:iam::313476888478:role/gateway-inf-firm-reader-role); AC1-AC3 PASS on the issuer's re-run; ledger nfra-mcpmsp-r1-firm-role CLOSED; instance VALID. Was: staged</status>
<round>1</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
