# G5r -- rival funds through the gateway MCP: search-tool spec (builds on G5; no re-census)

**archetype:** EXPLORE

- **Author:** 4.0.0_SA_CRO~Z, 2026-10-14 ~19:0xZ-19:2xZ.
- **Order:** crossbox `XB-20261014T185521Z-eda5` (laptop 1.0.0_SA_CTO; acked 19:03:00Z), on Andrew-direct ~19:0xZ (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_190xZ_RIVALFUNDS_INDEXED_INTO_OPALGATEWAY.md`).
- **Scope:** 1.0.0_SA_CTO~Z msg 34190: build on G5. Add the platinum manifest as a candidate source, the gold-vs-manifest choice per tool, one real rival fund end to end, and what could not be read.
- **Base:** `G5_etfs.md` @35f45893a7 holds the 14 rival contracts (13 gold tables + the platinum page) with full column lists. They are not repeated here.
- **Bounds kept:**
  - read only;
  - no vendor call;
  - Opal users only (gateway entitlements);
  - the ETFS_RIVALS pipeline stays the single writer.
- **Freshness:** in trading days against T-1 = 2026-10-13.

## 0. Answer in five lines

1. **Where the summary lives:** every rival layer sits in `s3://opal-data-etfs/rivalfunds/etfs/` (5,620 keys: gold 13 tables, platinum page, state markers).
   - The queryable summary is **gold**: holdings by fund and report date, inferred trades, flows, coverage, peer map and research notes.
   - The platinum `manifest.json` (~100 KB per revision) is a **page-state record** (per-fund status, checks, chart inputs), not a dataset.
2. **Every search tool reads gold**, from the NEWEST part of the newest date partition (re-run parts supersede; G5). One tool reads the manifest, to answer "what does the published page say, and did it pass its checks".
3. **Keys:**
   - fund: `fund_ticker` = `fund_id`;
   - date: `report_date`;
   - position: `position_id` / `snapshot_id`.
   - Securities carry ticker, Bloomberg id, CUSIP, ISIN and SEDOL per position. Unlike the harvest, **a CUSIP/ISIN search works here**, within the fill rates of section 2.
4. **Tools:** G5's nine `etfs_*` rival tools stand, plus one new `etfs_get_rival_page_status`. All are firm-free (Opal fund research), in the read class.
5. **One defect changes an answer** (Z-S124):
   - gold `holdings_coverage` and the published page understate 9 funds' latest report;
   - so a fund's latest report is taken from `canonical_shape`, never from coverage or the manifest.

## 1. The layers, measured today (newest part of the newest partition)

| table (`rivalfunds/etfs/...`) | newest partition / part | rows (newest part) | behind T-1 | backs tool |
|---|---|---|---|---|
| `gold/peer_group_map/` | 2026-10-14 / `map-2.parquet` | 13 (2 groups) | 0 | `etfs_get_peer_group` |
| `gold/canonical_shape/` | 2026-10-13 / `holdings-20261014T110753Z-151ac337dbc8.parquet` (2nd of 2 parts) | 500 (11 funds, report_date 2026-10-13) | 0 | `etfs_get_fund_holdings`, `etfs_who_holds` |
| `gold/trade_schedule/` | 2026-10-13 / `trades-20261014T110753Z-...` (2 parts) | 51 | 0 | `etfs_get_fund_trades` |
| `gold/flow_reconciliation/` | 2026-10-13 / `reconciliation-20261014T110753Z-...` (2 parts) | 11 | 0 | `etfs_get_fund_flows` |
| `gold/holdings_coverage/` | 2026-10-13 / `holdings_coverage.parquet` (written 11:03Z) | 13 | 0 | NOT a freshness source (Z-S124) |
| `gold/research_hypotheses/` | 2026-10-14 / `research_hypotheses-20261014T130234Z-ai.parquet` | 26 | 0 | `etfs_get_research_notes` |
| `gold/buying_trend/` | 2026-10-14 (2 parts) | 1,520 | 0 | `etfs_compare_peers` |
| `gold/holding_contribution/` | 2026-10-14 (2 parts) | 6,185 | 0 | `etfs_compare_peers` |
| `gold/security_universe/` | 2026-10-13 / `universe-20261014T131155Z-...` | 1,058 | 0 | `etfs_who_holds` (resolve) |
| `gold/security_market/`, `gold/corporate_actions/`, `gold/security_names/` | G5 (10-13 / 10-13 / 10-08) | G5 | G5 | `etfs_get_security_reference` |
| `gold/input_census/` | G5 (10-14) | G5 | 0 | `etfs_get_coverage` (reasons) |
| `platinum/page/date=2026-10-14/revisions/20261014T131150Z/manifest.json` | page day 2026-10-14, 99,633 B | 13 fund entries | 0 | `etfs_get_rival_page_status` |

- **Peer groups (measured):**
  - IDVZ: home IDVZ; rivals BIDD, CGIC, INEQ, SCHY, TXUE.
  - PFOE: home PFOE; rivals BASG, ETFT, GQGU, PCLG, TSEL, WCMG.
  - DIVZ and PFDE have no peer group (G5).
- **Two rivals have no 2026-10-13 report:** CGIC and SCHY. Their latest is 2026-10-09 (page check `report_date_freshness`: lag 2 trading days against an allowance of 1), so `canonical_shape`'s newest partition holds 11 of 13 funds.

## 2. Keys and identifier coverage

- **Fund:** `fund_ticker` (canonical, trades, flows); `fund_id` (canonical, coverage, research, peer map). They carry the same value; INEQ is `INEQ` in both.
  - `fund_name` is null for INEQ in the newest canonical part, so a name search goes through `peer_group_map.ticker` and the manifest's `fund` field.
- **Report date and position:** `report_date`; `snapshot_id` (`<FUND>-<report_date>-<hash>`); `position_id`.
- **Security,** in `security_universe` (newest, 1,058 securities):

  | identifier | filled |
  |---|---|
  | `security_ticker` | 1,058 |
  | `security_bloomberg` | 863 |
  | `security_name` | 773 |
  | `security_cusip` | 240 |
  | `security_isin` | 189 |

  - `canonical_shape` carries the same identifiers per position, plus `security_sedol`.
  - A CUSIP or ISIN query therefore resolves for about 23% / 18% of securities.
  - The tool answers `not_held_for_this_security` (never `none`) when the identifier column is empty for a matched ticker.

## 3. Gold vs manifest, per tool

| tool | reads | why not the other |
|---|---|---|
| `etfs_get_peer_group(home_ticker)` | gold `peer_group_map` | the manifest's `peer_group_map` copy is the page's snapshot of it; the gold table is its source |
| `etfs_get_fund_holdings(fund_ticker, as_of?)` | gold `canonical_shape` | the manifest holds no positions |
| `etfs_who_holds(security, peer_group?, as_of?)` | gold `canonical_shape` + `security_universe` | same |
| `etfs_get_fund_trades(fund_ticker or peer_group, from, to, action?)` | gold `trade_schedule` (claim INFERRED, passed through) | the manifest holds only counts (`trades_shown`, `trades_held`) |
| `etfs_get_fund_flows(fund_ticker, from, to)` | gold `flow_reconciliation` (INFERRED) | not in the manifest |
| `etfs_compare_peers(home_ticker, period, axis)` | gold `buying_trend` + `holding_contribution` | the manifest `charts` are rendered inputs of the same rows |
| `etfs_get_research_notes(fund_ticker)` | gold `research_hypotheses` (every row labelled AI, `model_version`, `grounding`) | not in the manifest |
| `etfs_get_security_reference(security)` | gold `security_market`, `corporate_actions`, `security_names` | not in the manifest |
| `etfs_get_coverage(fund_ticker?)` | latest `report_date` per fund from `canonical_shape` (newest part), with `input_census` reasons | `holdings_coverage` and the manifest's `latest_report` understate freshness (Z-S124) |
| **NEW** `etfs_get_rival_page_status(page_day?)` | platinum `manifest.json` (newest revision): `status`, `page_date`, `funds_total` / `funds_updated`, per-fund `status` / `checks` / `latest_report` / `excluded` / `reason`, page `checks` | it is the record of what was PUBLISHED. Its `latest_report` is returned beside the gold value with both labelled, never alone |

Common rules for all ten:
- Admission is the read class (Opal users), as harvest; no firm fork.
- Answers carry `as_of`, `source_keys[]` (the exact part keys read), a denominator and `absent_reason`, projected to 50 KB.
- Read the newest part per date partition and never sum parts.
- Pass `claim` through on the inferred tables.

## 4. Worked example: INEQ (rival in the IDVZ group), end to end

Read 2026-10-14 ~19:05Z-19:15Z.

| question | answer (layer) |
|---|---|
| which group, who is home? | IDVZ group, role rival; home IDVZ (gold `peer_group_map`, 2026-10-14) |
| what does it hold? | report_date 2026-10-13, 106 positions (100 RESOLVED, 6 UNRESOLVED; the page's identity check counts 100 of 100 non-cash lines identified, so the 6 are inferred to be cash or other non-security lines); source `bloomberg` (gold `canonical_shape`, newest part, captured 2026-10-14T11:07:53Z) |
| top holdings | BHP Group 4.63%; Siemens Energy 4.34%; Mitsubishi Corp 4.27%; UniCredit 4.25%; Deutsche Telekom 4.03% (weights as fractions in the table) |
| sector mix (top 5) | Financials 28.6%, Industrials 18.5%, Materials 15.3%, Health Care 8.0%, Consumer Staples 7.6% |
| what did it trade? | 0 inferred trades in the 2026-10-12 -> 10-13 window (gold `trade_schedule`, newest part) |
| flows | 1 window row (2026-10-12 -> 10-13), `trade_count` 0 (gold `flow_reconciliation`) |
| research notes | 2 items (`activity_30d`, `direction_verdict`), grounding PASS on both, AI-labelled (gold `research_hypotheses`, 2026-10-14) |
| what did the page publish? | status `updated`, `latest_report` **2026-10-12**, `trades_shown` 0; fund checks report_date_freshness / content_repeat / completeness / identity_coverage all PASS (platinum manifest, revision 20261014T131150Z) |
| is the page current? | **no for this fund:** gold holds the 2026-10-13 report; the page states 2026-10-12, because coverage was built before the batch that delivered it (Z-S124). `etfs_get_coverage` answers 2026-10-13 from gold; `etfs_get_rival_page_status` shows the page's 2026-10-12, labelled |

## 5. Defects and their tool rules

| id | finding | rule |
|---|---|---|
| Z-S124 | `holdings_coverage` (10-13) was built at 11:03Z between canonical batches (11:01Z: BASG, GQGU; 11:09Z: 11 funds), so 9 funds (BIDD, ETFT, IDVZ, INEQ, PCLG, PFOE, TSEL, TXUE, WCMG) read `gap` in gold coverage and 2026-10-12 on the published page (manifest `latest_report`, all 13 read) | latest report from `canonical_shape` only; the manifest value is shown labelled |
| G5 | re-run parts per date (canonical 692,547 rows across all parts vs 321,049 in the newest parts) | newest part per partition |
| G5 | DIVZ and PFDE have no peer group | `etfs_get_peer_group` answers `no_peer_group` for them |
| measured | CGIC and SCHY latest report 2026-10-09 (2 trading days behind, over the 1-day allowance) | holdings tools state the fund's own `report_date` and its lag |
| measured | `fund_name` null for INEQ in canonical | resolve names through the peer map ticker and the manifest `fund` field |

## 6. What could not be read, and why

- **Coverage rebuild:** whether `holdings_coverage` is rebuilt by a later run on the same date. One partition was read; the next run is tomorrow.
- **Older manifests:** only the newest manifest revision was read (1 of the 2026-10-14 revisions; 12 page days exist per G5).
- **Page HTML:** `index.html` and `audit.html` were not read. They are the human page; the manifest is its machine record.
- **Other tables:** the security reference tables, `input_census` and the bronze/silver inputs (`issuer-site/etfs/silver/`, `bloomberg/etfs/silver/`) were not re-read here. G5 contracts them.
- **State markers:** `rivalfunds/etfs/state/` (405 keys) are run markers, not served.
- **Grant:** the gateway role's read grant on `opal-data-etfs/rivalfunds/etfs/gold/` and `platinum/page/` is not in place. G5 measured the role denied on gold. It is one never-widen ask per group (v3.1).

-- 4.0.0_SA_CRO~Z
