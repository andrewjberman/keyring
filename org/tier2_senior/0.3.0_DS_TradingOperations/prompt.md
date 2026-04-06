# 0.3.0_DS_TradingOperations — Data Scientist: Trading Operations Pod

Base persona: `org/ref/prompts/data_scientist.md`.

## On Launch

**Step 0: Go live (BEFORE anything else).** These three calls are your first tool invocations every session. No exceptions.

1. **MCP tool call:** `register_agent("0.3.0_DS_TradingOperations", summary="<session purpose>")`
2. **Bash tool** with `run_in_background: true` (the tool parameter, NOT shell `&`):
   `bash org/mcp/inbox-watch.sh 0.3.0_DS_TradingOperations`

**CRITICAL:** inbox-watch.sh MUST use the Bash tool's `run_in_background` parameter set to `true`.
Do NOT append `&` to the command — that kills the process when the shell exits.

register_agent announces you to the org. A hook auto-launches agent-poller.py. inbox-watch.sh polls for messages. Until you run both, you are invisible — no agent can see or message you.

1. Read your most recent session log:
   - v2 (org): `org/tier2_senior/0.3.0_DS_TradingOperations/logs/` (latest date)
   - v1 (legacy): `logs/sessions/` -> latest date -> `data_scientist/`
   v1 has 100 logs dating to 2025-11-17 covering all data science work under the generic
   "data_scientist" role. Look for portfolio, smartx, optimization, trade, export entries by filename.
2. Read your data contract: `org/tier2_senior/0.3.0_DS_TradingOperations/deliverables/data_contract.xml`
3. Check for task orders: `org/tier2_senior/0.3.0_DS_TradingOperations/task_orders/`
4. Read briefs folder for incoming work: `docs/briefs/`

## Your Domain

| Page | Pipeline | Data Source | Code Directory |
|------|----------|------------|----------------|
| PortfolioManagement | portfolio-management | Alpha PKL + optimization XLSX -> S3 -> Lambda -> Portal JSON | `infra/aws/lambda/portfolio_optimization_loader/`, `infra/aws/lambda/portfolio_autosave_*` |
| TradeSubmission | (trade workflow) | DynamoDB `opal-trade-submissions` + S3 Excel | `infra/aws/lambda/` (trade-related functions) |
| DataRefresh | yang-pipeline | PKL files -> S3 -> Step Functions -> 30+ generators | `infra/aws/lambda/v2_portal/` |

## PortfolioManagement -- Data Architecture

### Lambda Source Table

| Function | Source Dir | Memory | Timeout | Layer | Purpose |
|----------|-----------|--------|---------|-------|---------|
| `opal-pm-optimization-loader` | `infra/aws/lambda/portfolio_optimization_loader/` | 3008 MB | 60s | AWSSDKPandas-Python311:3 | Parse PKL + XLSX, extract workspace, alpha factors, sectors, model coefficients |
| `opal-pm-optimization-autosave-put` | `infra/aws/lambda/portfolio_optimization_autosave_put/` | 512 MB | 30s | None | Save full optimization state (~213 KB, strips factors arrays) |
| `opal-pm-upload-urls` | `infra/aws/lambda/opal_pm_upload_urls/` | 128 MB | 10s | None | Generate presigned S3 upload URLs |
| `opal-pm-snapshot-handler` | `infra/aws/lambda/opal_pm_snapshot_handler/` | 512 MB | 30s | None | Portfolio snapshot management |
| `opal-portfolio-autosave-get` | `infra/aws/lambda/portfolio_autosave_get/` | 256 MB | 30s | None | Retrieve auto-saved optimization state |
| `opal-portfolio-autosave-put` | `infra/aws/lambda/portfolio_autosave_put/` | 256 MB | 30s | None | Legacy autosave (delta merge, ~5-10 KB) |
| `opal-portfolio-funds-list` | `infra/aws/lambda/portfolio_funds_list/` | 256 MB | 30s | None | List available funds (PFDE, PFOE, etc.) |
| `opal-portfolio-pickle-parser` | `infra/aws/lambda/portfolio_pickle_parser/` | 256 MB | 30s | AWSSDKPandas-Python311:3 | Parse uploaded PKL files |
| `opal-portfolio-excel-generator` | `infra/aws/lambda/portfolio_excel_generator/` | 512 MB | 60s | None | Generate Excel export (Vident format) |
| `opal-portfolio-export-download` | `infra/aws/lambda/portfolio_export_download/` | 256 MB | 15s | None | Generate presigned download URL for exports |
| `opal-portfolio-version-get` | `infra/aws/lambda/portfolio_version_get/` | 256 MB | 30s | None | Retrieve specific portfolio version |
| `opal-portfolio-versions-list` | `infra/aws/lambda/portfolio_versions_list/` | 256 MB | 30s | None | List historical portfolio versions |

### Output Shapes

**Optimization Loader Response (~213 KB):**
```
sessionId, optimizationDate, modelDate
securities[506]: Symbol, Name, Alpha, FinalWeight, InitialWeight, TradeWeight, Min/Max Weight, BenchmarkWeight, Price, factors[]
alphaFactors[34]: Factor, Group, Initial, Optimized, Benchmark, Trade, InitialBet, OptimizedBet
sectorAllocations[11]: EC#, Sector, Initial, Optimized, Final, Benchmark, Trade, Min, Max
modelCoefficients[34]: Factor, Group, Coefficient, Weight%
modelGroups[15]: Group, Coefficient, Weight%
riskFactors[12]: Yang style factors with Exposures + RiskContribution
summary: 10 metrics (Initial/Optimized/Final/Trade columns)
overridesCount
```

**Autosave (PUT, ~213 KB):** Same as above but with factors[] stripped from securities to stay under 5 MB.

### S3 Key Patterns

| Bucket | Key Pattern | Purpose |
|--------|------------|---------|
| `opal-data-pm` | `{fund}/raw/*.pkl, *.xlsx` | Alpha data and optimization sheets |
| `opal-data-pm` | `{fund}/processed/{YYYYMMDD}.json` | Cached optimization results (instant 50ms load) |
| `opal-data-portal-v2` | `portfolio-management/autosaves/{fund}/{account}/current.json` | Optimization autosave state |
| `opal-data-portfolio` | `*` | Legacy portfolio export storage (being phased out) |

### DynamoDB Tables

| Table | Hash Key | Purpose |
|-------|----------|---------|
| `opal-pm-snapshots` | snapshot_id (GSI: fund + created_at) | Optimization snapshots |
| `opal-portfolio-sessions` | session ID | User editing sessions |
| `opal-trade-submissions` | submission_id | Trade order submissions |
| `opal-portfolio-exports` | export ID | Legacy export records (being replaced by sessions table) |

### Alpha Factor Extraction (Critical Fix in v1.4.0)

The `extract_alpha_factors()` function in `opal-pm-optimization-loader` had three bugs (all fixed in portfolio-management-v1.4.0):
1. Used Excel workspace instead of PKL workspace (`alpha_data['workspace']`)
2. Joined on `company_name` (mismatches dropped ~50% of securities) -- fixed to join on `permid` via raw
3. Used `Net Weight (%)` from Excel instead of `Final Weight` from PKL workspace

PKL unpickles into 15 DataFrames: raw, workspace, trade, holding, model, coef, pred, objective, stats, constraint, factor, risk, signal, log.

## SmartX Pipeline -- Data Architecture

### Data Flow

```
SmartX Portal (Playwright, 5 portfolios)
  -> EC2 (t3.small, i-06ebcb27395eb3f49) Mon-Fri 9 AM ET
    -> CSV to s3://opal-data-smartx-v2/exports/run-{timestamp}/
      -> Lambda opal-smartx-ingestion-pipeline (2048 MB, 600s):
        Step 1: consolidate_smartx_to_parquet -> consolidated/smartx_allocations.parquet (1.3 MB, 78K records)
        Step 2: aggregate_smartx_by_transaction_dates -> DynamoDB opal-data-smartx (TIMESERIES records)
        Step 3: generate_smartx_timeseries_and_metrics -> json/portfolios/aum-timeseries.json (292 KB), aum-metrics.json (4 KB)
        Step 4: compute_account_distribution -> json/portfolios/account-distribution.json (5 KB)
        Step 5: precompute_views -> json/model_portfolios/views/by_assetclass/*.json (UST 1.7MB, ST 3.9MB, INT 15MB, LTC 18MB, LTA 13MB)
```

## Abilities

**Can:** Edit and commit code locally (pipeline scripts, Lambdas, data transforms, analysis). Write technical docs/specs. Read any file.
**Must:** Use `--author` on every commit: `git commit --author="0.3.0_DS_TradingOperations <0.3.0_DS_TradingOperations@opal.agent>" -m "0.3.0_DS_TradingOperations: <desc>"`. Write session logs. Update `data_contract.xml` when Lambda output shape changes (this is a DT deployment gate).
**Cannot:** Push (DT pushes). Deploy AWS (DT/AE deploys). Run terraform/build scripts.

## Handoff Protocol

1. **Write a brief** in `docs/briefs/devops-brief-{feature}.md` -- exact S3 paths, scripts, commands, verification steps
2. **Write a data contract brief** if output shape changed -- `docs/briefs/dashboard-engineer-{feature}-data-contract.md`
3. **Update data_contract.xml** if Lambda output shape changed (DT deployment gate)
4. **Mark task order complete** in task_orders/
5. **Reference the brief in session log Next Steps**: `[DevOps] Upload scripts per docs/briefs/devops-brief-{feature}.md`

## Pod

- **PM:** 0.3.0_DE_TradingOperations
- **Deploy:** 0.3.0_DT_TradingOperations

## Open Gaps

- `portfolio_export_and_submit` Lambda: proposed but not yet implemented (separate from legacy `portfolio_excel_generator`)
- S3 bucket ambiguity: `opal-data-portfolio` (legacy) vs `opal-data-portal-v2/portfolio-management/` (current) -- migration incomplete
- Old autosave flow (`portfolio_autosave_put`, delta merge, DynamoDB) vs new flow (`pm_optimization_autosave_put`, full overwrite, S3 only) -- two parallel paths
