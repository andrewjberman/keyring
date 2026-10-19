# CTO ruling -- routing the opal-data-assets audit's defects (D1-D3, P1-P3, S1)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-19 ~17:1xZ.
**Source:** `4.0.0_SA_CRO~Z`'s `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_TOOL_AUDIT_OPAL_DATA_ASSETS_20261019.md`
@216dfc8144 (msg 36019), on Andrew-direct ~16:2xZ (@634d368d98).
**Governing text:** NFRA_MCPINDEX PRD v0.19 @7c42c0c743 (ADMITTED): FWD-23's routing arm with the defect classes `link`, `code`
and `display`, and FWD-24's `misrouted` FAIL class.

## As read

The audit read 32 tool-by-segment rows live: 15 PASS (3 with caveats), 1 mislabelled, 9 FAIL, 2 unreachable, 4 refused by
design, and 1 not run. The served bytes equal HEAD for every audited file.

## Routing (each owner's next round; nothing here is a hand fix)

| # | Defect | Class (v0.19) | Owner | Cut as |
|---|---|---|---|---|
| D1 | Orion, Eclipse and Commonwealth have no `fence_kind`, so every call refuses `firm_not_served`. Inflection and Cottonwood's Commonwealth have never answered. | code | NFRA_OPLGTW `2.0.0_SA_COO~O` | the round-47 FIRST cell; proof is one live call per vendor reading PASS |
| D2 | the Cottonwood Black Diamond `_date()` is ISO-only while the source writes MM/DD/YYYY, so transactions and fees always come back empty | code | NFRA_OPLGTW | round 47; proof is the test account's 2 S3 transactions returned |
| D3 | `client_resolve_account` keeps the first adapter's envelope and hides other vendors' refusals | code | NFRA_OPLGTW | round 47; per-vendor `source_keys` and denominator, with refused vendors listed by code |
| P1 | /gateway segment tables list every vendor's indexes for a tool | display | NFRA_MCPORTAL `2.0.0_SA_COO~MP` (page), with the breakdown handler in NFRA_OPLGTW | the page filters a segment's indexes to that segment's (vendor, firm); the handler supplies the pair per index |
| P2 | the catalog's `serves` disagrees with what each adapter answers (Schwab listed on `client_*` tools that can never reach it) | link | NFRA_MCPINDEX `2.0.0_SA_COO~MI` | round 23, inside FWD-23's routing arm: `serves` generated from the traced source set, with Schwab on `client_*` marked unreachable |
| P3 | the Schwab grant's account list is frozen: 7,559 granted against 7,690 in S3 (150 accounts, about $17.3M, outside every answer, the owner's included) | -- | **Andrew** | put to him; NFRA_OPLGTW applies whichever he picks |
| S1 | the 49F crosswalk and fee roles are stale (09-28), and so is the allocation profile (08-18) | -- | the 49F Black Diamond producer's owner | surfaced as a surprise row by the auditor; this seat does not seat a producer |

## Rules for the cuts

- Every D cell rides NFRA_OPLGTW's batched releases under its own never-widen ask.
  - D1 widens nothing for a principal: the data grant still gates every firm.
  - The ask states it, and states that client data stays master_admin until a per-firm grant shape exists (v3.14).
- The mask from Z-S407 (CVO condition C1) stays a named round-47 cell beside D1-D3.
- After each fix, FWD-24's battery and the FWD-23 routing script re-run on opal-data-assets. The CRO's hand-run is the first
  record, never the proof.
- The auditor files D1, D2, D3 and S1 as surprise rows in NFRA_OPLGTW's channel, with `disarm_owner` `2.0.0_SA_COO~O`. S1's
  row names its producer.

## Part 2 routing (2026-10-19 ~17:4xZ; audit part 2 @48c5806982, msg 36033)

Part 2 called 62 tools: 57 PASS (16 with a caveat) and 5 FAIL. All 16 spot-checks equal their source.

| Items | Class (v0.19) | Owner | Channel for the row |
|---|---|---|---|
| P4, P5, P6, P7 (size and projection: indent-blind 50 KB, whole-field nulling, no MDPF projection, uncapped discover) and H2 (`news_for_security` name fallback and zero reason) | code | NFRA_OPLGTW `2.0.0_SA_COO~O`, round 47 beside D1-D3 | NFRA_OPLGTW, `disarm_owner` `2.0.0_SA_COO~O` |
| H7, E4, P8 key, and the 4 routing mismatches (`harvest_get_published_analysis`, `etfs_get_positioning`, `etfs_get_security_reference`, `mdpf_get_security_classification`) | link | NFRA_MCPINDEX `2.0.0_SA_COO~MI`, round 23 routing arm | NFRA_MCPINDEX, `disarm_owner` `2.0.0_SA_COO~MI` |
| H1 (article mentions and chatter stopped 10-08), plus harvest posture and scores | producer, owned on dell1 (AMGT harvest) | relayed MSTR to MSTR (rule 32) | NFRA_OPLGTW row naming the producer; INERT here |
| E1 (49F ETF ownership from one Schwab master; DIVZ understated $1,673,459.07 across 17 accounts) | producer | the ETF ownership producer's owner, named in the row | NFRA_OPLGTW row; ARMED (a number Andrew reads is wrong) |
| security scanner (10-02), ETF classifications (09-30), capital-markets views (2026-01-09) | producer | each pipeline's owner, named in the row | NFRA_OPLGTW rows; INERT |
| E2, E3, E5, H3-H6, H8 | hygiene | at the battery's next round | none of their own; listed in the next battery record |

**For the 19:00Z session with Alyssa:** `portal_get_macro` (P5, all macro data nulled) and `portal_get_valuation` (P5, 420
bytes) are not demonstrated. Use one model-portfolio or AUA question that the part-2 matrix read as PASS.

## Part 3 routing (2026-10-19 ~19:1xZ; audit part 3 @df8a98cbed, msgs 36079 and 36080)

Part 3 called 54 tools (42 Microsoft 365 and 12 integrations): 38 PASS (6 with a caveat), 2 FAIL, 2 correct refusals and 12
NOT RUN. Parts 1-3 together cover 127 served tools.

| Items | Class (v0.19) | Owner | Row |
|---|---|---|---|
| Oversize replies from `search_files`, `search_site_files` and `ycharts_fund_series` | code | NFRA_OPLGTW, with Z-S413 (P4-P7) | fold into the Z-S413 row, no new row. This is now an availability fix: an uncapped reply is a load risk to the host |
| Y2: `ycharts_time_series` and `ycharts_risk_return_scatter` get a 403 and answer an empty series with no reason | code | NFRA_OPLGTW (YCharts integration). First read whether the 403 is an entitlement or an endpoint change; either way, the empty series must carry its reason | one NFRA_OPLGTW row |
| Y1 (`ycharts_snapshot_metrics` loses the symbol key), R1 (`opal_data_refresh_status` with an unknown id never reaches a terminal state), T1 (`poll_addressed_teams_messages` ignores `top`) | code | NFRA_OPLGTW | one NFRA_OPLGTW row for the three |
| The 8 send tools have no always-preview path | -- | not a defect. Andrew answered c5c2 YES (@65a05f6658): the FWD-24 battery exercises each sending tool with ONE real message to the tester's own mailbox or chat, read back. The battery covers it | no row |
| A1: Cottonwood's mail tenant is not a registered partner tenant, so a Cottonwood sender gets `asker_tenant_denied` from `opal_asker_query` | -- | Andrew: whether Cottonwood's tenant is registered for asker answers | open call on site Z's list |
