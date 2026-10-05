# IRPT_YCDGEN -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

Worker rows are `IRPT_YCDGEN-W<n>-S<k>`; append-only; gate `.tools/surprise-row-gate.py`.

## IRPT_YCDGEN-W3-S1 -- the laptop has no bundled Chromium; Edge's close() hangs 20-90 s after the PDF is written

```json
[
  {
    "id": "IRPT_YCDGEN-W3-S1",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
    "surfaced_at": "2026-10-04T01:45:00Z",
    "one_line": "YCD-l-1 render_pdf.cjs: no playwright-bundled Chromium is installed, so it launches the msedge channel (bundled as fallback), and browser.close() takes 20-90 s on this laptop, so the close is bounded at 3 s and the process exits.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "YCD-l-1: render_pdf.cjs loads playwright-core from portal/node_modules, launches chromium headless, sets the HTML and prints to PDF.",
    "world_is": "C:/Users/AndrewBerman/AppData/Local/ms-playwright holds only an MCP msedge profile dir (no chromium-<rev> build), so a bundled launch fails; msedge (channel) launches in about 1 s, prints in about 0.1 s, but await browser.close() took 21.8 s (measured with a timing script) and 93 s in a second run. A first test run took 85 s; with the bounded close it is 7 s. The issuer's host run therefore needs Edge or Chrome installed (IRPT_CHROMIUM_CHANNEL overrides the channel); the PDF is already on disk before the close.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "node timing script under .runtime of the worker worktree: launch 1164 ms, pdf 1278 ms, close 21789 ms (msedge channel)",
        "infra/aws/lambda/investor-reporting/ycharts/research/render_pdf.cjs: Promise.race of browser.close() against a 3000 ms timer, then process.exit(0)",
        "pytest tests/test_layout_overview.py: 6 passed in 85.04s before the change, 6 passed in 7.17s after"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  }
]
```

## IRPT_YCDGEN-W2-S1 -- the gateway client the order names does not carry `/securities/securities_info`

```json
{
  "id": "IRPT_YCDGEN-W2-S1",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
  "surfaced_at": "2026-10-04T01:43Z",
  "one_line": "TO-YCD-m-1 names the gateway client as the home of the five estate-called data endpoints including /securities/securities_info; the client carries four of them and no securities_info method. The call lives in the Lambda's ycharts/generate/recipe.py as COMPARISON_IDENTITY_ROUTE. The map still lists it as portfolio_info, sourced from the Lambda route.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "The order lists the endpoints the estate already calls as those of infra/aws/ec2/opal-gateway/app/integrations/ycharts/client.py: general_data.json, fund_data.json, /indices/table_data, scatter_plot_data.json and /securities/securities_info.",
  "world_is": "client.py defines indices_table_data, general_data, fund_data, scatter_plot_data, search and freshness_probe, and no securities_info method; /securities/securities_info is read by the Lambda (ycharts/generate/recipe.py COMPARISON_IDENTITY_ROUTE, and the session tests). The map's portfolio_info call is therefore backed by the Lambda route, not the gateway client.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/opal-gateway/app/integrations/ycharts/client.py@ad781b948a: def lines are indices_table_data, general_data, fund_data, scatter_plot_data, search, freshness_probe; no securities_info.",
      "infra/aws/lambda/investor-reporting/ycharts/generate/recipe.py:412@ad781b948a: COMPARISON_IDENTITY_ROUTE = \"/securities/securities_info\"."
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_YCDGEN-W2-S2 -- the retained PDF carries no template id; "Overview" is read from page 1's title and the page count

```json
{
  "id": "IRPT_YCDGEN-W2-S2",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
  "surfaced_at": "2026-10-04T01:43Z",
  "one_line": "The order says page 1's title and the template's report type identify an Overview. The PDF's own metadata names no template (Title empty, Creator wkhtmltopdf), so the map's template_id 14141822 is carried from the CRO research (an Overview of 23 pages), matched here on page 1 title 'Portfolio Overview' and 23 pages. The PDF is 23 pages, not the 4 of the contract's example.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "A retained Overview among Cottonwood's ORIGINAL_VENDOR_PDF objects is identified by page 1's title and the template's report type (aggregate_security_overview, template 14141822).",
  "world_is": "Read in memory from opal-data-irpt irpt/cottonwood/state/vendor_documents/ART-ac668d3baaab.../6e753361...pdf (582,765 bytes, listed 2026-09-27): page 1 title 'Portfolio Overview', 23 pages, producer wkhtmltopdf; no template id or report type field is readable in the file. The 23-page count matches docs/research/investor_reporting_ycharts_variants_20260911/README.md (Overview, template 14141822, 23 pages). The other objects were listed by size only; none was opened.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3api list-objects-v2 opal-data-irpt irpt/cottonwood/state/vendor_documents/ read-only on 2026-10-04: 12 objects; one 582,765-byte object read with get-object into the OS temp dir (outside the repo) and removed after the map was built.",
      "docs/research/investor_reporting_ycharts_variants_20260911/README.md@ad781b948a: Overview, template 14141822, 23 pages, portrait."
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_YCDGEN-W2-S3 -- no estate document names the table_data column ids or the portfolio response shape; the map's table_data and scatter sources are inferred from printed labels, and holdings rows cannot be templated

```json
{
  "id": "IRPT_YCDGEN-W2-S3",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
  "surfaced_at": "2026-10-04T01:43Z",
  "one_line": "The order has each element sourced from an estate-called endpoint and the 2026-09 field scrape. The scrape is of a Comparison report and names printed fields, not API columns; the estate's own use shows only the column names ytd_total_return, price and pe_ratio and the level/price/total_return series. So 176 of the 249 elements carry a table_data or scatter source whose column id (or metric) is inferred from the printed label and unmeasured for a P:<id> portfolio, 8 more rest on the level series or securities_info, and 65 are BUILDER_ONLY, including every per-holding table (the three permitted placeholders cannot carry holding ids). Each is claim inferred; the live run measures them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Each element's source is a data endpoint and field chosen from the endpoints the estate already calls and the 2026-09 field scrape, or BUILDER_ONLY when no data endpoint carries it.",
  "world_is": "docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json holds sections, printed field names and units for a Comparison report; it carries no endpoint, calc or column id. The gateway reads table_data by calc_name (integration.py _parse_table) and the estate documents only ytd_total_return, price and pe_ratio as columns. Whether /indices/table_data answers for a P:<id> typed portfolio, and under which calc names, is unmeasured at the cut. The map therefore names columns by the printed label (for example asset_allocation_cash, std_dev_5y) as inferred, uses the level series for the cumulative, annual and drawdown elements, and marks per-holding and look-through-holdings rows BUILDER_ONLY.",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json@ad781b948a: top-level keys _meta, entities, sections, field_catalog, distinct_field_names, feasibility_read_PROPOSAL; sections carry field names and units only.",
      "infra/aws/ec2/opal-gateway/app/integrations/ycharts/integration.py:74-98@ad781b948a: _parse_table matches datum calc_name; _parse_series reads chart_data[0][0].raw_data (fund_data) or chart_data[0].raw_data (general_data).",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json: 249 elements, 12 calls; 65 elements BUILDER_ONLY, the rest sourced to a listed call."
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_YCDGEN-S1 -- the close run's first write is denied by Cottonwood's firm fence; the applied grant was proven by an identity-only simulation

```json
{
  "id": "IRPT_YCDGEN-S1",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~Y",
  "surfaced_at": "2026-10-04T18:45:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "The close run (YCD-R1-20261004T1842Z) stopped at its first write: opal-data-cottonwood's bucket policy DenyForeignFirmPrincipals explicitly denies s3:* to any principal not matching role/*-cot-* (plus three users and irpt-holdings-role), and the resident host's irpt-ycharts-runner-role is none of them. The grant applied at 02:44Z (batch 237) was proven by an identity-policy simulation only, which cannot see a bucket policy's explicit Deny",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/YCD-R1-20261004T1842Z_host_run.txt: ssm 9da96471 18:42:50Z-18:42:52Z, runner rc=1, botocore ClientError AccessDenied on s3:PutObject by assumed-role/irpt-ycharts-runner-role on opal-data-cottonwood/irpt/cottonwood/...",
      "s3api get-bucket-policy opal-data-cottonwood read 2026-10-04 ~18:44Z: Sid DenyForeignFirmPrincipals, Deny s3:* on the bucket and /*, Principal *, ArnNotLike aws:PrincipalArn [role/*-cot-*, user/Andrew_Berman, user/Andrew_Berman_Console, user/Opal_Terminal, role/irpt-holdings-role]",
      "infra/aws/terraform/investor-reporting/directory/holdings_refresh.tf:6-10: one principal per firm; the host role does not carry the firm's slot and widening it is the forbidden cross-firm act, so each firm's run is ASSUMED onto that firm's principal"
    ]
  },
  "spec_asserts": "IRPT_YCDGEN C-STORE: the runner keeps each answer and run.json at address('irpt','cottonwood','state',ycharts_responses|ycharts_runs,...) = s3://opal-data-cottonwood/irpt/cottonwood/state/..., written by the resident host's runner role under statement KeepYChartsResearchAnswersAndRunRecords.",
  "world_is": "The firm fence denies that role on the whole bucket, so the statement is inert. The run acquired and released the provider lease (session item lease_expires_at 0 at ~18:44Z); at most one vendor GET (step 1, securities_info) was sent before the first keep failed; nothing was written. Remedy proposed (estate pattern): a Cottonwood-scoped research principal named by opal_name with the cot scope token, holding exactly PutObject+GetObject on the two research prefixes, assumed by the runner role for the writes; the runner composes its S3 client from that role. Never-widen-class act: needs the CTO half.",
  "notes": "The grant ledger irpt-ycdgen-grant-20261004 V1 stays open; the after-read for the remedy reads the bucket policy as well as the identity simulation."
}
```

## IRPT_YCDGEN-S2 -- DISARM of S1: the research writes run on Cottonwood's own principal and are measured landed

```json
{
  "id": "IRPT_YCDGEN-S2",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~Y",
  "surfaced_at": "2026-10-04T19:55:00Z",
  "disposition": "DISMISSED_WITH_REASON",
  "one_line": "DISARM of IRPT_YCDGEN-S1: the research writes now run on irpt-cot-ycharts-research-role (Cottonwood's own principal, assumed by the runner), applied under both never-widen halves (CTO batch 239); close run 3 wrote 6 kept answers and run.json, and the Opal report was stored and read back",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~Y",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "fix 9a01678592 + packet bd21077c42 (merged 4e03aecc26); CTO half a44bc85977 on blob 97578e0eda; apply + after-read b9f350b215 (close/AFTER_READ_PRINCIPAL_20261004.txt: WITH the cottonwood bucket policy both research prefixes allowed, ycharts_opal_reports implicitDeny; WITH the 49financial bucket policy explicitDeny; runner sts:AssumeRole allowed)",
      "close run 3 YCD-R1-20261004T1944Z (close/YCD-R1-20261004T1944Z_host_run.txt): 6 KEPT keys and run.json written on the research principal; ledger irpt-ycdgen-principal-20261004 CLOSED with V1 read back"
    ]
  },
  "dismissal_reason": "The fence admits the firm's own principal by name; the host role gains only the assume; the writes the row named are measured landed.",
  "spec_asserts": "IRPT_YCDGEN-S1: the close run's writes are denied by opal-data-cottonwood's DenyForeignFirmPrincipals.",
  "world_is": "MEASURED: run 2 and run 3 wrote their keeps and run.json; the stored report reads back sha256-equal."
}
```

## IRPT_YCDGEN-S3 -- the step-7 firewall challenge stopped runs 2 and 3 with no row filed (C-SESSION)

```json
{
  "id": "IRPT_YCDGEN-S3",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-04T21:15:00Z",
  "one_line": "Runs 2 and 3 (YCD-R1-20261004T1924Z, T1944Z) stopped at step 7 on a 202 with x-amzn-waf-action (WAF_REFRESH_REQUIRED), at about 1.5 s and 8 s spacing; C-SESSION says a firewall challenge STOPS research and 'files a row', and no row was filed for either stop -- the challenge is recorded only in the drain-end packet's round-2 candidates.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round1/DRAIN_END_PACKET.md section 2 (run 2 STOPPED WAF_REFRESH_REQUIRED at step 7; run 3 step 07 a 202 with x-amzn-waf-action) and section 5 item 3",
      "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md C-SESSION: 'A firewall challenge or a lost session STOPS research: the run releases the lease, files a row and makes no retry storm'",
      "INVESTIGATION_v1.md at HEAD: 0 rows mention a firewall or WAF challenge (this seat's read)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "C-SESSION: a firewall challenge stops the research run, which releases the lease and files a row.",
  "world_is": "The runs stopped and did not retry, as C-SESSION requires; the row half of the contract was not done, so the challenge's shape (request-shaped, not rate-shaped, per the packet) is carried only in a packet note.",
  "notes": "INERT (no retry, session kept). Owner 2.0.0_SA_COO~Y: have the runner file the row on a WAF stop, and carry the step-7 call's split or drop as a round-2 item."
}
```

## IRPT_YCDGEN-W3-S2 -- the coverage enum has no member for an element computable from the portfolio's own kept series

```json
[
  {
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
    "surfaced_at": "2026-10-05T00:30:00Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "IRPT_YCDGEN-W3-S2",
    "one_line": "YCD-c-2: the coverage enum (HELD_DATA, OTHER_ENDPOINT, BUILDER_ONLY) has no member for an element computable from the portfolio's own kept level series; 10 risk, return and drawdown elements were placed under HELD_DATA through the holdings' series.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "C-COVERAGE (decomposition 2.7): HELD_DATA is computable from security-level answers weighted by the portfolio's holdings; OTHER_ENDPOINT is a YCharts endpoint that answers for a model portfolio; BUILDER_ONLY is neither.",
    "world_is": "Run 3 kept a 200 level series for the portfolio itself (step 02, shape DATA), so periodic returns, drawdowns and the Sharpe, Sortino, alpha, beta, standard deviation and VaR rows are computable from an answer that is neither security-level nor a probe. The worker classed them HELD_DATA (buy-and-hold series from the holdings, step-02 series named as the cross-check) rather than add a class. If the CTO wants the derived-from-portfolio-answer case separate, the enum and check c-2.AC1 change, not the file.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_coverage.json (via.weighting and via.cross-check text on the series rows)",
        "s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_responses/request=YCD-R1-20261004T1944Z/step=02_portfolio_level_series.json (status 200, read into OS temp, deleted)"
      ]
    },
    "notes": "INERT: classification choice inside the order's three classes; owner 2.0.0_SA_COO~Y at the round-2 close."
  }
]
```

## IRPT_YCDGEN-W3-S3 -- the probe map cannot reach the dashboard module routes or any per-holding call

```json
[
  {
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
    "surfaced_at": "2026-10-05T00:30:00Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "IRPT_YCDGEN-W3-S3",
    "one_line": "YCD-c-2: the probe map cannot reach the dashboard module routes (/dashboard/*_module_data/{n}) or any per-holding call, because its placeholders are only {security_id}, {start} and {end}; the two probes it holds use ids evidenced in the estate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Decomposition 2.7 and the order's section 3: the probe map is planned by runner.plan_calls with placeholders {security_id}, {start}, {end}; one candidate call per OTHER_ENDPOINT route.",
    "world_is": "The HAR lists /dashboard/fund_chart_module_data/{n} and /dashboard/scatter_plot_module_data/{n}, which need a dashboard id the run does not hold, and the HELD_DATA route needs holding tickers from the upload; neither is a placeholder, so the map holds two probes: a scatter POST with the two axis metric ids documented VERIFIED in docs/briefs/mdsrc-ycharts-endpoint-spec-20260520.md, and a general_data cross-section (xAxis=metrics) with those plus ytd_total_return (the gateway's freshness-probe column). The per-holding security-level queries (table_data, fund_data) are not in this map and need a runner step that reads the frozen upload.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/ycharts/research/runner.py plan_calls (_PLACEHOLDERS = security_id, start, end; READ_ONLY_POSTS = the scatter path)",
        "C:/Users/ANDREW~1/AppData/Local/Temp/claude/C--Users-AndrewBerman-Desktop-ajb-workspace/b55fbe94-a2b0-45e3-adad-582b87cc1103/scratchpad/har_request_shapes.json (dashboard routes carry {n})"
      ]
    },
    "notes": "INERT: scope of the probe map, not a defect; owner 2.0.0_SA_COO~Y to cut the holdings-reading runner step if the 167 HELD_DATA elements are to be answered."
  }
]
```

## IRPT_YCDGEN-S4 -- the keeper classes a data.series answer as IDENTIFIERS (C-KEEP)

```json
{
  "id": "IRPT_YCDGEN-S4",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-05T00:31:00Z",
  "one_line": "The keeper labels the scatter_plot_data answer IDENTIFIERS although it carries a data series (data.series): in round 2's close runs YCD-R2-20261004T2315Z-A/B the POST with the documented metric ids answered 200 with data.series, and C-KEEP's shape rule has no member for that key, so a DATA answer is filed as identifiers and an element sourced from it would read as not available.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/DRAIN_END_PACKET.md section 3 ('One defect found') and section 5 item 3",
      "this seat's round-2 L9 read (delegate): both close runs' run.json, scatter call status 200 with data.series"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "C-KEEP: each kept answer is classed by its shape, and an answer carrying data is DATA.",
  "world_is": "An answer with data.series is classed IDENTIFIERS; no element reads it yet, so nothing printed is wrong today.",
  "notes": "INERT (no element sourced from the scatter yet). Owner 2.0.0_SA_COO~Y: teach the shape rule the series key and pin it with the round-2 scatter answer's shape, before the OTHER_ENDPOINT re-pointing (packet section 5 item 2) reads it."
}
```

## IRPT_YCDGEN-W1-S1 -- run.json schema is v2 only for a run given holdings; the kept runner tests pin v1

```json
{
  "id": "IRPT_YCDGEN-W1-S1",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~1",
  "surfaced_at": "2026-10-05T01:08:00Z",
  "one_line": "YCD-r-3: contract 3.2 says run.json schema 'becomes irpt-ycdgen-run-v2', but the 25 kept runner tests pin v1 and the exact v1 key set; the runner writes v2 (with the holdings block) only for a run given holdings, and v1 unchanged otherwise.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/ycharts/research/tests/test_runner.py valid_run_record (asserts schema == irpt-ycdgen-run-v1 and the exact 13-key set) at base 7616d7a7d9",
      "infra/aws/lambda/investor-reporting/ycharts/research/runner.py run(): schema v2 and the holdings key only when holdings is not None"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "C-RUN v2 (decomposition 3.2): run.json gains a holdings block and schema becomes irpt-ycdgen-run-v2, every v1 key kept; the order also says keep every existing test passing.",
  "world_is": "Both cannot hold for a run without holdings: an unconditional v2 breaks valid_run_record. A run with holdings writes v2 plus the block; a run without writes v1 with no holdings key, which is honest (it read none). Also: _compose now returns (session, research_s3, {s3, dynamodb} host clients), so World.main's _compose fake in test_runner.py returns a 3-tuple.",
  "notes": "INERT: a consumer (YCD-l-3) must read schema v1 as 'no holdings' and v2 as holdings present. Owner 2.0.0_SA_COO~Y to rule if v2 should be unconditional (then valid_run_record is amended)."
}
```
