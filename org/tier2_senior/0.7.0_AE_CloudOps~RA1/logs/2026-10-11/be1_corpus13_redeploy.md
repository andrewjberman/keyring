# 0.7.0_AE_CloudOps~RA1 -- 2026-10-11 -- AMGT_RESAPP AMGT-be-1: AMGT_CORPUS's /13 corpus files redeployed from a merged pin, bd-1's serve kept

**Date:** 2026-10-11 (GO 22:00Z, msg 4141; captures 22:08-22:13Z; apply 22:14:54Z; function LastModified 22:15:23Z; KEEP 22:29Z; ledger closed after AC1-AC3)
**Task Order:** AMGT_RESAPP.TO-AMGT-be-1.redeploy-the-scoped-api-carrying-the-13-corpus-files-from-a-merged-pin
**Status:** COMPLETE (AC1, AC2, AC3 PASS; ledger CLOSED 10 of 10; one STOP-class item ruled KEEP by the CTO)

## Objective

One code redeploy of `opal-amgt-scoped-api` from the MERGED pin `a03d92221a` (a `box/dell1` first-parent commit): AMGT_CORPUS's
`dossier.py` at METHOD /13 and its corpus files, with bd-1's listing-sector serve kept (the pin's `scoped_amgt.py` and
`monthly_chatter.py` are bd-1's blobs). The served effect is the Thesis payload's `model.team_sheet` at the stored /13 field.

## The act
**archetype:** DEPLOY

1. Read both halves and the order; verified the pin is on the first-parent line, carries bd-1's two blobs, and is neither
   `box/dell1` HEAD (which carries /14) nor a scratch pin. Detached worktree; `r94_admission_table.py --pin 08d5ea2920` showed the
   half's six lib members at its blobs and the two registry files; the replay read YES (81 calls, 0 differ).
2. Captured the rollback package (hash-checked), re-hashed the wheels (6 of 6), read the source-map entry, swept 63 worktrees
   (1213 entries): only this seat's own entry names the function's projects; AMGT_CORPUS's /13 and /14 writes are both CLOSED.
3. Built at the pin offline: 408 files, CHANGED 4 (`exemptions.json`, `opal_naming.py`, `dossier.py`, `team_sheet.py`), ADDED 0,
   off-list 0. The package carries a subset of the half's eight admitted members. One extra control: unzipped the built and the
   live packages and compared the naming builder on the packaged registry (7 files, no `name_rulings.json`): 15 of 15 equal.
4. Captured, immediately before the apply, the 95 live Thesis payloads (`aw4_capture.py`, local and uncommitted) and the 527-request
   route baseline.
5. Uploaded with read-back, planned untargeted (1 of 53), applied through `safe-apply`, sent the CodeSha256 and apply time at once.
6. Post-act: thesis capture and `aw4_compare` read Branch A (95/95, 95/95, growth within delta 0, max 1,289,805 B). The first route
   replay read one request with no status (an overlay timeout at 29 s, concurrent with the issuer's own thesis sweep); reported
   STOP-class with evidence and a rollback deadline; the CTO named KEEP (ADDENDUM 1). The second replay, with no concurrent
   capture of ours, read status moved 0 and exactly the half's 981 `team_sheet` paths on 10 subjects.
7. AC1-AC3 PASS; the record step; the ledger closed; both scratch branches read after the apply.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L10, close | PASS | opened before the first live act |
| r94_admission_table.py / r94_naming_replay.py | at the pin, --pin 08d5ea2920 | PASS | 6 lib + 2 registry; YES |
| build-and-upload-scoped-amgt.sh | --build-only | PASS | offline, 0 downloads |
| aw4_capture.py / aw4_compare.py | pre and post | PASS | build 1/1; local, uncommitted |
| aa5_capture.py | capture, replay x2, compare | PASS (second replay) | first replay: one timeout, KEEP |
| r97 / r95 / r94 / r89 / r92 checks | AC1, AC3 | PASS | exit 0 |

**What worked:** grading the payload bound on the live-before vs live-after read as the half specified; stating the one anomaly with
the pre/post latency distribution and a deadline instead of waiting or self-waiving; reading the package's own naming builder
rather than only the worktree's.
**What failed:** my route replay ran at the same time as the issuer's four-thread thesis sweep, which neither of us had flagged to
the other; the one timeout landed in that overlap. Recorded in L8; the CTO ruled it one transient.
**Gap found:** the half's table calls `template.py` and `factset_descriptions.json` "packaged, inert"; the package's import closure
does not carry them (CHANGED 4, ADDED 0). Inside the admitted set; noted in L5.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Reported the timeout as STOP-class and held until the CTO ruled | the half names "a status other than 200" as Branch 2; the evidence argued for KEEP but the ruling is the CTO's |
| Did not roll back while the ruling was pending | the deadline was 23:05Z and the issuer asked for the second replay first |
| Committed a derived compare only | the thesis `team_sheet` values are client research content and stay local |

## Files Modified

- `org/critical_paths/change_management/20261011T2201Z_amgt-resapp-r98-be1-corpus13-redeploy-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the derived compare report and the proof instance
- `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/harvest/CHANGELOG.json` (record commit 002626cdbe)
- the order's `<status>` (complete)
- local only, uncommitted: `.scratch_be1/thesis_pre.json`, `.scratch_be1/thesis_post.json`

## Next Steps

1. `[2.0.0_SA_COO~R1]` Delete the two scratch branches after the post-act reads close (the CTO's condition); round 99 reads the overlay tail per name.
2. `[2.0.0_SA_COO~C1]` Post-act read and FWD-12/20's rendered census on DEV; /14 follows as a second redeploy under its own pair.
3. `[box-sync / MSTR]` Push the local commits; `C:/tmp/be1-build` is left in place for the user to clear (a recursive deletion).
