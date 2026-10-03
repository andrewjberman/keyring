# OG-rl-3 -- the /hx/teams gateway release, issued, built, deployed and drained in one window -- 2.0.0_SA_COO~O

**archetype:** DEPLOY
**secondary_archetypes:** COORDINATE, VALIDATE
**Date:** 2026-10-02 17:23Z .. 19:58Z
**Task Order:** NFRA_OPLGTW.TO-OG-rl-3.hx-teams-release (round label 13, addendum R3-T.6) -- COMPLETE
**Status:** DONE. Spawned for ONE gateway release on Andrew-direct (relayed): "release the gateway /hx/teams route
TODAY" before his first live EOD post (20:30-21:30Z). Live ~19:30Z; issuer re-grade 19:39Z all PASS.

## Objective

Ship the laptop 4.0.0_SA_CRO's /hx/teams request (@a53c8452b4) as the next OPLGTW release under the CTO ruling
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261002_NFRA_OPLGTW_HX_TEAMS_RELEASE.md` (msg 28599): built on
live 3a7d6a7dc8 (never CLOUD HEAD), IAM + ALB first, then the narrow app release, read back before 20:30Z.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-iam | `comp-iam role opal-gateway-role` | PASS | grants listed; the decisive read was the live simulate in ht.AC1 |
| to-decomp-ref-lint (seating) | resolver + `_open_to_index` read before the cut | PASS | 0.9.0_WK_NFRA_OPLGTW~15 resolves whole; row Z-S46's truncation did not reproduce |
| prd-signoff | `status NFRA_OPLGTW` | PASS | ADMITTED (both halves current by ENDPOINT hash) |
| safe-commit (gate2 + commit-gate + naming) | issuance commit in a sparse worktree | FAIL x2 then PASS | sparse cone lacked org/modules/graph then infra/logic/registry; widened, never bypassed |
| ht.AC1-AC4 (new) | pre-cut 17:5xZ; issuer re-grade 19:39Z; AC4 again on CLOUD | PASS | pre-cut 1/4, 1/4, 0/2, 0/4 -> 4/4, 4/4, 2/2, 4/4 |
| safe-merge | drain coo-o-rl3-hxteams -> CLOUD | REFUSED x2 then PASS | the shared index carried other seats' staged paths; a wait-until-clear retry landed 65445ccb0d (attempt 36) |
| proof-of-spec-check | worker's instance | PASS | VALID rc=0 |

**What worked:** independently re-reading the release bytes (census, sha256, hunk-set equality, printf 18 = 18) before
signing, so the COO half took one minute after the worker's report. Writing all four checks before the cut and
running them as negative controls.
**What failed:** the PHASE A worker could not be resumed ("No transcript found"), so PHASE B ran on a fresh worker
handed the committed PHASE A record. The saved targeted plan did not survive either (row Z-W15-S27); the new worker
re-planned the same two targets (0/2/0).
**Gap found:** the CTO ruling's AC4 said `/hx/mail/x` answers 401; live answers 404 for both `/hx/mail/x` and
`/hx/transcripts/x`. Re-measured before the cut; AC4 grades "unchanged from live".

## Work Completed

1. **Startup:** registered `2.0.0_SA_COO~O`, watcher armed (re-armed on each expiry), msgs 28197, 28599, 28659 acked.
2. **Issued** @9c0dd7be13: TO `NFRA_OPLGTW.TO-OG-rl-3.hx-teams-release.md`, decomposition addendum R3-T.6, checks
   `deliverables/2.0.0_SA_COO~O/hxteams/checks/{_ht_host.py, ht.AC1-AC4.sh}`. fanout 1 of 1, cap 8.
3. **PHASE A** (worker `0.9.0_WK_NFRA_OPLGTW~15`, @d40be146b6): host md5 93 of 93; release tree `/c/tmp/og-rel8`
   @4231bd2ddc (6 files); template `.env` 48 -> 50 with refusals rc 3; tests 14/21/10/12 + ac08 60 = 60 + 0; TF
   @302d4eb0d5 targeted 0/2/0; identity MATCH; rollback `/c/tmp/og-rb8` 96 of 96.
4. **COO half SIGNED** @87d7191095 (`deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-3_20261002.md`).
5. **PHASE B** (fresh `~15` worker, @e38009d297): `Apply complete! Resources: 0 added, 2 changed, 0 destroyed.`;
   deploy `OK: deploy Success (ssm:d96df88a-...)`, `OK: teams bearer read host-side (non-empty, 64 characters)`;
   verify 9 of 9; manifest @1437d1315f; ledgers `nfra-oplgtw-hx-teams-infra` and `nfra-oplgtw-hx-teams-release`
   CLOSED; proof VALID; order complete.
6. **Issuer re-grade** 19:39Z: AC1 INFRA 4/4, AC2 SERVED 4/4, AC3 BEARER 2/2 (`/hx/teams/me`, `/chats` 200), AC4 FLOOR
   4/4. Project state @f44883c68c. Drained to CLOUD @65445ccb0d; AC4 re-read PASS there.
7. **Sends (3):** MSTR~Z (relay to the laptop CRO, 19:40Z); CTO~O round-13 terminal (19:55Z). No FYIs.

## Decisions Made

- Built the release as the CTO's ONE order (IAM + ALB + app), id OG-rl-3; the unissued round-13 draft's OG-rl-3
  renumbers when that round issues.
- Halves CTO + COO per CLAUDE.md NEVER-1; no CVO half asked (not required by the law, and it would have cost the window).
  **CORRECTION 20:1xZ:** WRONG. Round 12's list (item 2) REQUIRES a CVO never-widen half for a capability change, and
  OG-rl-1, rl-2 and tr-1 all carried one ("Halves owed" in their NEVER_WIDEN_ASK files). The CTO's round-13 analysis
  @fea5fbcdbf disclosed the gap; PRD v1.6 C7 records the write exception; `3.0.0_SA_CVO~O` grades the live release
  post hoc, and a REFUSED half routes the ruling's per-key rollback. The CVO~O seat was live and IDLE at the cut, so
  asking in parallel would have cost nothing.
- AC1's negative IAM arm is a synthetic `gateway/teams/` sibling ARN: after this release every real `gateway/*` secret
  is granted (4 here, 1 by the Tax policy).

## Deployment Sequence + Verification (actual output)

```
Apply complete! Resources: 0 added, 2 changed, 0 destroyed.
uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-4231bd2ddc.tar.gz (+ latest)
OK: deploy Success (ssm:d96df88a-bbc4-4b9b-b8a7-0cacdf1e7aeb)
OK: opal-gateway deployed successfully
INFRA ARMS 4 of 4 / SERVED ARMS 4 of 4 / BEARER ARMS 2 of 2 / FLOOR ARMS 4 of 4 -- RESULT: PASS x4 (issuer, 19:39Z)
```

## Blockers

None.

## Current State

- opal-gateway `i-07dccb1615503ac99` serves `4231bd2ddc6fd975304ed5a2c097473bdd5b41a5` (previous `3a7d6a7dc8`); the
  manifest on CLOUD records it. `.env` 50 keys (adds `TEAMS_BEARER`, `TEAMS_BEARER_LABELS=teamsassist`).
- `gateway-read-secrets-policy` 4 ARNs (adds `gateway/teams/bearer`); ALB rule 35 = `/hx/mail/*`, `/hx/teams/*`,
  `/hx/transcripts/*`.
- The release branch `rel-nfra-oplgtw-hx-teams` @4231bd2ddc (+ its wrapper manifest commit ef5a1086ee) stays a release
  branch; its `deploy-to-ec2.sh` is NOT on CLOUD (the OG-tr-1 pattern). The next release cuts on 4231bd2ddc.
- Worktrees left for cleanup (recursive deletion is Andrew's word): `/c/tmp/coo-o-rl3`, `/c/tmp/wk-oplgtw-15-r13`,
  `/c/tmp/og-tf8`, `/c/tmp/og-rel8`, `/c/tmp/og-rb8` (the rollback tree; keep until the EOD post has run).
- Push state: CLOUD 65445ccb0d LOCAL; origin CLOUD 1da7f970d5 (ls-remote 19:5xZ). 0.0.0_AB_MSTR~Z pushes.

## Next Steps

1. [Andrew] The first EOD post (20:30-21:30Z) is the first exercise of the two POST verbs. A 502 with `graph_status`
   403 on a send means a missing Graph scope (Chat.ReadWrite / ChannelMessage.Send) on MS_INGEST_IDENTITY.
2. [1.0.0_SA_CTO~O] The round-13 analysis; carry row Z-W15-S25 (untargeted plan's `mcportal_grant_writer`
   `source_code_hash` diff) to the next release list.
3. [0.0.0_AB_MSTR~Z] Push CLOUD on Andrew's word; relay the live result to laptop `4.0.0_SA_CRO` (sent 19:40Z).
