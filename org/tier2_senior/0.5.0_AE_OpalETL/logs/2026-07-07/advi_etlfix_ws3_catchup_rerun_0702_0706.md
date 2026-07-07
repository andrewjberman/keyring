# ADVI_ETLFIX WS-3 -- sanctioned catch-up re-run: 07-02/07-06 custody unfrozen, recon PASS, drift landmine filed

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE
**Date:** 2026-07-07 | **Serial:** 0.5.0_AE_OpalETL | **TO:** ADVI_ETLFIX.WS3 (COO GO 20260707T151408Z + deviation-approval 152953Z)

## Outcome
The 06-25-class custody freeze (partner_custody_total stuck at $1,604,173,986.44 for 07-02..07-06) is
RESOLVED end-to-end. Root cause was the Schwab vendor-delivery gap (COO-ruled); Andrew's manual SI2 pull +
0.6.2's silver roll landed RPS 07-02/07-06 at 14:44Z. Today's 07-07 nightly (15:01Z) unfroze the frontier
on its own; this session's COO-sanctioned catch-up corrected the two stale historical partitions. All
served MDPF surfaces now carry per-date-correct schwab-native custody.

## What ran (surgical, COO-approved deviation from "full chain")
Grounded BEFORE running (Rule 22): (1) WS-B is CURRENT-SNAPSHOT -- SmartX enterprises/allocations has no
as-of param (wsb_49f_smartx_model_aua.py:153); --date is stamped (:168); a historical Stage-1 re-run would
OVERWRITE correct feeder vintages with today's values. (2) WS-E's default RPS resolution is a GLOBAL max
(build_mdpf_wse_49f_non_model_aua.py:271) -- unbounded, unlike WS-D.2's date-bounded resolver
(wsd_partner_held_etf.py:226) -- so a plain --date 2026-07-02 run would price 07-02 custody off the 07-06
RPS (look-ahead). Deviation surfaced to COO pre-execution; approved ("correct and safer").

Per date (07-02 then 07-06): WS-D.2 (--date d --rps-date d) -> WS-E (--date d --rps-date d
--custody-source schwab) -> WS-A (--date d --source s3) -- then rollup + OWNTS (--date 2026-07-07
frontier) once. WS-B/WS-C/WS-D.1 feeders untouched. Mechanism: mdpf-catchup-etlfix-ws3.sh (commit
338f754b5) -> s3://opal-data-mdpf/code/ -> SSM 2d695d17 fetch+exec on mdpf-daily-runner (Rule 12;
mirrors the production trigger bootstrap incl CUSTODY_SOURCE=schwab stamp). Runner auto-stopped after.

## Verification (live served artifacts, post-run)
- platinum/mdpf/aggregate_aua/{07-02,07-06}.json: reconciliation.overall PASS both.
- Custody UNFROZEN + per-date-distinct: 07-02=$1,614,447,381.76 (RPS 20260702), 07-06=$1,621,251,574.22
  (RPS 20260706); movement arc 1.6041B (07-01 basis) -> 1.6144B -> 1.6213B.
- aggregate_aua_timeseries.json as_of_last=2026-07-07 (425 pts); OWNTS 4/4 tickers as_of_last=2026-07-07.
- EXPECTED nuance (not a freeze): 07-06 == 07-07 custody -- both price off RPS 20260706 (no 20260707 RPS
  yet, vendor T+1 roll-forward per contract 3.4, recorded in rps_date_used).
- Prerequisite (DS~A aggregator wire) confirmed by EXERCISE: wire present at mdpf_aggregate_aua.py:916 +
  nightly chain passing identity_2 in production (07-06/07-07 recon PASS) -- stronger than a config read.

## FINDING filed then RETRACTED (false positive) + net-no-op deploy closed at 0-diff
Filed a "CUSTODY_SOURCE drift landmine" finding (SSM /mdpf/custody_source "does not exist", fail-safes
armed to regress the served basis to bd); COO GO'd a TF fix; DURING execution the premise collapsed:
`ParameterAlreadyExists` on create + TF reading the param fine while my Git Bash `aws` NotFound'd it.
Root cause of the false finding: MSYS path-mangling of the leading-slash param name in every Git Bash
aws call (the documented CLAUDE.md footgun) -- the param existed CONTINUOUSLY since 07-01 (PowerShell
get-parameter-history: v1=bd 07-01 dormant TF create by the ALREADY-CANONICAL
aws_ssm_parameter.mdpf_custody_source, lambdas.tf:55, ignore_changes=[value] design; v2=schwab the
07-02 cutover flip). System was healthy end-to-end; deployed Lambda == repo (byte-verified, true).
Deploy disposition: my duplicate resource applied (v3=schwab, value unchanged) -> duplicate discovered
via perma-diff -> state-rm + ssm.tf deleted -> canonical reconciled (v4, value unchanged) -> plan "No
changes" (0-diff), live param verified via PowerShell. Zero production impact. Correction RAVC'd to COO
(155624Z; accepted no-fault 155652Z). Ledger 20260707T1545Z CLOSED with corrected narrative. Lessons
banked (memory: gitbash-aws-leading-slash-notfound-not-evidence): single-path absence = INFERRED,
non-actionable; grep the module for the resource type before authoring a "new" TF resource. Standing
TRUE finding: comp-pipescript/graph MDPF coverage gap (COO noted for later prioritization).

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| comp-freshness artifact x14 (schwab silver {7 tables} x {0702,0706}) | 14/14 PASS | grounded 0.6.2's unfreeze claim live before pinging COO (freshness-watch fire) |
| comp-freshness artifact (canonical rps prefix discovery) | PASS + canonical-layout note | the tool's NOTE field carried the bucket-drift history that located opal-data-bd/schwab/silver/ |
| comp-grep (WS-E/WS-B/WS-D.2 arg + RPS-resolution semantics; dispatch/TF trigger wiring) | grounded the deviation | found the WS-B current-snapshot risk + WS-E unbounded-resolver asymmetry that made the literal full-chain re-run unsafe |
| comp-pipescript deployed (all-trees sweep, background) | mdpf not covered by sweep output in time; superseded by direct byte-compare | GAP (repeat of WS-3 finding): mdpf scripts still outside comp-pipescript coverage; did cmp -s repo vs s3://opal-data-mdpf/code/ -- 5/5 scripts + dispatch byte-identical |
| comp-which / comp-glob | routed runbook + bucket questions | comp-glob found RUNBOOK_AE_mdpf_daily_chain.md on 2nd pattern |
| aws (operational: ssm send-command/get-command-invocation, ec2 start/describe, s3 cp verify; rail-checked inspections: lambda env, SSM command history) | all grounded live | Rule 22a applied-truth pulls for the fresh-change/drift questions comp-iam DESIRED cannot answer |

## Current State + Next Steps
- WS-3 remains OPEN per COO ruling; freshness watch continues. Req-1 (3 consecutive nightly advances)
  accrues from tonight's nightly on RPS 20260707+ vintages -- COO calls the formal re-check.
- [COO] GO/no-GO on the CUSTODY_SOURCE fix plan (SSM param + trigger redeploy). Until then: do NOT
  redeploy mdpf-daily-trigger; any ad-hoc WS-E run MUST pass --custody-source schwab.
- [0.6.2_AE_PartnerETL] Schwab-silver side validated clean from this end (RAVC ack sent 15:13Z).
- Catch-up script retained at infra/aws/ec2/mdpf-daily-runner/mdpf-catchup-etlfix-ws3.sh (reusable
  pattern for late-vendor-landing recovery; the --rps-date pinning is the load-bearing part).
