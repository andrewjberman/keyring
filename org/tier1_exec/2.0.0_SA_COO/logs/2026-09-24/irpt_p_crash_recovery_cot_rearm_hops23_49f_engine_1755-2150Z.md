# 2.0.0_SA_COO~P -- crash recovery, COT re-arm, upload hops 2+3, 49F on our engine (17:55-21:50Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, DIAGNOSE, VALIDATE

Seat `2.0.0_SA_COO~P` (Claude, session eb36f7b2). Blast mode (closer, FAST lease `IRPT_BCKEND~P`), 20m goal loop
cron f599225b (C11: reads the lease each tick; the loop body ran continuously so no tick fired idle).
Goal: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_P_GOAL_PERFORMANCE_REPORTING_THREE_FIRMS_LOOP_20M.md`.

## Summary

1. Crash recovery (CTO 100730): A1 `_authz` log line = answer 4fffe13f01; A3 Y pin cherry-picked abb74dc689;
   A2 portal candidate 8 committed (771e4d2d), merged to origin/DEV 5e339ffd, orphan 814d7473 folded (237bdfda), handed
   to ~D (landed DEV 92d16efc); C1 `irpt-directory-bootstrap-20260923` closed SUPERSEDED aa3aabe2ca. N1 never-widen
   half not filed: the push had landed on Andrew's "Push it" and M's record covered P's key (msg 100812-ish to CTO).
2. COT live-thread defect: the one-use plan was SPENT 13:47:53Z and refused by our own `series window mismatch`
   check. Fixed dd1811bbaa (provider window inside the request -> actual dates), deployed NuIaCuqn.., ONE new plan armed
   99052771 on Andrew's second word (f0bd1c267e). Unspent at 21:4xZ; expires 2026-09-25T00:00Z.
3. Y's hop-3 blocker: M's viewer seam restored 19b38e2f22 (27/27 + 174). Upload hops 2+3 composed a58859baa7,
   grants 54bc1359f4, M's registry via cherry-pick 0e8b5da51b, Y 522afcfd17; resident f624e8a72f installed by SSM,
   irpt-ycharts-generate LdjdnnLh.. deployed. Upload contract a47102cc8f (+ on CLOUD aa21133b67).
4. 49F/INF named refusal (UNSUPPORTED_OPERATION) 7f6b5589f6 served l3NswChj.. (was INVALID_INPUT x10).
5. S125 directory-refresh re-dispatch fix 82679477a6 deployed d5fqVJ0f..; refresh.py then granted to ~M (CTO 100876),
   M's further fix DXuzx9jp superseded mine; my ledger closed SUPERSEDED.
6. 49F Performance on OUR GIPS engine (Andrew-direct @964fb4ed6b): f49_engine 94cf4cd61e (reuses the engine lane's
   parity_period_returns linker), retained composition 4573b3e3e3, contract provider OPAL_ENGINE (CLOUD 69cac32dce),
   grants + code 55b39f2d11 deployed YPSX1+nS.. 21:28:08Z. BD cross-check harness ed9ea1ba55: 300-sample, 244/293
   within 10bp, 286 within 100bp, 7 divergent (engine-lane findings, parked).
7. INF (Orion) design card 925835306a (mapping direct, JWT auto-refreshed, request grammar needs one live proof).

## Deployment Sequence + Verification (each under a NEVER-2 ledger, safe-apply, readback, 0-diff re-plan, recorder)

| Ledger | Act | Readback |
|---|---|---|
| irpt-performance-window-rearm-20260924 (4/5, S1 open) | adapter dd1811bbaa + plan 99052771 | CodeSha256 NuIaCuqn.. 18:46:42Z, egress 99052771, replan No changes |
| irpt-upload-hop2-20260924 (3/4, S1 = Y's live 12.03) | ycharts grants 0/2/0; resident SSM 10cde8d4; generate | resident active 19:43:01Z on /opt/irpt-resident/f624e8a72f; generate LdjdnnLh.. 19:49:52Z; invoke {} -> 200 CONTRACT_VERSION |
| irpt-directory-refresh-s125-20260924 (CLOSED, S1 SUPERSEDED by M) | refresh d5fqVJ0f.. | 20:13:37Z; then M DXuzx9jp 20:59:50Z |
| irpt-performance-named-unsupported-20260924 (CLOSED) | adapter l3NswChj.. | 20:26:37Z, plan unchanged |
| irpt-performance-49f-engine-20260924 (A1 closed, S1 open) | retained policy (engine read, 49F retention, LeadingKeys) + adapter YPSX1+nS.. | 21:28:08Z, egress 99052771 unchanged, replan No changes |

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| comp-find | 'smartx' --files; 'Reporting/Scope' | PARTIAL | slow (170s timeouts); banded output useful, the top band cut by my tail |
| drive-mode.py read/status | IRPT_BCKEND~P | PASS | lease FAST, extended by Andrew's presence to 21:55Z |
| deploy_ledger.py | 5 ledgers | PASS | open/close-leg/close; a sentinel never committed cannot be pathspec'd (commit the .md only) |
| build-and-upload.sh | performance x4, generate, directory-refresh | PASS/WARN | every performance build deletes tracked performance/*.py in the publish worktree (restored from HEAD; parked) |
| record-terraform-deploy.sh | 5 deploys | PASS | c67c4143e9, 174e39b4ad, ecd196e609, c9af24bdda, 25d91fb405 |
| safe-apply.sh | 6 applies | PASS | HALT_ACK=1; plans read before each |
| naming gate (safe-commit) | f49_engine, retained | FAIL->PASS | refused typed 'cottonwood' and 'opal-49f-gips-engine'; read through tenants/registry instead |

**What worked:** the census-by-S3-version pattern before every apply (exact member deltas), and reusing the engine
lane's linker as both the served code and the test oracle. **What failed:** comp-find latency; Bash rail aborts
whole calls. **Gap found:** the performance build's source_dir cleanup deletes tracked files (reproducible).

## MCP traffic

~30 messages. Significant: CTO 100730/100782/100796/100811/100817/100833/100876/100886 (orders, Andrew-directs);
Y 100823/100838/100842/100853/100858/100862/100870; M 100845/100855/100867/100871/100889; ~D 100835/100859/100880/
100882/100895. Sent: CTO x5 (N1 decision, re-arm ask, READY, 49F call, 49F served), Y/M/~D interface notices.

## Blockers

None BLOCKED. Waiting on Andrew's browser acts (COT S1 by 8 PM ET; a 49F account; Y's 12.03 upload).

## Current State

- Backend branch `irpt-smoke-p-backend-20260923` (worktree C:/Users/AndrewBerman/Desktop/irpt-smoke-p-backend-20260923)
  @ed9ea1ba55, LOCAL. Publish branch `irpt-p-publish-20260923` @25d91fb405, LOCAL. CLOUD commits: STATUS~P.md
  0252eeefca; contracts aa21133b67, 69cac32dce.
- Served: irpt-performance-adapter YPSX1+nS.. (COT bd_selected + 49F engine; INF UNSUPPORTED_OPERATION);
  irpt-ycharts-generate LdjdnnLh..; resident f624e8a72f; irpt-directory-refresh (M's DXuzx9jp).
- Armed: COT one-use plan 99052771 (acc_d486fc94.., 2026-01-01..2026-09-24, var-file in this session's scratchpad
  rearm.tfvars.json; a later apply WITHOUT it removes the plan env).
- STATUS: `org/missions/D9/IRPT/IRPT_BCKEND/STATUS~P.md`.

## Next Steps

1. [2.0.0_SA_COO~P] Read COT S1 when Andrew runs it (PERFORMANCE_USE#99052771 + PERFORMANCE_ACCEPTED#; adapter log);
   read 49F S1 on the first signed-in 49F request.
2. [2.0.0_SA_COO~P] INF (Orion): build per the card 925835306a; one live proof needs Andrew's per-use word or an
   Orion Performance-screen HAR.
3. [2.0.0_SA_COO~P] `f49_bd_crosscheck.py --all` (5309 accounts) when useful.
4. [1.0.0_SA_CTO] Route the 7 engine divergences (receipt F49_BD_CROSSCHECK_20260924.json) to the 49F engine lane.
5. [0.0.0_AB_MSTR] Drain/push both P branches and the CLOUD commits on Andrew's word.
