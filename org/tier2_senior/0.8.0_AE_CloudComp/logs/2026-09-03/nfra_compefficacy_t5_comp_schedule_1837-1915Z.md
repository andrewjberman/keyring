# NFRA_COMPEFFICACY T-5 comp-schedule s.4 Audit - 0.8.0_AE_CloudComp~K

**archetype:** IMPLEMENT
**Date:** 2026-09-03
**Task Order:** NFRA_COMPEFFICACY.TO-CE-T-5
**Status:** COMPLETE - implementation, audit, independent witness, and proof VALID; lane-owned complete flip prepared

---

## Objective

Audit `.tools/comp-schedule` against the PRD s.4 per-tool schema; add four
machine-readable planted answer states without changing the five carriers'
semantics; add shared Rule-T budget behavior whose partial prefix returns a
non-clean rc; create a RED-mutant battery; record "ARNs absent BY DESIGN"
without remediation; and deliver a 31-field result with measured local push
state.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read | `comp-read .tools/comp-schedule --for "the five carriers, how each decides or refuses to decide, what the rc means, every loop over a carrier's population"` | PASS | Established the five factory functions, carrier-native denominators, output contract, and per-population loops before write. |
| comp-read | `comp-read .tools/to-pipeline-gate.py --for "whether the preflight reads comp-schedule's rc"` | PASS | The gate parses textual preflight declarations only; it never invokes comp-schedule or reads its rc. |
| comp-passcraft | `bash .tools/comp-passcraft recon comp-schedule` | PASS | Moves 1-3 observed; moves 4-8 were hand-run and recorded in the result. |
| comp-schedule | `python .tools/comp-schedule`; `python .tools/comp-schedule --answer-state-cases`; `python .tools/comp-schedule --budget 0.001` | PASS | Complete rc 0 measured 5/5 carriers; one invocation printed 4/4 distinct states; tiny budget cut returned rc 3 with prefix warning and reached denominators. |
| test battery | `python .tools/tests/test_comp_schedule_battery.py`; `python -m pytest -q .tools/tests/test_comp_schedule_battery.py` | PASS | 18/18 direct; 1 pytest file passed. RED mutants cover each new behavior. |
| historical regression | `python .tools/tests/test_comp_schedule.py` | PASS | 9/9 direct, unchanged historical file. |
| commit-gate | `bash .tools/commit-gate.sh .tools/tests/test_comp_schedule_battery.py` | PASS | Clean for 1 of 1 touched Python test files; the executable has no `.py` suffix and was separately compiled/exercised. |
| proof-of-spec-check | `python .tools/proof-of-spec-check.py <T-5 proof> T5-AC1,T5-AC2,T5-AC3,T5-AC4,T5-AC5,T5-AC6` | PASS | VALID rc 0 before complete flip: 6 rows, 0 violations, criterion alignment 6/6, owned-cell alignment 1/1, surprises 0. |

Results: PASS=accurate+useful | PARTIAL=present but noisy | FAIL=wrong/crash/silent | SKIPPED=explain why | WARN=empty+correct WARN message

**What worked:** The shared `_compbudget.py` deadline could be checked inside
each carrier's enumeration, so even a large first carrier is bounded. Explicit
answer-state fixtures provide one-invocation evidence while preserving C4/C5's
adopted `NOT-DECIDABLE` tool voice. Direct and pytest file-grain battery runs
both passed.

**What failed:** Directory-wide pytest collection remains unusable because the
pre-existing `.tools/tests/test_fabric_check_classify.py:76` exits at module
scope. The run enumerated both comp-schedule test files before aborting; the
required new battery still passes at direct and pytest file grain.

**Gap found:** The L6 preflight requires a textual `comp-schedule: RUN`
disposition but does not execute the compiler or branch on its rc. This
correct-but-unwired finding belongs to the gate owner and is outside T-5's
write bounds. No project surprise row was required because the gap is already
visible in the governing source/spec faces.

---

## Work Completed

1. Read the exact reseated task order, current PRD v0.7, current decomp v0.2.7,
   the engine, and the preflight consumer before write.
2. Added exact answer-state tokens and `--answer-state-cases`, with all four
   planted branches emitted in one invocation.
3. Preserved `NOT-DECIDABLE` as the tool voice for C4 and C5 and printed native
   denominators on every carrier.
4. Integrated `.tools/_compbudget.py`; added flag/env/default precedence,
   deterministic cursor, per-loop deadline checks, complete/cut disclosure,
   and non-clean partial rc 3.
5. Added `.tools/tests/test_comp_schedule_battery.py` with 18 production and
   negative-control arms; retained the historical test unchanged.
6. Committed the engine and battery at `86b4ecc2656c3bb0319e777b230c82f9b68802fe`.
7. Sent FWD-9 to `2.0.0_SA_COO` for `python .tools/comp-schedule --budget 0`.
8. Wrote and committed the exact 31-field s.4 result at `f82be2192b`.
9. Received an independent exact `--budget 0` witness from live lane ~G:
   rc 0, 5/5 carriers, 19.032 seconds, C1=21/C2=4/C3=12/C4=20/C5=337,
   21 armed gates, 138 needs-read fields, and correct C4/C5 tool voice.
10. Committed the proof and witness update at `b5148c3456`; proof validator
    returned VALID before the task-order status was changed.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Return rc 3 for every budget prefix | The compiler is verdict-bearing at its five-carrier boundary; an incomplete view must never look clean to an rc-only caller. |
| Check the clock inside carrier loops | A boundary-only check can overrun indefinitely in a large carrier and would not satisfy Rule T. |
| Keep the historical test unchanged and add the dispatched new battery | The reseat GO superseded the older task-face wording and explicitly ordered `.tools/tests/test_comp_schedule_battery.py`. |
| Record ARNs as absent by design | The five carriers share gate armedness, not AWS resource identity; inventing ARNs would mix two axes and change semantics. |
| Do not modify to-pipeline-gate | Consumer wiring is outside the audit cell and the gate owner's surface. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.tools/comp-schedule` | Four states, per-carrier state disclosure, Rule-T budget/cursor/rc behavior | Yes - `86b4ecc265` |
| `.tools/tests/test_comp_schedule_battery.py` | New 18-arm file-grain and RED-mutant battery | Yes - `86b4ecc265` |
| `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~K/comp-schedule.result.md` | Required 31-field s.4 result and evidence quotes | Yes - `f82be2192b` |
| `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~K/NFRA_COMPEFFICACY.TO-CE-T-5.comp-schedule-s4-audit.proof_of_spec.json` | Six-row machine-readable proof, including independent witness | Yes - `b5148c3456` |

---

## Blockers

None. The canonical COO base seat was offline and retained its exact FWD-9
command unread, but live independent lane `0.8.0_AE_CloudComp~G` ran the same
exact command and returned the required witness. Canonical COO routing remains
delivered; no identity was impersonated.

---

## Current State

Implementation commit `86b4ecc265`, result commit `f82be2192b`, log commit
`b2bc206fba`, and proof commit `b5148c3456` are local on `CLOUD`. The new
battery is 18/18 direct and green under pytest file grain;
the historical battery is 9/9 direct. Default compilation completes 5/5
carriers under the 90-second default; a 0.001-second cut returns rc 3 with a
reached-denominator prefix. `origin/CLOUD` was measured at
`351f309e0a6ded1a5a5bdf3aacec18a5f9f8dbee`, and the implementation ancestry
probe returned rc 1. The independent unbounded run returned rc 0 over all five
carriers, and the final proof validator returned VALID. No push was performed.

---

## Next Steps

1. Commit the prepared task-order complete flip with these final evidence
   updates.
2. Send the per-criterion completion report to `2.0.0_SA_COO`; do not push.
