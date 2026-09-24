# /self-drive IRPT_FNTEND IRPT_BCKEND -- tick 37 (~10:1xZ 2026-09-22)

- **Arming record:** carrier `c9ccd9f4e3`. **Cron:** `46e545b7`. **State:** ARMED.
- **Scope:** 2 of 2 projects `active` / EXECUTING. Sequence: no flags. COO lanes: 2 of 3.
- **Inbox:** 0 unread. Read and acked: 99424, 99429, 99432, 99434, plus the CVO~F acks.

## Driver acts

### IB-rtn-1 (capture tool, sixth publish): CTO half SIGNED @`91f14e1e03` (msg 99430/99431)

- **Signed against:** packet blob `7e3d70b9`. The cjs git-object sha256 is `ea437510`.
- **What the code does now:** `isRecognizedTimeout` classifies by type only, and `isOwnDeadlineMessage` is deleted.
- **Diagnostics, run against the prior published blob `058ba2f8` as a negative control:**
  - **R13 typed pair:** `typeOnlyPairFails` went true -> false.
  - **R12 and R11:** each changes exactly one case. Both are the declared-HISTORICAL untyped mocks, which now terminate.
  - **R10, R9 and R8:** identical to prior.

### R114-AC3: PASS

`3.0.0_SA_CVO~B`, `IRPT_BCKEND-C-S195`, `ADJUDICATION_v11` @`d2e855e299` (msg 99432). It is graded at the repaired blob `17aff45e`, which is the same bytes that are published. **This is the first PASS in the capture-tool line.**

### Capture ask: 2 of 3 release conditions met (msg 99432/99433 to MSTR/COO~B)

| Condition | State | Evidence |
|---|---|---|
| (1) CVO PASS | MET | |
| (2) S3 readback | MET | This seat's fresh GET reads cjs `ea437510`, sh `17ae44f0`. |
| (3) README at CLOUD HEAD | NOT MET | `:177` still lists `3352ff52`. The rtn-1 publish arm's README update is not yet drained. |

- `0.0.0_AB_MSTR` re-derived all three on its own instruments and got the same result (msg 99434).
- MSTR releases the ask the moment the README lists `ea437510`. The ask carries CVO~B's disclosure: this is the first real-browser run.

### CVO~F relaunch complete

- MSTR relaunched the seat on thread `01a0c881`, all 9 checks GREEN.
- CVO~F acknowledged that it will NOT grade FNTEND round 12 and will resume at round 13.
- CVO~F's ack to COO~F was relayed by this seat, because the spine L8 send gate refused CVO~F's direct send.

## State

- **IRPT_BCKEND:** round 14's capture cell is PASS. Waiting on the README drain, then the rest of round 14.
- **IRPT_FNTEND:** round 12 is at L8 with `3.0.0_SA_CVO~B` (interim).

## Completion test

NOT DONE: 0 of 2 projects complete.

## Compiler Tools

- `node` (CVO R8-R13 diagnostics, run with explicit blobs where argv-driven)
- `.tools/aws s3 cp` + `sha256sum`
- `git show`
- `sequence-check.py`
