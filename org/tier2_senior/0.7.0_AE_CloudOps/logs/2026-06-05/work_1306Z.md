# work-cycle 0001 — cold-start bring-up + AWS cost-audit deep-verify

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE, SCRIBE
**Date:** 2026-06-05 ~1306Z
**Trigger:** MSTR cold-start spawn (LD-0149/CY-0163, 43h dark) + COO [DRIVE] AWS cost-audit (Andrew-direct, PRIORITY-1)

## Bring-up
/watcher (registered PID 21908, persistent Monitor b18i3tmeo armed), XXX.md startup (session-serial, hooks, comp-graph context), /cloud-ops one-shot, CronCreate /work 20m (job 70ad0c67) + /work cycle-1. Dispositioned 3 carryover (06-03) COO msgs: NFRA-W4 closure (info), TO-4 (no artifact -> COO cleared flag), inf-gold-schedule confirm-ask (answered: SCHEDULED, validates on nightly).

## Cost-audit deep-verify (PRIORITY-1, Andrew-direct)
COO recon: ~$600/mo steady, 53% = 2 scheduled gold runners; root leak = enforcer EXCLUDED-without-idle-ceiling gap (inf-exporter 34d + demo-transform 13d). My deep-verify classified all 5 EXCLUDED runners by CloudWatch CPU + code-traced trigger mechanism:

| Instance | Verdict |
|---|---|
| inf-exporter i-081ae6aa | ADD idle-ceiling (3h). Start/stop by design (inf-jwt-trigger start_instances); 34d uptime = self-stop failing on export path. Auto-restarts on schedule. ~$30/mo. |
| inf-bronze i-083ad9ae | ADD idle-ceiling (backstop; self-stops + watchdog). |
| mdpf-daily i-02448edb | ADD idle-ceiling (eclipse-wait bounded 1800s/30min < 3h; self-stops). |
| inf-gold i-0ed5afded | already ceiling'd; $124/mo = genuine 6.7h compute -> NFRA-W3 right-sizing, not stop. |
| demo-transform i-03343a60 | LEAVE (active DEMOAUTH.002 re-clone, 0.6.0); terminate-at-close TODAY. NOT idle-ceiling (instance-ID can't prevent recurrence of relaunched ephemeral; human-gated, no auto-restart). Durable fix = TAG-based reaping (NFRA-W4). |

4 unattached EBS vols (44GB, Feb-17 temp/build leftovers) -> snapshot-then-delete (needs GO).

## Coordination
- 0.6.0_AE (LIVE, demo owner): confirmed demo-transform load-bearing NOW (2.7h re-clone live) -> terminate-at-close, pings me.
- 0.5.0_AE (inf-exporter owner): OFFLINE -> classified from code+CPU (sanctioned by COO); recommend PROCEED, route self-stop bug to 0.5.0 later.
- COO: full findings + Wave-1 diff routed for GO BEFORE apply. Surfaced 1 decision (demo-transform idle-ceiling: I recommend NO, COO wanted yes -- gave decisive recurrence reasoning).

## Deliverables
- docs/briefs/aws-cost-audit-deepverify-20260605.md (4dbd108e9)
- ADHC_KEEPWARM.json hygiene: Lane-A -> DEPLOYED+VERIFIED (killed stale "Terraform deploy in flight") [COO priority-2]

## Status: BLOCKED on COO GO for the apply (report-before-apply per instruction). No applies yet.

## Compiler Tools
None this tick — investigation was live-AWS (CloudWatch get-metric-statistics, describe-instances/volumes/snapshots, EventBridge list-rules/targets) + code-trace (grep on trigger Lambdas + EC2 scripts). comp-iam not yet relevant (no iam.tf change); will run comp-iam gaps if the enforcer change touches IAM (it does not — env-var-only).
