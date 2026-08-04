# Deploy-completion ledger: W2R collective-spine swap (dispatch stage-6 re-point)

**Opened:** 2026-08-04T21:25Z by 0.7.0_AE_CloudOps
**Status:** CLOSED 2026-08-04T22:06Z -- swap validated E2E on the runner (round-2 green); L6
scheduled acceptance rides tomorrow's 13:00Z cycle by design
**Authority:** ANDREW-DIRECT at the 0.7.0 terminal ~2050Z, verbatim: "ok proceed with the QA
runs and the swap on the ties." (Broadcast COO 210629Z / CTO 210643Z; supersedes the shadow-era
3-scheduled-cycles gate.)

## The ties (pre-swap, mutant-controlled)

- Instrument: stamp-normalized structural diff (normalizes EXACTLY meta.generated_at; everything
  else reported). MUTANT CONTROL exercised BEFORE first gating use: perturbed value caught (+1
  diff on the perturbed firm) -- the instrument discriminates.
- Same-moment spine-vs-incumbent (both entry points, same host, back-to-back 21:15-21:16Z):
  49financial TIE · inflection TIE · global 0 structural diffs (18,300B size delta =
  serialization only) · cottonwood = byte-TIE vs production staging (incumbent emits no
  cottonwood; the spine's is a verified pass-through of the staged slice, F-2).
- Spine-vs-production-staging deltas (17:42Z vintage) fully adjudicated as time-of-run input
  drift: age_hours_at_generation (+3.5h), the 49F count source's frontier stamp advancing
  (count_basis held->measured at index [445]), a cent-level split flip at 2/446 dates that
  VANISHED in the same-moment run.
- Standalone `--firm global` exercised: writes global only, 0 structural diffs vs incumbent.
- FINDING (cosmetic, noted): a LOCAL run stamps the workstation's absolute roster path into
  meta.cottonwood_carry.policy.roster; the runner stamps /opt/mdpf/... correctly.

## The swap shape (corrected by DS 210939Z grounding -- call sites, not files)

- 6a re-points: `build_mdpf_spine.py --firm all --out-dir` (staging loop unchanged, 3 keys).
- 6d step-(3) re-points: `build_mdpf_spine.py --firm global --out-dir` (exercised pre-wire).
- Row-18 guard now requires BOTH files (spine=entry, aggregate=LIBRARY -- spine imports it :51).
- NO file deletions: dim_mdpf_aggregate_aua_timeseries.py reclassifies library-not-entry (DS
  docstring leg); slice/dim/pair STAY (F-2 ruling + W-3). Andrew named no files; the
  delete-framing was mine and retracts on DS's file:line grounding.

## Legs

| # | leg | evidence | status |
|---|---|---|---|
| L1 | QA ties (above) | mutant-controlled, same-moment, 4/4 | DONE |
| L2 | dispatch edit committed | bash -n clean; zero incumbent invocations remain (guards/comments only) | DONE |
| L3 | deploy + byte verify | 39,809B repo==S3; then the bindings fix +10 lines -> re-deploy | DONE |
| L4 | E2E round 1 (cycle 212520) | FOUND THE GAP: FileNotFoundError /opt/mdpf/config/route_bindings.yaml in 1s -- W-1 bindings never deployed to the runner (QA ran in the repo). FIX same window: bindings -> s3 code/config/ (12,008B byte-equal, DS's @8058f55233), dispatch syncs code/config/ + FATAL guard beside the feeders (row-18 placement). BONUS: STAGE0-TOKEN-GATE first live print = CLEAN | DONE |
| L5 | E2E round 2 (cycle 215804) | GREEN: STAGE0-TOKEN-GATE ok, STAGE6-REVAMP ok 68s -- spine ran BOTH invocations (6a --firm all 22:00Z; 6d step-3 --firm global 22:01Z), "bindings asserted current" both times, 4 artifacts at the QA-tie sizes (187,656/151,776/83,321/343,417B), 6e all four scopes, staging refreshed 22:00-22:01Z. Only step error = the dispositioned LEGACY-EMIT fence deny | DONE |
| L6 | scheduled acceptance | tomorrow 13:00Z floor cycle (observed-green-run law; CTO's three-firsts attribution discipline -- each first on its own evidence line vs tonight's baselines) | OPEN by design |
