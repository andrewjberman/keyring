# CVO REVIEW -- P2 UNIFIED MORNING SCHEDULE / TIMING MAP SPEC @4e1ec757f8 (CRO base)

**Reviewer:** 3.0.0_SA_CVO · **2026-08-11 ~2010Z** · **archetype:** REVIEW (instrument lens).
**Protocol:** CRO authors -> **CVO reviews (this)** -> CTO ratifies -> AE implements at P2-open.
**Verdict: CONCUR -- the spec is sound and well-grounded. Ratifiable with 2 instrument additions + 1
tradeoff that is Andrew's, correctly routed by CRO (not adjudicated).**

## THE HEADLINE FINDING (S5) IS CORRECT AND LOAD-BEARING
The ADVI-morning-ready premise does NOT hold for inf/Orion, and CRO grounded it rather than assumed it
past: Orion lands ~14:16Z (MEASURED, MDPF_PIPELINE_TRUTH.md:120-137 + a corroborating comp-freshness
read), AFTER the mdpf floor (13:30Z, RULED). So any Orion-sourced inf leg is stale-as-of-floor EVERY
DAY BY CONSTRUCTION, not intermittently. **The sharpest thing in the spec, and I endorse it: the §1
correction that the "13:31Z" figure is when a freshness-CHECK LAMBDA FIRES, ~45min BEFORE Orion's own
data exists -- "a wrongly-timed CHECK, not a wrongly-timed vendor."** That is the check-the-right-layer
discipline exactly: the daily "gap" the bar shows is an instrument-timing artifact, and reading it as a
vendor-staleness finding is the error the correction prevents. This alone earns the spec its keep.

## THE RECOMMENDATION IS BUILD-LADDER-ALIGNED -- I CONCUR
CRO recommends extending mdpf's ALREADY-RATIFIED carry-forward + accelerator-heal pattern
(scheduled-floor.tf:120-127, DS-option-A / COO-endorsed) to inf's gold runner, over forking a later
ADVI-specific floor. This REUSES an existing ratified pattern rather than building a new floor regime
(the "estate already has it" rung), and it preserves the "unified" half of Andrew's word. Concur as the
default.

## THE ONE TRADEOFF THAT IS ANDREW'S (surface, do not adjudicate)
Does inf's OWN gold runner take the mdpf carry-forward treatment (one unified floor), OR does an
ADVI-specific floor sit later than 14:16Z + inf's chain margin (a schedule FORK that contradicts
"unified")? CRO correctly did NOT rule this. **My instrument read: the unified-floor + carry-forward
option is strictly better on the axes I can measure** -- it reuses a ratified pattern, keeps one floor,
and the "stale at floor" it accepts is honestly carry/participation-labeled and heals on the accelerator
(never stale-presented-as-complete). A later ADVI-specific floor buys fresher-at-floor at the cost of a
fork and a second schedule to maintain. **But whether "unified" tolerates a labeled-carry inf leg is a
scope call on Andrew's own word -- his to bound.** Route with my concurrence on the mdpf-pattern default.

## TWO INSTRUMENT ADDITIONS (my review contribution -- neither blocks ratification)
1. **The §2 floor anchors are tf-DECLARED (desired), not live-verified (applied).** They cite `.tf`
   crons -- correct for what is DECLARED, but a tf-grep cannot catch a schedule that drifted in AWS but
   not terraform. §3 already mandates the live both-namespace API sweep as a P2 prerequisite; state
   explicitly that the §2 floors are PROPOSED-FROM-TF and become RULED only after that live sweep
   confirms applied == desired per pipeline. (Rule-22a: desired and applied are different layers.)
2. **The closed-world dispatch roster {events, scheduler} answers "has a SCHEDULE?" but NOT "is it
   EVENT-ONLY-triggered?" -- and those are different states with the SAME two-namespace result.** A
   pipeline absent from BOTH namespaces is either DEAD (no trigger at all) or EVENT-ONLY (the NEVER#4
   defect: triggered solely by an upstream marker / S3 event, no schedule). The two-namespace sweep
   returns "no schedule" for both, indistinguishably. Since surfacing the NEVER#4 event-only defect is
   half of why P2 exists, the schedule-existence sweep must be PAIRED with a trigger-characterization
   check (S3-event notifications + Lambda-invoke source) to tell dead from event-only. §3 names the
   two-namespace sweep; add the trigger check beside it, or a "no schedule" result cannot be classified.

## THE ATTACK SURFACE CRO NAMED -- checked
- **§1 confidence column: no row too generous.** BD-REST is honestly SOVEREIGN-STATED (Andrew's word +
  consistent sentinels, "not independent proof"); Orion MEASURED (~, appropriately approximate); cot
  rebalancer DEPLOYED-VALUE-UNRULED (placeholder, self-marked). Each certainty is qualified to what it
  actually is.
- **The unlocatable "10:20Z same-S3-event replay" specimen (§6): correctly flagged NOT-LOCATED, not
  fabricated.** That is the right move (say the source is absent rather than invent a citation). It IS a
  real gap -- the commission cited a specimen that is not in the record as searched; CTO/commission owns
  reconciling whether it was mis-named or uncommitted.
- **§7 note:** CRO's routing message referenced "§7 worked examples / seven FP classes" -- that belongs
  to the P5 DEBT-ID METHODOLOGY spec (already CVO-reviewed + CTO-ratified), NOT this P2 timing spec,
  which has no §7. No gap here; a cross-reference between two commissions.

## GAPS (§6) -- all honestly named with owner-shaped next steps
cot N-date sample (P2 prereq), inf/cot Group W A1-A5 pages absent (comp-find 0/25,498), inf
event-trigger build unconfirmed. Each names its owner. Good.

-- 3.0.0_SA_CVO
