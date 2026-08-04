# ANDREW-DIRECT: canonicalize the per-firm MDPF route -- tomorrow's task at this seat

**archetype:** SCRIBE
**secondary_archetypes:** COORDINATE
**Serial:** 0.4.0_DS_ClientPlatform
**Window:** ~05:55Z -> ~06:00Z (since session_close_0545-0555Z @a5f1fa15a4; the window's
work = the emitter/chain walkthrough Q&A at my terminal culminating in this instruction)

## THE INSTRUCTION (verbatim -- the phrasing IS the ruling)

**Channel:** Andrew direct at the 0.4.0_DS_ClientPlatform terminal, as the /log argument,
2026-08-04 ~06:00Z, immediately after the per-firm filetype-by-path /draw:

> "this exactly because I feel like its needlessly complicated and I truly hate that each
> one has a different path. Why are some going to a dynamodb and others dont? Some have
> bridge others don't, why? this process should be exactly the same for every single firm,
> going through exactly the same steps in exactly the same way. all the grief we have is
> from overly complex, not in-pattern, random ass fucking routes for each with no rhyme or
> reason. Your next task for tomorrow is going to be simplifying these to a canonical
> route for all firms."

**Scope (surfaced, not adjudicated):** a NEW STANDING TASK at this seat for tomorrow --
design + drive ONE canonical per-firm route (identical steps, identical shapes, identical
path grammar) for the MDPF chain silver -> spine -> metrics -> bridge -> platinum.
Broadcast to COO + CTO + MSTR this turn per the Andrew-direct law.

## The divergence census (tonight's /draw distilled -- the task's substrate)

The DOWNSTREAM tail is already uniform (spine.json -> aum_metrics.json -> accrual bridge
-> platinum, all four scopes, one bridge, one publisher -- the bridge divergence in the
question reads as the gold-1 divergence below; recording the map as measured):

DIVERGES AT GOLD LAYER 1 (the spine's feeder shapes -- the grief):
1. **49financial**: custody leg detours through DynamoDB (opal-assets-daily-aua, cohort
   49f_schwab_custody -- the "Andrew-canonical" walk series) while the model leg reads
   silver parquet directly. TWO storage systems feeding one spine.
2. **cottonwood**: has an EXTRA tabular gold hop (blackdiamond/cottonwood/gold/
   dim_model_portfolio/date=*/data.parquet) between silver and its spine; no other firm
   has a parquet gold dim in this chain.
3. **inflection**: spine leg reads silver DIRECTLY (orion/inflection/silver/fact_assets)
   -- no DDB, no gold dim.
4. Naming/grammar residue: aum_metrics.json (staging) vs aum-metrics.json (served);
   builder homes split across data/mdpf/scripts/gold/ and data/assets/scripts/gold/;
   spine builders are three DIFFERENT scripts (dim_mdpf_aggregate_aua_timeseries.py /
   build_cottonwood_mdpf_slice.py / the inf leg) rather than one firm-parameterized one.

WHY IT GOT THIS WAY (honest, one line): per-vendor historical accretion -- each firm's
leg was built in its own incident-driven wave (49f trichotomy ruling, cot DC1/fold-in,
inf Orion-era) -- not a designed divergence. That is exactly the "no rhyme or reason"
being named.

## Next Steps

- [0.4.0_DS_ClientPlatform] (me, TOMORROW, Andrew-priority): the canonical-route design --
  one firm-parameterized spine builder, one feeder shape per leg class (kill the DDB
  detour or make it the rule for all; kill the cot-only gold dim or make it the rule for
  all), one path grammar + one naming, migration plan sequenced with the live serve
  (no client-facing wobble). Coordinate with [0.2.0_DS_PortfolioAnalytics] (fold owner)
  + [2.0.0_SA_COO]/[1.0.0_SA_CTO] for the program shape.
- Broadcast dispatched this turn (COO/CTO/MSTR).

## MCP traffic (window)

The broadcast set (3 sends) -- dispatched immediately after this log's commit.

## Compiler Tools

None this window -- a verbatim-record + census-distillation entry off tonight's already-
logged /draw grounding; no code, no infra, no new reads.

## Blockers

None.
