# Basis-Move Protection-Gate Pattern (generalized from the MDPF leg-2 gate)

**Author:** 0.5.0_AE_OpalETL | **Status:** v2 -- CTO ARCH-BLESSED 2026-07-02, GATE-3 never-widen sub-doctrine, with 3 refinements FOLDED (bounded flip-day exemption / source-grounded bands / DEFER fail-loud+staleness-ceiling). | **WS-3 (2), ADVI_ETLFIX.** Proven in production on the MDPF 49F custody bd->schwab flip (2026-07-02). CC 2.0.0_SA_COO, 3.0.0_SA_CVO (parity = the flip-day guard), 0.6.2_AE_PartnerETL (the upstream pairing).

## The problem -- why a basis move needs a guard by default

A **basis move** = cutting over a served metric's SOURCE-OF-RECORD (e.g. MDPF 49F custody: bd-silver alloc/fees -> schwab/silver/rps). The failure mode: on the FIRST run of the new basis, a **fresh-but-WRONG** number (mis-computed new-basis value from a bad/partial source, a schema drift, a magnitude error) would REPLACE the known-good served number. A wrong-fresh number is WORSE than a stale-but-correct one. The never-widen standing (CTO GATE-3) requires a served number never move to a wrong/widened value. Today the guard is re-invented per basis move; this pattern makes it INHERITED-BY-DEFAULT.

## The pattern -- 5 elements

1. **PLACEMENT: a POST-compute / PRE-serve HARD-DEFER validator.** Insert the validator AFTER the new-basis computation and BEFORE the serve/aggregate stage, so a DEFER stops EVERY downstream served surface (per-date artifact, legacy emit, rolled timeseries) -- a fresh-but-wrong number can never REACH the serve. NOT post-serve (where a wrong number already served). [MDPF: Stage 2.5, post-WS-E / pre-WS-A in mdpf-daily-dispatch.sh.]

2. **THE CHECK: bounded internal sanity, SOURCE-GROUNDED bands (CTO refinement 2).** Validate the new-basis output vs bounded expectations: (a) STRUCTURAL (partition exists + schema), (b) MAGNITUDE bands (position/account/value ranges for the new basis), (c) CONTINUITY (day-over-day / period-over-period tolerance vs the prior served), (d) CROSS-BASIS PARITY where a 2nd computation exists (new-basis == independent-recompute to tolerance). **The bands/tolerances MUST be DERIVED FROM + CITED to the new basis's OWN AUTHORITATIVE SOURCE -- never a guessed/hardcoded range.** (e.g. the schwab-custody band is grounded on the schwab-RPS feed, CVO-parity-verified; not an invented tolerance.) A guessed bound either false-DEFERs a legitimate value or waves through a wrong one -- the source-grounding is what makes the band trustworthy. [MDPF leg-2: partition+schema / positions[85k,96k] / accounts[5.6k,6.2k] / custody[$1.4B,$1.8B] + RPS-to-RPS DoD<=1.6% -- all grounded on the schwab-RPS feed.]

3. **SEMANTICS: HARD-DEFER, FAIL-LOUD + STALENESS-CEILINGED, never warn-and-continue and never a silent carry-forward (CTO refinement 3).** rc!=0 -> CHAIN_STATUS=failed + exit 1 + SKIP the serve stages + keep last-good (known-stale) + emit a LOUD alarm on EVERY DEFER ("new-basis value out-of-band, serving prior, INVESTIGATE"). The served surface HOLDS the known-good value; NEVER serves the fresh-but-wrong one. **CRITICAL:** a DEFER serves the PRIOR (old-basis) value -- correct for ONE run, but a PERSISTENT DEFER (the new basis keeps failing the check) would silently serve the OLD basis indefinitely = a stuck-on-old-basis SILENT FREEZE (the exact failure class we've been closing). So a STALENESS-CEILING escalates a persistent DEFER: do NOT carry the old basis past N runs without a HARD COO/CTO escalation. (This is the robustness-contract limb-3 -- DEFER + fail-loud + ceiling -- applied to basis moves.) [MDPF: skip Stages 3/3.5/4/5; emits MDPF/DailyChain.SchwabNativeCustodyGateFail=1; the mdpf-freshness-checker alarm is the standing loud signal + the ceiling hook.]

4. **DORMANT-SAFE ACTIVATION: keyed on the basis flag.** The gate keys off the basis cutover flag (the SSM param). Active ONLY under the new basis; SKIP (rc=0) under the old. So it LANDS + WIRES DORMANT (zero served effect) BEFORE the flip and CO-ACTIVATES with it. This is what makes the guard INHERITED-BY-DEFAULT: the basis change SHIPS with its gate (dormant), and the flip arms it -- no separate guard project. [MDPF: SKIP under CUSTODY_SOURCE=bd; active under schwab.]

5. **FLIP-DAY CONTINUITY EXEMPTION -- TIGHTLY BOUNDED (CTO refinement 1; the RISKIEST element -- the one moment the gate is disarmed).** The continuity (DoD) check MUST be flip-day-exempt (the basis switch legitimately moves the number on the flip day), but the exemption is BOUNDED, not a blanket disarm:
   - (i) **SINGLE-RUN-scoped** -- the FIRST new-basis run ONLY.
   - (ii) **AUTO-EXPIRING** -- the gate RE-ARMS immediately after the flip-day transition; every subsequent run is fully guarded.
   - (iii) **EXPLICIT COUPLING (the flip-day is NOT unguarded)** -- it is guarded by the NEVER-WIDEN 3-WAY SIGN-OFF (CTO+COO+CVO) + CVO PER-FIELD PARITY *instead of* the gate. That human/parity gate is exactly what caught today's value to the cent. Doctrine: the gate's DEFER is exempted for the ONE flip-day BECAUSE the human/parity gate covers that day; the gate takes over for the subsequent UNATTENDED runs.
   - (iv) **FORBIDDEN:** a too-broad (N-day) disarm -- it would leave an UNATTENDED wrong-value window.
   - PREFERRED mechanism: exempt-BY-CONSTRUCTION (a same-basis DoD, e.g. new-source-to-new-source, which the switch does not move) -- it needs NO explicit disarm window at all, so there is no re-arm to get wrong. Else a flip-day CROSS-BASIS PARITY (new-basis == the intended new value) in place of DoD, single-run.
   [MDPF leg-2: RPS-to-RPS DoD is flip-exempt BY CONSTRUCTION -- zero disarm window; the -3.2% basis step never trips it; the flip-day itself was covered by the 3-way sign-off + CVO cent-parity (14:06Z flip -> 18:17Z parity PASS).]

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
- **AC4 GROUNDED-BAND + BOUNDED-EXEMPTION:** the acceptance bands are DERIVED FROM + CITED to the new basis's AUTHORITATIVE SOURCE (not a guessed tolerance); AND the flip-day continuity exemption is SINGLE-RUN-scoped + auto-expiring (or exempt-by-construction), with the flip-day covered by the 3-way sign-off + CVO parity -- NO N-day disarm (grep the gate for a multi-day disarm window = fail).
- **AC5 DEFER-SAFE SERVE:** on DEFER, the served artifact is UNCHANGED (last-good) + an alarm metric is emitted (served-unchanged + alarm-emitted check).
- **AC6 DEFER FAIL-LOUD + STALENESS-CEILINGED (CTO refinement 3):** every DEFER fires a LOUD alarm (out-of-band / serving-prior / INVESTIGATE); a PERSISTENT DEFER escalates via a staleness-ceiling (the old basis is NOT carried past N runs without a hard COO/CTO escalation) -- never a silent carry-forward that becomes a stuck-on-old-basis freeze. (Verifiable: an N-consecutive-DEFER injected test escalates, not silently carries.)

## Reference implementation (the production proof)

MDPF 49F custody bd->schwab (2026-07-02):
- Gate: `data/mdpf/scripts/gold/validate_schwab_native_custody.py`.
- Wire: `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh` Stage 2.5 (HARD-DEFER, dormant-safe).
- Flip fired 14:06Z (SSM /mdpf/custody_source bd->schwab). First schwab-native run 18:05Z: telemetry LEG2-CUSTODY-GATE=ok (PASSED), served fresh custody, never-widen HELD (CVO parity to the cent, all fields DOWN/flat, 06-25 freeze cleared). The gate proved the DEFER-not-serve-wrong guarantee in production.

## Pairing -- the full basis-move failure surface (cross-reference)

This gate is the DOWNSTREAM half. A basis move must have BOTH:
- **UPSTREAM: source-STALE fail-loud** (the ingest keeps the new-basis source fed + alarms a stall before the gate has to DEFER) -- e.g. 0.6.2's Schwab-ingest harden (daily-bridge-through-accrual + per-date completeness fail-loud @ the consumer's freshness SLA; brief f925d3033). Catches: the new-basis SOURCE went stale.
- **DOWNSTREAM: fresh-but-WRONG backstop** (THIS gate) -- the new-basis value computed but out-of-band. Catches: the source is fresh but the computed basis value is wrong.

Together they cover the full surface: STALE-SOURCE (upstream) AND WRONG-VALUE (downstream). A basis move that wires only one is half-guarded. [MDPF: 0.6.2's ingest fail-loop (upstream) + this leg-2/Stage-2.5 gate (downstream) -- both required for MDPF-custody-durable.]

---

RAVC CTO (folds confirmed -> sign the GATE-3 promotion) + COO; CC CVO + 0.6.2. **AC1-AC6** are the reusable checklist the next basis move inherits by default.
