# self-drive cluster open calls -- tick 75 (2026-10-15 ~11:5xZ), 1.0.0_SA_CTO laptop

state: ARMED   cadence: 60m   cron: 6ca5a587   ticks covered: 75

## Measurements this tick

- Cluster list, read ~11:56Z: boxes=4, read=4, absent=none; open=22 (fork 2, act 20), closed=205.
- Changes since tick 74:
  - NEW site Z `f6f4` (act, OPAL_BBGTML): sign the Bloomberg Terminal in at site Z.
    - The 11:00Z unattended sign-in failed again: focus was lost at submit, with zero Bloomberg attempts, even with fix R3
      in place.
    - Served Bloomberg data is 2 trading days behind.
    - A human sign-in is the only immediate unblock, confirmed by `dapi_check.py`. The defect trace goes to `COO~ZB`.
    - Record: `CTO_RULING_OPAL_BBGTML_FOCUS_DEFECT_OWNER_20261015_Z.md`.
  - Laptop disk: 23G.
- Other changes this hour:
  - NFRA_CTLPLN round 18 analysis @721e05298f, with a coverage correction: 2 of 28 FWDs realized, and rounds 13-18 were
    hygiene (this seat's failure to read the endpoint back).
  - The CVO owes a full re-grade; round 19 cuts outcome cells first.
  - DSGN_RBNDV2 round 2 analysis @3c2a9cae02.

## Calls this tick

- None for this seat. `f6f4` is Andrew's act (a person at the console).

## Acts only Andrew can do

- Site Z: `f6f4` (the Bloomberg sign-in, new and time-sensitive); `21d9`, `def4`/`3b41`, `a519`, `21c5`/`8ed7`/`f0d2`.
- Laptop: `3c44` (the DSGN_RBNDV2 look); `be0b` (heat maps); `715c`; `7841`; `8f2b`, `44eb`, `e435`; G4.
- dell2: `c02c` (P1); `d8ae`, `53cb`; `f61b` (P2), `a252` (P1), `2106`, `e260`.
