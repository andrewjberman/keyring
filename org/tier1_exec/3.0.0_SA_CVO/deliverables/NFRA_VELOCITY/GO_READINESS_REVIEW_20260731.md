# NFRA_VELOCITY -- GO-readiness review vs the 2026-07-30 ontology motion (CVO, 2026-07-31 ~0210Z)

**Commissioning instruction (Andrew-direct, CVO terminal, MID-TURN ~0200Z Jul 31, VERBATIM):**

> i do want to go through and do all the remaining tools through this, but first, now that MSTR~Z
> sitez terminal fabric seems to be up and running, i want to explore if we are ready to kick off
> NFRA_VELOCITY one more time. the specification will be that from the GO on NFRA_VELOCITY, NO
> OTHER WORK ASIDE FROM THAT PROJECT AND ITS NEEDS WILL BE ADDRESSED UNTIL I SAY OTHERWISE. The
> only question really is if we should have you do a quick review of that project and make sure
> its all still properly aligned based on all the ontology work we have done today, or if there
> are other opportunities to enrich it based on said work.

*(Recorded per XXX.md. This lifts the 07-30 ~2215Z by-name deprioritization of NFRA_VELOCITY.
The exclusive-work specification binds FROM THE GO, which has not been given -- this review is
the pre-GO work he named.)*

**Denominator of this review:** all three staged PRDs (PROGRAM read in full; CORE/ESTATE headers
+ workstream greps), REGISTRY rows 22/23, NFRA_VELOCITY twin JSONs, NFRA_WORLDMODEL.json,
NFRA_ONTOLOGY_RULE_BANK.yaml v1.7 (grounded greps), tonight's session records (rulings 1-8).

---

## VERDICT: THE ARCHITECTURE SURVIVES TODAY INTACT; THE GO NEEDS 4 FIXES + 4 CARVE-OUT RULINGS.

Nothing in today's ontology motion contradicts the thesis, the seam, the metrics, or the
constraints. The drift is in the ROLE TABLE (the fabric moved under it), the UNLANDED canonical
PRDs, and one pre-built positive nobody has recorded. Every fix is cheap and nameable at the GO.

## A. Grounded readiness findings

**A-1 (POSITIVE, ahead of plan): WS-C1's rails ALREADY EXIST -- but its critical-path piece does
not.** Rule bank v1.7 carries authored `D1_value_grain` / `D2_path_flow` / `D3_contract_obligation`
sections (:203/:244/:267), D-rail-aligned across four canon surfaces tonight. **The LIFECYCLE
extension is ABSENT** (zero hits for lifecycle / TRANSIENT / expiry; `successor` only incidental)
-- and that is exactly (i) the "true blocking edge" the PROGRAM names for the held-out products
(draft lifecycle vocabulary), (ii) what E1 contracts carry, (iii) what E3's kill-list derivation
needs ratified, (iv) the ~C-item-3 TRANSIENT trap closure. **Consequence: P1 is FURTHER ALONG and
MORE PRECISELY BLOCKED than the PRD states -- the first CORE motion is the lifecycle vocabulary,
not the rails.**

**A-2 (BLOCKER-CLASS, cheap): the canonical PRDs never landed.** docs/architecture/ has no
NFRA_VELOCITY_*.md -- the ANY_CTO-gated landing relayed 07-29 is still open ("CTO holds without
intent" in my 0100Z handoff). A GO would start an exclusive regime on a constitution that exists
only as my staged copies. Base CTO is LIVE tonight; the landing is one gated commit -- with A-3's
refresh folded in.

**A-3 (BLOCKER-CLASS, needs Andrew): the ESTATE role table names a fabric that no longer
exists.** Written 07-29/30: base CTO "dead, deliberately not respawned" (~C designated), COO
decompose/drive, workers 0.4.0_DS / 0.5.0 / 0.6.2 / 0.2.0_DT. Since the 07-30 ~1810Z narrowing:
COO KILLED, those worker seats KILLED, no respawns authorized -- and base CTO is ALIVE (landed
NFRA_WORLDMODEL tonight). The ESTATE PRD cannot execute on the current fabric. **Staffing is a
sovereign call: respawn the worker set (spawns via MSTR) or re-map the roles at GO.** The CORE
table likely holds IF site-Z seats are live (A-4).

**A-4 (VERIFY, one probe): site-Z seat liveness is an assertion until the bus round-trips.**
"Seems to be up and running" + a localhost broker that cannot see site Z = exercise the seam's
own Protocol-4 as the readiness probe: MSTR->MSTR~Z roll-call over agentbus, CORE seats
(CTO~Z, 0.8.0_AE base+lanes, CVO~Z) each ACK. SENT != READ; only the round trip counts. Also
confirm `.owned-paths.yaml` carries the CORE/ESTATE surface split the PROGRAM's collision
control requires (registration-time amendment -- unverified tonight).

## B. Carve-out rulings only Andrew can make (the exclusive regime's boundary)

1. **Aug 1 14:00Z ETFS month-end fire** (TOMORROW; HARD; owner 0.7.0_AE_CloudOps~A;
   partner-rebate basis). Inside "its needs" or an explicit carve-out?
2. **~B's estate-report v4 build** -- mid-build on tonight's rulings 6-8. It is Limb C of
   NFRA_WORLDMODEL (registered-and-parked, `related: NFRA_VELOCITY`). Continue, pause, or fold?
   NOTE: the CAPTURE MANDATE (R7a) is standing sovereign -- if the build pauses, the day-by-day
   text store arguably should not.
3. **The daily semantic-evolution loop** (R3: "CVO owns the loop") once the pipeline is live.
4. **Aug 6 mockadv FIRM_ALLOWED_PATHS expiry** -- fires loud on a question Andrew deprecated
   07-29; retirement is ~Z-side work that will interrupt CORE if not pre-cleared.
   *(Dialed-tool-flow needs no ruling -- Andrew already sequenced it AFTER, and E-2 below offers
   the fold that makes the sequencing moot.)*

## C. Enrichment opportunities from today (all cheap to fold at landing)

**E-1 CO-CHANGE (Ruling 8) belongs to VELOCITY too.** What-moves-together is a measured,
graph-independent coupling detector: WS-E1 contract DISCOVERY (undeclared coupling -> candidate
contracts), WS-E3 residue detection (a file that stopped co-changing with former partners), WS-C5
evidence plane. One implementation, two consumers (THE STORY already requires it).

**E-2 DIALED-TOOL-FLOW is WS-C4/C7's execution vehicle.** The just-designed workflow
(@b5c6441086) IS per-tool tightening/dependency-frontrunning: DIAL-record re-dial triggers are D3
lifecycle contracts ON TOOLS; the routing-centrality queue is a D2 derivation. Folding it in
squares "all remaining tools through this" WITH the exclusive regime instead of against it.

**E-3 Tonight's 7 banked laws are WS-C8 corpus.** Fresh mechanism-law candidates with measured
instances (guard-shares-failure-mode x5, record-outward-relocates-frontier, grant-widened-by-
worlds-motion, escape-belongs-to-consuming-layer, stub-conceals-layer-below, loud-vs-informative,
no-rigour-validates-frame) for the 14-law PREVENTION collapse.

**E-4 THE REAL STORY is the program's human-grade progress artifact.** Its three sources (user
input / change-cochange / deployment motion) are exactly VELOCITY's progress evidence; Protocol-4
per-wave sync can cite the day's story instead of inventing a fourth status format.

**E-5 Declare the WORLDMODEL <-> VELOCITY seam (one paragraph, prevents a vocabulary fork).**
Two ontology programs now coexist: WORLDMODEL's 30 sovereign-captured classes + semantic rung
(parked) vs CORE's D1/D2/D3 type system (about to be exclusive). Proposed one-liner for the
PROGRAM doc at landing: the rule bank remains the SINGLE vocabulary carrier; WORLDMODEL classes
enter CORE only via the Z-ratification chain; WORLDMODEL stays the semantic/sovereign layer,
CORE the mechanical type system. CTO word at landing.

## D. Recommended GO sequence (all pre-GO items are hours, not days)

1. Base CTO lands the canonical trio WITH: role-table refresh (per Andrew's A-3 staffing ruling),
   the E-5 seam paragraph, and A-1's status correction (rails exist @v1.7; lifecycle is the first
   CORE motion). 2. MSTR<->MSTR~Z bus roll-call; CORE seats ACK; owned-paths confirmed.
3. Andrew rules B-1..B-4 + A-3 staffing at the GO. 4. GO -- exclusive regime binds; first
motions: CORE = lifecycle vocabulary (draft D3 grammar for E1); ESTATE = product baselines
captured BEFORE anything touches the estate (the perishable §5.9 metric), then E1 specimen chain.

-- 3.0.0_SA_CVO
