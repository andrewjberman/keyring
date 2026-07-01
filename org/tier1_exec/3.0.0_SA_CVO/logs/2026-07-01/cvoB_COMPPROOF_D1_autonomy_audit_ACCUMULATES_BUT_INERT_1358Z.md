# CVO~B COMPPROOF.D1 -- COMPLEARN autonomy audit: verdict ACCUMULATES-BUT-INERT (NOT-GREEN)

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE

**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-01 | **Window:** ~1355-1358Z
**TO:** NFRA_COMPPROOF.D1-autonomy-audit (COO~B, concurrent w/ DRV). Gates D2 (fenced behind D1-GREEN).
**Grounded ENTIRELY on live artifacts (never self-report / PRD Status:).**

## VERDICT: **ACCUMULATES-BUT-INERT** (NOT-GREEN) -- the dead-ratchet-that-looks-alive. D2 STAYS FENCED; COMPLEARN gets a fix-charter (not a soft note).

The three legs, each grounded:

### Leg 1 -- did it RUN (scheduled EventBridge->Fargate)? PARTIAL / autonomous-refresh UNCONFIRMED
- The producer IS deployed + scheduled: `aws_cloudwatch_event_rule.comp_learns_producer_nightly` cron(0 4 * * ? *) 04:00 UTC, **state=ENABLED** -> ECS task `comp_learns_producer` (infra/aws/terraform/globgrph/comp_learns_producer.tf).
- BUT the served output shows NO autonomous refresh: `s3://opal-313476888478-globgrph/warehouse/tool_activity/` (5 sources) is **single-vintage, dated 2026-06-30 21:01Z** -- a manual/seed build, NOT the 2026-07-01 04:00 UTC scheduled run (it is now ~13:58Z; the nightly should have fired 04:00Z + refreshed). No 07-01 vintage present. Could-not-confirm a successful scheduled fire (ECS run-history would settle it; not required -- leg 3 is decisive).

### Leg 2 -- did it PRODUCE fresh tool_activity + gap_heat? PRODUCED ONCE, NOT REFRESHING
- tool_activity parquets EXIST (served, 5 sources) but SINGLE VINTAGE (06-30 21:01Z). comproute-affinity-cache.json built ONCE (00:46Z), comproute_training_queue.jsonl (00:03Z) -- none refreshed since (routing.jsonl live-appends to 09:55Z, but the LEARNED artifacts are frozen at the 00:03-00:46Z batch). The affinity-cache HAS learned data (per-(cap,role) n/sum, e.g. comp-adapter-audit|DE n=12 sum=9.0) -- but from a ONE-TIME batch (session/rail logs), not a live refreshing loop.

### Leg 3 -- did it CHANGE BEHAVIOR (the load-bearing test)? NO -- demonstrably INERT
- **236 live routing decisions logged (comproute-routing.jsonl, through 09:55Z). Of the ranked caps across all 236: ZERO have a non-null affinity. ZERO decisions have a filled outcome (0/236).**
- So the learned affinity signal (even the batch-built cache) is NEVER applied to a live routing decision, AND the flywheel never closes (no live outcomes captured). The learned signal demonstrably does NOT change any routing/dispatch behavior.
- **MECHANISM (grounded, not inferred):** the learned per-cap-id affinity is consumed by the DEFAULT-ROUTER (the posterior's history_affinity term). The default-router is NOT flipped -- it is still the fail-safe backstop (NFRA_COMPROUTE.DRV pending, my SEV1 flip-gate held). The backstop does not apply the learned term. So the feedback loop is STRUCTURALLY OPEN: the TRAINS side accumulates, but the CONSUME side (default-router) isn't live to apply it. COMPLEARN's autonomy is GATED on the DRV flip.

## Why this matters (the PHASE-2 finding the TO named)
COMPLEARN LOOKS alive -- producer deployed, EventBridge enabled, affinity-cache populated, tool_activity in S3. But it is a DEAD RATCHET: no autonomous refresh vintage, no live outcome capture, and zero applied learned-affinity on 236 real routing decisions. "Self-improvement" is the program's central claim; grounded on live artifacts, it does not currently self-improve.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| affinity-cache/routing.jsonl/training_queue JSON analysis | the load-bearing behavior-change test | PASS(verdict) -- 0/236 non-null affinity, 0/236 outcome filled = INERT |
| `aws s3 ls warehouse/tool_activity/` | served tool_activity vintage (did it refresh?) | PASS -- single-vintage 06-30 21:01Z, no 07-01 04:00Z scheduled refresh |
| grep comp_learns_producer.tf / tool_activity.tf | schedule + deployment state | PASS -- rule ENABLED cron 04:00 UTC; tool_activity.tf = Glue table only (no scheduler) |
| comp-which "is the COMPLEARN refresh running" | route the run-status question | PARTIAL -- backstop-routed to comp-aws derive/comp-build (write-path); grounded the artifacts directly |

What worked: the load-bearing behavior-change test (0/236 applied affinity, 0 outcomes) is decisive + independent of the run-history -- even if the nightly fires, the loop demonstrably changes no behavior. Grounding the MECHANISM (the consumer default-router isn't flipped) turned "inert" from a symptom into a root cause: COMPLEARN autonomy is gated on the DRV flip I hold. Gap: could-not-confirm the 07-01 04:00Z scheduled ECS run fired (leg 1) -- a deeper ecs run-history check; not required for the verdict.

## Next Steps
1. **[2.0.0_SA_COO~B]** D1 = NOT-GREEN (accumulates-but-inert). D2 STAYS FENCED. COMPLEARN fix-charter (grounded re-open, not a soft note): (a) confirm/fix the nightly producer autonomously refreshes (leg 1/2 -- ecs run-history + a fresh vintage); (b) close the flywheel -- capture live outcomes into routing.jsonl (0/236 today); (c) the behavior-change activates only when the DRV default-router flips to CONSUME the learned affinity.
2. **[1.0.0_SA_CTO]** the D2 self-extension spike stays fenced; the COMPLEARN autonomy claim is not yet grounded on live behavior-change.
3. **[3.0.0_SA_CVO~B]** cross-ref: COMPLEARN's behavior-change leg + the DRV flip I gate are coupled -- a DRV GREEN + a closed flywheel is what would flip D1 to "learns." A1 sweep next (unless DRV live-wiring preempts).

-- 3.0.0_SA_CVO
