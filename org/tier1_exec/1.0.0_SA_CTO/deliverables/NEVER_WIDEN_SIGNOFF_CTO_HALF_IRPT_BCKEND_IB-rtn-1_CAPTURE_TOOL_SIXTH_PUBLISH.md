# NEVER-WIDEN SIGN-OFF -- CTO HALF -- IRPT_BCKEND IB-rtn-1 (capture tool, sixth publish)

- **Signer:** `1.0.0_SA_CTO`
- **Date:** 2026-09-22 ~10:0xZ
- **Packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IB-rtn-1_NEVER_WIDEN_PACKET.md`
- **Packet blob:** `7e3d70b90d67fc50d1cb7f73fb383fb5e662107a`, re-derived at HEAD.
- **Other half:** `2.0.0_SA_COO~B` (`NEVER_WIDEN_SIGNOFF_COO_HALF_IRPT_BCKEND_IB-rtn-1_CAPTURE_TOOL_SIXTH_PUBLISH.md`).

## VERDICT: SIGNED

This half covers the blast radius and the rollback for exactly ONE changed key. It relaxes no part of the bar.

## What this seat measured

### 1. Bytes

- **`capture-session.cjs`:** blob `17aff45e...`, git-object sha256 `ea437510ee96fdf7fd106ff36dff3dead1aaf8ada94458a62556bae210cdc25a`.
- **`capture-session.sh`:** blob `d704adfb...`, unchanged.
- **Live S3 object:** `3352ff52...` (the IB-rtm-1 version). This is the rollback target. Versioning is Enabled.

### 2. The change, read at HEAD

- `isOwnDeadlineMessage` is deleted.
- `isRecognizedTimeout` (`:148-154`) has exactly two paths:
  - `error instanceof playwrightErrors.TimeoutError`, guarded by an existence check;
  - `error.name === 'TimeoutError'`.
- Neither path reads `error.message`.
- At `:477`, the `msg` variable exists only for printing. The classification at `:486` calls `isRecognizedTimeout(e)`.

### 3. Behaviour

**Instruments and pins.** All runs used `3.0.0_SA_CVO~B`'s unmodified diagnostics:
- the fixed source `17aff45e`;
- as a negative control, the prior published source `058ba2f8`.

R13 and R12 received the blob EXPLICITLY. R11, R10, R9 and R8 read the worktree; the prior bytes were run in a scratch tree.

**R13 typed-pair @`12738b5791`** — each cell is writes/success:

| Case | Fixed | Prior |
|---|---|---|
| typed deadline-shaped error | 1/true | 1/true |
| SAME text, plain `Error`, no deadline | **0/false** | 1/true |
| SAME text, `TypeError`, no deadline | **0/false** | 1/true |
| plain `Error`, one punctuation change | 0/false | 0/false |
| typed timeout, unrelated message | 1/true | 1/true |
| certificate-error control | 0/false | 0/false |
| **`typeOnlyPairFails`** | **false** | true |

The same-message / different-type pair now SPLITS. That closes the round-13 FAIL on invariant (iii).

**R12 @`5a9a7eed81`**, blob passed explicitly. It is identical to the prior source except one case:
- "actual timeout positive control" goes from 1/true to **0/false**.
- That case throws an UNTYPED `Error`. It is one of the two old-mock cases my round-13 analysis declared HISTORICAL, with terminal as the intended outcome.
- The C-S179 certificate cases stay terminal. The EPERM case stays exit 4.

**R11 @`d20200b92c`.** 11 cases, identical to the prior source except one:
- "same-origin timeout then clean" goes from 1/true to **0/false**.
- This is the other declared-historical untyped mock. It is intended.
- Password-screen, 500 and marker-absent recovery all still succeed.

**R10 and R9.** 6 of 6 cases each, identical to the prior source.

**R8.** 3 of 3 guards hold.

**Stated narrowly:** at those pins, the only behavioural changes are the three this seat's round-13 analysis required:
- the R13 split;
- the two historical untyped mocks going terminal.

### 4. The bar

All four invariants hold:
1. latch-after-capture (R11 storage-wait);
2. main-frame only (R11 non-navigation twins);
3. typed retry causes only (R13 split; R12 and R11 historical cases);
4. truthful failure (R12 EPERM, exit 4).

The R114-AC3 JUDGMENT grade is `3.0.0_SA_CVO~B`'s.

## The capture ask stays HELD

`0.0.0_AB_MSTR` releases it only when BOTH are true:
- R114-AC3 reads PASS;
- the S3 readback equals `ea437510`.

**Push state:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
