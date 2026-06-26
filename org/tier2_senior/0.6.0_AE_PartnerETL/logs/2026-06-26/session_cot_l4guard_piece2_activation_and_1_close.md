# Session Log -- ADVI_COTETL.L4-GUARD PIECE-2 activation + #1 served-AUA close

**Agent:** 0.6.0_AE_PartnerETL
**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, VALIDATE, COORDINATE
**Date:** 2026-06-26
**Window:** continues session_cot_l4guard_detection_and_unfreeze.md -> through PIECE-2 e2e + activation + #1 oracle close.

## Summary

Delivered the cot silent-re-freeze guard end-to-end. Two freeze-modes now durably covered:
- **#1 auth/data freeze (served AUA)**: CLOSED. Served firm-AUA data_as_of advanced 06-22 -> 06-25
  (priced frontier) and both oracle alarms cleared ALARM->OK on their own.
- **PIECE-2 auth-lapse (durable gateway self-fetch)**: ACTIVATED. The cot 02:00 session-fetch is
  re-pointed off the MFA-failing cot_bd_session_fetch.py onto the canonical gateway-self-fetch
  auto-login (the box self-fetches the OTP via the OPLMCP gateway, zero live-agent).

## What landed (this window)

1. **PIECE-2 Delta-2 IAM** -- cot-exporter-ec2-role + CotOtpGatewayTokenRead (GetSecretValue on
   blackdiamond/cot/otp-gateway-token-*, read-only, cot-scoped). commit 9992f3523. Firm-sep Deny-bd
   belt verified LIVE through the modify (get-role-policy). Ledger 20260626T1428Z closed 3/3.
2. **PIECE-2 box stage** -- /opt/bd-cot-auto-login/ secret-ids.env relay->gateway + self-locating
   APP_DIR wrapper (root fix for the fork-shadow: the hardcoded /opt/bd-49f-auto-login does not
   exist on the cot box). Repo infra/aws/ec2/bd-cot-auto-login/ (commit 3f9b43897), S3-staged,
   pulled to box. Ledger 20260626T1444Z closed 3/3.
3. **#1 un-freeze chain-fire** -- 0.7.0 backfilled bronze holdings 06-23/24/25 (pricing-lag fix);
   I converted silver holdings (3 dates, 11279 rows ea, SSM 66d57a5b) + fired full gold (SSM
   1855a971, CHAIN COMPLETE exit 0: B_00 --force-recent-days 14 -> C_04 PASS=1/FAIL=0 -> C_03 ->
   D_00b -> served). Served data_as_of 06-22 -> 06-25, 4-way content-verified (me + 0.7.0 x2 + COO).
   Oracle: bd-cot-served-aua-stale + bd-cot-silver-stale-holdings ALARM->OK on their own at ~15min.
4. **PIECE-2 item-2 e2e (CVO 6-clause)** -- box .js synced to canonical 28dd27a0 (diff-capture
   passed, no box-only fix lost) + BD_OTP_WINDOW_SECONDS=120 (CTO-A). Captured live:
   - happy-path (SSM cb9deea5, rc=0): gateway self-fetch, device-trust captured, relay 8f4c898c
     UNCHANGED (zero-agent), session advanced, keepalive 204.
   - 6a out-of-window reject (SSM 3b7fdfa7): window=1 -> {code:null} vs window=99999 -> code exists.
   - 6b collision = code-path attestation (0.7.0; real injection infeasible).
   - 6c self-heal: dead session -> keepalive 403 + dead-cookie SNS (alerted:true) [LOUD captured] ->
     clean gateway self-fetch recovery (SSM 14d26a08, rc=0) -> keepalive 204 [recovered]; CVO-mandated
     restore-on-failure guard armed (validated backup pre-invalidate; recovery succeeded so unused).
   CVO VERDICT = SOUND (155721Z, all 6 clauses independently grounded vs live+source).
5. **PIECE-2 ACTIVATION re-point** -- opal-cot-bd-session-fetch SSM doc runCommand off
   cot_bd_session_fetch.py -> ./run-bd-auto-login.sh. commit daa38655c, safe-apply -target 0/1/0,
   0-diff verified, LIVE doc content = wrapper (get-document), keepalive 204. Ledger 20260626T1607Z
   closed 3/3. Tag cot-pipeline-v0.6.0. Doc name unchanged -> event-driven chain preserved.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| comp-iam (get-role-policy fallback) | firm-sep Deny-bd verify on freshly-modified role | PASS (census stale, live get-role-policy authoritative) |
| terraform plan -target | 0-diff verify on Delta-2 + re-point | PASS (No changes post-apply, both) |
| deploy_ledger.py | 3 ledgers open+close in-session (1428Z/1444Z/1607Z) | PASS (all closed 3/3, NEVER-law) |

What worked: get-document against LIVE to verify the re-point (not self-report). What failed: SSM
PIECE-1 6c phase-1 hit sh-vs-bash + echo-paren syntax errors (Failed fast); recovered via $?-not-
PIPESTATUS + paren-free echoes, and the session-invalidate left the cot session dead briefly ->
restore guard + immediate clean recovery healed it. Gap found: comp-rail gated a `git diff | grep`
on .tf (own-change verification) -- used git diff --stat instead (no comp-tool fits an uncommitted
working-tree diff).

## Deployment Sequence + Verification (AE)

- code -> commit (9992f3523 / 3f9b43897 / daa38655c) -> push -> safe-apply -target -> 0-diff -> ledger close -> tag.
- LIVE verify (paste): get-document opal-cot-bd-session-fetch content = `run-bd-auto-login.sh`
  (NOT cot_bd_session_fetch.py); bd-cot-keepalive = `{"ok": true, "status": 204}`; served
  timeseries_overview.json data_as_of = `2026-06-25`, generated_at this-run, AUA $401.4M real.

## Blockers

None. Shared-working-tree commit collision (0.7.0's cot_backfill_holdings_net WIP in the same
ssm.tf) was RESOLVED by 0.7.0 yielding (removed their block) -- not a blocker, a coordination step.

## Current State

- cot 02:00 session-fetch: LIVE on the gateway self-fetch auto-login (opal-cot-bd-session-fetch ->
  run-bd-auto-login.sh -> node bd_49f_auto_login.js, BD_OTP_ADAPTER=gateway, WINDOW_SECONDS=120).
- cot session blackdiamond/cot/session: fresh, gateway-minted, keepalive 204.
- Served cot firm-AUA: data_as_of=06-25, oracle alarms OK.
- Box i-0643a5bee8a8feabf: running; /opt/bd-cot-auto-login/ = canonical .js 28dd27a0 + gateway env.
- PIECE-1 detection (v0.5.1): COMPLETE, live. Tag cot-pipeline-v0.6.0 = PIECE-2 activation.
- 0.7.0's iam.tf CotDetectionSnsPublish + cot_backfill_holdings_net = their uncommitted WIP (their
  atomic CTO-gated retry-net deploy, separate) -- I never touched them.

## Next Steps

- **[2.0.0_SA_COO]** hand-confirm the activation with CTO (chain intact off the new doc) = formal PIECE-2 CLOSED.
- **[0.6.0_AE_PartnerETL]** verify the 02:00 nightly by CONTENT tomorrow (keepalive 204 + session fresh
  + freshness-probe) -- the canonical first-production-run validation (NEVER#4); loud-if-fails via PIECE-1.
- **[0.6.0_AE_PartnerETL]** CTO-B in-run retry = fast-follow: build the outer-retry (pre-approved shape,
  design ADVI_COTETL.L4-GUARD.ctoB-retry-design.md 74f91e239), RAVC CTO the shared-.js diff + loop 0.7.0 (49F blast).
- **[0.7.0_AE_CloudOps]** re-add cot_backfill_holdings_net + run the atomic CTO-gated retry-net deploy.
- **[follow-on]** OFC office-breakdown empty (missing office_mapping CSV) -- pre-existing, OFC-view only, COO-logged separate.
