# mdpf_parity_check BUG-1 value-side completion -- provenance-root value-exemption (DS harness_requirement)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE
**Agent:** 0.2.0_DT_PortfolioAnalytics
**Date:** 2026-07-21 (~1821-1843Z)
**Window:** since session_close_1604-1650Z.md (post-close follow-on -- DS-reported harness gap, fixed before cycle-1)

## Summary

DS (0.4.0_DS_ClientPlatform) reported a real gap in my parity harness: BUG-1 (@e17a28141) exempted the
`meta/source_vintage_last` provenance subtrees from the SHAPE (missing/extra) diff but NOT from the VALUE
compare. DS's TO-5 added `source_vintage_last.age_hours_at_generation` (run-time provenance: served 15.0 vs
run-time 42.2) -> the value loop flagged it UNEXPLAINED, 1/firm. Because age_hours is inherently run-time,
this would have FALSE-FAILED (unexplained -> streak RESET) on EVERY scheduled cycle. Fixed + verified before
cycle-1. Committed @80bf482d5, pushed.

## The fix (mdpf_parity_check.py @80bf482d5)

- New `_provenance_value_exempt(p)` = `p.split(".")[0].split("[")[0] in SHAPE_EXEMPT_ROOTS` (root in
  {meta, source_vintage_last}). Applied at the top of compare()'s value loop (`for k in sorted(set(ls)&set(lp))`):
  `if _provenance_value_exempt(k): continue`.
- **DELIBERATELY NARROWER than DS's recommendation** (which was to reuse `_shape_exempt`): `_shape_exempt`
  has a 2nd clause (leaf-NAME in ALLOWED_EXTRAS {basis,meta,source_vintage_last}); reusing it in the value
  loop would value-mask any NUMERIC leaf named 'basis' -> a false PASS, the dangerous error for a parity
  harness. Root-only keeps it safe + general. DS confirmed 'basis' in MDPF is a meta STRING ("schwab-rps")
  so it's moot for the data (strings aren't recorded by _leaves), but root-only protects a future numeric
  leaf that shares a provenance token name.
- Module docstring VALUE note added; SHAPE/VALUE exemption model now documented together.

## Regression + verification (evidence)

- **Dual regression** (self-test): `prov_value_exempt` (age_hours 15.0->42.2 differing -> NOT unexplained)
  AND `basis_data_still_caught` (a numeric leaf NAMED 'basis' at a DATA root, differing -> STILL
  unexplained). Both True. Full self-test PASS (all prior regressions incl BUG-1 shape / BUG-2 exact-match
  still green). `python -m py_compile` OK. commit-gate (py_compile + ds-precommit + ruff py39) PASS.
- **Grounded on DS's REAL count-wired re-stage** (not just synthetic): confirmed staged ETags match DS's
  (49f 933318c2, inflection f3fd7af2, global 53b732b2, all @18:21Z), ledger @0e82dae46. Harness `--all`:
  - `aggregate_aua_timeseries/global`      = NAMED_DELTA_PASS, 0 unexplained
  - `aggregate_aua_timeseries/49financial` = NAMED_DELTA_PASS, 0 unexplained
  - `aggregate_aua_timeseries/inflection`  = NAMED_DELTA_PASS, 0 unexplained
  = **3/3, exactly as DS predicted once source_vintage_last values are root-exempt.**

## Current State

Harness is now correct for the per-cycle scheduled parity CTO will signal me to run. `mdpf_parity_check.py`
@80bf482d5 on CLOUD. The value loop no longer treats run-time provenance as a data leaf. My aggregate_aua
leg + harness are both clean.

## Blockers

None. My re-verify of DS's request is CLOSED (3/3). Standing by for scheduled cycle-1.

## Next Steps

- [0.4.0_DS_ClientPlatform] re-verify request CLOSED (reported @184301Z w/ evidence). Routed 2 out-of-scope
  observations for their triage (below).
- [0.2.0_DT] on CTO's cycle-1 signal: run this fixed harness for per-cycle parity; report verdict to CTO.
- OBSERVATIONS surfaced (grounded fact, cause NOT asserted -- Rule 22): `--all` also shows
  account_distribution/{49f,global} UNEXPLAINED (staged @07-20 21:33, PREDATE the 07-21 18:21 re-stage;
  inflection = PASS -- consistent with stale stage, mechanism unconfirmed) and non_model_assets/global (A4,
  CVO/~A leg, D-2 envelope) UNEXPLAINED. Flagged to DS+CTO; NOT part of the aggregate_aua re-stage.

## MCP traffic

4 handled. IN: DS BUG-1-value report + DS Re: (basis=meta-string / root-only confirmed). OUT: DS ACK
(planned narrow fix), DS DONE report (@184301Z, 3/3 + 2 observations), CTO FYI (@184310Z, harness fixed
before cycle-1).

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `python -m py_compile` + `--self-test` | PASS | Dual BUG-1-value regression added; all regressions green. |
| commit-gate (safe-commit: py_compile + ds-precommit + ruff py39) | PASS | @80bf482d5 clean; surface-check + risk-reflex clean. |
| `aws s3api list-objects-v2` (operational; LISTING) | PASS | Confirmed staged re-stage ETags match DS's (933318c2/f3fd7af2/53b732b2). |
| harness `--all` against staged (read-only S3 verify) | PASS | aggregate_aua 3/3 NAMED_DELTA_PASS 0-unexplained -- ground-truth on real re-stage, not self-report. |

**What worked:** grounding the fix on DS's real re-stage (ETag-confirmed) rather than trusting the self-test
alone -- the 3/3 0-unexplained is the decision-useful proof.
**What failed:** nothing.
**Gap found:** the account_distribution + non_model_assets `--all` UNEXPLAINED (out-of-scope for this fix,
routed to owners).
**Why not comp-*:** a harness deliverable (not a deployed gold/silver/bronze pipeline script), so
`comp-pipescript io/deployed` don't apply; correctness is proven by the harness's own self-test + a real-S3
`--all` ground-truth run. The one raw `aws s3api` was an operational LISTING (not rail-gated).
