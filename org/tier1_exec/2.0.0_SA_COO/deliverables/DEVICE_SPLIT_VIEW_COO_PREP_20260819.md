# DEVICE-SPLIT VIEW — COO prep for the CTO+COO session (WORKING DRAFT, pre-PRD-package; 2026-08-19 ~18:40Z)

**Authority/context:** Andrew-direct @ec79827b18 — 10 PRDs (D0-D9) at CTO tonight, then an
adversarial CTO+COO split session; HIS EMPHASIS verbatim: *"We need to be able to parallelize and
get the labor out to the other fabric."* Load-shedding is the INTENT: the S8 laptop-heavy status
quo is the PRIOR, not the answer. This is my capacity/staffing half, written BEFORE the PRDs'
SITEZ-CANDIDATE-LEGS sections so the session is a collision of two prepared views, not one view
reviewed. Capability-envelope facts (sitez AWS creds / deploy tooling / m365 reach) are MSTR's
parallel answers — placements marked ENV below are conditional on them.

## 1. PLACEMENT PRINCIPLES (my side's frame; challenge targets welcome)

1. **Events pin work to the fabric where they fire.** The 49F Thu/Fri critical path (greens, PB-1,
   emit, pins, flip, promote) is laptop — in flight, laptop event clocks, proven deploy tooling.
   NOT movable this week; not a session topic.
2. **Whole workstreams move, never split legs.** A cross-fabric seam inside one workstream costs
   agentbus round-trips on every handoff and reintroduces the coordination class /integrate exists
   to reconcile. Place PROGRAMS on a device, not stages of a program. (Partition discipline,
   standing.)
3. **Read/recon/spec/census work is the natural sitez export** — no deploy gates, no served-key
   acts, evidence is git-carried, and full parity @f970ea785d means citations resolve both sides.
4. **Apply-legs follow the capability envelope, not optimism.** Nothing carrying safe-apply /
   safe-deploy / IAM acts places on sitez until MSTR confirms creds + tooling + gate hooks live
   there (ENV). A fabric that can read but not apply still parallelizes 80% of most programs.
5. **Single-writer/device laws bind placement:** missions register-owner = laptop-MSTR device;
   the estate-report/Kimi loop = its ruled owner; laptop-is-SOURCE (site-Z pulls) stands — sitez
   work lands as commits the laptop integrates per /integrate, and a sitez failed load-pull is a
   REAL finding (standing memory law).
6. **The coordination tax is paid by the COORDINATORS, not the lanes:** cross-fabric kickoff is
   never implicit (VELOCITY seam law); each shipped program carries (prd, workstream, head_version)
   on the bus; MSTR~Z is the sole site-Z coordinator.

## 2. MY PRIOR SPLIT (to be collided with the PRDs' candidate legs)

**SITEZ-LEAN (ship whole):** world-model-class recon/census work where not already CRO-seated;
research/spec authoring programs; the BD PARITY CENSUS ANALYSIS leg (P2 census Mon-Tue — the
harness RUNS laptop where the data lands, but classification analysis/reporting ships); ticketing
v1 build IF its m365 surface reaches from sitez (ENV — the BBG-box placement is already FINAL per
Andrew, which may make sitez the natural neighbor); long-horizon audits (two-homes consolidations'
analysis legs, stale-TO sweep execution when worded).

**LAPTOP-PINNED:** 49F E2E completion + P5 teardown (event+gate-pinned); anything touching
opal-data serving planes, IAM applies, PROD promotes; the missions revival (register-owner device);
MDPF/INF/COT producer chains (data lands here; deploy lanes proven here); the TIGHTENING T1 broker
build (the broker RUNS here; 0.8.0-class seat here).

**SESSION QUESTIONS I BRING:** (a) per PRD: where do its EVENTS fire, where does its EVIDENCE
land, does it ever APPLY — the three answers decide placement mechanically for most items;
(b) sitez seat inventory + who spawns/coordinates there (MSTR~Z's capacity is the real constraint,
not the machine's); (c) the integration cadence both fabrics can afford (per-program /integrate
points, not continuous); (d) what Andrew wants VISIBLE from each fabric (his terminals are
laptop-side today — sitez work must surface through records he reads, or it is invisible labor).

## 3. CAPACITY LEDGER (laptop, as of tonight)

Live: CTO, COO, CRO(+~A), AE 0.7.0. THU AM wave (unchanged): DS base, DS~A(live), DS~B, CVO, DE,
DT, 0.8.0. Standing load through Friday: the 49F close. Post-Friday laptop capacity opens for:
parity P2/P3, GLDRNS disambiguation, T1/T2 tightening builds, W-15 aftermath, the allocation
stack. Everything in that post-Friday list EXCEPT the builds touching laptop-pinned planes is
split-session material.
