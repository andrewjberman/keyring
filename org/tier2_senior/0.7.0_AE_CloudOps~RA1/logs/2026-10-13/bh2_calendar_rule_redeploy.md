# 0.7.0_AE_CloudOps~RA1 -- 2026-10-13 -- AMGT_RESAPP AMGT-bh-2: the calendar rule for the freshness snapshot applied, no served byte moved

**Date:** 2026-10-13 (GO 13:01Z, msg 4823; captures 13:09-13:14Z; apply 13:16:29Z; function LastModified 13:17:52Z; ledger closed after AC1-AC3)
**Task Order:** AMGT_RESAPP.TO-AMGT-bh-2.redeploy-the-scoped-api-carrying-the-calendar-rule-from-a-merged-pin
**Status:** COMPLETE (AC1, AC2, AC3 PASS; ledger CLOSED 10 of 10; the cold-live arm read NOT QUIET, the alternative the order names)

## Objective

One code leg of `opal-amgt-scoped-api` from the MERGED pin `7da642c1ff`, whose one change is `AMGT-bh-1`'s
`lib/research/freshness/snapshot.py` (`f8df11bd6cce` -> `64fa354a1e1c`): a stored coverage snapshot counts as current when
written at or after the latest trading day's 12:30Z write, where it counted only 24 hours (the weekend steady state). On a
weekday after the write, the snapshot is current under both rules, so no served byte may move.

## The act
**archetype:** DEPLOY

1. Read both halves and the order; verified the pin is on the first-parent line and that the live CodeSha256 reads `42z0tn68...`
   first, as the GO requires. Detached worktree; `r94_admission_table.py --pin ba22af15f5` printed exactly ONE member; the replay
   read YES (78 calls, 0 differ).
2. Printed the rebuild rollback's blob table (`ba22af15f5`) before the apply, kept the live package as a hash-checked reference,
   re-hashed the wheels (6 of 6), read the source-map entry, swept 34 worktrees (501 entries): only this seat's entry.
3. Built at the pin offline: 408 files, CHANGED 1 (`snapshot.py`), ADDED 0, off-list 0.
4. Read the stored snapshot straight from S3 through the pin's module (generated 12:30Z, age 0.76 h, current by both rules), then
   captured, in sequence and single-threaded, the timed 527-request route baseline and the 95 thesis payloads (local, uncommitted).
5. Uploaded with read-back, planned untargeted (1 of 53), applied through `safe-apply`; the FIRST reads after the apply were a
   simultaneous cold pair (25.3 s and 21.7 s, 200, identical); told the issuer and asked for a HOLD.
6. As the only reader: the timed replay (status moved 0, clocks only, 0 over 20 s), the thesis capture and `ay4_compare` (95/95,
   95/95, growth 0 for every name), AC1, then AC3's three checks (`R101 SNAPSHOT EQUAL: YES`, `R101 COLD LIVE: NOT QUIET`,
   `R89 DEPLOYED CLOSE: YES`).
7. The hold released; the record step; the ledger closed.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L10, close | PASS | opened before the first live act |
| r94_admission_table.py / r94_naming_replay.py | at the pin, --pin ba22af15f5 | PASS | 1 member; YES |
| build-and-upload-scoped-amgt.sh | --build-only | PASS | offline, 0 downloads |
| snap_read.py | the stored snapshot from S3 via the pin's module | PASS | no invocation of the function |
| aw4_capture.py / ay4_compare.py | pre and post | PASS | growth 0 for every name; local, uncommitted |
| bf1_capture.py, cold_pair.py | timed capture/replay; first-request pair | PASS | clocks only; recorded |
| r97 / r95 / r94 / r101 / r89 checks | AC1, AC3 | PASS | exit 0 |

**What worked:** reading the snapshot's own object before the apply to confirm the half's premise (current by both rules), so a
moved byte would have been unexplained; printing the rebuild rollback's blob table first, since the function keeps no previous
version; replay FIRST after the apply so nothing warmed the function before the first requests.
**What failed:** my snapshot helper first tripped on a naive-vs-aware datetime in the pin's age function; fixed and re-read
before the apply. Nothing in the act.
**Gap found:** the cold-live check printed NOT QUIET because the preceding 15 minutes held 925 invocations (my own captures); a
quiet reading of it on a weekday needs the issuer's window, not this order's.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Kept the live package as a reference although the rollback is a rebuild | a hash-checked copy costs one download and shows the base the content diff was taken against |
| Accepted NOT QUIET as AC3's reading | the order names it as an alternative: "the numbers printed are graded"; the warm figures are 0.74 s and 0.67 s |
| Did not claim the cold first request | the half says the act is not its lever; the live reading (25.3 s, 21.7 s) is unchanged within the spread |

## Files Modified

- `org/critical_paths/change_management/20261013T1304Z_amgt-resapp-r101-bh2-calendar-rule-redeploy-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the derived compare report and the proof instance
- `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/harvest/CHANGELOG.json` (record commit 7a5e939c9b)
- the order's `<status>` (complete)
- local only, uncommitted: `.scratch_bh2/thesis_pre.json`, `.scratch_bh2/thesis_post.json`

## Next Steps

1. `[2.0.0_SA_COO~R1]` The weekend read (Saturday 2026-10-17 from 12:35Z): three deliberate warm overlay requests more than 60 s apart, Lambda against Lambda.
2. `[2.0.0_SA_COO~R1]` Round 102's phase logs for the cold first request; remove the pin worktree (`C:/tmp/bh2-build` is the user's to clear).
3. `[box-sync / MSTR]` Push the local commits.
