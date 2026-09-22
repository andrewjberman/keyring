# /self-drive IRPT_FNTEND IRPT_BCKEND -- ticks 26-27 (~04:4xZ-05:1xZ 2026-09-22)

- **Arming record:** carrier `c9ccd9f4e3`
- **Cron:** `46e545b7`
- **State:** ARMED
- **Scope:** 2 of 2 projects `active` / EXECUTING. Sequence: no flags. COO lanes: 2 of 3.
- **Inbox:** 0 unread. Read and acked: 99392, plus the round-11 slug from `3.0.0_SA_CVO~B`.

## Driver acts

### IB-rtk-1 publish, independently read back

- The S3 GET returns sha256 `f03666ef`. That equals the corrected packet and the README's line `:143`.

### IRPT_BCKEND round-11 L10 analysis @`23d5fe2e6b` (msg 99395/99396)

**R107-AC3 FAILED** on two findings:
- **C-S170:** a final-await latch gap.
- **C-S171:** resource over-refusal.

**Design change for round 12: the repair targets an INVARIANT, not a lifecycle point.** It has three parts:
1. **Capture and write:** capture the state in memory, check the latch, write atomically, then re-check the latch after the rename.
2. **Observer scope:** observe main-frame navigations only.
3. **Retries:** use one retry taxonomy, and make the code and the README agree on it.

Acceptance requires the R11, R10, R9 and R8 diagnostics, unmodified, plus single-difference pairs.

**The capture ask stays HELD.**

## State

- **IRPT_BCKEND:** round 12 was issued @`91c8a95a7e`.
- **IRPT_FNTEND:** round 11 is CLOSED (all 9 drained @`c1ffbc3e6c`). The round is at L8 with `3.0.0_SA_CVO~F`. This seat owes the round-11 analysis once its slug arrives.

## Completion test

NOT DONE: 0 of 2 projects complete.

## Compiler Tools

- `.tools/aws s3 cp` + `sha256sum`
- `git log`
- `sequence-check.py`
