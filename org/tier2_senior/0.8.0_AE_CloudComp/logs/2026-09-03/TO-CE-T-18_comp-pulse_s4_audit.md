# TO-CE-T-18 — comp-pulse s.4 audit

**archetype:** IMPLEMENT

Implemented the `comp-pulse` audit correction for CE-t-18. The engine now treats absent or stale danger maps as `PARTIAL_OR_BLIND` / `NOT-DECIDABLE`, never auto-rebuilds them in the query path, distinguishes all four ratified answer states, and carries Rule-T budget/cursor form through telemetry scans and verdict-bearing `diff`. Added `.tools/tests/test_comp_pulse_battery.py`: 12/12 direct arms passed and its one pytest test passed. The directory collection grain reached 49 tests including this battery but then aborted on an unrelated pre-existing module-scope `SystemExit` in `test_fabric_check_classify.py`.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-to` | PASS | Set the exact CE-t-18 task context. |
| `comp-read` | PASS with friction | Inspected engine and safe-commit reflex; its wrapper dropped multiword `--for` text. |
| `comp-passcraft` | PASS with finding | Recon found the wrapper/engine pair but missed the wrapper telemetry append; filed `NFRA_COMPEFFICACY-S25`. |

The project-tree report and proof instance are staged for pre-complete validation. The task remains pending until the implementation commit is made, its push state is measured, and a non-lane seat exercises the committed shim as the TO requires.
