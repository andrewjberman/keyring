# POSN_ASTTAX round 5 - the single L10 slug

From `3.0.0_SA_CVO~Z` to `1.0.0_SA_CTO~Z`. Release basis: CTO reported round-5 L7 closed at `@0803788f29` with nine of nine orders complete. The CVO proof check records nine valid proof-of-spec instances, and `ADJUDICATION_v7.Z.md` dispositions every remaining investigation original. No portal, deployment, promotion, or S3 write is authorized by this slug.

The prior round-4 slug remains the inherited remediation register. This round adds the three open items below for the CTO's round-5 analysis: the presence-driven Positioning Summary polish, the corrected Satellites footer provenance, and the unserved per-holding Satellites measures. The last item is decomposition-invalidating until its PRD addendum and backend/frontend cell are served.

```json
[
  {
    "id": "POSN_ASTTAX-Z-C-S142",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "PositioningSummary renders all five asset-class legend and detail rows even when the current view has zero exposure.",
    "evidence": ["org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/adjudications/ADJUDICATION_v7.Z.md#POSN_ASTTAX-Z-C-S142"],
    "remedy": "Derive one presence set from the current render's displayed books and apply it to legend, rows, count, and bars while preserving ASSET_CLASSES order and colors; verify Models and post-retag Satellites.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v5",
    "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO~Z", "round": "v5"},
    "closed": false,
    "disarm": {"state": "ARMED", "owner": "1.0.0_SA_CTO~Z", "at": "2026-09-15T02:45:00Z"}
  },
  {
    "id": "POSN_ASTTAX-Z-C-S143",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The Satellites Positioning Summary footer displays the stale Bloomberg 2026-09-11 date/source while the served holdings are Black Diamond holdings as of 2026-09-14.",
    "evidence": ["org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/adjudications/ADJUDICATION_v7.Z.md#POSN_ASTTAX-Z-C-S143"],
    "remedy": "Bind footer date and source to the served holdings artifact metadata in the same frontend polish cell as the presence filter.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v5",
    "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO~Z", "round": "v5"},
    "closed": false,
    "disarm": {"state": "ARMED", "owner": "1.0.0_SA_CTO~Z", "at": "2026-09-15T02:45:00Z"}
  },
  {
    "id": "POSN_ASTTAX-Z-C-S144",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Satellites Holdings Breakdown receives no per-holding characteristics or performance values; characteristics.json contains satellite aggregates and contributor lists only.",
    "evidence": ["org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/adjudications/ADJUDICATION_v7.Z.md#POSN_ASTTAX-Z-C-S144"],
    "remedy": "CTO PRD addendum and next decomposition must specify B4 per-ticker measures, adapter attachment without arithmetic, and an explicit source or omission for MC, Active, and Credit.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v5",
    "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO~Z", "round": "v5"},
    "closed": false,
    "disarm": {"state": "ARMED", "owner": "1.0.0_SA_CTO~Z", "at": "2026-09-15T02:45:00Z"}
  }
]
```
