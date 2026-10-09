# ETFS_RIVALS -- surprise channel, investigations (dell1's append file)

dell1's own append file for this project's channel. ETFS_RIVALS moved to dell1 on Andrew-direct ~01:5xZ 2026-10-09
(@a0db38c8ae). The site-Z rows before that move are in `INVESTIGATION_v1.Z.md`, which only site Z writes. Rows minted here carry
dell1's coordinate `D1-` (org/devices/DEVICES.json), so they cannot collide with that file's `Z-` rows.

```json
[
  {
    "id": "ETFS_RIVALS-D1-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~RV1",
    "surfaced_at": "2026-10-09T03:12:59Z",
    "one_line": "DISARM of ETFS_RIVALS-Z-S79 and ETFS_RIVALS-Z-S80 on their disarm owner's act (2.0.0_SA_COO~V1, commit c07077f4e1, word msg 1474): RIV-tw-1 J1 AMENDMENT 1 reads J1 only on the first scheduled run that REACHED the enrichment leg, so the 2026-10-08 run (exit 97, no session) reads UNVERIFIABLE, never PASS. The act is the one sentence S79's notes name as its disarm. J1 itself stays owed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "commit c07077f4e1 (2.0.0_SA_COO~V1), an ancestor of HEAD bc1ce7b850 (merge-base read by this seat 03:12Z): J1 at TO-RIV-tw-1 now carries 'AMENDMENT 1 ... J1 is read on the FIRST scheduled vehicle run that REACHED the enrichment leg -- its log carries the RIVALFUNDS ENRICHMENT STEP line, an enrichment exit code other than 97, and no vendor-session-failure line ... A run that did not reach the leg reads UNVERIFIABLE for J1, never PASS; the 2026-10-08 11:00Z run is such a run.' (printed from git show HEAD:<order>, one match)",
        "the same commit amends TO-RELAY-tw1-vehicle-log-20261009: the transcriber adds the verdict line '-- DID THIS FIRE REACH THE ENRICHMENT LEG? --' and the whole log is committed beside it as VEHICLE_LOG_20261009_1100Z.full.log",
        "S79 notes (@c086fcc096): 'the disarm is one sentence from the issuer -- that J1 is read on the first fire that REACHED the enrichment leg, not on the earliest date in the range'",
        "S80 (@eaf6d69c9a): disarm_owner moved to 2.0.0_SA_COO~V1 per 0.0.0_AB_MSTR~Z msg 32284"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "ETFS_RIVALS-Z-S79",
      "ETFS_RIVALS-Z-S80"
    ],
    "spec_asserts": "S79/S80: ARMED until the issuer states that J1 is read on the first fire that reached the enrichment leg; the CVO writes the disarm clock (surprise-row-gate R-15).",
    "world_is": "The issuer's statement is in the order at HEAD, and its predicate is sharper than the row asked for: it names the three conditions (STEP line, exit not 97, no session-failure line) and the four session-failure strings. The hazard S79 named (a non-reaching run consumed as a PASS) can no longer arise from J1's wording. What survives the disarm: (1) J1 is still owed, and the 2026-10-09 11:00Z fire reaches the leg only if the Terminal is signed in at 07:00 local; (2) a remediation row with the disarm clock is written at the round-28 slug, because a new remediation row is refused while task orders are open (2 pending at HEAD).",
    "notes": "Written as an investigation row because the surprise-row gate refuses a new remediation row mid-round (LD-0521); a REMEDIATION_v22 with this clock was refused at commit (2 of 128 orders not terminal) and withdrawn uncommitted. The remediation rows for S79 and S80, with disarm DISARMED at this row's surfaced_at, are owed at the next slug."
  },
  {
    "id": "ETFS_RIVALS-D1-S2",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~V1",
    "surfaced_at": "2026-10-09T04:02Z",
    "one_line": "The ruling that puts act 3's standing Bloomberg draw on MDPF_DEMQUE's books says the vehicle reads the queue's pause/stop state before each draw, but no such state exists to read and the history-owed step (tw-1 + tc-1) reads none: switching RIVALFUNDS_HISTORY_OWED to ask on the code as built would draw past a queue pause",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~V1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Ruling XA-20261009T033809Z-8c1a (1.0.0_SA_CTO on laptop, 2026-10-09T03:42:38Z, read with `xadj.py show`), condition 1: '2.0.0_SA_COO~Q1 enters the standing request before the first run. The queue may pause or stop it at its reserve, or when a higher tier needs the budget; the vehicle reads that state before each draw.'",
        "data/etfs/scripts/rivalfunds/enrichment_bloomberg.py `_history_owed` on branch wk-ETFS_RIVALS-22 @b0b65368fb (read in full at the simulated merge onto origin/box/sitez 37aefc2855): the only gate before a request is `bbg_budget.check_points`; no queue or request-state read.",
        "org/missions/D8/MDPF/MDPF_DEMQUE/prd/MDPF_DEMQUE_PRD.md: one Grep for standing / pause / stop / reserve near state / status / read returns 2 lines (:149 the backfill allowance arithmetic, :174 a corporate-actions sentence); no readable per-request state is specified. The ruling's condition 3 names a standing request as a new request shape for C-QUOTE at Q1's next round."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "XA-...-8c1a condition 1: before each history-owed draw the vehicle reads the standing request's queue state and draws nothing when it is paused or stopped.",
    "world_is": "No queue state for a standing request exists to read (MDPF_DEMQUE PRD), and the vehicle's history-owed step reads none. Acts 1 (aw-1 deploy) and 2 (tc-1 merge) draw nothing and are unaffected; act 3 (the switch-on) cannot meet condition 1 until (i) Q1 names where the state lives and (ii) a rivalfunds cell reads it.",
    "notes": "Disarm (this seat, now): act 3's order is not cut and RIVALFUNDS_HISTORY_OWED is not set to ask until both (i) and (ii) exist; the switch stays unset. The cell for (ii) is new work outside the frozen round-28 decomposition, so it is the CTO's to place (round 29 or an addendum); (i) is Q1's interface. Owner of the remedy: 1.0.0_SA_CTO~DELL1 places it; 2.0.0_SA_COO~Q1 names the state."
  },
  {
    "id": "ETFS_RIVALS-D1-S3",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~V1",
    "surfaced_at": "2026-10-09T04:26Z",
    "one_line": "`.tools/crossbox-call.py open` writes an ORDER's file under org/devices/crossbox/ and says to commit it, but org/devices/** is lane NFRA_CTLPLN_FAST_C and a COO issuer is not a permitted agent, so a COO cannot commit the ORDER site Z asked it to open; only a CTO has committed crossbox files so far",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "crossbox-call.py open, 2026-10-09T04:24:21Z: OPENED XB-20261009T042421Z-e448 and XB-20261009T042421Z-897f, each printing 'NEXT: commit org/devices/crossbox/<id>.json'",
        "safe-commit 04:24:51Z and 04:25:15Z: 'VIOLATION: org/devices/crossbox/XB-20261009T042421Z-897f.json -- lane=NFRA_CTLPLN_FAST_C ... agent=2.0.0_SA_COO~V1 not in permitted_agents' (org/git-author-override-audit.log, 2 BLOCK lines)",
        "git log -8 -- org/devices/crossbox/: 4 commits, all by 1.0.0_SA_CTO~DELL2",
        "site Z REC (0.0.0_AB_MSTR~DELL1 msg 1681) asked this COO to open the ORDER itself"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "An issuer opens a crossbox ORDER and commits it so the other box pulls it (crossbox-call.py NEXT line).",
    "world_is": "The lane on org/devices/** refuses a COO's commit of the ORDER file; the file sits uncommitted until a permitted seat commits it.",
    "notes": "Worked around by asking 1.0.0_SA_CTO~DELL1 to commit the two files; the order files themselves (e9fe72e427, e3b33d03c4) are committed. Remedy owner: the NFRA_CTLPLN lane's grantor (a lane-ANY carve-out for org/devices/crossbox/), not this seat."
  },
  {
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~25",
    "surfaced_at": "2026-10-09T06:10Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "ETFS_RIVALS-D1-W25-S1",
    "one_line": "RIV-wc-1 cannot keep two script-size caps green: test_r24cu1_chart_frame_ticks_tip.py::test_script_shape (<= 7369+3000 = 10369 bytes) and test_r25mr1_marker_readout.py::test_script_growth_bound (<= 9348+600 = 9948 bytes) cap CHART_SCRIPT, which is 9502 bytes at the base and 10595 with the cell; neither test is in the order's <paths>",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "The order says 'every other test stays green' and its <paths> name only test_r21pl1 and test_r18tl1 as tests to update.",
    "world_is": "The cell (tradehead, a windowed tradelines, putTrades with the empty-window sentence, adjwords and the dialog line) adds 1093 bytes to the one script. r25mr1's cap (9948) leaves 446 bytes of growth and r24cu1's (10369) leaves 867; the 9502-byte base was already above r24cu1's pre-r25 figure of growth. AC1 passes; the rivalfunds suite ends at 3 failed, 918 passed, 6 skipped, and these two are 2 of the 3.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "pytest -q rivalfunds/tests from data/etfs/scripts at branch wk-ETFS_RIVALS-25: 'assert 10595 <= (7369 + 3000)' and 'assert 10595 <= (9348 + 600)'",
        "len(CHART_SCRIPT.encode()) at box/dell1 base render.py = 9502"
      ]
    },
    "notes": "Not edited: the two tests are outside <paths>. Remedy for the issuer: widen both caps to the new figure (a one-number edit each) in a later order or at the merge, or rule that the cell must shrink. Owner: 2.0.0_SA_COO~V1."
  },
  {
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~25",
    "surfaced_at": "2026-10-09T06:10Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "ETFS_RIVALS-D1-W25-S2",
    "one_line": "test_r15md1_chart_frame_and_script.py:63 pins the static placeholder \"The fund's trades over the last 365 days load with the chart.\", which the order's own interface item 1 ('No static text names 365 days') and AC1 arm (a) forbid; the test is not in <paths>",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "Item 5 lists test_r21pl1 and test_r18tl1 as the only tests that pin the old heading, and says every other test stays green.",
    "world_is": "AC1 arm (a) fails if '365 days' appears anywhere in _trade_list([]), so the placeholder had to become \"The fund's trades load with the chart.\"; test_r15md1::test_the_trades_are_in_the_frame_in_words_and_a_fund_without_one_says_so asserts the old sentence and now fails (third of the 3 suite failures).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "render.py HEADP / _trade_list at this branch; test_r15md1_chart_frame_and_script.py:63"
      ]
    },
    "notes": "Not edited (outside <paths>). The one-line fix is to replace the old sentence with the new one in that assertion. Owner: 2.0.0_SA_COO~V1."
  },
  {
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~25",
    "surfaced_at": "2026-10-09T06:10Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "ETFS_RIVALS-D1-W25-S3",
    "one_line": "Interface item 2 says tradelines returns the lines 'oldest first ... worded as today's tradelines', but today's tradelines is newest first with a trailing 'and n earlier trades' line capped at 20; the two cannot both hold",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "tradelines(markers, from) -> trade lines oldest first, worded as today's.",
    "world_is": "Chosen: the window's markers are capped at the 20 most recent, shown oldest first, and the 'and n earlier trade(s) in the last <window>.' line LEADS (the omitted trades are earlier than the listed ones); an empty window returns [] and putTrades writes 'No trades in the last <n> days.'. test_r18tl1 was re-pinned to this shape. AC1 does not grade the order.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "render.py CHART_SCRIPT tradelines; tests/test_r18tl1_trade_list_from_markers.py; tests/test_ws2_wc1_trade_list_scope.py"
      ]
    },
    "notes": "J1 (CVO) sees the shipped order. If newest-first was meant, a one-line change to the sort."
  }
]
```
