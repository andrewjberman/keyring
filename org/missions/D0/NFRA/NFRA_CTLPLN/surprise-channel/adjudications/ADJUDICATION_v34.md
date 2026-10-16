# NFRA_CTLPLN: CVO reads on the round-29 analysis -- FWD-11, FWD-4, FWD-12, FWD-22 graded (2026-10-16)

<sweep_watermark>2026-10-16T16:30Z</sweep_watermark>

L9 by `3.0.0_SA_CVO~L` (laptop), on `1.0.0_SA_CTO` msg 109722 (`ledger/ROUND_ANALYSIS.round29.md` @ae11f384bd, ruling 6 and
enrichment item 5). These are reads of evidence that already exists; no seat act was owed before them.

**Result: FWD-11, FWD-4, FWD-12 and FWD-22 REALIZED (C-S106 to C-S109). Tally: 17 REALIZED (1, 3, 4, 5, 8, 11, 12, 15, 16,
17, 18, 19, 22, 23, 24, 25, 28), 7 ADVANCED, 0 GATED, 1 PARKED (9), 3 MOVED (13, 20, 26); denominator 28 (C-S110).** No
deliberate reboot is owed: C-S90's two routes are superseded by ruling 6 and the read below.

```json
[
 {
  "id": "NFRA_CTLPLN-C-S106",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T16:30Z",
  "one_line": "FWD-11 graded REALIZED on the laptop's own reboot: Windows shut down and restarted twice between 00:54:11Z and 00:58:32Z on 2026-10-16 with NFRA_CTLPLN round 24 in flight (issued 00:16:39Z, its worker's code and tests committed 00:27-00:36Z), and the round then finished (proof 02:36Z, merge 02:38Z, flip 02:40Z, packet 02:44Z) with nothing redone or lost.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 FWD-11 DONE WHEN: one box restarted mid-round, and the round finished. ACCEPT: the next person to look can say which round was where, and the round finishes without work being redone or lost. Round-29 analysis ruling 6: grade it on this reboot.",
  "world_is": "Windows System log read at 16:2xZ: event 1074 at 00:54:11Z (a restart started from the Start menu), 6006/13 at 00:56:30-38Z, 12 at 00:56:40Z (started), 1074 at 00:58:03Z (TrustedInstaller restart), 13 at 00:58:24Z, 12 at 00:58:32Z; Win32_OperatingSystem.LastBootUpTime 2026-10-16T00:58:32Z. Round 24 in UTC: issue 67d0509936 00:16:39Z; worker ~126 commits 7a5d1e28f3 (intake_receive.py), ed6212adcb (test_round24_pip_log.py), 5f3bcfe8a2 (test_intake_receive.py) at 00:27-00:36Z; the COO's session-close log 592119ef2d at 00:51:15Z names 'round 24 issued (worker ~126 stopped, tree left for the next COO)'; after the boot, 37de3417f1 (the W126-S1 row) and 74aeadbbab (the proof instance) on the same branch, merge 79ee07a0b7 02:38:12Z, flip 2a7e490280 02:40:21Z, packet 52567a1a41 02:44:17Z, whose header says the slot was re-seated on the same branch. The two after-boot commits touch only the channel file and the proof file: none re-writes the code or tests, so nothing was redone; nothing the worker committed was lost. Limits, stated: the restart was Andrew's own, not a drill (ruling 6 grades on it); the worker had stopped with the COO's session 3 minutes before the shutdown, so the reboot interrupted a round, not a running worker.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "Get-WinEvent System log ids 1074/6005/6006/12/13 since 2026-10-15T18:00 and Win32_OperatingSystem.LastBootUpTime, laptop, 2026-10-16T16:2xZ",
    "git log (UTC) of the round-24 commits 67d0509936 .. 52567a1a41, and git show --stat of the five worker commits",
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND24.md @52567a1a41 header paragraph"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard."
 },
 {
  "id": "NFRA_CTLPLN-C-S107",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T16:30Z",
  "one_line": "FWD-4 graded REALIZED: two boxes' finished rounds reached CLOUD only through the integrator: the laptop's NFRA_CTLPLN round 28 packet (cf7b334a00) by integrate dd491231c5 (11:50Z, box/laptop @1493028f0b) and dell2's IRPT_DASHBD round 132 slug (8d1e88436a) by integrate 3cddcafee2 (15:10Z, box/dell2 @653504bd5b); every first-parent commit on CLOUD since 2026-10-15 is 0.0.0_AB_MSTR's.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 FWD-4 DONE WHEN: two boxes' rounds pushed to their own branches and merged by the integrator. ACCEPT: no box writes the shared trunk itself; no box holds more than one unpushed round per lane.",
  "world_is": "git log origin/CLOUD --first-parent --since=2026-10-15: 798 commits, all authored 0.0.0_AB_MSTR. For each round, the first integrate commit on CLOUD whose carried box tip contains the round's close commit (git merge-base --is-ancestor), read at 16:2xZ after a fetch: laptop cf7b334a00 -> dd491231c5; dell2 8d1e88436a (on origin/box/dell2, author 3.0.0_SA_CVO~IRPT) -> 3cddcafee2. Not read: the ACCEPT clause 'no box holds more than one unpushed round per lane'.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git log origin/CLOUD --first-parent --since=2026-10-15T00:00:00Z --format=%an | sort | uniq -c -> 798 0.0.0_AB_MSTR",
    "the pairing loop over integrate(0.0.0_AB_MSTR): box/<box> @<tip> subjects with git merge-base --is-ancestor, 2026-10-16T16:2xZ"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard."
 },
 {
  "id": "NFRA_CTLPLN-C-S108",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T16:30Z",
  "one_line": "FWD-12 graded REALIZED: dell2's call dell2-20261008T194221Z-2cf8 (one S3 delete, an act needing a human's yes) reached the laptop, Andrew answered it at the laptop ('Yes do it'), and the answer reached dell2, which closed its side: crossbox XB-20261008T203134Z-a3f0 reads CLOSED-BOTH.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 FWD-12 DONE WHEN: a decision raised on another box answered by Andrew from the laptop. ACCEPT: it appears in one list on the laptop, and his answer there reaches the box that asked.",
  "world_is": "org/devices/crossbox/XB-20261008T203134Z-a3f0.json: from dell2 (1.0.0_SA_CTO~DELL2) to laptop (1.0.0_SA_CTO), opened 20:31:34Z, acked 20:54:36Z by 1.0.0_SA_CTO, closed from-side 20:58:34Z by 1.0.0_SA_CTO~DELL2 and to-side 21:00:14Z; crossbox-call.py status reads CLOSED-BOTH. Its body CROSSBOX_BODY_E6_S3_DELETE_APPROVED_20261008.md records 'Andrew, ~19:3xZ at the laptop, VERBATIM \"Yes do it\"', recorded in amendment 39ab7ddd70 (2.0.0_SA_COO~C, citing CTO msg 107163). The one list today: open-calls.py list --cloud unions every box's calls (FWD19 read, C-S89).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "python .tools/crossbox-call.py status --id XB-20261008T203134Z-a3f0 -> CLOSED-BOTH, 2026-10-16T16:2xZ",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/CROSSBOX_BODY_E6_S3_DELETE_APPROVED_20261008.md",
    "git log -1 39ab7ddd70"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard."
 },
 {
  "id": "NFRA_CTLPLN-C-S109",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T16:30Z",
  "one_line": "FWD-22 graded REALIZED: a decision touching one box (the toml request, call 66e3) was settled by the laptop's lead in XA-20261016T050614Z-0021 with no Andrew touch, and a decision touching two boxes (NFRA_TRNSPT FWD-5 reader holders) was ruled by the laptop's lead, adopted and signed against by dell2's lead, and reads the same from both boxes.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 FWD-22 DONE WHEN: one decision that touched one box settled there and never shown to Andrew, and one that touched two boxes read afterwards from both sides.",
  "world_is": "One box: org/critical_paths/cross_adjudication/20261016T0506Z_XA-20261016T050614Z-0021.md, RULED by 1.0.0_SA_CTO at 05:06:18Z on call laptop-20261016T045125Z-66e3 (the call's CROSS-BOX scope comes from the project's shared paths, as the record says; the decision touched only the laptop lane); the record names no question to Andrew. Two boxes: XB-20261009T125323Z-c442 (dell2 call dell2-20261009T114756Z-886a), CLOSED-BOTH; its body says the ruling was made on the laptop (CTO_RULING_NFRA_TRNSPT_FWD5_WIPED_SILVER_READER_HOLDERS_20261009.md @374553467d) and dell2 adopted it, its CTO half @91e314b74e signed against it. 374553467d is an ancestor of origin/box/dell2, origin/box/laptop and origin/CLOUD, and the body file is present on origin/box/dell2, so someone on either box reads what was agreed and by whom. 'Never shown to Andrew' is read as the absence of any Andrew line in the record, not as a sweep of his inbox.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/critical_paths/cross_adjudication/20261016T0506Z_XA-20261016T050614Z-0021.md",
    "org/devices/crossbox/XB-20261009T125323Z-c442.json and its body org/tier1_exec/1.0.0_SA_CTO/deliverables/CROSSBOX_CALL_886a_NFRA_TRNSPT_FWD5_HOLDERS_CLOSE_BOTH_20261009.md",
    "git merge-base --is-ancestor 374553467d origin/box/dell2, origin/box/laptop, origin/CLOUD -> true"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard."
 },
 {
  "id": "NFRA_CTLPLN-C-S110",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T16:30Z",
  "one_line": "FWD delta on the round-29 analysis reads: 13 -> 17 REALIZED (FWD-4, FWD-11, FWD-12, FWD-22), 11 -> 7 ADVANCED, 0 GATED, 1 PARKED, 3 MOVED; denominator 28. ADVANCED now: FWD-2, 6, 7, 10, 14, 21, 27.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 DONE WHEN and ACCEPT per outcome.",
  "world_is": "C-S106 to C-S109. Of the 7 ADVANCED: FWD-7 waits on source-map stage 2 (round 30 item 1; C-S102 ARMED); FWD-10 and FWD-21(a) are held for a later round; FWD-2, 6, 14 and 27 need Andrew's acts.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this record's C-S106 to C-S109",
    "adjudications/ADJUDICATION_v33.md C-S105 (the table entering these reads)",
    "ledger/ROUND_ANALYSIS.round29.md section 3"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade delta, not a hazard."
 }
]
```
