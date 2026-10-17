# /self-drive dell2-box -- ticks 78-79 (2026-10-17 ~02:03Z-02:59Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** the time since the ticks 75-77 log (@7bfae213bb). Substantive delta. Inbox 0 unread.

## Andrew's words this window

- **~02:48Z,** with a screenshot: "still broken on f1bb" (Thiessen, OBJECT_NOT_COVERED). This is expected until the Cottonwood read function is
  live. `~D2`'s ETA by cell is ~06:30Z.
- **~02:5xZ:** "let's just use the match sheet from DELL1 for now" and "have MSTR reach out to DELL1 to get /tdrop of the folder. there is a
  lot of data on this". Recorded @08e88fadba and relayed to MSTR. It lands outside the repo, and `~D2` builds the Cottonwood ownership map from
  it. Global staff do not need the map (`_scope/resolve.py:445-469`); advisor and client views do.

## Acts taken

| act | carrier |
|---|---|
| FWD-1 ADDENDUM 5 AMENDMENT 3 (R0e r34j; weekdays 00-13Z only) SIGNED | @deb2ace7f0 |
| r34j ROLLED BACK. Cause found: lib is not on the resident path (deterministic). r34k: lib on the path once, plus a whole-package import smoke | msgs to `~G2` |
| HMAC list: B (raw ids), then per firm at the mint in `directory_runner.py:484`, one key per firm | msgs to `~P2` |
| f3d4: the 5174 handover waits on Andrew; ruled and CLOSED | @e28f6e1f70 |
| Source-map drain released and LANDED (241 function-map files). d95f, 2031 and 9bfe CLOSED on their XA files. The 49F port is a one-file order to IB2 | msgs |

## Runtime lines carried
- tick78 (02:26Z): quiet. Inbox 0. Open: d95f, 2031 and 9bfe ruled on the laptop (files wait on MSTR's released drain); f1bb, 3c22 held for Andrew; c02c. In flight: the Cottonwood read path (C1), r34k (lib path plus package smoke), the HMAC producer cell 1, the source-map drain.
- tick78+ (02:30Z): MSTR's drain landed (ruling files synced): d95f, 2031 and 9bfe CLOSED on their XA records.
- tick78+ (02:31Z): drain landed: function-map 241 files, source map removed, exemptions.json has the export render row; ~F2 (49F port), ~D2 (cot port check) and ~S2 (fence row present) told.
- tick78+ (02:41Z): the drained function-map entry for the 49F gold function holds first-stage values (SCt7IgN3 and the old pins); ~F2's three-field correction gives BUILD_ONLY equal to JgSV12Tz; ~F2 is not in the lane: routed as a one-file order to IB2 (no lane change), plan must read No changes, before Monday's fire.
- tick78+ (02:49Z): ANDREW re-checked Thiessen on f1bb: still OBJECT_NOT_COVERED (expected: the Cottonwood read function is not built or deployed). Pressed ~D2 for an ETA by cell, C1 and C2 in parallel, the pair drafted alongside.
- tick78+ (02:51Z): Cottonwood read-path ETA ~06:30Z (~D2: C1 ~30m, C2 ~90m, C3 +40m, C4 apply ~60m, C5 ~15m); risk 1 (Cottonwood ownership map absent) to be settled by a code read now. HMAC list: RULED B (raw custodian numbers, from ids in process at mint if present; no new all-firm reader without my word).
- tick78+ (02:58Z): ANDREW: use DELL1's match sheet for now and have MSTR /tdrop the folder from dell1 (record @08e88fadba); relayed to MSTR (outside the repo; path and count to me and ~D2). Ownership map: Global staff do not need it (resolve.py:445-469), advisor and client views do. HMAC list: per firm at directory_runner.py:484 (raw keys in process), one key per firm, the hook reads the union; no combined key. Watcher re-armed.

## ACTS ONLY ANDREW CAN DO

- **f1bb:** approve the Performance tab once Cottonwood shows (CLAUDE.md Portal; XA-3f7e term 5).
- **3c22:** lift C-V1 ("on Andrew's word only", IRPT_YCDGEN PRD :312) or keep it.
- **c02c:** POSTPONED on his word.

Completion test: NOT DONE. state: ARMED

## Compiler Tools

safe-commit.sh, open-calls.py, comp-find, send_message, Monitor.
