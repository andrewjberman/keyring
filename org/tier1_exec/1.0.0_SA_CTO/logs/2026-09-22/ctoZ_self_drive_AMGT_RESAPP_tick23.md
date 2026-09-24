# /self-drive AMGT_RESAPP -- ticks 20-23 (1.0.0_SA_CTO~Z), 2026-09-22 ~00:3xZ to ~02:4xZ

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_145xZ_SELF_DRIVE_AMGT_RESAPP_POST_REBOOT_REARM.md`.
**state: ARMED.** Cursor: tick 19's log @`fcbe2de4fd`.

## Since tick 19

- **rk-89 (DT PROD promote) COMPLETE** @`6c64d69977`: portal v2.1.182 on PROD, 7/7. Z-S201 was disarmed by the COO
  (Z-S211).
- **The CVO says the capture is ready** (msg 24131). Every precondition for the three open judgment grades (rk-43 AC5,
  rk-2 AC6, rk-8 AC4) is met on PROD. The look is Andrew's (PROD is gated to him), and he was notified this turn.
- **rk-88 (H5 SERP) drained** @`b48fe0cd6b`.
- **rk-90 (M1) live acts DONE**, read back independently by this seat:
  - bronze 110, pull_log 9, raw/bloomberg still 119 with its newest at 16:25:37Z (the window condition HELD);
  - adapter CodeSha256 `stDlDaeG...`.
  - The amendment was RULED (msg 24133): widen by exactly test_forecast_fallback.py, and rewrite AC3/AC6 to the real
    invocations.
  - **Row Z-S212 filed @`0c68e3b507`** (INERT): 3 artifact versions against the 1 both halves named, caused by a
    same-turn packaging fix. The radius and the rollback target are unchanged. The remedy is the "one or more builds"
    pair wording.
  - Drained @`e995453666`, 9/9, 0 new test failures.
- **rk-91 (M2) CTO half SIGNED** @`1b9eb552c3` against M1's drained state:
  - filings/v1 holds 194 `.source.json` (14 + 180) and 12 `.analysis.json`; the targets are 0; adapter `stDlDaeG`;
    policy `0c6b3cf46bdff811` under the compact-separator formula (W90-S6's trap named);
  - window condition on filings/v1.

## Open calls in scope: 2 RESERVED at Andrew, plus one look he alone can take

1. The PROD capture of Exec Management, Model and the SA tabs. This is not a call; it is the grading instrument, and it
   is his (PROD is gated to him).
2. One EDGAR fetch for CAT's Item 1D (`C-FILINGS-ANALYZER` per-use word). REC yes.
3. The Lusha public profile URL under `C-LUSHA-EXCEPTION`. REC keep.

## State

- AMGT_RESAPP: `active` / `EXECUTING`. Round 22: rk-91 (M2) running; rk-92 (M3) after it.
- 0 unread.
- **COMPLETION TEST: NOT DONE.**

## Compiler Tools

`s3api list-objects-v2` and `list-object-versions`, `lambda get-function-configuration`, `iam get-role-policy`
(rail-checked; both hash formulas), `git ls-remote` / `merge-base --is-ancestor`, `safe-commit.sh`, `send_message`,
`PushNotification`.

-- `1.0.0_SA_CTO~Z`
