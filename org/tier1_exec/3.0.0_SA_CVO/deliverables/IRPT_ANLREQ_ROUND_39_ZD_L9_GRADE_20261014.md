# IRPT_ANLREQ round 39, workstream ZD -- L9 grades of AR309-y-AC2J, AR310-y-AC2J, AR311-y-AC2J

**Grader:** `3.0.0_SA_CVO~DELL2`, 2026-10-14 ~12:2xZ. **Asked by:** msg 7596. Packet:
`org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND39_ZD_L8_COMPILE_20261014.md`, blob ccc08c2ebf (@9d060ecbe3).
Each criterion is graded on its own order's text (`task-orders/IRPT_ANLREQ.TO-AR-y-30{9,10,11}.*.md`, lines 55-57), not on the packet's
summary of it.

**This seat's own reads:**
- `ar21_checks.py y309-build|y310-build|y311-build --root .` on HEAD prints Y309-BUILD-OK, Y310-BUILD-OK and Y311-BUILD-OK. The
  artifacts re-hash to c8da70e3..., e5344565... and 2de2adce..., equal to the records.
- Live read at 2026-10-14T12:13:19Z: `irpt-status` CodeSha256 MIVrDbv+... (LastModified 2026-10-14T01:51:15Z) and `irpt-ycharts-generate`
  reAjAQOV... (LastModified 02:50:16Z). Both equal the records' live reads and the release-28 apply. Nothing of release 29 is live.
- The host-script diff `r39/diff_host_r28_to_r29.txt`, and a diff of each of the three scripts against its release-28 version
  (`~119/r31/*_r28.sh`).

**Result: 3 of 3 PASS.**

## AR309-y-AC2J (irpt-status) -- PASS

- **Live read in this run.** The record names the commands (`get-function`, `get-function-configuration`) and a downloaded zip whose
  sha256 equals the CodeSha256 (49 members). It is not copied from a record.
- **Guard count printed before each build.** 8 at each of the three trees, `printed_before_build` stated for the control and release
  builds.
- **Both builds BUILD_ONLY.**
- **Delta is exactly one member, words only.** The delta is `status.py` alone (nothing only in live, nothing only in release). The AST
  check shows one key added (SHARES_PRICE_SOURCE_NOT_COMPOSED) and none removed.
- **Nothing uploaded or applied.** The live digest is unchanged at 12:13Z.

## AR310-y-AC2J (irpt-ycharts-generate) -- PASS

- **Live read in this run.** The record carries the commands, a download script run with `python -I`, and a zip equal to CodeSha256
  reAjAQOV... (105 members).
- **The control reproduces the package that is live now.** The control at 0c0ae5a8f5 plus the release-28 input builds reAjAQOV...,
  and this seat read that digest live at 12:13Z. The record also shows that the map's `last_deployed_commit` does NOT reproduce it
  (row W124-S3), so the worker did not take the base on trust.
- **Guard count.** 8 at both trees, printed before each build.
- **Delta.** Exactly `generate_installed.py` and `uploads.py`, plus `ordinary_viewer.py` added. Nothing is only in live, and 103 members
  equal live.
- **Nothing uploaded or applied.** The live digest is unchanged.

## AR311-y-AC2J (the resident tarball) -- PASS

- **Delta.** Exactly `intake/uploads.py`, `ops/status.py`, `reports/resident_bindings.json` and `SHA256SUMS`: 4 differing, 295
  unchanged, 0 added, 0 removed.
- **The host script changes only release naming.** Changed lines: the header, NEW/OLD, WANT_TAR, the two moved members' hash checks, and
  the ledger string. WANT_TAR and the two checks must change with the tarball. Nothing else moved, and the 23 member checks equal the
  tarball bytes.
- **The three scripts change only what release 28 changed, with every guard kept.** This seat diffed `pre_read`, `install` and
  `rollback` against their release-28 versions. Only roots, ledger and comment text, wanted hashes, and read-back values changed. The
  count of guard lines (exit, refuse, sha256 and comparison lines) is equal in each: 5/5, 11/11, 4/4. No exit code moved.
- **A one-byte change is refused by the dry run.** RECORD: rc 31 for the script gate and rc 33 for the sums gate, rc 0 on the
  unchanged copies. This seat did not repeat the dry run; the scratch it ran in is outside the deliverables.
- **Nothing uploaded, installed, applied or run on the host.** The record makes no AWS call and no host call, and its `not_read` list
  names the host and the S3 key as unread.

## Limits

- The worker scratch zips named in the 309 and 310 records are gone (worktrees cleaned). The "read in this run" clause rests on the
  records plus this seat's live digest matching them, not on the downloaded bytes.
- Row W123-S1 (ARMED, `0.7.0_AE_CloudOps~AQ2`) stays open: the map record for `irpt-status` names a commit that does not rebuild the live
  zip. The applier's map-close commit in TO-APPLY-R29a step 7 closes it.

-- 3.0.0_SA_CVO~DELL2
