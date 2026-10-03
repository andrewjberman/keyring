# CTO RULING 2026-10-02 ~17:4xZ -- NFRA_OPLGTW release OG-rl-3: the /hx/teams route, TODAY

**By:** 1.0.0_SA_CTO~O. **For:** 2.0.0_SA_COO~O (issuer). **Authority:** Andrew-direct (laptop 0.0.0_AB_MSTR bus
d38d682f, 17:17Z, relayed by 0.0.0_AB_MSTR~Z msg 28592), verbatim: "release the gateway /hx/teams route TODAY. Andrew's
first live End of Day post, 4:30-5:30 PM ET (20:30-21:30Z), depends on it." Request:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/SITEZ_GATEWAY_RELEASE_REQUEST_HX_TEAMS_20261002.md` @a53c8452b4.
Parked item: `org/missions/D9/NFRA/NFRA_OPLGTW/project.json` @09ba293969.

**Deadline:** live and read back before 20:30Z.

## Measured at ~17:3xZ (each read is repeatable)

| # | Read | Result | Consequence |
|---|---|---|---|
| M1 | `infra/aws/ec2/EC2_MANIFEST.json` services.opal-gateway | deployed_commit `3a7d6a7dc8` (OG-tr-1, 2026-10-01 18:50Z) | the release base |
| M2 | `git merge-base --is-ancestor 3a7d6a7dc8 HEAD` | NOT an ancestor | the live ref is a release-branch pin; resolve it by CONTENT |
| M3 | `git diff 3a7d6a7dc8 HEAD -- infra/aws/ec2/opal-gateway/app` | 7 files; besides db92656c72's hunks, HEAD DROPS live behaviour: `schwab/integration.py` loses `aws_roles.environ_with_external_ids(...)`, `aws_roles.py` differs by 40 lines, `admin_refusals.py` differs | a release cut from CLOUD HEAD REGRESSES the live gateway. **Refused.** |
| M4 | `aws elbv2 describe-rules` on the opal-gateway :443 listener | priority 35 = `/hx/transcripts/*`, `/hx/mail/*` | 8e6872f265's `/hx/teams/*` is DESIRED, not APPLIED |
| M5 | `iam simulate-principal-policy` opal-gateway-role, GetSecretValue, `gateway/teams/bearer-93ZHiU` | **implicitDeny** (positive control `gateway/mail/bearer`: allowed) | the host cannot read the bearer |
| M6 | `git show 3a7d6a7dc8:infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` | the `.env` is one fixed `printf`; no `TEAMS_BEARER` key | a host-edited `.env` line dies at the next deploy; the key must ride the script |

## The release (ONE order; the Phase A shape of OG-rl-2 and OG-tr-1)

1. **Code:** the release branch = live `3a7d6a7dc8` + db92656c72's five files merged onto the LIVE bytes:
   `app/teams_route.py` (new), `tests/test_teams_route.py` (new), and only db92656c72's hunks in `app/config.py`,
   `app/server.py` and `app/taxsma_workbook.py` (Z-S41). Nothing else from CLOUD moves.
2. **deploy-to-ec2.sh** (on the release branch): fetch `gateway/teams/bearer` host-side exactly like `MAIL_BEARER`
   (refuse on failure or empty), and add `TEAMS_BEARER=%s` and `TEAMS_BEARER_LABELS=teamsassist` to the `.env` printf.
   The key count goes up by 2.
3. **IAM:** `infra/aws/terraform/opal-gateway/gateway-read-secrets.tf` gains a fourth data source and ARN for
   `gateway/teams/bearer`. Same statement, same action, no wildcard.
4. **ALB:** apply 8e6872f265's `hx-capability.tf` value (rule 35 gains `/hx/teams/*`).
5. Steps 3 and 4 go through ONE `safe-apply` on the opal-gateway root. The plan must show exactly those two in-place
   changes. Any other diff in that plan is NOT applied here: `-target` the two resources and file a row for the rest.
6. **Order:** steps 3 and 4 first, then the deploy with `DEPLOY_BASE_REF=3a7d6a7dc8`, then the reads.

## Acceptance (mechanical; the issuer runs each)

- **AC1:** the step 3 and step 4 reads give opposite answers for the bearer and the paths:
  - `simulate-principal-policy` on `gateway/teams/bearer` is **allowed**;
  - a sibling `gateway/*` secret still reads **implicitDeny**;
  - rule 35 lists 3 path values.
- **AC2:** after the deploy, `GET https://mcp.opalinvest.dev/hx/teams/x` with no bearer is refused BY THE APP (401 or
  404, no redirect), while `GET /` still 302s.
- **AC3:** with the bearer, `GET /hx/teams/me` and `GET /hx/teams/chats` return 200.
  - A 502 carrying `graph_status` 403 means a missing Graph scope on MS_INGEST_IDENTITY. That is a BLOCKING row to
    Andrew, not a code fix.
- **AC4:** the regression floor. After the release, `/hx/mail/x` and `/hx/transcripts/x` still answer 401 from the
  app, and the Tax workbook route answers as it did on `3a7d6a7dc8`.
- **NOT graded here:** the two POST verbs (Chat.ReadWrite and ChannelMessage.Send). They are proven only by a real
  send, so Andrew's first EOD post is their exercise; the scopes stay UNEXERCISED until then.

## Blast radius (the CTO half of the never-widen sign-off)

- **May touch:**
  - the opal-gateway host code and `.env`;
  - `gateway-read-secrets-policy` (adds one ARN);
  - ALB rule 35 (adds one path).
- **Must not touch:** any other route's behaviour (AC4), any other IAM statement, any other listener rule.
- **Rollback per key:**
  - code: redeploy `3a7d6a7dc8` with the same base guard;
  - IAM: revert the fourth ARN;
  - ALB: revert to 2 values.
- Each rollback stands alone.
- `EC2_MANIFEST.json` `deployed_commit` moves to the release head in the same order.
