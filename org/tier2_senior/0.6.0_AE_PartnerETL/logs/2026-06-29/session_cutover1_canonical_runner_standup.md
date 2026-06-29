# Session Log -- DATA_SSOTMG.CUTOVER-1: unattended canonical chain stood up + verified

**archetype:** DEPLOY
**secondary_archetypes:** COORDINATE, VALIDATE
**agent:** 0.6.0_AE_PartnerETL | **date:** 2026-06-29 | **window:** session start (~1850Z) -> 2111Z

## Summary
Andrew-direct GO on CUTOVER-1: wire the unattended canonical Schwab-SSOT ETL chain on the new
direct-Schwab EC2. Delivered the parallel/NOT-served canonical chain end-to-end -- 4 dependency-
ordered seams (S6 IAM -> S1 promote-staged -> S4 trigger -> S8 ordering) -- APPLIED + live-verified,
producing 14 real gold partitions. Five latent defects caught in verification before they bit.

## What was done (dependency order)

**S6a -- box-role IAM (fb174196e).** Brought the ad-hoc DERISK-1 spike IAM (quartz-si2-spike-role/
-profile/-inline, created out-of-band) under Terraform via a new module infra/aws/terraform/
canonical-schwab-ec2/. Imported the 3 IAM resources, proved 0-diff import fidelity FIRST (so apply
couldn't silently delete SchwabSecrets), then applied a PINPOINT grant (Andrew-direct scoping
directive): ListBucket tightened whole-bucket -> prefix-Condition (01_raw/* + 01_raw_quartz_validation/*);
PutObject object-scoped; GetObject DROPPED (write-only box); no canonical grant (NEVER-WIDEN).

**S6b -- canonical-runner role + S4 + S8 (0506c9ada, 537359cca, 15e3a25b9, be0b76358 + the 4 fixes).**
Dedicated canonical-schwab-runner (Linux, CTO-arch-gated over Lambda/Fargate). PINPOINT role on
base-DS's authoritative read-set (caught a fees/G12 grant I'd missed = a latent 403; single
AES256-conditioned canonical write; no raw-write; no ec2:). S8 = hard fail-loud gate (s8_gate.py:
UPT sentinel + 6 required CRS types). S4 = EVENT-DRIVEN trigger (COO+CTO blessed over time-cron):
EventBridge xref-success rule -> SSM-Automation start -> S8 gate -> build -> OS self-stop. Plus the
CTO-required sentinel-absence alarm.

**Apply-push (ledger 20260629T2012Z, CLOSED 6/6).** safe-apply 12 resources 0-diff. Two unattended-
bootstrap bugs found via live cloud-init/SSM debugging + fixed IN SOURCE + recreated (not hand-
patched): (1) base Ubuntu AMI ships no aws CLI -> user-data died at the s3-fetch; (2) apt awscli v1
conflicts with pip botocore (KeyError opsworkscm) -> switched to pip awscli. 3rd boot clean hands-off.

## VERIFICATION caught 5 defects before production (the session's core value)
1. Missing fees/G12 read grant (latent 403) -- caught by getting the exact footprint vs guessing.
2. base-DS's xref-location fix was PARTIAL -- source-grounding (SRC_BUCKET="opal-data-schwab" at
   build_dim_account.py:88 + build_dim_relationship.py:138) showed 2 dims still on the stale 04-21
   xref; held the role-tighten + flagged file:line evidence -> base-DS completed (f196aa684).
3+4. Two bootstrap bugs (no-CLI-in-AMI; apt-vs-pip botocore) -- live-debugged, source-fixed, reproven.
5. Reused bd-gold WATCHDOG would've shut the box MID-BUILD on a multi-date catch-up (its regex
   matches gold subprocesses, not the build_canonical_daily PARENT/silver phase) -- caught by READING
   the reused script; built a canonical parent-keyed watchdog (c48b74fed); proved the box idles
   correctly (state=stopped, confirming instance_initiated_shutdown_behavior=stop).
Plus my own premature absence-alarm fire (treat_missing_data=breaching on a not-yet-firing rule) ->
fixed to notBreaching + forced OK + <<<FLIP-AT-GO-LIVE>>> doc (f69f9b70b).

## Compiler Tools
| tool | use | result |
|---|---|---|
| comp-iam role | runner role modeled view post-apply | PASS -- DESIRED==LIVE, pinpoint confirmed |
| comp-which | routed instance-role/TF-home questions | PASS -- routed to comp-iam; ran comp-grep on-rails |
| comp-grep | source-ground the xref read-location across the 4 dim builders | PASS -- caught the partial fix (2 stale) + confirmed all schwab reads are 01_raw |
| live aws iam get-role-policy | fresh-grant ground-truth (rule 22, rail-checked) | PASS -- box + runner roles exactly as intended |
| terraform plan/validate | import-fidelity 0-diff + apply 0-diff + module validate | PASS -- 0-diff box; 12-add runner; post-apply 0-diff |
| deploy_ledger.py | open/close-leg/close the 6-leg apply ledger | PASS -- CLOSED clean, no stranded leg |
**What worked:** comp-grep source-grounding caught base-DS's partial fix (defect #2) -- the pinpoint
discipline's highest-value catch. **What failed:** none. **Gap found:** comp-freshness has no config
surface for a brand-new parallel/NOT-served prefix (canonical/schwab/gold) -- fell back to rail-checked
head-object for the NEVER#7 artifact proof (exact SSE+LastModified, which comp-freshness doesn't give).

## Files Modified
see commit messages: fb174196e, 0506c9ada, 537359cca, 15e3a25b9, be0b76358, 4136af326, bab5a8136,
c48b74fed, f69f9b70b. New module infra/aws/terraform/canonical-schwab-ec2/ (main/iam/runner/
runner-iam/runner-trigger.tf + S4_S6b_S8_DESIGN.md); new infra/aws/ec2/canonical-schwab-runner/
(s8_gate.py, run-canonical.sh, setup-instance.sh, user-data.sh, watchdog-shutdown.sh).

## Deployment Sequence + Verification (actual output)
- safe-apply: "Apply complete! Resources: 12 added, 0 changed, 0 destroyed" -> instance i-0ed92ce2e72f505dc.
- Dry-run (SSM): "=== done: 25/25 steps OK ===" (date=2026-06-24, production 01_raw/).
- Live build (SSM): "=== done: 25/25 steps OK ===" -- every dim built, ZERO 403s.
- NEVER#7 S3 verify: 14 gold partitions date=2026-06-24; portal_aggregates LastModified 20:36:37Z,
  20585 bytes, SSE=AES256.
- Idle self-stop: instance state=stopped, "User initiated" (watchdog + shutdown_behavior=stop proven).
- Alarm: StateValue=OK (premature fire suppressed).

## Current State (zero-context handoff)
- **canonical-schwab-runner** i-0ed92ce2e72f505dc (r6i.xlarge, Ubuntu 22.04, sg-0c74897be78ba49d5,
  TF module canonical-schwab-ec2): STOPPED/idle. Role canonical-schwab-runner-role (pinpoint).
  Runner systemd service ENABLED; canonical-watchdog.timer active (parent-keyed). Code at
  s3://opal-data-bd/code/canonical-schwab-runner/ (AE) + s3://opal-data-bd/code/canonical/schwab/ (DS).
- **EventBridge rule** canonical-schwab-xref-success: matches {source:opal.canonical-xref,
  detail-type:XrefRefreshSuccess} -> SSM-Automation AWS-StartEC2Instance (start role holds
  ec2:StartInstances, not the box). LIVE, awaiting base-DS's S10 put_events emit.
- **Alarm** canonical-schwab-xref-sentinel-absence: OK, treat_missing_data=notBreaching (build-out
  suppression). MUST flip to breaching when the first trigger-driven cycle fires.
- **Box (SI2)** i-0f3d57a97f14727af (quartz-si2-spike-role): lands raw to 01_raw_quartz_validation/
  (parallel-run). S1 repoint to prod 01_raw/ HELD on N=5 clean box-days.
- **Output:** s3://opal-data-bd/canonical/schwab/{silver,gold}/ (parallel/NOT-served), 14 gold
  partitions @ date=2026-06-24 on the fresh-xref number, ready for CVO S7 parity.
- Both boxes registered in EC2_MANIFEST.json (0.7.0, e4bcdf2e8). Ledger 20260629T2012Z CLOSED.

## Next Steps
- **[0.4.0_DS_ClientPlatform]** Wire the S10 xref-refresh-success put_events emit (opal.canonical-xref/
  XrefRefreshSuccess, default bus, on clean refresh only; events:PutEvents on the S10 role). Next-after
  the inf-AUM work.
- **[0.6.0_AE_PartnerETL]** ON base-DS's emit: flip the absence-alarm treat_missing_data back to
  breaching + verify the first trigger-driven unattended cycle (full AC5) + RAVC COO/CTO/Andrew.
- **[0.6.2_AE_PartnerETL]** Track the daily clean/not-clean box-day call (N=5-incl-1-heavy) from
  tomorrow's 12:00Z first with-files run -> gates the S1 box-repoint.
- **[3.0.0_SA_CVO]** S7 parity window can start accumulating clean-days on the 14 fresh-xref gold
  partitions (canonical-vs-BD-served).

## Blockers
None. The 2 open items (base-DS S10-emit -> trigger-driven AC5; 0.6.2 N=5 streak -> S1 repoint) are
genuine external-event gates (COO-confirmed legitimate standby, not a coast), not assumption-blocks.
Inherited TOs (ADHC_GLDINC.SS4c / ADVI_BDAPIMIG.P1 / ADVI_COTETL.L4-GUARD) HEAD-grounded as
landed/tail/externally-gated -> COO parked their closeouts post-cutover.
