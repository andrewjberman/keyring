# Retire ruling + BR1 plan + EMIT-2 fork-caught-and-retired arc

**archetype:** MIXED (COORDINATE + IMPLEMENT + VALIDATE)
**Serial:** 0.4.0_DS_ClientPlatform
**Window:** 2026-08-04 ~01:40Z - 05:20Z (follows the 08-03 T4A/ADHOC log)

## The Andrew-direct retire ruling -> executed pipeline (one hour, word to dispatched plan)

- **Ruling recorded verbatim @6f4ad98db (+time-fix @83beb6ddc):** after the R-1 dual-writer
  lineage + Orion auth walkthrough, Andrew: "The lambda pattern is lighter/better..." then
  "ok great, so that means we can get rid of the EC2 run, whichever one this is
  i-083ad9ae297f88e9f" (= inf-bronze-runner, Writer B; NOT the auth exporter). Broadcast
  COO+CTO+MSTR same turn; scope surfaced not adjudicated (two rehome prerequisites).
- **BR1 re-scoped + GO'd** (COO 042235Z) -> **EXECUTION PLAN shipped @7538cbc5f** (3 gates:
  Eclipse rehome w/ staging-prefix overlap -- never a production dual-write during its own
  fix; sentinel re-source via dedicated cron emitter + BOTH consumer floors named per CTO
  042600Z condition -- gold floor CITED at cron 14:00Z, silver floor NEW ~15:15Z; teardown
  last, human-confirmed, 14-day stopped-not-terminated rollback).
- **BR1-DS.script-legs GO** (043442Z) -> pending @d0725ee62 (puller -> emitter -> harness).
- bd-plane deploy earlier in-window: @1d6b910e37 MATCH; parity restored; RAVC-closed both
  directions on ~B's independent re-derivation.

## EMIT-2: THE FORK-CAUGHT-AND-RETIRED ARC (verbatim for the doctrine record, COO 051526Z ask)

1. GO 044117Z (sovereign-priority). Spec @90db23580 read; family located; built
   `mdpf_emit_49f_leg.py` v0 -- a raw-silver re-derivation of 49f model_aum with
   tie-by-construction IMPORTS of the timeseries' loaders (@41a7b8c31).
2. **Its own tie exercise REFUSED it**: -22,853,445.47 vs the landed spine @07-30.
3. Discriminating checks, in order: partition-vintage drift RULED OUT (day=07-30 sum
   byte-stable across partitions 07-31/08-01/08-02/08-03 = 1,442,760,941.59); the F5
   crosswalk-filter hypothesis APPLIED AND DISPROVEN (identical sum -- all 7 roster models
   map to SERVED_MODEL_KEYS).
4. Mechanism closed by 0.2.0's contract note 050922Z + source read: **the canonical 49f
   metrics leg already exists** -- `build_firm_aum_metrics` (dim_mdpf_aum_metrics, my own
   prior authorship, 0.2.0's EMIT-1 lane) is a THIN PROJECTION off the firm's own
   timeseries spine; the tie is BY CONSTRUCTION (the radial reads the spine). Tonight's
   fold builds verified 49f total 1,696,469,951.41 / model 1,419,907,496.12 @07-30 ==
   spine exact. A raw-silver re-derivation at my layer is the FORKED PRODUCER the spec
   forbids and structurally cannot tie under vintage motion.
5. **RETIRED same-hour** (git rm, mechanism in the commit message). What stands: the
   naive-sum discriminating control to the cent (fixture delta exactly 205,070.77;
   0 dual rows on the 49f substrate, denominators printed) = EMIT-2's grain-law leg;
   T4.A substrate citations hold through the spine.
6. Ratified by COO 051526Z: "the tie exercise refusing its own author's module pre-deploy
   is the control working at full value, not a fault."

REMAINING EMIT-2 acceptance at this seat: honest-null render evidence + the scheduled-fire
read -- AE wired the fold as dispatch stage 6e into TODAY'S 09:00 cycle (soft-launch
WARN-not-fatal), so the read runs against today's real scheduled artifacts. The acceptance
tie print must carry the verified figures WITH VINTAGE (@07-30) for the DT gate.

## Compiler Tools (this window)

| Run | Observed | Verdict |
|---|---|---|
| BR1/EMIT-2 phase-1 spec+source reads | spec @90db23580 whole; builder family located (comp-grep); crosswalk API enumerated | PASS |
| EMIT-2 phase-2 exercises (scratch, read-only) | tie print (MISS -> the fork catch), control (PASS to the cent), honest-null (n/a on 49f -- custody series reaches 2025-09; the demo rides another scope) | the MISS executed the if_mismatch STOP-and-route exactly |
| commit-gate + ruff | v0 gated clean (1 advisory lane note); ruff caught the dead import that exposed the unapplied third edit | PASS |
| Discriminating probes | 4-vintage partition stability; crosswalk rule-out; build_firm_aum_metrics source read | mechanism closed at source |

## Do NOT (successors)

- Do NOT rebuild a per-scope metrics derivation from silver -- the metrics artifact is a
  thin projection off the firm spine (build_firm_aum_metrics); extending THAT is the only
  lawful change surface.
- The BR1 Eclipse puller writes bronze/eclipse_qa/ ONLY until cut day.
- The retire ruling's box keeps running until BOTH BR1 gates are live + exercised; the
  stop is Andrew/COO-confirmed, never automatic.
