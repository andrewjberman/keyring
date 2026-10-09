# LGIC_ENFORCE -- round 20 remediations (dell1)

<sweep_watermark>2026-10-09T16:53Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T16:53:00Z. Graduated at ADJUDICATION_v3: 4 rows, all INERT (D1-W1-S1 disarmed).

```json
[
  {
    "id": "LGIC_ENFORCE-D1-W1-S1",
    "project": "LGIC_ENFORCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "lib/opal_naming.py census_judge() cards on (plane, name) alone and never re-grades a carded name, so cards carried forward outlive their RAISE: 121 of 478 r20 cards named names grade() could read. Disarmed by the issuer's close run @119661e0fc, which keeps a card only where its item still RAISES (in 478, kept 355, dropped 121, unmatched 2; CENSUS: COMPLETE 3701 judged + 359 carded).",
    "evidence": [
      "investigation row LGIC_ENFORCE-D1-W1-S1 (ARMED)",
      "org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/r20_close/CLOSE_CENSUS_R20.json (rc 0, cards_in 478, kept 355, dropped 121, matching no item 2)",
      "3.0.0_SA_CVO re-graded all 357 cards in org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/r20_close/NOT_JUDGED_R20_CLOSE.json at HEAD: 357 RAISE, 0 verdict"
    ],
    "remedy": "census_judge() re-grades every carried card and drops one whose name no longer RAISES, in the census itself rather than a close-time prune. Close when: a census run with a planted stale card drops it and the report's carded count equals the names that RAISE",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v21",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v21"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": "2026-10-09T16:53:00Z"
    },
    "closed": false
  },
  {
    "id": "LGIC_ENFORCE-D1-S1",
    "project": "LGIC_ENFORCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "grade() does not read infra/logic/registry/name_rulings.json (0 mentions in lib/opal_naming.py), so three names with ruling rows still RAISE and are carded: calculated-group (R1.f), astn/kimi/api-key (R1.c), restricted-prefix-get-put-list (R1.f).",
    "evidence": [
      "investigation row LGIC_ENFORCE-D1-S1",
      "3.0.0_SA_CVO read: the three names are in name_rulings.json; grade() at HEAD raises on each with the rule named"
    ],
    "remedy": "Rule whether grade() or the census reads name_rulings.json. Close when: the ruling is recorded and, if adopted, the three names carry verdicts in the next census",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v21",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v21"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "LGIC_ENFORCE-D1-S2",
    "project": "LGIC_ENFORCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "lib/tests/test_opal_naming_scope.py fails on the trunk: 'etfs-rivalfunds: the generated role name is not counted at its json line' (826 assertions, 1 failure), from ETFS_RIVALS' change to that root, not LGIC_ENFORCE's.",
    "evidence": [
      "investigation row LGIC_ENFORCE-D1-S2",
      "3.0.0_SA_CVO ran python lib/tests/test_opal_naming_scope.py at box/dell1 HEAD: FAIL etfs-rivalfunds ..., SCOPE-TEST ok=False assertions=826"
    ],
    "remedy": "ETFS_RIVALS' issuer counts the generated role name or moves the test's case. Close when: SCOPE-TEST ok=True on the trunk",
    "owner": "2.0.0_SA_COO~V1",
    "round": "v21",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~V1",
      "round": "v21"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~V1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "LGIC_ENFORCE-D1-W2-S152",
    "project": "LGIC_ENFORCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "On the live commit gate a planted per-firm PATTERN name (investor-reporting/directory as an os.environ.get default) graded nothing: 'NAMING-GATE: PASS 0 graded', no skip line. Which of three causes (PATTERN skipped, the env-default literal, no new stored name) applies is unmeasured.",
    "evidence": [
      "investigation row LGIC_ENFORCE-D1-W2-S152",
      "git: a09b284984 is reachable only from qa/lgic-enforce-r20-s12 (never merged)"
    ],
    "remedy": "Isolate the cause with one plant per cause, then make the gate grade a PATTERN name or print a skip line for it. Close when: a planted PATTERN name prints a NAMING line (graded, or skipped with its reason)",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v21",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v21"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  }
]
```
