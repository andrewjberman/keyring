# DELL1 self-drive box -- tick 210, 2026-10-20 ~23:48Z (delta: the Fidelity box signed in; co-7 addendum 1 countersigned)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 23:48Z. Acked since tick 209: 8863, 8867.
- open_calls.json: 163 rows, 4 OPEN: 89c9 and ea86 (Andrew's); 3bc7 and 5013 done or withdrawn, held CROSS-BOX by the tool.

## Acts and rulings
- **NFRA_FIDUPL: the box signed in at 23:36Z** (P1 8867, record @bbb1ebe05ac). Track B run 4 with REPAIR 13's human-like input, in
  the plain Chrome over CDP: `_abck` field[1] read 0 before the password POST, the password was accepted, "Text me the code" went to
  the ...3066 line, the box helper read the Quo code and submitted it, and the browser reached Home Experience with ATT and JSESSIONID
  present. Logged out (204, 400). Two defects of ours, neither a refusal: the authorize wait (fixed as REPAIR 14 @538bb40f223, accepts
  the home page) and a factor-click race.
  - **Ruled:** GO on the whole thread. One Track A run on the puller profile with the same input: sign-in, the G-switch probe and the
    `account.txt` G-number read (counts only), the six-file download, the landing with its run record, logout. Stop at the first
    refusal. Then FU-s-13's whole-root apply and the schedule under its own addendum.
  - The thirteenth delivery (REPAIR 14) is pending on the box.
- **AMGT_HARVST co-7 addendum 1** (W1 8863): the image digest `sha256:4da76365...`, 286,233,455 bytes, tag `git-9e26b79f7edf`. I
  read ECR myself (one image, equal on every figure) and countersigned @191e42726b. The push scan (HIGH 12) is ruled a finding, not
  a stop, for the deliberate run; W1 filed row S69 @7aee87a440b, and its triage gates the schedule-enable addendum. Stage 3 (the run
  half, schedule DISABLED) may start.

## Scope state
- **NFRA_FIDUPL:** FU-s-10 (thirteenth delivery), FU-s-11, FU-s-13 and FU-x-1 pending. 3 run records, 0 data objects. The 3 fetch
  rules are DISABLED.
- **AMGT_HARVST:** round 100, co-7 at stage 3.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).

## Compiler Tools
- `ecr describe-images`.
- `sha256sum` and `git show <pin>:<path>`.
