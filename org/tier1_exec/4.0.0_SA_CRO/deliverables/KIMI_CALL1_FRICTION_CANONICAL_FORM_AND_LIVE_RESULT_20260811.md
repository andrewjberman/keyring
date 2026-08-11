# KIMI SVP -- CALL #1 (FRICTION AXIS): CANONICAL FORM + LIVE RESULT + GRADED VERDICT

**Author:** `4.0.0_SA_CRO~B` · **Andrew-direct 2026-08-11** (spec Kimi calls one at a time; live-call method).
**Live call:** kimi-k3 @ api.moonshot.ai, 2026-08-11 ~0819Z. **Verdict: PASS** (7/7 pre-registered
criteria, 0 hard fails). Rubric pre-registered @KIMI_CALL1_FRICTION_PREREG_20260811.md BEFORE the read.
**Runnable spec:** `scratchpad/kimi_call1_friction.py` (mirrors `call_kimi_sub`).

## 1. CANONICAL FORM (established)

**API call** (new `friction` kind on the proven `call_kimi_sub` structure): single user message ·
`model=kimi-k3` · `temperature=1` (mandatory) · JSON output · Bearer from Secrets Manager
`astn/kimi/api-key` · pre-call telemetry. **Measured budget/timeout:** the call used **1,267 completion
tokens (844 reasoning + 423 content) in 44.2s** against a 16,000 ceiling / 300s window -> the friction
call is CHEAP; price `KIMI_BUDGETS["friction"]` from this (a ~4-6k ceiling is safe WITH reasoning
headroom -- never starve it, per the coupled-set law), `KIMI_TIMEOUTS["friction"]` ~120-180s.

**Input contract -- the F1-F4 battery, per vertical.** Each axis is a DETERMINISTIC figure carrying
`status` (MEASURED|UNMEASURED) + its instrument + `intent_denominator` + `boundary_declaration`
(incl. `failure_direction`). UNMEASURED is a declared BLIND SPOT, never a zero. The prompt (full text
in the runnable spec) mirrors the house style: role+scope, per-axis evidence blocks with denominators,
a HOW-TO-READ contract (translate-don't-remeasure; UNMEASURED is a blind spot; cite every claim),
the JOB (characterize friction HEATING/SPREADING/CONSOLIDATING/STABLE/BEING-ABANDONED/INDETERMINATE +
direction), a strict JSON output schema, ASCII-only.

**Live battery (mdpf, honest current state):** F2 MEASURED (mean 0.497 / 57 paths / hottest 0.998 @0.08d)
· F4 MEASURED (estate-wide agent-type, boundary: not mdpf-scoped) · F1 UNMEASURED (materializer unbuilt,
s.13) · F3 UNMEASURED (capture uploader unbuilt, s.9.1). 2 real axes + 2 declared = an internal control.

## 2. LIVE RESPONSE (verbatim)

`friction_character=HEATING · direction=UNDETERMINED · confidence=LOW`. Summary grounded F2's hot tail
as active work ("HEATING rather than stable or abandoned"), forced direction UNDETERMINED because F2
trajectory is unwired, honored F4's boundary ("context only ... cannot be attributed to mdpf-specific
coupling"), and DECLINED SPREADING because F1 is blind + DECLINED an operator read because F3 is blind.
`cites=[F2,F4]`; F1/F3 appear only as `blind_spots`.

## 3. GRADED VERDICT vs the pre-registered rubric -- PASS 7/7, 0 hard fails

| criterion | result |
|---|---|
| 1 blind-spot honesty | PASS -- named F1/F3 blind; declined SPREADING + operator-read rather than reading calm |
| 2 every claim cites a figure | PASS -- cites=[F2,F4]; F1/F3 never cited as signal |
| 3 F2 read correctly | PASS -- hot tail = HEATING; did not misread the 0.497 mean as calm |
| 4 F4 boundary honored | PASS -- treated F4 as estate context, not mdpf coupling |
| 5 no overreach | PASS -- no lifecycle value, no change, no invented axis |
| 6 direction honesty | PASS -- UNDETERMINED because trajectory unwired |
| 7 confidence honesty | PASS+ -- LOW, and SHARPER than asked: it discounted F4 to "1 of 4 mdpf-specific" because of the boundary |

**The boundary_declarations were READ and USED** (the confidence nuance proves it) -- the single most
important thing to validate, because the whole design rests on the model honoring declared blindness
rather than confabulating over it. It did.

## 4. REFINEMENTS THE LIVE CALL SURFACED (a paper spec would have missed these)

1. **F4 grain is wrong for a per-vertical battery.** The model correctly flagged F4 is estate-wide
   agent-type, not mdpf-scoped -- so per-vertical friction needs `comp-cochange file <vertical-path>`
   (file-scoped), not the estate matrix. Input-contract refinement.
2. **F2 direction is the wanted-but-absent signal.** Trajectory (converging/diverging) needs
   `comp-heat compare` vs a trailing window; without it the friction call can say HEATING but never
   "heating and ACCELERATING." Highest-value cheap add.
3. **Budget is over-provisioned** -- tune from the measured 1,267 tokens, do not starve.

## 5. OPEN FOR ANDREW
- **Confirm the design premise:** call #1 = Kimi TRANSLATES the deterministic battery -> friction
  characterization (STATE deferred per s.13). Built on this; redirect if wrong.
- **Call #2:** his direction -- the natural next is either the F2-direction/F4-grain refinement to make
  call #1's inputs richer, or moving to the next call in the chain.
