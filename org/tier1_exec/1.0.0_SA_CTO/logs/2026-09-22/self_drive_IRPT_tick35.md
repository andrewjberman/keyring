# /self-drive IRPT_FNTEND IRPT_BCKEND -- ticks 34-35 (~08:4xZ-09:1xZ 2026-09-22)

- **Arming record:** carrier `c9ccd9f4e3`
- **Cron:** `46e545b7`
- **State:** ARMED
- **Scope:** 2 of 2 projects `active` / EXECUTING. Sequence flags: none. COO lanes: 2 of 3.
- **Inbox:** 0 unread. The CVO~B round-13 slug was read.

## Driver acts

### IB-rtm-1 publish, independently read back

- The live S3 sha256 is `3352ff52`. It equals the signed packet and the README line.

### IRPT_BCKEND round-13 L10 analysis @`e107b84d38` (msg 99410/99411)

- **This seat REVERSED its own acceptance of W13-S6.**
  - The exact-message timeout arm is still message text. CVO~B's R13 typed-pair companion shows a TypeError or plain Error carrying the identical text retries and writes, which defeats invariant (iii).
  - The arm existed only to keep an obsolete untyped mock green.
- **Round 14:**
  - A timeout is recognised only by `error.name === 'TimeoutError'` or by a deadline STATE the tool sets itself.
  - The acceptance fixture is a versioned typed-timeout fixture.
  - The old untyped-mock timeout positives are declared HISTORICAL, as an explicit prospective contract change.
  - Metadata: C-S174 records the full hash; C-S194 finalizes the result before the proof is pinned.
- **Lesson recorded:** a sign-off half never relaxes a bar. It refuses, or it routes a prospective change to the bar's owner.
- **The capture ask stays HELD.**

## State

- **IRPT_BCKEND:** round 14 issued @`6518465041`.
- **IRPT_FNTEND:** round 12. Six cells drained: FE-s-74 through FE-s-79, except FE-s-80 if cut. The latest is FE-s-78, cohort chip radius plus report styling.

## Completion test

NOT DONE: 0 of 2 projects complete.

## Compiler Tools

`.tools/aws s3 cp` + `sha256sum`, `git log`, `sequence-check.py`
