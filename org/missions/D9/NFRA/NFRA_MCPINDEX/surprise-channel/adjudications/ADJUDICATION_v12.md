# NFRA_MCPINDEX ROUND 17 -- L8 COMPILE + plausibility read

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-10-15 ~20:3xZ, on `2.0.0_SA_COO~MI` msg 34574
(`deliverables/2.0.0_SA_COO~MI/round17/L8_PACKET_ROUND17.md` @63f2ca93c6, read whole).

**Terminality.** All four orders are complete. MX-r-14 is live: EC2_MANIFEST `deployed_commit` c4c106aea1 at
2026-10-15T19:50:39Z. This seat re-ran round-close-check and it reads MAY-CLOSE. There are no judgment criteria.

**This seat's reads (~20:3xZ).** These are taken from the served catalog `c4c106aea1:.../refs/DATA_CATALOG.yaml`. This
session's opalgateway connection is still refused (429).
- 304 rows carry a `read_tool`.
- 304 of 304 carry a non-empty `nl_tags`. 44 carry `nl_tags_basis: inferred`.
- 24 silver rows carry a `firm`: 49financial 23, inflection 1.
- Every `firm` agrees with the row's own measured fork-key value. Seven SmartX rows sit at the shared
  `smartx/platform/silver/` prefix, but each measures "49 Financial Group (23,213 of 23,213)", a single-firm table.
- No row names another firm in its text.

**Round-10 to round-16 remediation Z-C-S57: MET, flipped REMEDIATED in REMEDIATION_v10 in this commit.** Its close was
"304 of 304 rows carry a non-empty nl_tags AND each landed group has one plain-words discover read returning its table
row". Tags read 304 of 304. Plain-words reads are recorded for every group:
- harvest (round 11-16);
- G5r and portal/ETFs (rounds 12-16);
- this round: a G2 client table (`opal_data_assets_silver_49f_dim_advisor_fee_role`, a gap, owner NFRA_OPLGTW, with its
  staleness and producer failure stated);
- this round: a G6 news table (five servable matches).

G4 has no table of its own: its delta rides G2's `client_get_allocation` (NFRA_OPLGTW v3.3).

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S59",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-15T20:34Z",
    "one_line": "FWD-22 grade: REALIZED on this project's side -- the one catalog is the table of contents at table grain (304 rows, every row tagged, every read_tool a deployed tool or null with its gap owner, retired rows never a target, a plain-words read per landed group); the tools that READ the G2 client rows are NFRA_OPLGTW's FWD-22, not this project's.",
    "class": "OBSERVATION",
    "spec_asserts": "FWD-22 (v0.11-v0.17): for one table per landed census group, opal_discover in plain words returns that table's catalog row (contract, nl_tags, read_tool naming a DEPLOYED tool); opal_describe returns its columns; a retired dataset is never a tool target.",
    "world_is": "Served catalog v0.5 at c4c106aea1: 304 rows, 304 tagged (44 inferred), a 99-tool index, 0 read_tools naming an undeployed tool (round 16 count; MX-c-20 adds 7 rows naming the six live OG-ap-20 tools). The retired-target rule is at integration.py:643-645. A plain-words read is recorded for each landed group (header). The G2 client rows answer as gaps with gap owner NFRA_OPLGTW: the catalog finds the table and says nothing reads it yet. That is this outcome's DONE WHEN, which is the index, not the reader. Bound: this seat read the bytes, not a live discover, this session.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "c4c106aea1:infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml, counted by this seat",
        "L8_PACKET_ROUND17.md @63f2ca93c6 section 2 (the G2 and G6 plain-words reads)",
        "infra/aws/ec2/EC2_MANIFEST.json deployed_commit c4c106aea1"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S60",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-15T20:34Z",
    "one_line": "Round 17 L8: the firm widening reaches only each firm's own rows (24 labels each equal the row's measured fork value; the issuer's 1,326-pair control reads 0 cross-firm and the host matrix equals the cut); the round's rows are DISMISSED; the 44 inferred tags GRADUATE as a quality item (mechanical n-grams).",
    "class": "OBSERVATION",
    "spec_asserts": "CTO ruling 2 / the never-widen pair: a firm principal sees its own firm's catalog rows and no other's; this seat's Z-C-S57 remedy allowed inferred tags derived from the row's own text.",
    "world_is": "Widening: 23 rows labelled 49financial and 1 inflection. Each label matches the row's own measured fork_keys.firm value; the seven SmartX rows are single-firm at 23,213 of 23,213 rows, and no row text names another firm. The issuer's difference control reads 221 rows x 6 principals, newly visible 24, leaks 0, and the host-run matrix sha equals the cut's. A visible catalog row reads no data, because data still needs its grant. Nothing widens a partner beyond its own rows. Inferred tags: the 44 are deterministic phrase fragments drawn from the row's own fields. Some are meaningful ('schwab account balances') and some are not ('opal harvest grain', 'v1 gold harvest bucket'). They meet the letter of the remedy and fall short of the plain-language intent. Rows Z-S120 (fixed live), Z-S121 (ranking, owner 2.0.0_SA_COO~O, pin relaxed), Z-W42-S1 and Z-W43/Z-W44 are ruled by MX-c-19 A1, MX-c-20 A2-A4 and the order records.",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-S120", "NFRA_MCPINDEX-Z-S121", "NFRA_MCPINDEX-Z-W42-S1",
      "NFRA_MCPINDEX-Z-W43-S1", "NFRA_MCPINDEX-Z-W43-S2", "NFRA_MCPINDEX-Z-W43-S3",
      "NFRA_MCPINDEX-Z-W43-S4", "NFRA_MCPINDEX-Z-W43-S5", "NFRA_MCPINDEX-Z-W43-S6",
      "NFRA_MCPINDEX-Z-W44-S1", "NFRA_MCPINDEX-Z-W44-S2", "NFRA_MCPINDEX-Z-W44-S3",
      "NFRA_MCPINDEX-Z-W44-S4", "NFRA_MCPINDEX-Z-W44-S5"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "c4c106aea1 DATA_CATALOG.yaml silver_datasets firm rows and fork_keys (this seat)",
        "L8_PACKET_ROUND17.md @63f2ca93c6 sections 1, 2 and 4 (f1.AC2 1,326 pairs, leaks 0; host matrix sha equal)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The widening is own-firm only on this seat's read and the issuer's control; the rows are ruled. The tag-quality gap graduates separately as Z-C-S61."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S61",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-15T20:34Z",
    "one_line": "The 44 inferred nl_tags are mechanical n-grams of each row's own fields ('opal harvest grain', 'v1 gold harvest bucket'), not natural-language tags a person would type; they meet Z-C-S57's letter, not Andrew's 'natural language tags' intent.",
    "class": "OBSERVATION",
    "spec_asserts": "Andrew-direct ~12:4xZ 2026-10-14: 'All of this should have tags and natural language tags associated'.",
    "world_is": "In the served catalog, 44 rows carry nl_tags_basis inferred. A sample of four shows each row's tags as 2- to 5-word fragments of its entity, layer and format. Some route ('schwab account balances') and some carry no meaning a user would ask with ('opal harvest grain'). Most of the 44 are harvest bronze and state layers, which few people ask about. That bounds the cost.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "c4c106aea1 DATA_CATALOG.yaml, 4 sampled inferred rows (this seat)"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~Z
