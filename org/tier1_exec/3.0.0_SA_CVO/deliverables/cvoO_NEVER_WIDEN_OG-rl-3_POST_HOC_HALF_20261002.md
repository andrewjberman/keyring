# NEVER-WIDEN half, POST HOC -- NFRA_OPLGTW OG-rl-3, the /hx/teams release -- SIGNED (3.0.0_SA_CVO~O, 2026-10-02 ~20:4xZ)

**Asked:** `1.0.0_SA_CTO~O` msg 28721, ruling 4 of
`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round13.md` @fea5fbcdbf (PRD v1.6 C7 addendum). The release ran
on the CTO and COO halves only. This seat grades the LIVE release after the fact against the v1.6 addendum and the CTO's
blast radius (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261002_NFRA_OPLGTW_HX_TEAMS_RELEASE.md` @6b6bccb300,
section "Blast radius").

**VERDICT: SIGNED.** The live state is inside the blast radius on every key this seat could read. Guard N1 is attached for
future rotations, and the scope of this half is stated at the end.

## Independently measured (2026-10-02 ~20:2xZ-20:3xZ)

**Code, by content (rule 22a).**
- `3a7d6a7dc8` is an ancestor of `4231bd2ddc`.
- Census of `3a7d6a7dc8..4231bd2ddc` over `infra/aws/ec2/opal-gateway`: 6 files, +804/-3, in 2 commits by
  `0.9.0_WK_NFRA_OPLGTW~15`:
  - `app/teams_route.py` (new) and its test;
  - `config.py` +7 (two keys);
  - `server.py` +9 (one import and four `Route`s, all on `/hx/teams`);
  - `taxsma_workbook.py` (the refusal tuple gains the three `/hx` bearers: a tightening, Z-S41);
  - `deploy-to-ec2.sh` (the teams bearer read host-side; it REFUSES before extract on a failed or empty read).
- `mail_route.py` and `transcript_route.py` are NOT in the census.
- `.env` printf, parsed on both sides: 48 keys -> 50, +`TEAMS_BEARER` +`TEAMS_BEARER_LABELS`, 0 removed, 0 duplicates.

**Running bytes.** SSM read-only on `i-07dccb1615503ac99` (command `c5b44138-144f-44a0-b5f1-a8e1bdfded23`):
- md5 of `app/{teams_route,server,config,taxsma_workbook,mail_route,transcript_route}.py` equals the `4231bd2ddc` blobs
  on 6 of 6.
- Negative control: the 4 changed files differ from `3a7d6a7dc8`'s, and `teams_route` is absent there. The 2 unchanged
  routes are byte-equal on both pins.
- `opal-gateway` ActiveEnterTimestamp is 19:23:25Z (MainPID 572341).
- The live `.env` holds 50 keys, with `TEAMS_BEARER` exactly once. No value was read.

**Artifacts and rollback key.**
- S3 `opal-gateway-latest.tar.gz` and `opal-gateway-4231bd2ddc.tar.gz` have the same ETag (`90196691...`), and no newer
  key exists.
- `opal-gateway-3a7d6a7dc8.tar.gz` is present (ETag `e1e72015...`).
- `EC2_MANIFEST.json` `deployed_commit` = `4231bd2ddc...` and `previous_deployed_commit` = `3a7d6a7dc8...`.

**IAM.**
- `opal-gateway-role` inline `gateway-read-secrets-policy` has ONE statement, `secretsmanager:GetSecretValue`, over 4
  ARNs: transcripts bearer, mail bearer, principals rosters, and the fourth, `gateway/teams/bearer-93ZHiU`.

**Edge.** ALB 443 listener rule priority 35 forwards exactly 3 paths: `/hx/teams/*`, `/hx/transcripts/*`, `/hx/mail/*`.

**Live route probes** (https://mcp.opalinvest.dev, with a deliberately wrong bearer, so no Graph call and no send):

| probe | result |
|---|---|
| GET `/hx/teams/me` | 401 `unauthorized` |
| GET `/hx/teams/chats` | 401 `unauthorized` |
| POST `/hx/teams/chats/<id>/messages` | 401 `unauthorized` |
| POST `/hx/teams/channels/<t>/<c>/messages/<m>/replies` | 401 `unauthorized` |
| PUT `/hx/teams/me` | 405 |
| POST `/hx/teams/me` | 405 |
| DELETE on the chat-messages path | 405 |
| GET `/hx/teams/x` | 404 |
| POST `/hx/mail/messages` | 405 (`/hx/mail` stays GET-only) |
| POST `/hx/transcripts/x` | 404 |

**Code read against the v1.6 addendum, at `4231bd2ddc`.**
- The Graph allowlists are separate per verb and fail closed (`_graph`, `PathRefused`):
  - GET: 4 path shapes;
  - POST: exactly 2 (`/chats/{id}/messages` and the channel replies path).
- The token is always `get_token(MS_INGEST_IDENTITY)`, and no caller identity is read.
- The bearer is compared with `hmac.compare_digest`. A value that also equals any of the other six route bearers is
  refused (`_shared_elsewhere`).
- The POST body must be exactly `{"html": <non-empty str>}` under `MAX_HTML_BYTES`.
- The output is allow-by-key (`project_message`, `project_chat`).
- The audit carries the route, ids, counts and label, never the content.

## Finding -- the shared-value refusal is ONE-SIDED (latent, not live)

The teams route refuses a `TEAMS_BEARER` value that equals another route's bearer. `mail_route.match_bearer` and the
transcript route compare only their own bearer and refuse nothing shared. If a future rotation made `TEAMS_BEARER` equal
to `MAIL_BEARER` (or `TRANSCRIPT_BEARER`), the teams route would go 401 for its holder, but the mail route would ACCEPT
that holder: one bearer would then reach a second prefix, against C7 "one leaked bearer reaches one prefix".

Today the values are distinct. The issuer's ht.AC3 read 200 on `/hx/teams/me` and `/chats` with the live bearer, and
`match_bearer` returns a label only when the value is not shared. That 200 is the issuer's measurement (claim: held,
proof @e38009d297); this seat does not hold the bearer. The fix (the same tuple in `mail_route` and `transcript_route`)
is carried to the CTO for OG-rl-4's payload.

## Guard

- **N1 -- rotation.** Any rotation of `gateway/teams/bearer`, `gateway/mail/bearer` or `gateway/transcripts/bearer`
  re-runs ht.AC3's 200 arm on `/hx/teams` the same sitting. A 401 there means a shared value: roll the rotated secret
  back before anything else. N1 lapses when OG-rl-4 ships the symmetric refusal.

## Writers of the property ("what /hx/teams serves"): N = 4, 3 read

1. The deploy (app code and `.env`): read.
2. Terraform ALB rule 35: read.
3. Terraform IAM `gateway-read-secrets-policy`: read.
4. The Secrets Manager value of `gateway/teams/bearer`: NOT read by design, because a value read is a credential read.
   Its distinctness rests on ht.AC3 (above).

"Must not touch any other IAM statement or listener rule" rests on the issuer's targeted `safe-apply` read (0 added,
2 changed, 0 destroyed; claim: held). This seat read only the two named resources.

## What this half covers and does not

**Covers:** the live code, `.env` key set, IAM ARN and ALB paths of `4231bd2ddc`, against the v1.6 addendum. Both
branches of the rollback are named in the ruling, each standing alone:
- code: redeploy `3a7d6a7dc8` (artifact present). That also reverts Z-S41's tuple, which re-opens the latent Tax-route
  gap until OG-rl-4.
- IAM: revert the fourth ARN.
- ALB: revert to 2 values.

**Does NOT cover:**
- the two POST verbs' first real send (UNEXERCISED until Andrew's first End of Day post; a 502 with `graph_status` 403
  is a missing scope, a row to Andrew);
- the caller-side send approval (LDO-001, laptop);
- any rotation (N1);
- OG-rl-4.

-- 3.0.0_SA_CVO~O
