# IRPT_YCDGEN -- DECOMPOSITION, ROUND 1 (THE THREAD, FWD-1): one Cottonwood Overview, kept answers, an element map, Opal's own layout

```json
{
 "project": "IRPT_YCDGEN",
 "round": 1,
 "prd_ref": "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (v0.1 @8b364d6d94; RATIFIED)",
 "prd_version": "v0.1",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7"],
 "round_scope": ["FWD-1"],
 "author": "2.0.0_SA_COO~Y",
 "cells": 4,
 "chains": 3,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "cell_ids": ["YCD-k-1", "YCD-r-1", "YCD-m-1", "YCD-l-1"]
}
```

**Issuer:** `2.0.0_SA_COO~Y`, 2026-10-04 ~00:4xZ, FULL lease. **Source:** the PRD's section 2 (THREAD) and its four
round-1 cells, the CONTRACTS table, the SURFACE MANIFEST S01-S08, and the L5 battery read on 2026-10-03 ~22:2xZ.

## Issuer rulings at this cut

1. **Round 1 is the thread only** (PRD section 2; spine v3.16). FWD-2 to FWD-7 are the enrichment backlog (PRD section 3).
2. **Cut by write set (C10).** Three chains:
   - `~1`: `YCD-k-1` then `YCD-r-1` (the runner consumes the keeper's functions);
   - `~2`: `YCD-m-1`;
   - `~3`: `YCD-l-1`.
   Each cell builds against the contracts in section 2 below, with fixtures, so no chain waits on another's code. The joins
   (the runner reading the map's call list; the layout reading the runner's run record) are the issuer's at the merge.
3. **Workers never call YCharts, never write S3, never deploy.** C-VENDOR admits `~Y`'s agents, but this round keeps every
   vendor call and every store write as the issuer's act at close (the one real run of FWD-1), under the served path's lease.
   Tests use fakes: an in-memory DynamoDB double, `ReplayTransport`-style fixtures and a fake S3.
4. **Where each part runs.** The runner runs ON THE RESIDENT HOST (`i-0167fd745ad906a66`), because the session cookie and its
   WAF token are bound to that host (bundle `capture_origin` EC2). The layout runs ON THE LAPTOP, because the approved brand
   assets exist only in the laptop's main tree (gitignored, `deck_generation/.gitignore:14`) and Chromium (`playwright-core`
   1.60 in `portal/node_modules`) is there. The store connects them.
5. **Addresses come from the builders (rule 30).** Research outputs use `lib/opal_naming.address('irpt', <firm>, 'state',
   <table>, 'request=<REQ>', object=...)`, which for Cottonwood is `s3://opal-data-cottonwood/irpt/cottonwood/state/...`
   (C-STORE, printed at L4 and re-read at this cut). The retained YCharts PDFs the map reads are elsewhere: family
   ORIGINAL_VENDOR_PDF, written through `reporting_destination`, bucket `opal-data-irpt`, prefix
   `irpt/cottonwood/state/vendor_documents/ART-<64 hex>/<sha256>.pdf` (12 objects listed at this cut).

## 2. CONTRACTS THE CELLS SHARE (fixed for round 1)

### 2.1 The kept object (C-KEEP) -- written by the keeper, one per call

Key: `address('irpt', firm, 'state', 'ycharts_responses', 'request=' + request_id, object='step=%02d_%s.json' % (step, name))`.

```json
{
 "schema": "irpt-ycdgen-kept-v1",
 "request_id": "REQ-...", "firm": "cottonwood", "step": 1, "name": "snake_case_call_name",
 "call": {"method": "GET", "path": "/charts/general_data.json", "query": {"securities": "id:P:123,include:true,,"},
          "body_keys": []},
 "response": {"status": 200, "content_type": "application/json", "bytes": 1234, "sha256": "<hex of the kept body bytes>",
              "body_json": {}, "body_b64": null},
 "shape": "IDENTIFIERS | DATA | DOCUMENT",
 "changed_since_previous": "true | false | no_previous",
 "kept_at": "2026-10-04T00:00:00Z"
}
```

- **Scrub:** any key (at any depth, in `query`, `body_json` or a header-like map) matching
  `(?i)cookie|token|csrf|session|password|secret|authorization|api[_-]?key|credential` has its value replaced by
  `"<scrubbed>"`; any string value carrying `ycsessionid=`, `csrftoken=`, `aws-waf-token=` or `cf_clearance=` is replaced
  the same way. `sha256` is of the SCRUBBED body bytes, so a rotated cookie never reads as a changed answer.
- **Shape** (one axis: what the call gave back): `DOCUMENT` when the content type is `application/pdf` or `application/zip`
  or the body starts with `%PDF`; else, for JSON, `DATA` when it holds a key `raw_data`, `calc_raw_value` or `chart_data`, or
  any list of two or more numbers (or of `[number, number]` pairs); else `IDENTIFIERS`.
- `changed_since_previous` compares `sha256` with the same call name's sha256 in the previous run for the same portfolio;
  the caller passes that previous sha256 (or none).

### 2.2 The run record (C-RUN) -- `ycharts_runs/request=<REQ>/run.json`

```json
{
 "schema": "irpt-ycdgen-run-v1",
 "request_id": "REQ-...", "firm": "cottonwood", "report_type": "OVERVIEW", "template_id": "14141822",
 "portfolio": {"security_id": "P:123"}, "window": {"start": null, "end": null},
 "lease": {"fence": 7, "session_fence": 25},
 "calls": [{"step": 1, "name": "...", "key": "irpt/cottonwood/state/ycharts_responses/...", "shape": "DATA",
            "sha256": "...", "changed_since_previous": "no_previous", "status": 200,
            "started_at": "...", "ycharts_ms": 812, "waited_ms": 2000}],
 "elements": [{"id": "p1.e03", "source": {"call": "...", "field": "$.chart_data[0][0].raw_data"}},
              {"id": "p2.e01", "source": "NOT_AVAILABLE", "reason": "BUILDER_ONLY"}],
 "clocks": {"ycharts_working_ms": 0, "opal_waiting_ms": 0, "opal_building_ms": null},
 "report": null,
 "status": "COMPLETE | STOPPED", "stop_reason": null
}
```

- **Three clocks (FWD-6):** `ycharts_working_ms` sums each call's request-sent-to-last-byte time; `opal_waiting_ms` sums the
  time held by the lease's spacing (`next_allowed_at`), the lease queue or a poll interval; `opal_building_ms` is the
  layout's. The runner writes the record with `opal_building_ms: null` and `report: null`; the layout fills both and
  rewrites the same key.
- `elements` copies the map's element ids and sources (the trace from each element to its call and field).

### 2.3 The element map (C-MAP) -- `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json`

```json
{
 "schema": "irpt-ycdgen-map-v1", "report_type": "OVERVIEW", "template_id": "14141822",
 "source_pdf": {"bucket": "opal-data-irpt", "artifact_prefix": "ART-<first 12 hex>", "pages": 4},
 "calls": [{"name": "snake_case", "method": "GET", "path": "/charts/general_data.json",
            "params": {"securities": "id:{security_id},include:true,,", "metrics": "id:total_return,include:true,,"}}],
 "elements": [{"id": "p1.e01", "page": 1, "kind": "number | table | chart | text", "label": "printed label text",
               "source": {"call": "snake_case", "field": "JSONPath into the kept body_json"},
               "claim": "inferred | measured", "note": "one line"},
              {"id": "p3.e04", "page": 3, "kind": "chart", "label": "...", "source": "BUILDER_ONLY",
               "claim": "inferred", "note": "computed only inside YCharts' report builder"}]
}
```

- Labels are printed label text only. **No figure value from the PDF enters git** (C-FIRM): no number read from a figure's
  position, no dollar amount, no percentage value.
- `params` placeholders: `{security_id}` (the portfolio's typed id), `{start}`, `{end}`.

### 2.4 Module home and run environment

- Package: `infra/aws/lambda/investor-reporting/ycharts/research/` (new): `keeper.py`, `runner.py`, `layout_overview.py`,
  `render_pdf.cjs`, `map_pdf.py`, and `tests/`. Tests follow the sibling layout: beside the code, no `conftest.py`, paths
  inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`).
- The runner imports the served session modules as top-level modules, so it puts `ycharts/session` and `ycharts/generate`
  on `sys.path` (`resident_session.py` imports `broker`, `transport`, `deadline_transport`).

## 3. THE CELLS

### `YCD-k-1` -- the keeper, its scrub, and the X10 policy row (S01, S02; FWD-1, FWD-2)
- `ycharts/research/keeper.py`, pure functions plus one store class:
  - `scrub(value)`: the rule in 2.1, recursive over dicts and lists; returns a new object.
  - `shape_of(content_type, body_bytes) -> "IDENTIFIERS" | "DATA" | "DOCUMENT"`: the rule in 2.1.
  - `kept_object(*, request_id, firm, step, name, method, path, query, body_keys, status, content_type, body_bytes,
    previous_sha256=None, kept_at=None) -> dict`: the 2.1 object. JSON bodies are parsed, scrubbed and re-serialized
    canonically (sorted keys, no spaces) before hashing; other bodies are kept as base64 of the scrubbed bytes.
  - `kept_location(firm, request_id, step, name) -> (bucket, key)`: from `opal_naming.address(...)`, the `s3://` URI split.
  - `class KeptStore(s3_client)`: `put(obj) -> key` (`ContentType` `application/json`, the canonical bytes) and
    `get(firm, request_id, step, name) -> dict`.
- **The X10 row:** append ONE policy row `irpt-ycdgen-research` to `infra/logic/registry/reporting_policies.json` with the
  exact field set of the existing rows (`reporting_policies.json:34-53`): `state` `PENDING_ENFORCEMENT`, `enforcement_ref`
  null, `physical_disposal` `OPEN`, `firms` `["cottonwood"]`, `source` and `product_scope` `irpt`, and three families --
  `YCHARTS_RESPONSE` (tier `state`, table `ycharts_responses`, extension `json`), `YCHARTS_RUN` (`state`, `ycharts_runs`,
  `json`), `YCHARTS_OPAL_REPORT` (`state`, `ycharts_opal_reports`, `pdf`) -- each `unreferenced_days` 30 and
  `accepted_ceiling_days` 2555. `register_commit` and `ruling_commit` are the 40-hex commits the existing rows carry.
  `lib/opal_naming.py`'s `_validate_reporting_policies` must accept the file.
- Tests (`tests/test_keeper.py`): a planted cookie, token and session value in a response body, a query and a nested list are
  each ABSENT from the kept object and its serialized bytes; the three shapes; `changed_since_previous` true, false and
  `no_previous`; the key equals the builder's output for `cottonwood`; a fake S3 receives exactly the canonical bytes.

### `YCD-r-1` -- the runner inside the served lease, and the run record (S03, S05, S06; FWD-1, FWD-6)
- `ycharts/research/runner.py`:
  - `run(*, session, store, runs, firm, request_id, portfolio_security_id, map_doc, clock, previous=None) -> dict` where
    `session` is a `ResidentSession`-shaped object (`acquire(request_budget=..., ttl=...)` returning an
    `OperationTransport`), `store` a `KeptStore`, `runs` a writer of run.json (same builder, table `ycharts_runs`, object
    `run.json`).
  - It acquires the lease through `session.acquire(...)`, issues each of `map_doc["calls"]` in order through the transport's
    `request(path_with_query)`, keeps each answer through the keeper, and closes the transport (which releases the lease) in
    a `finally`.
  - **Clocks:** the transport's `wait` hook is wrapped so time spent waiting for `next_allowed_at` adds to
    `opal_waiting_ms`; each request's own duration adds to `ycharts_working_ms`.
  - **Stop, never storm:** a reply that `transport.decision` classifies as `WAF_REFRESH_REQUIRED`, `BROWSER_CHALLENGE` or
    `BACKOFF`, or any refusal from the lease, ends the run at once with `status` `STOPPED` and the reason; the lease is
    released; no call is retried.
  - `previous`: the previous run.json for the same portfolio, if any, gives each call's previous sha256.
  - A command-line entry (`python runner.py --firm ... --request ... --portfolio ... --map <path>`) for the issuer's host run;
    it composes the real `ResidentSession` from the environment the resident uses and prints only store keys and counts.
- Tests (`tests/test_runner.py`) with the REAL `operation_lease.OperationLease` and `OperationTransport` over an in-memory
  DynamoDB double (as `ycharts/session/tests/test_resident_session.py:18-34`) and a scripted transport: the lease is held
  during the calls and released after (also after a failure); spacing waits land in `opal_waiting_ms`; every call is kept
  and listed in run.json, valid against 2.2; a challenge on call 2 of 3 stops with STOPPED, two calls issued, lease released.

### `YCD-m-1` -- the Overview element map from a retained certified Overview PDF (S04; FWD-1, FWD-3)
- Find a retained Overview among Cottonwood's ORIGINAL_VENDOR_PDF objects (bucket `opal-data-irpt`, prefix
  `irpt/cottonwood/state/vendor_documents/`), READ-ONLY, in memory: page 1's title and the template's report type
  (`aggregate_security_overview`, template 14141822) identify it. No object is written and no PDF is saved to disk in the repo.
- `ycharts/research/map_pdf.py`: lists every number, table and chart on each page (pdfplumber words, tables and image or
  vector-chart regions) with its printed label, as the element skeleton.
- The map file (2.3): for each element, the YCharts DATA endpoint and field that supplies it, chosen from the endpoints the
  estate already calls (the gateway's `infra/aws/ec2/opal-gateway/app/integrations/ycharts/client.py`: `/charts/general_data.json`,
  `/charts/fund_data.json`, `/indices/table_data`, `/charts/scatter_plot_data.json`, `/securities/securities_info`) and the
  2026-09 field scrape `docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json`; or `BUILDER_ONLY` when no
  data endpoint carries it. Every source is `claim: "inferred"` until the live run measures it.
- `calls` lists each data call the elements need, deduplicated, with its params template.

### `YCD-l-1` -- the Opal-branded Overview layout (S07, S08; FWD-1, FWD-4)
- `ycharts/research/layout_overview.py`:
  - `build(run_doc, kept_by_name, map_doc, brand) -> html`: one section per map page; each element shows its label and the
    value read from its kept answer by its `field`, or, for `BUILDER_ONLY` and `NOT_AVAILABLE`, the line "Not available from
    YCharts' data endpoints." Charts are drawn as inline SVG from the kept series. A footer carries a plain source credit
    ("Data: YCharts") and nothing else of YCharts' identity: no logo, no layout imitation.
  - `brand`: read at run time from `deck_generation/brand_spec/brand.json` and the Opal logo SVG
    (`deck_generation/brand/logo_package/Opal-Capital-Logo-Package/Full Logo/Full Color/Opal-Capital-Logo-Full-Color.svg`) in
    the laptop's main tree, paths overridable by `IRPT_BRAND_SPEC` / `IRPT_OPAL_LOGO` as `export/assets.py:112-118` does.
    The assets are never copied into git.
  - `render(html) -> pdf_bytes` through `render_pdf.cjs`, which loads `playwright-core` from `portal/node_modules` and prints
    with Chromium.
  - `finish(run_doc, pdf_bytes, built_ms) -> run_doc`: fills `report` (`{"key", "sha256", "pages"}`) and
    `clocks.opal_building_ms`.
  - A command-line entry for the issuer (`--run <run.json> --kept <dir> --map <path> --out <pdf>`); writing to the store and
    printing the signed link are the issuer's acts.
- Tests (`tests/test_layout_overview.py`) on fixtures (a run.json, kept answers and a two-page map under `tests/fixtures/`):
  the PDF parses (pypdf), every element label appears, a BUILDER_ONLY element prints the not-available line, the Opal logo
  is embedded, and no page text carries "ycharts.com".

## 4. Not in round 1

FWD-2 to FWD-7 (PRD section 3). No portal page, no schedule, no second firm, no comparison runner.
