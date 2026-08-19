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

---
## ADDENDUM 18:47Z — CONSOLIDATED ENVELOPE (MSTR 184400Z, every cell MEASURED by MSTR~Z; supersedes the 18:45Z partial)

**PROVEN sitez:** same AWS principal as laptop (sts-verified); safe-deploy data-bucket writes +
portal-v2 publisher writes EXERCISED; safe-commit 4x today full gates; comp-tools 91/97; full
checkout parity; **m365 gateway REACHABLE + EXERCISED (whoami) — the headless-auth conditional is
RETIRED** — plus `opal-gateway-bbg` (the Bloomberg identity) lives ONLY at the BG seat: BBG-identity
legs are **SITEZ-ONLY**, an affirmative export class the laptop cannot hold.
**HARD CAVEAT:** `.tools/terraform.exe` ABSENT — **SITE Z IS NOT A TF-APPLY SITE** until
deliberately provisioned; safe-apply unexercised; ALL infra applies route laptop. (Data-bucket
safe-deploy stands proven; the TF distinction is the placement line.)
**CHEAP-PROOF class:** portal dev-build (bun installed, submodule one fetch behind) — price a
first-act proof into any DE-class sitez TO, never assume.
**AFFIRMATIVE sitez advantages:** sole Bloomberg terminal + DAPI + entitlements + the tplus1
pipeline; SharePoint library OneDrive-synced to LOCAL DISK (doc-heavy work is FASTER there);
RDP-over-tailnet; a resident heavy ML/graph stack (torch/faiss/kuzu/duckdb/pyarrow) — making sitez
the natural home for graph/world-model COMPUTE, not just reads.
**CONCURRENCY (their word):** the binding constraint is the ONE SHARED CHECKOUT — 6 sustained /
8 burst; keep 07:00 ET ±30m light (BBG window); the uncommitted-work-loss hazard is live at high
concurrency → prefer FEW SEATS x WHOLE PROGRAMS (principle 2 reinforced by the machine itself).
**WDAC freeze until 08-20 07:00 acceptance** (unsigned-binary-loading work exposed until then).
Parity: sitez pushed+clean through 0a6cf6dc78; their merge leg fires fast on CTO's PRDs-done word.
