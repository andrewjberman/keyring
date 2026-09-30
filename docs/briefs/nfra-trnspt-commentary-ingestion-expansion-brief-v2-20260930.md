# BRIEF v2 (expansion): NFRA_TRNSPT -- Investment Commentary pipeline that accompanies the IRPT Analysis tab

- Author: `4.0.0_SA_CRO` (base), 2026-09-30. Supersedes `docs/briefs/nfra-trnspt-commentary-ingestion-expansion-brief-20260930.md` (v1) where they differ; v1 items not restated here stand.
- Consumer: `1.0.0_SA_CTO` (L4 PRD, L3 registration). Extends `docs/briefs/nfra-trnspt-opal-transcript-database-brief-20260929.md`.
- Andrew's words, verbatim, in `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260930_023xZ_TRNSPT_EXTERNAL_SEND_IS_APPROVED_DREDGE_BACK_AS_FAR_AS_POSSIBLE.md` and `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_020xZ_TRNSPT_COMMENTARY_TIERS_KIMI_TEST_MAILBOX_HANDOFF_TO_CRO.md`, and in the 2026-09-30 walkthrough turn: the pipeline accompanies the Analysis tab; a Generate triggers a Kimi analysis that reads the generate metadata and picks relevant prior emails; no AI anywhere before that call.
- Claim classes: READ (file:line seen by this seat or its subagent, not re-opened line by line), MEASURED, PROPOSED, OPEN, ABSENT (scope stated). Every path below is a SHAPE, not an address: real paths are `address()` output after the registry rows exist.

## 1. The premise, as a flow

```
IRPT Analysis tab: user hits Generate
  -> irpt-ycharts-generate (accepts, enqueues)  -> resident worker -> YCharts -> report READY
  -> [NEW HOOK]  -> commentary Lambda
        1. read the request's frozen composition (variant, comparison_keys, holdings, settings)
        2. PYTHON slices the gold commentary table -> ~10 candidate emails
        3. ONE Kimi call: candidate cards + bodies + system prompt -> picks the best few, drafts commentary
        4. write the draft JSON keyed by report id -> Analysis tab reads it
```

Steps 1-2 are deterministic Python. Kimi is used once, in step 3.

## 2. What exists on the IRPT side (READ, subagent read of `infra/aws/lambda/investor-reporting/`)

- **Request half** `irpt-ycharts-generate` (`ycharts/generate/entry.py:64-195`): `POST /api/scoped/investor-reporting/analysis`, persists acceptance, enqueues to SQS `irpt-generation`; it never calls YCharts. A resident host process (`resident_main.py`) consumes the queue.
- **Browser fields** (`submission.py:14-16`): `request_id, client_id, account_ids, snapshot_id, variant, comparison_keys, report_title, prepared_for` (+ `input_id` for a prospect CSV).
- **Variant map** (`submission.py:19`, `recipe.py:130-132`): 0 comparisons = Overview, 1 = Comparison, 2-5 = Multi. This matches `yc_variant` 1/2/3 one to one, so the IRPT metadata and Alyssa's gold field are the same axis.
- **Frozen composition** `irpt-analysis-composition.v1` (`submission.py:183`): `browser`, `resolved` (owner, client, holdings with `snapshot_id` and rows, `comparison_catalog`), `recipe_version`, `settings` (`management_fee, rebalance, dividends, start, price, tax_status, benchmark`).
- **Post-assembly metadata** (AnalysisReport schema): `request_ref`, `vendor_artifact{sha256,...}`, `effective_inputs{holdings_fingerprint, settings}`, `sections`, `extraction_validation`, `release`. READY detail: `report_id, revision, certification_sha256` (`durable_job.py:140`).
- **Not stored:** account/portfolio type is not a browser field. It must be derived from the frozen composition's owner or holdings (OPEN how).
- **Hook point: ABSENT.** `irpt-requests`, `irpt-jobs`, `irpt-outbox` (DynamoDB, `core/dynamodb.tf`) declare no streams; no S3 notification, no Step Functions, no EventBridge on the generate path. READY is a transactional put of `REPORT#<report_id>#<revision>` into `irpt-requests` (`report_index.py:46-50`). Queue messages carry ids only, max 4096 bytes (`core/sqs.tf:27`).
- **Existing `irpt-narrative`** (`narrative/entry.py`): a deterministic template narrative ("model_version: none"), route-only, no LLM, reads `opal-news-trending-daily` and `opal-news-articles` read-only (`evidence.py:56-58`). It is a sibling, not the commentary.
- **Served output today:** bucket `opal-data-irpt`, platinum family `analysis_reports`, key shape `irpt/<firm>/platinum/analysis_reports/RPT-<32hex>/<sha256>.json` (from `preview_reporting_destination`). The portal reads it through `GET /analysis/{jobId}/sections` (`ops/owned_report.py:57-80`). NOT READ: the portal's `AnalysisTab.tsx`.

## 3. The trigger (PROPOSED; the build is IRPT_BCKEND's, not this project's)

Two ways, both need a change in the IRPT tree, so both are a task order to that project's COO, not a TRNSPT build:
- **A. DynamoDB stream on `irpt-requests`**, filtered to items whose sort key starts `REPORT#`, into the commentary Lambda. Touches no worker code.
- **B. An SQS message enqueued after `publication_worker.finish`**. Touches worker code on a live path.
Recommendation: A. Either is a route, not an alert, so the standing moratorium does not apply. Failure handling is a dead-letter queue and a retry, not a notification.
The commentary must never block or fail the report: the report is READY before commentary starts; the tab shows commentary when it exists.

## 4. Bronze (PROPOSED; addresses from `address()`)

- Shape: `s3://opal-data-transcripts/outlook/transcripts/bronze/analysis_commentary/date=<sent date UTC>/`. Objects: `<mailbox_tag>/msg_<sha256(internetMessageId)[:16]>.json` (Graph message byte for byte), `attachments/<sha256>.<ext>` (raw), `<...>.meta.json` sidecar (`pulled_at`, mailbox tag, Graph id, `internetMessageId`, run id, source marker `mailbox` or `alyssa_fixture`).
- Partition by SENT date so a re-pull overwrites the same key. Whether the grammar allows subfolders under `date=` is UNPROVEN until `address()` runs; if not, the mailbox tag and hash move into the filename.
- Requires registry rows `outlook` (and `sharepoint` for FWD-6) in `infra/logic/registry/systems.json` (READ procedure, `lib/opal_naming.py:1701-1704`; ABSENT today).
- PII lives here. Two named readers, per the L1 brief O8.
- **Fetch:** everything the test mailbox holds, back as far as it goes (Andrew's word), then a daily delta. Gateway limits (MEASURED by a subagent): `search_email(query, top)` has no folder or date filter and is fuzzy; `list_recent_email(since_iso, top, unread_only)` is the only date filter, lower bound only. A test pull is date-list plus client-side filtering; a production Lambda goes to Graph directly (auth is Andrew's call, v1 item 2).
- **Alyssa's cache:** 183 Graph messages and 70 labels on her machine (hand-off section 2). Use as (a) a seed, if she hands the raw Graph JSON over, source marker `alyssa_fixture`; (b) the acceptance labels. It merges with the dredge on `internetMessageId`. Whether to hand the fixtures over is her call; the ask is the CTO's or Andrew's.

## 5. Silver and the PII wipe (PROPOSED)

- Shape: `.../outlook/transcripts/silver/analysis_commentary/date=<sent date>/` parquet, one row per unique `internetMessageId`, built by an event-triggered Python Lambda from bronze.
- **The wipe runs inside this bronze-to-silver step**, so unwiped text never reaches silver. Pure Python, no AI:
  1. Parse HTML with the stdlib parser into a block list; keep block structure (`classify.py` needs it).
  2. Compute the header-derived booleans from RAW headers: `sent_external` (below), `sender_role` (Manav/Yang/Alyssa/other by a staff table, not a name string in silver), `sender_domain`.
  3. Regex out emails, phone numbers, account numbers.
  4. Replace names on a per-message roster: From/To/CC display names, subject-line clients, a curated list. Salutation regex (`Hi <name>`, `Dear ...`).
  5. Wipe THEME LABELS too: samples show client-specific position names used as bold headings.
  6. Any capitalized token not on an allowlist goes to `pii_residual_flags`; flagged rows are excluded from serving until reviewed.
  7. Attachment names hashed/classed; original names stay in bronze.
- **`sent_external` (Andrew: an external send is approved).** True when at least one recipient in To, CC or BCC is not internal, computed at this step from the raw recipients and stored as a boolean plus `external_recipient_count`. A domain rule alone fails: Manav sends from `@opalinvest.com` AND `@49financial.com`, and advisors who receive commentary may sit at `@49financial.com` (OPEN, CTO 103109). PROPOSED definition: INTERNAL = an explicit staff address list (Manav, Yang, Alyssa, Andrew, the shared Opal 49 mailbox) plus the `@opalinvest.com` domain; every other recipient is external. The list is Andrew's to supply (Opal-owned domains and staff).
- **Limit stated plainly:** the wipe catches roster and header-derived names, patterns and labelled classes. A client named only in a body and on no list is caught only by the residual flag.
- **Test:** planted-token leak test (v1 item 1), including a name inside a theme heading, in a PDF-derived string, split across a tag, in a different case.
- The roster's source is OPEN: a client list from a different firm's pipeline tree must not be imported (CLAUDE.md, cross-firm rule).

## 6. Gold: Alyssa's schema, derived from silver in Python (PROPOSED)

Parquet, `.../outlook/transcripts/gold/analysis_commentary/date=<sent date>/`, one row per silver row. No AI. Fields (PRD-001 section 8 list; `yc_variant`, not `model_variant`):

| Field | Derivation in Python | Notes from the email sample |
|---|---|---|
| `record_id` | `sha256(internetMessageId)` | v1 item 3 |
| `sent_at` | header, UTC | |
| `body_text` | cleaned blocks, reply chain cut, signature and compliance disclaimer cut | Outlook bottom-quoted chain; long disclaimer on every mail |
| `yc_variant` | 1 if 0 models, 2 if 1, 3 if 2+, from `models_referenced` | most emails have 0 or 1 model; one had three |
| `models_referenced` | ALIAS TABLE match on body | names appear in prose under aliases: LTC / 49 Long Term, ULT / Ultra Long Term / LTA, UST, PFOE, DIVZ, Dividend Income Strategy, Short/Intermediate/Long Term. The alias table is a new artifact and must map to the IRPT `comparison_keys` (OPEN: how those keys are named) |
| `account_type` | keyword rules (IRA, Roth, 401(k), brokerage, trust, else household) | |
| `holdings` | PDF table parse (nullable) | PDF is NOT always attached (2 of 4 replies sampled) |
| `mention_rate` | holdings named in body / holdings count | null when `holdings` is null |
| `themes` | `list<struct{theme, client, model}>` from block headings + first "X% versus Y%" per paragraph | Manav: bold-label paragraphs. Yang: plain-text headings with 2-3 bullets. Comparisons are inline prose, never tables |
| `sent_external` | silver boolean | replaces `approved` (Andrew) |
| `model_as_of` | join to a model-weights table (nullable; source OPEN, v1 item 6) | |
| `finder_status` | `classify.py` | may under-detect Yang's plain-text headings and messages with no PDF/YCharts link (they land in `review`); test on both formats before trusting |
| `author_role` | silver `sender_role` | commentary author is Manav or Yang; Alyssa produces PDFs/decks |
| `body_hash`, `paragraph_hashes[]` | SHA-256 of cleaned body and each paragraph | to de-duplicate boilerplate reused across clients |

**A concrete example row (synthetic, no real content):**
```
record_id            9f2c...e1  (sha256 of internetMessageId)
sent_at              2026-09-02T14:31:07Z
yc_variant           3
models_referenced    ["Short Term","Intermediate","Long Term"]
account_type         "brokerage"
sent_external        true        external_recipient_count 1
author_role          "yang"
holdings             null
themes               [{theme:"Risk Positioning", client:"...", model:"..."}, ...]
finder_status        "keep"
body_text            "[CLIENT] ... Fixed income duration of 6.1 versus 4.4 ..."
```

**Paths from silver:** one Python Lambda, `pyarrow` (layer `pandas-pyarrow-layer:1` exists, READ `lambda-layer-map.json:85`). The estate has no shared tier-writer in `lib/` (ABSENT), so the schema module is authored here. PDF parsing: `pypdf` is packaged in two layers (`print-deps-layer`, `irpt-render-deps`); `pdfplumber` is NOT in the python3.12 Lambda runtime (`ycharts/extract/extract.py:129-135`). Whether pypdf alone recovers the holdings table is UNTESTED; `holdings` stays nullable until it is. For a NEW Generate the holdings are known exactly from the frozen composition, so the parser is only needed for historical emails.

## 7. The slicer: what the Generate metadata gives and what gold must expose

- **Query inputs from the frozen composition (READ):** `variant` (0/1/2-5), `comparison_keys` (the models compared), holdings and `holdings_fingerprint`, `settings` (`tax_status`, `benchmark`, ...), derived `account_type`.
- **Slice (PROPOSED, all Python):** `sent_external = true` AND `finder_status = keep` (or reviewed) AND `yc_variant` equal to the request's variant; rank by model overlap (`comparison_keys` vs `models_referenced`), then `account_type` match, then recency; remove near-duplicates by `paragraph_hashes` so five boilerplate-clone emails do not fill the list; return about 10 candidates.
- **`commentary_slice_key`** (undefined in the hand-off): PROPOSED as the tuple (`yc_variant`, sorted `models_referenced`, `account_type`, month of `sent_at`), stored as a column and used as the parquet sort order. At about 70 rows (and hundreds after the dredge) the Lambda reads the gold partitions with pyarrow directly; no Athena is needed.
- If a request's variant has no candidate (the sample suggests multi-model emails are rare), the slicer falls back to the nearest variant and says so in the draft's provenance.

## 8. The Kimi call and where the output lives

- **One call.** Input: the request's abstract metadata, up to 10 candidate emails (card + wipe-clean body), the system prompt (Alyssa's `/yc-commentary` text as a prompt asset; NOT READ, it lives on her machine). Kimi picks the few most relevant and drafts. A second call is added only if candidate bodies exceed the context.
- **Precedent:** Kimi is already used in `investor-reporting/intake/resolution_kimi.py:20` (`kimi-k3`), secret `astn/kimi/api-key`, endpoint `https://api.moonshot.ai/v1/chat/completions` (READ). The IRPT tree already carries a Kimi call pattern to copy.
- **Egress (OPEN, Andrew's per-use word):** the request metadata includes a client's holdings. Recommendation: send only abstract fields (variant, model names, account type, theme list, and holdings as sector or category weights, never client identity or account ids).
- **Output home (PROPOSED):** IRPT's served tier, not the transcripts bucket: a new platinum family in `opal-data-irpt` next to `analysis_reports`, keyed by `report_id` and `revision`, provenance in the JSON (`candidate_record_ids`, `kimi_model`, `prompt_hash`, `slice_key`). The portal reads it through a new route modelled on `GET /analysis/{jobId}/sections`. Adding the family is an IRPT policy change (`reporting_policies.json`) and the portal route is IRPT_BCKEND / portal work.
- **Draft, not delivery.** The hand-off says the draft goes to Alyssa; the tab shows it. Whether it shows to the advisor user or only to Opal staff is OPEN, Andrew's call.
- **Reader rule (OPEN, Andrew):** the commentary Lambda reading gold in `opal-data-transcripts` would be a third reader against the two-reader rule. PROPOSED: bronze keeps the two named readers; a scoped role reads only the PII-wiped `silver/` and `gold/` prefixes.

## 9. Context pipelines (READ, subagent)

The sampled emails cite macro themes only (AI capex, breadth and concentration, international valuations, rates, fees, tax efficiency); no news headlines and no other Opal output. So news context is OPTIONAL enrichment, not a dependency.
- **News:** ingestion every 1-3 hours into DynamoDB `opal-news-articles` (`title, source, url, published, summary, sentiment_finbert`); `news_trending_analysis` (cron 07:15 and 17:15 ET) writes `s3://opal-data-news-v2/trending_reports/latest.json`; `news_layer3_curation` writes `opal-news-trending-daily` (PK `date`; rows with `affected_sectors`, `affected_tickers`, `top_articles`, `citations`, `original_keyword`) (READ, `lambda_function.py:2478-2513`). No per-article entity tagging found; ticker linkage is GPT-supplied per topic and UNVERIFIED against live data.
- **Keyword intelligence:** `keyword_intelligence_generator` (twice daily) into `opal-keyword-intelligence` (PK `keyword`, SK `generated_date`); drilldown JSON under `json/sentiment/keyword-history-*` in `opal-data-portal-v2`. Its cron and its docstring disagree (`eventbridge.tf:633`). No portal page found for it.
- **Reuse:** `irpt-narrative` already reads the trending and article tables read-only (`evidence.py:56-58`). PROPOSED for a later round: add a "today's topics whose `affected_tickers` intersect the holdings" block to the Kimi input. Not round 1.

## 10. Revised round-1 shape (for the CTO's decomposition)

1. Registry rows `outlook`, `sharepoint`; the model alias table and staff address list as versioned assets.
2. Bronze landing: the mailbox dredge plus Alyssa's fixtures if handed over.
3. Silver with the wipe and its planted-token test as the gate; `sent_external` computed here.
4. Gold first run on the section 6 fields (`holdings`, `model_as_of` nullable).
5. The slicer as a tested Python function against gold, run over a replay of past Generate compositions (no live trigger yet).
6. Reconciliation note with PRD-001 (v1 item 8).
Round 2 and after: the IRPT trigger (task order to IRPT_BCKEND), the Kimi call (after a passed wipe test and Andrew's egress word), the portal route and family, news enrichment, the PDF holdings parser.

## 11. Calls waiting on Andrew

1. The staff address list and Opal-owned domains that define "external".
2. Client roster source for the wipe (not from another firm's tree).
3. What metadata may go to Kimi (abstract only?) and the per-use egress word.
4. The reader rule for the serving role.
5. Whether the draft shows to the advisor user or only to Opal staff.
6. Production mailbox identity and scope; PRD-001 Q3 model-weights source; the field freeze and PRD-001 reconciliation sign-off.
7. Whether Alyssa hands over the fixtures, and who asks.

## 12. What this brief does not claim

- I have read about twelve commentary threads' structure through a subagent, not a census; the count of commentary emails is unmeasured.
- I did not open `AnalysisTab.tsx`, `resolution_kimi.py`, `graph_client.py`, the model-weights source (none found), or `/yc-commentary`.
- The stream/queue hook, the new platinum family and the portal route are proposals to another project; none is designed to the field.
- The alias table, staff list and roster are named as needed assets; none exists.
- No client names appear here; the email sample's client surnames that reached this seat were not copied into any file.
