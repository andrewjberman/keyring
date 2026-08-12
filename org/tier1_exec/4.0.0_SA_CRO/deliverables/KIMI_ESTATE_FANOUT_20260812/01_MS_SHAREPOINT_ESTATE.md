# FANOUT 01 — MS/SharePoint estate + producer (verbatim agent report, received 2026-08-12 ~20:15Z)

**Agent scope:** what the MS estate contains; whether document CONTENT (vs metadata) is retrievable;
existing classification; NFRA_MSGRAPH status; limits. **Evidence class: agent-derived; the two crux
claims (content cert, no text-extraction lib) were GROUND-CHECKED at the CRO seat same hour —
`ms_cloud_extract.py:139-150` + `:81-90` read directly; `m365-mcp-gateway/requirements.txt` read
directly (9 lines, no text-extraction dependency). Both hold.**

---

**What I scanned.** Live graph via `comp-kuzu` (`kuzu_nessie_db`, 20,639 nodes / 41,253 edges, built
2026-08-12T18:25:51Z, age 2.0h, Nessie HEAD current, pin == marker). Producer + gateway source read
in full. 3 task orders, 1 PRD (167 lines), 424 files in `docs/architecture/`, 309 project JSONs, 407
ledger files, 28 gateway `app/` files, 41 MCP tool definitions.

## 1. THE PRODUCER — metadata only, and it is structurally enforced

`infra\aws\globgrph\ms_cloud_extract.py` (656 lines), called from `infra\aws\globgrph\derive_runner.py:2326`.
**LIVE in production**: `infra\aws\terraform\globgrph\item2a.tf:395-396` sets `GLOBGRPH_MS_ENABLED = "1"`
(code default is OFF, `ms_cloud_extract.py:621`).

**Emitted per MS_FILE** — `_item_node`, `ms_cloud_extract.py:305-337`: `name`:315, `item_id`:318,
`drive_id`:319, `web_url`:320, `path`:321, `last_modified_dt`:322, `size`:323, `file_type`:329-330,
`mime_type`:331, `owner_upn`:334-336, plus `id/arn/type/layer/drift_class/source`. Verified against
live `props` payloads.

So: **NAME yes · PATH yes · MIME yes · SIZE yes · MODIFIED yes · AUTHOR yes** (`owner_upn`,
`lastModifiedBy` preferred over `createdBy`, `_owner_upn`:362-370). **CONTENT: never.**

**Not emitted, though available:** `createdDateTime` reaches the gateway and is passed through
(`app\ms_ingest.py:100`) but the derive drops it. `quick_xor_hash` and `created_dt` are *declared* on
MS_FILE at `S1_MS_GRAPH_SCHEMA.md:30` — schema-vs-implementation drift; the hash is also absent from
`_ITEM_SELECT` (`ms_ingest.py:37-38`), so unreachable without a `$select` change.

**Content is gate-impossible on this path — three independent layers:**
- Source-call allowlist: `MsGatewayCaller` exposes only 4 methods (`ms_cloud_extract.py:388-398`); no
  `read_file` method exists on the surface.
- Gateway output allowlist: `_strip_item` (`ms_ingest.py:93-117`) is allow-by-key, not deny-by-key.
- Emit-time cert `assert_no_content_comms` (`ms_cloud_extract.py:139-182`) raises and fails the
  derive closed.

**Precise reading of the cert** (`:147-182`): it blocks four things — a non-allowlisted `node_type`,
a field **key** matching a substring in `_FORBIDDEN_FIELD_SUBSTRINGS` (`:81-90`), a comms-surface URL
fragment, and a non-allowlisted `edge_type`. It is a **key-name blocklist, not a content oracle**: a
field key containing `content`/`body`/`preview` fails, but a key such as `subject_class` would pass
it. Stated as measured from source, not as a recommendation.

## 2. Coverage — 1 site / 1 library is BY CONSTRUCTION, not thin modelling

`_crawl_sharepoint_site` (`:509-536`) emits exactly one `MS_SITE` plus one **synthesized**
`MS_LIBRARY` (`"Documents (default)"`, id `{site_id}::default`, `:528-529`) per crawled site.
`DEFAULT_SITE_PROBES = ()` (`:457`) — only the one pinned site is crawled: `opalinvest.sharepoint.com
/sites/Shared` (`:199-204`). OneDrive is OFF (`:210`). `MULTI_LIBRARY_GAP` (`:463-464`):
`list_site_files` reaches only the site's **default** drive; non-default libraries are unreachable,
deferred to S5.

**Live node counts (denominator 5,886, ties exactly):** MS_FILE 4,810 · MS_FOLDER 1,059 · MS_USER 15
· MS_SITE 1 · MS_LIBRARY 1. Uniform `snapshot_ts` (1786500030529) — one fresh derive. Registry
recorded 5,520 nodes / 4,498 MS_FILE on 2026-07-15, so the nightly crawl **is live and growing**
(+312 files).

**Measured silent truncation.** `_TOP = 200` (`ms_ingest.py:40`) and `graph.call` (`app\graph.py:45-57`)
never follows `@odata.nextLink`. Live probe: folder `Recruiting/Portfolio Analyst/linkedin` declares
`child_count` 238; **exactly 200 ingested**. Bounded — only 1 folder of 1,059 exceeds 200 (next
highest 165). Could not determine whether the 38 missing items include folders, whose subtrees would
also be absent.

**Measured denominator contamination.** `DEFAULT_SP_EXCLUSIONS = {}` (`:229`) with an explicit
comment asserting `/sites/Shared` has no repo mirror. That assertion is **false as measured**: 526
`.git` internals + 35 `__pycache__` + 20 `GPUCache` = **581 of 4,810 (12.1%) are non-organic**. The
4,810 is not 4,810 business documents.

## 3. Gateway content access — the crux, and the answer is mostly NO

Document text retrieval exists on a **separate surface** from ingestion (`app\tools.py`, 34 tools) —
human/agent-invoked MCP tools, not the derive. **There is no text-extraction library on the gateway
at all** (`requirements.txt:1-9`: no python-docx, pdfminer, PyPDF2, openpyxl).

Against the measured extension mix (denominator 4,810; top-30 = 4,797, 13 in tail):

| Class | Files | % | Text available? |
|---|---|---|---|
| .pdf 1444 · .docx 557 · .pptx 264 · .PDF 4 | **2,269** | **47.2%** | **NO — none** |
| .xlsx | 1,137 | 23.6% | Cell text only, first sheet, 500-row cap |
| .md/.py/.csv/.txt/.ASC/.vba/.bat/.svg/.json/.ipynb/.html | 507 | 10.5% | Yes, raw decode, 20k chars |
| extensionless (sampled = .git objects, GPU cache) | 538 | 11.2% | Not documents |
| non-doc binary (.pkl/.pyc/.png/.jpg/.zip/.mp4/…) | ~289 | 6.0% | No |
| legacy OLE2 .doc 11 · .xls 21 | 32 | 0.7% | **Mojibake hazard** |

- `read_site_file` (`tools.py:346-359`) raw-decodes UTF-8; magic-byte guard `_office_binary_hint`
  (`:294-308`) intercepts `PK\x03\x04` and `%PDF` and returns a hint, not text. The guard knows only
  those two signatures — legacy OLE2 (`D0CF11E0`) falls through to `decode("utf-8","replace")` at
  `:357`, returning garbage presented as `content`.
- `read_document` (`:559-582`) — despite the name, returns a **Graph-rendered PDF's bytes and
  byte_size, zero text**. Docstring `:563-566`: *"v1 is LEAN (no heavy PDF-text dep on the gateway,
  by design)… Full document text-extract is an honest follow-on."*
- `profile_site_file` (`:362-414`) genuinely reads inside — sha256, line-length stats, delimiter
  probe, `first_lines`/`last_line` clipped to 300 chars — but **bails on binary Office/PDF** at
  `:383-385`, yielding only bytes + sha256.
- `search_site_files` (`:522-528`) returns metadata only, **no snippet**. Graph's index matching on
  file content is a Microsoft platform property NOT verified in this tenant — INFERRED.

**Bottom line on METADATA vs CONTENT:** for the 47.2% of the estate that is PDF/Word/PowerPoint — the
classes most likely to carry client reports and market research — **document text is not retrievable
by any mechanism that exists in this estate today.**

## 4. Existing classification — ZERO

No code, config, schema, or artifact assigns a subject, topic, category, or content-derived label to
any MS document. `file_type` is a filename suffix (`_ext`, `:357-359`). Ontology placement is
structural role only: `MS_FILE` → `Entity.ARTIFACT` (`org\modules\graph\cse_schema.py:269`), `Store`
role (`NFRA_ONTOLOGY_RULE_BANK.yaml:220`). Grep for a "Subject" axis returns only query-subject and
email-subject senses. `comp-pii` is 100% portal/serving-path scoped — 0 MS hits.

Closest existing per-document labelling is `org\modules\heatmap\ms_heat_index.json` (5,604 rows; hot
119 / warm 198 / cold 5,287) — `band` is **recency**, `cluster` is **the parent directory string**.
Explicitly non-semantic.

The estate has capable NLP machinery (Potion/model2vec, SentenceTransformers+HDBSCAN, FinBERT, BM25,
one Bedrock KB over 143 market-update snippets, last ingested 2025-12-05) — **none has ever run over
MS documents**. No Comprehend, no Textract.

## 5. NFRA_MSGRAPH — PRD exists, substrate shipped, headline deliverable never cut

`docs\architecture\NFRA_MSGRAPH_PRD.md` (167 lines, 2026-06-26, `4225ab5bd`). Headline driver is
**agent-findability** (`:17`); S4 is named *"the deliverable Andrew is buying"* (`:135`). S1 complete
(`S1…md:6`); **S2's `<status>pending</status>` tag (`S2…md:6`) is stale — it is deployed and live**;
S3 active and shipped (`ms_heat_index.py`, `8a302757c9`). **S4 was never cut as a TO** — zero
`comp-ms-*` executables in `.tools/`.

Project is dormant: last MSGRAPH commit 2026-07-16; `ms_cloud_extract.py` untouched since 2026-06-26
(`f861a238e6`); ms_heat has zero scheduled trigger, memo'd "leave-dormant-with-declared-status". **MS
is formally PARKED pending Andrew** with zero C2 motif instances
(`org\tier1_exec\4.0.0_SA_CRO\deliverables\CODEBASE_MS_EXTRACTOR_GAP_SPEC_20260811.md:14,31-35`). An
open closeout-drift finding is past its review date
(`org\critical_paths\.open_findings\NFRA_MSGRAPH_closeout_drift_20260806T235728Z.json`).

## 6. Limits — throttling, permissions, PII

- **Throttling: there is no Microsoft Graph 429 handling anywhere.** `graph.py:45-57` is a single
  httpx request — no retry, no backoff, no `Retry-After`. Any status >=400 including 429 raises
  `GraphError` immediately, indistinguishable from a permission failure at the tool boundary.
  Timeouts 60s (call) / 180s (upload). The gateway's *inbound* limiter (`server.py:129-133,191-195`)
  is a different concern and fails open (`ratelimit.py:120,136`).
- **Permissions:** `GRAPH_SCOPES` = `Files.ReadWrite.All Sites.Read.All` (`config.py:51`).
  `READ_ONLY_GRAPH_SCOPES` (`:85-90`) contains **no `Files.*` scope at all** — a read-only-tier token
  physically cannot read OneDrive. The ingest surface is read-only by construction: `_read_get`
  hard-pins GET (`ms_ingest.py:154-163`).
- **PII:** the audit args allowlist is fail-closed and **none of the 12 document tools are in it**
  (`audit.py:71-104`), so their args are logged as `_omitted`. Critically, **redaction applies to
  arguments only — there is no PII scan, redaction, or filter of any kind on tool return values.**
  Any document text retrieved flows to the model unexamined.
- 11 of 12 document tools are classed SAFE with **no tier gate** beyond Graph's own per-user
  permissions (`destructive_ops.py:30-41`, `guard.py:45-46`).

## Could not determine
Composition of the 38 truncated items (files vs folders); whether the deployed EC2 gateway runs this
exact source revision (repo source read, not the live host); whether `.xlsm` is accepted by the Graph
Workbook API; whether `max_depth=12` (`:540`) truncated any subtree — Kuzu lacks `split()`; whether
Graph content-indexing is active in this tenant.
