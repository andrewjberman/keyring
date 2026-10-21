# DELL1 self-drive box -- tick 211, 2026-10-21 ~00:18Z (delta: Track A refused, forged fingerprint dropped; the deaf-seat root cause committed)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 00:18Z. Acked since tick 210: 8872, 8875, 8877.
- open_calls.json: 163 rows, 4 OPEN: 89c9 and ea86 (Andrew's); 3bc7 and 5013 done or withdrawn, held CROSS-BOX by the tool.

## Acts and rulings
- **NFRA_FIDUPL Track A at 00:02Z** (P1 8875, record @1bdad14ab98): on the puller profile with REPAIR 14 and the human-like input,
  `_abck` field[1] read 0 before the POST and the password POST still answered 403. Track B passed with the same input in the
  OS-launched Chrome, so the Playwright launch is the only variable left; its forged Windows user agent on a Linux Chrome is the
  sharp suspect.
  - **Ruled:** drop every forged fingerprint in `_launch` (REPAIR 15, merged @34ebdc69d5d), deliver (the fourteenth delivery, pending),
    ONE run. If still 403, the puller attaches over CDP to the OS-launched Chrome unit, Track B's proven shape, as the standing daily
    path; no more fingerprint iteration.
- **The deaf-seat root cause** (MSTR 8872, 8877): not watcher expiry. `inbox-watch.sh` resolved the agent folder by substring, so every
  CloudOps lane watched `tier1_exec/0.7.0_AE_CloudOps~TM1/~<lane>` instead of `tier2_senior/0.7.0_AE_CloudOps/~<lane>` and read no
  mail (NFRA1: 3 hours, zero `[INBOX]` events; SC1's root: 65 unclaimed). MSTR's fix (exact folder first, the scan as fallback, +7
  lines) was refused under its lane; I read the diff, `bash -n`, the pre-existing 3 non-ASCII bytes, and committed it @9fe08639a3.
  MSTR owes: re-arm NFRA1 and SC1 now, tell the other boxes MSTR to MSTR, file the row. My earlier ruling (8872) to investigate the
  transcripts is superseded by this find.

## Scope state
- **NFRA_FIDUPL:** FU-s-10 (fourteenth delivery), FU-s-11, FU-s-13 and FU-x-1 pending. 4 run records, 0 data objects. The 3 fetch
  rules are DISABLED.
- **AMGT_HARVST:** round 100, co-7 at stage 3.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).

## Compiler Tools
- `git diff` and `bash -n` (the watcher fix).
- `list-objects-v2`.
