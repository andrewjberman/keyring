# OPAL_GLDRNS.A3 COMPLETE — dry-fit executed zero-write: plumbing control PERFECT (4.1M fields), THE FIT measured (C_08 coverage bar quantified), D_04 firm x12 exact

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, TRACE
**serial:** 0.4.0_DS_ClientPlatform~A | **window:** 2026-07-15 ~21:45Z -> ~22:35Z
**TO:** OPAL_GLDRNS.A3 (dry-fit half, CTO GO 212552Z w/ shim-census-first addition) — TO now COMPLETE

## Summary

Deliverable: `deliverables/DRYFIT_REPORT_49F_20260715.md` + driver `runners_49f/dryfit_driver.py`
+ harness upgrades (test-pinned). SHIM CENSUS first per the GO: 0/3 D_00f inputs drop-in, coverage
MATERIALLY LOW (stated) -> D_00f = exercise-1 (FIT), D_04 firm = exercise-2 (SHIM), both declared.
Zero bucket writes across the whole run (native dry-run + guarded s3 proxy; prior_week copy
NEUTRALIZED; read/write surfaces enumerated in the report per the TO).

- **Census findings:** F1 STRUCTURAL — the daily-atomic NNA grain is a hard D-group input and the
  seed/plan C_03 is windowed-only -> A2 T10 correction, C_03 spec must carry daily-atomic (CTO,
  pre-port). F2 seed dim_account lacks geo/first-seen/names (spec-covered, materialization gap).
  F3 MEASURED id-space duality: seed CRS keys vs legacy BD-z keys, zero direct join — dim_account_xref
  is the fit's first dependency (dictionary §4's warning, now a run requirement).
- **Exercise-1:** baseline ties SERVED at 4,100,619/4,100,619 fields under the declared cent policy
  (raw: 369 cent-flips = 0.009%, float summation jitter). Shimmed (xref-bridged seed attribution,
  4,926/5,923 bridged, 997 dropped-and-counted): ALL in-artifact invariants still PASS, firm spine
  BYTE-IDENTICAL, and the attribution axis moved exactly as D6 declared — 148,046/148,058 diff rows
  classified DESIGN in `advisors.*`; 11 FAILs = consequence fields whose glob-widening is REQUESTED
  of CTO (tuning law), not applied. C_08 port acceptance bar quantified: 19 advisor books, +1,609
  bucket-fallback accounts, -44%/-63% attributed-mass deltas, the 997-row xref gap.
- **Exercise-2:** D_04 firm phases 8/8, 13 files local, harness 12/12 PASS, DESIGN 0 / FAIL 0,
  2,921,738 fields — local rebuild reproduces served EXACTLY; plumbing proven at full artifact scale.
- **Instrument hardening from real bytes:** --abs-tol (tolerance = DECLARED POLICY, exact default) +
  micro-cent epsilon (one-cent binary-float delta measures 5.4e-9 above 0.01; 7 rows leaked before
  the fix and were saved only by declared-domain luck — the instrument was seen failing again and
  fixed at source); one-build-per-process driver mode (the OOM lesson: 999MiB melt alloc under fleet
  memory load — host-resource fact, not code defect; F4).

## Compiler Tools

| tool | run | result | note |
|---|---|---|---|
| comp-pipescript postdeps | 2x (D_04, D_00f) | PASS-EMPTY | no declared post-deps for either (bd config) |
| commit-gate.sh | 5 runs across driver+harness edits | PASS | 1 real ruff block fixed at source |
| pytest (runners_49f) | 33 passed | PASS | +1 abs-tol test |
| fit_harness (CLI + library) | control + fit + 12-surface shim diffs | see report | 11.1M fields diffed total this session |
| dryfit_driver | 3 runs (baseline solo, shimmed solo, d04 firm) | ALL OK | zero bucket writes; guard exercised (copy neutralized, live) |

Appended org/compiler-tools-log.md line same commit.

## Current State / Next Steps

1. **A1+A2+A3 ALL COMPLETE** — the full batch GO (192248Z) is discharged. RAVC close to CTO with
   this commit. Lane goes IDLE pending new TOs.
2. Standing requests at CTO from this close: D6 glob widening (tuning law); F1 C_03 daily-atomic
   spec cell; the C_08 coverage bar as Wave-4 acceptance input.
3. Watcher bmzbcge9k LIVE. Streak files + sinks in session scratchpad (evidence quoted in report).
