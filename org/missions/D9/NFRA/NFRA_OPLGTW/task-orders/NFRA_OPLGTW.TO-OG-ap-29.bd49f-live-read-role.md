# NFRA_OPLGTW task order -- `OG-ap-29` -- APPLY (grant): a dedicated read-only role on exactly opal-data-bd/silver/{unrealized,transactions,allocations,fees}/ for the 49F Black Diamond live tables (round 38; CTO ruling @8b2865e461; PRD v3.6 item 2; row Z-S292)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-29</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-29</to_id>
<issued_to>0.7.0_AE_CloudOps~ZS</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; the applier still runs `comp-schedule --drift` at the act and records what it scanned.
comp-iam: RUN-BY-ISSUER at the cut (`comp-iam stats` 2026-10-16 ~06:3xZ: 222 IAM roles parsed, 197 services, 1175 operations, 345 permission gaps estate-wide; a DESIRED-plane lens that cannot see a live-only policy, so the applier reads the live roles in Phase A step 1): ONE new role and ONE inline policy (read-only on four prefixes of one bucket), plus at most one change to the Gateway instance role's permission to assume client roles if its policy lists role ARNs (read how `client_vendor_roles_iam.tf` and its siblings let the instance role assume the six vendor roles, and do the same for this one). Nothing is removed; `gateway-49f-blackdiamond-read-role` keeps its explicit Deny and is NOT touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling (@8b2865e461: "-live routes to a dedicated read-only role on exactly opal-data-bd/silver/{unrealized,transactions,allocations,fees}/ (v3.6 item 2), never-widen with three halves; blackdiamond49f keeps its Deny") on PRD v3.6 (Andrew-direct 2026-10-14: "We can allow 49F Black Diamond pulls from opal-data-bd, you're right that's fine") and the CVO's row Z-S292 (the 49F role's policy explicitly denies every opal-data-bd key; simulate reads explicitDeny).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-29` (decomposition addendum R3-T.96, round 38, workstream ENRICH-R38-D, FWD-22)

WHY. The 49F Black Diamond adapter's live tables sit in `opal-data-bd/silver/`. The code (`OG-en-12`, building now) routes the `-live` segment to its OWN role key (`blackdiamond49flive`, environment variable `BLACKDIAMOND49FLIVE_READER_ROLE_ARN`), because `gateway-49f-blackdiamond-read-role` explicitly denies every opal-data-bd key and is not to be widened. This cell creates that role. It never deploys: the release is a later applier order, and this grant is applied BEFORE it.

### PHASE A (files, plan, ask; NO apply IN ANY FORM)

1. **Read the live state first.** `get-role` and `get-role-policy` for `gateway-49f-blackdiamond-read-role` (to copy its trust form and to confirm what stays), `get-role` for `opal-gateway-role` (the instance role: its ARN and how it is allowed to assume the vendor roles), `list-roles` filtered to prove the new role name is absent. Read `infra/aws/terraform/opal-gateway/client_vendor_roles_iam.tf` and `blackdiamond_reader_iam.tf` for the Terraform form. Write `W/BDLIVE_BEFORE.json` (names, document hashes, no ARN of an account other than as the ARN the checks need).
2. **Write the Terraform** `infra/aws/terraform/opal-gateway/blackdiamond_live_reader_iam.tf`: ONE `aws_iam_role` and ONE `aws_iam_role_policy` on it. Names are `lib/opal_naming.py name()` output through `../modules/opal_name` (a builder refusal is a missing registry row to add under `infra/logic/registry/`, never a typed workaround). Trust: ONLY the Gateway instance role (`aws_iam_role.gw`), the same form as the six vendor roles. Policy: `s3:GetObject` and `s3:GetObjectVersion` on `arn:aws:s3:::opal-data-bd/silver/<t>/*` for `<t>` in `unrealized`, `transactions`, `allocations`, `fees` (read the catalog rows and the adapter, `app/client_adapter_bd49f.py`, to confirm these are the four tables it reads, and state any difference in the ask rather than adding a prefix); `s3:ListBucket` on `arn:aws:s3:::opal-data-bd` ONLY with an `s3:prefix` `StringLike` of `silver/<t>/*` for the same four; explicit Deny on every other object, every other prefix's listing, every other bucket and every non-read S3 action (copy the form of `cv_blackdiamond49f_read_policy`). No `*` resource, no bucket-root object ARN, no Put, no Delete. If the instance role's assume permission lists role ARNs, add this one by the same mechanism (a `1 to change`).
3. **The plan**, targeted at the new resources (and the one change if any), `-lock=false`, no `-out`, no apply: it must read `2 to add, M to change, 0 to destroy` with M 0 or 1 and every change named. Save it as `W/BDLIVE_PLAN.txt`. Any other change is a STOP.
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-29.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`), each under a heading containing its word (CTO, COO, CVO): (1) the `diff`; (2) the `widening`, stated plainly: a new role, assumable only by the Gateway instance role, gains read-only on four opal-data-bd silver tables that hold Black Diamond client data for firm 49F (the live tables the code will read through it), nothing else, no other firm; the instance role gains the right to assume it; `gateway-49f-blackdiamond-read-role` and its Deny are untouched; state who can assume it today (read the trust) and what the alternative to a same-account role-ARN trust costs; (3) the `tools` that will use it (the four 49F client tools: holdings, transactions, allocation, fees, master_admin only per PRD v3.14); (4) the `order` of acts (one targeted apply; the role and the instance-role change read back from IAM; BEFORE the batched release); (5) `both branches` (an in-scope read serves; anything else is denied by IAM; a non-master_admin caller is refused by the gateway before any S3 call); (6) the `rollback` (a targeted destroy of the role and policy and the removal of the assume entry; the prior state is `BDLIVE_BEFORE.json`; nothing serves through it until the release); (7) the `triggers`. Commit, run AC1, REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at the `.tf` hash)

5. Ledger `nfra-oplgtw-grants-ap29`, entry AND sentinel first. Apply through `safe-apply`, targeted. Read back from IAM: the role exists, trust names only the instance role's ARN, the policy equals the file; the instance role's assume entry (if any); `simulate-principal-policy`, ONE resource per call: GetObject allowed on a probe key under each of the four prefixes, ListBucket allowed with each as the `s3:prefix` value, and NOT allowed on `opal-data-bd/silver/ap29-negative-control/probe`, on an `opal-data-assets` key, PutObject on an allowed prefix, and ListBucket with an out-of-scope prefix (run as their own invocations); a `*`-principal positive control beside any deny read. Re-plan the target: `No changes`. On a trigger failing, destroy the role and policy, restore the instance role's prior state and file an ARMED row naming `2.0.0_SA_COO~O`. Close the ledger, write `W/BDLIVE_APPLIED.json` = `{"role_name": "<name>", "policy_names": ["<n>"], "prefixes": ["opal-data-bd/silver/<t>/", ...], "applied_at": "<iso>"}`, commit, run AC2, report once.

## 2. BOUNDS

- IAM and Terraform of the one new role and its policy (and the one assume-permission change if any). No object read or written; no deploy; no other role or policy touched, `gateway-49f-blackdiamond-read-role` least of all.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform apply` (use `safe-apply`); apply in Phase A in ANY form; print an account number or an object's content.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/blackdiamond_live_reader_iam.tf
infra/aws/terraform/opal-gateway/client_vendor_roles_iam.tf
infra/aws/terraform/opal-gateway/main.tf
infra/aws/terraform/opal-gateway/.terraform.lock.hcl
infra/logic/registry/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-grants-ap29.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZS/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZS/`. You WRITE the one new `.tf` and, only for the assume-permission entry if the instance role's policy lists role ARNs, the file that holds it (the generated `client_vendor_roles_iam.tf` is NOT to be edited by hand: put the entry where a non-generated file already carries the instance role's assume policy, or in the new file); `client_vendor_roles_iam.tf` and `main.tf` are listed only so you can name the exact place if it is needed. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free; a correction is a NEW row citing the old id), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from the repo root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-29"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ap29.AC1.sh; echo "exit=$?"</invocation><expect>(?s)terraform: roles 1 \(want 1\); policies 1 \(want 1\); trust names the instance role True; put/delete/star actions \[\] \(want none\); wildcard False \(want False\); bucket-root object arn False \(want False\); other bucket named False \(want False\).*prefixes: the four silver tables in GetObject resources True; in ListBucket s3:prefix values True.*plan: 2 to add, 0 or 1 to change, 0 to destroy True; ask has the three halves True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-29"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ap29.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0; role exists yes; trust is only the instance role 1 \(1 = yes\); simulate GetObject allowed 4 of 4, ListBucket allowed 4 of 4; negative controls not allowed 4 of 4.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the one `.tf` creates one role and one policy, read-only on the four prefixes of opal-data-bd, trusting only the instance role, and the plan is two additions (and at most one named change). `AC2`: the role is live, trusts only the instance role, the simulator allows the four prefixes and refuses the four negative controls, and the ledger is closed.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-29.bd49f-live-read-role.proof_of_spec.json` (the file name includes the slug). Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 38 (CTO ruling @8b2865e461; row Z-S292), workstream ENRICH-R38-D (decomposition addendum R3-T.96). Chain: NFRA_MCPINDEX writes the `address` field on the four catalog rows; `OG-en-12` (the code, worker `~125`); this cell (the role); the batched gateway release, whose deploy hunk adds the env key `BLACKDIAMOND49FLIVE_READER_ROLE_ARN` (read from `iam get-role`, as the six keys of `OG-ap-23` A3 were) and refuses before upload if the role does not resolve; then the `OG-en-11` re-run closes Z-S292.
- The Phase A GO is the issuer's message citing this order. Applied BEFORE the release.
- Pre-cut: ap29.AC1 base FAIL as expected (tf, plan and ask absent); ap29.AC2 base FAIL as expected (BDLIVE_APPLIED.json absent).

<status>complete</status>
<round>38</round>
<workstream>ENRICH-R38-D</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
