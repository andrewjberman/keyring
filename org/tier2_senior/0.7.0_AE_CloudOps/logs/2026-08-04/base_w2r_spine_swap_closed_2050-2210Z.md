# W2R collective-spine swap: Andrew-direct GO -> ties 4/4 -> swap -> exercise-caught gap -> GREEN

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Serial:** `0.7.0_AE_CloudOps` (base) · **Window:** 2026-08-04T~20:50Z -> ~22:10Z
**Branch:** CLOUD · **Prior log:** logs/2026-08-04/base_fb_wiring_br1_legs12_live_1900-2040Z.md

## Summary

1. **ANDREW-DIRECT at this terminal ~2050Z, verbatim: "ok proceed with the QA runs and the swap
   on the ties"** (immediately after his asked-for walk-through + /draw of the collective spine
   plan). Recorded + broadcast same turn (COO 210629Z, CTO 210643Z, DS seats). CTO: his word
   supersedes the tomorrow-timing, latest binds, no gate added.
2. **QA ties:** deployed-check MATCH; spine --firm all --out-dir local build (4 firms, all
   internal gates PASS); diff instrument mutant-controlled BEFORE first gating use (perturbed
   value caught). First diff vs production staging = time-of-run input drift only; the
   discriminating SAME-MOMENT run of both entry points: **4/4 TIE** (49f/inflection exact,
   global 0 structural diffs -- 18,300B size delta = serialization; cottonwood byte-TIE).
   --firm global standalone exercised pre-wire (global-only emission, 0 diffs).
3. **Swap shape corrected by DS 210939Z grounding (file:line):** NO file deletions --
   dim_mdpf_aggregate_aua_timeseries.py is the spine's IMPORTED LIBRARY (:51); slice/dim/pair
   stay (F-2 + W-3). Andrew named no files; my delete-framing retracted. Swap = call-site
   retirement: 6a -> spine --firm all; 6d step-3 -> spine --firm global; row-18 guard requires
   BOTH files. Committed + deployed byte-equal.
4. **E2E round 1 (cycle 212520): the exercise caught what care missed** -- STAGE6 died in 1s,
   FileNotFoundError /opt/mdpf/config/route_bindings.yaml. W-1's binding table: validated
   33/33, committed (@8058f55233), NO DEPLOY LEG -- the runner never carried it; QA resolved it
   from the repo. Fix same window: bindings -> s3://opal-data-mdpf/code/config/ byte-equal
   12,008B; dispatch syncs code/config/ beside code/scripts/; FATAL missing-bindings guard at
   the feeder placement (row-18 law). BONUS: STAGE0-TOKEN-GATE first live print = CLEAN.
5. **E2E round 2 (cycle 215804): GREEN.** Token-gate clean (2nd print); spine ran BOTH
   invocations, "bindings asserted current" each time (W-1's currency gate live on the runner);
   4 artifacts at exactly the QA-tie sizes (187,656/151,776/83,321/343,417B); 6e all four
   scopes; staging refreshed 22:00-22:01Z; only step error = the dispositioned legacy fence
   deny. Ledger 20260804T2125Z CLOSED 22:06Z.
6. **CTO acceptance 220706Z:** reported to Andrew; **DECLARED-CONFIG-IS-DEPLOY-SURFACE adopted**
   to the day's ledger beside cite-the-resource-not-the-state (config keys join the deploy-parity
   gate candidate + CANRTE W-4/W-5 inherit it). MSTR integrator push landed the full queue on
   origin mid-window (75 commits, all tags).

## Compiler Tools

| Tool / probe | Result | Note |
|---|---|---|
| comp-pipescript deployed build_mdpf_spine.py --pipeline mdpf | MATCH | pre-run gate |
| spine QA builds x3 + incumbent build x1 (local, --out-dir) | PASS | ad-hoc run-and-read per the veto regime; nothing standing, out-dirs scratchpad-only |
| spine_tie_diff.py (mutant-controlled structural diff) | 4/4 TIE | mutant fired (+1 diff) before first gating use; stamp-normalizes ONLY meta.generated_at |
| bash -n (dispatch) x2 | PASS | both edits |
| live reads (telemetry history/logs, staging listing, s3 byte-verifies x3) | PASS | every claim grounded on artifacts, never rc |
| comp tools otherwise | none needed | the window was a scoped swap on paths already graph-known this session; comp-glob located the bindings file |

**Gap found (CTO-adopted):** DECLARED CONFIG IS DEPLOY-SURFACE -- a script's config dependency
needs the script's deploy-verify discipline; a committed binding with no deploy leg is a
silently stale route. **What worked:** the E2E exercise as the oracle (1-second catch of a gap
every static check passed); same-moment dual-entry runs as the tie discriminator.

## MCP traffic

~12 handled; significant: the Andrew-direct broadcast x3, DS deletion-hold (folded into the
swap shape), CTO ack + swap-close acceptance, DS swap-close + W-1 deploy-gap notice, MSTR push
confirmation.

## Blockers

None. W2R owes nothing tonight.

## Current State (zero-context handoff)

- **PRODUCTION stage-6 entry = build_mdpf_spine.py** (6a --firm all; 6d step-3 --firm global);
  library = dim_mdpf_aggregate_aua_timeseries.py (reclassification docstring = DS leg, cosmetic).
  Dispatch deployed s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh; bindings at
  s3://opal-data-mdpf/code/config/route_bindings.yaml (FUTURE BINDING EDITS NEED THE S3 CP --
  flagged to DS as their deploy-cycle leg or routed to me).
- **Tomorrow 13:00Z = THREE FIRSTS, each on its own evidence line vs tonight's baselines**
  (CTO discipline): (1) token minted ~12:06Z (12:05Z rule's first fire); (2) F-B gate line +
  floor 13:02Z; (3) the spine's first SCHEDULED cycle (baseline sizes above). Plus 13:33Z BR1
  Eclipse overlap day-1 + 14:43Z first sentinel emit.
- Rest of board unchanged: floors wave (row-2 + GF-1) after contract reads; gate-cut on Leg-4
  verdicts; CTO~B non-P0 queue; Leg A held at CTO.

## Next Steps

1. **[0.7.0_AE_CloudOps]** Tomorrow's observation slate (the five reads above) -> COO/CTO/DS.
2. **[0.7.0_AE_CloudOps]** Floors wave; then CTO~B queue.
3. **[0.2.0_DS_PortfolioAnalytics]** Library-reclassification docstring; W-1 deploy-leg fold
   into their cycle; six-signal read on tomorrow's scheduled spine cycle.
4. **[1.0.0_SA_CTO]** W-3 sequencing on C1 delivery (Leg-A discharge path).
