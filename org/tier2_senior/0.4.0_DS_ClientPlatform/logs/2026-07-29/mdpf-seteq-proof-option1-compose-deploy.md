# MDPF Global: Set-Equality Proof + Option-1 Compose Fix + Deploy (2026-07-28 2350Z - 2026-07-29 0027Z)

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, IMPLEMENT, DEPLOY

## Window
Reinstantiated ~2353Z off handoff @20c2e35b57. Three CTO orders arrived and closed inside the
window: 235422Z (set-equality URGENT), 235944Z (Andrew-direct Option 1 fix-then-flip + spec),
0004Z rider (scope consistency). All executed; CTO ACK/validation 002617Z.

## What happened

1. **Set-equality proof (CTO 235422Z; ACCEPTED COMPLETE 001553Z).** COO measured 31 historical
   dates moved in the refreshed global artifact; hypothesis was Finding B (the de-interpolated
   window). Proven both directions from versioned S3 artifacts:
   - COO's baseline identified as gold version A2QBuod0Amch @2026-07-23T21:44:26Z (447 dates);
     re-diff reproduces COO's numbers exactly.
   - Direction A: moved MINUS interp = EMPTY; (old-new) == one-off MODEL leg 31/31 TO THE CENT.
     Load-bearing axis: the fold consumes ONLY the cottonwood model leg -- the one-off's
     ~$334mm non_model never participated; naive total-vs-total fails.
   - Direction B: interp MINUS moved = 14, ALL null-row dates in both artifacts (weekends
     05-30/31, 06-06/07, 06-13/14, 06-20/21; Juneteenth 06-19; exempt weekdays 06-01, 07-01,
     07-13/14/15 == members of GLOBAL_CROSS_AXIS_EXEMPT_DATES). 31+14=45, no remainder.
   - +136,978,678.52 step @07-20/21 = cottonwood measured onset 124,376,009.73 + 2-firm delta
     12,602,668.79 -- pure composition.
2. **Option-1 compose fix (Andrew-direct, verbatim in-code; CTO design-approved 001553Z).**
   `compose_cottonwood_leg()` + rewritten `load_cottonwood_slice()` in
   `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`: one-off spliced ONLY strictly
   before first_measured_date (derived from daily covered set); labels VERBATIM
   (interpolated_estimate, never relabeled); counts never backfilled; measured-vs-backfill
   collision refuses LOUD; fail-closed BOTH legs; composed leg carries its own
   cohort_provenance so the fold changed ZERO lines. Read-preference removal NOT reverted.
3. **Rider resolved (proposal ACCEPTED 001553Z, invariant now BINDING):** scope artifact rides
   the post-fires gated slice change (value_date re-key + W-2b, CTO's 3 conditions); the
   composition MOVES into build_cottonwood_mdpf_slice.py there and the loader splice is
   REMOVED same change. AT EVERY MOMENT EXACTLY ONE LIVE COMPOSITION. Reason accepted:
   deploying the slice tonight would activate W-2b ahead of its gate (the 4c-zip class).
4. **Acceptance dry-run (local build, serve untouched):** all gates PASS across 450 dates;
   31/31 restored to the cent, zero residual movers; frontier byte-held (1,950,519,805.86
   @07-27); movers-vs-current-serve == exactly the 31; seam gone (+13,083,893.86); remaining
   >$60mm steps byte-identical in served baseline (pre-existing, named); slot histogram
   400 absent / 45 interpolated_estimate / 2 measured / 3 carried(as_of=07-22).
5. **Rule-13 deploy under Andrew's Option-1 freeze exception:** commit @e56eef609e (gate clean,
   -F message) -> push origin/CLOUD -> s3 cp -> head-object ETag 952402715361ded38a3e3afea37ec6df
   == working tree == git HEAD (three-way). AE GO'd 002528Z with measured expected-output
   checklist; COO briefed 002604Z for the acceptance diff.

## Files Modified
See commit message: @e56eef609e (producer + tests + deliverable). Tests 16/16 (5 new boundary
tests: window selection, 07-20/21 seam end-to-end, label integrity, loud collision,
underivable-window refusal).

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| commit-gate.sh | producer + test file | PASS | 2 files clean |
| comp-pipescript deployed | (not run) | N/A | still blind to the mdpf tree (filed 07-24/07-28); deploy verified by head-object ETag==md5 three-way instead |
Raw S3 version retrievals carried `# rail-checked` markers (versioned GetObject -- no comp-tool
serves object-version history). What worked: ETag==md5 as the mdpf deploy oracle. Gap (carried,
already filed): comp-pipescript mdpf-tree blindness.

## MCP Traffic
~8 significant: CTO 235422Z order; CTO 235944Z Option-1 order; CTO 0004Z rider; my 001511Z proof
(-> accepted 001553Z, rider proposal accepted, invariant made binding); my 001532Z COO brief;
my 002528Z AE GO; my 002549Z CTO deploy report (-> validated 002617Z); my 002604Z COO
acceptance brief.

## Blockers
None. Standing by (event-driven) on: AE trio result, COO live diff, any gate trip (mine
immediately).

## Current State (zero-context handoff surface)
- **Deployed producer:** s3://opal-data-mdpf/code/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py
  ETag 952402715361ded38a3e3afea37ec6df == repo HEAD @e56eef609e. Composes daily slice
  (gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json, opal-data-assets) + one-off
  backfill (.../aggregate_aua_timeseries_interpolated.json -- NOW CONTRACT, fail-closed, do not
  move/delete).
- **In flight:** AE re-runs the refresh trio -> COO full-axis diff (expect exactly 31 movers,
  restored to 07-23-baseline values) -> DT flip. Formal RAVC close of the Option-1 leg rides
  that (CTO 002617Z).
- **Tomorrow's fires still stand** (15:00Z chain / ~16:15Z publisher / 17:15Z emitter): D2
  evidence + freeze lift; slice frontier will NOT advance (Finding-A fix post-fires, expected,
  not a regression). Post-fires queue unchanged: slice value_date re-key + W-2b under CTO's 3
  conditions NOW PLUS the compose migration + loader-splice removal (one-live-composition
  invariant, binding) + scope acceptance row; pair UNION merge separate commit; then AE dim
  backfill.
- Deliverable: org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/SETEQ_PROOF_AND_COMPOSE_ACCEPTANCE_20260729.md

## Next Steps
1. **[0.4.0_DS_ClientPlatform]** stand ready on trio/gate trips; post-fires execute the gated
   slice change (re-key + W-2b + compose migration + splice removal) then pair merge.
2. **[0.7.0_AE_CloudOps]** trio re-run (GO 002528Z); keep the backfill key fixed; dim backfill
   after my re-key lands.
3. **[2.0.0_SA_COO]** full-axis acceptance diff per 002604Z checklist.
4. **[1.0.0_SA_CTO]** RAVC close on COO diff + DT flip; post-fires gate unchanged.
