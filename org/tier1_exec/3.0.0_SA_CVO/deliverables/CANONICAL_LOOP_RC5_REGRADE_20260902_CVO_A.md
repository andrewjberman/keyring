# Canonical loop RC5 re-grade -- CVO~A (superseded by T-16 correction)

> **CURRENT VERDICT: RC5 PARTIAL / HOLD.** CVO Base message 92685 exposed a
> second module-import defect and an unevidenced end-to-end mutant limb after
> the initial GREEN below. The correction in this record supersedes the first
> verdict and keeps comp-adversary effective admission and the step-6 seam held.

**Date:** 2026-09-02  
**Order:** CloudComp message 92670  
**Implementation pinned:** `e66d5e698d6ea99af959a9c9d6ec7178d5877f47`  
**Battery blob:** `0ab3045dbe0773a36a4b9d53f87d0062e8bec5e6`  
**Parent review:** `CANONICAL_LOOP_ADVERSARIAL_REVIEW_20260902_CVO_A.md` @ `af981709a1`  
**Initial verdict (withdrawn):** **RC5 GREEN.** The standard runner now collects and executes the comp-adversary battery with a real denominator, while direct mode retains the original seven-arm contract and the pytest entry point fails on a red arm.

## Independent evidence

- `python -m pytest --collect-only -q .tools/tests/test_comp_adversary_stage4_packet.py` exits 0 and reports exactly `1 test collected` (`test_all_arms_pass`).
- `python -m pytest -q .tools/tests/test_comp_adversary_stage4_packet.py` exits 0 and reports `1 passed`.
- `python .tools/tests/test_comp_adversary_stage4_packet.py` exits 0 and reports `STAGE-4 PACKET BATTERY: 7/7 PASS (denominator 7)`.
- The direct run exercises and passes `DIGEST-CONTENT`, `DENOMINATOR`, `EXCLUSIONS-5`, `OPEN-MODE`, `MUTANT-NO-DIGEST`, `NEGATIVE-CONTROL`, and `MECE-PARTITION`.
- A forced-failure control compiled the exact committed `test_all_arms_pass` function with one synthetic `FAIL` row. It raised `AssertionError` and reported `stage-4 packet battery arms failed (1 of 1)`, proving the added pytest denominator is failure-sensitive rather than nominal.
- `python -m py_compile .tools/tests/test_comp_adversary_stage4_packet.py` exits 0.
- The pinned diff changes only module-final reporting and entry-point structure: the module-scope `sys.exit` becomes `_report()`, `test_all_arms_pass()` is added, and direct exit is guarded by `if __name__ == "__main__"`. None of the seven arm bodies changes.

## T-16 corrective re-grade

The collection count was correct but insufficient. The same independent run
reported `1 test collected in 111.95s`. CTO and CVO Base independently measured
131.9s and 135.14s. Source inspection at the pinned implementation explains the
clock: `WS = subprocess.run(...)` at module scope and, critically,
`OUT = run(["compose", ...])` at module scope execute the battery while pytest
imports the file. `test_all_arms_pass()` only grades the `RESULTS` that import
already populated.

That violates the P0.1 battlefield contract adopted for the efficacy project:

- collection and execution must be reported separately;
- module-scope unbounded subprocess work must be caught; and
- each important green needs a red-first mutant or negative control.

A 90-second collection ceiling was independently killed with no output and
exit 124. Thus the repair changed collector death into a long import that still
looks hung or dead to a runner with a lower ceiling. Collection is not inert and
cannot be distinguished from execution.

The forced-failure control in the initial re-grade proved only that the isolated
`test_all_arms_pass()` assertion rejects a synthetic `FAIL` row. It did **not**
plant a defect in the production tool and demonstrate that the standard pytest
invocation turns red. The FWD-6/T-16 end-to-end mutant limb therefore remains
unevidenced.

### Surgical acceptance bar

1. Import and `pytest --collect-only` perform no comp-adversary compose work and
   finish in under 5 seconds with one collected test.
2. The collected pytest test performs the seven-arm work and passes; direct mode
   remains 7/7 with the same arm semantics.
3. A planted production-tool mutant is selected by the standard pytest path and
   makes pytest fail. The unmutated tool then passes under the identical command.
4. The diff remains confined to the battery's execution/reporting boundary; no
   production behavior or test-arm meaning changes.

## Corrected release effect

Release condition 5 is **not yet satisfied**. Collector death is fixed and the
existing substantive arms are green, but inert collection and the end-to-end
mutant proof remain open. `comp-adversary` effective admission and the
corresponding step-6 seam remain held.

The broader canonical-loop and ETFS release hold also remains: RC2 and RC4 are
red/partial, with RC7 not yet closed.

-- 3.0.0_SA_CVO~A
