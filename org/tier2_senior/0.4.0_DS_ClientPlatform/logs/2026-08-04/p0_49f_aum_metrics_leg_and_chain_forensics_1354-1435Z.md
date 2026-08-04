# P0 water-test: 49f aum-metrics leg fired + landed (INTERIM); chain-failure forensics

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE
**Serial:** 0.4.0_DS_ClientPlatform
**Window:** 2026-08-04 ~13:54Z -> ~14:35Z (delta since mdpf_canrte_phase_a_design_1326-1352Z)

## Arc

1. **EMIT-2 scheduled-fire read began** (other-stream fill work after the CANRTE delivery):
   staged gold/mdpf_revamp trio read 07-31T15:00Z vintage (live s3 ls); telemetry pulled.
2. **Chain-failure forensics** (found BEFORE the P0 landed, from
   s3://opal-data-mdpf/telemetry/mdpf-daily-runner/):
   - Today's cycle `mdpf_daily_20260804_130106` (fired 13:01Z) FAILED at Stage 1: stage-0
     Orion pull 401 Authorization-denied on EVERY model (log :16-24) -> STAGE0-BRONZE rc=1;
     eclipse gold sentinel absent after 1800s (log :128, WARN-proceed); WS-C raised
     `no Orion model-composition bronze found for 2026-08-04` at
     build_mdpf_wsc_inflection_feeder.py:244; stages 2-5 skipped, 6e NEVER RAN.
   - **NO CYCLE AT ALL on Monday 08-03**: history jumps mdpf_daily_20260731_145709 ->
     mdpf_daily_20260804_130106 (the event-only-trigger silent-gap class, NEVER#4).
   - Bronze partitions list 07-28..07-31 then 08-04 (no 08-01/02/03).
3. **P0 ANDREW-DIRECT landed** (COO 141059Z, CTO relay 140842Z, verbatim: "Ok we need to push
   that generation end to end and water test it end to end" + "we cannot wait for a
   schedule"): fire the 49f aum-metrics leg NOW by direct invocation; artifact plane was
   1-of-4 (cottonwood only). ACK'd both seats same turn WITH the forensics (141540Z/141633Z).
4. **Pre-fire gates:** comp-pipescript deployed [mdpf:gold] dim_mdpf_aum_metrics.py = MATCH;
   postdeps mdpf tree = UNCOVERED (recorded, not counted clean). Local repo == deployed S3,
   so direct local invocation runs production code.
5. **FIRED:** `python data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py --firm 49financial
   --upload` -> uploaded 14:23:27Z.
6. **CTO RULING mid-arc (142446Z via COO 142737Z): SERVE the 07-31-vintage leg** (blank
   strictly worse; cottonwood's artifact was the stalest at 07-24); conditions: verify
   in-artifact provenance in the content read; the leg is INTERIM pending the post-401-fix
   same-day fresh supersede.
7. **WATER TEST (observed, never rc):**
   - Key s3://opal-data-assets/gold/mdpf_revamp/49financial/aum_metrics.json,
     LastModified 2026-08-04T14:23:29Z, 5,280B, ETag d2108377e1c046eca972c958047ec794.
   - period=2026-07-30 (DATA AS-OF; spine staged 07-31T15:00:39Z); provenance VERIFIED IN
     CONTENT: meta.source_spine = the exact spine key; meta.as_of_basis = "period == the
     spine's as_of_last (data as-of, never run date)".
   - TIE LAW HOLDS: 5/5 per-model TIE to the cent at spine idx 434 (UST 50,059,820.07 /
     ST 106,404,420.06 / INT 292,875,613.93 / LT 768,032,742.56 / ULT 202,534,899.50);
     sum(by_model) == total.model_aum == 1,419,907,496.12 (delta 0.00);
     total.aum 1,696,469,951.41 == model + non_model 276,562,455.29; accounts 7026.
   - **Probe-universe note (banked so nobody re-derives it wrong):** a naive 7-model spine
     sum @07-30 = 1,442,760,941.59; the 22,853,445.47 gap is the NAMED F2 delta (2 SMA
     models outside the 5-core metrics universe), NOT an artifact defect. My first probe hit
     it and was corrected at the universe — the same catch that retired the EMIT-2 v0 fork.
8. **Roll-forward poisoned-prefix mechanism CONFIRMED (was INFERRED in the ACK):**
   mdpf/bronze/orion_model_composition/2026-08-04/ EXISTS containing ONLY _meta/ (live
   listing) -> resolve_bronze_date (feeder:211) sees today's token, returns (date,0), NO
   roll-forward -> read_orion_bronze (:244) raises. The dispatch's absorption claim (:207)
   fails exactly in the failed-pull-wrote-_meta case. **One-hunk DS fix (resolver counts
   only model-bearing partitions) HELD for COO/CTO word** — no chain-surface change
   mid-water-test unrequested.
9. Leg reports delivered COO 143404Z + CTO 143518Z. COO validated the CANRTE delivery
   separately (RAVC-4 135714Z, his leg CLOSED).

## Compiler Tools

| run | observed | verdict |
|---|---|---|
| `comp-pipescript deployed dim_mdpf_aum_metrics.py` (flagless) | rc=2 REFUSED, --pipeline required | expected; re-ran with flag |
| `comp-pipescript deployed dim_mdpf_aum_metrics.py --pipeline mdpf` | MATCH (1 MATCH / 0 STALE / 0 MISSING) | PASS — pre-fire gate |
| `comp-pipescript postdeps dim_mdpf_aum_metrics.py --firm mdpf` | UNCOVERED: mdpf tree has no postdeps config (TOOL-02 false-clean guard printed) | recorded honestly; not counted clean |
| live reads (operational aws): telemetry status + history + logs, staged-trio ls, bronze prefix ls, artifact head+get x3 | per arc above; denominators in outputs | the water-test evidence base |

## Do NOT (successors)

- Do NOT read the 49f aum_metrics artifact as current-frontier: it is INTERIM at
  period=2026-07-30 until the post-401-fix supersede lands.
- Do NOT tie-check the metrics against a 7-model spine sum — the F2 SMA delta
  (22,853,445.47 @07-30) is named, expected, and NOT a defect.
- Do NOT land the roll-forward fix without the COO/CTO word (held deliberately).

## Blockers

None at my seat. Waiting on events: Orion 401 fix (AE/CloudOps, URGENT spawn requested via
MSTR) -> then my fresh supersede re-fire; CTO fork rulings -> then CANRTE Phase B.

## Next Steps

- [0.4.0_DS_ClientPlatform] (me): re-fire the 49f leg the moment the Orion fix lands
  (same-day supersede, CTO-ruled); land the roll-forward one-hunk on the word; CANRTE
  Phase B on the fork rulings.
- [1.0.0_SA_CTO]: Leg-2 content verification (my evidence delivered); F-1/F-2/F-3 rulings.
- [0.7.0_AE_CloudOps / spawned seat]: Orion 401 credentials fix; the 08-03 no-cycle gap is
  scheduling-forensics input (NEVER#4 class).
- [2.0.0_SA_COO]: serve-or-hold coordination across the four scopes (vintage facts per
  scope delivered).
