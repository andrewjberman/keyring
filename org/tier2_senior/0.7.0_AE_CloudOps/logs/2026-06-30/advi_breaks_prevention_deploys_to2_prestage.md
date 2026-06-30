# ADVI_BREAKS P0 -- inf un-freeze recovery + TO-6 prevention LIVE + TO-2 enforcer pre-stage

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE (runner-overrun grounding), IMPLEMENT (TO-2 module)

**Serial:** 0.7.0_AE_CloudOps (cross-firm general-infra; prevention/verification axis)
**Window:** 2026-06-30 09:49Z -> 19:40Z (since `eaf2bb179` diagnose-phase log)
**Project:** ADVI_BREAKS P0 (gate for DATA_ANALYTICS + DATA_SSOTMG)

## Summary

Drove the inf LIVE-break to RESOLVED + stood up the TO-6 prevention layer LIVE across firms +
pre-staged the TO-2 write-path enforcer to apply-ready. Net: inf GREEN, cot GREEN, 49F teed,
all-3-firms prevention on track. 18 commits, 4 safe-applies, all firm-isolated (NEVER#1-clean).

## Work done (sequence)

1. **inf un-freeze recovery** (`9c3c4b165`, `b9e1208ad`): root = pull_inflection_performance_rest.py
   hangs (Orion, no timeout, `set -e` blocks). Deployed ~A's durable timeout-tolerate
   (`9ea447b3a`, generalized to all REST pulls), killed the hung chain + cleared the orphaned
   dispatch-lock, re-fired clean. Served RICH 06-30 $202,125,678.08, data_as_of=06-30 (full
   un-freeze to TODAY, no T-1 residual), DLQ=0. Durable fix also hardens tonight's nightly.
2. **TO-6 item2d freeze-monitor LIVE** (`bb9684f0c`, `9882e30f9`): opal-globgrph-freeze-monitor,
   8 resources, hourly. Then **cot accept-lag retune** (`91efbd0ee`, `0b5de6455`): in-place
   Lambda update (7cb765fdd) -> cot DATA-AS-OF-FRONTIER-LAG accepts 2td (threshold 3); post-retune
   only 49F STOPPED-WRITER fires. First-publish PROVEN (`0611fa049`): boto3-pulled the
   `published=True ... fired=3` log-line past the CLI-v1 CW-Logs quirk; SNS delivered 6/6/8 to andrew@.
3. **TO-6 detection-4 value-parity readers**: inf LIVE + two-sided proven (`5c652feaf`,
   `79fe23ff1`; fire-on-stale $1.59M exit1 / quiet-on-fresh diff 0.0000) -- fixed a self-inflicted
   413 zip-bloat by relocating the root OUT of compdiff/. cot LIVE (`2665c5b33`->`33868112f`->
   `396fe456c`; served $432.46M == silver/holdings[06-26].market_value to the cent). 49F CERT-READY
   (`74d04407d`; anchor.sum==cert.gold_aua, NOT served=cert.certified_aua -- avoids the cot-pattern
   false-break; gap vars unset pending ~B/CVO).
4. **inf-gold-runner-overrun** (DIAGNOSE, no TF): grounded OBSERVABILITY-ONLY (SNS-only, no kill),
   6h threshold vs ~2h nightly -> won't re-fire; fired correctly on the abnormal recovery run.
   RAVC'd COO recommend ACK-not-retune -> COO accepted. No code change.
5. **TO-2 enforcer pre-stage** (`3eb5a96b3`, `f2e49224c`): firm-parameterized module
   `infra/aws/terraform/modules/served-guard/` + 3 distinct-state roots served-guard-{inf,cot,49f}/.
   CTO GATE-2 declared the uniform required-keys -> dropped in -> validate PASS. APPLY-GATED on COO floor.

## Compiler Tools

| Tool | Where | Result |
|---|---|---|
| terraform validate | served-guard module + 3 roots (TO-2), pre + post GATE-2 drop | PASS (Success, all 3) |
| terraform fmt | served-guard module + 3 roots | PASS (clean after 1 align fix) |
| safe-apply.sh (HALT-gate) | item2d, inf value-parity, cot value-parity, item2d cot retune | PASS (HALT-gate clean x4; 0-diff verified each) |
| safe-commit.sh | 18 commits, pathspec-scoped, surface-check | PASS (no critical-surface touch) |
| boto3 logs.filter_log_events | freeze-monitor published=True attribution | PASS (bypassed CLI-v1 CW-Logs quirk) |

**What worked:** terraform validate caught the module wiring early (apply-ready confidence pre-GATE-2);
boto3 reliably bypassed the CLI-v1 describe-log-streams/--max-items constraint bug for log attribution.
**What failed:** CLI-v1 CloudWatch-Logs API (spurious logGroupName-constraint) -- worked around via boto3.
**Gap found:** none new. comp-iam service on the TO-2 enforcer is DEFERRED to apply-GO (the module isn't
in the census until applied) -- IAM hand-grounded to served_guard.py's exact boto3 calls in the interim.

## Deployment Sequence + Verification (AE)

- **item2d freeze-monitor:** safe-apply "8 added, 0 changed"; lambda Active, hourly rule ENABLED; 0-diff.
- **inf value-parity:** safe-apply 8 resources (post-relocate); fire-on-stale $1.59M exit1 + quiet-on-fresh
  diff 0.0000 (0.8.0~B independent invokes). **cot value-parity:** "8 added, 0 changed"; dry-run
  `{firm:cot, fired:false, FRESH}` 432,464,116.36 to the cent. **item2d retune:** in-place
  source_code_hash update, LastUpdateStatus Successful, dry-run cot accepted @2td.
- **TO-2 enforcer:** NOT applied (apply-gated). validate PASS x3 roots + module; commits `3eb5a96b3`
  (build) + `f2e49224c` (GATE-2 drop), pushed CLOUD.

## MCP traffic

~12 significant dispatches handled (rest = broker re-surfaces of handled msgs). Key: COO GO on TO-2
pre-stage (190737Z) + ACK-not-retune accept; CTO GATE-2 DECLARED (193333Z, required-keys uniform);
0.8.0~B 49F wiring CONFIRMED (190300Z); base-DS cot anchor pin + 49F-DS 49F cert anchor. RAVC opens
to CTO (GATE-2 unblock 193124Z) + COO (floor-GO request 193707Z) -- both OPEN at window close.

## Blockers

None (assumption-blocked: none). The two open items are GATES, not blockers:
- TO-2 apply: awaiting COO floor-GO (GATE-2 already cleared). Not blocked -- sequenced.
- 49F reader apply: awaiting the ~23:00Z 49F un-freeze (hard external data gate). Not blocked.

## Current State (zero-context handoff)

- **inf:** GREEN. Served opal-data-inf/platinum/firm/header_metrics.json RICH 06-30 $202.13M.
  value-parity reader `opal-inf-value-parity` LIVE (state compdiff-inf-value-parity/tfstate). Durable
  timeout-tolerate in orion-gold-dispatch.sh (9ea447b3a) deployed to s3://opal-data-inf/code/gold/.
- **cot:** GREEN. `opal-cot-value-parity` LIVE (compdiff-cot-value-parity/tfstate); freeze-monitor
  accept-lag retuned (cot quiet @2td). cot ledgers CLOSED.
- **49F:** reader CERT-READY (`74d04407d`, infra/aws/terraform/49f-value-parity/, state
  compdiff-49f-value-parity/tfstate) -- mutually wiring-confirmed w/ 0.8.0~B. NOT applied; gated on
  ~23:00Z un-freeze + ~B/CVO gap baseline (VP_CERT_GAP_* unset).
- **TO-2 enforcer:** FULLY apply-ready (`f2e49224c`). Module infra/aws/terraform/modules/served-guard/
  + 3 roots served-guard-{inf,cot,49f}/ (states compdiff-served-guard-{firm}/tfstate). Handler
  served_guard.handler (infra/aws/compdiff/served_guard.py, b47bbdfca); engine.assess_write_regression.
  required_keys_json = ["total.aua","total.account_count","total.nna_12m","by_architect"] (CTO GATE-2).
  NOT applied -- awaiting COO floor-GO. Each = 1 firm-scoped Lambda + role + recheck SQS + EventBridge
  on-write rule, ZERO cross-firm. inf grace_seconds=600 until DS~A drops INF_D_00 emit, then ->0.
- **freeze-monitor:** opal-globgrph-freeze-monitor LIVE (infra/aws/terraform/globgrph/item2d_freeze_monitor.tf).
- **PROPOSED/not-applied (own GO):** item2e write-trail (`709d693c6`, infra/aws/terraform/globgrph/item2e_served_write_trail.tf).

## Next Steps

1. **[2.0.0_SA_COO]** floor-GO on TO-2 -> I run 3 firm-isolated safe-applies (comp-iam service +
   EventBridge-enabled check per firm, deploy-ledger per firm). RAVC at each firm LIVE.
2. **[~23:00Z un-freeze]** safe-apply the 49F reader -> 0.8.0~B dry-run co-verify -> CVO 3-of-3;
   my independent boto3 served-flip verify (data_as_of off 06-24 + AUA to the cent; reads whatever
   lands -- clean cert ~$1.8B / guard-hold $1.815B / guard-gold per 0.8.0~B RAVC).
3. **[1.0.0_SA_CTO / DS~A]** inf grace->0 switch sequences with the INF_D_00 emit drop.
