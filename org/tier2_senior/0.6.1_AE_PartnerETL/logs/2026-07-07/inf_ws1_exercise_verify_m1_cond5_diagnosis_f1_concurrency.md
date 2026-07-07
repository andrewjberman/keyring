# INF session -- WS-1 alarm exercise-verify (+CVO P1 catch), M1 condition-5 first-nightly DIAGNOSIS, F1 perf-pull concurrency BUILT+scale-gated+ratified

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT (primary -- F1), DIAGNOSE (condition-5 root-cause), VALIDATE (WS-1 + scale-gate), COORDINATE

**Date:** 2026-07-07 (window ~15:55Z - 16:30Z), fresh session continuing the 07-07 overnight backfill's open items.
**Task Order:** ad-hoc (ADVI_INFPERF F1 + ADVI_ETLFIX WS-1 exercise-prove -- CTO/COO/CVO coordination, no single TO).
**Status:** F1 BUILT + scale-gated PASS + CTO-RATIFIED, awaiting DS-lane commit routing (COO) then AE deploy then condition-5 proof on the 07-08 nightly. WS-1 certed (CVO), P1 owned by CloudOps.

---

## Objective

Close the two open items handed off from the overnight backfill: (1) the WS-1 all-step `ChainStepDegraded` alarm exercise-prove (CloudOps flagged it went live + caught the real degrade naturally), and (2) the ADVI_INFPERF M1 condition-5 proof on the first real scheduled nightly. Item 2 turned into a diagnosis (condition-5 FAILED at the 600s margin) that drove building F1 (the CTO-flagged concurrency-hardening follow-on) same-session.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| commit-gate.sh | on the F1 patch (pull_inflection_performance_rest.py) | PASS | py_compile + ds-precommit AST + ruff py39 all clean; the mandatory gate for the .py edit |
| comp-which | "how is the inf gold nightly scheduled + where are runner env vars set" | ROUTED (no fit) | routed to comp-freshness (data-freshness), which doesn't answer an infra-config/env-injection question; fell back to a rail-checked source grep of eventbridge.tf. Minor coverage gap noted -- no comp-tool maps "where is the runner env configured." |
| comp-pipescript deployed/postdeps | not run | N/A | no gold-chain trigger this session -- the scale-gate was a standalone `--dry-run` pull (bronze pull script), not a gold dispatch. Deploy is code-sync only, verified by ETag. |
| comp-iam / comp-blast | not run | N/A | no iam.tf / infra / boto3-surface change -- F1 is pure pull-script concurrency logic + a deterministic sort; zero IAM/blast surface. |

**What worked:** grounding the condition-5 result straight from the run log (300/312 @ 575s, 0 fails) let me state "not Orion-down, it's sequential-throughput" as a SOURCE-confirmed mechanism (Rule 22), which CTO explicitly praised and which correctly pointed the fix at F1 rather than an upstream wait.
**What failed:** nothing tool-side.
**Gap found:** comp-which has no route for "where is a pipeline's runner environment / schedule configured" (infra-config lens) -- it routes to data-freshness. Candidate for a comp-tool coverage note.

---

## Work Completed

### 1. WS-1 all-step ChainStepDegraded alarm -- exercise-verified, and CVO caught my bar was one level too high

CloudOps deployed `inf-gold-chain-step-degraded-allstep` (SUM over a Metrics-Insights SCHEMA query, all-step, no Step pin) and it went live already in ALARM on the real ongoing PERF degrade. I verified from live AWS: ActionsEnabled=true, AlarmActions -> SNS opal-partner-etl-ops-alerts, StateValue=ALARM, describe-alarm-history Action = "Successfully executed action ...opal-partner-etl-ops-alerts" (actionState=Succeeded) on the INSUFFICIENT_DATA->ALARM transition @14:34:55Z, and confirmed 2 live subscriptions (SMS +1786..., SQS partner-etl-ops-queue). I certed the exercise-proof at "action-Succeeded + confirmed subs."

**CVO (3.0.0_SA_CVO) went one level deeper and I was WRONG:** "AlarmAction Succeeded" = published-to-TOPIC only, blind to per-endpoint fan-out. CVO pulled the SNS topic delivery metrics for the fire: MessagesPublished=1, NotificationsDelivered=1, **NotificationsFailed=1** -- the SMS endpoint FAILED (account in SNS SMS sandbox, +1786... number status Pending / OTP never completed -> SNS drops SMS). The human SMS pager for the whole ops topic is dark; only SQS delivers (and the queue had ZERO consumers ever wired). This is a measured P1, not "unprovable receipt." Banked as memory `feedback_sns_action_succeeded_not_endpoint_delivered` (ties to Rule 22a -- a "pages" claim's exercised path ends at endpoint delivery, not the alarm action). CVO PASS'd the alarm-logic deliverable + authorized the per-step PERF retirement (all-step is a strict superset).

**Actions:** told CloudOps per-step PERF retire is authorized (they're retiring it); routed the P1 to CloudOps as topic/alarm-infra owner (me CC + WS-1 design owner). CloudOps took it: building a TF-managed SQS-consumer -> SES email Lambda as the durable fix (ships today, no SMS-sandbox dependency; sandbox-exit parked for Andrew/console). I re-verify (endpoint-delivery-grounded this time) when the consumer's live.

### 2. M1 condition-5 -- first real scheduled nightly DIAGNOSIS: FAILED the <600s gate at the margin, SAFELY

A real scheduled full chain ran + completed today (`chain_full_20260707_133419.log`, completed 15:00:59Z) -- the condition-5 event. Result: NOT met, but safely.
- INF_API_PULL_PERF ran mode=incremental (M1 cutover IS live). Progress: [300/312]=575.1s, then exit=124 at the 600s `PULL_STEP_TIMEOUT` wall. 297 ok / 296 incremental / 3 escalated / 2 empty / **0 fail**.
- bronze/performance did NOT advance (still 06-30, 7 days stuck). Silver deferred (carry-forward), ChainStepDegraded=1 + TxnSilverStalenessDays=5 emitted, within the 10-day ceiling. Chain COMPLETE, served fresh (TXN/AUA current), NO freeze -- the durability engineering absorbed it. This is the naturally-occurring degrade that fired WS-1.

**Mechanism (source-grounded, not inferred):** NOT "Orion down" (0 fail, 297 ok -- Orion returns data fine). The bottleneck is single-threaded sequential pull: ~1.9s/client x 312 > 600s. The M1 scale-gate was 1.72s/client (536.5s); current per-call latency crept ~11% and blew the ~10% headroom CTO flagged. => F1 (concurrency) is the critical-path fix; the data is available, we just can't pull 312 sequentially in 600s.

### 3. ADVI_INFPERF F1 -- perf-pull concurrency hardening (BUILT, scale-gated, CTO-ratified)

CTO NOD'd the approach (I asked before cutting code, given how heavily M1 was gated). Built entirely inside the pull script, `rate_limiter.py` UNTOUCHED (shared by other sequential pull scripts -- zero blast radius):
- Bounded `ThreadPoolExecutor` (`--workers`, default 8, env `PERF_PULL_WORKERS`) over the per-client loop; results drained on the main thread as futures complete (counters + all_rows single-writer, no lock).
- Thread-safe `_ConcurrentLimiter` adapter wrapping `AdaptiveRateLimiter`: a shared next-slot pacer keyed on `current_rps()` holds AGGREGATE request rate <= the adaptive ceiling (Orion sees the same rate as sequential, wall-clock-compressed by decoupling pacing from the in-flight network wait); `observe_call`/`flush`/`persist_state` lock-serialized. Per-client fetch/chain-link functions unchanged -> concurrency is math-invariant.
- Deterministic (client_id, date) sort before write -> byte-stable artifact regardless of thread completion order.
- `--state-dim` (default "performance") so a scale-gate uses a scratch rate-limit state file -> zero prod-state pollution.

**Validation (CTO's gate discipline):**
- commit-gate.sh clean (py_compile + AST + ruff). Diff 140+/34-.
- Smoke (5 clients, 8 workers, parity, dry-run): parity 6.66e-16 (machine-zero), 5/5 ok, integrity clean.
- Full-312 scale-gate (prod-seeded scratch state for representative timing, dry-run): pull **154.5s** / run+parity 179.6s -- both << 600s (~74% margin), vs the nightly's 575s->600s-timeout = **~3.7x**. Parity PASS 8.27e-06 @ 2026-05-31 (<< tol 1e-4). Integrity 310/310 anchored@1.0. **Adaptive fallback proven thread-safe LIVE:** a real 6x503 ConnectionReset burst (clients 446-452) triggered FALLBACK 5.173->4.173 + retries recovered -> 0 final fails. 211 non-positive rows = the pre-existing F2 (4 escalated full-path clients; incrementals can't produce them), not an F1 regression.

**CTO RATIFIED** ("excellent work, ratified. No further ruling needed. Proceed to deploy once it lands; RAVC the condition-5 proof on the 07-08 nightly").

### 4. Stopgap (PULL_STEP_TIMEOUT 600->900s) -- CTO-approved, HELD as fallback (not applied)

Grounded: nothing currently sets `PULL_STEP_TIMEOUT` (defaults to 600 via `timeout -k30 ${PULL_STEP_TIMEOUT:-600}` at orion-gold-dispatch.sh:586); the nightly is EventBridge-cron at ~13:30-14:00 UTC (next perf run ~24h out). Since F1 is same-day and applying the stopgap needs net-new env-injection plumbing through the inf-gold-trigger Lambda/EC2, I proposed holding it as a fallback (apply only if F1 slips past the 07-08 ~13:34Z run). CTO agreed. Worst case if wrong: one more harmless in-ceiling defer, not a freeze.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Diagnose condition-5 as F1-margin (not Orion outage) | Run log: 0 fail / 297 ok = Orion returns data; 300/312 @ 575s = sequential throughput vs the 600s wall. Source-confirmed mechanism (Rule 22), not inferred. |
| Build F1 inside the pull script; do NOT modify rate_limiter.py | rate_limiter.py is DS-authored + shared by other SEQUENTIAL pull scripts; a global-pacer change there would blast-radius them. Wrap-don't-modify = zero blast radius. |
| `_ConcurrentLimiter` pacer keyed on current_rps + lock-serialized observe_call | Preserves the adaptive rate semantics exactly (Orion sees the same ceiling) while decoupling pacing from the network wait -- the whole speedup. Adaptive feedback still fires (proven by the live 503 fallback). |
| Scale-gate with a prod-SEEDED SCRATCH state-dim + dry-run | Representative timing (resumes at prod 4.173 rps) with zero prod-state pollution and zero bronze mutation -- validate the thing that ships, no side effects. |
| Hold the stopgap as fallback vs apply pre-emptively | F1 is same-day, next run ~24h out, stopgap needs real env-injection plumbing + a revert; applying it pre-emptively is net-negative if F1 lands first (very likely). |
| Route the F1 commit through COO (not force-bypass) | data/inf/manual_api is DS-authoring-lane (rule 13, owned-paths-blocked on M1); INF DS lane is offline; F1 isn't urgent -> clean DS-lane commit via COO's driver, not an audited bypass. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/inf/manual_api/pull_inflection_performance_rest.py` | F1 concurrency: ThreadPoolExecutor + `_ConcurrentLimiter` + `--workers`/`--state-dim` + deterministic sort (+140/-34) | NOT YET -- validated in working tree, awaiting DS-lane commit routing (COO); local sha dbcf64a7 |
| `memory/feedback_sns_action_succeeded_not_endpoint_delivered.md` (+ MEMORY_FULL pointer) | banked the CVO "action-Succeeded != endpoint-delivered" lesson | committed via memory dir (not repo) |

**AE deploy actions:** NONE yet -- F1 deploy (code/manual_api + code/gold + code/bronze, byte-identical, ETag-verified) is pre-staged (all 3 homes currently at pre-F1 ETag 9a3ca1a7, 29230b) and fires the instant the commit lands.

---

## Blockers

None BLOCKED-class on me. F1 commit is gated on COO raising the offline INF DS lane (or authorizing an audited force-bypass) -- asked, COO is live. WS-1 re-exercise is gated on CloudOps's SES-consumer build (in flight). condition-5 proof is gated on the 07-08 ~13:34Z scheduled nightly (the correct validate-on-scheduled-artifact path; no ad-hoc trigger).

---

## Current State (zero-context handoff)

- **F1 is built, gate-clean, scale-gate PASS, CTO-ratified** -- sitting validated in the working tree (data/inf/manual_api/pull_inflection_performance_rest.py, +140/-34). Next mechanical steps: DS-lane commit (COO routing) -> AE multi-home deploy (pre-staged) -> the 07-08 nightly picks up `--mode incremental` automatically (no dispatch change), the concurrent pull completes <600s, bronze/performance goes fresh, the 7-day perf carry-forward clears -> RAVC CTO the condition-5 proof on that live run.
- **WS-1**: all-step alarm certed PASS (CVO), per-step PERF retirement in progress (CloudOps). P1 = the topic's SMS pager is provably dark (SNS sandbox + unverified number) -- CloudOps owns the durable fix (SQS-consumer -> SES email Lambda, ships today); I re-exercise-verify (endpoint-delivery-grounded) when live.
- **Holds/reverts**: stopgap PULL_STEP_TIMEOUT 900 held as fallback (never applied). PERF_SILVER_STALENESS_CEILING_DAYS stays 10. Both reverts (timeout->600 if ever applied; ceiling 10->2, pending DS~A holiday-aware fix) bundled into F1's closeout post-clean-nightly, per CTO.

---

## Next Steps

1. **[0.6.1 / COO]** Land the F1 DS-lane commit (COO routing) -> then AE deploy code/manual_api+gold+bronze (byte-identical, ETag-verify).
2. **[0.6.1]** RAVC CTO the condition-5 proof on the 07-08 ~13:34Z nightly (bronze/performance fresh + INF_API_PULL_PERF <600s on the real concurrent run).
3. **[0.6.1]** F1 closeout: bundle the ceiling 10->2 revert (with DS~A's holiday-aware staleness fix) + stopgap revert if applied; RAVC CTO.
4. **[0.6.1 / CloudOps]** WS-1 re-exercise-verify once the SES-consumer Lambda is live -- confirm NotificationsFailed=0 + the email actually lands.
5. **[filed, not urgent]** comp-which coverage gap (no route for "where is a runner's env/schedule configured").

## Contacts

CTO=1.0.0_SA_CTO (F1 nod+ratify, condition-5 gate), COO=2.0.0_SA_COO (F1 commit routing, drive), CVO=3.0.0_SA_CVO (WS-1 cert + the SMS-pager-dark P1 catch), 0.7.0_AE_CloudOps (WS-1 alarm build + P1 SES-consumer owner), DS INF lane=0.4.0_DS_ClientPlatform~B (offline -- F1 commit target per rule 13).
