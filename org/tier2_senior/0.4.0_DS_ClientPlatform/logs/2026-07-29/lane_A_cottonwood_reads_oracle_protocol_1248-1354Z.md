# ~A lane: cottonwood Andrew-direct reads + two-derivation oracle protocol (1248-1354Z)

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE

Window: COO 124845Z redirect -> CTO 135415Z oracle settlement. All read-only; zero
commits, zero deploys (post-fires holds intact).

## What happened

1. **Andrew-direct cottonwood custody read (COO 124845Z, DS base dead).** Grounded all
   four questions pre-fire: the 0/450 custody/non-model on the served cottonwood slice
   is an ARTIFACT-VINTAGE gap, not a code gap. Chain: cottonwood never rides WS-A
   (zero cottonwood feeder keys, live-listed with positive control); slice producer =
   dispatch 6d build_cottonwood_mdpf_slice.py; deployed copy md5 == HEAD blob
   @0d653d4aa3 (G7+W-2b); served artifact (LM 00:35:22Z) lacks every W-2b meta key =
   pre-deploy vintage. Expected to populate at the 15:00Z fire; falsifier: blank after
   16:15Z = stage-6d failure. Reported 130026Z.

2. **Andrew's sibling-artifact challenge (COO 131331Z Q5-Q7).** Q5: pair total.aum and
   slice custody are SAME-source SAME-predicate parallel channels -- tied the pair's
   463,015,162.92 to the cent by independent re-sum of fact_holdings/07-24; frontier
   07-27 pre-measured 466,552,705.91. Q6: 294 vs 292 = one population, declared
   excluded_unfunded_count=2 published in-artifact. Q7: 07-27 is DATA reach.
   Reported 131628Z. CTO ruled the parallel-channel finding -> coherence gate in the
   slice (option i, my lane, post-fires, four design pins; 131711Z).

3. **Chain-read absorb and handback.** CTO 133008Z: absorbed dead DS base's 15:00Z
   chain read vs the D-A oracle (assertion set reconstructed from base's G7 log + CTO
   052732Z re-base); closed base's dead ~1430Z checkpoint (AE dim backfill LANDED,
   6 partitions vs P0's 3). Base respawned 1337Z; CTO 134307Z handed the chain read
   back; chain ETag Monitor stopped + orphan bash child reaped (TaskStop-leaves-child
   doctrine).

4. **Two-derivation oracle protocol (CTO 134450Z p.3 mandatory diff).** Base flagged
   that its 3-partition fold numbers were superseded by the 6-partition backfill; I
   corrected my own carried-forward assertion set to CTO at 134319Z (before base's
   re-derivation, so no stale-oracle interval). Then derived the model-leg oracle
   INDEPENDENTLY (raw parquet reads of all 6 dim partitions + deployed-code dry-run;
   banked with CTO 134908Z before base's set arrived). Diff verdict 135201Z: 4/6 +
   frontier label AGREE; DISAGREE on dollar axis -- base's numbers were pre-income-
   routing opal sums; exact tie 126,369,737.47 - 1,246,019.40 = 125,123,718.07 ==
   model_aua_last_non_null. Also flagged base's omission of the 44 composed dates and
   CLOSED base's 05:36Z overwrite governance question (base's own 051021Z run map,
   AE-executed, ledgered -- the respawn had flagged its own predecessor's design).

5. **CTO 135415Z SETTLEMENT: single oracle of record.** Dollar axis ruled to my
   derivation (income-routed); count 50/450 = 6 measured + 44 composed; my F5 grading
   rule ADOPTED (artifact stating unrouted numbers = G8 regression, not a pass); six
   named failure signatures written before the fire; R5 overwrite CLOSED not-a-
   violation on my citations. CTO's assessment: the disagreement was the product --
   quiet harmonization would have let a G8 regression grade GREEN.

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| comp-grep | dim_mdpf_aum_timeseries, legacy_compat_emit, build_cottonwood_mdpf_pair, served key | PASS | writer census + producer location, dependency context |
| comp-glob | *mdpf*dispatch* | PASS | located the dispatch |
| comp-grep (x2, cottonwood) | slice/pair producers | PASS | custody-field census |

Raw reads (rail-checked where gated): dim partition enumeration + parquet value_date/
sum reads -- the value_date-vs-partition-key axis no comp tool models (carried finding,
base 07-29 log concurs). One rail-checked marker logged for the dim listing.

## Blockers

None. All deploys/builds remain post-fires on CTO word.

## Current State (zero-context handoff)

- ORACLE OF RECORD for the 15:00Z fire = CTO 135415Z message (supersedes both
  derivations). Base reads the chain output and reports; I do NOT report on it.
- MY REMAINING FIRE DUTY: penny read at the 15:45Z accrual landing -- report the
  artifact's STATED total only (penny ruled MOOT; do not hunt .15/.16). Watch: Monitor
  b512cydxw (accrual prefix, 300s poll, timeout 17:00Z). Inbox watcher bi6a8ps84.
- POST-FIRES QUEUE (CTO word): WI-2 aum-metrics deploy + retirement pair
  (32e953198a + ca3739c2fc) deploy together; coherence gate build (four pins in CTO
  131711Z); three-bucket cottonwood backfill scoping (CTO 124857Z; hard edge: no
  holdings silver before 2026-06-09).
- Coherence numbers pre-committed for post-fire acceptance: custody @07-24 =
  463,015,162.92; @07-27 = 466,552,705.91; non_model @07-24 = 337,882,950.89,
  @07-27 = 341,428,987.84; model frontier = 125,123,718.07.

## Next Steps

- [0.4.0_DS_ClientPlatform~A] (me): penny read on accrual landing; then post-fires
  queue on CTO word.
- [0.4.0_DS_ClientPlatform base]: 15:00Z chain read vs the settled oracle (theirs).
- [1.0.0_SA_CTO]: R5-as-written re-ruling post-fires; D-I certification carries the
  session-edge context-loss residual (three instances today).
