# Knowledge Items Index

**Last Updated:** 2025-12-05
**Total KIs:** 12

---

## Quick Reference

| KI ID | Title | Status | Tags | Key Artifacts |
|-------|-------|--------|------|---------------|
| `aws_infrastructure` | AWS Infrastructure Patterns | Active | aws, lambda, dynamodb | lambda_patterns.md, iam_roles.md |
| `news_pipeline` | News Ingestion & Analysis | Active | news, lambda, finbert | architecture.md, troubleshooting.md |
| `market_update` | Market Update Generator | Active | market, orchestrator, rag | datewindow.md, evidence_system.md |
| `portal_dashboard` | Portal React Dashboard | Active | react, portal, api | component_patterns.md, api_proxy.md |
| `smartx_data` | SmartX AUM Pipeline | Active | smartx, parquet, etl | pipeline_overview.md |
| `schwab_aum` | Schwab AUM Carving | Active | schwab, aum, rps | rps_format.md, account_mapping.md |
| `vix_strategy` | VIX Trading Strategy | Active | vix, volatility, research | strategy_overview.md |
| `agent_system` | Agent System & Orchestration | Active | agents, prompts, sync | agent_personas.md, sync_architecture.md |
| `session_logging` | Session Logging & Changelogs | Active | logging, sessions, git | log_structure.md |
| `factor_scanner` | Factor Scanner Model | **Archived** | factor, quant, archived | model_overview.md |
| `connection_pool` | AWS Connection Pool | Active | aws, boto3, performance | api_reference.md |
| `architectural_docs` | Architectural Documentation | Active | architecture, decisions | doc_structure.md |

---

## KI Summaries

### aws_infrastructure
**Path:** `logs/knowledge/aws_infrastructure/`
**Status:** Active (CRITICAL)
**watched_paths:** `infra/aws/*`, `lambdas/*`
**Summary:** Lambda deployment patterns, IAM role configurations, DynamoDB table schemas, EventBridge scheduling, S3 buckets, Secrets Manager, API Gateway, CloudFront.
**Key Gotchas:**
- `url_hash` in news tables MUST be Number type (not String)
- NewsAPI keys are in `opal/external-apis`, not `newsapi-keys`
- All Lambdas use us-east-2 region
- CloudFront distribution has broken origin (deleted bucket)

---

### news_pipeline
**Path:** `logs/knowledge/news_pipeline/`
**Status:** Active (CRITICAL)
**watched_paths:** `tools/news_scanner/*`, `infra/aws/lambda/news_*`
**Summary:** RSS feed ingestion, NewsAPI integration, FinBERT sentiment analysis, trending topic extraction, word cloud generation, Layer 3 GPT curation.
**Key Gotchas:**
- `article_date` partition key format: YYYY-MM-DD
- sgmllib3k required for feedparser in Lambda
- GPT validation uses gpt-4o (upgraded from mini)
- FinBERT returns 0.0 for articles with no detectable sentiment

---

### market_update
**Path:** `logs/knowledge/market_update/`
**Status:** Active (CRITICAL)
**watched_paths:** `tools/market_update/*`, `logs/weekly_update/*`
**Summary:** Weekly market update orchestrator, DateWindow architecture, MarketState context, evidence mapping, quality gates, news recap, calendar, positioning.
**Key Gotchas:**
- DateWindow: send_date = Monday deck goes out
- recap_window = prior Mon-Sun, preview_window = current Mon-Sun
- News recap: NO market performance claims (only news developments)
- Components: calendar, market_performance, news_recap, positioning, model_portfolio

---

### portal_dashboard
**Path:** `logs/knowledge/portal_dashboard/`
**Status:** Active (CRITICAL)
**watched_paths:** `portal/src/*`, `portal/lambda/*`, `infra/aws/lambda/portal*`
**Summary:** React portal architecture, page patterns (PageThemeProvider, gradient cards), API proxy caching, component colocalization.
**Key Gotchas:**
- API proxy uses 60-min cache for most endpoints
- Portfolio colors defined in modelPortfolioColors.ts
- New pages follow Positioning page patterns
- CloudFront CDN serves precomputed market metrics

---

### smartx_data
**Path:** `logs/knowledge/smartx_data/`
**Status:** Active
**watched_paths:** `data/smartx/*`
**Summary:** SmartX AUM data pipeline, Parquet storage on S3, Excel API integration, daily/timeseries processing.
**Key Gotchas:**
- Config via AWS Secrets Manager (`opal/smartx/config`)
- Data bucket: `opal-data-smartx`
- Use connection pool, not bash subprocess

---

### schwab_aum
**Path:** `logs/knowledge/schwab_aum/`
**Status:** Active
**watched_paths:** `data/schwab/*`, `tools/schwab_aum_carving/*`
**Summary:** Schwab institutional RPS file parsing, account-to-model mapping, AUM carving strategy.
**Key Gotchas:**
- RPS files are 82.8 GB total in S3 (opal-data-schwab)
- Position records have specific fixed-width format
- Account IDs need mapping to model portfolios

---

### vix_strategy
**Path:** `logs/knowledge/vix_strategy/`
**Status:** Active
**watched_paths:** `research/vix_strategy/*`
**Summary:** VIX trading strategy research, backtesting, signal generation.
**Key Gotchas:**
- Uses local .secrets folder for API keys
- Has its own venv environment

---

### agent_system
**Path:** `logs/knowledge/agent_system/`
**Status:** Active
**watched_paths:** `infra/prompts/*`, `infra/orchestration/*`, `scripts/sync_agent/*`, `lambdas/workspace-sync-agent/*`
**Summary:** Agent persona prompts, orchestration launchers, OneDrive sync agent, workspace-sync-agent Lambda.
**Key Gotchas:**
- START_HERE.md is the entry point for new agents
- Agents must read their own logs before starting work
- Local sync agent runs at 9 AM and 7 PM ET via cron
- Persona prompts are in infra/prompts/

---

### session_logging
**Path:** `logs/knowledge/session_logging/`
**Status:** Active
**watched_paths:** `logs/sessions/*`, `logs/git_logs/*`, `logs/daily/*`
**Summary:** Session log structure, git changelog automation, log file naming conventions.
**Key Gotchas:**
- Session logs: logs/sessions/YYYY-MM-DD/{agent_name}/descriptive_name.md
- Git logs: logs/git_logs/YYYY-MM-DD.md (auto-generated by Lambda)
- Agents must create logs at session end
- Log filenames should be descriptive (snake_case)

---

### factor_scanner
**Path:** `logs/knowledge/factor_scanner/`
**Status:** **Archived**
**watched_paths:** `models/factor_scanner/*`
**Summary:** Factor analysis model for equity tilts. Cloud Lambda deleted Dec 2025, code archived locally.
**Key Gotchas:**
- Lambda deleted, code in models/factor_scanner/archive/
- Uses pandas, numpy for factor calculations
- S3 bucket opal-code-factorscanner still exists

---

### connection_pool
**Path:** `logs/knowledge/connection_pool/`
**Status:** Active
**watched_paths:** `infra/aws/connection_pool/*`
**Summary:** AWS connection pooling module - singleton pattern, thread-safe sessions, 30+ convenience methods.
**Key Gotchas:**
- 5-10x faster than bash subprocess calls
- Credentials refresh every 1 hour
- All agents should use pool instead of AWS CLI

---

### architectural_docs
**Path:** `logs/knowledge/architectural_docs/`
**Status:** Active
**watched_paths:** `infra/architectural_docs/*`, `docs/*`
**Summary:** Architecture decision records, quarantine container for untrusted code, documentation mirror structure.
**Key Gotchas:**
- Quarantine container has AI system prompts for reference
- docs/ mirrors source directory structure
- Architecture decisions go in decisions/ subfolder

---

## Folder → KI Mapping

| Root Folder | Owning KI(s) |
|-------------|--------------|
| `data/schwab/` | `schwab_aum` |
| `data/smartx/` | `smartx_data` |
| `docs/` | `architectural_docs` |
| `infra/aws/` | `aws_infrastructure` |
| `infra/aws/connection_pool/` | `connection_pool` |
| `infra/orchestration/` | `agent_system` |
| `infra/prompts/` | `agent_system` |
| `infra/architectural_docs/` | `architectural_docs` |
| `lambdas/` | `aws_infrastructure` |
| `logs/sessions/` | `session_logging` |
| `logs/git_logs/` | `session_logging` |
| `logs/weekly_update/` | `market_update` |
| `models/factor_scanner/` | `factor_scanner` |
| `portal/` | `portal_dashboard` |
| `research/vix_strategy/` | `vix_strategy` |
| `scripts/sync_agent/` | `agent_system` |
| `tools/market_update/` | `market_update` |
| `tools/news_scanner/` | `news_pipeline` |
| `tools/schwab_aum_carving/` | `schwab_aum` |

---

## How to Use This Index

1. **At session start:** Scan this index for relevant KIs
2. **Before research:** Check if a KI covers your topic
3. **During work:** Reference KI artifacts for patterns
4. **After solving problems:** Update or create KIs

See `KNOWLEDGE_SYSTEM.md` for full protocol.
