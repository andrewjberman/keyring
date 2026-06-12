# Critical Path Change Record
**Date:** 2026-06-12T21:20Z
**Surface:** model_portfolios (SEV1, headline/benchmark -- served display names render on it)
**Class:** approval
**Authored by:** 0.7.0_AE_CloudOps
**Verified by:** pending CVO sitting (queued 20260612T211531Z rider; ledger leads the change per s10.6)

---

## Change

**File:** `s3://opal-data-mdpf/code/scripts/gold/mdpf_model_registry.json` (deployed copy)
**Repo source:** `data/mdpf/scripts/gold/mdpf_model_registry.json` (registry v4, commit `e88c54e23`, MDPF_SCOPED.F5)
**Deploy pass:** ADVI_INFETL.BRONZE-FIX #4 (`24753c70e`), 2026-06-12 ~21:13Z, sha256 MATCH verified

The runner's deployed registry was STRANDED at v3 while the repo carried v4
(F5, CTO-sanctioned). This pass completed the stranded deploy. On the next
rollup reconsolidation the served `by_model[].display_name` values change for
the 5 core models:

| v3 (served until now) | v4 (canonical, F5) |
|---|---|
| Ultra Short-Term | Ultra-Short Term |
| Short-Term | Short Term |
| Intermediate | Intermediate Term |
| Long-Term Conservative | Long Term |
| Long-Term Aggressive | Ultra-Long Term |

`model_key` values are UNCHANGED -- display labels only.

## Surface detail

`model_portfolios` headline/benchmark (SEV1, "must always be right") renders
the per-model rows across the MDPF aggregate-AUA timeseries slices
(`platinum/mdpf/{global,49financial,inflection}/aggregate_aua_timeseries.json`)
and per-date partitions. Display names are part of what renders, hence
ledger-entry treatment despite zero numeric movement.

## Why the change was made

F5 (`e88c54e23`) made the registry the single canonical source of model
display names ("resolves by_model display_name from the registry by
model_key... so the whole trend carries canonical names without per-partition
re-emit. Effect lands on next reconsolidation."). The effect never landed
because the deploy was stranded: the EC2 runner pulls code+registry from
`s3://opal-data-mdpf/code/` and that copy was still v3. Discovered during the
BRONZE-FIX #4 AC5 DELTA=0 replay (the ONLY diffs between a local rebuild of
the 2026-06-11 partition and the served artifact were the 10 display_name
fields + registry version 3-vs-4). Third stranded-deploy instance of
2026-06-12; the class is the MDPF_COUNTS class (committed fix never reaching
the runner's S3 code copy).

## Risk assessment

**Numeric movement: ZERO.** AC5 replay evidence: full local rebuild of the
2026-06-11 partition from the real S3 feeds vs the served
`aggregate_aua/2026-06-11.json` -- 0 diffs across every aggregate / partner /
etf_decomposition / reconciliation value. The 11 non-numeric diffs are exactly
the 10 display_name fields + `meta.model_registry_version` (3 vs 4).

**Behavior direction:** completion of an already-sanctioned change (F5 was
committed by DS with CTO-relayed canonical-naming intent: "S4 canonical model
display_names"). No new decision was taken in this pass -- only the stranded
deploy step was completed.

**Never-widen posture:** display-name-only movement on a verified-DELTA=0
deploy; per the never-widen doctrine (gates served-output MOVEMENT;
display-label movement already sanctioned via F5's own approval chain), no
hold required -- approval-as-ledger-entry per NFRA_GRAPHS s10.6.

## Evidence

- Stranded-deploy discovery: BRONZE-FIX #4 RAVC2 FINDING 2 (20260612T211444Z)
- DELTA=0 numeric proof: `.runtmp/bronzefix4/` replay vs served diff (RAVC2)
- Deploy verification: sha256 MATCH on `code/scripts/gold/mdpf_model_registry.json`
- F5 sanction: commit `e88c54e23` (MDPF_SCOPED.F5, registry v4)
- COO RAVC3 acceptance: 20260612T211637Z ("display-name-only, F5-sanctioned")
- CVO rider requesting this entry: 20260612T211531Z

## Follow-up

- Takes effect on the NEXT rollup reconsolidation (Stage 4 of the mdpf daily
  chain). NOTE: the chain did not run 2026-06-12 (FINDING 1, routed to
  CTO/DS); first reconsolidation carrying v4 names = next successful chain run.
- CVO sitting verify cue (queued): confirm served by_model display_names match
  the v4 canonical set + zero numeric movement on the same artifacts.
- Portal render check rides the existing F5 acceptance path (F5 removed the
  modelPortfolioColors legacy alias dependence).
