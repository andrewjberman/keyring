# NFRA_MCPINDEX -- surprise channel, REMEDIATION v10 -- THE ROUNDS 12-16 SLUG

Author: 3.0.0_SA_CVO~Z. Round: v10 (rounds 12-16). Fabric: site-z. Recorded: 2026-10-15 ~08:3xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Rounds 12-16 are all complete and read MAY-CLOSE, served at 1b18b94979 with catalog v0.5. L8 is at
`adjudications/ADJUDICATION_v11.md`. This session's opalgateway connection is rate-limited, so the second instrument
was the served catalog bytes, plus one served S3 object.
- **FWD-20: REALIZED** (Z-C-S56). All 11 index-linked tools carry a depth claim matching their case:
  - 5 measured, 1 inferred, 5 per-link, 0 absent;
  - aum-metrics' `series_start` of 2024-11-01 was confirmed against the served object.
  - Z-W34-S3 is flipped REMEDIATED.
- **FWD-22: at table grain, but NOT YET REALIZED** (Z-C-S57, below):
  - 304 rows; every `read_tool` names a deployed tool; retired rows are never a tool target.
  - 44 rows carry an empty `nl_tags`.
  - The live plain-words read is shown for harvest, G5r and portal only, not for G2 client or G6 news.
- **MX-c-16 widened nothing.** The difference control read 390 firm-key pairs, deny->serve 0.
- **Z-W39-S1's firm prose reaches no partner.** All 25 such rows are firm-scoped with no `firm` field, so the gate
  refuses every firm principal.
- **The first release rolled back and the re-cut passed** (Z-S118, Z-S119, ruled).

**For the analysis:**
1. **Z-C-S57:** tags on the 44 rows, and one plain-words discover read for a G2 table and a G6 table.
2. **The 25 firm-scoped silver rows have no `firm` field,** so the gate refuses even their OWN firm. That is not a
   leak, but those rows serve Opal staff only until the field is set.
3. **Readers for the gap rows** (rival-fund, client, ETFs) are NFRA_OPLGTW's. `json-tiered/` waits on Z-S114.
4. **The lane gate refuses this COO's catalog and registry writes** (MX-c-14 A8-A13). This belongs on one line of the
   cut template.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S57",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "44 of 304 served catalog rows carry nl_tags = [] (32 of 78 harvest: the bronze and state layers; 7 of 221 silver; 5 of 5 portal_datasets), against Andrew's 'All of this should have tags and natural language tags associated'; and FWD-22's per-group plain-words discover is shown live for harvest, G5r and portal only",
    "evidence": [
      "3.0.0_SA_CVO~Z count of 1b18b94979 DATA_CATALOG.yaml, ~08:2xZ 2026-10-15",
      "L8_PACKET_ROUNDS12_16.md @e9c5a5e893 section 2"
    ],
    "remedy": "Fill nl_tags on the 44 rows. Where a census contract supplied none, derive the tags from the row's own business_meaning and example_questions, and mark them inferred. Run one plain-words opal_discover per landed census group not yet shown (at least one G2 client table and one G6 news table) on the served host. Closes when 304 of 304 rows carry a non-empty nl_tags, with the denominator printed, AND each landed group has one plain-words discover read returning its table row.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v10",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v10"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
