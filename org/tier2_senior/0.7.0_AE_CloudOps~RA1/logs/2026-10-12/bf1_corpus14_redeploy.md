# 0.7.0_AE_CloudOps~RA1 -- 2026-10-12 -- AMGT_RESAPP AMGT-bf-1: AMGT_CORPUS's /14 corpus files redeployed from a merged pin, bd-1's serve kept

**Date:** 2026-10-12 (GO 00:06Z, msg 4185; captures 00:15-00:21Z; apply 00:23:02Z; function LastModified 00:23:30Z; ledger closed after AC1-AC3)
**Task Order:** AMGT_RESAPP.TO-AMGT-bf-1.redeploy-the-scoped-api-carrying-the-14-corpus-files-from-a-merged-pin
**Status:** COMPLETE (AC1, AC2, AC3 PASS; ledger CLOSED 10 of 10; the slow-request clause read PASS)

## Objective

The second corpus redeploy of `opal-amgt-scoped-api`, from the MERGED pin `b3d4856531` (a `box/dell1` first-parent commit; /15 not
carried): AMGT_CORPUS's `dossier.py` METHOD /14 and its corpus files, with bd-1's listing-sector serve kept. The served effect is
the Thesis payload's `model.team_sheet` at the stored /14 field: 252 label rows on 83 names move from `absent` to `held`.

## The act
**archetype:** DEPLOY

1. Read both halves and the order; verified the pin is on the first-parent line and carries bd-1's two blobs. Detached worktree;
   `r94_admission_table.py --pin a03d92221a` showed exactly the half's three lib members at its blobs; the replay read YES (88 calls).
2. Captured the rollback package (hash-checked), re-hashed the wheels (6 of 6), read the source-map entry, swept 65 worktrees (1256
   entries): in the shared tree only this seat's entry and AMGT_CORPUS's `r49-ay3` (the /15 write, OPEN, new objects the /14 reader
   skips; named in the ledger and to the issuer).
3. Built at the pin offline: 408 files, CHANGED 2 (`dossier.py`, `team_sheet.py`), ADDED 0, off-list 0; bd-1's members identical.
4. Captured, in sequence and single-threaded, the 528-request route baseline (with per-request duration and request id) and the 95
   live Thesis payloads (`aw4_capture.py`, local and uncommitted), the latter finishing minutes before the apply.
5. Uploaded with read-back, planned untargeted (1 of 53), applied through `safe-apply`, told the issuer at once and asked for a HOLD on
   every other reader until this seat reported.
6. Post-act, as the only reader: thesis capture and `ax7_compare` read Branch A (95/95, 95/95, growth within delta 0, max 1,289,958 B,
   as predicted); the timed route replay read status moved 0 and exactly the half's 88 `team_sheet` paths on 7 subjects. One request
   over 20 s (the first request of the sequence, 24.9 s; 29.3 s before the apply), re-invoked three times at 200 with identical bytes.
7. AC1-AC3 PASS; the hold released; the record step; the ledger closed.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L10, close | PASS | opened before the first live act |
| r94_admission_table.py / r94_naming_replay.py | at the pin, --pin a03d92221a | PASS | 3 members; YES |
| build-and-upload-scoped-amgt.sh | --build-only | PASS | offline, 0 downloads |
| aw4_capture.py / ax7_compare.py | pre and post | PASS | build 1/1; local, uncommitted |
| bf1_capture.py | timed capture, replay, compare | PASS | per-request duration and request id for the slow clause |
| r97 / r95 / r94 / r89 / r92 checks | AC1, AC3 | PASS | exit 0 |

**What worked:** asking for the HOLD in the APPLIED message instead of assuming the relay would wait; timing every request so the
slow-request clause was answered from a record, not from memory; capturing the baseline first and the thesis last so the thesis
capture sat minutes before the apply.
**What failed:** nothing in the act. One thing learned: the slow request in both this act and round 98 is the first request of a
sequence after idle (ASML_NA overlay, 29.3 s before the apply, 24.9 s after, 6.6 s on the first re-invoke, then 1.0 and 0.9 s).
**Gap found:** none new; the pattern is stated for round 100's cell.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Proceeded with AMGT_CORPUS's `r49-ay3` open | the /13 and /14 readers pick among objects at their own literal; /15 objects are new keys; a corpus path outside the half's table would have been the signal, and there was none |
| Released the hold myself once my reads were done | the issuer's hold was tied to my report; my reads were complete and the message said so |
| Did not repeat the package-level builder probe | opal_naming and the registry files are byte-equal to the live package |

## Files Modified

- `org/critical_paths/change_management/20261012T0008Z_amgt-resapp-r99-bf1-corpus14-redeploy-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the derived compare report and the proof instance
- `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/harvest/CHANGELOG.json` (record commit d0da5d590d)
- the order's `<status>` (complete)
- local only, uncommitted: `.scratch_bf1/thesis_pre.json`, `.scratch_bf1/thesis_post.json`

## Next Steps

1. `[2.0.0_SA_COO~C1]` Post-act read and FWD-20's label-share census; /15 (ay-3) is a THIRD redeploy under its own pair.
2. `[2.0.0_SA_COO~R1]` Round 100's overlay cell: first-request-after-idle tail and the pool warnings; the pin worktree is the issuer's to remove.
3. `[box-sync / MSTR]` Push the local commits.
