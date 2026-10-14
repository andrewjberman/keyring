# Andrew-direct 2026-10-14 ~19:0xZ (laptop, 1.0.0_SA_CTO terminal) -- rival funds indexed and served through the gateway MCP, as opal-data-harvest is

## VERBATIM

> "Also, I want to know where the summary data for rivalfunds is actually stored and in what form, because that would be a good
> addition to the opalgateway efforts in sitez. just like how we are setting up opal-data-harvest over there for the research team,
> we should also have the rivalfunds indexed out and available too, have MSTR issue that directive over there with the instruction
> that the CRO~Z on that box analyze and spec it out, issuing that to their CTO~Z to fold into the workstream between OPLGTW and
> MCPINDEX projects."

## Where the rival funds data lives (measured by this seat, ~19:0xZ)

Every layer is in bucket `opal-data-etfs`, under the ETFS_RIVALS pipeline's prefix `rivalfunds/etfs/`. The layer map is
`org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` lines 519-525. The last three objects of each prefix were read with
`list-objects-v2`.

| layer | address | form | latest read |
|---|---|---|---|
| gold, the master shape (fund x report date x position; every disclosed position, with `source_used` and the corporate-action flag) | `s3://opal-data-etfs/rivalfunds/etfs/gold/canonical_shape/date=<D>/holdings-<stamp>-<id>.parquet` | Parquet, one file per batch per date | date=2026-10-13, written 2026-10-14 11:09Z |
| gold, the trade schedule (trades, income-funded label, excluded events) | `.../gold/trade_schedule/date=<D>/trades-<stamp>-<id>.parquet` | Parquet | date=2026-10-13, 11:10Z |
| gold, the security universe | `.../gold/security_universe/date=<D>/universe-<stamp>-<id>.parquet` | Parquet | date=2026-10-13, written 2026-10-14 13:11Z |
| platinum, the served page | `.../platinum/page/date=<D>/revisions/<stamp>/{index.html, audit.html, manifest.json}` | HTML page, audit page, and a JSON manifest (~100 KB) | date=2026-10-14, 13:11Z |
| silver inputs | `s3://opal-data-etfs/issuer-site/etfs/silver/holdings/date=<D>`, `s3://opal-data-etfs/bloomberg/etfs/silver/holdings/date=<D>` | per source | not read here |
| run state | `.../rivalfunds/etfs/state/<stage>/date=<D>` | batch-complete markers | not read here |

**"Summary" data:** two places carry it.
- The platinum `manifest.json` is the page's machine-readable record per revision.
- The gold tables are the queryable form: positions, trades and universe, by fund and date.

Which of the two should back a search tool is the CRO's first question below.

## The directive (issued by `0.0.0_AB_MSTR` to site Z)

1. **`4.0.0_SA_CRO~Z` analyzes and specs.** Using the opal-data-harvest assessment
   (`OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md`) as the pattern, it reads the rival funds layers above, gold first, then
   the platinum manifest. It proposes the tools for searching rival funds through the gateway MCP. The proposal names:
   - the datasets and their keys (fund id, ticker, report date, position id);
   - the columns worth exposing, their freshness and row counts;
   - each tool's name, input, output columns, and the layer it reads;
   - one worked example: one real rival fund, end to end;
   - what it could not read, and why.
2. **The CRO issues the spec to `1.0.0_SA_CTO~Z`**, who folds it into the gateway workstream shared by NFRA_OPLGTW (serving
   and grants) and NFRA_MCPINDEX (catalog and tools), beside opal-data-harvest.
3. **Bounds already standing:** Opal users only, managed by gateway entitlements. A search reads what the pipeline already holds
   and makes no new vendor call. The pipeline stays the single writer: the gateway only reads. Priority is item 4 of
   `ANDREW_DIRECT_20261014_173xZ_DELIVERABLES_FOUR_PRIORITIES_AND_DATES.md` (site Z, in the background).
