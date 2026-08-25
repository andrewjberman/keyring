<task_order>
<id>NFRA_COMPLEARN.AMD-P3a</id>
<title>AMENDMENT P3a -- leg-3 robustness: audit the 5 behavior sources (cloud-ship vs explicit-host-local-with-alarm), promote the staleness watch to a HARD freshness gate, and make the "nightly Fargate emit" claim TRUE or DELETE it</title>
<issued_to>0.7.0_AE_CloudOps **LANE (~A -- base is ANDREW-RESERVED for Schwab ad-hoc)** for the scheduled cloud job + infra. **STAGED -- DO NOT ISSUE. DOUBLE-GATED: (1) 0.7.0 IS ANDREW'S (COO~A constraint #1, Andrew-direct 2026-07-10) -- COO~A cannot dispatch this at all until Andrew stands up a 0.7.0 lane or assigns it; (2) builder-spawn-gated (the 0.7.0 lane is unspawned). DECOMPOSED + STAGED per CTO~A mandate; marked ANDREW-GATED-ON-SPAWN.**</issued_to>
<issued_by>2.0.0_SA_COO~A (PRD decomposition 2026-07-10; returned to 1.0.0_SA_CTO~A for the arch-gate. NOT dispatched -- 0.7.0 is Andrew's.)</issued_by>
<issued_date>2026-07-10</issued_date>
<status>complete -- SPRING-CLEAN 2026-08-25 (S2): <project> field repaired from "NFRA_COMPLEARN (amendment: NFRA_COMPLEARN_amend_loop-closure" to NFRA_COMPLEARN, which is complete. Closed as a record act, not a work verdict. Prior status: pending</status>
<dispatch>DISPATCHED 2026-07-10 by 2.0.0_SA_COO~A -> 0.7.0_AE_CloudOps~B (Andrew-cleared as OURS via CTO~A relay; 0.7.0 base + ~A remain Andrew's -- off-limits). Agent-queue pointer: org/tier2_senior/0.7.0_AE_CloudOps/task_orders/NFRA_COMPLEARN.AMD-P3a.leg3-producer-robustness.md. NON-URGENT LAST leg -- leads behind the 0.8.0 P1 foundations. Route diffs to 1.0.0_SA_CTO~A.</dispatch>
<priority>P3a -- CloudOps infra. **THE hard gate of the amendment: it cannot leave STAGED until Andrew resolves the 0.7.0 assignment.** Leg-3 currently reads as CLOSED and is not (a single-host cron wearing the correct-but-unwired + terminal-lies-to-artifact mask) -- worse than an honest gap, so it is the amendment's priority once un-gated.</priority>
<project>NFRA_COMPLEARN</project>

<context>
`infra/aws/globgrph/tool_activity_emit.py` (a SessionEnd-hook + host-local schedule) writes the `tool_activity` catalog -- but it is host-local, not cloud (3 of 5 behavior sources are gitignored/host-only, so no Fargate can emit the full catalog), and it went 2d+ SILENTLY STALE behind a comment claiming a nightly EventBridge->Fargate emit that "was NEVER materialized." Leg-3 is not missing; it is a single-host cron wearing a failure mask that reads as closed.
</context>

<scope>
1. **Audit the 5 behavior sources;** per source decide: **cloud-ship** (EventBridge->Fargate, the gold-run pattern, for the git-tracked sources) vs **explicit-host-local-with-alarm** (for the irreducibly host-only ones -- make the constraint LOUD, not a comment).
2. **Promote the staleness watch to a HARD freshness gate:** a stale `tool_activity` blocks / loudly alarms, NEVER silently serves stale.
3. **Resolve the false claim:** make the "nightly Fargate emit" claim TRUE (locate/stand up the actual scheduled invoker, live) or DELETE it.
</scope>

<locked_invariants note="CTO~A arch-gate checks these">
  1. **"MAKE THE CLAIM TRUE OR DELETE IT":** no comment may assert an emit that does not run. Either the nightly Fargate emit exists (verified by locating the actual scheduled invoker, LIVE) or the claim is removed.
  2. **FRESHNESS IS A HARD GATE, exercised by going stale:** the gate is proven by letting the catalog go stale and OBSERVING the alarm/block -- not by a comment (AC-L3a). A staleness watch that cannot be shown to fire has not been shown to work (the "census of survived failures" trap).
  3. **EVERY host-only source DISCLOSED as host-only with an alarm** -- no source silently absent from the cloud catalog (AC-L3b).
  4. **0.7.0 IS ANDREW'S:** this TO does not dispatch. Surface the 0.7.0-assignment decision to Andrew; do not adjudicate it.
  5. **BOUNDARY (sovereign):** no bd / 49F / Schwab read or target.
</locked_invariants>

<acceptance_criteria>
  - **AC-L3a:** `tool_activity` freshness is a HARD gate (stale -> block or loud alarm), EXERCISED by letting it go stale and observing the alarm/block; the "nightly Fargate emit" claim is made true (actual scheduled invoker located live) or removed.
  - **AC-L3b:** every host-only source is DISCLOSED as host-only with an alarm; no source silently absent from the cloud catalog.
</acceptance_criteria>

<references>
  <ref type="amendment">docs/architecture/NFRA_COMPLEARN_amend_loop-closure_20260710.md @ 362272cce (A1 P3a, A2 AC-L3a/b)</ref>
  <ref type="parent-prd">docs/architecture/NFRA_COMPLEARN_PRD.md (the parent P3 this amendment drives to done)</ref>
  <ref type="producer">infra/aws/globgrph/tool_activity_emit.py (the fragile host-local producer)</ref>
  <ref type="pattern">the gold-run EventBridge->Fargate scheduled pattern (the cloud-ship target for git-tracked sources)</ref>
</references>

<data_reprocess_scope><no_reprocess_needed>Infra (scheduled producer + freshness gate). tool_activity catalog is an observability substrate, not a served pipeline artifact.</no_reprocess_needed></data_reprocess_scope>
</task_order>
