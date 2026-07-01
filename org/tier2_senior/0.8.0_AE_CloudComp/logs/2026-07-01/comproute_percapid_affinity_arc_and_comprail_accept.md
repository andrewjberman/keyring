# NFRA_COMPROUTE per-cap-id affinity arc (flywheel + engine + shadow provider) + COMPRAIL close-accept

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE, DIAGNOSE
**Serial:** 0.8.0_AE_CloudComp~E
**Date:** 2026-07-01
**Window:** since the L4-seam log (37928970b) ~0419Z -> ~0505Z (the affinity arc was NOT in the TO-5 log)

## Current State

Two threads since the L4-seam log: (A) the COMPROUTE per-cap-id affinity ARC -- 3 commits, all landed +
CTO-validated; (B) COMPRAIL TO-5 accepted with a COO HOLD disposition (the TO-5 BUILD is in its own log;
this captures the affinity arc it skipped + the TO-5 acceptance).

## A. COMPROUTE per-cap-id affinity arc (CTO seq steps 1+2 + the flywheel ingest)

Triggered by L4 landing (~C 442633124 -- my posterior LIVE in comp-which as a fail-safe grep-tail
backstop, emitting each route()'s training_row to org/mcp/comproute-routing.jsonl).

**A1. Flywheel INGEST -- `51c37dcb4`.** `parse_routing_log` in comp_learns_score.py: the live router's
route rows now feed the P2 scorer; a DISAMBIGUATION (the router hedged a near-tie) becomes a
routing-friction candidate (a curated comp-which rule / keyword refinement would sharpen it, LD-0226);
a confident decision is healthy, not a candidate. Verified: scorer ingests routing=4 real rows. Sink
gitignored + rotated (ingest-side hygiene).

**A2. GROUNDED FINDING -> CTO grain ruling.** I surfaced that the L3 engine keyed history_affinity by
affinity_key=SURFACE, which is (i) redundant with surface_prior and (ii) useless for the hard case
(two same-surface tools get the same value). ~C confirmed provider-side: cap.id is already exposed, no
L2 change. CTO RULED (a) per-cap-id + m-estimate prior=surface-grain (subsumes the (c) hybrid).

**A3. Engine per-cap-id keying -- `f64083634` (CTO-approved change to accepted L3).** _score_one keys the
LEARNED term (w_h) by cap.id; PRIOR (w_s) stays surface-keyed; m-estimate prior = the cap's surface_prior
so a cold cap backs off, a hot cap converges to its per-cap outcome mean. Proven: self-test 14/14 --
affinity.per_cap_disambiguates_same_surface (no-aff=disambiguation -> with-aff=confident decision, the
same-surface tie the surface-grain term could NOT break) + cold_cap_backs_off_to_surface_prior. pytest
18/18. No L2/route()-signature break.

**A4. CachedAffinityProvider -- `5434b66aa` (SHADOW, CTO seq step 2).** org/modules/graph/comp_route_affinity.py:
fast O(1) provider off a per-cap-id cache (sufficient stats {sum,n}); applies the m-estimate with the
runtime surface_prior; filtered to real cap-ids. self-test 4/4 incl. usage_does_not_rescue_low_outcome
(100 FAILs -> 0.024). SHADOW: comp-which keeps affinity=None; computed+logged, not weighting live.
GROUNDED OBSERVATION: the live emit (213 real-cap entries) is near-uniformly HIGH because the rolling-log
proxy is PASS-heavy -- which EMPIRICALLY CONFIRMS CTO's ruling (the real signal is routing-OUTCOMES, not
tool-run success). CTO RAVC-CLOSED steps 1+2 as clean + validated the shadow observation.

**Step-3 outcome-capture = DATA-GATED** (CTO caveat): inference (correlate a routing row to the agent's
next in-window tool run = the pick) carries attribution risk -> must validate correlation-quality on
real volume (4 rows now). Raw logs persist -> post-hoc correlation loses no data by waiting. Sequenced.

## B. COMPRAIL TO-5 accept

COO~B RAVC-ACCEPTED TO-5 (comp-rail-audit 3b87a05a1) + disposed **HOLD** (broad-repo-grep hard-DENY tier
stays STAGED-BY-DESIGN): grounded on data-thin FP/TP (27 governed-grep events, some dryrun) + the nudge
already working (769 comp-grep adoptions). Coverage-gap classes -> COMPLEARN. Closes COMPRAIL on CVO~B
co-gate concur -> COO~B 2-step. I correctly did NOT touch the settings matcher (advisory only).

## Compiler Tools

| Tool | Command | Result |
|---|---|---|
| comp_route --self-test | per-cap-id disambiguation + cold-backoff | PASS 14/14 |
| comp-route-affinity --self-test / emit / show | shadow provider + live cache (213 caps) | PASS 4/4; emit OK |
| ds-commit-gate.sh | comp_route.py / comp_route_affinity.py / comp_learns_score.py | PASS (per commit) |
| safe-commit.sh | 51c37dcb4 / f64083634 / 5434b66aa (~E author) | PASS (surface-check clean) |
| pytest | test_comp_route + test_comp_learns_score | PASS 18/18 |

**What worked:** surfacing the affinity-grain finding BEFORE building (not shipping the weak surface-grain
version) -> CTO ruled the right design; the shadow observation then empirically validated the ruling.
**What failed / self-caught:** my first CachedAffinityProvider self-test asserted "usage doesn't change
the score" -- WRONG (m-estimate convergence with n is confidence, not inflation; the honest invariant is
"usage doesn't RESCUE a low-outcome cap"). Fixed -- the exact "check the assertion isn't a wrong belief"
lesson I banked as [[feedback_dont_tune_thresholds_to_selftests_calibrate_on_real_outcome_dist]]. Cache
also polluted by non-tool rolling-log `tool` text -> filtered to real cap-ids. **Gap found:** rolling-log
tool-success is a weak affinity proxy (uniform-high) -> routing-OUTCOME capture is the real signal (banked).

## Blockers

None. Step-3 outcome-capture data-gated (routing volume, per CTO's attribution caveat) -- a real gate,
not assumption-blocked. COMPRAIL close pends CVO~B concur (COO~B's 2-step). Phase-B co-sign armed.

## MCP traffic

~14 messages. Significant: L4-landed handoff (~C) -> flywheel ingest; affinity-grain finding -> CTO
RULING (a) per-cap-id -> steps 1+2 RAVC -> CTO RAVC-CLOSE; ~C doc-clarification (afd14e70f); COMPRAIL
TO-5 RAVC2 -> COO~B ACCEPT + HOLD disposition (CC CVO~B/CTO).

## Next Steps

1. **[3.0.0_SA_CVO~B + 2.0.0_SA_COO~B]** COMPRAIL: CVO~B co-gate concur on the HOLD -> COO~B 2-step close.
2. **[0.8.0_AE_CloudComp~E / self]** COMPROUTE step-3 outcome-capture (build + attribution-validate on real
   routing volume) -> CTO step-4 activation justification -> ping ~C for the one-line CachedAffinityProvider swap.
3. **[me]** Phase-B co-sign priority-interrupt STILL ARMED -- break immediately for the ~B-fired derive.
