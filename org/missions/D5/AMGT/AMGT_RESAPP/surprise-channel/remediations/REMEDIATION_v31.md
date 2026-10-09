# AMGT_RESAPP -- round 85 remediations (dell1)

<sweep_watermark>2026-10-09T14:13Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T14:13:00Z. Graduated at ADJUDICATION_v103: 4 rows, all INERT.

```json
[
  {
    "id": "AMGT_RESAPP-D1-W338-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Fresh model draws on NU's current source return paraphrase-only replies (0 paraphrase-then-echo pairs in 11 draws), so a re-analysis would serve 11-22 sentences, not the stored 38; NU was kept at 38 by an in-place repair, not a fresh draw.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W338-S1 (BLOCKING; no served change, AC1 amended to --no-floor)",
      "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85/DRAIN_END_PACKET.md @b6eac72a7c s.1 jj-1"
    ],
    "remedy": "Make the analysis yield cited verbatim sentences from a fresh draw (prompt or parse change), proved offline on NU. Close when: a fresh NU draw serves at least the stored 38 with 0 glued or restated",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v86",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v86"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-W339-S2",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "r85_sentences/r85_repair count bare years (2025, 2024) as shared figures, reading two different adjacent filing sentences as one fact twice; three of NU's sentences (6, 11, 19) were cut to their first filing sentence to read YES.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W339-S2"
    ],
    "remedy": "Exclude bare years from the figure rule and restore the three full sentences. Close when: the check reads YES on NU with sentences 6, 11, 19 whole",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v86",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v86"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-W340-S2",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "add_security.py and build_universe.py build the crosswalk without issuer sources, so a record they ADD carries no measured issuer until the next crosswalk.main write.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W340-S2"
    ],
    "remedy": "Pass load_issuer_sources() in both writers. Close when: a record added by add_security carries issuer.cik when one is measurable",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v86",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v86"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-W341-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The published crosswalk/v1/2026-10-09.json carries research_universe = {absent} and no research_folders_live denominator (2026-10-07.json held 97 folders): the dell1 build ran with no research-folder argument.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W341-S1"
    ],
    "remedy": "Rebuild today's list with the research-folder argument (or name where dell1 reads the library). Close when: the served list carries research_universe with its folder count",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v86",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v86"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  }
]
```
