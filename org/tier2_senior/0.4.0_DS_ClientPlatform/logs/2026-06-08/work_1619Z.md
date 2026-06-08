# 0.4.0_DS_ClientPlatform — work_1619Z (MDPF chain-down: feeder redeploy + cohort_0 sentinel downgrade)

**archetype:** DIAGNOSE + DEPLOY

## Incident
COO DRIVE-ESCALATE (160554Z): live MDPF nightly chain HARD-FAILED today (06-08 15:00Z) at Stage-3
WS-A reconciliation — cohort_0 +78% (58.6M->104.3M) tripped Sentinel-1, drop-rather-than-fabricate
skipped the platinum write -> NO 06-08 partition -> served surface FROZEN at 06-05. Gates tomorrow's
MDPF_CADENCE ~10:21Z first-fire. 2 stale MDPF deploys also flagged (160321Z). My Rule-13 MDPF lane.

## Adjudication (verify-before-fix — checked the link as COO asked)
**Feeder (build_mdpf_wsc_inflection_feeder.py): RUNNER-BEHIND.** Deployed S3 == pre-F1 commit
7d41d28cd EXACTLY (diff -bw match) — entirely lacks the 30c19b26c spine-repoint (14 client_performance
refs in HEAD, 0 in S3). The 5/29 $1.5M-gap fix never reached the runner. NOT reverse-drift. Redeployed
(Andrew-direct via CTO 161609Z): aws s3 cp committed->S3, MATCH. No new commit (already committed).

**LINK FALSIFIED — feeder is NOT the cohort_0 cause:**
- cohort_0 = etf_public_residual_total = AUDIT-ONLY ETF-decomposition residual (aggregate L100/520/612).
- The feeder's output non_model_aua = $85,652,260.50 = cohort_2b (a DIFFERENT cohort). Read the stale
  feeder's actual 06-08 output: source_pipeline=eclipse, partner_custody_total=202.67M.
- F1 changes Inflection CUSTODY source (Eclipse->client_performance spine, ~$1.5M into cohort_2b). The
  F1 diff's only functional changes = load_client_performance_total + build_non_model_aua; the 3
  "decomposition" diff hits are docstring comments (Andrew's "do NOT recreate the decomposition"). F1
  does NOT touch the ETF decomposition / etf_public_residual.
- Magnitude: a $1.5M custody source-shift cannot drive a $45.6M cohort_0 move. -> feeder redeploy will
  NOT clear the reconciliation. Confirmed Sentinel-1 was the SOLE tripper (certified_aua cross-check
  PASS L3077, partners=2, headline clean).

**Backfill (build_mdpf_process_backfill.py): RUNNER-BEHIND** (deployed S3 == old commit bc3b08c8f, lacks
F4 + onboard-guard + write-guard). NOT reverse-drift. BUT it's an AD-HOC historical tool (PARTNER-
hardcoded, run manually w/ explicit GO, no dispatch/cron ref) = NOT nightly-chain -> not chain-blocking.
Andrew scoped it as a separate follow-on. (3 MISSING_ON_S3 = one-time backfills, not nightly-chain.)

## Fix (Andrew-direct, conversational)
Andrew: "dont worry about cohort 0, we are not using that for anything right now... it doesnt display
anywhere on the portal... the more important thing is that from the engineering side we are simply
procuring and storing that data consistently and reliably." => the cohort_0 hard-gate is the wrong
posture (an unused audit field froze the whole served surface). DOWNGRADED Cohort-0 DoD Sentinel-1
ERROR->WARN (mdpf_aggregate_aua.py, commit 71dea8a82, deployed, MATCH). `overall` escalates only on
"ERROR" so a WARN records the anomaly (in the reconcile block) without dropping the platinum write ->
the chain STORES the data (headline + cohort_0=104.3M flagged WARN) + advances the served surface.
SAME WARN pattern already established for id2 (Andrew-direct 2026-05-26). HEADLINE PROTECTION UNCHANGED
+ still ERROR-gated: identity_1 + Sentinel-2 (partners-present) + Sentinel-3 (2nd-producer cross-val).

## Effect / verification
Takes effect on tomorrow's MDPF_CADENCE ~10:21Z SCHEDULED run (NO manufactured run — C1 / Andrew's
no-ad-hoc rule): writes the 06-08 partition, unfreezes the served surface, stores cohort_0/ETF values
daily (Andrew's goal). Per Andrew, did NOT deep-analyze the cohort_0 jump (stored + flagged, not
investigated). RAVC2 to COO+CTO.

## Files / commits
| File | Commit | Deploy |
|---|---|---|
| build_mdpf_wsc_inflection_feeder.py | (redeploy 30c19b26c, no new commit) | S3 MATCH |
| mdpf_aggregate_aua.py (cohort_0 Sentinel-1 ERROR->WARN) | 71dea8a82 | S3 MATCH |

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| comp-pipescript deployed --pipeline mdpf | drift report + post-fix MATCH | 2 STALE found -> both resolved (feeder MATCH, aggregate MATCH) |
| (S3 + git adjudication) | deployed-vs-commit diff per script | feeder==pre-F1 7d41d28cd / backfill==bc3b08c8f = runner-behind both |
| ds-commit-gate | mdpf_aggregate_aua.py | PASS |

work-cycle:0005
