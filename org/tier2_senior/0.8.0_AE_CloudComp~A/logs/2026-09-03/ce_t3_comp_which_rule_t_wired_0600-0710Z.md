# TO-CE-T-3 -- comp-which Rule T wiring, the s.4 audit deliverable, and the 4.3 four-case test -- 0.8.0_AE_CloudComp~A

**Date:** 2026-09-03
**Task Order:** NFRA_COMPEFFICACY.TO-CE-T-3.comp-which-s4-audit
**Status:** COMPLETE (pending CVO grade + MSTR push)

---

## Objective

Deliver the s.4 per-tool audit for `comp-which` (row T-3, cell CE-t-3, STAGE 1's last cell), the
4.3 four-case test with the NOFIT-POSTERIOR no-match as a planted case, and the one code change
this cell owed: wire the shared `.tools/_compbudget.py` carrier onto comp-which's TWO
timeout-carrying subprocess sites (`_run_primitive`'s fallback-to-comp-find Popen/wait/kill, the
corrected 84-minute-hang site; `_self_report`'s telemetry sink), mirroring the reference
application (`.tools/comp-find`, CE-t-1) and this lane's own precedent (`.tools/comp-read`, CE-t-2).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read | `.tools/comp-which --for "where the routing decision becomes NOFIT-POSTERIOR..."` + `--enumerate 'timeout=\|wait\(\|NOFIT-POSTERIOR\|ROUTE-POSTERIOR'` (before write, and again post-edit) | PASS | 19 hits both times; located the fallback ceiling, the self-report ceiling, and both NOFIT/ROUTE-POSTERIOR log sites exactly, pre- and post-edit |
| commit-gate.sh | on `.tools/comp-which` | PASS | clean |
| comp-system | regenerate `06_current_state` (commit-gate dependency, blocked twice on stale state across this cell's two commits) | PASS | regenerated + staged both times |
| `.tools/comp-which-routing-test.py --binary-ref WORKING` | the battery itself (T3-AC4) | FAIL then PASS | run 1: INSTRUMENT FAILED (exit 2) on a real bug this cell's own audit exposed (F4, see below); run 2 after the fix: PASS, identical score distributions |
| proof-of-spec-check.py | on this instance | see below | validated before the `complete` flip |

**What worked:** the reference-application pattern (comp-find's Rule T rework, CE-t-1) and this
lane's own comp-read precedent (CE-t-2) transplanted cleanly onto comp-which's TWO subprocess
sites -- the shared-Clock, cumulative-budget design generalized from comp-read's single-subprocess
case exactly as expected, with no surprises in the core mechanism.

**What failed, found, and fixed BEFORE the code commit landed (all caught by this seat's own
exercise):**
1. **`--hud`-class near-miss (F3), caught by re-reading, not by testing.** An early draft printed
   the Rule T status unconditionally from `_self_report()`. comp-which's own docstring documents a
   hard side-effect-free contract for `--route-only` ("no rail row, no telemetry row either").
   Re-reading that docstring before commit showed `_ROUTE_ONLY`'s existing early return already sat
   above where the new print would land, so no live regression occurred -- but the class of bug is
   the SAME one CE-t-2 shipped once (the `--hud` zero-bytes regression) before catching it by
   testing. Recorded as a near-miss, not a fix, since nothing needed changing.
2. **A real, live bug in the test harness itself (F4), found by actually running T3-AC4's required
   battery, not by reading.** `.tools/comp-which-routing-test.py`'s `build_mirror()` copies
   comp-which's sibling runtime files into a sandbox but did not know about the new
   `_compbudget.py` dependency. The harness's own POSITIVE-CONTROL mirror invocation (a real
   subprocess, not the warm in-process path) crashed on `ModuleNotFoundError` before reaching
   `main()` -- zero stdout, zero rail row -- which the harness's own v4 no-pollution alibi correctly
   read as "MIRROR CAPTURES NOTHING" and failed the run (exit 2, INSTRUMENT FAILED, "the harness
   POLLUTED the rail log"). Root-caused by reading `build_mirror()`'s aux-copy list directly. FIXED
   by adding `_compbudget.py` to that list (in-lane per the TO: `.tools/comp-which-routing-test.py`
   is named as "its battery"). Re-run: VERDICT PASS, score distributions byte-identical to the
   pre-fix run (the bug only affected the control's own alibi-check, never the sweep's routing
   measurements).

**Gap found, not fixed (BOUNDS: routing semantics do not change under this TO), and the most
consequential finding across all three CE-t cells so far:** F2 -- a syntactically-valid but
non-existent gold-script ID (`A_99z`, confirmed 0 hits anywhere in the estate) is routed by
comp-which with a FULL-CONFIDENCE curated score (2.00), identical in shape to a route for a real
gold script. The router validates the ID's SHAPE, never its EXISTENCE -- a genuine wrong-object
risk class, carried as a finding, not fixed here.

---

## Work Completed

### 1. Rule T wiring, commit `e8f67c34f5`

`--budget` CLI flag stripped the same way `--route-only`/`--json`/`--live-affinity` already are
(comp-which's own established idiom, not comp-read's dict-based carrier); resolved and a shared
`_CLOCK` started ONCE at the top of `main()`, before either subprocess site can fire, so the
budget is one wall-clock allowance for the whole run, cumulative across both. `_run_primitive`'s
`FALLBACK_TIMEOUT_S=60` constant retired as the live ceiling (kept, documented, for history --
confirmed by census that its only other reader was a one-time 2026-07-25 GATEBOUND verification
exercise, already delivered, not a standing consumer); its `Popen.wait()` now derives from
`_CLOCK.remaining()`. `_self_report`'s `timeout=20` likewise now derives from the SAME clock.
`--help` discloses the carrier. Regenerated `infra/system/06_current_state.{md,json}` (twice,
once per commit) for `comp-system-gate`.

### 2. A genuine, measured, real-world finding: the fallback ceiling is tight

An UNSCOPED `comp-find` fallback call (comp-which routes "grep the repo for X" with no way to
scope the pathspec) measured **82.759s DIRECT** on this box (146,464 files, `corpus=all`
default) -- right at the edge of Rule T's shared 90s default, and repeat exercises through
comp-which itself showed both outcomes (BUDGET REACHED on one run, WITHIN BUDGET at ~89s used on
another) consistent with ordinary system-load variance around that boundary. Ground-truthed via a
DIRECT, non-comp-which instrument (`time python .tools/comp-find <term>`), independent of
comp-which's own self-timing. **Not a regression**: the OLD fixed `FALLBACK_TIMEOUT_S=60` is
strictly tighter than 90s, so the identical query would ALSO have been killed under the pre-Rule-T
code (82.7s > 60s). Both BUDGET REACHED sub-branches (pre-flight SKIP on a slower read,
`TimeoutExpired` on a faster one) and the WITHIN BUDGET completion (at `--budget 110`, giving
headroom over the measured ~89s) were exercised live on the real binary -- no mutant needed for
any of it.

### 3. The 4.3 four-case test, keyed on real historical rail-log queries where possible

SUBJECT_ABSENT_FROM_CORPUS via the fabricated gold-ID case (F2, above). PRESENT_WITH_ZERO_RESULTS
via a real historical NOFIT-POSTERIOR probe ("asdfqwerzxcv nonsense control question") reproduced
live today. PARTIAL_OR_BLIND via a real historical near-tie probe ("registry narrative vs project
json") -- found by batch-probing 11 historical `ROUTE-POSTERIOR-DISAMBIG`-tagged queries warm
in-process (fast), of which 2 of 11 still reproduce the tie today (the catalog/scoring has drifted
since the 2026-07-01 log entries; the other 9 no longer tie -- stated, not hidden). NOT_APPLICABLE
via `comp-which --surfaces` (the taxonomy data-view, structurally outside the routing-decision
shape entirely).

### 4. Deliverable + proof instance

`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/comp-which.result.md`
(the T-16/T-1/T-2 shape, all 31 s.4 fields present or explicitly ABSENT with a reason) and its
proof instance, validated against `PROOF_OF_SPEC.schema.json` and `.tools/proof-of-spec-check.py`
before the `<status>` complete flip, which this seat commits itself.

---

## Acceptance (summary; full evidence in the deliverable + proof instance)

T3-AC1 (parses, 4.1 from the engine, incl. the DR2 delegate) PASS · T3-AC2 (four distinguishable
planted cases, two findings F1/F2) PASS · T3-AC3 (Rule T form on BOTH sites, shared clock, both
sub-branches, measured near-timeout finding) PASS · T3-AC4 (battery -- found and fixed a real
harness bug, F4 -- PASS after the fix, identical score distributions) PASS · T3-AC5 (usage at
both instruments with denominators, stated) PASS · T3-AC6 (push state measured at report, not
asserted).

---

## Push State

Measured in the commit report to `2.0.0_SA_COO`, not asserted here.
