# IRPT_YCDGEN task order -- `YCD-o-4` -- ROUND 4 (ENRICHMENT): THE HELD-DATA FEED CENSUS AND THE SECURITY PROBE MAP

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R4.md</decomp_doc>
<owned_cells>YCD-o-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~2</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, trigger or EventBridge rule is added or read; the project runs on demand only (PRD C-SCOPE)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE nothing is returned at the cut; the issuer's evidence context is this order's check files
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- YCharts direct-API generation, Opal-branded: every YCharts answer of a research run kept in the client firm's store with no secret in it, each report element traced to the answer it comes from, and Opal's own script making the report in Opal's branding. **Round 4** gives the runner a per-window call budget (the firewall challenges the 7th request of any run), finds which held-data figures Opal already holds, adds six risk statistics, and fixes the two maps' missing rows. No worker calls YCharts, writes the store, deploys or grants: the issuer makes every live call at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-3 decomposition)

### `YCD-o-4` -- the held-data feed census and the security probe map (E1 build; FWD-1, FWD-3)
- Offline, read-only: for each of the 158 HELD_DATA rows' column groups, find whether Opal already holds that figure per
  holding, in the served holdings data or the estate's security tables (DynamoDB tables and S3 families the estate already
  reads, e.g. the ETF classifications, the security master, the served holdings snapshots). Read schemas, field names and
  key shapes only, never a client figure.
- Write 4.2's `feed` on each HELD_DATA row and `feed_probe_map.json` for the rest (at most 6 requests for 99 holdings).

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined verbatim from the decompositions)

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

### 2.7 The coverage table and the probe map (cell YCD-c-2)

- `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_coverage.json`:
  `{"schema": "irpt-ycdgen-coverage-v1", "run": "YCD-R1-20261004T1944Z", "elements": [{"id": "p2.e05", "class":
  "HELD_DATA | OTHER_ENDPOINT | BUILDER_ONLY", "reason": "one line", "via": {...}}]}`.
  - `HELD_DATA`: computable from security-level answers weighted by the portfolio's holdings, which Opal holds (the
    frozen upload); `via` names the security-level endpoint and field, and the weighting.
  - `OTHER_ENDPOINT`: a YCharts endpoint that answers for a model portfolio; `via` names the probe call (by `name` in the
    probe map).
  - `BUILDER_ONLY`: neither; `reason` says why.

  Exactly one class per element, for exactly the 176 element ids run 3 left with no answer.
- `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/coverage_probe_map.json`: the C-MAP shape (2.3) holding `calls`
  only (and `elements: []`): one candidate call per OTHER_ENDPOINT route, each GET or the one admitted read-only POST, with
  the same placeholders. It is what the issuer runs live at close.

### 3.1 The expand call (C-MAP v2; built by YCD-r-3, used by YCD-w-3)

A map call may carry:

```json
"expand": {"over": "holdings", "param": "indices", "chunk": 20, "item": "{ticker}", "join": ","}
```

- `param` names the one param the runner fills with the chunk. `item` is `{ticker}` or `id:{ticker},include:true,,`.
  `chunk` is 1-50.
- The runner issues one request per chunk of the holdings' tickers, in the holdings' order. Each answer is kept under the
  name `<call name>__c<kk>` (kk = 01, 02, ...), with one step per chunk, continuing the run's step numbers.
- Every other param is filled as today: `{security_id}`, `{start}`, `{end}`.
- `runner.plan_calls(map_doc, security_id, window, holdings=None)` plans the expanded requests. An `expand` call with no
  holdings given REFUSES before any lease (`EXPAND_REQUIRES_HOLDINGS:<name>`).

### 4.2 The held-data feed (written by YCD-o-4)

Each HELD_DATA row of `overview_coverage.json` gains `"feed"`:
- `{"source": "OPAL_HELD", "table": "<estate table or object family>", "field": "<field>", "key": "<how a holding is keyed>"}`;
- or `{"source": "YCHARTS_SECURITY", "call": "<a call name in feed_probe_map.json>", "field": "<JSONPath>"}`;
- or `{"source": "NONE", "reason": "..."}`.

`deliverables/maps/feed_probe_map.json` is the C-MAP shape (calls only). Its calls are the YCharts security-level candidates
(`/charts/general_data.json`, `/charts/fund_data.json`, `/securities/securities_info`), each with `expand` over the holdings,
and it plans to **at most 6 requests** for Y-5's 99 holdings. It is what the issuer runs live.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- `deliverables/maps/overview_coverage.json`: 158 HELD_DATA rows, each with `via` naming the table_data column group (`columns`), `field`, `aggregation` and `weighting`; 9 OWN_SERIES; 7 OTHER_ENDPOINT; 2 BUILDER_ONLY. `/indices/table_data` answers 404 for the holdings' tickers (row S6), so those `via` routes are dead.
- Where Opal may already hold per-security figures (read schemas, keys and field NAMES only, read-only, with the laptop's credentials): the estate's catalog `comp-which "<question>"` and `comp-estate --definitions` (repo tools) name the tables; candidates include the ETF classifications table (`etf-classifications`, with its two GSIs), the security master (`bd-securities`), the served holdings snapshots (`intake/` and `holdings/` code), and `data/etfs/`. Record per column group: the table or object family, the field, and how a holding (ticker) is keyed. A figure Opal does not hold per holding gets a YCHARTS_SECURITY feed or NONE.
- The holdings are Y-5's 99 frozen rows (tickers such as AAPL, ABBV, SGOV; amounts are client figures: never read or printed). The probe map's calls expand over the holdings (3.1) and must plan to at most 6 requests for 99 holdings, so use the largest chunk a call admits (`chunk` up to 50) and few calls.
- `runner.plan_calls(doc, 'P:1', window, holdings=...)` is what check o-4.AC2 runs on your probe map.

## 4. SURFACES AND BOUNDS

You READ (never edit): `infra/aws/lambda/investor-reporting/` outside your `<paths>`, `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions, the maps you do not own). NEVER: a YCharts call (or any vendor call), an S3 or DynamoDB write, a deploy, a Terraform command, a portal change, a cookie, token or session value in any file, a figure value from a client file or a vendor answer in any committed file (C-FIRM), and none of another cell's files. Read-only AWS reads your order names use the main tree's shim `C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/aws`, into your OS temp directory only, deleted when done. Tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W<slot>-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_coverage.json
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/feed_probe_map.json
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- every HELD_DATA row carries a 4.2 feed: OPAL_HELD with table, field and key; YCHARTS_SECURITY naming a probe call; or NONE with a reason (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round4/checks/o-4.AC1.py`)
- **AC2** -- the probe map plans through runner.plan_calls to 1..6 requests for 99 holdings (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round4/checks/o-4.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-o-4"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round4/checks/o-4.AC1.py</invocation><expect>o-4.AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-o-4"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round4/checks/o-4.AC2.py</invocation><expect>o-4.AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~2/IRPT_YCDGEN.TO-YCD-o-4.held-data-feed-census-and-probe-map.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-o-4.held-data-feed-census-and-probe-map`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 4 cut from the CTO's round-3 analysis @033795b666 sections 2-3 (E1-E6); decomposition round 4 v1.0 (`IRPT_YCDGEN_DECOMP_R4.md`); PRD v0.1 @8b364d6d94; Andrew's egress word @ce20ca6854 (the issuer's live calls only). Chain `~2`. Risk WORLD: the gate's floor for infra paths. Checks dry-run at the base: o-4.AC1 FAIL as expected; o-4.AC2 FAIL as expected.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~06:0xZ):** worker 0.9.0_WK_IRPT_YCDGEN~2 @aeaf356634, merged c6a2cbb058 (channel conflict resolved as base plus both appendices); o-4.AC1 PASS (158 of 158 fed: all YCHARTS_SECURITY), o-4.AC2 PASS (6 requests for 99 holdings) on the merged tree. Row W2-S6 ACCEPTED. Live (the issuer's E1 half, run YCD-R4-20261005T0620Z-C): 6 of 6 requests answered HTTP 400 -- invalid security items and invalid region/maturity metric ids; row IRPT_YCDGEN-S8. The census stands (no Opal table holds the figures per holding); the probe map's request form is the next round's item.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>4</round>
<slot>~2</slot>
<fabric>laptop</fabric>
