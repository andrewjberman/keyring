# NFRA_OPLGTW task order -- `OG-zs-1` -- APPLY: attach the edge auth validator to CloudFront behavior `/json-tiered/*` (row Z-S114, CTO ruling msg 34093)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-zs-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-zs-1</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-APPLIER at the act (`comp-schedule --drift`): no hold or moratorium may name CloudFront `EVTSA9VEHNZVH` or the portal-auth Terraform root; none is known at the cut.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change. The change attaches a Lambda@Edge function version that already serves the twin behavior (`auth-validator-edge:23`); CloudFront's existing service access to it is the twin's.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's ruling (msg 34093) on row NFRA_OPLGTW-Z-S114 (4.0.0_SA_CRO~Z @f5d2c93a6a). It NARROWS access; nothing is widened.
EGRESS CLASS, declared: NONE beyond Opal's own AWS and one unauthenticated HTTPS GET of opalinvest.dev (the proof).
</preflight>

## 1. THE CELL -- `OG-zs-1` (decomposition addendum R3-T.51, workstream ZS114-EDGE-AUTH)

CloudFront `EVTSA9VEHNZVH` (opalinvest.dev) serves `s3://opal-data-portal-v2/json-tiered/*` through the behavior
`/json-tiered/*` with NO Lambda@Edge association: an unauthenticated GET of
`https://opalinvest.dev/json-tiered/market-overview/rsi-summary.json` returns 200, while the twin
`/api/general/json-tiered/*` (viewer-request `auth-validator-edge:23`, origin-request `public-data-router:7`, origin-response
`cache-control-injector:2`) returns 401. The CTO ruled the bare path is a leftover, not a public path: the portal reads only
`/api/general/json-tiered/*` (`portal/src/api/endpoints/market.ts`). The tree holds 375 market-overview keys today; any key
written under `json-tiered/` later would be public the moment it lands.

1. **Read the traffic first.** Read 7 days of requests for the bare path `/json-tiered/*` on `EVTSA9VEHNZVH` (CloudFront
   standard logs or the distribution's metrics, whichever exists; name the source). If a consumer other than the portal
   shows up, STOP: file a BLOCKING row and message nothing else; the issuer takes it to the CTO. Write
   `W/ZS1_LOGREAD.json` = `{"window_days": 7, "source": "<named>", "requests_bare_path": N, "non_portal_consumers": 0}`.
2. **The change.** In `infra/aws/terraform/portal-auth/cloudfront-distribution.tf`, behavior 7 (`path_pattern = "/json-tiered/*"`)
   gains ONE `lambda_function_association` block: `event_type = "viewer-request"`, `lambda_arn = local.auth_validator_edge_arn`,
   `include_body = false` (the same reference behavior 6 uses). Do NOT delete the behavior: the default behavior would then
   serve the path. Read the code of `public-data-router` and `cache-control-injector` and add their associations ONLY if
   they are no-ops or harmless on the bare path; otherwise leave them off and say why in a row. The validator alone closes the hole.
3. **Plan, then stop on any surprise.** Run `terraform plan` for the portal-auth root directly (`safe-apply` gates `apply`
   only). The plan must read `0 to add, 1 to change, 0 to destroy`, and the one change is the distribution's behavior-7
   association list. Save it as `W/ZS1_PLAN.txt`. Any other change in the plan (drift from another applier) is a STOP and a
   BLOCKING row: never apply a plan that is wider than this cell.
4. **Apply as a deploy with a ledger.** Ledger `nfra-oplgtw-edge-auth-json-tiered`, entry AND sentinel first; `safe-apply`
   targeted at the distribution resource; wait for the distribution status `Deployed`. Rollback: remove the one association
   block and apply again.
5. **Prove it.** An unauthenticated GET of the bare path returns 401 (or 403 if the validator answers so; name it). The
   authenticated twin `/api/general/json-tiered/market-overview/rsi-summary.json` still returns 200 with a valid portal
   credential (name the source of the credential: a service account or the walker account; print no token). Write
   `W/ZS1_PROOF.json` = `{"bare_unauth_status": 401, "twin_authed_status": 200, "twin_auth_source": "<named>", "scanner_authorizer": "<what you read>"}`.
6. **Read the `/api/scoped/security-scanner/*` authorizer once** (API Gateway `7k3ed8px20`, behavior with no Lambda@Edge association): does the
   API route carry its own authorizer? Record the answer in `scanner_authorizer` in one sentence. Do not change it.
   If it carries none, file an OBSERVATION row; this order does not fix it.
7. Close the ledger, commit, run the criteria, report once.

## 2. BOUNDS

- ONE change: the one association on behavior 7. No other behavior, origin, cache policy or Lambda is touched; no object is
  written to any bucket; no key under `json-tiered/` is moved or deleted.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform apply`; apply a plan wider than the cell; print a
  credential.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/terraform/portal-auth/cloudfront-distribution.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-edge-auth-json-tiered.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-zs-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/zs1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)log read: window \d+ days, source named, non-portal consumers 0.*behavior /json-tiered/\* carries auth-validator-edge viewer-request: yes; twin associations 3 of 3.*plan 0 to add, 1 to change, 0 to destroy: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-zs-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/zs1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0.*live bare path unauthenticated: 40[13]; twin unauthenticated: 40[13].*proof file: bare 40[13], twin authenticated 200, scanner authorizer read yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the 7-day read shows no non-portal consumer, the Terraform carries the validator on behavior 7 beside an untouched twin, and the saved plan was exactly one change.
- `AC2`: the deploy closed, the bare path now refuses an unauthenticated read (the check performs it live), and the authenticated twin still serves.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-zs-1.json-tiered-edge-auth.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once to `2.0.0_SA_COO~O`.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream ZS114-EDGE-AUTH (decomposition addendum R3-T.51). PRD v3.2 ADMITTED (`prd-signoff.py status` read at the cut).
  A narrowing act inside the issuer's own decomposition on the CTO's ruling (msg 34093); no never-widen halves.
- Queue: staged until OG-hv-2 closes (CTO: "seat it with CloudOps after OG-hv-2"); the GO is the issuer's message citing this order.
- Pre-cut: zs1.AC1 and zs1.AC2 base FAIL as expected (the records are absent and the bare path returns 200).

<status>staged</status>
<round>37</round>
<workstream>ZS114-EDGE-AUTH</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
