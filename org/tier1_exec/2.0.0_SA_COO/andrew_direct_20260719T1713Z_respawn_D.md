# Andrew-direct record -- ~D reactivation (2026-07-19 ~17:13Z)

**Protocol:** Andrew-direct RECORD + BROADCAST (org/XXX.md). Recorded durably by 2.0.0_SA_COO same-turn.

## Verbatim (do NOT paraphrase -- the phrasing IS the ruling)

> "~D is not active, coo needs to get on this"

- **Channel:** relayed VERBATIM by 3.0.0_SA_CVO (Andrew-direct to the CVO session), inbox msg `20260719T171542Z_3.0.0_SA_CVO`.
- **Time:** 2026-07-19 ~17:13Z.
- **Named actor:** 2.0.0_SA_COO (COO drives).

## Scope (SURFACE, do not adjudicate -- but the named target is explicit)

- Releases **0.8.0_AE_CloudComp~D SPECIFICALLY.** Confirmed dark: `get_live_agents` @17:13Z = only MSTR/CTO/COO/CVO; MSTR + CTO independently grounded ~D absent from the broker.
- **Does NOT widen to the wave.** ~A / ~Z / ~B (incl. the 07-23 audit-invoker) have NO Andrew word -- they stay HELD (RV-0052 F-007). CTO + MSTR both flagged this scope guard; do not over-read "coo needs to get on this" as a blanket wave release.
- This is the sequencing word the ~D leg of the respawn wave was held for.

## Execution (COO-driven, MSTR-executed)

- **Spawn:** GO to MSTR `20260719T171858Z` -> `/mstr-spawn 0.8.0_AE_CloudComp~D` + broker-registration verify (MSTR's lane/mechanism). COO owns tasking/sequencing + drive-to-closure.
- **~D resume target:** NFRA_COMPSIMILAR PH2-C2 motif-enrich (interrupted mid-build by the 07-19 crash; last landed @2cf90c507, LD-0315 variance arc; SERVED_LINEAGE class delivered @4c57b963a, other 3 classes DEPLOY/AUTH/PIPELINE at CTO role-key + source-wiring @a0ff6f769). PH2 engine-supersede stays STAGED behind CTO arch-gate.
- **Gates:** CTO normal (comp-manifest-check; plan-gate + live 22a IAM sim for any store-writer/apply).
- **Downstream:** on ~D PH2-C2 build-land -> ping COO + CVO -> CVO exercises held item-2 (COMPSIMILAR PH2 semantic-axis: variance magnitude/parity on live firm bucket) same-turn.

## Broadcast (same-turn, per protocol)

- MSTR `20260719T171712Z` (spawn directive) + `171858Z` (GO).
- CTO `20260719T171718Z` (build-lane + scope guard).
- CVO `20260719T171722Z` (ACK relay).

## Discharge condition

This drive DISCHARGES when ~D is (a) LIVE on the broker AND (b) its PH2-C2 build has resumed (first substantive commit or a clear blocker surfaced to COO). Until then COO owns it; if the COO session ends first, the successor picks this up from this file.

**Status update 172221Z: ~D LIVE (PID 25024, broker-confirmed; MSTR spawn clean -- 0 identity collision, concurrency 0/16; independent broker read by COO = 2 signals). Condition (a) MET.** ~D came up, armed watcher (Monitor bh9gvom39/own), grounding its exact PH2-C2 state.

**Awaiting condition (b) -- and note the real forward gate:** per ~D's own logs, PH2-C2 `SERVED_LINEAGE` class is DELIVERED @4c57b963a; the other 3 classes (DEPLOY code-prefix / AUTH comp-routes / PIPELINE pipescript) sit at a HARD EXTERNAL GATE = **CTO arch-gate role-key blessing (@a0ff6f769 mapping) + per-class source-wiring**. The normal relay (base 0.8.0_AE) is DARK post-crash, so COO bridges: when ~D surfaces its grounded state, drive the CTO arch-gate for the 3 role-keys so ~D isn't immediately re-blocked. CTO already primed (gate-ready, its msg 171737Z). CVO exercises on build-land.

**Scope reminder for the successor:** ~D holds 14 pending TOs (COMPSIMILAR PH1/PH2-C2, COMPLEARN AMD-P3b/c/d, PASSCRAFT TO-1/2/3, TOOLGRAPH TO-1/2, KUZUSPLIT P0-P1, GRAPHFEED W1, OPAL_ASSETS P0-A, CONSOLIDATION P3-census). Andrew's word reactivated ~D for the PH2-C2 priority; the rest stay on their existing gates/sequencing -- do NOT read the reactivation as a GO on the whole queue.

## DISCHARGED 173936Z -- both conditions MET (+ a self-correction ~D caught)

**~D active (a) AND PH2-C2 build resumed + COMPLETED (b) = drive DISCHARGED.** ~D came up clean (watcher bs1gsnh6o, LD-0290 serial, own-state reconciled), resumed PH2-C2, and marked the TO COMPLETE @ccb6c928e (AC 1-6 met, live-exercised on the 07-19 graph: self-test 10/10, comp-describe opal-data-bd renders the SERVED_LINEAGE clause / opal-data-mdpf graceful, --build coverage 5-matched/1785-unmatched as arch-gated). COO validated all evidence per RAVC before accepting. Elapsed 17:13Z (Andrew) -> 17:22Z (~D live) -> 17:39Z (PH2-C2 complete).

**CORRECTION (records-honesty -- ~D caught a stale claim in the 172221Z update above):** the update named "CTO arch-gate role-key blessing (@a0ff6f769)" as an OPEN forward gate needing a COO bridge. **That was WRONG -- the blessing had ALREADY LANDED ~27h earlier:** CTO blessed SERVED_LINEAGE roles @ddfe05ae9 (07-17 23:40) and PIPELINE/AUTH/DEPLOY roles + SERVED_LINEAGE drift-refresh @e462e04da (07-18 10:13). Root cause: I inferred the gate from ~D's PRE-blessing session logs (they listed it as a pending next-step) instead of grounding on git/live state -- a stale-record-speaks-with-authority miss. ~D grounded it on the live graph and corrected me. No COO bridge was needed; none issued. Lesson banked: ground a forward-gate claim on git/live, never on another agent's prior next-steps.

**Follow-on 3 classes (DEPLOY/AUTH/PIPELINE) -- TRACKED, not active:** role-keys ARE CTO-blessed, but instance-grain sources are UNWIRED on the live graph (~D verified via comp-kuzu 07-19: DEPLOY 0 code/-prefix nodes, AUTH 0 route-triggers, PIPELINE no FEEDS edge). Each is a SEPARATE source-gated increment in an upstream domain (DEPLOY->0.7.0 globgrph extractor / AUTH->comp-routes adapter / PIPELINE->pipescript adapter), explicitly deferred by the PH2-C2 TO's own AC ("follow as source is wired"). NOT reopened; NOT dispatched (no fabric intent to fire them yet). COO sequences each against its source owner if/when the fabric wants that class fired. CVO exercising its held semantic-axis check on ~D's build-land ping.
