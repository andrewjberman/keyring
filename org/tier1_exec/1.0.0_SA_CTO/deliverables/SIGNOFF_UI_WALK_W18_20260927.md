# CTO half -- UI walk WINDOW 18: the round-8 walk, K8 on the async export, four identity reads (packet blob b74de7e4) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~20:2xZ. **Request:** 2.0.0_SA_COO~P msg 102075.

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W18_20260927.md`
@`ec6aae3838`, blob `b74de7e4`. Read at HEAD: `git hash-object` equals `git rev-parse ec6aae3838:<path>`.
**The base texts:** window 17 (`b185fd73`, CTO @`1c73f2d7fa`) and window 9's read-only shape (`6dd81fbf`).

## What was read

- **Part A**, ~D's round-8 walk: GET only on local DEV `3b98939b`, window 9's shape. It is CVO's round-8 grading
  artifact.
- **Part B**, K7/K8 on `Ulim/gmf`. It carries the arms of both export packets (`dd91065c`, `5f45ed04`) and my
  conditions:
  - the POST timed at the client from the HAR;
  - exactly 2 invocations counted by request id;
  - the pointer's binding names this window's principal;
  - the narrative slot never shows internal validation text.
  - On any arm failing, the rollback runs the same turn.
- **Part C**, the four identity reads. The runner `comparison_identity_read_20260927.sh` was read at blob `cf3f4c5d`:
  - it sends exactly the 4 P: ids, `securities_info` only;
  - there is no retry: an exception or a non-200 / login / non-JSON answer stops the act;
  - the transport is closed in `finally`;
  - it writes one evidence file of Opal's own model rows and no client data.
  Authority: CTO 19:01Z (1), with the API egress arm. Andrew's feature permission (@`fce766f6ed`) is separate and not
  needed for the reads.
- **Timing:** it opens only after the CRO's walker is DISARMED, and closes well before MSTR's ~03:00Z freeze.

## Named item (a condition of this half)

**Part C's session:** the resident journal for part C's span must show **0** host re-captures and **0**
`session_refresh` intents. A WAF challenge on a read counts as the read stopping, never as a re-capture. The audit
prints both counts from the journal. A non-zero count is a BLOCKING row the same tick.

**CTO half: SIGNED on blob b74de7e4.** The CRO half is separate.

## RE-SIGN, part C only: runner `cf3f4c5d` -> `3373f308` (~P 102093, @8b62d16176), ~20:5xZ

- Read at HEAD: `git hash-object` equals `git rev-parse 8b62d16176:<runner>` = `3373f308`.
- `git diff cf3f4c5d 3373f308` is ONE line: `UNIT=irpt-resident` becomes `UNIT=irpt-analysis-resident.service`. The
  request loop, the stop rule and the write set are byte-unchanged.
- The unit resolves read-only to the W18-2 pin `/opt/irpt-resident/fe64236bbb-lt`.
- Parts A and B are unaffected. The named item above carries.

**CTO half, part C: RE-SIGNED on runner blob 3373f308.**
