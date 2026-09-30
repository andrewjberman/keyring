# NFRA_MCPMSP task order -- `MS-t-2` -- ROUND 1, hop 2 build: the Inflection firm role, in Terraform

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-t-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~2</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, alarm, monitor or cadence.
comp-iam: RUN at MS-a-1 (the applied role and the gateway's grant, by simulate-principal-policy); this cell writes the Terraform the lens grades there. Blindness: this cell sees the text, not the applied plane.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: none (the plan reads Opal's own AWS account).
</preflight>

## 1. THE CELL -- `MS-t-2` (decomposition section 2)

For each partner request the gateway assumes the asking firm's role, and that role reads ONLY that firm's data (PRD
C5 v0.2-v0.3). Round 1 builds Inflection's role. Write ONE new file,
`infra/aws/terraform/opal-gateway/mcpmsp_firm_roles.tf`, declaring:

1. **The role** named `gateway-inf-firm-reader-role`, which is `lib/opal_naming.py`
   `name('gateway', 'inflection', 'firm-reader', 'role')` output (measured at the cut; re-run it and use its output
   literally -- Rule 30: never hand-type a name the builder refuses). Trust: ONLY the gateway's instance role
   `opal-gateway-role` (declared in this directory as `aws_iam_role.gw`, `main.tf:146`; reference it, do not
   redeclare it) may `sts:AssumeRole`.
2. **Its policy** (inline or attached, your choice, in this file): `s3:GetObject` ALLOWED on
   `arn:aws:s3:::opal-data-inf/*` and on `arn:aws:s3:::opal-data-portal-v2/platinum/mdpf/inflection/*`; an explicit
   `Deny` on `s3:*` for `opal-data-cot`, `opal-data-bd` and `opal-data-49financial` (bucket and objects); and an
   explicit `Deny` on `s3:GetObject` for every `opal-data-portal-v2` object OUTSIDE `platinum/mdpf/inflection/`
   (a `NotResource` Deny is the usual shape). The CLAUDE.md cross-firm rule: "shared bucket -> key-prefix + IAM
   condition; per-firm buckets -> bucket-scoped Deny" -- both shapes, here.
3. **The gateway's one new grant**: `sts:AssumeRole` for `aws_iam_role.gw` on exactly this role's ARN, as a new
   `aws_iam_role_policy` in this file. Change NOTHING else about `aws_iam_role.gw` (its reads of
   `opal-data-portal-v2` are the accepted residual, PRD C5 v0.3, and stay).

**The directory's plan quirk (measured at the cut):** every plan here evaluates `filebase64sha256` over NFRA_MCPORTAL's
gitignored layer zip `infra/aws/lambda/layers/mcportal-grant-writer-deps/.build/mcportal-grant-writer-deps.zip`, and
the directory requires the two writer variables `mcportal_owner_key_claim` / `mcportal_owner_key`. AC2's check copies
the zip from the main tree (the issuer restored the DEPLOYED layer's exact bytes there, hash = the live CodeSha256)
and passes plan-only placeholders for the two variables; it borrows the main tree's `.terraform` through
`TF_DATA_DIR` (no `init`, which would fetch providers). Do not run `terraform init` and do not apply anything.

**AMENDMENT 1 (issuer, 2026-09-30, on your row NFRA_MCPMSP-Z-W2-S2 -- the naming gate is ENFORCE and refused 14
literals).** Items 1-3 above are REPLACED by these; keep your worktree and branch, rewrite the file:
1'. **Every name through the HCL builder module** `infra/aws/terraform/modules/opal_name` (it is `lib/opal_naming.py
   name()` in HCL; precedent `infra/aws/terraform/investor-reporting/holdings-performance/iam.tf:34-54`): one module
   call per name, `system = "gateway"`, `scope = "inflection"` (a module `scope` input is the gate's permitted context
   for the firm literal), `function = "firm-reader"`, `kind = "role"` for the role and `kind = "policy"` for its
   policy; a second function (e.g. `firm-assume`, `kind = "policy"`) for the gateway's grant policy. Every
   `name =` reads `module.<call>.name`. No typed name.
2'. **The role reads ONE thing in round 1: `opal-data-portal-v2/platinum/mdpf/inflection/*`**, built ONLY from builder
   outputs: the bucket is `module.<call>.scope_bucket["global"]`, and the firm's long form is derived from the
   builder's own name output, e.g. `module.<call>.scope_long[split("-", module.<call>.name)[1]]` (a literal index
   like `scope_long["inflection"]` or a variable default is refused by the gate -- measured). Allow `s3:GetObject` on
   that prefix; add an explicit `Deny` on `s3:GetObject` for every OTHER object of that same builder-named bucket
   (`NotResource` = the prefix). **Drop** the `opal-data-inf` Allow and the literal Denies on `opal-data-cot`,
   `opal-data-bd`, `opal-data-49financial`: the builder cannot name the live `opal-data-inf` today (the registry's
   `scope_bucket["inflection"]` is `opal-data-inflection`, and the live bucket is an alias with `lookup: false`; row
   Z-S2 carries it to the CTO), round 1's figures live only under the portal prefix, and every firm bucket carries its
   own live `DenyForeignFirmPrincipals` policy admitting only principals named `*-<firm short>-*` (measured in the
   holdings-performance precedent's header), which already refuses this role on the other firms' buckets.
3'. **The gateway's grant** unchanged in intent: `sts:AssumeRole` for `aws_iam_role.gw` on exactly this role's ARN.
   The role's trust names `aws_iam_role.gw.arn`.
4'. **Plans need the module registered:** AC2's check makes a PRIVATE copy of the main tree's `.terraform` providers
   and backend state and runs `terraform get` (a local module path: no network) before the plan. Never `init`, and
   never write the main tree's `.terraform`.
The criteria below are amended to this; the issuer ran both against a conforming prototype and against your current
file (AC1 PASS/FAIL respectively; AC2 `Plan: 3 to add` and the builder's role name seen on the prototype).

## 2. BOUNDS

1. Write surface: `mcpmsp_firm_roles.tf` only. No other `.tf`, no apply, no registry file (the name resolves with no
   registry row).
2. `terraform fmt` the file. Standing: no push, no vendor call. REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/mcpmsp_firm_roles.tf
infra/aws/lambda/layers/mcportal-grant-writer-deps/.build/mcportal-grant-writer-deps.zip
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~2/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

(The layer zip is gitignored; the entry admits the check's local copy into your worktree, never a commit.) Read, never
write: `infra/aws/terraform/opal-gateway/*.tf`, `lib/opal_naming.py`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W2-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-t-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/t2.AC1.sh; echo "exit=$?"</invocation><expect>role_module=y role_named_by_module=y served_bucket_from_builder=y mdpf_prefix=y assume_grant=y no_bucket_literal=y verdict=OK; naming gate: NAMING-GATE: PASS (paths in the graded diff: 1) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-t-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/t2.AC2.sh; echo "exit=$?"</invocation><expect>plan: Plan: N to add, 0 to change, 0 to destroy with N >= 3; planned role name gateway-inf-firm-reader-role seen>=1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~2/NFRA_MCPMSP.TO-MS-t-2.inflection-firm-role-build.proof_of_spec.json`.
Report once, with: the resource addresses; the plan line; the commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 issuance (CTO msg 26985). Checks dry-run at base: AC1 FAIL as expected (file absent); AC2
FAIL as expected (file absent). AC2's machinery controlled at the cut: a plan targeted at the existing
`aws_iam_role.gw` with the restored layer zip and the placeholders reads "No changes" in ~4 s. The restored zip:
`mcportal-grant-writer-deps-layer` version 1, 5,016,850 bytes, b64 sha256 `oO8BxcnG9EOvVz/pMpHlQCUGzkayANH3ryCKpNAaKfk=`
= the live CodeSha256. Slot `~2` continues to MS-a-1.

**AMENDMENT 1 (issuer):** on row Z-W2-S2 (naming gate ENFORCE, 14 REFUSE on literal names and bucket ARNs; also
Z-W2-S1, AC1 not recognising `aws_iam_role.gw`). Names move to `module opal_name`; the role reads only the builder-
built portal prefix; firm-bucket reads and literal cross-firm Denies are dropped for round 1 (the live firm-bucket
fences deny foreign principals; the `opal-data-inf` builder gap is row Z-S2, disarm_owner `1.0.0_SA_CTO~O`). AC1 now
checks module use, no bucket literal, and the naming gate over the whole file (denominator >= 1 path); AC2 adds the
builder's role name to the plan read and uses a private TF data dir + `terraform get`. Controls: AC1 FAIL on the
worker's literal file (REFUSE 14), PASS on the issuer's prototype; AC2 PASS on the prototype (`Plan: 3 to add`,
name seen). Graded by: no gate limb grades a modification's criteria (GATE (viii) `<placeholders>` only, NONE).

<status>pending</status>
<round>1</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
