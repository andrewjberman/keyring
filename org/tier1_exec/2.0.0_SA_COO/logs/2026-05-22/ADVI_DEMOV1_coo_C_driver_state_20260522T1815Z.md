# COO~C Session Log — ADVI_DEMOV1 Driver — State Snapshot

- **Agent:** 2.0.0_SA_COO~C
- **UTC:** 2026-05-22T18:15Z
- **Supersedes:** the 17:18Z snapshot.
- **Scope lock:** ADVI_DEMOV1 only.

## This turn — TO-1 closed, TO-3 GO'd (scoped), DE-lane gap surfaced

### TO-1 (infra) CLOSED — RAVC2-accepted

AE~C delivered the TO-1 RAVC2. Evidence empirically verified by COO~C (not
self-report alone):

- **Commits** (all confirmed ancestors of origin/CLOUD): `16fd50aa6` source
  (s3.tf +96 / firm-config.mjs +9 / firm-routing.spec.mjs +7), `1941ec3e5`
  edge artifacts + lambda-source-map.json, `713d99116` shared-infra
  record-deploy + CHANGELOG, `380fb6ab6` portal-auth record-deploy + CHANGELOG,
  `7bfd8bd46` session log.
- **Tags:** `shared-infra-v1.16.0` @713d99116, `portal-auth-v1.16.0` @380fb6ab6 — both verified.
- **Terraform 0-diff:** shared-infra 5-added -> "No changes."; portal-auth
  two-stage edge apply -> "No changes."
- **AWS state (COO~C independent check):** `opal-data-demo` bucket EXISTS
  us-east-1, versioning Enabled, AES256, public-access-block all-true; bucket
  policy live with both statements (AllowCloudFrontOACReadPlatinum w/
  EVTSA9VEHNZVH SourceArn + AllowScopedAdvisorOAI w/ OAI E139998VWH0PD).
- **Criterion 3:** no iam.tf edit — the `partners-lambda-role` ReadPartnerBuckets
  `opal-data-*` wildcard already covers opal-data-demo; comp-iam gaps 0 NEW.
  COO~C concurred (criterion end-state satisfied by existing infra).
- **Criterion 8 — acceptance flex** pre-flagged to 1.0.0_SA_CTO (18:10Z): the
  comp-routes trace confirms CF -> shared-advisor-router but cannot represent
  the runtime origin-mutation leg to opal-data-demo (FIRM_CONFIG data, not a
  static route edge). Substituted verification: firm-routing.spec.mjs 8/8 in
  the build gate (asserts the deployed handler's origin.s3.domainName =
  opal-data-demo) + the AWS-state check above — strictly stronger than a static
  trace. Closeout triple cited verbatim in the TO comment.

TO-1 `<status>` flipped to complete (closeout comment with full evidence).
RAVC2-accept relayed to AE~C.

### TO-3 (firm + user registration) GO'd — SCOPED to the DS lane

Gate met (TO-1 + TO-2 both closed). GO issued to DS~C, but scoped:

- **DS~C executes NOW:** the DynamoDB `FIRM#demo` record (s3Bucket=opal-data-demo)
  + the demo Cognito user (criteria 1, 2, partial 4, 9).
- **HELD pending a DE lane:** the portal items — `ROUTER_FIRM_SUFFIX` in
  advisor-intelligence.ts, `firmAccess.ts FIRM_ALLOWED_PATHS['demo']`,
  `_partners/demo/` tenant-layout dir. All three are `portal/**` =
  `POD_DE_ANY`-laned; no DE is in the ~C team. (TO-3's own context already
  carved firmAccess.ts + _partners/demo/; the ROUTER_FIRM_SUFFIX item was
  authored as DS scope but is equally portal/DE-laned — carved here too.)

### DE-lane resourcing gap — surfaced to CTO

ADVI_DEMOV1 needs a DE for TO-3's portal items. The ~C team Andrew launched is
COO~C + DS~C + AE~C — no DE. TO-3 criteria 3/6/7/8 + the end-to-end demo-login
verification cannot close without the DE work. Surfaced to 1.0.0_SA_CTO with
the recommendation to stand up a DE~C lane or assign the base Pod-4 DE.

## ADVI_DEMOV1 standing

| TO | Phase | Owner | State |
|----|-------|-------|-------|
| TO-0 | probe | DS~C | CLOSED — RAVC2-accepted |
| TO-1 | infra | AE~C | CLOSED — RAVC2-accepted, 10/10 ACs, bucket+routing live |
| TO-2 | transform engine | DS~C | CLOSED — RAVC2-accepted |
| TO-3 | firm + user registration | DS~C | **PENDING — GO'd scoped (DS-lane); portal items held for DE** |
| TO-4 | run + PII-leak scan | DS~C | staged; GO gate = TO-3 (demo bucket now live) |

**Critical path:** TO-3 DS-scope -> TO-4. The DE-lane items run as a parallel
track (gate TO-3 full close + the demo-login check) once a DE is resourced.

## Side finding (out of ~C scope — routed)

AE~C's Phase-2 comp-iam gaps flagged 2 PRE-EXISTING IAM gaps on
`mdpf-daily-trigger` (mdpf-pipeline; predates ADVI_DEMOV1). Routed to base COO
as an FYI — candidate for a separate mdpf-pipeline IAM TO.

## Next events (driver mode)

1. DS~C executes TO-3 DS-scope (DynamoDB FIRM#demo + Cognito user) -> RAVC2.
2. CTO responds on the DE-lane gap -> resource the portal track.
3. On TO-3 DS-scope RAVC2: GO TO-4 (transform run can proceed — bucket live).
4. /loop ADVI_DEMOV1 persistent until project close.

## Notes

- Andrew Q1 / Q2 still open — non-blocking.
- COO~C commits under the base `2.0.0_SA_COO` serial (owned-paths).
