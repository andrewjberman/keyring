# AWS Cost Audit — Deep-Verify + Remediation (AE 0.7 CloudOps)

**Date:** 2026-06-05 ~13:00Z · **Author:** 0.7.0_AE_CloudOps · **Companion to:** `aws-cost-audit-20260605.md` (COO recon)
**Trigger:** COO [DRIVE] AWS cost audit (Andrew-direct) — deep-verify the enforcer-gap leaks + propose remediation.
**Constraint:** stop/config-only, ZERO manufactured gold runs (Andrew standing cost-discipline). Enforcer config via Terraform (safe-apply, commit-before-apply, tag). Report BEFORE apply.

---

## Per-instance verdicts (CloudWatch CPU + code-traced trigger mechanism)

| Instance | Type | State | CPU (7d) | Trigger mechanism | Self-stop | Verdict |
|---|---|---|---|---|---|---|
| **inf-exporter** i-081ae6aafb | t3.medium | running **34d** | mean 0.25%, brief 14-18% export spikes | `inf-jwt-trigger` Lambda `start_instances` (jwt cron 12:13 UTC + export 21:00 UTC) | YES (`inf-jwt-fetch.sh:86 shutdown -h now`) but **failing on some path** (34d uptime proves it) | **ADD to IDLE_CEILING (3h).** Auto-restarts on schedule. The leak = self-stop not firing on the export path; idle-ceiling is the structural backstop. |
| **demo-transform-runner** i-03343a60 | t3.large | running **13d** (ACTIVE 2.7h re-clone now, launched 12:59Z) | mean 1.03%, one 58% transform burst | **NONE** — manual SSM dispatch, ephemeral one-shot, human-gated phase holds | terminate-on-RAVC2 (manual) | **LEAVE RUNNING (load-bearing now) → TERMINATE at DEMOAUTH.002 close (0.6.0 pings TODAY).** Do NOT idle-ceiling — see disagreement note below. Remove from EXCLUDED at terminate. |

### Disagreement resolved: demo-transform idle-ceiling — NO

COO proposed adding i-03343a60 to IDLE_CEILING (3h) as a pure config-add (auto-reaps 3h after idle, never touches the active run). Owner 0.6.0 objected: human-gated ephemeral, no auto-restart. **Decisive tiebreaker: instance-ID-based idle-ceiling cannot prevent recurrence anyway** — this box terminates at DEMOAUTH.002 close (today); any *future* demo run launches a *fresh* ephemeral with a *new* instance ID, which would not be in the list. So adding this ID:
- gives ZERO recurrence-prevention (the stated benefit), and
- adds real risk: a human-gated hold (transform-done → awaiting DS PII-verify / Andrew visual smoke) can sit idle >3h; a 3h reap mid-hold strands the operator AND can force a full multi-hour re-clone (ephemeral local state lost on stop) — the exact expensive operation cost-discipline forbids running ad-hoc.

**→ demo-transform: terminate-at-close (owner-driven, today), NOT idle-ceiling.** The DURABLE fix for the ephemeral-recurrence class is **tag-based reaping** (enforcer reaps any box tagged e.g. `AutoShutdown=idle-ceiling-3h` regardless of ID) — flag for NFRA-W4. Instance-ID lists only fit persistent-ID scheduled runners.
| **inf-bronze-runner** i-083ad9ae | t3.small | running (chain 12:43) | brief sequential pulls | `inf-bronze-trigger` (cron 12:30 UTC) | YES (`inf-bronze-fetch.sh:115` + `watchdog-shutdown.sh`) | ADD to IDLE_CEILING (3h) — defense-in-depth backstop. Cheap (t3.small); low leak risk but closes the gap. |
| **mdpf-daily-runner** i-02448edb | t3.medium | stopped | 4-stage DAG | `mdpf-daily-trigger` (cron 15:00 UTC MON-FRI) | YES (`mdpf-daily-dispatch.sh:117`); eclipse-wait **bounded 1800s/30min** < 3h | ADD to IDLE_CEILING (3h) — eclipse-wait bounded under ceiling, safe. |
| **inf-gold-layer-runner** i-0ed5afded | c6a.4xlarge | stopped (cycled 12:52 today) | genuine ~6.7h active gold compute | `inf-gold-trigger` (silver-complete event + 14:00 UTC fallback) | YES | ALREADY in IDLE_CEILING (3h). $124/mo is **genuine run-duration, not idle-waste** → NFRA-W3 right-sizing candidate (validate on scheduled nightly, no ad-hoc), NOT a stop-now item. |

## Key distinction (governs task-4 design)

Idle-ceiling reaping is **only safe for runners with an automated start-trigger** (the trigger restarts them next schedule). The four scheduled runners (inf-exporter, inf-bronze, mdpf-daily, inf-gold) all qualify. **demo-transform-runner does NOT** — it is a manual ephemeral one-shot with no trigger Lambda and human-gated SSM phase holds; reaping it would strand the operator. The correct treatment for it is terminate-when-done, not idle-management.

→ Task-4 "make idle-ceiling the default for excluded batch runners" is correct **scoped to scheduled/auto-restart runners**. A blanket rule including manual ephemerals would be a footgun.

## Proposed enforcer config diff (`infra/aws/lambda/ec2-auto-shutdown-enforcer/main.tf`)

**Wave 1 (deployable after COO GO — pure config, no manual destructive op):**
```diff
- IDLE_CEILING_INSTANCES = "i-0ed5afded2ebd4ed4"
+ IDLE_CEILING_INSTANCES = "i-0ed5afded2ebd4ed4,i-081ae6aafb394fb1a,i-083ad9ae297f88e9f,i-02448edb624a7a7cf"
+ # added inf-exporter, inf-bronze, mdpf-daily — persistent-ID scheduled runners, all self-stop + auto-restart
  IDLE_CEILING_HOURS     = "3.0"   # unchanged; mdpf eclipse-wait (30min) < ceiling, inf-gold genuine compute won't idle 3h straight
  EXCLUDED_INSTANCES     = "...unchanged in Wave 1..."  # all 5 stay; demo-transform handled in Wave 2
```
- inf-exporter (up 34d idle, 0.22% CPU now = not mid-export) qualifies for reap on the **next enforcer run (~5min post-deploy)** — this is the enforcer's sanctioned auto-stop, NOT a manual `stop-instances` by me, so it needs no separate Andrew destructive-gate. Restarts on next schedule (jwt 12:13 UTC / export 21:00 UTC today). ~$30/mo recovered + recurrence-proof.
- inf-bronze / mdpf-daily: backstops (both already self-stop) — close the gap, recurrence insurance.

**Wave 2 (after 0.6.0 pings DEMOAUTH.002 close, today):**
```diff
- EXCLUDED_INSTANCES   = "...,i-03343a6072834f77d,..."
+ EXCLUDED_INSTANCES   = "..."   # remove demo-transform after I terminate it
```
+ terminate i-03343a60 (Andrew/COO destructive-GO). ~$61/mo recovered.

**0.5.0_AE confirm (inf-exporter owner, offline):** evidence is overwhelming it should not be always-on (designed start/stop — `inf-jwt-trigger` explicitly `start_instances` it; 34d at 0.25% CPU). Recommend PROCEED on Wave 1 without waiting; route the underlying self-stop bug to 0.5.0 for later. COO's call whether to hold for 0.5.0.

## Task 5 — unattached EBS volumes (44GB, ~$4/mo)

All 4 are **Feb-17 one-time temp/build leftovers**, unattached 3.5 months, no covering snapshots:

| Volume | GB | Name |
|---|---|---|
| vol-0ba59aa26025649d5 | 20 | docker-builder-temp-encrypted |
| vol-07e6ca7175ef9d1c1 | 8 | bd-snapshot-gen-v3-encrypted |
| vol-05425c3a28f7e2ca9 | 8 | bd-all-historical-snapshots-encrypted |
| vol-0a6bb3594ff6393cc | 8 | bd-snapshot-PRODUCTION-encrypted |

**Recommendation:** snapshot all 4 first (cheap reversible insurance, ~$0.50/mo for snapshots vs $4/mo for volumes), then delete the volumes. EBS delete is destructive → needs explicit GO (COO/Andrew).

---

## ADDENDUM — SUPERSEDED BY R8 UNIVERSAL CAP (Andrew sovereign scope-up, 13:10Z)

Andrew (verbatim): *"everything should be on the 3hr kill, there is no reason anything should be running longer than 3 hrs."* This **retires the per-ID allowlist architecture** (EXCLUDED_INSTANCES / IDLE_CEILING_INSTANCES) entirely — the narrow Wave-1 diff above is superseded. Now PRD **R8 (NFRA_COSTRED v0.2)**: "Universal 3h idle-aware cap, no per-instance exemptions" (absorbs R4+R6).

**Implemented (enforcer redesign, this session):**
- Single universal rule for EVERY running instance: reap if `uptime > 3h` AND `idle across the entire 3h window` (Maximum CPU < 3% in every 5-min bucket). No allowlist.
- Only exemption = a consciously-set `AutoShutdown=disabled` instance tag (currently ZERO, per Andrew's no-exceptions).
- **IDLE-AWARE** (Andrew confirmed to CTO 13:15Z): any 5-min bucket above threshold spares the box → no mid-write corruption. **AC4 preserved exactly** from the i-0ed5 logic (`idle_entire_window`, Maximum-per-bucket) and now generalized fleet-wide.
- Optional hard-cap `MAX_RUNTIME_HOURS` = `0` (DISABLED) — idle-aware only per COO. Knob retained for the runaway-busy gap (process pegged >3% for >3h is never "idle") if Andrew later wants hard-kill.
- **R6 reliable stop-path:** the enforcer calls `ec2.stop_instances` directly (AWS-side), independent of the unreliable in-OS `shutdown -h now` that was the root of the inf-exporter 34d + the 24h runaways.

**AC4 fleet-wide poll-gap safety verification:** legit run durations all < 3h → none reach the idle-check while busy: bd-gold ~77min full (~2.4h incl poll), inf-gold ~2h active, demo-reclone ~2.7h (CPU-busy, spared), mdpf eclipse-wait bounded 1800s/30min < 3h. **Watch-item for nightly validation (C1, no ad-hoc):** any exporter/scraper class (smartx-exporter, inf-exporter) that could have a >3h LOW-CPU I/O/network-bound active phase — none observed (inf-exporter export bursts hit 14-18% > 3% threshold), but confirm on the scheduled runs that no legit job is false-reaped.

**Tests:** `test_enforcer.py` 10/10 pass (idle-reap / busy-spare / sub-ceiling-spare / None-coverage-conservative / AutoShutdown-disabled / demo-busy-spare / inf-exporter-idle-reap / hard-cap disabled+enabled). ds-commit-gate clean. `terraform plan` = 1 resource in-place (0 add/destroy).

**Immediate actions executed (Andrew GO):** inf-exporter i-081ae6aa STOPPED (was idle 0.3% the full prior 30min); **ALL 4/4** unattached EBS vols snapshotted (pre-delete insurance) then DELETED — vol-07e6ca7175ef9d1c1, vol-05425c3a28f7e2ca9, vol-0a6bb3594ff6393cc (bd-snapshot, 8GB ea), vol-0ba59aa26025649d5 (docker-builder-temp, 20GB). Snapshots retained: snap-05db82f8d4286a2ba, snap-01771ef4a3a1dcb3f, snap-06d7ff3c4fc26977f, snap-04d33fef82d0d16bf. (Reconciled 4/4 per CVO correction — an interim report read 3/4 while the docker-builder-temp snapshot was still completing.)

**demo-transform note:** the universal cap also handles it — once its live re-clone completes + goes idle 3h, the enforcer auto-reaps it (stop), no manual EXCLUDED maintenance. 0.6.0 still terminates at DEMOAUTH.002 close for full teardown.

---

## Underlying-bug flag (route to inf owner 0.5.0_AE_OpalETL, offline)

inf-exporter's 34-day uptime is the *symptom*; the *root cause* is its self-stop not firing on the export path (the 21:00 `opal-inf-export-run` SSM doc likely lacks the `shutdown -h now` that the jwt-fetch path has). The idle-ceiling backstop covers the cost regardless, but the self-stop bug should also be fixed. Routing to COO since 0.5.0_AE is offline.
