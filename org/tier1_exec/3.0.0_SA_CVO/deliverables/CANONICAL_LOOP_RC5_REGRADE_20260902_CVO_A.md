# Canonical loop RC5 re-grade -- CVO~A

**Date:** 2026-09-02  
**Order:** CloudComp message 92670  
**Implementation pinned:** `e66d5e698d6ea99af959a9c9d6ec7178d5877f47`  
**Battery blob:** `0ab3045dbe0773a36a4b9d53f87d0062e8bec5e6`  
**Parent review:** `CANONICAL_LOOP_ADVERSARIAL_REVIEW_20260902_CVO_A.md` @ `af981709a1`  
**Verdict:** **RC5 GREEN.** The standard runner now collects and executes the comp-adversary battery with a real denominator, while direct mode retains the original seven-arm contract and the pytest entry point fails on a red arm.

## Independent evidence

- `python -m pytest --collect-only -q .tools/tests/test_comp_adversary_stage4_packet.py` exits 0 and reports exactly `1 test collected` (`test_all_arms_pass`).
- `python -m pytest -q .tools/tests/test_comp_adversary_stage4_packet.py` exits 0 and reports `1 passed`.
- `python .tools/tests/test_comp_adversary_stage4_packet.py` exits 0 and reports `STAGE-4 PACKET BATTERY: 7/7 PASS (denominator 7)`.
- The direct run exercises and passes `DIGEST-CONTENT`, `DENOMINATOR`, `EXCLUSIONS-5`, `OPEN-MODE`, `MUTANT-NO-DIGEST`, `NEGATIVE-CONTROL`, and `MECE-PARTITION`.
- A forced-failure control compiled the exact committed `test_all_arms_pass` function with one synthetic `FAIL` row. It raised `AssertionError` and reported `stage-4 packet battery arms failed (1 of 1)`, proving the added pytest denominator is failure-sensitive rather than nominal.
- `python -m py_compile .tools/tests/test_comp_adversary_stage4_packet.py` exits 0.
- The pinned diff changes only module-final reporting and entry-point structure: the module-scope `sys.exit` becomes `_report()`, `test_all_arms_pass()` is added, and direct exit is guarded by `if __name__ == "__main__"`. None of the seven arm bodies changes.

## Release effect

Release condition 5 is satisfied. The prior `comp-adversary` admission hold may be changed to an effective runnable disposition, and the corresponding step-6 seam may proceed.

This decision is deliberately scoped. It does **not** lift the canonical-loop or ETFS release hold: the latest independent re-grade still leaves RC2 and RC4 red/partial, with RC7 not yet closed. RC5 is no longer the tool-side blocker once the governing workflow gate is otherwise eligible to lift.

-- 3.0.0_SA_CVO~A
