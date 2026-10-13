# ADVI_FIRMBKTS -- round 3 remediations (dell1)

<sweep_watermark>2026-10-11T11:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T11:45:00Z. Graduated at ADJUDICATION_v4: 37 rows. To 2.0.0_SA_COO~B1: the face template, the act-2
census and behaviors, FB-f-7's text, the producers' role grant (D1-S18), the two dispatcher-gate rows INERT while the mode cannot be set,
and D1-C-S21. To 1.0.0_SA_CTO~DELL1: the FAULT-84 grain edges, three instruments, D1-S14, S12, and D1-S17 (ARMED). To
0.0.0_AB_MSTR~DELL1: the SEV1 SMS path (D1-S15, S16, S20). To 0.7.0_AE_CloudOps: D1-S19 (ARMED). FWD-1 PARTIAL (D1-C-S14).

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S4",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "THE WORKER FACE ASKS FOR THE ORDER'S <status> TO BE FLIPPED, BUT THE FACE CARRIES NO <status> AND THE ORDER FILE IS OUTSIDE THIS WORKER'S <paths>",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W16-S4",
      "adjudication row ADVI_FIRMBKTS-D1-C-S22"
    ],
    "remedy": "The round-4 cut either names the order file in the worker's <paths> for the flip, or states that the issuer flips it; and the face states the pin rule (each artifact row carries the commit that added it). Close when: the round-4 orders carry it",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W17-S4",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FB-f-7 section 5 asks for the order's <status> to be flipped to complete in the commit, but the order file is not in the cell's <paths> write grant, so the flip is not written by this worker.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W17-S4",
      "adjudication row ADVI_FIRMBKTS-D1-C-S22"
    ],
    "remedy": "The round-4 cut either names the order file in the worker's <paths> for the flip, or states that the issuer flips it; and the face states the pin rule (each artifact row carries the commit that added it). Close when: the round-4 orders carry it",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S15",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "THE FACE ORDERS THE INSTANCE COMMITTED WITH ITS ARTIFACTS IN ONE COMMIT, BUT THE PIN RULE REQUIRES EACH ARTIFACT ROW TO CARRY THE COMMIT THAT CARRIED THE FILE: THE ARTIFACTS ARE COMMITTED FIRST AND THE INSTANCE SECOND",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W16-S15",
      "adjudication row ADVI_FIRMBKTS-D1-C-S22"
    ],
    "remedy": "The round-4 cut either names the order file in the worker's <paths> for the flip, or states that the issuer flips it; and the face states the pin rule (each artifact row carries the commit that added it). Close when: the round-4 orders carry it",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S5",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "PRODUCER_CENSUS.json OMITS THREE SERVED gold/views/ WRITES IN D_00 (lines 1106-1108), SO THE CENSUS UNDER-COUNTS THE PLATINUM WRITE LINES OF THE 14 WRITERS",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W16-S5",
      "adjudication row ADVI_FIRMBKTS-D1-C-S22"
    ],
    "remedy": "Before act 2's GO, the act-2 reader and writer census accounts each named site (routed through the seam, or ruled not served). Close when: the act-2 un-park read prints each site's disposition",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S6",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "PRODUCER_CENSUS.json OMITS A SERVED gold/entities/clients/ WRITE IN C_06 (_write_relationship_views, LINE 381)",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W16-S6",
      "adjudication row ADVI_FIRMBKTS-D1-C-S22"
    ],
    "remedy": "Before act 2's GO, the act-2 reader and writer census accounts each named site (routed through the seam, or ruled not served). Close when: the act-2 un-park read prints each site's disposition",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S11",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "PRODUCER_CENSUS.json OMITS A SERVED ADVISOR-COMPOSITION WRITE IN D_03 (THE NON-ARCHITECT TUPLE, BASE LINE 870), WHICH THE RULED 62 DO NOT COVER",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W16-S11",
      "adjudication row ADVI_FIRMBKTS-D1-C-S22"
    ],
    "remedy": "Before act 2's GO, the act-2 reader and writer census accounts each named site (routed through the seam, or ruled not served). Close when: the act-2 un-park read prints each site's disposition",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S12",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "PRODUCER_CENSUS.json OMITS D_04's SPLIT-BRANCH WRITES (BASE LINES 395-408), INCLUDING THE SERVED platinum/firm/fee_efficiency.json KEY",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W16-S12",
      "adjudication row ADVI_FIRMBKTS-D1-C-S22"
    ],
    "remedy": "Before act 2's GO, the act-2 reader and writer census accounts each named site (routed through the seam, or ruled not served). Close when: the act-2 un-park read prints each site's disposition",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W17-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FB-f-7 1a.2 says the origin bucket comes from the path tenant's own configured bucket; the router sets the origin to the canonical tier constant for every platinum/advi/ request, as it did at base.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W17-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S22"
    ],
    "remedy": "The issuer corrects the FB-f-7 record text to the built behavior (or rules the text stands). Close when: the record or a ruling names it",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W17-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FB-f-7 ALIAS control is premised on a bucket difference between the alias and its declared directory that the registry does not carry today; the control's ALIAS arms therefore run on a cutover test double.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W17-S3",
      "adjudication row ADVI_FIRMBKTS-D1-C-S22"
    ],
    "remedy": "The issuer corrects the FB-f-7 record text to the built behavior (or rules the text stands). Close when: the record or a ruling names it",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W17-S6",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The hand-written header of _shared/firm-config.mjs (outside the generated block) still states the alias pair as mockadv -> {49financial}; the generated block now lists one equivalence class per scope.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W17-S6",
      "adjudication row ADVI_FIRMBKTS-D1-C-S22"
    ],
    "remedy": "The issuer corrects the FB-f-7 record text to the built behavior (or rules the text stands). Close when: the record or a ruling names it",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W20-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Legacy-copy PUTs (the dual writes to the legacy key) now go through platinum_destination(), so under canonical each copy lands at the canonical home of its legacy name and not at the legacy home",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W20-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S22"
    ],
    "remedy": "Read at act 2's un-park, with the pair: each canonical-mode behavior named is accepted, changed, or ruled. Close when: the act-2 pair names it",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W20-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Three helpers take the bucket as a caller argument (helpers.s3_object_exists, D_01 _load_aua_certification, etf_classifier IdentityResolver.from_s3), and the seam ignores a bucket argument, so the three calls are marked exempt instead of routed",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W20-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S22"
    ],
    "remedy": "Read at act 2's un-park, with the pair: each canonical-mode behavior named is accepted, changed, or ruled. Close when: the act-2 pair names it",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W20-S4",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Print and log lines beside the routed writes and reads still print s3://<S3_BUCKET or BUCKET>/<key>; under canonical the printed location is the legacy bucket, not the bucket the call used",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W20-S4",
      "adjudication row ADVI_FIRMBKTS-D1-C-S22"
    ],
    "remedy": "Read at act 2's un-park, with the pair: each canonical-mode behavior named is accepted, changed, or ruled. Close when: the act-2 pair names it",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W21-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "On the --chain downstream path the freshness gate reads before any sync of code/gold into SCRIPTS, so the step-2 gate block falls back to the legacy URI under canonical wherever lib/ is not already in SCRIPTS; the order's dirname contingency is not shown to reach lib/ on the runner.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W21-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S22"
    ],
    "remedy": "Disarmed at act 2's un-park: the dispatcher's gate reads the new home on every invocation path (wrapper and direct), exercised. Close when: that exercise is in the act-2 record",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": "2026-10-11T11:45:00Z"
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W23-S6",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The step-2 gate search reaches lib/platinum_dest.py through the dispatcher's own directory only on the wrapper path; a direct invocation from another directory, and any --chain downstream caller not in this repo, fall to SCRIPTS and then to the legacy URI on a fresh instance.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W23-S6",
      "adjudication row ADVI_FIRMBKTS-D1-C-S22"
    ],
    "remedy": "Disarmed at act 2's un-park: the dispatcher's gate reads the new home on every invocation path (wrapper and direct), exercised. Close when: that exercise is in the act-2 record",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": "2026-10-11T11:45:00Z"
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W22-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The read census grades boto3 call syntax only: opal-partners-data reads and lists through awswrangler at three sites (lambda_function.py:1100, :1160, :1224) whose s3:// paths the census does not see. Their keys (gold/timeseries/...) lie outside the 11 served classes, so no served read is unrouted, but the census's ALL SITES ROUTED line does not cover them.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W22-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S22"
    ],
    "remedy": "Before act 2's GO, the act-2 reader and writer census accounts each named site (routed through the seam, or ruled not served). Close when: the act-2 un-park read prints each site's disposition",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S18",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "TO-FB-f-9 step 2(b): the producers' role bd-exporter-ec2-role holds NO Allow for s3:PutObject or s3:GetObject on opal-data-49financial/advi/49financial/platinum/*, the new home of all 11 served classes, and its ListBucket allow is conditioned on other prefixes; the order's simulate instrument cannot run for this principal, so the read is a policy-document evaluation.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S18",
      "adjudication row ADVI_FIRMBKTS-D1-C-S22"
    ],
    "remedy": "Round 4's own act: the producers' role (bd-exporter-ec2-role) gets Put/Get on the new prefix through the laptop identity, with its pair, before act 2. Close when: an exercised write by that role at the new prefix is recorded",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W12-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "RULE (d) OVERLAP-0 MERGES CANNOT BE EXECUTED FROM MAPPING_V2: SEVEN NEW CLASSES RECORD NO DESTINATION, SO THE TABLE THEY MERGE INTO IS NOT IN THE ROW",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W12-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The CTO rules each edge (or the next table repair places it). Close when: the ruling exists and mapping reads the class placed or FAULT with that ruling cited",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W12-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "RULE (b) WOULD RE-ADDRESS PLACED COMPLETION-MARKER ROWS: A ROUND-1 SILVER MARKER GROUP SITS IN THE SILVER TIER, AND THE COPIED-UNCHANGED RULE FORBIDS A KIND FIELD ON PLACED ROWS",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W12-S3",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The CTO rules each edge (or the next table repair places it). Close when: the ruling exists and mapping reads the class placed or FAULT with that ruling cited",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W12-S5",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "INFLECTION AND SILVER COMPLETION MARKERS NEED STATE FAMILY NAMES THE RULING DOES NOT NAME (gold_complete, silver_complete, bronze_complete FOR ORION-API)",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W12-S5",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The CTO rules each edge (or the next table repair places it). Close when: the ruling exists and mapping reads the class placed or FAULT with that ruling cited",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W12-S6",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A QA-NAMED BRONZE FEED MATCHES TWO ROUND-1 RULES: RB (QA OUTPUT, NO DESTINATION) AND BRONZE/** (HOME). PLACED UNDER BRONZE/**",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W12-S6",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The CTO rules each edge (or the next table repair places it). Close when: the ruling exists and mapping reads the class placed or FAULT with that ruling cited",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W12-S7",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "1,142 performance_dim_SKIP.json FILES SIT BESIDE DATA IN ORION-API DATE PARTITIONS. RULE (b) NAMES COMPLETION MARKERS ONLY, SO THEY STAY DATA",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W12-S7",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The CTO rules each edge (or the next table repair places it). Close when: the ruling exists and mapping reads the class placed or FAULT with that ruling cited",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W12-S8",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "THE TWO ECLIPSE BRONZE CLASSES WRITE THE SAME STATE KEYS FOR SHARED DATES (66 MARKER KEYS), SO THEIR MARKER ROWS ARE FAULT",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W12-S8",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The CTO rules each edge (or the next table repair places it). Close when: the ruling exists and mapping reads the class placed or FAULT with that ruling cited",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W12-S9",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "INHERITED RE-GRID ROWS DID NOT SUM TO THEIR LIVE LISTING (logs/ 30 OBJECTS, gold/timeseries/ 3), AND CHECK ARM S2 READS ONLY THE FIELD",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W12-S9",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The CTO rules each edge (or the next table repair places it). Close when: the ruling exists and mapping reads the class placed or FAULT with that ruling cited",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W12-S10",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A CLASS-GRAIN ROW CARRIES THE TOKEN {partition} IN ITS ADDRESS: THE GOLD/CLIENTS CLASS PLACED AT ITS PREFIX HAS NO ONE PARTITION",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W12-S10",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The CTO rules each edge (or the next table repair places it). Close when: the ruling exists and mapping reads the class placed or FAULT with that ruling cited",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W12-S11",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TEN forwardfill _complete/ GROUPS ARE COMPLETION MARKERS BY NAME AND SIT BESIDE DATA IN THEIR RE-GRIDS, BUT STAY FAULT (1e): THEIR KEYS COLLIDE WITH EACH OTHER",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W12-S11",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The CTO rules each edge (or the next table repair places it). Close when: the ruling exists and mapping reads the class placed or FAULT with that ruling cited",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "comp-pipescript io UNDER-REPORTS D_04 WRITES (ONE PRINTED, 25 IN THE CODE) AND LISTS A READ AS A WRITE",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W16-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The tool's owner fixes the instrument or documents the blind spot in its own --help. Close when: the fix or the documented limit lands on that tool",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "comp-pipescript RESOLVES ONE OF THE 26 E-SERIES bd-gold IDS, AND E_01 AND E_24 WRITE SERVED KEYS WITH NO DISPATCH ENTRY",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W16-S3",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The tool's owner fixes the instrument or documents the blind spot in its own --help. Close when: the fix or the documented limit lands on that tool",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W22-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "targets classifies each Lambda copy of platinum_dest_view.py SHIP on the lambda plane only through the OTHER Lambda's served_seam.py import: lambda_plane_consumers skips the function that owns the file, so each copy's SHIP status rests on the other function's files list. If either function drops served_seam.py, its copy becomes UNCLASSIFIED and targets exits 1.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W22-S3",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The tool's owner fixes the instrument or documents the blind spot in its own --help. Close when: the fix or the documented limit lands on that tool",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S14",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "THE CTO'S ADDENDUM 4 CONDITION 1 ON E_01 AND E_24: E_01 IS NOT A SERVED-KEY WRITER UNDER THE MODULE'S OWN RULE AND LAST WROTE 2026-04-07; E_24 HAS NO LAUNCHER AND NO SendCommand NAMING IT IN 45 DAYS (0 OF 4,010)",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S14",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The CTO confirms or amends ADDENDUM 4 condition 1 for E_01 and E_24. Close when: the analysis names them",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "ADVI_FIRMBKTS-S12",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "TO-FB-f-8 act 1 APPLIED on the laptop (Branch A holds on every live read) but the pair's condition 'a post-apply plan reads no changes' is NOT met: the plan still lists aws_wafv2_web_acl.opal_cloudfront_protection (1 to change) because UpdateWebACL cannot clear the provider's stored empty Version; also AC4 as written reads 0, not 3, because OverrideAction.Count is an empty object.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-S12",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The portal-auth root's standing WAF ACL diff is reconciled in Terraform or carried as a named rider for every later apply there. Close when: a portal-auth plan reads no ACL change, or the rider is ruled standing",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S17",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "ARMED: a stale copy of 49 Financial's ownership map (authorization data) sits at the new home (F7 copy 04:01Z, 474,726 B; legacy rewritten 05:24Z, 474,841 B); once act 4 moves the registry map value, any ordinary deploy of auth-validator-edge or an IRPT consumer would read the stale map silently.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S17",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "Disarmed at act 4 when the validator and IRPT read the live map at the new home and the act-3 delta copy overwrites the stale copy (ADDENDUM 7). Close when: act 4's record shows both",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": "2026-10-13T06:10:00Z"
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S15",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The firm-isolation guard's SEV1 page path delivers nothing: every publish to opal-infrastructure-alerts in the 40 minutes read (08:14Z, 08:15Z, and this seat's 3 test publishes at 08:43Z) failed delivery to the topic's one subscription (SMS); NumberOfNotificationsDelivered 0, NumberOfNotificationsFailed 8.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S15",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The reason is read (D1-S20: no origination identity for the destination number); the remedy (an origination identity, a cost) goes to Andrew and its owner places it. Close when: a SEV1 test publish reads DELIVERED in the delivery-status log",
    "owner": "0.0.0_AB_MSTR~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S16",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "D1-S15 narrowed: the SEV1 SMS page path has delivered NOTHING in 14 days (0 delivered, 28 failed, 09-27..10-10); not sandbox (IsInSandbox false), not the USD 50 spend limit (SMSMonthToDateSpentUSD has no datapoints, i.e. no spend); origination number and opt-out unread (denied to the dell identity).",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S16",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The reason is read (D1-S20: no origination identity for the destination number); the remedy (an origination identity, a cost) goes to Andrew and its owner places it. Close when: a SEV1 test publish reads DELIVERED in the delivery-status log",
    "owner": "0.0.0_AB_MSTR~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S20",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "D1-S15/S16 cause READ: every SEV1 SMS fails with providerResponse 'No origination identity available to send to destination number' -- the registered ACTIVE toll-free number exists but SNS cannot use it for the subscriber's US number; not sandbox, spend, opt-out or registration.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S20",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The reason is read (D1-S20: no origination identity for the destination number); the remedy (an origination identity, a cost) goes to Andrew and its owner places it. Close when: a SEV1 test publish reads DELIVERED in the delivery-status log",
    "owner": "0.0.0_AB_MSTR~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S19",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE inf-pipeline ROOT HOLDS A PENDING, UNAPPLIED aws_secretsmanager_secret_version.eclipse_jwt_initial: ANY UNSCOPED APPLY OF THAT ROOT CREATES A NEW CURRENT VERSION OF orion/eclipse_jwt/current",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S19",
      "adjudication row ADVI_FIRMBKTS-D1-C-S23"
    ],
    "remedy": "The root's owner applies or removes eclipse_jwt_initial deliberately; until then every apply of inf-pipeline is scoped. Close when: a plan of the root reads no pending secret-version create",
    "owner": "0.7.0_AE_CloudOps",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "0.7.0_AE_CloudOps",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.7.0_AE_CloudOps",
      "at": "2026-10-13T06:10:00Z"
    },
    "closed": true
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S21",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "NEW: TO-FB-f-8 reached complete with its four criteria still typed as placeholders (<ROUTER_VERSION>, <ROUTER_SHA256>, <GUARD_VERSION>, <GUARD_SHA256>, <WAF_ACL_NAME>, <WAF_ACL_ID>). The values exist only in the change-management entry and the proof, so the order text cannot be re-run as written; this seat re-ran it from the entry's values (D1-C-S16).",
    "evidence": [
      "adjudication row ADVI_FIRMBKTS-D1-C-S21",
      "task-orders/ADVI_FIRMBKTS.TO-FB-f-8.act1-deploy-advtenant.md"
    ],
    "remedy": "Order criteria carry their values by the time the order is complete (the issuer amends the placeholders in, or the gate refuses the flip). Close when: TO-FB-f-8's criteria read values, or the round-4 template forbids a placeholder at complete",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  }
]
```
