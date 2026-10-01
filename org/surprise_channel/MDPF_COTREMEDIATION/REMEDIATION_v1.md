# MDPF_COTREMEDIATION -- remediations (closure compile)

<sweep_watermark>2026-09-22T18:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-01. Graduated at the closure compile (ADJUDICATION_v1.md): 11 rows. Closed here on this seat's own reads: S4, S5, S18, S20. Open with an owner: S3, S6, S7, S13, S16, S17, S19. The project has no live COO lane, so every open row is owned by 1.0.0_SA_CTO for placement; S19 is placed in MDPF_HEALGAP by CTO 103613 (RULINGS batch 69 @6291fa70e5), with finding F-A of the acceptance grade.

```json
[
  {
    "id": "MDPF_COTREMEDIATION-S3",
    "project": "MDPF_COTREMEDIATION",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The served cottonwood and global date axes carry nine non-trading days (eight weekend days and 2026-06-19) that 49financial and inflection exclude. It predates the freeze, survived the repair, and a re-run does not touch it.",
    "evidence": [
      "served payloads read by this seat 2026-10-01 07:4xZ against lib/trading_calendar.is_trading_day: cottonwood 9 non-trading dates of 486, global 9 of 486 (2026-05-30, 05-31, 06-06, 06-07, 06-13, 06-14, 06-19, 06-20, 06-21); 49financial 0 of 477, inflection 0 of 477",
      "investigation row MDPF_COTREMEDIATION-S3 (2.0.0_SA_COO)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_COTREMEDIATION_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P2: the cottonwood slice and the global fold drop non-trading dates from the served axis, or the page states why two scopes carry them. A served change: both never-widen halves. Placement is the CTO's (MDPF_CANON or MDPF_HEALGAP).",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "MDPF_COTREMEDIATION-S4",
    "project": "MDPF_COTREMEDIATION",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The AE vendor leg as written would have shipped a 33-day-old undeployed silver shape change (the rebalancer provenance sidecar) as a side effect of the contract repair, because the vendoring tool's copy mode has no module filter.",
    "evidence": [
      "lambda get-function opal-assets-silver-blackdiamond (this seat, 2026-10-01 07:5xZ; CodeSha256 DZl5N5Io..., LastModified 2026-09-27T10:35:46Z): the deployed rebalancer_conversion.py (ae60701ddd) and rebalancer_schemas.py (9d9fce1213) equal the lambda directory and differ from source (fd91303c33, 5471afded2); the deployed rebalancer_schemas.py has no PROVENANCE_CONTRACT_START. The sidecar did not ship",
      "the same read: mirror_schemas.py deployed 8818df2f03 = source, so the one module the repair needed did ship",
      "investigation row MDPF_COTREMEDIATION-S4 (0.5.0_AE_OpalETL~B): the seat refused the leg as written and the ruling made it a targeted vendor",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_COTREMEDIATION_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "Done: the leg ran as a targeted vendor of the contract module alone. 37 days and one later deploy of the same function on, the sidecar is still not in the deployed package.",
    "owner": "0.5.0_AE_OpalETL~B",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "0.5.0_AE_OpalETL~B",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.5.0_AE_OpalETL~B",
      "at": "2026-08-25T17:05Z"
    },
    "closed": true
  },
  {
    "id": "MDPF_COTREMEDIATION-S5",
    "project": "MDPF_COTREMEDIATION",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The source-map entry of the silver converter could not stay true through a sanctioned build (the build writes the artifact cells unconditionally), and one cell of the entry was already stale beside a true one, with nothing marking which.",
    "evidence": [
      "infra/aws/lambda/ci/lambda-source-map.json at HEAD, entry opal-assets-silver-blackdiamond (this seat): artifact_sha256 DZl5N5IoyMTwGZI1Dl/D+40Ldd+ZzkbF60M6JFwD3Pw=, last_deployed_at 2026-09-27T10:44:31Z, recorded_by record-terraform-deploy.sh, deploy_ledger nfra-mcpindex-silver-mirror-guard",
      "lambda get-function-configuration opal-assets-silver-blackdiamond (this seat): CodeSha256 DZl5N5IoyMTwGZI1Dl/D+40Ldd+ZzkbF60M6JFwD3Pw=, LastModified 2026-09-27T10:35:46Z -- the hash cell equals the live artifact and the date cell is the same deploy",
      "investigation row MDPF_COTREMEDIATION-S5 (0.5.0_AE_OpalETL~B)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_COTREMEDIATION_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "Done by a later deploy: the entry was re-stated whole by the deploy recorder on 2026-09-27, and both cells now describe the live artifact.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "closed": true
  },
  {
    "id": "MDPF_COTREMEDIATION-S6",
    "project": "MDPF_COTREMEDIATION",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The targeted vendor left the silver converter's lambda directory out of parity with source on purpose, and the residue has grown: three of four shared modules now differ, so a parity check on that directory cannot tell sanctioned residue from real drift.",
    "evidence": [
      "md5 over LF-normalised bytes (this seat, 2026-10-01 07:5xZ): rebalancer_conversion.py lambda directory ae60701ddd vs source fd91303c33; rebalancer_schemas.py 9d9fce1213 vs 5471afded2; mirror_conversion.py 259faec26b vs 8f96100280; mirror_schemas.py equal (8818df2f03). The deployed zip equals the lambda directory on all four",
      "the marker the row cites (BUILD_MANIFEST.json vendor_closure_note) was not confirmed to name the expected-red modules: the note read by this seat opens with the 2026-07-22 WSE_COTMDL text",
      "investigation rows MDPF_COTREMEDIATION-S6 (3.0.0_SA_CVO) and -S8 (0.4.0_DS_ClientPlatform~M)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_COTREMEDIATION_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P1: one seated deploy brings the silver converter packages to source (the twin deploy the row names), or the manifest states per module which difference is sanctioned and until when. The twin deploy has had no seat for 37 days. Placement is the CTO's.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_COTREMEDIATION-S7",
    "project": "MDPF_COTREMEDIATION",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "rebalancer_schemas.py declares PROVENANCE_CONTRACT_START = 2026-07-23 for columns whose producing code has never been deployed, and the converter's force-guard is drawn at that contract date rather than the deploy date. The day the twin ships, a forced re-run inside the gap would write provenance the design forbids fabricating. The gap was 33 days at filing and is 70 days today.",
    "evidence": [
      "data/assets/scripts/silver/rebalancer_schemas.py:83 at HEAD (this seat): PROVENANCE_CONTRACT_START = \"2026-07-23\"",
      "the deployed opal-assets-silver-blackdiamond package (this seat, 2026-10-01): rebalancer_schemas.py has no PROVENANCE_CONTRACT_START and differs from source, so the twin has not shipped and the hazard is not yet live",
      "investigation row MDPF_COTREMEDIATION-S7 (0.5.0_AE_OpalETL~B, re-derived by 3.0.0_SA_CVO)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_COTREMEDIATION_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P1, a condition on the twin deploy and not after it: the constant (or the guard) is drawn at the deploy date before the package ships, with a test that a forced re-run of a pre-deploy partition is refused. It rides the same seat as S6.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_COTREMEDIATION-S13",
    "project": "MDPF_COTREMEDIATION",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "One served field name carries different derivations: account_count_total is the by_model sum for 49financial, inflection and (on the last date) global, and is not for cottonwood, while every scope labels the count measured. A reader comparing account counts across partners compares different quantities under one name.",
    "evidence": [
      "served payloads read by this seat 2026-10-01 07:4xZ, last date 2026-09-29: cottonwood account_count_total 361 vs by_model account_count sum 542; global 8,242 vs 8,242; 49financial 7,144 vs 7,144; inflection 548 vs 548",
      "investigation row MDPF_COTREMEDIATION-S13 (0.4.0_DS_ClientPlatform~N; 317 vs 472 at filing)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_COTREMEDIATION_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P1, a decision about a served label before any code: the CTO rules what cottonwood's total counts (distinct accounts across overlapping models is the likely reading) and the payload says so in a field a consumer can read. Placement is the CTO's.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_COTREMEDIATION-S16",
    "project": "MDPF_COTREMEDIATION",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The gold run manifest recorded reconciliation PASS on a run that built 6 of 12 objects and lost 2 of 4 scopes: the failures sat in errors{} while the status-shaped scopes{} field did not know about them.",
    "evidence": [
      "investigation row MDPF_COTREMEDIATION-S16 (3.0.0_SA_CVO, 2026-08-26): this seat's read of that day's manifest",
      "NOT re-read at this compile: the manifest of a recent partial run was not located, so whether the field still answers green on a partial run is unverified",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_COTREMEDIATION_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P2: scopes.reconciliation is computed over the scopes the run set out to build, so a partial run cannot read PASS; or the field is renamed to what it measures. Placement is the CTO's (MDPF_CANON).",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_COTREMEDIATION-S17",
    "project": "MDPF_COTREMEDIATION",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The publisher stamps the day's written_at onto a payload whose data did not advance, so every freshness signal keyed on written_at or object time reads current on stale data. Finding F-A adds the sibling: as_of_last itself advances over a frontier point that is null.",
    "evidence": [
      "comp-xray frozen on as_of_last and _provenance.source_keys, four scopes (this seat, 2026-10-01 07:3xZ): OK: CLEAN on all four -- the discriminating read the row's rule names, and it is clean on a series whose point was null on 11 of 28 recent trading days",
      "served cottonwood payload (this seat): point_class absent on 2026-08-20, 08-21, 08-31, 09-01 to 09-04, 09-08, 09-09, 09-23, 09-24, each a date present in dates[]",
      "investigation row MDPF_COTREMEDIATION-S17 (3.0.0_SA_CVO, 2026-08-26): the rule published to the reading seats that day",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_COTREMEDIATION_AC_GRADE_20261001.md @7bc5eb882b, finding F-A"
    ],
    "remedy": "P1: the frontier read on these keys also reads the class of the last point (point_class[-1] is measured), one more field on the existing call and not a monitor. Placed with finding F-A in MDPF_HEALGAP by CTO 103613.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-08-26T14:00Z"
    },
    "closed": false
  },
  {
    "id": "MDPF_COTREMEDIATION-S18",
    "project": "MDPF_COTREMEDIATION",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The specified trigger R2 already existed on the EventBridge Scheduler plane, which a rules listing cannot see; building it as a rule would have landed a dual trigger and brought back the daylight-saving drift the schedule was chosen to prevent.",
    "evidence": [
      "aws scheduler list-schedules --name-prefix cot-bd (this seat, 2026-10-01 07:5xZ): one schedule, cot-bd-session-daily-et, ENABLED",
      "aws events list-rules --name-prefix cot-bd: 0 rules; control, --name-prefix bd-asset returns bd-asset-dim-pipeline-trigger ENABLED, so the zero is a read of the rules plane and not a failed call",
      "investigation row MDPF_COTREMEDIATION-S18 (0.7.0_AE_CloudOps~Z): the seat built nothing and held R2 pending the spec's amendment",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_COTREMEDIATION_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "Done: no rule was built. Five weeks on there is one trigger, on the Scheduler plane.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.7.0_AE_CloudOps~Z",
      "at": "2026-08-27T15:08Z"
    },
    "closed": true
  },
  {
    "id": "MDPF_COTREMEDIATION-S19",
    "project": "MDPF_COTREMEDIATION",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Carries on the served global aggregate with no attributed mechanism. Two were filed (2026-07-29 and 07-30 carried from 07-27). The served payload now lists the carries itself, and 11 more fall after the repair: global serves Cottonwood's prior value on every day Cottonwood's point is absent.",
    "evidence": [
      "served global payload (this seat, 2026-10-01 07:4xZ): point_class since 2026-08-20 is measured 17, carried 11, on the same 11 dates where cottonwood reads absent; meta.cottonwood_carry lists the pairs, the two filed ones among them",
      "comp-keys partitions fact_model_assignment (this seat): no partition for 2026-08-31 to 09-04, 09-08, 09-09, 09-10, which accounts for seven of the eleven; for 08-20, 08-21, 09-23, 09-24 both silver tables hold a partition and the cause is unread",
      "CTO 103613, RULINGS batch 69 @6291fa70e5: F-A and S19 are placed in MDPF_HEALGAP; the four days with both partitions present go to 4.0.0_SA_CRO~X as a read-only trace; no backfill is ordered",
      "investigation row MDPF_COTREMEDIATION-S19 (0.7.0_AE_CloudOps~Z)"
    ],
    "remedy": "Placed in MDPF_HEALGAP (CTO 103613): the missing model-assignment partitions are that project's subject; the four days whose partitions exist get a read-only trace first. The mechanism of the two July carries is still unattributed and travels with it.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_COTREMEDIATION-S20",
    "project": "MDPF_COTREMEDIATION",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A local dry run pinned Cottonwood's slice to the last landed gold partition while the axis ran further, and two latent readers failed on the trailing absent value; the crash was read as a production hazard and a rollback was executed on it.",
    "evidence": [
      "investigation row MDPF_COTREMEDIATION-S21 (1.0.0_SA_CTO, 2026-09-22T17:45Z): both parts of S20's disarm condition met and measured that day (held)",
      "served global payload written by the 2026-09-30 13:50Z scheduled run (this seat, 2026-10-01): it holds carried points on 2026-09-23 and 2026-09-24 beside Cottonwood's absent ones -- the covered-but-valueless shape on which the fold's coherence gate refused in the dry run is built by the production run without a refusal",
      "git merge-base --is-ancestor 1465fd3f7d e8994f23af: yes -- the 09-11 guard is in the deployed gold build (mdpf-gold-lambda CodeSha256 7hI4flW5..., built from e8994f23af)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_COTREMEDIATION_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "Done: both readers pass on production vintage. The limit that a local dry run is not vintage-equivalent to production for Cottonwood stays stated in the row.",
    "owner": "0.7.0_AE_CloudOps~V",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "0.7.0_AE_CloudOps~V",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.7.0_AE_CloudOps~V",
      "at": "2026-09-22T17:45Z"
    },
    "closed": true
  }
]
```
