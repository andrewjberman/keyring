# TO NFRA_OPSEC202609.TO-OP-S-3 -- THE ORIGIN SECRET: a request that did not come through our front door is refused even with a real login (the first atom, C-1)

<to_id>NFRA_OPSEC202609.TO-OP-S-3</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>pending</status>

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` v0.4 @43b75ffbd6 (ENDPOINT FWD-2, property 2; s.7.1 the dependency that comes first; 7.6 C-1) - **Decomp cell:** `OP-s-3` (v0.1 @bff1f8d012, s.1a; the ROUND 1 fence: "OP-s-3 first") - **Lane:** `infra/aws/terraform/portal-auth/**`, `infra/aws/terraform/shared-infra/apigateway-portal/**`, the HTTP API's authorizer/handler code under `infra/aws/opalinvest_dev/lambda/auth-handler/**` and `infra/aws/users/lambda/portal-authorizer/**` (AE lane; the OTP deploy @f4659653e8 is the precedent for the handler being in this lane) - **Round:** 1 of NFRA_OPSEC202609.

---

## THE CELL -- what the brief measured and what this cell changes

Today the only proof that a request came through CloudFront is the header `X-Origin-Verify` whose value is the CONSTANT string `"cloudfront"`, injected by `auth-validator-edge/index.mjs:392` and checked by NOTHING (the header name appears in exactly one first-party file -- brief F1, estate sweep). Both API gateways answer at their own `execute-api` addresses: the REST API `f61h681z9g` with no authorizer at all (S1's cell, NOT this one), the HTTP API `7k3ed8px20` with `portal-jwt-authorizer` on 60 of 72 routes and `ANY /auth/{proxy+}` deliberately NONE (pre-auth). So a caller holding a VALID login can talk to the back door with it, and credential stuffing can route around the CloudFront WAF rate rule (brief F1, F2, F4 -- the one mechanism all three share).

**This cell lands ONE secret with two consumers:** a value in Secrets Manager, set by CloudFront as a CUSTOM ORIGIN HEADER on the origins that front BOTH gateways (an origin header is set by the distribution, never by the edge function -- the edge's own Terraform is gated by a default-false variable with `ignore_changes` on the live association, `portal-auth/lambda-edge.tf:11,33-58,115`, so nothing in this cell rides that path), and REQUIRED by the HTTP API side for `/auth/*` and every `/v1/*` data route (the REST authorizer that will require it is OP-s-1's cell; this cell delivers the secret it will read). Rotation is a dual-value overlap: the consumers accept the outgoing and the incoming value for one overlap window, so a rotation never 401s the portal.

**C-1 is a RULING (PRD s.6, 7.6):** nothing in OP-s-14 (the sentinel) is EXERCISED before this cell is DONE. That is why this is the first atom.

## DELIVERABLE -- Terraform + one code change + one runbook, nothing else

1. **The secret.** `opal/portal/origin-verify` (or the name the module's convention dictates -- state it) in Secrets Manager, Terraform-declared, a random high-entropy value, with a `current` and a `previous` slot (or two versions with staging labels) so the overlap in 3 is possible. No value in any file, log or commit message.
2. **The header on the distribution.** The CloudFront distribution `EVTSA9VEHNZVH` (`portal-auth/cloudfront-distribution.tf`, an IMPORTED resource: `:5` says do not apply without verifying 0-diff first) gains a custom origin header carrying the secret's value on the origin(s) that front `7k3ed8px20` and `f61h681z9g`. Terraform reads the value from the secret at plan time (data source), never a literal. The header NAME may stay `X-Origin-Verify` (so the edge's constant injection is simply superseded by the distribution's) or be new -- state which and why in the proof; if the edge's line stays in the code, say that it is now inert and why that is safe.
3. **The check on the HTTP API side.** For `/auth/*` (NONE at the API by design) the check lives where a request first reaches our code: the auth handler refuses a request whose origin header does not match `current` or `previous` (a 403 with a fixed body, no detail). For the `/v1/*` data routes the check lives in `portal-jwt-authorizer` (the REQUEST authorizer already on 60 of 72 routes; the 9 NONE data routes gain it in OP-s-2's cell, which reads this secret through the same code path). Deployed by the estate's Lambda path (`build-nodejs-lambda` -> S3 -> plan -> `safe-apply` -> CodeSha256 verify), with the two site-Z script defects 1.0.0_SA_CTO~Z recorded on 2026-09-02 (`to_native_path` handles `/c/` only; `record-terraform-deploy.sh` cp1252 + unquoted space) named on the face if they bite, never silently worked around.
4. **The rotation runbook**, one file under `../deliverables/0.7.0_AE_CloudOps~Z/`: how a rotation is performed (mint next -> promote to `current`, demote to `previous` -> update the distribution header -> wait one overlap window -> retire `previous`), with the overlap window named and the reason it cannot 401 the portal.
5. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~Z/NFRA_OPSEC202609.TO-OP-S-3.origin-secret-both-gateways.proof_of_spec.json`, VALID under `.tools/proof-of-spec-check.py` before the complete flip, every `surprises` entry opening with a row id in `../surprise-channel/investigations/INVESTIGATION_v1.md`.
6. **A deploy-ledger entry** opened at the start of the apply and closed at completion (CLAUDE.md NEVER-2: a confirmed deploy is never left half-landed); `safe-apply`, never bare `terraform apply`.

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the instance

<criterion id="S3-AC1" cell_refs="OP-s-3"/> `S3-AC1` -- THE SECRET EXISTS AT APPLIED: `aws secretsmanager describe-secret` on the declared name returns the resource, Terraform-managed (state shows it), with the two-slot / two-version shape the runbook names; its VALUE appears in zero files of the commit (a `git show` census of the commit's diff for the value's first 8 characters returns 0 -- the negative control is that the SECRET NAME returns > 0).
<criterion id="S3-AC2" cell_refs="OP-s-3"/> `S3-AC2` -- THE HEADER IS ON THE LIVE DISTRIBUTION: `aws cloudfront get-distribution-config --id EVTSA9VEHNZVH` read AFTER the apply shows the custom origin header on every origin that fronts `7k3ed8px20` and `f61h681z9g` (denominator = the origin count in that config, printed), and the pre-apply plan against the imported distribution was 0-diff BEFORE this change was added (the `:5` bound, exhibited as the plan's own summary line).
<criterion id="S3-AC3" cell_refs="OP-s-3"/> `S3-AC3` -- THE CHECK IS DEPLOYED, NOT JUST COMMITTED: the auth handler's and the authorizer's live `CodeSha256` (`aws lambda get-function-configuration`) equal the built artifacts' sha (the OTP-deploy oracle @f4659653e8), and a Terraform re-plan after the apply reads 0-diff; the `file:line @ commit` of the check in both functions cited.
<criterion id="S3-AC4" cell_refs="OP-s-3"/> `S3-AC4` -- THE RUNBOOK NAMES ITS OVERLAP: the runbook file exists at its pin, names the overlap window in seconds and the two-slot mechanism, and states the reason a rotation cannot 401 the portal (both consumers accept `current` OR `previous`) with the code line that implements the OR cited.
<criterion id="S3-AC5" cell_refs="OP-s-3"/> `S3-AC5` -- EXERCISED (FWD-2 DONE WHEN), UNDER ANDREW'S WORD ONLY: a request carrying a VALID login (a FIXTURE account, never a pilot) sent to the DIRECT `execute-api` address of the HTTP API on a READ-ONLY route is REFUSED (status + fixed body quoted), and the SAME request through the portal path is ADMITTED. **This criterion is HELD on card OP-x-1 (the probe authorization). If his word has not arrived when the instance is filed, the status is `UNCOMPUTABLE-BY-CONSTRUCTION` with `status_reason` "OP-x-1 HELD at Andrew" -- the instance stays VALID, the cell reads IN-FLIGHT (APPLIED half done), and the exercise is a closing-pass act on his word. Never a probe without it; never a write to production data.**
<criterion id="S3-AC6" cell_refs="OP-s-3"/> `S3-AC6` -- PUSH STATE MEASURED at report (ls-remote + is-ancestor against origin/SITEZ); the expected reading is LOCAL (0.0.0_AB_MSTR~Z integrates; LD-0367) -- say which state was read. The deploy-ledger entry is CLOSED with its completion proof, sentinel removed.

<expected_criteria>S3-AC1, S3-AC2, S3-AC3, S3-AC4, S3-AC5, S3-AC6</expected_criteria>

## SURFACES (the brief's reads at @32daebf403; RE-GROUND EACH AT YOUR OWN VINTAGE AS YOUR FIRST ACT)

`infra/aws/lambda-edge/auth-validator-edge/index.mjs:392` (the constant header) - `infra/aws/terraform/portal-auth/cloudfront-distribution.tf` (imported; `:5` 0-diff bound; `:116` the WAF is full IaC in `waf-cloudfront.tf`) - `portal-auth/lambda-edge.tf:11,33-58,115,204` (the edge's gated Terraform; read `:204` for how the LIVE association is read) - `portal-auth/secrets.tf` (the JWT keypair's declaration pattern; follow it) - `portal-auth/cross-firm-secret-deny.tf` (the Deny-belt pattern; the new secret must NOT be reachable by the cross-firm-scoped roles that belt protects against) - `infra/aws/opalinvest_dev/lambda/auth-handler/src/index.ts` (the handler's entry; the `/auth/*` check lands here) - `infra/aws/users/lambda/portal-authorizer/index.mjs` (`portal-jwt-authorizer`) - `infra/aws/terraform/shared-infra/apigateway-portal/main.tf` (the HTTP API `7k3ed8px20`; to be confirmed as its carrier at your vintage) - brief `docs/briefs/PLATFORM_ATTACK_SURFACE_ASSESSMENT_20260902.md` F1 :14-60, F2 :65-83, F4 :113-130.

## BOUNDS

- **ONE secret, two consumers.** No second secret, no per-gateway values. The REST authorizer that will read it is OP-s-1's cell (next TO on this seat), not this one; do not build it here.
- **Never-widen.** The 9 NONE data routes stay NONE in THIS cell (OP-s-2 closes them); `/auth/*` stays NONE at the API (the check is in the handler). No route's authorizer configuration changes here except to READ the secret.
- **The imported distribution: 0-diff first** (`cloudfront-distribution.tf:5`), `safe-apply` only, a deploy-ledger entry open for the whole apply, the cache-key params untouched (`cloudfront.tf:16`: "firm-isolation load-bearing -- NEVER change them in a TTL pass").
- **No probe without Andrew's word** (S3-AC5); no request that writes; no pilot account.
- **No Cognito**, anywhere, in any comment (PRD s.6).
- **A spec-vs-world divergence is a ROW** at `../surprise-channel/investigations/INVESTIGATION_v1.md` (lane ANY; the file mints on your first row; site Z ids are `NFRA_OPSEC202609-Z-S<n>`; carry `project`, `fabric`, `spec_asserts`, `world_is`) -- then keep working. Never a message. The L8 seat reads the file.
- **One project per instance (Rule 27).** This seat holds NFRA_OPSEC202609 ONLY. `D12_PHONE_OTP_ALL_AWS` items that name `0.7.0_AE_CloudOps~Z` (the SB face, its instance) are NOT this seat's this round -- barred; the issuer re-addresses them.
- **Commit under your own serial** via `.tools/safe-commit.sh --author "0.7.0_AE_CloudOps~Z <0.7.0_AE_CloudOps~Z@opal.agent>" -F <msgfile>` (msgfile by a non-shell writer); push is the integrator's; the tree lanes admit you on `deliverables/0.7.0_AE_CloudOps~Z/**`, `task-orders/` for your own status flip, `surprise-channel/investigations/`, `cards/`.

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> @bff1f8d012 (v0.1), cell OP-s-3 (s.1a; manifest row S3; ROUND 1 first).
<owned_cells>OP-s-3</owned_cells>
Read-dependencies, NOT claimed: OP-s-1 and OP-s-2 (the consumers; their TOs follow on this seat), OP-s-21 (the coverage-bound text the sentinel carries until this cell is DONE), OP-x-1 (the probe word S3-AC5 waits on).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 20 gates armed over 5 carriers (C1 21 -> 5, C2 3 -> 3, C3 12 -> 12, C4 20 SEMI-DECIDABLE -> 0, C5 337 NOT-DECIDABLE -> 0); 0 gates name NFRA_OPSEC202609, the origin secret, CloudFront or the auth handler; G-15 (the alert/monitor moratorium) binds and this cell builds no monitor; read 2026-09-03 06:5xZ at the issuer's seat.
comp-iam: RUN -- DESIRED plane only (401 .tf files in 3 trees; 369 policy blocks attached, 24 NOT ATTACHED, 2 Deny statements unparsed); BLIND ON THIS SUBJECT: the auth handler is NOT a comp-iam service (0 matches in the 753-line services census), so the handler's and the authorizer's new `secretsmanager:GetSecretValue` on the new secret is grounded on live `simulate-principal-policy` (one `--resource-arns` per call, the positive control a separate invocation) at the worker's seat, and the cross-firm Deny belt is checked not to swallow it.
comp-adversary: RUN -- rc 0 at read-vintage @e10633f8b7 (2026-09-03T07:33:36Z); 4 commits, 8 repo paths, 0 file:line cites, 7 tool mentions; cited commits 4 attempted / 4 verified / 0 UNVERIFIABLE; cited paths 8 attempted / 7 stable / 1 flagged (the one flagged path is the proof instance this TO CREATES -- GONE at read-vintage, expected).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S3-AC1`..`S3-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~Z/NFRA_OPSEC202609.TO-OP-S-3.origin-secret-both-gateways.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the assignee commits itself (tree task-orders/** is lane ANY for the worker's own status flip). S3-AC1's value-absence census and S3-AC2's origin denominator are the controls that must be able to FAIL; S3-AC5 carries `UNCOMPUTABLE-BY-CONSTRUCTION` + `status_reason` while OP-x-1 is HELD, never a PASS on an un-run probe. Every `surprises` entry opens with a row id that resolves in the project's channel (the SURPRISES limb refuses the flip otherwise).
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">
    <step><run>comp-read infra/aws/terraform/portal-auth/cloudfront-distribution.tf --for "which origins front 7k3ed8px20 and f61h681z9g, whether any custom_header exists on them today, and what the import bound at line 5 requires"</run><expect>the origin blocks for both gateways located by line; the 0-diff bound quoted; 0 custom_header blocks today (or the ones present listed)</expect><if_mismatch>STOP; a custom header already present is a spec-vs-world row before any edit</if_mismatch></step>
    <step><run>comp-read infra/aws/opalinvest_dev/lambda/auth-handler/src/index.ts --for "where an incoming request's headers are first read and where a 403 refusal is returned today"</run><expect>the entry handler and the refusal shape located; the `/auth/*` check has one place to land</expect><if_mismatch>STOP; surface the ambiguity to the issuer as a row</if_mismatch></step>
    <step><run>comp-blast auth-validator-edge</run><expect>the consumers of the edge's injected headers enumerated; no consumer reads `X-Origin-Verify` today (the brief's zero re-measured)</expect><if_mismatch>STOP; a consumer of the constant header means the supersession is not safe -- row, then the issuer</if_mismatch></step>
    <step><run>aws iam simulate-principal-policy --policy-source-arn <auth-handler role> --action-names secretsmanager:GetSecretValue --resource-arns <the new secret's ARN> (ONE arn; positive control = the JWT public-key secret in a SEPARATE invocation)</run><expect>allowed on the new secret after the grant; the positive control allowed; the cross-firm belt's Deny does not fire on it</expect><if_mismatch>STOP; fix the grant, never the belt</if_mismatch></step>
  </phase>
  <phase id="2" when="before commit">
    <step><run>.tools/commit-gate.sh on every .py/.sh/.tf touched; bun/tsc on the handler and the authorizer; terraform plan (via the estate's wrapper) on portal-auth AND shared-infra/apigateway-portal</run><expect>gates clean; the plan shows ONLY the secret, the origin header and the Lambda code-hash changes -- nothing else in the diff</expect><if_mismatch>STOP; an unrelated change riding this apply is refused by NEVER-2's spirit and the `:5` bound</if_mismatch></step>
  </phase>
  <phase id="3" when="after commit">
    <step><run>aws cloudfront get-distribution-config --id EVTSA9VEHNZVH; aws lambda get-function-configuration on both functions; terraform plan re-run</run><expect>header present on the fronting origins (denominator printed); CodeSha256 == built; plan 0-diff</expect><if_mismatch>ROLL BACK inside the ledger entry and escalate loud (NEVER-2); never leave it half-landed</if_mismatch></step>
  </phase>
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO~Z` (the sequencer; the L8 seat reads the record, not a message) with per-criterion evidence, the origin denominator, both CodeSha256 values before/after, the ledger entry id, and push state as MEASURED. GO = this TO + the dispatch message. On completion this seat's next TO is OP-s-5 (logging), already cut.
