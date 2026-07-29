# Deploy-Completion Ledger -- MDPF Accrual Bridge (Scheduler + trigger Lambda)

**Opened:** 2026-07-29T07:45Z (deploy-start: targeted plan created)
**Closed:** 2026-07-29T08:00Z (all legs landed + exercised; nothing stranded)
**Operator:** 0.7.0_AE_CloudOps~A
**Authority:** CTO ruling 20260729T052742Z (accrual seam split) + 072447Z (apply GO, blocker cleared at 6846dba11f)
**Tag:** mdpf-pipeline-v1.9.0

## Legs (all closed)

1. **Staging** -- build_portal_gold_accrual.py (HEAD blob @6846dba11f) to
   s3://opal-data-mdpf/code/scripts/gold/ INSIDE the synced set; md5
   9cbef6b90f0bd630acda4ba6d05ed5c3 verified local == HEAD blob == S3 roundtrip.
   partner_roster.json already adjacent (ETag a22fc62be04777eb26f5b8f2ccba6ee1).
2. **Commits** -- 1163e28f5b (Lambda src + accrual-bridge.tf), dcb845d73b
   (source-map entry, Rule 4), record-terraform-deploy commit ([skip ci]).
3. **Artifact** -- mdpf-pipeline/mdpf-accrual-trigger.zip uploaded, write
   VERIFIED (size=2451, sha256 metadata match).
4. **Apply** -- targeted plan (8 targets): 9 to add, 0 to change, 0 to destroy
   -- ADDITIVE-ONLY PROVEN IN THE PLAN; trio trigger paths untouched (deploy
   freeze criterion for today's D2 evidence holds). safe-apply with HALT_ACK=1
   (2 routine base-inbox messages, both read + acted). Apply complete 9/0/0.
5. **0-diff** -- targeted re-plan: "No changes."
6. **Live verify (applied plane)** -- scheduler mdpf-accrual-bridge-daily
   ENABLED cron(45 15 * * ? *) UTC -> arn:...:function:mdpf-accrual-trigger;
   Lambda Active, python3.12, 360s/256MB, env correct.
7. **Exercised (behavior plane)** -- QA dry-run invoke 20260729T075310Z:
   Lambda started the stopped runner, waited SSM Online, dispatched; script
   pulled from synced set, roster resolved SCRIPT-ADJACENT
   (/opt/mdpf/scripts/gold/partner_roster.json), scopes derived
   [49financial, cottonwood, inflection, global], PLANNED 11 objects.
   rc=1 = the R4 fail-loud contract firing on 3 DECLARED-but-ABSENT sources
   (aum-metrics for 49financial/inflection/global -- DS~A is building exactly
   these). NOT a mechanism failure: on a real run the script writes every
   planned object and exits 1 only to flag the absent declarations
   (build_portal_gold_accrual.py:249-267). Clears when DS~A's artifacts land.
8. **Tag + push** -- mdpf-pipeline-v1.9.0 annotated, pushed --follow-tags
   (20ae9c1467).

## Deliberate design notes (on the record)

- **No shutdown by the bridge:** at 15:45Z the 15:00Z chain may be mid-run on
  the same runner; lifecycle stays with the chain's dispatch. The QA invoke
  left the runner RUNNING (started ~07:53Z); the 15:00Z trigger's
  start_instances is idempotent on a running instance and the chain's own
  shutdown stops it at end. Not stopped by hand: EC2 stop is a
  human-confirmation action (CLAUDE.md autonomy) and the running state is
  self-healing at chain end; cost is bounded instance-hours.
- **No convergence gate:** the bridge derives every artifact's as-of from
  content; gating on the chain would re-land the passenger defect.
- **No alarms** (moratorium, Andrew-direct 2026-07-28). Failure is loud where
  it happens: Lambda Errors + SSM command status.

## First unattended fire

15:45Z today (2026-07-29). Expectation: bridges the healed source before the
16:15Z publisher enumerates; rc=1 expected (loud) until DS~A's aum-metrics
land for the 3 non-cottonwood scopes; every available artifact still bridges.
