# work-cycle 0005 — enforcer-v1.1.1 threshold calibration (inf-gold I/O-bound fix)

**archetype:** DIAGNOSE
**secondary_archetypes:** DEPLOY, VALIDATE, COORDINATE
**Date:** 2026-06-05 ~1404-1423Z
**Trigger:** CVO R8 apply-verify CONDITIONAL + COO time-sensitive inf-gold reap-risk

## The issue
CVO flagged R8 apply-verify CONDITIONAL: inf-gold i-0ed5 running since 13:00:48Z, <3% CPU every bucket = pre-compute idle-wait; R8 3h reap-mark 16:00:48Z. The gold runner's "boot -> disarm watchdog -> await unbounded SSM dispatch" pattern is the one case idle-aware structurally struggles with.

## Discipline catch (mine)
I initially called ALL-CLEAR off a single 14:00Z 7.48% bucket = PREMATURE (next bucket fell to 2.82%). COO correctly pushed back. Re-pinned to GROUND TRUTH (SSM + log + CPU, not inference):
- SSM: 4x AWS-RunShellScript 13:41-13:58Z all Success -> gold compute DID dispatch.
- CPU: idle-wait 0.3% -> post-dispatch 2.8% (I/O-bound, hovering at the 3% line, NOT sustained).

## Root cause + fix (better than the proposed exemption tag)
The 3.0% IDLE_CPU_THRESHOLD was MISCALIBRATED: an I/O-bound active runner (~2.8%) read as "idle." Empirical fleet scan = BIMODAL: true-idle 0.002-0.3% (inf-bronze 0.002, inf-exporter/demo/inf-gold-wait 0.2-0.3), active 2.8%+. Clean gap, NOTHING in 0.3-1.0%.
=> FIX: IDLE_CPU_THRESHOLD 3.0 -> 1.0. Spares I/O-bound compute, still reaps every zombie. ZERO exemption (honors Andrew no-exceptions) -- strictly better than the AutoShutdown=disabled tag COO/0.6.0/CVO had been leaning toward. COO endorsed; Andrew GO'd.

## Deploy (enforcer-v1.1.1)
- Validation (COO ask): fleet idle-floors confirm clean 1.0% cut, nothing 0.3-1.0%.
- commit 84a2bd24d (single env var) -> plan 1 in-place -> tag enforcer-v1.1.1 -> safe-apply (HALTGT) 0/1/0 -> 0-diff verify -> push --follow-tags -> live config IDLE_CPU_THRESHOLD=1.0 confirmed.
- FLEET-CLEAN post-apply: inf-gold + demo still running (spared); inf-gold CPU climbing 2.85->5.95->6.87% (all >1.0) = robustly spared, fragility GONE. Backstop monitor dropped. RAVC2 -> COO + CC CVO -> CONDITIONAL clears to PASS.

## Live validation today (3 edge cases)
1. demo active-job (35-50%) spared through 18h run. 2. inf-gold idle-wait held then spared at compute-start. 3. inf-gold I/O-bound 2.8% compute now robustly spared post-calibration.

## Posture
R8 COMPLETE (enforcer-v1.1.1 final: universal, idle-aware, MAX_RUNTIME=0, threshold=1.0, zero allowlists/exemptions). moltbot terminate pending Andrew's hand. R1 S3 backfill next (paths mapped).

## Compiler Tools
None -- terraform apply/plan + live-AWS (cloudwatch get-metric-statistics fleet scan, lambda get-function-configuration, ssm list-commands, ec2 describe) + git. No iam.tf change.
