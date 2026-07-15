# OPAL_GLDRNS.A3 (harness half) — the S4 parity instrument COMMITTED + three-control self-test PASS on served bytes; dry-fit execution at CTO gate

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE
**serial:** 0.4.0_DS_ClientPlatform~A | **window:** 2026-07-15 ~21:20Z -> ~21:45Z
**TO:** OPAL_GLDRNS.A3 (pending — harness half done; dry-fit half CTO-gated by the TO's own
cross_domain_coordination clause)

## Summary

The S4 parity harness is committed beside the new runner (the committed-harness law):
`data/assets/scripts/gold/runners_49f/fit_harness.py` + `predeclared_divergences_49f.json` (A2
sec-5 as machine-readable registry, with the TUNING LAW row: narrow freely, WIDENING = CTO sign-off)
+ `tests/test_fit_harness.py`. Field-level recursive differ keyed off the A1 surface registry
(27 surfaces: 16 singletons + 11 entity fan-outs, run-time key enumeration, printed caps never
silent); declared divergences report DESIGN, undeclared FAIL; MISSING/EXTRA/LENGTH/TYPE/VALUE
kinds; volatile ignore = generated_at ONLY; gzip-sniffing + NaN-tolerant loads (both A1-measured
artifact facts); N=3 streak accounting w/ same-day-rerun replacement; serving-boundary guard
(refuses any new-root resolving into the legacy platinum tree). READ-ONLY by construction — no S3
write path exists in the file.

**Evidence:** commit-gate PASS x2 (after real ruff blocks: unused import, E702s, F841 — fixed
not overridden); full runner suite 32/32 PASS (my 14 fold clean on Wave-2's 18); self-test on the
REAL served mix_summary.json: identity=0 rows, UNDECLARED mutant (firm_id) FAILED loud, declared-
domain mutant routed DESIGN(D2), 368 fields compared, read-only. **The first self-test draft
FAILED honestly** — its mutant (concentration.top_n) sat inside D2's declared domain and correctly
routed DESIGN; the fix was a three-control self-test (identity / undeclared-FAIL / declared-DESIGN),
and the undeclared control (firm_id) now doubles as a registry-widening alarm.

## Bool-vs-number differ gap (caught by the suite, fixed at source)

Python's `True == 1.0` masked bool<->number type changes in the naive differ; a TYPE divergence
kind now fires on any bool/non-bool crossing. Test pinned.

## Dry-fit half (NOT run — gate honored)

Executing D_04 against the canonical seed's C-equivalents is execution beyond read-only analysis —
the TO routes that through the CTO gate, requested in the RAVC interim this window. Proposed
mechanics (for the gate): seed-execution pattern per the build plan (box not a blocker); D_04 reads
shimmed legacy-gold -> seed C-equivalents where they exist; writes monkeypatched to a LOCAL sink
(zero S3 writes of any kind); harness diffs local sink vs legacy-served via --new-root; failures
classify as A2-verdict corrections per the TO. comp-pipescript postdeps runs on D_04 at execution
time (mandate); not run for the harness itself — one sentence why: fit_harness is not a registered
gold script, its execution is S3-GET + local-file-write only.

## Compiler Tools

| tool | run | result | note |
|---|---|---|---|
| commit-gate.sh | 4 runs (2 blocked -> fixed -> 2 clean) | PASS | ruff blocks were real code smells; fixed at source, zero overrides |
| pytest (runners_49f full) | 32 passed | PASS | 14 new + Wave-2 18; 1 honest first-draft failure (bool/1.0) fixed in the DIFFER not the test |
| fit_harness --self-test | 1x vs served bytes | PASS 3/3 controls | read-only; the instrument can fail and was seen failing first |
| comp-pipescript postdeps | deferred to dry-fit execution | — | see one-sentence why above |

Appended org/compiler-tools-log.md line same commit.

## Current State / Next Steps

1. **[BLOCKED-ON-GATE, correctly]** Dry-fit execution awaits CTO GO (requested with proposed
   mechanics). On GO: postdeps D_04 -> shim-run -> harness diff -> dry-fit report (surfaces,
   field match rates w/ denominators, declared/undeclared classification, A2 corrections routed).
2. A1 @ 9be9c2402, A2 @ 92039a3e1, both CLOSED-ACCEPTED; five MISSING ruled 211544Z; Wave-3 spec
   freeze RELEASED conditional on M-folds into owning specs (CTO's text, not my lane).
3. Watcher bmzbcge9k LIVE.
