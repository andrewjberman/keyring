# Session log — 0.7.0_AE_CloudOps — 2026-06-02

AE_CloudOps lane (ws fabric). Andrew-direct parallel-velocity on ADVI_INFPRM (2nd PROD
promotion) + ADVI_INFNNA. Startup: /watcher self-heal -> /cloud-ops one-shot -> CronCreate /work
20m (dec2b98f). Discipline through-line: verify-against-ground-truth (served artifact / decoded
token / source table) before claiming done — it caught 5 would-be false-closures this session.

## Deliverables (all shipped/accepted or correctly gated)

### ADVI_INFPRM.W2 — getClientsTab firmId-fallback (the ONE true backend bug, Symptom 2)
- CONFIRM-FIRST: verified the P0 bifurcation against live infra (static-S3 JWT-resolves via
  shared-advisor-router X-Firm-Id; opal-partners-data ?firmId=-only -> 400, no fallback).
- Fix (15d500737): JWT/authorizer-firmId fallback in BOTH ?firmId= gate blocks; fires only when
  ?firmId= absent; is_authorized() still gates -> no cross-tenant leak.
- CAUGHT deploy-staleness: repo HEAD was ~92 lines ahead of live; a HEAD-deploy would have shipped
  the stranded INFLFE.005 Part A (closed-project tail, missing IAM). Escalated -> COO RULED (A)
  ISOLATE; built a live-base+W2-only artifact (deterministic Python zipfile swap; zip absent in
  Git Bash). Deployed partners-api-v1.16.2, safe-apply 0-diff, source-map, comp-iam no-gap.
- Verified live invoke T1-T5 + per-endpoint coverage (all ?firmId= routes self-scope, never 400).
- CVO SECURITY PASS (class-wide); RD~C FE rewire (8ff69f18 + 3753139e) consumed the contract I
  handed over (clients_tab <- getClientsTab, replacing the v10-emptied dashboard.json).
- Memory: feedback_pull_live_codesha_before_terraform_from_repo_lambda_deploy.

### ADVI_INFNNA.P2.W6.2 — NNA partition-completeness checker (durable W4 RIGID bar)
- New inf-nna-partition-checker Lambda (reused mdpf-freshness-checker pattern): reads served
  advisor_nna_canonical.json daily, asserts reconciliation.all_pass + deltas<=tol + coverage
  floors; PartitionCompletenessBreach metric -> alarm (treat_missing_data=breaching) -> ops SNS.
- Deployed inf-pipeline-v1.7.68 (9 resources, safe-apply 0-diff, least-priv IAM, source-mapped).
- Unit-verified (real=breach0; 3 synthetic faults breach=1) + AC8 synthetic-injection alarm PASS.
- CLOSED: CTO co-verify ACCEPT + CVO confirm (binds the exact DS-stamped properties).

### ADVI_INFPRM.W4a + W4-provisioning — admin access model
- Provisioned Peter firmRole=admin; confirmed edge admin-path (skips 004c); ownership_map N/A.
- CAUGHT the TABLE-SOURCE error: JWT identity claims mint from opal-partner-{firmId}
  (opal-partner-inflection), NOT opal-users-v2 (auth-only). Peter was already admin there since
  5/28; Joe-create needed the partner-table entry (created it). Prevented a Joe false-fail.
- Memory: reference_jwt_identity_claims_from_opal_partner_firmid_not_users_v2.
- Joe login LOOP: decoded a fresh Joe JWT -> advisorId=joe_brandenburg + firmId present -> edge
  :312 passes -> session holds. Loop was a pre-fix token. RESOLVED + proven.

### W4f — non-admin Distribution scope (Andrew ruling-b: NO tiering on Distribution)
- Analyzed: non-admin cross-advisor drill = 403 by edge .004a/.004c (own=200). Andrew ruled
  UNTIER Distribution (supersedes my rec-a/CTO RULING-a), keep Books admin-gated.
- Drove the security seam to ground truth + CAUGHT that relationship_stacked_periods embeds
  cleartext client display_names (CTO's trace had read it as roster-free) -> a naive L0 extract
  would leak rosters. FE pseudonymizes from client_key (display_name unused) -> safe split =
  DS strips display_name.
- CTO APPROVED the strip-split + LOCKED scope: named-path L0 exemption for
  ^/api/.../advisors/[^/]+/relationship_periods\.json$ ONLY (49F Lambda STAYS .004a-gated;
  bootstrap-L0 invariant; firm-containment on everything).
- Confirmed session-bootstrap hits only L0 firm/* paths (loop-class killed). Flagged 49F
  generality (pseudonymizer doesn't cover display_name) + filed P2 hardening (task #12).

## Open / gated at session end
- **Task #11 (edge untier Distribution): GATED** on DS emitting stripped relationship_periods.json
  (spec routed COO). Then: AE comp-pii (roster-free + re-id guard) + comp-routes -> CTO-approved
  edge diff -> HALTGT/safe-apply -> RD~C FE repoint -> CVO re-verify. Scope CTO-pre-approved in-shape.
- **Task #12 (P2): pseudonymizer.py extend to hash display_name** — tracked, not blocking, CTO-directed.
- **Andrew dual-login pixel-smoke** (Peter admin / Joe non-admin) on FRESH logins — external gate.
- 49F Distribution cross-drill product Q -> RD~C/COO.

## Deploys this session
partners-api-v1.16.2 (opal-partners-data W2), inf-pipeline-v1.7.68 (inf-nna-partition-checker).
DynamoDB: opal-partner-inflection joe@ create; opal-users-v2 Peter firmRole + Joe (auth) +
inert advisorId. All safe-apply/0-diff/comp-iam-clean where applicable.

## Memories saved
- feedback_pull_live_codesha_before_terraform_from_repo_lambda_deploy
- reference_jwt_identity_claims_from_opal_partner_firmid_not_users_v2

## Commit-cycle trail (work-cycle:0001-0012)
15d500737, e7f16a12b, 8c4a80b11 (W2) | 878fd6c8b, c080a8da2, ea64dd718, 844df40dd (W6.2) |
245a08d35 (coverage) | b3ae5720e (W4a) | 0df2b4afd, 486556175, 3b6b73656 (W4 provisioning + Joe
loop + table correction) | 92deebc30, 0435f026c, f6fa7939a (W4f analysis). Per-tick logs:
work_{1842,1905,1924,2000,2102,2117,2120,2128,2133}Z.md.
