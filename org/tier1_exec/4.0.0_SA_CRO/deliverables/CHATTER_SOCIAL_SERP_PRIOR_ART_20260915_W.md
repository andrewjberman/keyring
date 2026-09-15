# Chatter, social feeds and SERP: prior art and implementation audit

Author: `4.0.0_SA_CRO~W`. Audit vintage: 2026-09-15 06:02 UTC.

## Andrew-direct request, verbatim

Channel: user message in this Codex session; exact arrival timestamp unavailable.

> I also want you to look into any prior art regarding the "chatter" function and the live social feeds and SERP searching and etc. through Bright data for the 89 securities. Did we figure out a pipeline for that?

## Answer

There is substantial prior design, working SERP utility code, account-discovery
evidence, a social-item schema, and a deployed Chatter ranking producer. There is
**not an established end-to-end Bright Data social/SERP collection pipeline for
all 89 securities** in the inspected implementation. These components are also
not included in the current local-publications archive in opal-data-harvest.

## What exists

| Component | Source | What the evidence establishes |
| --- | --- | --- |
| Original mechanism | `CHATTER_VOLUME_DAILY_REFRESH_MECHANISM_20260911.md` in this directory | Daily per-security SERP counts; 30-day history; relative 0-100 score; top-10 Trending union top-10 Breakout narrows publisher refreshes. Live query-shape test recorded, plus synthetic ranking proof. Historical passages have stale 7-day language corrected by the explicit 30-day ruling. |
| SERP HTTP primitive | `data/find/dualbiz/scripts/serp.py:245` | `serp_brightdata()` uses a dedicated SERP zone, POST `/request`, parses JSON `organic[].link`, paginates and deduplicates URLs. Exists for other work; no 89-security daily collector/time-series writer found. `serp_search()` selects an engine; it does not automatically implement the fallback promised by the brief. |
| Deployed Chatter producer | `lib/research/metrics/chatter_axis.py` and `infra/aws/terraform/harvest/chatter-axis-schedule.tf` | Counts stored article dates in `opal-harvest-articles` via `ticker_date_index`; writes Trending/Breakout rankings to `opal-harvest-security-metrics`. Does not call Bright Data or collect social posts. |
| Social dataset plan | `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~6/MEASUREMENT_PLAN.md` | X posts first: dataset `gd_lwxkxvnf1cynvib9co`, Home Depot, cashtag then company then resolved handle. Cost, freshness, schema, latency and relevance are the planned observables. Reddit posts/comments are also catalogued. A catalogue listing is not a successful extraction. |
| Social library | `lib/research/social/measure.py`, `schema.json`, `validator.py` | Request-description builder and validation contract. `measure.py:206-218` explicitly has NO HTTP client and returns 4 even when a word record is supplied. No feed ingestion follows from running it. |
| Social account discovery | `IDENTITY_SOCIAL_ACCOUNT_PASS_20260914_Z.json` and `scripts/social_account_pass.py` | 89-name denominator; 88 domains attempted; 61 resolved, 263 account links; 27 attempted domains unresolved plus one without a held domain. Links are INFERRED from company websites, not account-page confirmed. No social-post stream was collected by this pass. |

Social contract fields: `item_id`, `platform`, `account.handle`,
`account.official`, `posted_at`, `text`, `url`, `admitted`, `rule_reason`,
`source_line`. Item identity is the vendor ID or a deterministic hash. Existing
account evidence is distinct from whether a post is about a security.

## Current read-only deployment verification

At 06:02:23 UTC, boto3 Scheduler `get_schedule` and Lambda
`get_function_configuration` returned:

- `amgt-resapp-chatter-axis-daily`: ENABLED, `cron(0 10 * * ? *)`, UTC.
- `amgt-resapp-chatter-axis`: Active, last update Successful,
  LastModified `2026-09-15T02:33:20.000+0000`.
- CodeSha256 `fj8wqp9jaZWfMaBrrAyUImGnt2c5Xeb7losUr+i65mM=` matches the
  02:29Z consolidation deployment record.
- No function invocation, secret read, publisher pull, or schedule mutation.

Readback: `.runtime/opal-data-harvest/chatter-pipeline-audit.json`.
Deployment record:
`org/critical_paths/change_management/20260915T0229Z_amgt-chatter-axis-consolidation-and-repoint_deploy_completion.md`.
Its 02:36Z QA invocation considered **34 tickers** and wrote 10 ranking rows.
The current checked-in default universe still yields 34 eligible Bloomberg
tickers when evaluated with `read_universe_tickers()`. This is not 89-name
coverage. The upcoming scheduled fire was not tested or awaited by this audit.

## Gaps and design decisions to resolve

1. **Instrument mismatch:** the original daily design uses SERP results;
   the implemented producer counts stored publisher articles. Social discussion
   is not an input. Keep source-specific raw counts and provenance; do not
   silently call these interchangeable measures of attention.
2. **Universe:** repoint/fix the ranking input to the canonical 89 identities,
   retaining explicit unresolved identifiers rather than silently excluding 55.
3. **SERP quality:** the utility returns only up to the requested pages of links
   (default two pages of ten), not total Internet mention volume. It also breaks
   on HTTP/JSON failures and returns an empty/partial list, so failures can look
   like silence. A daily collector must preserve failure state and query/window
   settings, and avoid treating capped search results as an uncapped count.
4. **Social collection:** the dataset trigger/download client, measured post
   relevance, ingestion/storage wiring, incremental cursor and scheduled worker
   are not present in the inspected social implementation. Start with a bounded
   one-security dataset measurement before deciding feed frequency.
5. **Identity vs relevance:** `attach_to_security()` currently rejects accounts
   whose official-company-account status is unresolved. That is too restrictive
   for general investor discussion. The design must distinguish a company's
   official feed from third-party posts about it before presenting a broad feed.
6. **Storage and local worker:** current publication archive manifest has no
   social/SERP/Chatter modules; these live elsewhere in the repository. No
   social/SERP-to-local-publications adapter is established. The Chatter DynamoDB
   reader also does not consume the new canonical S3 article/link objects directly.
7. **Selection bias:** if stored article counts decide which names receive more
   article collection, that selection can reinforce itself. Comparable discovery
   coverage across all 89 should supply the ranking signal before selective
   full-body retrieval is used to reduce publisher load.

The old social plan's per-call vendor-permission explanation is historical:
the current session has Andrew's fabric-wide egress grant relayed in 23033.
Permission is not the missing HTTP client. This request was an investigation;
no new feed, broad collection, deployment, or schedule was started.

Existing cloud Chatter ranking schedule and disabled local publication-collection
task are separate. The former computes rankings from stored records; the latter
remains disabled with production collection mechanism/cadence reserved to Andrew.

Push state: LOCAL. This seat does not push.
