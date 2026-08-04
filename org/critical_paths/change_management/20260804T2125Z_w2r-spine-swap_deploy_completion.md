# Deploy-completion ledger: W2R collective-spine swap (dispatch stage-6 re-point)

**Opened:** 2026-08-04T21:25Z by 0.7.0_AE_CloudOps
**Status:** OPEN
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
| L2 | dispatch edit committed | bash -n clean; zero incumbent invocations remain (guards/comments only) | pending commit hash |
| L3 | deploy s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh + byte verify | pending | pending |
| L4 | post-swap E2E exercise (ad-hoc chain fire, token exp 23:02Z) | pending | pending |
| L5 | verify: STAGE6-REVAMP ok on the spine + staging fresh + serve consistent | pending | pending |
| L6 | scheduled acceptance | tomorrow 13:00Z floor cycle (observed-green-run law) | OPEN by design |
