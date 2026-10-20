# /self-drive dell2-box -- ticks 183-184 (2026-10-20 ~18:27Z-19:26Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** ticks 183 and 184, since the tick 182 log (@0d05e73551). state: ARMED.

## Grants live

- **Status grant** (irpt-status reads `ycharts_opal_reports`): LIVE at 18:33Z (IB2 `A_AFTER_STATUSGRANT.txt`). Read here:
  simulate `s3:GetObjectVersion` on the denied key gives allowed.
- **Model grant v2** (the resident reads the model series and positioning): CTO re-signed @15bb73cc19 on packet v2 (blob
  6407306176; `git diff -w` empty). LIVE at 18:47Z (IB2 `A_AFTER_MODELGRANT_R2.txt`: G1 to G4 hold, and the host role read
  both objects).
- **Audit address:** Andrew answered "OK, per-firm folder (Recommended)" (`~TCKT` record @5635d7306c). The CVO re-signed v0.28
  @7be5e376e9.

## Run 7c: STOP at R (IB2 `A_E2E7C.txt`)

- **Green:** B1 to B3, P1 to P7 (filed TCK-20261020-85182d16 / REQ-1eb7e112fd97eaebddf1a3f6 at 18:57:03Z; package COMPLETE at
  18:59:16Z, 4 items held), and R2.
- **R refused** with INVALID_INPUT (`COMMENTARY_PDF_BINDING`). Run 7b's AccessDenied is gone.
- **Cause, read in source:**
  - `opal_packager.live_retained_package` (:285-286) retains the commentary PDF under logical id
    `<req>-commentary-<DRAFT sha256>`.
  - `owned_report.commentary_pdf` (:354-371) refuses when the retained PDF's sha256 differs from that draft sha, which it always
    does.
- **Ruled** (msg 11508): fix the route, with a test that fails on today's code. It ships as a code-only irpt-status release
  under a never-widen pair, then run 7d. `~Y2` cut AR-y-470 (worker 344).
- **`/pdf`:** no run has read the Opal report route. Ruled: probe it before the release. No live probe is possible (the
  7b and 7c rows are deleted), so `~Y2` cut AR-y-471, an offline trace through the real writers. A FAIL rides the same
  release. Run 7d reads both routes and saves the `/pdf` result as Andrew's FWD-9 sample.

## Acts only Andrew can do

- **Row a331** (an entitlement): the outside-domain users row in TCKT_VNEXT-D2-S53, which carries the internal firm id.
- **Recursive deletions and discards of uncommitted files** (CLAUDE.md, Agent Autonomy: "Human confirmation ONLY for:
  recursive deletion, destructive git"): `C:\dev\wk-irpt-dashbd-503`; row 544d; row 65a1; row a392.

## Completion test

NOT DONE. The dell2-box scope is a keep-driving scope; it ends on Andrew's stand-down word.

state: ARMED
