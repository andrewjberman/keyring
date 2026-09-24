# /self-drive AMGT_RESAPP -- ticks 24-27 (1.0.0_SA_CTO~Z), 2026-09-22 ~02:4xZ to ~04:4xZ

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_145xZ_SELF_DRIVE_AMGT_RESAPP_POST_REBOOT_REARM.md`.
**state: ARMED.** Cursor: tick 23's log @`eb691b7848`.

## Since tick 23

- **rk-91 (M2) mid-act safety read** (~03:4xZ, this seat): both grants were present (no reader left with neither), and
  the adapter redeployed `Successful`.
- **rk-91 (M2) DRAINED** @`96045cc865` (msg 24136), 9/9.
  - The COO's independent read-back: the window held (filings/v1 194 source, 12 analysis); 14/14 silver and 180/180
    state; `filings/v1` grant ABSENT and `filing_attempt` grant PRESENT; 3 of 3 names 200.
  - **Two live incidents:**
    - (1) The IAM add and the first redeploy ran before the copy, against the ruled order. 0 invocations, so an
      EXPOSURE that never fired.
    - (2) 4 live 500s while the adapter imported `lib.opal_naming` outside its closure. An INCIDENT on gated PROD with
      0 third-party traffic, fixed same-turn. Row W91-S3.
- **RULED (msg to the COO, 04:11Z): the Rule 30 call is (c).**
  - The adapter's BUILD STEP generates its new-grammar prefix constants from `address()` into a generated module in
    the artifact, with a box-side drift test. Nothing new goes into the Lambda closure.
  - (a) was refused: `opal_naming` resolves REPO/registry and also the schema and DIRECTIVES at runtime, so a wider
    closure on the served path, the class of both incidents.
  - (b) was refused: it would need an R20 acknowledgment from Andrew that (c) makes unnecessary.
- **Binding from M3 on:** before any live deploy, the handler is imported from the BUILT ZIP in a clean interpreter and
  each changed reader is exercised once. An ImportError STOPs the act.

## Open calls in scope: 2 RESERVED at Andrew, plus his PROD look

The capture (Exec Management, Model, SA tabs on v2.1.182); CAT's EDGAR fetch (REC yes); the Lusha profile URL (REC keep).

## State

- AMGT_RESAPP: `active` / `EXECUTING`. Round 22: rk-92 (M3) waits on its amendment ((c) plus the closure check), then
  this seat's CTO half.
- 0 unread.
- **COMPLETION TEST: NOT DONE.**

## Compiler Tools

`lambda get-function-configuration`, `iam get-role-policy` (rail-checked), a source read of `lib/opal_naming.py`
(REPO resolution, `generate()`), `git log`, `safe-commit.sh`, `send_message`.

-- `1.0.0_SA_CTO~Z`
