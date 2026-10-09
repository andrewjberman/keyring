# MDPF_SECCLASS -- rounds 13-15 remediations (dell1)

<sweep_watermark>2026-10-09T08:44Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T08:44:00Z. Graduated at ADJUDICATION_v11: 14 rows, all INERT (D1-S14 disarmed at 01:39:28Z when its one live entry closed).

```json
[
  {
    "id": "MDPF_SECCLASS-D1-S14",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "deploy_ledger.py has no state for an entry opened, never started and held on a sovereign gate before its first apply, so it ages into a RED that reads as half-landed. ARMED at filing; DISARMED for its one live case: the e65b entry ran and CLOSED at 01:39:28Z, before its 01:5xZ window.",
    "evidence": [
      "org/critical_paths/change_management/20261008T0123Z_secclass-e65b-namekey-deploy-s-20261007_deploy_completion.md: CLOSED -- nothing stranded -- closed 20261009T013928Z",
      "investigation row MDPF_SECCLASS-D1-S14 (BLOCKING, ARMED, disarm_owner 0.7.0_AE_CloudOps~SD)"
    ],
    "remedy": "The ledger tool's owner adds a NOT-STARTED/PRE-APPLY hold class (zero apply legs landed), the mirror of HELD. Close when: hold accepts an entry with no apply leg ever closed and check --red no longer flags it",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v16"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": "2026-10-09T01:39:28Z"
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-S15",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ai_leg_verify read_unresolved anchors on startswith('UNRESOLVED '), so a wrapper that timestamps stdout makes every reason line invisible and the close reads refused_final=0 with rc 0. Disarmed for e49 (stripped sidecars @f81718aa17); the trap stays live for any wrapped graded runner.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S15 (BLOCKING, INERT)",
      "e49 ledger CLOSED 6c3675723a on the stripped logs (packet)"
    ],
    "remedy": "The grader refuses when absent keys exist but the logs yield zero reason lines (the row's remedy iii). Close when: a prefixed log makes the grader print a refusal, not refused_final=0",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v16"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": "2026-10-08T21:36:00Z"
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-S8",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "49financial SmartX-path nodes carry security_id namespace TICKER/VENDOR, never CUSIP, so the CUSIP:<value> canonical row is never asked and e56's acceptance 1 is NOT MET on the served Holdings fire.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S8",
      "git log a2a06e7663 / 358f1cf2ee (dell2 rulings: ~M Holdings workstream closed; e56 COO half to ~P2)"
    ],
    "remedy": "Route to the dell2 owner of the 49F Holdings builder (IRPT_BCKEND ~P2): diagnose the mesh-merge identity and serve CUSIP-row classes. Close when: the five tabled 49F moves serve through their CUSIP rows on a served fire",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v16"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-S9",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "BD and COT client concentration served multi_asset after the six-class switch. BD is healed (e75, 04:00Z fire). COT's twin (SGIIX on z09305621/z09305679) waits on SC-e-67 leg G at the 2026-10-09 10:30Z COT run.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S9",
      "git log 9739408e8f (cot C_06 deployed alone, leg G at the 10:30Z COT fire)"
    ],
    "remedy": "Read e67 G. Close when: opal-data-cot platinum/clients/*/concentration.json serve 0 multi_asset after the 10:30Z run",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v16"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-W57-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "COT C_06 validates the pct sum over every class present but publishes only MIX_ASSET_CLASSES, so a date holding a class outside the list is published with a mix below 1.0 and no skip.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-W57-S1",
      "SC-e-67 (cot C_06 retired class) deployed 9739408e8f; G at 10:30Z"
    ],
    "remedy": "Confirm at e67 G whether the healed dates' mix sums reach 1.0; otherwise C_06 skips or flags a date whose published classes do not cover its total. Close when: no published COT date has a mix sum below 0.999 without a flag",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v16"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-W65-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "C_06's retained-entry reclass recomputes the mix from the top-10 holdings the envelope keeps, so 15 of 105 healed BD dates keep a mix sum below 0.999 (up to 0.0476 short); only a C_06 FULL build closes it.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-W65-S2",
      "e75 half's 'Known limit'"
    ],
    "remedy": "Decide whether to run a C_06 FULL build under its own pair or accept the limit on the record. Close when: the decision is recorded and, if built, the 15 dates sum to 1.0",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v16"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-W66-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two canonical rows disagree for AMERICAN CENTURY ULTRA INV: the CUSIP: row says equity, the NAME:: row fixed_income; the chain serves equity.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-W66-S1"
    ],
    "remedy": "The row owner settles the class and corrects the wrong row. Close when: the CUSIP: and NAME:: rows agree",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v16"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-W66-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The COT lib copy has no name path (classify_position takes no name; no NAME:: read), so a COT position the ticker and CUSIP rows do not place stays unclassified whatever NAME:: rows exist.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-W66-S2",
      "data/cot/scripts/gold/lib/etf_classifier.py:137-158"
    ],
    "remedy": "Measure COT's unclassified share a NAME:: row would place; if material, port SC-e-76's name lookup to COT under a pair. Close when: the measurement is recorded and, if ported, COT serves it",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v16"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-W66-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "32 BD group-A securities carry a ticker with no row; the rule 'a ticker is never changed' leaves them unclassified, and AC1's 795 of 796 called with a blank ticker, so it did not exercise them.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-W66-S3"
    ],
    "remedy": "Spec call: whether a ticker-no-row position falls back to its NAME:: row. Close when: ruled and, if yes, the 32 serve classified",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v16"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-S4",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "deploy_ledger.py check grades age/window/PAST-WINDOW/HELD-STALE from this device's checkout, so a foreign-authored entry reads PAST-WINDOW on fetch vintage, indistinguishable from a real overrun.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S4"
    ],
    "remedy": "The ledger tool prints the author device and the local fetch time beside any verdict on a foreign-authored entry. Close when: a foreign entry's verdict carries both",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v16"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-S18",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "seed-etf-classifications.py --dry-run prints 'OK: Seeding complete! Items written : N' while it writes nothing.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S18"
    ],
    "remedy": "The script's summary says DRY RUN and 'would write N'. Close when: a dry run's last lines claim no write",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v16"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-S19",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "test_deploy_tool_ships_the_shared_modules_beside_the_gold_files pins the retired ship-everything rule and fails at HEAD for every BD gold candidate.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S19"
    ],
    "remedy": "The deploy tool's lane rewrites the test to the named-file rule. Close when: the BD gold suite passes whole at HEAD",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v16",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v16"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "MDPF_SECCLASS-D1-S20",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "proof-of-spec-check's artifacts_produced/kind enum has no member for rows written to a DynamoDB table, and only s3_object skips git resolution, so a table-write DEPLOY order cannot declare its product truthfully.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S20"
    ],
    "remedy": "The schema owner brings a value-enum proposal (rule 24 four-postulate record) for a table-rows kind. Close when: a table-write instance validates with its true substrate",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v16"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-S22",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "crossbox-deploy-check.py's OPEN-DEPLOY limb lists worktrees, then ls-trees each, non-atomically; a worktree removed in between reads 'not readable, not clear'. INERT in WARN mode; it arms when the mode flips to ENFORCE.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S22"
    ],
    "remedy": "The tool treats rc=128 on a worktree no longer listed as PRUNED and re-lists once. Close when: a removed worktree no longer yields a STOP. Must land before the limb goes to ENFORCE",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v16"
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
