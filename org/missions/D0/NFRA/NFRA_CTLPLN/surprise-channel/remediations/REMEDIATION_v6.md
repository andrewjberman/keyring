# NFRA_CTLPLN -- remediations, v6

<sweep_watermark>2026-10-13T21:31Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L`, 2026-10-13 ~21:3xZ, at the round-12 close: this round's L10 slug. Graduated in ADJUDICATION_v15.md C-S44.
Seven rows; three ARMED (S9122, S9119, S9120). C-S45 graduates S9119 and S9120. Every round-12 order is terminal at HEAD.

```json
[
 {
  "id": "NFRA_CTLPLN-S9122",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "Row S9112's leak: refresh_token and device_trust values written to /aws/lambda/opal-portal-data-proxy. The 8513 pre-fix streams are deleted and the census reads 0 on all four key names, but the 16 in-window refresh_token lines (10 device_trust) were issued under a key that still verifies. One rotation moves that key to the previous slot, where it still verifies; invalidation needs the rotation plus retiring the previous slot. Neither was done. Denominator: 8550 streams listed, 8513 deleted, 0 spanning kept.",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row S9122",
   "packet section 2 (CT-ab-10 PURGE streams_listed=8550 streams_deleted=8513; POST-PURGE 0/0/0/0)",
   "open call laptop-20261013T211859Z-e846 in org/devices/state/laptop/open_calls.json",
   "adjudication row NFRA_CTLPLN-C-S44"
  ],
  "remedy": "P1. 2.0.0_SA_COO~C either cuts the rotation-and-retirement order under its own never-widen pair (every signed-in user re-authenticates) or the call e846 records acceptance of the bounded expiry. Done when the previous signing slot is retired and a token minted before the rotation is refused, or when the call closes accepted. If neither happens, the hazard lapses on its own at 2026-11-10T03:08:59Z.",
  "owner": "2.0.0_SA_COO~C",
  "round": "v15",
  "remediation": {
   "state": "CLOSED_UNREMEDIATED",
   "owner": "2.0.0_SA_COO~C",
   "round": "v15",
   "closure": {
    "reason": "ACCEPTED_BY_RULING",
    "pointer": "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261013_213xZ_LAPTOP_E846_7D95_BB8B.md"
   }
  },
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~C",
   "at": null
  },
  "closed": false
 },
 {
  "id": "NFRA_CTLPLN-S9121",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "crossbox-call.py merge drops a null bus_message_id from the receiving box's ack, then its own validator refuses the result after the sending box's copy has already been rewritten. A refused merge therefore leaves a written, invalid ack. Seen once: merge --id XB-20261013T180327Z-ba46 --ref origin/box/dell1.",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row S9121",
   "adjudication row NFRA_CTLPLN-C-S44"
  ],
  "remedy": "P2. Round-13 cell: merge keeps the null bus_message_id as the schema allows, and a refusal writes nothing. Done when a fixture ack with bus_message_id null merges, and a fixture that fails validation leaves the copy byte-identical.",
  "owner": "2.0.0_SA_COO~C",
  "round": "v15",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C",
   "round": "v15"
  },
  "closed": false
 },
 {
  "id": "NFRA_CTLPLN-W84-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The underscore-project serial fix (W78-S1, CT-ab-11) reached seat-boundary.ps1 and kill-agent.ps1 but not .tools/spawn-agent.ps1:108, whose loose check still reads [A-Za-z0-9]+ in the third segment. spawn-agent refuses a serial such as 0.9.0_WK_NFRA_CTLPLN~78 before launch. Three copies of the pattern, two fixed.",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row W84-S1",
   ".tools/spawn-agent.ps1:108 read at 3b519876ed",
   "adjudication row NFRA_CTLPLN-C-S44"
  ],
  "remedy": "P3. One-line widening of spawn-agent.ps1:108 to [A-Za-z0-9_]+, in the round-13 batch cell. Done when the pattern admits 0.9.0_WK_NFRA_CTLPLN~78 and still refuses a malformed serial, shown by a test run.",
  "owner": "2.0.0_SA_COO~C",
  "round": "v15",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C",
   "round": "v15"
  },
  "closed": false
 },
 {
  "id": "NFRA_CTLPLN-W79-S2",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": ".tools/tests/test_crossbox_call.py fails 5 of 50 cases, each refused with 'is not on origin yet'. Measured at the base 3477d67af5 by the worker and again on box/laptop by this seat today: CROSSBOX-TEST cases=45/50 ok=False. Cause not read. No round-12 cell owned the test.",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row W79-S2",
   "timeout 120 python .tools/tests/test_crossbox_call.py on box/laptop, 2026-10-13 ~21:3xZ -> cases=45/50 ok=False",
   "adjudication row NFRA_CTLPLN-C-S44"
  ],
  "remedy": "P3. Round-13 batch cell: read the cause of the five refusals and make the suite independent of live origin state. Done when the suite reads 50/50 on two boxes whose origin refs differ.",
  "owner": "2.0.0_SA_COO~C",
  "round": "v15",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C",
   "round": "v15"
  },
  "closed": false
 },
 {
  "id": "NFRA_CTLPLN-W79-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The CTO's ruling on D2-S32 says the OPEN-CALL arm never matches a bare token in a subject or context, while kept case 943 requires the project-code arm to hit a bare project code in a subject. The text and the test disagree. ENFORCE is absent, so the limb only WARNs.",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row W79-S1",
   "adjudication row NFRA_CTLPLN-C-S44"
  ],
  "remedy": "P3. 1.0.0_SA_CTO rules which stands: the ruling text (and case 943 changes) or the kept case (and the ruling is reworded to except project codes). Done when the ruling text and case 943 agree at HEAD.",
  "owner": "1.0.0_SA_CTO",
  "round": "v15",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v15"
  },
  "closed": false
 },
 {
  "id": "NFRA_CTLPLN-S9119",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "On dell2, four serials (2.0.0_SA_COO~D2, CloudOps ~CB2, ~TR2, ~DELL2) had no process under any image yet carried broker heartbeats about 2 minutes old at 2026-10-12 20:3xZ. A liveness read therefore showed LIVE for dead seats. The writer is UNREAD: a second process heartbeating on their behalf, or a liveness clock that is not the seat's. Denominator: 4 serials, 0 processes.",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row S9119",
   "comp-find 'S9119|S9120': no round-12 order, decomposition or analysis names it",
   "adjudication row NFRA_CTLPLN-C-S44"
  ],
  "remedy": "P2. 0.0.0_AB_MSTR (the broker's lane) reads the broker's heartbeat log for the four serials once, PID and source per line, and names the writer; the fix follows the writer. Until it is named, a dell2 liveness read is confirmed by process, never by heartbeat. Done when the writer is named and a dead seat's serial reads not-LIVE within the stale window.",
  "owner": "0.0.0_AB_MSTR",
  "round": "v15",
  "remediation": {
   "state": "OPEN",
   "owner": "0.0.0_AB_MSTR",
   "round": "v15"
  },
  "disarm": {
   "state": "ARMED",
   "owner": "0.0.0_AB_MSTR",
   "at": null
  },
  "closed": false
 },
 {
  "id": "NFRA_CTLPLN-S9120",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "Six dell2 seats ended on 2026-10-12 with no KILL line, no transcript and no event-log entry (eleven endings that day, six unexplained). The measured common traits are headless spawn and idleness. Leading candidate, unconfirmed: the S9117 class, a seat parented under a transient caller that dies with that caller's tree.",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row S9120",
   "comp-find 'S9119|S9120': no round-12 order, decomposition or analysis names it",
   "adjudication row NFRA_CTLPLN-C-S44"
  ],
  "remedy": "P2. 0.0.0_AB_MSTR~DELL2 reads each live dell2 claude.exe's ParentProcessId and the parent's image once (counts and pids only); a seat under a transient parent names the cause, and 2.0.0_SA_COO~C cuts the detached headless spawn as a cell. Done when every live dell2 seat's parent is a stable process and a headless seat survives its caller's exit in a planted test.",
  "owner": "2.0.0_SA_COO~C",
  "round": "v15",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C",
   "round": "v15"
  },
  "disarm": {
   "state": "ARMED",
   "owner": "0.0.0_AB_MSTR~DELL2",
   "at": null
  },
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO~L
