# NFRA_MCPINDEX ROUNDS 12-16 -- L8 COMPILE + plausibility read

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-10-15 ~08:3xZ, on `2.0.0_SA_COO~MI` msg 34401
(`deliverables/2.0.0_SA_COO~MI/round16/L8_PACKET_ROUNDS12_16.md` @e9c5a5e893, read whole).

**Terminality.** Every order of rounds 12-16 is complete. round-close-check reads MAY-CLOSE (this seat re-ran round 16).
There are no judgment criteria. EC2_MANIFEST `deployed_commit` is 1b18b94979 (2026-10-15T07:54:33Z).

**This seat's reads (~08:2xZ).** This session's opalgateway MCP connection is refused (429 rate_limited), so no live
discover was run here. The second instrument is the served catalog bytes:
- `git show 1b18b94979:infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, version 0.5. The issuer's r13.AC4 reads
  host md5 = tree md5.
- `s3://opal-data-portal-v2/platinum/mdpf/global/aum-metrics.json`.
- `opal_discover/integration.py:643-672` at 1b18b94979.

**Round-11 remediation Z-W34-S3 (depth per tool): MET, flipped REMEDIATED in REMEDIATION_v9 in this commit.** Its close
was "each of the 11 (a) tools reads a depth claim matching its case, with 'absent' on none whose artifact carries a
date". The served `tool_index` gives:
- 5 portal tools measured: `body-field` for aggregate_aua and aum_metrics, `snapshot-asof` for positioning,
  account_distribution and model_benchmarks.
- `blackdiamond_list_fees` inferred, as a live-queried window (2020-03-06..2026-10-13).
- 5 query tools `per-link`: gateway_query_catalog, opal_asker_query and the three schwab_* tools.
- 0 absent.
- This seat's own read of aum-metrics confirms the measured value: `total.series_start` = 2024-11-01, with 9 dated
  values running 2024-11-01..2026-10-14.
- **A correction to this seat's own round-11 row:** it said aum-metrics "carries a quarter series back to 2025-12-31".
  That read only the `dates` quarters and missed `series_start`. The finding's direction stood; its value was
  understated.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S56",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-15T08:29Z",
    "one_line": "FWD-20 grade: REALIZED -- the served partition holds (93 of 93, the issuer's live r13.AC2) and every one of the 11 (a) tools carries a depth claim matching v0.10's case, read from the served catalog by this seat, with the aum-metrics value confirmed against its served object.",
    "class": "OBSERVATION",
    "spec_asserts": "FWD-20 (v0.10): N served tools partitioned (a)/(b)/(c) summing to N; each (a) tool's depth read at answer time from the served artifact (first-date field or series first element; a snapshot's as-of; a live-queried row's served window inferred; absent only where no artifact carries a date).",
    "world_is": "Served tool_index at 1b18b94979: 93 tools. Of the 11 (a) tools, 5 are measured, 1 inferred and 5 per-link, with 0 absent (cases listed in the header). The second instrument is this seat's read of aum-metrics.json: total.series_start is 2024-11-01, equal to the catalog's measured value. This is the third round of the depth outcome. Rounds 10 and 11 passed checks that sampled one tool; this round's c10.AC3 graded 17 of 17 measured, with anchors 2 of 2.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "1b18b94979:infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml tool_index (this seat)",
        "aws s3 cp platinum/mdpf/global/aum-metrics.json (this seat, ~08:2xZ): total.series_start 2024-11-01",
        "L8_PACKET_ROUNDS12_16.md @e9c5a5e893 section 1 (r13.AC2 93 of 93, AC3 11 of 11)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S57",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-15T08:29Z",
    "one_line": "FWD-22 grade: NOT YET REALIZED -- the catalog IS at table grain (304 rows: 221 silver, 78 harvest, 5 portal; every read_tool names a deployed tool; retired rows are never a tool target), but 44 of 304 rows carry an EMPTY nl_tags list, and the per-group plain-words discover is shown live for harvest, G5r and portal only, not for G2 client or G6 news.",
    "class": "OBSERVATION",
    "spec_asserts": "FWD-22 (v0.11-v0.16): for one table per landed census group, opal_discover in plain words returns its table row (contract, nl_tags, read_tool naming a DEPLOYED tool); a retired dataset is never a tool target; Andrew: 'All of this should have tags and natural language tags associated'.",
    "world_is": "Served catalog v0.5 has 304 rows that carry read_tool. Every read_tool names one of the 93 deployed tools (0 undeployed). Three rows are marked retired: harvest_publication_links_v1, harvest_publications_v1 and harvest_research-dossier. Each still names a read_tool, but integration.py:643-645 empties the target for `retired: true` ('a RETIRED table is never a tool target'), so none is offered. 44 rows carry nl_tags = [] (key present, list empty): 32 of 78 harvest rows (the bronze and state layers), 7 of 221 silver (blackdiamond_fees, the schwab_dim_* rows, two smartx drafts) and 5 of 5 portal_datasets rows. Those rows still route by example_questions, but they do not carry the tags Andrew named. The live per-group proof the packet shows covers the harvest (opal_describe harvest_article_sentiment), G5r (the rival-fund question) and portal (etfs positioning) groups. A G2 client table and a G6 news table read by plain words are not shown, and this seat cannot run discover this session.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "1b18b94979 DATA_CATALOG.yaml silver_datasets/harvest_datasets/portal_datasets, counted by this seat",
        "1b18b94979:infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py:643-672",
        "L8_PACKET_ROUNDS12_16.md @e9c5a5e893 section 2"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S58",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-15T08:29Z",
    "one_line": "Rounds 12-16 L8: the round rows DISMISSED -- MX-c-16's three corrections widen nothing (the difference control this seat asked for read 390 pairs, deny->serve 0); Z-W39-S1's firm-bearing prose reaches no partner (all 25 such rows are firm-scoped with no firm field, so catalog_gate refuses every firm principal); the drain-time and procedure rows are ruled or resolved.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the rounds; this seat's R16 pre-issue read (@2a8a025031) asked for a per-firm difference control printing deny->serve.",
    "world_is": "MX-c-16 carried both of this seat's conditions: a difference control over 390 firm-key pairs, deny->serve 0, serve->deny 1 (the aum row, Opal-internal). (c) cannot have widened what that control proves did not move. Z-W39-S1: in the served catalog, 25 silver rows hold a spaced firm-alias string in fork_keys.firm.values. All 25 have firm_scope_rule firm-scoped, no `firm` field and no firm_resolution, so catalog_gate:117-120 refuses them to every firm principal (row firm '' never equals a firm). They are visible to Opal-internal only, and no partner reads another firm's name. Z-W36-S1 and Z-W36-S5 (the loader refused the 39 eleven-field rows) are resolved: MX-c-12's 78 rows replaced them, and the served catalog holds 78. Z-S118 (the first release rolled back on r13.AC2) and Z-S119 (AC2 could not pass on the base) are ruled by MX-r-13 A5. The re-cut passed AC1-AC4, and both causes were the issuer's. Z-W38-S9 to S11 are ruled by MX-c-14 A7. Z-W38-S16 is benign (the gate grades only added literals). Z-W40 and Z-W41 are covered by the MX-c-16/17 records. The remaining W35-W41 rows are worker notes (gate behaviour, denominators, status-flip paths, suite flakes) carried to the slug's cut-template line.",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-W35-S1", "NFRA_MCPINDEX-Z-W35-S2", "NFRA_MCPINDEX-Z-W35-S3", "NFRA_MCPINDEX-Z-W35-S4",
      "NFRA_MCPINDEX-Z-W36-S1", "NFRA_MCPINDEX-Z-W36-S2", "NFRA_MCPINDEX-Z-W36-S3", "NFRA_MCPINDEX-Z-W36-S4",
      "NFRA_MCPINDEX-Z-W36-S5", "NFRA_MCPINDEX-Z-W36-S6", "NFRA_MCPINDEX-Z-W36-S7",
      "NFRA_MCPINDEX-Z-W37-S1", "NFRA_MCPINDEX-Z-W37-S2", "NFRA_MCPINDEX-Z-W37-S3", "NFRA_MCPINDEX-Z-W37-S4",
      "NFRA_MCPINDEX-Z-W37-S5", "NFRA_MCPINDEX-Z-W37-S6", "NFRA_MCPINDEX-Z-W37-S7",
      "NFRA_MCPINDEX-Z-W38-S1", "NFRA_MCPINDEX-Z-W38-S2", "NFRA_MCPINDEX-Z-W38-S3", "NFRA_MCPINDEX-Z-W38-S4",
      "NFRA_MCPINDEX-Z-W38-S5", "NFRA_MCPINDEX-Z-W38-S6", "NFRA_MCPINDEX-Z-W38-S7", "NFRA_MCPINDEX-Z-W38-S8",
      "NFRA_MCPINDEX-Z-W38-S9", "NFRA_MCPINDEX-Z-W38-S10", "NFRA_MCPINDEX-Z-W38-S11", "NFRA_MCPINDEX-Z-W38-S12",
      "NFRA_MCPINDEX-Z-W38-S13", "NFRA_MCPINDEX-Z-W38-S14", "NFRA_MCPINDEX-Z-W38-S15", "NFRA_MCPINDEX-Z-W38-S16",
      "NFRA_MCPINDEX-Z-W39-S1", "NFRA_MCPINDEX-Z-W39-S2", "NFRA_MCPINDEX-Z-W39-S3",
      "NFRA_MCPINDEX-Z-W40-S1", "NFRA_MCPINDEX-Z-W40-S2", "NFRA_MCPINDEX-Z-W40-S3",
      "NFRA_MCPINDEX-Z-W41-S1", "NFRA_MCPINDEX-Z-W41-S2",
      "NFRA_MCPINDEX-Z-S118", "NFRA_MCPINDEX-Z-S119"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L8_PACKET_ROUNDS12_16.md @e9c5a5e893 sections 1 and 4",
        "1b18b94979 DATA_CATALOG.yaml silver_datasets fork_keys census (this seat): 25 spaced firm values, all firm-scoped, 0 with a firm field",
        "infra/aws/ec2/opal-gateway/app/graphql_plumbing/catalog_gate.py:117-120",
        "deliverables/3.0.0_SA_CVO~Z/R16_MX-c-16_PRE-ISSUE_READ_20261014.md @2a8a025031"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Ruled by the issuer's amendments and sound on this seat's reads, resolved at the drain, or a worker note carried to the cut template."
  }
]
```

-- 3.0.0_SA_CVO~Z
