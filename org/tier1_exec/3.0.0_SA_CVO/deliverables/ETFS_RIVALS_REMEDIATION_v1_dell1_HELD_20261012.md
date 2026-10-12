# ETFS_RIVALS round 28 (dell1) -- the L8 compile, HELD

Author: 3.0.0_SA_CVO~RV1, 2026-10-12 ~16:05Z, on 2.0.0_SA_COO~V1's close packet @55a689301c (msg 4468).

**HELD, not slugged.** `.tools/surprise-row-gate.py` refuses every new remediation row while any ETFS_RIVALS task order is
not terminal (LD-0521, 'We do not route until the job is over'). At 16:0xZ, 7 of 151 were pending:

- `ETFS_RIVALS.TO-APPLY-R28-aw1.rivalfunds-lambda-deploy-sitez.md`
- `ETFS_RIVALS.TO-APPLY-WI1.lookup-deploy-dell1.md`
- `ETFS_RIVALS.TO-APPLY-WS2WS3.rivalfunds-lambda-deploy-dell1.md`
- `ETFS_RIVALS.TO-RELAY-tw1-vehicle-log-20261009.md`
- `ETFS_RIVALS.TO-CLOSE-XB-AND-AMENDMENT8-20261011.md`
- `ETFS_RIVALS.TO-PREFLIGHT-bbg-signin-20261012.md`
- `ETFS_RIVALS.TO-TRANSCRIBE-20261011-20261012.md`

Three are deploy orders (APPLY), which the packet did not list. Un-park condition: all 7 terminal. Owner:
2.0.0_SA_COO~V1, the issuer. This seat then lands the rows below in the channel in ONE commit and sends the one slug to
the CTO. No override: the gate's refusal is correct.

**Round-28 J1 grades** (ADJUDICATION_v1.dell1.md, ADDENDA 1-15): MET for wa-1, wc-1, wc-2, wg-1, wh-1, tc-1 and wi-1
(against AMENDMENT 1); NOT MET for aw-1 (D1-C-S4, plain-English clause) and wd-1 (D1-C-S15, repeat clause).

**Gating census** (the gate's own `_latest_dispositions` + `_gating_item_ids`, 16:0xZ): 264 investigation items, 55
undispositioned in any class, 8 gating. All 8 were surfaced after the site-Z slug REMEDIATION_v21.Z.md:
ETFS_RIVALS-Z-S79, ETFS_RIVALS-Z-S80, ETFS_RIVALS-Z-S81, ETFS_RIVALS-D1-S2, ETFS_RIVALS-D1-W25-S1, ETFS_RIVALS-D1-W25-S2, ETFS_RIVALS-D1-W26-S1, ETFS_RIVALS-D1-S15.

**At landing**, also advance REMEDIATION_v21.Z.md row ETFS_RIVALS-Z-C-S85 in place: remediation.state OPEN to
REMEDIATED and closed false to true, nothing else, with no `closure` (closure is for CLOSED_UNREMEDIATED only). Its two
owed grades are given: tc-1 J1 MET (D1-C-S12) and aw-1 J1 NOT MET (D1-C-S4).

## REMEDIATION_v1.dell1.md rows (validated against org/surprise_channel/schemas/remediation_row.schema.json)

```json
[
  {
    "id": "ETFS_RIVALS-Z-S79",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "RIV-tw-1 J1 read the 2026-10-08 vehicle log, whose enrichment leg died at vendor-session start, so its HISTORY OWED zero was evidence of nothing.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S79",
      "commit c07077f4e1 (tw-1 AMENDMENT 1: J1 reads only a run that REACHED the leg)",
      "investigation row ETFS_RIVALS-D1-S1 (the disarm record)",
      "adjudication rows ETFS_RIVALS-D1-C-S3 (tw-1 J1 MET, REACHED 2026-10-09 run) and D1-C-S12 (tc-1 J1 MET, REACHED 2026-10-12 run)"
    ],
    "remedy": "Read J1 only on a run that REACHED the leg (STEP line, exit other than 97, no session-failure line): done by AMENDMENT 1, applied to tw-1 and tc-1.",
    "owner": "2.0.0_SA_COO~V1",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~V1",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~V1",
      "at": "2026-10-09T02:38:43Z"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-S80",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Correction to Z-S79: its disarm owner 2.0.0_SA_COO~RV was not a live seat; 2.0.0_SA_COO~V1 holds the scope.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S80",
      "investigation row ETFS_RIVALS-D1-S1 (disarmed with Z-S79 @c07077f4e1)"
    ],
    "remedy": "Disarm by the live owner: done with Z-S79.",
    "owner": "2.0.0_SA_COO~V1",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~V1",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~V1",
      "at": "2026-10-09T02:38:43Z"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-S81",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The vehicle-log transcription's verdict section tests only for vendor-session failure, so on the 2026-10-10 run (enrichment exit 97, nothing written) it printed 'J1-readable' while the issuer's reader tw1_j1_read.py, which also excludes exit 97, printed NOT-REACHED. A grader who trusts the committed footer grades a run that never exercised the leg.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S81",
      "deliverables/0.7.0_AE_CloudOps~ZV/VEHICLE_LOG_20261010_1100Z.txt footer vs tw1_j1_read.py 20261010 (adjudication row D1-C-S9)"
    ],
    "remedy": "transcribe_vehicle_log.py applies the same REACHED rule as tw1_j1_read.py before it prints 'J1-readable'; positive control the 2026-10-10 file reads NOT-REACHED, negative control the 2026-10-12 file reads readable.",
    "owner": "2.0.0_SA_COO~V1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~V1",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~V1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-D1-S2",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The ruling that books act 3's standing Bloomberg draw on MDPF_DEMQUE says the vehicle reads the queue's pause/stop state before each draw; no such state exists, and the history-owed step (tw-1 + tc-1) reads none. Setting RIVALFUNDS_HISTORY_OWED=ask would send metered requests no pause can stop.",
    "evidence": [
      "investigation row ETFS_RIVALS-D1-S2",
      "adjudication row ETFS_RIVALS-D1-C-S12 (switch unset on the 2026-10-12 run: no HISTORY OWED line)"
    ],
    "remedy": "Before the switch is set to 'ask': a pause/stop state the history-owed step reads before any request, or a ruling that withdraws the clause. Until then the switch stays unset; the hazard fires only on that act.",
    "owner": "2.0.0_SA_COO~V1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~V1",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~V1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-D1-W25-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "RIV-wc-1 could not keep two script-size caps green (test_r24cu1 test_script_shape, test_r25mr1 test_script_growth_bound) as filed by its worker.",
    "evidence": [
      "investigation row ETFS_RIVALS-D1-W25-S1",
      "pytest at HEAD 2026-10-12 15:5xZ: rivalfunds/tests/test_r24cu1_chart_frame_ticks_tip.py, test_r25mr1_marker_readout.py, test_r15md1_chart_frame_and_script.py -> 23 passed (script 10631 B), RIV-wc-1 merged and its J1 MET"
    ],
    "remedy": "The named caps are green with RIV-wc-1 merged.",
    "owner": "2.0.0_SA_COO~V1",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~V1",
      "round": "v1"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-D1-W25-S2",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "test_r15md1_chart_frame_and_script.py:63 pinned the static '365 days' placeholder that RIV-wc-1's interface item 1 forbids.",
    "evidence": [
      "investigation row ETFS_RIVALS-D1-W25-S2",
      "pytest at HEAD 2026-10-12 15:5xZ: the same three files -> 23 passed"
    ],
    "remedy": "The test and the order agree.",
    "owner": "2.0.0_SA_COO~V1",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~V1",
      "round": "v1"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-D1-W26-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Two G5 readers outside RIV-wd-1's paths (publish_page.py's audit window loop, ai_accounts.py's trade facts) did not skip the new below_tolerance action.",
    "evidence": [
      "investigation row ETFS_RIVALS-D1-W26-S1",
      "data/etfs/scripts/rivalfunds/publish_page.py:544 (7a25a44c24) and ai_accounts.py:178 (455b28ada6) skip below_tolerance at HEAD",
      "served s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-12/audit.html: 0 occurrences of 'below tolerance'"
    ],
    "remedy": "Both readers skip below_tolerance rows.",
    "owner": "2.0.0_SA_COO~V1",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~V1",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~V1",
      "at": "2026-10-09T13:20:22Z"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-D1-S15",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Since efb0b41626 (1.0.0_SA_CTO), round-close-check counts any CVO-kind row that MENTIONS an order's short id beside a generic criterion id as a GRADE, whatever verdict the row states. In round 28 it read MAY-CLOSE while three J1s had no terminal grade, and credited wi-1 J1 to a row that says in words it is not a grade.",
    "evidence": [
      "investigation row ETFS_RIVALS-D1-S15",
      ".tools/round-close-check.py :314, :420-423",
      "round-28 close packet @55a689301c cites a verdict per criterion (the row's named disarm condition); msg 4468 assigns the recording to this seat"
    ],
    "remedy": "Grade only on a row that DECLARES the criterion it grades with a verdict value (an `adjudicates`-style field, as the selftest at :575 uses), never on a free-text mention; GRADED and MET reported apart.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~V1",
      "at": "2026-10-12T16:05Z"
    },
    "closed": false
  }
]
```

## ADJUDICATION_v1.dell1.md row D1-C-S17 (same commit; times and world_is re-measured at landing)

```json
{
  "id": "ETFS_RIVALS-D1-C-S17",
  "project": "ETFS_RIVALS",
  "fabric": "dell1",
  "surfaced_by": "3.0.0_SA_CVO~RV1",
  "surfaced_at": "<the landing time>",
  "one_line": "Round-28 L8 compile (dell1): the 8 BLOCKING/ARMED investigation items the gate reads as undispositioned are GRADUATED into REMEDIATION_v1.dell1.md, each with the state measured at HEAD: 5 REMEDIATED, 3 OPEN.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
    "ETFS_RIVALS-Z-S79",
    "ETFS_RIVALS-Z-S80",
    "ETFS_RIVALS-Z-S81",
    "ETFS_RIVALS-D1-S2",
    "ETFS_RIVALS-D1-W25-S1",
    "ETFS_RIVALS-D1-W25-S2",
    "ETFS_RIVALS-D1-W26-S1",
    "ETFS_RIVALS-D1-S15"
  ],
  "spec_asserts": "Spine L10 (CLAUDE.md rule 27): ONE SLUG to the CTO only after every task order of the round is terminal and every BLOCKING or ARMED row is dispositioned. surprise-row-gate.py:1011-1028.",
  "world_is": "<re-measured at landing: the gate census, each item's state, the task-order census>",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "remediations/REMEDIATION_v1.dell1.md (same commit)",
      "close packet @55a689301c",
      "2.0.0_SA_COO~V1 msg 4468"
    ]
  },
  "disposition": "GRADUATED"
}
```

-- 3.0.0_SA_CVO~RV1
