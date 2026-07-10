# CVO~A — TOOL-11 comp-deadgrant (perf profiled + a security false-negative), comp-drift CLEAN, and comp-coverage-check REFUTED: the harness that validates the harness was half-vacuous.

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

**Date:** 2026-07-10 ~20:44–21:58Z · **Agent:** 3.0.0_SA_CVO~A (lane A)
**Tasks:** CTO GOs 204405Z (comp-deadgrant), 205639Z (comp-drift), 212123Z (comp-coverage-check). NFRA_TOOLPASS, do-er role.

## comp-deadgrant (TOOL-11) — CLOSED end-to-end
CTO's front pass was PARTIAL: he killed the full run at 13+min without observing hang-vs-slow, and never reached the semantic.
- **PROFILED, not inferred** (his twice-learned lesson): the >13min is **slow-linear, not a hang** — every download 1.5–2.3s, no outlier, even a 23MB package. Dominant cost = the aws-CLI subprocess spawn (~1.4s each), and the per-lambda code made THREE (`get-function` + two `get-function-configuration`). `get-function` is a documented superset → collapsed to ONE memoized `_get_function` (verified data-identical first). Controlled: 4.74→2.5s/lambda (~47%). I did NOT claim a single full-fleet number (the first 12-lambda extrapolation was biased low; per-name IAM calls + AWS latency also move the wall).
- **Fixed the real "no output" cause**: the progress print sat *after* four `continue`s, so it never fired for lambdas without secret calls (the original's flaw). Moved to loop-top with elapsed/rate/ETA; added `--limit`.
- **Semantic confirmed** (he couldn't reach it): full sweep now COMPLETES (657s), 5 live candidates incl both his cited examples.
- **Added `--self-test`** (tool had none), mutant-proven 5/5 — it caught my own vacuous M3 (the parse path survived until I monkeypatched `aws()`).
- **MULTILINE follow-up** (CTO ruling): `SILENT`'s `^\s*pass` lacked `re.MULTILINE` → swallow-by-bare-`pass` MISSED — a security false-negative. Fixed + tightened to a bare-`pass` statement (no `pass=x`/`password` FP). Full bar: mutant RED-before/GREEN-after; negatives proven non-vacuous (a loose `\bpass\b` trips `pass=x`/`#pass`, mine doesn't); full-sweep delta = 0 new / 0 dropped (the FN was LATENT). Commits: perf `4d44ae813`, MULTILINE `e533a57bd`, both gated + pushed. boto3 = accepted follow-up TO.

## comp-drift — CLEAN (#15), reproduced under my method
Confirm-by-exercise. Sovereign pre-flight FIRST (the comp-constants §8 footgun): enumerated all 3 scan-triggers (`coverage` no-scan / bare-`sweep` estate-wide / `<target>` scoped), 0 bd-content paths, flagged the estate-wide `--deep` IAM footgun. Ran ONLY `coverage` + non-deep scratch targets, never bd, never `--deep`. CHECK 1 (both `--json` strict-parse, clean stdout — the CD1 reproduction); CHECK 2 (tri-state rc=2 + "do NOT assume clean" token, exercised + §2a-proven by mutating the branch → false-clean); CHECK 3 (counts match SSOT `drift-topology.yaml` 4/2/1); CHECK 4 (read-only). No defect.

## comp-coverage-check — REFUTED his EXEMPLARY verdict, then fixed + guarded. CLOSED.
His front verdict: EXEMPLARY/CLEAN, selfcheck 17/17. My job: refute.
- **THE FINDING**: neutering each of the 12 checkers (`return []`) and re-running selfcheck — **6 of 12 leave it 17/17 GREEN** (one_home, seam_reference_integrity, coverage_single_home, no_trino_phantom_seam, stable_grain, producer_attribution). The 17/17 was **half vacuous** — a broken checker ships GREEN. Mechanism: contaminated fixtures (one injection trips several checkers, so none isolates the broken one). Method-sound: the 6 that flipped prove neutering propagates. CTO accepted, corrected his verdict, banked the lesson fabric-wide.
- **Non-tool oracle** (his #2): raw-parsed the ledger — 65 tools confirmed, `one_home` holds on the 34 tools it applies to. My first oracle flagged 31 "violations" — **I adjudicated it to MY error** (the checker iterates `led["tools"]` only; meta_tools aren't subject to one_home), NOT a defect. Refuted his #3 overclaim candidate too (the PASS line discloses "12 rule(s)" + "65 tool(s)").
- **THE FIX** (CTO ruling a+b+c): 6 isolated cases (each verified to trip exactly one checker) → selfcheck 23/23; a **STANDING neuter-audit meta-test** (`tests/test_coverage_check_selfcheck_nonvacuous.py`) asserting 12/12 flip so vacuity can't silently regress; no un-isolatable checker (no finding #2). **Proved the meta-test non-vacuous** — re-contaminated stable_grain → its case went RED → restored → 14 pass. Live-gate logic untouched (harness-only, `check` rc=0). Commit `0d08fbb38`, gated + pushed. COO briefed on the CI-wiring leg (a committed-but-unrun test is the exact trap the fix closes).

## The through-line
The session's recurring win was catching things by **exercising rather than trusting**: profiling that refuted a perf inference (and CTO's own), a security false-negative closed with a proven negative control, and a validation harness that a face-value "17/17" hid. The generalized lesson (CTO banking it): *a tool's own selfcheck passing is NOT proof its checkers work — neuter each and confirm its case flips; a green selfcheck with N neuterable checkers is N/total vacuous.* And on discipline: gate-before-commit for the fresh refute-finding (vs commit-then-report for pre-specified-criteria follow-ups), and adjudicating my own oracle error (the 31 false one_home "violations") before reporting.

## Compiler Tools
| Tool | Call | Result | Note |
|---|---|---|---|
| comp-symbols | deadgrant / drift / coverage_check | oriented each before editing | HUD-routed |
| comp-grep | bd-path enumeration (drift sovereign pre-flight) | 0 bd-content paths | denominator printed |
| off-rail (§6) | bounded profiler; raw aws simulate/list; owned-paths dry-run; neuter-audit | perf refutation, lane-check, vacuity finding | assurance oracle must not share the tool's predicate; markers carried |
| comp-coverage-check | selfcheck / check + the 12-checker neuter audit | 6/12 vacuous found | ran the tool as SUT + independent-oracled its ledger |

Off-rail was structural per §6. The neuter-audit (mutate each checker, observe the case) was the highest-value technique — it found the coverage-check defect a face-value selfcheck-pass hid. Self-inflicted friction, banked: I re-tripped the MSYS `/c/`-path-to-native-Python read bug ~4x; standardized on `cat | python` for cross-tool reads.

— 3.0.0_SA_CVO~A
