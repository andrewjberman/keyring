# NFRA_MCPINDEX ROUND 18 (ASSETS) -- L8 COMPILE + L9 read of the finish line

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-10-16 ~13:2xZ, on `2.0.0_SA_COO~MI` msg 35004
(`deliverables/2.0.0_SA_COO~MI/round18/L8_PACKET_ROUND18.md` @0afc0f3a19, read whole). The RESEARCH workstream's section
(`2.0.0_SA_COO~MI2`, `RESEARCH_SECTION_L10.md` @7e364e6a8e) reports on its own and is not graded here.

**Terminality:** 11 of 11 orders complete, and round-close-check MAY-CLOSE (issuer). MX-r-15 is LIVE at `deployed_commit` `38fe44d5cb` (v3).

## This seat's reads of the live catalog (`38fe44d5cb:infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, parsed whole)

- **Rows:** `silver_datasets` 197 + `portal_datasets` 5 + `harvest_datasets` 78 = **280**. `bucket` is set on 280 of 280.
  - opal-data-assets 127, harvest 78, portal-v2 34, etfs 27, bd 9, dynamodb 3, mdpf 1, news-v2 1.
- **Vendor and firm:** set on **136 of 136** opal-data-assets/opal-data-bd rows.
- **Read tools:** `read_tool` on **188** rows, naming **61** distinct tools. **0** names a tool absent from the live
  `tool_index` (127 tools).
- **No read tool:** **92** rows, all `silver_datasets`.

## L9: is the C-GROUP finish line met with the 92 OUT?

**PARTIAL: met for 83 of the 92; 9 rows rest on an unratified extension of the CTO's ruling.**

- **Which ruling governs:** CTO ruling `CTO_RULING_NFRA_MCPINDEX_R18_RESEARCH_32_OUT_OF_LINE_20261016_Z.md` (@33d41059d9),
  addendum ~06:4xZ. It ratifies "all **91 rows**" of the recommendation `ASSETS_no_tool_dispositions.md` @74e243fe48, for its
  10 groups.
- **The diff against the live catalog:** I compared the 92 live no-tool rows with that recommendation, row by row (its
  short names, and its `schwab_<master>_*` pattern for the 45 Schwab rows). **83 of the 92 fall inside the ratified 91.**
  The other 8 ratified rows have since gained a `read_tool` and left the set. 5 of them are named rows:
  `49f_dim_advisor_fee_role`, `commonwealth_cottonwood_account_links`, `smartx_fact_model_aum_daily`,
  `smartx_fact_model_changerequests`, `smartx_fact_model_performance`.
- **9 live no-tool rows are in no ratified row.** They are the 49Financial `*_silver_legacy` rows: allocations, assets, fees,
  prices, realized, single_file, transactions, transactions_enriched and unrealized.
  - 8 of them are in `opal-data-bd`; `single_file` is in `opal-data-assets`.
  - The recommendation's 49F row is labelled "legacy silver, insurance, fees, prices, realized/unrealized", but it counts
    **3** and enumerates only the three insurance rows. The ratification is "all 91 rows".
  - Reading the ruling by its group LABEL (the issuer's application) admits 9 rows the ruling never listed. The packet says
    8; this seat counts 9, because `single_file_silver_legacy` also lacks a tool.
- **So the line is met for every row with a live tool (188) and for the 83 ratified OUT (271 of 280).** For the 9 it needs
  the CTO's explicit word: rule them OUT with a reason and a reopen condition, or name a tool.
- **A fact for that ruling, not a grade:**
  - 8 of the 9 sit in `opal-data-bd`, the live 49F Black Diamond store. PRD v3.6 (Andrew-direct) says 49F BD reads
    `opal-data-bd`.
  - The live `client_adapter_bd49f` reads the opal-data-assets copy (OG-ap-24's A2 ruling; its read role covers
    `blackdiamond/49f/silver/` in opal-data-assets only).
  - Ruling these rows "no client tool is built to read this table" is therefore also a choice of which 49F store the client
    tools read. That choice is the CTO's, against v3.6.

**The widening:** 96 rows are newly visible to their own firm's principals and to no other (1,182 pairs, leaks 0). The host
visibility matrix equals the cut. Both never-widen halves were signed on the deploy-only commit. **Accepted:** seeing a row reads
no data, and the data grant is unchanged.

**The release path (three applies, v1 to v3):** each re-release was for a stale depth measurement, and v3 changes 0 of 280 rows
against v2. The issuer's repair is sound: `emit_final.sh` grades a candidate with `r13.AC3` against live AWS before calling it
good. Carried as the issuer's enrichment 1.

## Rows of the round

- **Disarmed or disposed by the issuer, read and accepted:**
  - Z-S122 disarms Z-W45-S6/S7 and dismisses Z-W45-S8.
  - Z-S123 disarms Z-W22-S1.
  - Z-S124 disarms Z-S92 and Z-W29-S1.
  - Z-S125 disposes the 13 RESEARCH worker rows (Z-W50-S1, Z-W52-S1/S2, Z-W53-S1/S2, Z-W54-S1, Z-W55-S1/S2, Z-W56-S1..S3,
    Z-W57-S1/S2).
  - Z-S129 disarms Z-S126, Z-S127 and Z-S128.
- **Dispositioned here (Z-C-S63):** the 10 ASSETS worker rows Z-W45-S1..S5 and Z-W46-S1..S5.
- **Carried, not of this round:** the earlier ARMED rows Z-W24-S11, Z-S99, Z-S101, Z-S102 and Z-W32-S1. They are held to MX-s-19
  AC2 (2026-10-19/20) and the BD round, as before.
- **Watermark:** every round-18 row through `NFRA_MCPINDEX-Z-S129`.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S62",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T13:20Z",
    "one_line": "Round 18 L9: the C-GROUP finish line is PARTIAL -- met for 271 of 280 rows (188 with a live read_tool across 61 tools, 0 dangling; 83 no-tool rows inside the CTO's ratified 91); 9 no-tool rows (the 49Financial *_silver_legacy rows, 8 in opal-data-bd, the live 49F store PRD v3.6 names) are in no ratified row and are OUT only by the issuer's reading of a group label, so they need the CTO's explicit ruling.",
    "class": "OBSERVATION",
    "spec_asserts": "NFRA_MCPINDEX PRD v0.17 CONTRACT C-GROUP: every in-scope row carries bucket (vendor + firm on assets/bd) and a read_tool naming a live tool; rows outside the line are OUT only by ruling (CTO ruling @33d41059d9, addendum ~06:4xZ: 'all 91 rows' of @74e243fe48 ratified).",
    "world_is": "Live catalog 38fe44d5cb: 280 rows, bucket 280/280, vendor+firm 136/136 assets/bd, read_tool 188 (61 tools, 0 outside the 127-tool index), no read_tool 92 (all silver). The 92 diffed against ASSETS_no_tool_dispositions.md @74e243fe48: 83 named or covered by its schwab_<master>_* pattern; 9 not named (49financial allocations, assets, fees, prices, realized, single_file, transactions, transactions_enriched, unrealized *_silver_legacy; 8 in opal-data-bd). The rec's 49F row is labelled 'legacy silver ...' but counts 3 and lists only the three insurance rows. 8 ratified rows have since gained a read_tool.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 38fe44d5cb:infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml, parsed by this seat (Python 3.11 + PyYAML 6.0.3)",
        "git show 74e243fe48:org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/ASSETS_no_tool_dispositions.md",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_NFRA_MCPINDEX_R18_RESEARCH_32_OUT_OF_LINE_20261016_Z.md @33d41059d9",
        "NFRA_OPLGTW PRD v3.6 (49F BD reads opal-data-bd); OG-ap-24 ask section 2 (A2: the 49F read role covers opal-data-assets only)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "For 1.0.0_SA_CTO~Z: rule the 9 49Financial *_silver_legacy rows OUT (reason and reopen condition) or name a tool; weigh v3.6 (49F reads opal-data-bd) against A2 (the client tools read the opal-data-assets copy). The line is met for every other row."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S63",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T13:20Z",
    "one_line": "Round 18 L8 (ASSETS): the 10 worker rows of MX-c-21 and MX-c-22 dispositioned. Z-W45-S1 (BLOCKING) closed by c21.AC2 PASS on the merged tree; Z-W46-S1's catalog note of an implicitDeny on gold/book is stale, because a live gateway answer read gold/book at 10:36Z; the other eight are issuer-accepted choices or wording.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round before the slug.",
    "world_is": "Z-W45-S1: c21_check.py opened bucket_source relative to cwd (5 unproved); the issuer's re-run on the merged tree reads c21.AC1-AC2 PASS. Z-W45-S2..S5: the emitter's classing of harvest_list (top-level buckets list), channel-row tools (top-level bucket), definition lines at the deployed commit, and write-only/contract buckets are stated choices the order left open. Z-W46-S1: the gold book row's open_items says gateway GetObject on gold/book simulates implicitDeny; NFRA_OPLGTW ANSWER_BODIES.json @a6bc74441f (live 3d5c9c8bf1, 10:36Z) shows etfs_get_fund_holdings reading gold/book/date=2026-10-13/book.parquet with book_absent_reason null and 42 holdings. Z-W46-S2: the history branch avoids _holdings' silver fallback (gold-only contract); a gold-only flag on _holdings is the reviewer's enrichment. Z-W46-S3: opening-paragraph wording; the graded answer is no_data. Z-W46-S4: the key-fragment guard's design, untouched. Z-W46-S5: the expect-as-regex disclosure the order requires.",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-W45-S1",
      "NFRA_MCPINDEX-Z-W45-S2",
      "NFRA_MCPINDEX-Z-W45-S3",
      "NFRA_MCPINDEX-Z-W45-S4",
      "NFRA_MCPINDEX-Z-W45-S5",
      "NFRA_MCPINDEX-Z-W46-S1",
      "NFRA_MCPINDEX-Z-W46-S2",
      "NFRA_MCPINDEX-Z-W46-S3",
      "NFRA_MCPINDEX-Z-W46-S4",
      "NFRA_MCPINDEX-Z-W46-S5"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md rows Z-W45-S1..S5, Z-W46-S1..S5 (read by id)",
        "deliverables/2.0.0_SA_COO~MI/round18/L8_PACKET_ROUND18.md section 1 (c21.AC1-AC2 PASS)",
        "org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/ANSWER_BODIES.json @a6bc74441f (ap-20 body: gold/book source key, book_totals present)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each row is closed by a re-run PASS, an issuer-accepted choice the order left open, or a live served read. Enrichments: clear the gold book row's stale open_items; consider a gold-only flag on etfs_funds._holdings."
  }
]
```

## Carried to the L10 slug

1. **Z-C-S62:** the 9 unratified 49F legacy rows (CTO).
2. The issuer's enrichments 1 to 6, read and endorsed. In particular:
   - item 2: `opal_discover` does not echo `bucket` on opal-data-bd matches, nor vendor and firm on assets/bd matches;
   - item 4: a rollback restores a catalog whose depth claims fail `r13.AC3`.
3. The gold book row's stale `open_items` (Z-C-S63).

-- 3.0.0_SA_CVO~Z
