# Basis-Move Protection-Gate Pattern (generalized from the MDPF leg-2 gate)

**Author:** 0.5.0_AE_OpalETL | **For:** 1.0.0_SA_CTO arch-bless / promote to the never-widen canon (GATE-3) + 2.0.0_SA_COO. | **WS-3 (2), ADVI_ETLFIX.** Proven in production on the MDPF 49F custody bd->schwab flip (2026-07-02).

## The problem -- why a basis move needs a guard by default

A **basis move** = cutting over a served metric's SOURCE-OF-RECORD (e.g. MDPF 49F custody: bd-silver alloc/fees -> schwab/silver/rps). The failure mode: on the FIRST run of the new basis, a **fresh-but-WRONG** number (mis-computed new-basis value from a bad/partial source, a schema drift, a magnitude error) would REPLACE the known-good served number. A wrong-fresh number is WORSE than a stale-but-correct one. The never-widen standing (CTO GATE-3) requires a served number never move to a wrong/widened value. Today the guard is re-invented per basis move; this pattern makes it INHERITED-BY-DEFAULT.

## The pattern -- 5 elements

1. **PLACEMENT: a POST-compute / PRE-serve HARD-DEFER validator.** Insert the validator AFTER the new-basis computation and BEFORE the serve/aggregate stage, so a DEFER stops EVERY downstream served surface (per-date artifact, legacy emit, rolled timeseries) -- a fresh-but-wrong number can never REACH the serve. NOT post-serve (where a wrong number already served). [MDPF: Stage 2.5, post-WS-E / pre-WS-A in mdpf-daily-dispatch.sh.]

2. **THE CHECK: bounded internal sanity, basis-parameterized.** Validate the new-basis output vs bounded expectations: (a) STRUCTURAL (partition exists + schema), (b) MAGNITUDE bands (position/account/value ranges for the new basis), (c) CONTINUITY (day-over-day / period-over-period tolerance vs the prior served), (d) CROSS-BASIS PARITY where a 2nd computation exists (new-basis == independent-recompute to tolerance). Bands/tolerances are per-basis parameters. [MDPF leg-2: partition+schema / positions[85k,96k] / accounts[5.6k,6.2k] / custody[$1.4B,$1.8B] + RPS-to-RPS DoD<=1.6%.]

3. **SEMANTICS: HARD-DEFER, never warn-and-continue.** rc!=0 -> CHAIN_STATUS=failed + exit 1 + SKIP the serve stages + keep last-good (known-stale) + emit an alarm metric. The served surface HOLDS the known-good value; NEVER serves the fresh-but-wrong one. [MDPF: skip Stages 3/3.5/4/5; emits MDPF/DailyChain.SchwabNativeCustodyGateFail=1.]

4. **DORMANT-SAFE ACTIVATION: keyed on the basis flag.** The gate keys off the basis cutover flag (the SSM param). Active ONLY under the new basis; SKIP (rc=0) under the old. So it LANDS + WIRES DORMANT (zero served effect) BEFORE the flip and CO-ACTIVATES with it. This is what makes the guard INHERITED-BY-DEFAULT: the basis change SHIPS with its gate (dormant), and the flip arms it -- no separate guard project. [MDPF: SKIP under CUSTODY_SOURCE=bd; active under schwab.]

5. **FLIP-DAY CONTINUITY EXEMPTION.** The continuity (DoD) check MUST be flip-day-exempt -- the basis switch legitimately moves the number on the flip day. Either exempt-BY-CONSTRUCTION (use a same-basis DoD, e.g. new-source-to-new-source, which the switch does not move) OR a flip-day CROSS-BASIS PARITY (new-basis == the intended new value) in place of DoD. [MDPF leg-2: RPS-to-RPS DoD is flip-exempt by construction; the -3.2% basis step never trips it.]

## Where / how it plugs into a future basis-move flow

A basis move follows this sequence; the gate is step (b):
- (a) Author the new-basis COMPUTE + the basis FLAG (SSM param), dormant (flag defaults to the OLD basis).
- (b) Author the PROTECTION GATE (this pattern) -- dormant, keyed on the flag, POST-compute / PRE-serve.
- (c) Deploy BOTH dormant (zero served effect; a DELTA=0 deploy needs no hold).
- (d) FLIP the flag (co-activates compute + gate) on the never-widen sign-off (CTO+COO+CVO).
- (e) The gate guards the FIRST new-basis run -> serve (PASS) or DEFER (hold known-good + alarm).

The gate is a chain-stage insertion (a HARD-DEFER run_step between the compute stage and the serve/aggregate stage), parameterized by the basis's bands + the continuity/parity choice. It reuses the existing chain's DEFER-skip semantics.

## Machine-checkable AC -- a basis move is PROTECTED iff

- **AC1 PLACEMENT:** the validator run_step sits between the new-basis compute stage and the serve/aggregate stage (chain-order check).
- **AC2 DORMANT-SAFE:** the validator SKIPs (rc=0) under the OLD-basis flag value (dormant-run test).
- **AC3 HARD-DEFER:** under an injected-fail, rc!=0 -> CHAIN_STATUS=failed + exit 1 + serve stages skipped (injected-fail test) -- NOT warn-and-continue.
- **AC4 BASIS-APPROPRIATE CHECK:** bands = the new-basis expected ranges; continuity is flip-day-exempt (same-basis DoD) OR a flip-day cross-basis parity is present.
- **AC5 DEFER-SAFE SERVE:** on DEFER, the served artifact is UNCHANGED (last-good) + an alarm metric is emitted (served-unchanged + alarm-emitted check).

## Reference implementation (the production proof)

MDPF 49F custody bd->schwab (2026-07-02):
- Gate: `data/mdpf/scripts/gold/validate_schwab_native_custody.py`.
- Wire: `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh` Stage 2.5 (HARD-DEFER, dormant-safe).
- Flip fired 14:06Z (SSM /mdpf/custody_source bd->schwab). First schwab-native run 18:05Z: telemetry LEG2-CUSTODY-GATE=ok (PASSED), served fresh custody, never-widen HELD (CVO parity to the cent, all fields DOWN/flat, 06-25 freeze cleared). The gate proved the DEFER-not-serve-wrong guarantee in production.

RAVC CTO (arch-bless / promote to the never-widen canon; this is a GATE-3 doctrine candidate) + COO. AC1-AC5 are the reusable checklist the next basis move inherits.
