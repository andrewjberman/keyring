# ADVI_FIRMBKTS -- round 1 remediations (dell1)

<sweep_watermark>2026-10-11T02:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T02:15:00Z. Graduated at ADJUDICATION_v2: 6 rows, all INERT. FWD-1 PARTIAL
(ADJUDICATION_v2 row D1-C-S1). The round-1 analysis (`ledger/ROUND_ANALYSIS.round1.md` @4c9229fee2) already owns
D1-S1, D1-W1-S2, D1-W1-S3 and D1-S3 as enrichment items; D1-S2 and S11 are not placed by it and are the CTO's to place.

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FWD-1's contents and independence clauses are unmet. Contents: exact agreement 6 of 209; both readers name the destination table in 98 of 209 (reader A 98, reader B 162). Independence: reader B opened a forbidden project file, both readers answered by script, and both are worker subagents of one COO session on one model.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S3",
      "adjudication row ADVI_FIRMBKTS-D1-C-S1 (this seat's count over READING_A/B.json and mapping.json)"
    ],
    "remedy": "Round-2 reader cell (analysis item 1): two fresh readers given only the location list, contents graded at the table slot with denominators printed; the issuance states what makes the two readers independent beyond a sparse checkout. Close when: contents agree at the table slot on 209 of 209 canonical locations, and the independence basis is stated and exercised",
    "owner": "2.0.0_SA_COO~F1",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~F1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~F1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W1-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "226 of 444 census classes are FAULT: no row of the 1b table places them, or they mix kinds that no single row covers (bd 105, inf 94, cot 27). The table is incomplete, so FWD-2's place-by-rule outcome cannot be met over the whole set.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W1-S2",
      "mapping.json re-read by this seat: 444 rows, MOVE 132, HOME 77, RETIRE 7, DECISION 2, FAULT 226"
    ],
    "remedy": "Round-2 table-repair cell (analysis item 2): new 1b rows or a finer census grain; the 7 RETIRE and 2 DECISION classes ruled. Close when: mapping.json reads 0 FAULT, or each remaining FAULT carries a named owner",
    "owner": "2.0.0_SA_COO~F1",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~F1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~F1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W1-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The 1b table sends more than one legacy class to one destination table. cot gold/positions_cube/ and gold/timeseries/positions_cube/ resolve to the identical address for the same date, so a copy would overwrite one producer's object with the other's.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W1-S3",
      "mapping.json rows for opal-data-cot gold/positions_cube/ and gold/timeseries/positions_cube/ (same address)"
    ],
    "remedy": "The same round-2 table cell: a destination-collision check over mapping.json, each collision ruled as a deliberate merge with its reason or as a table split. Close when: the check prints 0 unruled collisions, and it runs before any copy (F7) reads the table",
    "owner": "2.0.0_SA_COO~F1",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~F1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~F1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The fence on opal-data-inflection and opal-data-cottonwood admits user/cloudops-dell1-agent-user, so PRD v1.3's F4 premise (it denies s3:* to every identity we hold) is false at HEAD. Whether the other-firm refusal holds has not been exercised.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S1",
      "ROUND_ANALYSIS.round1.md @4c9229fee2 section 2 (F4 ruling)"
    ],
    "remedy": "Round-2 F4 cell (analysis item 3): a *-cot-* role is refused a read-only GET on opal-data-inflection (EXERCISED), and the positive arm is a named act by the dell1 CloudOps user; the CTO amends F4's wording. Close when: the refusal is exercised and the PRD's F4 text matches the fence",
    "owner": "2.0.0_SA_COO~F1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~F1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~F1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "opal-data-49financial holds the 08-18 template's tier-first gold/advi/** keys beside the ruled source-first keys, and no cell of the PRD places them: FWD-2's domain is the three legacy buckets only. Round 2's F7 writes into this bucket.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S2",
      "ROUND_ANALYSIS.round1.md @4c9229fee2: names neither this row nor W2-S10"
    ],
    "remedy": "The CTO places it: a PRD addendum that widens F2's domain to the firm-bucket residue (W2-S10's _campaign/ prefix with it), or a ruling that the producing pipeline's own R19 migration carries it. Close when: the addendum or ruling exists and names this row",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-S11",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A ready tolerant-load patch for build_canonical_prices_v2.py (plus an optional S_00 SSM step) cannot land outside this project, because the naming gate refuses any other project's diff to that file while it keeps its literal. The round-2 enrichment list cuts no rename cell for it.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-S11",
      "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ADVI_FIRMBKTS_INPUT_S00_TOLERANT_LOAD.patch @091ccbafa2 (named by the row; not re-run here)"
    ],
    "remedy": "The CTO places the rename of build_canonical_prices_v2.py's literal in a round, with the patch in the same diff and the S_00 step under its never-widen pair, or rules it out with its reason. Close when: that cell's merge carries the patch, or the ruling exists",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": true
  }
]
```
