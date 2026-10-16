# NFRA_CTLPLN: CVO L8/L9 at the round-27 close -- FWD-18, FWD-19, FWD-11 graded (2026-10-16)

<sweep_watermark>2026-10-16T10:05Z</sweep_watermark>

L8/L9 by `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~C` msg 109658 (packet `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND27.md`
@7f8eee22dc). Six tree orders, all complete; no judgment criterion on the orders; the grades owed are the round-26 analysis's
section 3 items 1-3.

**Result:**
- **FWD-18 REALIZED** (C-S88) and **FWD-19 REALIZED** (C-S89).
- **FWD-11 stays ADVANCED** (C-S90). The round-26 analysis left the reading to the grader: "A whole-box reboot is not required
  unless the PRD's text demands it." The text does demand it: DONE WHEN reads "one box restarted mid-round", and ACCEPT reads
  "after any one box restarts". The drill restarted one seat's process (`2.0.0_SA_COO~C1`) and shows the round carried and
  finished. That is the session half of a box restart, not the whole. **Decision for 1.0.0_SA_CTO, one of two:** (a) the
  missing act, a whole reboot of one box with a round in flight and no worker in flight, done by that box's MSTR on its CTO's
  word (your ruling's own route), after which the round is shown to finish; or (b) a PRD addendum that narrows FWD-11's
  ENDPOINT to "the process carrying a round restarts", which re-opens the ratified-text half for this seat's re-sign. Under
  (a), dell1's CTO reads Andrew's 2026-10-14 hold on a whole-box reboot as spent; no seat has adjudicated that, and it is
  Andrew's word, so it is yours to confirm before (a) runs.
- Tally: 10 REALIZED (1, 3, 5, 15, 16, 17, 18, 19, 24, 28), 14 ADVANCED, 0 GATED, 1 PARKED (9), 3 MOVED (13, 20, 26);
  denominator 28 (C-S92).
- 8 round rows dismissed with reason (C-S91); W130-S2 closes on its done-when, re-read here.

All 18 criteria of the six orders were re-run here in the main tree and pass (`JOURNEY-TAILDROP-SITEZ files_sent=4 failed=0
target=sitez ok=True`; `JOURNEY-PACK ... ok=True`; `LINUX-CLOSURE arms=7/7`; `INTAKE-CLOSURE-TEST cases=10/10`;
`INTAKE-CLOSURE ... closure=24 ... host_satisfied=7 host_conflicts=0 to_fetch=17 ok=True`; `RESOLVE arms=9/9`;
`INTAKE-FETCH-TEST cases=21/21`; `WAIVER arms=20/20`; `INTAKE-CHECK-TEST cases=60/60`; `INTAKE-RECEIVE-TEST cases=36/36`;
`BATCH-FETCH wheels=17 ... ok=True`; `BATCH-CHECK ... failed_total=4 ... check8=SIGNED released=True ok=True`;
`BATCH-REQUIRES ... new_deps=0 ... ok=True`; `BATCH-RELEASE released=17 ... ok=True`; `BATCH-PACK files=52 ... verified=17
... ok=True`; `BATCH-TAILDROP files_sent=52 failed=0 target=dell2 ok=True`).

The organic FWD-15/16 arm (section 3 of the packet; no re-grade owed, both REALIZED): dell2's collector record `40b21e0a58`
is on `origin/CLOUD` (52 of 52 files equal to the manifest). This seat did not re-read its contents.

```json
[
 {
  "id": "NFRA_CTLPLN-C-S88",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T10:05Z",
  "one_line": "FWD-18 graded REALIZED: the delivered tabulate file is now installed on site Z as it was on dell1, from the file alone with --no-index, and read from the scratch install; with C-S80's two stopped downloads (dell1, site Z), the DONE WHEN is met on both box kinds.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 FWD-18 DONE WHEN: a download tried on purpose and stopped on a Dell and on site Z, and the delivered file then installed on each. C-S80 left one act: the install on site Z.",
  "world_is": "origin/box/sitez carries 7d969d9aa6 (author 1.0.0_SA_CTO~Z), folder deliverables/1.0.0_SA_CTO~Z/xb_r27_sitez_scratch_receive/ (12 files). This seat hashed both committed pip logs: install 657 bytes 9b39364f...2bd84, prove 676 bytes 168853da...6016b, each equal to its receipt's pip_log. Both receipts' received_sha256 begin 024ca478df22, the laptop wheel. The install command is pip install --no-index --no-deps --target SCRATCH_TARGET_Z <the delivered wheel>, pins PIP_NO_INDEX=1 PIP_CONFIG_FILE=nul. output/4_read_from_scratch.txt prints PYTHONPATH = SCRATCH_TARGET_Z, sys.path[1] = SCRATCH_TARGET_Z, tabulate.__file__ under it, version 0.9.0, a 2-row table, rc=0. The departure is stated in the packet: the four files were auto-saved to Downloads and copied into PACK3; the hashes tie them to the laptop's send record. Dell half: C-S80, C-S81, C-S86.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git show 7d969d9aa6:org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/1.0.0_SA_CTO~Z/xb_r27_sitez_scratch_receive/ (pip logs re-hashed 2026-10-16T10:0xZ)",
    "git merge-base --is-ancestor 7d969d9aa6 origin/box/sitez -> true (fetched 10:0xZ)",
    "python .tools/tests/test_round25_journey_record.py --taildrop-sitez -> files_sent=4 failed=0 target=sitez ok=True",
    "adjudications/ADJUDICATION_v28.md C-S80 (the stopped downloads on dell1 and site Z)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard."
 },
 {
  "id": "NFRA_CTLPLN-C-S89",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T10:05Z",
  "one_line": "FWD-19 graded REALIZED: a lane waiting on toml==0.10.2 showed its wait in the one decision list (local and cloud) and in its broker summary, kept working elsewhere, and dropped its one piece of work when the request was refused; the reads were committed before the decision.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 FWD-19 ACCEPT: a lane that needs a package not yet delivered loses that one piece of work, keeps going elsewhere, and its wait shows in the same place he sees every box's open decisions; nothing watches or sends him anything on its own. The DONE WHEN (a day's downloads answered from a record) was exercised by this seat in C-S80; this clause was the open one.",
  "world_is": "The reads file FWD19_LANE_WAIT_READS_20261016.md was committed at 3f367473c0 (05:04:17Z), before the CTO's decision record 11905fe03d (05:07:26Z), so the waiting state was written at the time, not reconstructed. It shows status REQUESTED, call laptop-20261016T045125Z-66e3 OPEN in open-calls.py list and list --cloud, and the lane's broker summary 'WAITING (FWD-19): toml REQ REQUESTED, call 66e3 OPEN'; three lane commits during the wait touch other work. Re-read here at 10:0xZ: status -> REFUSED by=1.0.0_SA_CTO at=2026-10-16T05:05:35Z with its reason; open-calls.py list --all -> 66e3 [CLOSED]; requirements.txt 98 lines, 0 toml lines. Every read was a command someone ran; nothing pushed anything. Not shown: that Andrew himself read the list (FWD-12's arm), and a lane on another box (one laptop lane only).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/FWD19_LANE_WAIT_READS_20261016.md @3f367473c0",
    "python org/devices/intake/intake_request.py status --name toml --version 0.10.2, 2026-10-16T10:0xZ",
    "python .tools/open-calls.py list --all (66e3 CLOSED), 2026-10-16T10:0xZ"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard."
 },
 {
  "id": "NFRA_CTLPLN-C-S90",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T10:05Z",
  "one_line": "FWD-11 graded ADVANCED, not REALIZED: dell1's drill restarted one seat's process mid-round (round 95 drained but not closed, row W185-S1 BLOCKING) and the round then finished with nothing redone or lost, but the PRD names a BOX restart, and the round-26 analysis made a whole-box reboot required where the text demands it. It does.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 FWD-11 DONE WHEN: one box restarted mid-round, and the round finished. ACCEPT: after any one box restarts, the next person to look can say which round was where, and the round finishes without work being redone or lost. Round-26 analysis section 3 item 3: 'A whole-box reboot is not required unless the PRD's text demands it.'",
  "world_is": "On origin/box/dell1 (fetched 10:0xZ): 24b1e9d488 (the plan), d0591b6961 (the lane's handoff, 04:59:26Z), 923f06e998 (the first commit after, 05:24:40Z: 'round 95 drained @c2f2aff341 ... Nothing was redone or lost'), 26f2781a61 (round 96 drained 05:46:28Z), 251b7a4d10 (W185-S1 dispositioned), be7670e81f (dell1's result note); each an ancestor of origin/box/dell1. Mid-round holds: round 95 had drained but its BLOCKING row was open, so its L10 had not run. The round finished. What restarted was the Claude session of one lane; the box, its broker, its scheduled tasks and its other seats ran on. The kill and respawn times rest on MSTR~DELL1's msg 6514, which no laptop seat read. No worker was in flight at the kill, by design; a worker lives in its COO's session.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/FWD11_DRILL_READS_20261016.md",
    "git merge-base --is-ancestor <each of the six commits> origin/box/dell1 -> true",
    "org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round26.md section 3 item 3",
    "org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md FWD-11 (lines 122-126)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard; the two ways to REALIZED are the CTO's decision, stated in this record's header."
 },
 {
  "id": "NFRA_CTLPLN-C-S91",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T10:05Z",
  "one_line": "Round-27 rows: W129-S1, W130-S1, W130-S2, W132-S1, W133-S1, W133-S2, W134-S1 and W134-S2 dismissed with reason; W130-S2 (ARMED) closes on its done-when, re-read here.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-W129-S1",
   "NFRA_CTLPLN-W130-S1",
   "NFRA_CTLPLN-W130-S2",
   "NFRA_CTLPLN-W132-S1",
   "NFRA_CTLPLN-W133-S1",
   "NFRA_CTLPLN-W133-S2",
   "NFRA_CTLPLN-W134-S1",
   "NFRA_CTLPLN-W134-S2"
  ],
  "spec_asserts": "Every row a round mints is dispositioned before its L10; an ARMED row disarms on a verified done-when.",
  "world_is": "W129-S1: the two mutants live on --taildrop-sitez and read held=True there (re-run here). W130-S1: the hand-written manylinux list is checked by LINUX-CLOSURE arm 2 (7/7 here). W130-S2 (ARMED): intake_closure.py fetchlist --from-file closure_cp312_linux_x86_64_yfinance.json now prints 'this closure targets cp312-linux_x86_64; use intake_fetch.py resolve' and exits 2 (re-run here, rc=2). W132-S1, W133-S1, W133-S2 (BLOCKING, INERT): each cleared by the act the packet names (the exact approval line, the per-wheel signed names, the signed waiver of CT-av-1), and BATCH-RELEASE released=17 reads here. W134-S1: test_intake_check.py was red at the base; 60/60 here. W134-S2: intake_receive.py trusts a record's 'checked' verdict without re-reading checks 1-7; the sender's verdict rule is the authority and is tested (WAIVER 20/20, INTAKE-CHECK-TEST 60/60), so the gap is defense in depth only. Named for the CTO's round-28 enrichment list, not graduated.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "the 18 criterion re-runs in this record's header, 2026-10-16T10:0xZ",
    "python org/devices/intake/intake_closure.py fetchlist --from-file org/devices/intake/closure_cp312_linux_x86_64_yfinance.json -> rc=2",
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND27.md sections 3 and 5"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Each row is resolved in the round or is an accepted, tested state; W134-S2 is an enrichment candidate, not a hazard on today's route."
 },
 {
  "id": "NFRA_CTLPLN-C-S92",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T10:05Z",
  "one_line": "FWD delta after round 27: 8 -> 10 REALIZED (FWD-18, FWD-19), 16 -> 14 ADVANCED, 0 GATED, 1 PARKED, 3 MOVED; denominator 28. FWD-11 waits on the CTO's choice in C-S90.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 DONE WHEN and ACCEPT per outcome.",
  "world_is": "C-S88, C-S89, C-S90. FWD-14: Andrew scratched the MacBook remote-desktop arm (c9a4 closed); b87f stays; no grade change. The 12 other ADVANCED outcomes listed in ROUND27_ADVANCED_FWD_SHORT_ACTS.md were not re-graded this round.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this record's C-S88 to C-S90",
    "adjudications/ADJUDICATION_v30.md C-S87 (the table entering the round)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade delta, not a hazard."
 }
]
```
