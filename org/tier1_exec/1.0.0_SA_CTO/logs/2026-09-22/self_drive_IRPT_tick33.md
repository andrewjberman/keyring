# /self-drive IRPT_FNTEND IRPT_BCKEND -- ticks 32-33 (~07:4xZ-08:1xZ 2026-09-22)

| Field | Value |
|---|---|
| Arming record | carrier `c9ccd9f4e3` |
| Cron | `46e545b7` |
| State | ARMED |
| Projects | 2 of 2 `active` / EXECUTING |
| Sequence | no flags |
| COO lanes | 2 of 3 |
| Inbox | 0 unread; 99406 read and acked |

## Driver acts

### IB-rtm-1: CTO half SIGNED @`32a554592e` (msg 99407/99408)

This is the capture tool's fifth publish.

- **Signed against:** packet blob `db092cbd`; the cjs file's sha256 is `3352ff52`.
- **Diagnostics:** R12 through R8 were run against the fixed bytes, with `82abe684` as the negative control.
  - **C-S179** flips: a certificate error whose message contains `timeout=1` is now terminal.
  - **C-S180** flips: an EPERM on cleanup now exits 4 with a truthful message, disclosing `diskFinal`.
  - R11, R10, R9 and R8 are identical to the prior bytes.
  - All four invariants hold.
- **W13-S6 accepted:** the second timeout arm is an exact-string match, which is the tool's own deadline.

### Self-correction: the R12 diagnostic tests the wrong blob by default

- The diagnostic takes the blob under test from `argv[2]` and **defaults to the OLD blob** `82abe684`. It does not read the worktree.
- My first "fixed" run passed no argument, so it measured the old code and made C-S179 look unfixed.
- I caught this before signing, corrected it in the half, and warned COO~B and CVO~B.
- Lesson: before trusting a diagnostic, name the object it actually reads. The trap class is "A POSITIONAL/DEFAULT INPUT CAN MAKE A DIAGNOSTIC MEASURE THE WRONG OBJECT SILENTLY".

## State

- **IRPT_BCKEND:** round 13, with rtm-1 drained. Next come the publish, then CVO~B's R113-AC3 grade.
- **IRPT_FNTEND:** round 12. Drained so far: FE-s-74, 75, 76 and 79. COO~F is amending FE-s-77 and FE-s-78 after the workers flagged defects.
- **The capture ask stays HELD.**

## Completion test

NOT DONE: 0 of 2 projects complete.

## Compiler Tools

`node` (CVO diagnostics R8-R12, run with an explicit blob argument), `git diff`, `git show | sha256sum`, `sequence-check.py`.
