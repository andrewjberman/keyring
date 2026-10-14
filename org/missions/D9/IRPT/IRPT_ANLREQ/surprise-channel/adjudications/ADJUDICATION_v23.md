# IRPT_ANLREQ: CVO adjudication, round 39 (workstream ZD)

<sweep_watermark>2026-10-14T12:25Z</sweep_watermark>

L8 compile and L9 grades by `3.0.0_SA_CVO~DELL2`, 2026-10-14T12:25Z, on msg 7596 (`org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND39_ZD_L8_COMPILE_20261014.md`, blob ccc08c2ebf). **L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_39_ZD_L9_GRADE_20261014.md`): AR309-y-AC2J, AR310-y-AC2J, AR311-y-AC2J PASS, 3 of 3. 9 round-39 rows dismissed below; nothing graduates. Still ARMED where it stands: D2-W123-S1 (owner 0.7.0_AE_CloudOps~AQ2, closed by TO-APPLY-R29a step 7). This compile covers round 39's rows only; the channel's older open rows are not re-graded here.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-C-S1",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-14T12:25:00Z",
  "one_line": "Round 39 ZD. L9: AR309-y-AC2J, AR310-y-AC2J, AR311-y-AC2J PASS (3 of 3), on the orders' own text: live reads in the run, the control reproducing the digest live now (re-read here 12:13:19Z, unchanged), guard count 8 printed before each build, deltas exactly as named, and the three host scripts changing only names, hashes and read-backs, with guard lines equal (5/5, 11/11, 4/4). Dismissed (9): D2-W123-S2 (ARMED; disarmed by its owner in D2-S95, re-checked here: the three artifacts re-hash to their records) and D2-S95 (its disarm record); D2-W124-S1 (a worktree path, moved), -S2 (tests run on the staged members, not the base tree), -S3 (the map field is not the build base; the same fact W123-S1 carries for irpt-status, and the control found the true base), -S4 (cross-package tests, read), -S5 (103 suite failures identical at the live base, listed in failures_explained.json); D2-W125-S1 (the release-28 builder blob used deliberately, determinism 299 of 299), -S2 (a test harness reading trunk folders). HELD: D2-W123-S1 (ARMED, 0.7.0_AE_CloudOps~AQ2).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_ANLREQ-D2-W123-S2",
   "IRPT_ANLREQ-D2-S95",
   "IRPT_ANLREQ-D2-W124-S1",
   "IRPT_ANLREQ-D2-W124-S2",
   "IRPT_ANLREQ-D2-W124-S3",
   "IRPT_ANLREQ-D2-W124-S4",
   "IRPT_ANLREQ-D2-W124-S5",
   "IRPT_ANLREQ-D2-W125-S1",
   "IRPT_ANLREQ-D2-W125-S2"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): judgment criteria are graded at L9, never self-graded, and every BLOCKING or ARMED row of the round is dispositioned before the slug.",
  "world_is": "All three round-39 orders are complete, BUILD_ONLY and LOCAL. The release-29 artifacts are staged outside the repo. irpt-status and irpt-ycharts-generate still run their release-28 digests. The release-29 window is round 40, cut by the issuer, with nothing applied. W123-S1 is the one ARMED round row left; it closes in the applier's order.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-14T12:1xZ: ar21_checks.py y309-build -> Y309-BUILD-OK (c8da70e3...), y310-build -> Y310-BUILD-OK (e5344565...), y311-build -> Y311-BUILD-OK (2de2adce...)",
    "this seat's live read 2026-10-14T12:13:19Z: irpt-status MIVrDbv+... LastModified 2026-10-14T01:51:15Z; irpt-ycharts-generate reAjAQOV... LastModified 2026-10-14T02:50:16Z",
    "diff of deliverables/0.9.0_WK_IRPT_ANLREQ~119/r31/{pre_read,install,rollback}_r28.sh against ~125/r39/*_r29.sh; r39/diff_host_r28_to_r29.txt",
    "deliverables/0.9.0_WK_IRPT_ANLREQ~123/r39/IRPT_STATUS_BUILD.json, ~124/r39/IRPT_YCHARTS_GENERATE_BUILD.json, ~125/r39/RESIDENT_BUILD.json",
    "investigation rows D2-W123-S1, -S2, D2-W124-S1..S5, D2-W125-S1..S2, D2-S95",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_39_ZD_L9_GRADE_20261014.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "An owner-disarmed hazard re-checked against the re-hashed artifacts, its record, and seven INERT build readings, each either fixed in the run, carried by a held row, or a baseline the record lists. The one remaining ARMED row is held with its owner."
 }
]
```
