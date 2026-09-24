# /self-drive IRPT_FNTEND IRPT_BCKEND -- tick 38 (~10:4xZ 2026-09-22)

| Field | Value |
|---|---|
| Arming record | carrier `c9ccd9f4e3` |
| Cron | `46e545b7` |
| State | ARMED |
| Scope | 2 of 2 `active` / EXECUTING |
| Sequence | no flags |
| COO lanes | 2 of 3 |
| Inbox | 0 unread. Read and acked: 99440 plus the two slugs from `3.0.0_SA_CVO~B` (FNTEND round 12, BCKEND round 14) |

## Driver acts

### Capture ask released to Andrew at ~10:2xZ

- `0.0.0_AB_MSTR` re-derived all three release conditions (msg 99440).
- This seat independently confirmed README `:178-179` at HEAD: `ea437510` / `17ae44f0`.
- A push notification was sent to Andrew.

### IRPT_FNTEND round-12 L10 analysis @`94680a3bf2` (msg 99436-99438)

The round was graded by `3.0.0_SA_CVO~B` as interim. Results: 5 PASS; F78-AC7 NOT_EVALUATED because the evidence gap is an unscrolled 390px shot.

Round 13, wave 1:
- template-aware key classifier (C-S166/C-S147);
- generator guard (W25-S1);
- discriminating parent-colour check (W27-S2);
- scrolling visibility check (W27-S3).

Round 13, wave 2:
- breadcrumb weight 700 (C1);
- "View breakdown" link in navy (C8);
- F78 re-evaluated at 390px;
- C-S150;
- a MOUNTED DrillTree revision test (W17-S1).

`2.0.0_SA_COO~F` issued round 13 @`e01db98917`. Its L8/L9 go to `3.0.0_SA_CVO~F`, which acknowledged receipt.

### IRPT_BCKEND round-14 L10 analysis @`0782226170` (msg 99443/99444)

The capture-tool line is DONE: R114-AC3 PASS (C-S195) stands.

Round 15:
- C-S174 metadata: RECOMPUTE the transposed CRLF value, never copy it.
- IB-rti-6 is re-handed on Andrew's capture. If the capture fails, the tool's refusal cause becomes the next round's input.
- FWD-2 counts as an essential, qualified human wait.

## State

- **IRPT_BCKEND:** between round 14 and the round-15 cut, waiting on Andrew's capture.
- **IRPT_FNTEND:** round 13 issued.

## Completion test

NOT DONE: 0 of 2 projects complete.

## Compiler Tools

`git show` (README at HEAD), `PushNotification`, `sequence-check.py`
