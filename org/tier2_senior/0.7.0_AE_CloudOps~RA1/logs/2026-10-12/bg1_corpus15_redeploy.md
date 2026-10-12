# 0.7.0_AE_CloudOps~RA1 -- 2026-10-12 -- AMGT_RESAPP AMGT-bg-1: AMGT_CORPUS's /15 corpus files redeployed from a merged pin, bd-1's serve kept

**Date:** 2026-10-12 (GO 02:41Z, msg 4229; captures 02:47-02:53Z; apply 02:54:49Z; function LastModified 02:55:18Z; KEEP 03:07Z; ledger closed after AC1-AC3)
**Task Order:** AMGT_RESAPP.TO-AMGT-bg-1.redeploy-the-scoped-api-carrying-the-15-corpus-files-from-a-merged-pin
**Status:** COMPLETE (AC1, AC2, AC3 PASS; ledger CLOSED 10 of 10; one STOP-class item ruled KEEP by the CTO)

## Objective

The third corpus redeploy of `opal-amgt-scoped-api`, from the MERGED pin `6e8dcaf414`: AMGT_CORPUS's `dossier.py` METHOD /15 and
`team_sheet.py`, with bd-1's listing-sector serve kept and AMGT-bg-2's S3-client change NOT carried (a later apply). The served
effect is the Thesis payload's `model.team_sheet` BLOCK rows (3,103) and the `blocks` key at the stored /15 field.

## The act
**archetype:** DEPLOY

1. Read both halves and the order; verified the pin is on the first-parent line, carries bd-1's two blobs, and is not `box/dell1`
   HEAD (bg-2's `scoped_amgt.py` `9f72b58aa87e`). Detached worktree; `r94_admission_table.py --pin b3d4856531` showed exactly the
   half's two lib members at its blobs; the replay read YES (88 calls, 0 differ).
2. Captured the rollback package (hash-checked), re-hashed the wheels (6 of 6), read the source-map entry, swept 64 worktrees (1232
   entries): only this seat's entry in the shared tree; AMGT_CORPUS's `ay3` closed.
3. Built at the pin offline: 408 files, CHANGED 2 (`dossier.py`, `team_sheet.py`), ADDED 0, off-list 0; bd-1's members identical.
4. Captured, in sequence and single-threaded, the 528-request timed route baseline and the 95 live Thesis payloads (local and
   uncommitted), the latter finishing at 02:53:35Z, minutes before the apply.
5. Uploaded with read-back, planned untargeted (1 of 53), applied through `safe-apply`, told the issuer at once and asked for a HOLD.
6. Post-act, as the only reader: thesis capture and `ay4_compare` read Branch A (95/95, 95/95, growth within delta 0, max 1,303,205 B
   as predicted). Replay 1 read one overlay request with no status (a 29 s timeout, position 1) and a second at 28.4 s (200);
   reported STOP-class with evidence and a deadline; six re-invokes were 200 with identical bytes; the CTO named KEEP (ADDENDUM 1).
   Replay 2 read status moved 0, 0 requests over 20 s, the half's 663 `team_sheet` paths on 10 subjects, and six data-landing
   overlay paths that a control (the old package's own code, run locally) reproduced.
7. AC1-AC3 PASS; the hold released; the record step; the ledger closed.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L10, close | PASS | opened before the first live act |
| r94_admission_table.py / r94_naming_replay.py | at the pin, --pin b3d4856531 | PASS | 2 members; YES |
| build-and-upload-scoped-amgt.sh | --build-only | PASS | offline, 0 downloads |
| aw4_capture.py / ay4_compare.py | pre and post | PASS | build 1/1; local, uncommitted |
| bf1_capture.py | timed capture, replay x2, compare | PASS on replay 2 | per-request duration, request id, position |
| r97 / r95 / r94 / r89 / r92 checks | AC1, AC3 | PASS | exit 0 |

**What worked:** the bf-1 instruments reused unchanged; the per-request timing and position let the issuer's question (which
requests exceed 20 s, and is each the first of its sequence) be answered from a record; the six unexpected overlay paths were
settled by a control (the old package's code on the same pool) in one run, not by argument.
**What failed:** an addition slip in my own L8 proof text (701 for 706), caught on reading the numbers back and corrected before the
commit. The `bf-1` worktree I wanted for the control had been removed by the issuer, so the control used the kept rollback package.
**Gap found:** none new. The overlay first-request tail is again position 1 of the sequence; the CTO has it as bg-3's close.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Reported the timeout as STOP-class and held for the CTO | the half names "a status other than 200" as Branch 2, and replay 1 also had a second slow request, outside the clause's "one" |
| Ran the second replay before AC1/AC3 | the issuer asked for it, and AC runs are readers: nothing of mine ran alongside it |
| Ran the old-code control on the unpacked rollback package | the way to tell a data landing from a code effect is to serve the same pool from the old code |

## Files Modified

- `org/critical_paths/change_management/20261012T0243Z_amgt-resapp-r100-bg1-corpus15-redeploy-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the derived compare report and the proof instance
- `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/harvest/CHANGELOG.json` (record commit 7eed486add)
- the order's `<status>` (complete)
- local only, uncommitted: `.scratch_bg1/thesis_pre.json`, `.scratch_bg1/thesis_post.json`

## Next Steps

1. `[2.0.0_SA_COO~C1]` Post-act read and the DEV census (FWD-20's last read).
2. `[2.0.0_SA_COO~R1]` AMGT-bg-3 as the SECOND apply under its own pair; its close covers the first overlay request after idle.
3. `[box-sync / MSTR]` Push the local commits; `C:/tmp/bg1-build` is the issuer's to remove and the user's to clear.
