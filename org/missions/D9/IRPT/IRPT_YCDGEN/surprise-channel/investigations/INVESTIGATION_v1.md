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

## IRPT_YCDGEN-W3-S4 -- contract 3.4/3.5 leaves the computation conventions open; YCD-l-3 chose five and the issuer should confirm them

```json
{
  "id": "IRPT_YCDGEN-W3-S4",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-05T01:09:00Z",
  "one_line": "YCD-l-3: contracts 3.4/3.5 do not fix five conventions the layout needs (renormalization of the plain weighted mean, statistic units, the BUY_AND_HOLD start, the per-security field root, the sleeve source), so layout_overview.py fixes them and pins each in a test.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Contract 3.4: WEIGHTED_MEAN is `sum_i w_i * v_i` over holdings with an answer; the statistic ids give no unit; BUY_AND_HOLD is `V(t) = sum_i amount_i * series_i(t) / series_i(t0)`; `field` is a JSONPath per security; the sleeve share is the holding's asset_allocation_stock or asset_allocation_bond answer.",
  "world_is": "Chosen in layout_overview.py (all pinned by tests/test_layout_overview.py): (1) WEIGHTED_MEAN, HARMONIC_WEIGHTED_MEAN and the sleeve mean renormalize the weights over the holdings with an answer, so a weighted mean is a mean (the literal un-renormalized sum is biased low by the unanswered weight; the two agree at coverage 1.0); a harmonic holding with value 0 counts as no answer; SUM is the plain sum over answered holdings. (2) Series statistics return PERCENT (total_return, annualized_return, std_dev, max_drawdown, the last negative or 0), matching YCharts' calc values; cumulative_series returns [[ts_ms, V]] pairs. (3) BUY_AND_HOLD t0 is the latest first observation among the answered holdings, V runs on the union of their observation times with as-of carry-forward, and a window longer than that common history is NOT_AVAILABLE reason SERIES_TOO_SHORT. (4) A per-security `field` is read from that security's node (chart_data[k] or the indicesData entry); a field that starts `$.chart_data[N]` or `$.indicesData[N]` has that prefix re-rooted at the security's node; `columns` (calc ids) read an indicesData entry by calc_name; a chunk's tickers come from the kept query param whose items are all held tickers, and a chunk whose chart_data length differs from its ticker count is treated as unanswered. (5) The sleeve share is read by calc_name `asset_allocation_<sleeve>` from any kept 2xx table answer, not from a named call; absent everywhere gives INPUT_MISSING:asset_allocation_<sleeve>. The trace `inputs` are the run.json `calls[].key` of each kept answer that supplied an answered holding (the filename form `step=NN_<name>.json` when the run record lacks the call).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py compute_element / statistic_of / _nodes @ branch wk-ycdgen-r3-3",
      "infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py test_computed_* and test_coverage_below_* @ branch wk-ycdgen-r3-3",
      "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R3.md sections 3.4 and 3.5"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: no element is computed yet in a served report; the issuer's close run is the first read. Owner 2.0.0_SA_COO~Y: confirm or amend each convention before the map's computed sources are graded against YCharts' own printed values."
}
```

## IRPT_YCDGEN-W2-S4 -- the 3.4 statistic id list does not hold the statistics five OWN_SERIES elements and one buy-and-hold element name

```json
[
  {
    "id": "IRPT_YCDGEN-W2-S4",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
    "surfaced_at": "2026-10-05T01:13:00Z",
    "one_line": "YCD-w-3: contract 3.4's statistic ids lack alpha, beta, sharpe, sortino, monthly VaR and max_drawdown_15y; the OWN_SERIES elements p7.e02, p7.e03, p7.e05, p7.e06, p7.e08, p7.e07 name those ids in source.columns with statistic null, and p12.e04 (market-price returns) is BUY_AND_HOLD with total/annualized ids.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Decomposition R3 contract 3.4: statistic ids are total_return_<1m..15y>, annualized_return_<3y..15y>, std_dev_<1y..15y>, max_drawdown_<1y|3y|5y|10y|all>, cumulative_series; row W3-S2 says the risk and return rows are computable from the portfolio's own kept series.",
    "world_is": "Of the 9 elements moved to OWN_SERIES, p2.e08, p2.e13 and p6.e22 use only listed ids; p7.e07 needs max_drawdown_15y (unlisted) and p7.e02, p7.e03, p7.e05, p7.e06, p7.e08 need alpha_/beta_/sharpe_/sortino_/value_at_risk_monthly_5_ over 1y..15y, which need a benchmark or risk-free series the id list does not name. p12.e04 prints market-price returns and an inception date; the portfolio has no market price, so it stays HELD_DATA on BUY_AND_HOLD over the holdings' level series (the one consumer of holdings_level_series), and its price-only basis is inferred. Each such element carries its ids in source.columns, statistic null, claim inferred; YCD-l-3 prints NOT_AVAILABLE for an id it does not implement.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R3.md contract 3.4 (statistic ids)",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json elements p7.e02 p7.e03 p7.e05 p7.e06 p7.e07 p7.e08 p12.e04 (source.columns)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "INERT: wiring is complete against the contract; owner 2.0.0_SA_COO~Y at the round-3 close (extend the id list or accept NOT_AVAILABLE for these)."
  }
]
```

## IRPT_YCDGEN-W2-S5 -- one element needs 16 columns against the 8-column call bound, and the computed `field` and the probe answers' shapes are inferred

```json
[
  {
    "id": "IRPT_YCDGEN-W2-S5",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
    "surfaced_at": "2026-10-05T01:13:00Z",
    "one_line": "YCD-w-3: element p6.e02 names 16 bond-maturity columns, so with the 8-column bound they span holdings_bond_exposure_01 and _02 while a 3.4 source names one call; its source.call is the first chunk and source.columns lists all 16. Computed fields are per-security paths in the table_data entry dialect, and the two probe answers' shapes are inferred.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order section 3: split any table_data group above 8 columns (round 1's long column list drew the firewall); contract 3.4: a computed source names one `call` and a `field` JSONPath per security.",
    "world_is": "Every other multi-column element fits one chunk call (checked: the columns of all 156 other table_data held-data elements lie in their named call). For p6.e02 the layout must find columns 9-16 in the following chunk. `field` for table_data calls is `$.data[?(@.calc_name in columns)].calc_raw_value`, applied to one indicesData entry (entry shape per ycharts_client.parse_table_data: security_id|id, data[].calc_name/calc_raw_value); for fund_data `$.raw_data`. The two probe-call elements use `$.chart_data[*]` (general_data xAxis=metrics, shape not yet kept) and `$.data.series[*]` (scatter, shape per the endpoint spec WS2-MP-03); no answer was read, so these paths are inferred.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py parse_table_data and parse_chart_series (entry and chart shapes)",
        "docs/briefs/mdsrc-ycharts-endpoint-spec-20260520.md WS2-MP-03 (data.series[])",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json element p6.e02 and calls holdings_bond_exposure_01, _02"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "INERT: YCD-l-3 reads the dialect against its own contract; owner 2.0.0_SA_COO~Y to join at the drain and the close run."
  }
]
```

## IRPT_YCDGEN-W4-S1 -- map_pdf's footer-chrome rule is portrait-only, so the Multi PDF's 34 landscape pages each yield a footer logo read as a chart plus a footer caption and date read as text

```json
{
  "id": "IRPT_YCDGEN-W4-S1",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~4",
  "surfaced_at": "2026-10-05T01:27:00Z",
  "one_line": "map_pdf's footer-chrome rule is portrait-only, so the Multi PDF's 34 landscape pages each yield a footer logo read as a chart plus a footer caption and date read as text",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-m-3 section 3: map_pdf.py gives the element skeleton per page, and its chrome rule drops the page footer.",
  "world_is": "map_pdf.py FOOTER_TOP is 755 pt and CHROME_IMAGE_BOTTOM 112 pt, both set for a 612x792 portrait page. The Multi PDF's pages are landscape (a scatter chart's bbox runs to x1 above 740), so the 'Built with YCharts' logo at about y 588-603 survives as a 'chart' element and the footer line as 'caption' and 'date range' elements on every one of the 34 pages (34 logos, 34 captions, 34 dates), and the 'chart k of n' numbering counts the logo. comparison_map.json (portrait) has none. multi_map.json keeps all of them as kind text, labels 'page footer logo' / 'page footer text' / 'page footer date', BUILDER_ONLY, and renumbers the real charts of each heading; map_pdf.py was not edited.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "multi_map.json elements labelled 'page footer logo' (34), 'page footer text' (34), 'page footer date' (34)",
      "skeleton p12 chart bbox [45, 86, 747, 479] (a landscape page) and the logo bbox [35, 588, 94, 603] repeated on every Multi page; infra/aws/lambda/investor-reporting/ycharts/research/map_pdf.py constants HEADING/FOOTER_TOP/CHROME_IMAGE_BOTTOM"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: a map-side repair, no consumer reads the footer. Owner 2.0.0_SA_COO~Y: if the layout cell reuses map_pdf on a landscape report, a page-size-aware footer rule belongs in map_pdf (a later cell, not this one)."
}
```

## IRPT_YCDGEN-W4-S2 -- the C-MAP shape has no member for a second or third security's source; the two maps add three optional keys and one placeholder

```json
{
  "id": "IRPT_YCDGEN-W4-S2",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~4",
  "surfaced_at": "2026-10-05T01:27:00Z",
  "one_line": "the C-MAP shape has no member for a second or third security's source; the two maps add three optional keys and one placeholder",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "C-MAP (decomposition 2.3): an element's source is ONE {call, field}; params placeholders are {security_id}, {start}, {end}.",
  "world_is": "A Comparison prints each figure for two securities and a Multi for three, so one source per element cannot name them. The maps keep source as the portfolio's {call, field} and add: column_sources (list of {key_index, call, field}) on an element that prints all securities in one row or chart, key_index on a source that names one comparison key, and calls named comparison_<x> (the Overview call with {security_id} replaced by the new placeholder {comparison_security_id}, issued once per comparison key, key order = printed column order). The comparison_ table_data calls keep the Overview's `indices` parameter, correct for a model-portfolio key (Opal Long-Term, Opal Ultra Long-Term) and UNMEASURED for an ETF key (IWM in the Multi): the entity parameter of an ETF read is not in the Overview's measured answers. All claims are inferred.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "comparison_map.json and multi_map.json calls[] carry comparison_* entries; elements carry column_sources / key_index",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json: the 12 portfolio_* calls the comparison_* calls copy"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: extra keys are ignored by a reader of the Overview shape. Owner 2.0.0_SA_COO~Y: the layout and runner cells that read these maps must read the new keys, and the round-3 close should read one comparison key's table_data answer to settle the ETF entity parameter."
}
```

## IRPT_YCDGEN-W4-S3 -- Cottonwood's retained PDF for REQ-e4b7f5aba7fb218c37f28002 is a variant-2 Comparison whose pages never print the comparison key's name

```json
{
  "id": "IRPT_YCDGEN-W4-S3",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~4",
  "surfaced_at": "2026-10-05T01:27:00Z",
  "one_line": "Cottonwood's retained PDF for REQ-e4b7f5aba7fb218c37f28002 is a variant-2 Comparison whose pages never print the comparison key's name",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "The order: Comparison REQ-e4b7f5ab... or REQ-7ea49c2d... are interchangeable sources for the Comparison map.",
  "world_is": "Both jobs are READY, variant comparison, one key (opal_long_term), template 14141824. REQ-7ea49c2d9b27957d0ea8888f's PDF (32 pages) prints the key's name 'Opal Long-Term' on 16 pages and a Security B section; REQ-e4b7f5aba7fb218c37f28002's PDF (28 pages) prints it on none (only the 'Sec A'/'Sec B' column heads and Security A holdings pages). The map is read from REQ-7ea49c2d9b27957d0ea8888f (source_pdf.request_id). The two are not interchangeable for FWD-3 evidence.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "each retained PDF read into OS temp by the job checkpoint's pdf_ref (the case_trace.py route), pdfplumber text, search for 'Opal Long-Term': 0 of 28 pages in e4b7f5ab, 16 of 32 pages in 7ea49c2d",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/case_trace.py: its 'the PDF prints exactly the chosen comparisons' link is the check e4b7f5ab would fail"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: an observation about a retained live artifact; this cell only reads. Owner 3.0.0_SA_CVO / 2.0.0_SA_COO~Y to decide whether REQ-e4b7f5ab is a defect of the vendor build or of the case."
}
```

## IRPT_YCDGEN-W4-S4 -- map_pdf reads 17 labels of the two PDFs wrongly; the maps carry the repaired printed label and say so in the note

```json
{
  "id": "IRPT_YCDGEN-W4-S4",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~4",
  "surfaced_at": "2026-10-05T01:27:00Z",
  "one_line": "map_pdf reads 17 labels of the two PDFs wrongly; the maps carry the repaired printed label and say so in the note",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-m-3: elements carry the printed label text the skeleton gives.",
  "world_is": "The skeleton gives a blank label to a first or last row (Asset Allocation Cash, Bond Sector Securitized, four Multi Fundamentals rows), glues a legend name into a label (Comparison Region Exposure), splits a wrapped long name over two lines (United Arab Emirates, Africa And Middle East / Indonesia) and reads the '5 percent' of the Monthly Value at Risk label as a number in the Multi. Each label in the maps is repaired from the page text order (numbers masked, nothing printed kept) and the element note says 'printed label repaired'; the Value at Risk stray is re-kinded text.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "comparison_map.json (13 notes) and multi_map.json (4 notes) containing 'printed label repaired'",
      "page text of Comparison pages 3, 4 and Multi pages 10, 13 read with numbers masked, in OS temp only"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: a map-side repair; owner 2.0.0_SA_COO~Y if map_pdf is to be fixed for the layout cell."
}
```

## IRPT_YCDGEN-S5 -- Research run YCD-R3-20261005T0219Z STOPPED: WAF_REFRESH_REQUIRED at step 7 (holdings_key_stats__c05)...

```json
{
  "id": "IRPT_YCDGEN-S5",
  "class": "OBSERVATION",
  "disposition": "UNDER_INVESTIGATION",
  "fabric": "laptop",
  "grounding": {
    "evidence": [
      "run record s3 key (bucket of the firm's store): irpt/cottonwood/state/ycharts_runs/request=YCD-R3-20261005T0219Z/run.json",
      "stop reason in that run record: WAF_REFRESH_REQUIRED at step 7 (holdings_key_stats__c05) status=202"
    ],
    "status": "GROUNDED"
  },
  "hazard_standing": "INERT",
  "one_line": "Research run YCD-R3-20261005T0219Z STOPPED: WAF_REFRESH_REQUIRED at step 7 (holdings_key_stats__c05) status=202",
  "project": "IRPT_YCDGEN",
  "spec_asserts": "C-SESSION: a firewall challenge or a lost session STOPS research; the run releases the lease, files a row and makes no retry storm.",
  "surfaced_at": "2026-10-05T02:20:17Z",
  "surfaced_by": "2.0.0_SA_COO~Y",
  "world_is": "The run STOPPED at step 7, call holdings_key_stats__c05: HTTP status 202, decision WAF_REFRESH_REQUIRED; no later call was sent, nothing was retried."
}
```

## IRPT_YCDGEN-S6 -- the firewall challenges the 7th request of any run, and table_data answers 404 for the holdings' tickers

```json
{
  "id": "IRPT_YCDGEN-S6",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~Y",
  "surfaced_at": "2026-10-05T02:25:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "Round-3 close measured two things that bound E1. (1) The firewall challenge falls on the 7th request of every run, not on one request's shape: runs 2, 3 and 4 were each challenged at step 7, at ~1.5 s, 8 s and 2 s spacing, and on three different calls. A run gets about 6 YCharts requests per window. (2) /indices/table_data answers 404 for chunks of the holdings' own tickers (4 of 4 chunks of 20, holdings_key_stats), so the coverage table's HELD_DATA route is wrong for these holdings",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "run 2 YCD-R1-20261004T1924Z: steps 1-6 ok, step 7 (portfolio_equity_exposure) 202 x-amzn-waf-action, spacing ~1.5 s (close/YCD-R1-20261004T1924Z_host_run.txt)",
      "run 3 YCD-R1-20261004T1944Z: same, --min-gap-s 8 (close/YCD-R1-20261004T1944Z_host_run.txt)",
      "run 4 YCD-R3-20261005T0219Z: steps 1-6 ok, step 7 (holdings_key_stats__c05, a 5-column call over 19 tickers) 202, lease spacing 2 s (close/YCD-R3-20261005T0219Z_host_run.txt); row S5",
      "run 4 run.json: holdings_key_stats__c01..c04 each HTTP 404 with no indicesData; holdings 99 rows from REQ-a618aa83's frozen input",
      "the round-2 probe runs A and B (2 calls each, 10 s apart) were not challenged"
    ]
  },
  "spec_asserts": "IRPT_YCDGEN-S3 and the round-2 drain packet: the step-7 challenge is request-shaped (the long table_data column list). Coverage table (round 2): HELD_DATA elements are computable from /indices/table_data over the holdings' tickers.",
  "world_is": "S3's reading is corrected: the challenge is count-shaped (the 7th request), at every spacing tried. And table_data with indices=<holding tickers> answers 404 like indices=P:<id>. So E1 needs a different security-level route (or the served path's own data) and a call budget of about 6 per window, measured before the next build. No retry was made; the session served Y-2 READY between runs."
}
```

## IRPT_YCDGEN-W3-S5 -- the base's test_computed_own_series_statistics asserts beta_1y is STATISTIC_UNKNOWN; 4.3 makes beta_1y a statistic id

```json
{
  "id": "IRPT_YCDGEN-W3-S5",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-05T05:40:06Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "Order YCD-l-4 says keep every existing test passing, but one existing assertion pins the pre-4.3 world: test_computed_own_series_statistics expects beta_1y to read STATISTIC_UNKNOWN:beta_1y. Contract 4.3 makes beta_1y a known id, so the assertion could not stay; it now uses kurtosis_1y (an id no contract names) and the same reason shape.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py @ f867ec3bca: line 205 asserted STATISTIC_UNKNOWN:beta_1y",
      "contract 4.3 (task order YCD-l-4 section 2): statistic ids alpha_<w>, beta_<w>, sharpe_<w>, sortino_<w>, var_monthly_<w>"
    ]
  },
  "spec_asserts": "The order: keep every existing test passing (14 at the base); the order's contract 4.3: beta_<w> is a statistic id.",
  "world_is": "Both cannot hold for that one assertion; the assertion's intent (an unnamed id is STATISTIC_UNKNOWN) is kept with an id no contract names. The other 13 existing tests are unchanged and pass (21 passed in all with the 7 new tests)."
}
```

## IRPT_YCDGEN-W3-S6 -- contract 4.3 names "a risk-free series Opal holds" but not its form (level or rate), nor how the inputs reach compute_element

```json
{
  "id": "IRPT_YCDGEN-W3-S6",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-05T05:40:06Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "4.3 does not say whether the risk-free input is a level (index) series or a rate series, nor the signature that carries benchmark and risk-free into the computation. Built: both are optional LEVEL series [[ms, level], ...] (or {series, key}), passed as benchmark= / risk_free= to statistic_of, compute_element and compute_all; the monthly return of each is taken from month-end levels exactly as for the portfolio. Conventions fixed where 4.3 is silent: sample (n-1) variance and covariance; alpha = (mean(rp-rf) - beta*mean(rb-rf)) x 12 in percent; Sharpe = mean excess x sqrt(12) / sample sd of excess; Sortino downside deviation about 0 over all n excess months; VaR = linear-interpolation 5th percentile of monthly returns in percent.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "contract 4.3 (task order YCD-l-4 section 2): 'a benchmark series kept by the run, and a risk-free series Opal holds'; the map wiring is a later cell (section 3)",
      "infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py: _risk_stat, _named_series, statistic_of(points, statistic, benchmark, risk_free)"
    ]
  },
  "spec_asserts": "4.3: each statistic computed only from held series, an input not kept or held reads NOT_AVAILABLE with INPUT_MISSING:<series>.",
  "world_is": "The wiring cell must hand a rate series through a level conversion (or this function must gain a rate form) if Opal's held risk-free series is a yield. Series names in the reason are `benchmark` and `risk_free`. Nothing was called or read from a store; only fixtures."
}
```

## IRPT_YCDGEN-W2-S6 -- no Opal table holds the held-data columns per holding; the feed is all YCharts security-level and the 6-request budget has no slack

```json
[
  {
    "id": "IRPT_YCDGEN-W2-S6",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
    "surfaced_at": "2026-10-05T05:50:00Z",
    "one_line": "YCD-o-4: no Opal table found holds any of the 158 held-data columns as the same per-holding figure, so all 158 feeds are YCHARTS_SECURITY; the probe map plans to exactly 6 requests (zero slack) through three expand calls, two general_data calls with 68 and 80 metric ids (request paths about 3.8K and 4.6K characters) and one fund_data series call, and the metric ids and the answer field are inferred.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order YCD-o-4 / contract 4.2: for each HELD_DATA column group find whether Opal holds the figure per holding (OPAL_HELD with table, field, key) else a YCHARTS_SECURITY call of at most 6 requests for 99 holdings.",
    "world_is": "Measured with schema and field-name reads only (no client figure, no vendor call): etf-classifications (key ticker, 2866 items, fields asset_class, sub_asset_class, name) and bd-securities (key ticker, 10965 items, same classes) hold a class LABEL per ticker, not a look-through share; opal-data-etfs bbg/<date>/characteristics.parquet (114 rows, key `security` = '<TICKER> US Equity') holds FUND_EXPENSE_RATIO, EQY_DVD_YLD_IND_NET, HB_OAS_EFF_DURTN, TOTAL_NUMBER_OF_HOLDINGS_IN_PORT, GICS_SECTOR_NAME, CNTRY_OF_DOMICILE for the ETF book's universe only, and gold/holding (188 rows) and gold/book (4 rows) are the four Opal ETF books and their constituents; their overlap with the upload's tickers was not measured (the client file is not read), and they are universes of other purposes, not the upload; no table found holds region, sector-share, maturity, credit-quality or market-cap-bucket shares per holding. With chunk 50 each expand call is 2 requests, so the 6-request bound allows exactly three calls: general_data twice (a single 148-id call would not fit one URL comfortably) and fund_data once. The metric ids are the table_data column ids, inferred to be the general_data metric ids, and the field `$.chart_data[*]` is the round-3 map's inferred general_data shape; the issuer's live run decides all three, and whether general_data admits 50 securities and 80 metric ids in one GET. A leaf that returns nothing for a holding is a NONE for that holding at run time, not at the map.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws dynamodb describe-table etf-classifications, bd-securities, trade-security-identifiers (read-only, key schema + item count; item field names only)",
        "s3 opal-data-etfs/bbg/2026-10-02/characteristics.parquet and gold/{book,holding}/date=2026-10-02 (parquet schema and row counts only)",
        "data/etfs/scripts/gold/etf_positioning_gold.py (the fields it reads: lines 1263-1280, 1521-1530)",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/feed_probe_map.json; check o-4.AC2 planned 6 requests (3 calls x 2 chunks of <=50)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "INERT: owner 2.0.0_SA_COO~Y at the round-4 close run; a refusal of the 80-id URL would split the metric list and needs a runner or budget ruling because the budget has no slack."
  }
]
```

## IRPT_YCDGEN-W4-S5 -- the skeleton gives no stat name to a comparison security's Risk Info row, and a baselines-only chart column is outside map_pdf's vector rule, so two m

```json
{
  "id": "IRPT_YCDGEN-W4-S5",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~4",
  "surfaced_at": "2026-10-05T06:09:07Z",
  "one_line": "the skeleton gives no stat name to a comparison security's Risk Info row, and a baselines-only chart column is outside map_pdf's vector rule, so two map-side steps remain after the label rule",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-m-4 and contract 4.4: the two maps' rows come from the label rule, with no map-side repair.",
  "world_is": "The 29 Multi and 21 Comparison rows come from the rule alone (map_pdf at this commit gives 573 and 423 elements, equal to the maps' skeleton counts). Two things the rule does not give: (1) the Multi's third-security Risk Info rows print the statistic's name only on the portfolio's line, so the skeleton labels all seven 'Risk Info: iShares Russell 2000 ETF'; the maps carry the statistic name copied from the key-1 row printed just above, as round 3 did for the key-1 rows. (2) Comparison page 8's portfolio Bond Maturity column is drawn with baseline rules only; map_pdf's vector-chart rule needs a bar, so the chart is listed in the map as p8.e33 from the page's shapes, and p8.e03 (the comparison key's bars) is sourced to comparison_bond_exposure at key_index 1. The existing key-1 labels repaired in round 3 (W4-S4) were not re-derived by the rule.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "multi_map.json p10.e21 to p10.e27 labels; comparison_map.json p8.e03 and p8.e33",
      "page 10 of REQ-329a56182b2668d44a28c8d7 and page 8 of REQ-7ea49c2d9b27957d0ea8888f read in OS temp: statistic names only on the IRPT line; the p8 portfolio column holds 0.9 pt wide axis rules and no bar"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: map-side labels and one listed chart. Owner 2.0.0_SA_COO~Y: a later map_pdf cell could carry the stat name down a Risk Info block and list a baselines-only column."
}
```

## IRPT_YCDGEN-W4-S6 -- round 3's map sourced a Multi holdings row as comparison key 2 because the third security's row was missing; with that row listed, p21.e06 is a holdin

```json
{
  "id": "IRPT_YCDGEN-W4-S6",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~4",
  "surfaced_at": "2026-10-05T06:09:07Z",
  "one_line": "round 3's map sourced a Multi holdings row as comparison key 2 because the third security's row was missing; with that row listed, p21.e06 is a holdings row and 129 existing data-row labels moved by their rule ordinal",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-m-4: element ids are never renumbered; the m-3 rows W4-S4 names are added.",
  "world_is": "multi_map.json p21.e06 was sourced to comparison_standardized_returns at key_index 2 ('row printed after the portfolio's own row, taken as comparison key 2'), but the row it stands for is Global X's; the key-2 row (iShares Russell 2000 ETF) was one of the dropped rows. p21.e06 is now BUILDER_ONLY like its neighbours and the new key-2 row is p21.e21. Separately, a masked 'data row N' label counts the rows of its heading, so the 50 added rows moved the ordinal of 129 existing elements (83 Comparison, 46 Multi, including the four Waivers rows now masked as data rows); their labels were updated to the rule's ordinal, their ids and sources kept. A consumer that matched an element by its old 'data row N' label would now miss it.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git diff of multi_map.json and comparison_map.json (labels only on the 129; p21.e06 source)",
      "page 21 of REQ-329a56182b2668d44a28c8d7: the iShares Russell 2000 ETF row is printed between the Opal Ultra Long-Term row and the Global X row"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: the maps have no reader yet that keys on a data-row label (layout reads source and ids). Owner 2.0.0_SA_COO~Y."
}
```

## IRPT_YCDGEN-S7 -- E5's --end driver is false: fund_data ignores startDate and endDate

```json
{
  "id": "IRPT_YCDGEN-S7",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~Y",
  "surfaced_at": "2026-10-05T06:43:17Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "E5's driver is false: /charts/fund_data.json ignores startDate and endDate. Four runs with --end 2026-09-30 and 2026-10-02, with zoom=max and without zoom, kept byte-identical level series (23,651 points through 2026-10-02, the last close), so a different --end cannot drive FWD-2's true arm",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "runs YCD-R4-20261005T0552Z-A (--end 2026-09-30) and -B (--end 2026-10-02), zoom=max: portfolio_level_series sha256 539579bbaee2.. in both; B reads changed_since_previous false (close/YCD-R4-20261005T0552Z_host_run.txt, run.json read 06:1xZ)",
      "A also reads false against run 3 (YCD-R3-20261005T0219Z, empty start and end)",
      "runs YCD-R4-20261005T0620Z-D (--start 2025-10-01 --end 2026-09-30) and -E (--end 2026-10-02), no zoom (close/e5_dated_level_map_r4.json): sha256 ef306d6162e1.. in both; E reads false (close/YCD-R4-20261005T0620Z_host_run.txt)",
      "the kept series of A and D both hold 23,651 points, the first in 1962 and the last on 2026-10-02 (dates read, no value)"
    ]
  },
  "spec_asserts": "CTO round-3 analysis E5 (ROUND_ANALYSIS_IRPT_YCDGEN_ROUND3_20261005.md:28-30, :66): a run whose --end differs from the indexed run's changes that call's answer under the same call name, so two runs with different --end dates show changed_since_previous true.",
  "world_is": "The endpoint returns the whole series whatever the dates, so --end is not a driver. The false arm is measured twice (B vs A, E vs D). The issuer substitutes a lever that does change the answer under one call name: zoom=5y then zoom=max (2 requests, run at ~D's next free slot), and records the result in the round-4 packet. No retry was made."
}
```

## IRPT_YCDGEN-S8 -- E1's live probe: the held-data feed calls answer 400 (invalid security items and metric ids)

```json
{
  "id": "IRPT_YCDGEN-S8",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~Y",
  "surfaced_at": "2026-10-05T06:43:17Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "E1's live probe: all 6 requests of feed_probe_map.json answered HTTP 400. general_data says security_needed ('At least one valid, included security is required') on the 68-metric call and metrics_needed ('Metrics X-Axis needs to have more than one metric') on the 80-metric call; fund_data over the holdings says 'There are no valid items on this chart'. /securities/securities_info answers 200 for a public ticker with its security_id",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "run YCD-R4-20261005T0620Z-C: 6 of 6 requests HTTP 400, COMPLETE, no challenge at 8 s spacing; holdings from REQ-a618aa83 (99 rows; tickers not printed)",
      "kept bodies read for err_code and err_message only: step 01 security_needed, step 03 metrics_needed, step 05 text/plain no valid items",
      "run YCD-R4-20261005T0552Z-A step 05 security_info_probe (securities=AAPL): 200, a list of 1 with security_id and display_security_id",
      "run A step 06 security_price_probe (general_data, id:AAPL price, xAxis time): 500, BACKOFF stop (same in run B)"
    ]
  },
  "spec_asserts": "Contract 4.2 / YCD-o-4: feed_probe_map.json's calls fetch the 158 held-data figures per holding by passing the holdings' tickers as id:<ticker> items joined by ',' with table_data column ids as general_data metric ids (W2-S6 marked the ids and the answer field as inferred).",
  "world_is": "The ticker items are not valid YCharts security items as sent (the expand join puts ',' after an item that already ends ',,', and a ticker may not be the YCharts id), and the region and maturity column ids are not valid general_data metrics. Next: resolve each holding through /securities/securities_info to its security_id, send items with no extra separator, and validate metric ids on one public security before a holdings run. The 158 rows keep feed YCHARTS_SECURITY; no element is fed yet, so E6 has no new figures to render."
}
```

## IRPT_YCDGEN-W1-S2 -- lookup.py needs a region the order does not name

```json
{
  "id": "IRPT_YCDGEN-W1-S2",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~1",
  "surfaced_at": "2026-10-05T11:07:34Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "Contract 5.4's lookup needs an S3 client on the firm's research principal and the order names no region source, so lookup.py takes --region (default us-east-1) and calls runner.research_s3; the issuer confirms the region at the first live lookup.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/ycharts/research/lookup.py main(): --region default; runner.py research_s3(boto3, region, firm, request_id); runner._compose reads the region from resident bindings, which a lookup does not load"
    ]
  },
  "spec_asserts": "Contract 5.4: `python lookup.py --firm <f> --request <REQ> --call <name>` prints the call's kept record, reading through the keeper's store.",
  "world_is": "The three flags alone give no region and no S3 client; the runner's region comes from resident_bindings.json, which the lookup does not load. A tested default (us-east-1, the estate's region) with an override flag was added; the tests inject a fake S3 client and never reach this line."
}
```

## IRPT_YCDGEN-W2-S7 -- the model portfolio's portfolio_info answer names its benchmark by display name, not by a YCharts id; the map'

```json
{
  "id": "IRPT_YCDGEN-W2-S7",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
  "surfaced_at": "2026-10-05T11:38:47Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "YCD-p-5: the model portfolio's portfolio_info answer names its benchmark by display name, not by a YCharts id; the map's benchmark call uses ^SPXTR from the COO's record",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_responses/request=YCD-R4-20261005T0700Z-G/step=01_portfolio_info.json read-only: body_json[0] keys include `benchmark` (a string, the display name 'S&P 500 Total Return') and no benchmark id field; the other keys are security_id, display_security_id, id, security_name",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/COMPARISON_BENCHMARK_NEVER_RENDERS_20260927.md line 28 pairs the display name 'S&P 500 Total Return' with `^SPXTR`; overview_map.json has no p7 element naming a benchmark, so the source PDF's p7 names none",
      "overview_map.json call benchmark_level_series: securities=id:^SPXTR,include:true,, (the same fund_data level-series params as portfolio_level_series); no vendor call was made by this worker"
    ]
  },
  "spec_asserts": "Contract 5.3: the benchmark level series is one fund_data call for the benchmark the source PDF's p7 names, else the one portfolio_info's answer names.",
  "world_is": "portfolio_info names a display name only; the id ^SPXTR is taken from a prior record (pairing name and id), not from this answer. If YCharts does not accept ^SPXTR as a fund_data security id the benchmark call answers non-2xx, benchmark_from_kept returns None and alpha and beta read INPUT_MISSING:benchmark; nothing is approximated. The issuer's live window confirms or corrects the id."
}
```

## IRPT_YCDGEN-W2-S8 -- AC1 requires every map call to be read by an element, so the benchmark call is read by a new map element p7.e1

```json
{
  "id": "IRPT_YCDGEN-W2-S8",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
  "surfaced_at": "2026-10-05T11:38:47Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "YCD-p-5: AC1 requires every map call to be read by an element, so the benchmark call is read by a new map element p7.e15 that the source PDF does not print",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/p-5.AC1.py: unread = calls whose name is no element's source.call; PASS needs none",
      "overview_map.json: element p7.e15 'Benchmark level series (input to Alpha and Beta)', kind chart, source call benchmark_level_series; the 6 statistic elements read portfolio_level_series, so no existing element could carry the benchmark call",
      "the page renders p7.e15 as a line chart of the benchmark's level over the run window; the map now holds 254 elements (253 + 1) and 8 calls (plan 8 requests for 99 holdings)"
    ]
  },
  "spec_asserts": "Contract 5.1: the Overview map keeps only the calls an element reads, counting YCD-p-5's benchmark call; contract C-MAP labels are printed label text only.",
  "world_is": "The benchmark call can only stay in the map if some element reads it, so one element was added whose label is not printed text of the source PDF. Option for the issuer: drop p7.e15 and the check's read test for this call (the layout reads the benchmark by call name, BENCHMARK_CALL, not through an element)."
}
```

## IRPT_YCDGEN-W2-S9 -- the held risk-free series is the portal's FRED 3M Treasury yield, coded for a 2-year history, so only the 1y w

```json
{
  "id": "IRPT_YCDGEN-W2-S9",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
  "surfaced_at": "2026-10-05T11:38:47Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "YCD-p-5: the held risk-free series is the portal's FRED 3M Treasury yield, coded for a 2-year history, so only the 1y window of alpha, Sharpe and Sortino can compute; and one `statistic` per five-column element prints one window",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "comp-which 'risk-free rate treasury yield series' timed out inside its 90 s budget (rc, no result); comp-estate --definitions has no risk-free or Treasury definition; the search then fell back to Grep over data/ and infra/aws/lambda",
      "infra/aws/lambda/fred-data-ingestion/ingest_yield_curve_fred.py: series DGS3MO displayed as 'US Treasury 3M', output s3://opal-data-portal-v2/json/macro/yield_curve_fred.json, list of {date, value}, fetch_series(lookback_years=2) and fetch_all_treasury_yields(lookback_years=2) (a coded default, the object itself not read: the order names no S3 read for it)",
      "infra/aws/lambda/fred-macro-ingestion/ingest_fred_macro.py: group 'Treasury Yields' DGS3MO writes json/macro/macro_data_fred.json with a trailing-12-month window only",
      "layout_overview.py RISK_FREE_SOURCE / risk_free_levels(): the yield becomes a level series (starts 100, grows at each earlier observation's yield, days/365); CLI --risk-free takes a copy of that object",
      "overview_map.json p7.e02,e03,e05,e06,e07,e08: `statistic` is one id (the first column's window: alpha_1y, beta_1y, sharpe_1y, sortino_1y, max_drawdown_1y, var_monthly_1y) over five `columns`; compute_element reads `statistic` only, so each p7 element prints one value, and the three other OWN_SERIES elements with statistic null (p2.e08, p2.e13, p6.e22) still read STATISTIC_UNKNOWN:None"
    ]
  },
  "spec_asserts": "Contract 5.3: a risk-free series Opal holds, named by table and field; 4.3: alpha, Sharpe and Sortino for 1y, 3y, 5y, 10y and 15y; 3.4: one statistic per computed element.",
  "world_is": "Opal holds a Treasury 3M yield series (object and key named above) but its coded history is 2 years, so alpha_3y and longer would read SERIES_TOO_SHORT even with the series passed. The 1y window is the only one this wiring can make computable, which is why every p7 element carries its _1y id. A multi-column element needs a per-column compute (a dict of window to value) to print the five windows the PDF shows; that is not in this cell's contract and was not built."
}
```

## IRPT_YCDGEN-W3-S7 -- Opal holds the held-data figures for 37 of Y-5's 99 holdings at most, no price series for the rest, and the order names no loader for the census's sources

```json
{
  "id": "IRPT_YCDGEN-W3-S7",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-05T12:06:00Z",
  "one_line": "YCD-h-5 census over Y-5's 99 holdings: 86 of 158 HELD_DATA rows OPAL_HELD (83 of 153 groups) but every FED figure is label-grain or field-grain over at most 37 of 99 holdings (asset-class labels 97 of 99), 72 rows NOT_HELD, and `census`/`value_of` take already-read rows because 5.2 names no loader.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Contract 5.2 / cell YCD-h-5: the sources are Opal's security tables, prices and classifications; each group's weights are the holdings' amounts renormalized over the held holdings, so a held figure stands for the portfolio's.",
  "world_is": "Measured read-only, counts only (no ticker or amount printed or written): etf-classifications 97 of 99 holdings (asset_class: equity, fixed_income, multi_asset, structured, commodities, alternatives; no cash label), bd-securities 98 of 99 (a label), opal-data-etfs bbg characteristics 37 of 99 (all 37 single stocks, domicile US; EQY_DVD_YLD_IND_NET non-null for 27, GICS_SECTOR_NAME, CNTRY_OF_DOMICILE, CUR_MKT_CAP, BETA_ADJ_OVERRIDABLE for 37; FUND_EXPENSE_RATIO, HB_OAS_EFF_DURTN, TOTAL_NUMBER_OF_HOLDINGS_IN_PORT null for all 99), gold/holding 47 (it is derived from the characteristics row), history_topup PX_LAST 37, fund_daily and etf_history 0, trade-security-identifiers 8, opal-harvest-security-metrics 0. So Opal holds no price series for 62 of 99 holdings (p12.e04 is NOT_HELD) and no look-through share of any kind: the 83 FED groups are sector and region LABEL shares of the 37 stocks (100 or 0 per holding), asset-class label shares (stock, bond, other) and three field means (dividend_yield 27 of 99, weighted_avg_market_cap 37, net_expense_ratio measured empty so NOT_HELD). A FED value is renormalized over its held holdings, so the sector and region elements describe the 37 stocks only; the held-of count is in `value_of`'s method, and the layout (YCD-w-5) shows it in the 3.5 trace. The order names no way to read the sources, so held_data takes ready rows (`sources`, `held_rows`) and reads no store; the census's reads were made by a scratch script that is not committed, so the issuer or YCD-w-5 loads characteristics (parquet) and etf-classifications (DynamoDB scan) before calling it. Region and super-sector mappings are my own (decided countries US CA GB CH JP DE FR IE NL AU; GICS sectors to the Morningstar-style group names) and the group id is `group_id_of(columns)` (the columns joined by '+', 'level_series' for the no-column row); each feed also carries `group`.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "runner.read_holdings over REQ-a618aa83407689bc95193a01 (99 rows, 99 distinct, basis USD), counts only",
      "s3 opal-data-etfs bbg/2026-10-02/{characteristics,fund_daily,history_topup}.parquet, etf_history.csv, silver/holdings/2026-10-04.parquet, gold/{book,holding}/date=2026-10-02 (schema and key overlap counts)",
      "dynamodb scan of etf-classifications, bd-securities, trade-security-identifiers, opal-harvest-security-metrics (field names, key overlap counts, label value counts)",
      "data/etfs/scripts/gold/etf_positioning_gold.py lines 1263-1280 (gold holding yield and beta are the characteristics row's)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: owner 2.0.0_SA_COO~Y at the round-5 close; a wider feed (a per-holding look-through table) is a data decision, not a cell."
}
```

## IRPT_YCDGEN-W2-S10 -- contract 3.5's 0.95 coverage floor is not applied to an OPAL_HELD element; its held-of count is the honesty carrier

```json
{
  "id": "IRPT_YCDGEN-W2-S10",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
  "surfaced_at": "2026-10-05T12:58:00Z",
  "one_line": "Contract 3.5's 0.95 coverage floor is not applied to an OPAL_HELD element (the issuer's spawn ruling renormalizes over the held holdings), so a held value can print at any coverage with its held-of count in the trace and on the page.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Contract 3.5: below 0.95 coverage a computed element is NOT_AVAILABLE with reason COVERAGE_BELOW_0.95. Contract 5.2 / the issuer's ruling at spawn: an OPAL_HELD value is renormalized over the held holdings and its method says how many of how many.",
  "world_is": "layout_overview._compute_opal_held applies no floor: trace.coverage is the weight share of holdings carrying the figure (informational) and the trace for an OPAL_HELD value adds `held` and `of` beside `method` ('OPAL_HELD: <held_data method> (held n of N)'); the page prints 'Opal-held data: n of N holdings.' under the value. Measured on Y-5 by the census (row W3-S7): the figures stand on at most 37 of 99 holdings, so a sector or region share would print on roughly that weight share; only the page note and the trace say so. The wiring also calls two of held_data's module-private helpers (_held_pairs, _decimal) for the coverage share, because value_of returns counts but not the weight share. The default loader readers (S3 get of the latest dated bbg characteristics.parquet, paginated DynamoDB scan of etf-classifications) were exercised against fakes in tests and the layout was CLI-confirmed (bucket layout, table key, column names) but not run live by this cell.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py _compute_opal_held and load_held_rows (branch wk-ycdgen-r5-5)",
      "tests test_layout_overview.py -k opal_held: 6 passed",
      "aws s3 ls s3://opal-data-etfs/bbg/ (dated folders and constituents/), describe-table etf-classifications (hash key ticker), characteristics.parquet schema read into temp and deleted"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: owner 2.0.0_SA_COO~Y at the round-5 close; if a floor on held values is wanted it is one constant in _compute_opal_held."
}
```

## IRPT_YCDGEN-S9 -- the held risk-free object stopped updating on 2026-08-05 (last observation 2026-08-04)

```json
{
  "id": "IRPT_YCDGEN-S9",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "4.0.0_SA_CRO",
  "surfaced_at": "2026-10-05T19:55:00Z",
  "one_line": "The held risk-free object (portal FRED Treasury yields) was last written 2026-08-05 and its last observation is 2026-08-04, so it is two months behind as well as two years short.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Handoff HANDOFF_TO_CRO_ONPREM_GENERATION_20261005.md section 6 family 5 and row IRPT_YCDGEN-W2-S9: opal-data-portal-v2/json/macro/yield_curve_fred.json is written daily (EventBridge 6pm ET) with a 2-year lookback; W2-S9 says the object itself was not read.",
  "world_is": "Read 2026-10-05 ~19:5xZ: head-object LastModified 2026-08-05T23:02:30Z; body data_as_of 2026-08-05, generated_at 2026-08-05T23:02:29Z; series 'US Treasury 3M' has 499 observations, first 2024-08-05, last 2026-08-04. No later write exists at that key. Whether the ingestion schedule is disabled, failing, or writing elsewhere was not read. An in-house 1y alpha, Sharpe or Sortino computed from this object today would use a risk-free series ending two months before the report date.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "boto3 s3 head_object + get_object opal-data-portal-v2 json/macro/yield_curve_fred.json (ContentLength 675314), keys and first/last list entries printed",
      "positive control: same session read opal-data-bd silver/historical_prices.parquet with max date 2026-10-02"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: no served report reads this object today (layout_overview.py takes it as a CLI file). Owner of the ingestion Lambda is outside this project; placed here because the in-house build would make the object load-bearing. Feasibility analysis: docs/briefs/irpt-ycharts-inhouse-generation-feasibility-20261005.md."
}
```

## IRPT_YCDGEN-W2-S11 -- AC5 pin @62301f71e0 predates the v1 schema file; v1_untouched pins by content hash and published copy

```json
{
  "id": "IRPT_YCDGEN-W2-S11",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
  "surfaced_at": "2026-10-05T21:21:00Z",
  "one_line": "AC5 asks the v1 schema file be byte-identical to its pin @62301f71e0, but that pin is the PRD pin and the file did not exist at it; v1_untouched pins the file by content hash and by its byte-equal published copy instead.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Order AC5 / PRD v0.28 item 29: the generated v1 schema _contracts/AnalysisReport.schema.json (pinned @62301f71e0) is untouched; test -k v1_untouched compares the file to its pin.",
  "world_is": "git cat-file at 62301f71e0 holds no infra/aws/lambda/investor-reporting/_contracts/AnalysisReport.schema.json (git show: path exists on disk, but not in 62301f71e0); the file was added later (c4214773c9) and edited since (98d579cd1b date_claim, 1dae563e21), 366 lines at the cut base b091a522e9. 62301f71e0 is the PRD pin the schema is generated from. The test therefore asserts sha256 1bd0dc85847690b277e3a3011bcbe500a02820792cd53a38a1201fc3c55d153f (measured at b091a522e9) and byte-equality with docs/contracts/investor-reporting/v1/AnalysisReport.schema.json, the published copy.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git show 62301f71e0:infra/aws/lambda/investor-reporting/_contracts/AnalysisReport.schema.json -> fatal: exists on disk, but not in 62301f71e0",
      "git log --oneline on the file: 1dae563e21, 98d579cd1b, c4214773c9",
      "sha256sum of the _contracts file and the docs/contracts copy are equal"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: the criterion passes on the stated substitute; a later legitimate v1 edit would need the hash constant in test_analysisreport_v2.py updated."
}
```

## IRPT_YCDGEN-W2-S12 -- R4 leaves v2 section typing open; the schema fixes nullability, inputs_as_of and coverage one way

```json
{
  "id": "IRPT_YCDGEN-W2-S12",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
  "surfaced_at": "2026-10-05T21:21:00Z",
  "one_line": "Contract R4 leaves the OPAL_ENGINE section's nullability, the inputs_as_of shape, the coverage type and the VALUE-branch reason open; the v2 schema fixes them one way that a consumer may need to confirm.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "R4 names the section members section_id, section_type, units, as_of_date, status, reason, method, coverage (page optional) and effective_inputs.inputs_as_of 'the as-of date of each input', without types or nullability.",
  "world_is": "AnalysisReport.v2.schema.json chooses: inputs_as_of is an object of input name to YYYY-MM-DD, at least one; section coverage is a number 0..1 or null; as_of_date is a date string, or null only when status is NOT_AVAILABLE (a NOT_IN_THIS_VERSION section has no date of its own); value and method and coverage are required on every section; reason is required, a string from the closed set (INPUT_MISSING:<name> with a non-empty name), and value null when NOT_AVAILABLE; under VALUE reason is absent or null and value is a number or string. computation_validation.status reuses v1's CERTIFIED/UNCERTIFIED/FAILED. Any of these is one line in the schema to change.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/_contracts/AnalysisReport.v2.schema.json $defs.opal_engine",
      "IRPT_BCKEND PRD v0.28 item 29 read at HEAD: no types given for these members",
      "tests test_analysisreport_v2.py: 5 passed"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: no producer or consumer reads the v2 schema yet."
}
```

## IRPT_YCDGEN-W1-S3 -- the round-6 methods are not in overview_map.json, and pricing=False is a parameter whose default stays True

```json
{
  "id": "IRPT_YCDGEN-W1-S3",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~1",
  "surfaced_at": "2026-10-05T21:25:51Z",
  "one_line": "Round 6 b-6's classified elements need three new computed method names the shipped overview_map.json does not carry, and the no-pricing mode is switched on by pricing=False (default True), so the producer that calls build must pass it.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y",
  "spec_asserts": "YCD-b-6 / R2: price-based elements print NOT_AVAILABLE with NOT_IN_THIS_VERSION; allocation by asset class and sub asset class is computed; the order also says keep every existing test in test_layout_overview.py passing.",
  "world_is": "Existing tests call compute_element, compute_all, build and main with no mode argument and expect OWN_SERIES statistics to compute (test_six_statistic_*, test_wired_both_render_paths_pass_the_two_series), so the no-pricing behaviour cannot be the default. It is built as pricing=False on compute_element, compute_all and build, and --no-pricing on main; default True is the YCharts-priced path, unchanged. The new computed methods are HOLDINGS_CLASSIFIED, ALLOCATION_ASSET_CLASS and ALLOCATION_SUB_ASSET_CLASS (constants CLASSIFY_METHODS); deliverables/maps/overview_map.json carries none of them (its computed methods are OPAL_HELD 158, OWN_SERIES 9, and 65 BUILDER_ONLY), so a map the a-6 producer uses must name them. A producer that calls build or compute_all without pricing=False prints the OWN_SERIES elements from kept answers (INPUT_MISSING:<call> when nothing is kept), not NOT_IN_THIS_VERSION.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python count of overview_map.json elements by source.computed: OPAL_HELD 153+4+1 (158 per the existing map test), OWN_SERIES 8+1, BUILDER_ONLY 52+9+2+2, plain 11+4+4+3",
      "pytest test_layout_overview.py -k not_in_this_version: 1 passed (pricing=False on the six price-based forms and the 9 real OWN_SERIES elements; positive control with pricing on computes)",
      "layout_overview.py compute_element, compute_all, build, main signatures on branch wk-IRPT_YCDGEN-61"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "ARMED until a-6's order names pricing=False (or its own map) at its build call and its test asserts a price element reads NOT_IN_THIS_VERSION through the producer. Owner 2.0.0_SA_COO~Y at the a-6 cut."
}
```

## IRPT_YCDGEN-W1-S4 -- R2's closed reason set is narrower than the module's other reasons, and _scan_classifications is kept (retired from the path) because an existing test calls it

```json
{
  "id": "IRPT_YCDGEN-W1-S4",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~1",
  "surfaced_at": "2026-10-05T21:25:51Z",
  "one_line": "R2 states a closed reason set (COVERAGE_BELOW_0.95, STALE_INPUT, INPUT_MISSING:<name>, NOT_IN_THIS_VERSION); the module's existing paths still produce NOT_HELD:<reason>, SERIES_TOO_SHORT, OUTSIDE_TIME_BUDGET and others, and plain vendor-call elements carry no price marker.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "R2: two states only, a value or NOT_AVAILABLE with a reason from the closed set COVERAGE_BELOW_0.95, STALE_INPUT, INPUT_MISSING:<name>, NOT_IN_THIS_VERSION. R1: the module's own _scan_classifications path is removed from the Overview path.",
  "world_is": "The new classified methods use only COVERAGE_BELOW_0.95 and INPUT_MISSING:<name>, and pricing=False uses NOT_IN_THIS_VERSION. The older OPAL_HELD path still returns NOT_HELD:<reason> (pinned by existing tests test_opal_held_*), the series methods return SERIES_TOO_SHORT / SERIES_INVALID / STATISTIC_UNKNOWN:<id>, and a map-less call returns OUTSIDE_TIME_BUDGET; none are in the closed set. A plain (non-computed) element reading a YCharts call has no marker saying it is price-based, so pricing=False does not turn it into NOT_IN_THIS_VERSION: with nothing kept it prints the existing 'YCharts gave no answer' line. _scan_classifications is no longer called by load_held_rows, main, compute_all or build (test no_second_classification_read asserts it); the function body stays, marked retired, because the existing test test_opal_held_default_readers_are_read_only_s3_get_and_dynamodb_scan calls it directly and the order says keep every existing test passing.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "layout_overview.py on branch wk-IRPT_YCDGEN-61: reasons raised by _NA(...) in _compute_held, _compute_opal_held, statistic_of, compute_element",
      "pytest test_layout_overview.py: 38 passed (the 6 held tests and the scan test unchanged)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: the a-6 producer maps each reason to the v2 schema's status; whether NOT_HELD:<reason> and the series reasons map into the closed set is its and YCD-s-6's call. Deleting the retired scan function and its test is a one-line follow-up for a cell that owns the test."
}
```

## IRPT_YCDGEN-W1-S5 -- the criterion expectations anchor at the line start, and this shell forces ANSI colour into pytest output

```json
{
  "id": "IRPT_YCDGEN-W1-S5",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~1",
  "surfaced_at": "2026-10-05T21:25:51Z",
  "one_line": "With FORCE_COLOR=3 in the environment the literal pytest invocations print their summary line behind ANSI escapes, so an expectation anchored at the line start (^[1-9][0-9]* passed) does not match the raw bytes.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Proof of spec AC1-AC6: each invocation's output matches ^[1-9][0-9]* passed (AC6 ^[0-9]+ passed).",
  "world_is": "env in the worker shell shows FORCE_COLOR=3; the last output line of `python -m pytest ... -q -p no:cacheprovider -k not_in_this_version` begins with bytes 033 [ 3 2 m 033 [ 3 2 m 033 [ 1 m then '1 passed'. With the escape sequences stripped the line reads '1 passed, 37 deselected' and each criterion matches. The recorded outputs in the proof instance are the stripped lines, and the raw-bytes difference is stated here.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "env | grep -i color -> FORCE_COLOR=3",
      "od -c of the pytest summary line printed 033 [ 3 2 m before the count"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: a checker that runs the invocation with FORCE_COLOR unset, or strips ANSI, reads the same pass."
}
```

## IRPT_YCDGEN-W1-S6 -- the retained-report validator and the publication path are bound to the v1 AnalysisReport; an OPAL_ENGINE document is refused there

```json
{
  "id": "IRPT_YCDGEN-W1-S6",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~1",
  "surfaced_at": "2026-10-05T21:56:59Z",
  "one_line": "reports/resident_installed.py binds ANALYSIS to AnalysisReport.schema.json (v1) and publisher.py / publication_worker.py accept only a vendor metadata key set, so an OPAL_ENGINE document cannot be persisted or published on the existing path.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y",
  "spec_asserts": "Order a-6 section 3: if publisher.py or publication_worker.py would reject an OPAL_ENGINE document, file a row naming the line; the document is written where OwnedAnalysisReader reads a report.",
  "world_is": "infra/aws/lambda/investor-reporting/reports/resident_installed.py:47 REPORT_SCHEMAS = {ANALYSIS: AnalysisReport.schema.json} and :121 (the validator the ReportRepository is built with, so persist and get both validate against v1: an OPAL_ENGINE document carries opal_artifact and computation_validation, which the v1 schema's additionalProperties false refuses). ycharts/generate/publisher.py:107 and ycharts/generate/publication_worker.py:47 require set(metadata) == {request_ref, vendor_artifact, effective_inputs, release}. opal_producer.produce calls reports.persist directly on the injected repository, so it does not pass through the publisher, but the repository's validate callable is the issuer's to build against the v2 schema.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "reports/resident_installed.py:47,121@wk-IRPT_YCDGEN-63",
      "ycharts/generate/publisher.py:107@wk-IRPT_YCDGEN-63",
      "ycharts/generate/publication_worker.py:47@wk-IRPT_YCDGEN-63",
      "opal_producer tests persist through a recording fake; no test builds the real ReportRepository"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "ARMED: the first Opal request persisted through a repository validating v1 is refused at persist ('report schema validation failed'), loudly. Another lane's files; the owner cuts the change (a v2-aware validate callable keyed by provider)."
}
```

## IRPT_YCDGEN-W1-S7 -- OwnedAnalysisReader reads vendor members an OPAL_ENGINE report does not carry

```json
{
  "id": "IRPT_YCDGEN-W1-S7",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~1",
  "surfaced_at": "2026-10-05T21:56:59Z",
  "one_line": "ops/owned_report.py reads report['extraction_validation'] in sections() and report['vendor_artifact'] / release.protected_pdf_ref in pdf(); an OPAL_ENGINE document has computation_validation and opal_artifact instead.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y",
  "spec_asserts": "Order a-6 section 1 and PRD item 29: a consumer that needs a vendor member rejects the document; the v2 document is written where OwnedAnalysisReader reads a report.",
  "world_is": "infra/aws/lambda/investor-reporting/ops/owned_report.py:49 builds the public projection with report[key] for request_ref, sections and extraction_validation (KeyError on an OPAL_ENGINE document, which has no extraction_validation); :126-133 pdf() needs release.protected_pdf_ref with server_only true and vendor_artifact.sha256/byte_length, and the OPAL_ENGINE release carries released_revision only (the artifact is opal_artifact). The class is not edited by this cell.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ops/owned_report.py:49,125-133@wk-IRPT_YCDGEN-63"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "ARMED: reading or downloading an Opal report through the existing reader fails (KeyError / ANALYSIS_PDF_NOT_RETAINED) until the reader's owner reads provider and opal_artifact. Whether the PDF is reached through release.protected_pdf_ref (the producer does not write one) or opal_artifact is that owner's decision."
}
```

## IRPT_YCDGEN-W1-S8 -- under pricing=False the layout still prints YCharts wording on a report with no YCharts data

```json
{
  "id": "IRPT_YCDGEN-W1-S8",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~1",
  "surfaced_at": "2026-10-05T21:56:59Z",
  "one_line": "layout_overview.py prints 'Not available from YCharts' data endpoints.' for builder-only elements, 'YCharts gave no answer' / 'outside the run's time budget' for vendor-call elements, and a 'Data: YCharts' footer on every page of the Opal report.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Order a-6 R2: every price-based element prints NOT_AVAILABLE with NOT_IN_THIS_VERSION; the producer calls build with pricing=False.",
  "world_is": "layout_overview.py:56-59,67,943 and the footer in build (:1088): only elements the layout classes as price-based (_price_based) print the NOT_IN_THIS_VERSION line. In the real Overview map the 65 BUILDER_ONLY and 22 call-sourced elements are not price-based by that test, so the page prints the YCharts / time-budget lines while run.json and the AnalysisReport section carry reason NOT_IN_THIS_VERSION (the producer's closed-set mapping). The footer credit 'Data: YCharts' prints on pages that hold no YCharts figure.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "layout_overview.py:56,57,59,67,943,1088@wk-IRPT_YCDGEN-63",
      "opal_producer on the real overview_map.json (scratch run): 65 BUILDER_ONLY, 22 VENDOR_SOURCED, 9 OWN_SERIES are NOT_AVAILABLE / NOT_IN_THIS_VERSION in run.json"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT for the record (the document and run.json are consistent); the printed page is not. layout_overview.py is YCD-b-6's merged file, outside this cell's paths."
}
```

## IRPT_YCDGEN-W1-S9 -- three choices the order left to the producer: the classified element list, the reason mapping and a table value inside a scalar section

```json
{
  "id": "IRPT_YCDGEN-W1-S9",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~1",
  "surfaced_at": "2026-10-05T21:56:59Z",
  "one_line": "The layout has no element list of its own for the three classified methods, the closed reason set excludes NOT_HELD:<r>, OUTSIDE_TIME_BUDGET and METHOD_UNKNOWN, and the v2 section value is number|string|null while the layout's table values are lists.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Order a-6 section 3: the producer reads the layout's own element list for the classified methods, never the map; R2 two states with a closed reason set; R4 section value.",
  "world_is": "layout_overview.py defines the method names (HOLDINGS_CLASSIFIED, ALLOCATION_ASSET_CLASS, ALLOCATION_SUB_ASSET_CLASS) and consumes elements from the map, but holds no element list. opal_producer builds three elements (ids opal.classified.holdings, .asset_class, .sub_asset_class, on a page after the map's last) from those constants and adds them to a copy of the map when the map has none. Reasons: NOT_HELD:<r> -> INPUT_MISSING:held_<group>; OUTSIDE_TIME_BUDGET -> NOT_IN_THIS_VERSION; any other layout word -> INPUT_MISSING:<word>; the layout's own word is kept as layout_reason in the run.json entry. A table or chart value is written as canonical JSON in the string value with units 'json'. The map copy the producer passes has calls = [] because the run makes no vendor call.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "opal_producer.py _classified_elements, _opal_map, closed_reason, _section",
      "test_opal_producer.py test_closed_reason_maps_every_layout_word_into_the_closed_set"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: each choice is stated in the code and covered by a test. YCD-s-6 (schema) or the CTO may rule a different mapping; closed_reason is the one place to change."
}
```

## IRPT_YCDGEN-W1-S10 -- the held tables carry no as-of date the producer can read, so every input's as-of is its read date

```json
{
  "id": "IRPT_YCDGEN-W1-S10",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~1",
  "surfaced_at": "2026-10-05T21:56:59Z",
  "one_line": "run.json inputs and the document's inputs_as_of carry the date the run read each input (as_of_basis READ_DATE), because the layout's held-row loaders return rows without the dated folder or the table's own date.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "R3: run.json holds each input read with its as-of date; R4: inputs_as_of is an object of input name to date.",
  "world_is": "layout_overview._read_characteristics picks the latest dated bbg/<YYYY-MM-DD>/characteristics.parquet folder and returns rows only, so the folder date is not exposed; read_classifications returns classifier rows with no table date; read_holdings returns no acceptance date. The producer therefore records the UTC date of the run for every input and marks it READ_DATE in run.json (not in the schema-bound document, whose inputs_as_of has no basis member). A stale held table would not read STALE_INPUT.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "layout_overview.py _read_characteristics, read_classifications@wk-IRPT_YCDGEN-63",
      "runner.py read_holdings@wk-IRPT_YCDGEN-63"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: the STALE_INPUT reason cannot fire from this producer until a loader returns the table's own date; exposing the dated folder is a small change in the layout's loader (another cell's file)."
}
```

## IRPT_YCDGEN-W2-S13 -- the published analysis-report response contract is closed to the v1 form, so the Opal sections answer does not validate against it

```json
{
  "id": "IRPT_YCDGEN-W2-S13",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
  "surfaced_at": "2026-10-05T22:46:55Z",
  "one_line": "OwnedAnalysisReader.sections now answers provider, request_ref, sections and computation_validation for an OPAL_ENGINE document, but the published response schema for the sections route requires extraction_validation and forbids any other member, so that answer is outside the published contract.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-c-6: sections returns provider, request_ref, sections and computation_validation (never extraction_validation) for an OPAL_ENGINE document.",
  "world_is": "docs/contracts/investor-reporting/v1/responses/analysis-report.response.schema.json data: additionalProperties false, required request_ref, sections, extraction_validation; sections and extraction_validation are $ref to the v1 AnalysisReport schema. The existing test test_sections_projection_matches_existing_closed_response_schema validates only the v1 projection. Whether ops/entry.py validates a served response against this schema at runtime was not read (not in this cell's paths). The docs/ schema and any frontend parser are outside this order's paths.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "docs/contracts/investor-reporting/v1/responses/analysis-report.response.schema.json lines 46-64 @wk-IRPT_YCDGEN-64",
      "infra/aws/lambda/investor-reporting/ops/entry.py sections 194-195 (read only)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT until an OPAL_ENGINE report is READY on a served route: the response contract needs a v2 data branch (provider discriminator) and the frontend consumer a matching parse before the first Opal report is opened."
}
```

## IRPT_YCDGEN-W3-S8 -- the Opal artifact family OPAL_REPORT_PDF is named by the publisher but registered nowhere, and the producer does not write the PDF through the artifact store

```json
{
  "id": "IRPT_YCDGEN-W3-S8",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-05T22:57:27Z",
  "one_line": "The Opal artifact family OPAL_REPORT_PDF is named by the publisher but registered nowhere, and the producer does not write the PDF through the artifact store.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y",
  "spec_asserts": "R7: the Opal path takes an artifact reference of its own family, not ORIGINAL_VENDOR_PDF; the family is named in a surprise row.",
  "world_is": "publisher.py (OPAL_FAMILY) and publication_worker.py accept a retained ref of family OPAL_REPORT_PDF (application/pdf, immutable, retention_ref). The reporting policy irpt-x10-v1 holds 13 families (lib/tests/test_irpt_destination.py FAMILIES) and none is OPAL_REPORT_PDF, so ArtifactRepository.put refuses that family until a registry row exists in infra/logic/registry/ (not this cell's file). opal_producer.produce writes the PDF straight to the ycharts_opal_reports S3 family through an injected put_object and never calls artifacts.put, so no retained Opal artifact_ref exists for the publisher to take. Tests register the family in the retention world themselves.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ycharts/generate/publisher.py OPAL_FAMILY, _publish_opal@wk-IRPT_YCDGEN-65",
      "lib/tests/test_irpt_destination.py FAMILIES (13 members)@wk-IRPT_YCDGEN-65",
      "ycharts/research/opal_producer.py produce (put_object, no artifacts.put)@wk-IRPT_YCDGEN-65"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "ARMED: the live Opal request reaches the publisher only after (a) the family is registered in the reporting policy and (b) the driver of the Opal request retains the PDF as that family and hands the ref in. Until then publish() refuses with a loud policy/registry error. The name is this worker's choice; the owner of the registry may rule another."
}
```

## IRPT_YCDGEN-W3-S9 -- resident_worker reopens a READY job through provenance.extraction_evidence_ref, which an Opal report's provenance does not carry

```json
{
  "id": "IRPT_YCDGEN-W3-S9",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-05T22:57:27Z",
  "one_line": "Resident_worker reopens a READY job through provenance.extraction_evidence_ref, which an Opal report's provenance does not carry.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y",
  "spec_asserts": "R7: an Opal job reaches READY; a redelivered message for a READY job reopens the retained report and checks its certification.",
  "world_is": "ycharts/generate/resident_worker.py:513-519 reads retained['provenance']['extraction_evidence_ref']['sha256'] and compares it to detail['certification_sha256'] for a READY job. The Opal publication writes provenance {schema_version irpt-opal-publication.v1, provider, composition_ref, opal_artifact_ref} (no extraction evidence exists) and the READY receipt's certification_sha256 is the Opal PDF's own sha256, so a redelivery of a READY Opal job raises KeyError there. Not this cell's file.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ycharts/generate/resident_worker.py:513-519@wk-IRPT_YCDGEN-65",
      "ycharts/generate/publisher.py _publish_opal provenance@wk-IRPT_YCDGEN-65"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "ARMED: loud (KeyError) on the first redelivery of an Opal job's SQS message after READY. The resident-worker owner reads provenance by provider (opal_artifact_ref.sha256 against certification_sha256 for OPAL_ENGINE)."
}
```

## IRPT_YCDGEN-W3-S10 -- the job-state sequence for an Opal job is RECEIVED -> CERTIFYING -> READY, and the READY receipt's certification_sha256 is the PDF's sha256

```json
{
  "id": "IRPT_YCDGEN-W3-S10",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-05T22:57:27Z",
  "one_line": "The job-state sequence for an Opal job is RECEIVED -> CERTIFYING -> READY, and the READY receipt's certification_sha256 is the PDF's sha256.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "R7: the job reaches READY without DOWNLOADING, EXTRACTING and CERTIFYING, or through a state sequence named in a surprise row if the machine forces one.",
  "world_is": "durable_job.put_state accepts READY only from CERTIFYING (condition '#state = :certifying') and demands report_id, revision and certification_sha256 in the receipt. The Opal path therefore passes through CERTIFYING alone: PublicationWorker.finish sets CERTIFYING (phase opal_report_publication) from RECEIVED (the accepted job's first state; CLAIMED also admitted), the caller then puts READY. DOWNLOADING and EXTRACTING are never entered. With no extraction wrapper, certification_sha256 is the sha256 of the Opal PDF (pdf_ref.sha256, equal to document.opal_artifact.sha256). The vendor path's states are unchanged and a vendor checkpoint is still refused in RECEIVED.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ycharts/generate/durable_job.py put_state (143-153)@wk-IRPT_YCDGEN-65",
      "ycharts/generate/publication_worker.py OPAL_STATES, finish@wk-IRPT_YCDGEN-65",
      "ycharts/generate/tests/test_publication_worker.py test_opal_engine_worker_reaches_ready_without_the_vendor_download_states@wk-IRPT_YCDGEN-65"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: stated in code and covered by a test. CERTIFYING for an Opal job means 'document persisted', not 'extraction certified'; the status wire shows the same word for both."
}
```

## IRPT_YCDGEN-W3-S11 -- a full OPAL_ENGINE document does not fit the 32 KiB pdf checkpoint when its sections carry tables, and the Opal path has no spill

```json
{
  "id": "IRPT_YCDGEN-W3-S11",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-05T22:57:27Z",
  "one_line": "A full OPAL_ENGINE document does not fit the 32 KiB pdf checkpoint when its sections carry tables, and the Opal path has no spill.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y",
  "spec_asserts": "R7: the Opal metadata key set and the sections and computation_validation the v2 schema carries are accepted by the worker.",
  "world_is": "PublicationWorker.checkpoint_pdf stores {pdf_ref, census, metadata} in the job row via put_checkpoint, which refuses more than CHECKPOINT_BYTES = 32 KiB (WORKER_CHECKPOINT_SIZE). The vendor path spills only the census to an EXTRACTION_EVIDENCE artifact. The Opal metadata is the whole v2 document (opal_producer writes table values as canonical JSON strings inside sections), so an Overview with the three classified tables over a large portfolio can exceed 32 KiB; the Opal path does not spill (it is skipped for kind OPAL) and the store refuses loudly. The 99-holding Cottonwood portfolio was not measured here.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ycharts/generate/durable_job.py CHECKPOINT_BYTES, put_checkpoint@wk-IRPT_YCDGEN-65",
      "ycharts/generate/publication_worker.py checkpoint_pdf@wk-IRPT_YCDGEN-65",
      "ycharts/research/opal_producer.py _section (table values as JSON strings)@wk-IRPT_YCDGEN-65"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "ARMED: loud (WORKER_CHECKPOINT_SIZE) for a large document. A fix is a spill of the sections to a retained artifact of a registered family (needs the registry row of S8) or a checkpoint of the document's hash with the document read from the repository; neither is in this cell's paths."
}
```

## IRPT_YCDGEN-W3-S12 -- test_factory_returns_exactly_the_resident_shape_without_any_aws_call fails when test_resident_installed.py is run alone

```json
{
  "id": "IRPT_YCDGEN-W3-S12",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-05T22:57:27Z",
  "one_line": "Test_factory_returns_exactly_the_resident_shape_without_any_aws_call fails when test_resident_installed.py is run alone.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Cell g-6: keep every existing test in test_resident_installed.py passing.",
  "world_is": "Run alone (python -m pytest reports/tests/test_resident_installed.py -q -p no:cacheprovider) the test fails at resident_worker.py:18 'import extract' (ModuleNotFoundError): the file's sys.path list names reports, ycharts/generate, ycharts/session, _scope, _ids, _keys, _authz, intake and ops but not ycharts/extract. With PYTHONPATH=infra/aws/lambda/investor-reporting/ycharts/extract all 14 original tests pass (and the 3 added). The failure does not depend on R7: resident_installed's import list and the test's imports are unchanged by this cell. The AC4 criterion (-k resident_validator_v2) selects only the added tests.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "reports/tests/test_resident_installed.py:18-22@wk-IRPT_YCDGEN-65",
      "ycharts/generate/resident_worker.py:18@wk-IRPT_YCDGEN-65"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: an order-dependent test (it passes when a sibling test file has already put ycharts/extract on sys.path). A one-line path addition in the test file's loop is the owner's."
}
```
}
```



## IRPT_YCDGEN-W2-S14 -- the Analysis tab renderer and typed contracts are outside the e-6 paths and still v1-shaped

```json
{
  "id": "IRPT_YCDGEN-W2-S14",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
  "surfaced_at": "2026-10-05T23:02:10Z",
  "one_line": "The Opal sections reach the Analysis tab only through the adapter's carried members; NativeSections and the typed contracts are outside the e-6 paths and still speak the v1 vendor wording.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-e-6: sections render from status, method and coverage; a NOT_AVAILABLE section shows its reason; no visual change beyond the sections the form adds.",
  "world_is": "adapt.ts now returns OpalReportSection (a ReportSection plus status, reason, method, coverage) and names the reason in the NOT_AVAILABLE value label, which the existing Label column prints. tabs/analysis/NativeSections.tsx (outside the order's paths) still prints the heading 'Certified sections', 'Extraction validation:' and 'Vendor attribution:' (null source coordinate prints 'no source coordinate stated for this section'), and reads only the base ReportSection members, so method and coverage are not printed. contracts/index.ts (ReportSection), contracts/wire/index.ts (no AnalysisReportOpalWire export), wire/consumed.ts 64-65 (AnalysisReport reads list names vendor_artifact), wire/responses.ts 162-166 (slice wire typed on the v1 members) and api/endpoints/investor-reporting.ts 1093 and 1188 (send<AnalysisReportWire,...>) are outside the paths and unchanged; the adapter's parameter types are the wider unions so those call sites still typecheck (tsc -b --noEmit rc 0).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/src/pages/InvestorReporting/tabs/analysis/NativeSections.tsx lines 106-176 @wk-IRPT_YCDGEN-67-portal",
      "portal/src/pages/InvestorReporting/contracts/wire/consumed.ts lines 64-65 @wk-IRPT_YCDGEN-67-portal",
      "portal/scripts/adapt-analysis-report-opal-exercise.mjs opal: RESULT: opal PASS"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT until an OPAL_ENGINE report is served to the tab (also IRPT_YCDGEN-W2-S13). A later cell owning NativeSections.tsx would print method and coverage with isOpalReportSection(section) and drop the vendor wording for the Opal form."
}
```

## IRPT_YCDGEN-W2-S15 -- eleven fe-s-13 tests are red in this worktree on route, envelope and pin checks unrelated to the adapter

```json
{
  "id": "IRPT_YCDGEN-W2-S15",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
  "surfaced_at": "2026-10-05T23:02:40Z",
  "one_line": "Eleven tests in portal src/pages/InvestorReporting/__tests__/fe-s-13 are red in this worktree on route-table, response-envelope and content-pin checks, none of them on the AnalysisReport adapter.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-e-6 AC3 names tsc -b --noEmit only; no test run was required of this cell.",
  "world_is": "bun test src/pages/InvestorReporting/__tests__/fe-s-13 src/pages/InvestorReporting/tabs/analysis on the worktree after the e-6 edits: 40 pass, 11 fail (51 tests, 9 files). The failures name the routes table (expected 19 DECLARED routes, received 18), the response envelope ('unprojected_grant' no longer declared on comparison-catalogue and analysis-request-pdf) and the content pins; field-map.test.ts, which adapts the v1 AnalysisReport fixture, is not among them. The run on the unedited tree was not made (git stash is refused in this tree), so the reds are not shown to pre-date the edit; their messages do not touch AnalysisReport.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bun test output, run 2026-10-05T23:00Z in C:/tmp/wk-ycdgen-6-67/portal",
      "portal/src/pages/InvestorReporting/__tests__/fe-s-13/routes.test.ts line 239 @wk-IRPT_YCDGEN-67-portal"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT for this order (AC3 is the typecheck). Left for the issuer to compare against portal DEV @481b3bcc5f."
}
```

## IRPT_YCDGEN-W1-S11 -- the resident installer composes no ports for the Opal producer, so a listed principal's job is refused until it does

```json
{
  "id": "IRPT_YCDGEN-W1-S11",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~1",
  "surfaced_at": "2026-10-05T23:26:38Z",
  "one_line": "ResidentAssembly now takes an opal_stores(principal, record) port, but reports/resident_installed.py (outside the d-6 paths) does not pass one, so an allow-listed principal's job raises OPAL_STORES_REQUIRED until the issuer wires it.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y",
  "spec_asserts": "R6: a principal on the allow list gets opal_producer.produce. The order's paths are resident_worker.py and its test file.",
  "world_is": "opal_producer.produce(request_ref, firm, stores) needs dynamodb, s3 (host-role read clients), classifier (ETFClassifier), objects (the firm's research-principal put_object client) and map (the Overview element map); reports, principal and owner the worker supplies. build_resident_runtime (reports/resident_installed.py:269) constructs ResidentAssembly with none of those, and the file is outside this order's paths. resident_worker.py adds an optional opal_stores keyword; with it absent a listed principal's job raises ValueError OPAL_STORES_REQUIRED at the switch (loud, retried by the queue, never served by the YCharts producer). With the shipped placeholder allow list no real principal is listed, so nothing is affected until the issuer sets Andrew's principal id.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ycharts/generate/resident_worker.py ResidentAssembly.__init__ and execute@wk-IRPT_YCDGEN-68",
      "reports/resident_installed.py:269-272@wk-IRPT_YCDGEN-68",
      "ycharts/research/opal_producer.py produce docstring (the stores dict)@wk-IRPT_YCDGEN-68"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "ARMED until the installer passes opal_stores AND the allow list names Andrew's id; setting the list first makes his Overview request fail loud on every receive. Both are the issuer's release acts (a never-widen half). The ports are built from the instance role's clients; the worker adds no client of its own."
}
```

## IRPT_YCDGEN-W1-S12 -- five choices the order left to the switch: the persist port, the PDF family call, the attempt id, the refusal code and the missing-ports outcome

```json
{
  "id": "IRPT_YCDGEN-W1-S12",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~1",
  "surfaced_at": "2026-10-05T23:26:38Z",
  "one_line": "The order says only 'choose the producer'; the worker took five unstated choices to make an Opal job reach READY through the existing entry points.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "R6 names the switch only; g-6 and i-6 name checkpoint_pdf and finish as the persist entry points.",
  "world_is": "(1) produce() calls stores['reports'].persist itself; the worker hands it a capture port that keeps the document and writes nothing, then retains the PDF (family OPAL_REPORT_PDF, read from the objects.put_object call whose ContentType is application/pdf) and publishes through checkpoint_pdf(census={}) and finish, so the repository is written once, by _publish_opal. (2) request_ref is {request_id, request_revision, attempt_id, attempt_number}, with attempt_id ATT- plus the first 24 hex of sha256 of request_id|revision|opal. (3) producer.ProducerRefused ends the job as ATTENTION code OPAL_PRODUCER_REFUSED; any other exception propagates for queue redelivery; a producer that wrote no PDF or no document ends as ATTENTION OPAL_PRODUCER_OUTPUT. (4) A retained 'pdf' checkpoint skips the producer on redelivery. (5) The reopen of a READY job reads provenance.provider: OPAL_ENGINE compares opal_artifact_ref.sha256, every other form keeps extraction_evidence_ref.sha256 (row W3-S9).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ycharts/generate/resident_worker.py run_opal, _OpalCapture, execute@wk-IRPT_YCDGEN-68",
      "ycharts/generate/tests/test_resident_worker.py test_allow_listed_principal_opal_producer and test_redelivered_ready_opal_job_is_acknowledged_without_a_key_error@wk-IRPT_YCDGEN-68"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: each choice is in the code and under a test. The produce-side objects.put_object for the PDF reaches the firm's store before the retained copy is made, so a redelivery before the checkpoint writes the same key again (a deterministic address)."
}
```

## IRPT_YCDGEN-W4-S7 -- The order's path for the endpoint client does not exist; the file is portal/src/api/endpoints/investor-reporting.ts, outside the grant, so its two sen

```json
{
  "id": "IRPT_YCDGEN-W4-S7",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~4",
  "surfaced_at": "2026-10-05T23:28:45Z",
  "one_line": "The order's path for the endpoint client does not exist; the file is portal/src/api/endpoints/investor-reporting.ts, outside the grant, so its two send<AnalysisReportWire,...> call sites are untouched.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-j-6 names portal/src/pages/InvestorReporting/api/endpoints/investor-reporting.ts (cell: 'all under portal/src/pages/InvestorReporting/') and R10 says the typed contracts name the Opal members so the adapter's wider unions are the declared types.",
  "world_is": "That path does not exist: portal/src/pages/InvestorReporting has no api directory. The client is portal/src/api/endpoints/investor-reporting.ts (git ls-files line src/api/endpoints/investor-reporting.ts), whose lines 1093 and 1188 still declare send<AnalysisReportWire, ...>. It is outside <paths>, so it was not edited and no file was created at the named path. The adapters accept AnalysisReportAnyWire, so those call sites typecheck unchanged (tsc -b --noEmit rc 0); the declared wire type at the two call sites is still the v1 one. Everything else of R10 is in portal commit cd3924d5.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/src/api/endpoints/investor-reporting.ts lines 1093 and 1188 @wk-IRPT_YCDGEN-70-portal cd3924d5",
      "portal/src/pages/InvestorReporting directory listing: no api entry @cd3924d5"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "A later cell owning portal/src/api/endpoints/investor-reporting.ts would change both generics to AnalysisReportAnyWire (and the slice call to the union slice type). INERT: no behaviour differs, only the declared type."
}
```

## IRPT_YCDGEN-W4-S8 -- The adapter does not set AnalysisReport.provider, so the tab tells the Opal form from its sections; an Opal report with an empty section list renders 

```json
{
  "id": "IRPT_YCDGEN-W4-S8",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~4",
  "surfaced_at": "2026-10-05T23:28:45Z",
  "one_line": "The adapter does not set AnalysisReport.provider, so the tab tells the Opal form from its sections; an Opal report with an empty section list renders the v1 wording.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-j-6 R10: for a section list whose report has provider OPAL_ENGINE the tab prints the Opal wording; the typed contract names the Opal members.",
  "world_is": "contracts/adapt.ts (outside <paths>) builds AnalysisReport without a provider member, so NativeSections decides on `report.provider === 'OPAL_ENGINE' || (sections.length > 0 && every section isOpalReportSection)`. An OPAL_ENGINE report whose sections array is empty therefore prints the v1 heading 'Certified sections' and the v1 'Extraction validation:' line (exercise leg 'V1 empty list keeps its v1 wording' pins that no-provider case). Also: wire/consumed.ts is marked GENERATED by __tests__/fe-s-13/gen-consumed.ts; WIRE_CONSUMED_OPAL_FIELDS was added by hand beside the generated table (the v1 content pins would red on members v1 does not publish), so a regeneration would drop it.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/src/pages/InvestorReporting/tabs/analysis/NativeSections.tsx isOpalReport @wk-IRPT_YCDGEN-70-portal cd3924d5",
      "portal/src/pages/InvestorReporting/contracts/adapt.ts adaptOpalAnalysisReport @81bbeba2: returns no provider member"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT until an OPAL_ENGINE report with zero sections is served. A later cell owning adapt.ts would add `provider: 'OPAL_ENGINE'` in adaptOpalAnalysisReport; the tab already honours it. A cell owning gen-consumed.ts would emit WIRE_CONSUMED_OPAL_FIELDS."
}
```

## IRPT_YCDGEN-W3-S13 -- the Opal document spills to the EXTRACTION_EVIDENCE family, always, for an Opal checkpoint

```json
{
  "id": "IRPT_YCDGEN-W3-S13",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-05T23:29:10Z",
  "one_line": "The Opal document is spilled to an artifact of the existing json family EXTRACTION_EVIDENCE, on every Opal checkpoint rather than only past the limit.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "R9 (3): spill to an existing registered json family; name the choice in a surprise row.",
  "world_is": "R9 (3) asks the Opal path to spill an over-limit document to an EXISTING registered json family. Chosen: EXTRACTION_EVIDENCE (tier state, json, 30 unreferenced days, 2555 ceiling), the family the vendor path spills its census to; no family was added. The spill is unconditional for kind OPAL (checkpoint = pdf_ref, census {}, metadata_ref, metadata_sha256), not size-gated as the vendor census is, so one code path and one checkpoint shape serve every Opal job; the logical id is request_id-opal-document-<sha256> so a replay retains to the same ref. finish reads the document back, verifies the digest and promotes the artifact beside the PDF. A checkpoint stored in the earlier inline form (metadata) is still read.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ycharts/generate/publisher.py retain_document, read_document@wk-IRPT_YCDGEN-69",
      "ycharts/generate/publication_worker.py checkpoint_pdf, finish@wk-IRPT_YCDGEN-69",
      "ycharts/generate/tests/test_publication_worker.py test_opal_checkpoint_is_a_reference_to_the_retained_document_and_finish_publishes_the_document@wk-IRPT_YCDGEN-69"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: the choice is named and tested. The family also holds the vendor evidence wrapper, so a retention sweep of EXTRACTION_EVIDENCE sees Opal documents beside vendor ones; the owner may rule a family of its own."
}
```

## IRPT_YCDGEN-W3-S14 -- adding OPAL_REPORT_PDF changes irpt-x10-v1's policy_sha256, and a retention row stored under the old digest is refused 'retention binding changed' by a deployed registry that carries the new one

```json
{
  "id": "IRPT_YCDGEN-W3-S14",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-05T23:29:10Z",
  "one_line": "Registering OPAL_REPORT_PDF changes irpt-x10-v1's policy_sha256 from e0046398... to a65635d3..., and retention.py refuses any retained artifact stored under the old digest once the deployed registry carries the new one.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y",
  "spec_asserts": "R9 (1): add family OPAL_REPORT_PDF to irpt-x10-v1 with the retention fields of its sibling.",
  "world_is": "reporting_policies.json now holds 14 families in irpt-x10-v1 (OPAL_REPORT_PDF, table opal_report_documents, added). reporting_policy('irpt-x10-v1')['policy_sha256'] is a65635d318c6c10f9466fc831c36417a3c934294ed3e27391bbfcbc4fd62c3ab; before it was e0046398e23951451498c0fcfec29154db5b26d4c70d80c4121f50fd3dfc8c85 (test_s12_active_policy_row_is_unchanged pinned it; re-pinned in this cell's test file). reports/retention.py:108-113 compares each stored retention row's policy_sha256 with the packaged registry's and raises RetentionRefused('retention binding changed') on a difference; generate_installed.py:105-110 and status_installed.py:125 publish the digest as destination_revision. Nothing here deploys: the packaged registry in the live Lambda still carries the old digest until the issuer's deploy.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/registry/reporting_policies.json OPAL_REPORT_PDF@wk-IRPT_YCDGEN-69",
      "infra/aws/lambda/investor-reporting/reports/retention.py:108-113@wk-IRPT_YCDGEN-69",
      "lib/tests/test_irpt_destination.py ACTIVE_ROW_SHA@wk-IRPT_YCDGEN-69"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "ARMED: loud (RetentionRefused) at the first read of an already-retained artifact (a vendor PDF, a composition, a report) after the registry with the new digest is deployed. The issuer deploys the registry and the code together and reads whether the existing retention rows carry the old digest; retention.py and the live rows are not this cell's. reports/tests (retention, generate_installed: 31 tests) pass in this worktree."
}
```

## IRPT_YCDGEN-W3-S15 -- produce retains the PDF only when its caller injects an artifact store, and no caller of produce injects one yet

```json
{
  "id": "IRPT_YCDGEN-W3-S15",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-05T23:29:10Z",
  "one_line": "opal_producer.produce retains the PDF through put only when stores carry artifacts; resident_worker (cell d-6) is the caller that must inject it and hand the returned artifact_ref to the checkpoint.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y",
  "spec_asserts": "R9 (2): produce retains the PDF through put and returns the retained artifact_ref; the publisher takes that ref.",
  "world_is": "produce(request_ref, firm, stores) keeps its signature. With stores['artifacts'] (an ArtifactRepository-shaped put) it retains the PDF as OPAL_REPORT_PDF (logical id request-overview-<sha256>, dependencies stores['retention_dependencies']) and returns the run record with artifact_ref; without it the PDF still goes to the ycharts_opal_reports S3 family and the record has no artifact_ref (the 12 earlier producer tests build stores without it and must keep passing). resident_worker.py is d-6's file and was not read here for its call.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ycharts/research/opal_producer.py produce@wk-IRPT_YCDGEN-69",
      "ycharts/research/tests/test_opal_producer.py test_produce_retains_pdf_artifact_through_put_and_returns_its_artifact_ref@wk-IRPT_YCDGEN-69"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "ARMED: a live Opal request whose caller omits artifacts writes the PDF to S3 only, has no ref, and the publisher refuses it (RETAINED_OPAL_PDF_REQUIRED). The caller also passes the accepted composition's retention ref as retention_dependencies and then calls checkpoint_pdf with pdf_ref=record['artifact_ref'] and metadata=the document."
}
```

## IRPT_YCDGEN-W3-S16 -- with the PDF retained, the run record's report.key still names the layout's ycharts_opal_reports address, where no object is written

```json
{
  "id": "IRPT_YCDGEN-W3-S16",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-05T23:29:10Z",
  "one_line": "When the PDF is retained as an artifact, run.json's report.key (the layout's own key) names an S3 address nothing is written to; the retained location is artifact_ref.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "R9 (2): the PDF is a retained artifact; run.json's report key is the layout's.",
  "world_is": "layout_overview.finish sets report.key from _report_key(run_doc) and produce checks it equals the builder's ycharts_opal_reports address. In the retained path produce skips the S3 put of the PDF, so that key is an address with no object, and the record's artifact_ref (top level) is the true location. Left as is: the layout and run.json shape are not this cell's, and the check keeps the key equal to the builder output.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ycharts/research/opal_producer.py produce@wk-IRPT_YCDGEN-69",
      "ycharts/research/layout_overview.py finish (1157-1172)@wk-IRPT_YCDGEN-69"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: a reader of run.json who follows report.key finds nothing; the reader should follow artifact_ref when present."
}
```

## IRPT_YCDGEN-W3-S17 -- resident_worker.py still retains the Opal PDF under OPAL_REPORT_PDF, which no policy registers after l-6, and the deployed composition does not opt in to the research revision

```json
{
  "id": "IRPT_YCDGEN-W3-S17",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-05T23:55:30Z",
  "one_line": "ycharts/generate/resident_worker.py:122 (OPAL_PDF_FAMILY = OPAL_REPORT_PDF, put at :429) and its test file are outside cell l-6's paths; with l-6 the worker's put refuses and 4 tests of test_resident_worker.py fail; reports/resident_installed.py builds the repositories without the research revision.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y",
  "spec_asserts": "Cell l-6: the producer, publisher and publication worker name YCHARTS_OPAL_REPORT where they named OPAL_REPORT_PDF; paths exclude resident_worker.py and test_resident_worker.py.",
  "world_is": "After l-6 publication_worker and publisher require pdf_ref family YCHARTS_OPAL_REPORT, but resident_worker.py:122/:429 puts the PDF as OPAL_REPORT_PDF (no longer registered anywhere). test_resident_worker.py::test_allow_listed_principal_opal_producer, test_one_producer_per_request, test_one_producer_per_request_a_retained_opal_pdf_publishes_without_producing_again and test_redelivered_ready_opal_job_is_acknowledged_without_a_key_error fail with RequestReadRefused at publication_worker.py:76 (base checkout: 53 passed, 8 skipped before l-6). test_resident_worker.py:51 and :697 also name OPAL_REPORT_PDF. Cell l-6 adds the mechanism instead: composition.build_retained_repositories(additional_policy_revisions=('irpt-ycdgen-research-v1',)) and ArtifactRepository(revisions={family: revision}) / put(policy_revision=...) retain a family under its own revision; reports/resident_installed.py (build_resident_runtime) does not pass it, since test_resident_installed.py cannot run here (S18) and the order does not wire the deployment.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py:122,429@wk-IRPT_YCDGEN-72",
      "infra/aws/lambda/investor-reporting/reports/composition.py build_retained_repositories@wk-IRPT_YCDGEN-72",
      "infra/aws/lambda/investor-reporting/reports/resident_installed.py:253-256@wk-IRPT_YCDGEN-72"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "ARMED: the live Opal request would fail at the PDF put (unregistered family) until a cell renames the family in resident_worker.py and its test, passes the research revision in resident_installed.py, and the row irpt-ycdgen-research-v1 is ACTIVE (CTO acceptance, ruling item 5)."
}
```

## IRPT_YCDGEN-W3-S18 -- reports/tests/test_resident_installed.py::test_factory_returns_exactly_the_resident_shape_without_any_aws_call fails on the base checkout with ModuleNotFoundError: extract

```json
{
  "id": "IRPT_YCDGEN-W3-S18",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-05T23:55:31Z",
  "one_line": "One test of a file under l-6's reports/tests/*.py fails identically before and after l-6: resident_worker.py:20 imports extract, which is not on that test's path.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Cell l-6: keep every existing test in the touched files passing.",
  "world_is": "python -m pytest reports/tests/test_resident_installed.py -q gives 1 failed, 13 passed in the worktree and in the base checkout (no l-6 change): ModuleNotFoundError: No module named 'extract' at ycharts/generate/resident_worker.py:20. Not caused by this cell; reports/tests/test_resident_installed.py was not edited.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/reports/tests/test_resident_installed.py test_factory_returns_exactly_the_resident_shape_without_any_aws_call@wk-IRPT_YCDGEN-72 and CLOUD base checkout"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: runs of the whole reports/ directory report this one failure; the criteria name test_retention.py and test_publisher.py, which pass."
}
```

## IRPT_YCDGEN-W1-S13 -- the Opal Overview element map has no installed home, and the default classifier and research S3 openers read paths the package may not carry

```json
{
  "id": "IRPT_YCDGEN-W1-S13",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~1",
  "surfaced_at": "2026-10-06T00:18:40Z",
  "one_line": "The producer's `map` store has no file in the investor-reporting package; the installer reads it from an optional pinned `opal_map` binding that no installed bindings file carries yet, and the two default openers reach outside the package.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y",
  "spec_asserts": "R11 (1): the factory builds the stores opal_producer.produce takes (holdings reader, classifier, firm-store put, artifacts, clock); the order names no source for the `map` store.",
  "world_is": "opal_producer.produce requires stores['map'] (the Overview element map). The only maps in the tree are test fixtures and the issuer's close artifact org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/overview_map_r3_close.json; none sits in the package. reports/resident_installed.py now reads it from an optional bindings member opal_map {path, sha256} (pinned by content like the census, read only when a listed principal's job asks, refusing OPAL_MAP_BINDING_REQUIRED / PINNED_FILE_ABSENT:opal_map / PINNED_FILE_DIFFERS:opal_map). The shipped resident_bindings.json is not in this order's paths and carries no opal_map. Two defaults are also unproven offline: the classifier opener calls layout_overview._default_classifier(), which imports etf_classifications_dynamodb from the Lambda's v2_portal/_shared folder (absent from an installed investor-reporting package, then LayoutRefused), and the firm-store opener calls runner.research_s3 (an STS assume of the firm's ycharts-research role). Both were exercised only as injected fakes.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/reports/resident_installed.py make_opal_stores, _opal_map_loader, _open_research_s3, _open_classifier@wk-IRPT_YCDGEN-73",
      "infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py _default_classifier@wk-IRPT_YCDGEN-73",
      "infra/aws/lambda/investor-reporting/ycharts/research/runner.py research_s3@wk-IRPT_YCDGEN-73"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "ARMED until the issuer, at release: (a) installs the map file beside the resident module and adds opal_map {path, sha256} to resident_bindings.json, (b) confirms the classifier client module is importable on the host, (c) confirms the firm research role is assumable by the host role. Until then a listed principal's job raises loud on every receive and is retried by the queue; the placeholder allow list keeps every real principal on the YCharts path."
}
```

## IRPT_YCDGEN-W1-S14 -- the worker prefers the artifact_ref produce returns, and keeps the objects-port retention for a producer that returns none

```json
{
  "id": "IRPT_YCDGEN-W1-S14",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~1",
  "surfaced_at": "2026-10-06T00:18:40Z",
  "one_line": "run_opal reads artifact_ref from the run record produce returns and checkpoints it as is; with none it still retains the PDF captured from the objects port, now as YCHARTS_OPAL_REPORT.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "R11 (2): the artifact_ref produce returns reaches the publisher's checkpoint; W3-S17: rename OPAL_REPORT_PDF at the two lines.",
  "world_is": "resident_worker.run_opal had one retention route (capture the PDF from objects.put_object, put it as OPAL_PDF_FAMILY). With the repository's artifacts in the stores, produce retains the PDF itself (so objects.put_object never sees it) and returns artifact_ref; the old route would have found no PDF and ended the job ATTENTION OPAL_PRODUCER_OUTPUT. The worker now takes the returned ref when present and keeps the old route for a producer without it (the existing fake-producer tests of test_resident_worker.py). The legacy put passes no policy_revision: the repository's family-to-revision map decides it, so a repository built without the research revision refuses it loudly. OPAL_PDF_FAMILY is now YCHARTS_OPAL_REPORT; test_resident_worker.py registers that family in its fixture registry in place of OPAL_REPORT_PDF.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py run_opal@wk-IRPT_YCDGEN-73",
      "infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_opal_thread_integration.py test_opal_artifact_ref_reaches_checkpoint@wk-IRPT_YCDGEN-73"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: tested both ways (the thread test fails with OPAL_PRODUCER_OUTPUT when the worker ignores the ref). The legacy route is dead code in the installed service once the installer supplies artifacts; the release that deletes the YCharts producer may delete it. Also: reports/tests/test_resident_installed.py now puts ycharts/extract on its test path, so the whole file passes run alone (the cure of row W3-S18, whose one failing test was the only one importing resident_worker)."
}
```

## IRPT_YCDGEN-W1-S15 -- the gate learns the opal map's repo path from the bindings provenance, and --research under --base-pin reads P's tree

```json
{
  "id": "IRPT_YCDGEN-W1-S15",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~1",
  "surfaced_at": "2026-10-06T01:37:30Z",
  "one_line": "R13 names no way for the gate to find the opal map's repo path, nor which tree --research reads under --base-pin; the worker chose provenance.opal_map_source and the base tree.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "R13 (2) packages --opal-map REPO_PATH as ycharts/research/overview_map.json; (5) the gate compares each listed member to git show <pin>:<path> and every other member to git show P:<path>; (1) --research packages the research files 'at the pin'.",
  "world_is": "The map's package name (ycharts/research/overview_map.json) is not its repo path (org/missions/.../maps/overview_map.json), and the gate takes only --base-pin and --files-from, so it cannot invert the name. The builder therefore records provenance.opal_map_source (the repo path) in the bindings and the gate reads it from the package's own bindings; the map is always expected from --pin, never P. Under --base-pin the --research files are read from P's tree like every other rule member (a research file that P lacks must be in LIST), because the spec says no unlisted member differs from P. The gate also fails when a listed path is not in the package. A build without --opal-map carries no opal_map_source and a build with no flags adds no key (test default_build_unchanged compares against the builder at 4d2331db75).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py main@wk-IRPT_YCDGEN-74",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/resident_package_gate.py main@wk-IRPT_YCDGEN-74",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_listed.py@wk-IRPT_YCDGEN-74"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: one extra provenance key and one extra gate read; both are covered by the tests. The issuer may rule the key name."
}
```

## IRPT_YCDGEN-W1-S16 -- f-6 AC5 cannot pass on the contract's own List statement: the check reads the condition key "s3:prefix" as a second action

```json
{
  "id": "IRPT_YCDGEN-W1-S16",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~1",
  "surfaced_at": "2026-10-06T02:12:30Z",
  "one_line": "f-6.check.py AC5 collects every quoted s3:<word> in the List statement as an action, so the Condition key s3:prefix that R14 (5) requires makes it FAIL; the HCL follows R14 literally.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "R14 (5) ListTheHeldFundCharacteristicsFolder: Action [s3:ListBucket], Condition { StringLike = { \"s3:prefix\" = [\"bbg/\", \"bbg/*\"] } }; AC5 passes when that statement is correct.",
  "world_is": "AC5 runs re.findall of a quoted s3:<letters> token over the statement block and demands exactly [\"s3:ListBucket\"]; the required Condition key \"s3:prefix\" is also a quoted s3:<letters> token, so findall returns [\"s3:ListBucket\", \"s3:prefix\"] and the check prints `f-6.AC5 RESULT: FAIL list statement missing, wrong, or not cut to the bbg/ prefix`. Measured on the worktree resident.tf (statement present, action exactly s3:ListBucket, resource exactly \"arn:aws:s3:::opal-data-etfs\", condition exactly as R14 (5)). The worker did not reshape the HCL (an interpolated key, or a key moved out of the statement) to defeat a defective regex; AC1-AC4 and AC6 PASS. The fix is in the issuer's check (match the action list from the Action line only), outside the worker's paths.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6/checks/f-6.check.py (AC5 branch) main@wk-IRPT_YCDGEN-77",
      "infra/aws/terraform/investor-reporting/ycharts/resident.tf (ListTheHeldFundCharacteristicsFolder) main@wk-IRPT_YCDGEN-77"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: a check-side defect; the HCL is the contract's. The issuer amends the check or grades AC5 on the statement's text."
}
```

## IRPT_YCDGEN-S10 -- the resident package does not carry the classification client the Opal producer imports

```json
{
  "id": "IRPT_YCDGEN-S10",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~Y",
  "surfaced_at": "2026-10-06T02:54:14Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "the resident package does not carry the classification client the Opal producer imports; the first Opal request from a listed principal ends as an ATTENTION",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y",
  "spec_asserts": "Branch B installed (ledger irpt-ycdgen-r6-branch-b-20261006 V1): a listed principal's request is served by the Opal producer, which reads classifications through ETFClassifier.",
  "world_is": "layout_overview._default_classifier imports etf_classifications_dynamodb, else looks for HERE.parents[2]/v2_portal/_shared. In the installed package HERE is <root>/ycharts/research, so parents[2] is /opt/irpt-resident, which has no v2_portal; the module lives in infra/aws/lambda/v2_portal/_shared (MDPF_SECCLASS's file) and is in no packaged directory. resident_installed._open_classifier calls it, so the producer raises LayoutRefused before any output and the job ends ATTENTION for the listed principal; other principals are unaffected.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "host read SSM 30b2fdeb (host_real_stack_reads.sh, root 09139ee34d-st23): 'No module named etf_classifications_dynamodb' with the package paths on sys.path",
      "infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py _default_classifier; reports/resident_installed.py _open_classifier",
      "the module imports only boto3 and botocore (357 lines)"
    ]
  },
  "notes": "Not found by any fake-backed test because every test injects a classifier. Fix: package the one file as ycharts/research/etf_classifications_dynamodb.py (the research directory is on sys.path when load_opal_producer runs, so the first-try import finds it); needs a builder member mapping (cell YCD-n-6). Until then Andrew's own requests fail by name; nobody else is affected. F1 is held."
}
```

## IRPT_YCDGEN-S11 -- pyarrow is not installed on the resident host, so the held fund characteristics (81 of the Overview map's 153 held groups) read INPUT_MISSING

```json
{
  "id": "IRPT_YCDGEN-S11",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~Y",
  "surfaced_at": "2026-10-06T02:54:14Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "pyarrow is not installed on the resident host, so the held fund characteristics (81 of the Overview map's 153 held groups) read INPUT_MISSING",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "The Opal Overview reads the Bloomberg characteristics parquet under opal-data-etfs/bbg/ for 81 held groups.",
  "world_is": "host pydeps and the system python3.12 carry no pyarrow (pydeps probe SSM 8d5e6fd5); layout_overview._read_characteristics imports pyarrow.parquet; opal_producer._characteristics_reader catches any exception and returns None, so those elements read INPUT_MISSING:<table> with the reason on the page. The IAM path itself works: ListBucket read 31 dated folders, latest bbg/2026-10-02/.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "host read SSM 30b2fdeb and 8d5e6fd5",
      "opal_producer.py _characteristics_reader"
    ]
  },
  "notes": "Inert for FWD-1's thread (cover, holdings with the table's names and classes, allocation by the table's classes do not read characteristics) and honest by contract (a figure Opal cannot work out says so with the reason). A host dependency (a pyarrow wheel into pydeps through S3) is its own act with its own half; the sector and look-through pages (FWD-13) need it."
}
```

## IRPT_YCDGEN-S12 -- the Analysis tab lets an internal user submit with no firm selected; the request then fails as UNEXPECTED

```json
{
  "id": "IRPT_YCDGEN-S12",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~Y",
  "surfaced_at": "2026-10-06T13:10:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "the Analysis tab lets an internal user submit with no firm selected; the intake function refuses it as BucketUnmapped, shown to the user as 'Needs attention' with no reason",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "A submit from the Analysis tab either carries the firm the request is for or the page asks for one first.",
  "world_is": "F1 walk 2026-10-06 ~13:03Z, Andrew signed in as andrew@opalinvest.com: the page showed 'Needs attention -- areq-efd72c44'; the resident host saw no job (0 rows naming it, 0 handled polls); irpt-ycharts-generate logged operation comparison-catalogue, exception BucketUnmapped 'no directory bucket declared for firm token in IRPT_DIRECTORY_BUCKET_MAP', public code UNEXPECTED. The map holds 49financial, cottonwood, inflection. CTO read (msg 105558): an internal principal is tenant opal-capital unless the request names selected_tenant, and opal-capital is unmapped. The firm token in the request is NOT in the log, so this is inferred, not measured.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "CloudWatch /aws/lambda/irpt-ycharts-generate stream 2026/10/06/[$LATEST]3731eb19282f4b7684ea79bbb91ba11d, correlation_id corr-a589f1e24fb0",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6/act/F1_AREQ_READ_20261006.txt",
      "IRPT_DIRECTORY_BUCKET_MAP read from the live function configuration"
    ]
  },
  "notes": "Owner of the fix is a next-round portal cell (the composer asks for a firm before Generate) and the intake's reason code (UNEXPECTED hides BucketUnmapped; CTO says r58 ships a named code). F1 retries with Cottonwood selected in the firm selector."
}
```

## IRPT_YCDGEN-W2-S16 -- on a served Global wire the picked client's scope already holds its firm as registryTenant; the empty tenant comes from the no-tenant composer mount and fallback, not a lost field

```json
{
  "id": "IRPT_YCDGEN-W2-S16",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
  "surfaced_at": "2026-10-06T13:34:00Z",
  "one_line": "For a Global principal who picked a client, selectedScope.registryTenant and the global firm's tenant both hold the firm on the repo's served-wire fixture; the empty tenant comes from GenerateComposer reading and submitting with the bootstrap scopeRef, which carries none.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-p-6 section 3: measure what selectedScope.registryTenant and the global firm's tenant hold, then fix the one place it is lost.",
  "world_is": "Through the real strict reader (readDirectoryResolution) on tests/opal-scope/server-wire.json with the first member relabelled cottonwood: registryTenant=cottonwood, globalFirm.tenant=cottonwood, verifiedRequestFirm.tenant=cottonwood, scope.scope.tenant=the opaque fir_ id, principalClass=global. The Global arm of the reader refuses a scope without registry_tenant, so no field is lost in the adapters. The paths that carry no tenant are AnalysisTab's `selectedScopeRef ?? scopeRef` (the bootstrap ref has no selectedTenant, mounted before any client is accepted) into GenerateComposer, whose effect called fetchCatalogue(undefined) and whose submit sent no selected_tenant. The fix is therefore a guard (no read, no send, a plain-words line when the tenant is missing) plus selectedTenantFor reading the global firm's tenant first. The live wire at 2026-10-06 ~13:03Z was not read here (no live call is permitted to a worker).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bun portal/scripts/global-tenant-exercise.mjs global (MEASURE line)",
      "portal/src/pages/InvestorReporting/contracts/directory-context.ts lines 77-88"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "If the issuer's live close still shows a request with no firm after this lands, the live wire or the row's firmId differs from the fixture; the exercise's MEASURE line is the thing to compare."
}
```

## IRPT_YCDGEN-S13 -- the picked-client (custody) Generate path cannot submit from the browser: snapshot_id is minted server-side and no route returns it; the composer fails before sending and shows "Needs attention" with no reason

```json
{
  "id": "IRPT_YCDGEN-S13",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~Y",
  "surfaced_at": "2026-10-06T18:50:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "the picked-client Generate path sends a snapshot_id the browser builds from source_set_revision; the server needs the opaque cst_ id it minted, and no route returns it",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "A submit from the Analysis tab for a picked client either reaches the server with the id the server holds for that selection or the page says why it cannot.",
  "world_is": "Andrew's HAR 2026-10-06 ~18:23Z (Downloads~~~~~~~~/localhost testing.har): every API call carried selected_tenant=cottonwood and returned 200; Generate sent NO submit request. GenerateComposer snapshotIdOf = HoldingsSnapshot.sourceSetRevision, joined at contracts/adapt.ts:1123 as source:revision entries with ',' (3 entries here: 225 chars, containing ',', '/' and '@'); contracts/submission-request.ts identifier() allows 200 chars and [A-Za-z0-9_.:-], so readSubmissionRequest throws TypeError before any send and composer.ts:469 shows 'Needs attention' with no reason code. The server applies the same rule (ycharts/generate/submission.py:40-42) and requires browser snapshot_id == owner snapshot_id (submission.py:152), which _scope/accepted_custody.py:106 mints as 'cst_' + token_hex(32), 'trusted server writer only; never installed as an HTTP request route'. The holdings reply carries source_set_revision only. In the same HAR REQ-6eaec4e9e48b4d4f409148b6 is operation_kind analysis_generate, state UNAVAILABLE. This SUPERSEDES the one_line of IRPT_YCDGEN-S12 (the firm was sent; the firm fix p-6 worked).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Downloads/localhost testing.har entries 7, 8, 24 (not committed: client data)",
      "portal e107538d contracts/adapt.ts:1123; contracts/submission-request.ts:4-36; tabs/analysis/composer.ts:439-471",
      "infra/aws/lambda/investor-reporting/ycharts/generate/submission.py:40-42,152; _scope/accepted_custody.py:106"
    ]
  },
  "notes": "Inert for FWD-1: the thread is the Prospect portfolio upload (PRD v0.8 FWD-1 and s2 step 1; input_id, snapshot_id null). CTO ruling msgs 105681 and 105683: one definition, the server's; no cell now; for the CTO's round analysis."
}
```

## IRPT_YCDGEN-W3-S19 -- the Prospect card cannot read the firm catalogue through any prop the order's paths reach, so the page header publishes it to a module-level holder the card reads

```json
{
  "id": "IRPT_YCDGEN-W3-S19",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-06T21:12:00Z",
  "one_line": "HeaderSelection (header/HeaderSelectionContext.ts) and TabShell.tsx carry no firm catalogue and are outside YCD-q-6's paths, so index.tsx publishes the catalogue to stagedProspect.ts and AnalysisTab reads it from there.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-q-6 R18 (a): the card shows a firm choice 'from the same catalogue the Firm dropdown uses'; the paths named are ProspectComposer, AnalysisTab, stagedProspect.ts (new), FirmDropdown and index.tsx.",
  "world_is": "AnalysisTab receives only api, scope, firmId and selectedScopeRef from TabShell; the catalogue (index.tsx catalogueQuery) lives above TabShell and the only carrier between them is HeaderSelectionContext, whose HeaderSelection type is in a file outside the order's paths. A useQuery in AnalysisTab would throw in the existing static-render tests (no QueryClientProvider). So index.tsx calls publishFirmCatalogue({internal, firms}) in an effect (withdrawn on unmount) and AnalysisTab reads useFirmCatalogue() (useSyncExternalStore) from stagedProspect.ts. Memory only; one workspace per page, so one holder. A later cell holding HeaderSelectionContext.ts and TabShell.tsx could replace the holder with a context field.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal wk-IRPT_YCDGEN-82-portal src/pages/InvestorReporting/header/HeaderSelectionContext.ts:15-50 (HeaderSelection fields)",
      "portal src/pages/InvestorReporting/tabs/TabShell.tsx:164-172 (AnalysisTab props)",
      "bun portal/scripts/prospect-firm-exercise.mjs firm and dropdown (render the real components through the holder)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "For the CTO's round analysis: the holder is a second carrier of the catalogue beside the page's own prop; both are fed from the one catalogueQuery."
}
```

## IRPT_YCDGEN-W3-S20 -- the portal has no DOM library, so no button handler or effect can run in a bun exercise; YCD-q-6's exercise grades the card by static render, the real send helpers and source-wiring checks

```json
{
  "id": "IRPT_YCDGEN-W3-S20",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-06T21:13:00Z",
  "one_line": "No happy-dom, jsdom or testing-library is installed under portal/node_modules, so prospect-firm-exercise.mjs cannot press Review or Generate or run the write-through effect; the send decision lives in exported helpers it drives directly.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-q-6: 'firm drives the Prospect card ... the upload request and the submit request both carry cottonwood'; 'remount stages a file and a review result, remounts the composer as a client pick or tab switch does'.",
  "world_is": "ls portal/node_modules finds no happy-dom, jsdom, @testing-library or react-test-renderer; react-dom/server runs neither handlers nor effects. The exercise therefore (1) drives sendProspectUpload / sendProspectSubmit / prospectFirmDecision (exported from stagedProspect.ts and the only code the composer sends through) against a recording stub, (2) static-renders the real ProspectComposer and AnalysisTab for what a fresh mount shows (a fresh mount reads the staged slot exactly as a remount does), and (3) checks by source regex that the composer writes through to the slot (holdStaged in an effect) and clears on a new file or firm. What is NOT executed: the click on Review portfolio, the useEffect write-through and the file input's change handler. Precedent: portal/scripts/global-tenant-exercise.mjs (p-6) grades the same way; src/pages/InvestorReporting/__tests__/dsgn-irptv1/s55.component-wiring.test.tsx drives handlers by wrapping the JSX runtime.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/node_modules directory listing (no DOM library present)",
      "portal/scripts/prospect-firm-exercise.mjs remount arm (the three source-wiring checks)",
      "portal src/pages/InvestorReporting/__tests__/dsgn-irptv1/s55.component-wiring.test.tsx:28-50"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "If the issuer's live close shows a file lost across a client pick, the effect write-through is the first thing to read (ProspectComposer.tsx holdStaged effect)."
}
```

## IRPT_YCDGEN-W3-S21 -- running the whole InvestorReporting bun suite rewrites four tracked wire files (AnalysisReport.ts, ExportBundle.ts, index.ts, responses.ts) in the worktree

```json
{
  "id": "IRPT_YCDGEN-W3-S21",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
  "surfaced_at": "2026-10-06T21:14:00Z",
  "one_line": "bun test src/pages/InvestorReporting leaves contracts/wire/{AnalysisReport,ExportBundle,index,responses}.ts modified (120 changed lines, 56 deleted from AnalysisReport.ts) in the portal worktree; the IVE17-AC2 regenerated-wire test is the likely writer.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-q-6 section 3: the baseline is bun test over fe-s-13 and tabs/analysis (40 pass, 11 fail); the order names only that narrower run, not the whole suite.",
  "world_is": "Running the wider bun test src/pages/InvestorReporting (to check no other test read the four files I edited) ended with git diff --stat showing those four tracked wire files changed outside every order's paths (twice: after the base-source run and after mine). The failing-test list names 'IVE17-AC2 -- the regenerated wire carries every landed ask'. I restored the four from HEAD with git show and committed none of them. The narrower baseline run (fe-s-13 + tabs/analysis) did not touch them.",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "git diff --stat in the portal worktree after bun test src/pages/InvestorReporting (AnalysisReport.ts 56, ExportBundle.ts 6, index.ts 8, responses.ts 30 changed lines)",
      "bun test output: IVE17-AC2 line in the failing list of the base-source run"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT for this order (nothing committed). A worker or drain that runs the whole suite and commits with a broad path set would carry the rewritten wire files; the writer was inferred from the test name, not read."
}
```

## IRPT_YCDGEN-W5-S1 -- `bunx` is not on the worker shell PATH, so the order's `bunx tsc --noEmit` cannot run as written

```json
{
  "id": "IRPT_YCDGEN-W5-S1",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~5",
  "surfaced_at": "2026-10-07T08:05:19Z",
  "one_line": "bunx tsc --noEmit fails with 'bunx: No such file or directory' (rc 127) in the worktree shell where bun resolves; bun x tsc --noEmit ran instead and printed 0 errors before and after the edit.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-t-6 section 3: run bunx tsc --noEmit from the portal directory and state its error count before and after.",
  "world_is": "With the bun directory from the spawn line on PATH, bun runs but bunx is absent (timeout: failed to run command 'bunx', rc 127). bun x tsc --noEmit from the portal directory exits 0 with 0 'error TS' lines both on the base source (HEAD files restored) and with the edit.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bunx tsc --noEmit output: failed to run command 'bunx': No such file or directory (rc 127)",
      "bun x tsc --noEmit: rc 0, 0 error TS lines, base and after"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Substituted the equivalent bun x form; no criterion depends on tsc."
}
```

## IRPT_YCDGEN-S14 -- dell2's AWS user cannot run SSM commands on the resident host, so every host read and resident build for this project's dell2 lane is blocked

```json
{
  "id": "IRPT_YCDGEN-S14",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-07T09:12:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "ssm:SendCommand on resident host i-0167fd745ad906a66 is denied to cloudops-dell2-agent-user, so dell2 cannot read the host for ledger irpt-ycdgen-r6-branch-b2-20261006 (F1 reads) or ship the next resident build (M1, the 390 s release)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "The seat that owns the resident host files and the open ledger (2.0.0_SA_COO~G2, CTO msgs 90/189) can read the host it is accountable for.",
  "world_is": "2026-10-07 ~09:10Z, python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/host_read.py <host_root_read.sh> from dell2 returned: AccessDeniedException ... User: arn:aws:iam::313476888478:user/cloudops-dell2-agent-user is not authorized to perform: ssm:SendCommand on resource: arn:aws:ec2:us-east-1:313476888478:instance/i-0167fd745ad906a66. Nothing ran on the host.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "the AccessDeniedException text above (dell2 session, 2026-10-07 ~09:10Z)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/host_root_read.sh (the read-only script; changes nothing)"
    ]
  },
  "notes": "Inert now: no host act is due before Andrew's F1 click. Per 1.0.0_SA_CTO~DELL2 standing rule msg 218 the read goes to the laptop as a FILE through 0.0.0_AB_MSTR~DELL2; no fence is widened from dell2. Whether dell2 should hold ssm:SendCommand on this host is NFRA_CTLPLN's question, not this project's."
}
```

## IRPT_YCDGEN-S15 -- the t-6 worker fetched portal packages from the npm registry (egress off Opal) on the issuer's instruction

```json
{
  "id": "IRPT_YCDGEN-S15",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-07T12:12:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "the issuer's spawn line for worker 0.9.0_WK_IRPT_YCDGEN~5 (cell t-6, ~07:58Z) told it to run bun install in C:/dev/wk-ycdgen-6-t5/portal; that is one npm-registry fetch, egress off Opal infrastructure",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "No seat makes egress off Opal infrastructure; a dell2 portal worktree links or copies the shared lockfile-matched portal/node_modules and never runs npm or bun install (CLAUDE.md Agent Autonomy; 1.0.0_SA_CTO~DELL2 msg 473).",
  "world_is": "One registry fetch at ~08:0xZ 2026-10-07, 244 top-level packages placed in C:/dev/wk-ycdgen-6-t5/portal/node_modules only (untracked); bun.lock restored by the worker; nothing built from those packages was committed or shipped. The error is the issuer's instruction, not the worker's. Re-proof on the shared node_modules (laptop pack, lockfile-matched), worktree C:/dev/wk-g2-pageproof with a junction to C:/dev/ajb_workspace/portal/node_modules: at 949830e8 typecheck rc=0; exercise arms signout, remount, firm, dropdown all PASS; bun test fe-s-13 + tabs/analysis 32 pass / 16 fail / 1 error over 48 tests, identical at base 4d16a2a0 (standalone-worktree path artifact, docs/ unresolved), so t-6 changes no test count.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ls C:/dev/wk-ycdgen-6-t5/portal/node_modules: 244 entries; git status in that portal worktree clean",
      "1.0.0_SA_CTO~DELL2 msgs 473 and 481 (ruling: file the row, leave the directory, re-prove on the shared node_modules)",
      "re-proof transcript in the issuer's session 2026-10-07 ~12:1xZ (commands and outputs above)"
    ]
  },
  "notes": "Per CTO msg 481 the directory is NOT deleted (a recursive delete would need Andrew's word); it goes when that worktree is retired. The t-6 proof of record is the re-proof above, not the worker's run."
}
```

## IRPT_YCDGEN-S16 -- F1 stopped at ENVELOPE_STATUS: the analysis POST's success reply carries internal_correlation_id, which the browser's public-status check refuses

```json
{
  "id": "IRPT_YCDGEN-S16",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-07T19:00:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "Andrew's F1 run (localhost:5174, portal DEV 3b8c292f47) stopped at generation with 'This action is unavailable (ENVELOPE_STATUS). Your request is kept for retry.'; the code reading says the POST was accepted and the browser refused the success reply's status member",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "spec_asserts": "Every v1 response's status member is a PublicStatusEnvelope: operation, state, source_dates, actions, public_reason_code (+ contract_version); internal_correlation_id is x-server-only and never on the wire.",
  "world_is": "Code at dell2 CLOUD: ycharts/generate/entry.py submit_analysis returns _status = _entry.status_envelope(...), which includes internal_correlation_id (_authz/served.py:295); response_envelope passes it through unchanged (served.py:928 path; measured locally: wire status keys = actions, internal_correlation_id, operation, public_reason_code, source_dates, state). Only the refusal path projects it out (served.py:416-423, added 0c2a7938cc 2026-09-22). The portal's requirePublicStatus (contracts/public-status.ts, closed key set, tightened c09fea54 2026-09-22) refuses the extra key, so envelope.ts:316-318 throws EnvelopeMismatch('status') -> public code ENVELOPE_STATUS (envelope.ts:94-96). So every ACCEPTED analysis POST since 2026-09-22 reads as a failure in the browser. UNMEASURED: the deployed bytes of the handler that served Andrew's POST, and whether his request row exists server side (dell2 is denied kms:Decrypt on irpt-jobs; read relayed to the laptop with f1_find_request.py).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "local run of entry.status_envelope + served.response_envelope at dell2 CLOUD (2026-10-07 ~18:5xZ): status keys include internal_correlation_id",
      "portal 3b8c292f47 src/pages/InvestorReporting/contracts/public-status.ts requirePublicStatus closed key set; envelope.ts:94-96, 316-318; ProspectComposer.tsx:40 message",
      "git -S: entry.py _status since 4356085122 (2026-09-11); served.py refusal projection 0c2a7938cc (2026-09-22); portal closed check c09fea54 (2026-09-22)"
    ]
  },
  "notes": "Fix shape (a cell, not yet cut): project the success-path status the same way the refusal path does, so internal_correlation_id never reaches the wire. Ledger irpt-ycdgen-r6-branch-b2-20261006 stays OPEN with leg F1 failed at this point; nothing on it is re-run before the artifact is measured (NEVER-2)."
}
```

## IRPT_YCDGEN-W6-S1 -- no schema change can make a regeneration byte-identical to the committed AnalysisReport.ts: the generator cannot emit the committed form and its header carries the schema sha256

```json
{
  "id": "IRPT_YCDGEN-W6-S1",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~6",
  "surfaced_at": "2026-10-08T07:50:00Z",
  "one_line": "YCD-u-6 AC2 is unreachable: with the OPAL_ENGINE branch added the generator output differs from the committed type first at line 5 (the Source sha256 line) and in 43 committed lines no schema can make it emit.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "spec_asserts": "YCD-u-6 contract R19: the generator, run to a temporary directory against the new schema, produces an AnalysisReport.ts byte-identical to the committed one at portal d1b21c97.",
  "world_is": "u6_checks.py regen (a copy of gen-wire.ts run from portal/ with --no-install, out-dir in a temp tree, portal tree unchanged before and after): against the BASE schema a regeneration drops 56 lines of the committed type (S388 reproduced); against the changed schema (sha256 9c55f7c9b8fd0a52956cc394d28859f9917cf4aeca7413530d546496d00b5b67) the generator wrote 241 lines / 7810 bytes, the committed file is 149 lines / 5314 bytes, identical False. FIRST DIFFERING LINE 5: generated ' * Source sha256: 9c55f7c9...' against committed ' * Source sha256: 1bd0dc85...'; the header hashes the schema, so ANY schema change moves it. Beyond line 5 the committed file holds declarations the generator has no code to emit (renderModule prints one export per schema, no descriptions as comments, no named aliases, no template-literal types): AnalysisSectionNotAvailableReason, AnalysisReportOpalSectionWire, AnalysisReportOpalWire, AnalysisReportAnyWire, the INPUT_MISSING:${string} member and the '/** v2 discriminator' comment; all six tokens measured absent from the generated output. The type generated for the changed schema is an intersection 'Base & (YCHARTS form | OPAL form)', not the committed interface plus the hand-added OPAL declarations. The other 26 generated files are identical between the base-schema run and the changed-schema run. A regeneration therefore still replaces the committed hand-added OPAL declarations.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "u6_checks.py regen output (this order, run from the worktree root): rc=1, 'FIRST DIFFERING LINE 5', 'DIFF: 135 lines only in generated, 43 lines only in committed', 'MEASURE base schema: a regeneration drops 56 lines'",
      "portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts at d1b21c97: renderModule emits one export interface or type per schema; no description comments, no named aliases",
      "portal/src/pages/InvestorReporting/contracts/wire/AnalysisReport.ts at d1b21c97 lines 96-149 (the hand-added block)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "A decision is owed, not by this worker: extend the generator to emit the OPAL declarations, or move them to a file the generator does not write, or re-stamp the committed header by hand after each schema change. Until then nobody runs gen-wire into contracts/wire/; iv-e-26.wire-regen.test.ts and any test that calls generate() will still rewrite or fail on this file. No existing branch was changed to force a match."
}
```

## IRPT_YCDGEN-W6-S2 -- the OPAL_ENGINE branch turns existing readers red: five python tests, two portal content pins and the lambda source map's schema sha pin

```json
{
  "id": "IRPT_YCDGEN-W6-S2",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~6",
  "surfaced_at": "2026-10-08T07:50:00Z",
  "one_line": "With the branch in, u6_checks.py census finds 5 python tests and 2 portal content pins newly red against the base schema, plus a stale sha256 pin in lambda-source-map.json; none is fixable inside this order's paths.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "spec_asserts": "YCD-u-6: every reader of the schema is named and reads the new branch without error (AC3).",
  "world_is": "Measured by u6_checks.py census, each reader run under the changed schema and, if red, again under the BASE schema swapped into the working tree (restored afterwards; sha printed). NEW RED against base: (1) _contracts/tests/test_analysisreport_v2.py::test_v1_untouched (pins the v1 file sha256 1bd0dc85 and equality with the packaged copy); (2) export/tests/test_packaged_contracts_match_docs.py[AnalysisReport.schema.json] (the packaged copy under _contracts/ is byte-equal to the docs copy; it is outside this order's paths and still v1, sha 1bd0dc85); (3) ycharts/extract/tests/test_publication.py::test_committed_three_variant_pdfs_preserve_denominators_and_undated_rows[overview, comparison, multicomp] (3 tests: it validates a PARTIAL view with dict(schema, required=list(view)); the v1 required members now live in $defs/ycharts under a top-level oneOf, so the partial view is refused; any root that also validates OPAL documents cannot keep the vendor members in its root required list); (4) portal fe-s-13/content-pins.test.ts: 'AnalysisReport.extraction_validation: no longer REQUIRED' and 'AnalysisReport.vendor_artifact: no longer REQUIRED' (same cause as 3; the other four consumed-required members stay in the root required list, which now names the five members both forms share); (5) infra/aws/lambda/ci/lambda-source-map.json carries the docs schema sha256 1bd0dc85 for two packagings, now stale. UNCHANGED and green: test_undated_analysis (12), test_owned_report (32), test_repository (24); the 7 portal tests failing at base (incl. unprojected_grant) are identical before and after. The deployed validators (export/submit_installed.py, reports/resident_installed.py, reports/generate_installed.py, both run_offline_suite.py) read the PACKAGED copy, which carries no OPAL branch until it is synced to the docs copy and re-pinned.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "u6_checks.py census output: 'NEW RED 1: [test_v1_untouched]', 'NEW RED 1: [test_the_packaged_schema_is_byte_equal_to_the_published_docs_copy[...]]', 'NEW RED 3: [test_committed_three_variant_pdfs_...]', 'PORTAL NEW AnalysisReport pin problems vs base: 2', 'manifest ... sha256 pin of the docs schema is the BASE sha (STALE after this change)'",
      "baseline run by hand before the edit: the six python modules 93 passed; portal content-pins, producer-fixtures and fe-s-1 fixtures 15 pass 5 fail, the same 5 failing under the base schema",
      "infra/aws/lambda/ci/lambda-source-map.json lines 4235 and 4888 (repo_path docs/.../AnalysisReport.schema.json, sha256 1bd0dc85...)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Landing this schema without the follow-ups reddens those tests in the drain: packaged copy sync and the v1 sha re-pin (BCKEND lane), the source-map re-pin, the partial-view test (it reads a root required list that no OPAL-capable root can keep) and portal consumed.ts / content pins. None is touched here: all are outside <paths>."
}
```

## IRPT_YCDGEN-W6-S3 -- carrying the OPAL_ENGINE form at the v1 root needed more than a new branch: the root additionalProperties and required moved into $defs/ycharts and two property definitions became anyOf

```json
{
  "id": "IRPT_YCDGEN-W6-S3",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~6",
  "surfaced_at": "2026-10-08T07:50:00Z",
  "one_line": "A document of the OPAL form cannot validate against the v1 root as it stood (root additionalProperties false, vendor members required, sections and effective_inputs shaped for the vendor form), so the root was restructured while every v1 document and every #/properties pointer stays valid.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-u-6 section 1: add the OPAL_ENGINE form as a NEW, ADDITIVE branch; do not change, narrow or remove any existing branch.",
  "world_is": "What changed in AnalysisReport.schema.json (sha256 9c55f7c9b8fd0a52956cc394d28859f9917cf4aeca7413530d546496d00b5b67): the v1 form is now $defs/ycharts, with the root's old additionalProperties:false and full required list moved into it unchanged and every property referenced from the root properties; $defs/opal_engine is copied verbatim from _contracts/AnalysisReport.v2.schema.json $defs/opal_engine; the root is oneOf those two, with required narrowed to the five members both forms share (request_ref, effective_inputs, sections, disclosures, release); a root provider property (enum YCHARTS or OPAL_ENGINE, optional on the v1 form) is added. The root properties stay so #/properties/request_ref, sections, extraction_validation, undated_sections and extraction_coverage (analysis-report.response.schema.json; test_owned_report.py) keep resolving; properties.effective_inputs and properties.sections.items are now anyOf [v1 definition, OPAL definition], and undated_sections' internal refs point at #/properties/sections/items/anyOf/0/... Measured: 7 AnalysisReport documents in 10010 tracked json files (outer plus portal); 2 valid before, the same 2 valid after, 0 regressions, 2 newly valid (the v2 OPAL and v2 YCHARTS fixtures), 3 invalid both; the OPAL fixture is valid and the vendor-member and NOT_AVAILABLE-without-reason fixtures are refused. The file is re-serialised with json.dumps(indent=2), so the diff is larger than the change.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "u6_checks.py schema output: 'COUNT: 7 documents; valid before 2; valid before and after 2; valid before and NOT after 0; newly valid 2; invalid both 3' and six BRANCH lines as expected",
      "base schema bytes: git show 1974945570:docs/contracts/investor-reporting/v1/AnalysisReport.schema.json sha256 1bd0dc85847690b277e3a3011bcbe500a02820792cd53a38a1201fc3c55d153f"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "A purely additive change (new $defs and an optional provider only, root untouched) would keep every reader green but leave the OPAL form invisible to the root validator and to the generator, which reads the root. Which reading the CTO's ruling (msg 1194) meant is the issuer's to confirm; the worker took the reading that makes the root carry the form."
}
```

## IRPT_YCDGEN-W6-S4 -- the analysis-report response schema requires extraction_validation, so a response slice of the OPAL form is refused

```json
{
  "id": "IRPT_YCDGEN-W6-S4",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~6",
  "surfaced_at": "2026-10-08T07:50:00Z",
  "one_line": "analysis-report.response.schema.json data requires request_ref, sections and extraction_validation; an OPAL_ENGINE report has no extraction_validation (it has computation_validation), so its sections slice does not validate against the response contract even though the sections pointer now accepts the OPAL section shape.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-u-6 section 1: every reader of the schema is read against the new branch.",
  "world_is": "u6_checks.py census builds the response validator over the five pointers into the changed schema (registry of the v1 schemas) and validates a slice from the v1 valid fixture (request_ref, sections, extraction_validation): VALID; the same slice from the v2 OPAL valid fixture (request_ref, sections): invalid (a required member of the response data is absent). The five pointers all resolve in the changed schema.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "u6_checks.py census: READER [response] ... 'AnalysisReport.valid.json VALID; AnalysisReport.v2.opal.valid.json invalid'",
      "docs/contracts/investor-reporting/v1/responses/analysis-report.response.schema.json lines 48-70 (data required: request_ref, sections, extraction_validation)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The response schema is outside this order's paths and the served OPAL route is not this cell's; recorded so the response contract is read against the OPAL form before anyone serves it through this route."
}
```

## IRPT_YCDGEN-D2-W6-S1 -- With gen-wire.ts reading AnalysisReport from the v2 schema, the generated body is not identical to the committed AnalysisReport.ts: the committed file

```json
{
  "id": "IRPT_YCDGEN-D2-W6-S1",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~6",
  "surfaced_at": "2026-10-08T17:20:00Z",
  "one_line": "With gen-wire.ts reading AnalysisReport from the v2 schema, the generated body is not identical to the committed AnalysisReport.ts: the committed file is hand-edited (annotation, optional provider, three hand-added OPAL types), the generator emits one union type.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-u-6 section 2 R19 (recut): the generated AnalysisReport.ts body equals the committed one (header excluded); section 1: the OPAL_ENGINE form is carried by the generated type.",
  "world_is": "u6_checks.py regen (bun --no-install from portal/, schemaFilePath('AnalysisReport') = the v2 file, source header cites infra/aws/lambda/investor-reporting/_contracts/AnalysisReport.v2.schema.json): generated body 134 lines, committed body 139 lines; FIRST DIFFERING BODY LINE 2: generated '  readonly provider: 'YCHARTS'' vs committed '  /** v2 discriminator (IRPT_BCKEND PRD v0.28 item 29). ... */' followed by 'readonly provider?: 'YCHARTS''. The generator renders the schema's top-level oneOf as `export type AnalysisReportWire = {...YCHARTS...} | {...OPAL_ENGINE...}` (inline, provider required on both). The committed file keeps `export interface AnalysisReportWire` (YCHARTS members only, provider optional) and appends hand-added AnalysisSectionNotAvailableReason (template-literal union for reason), AnalysisReportOpalSectionWire, AnalysisReportOpalWire (request_ref and disclosures and release as indexed access into AnalysisReportWire) and AnalysisReportAnyWire. Last change to the committed file: portal 81bbeba2 (YCD-u-6-adjacent YCD-e-6, Analysis tab reads the OPAL_ENGINE form), whose in-file comment says 'Hand-added beside the generated v1 interface'. The generator edit itself is correct and complete for this cell (v1 byte-frozen, every other contract unchanged); equality cannot be reached without editing a schema (reason as a pattern, provider optional) or the committed type or the generator's union rendering, none of which this cell may do.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "u6_checks.py regen output 'FIRST DIFFERING BODY LINE 2' and 'DIFF: 33 lines only in generated, 38 only in committed'",
      "portal/src/pages/InvestorReporting/contracts/wire/AnalysisReport.ts lines 92-149 at d1b21c97 (hand-added OPAL types)",
      "consistent with row IRPT_YCDGEN-W6-S1 (measured on the v1-edit attempt)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Consumers that index AnalysisReportWire['request_ref'] and the three OPAL names depend on the committed shape, so replacing the committed file with the generated union would break them. A next cell has to choose one of: teach the generator to emit the interface-plus-OPAL-types form from the v2 schema, or drop the hand-added block and migrate the consumers to the union. AC2 is recorded FAIL, not forced."
}
```

## IRPT_YCDGEN-D2-W6-S2 -- Three python tests among the readers of the AnalysisReport schemas fail in this worktree for reasons that do not touch either schema: a routes.json co

```json
{
  "id": "IRPT_YCDGEN-D2-W6-S2",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~6",
  "surfaced_at": "2026-10-08T17:21:00Z",
  "one_line": "Three python tests among the readers of the AnalysisReport schemas fail in this worktree for reasons that do not touch either schema: a routes.json count of 19 where the test expects 20 (two tests), and an absent brand asset (one test).",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-u-6 AC3: every reader of either AnalysisReport schema is named and its tests pass.",
  "world_is": "u6_checks.py census runs 20 python tests (33 outer readers outside org/, found by searches A and C; 6 portal readers named, not run): 17 pass; test_owned_request_contracts.py::test_public_routes_are_declared_against_the_installed_status_handler and test_upload_contract.py::test_route_denominators_are_measured_and_upload_is_declared_against_generate both fail 'assert 19 == 20' on the length of a route list; ycharts/research/tests/test_opal_producer.py::test_the_real_layout_renders_the_pdf_with_the_not_in_this_version_line fails 'LayoutRefused: brand asset absent in 2 root(s): deck_generation/brand_spec/brand.json (set IRPT_BRAND_SPEC)'. test_upload_contract.py fails identically when run from the main checkout C:/dev/ajb_workspace, and deck_generation/brand_spec/ is absent from the main checkout and untracked in this worktree. v1 is byte-equal to its merge-base copy and the only portal edit is gen-wire.ts, which no python test reads, so none of the three can be caused by this cell. Consistent with the 19-vs-20 route count carried to the CTO's analysis in row IRPT_BCKEND-S391 (stale api/routes.json).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "u6_checks.py census output 'TESTS: 20 run, 3 failed [...]'",
      "pytest E lines: 'assert 19 == 20' (x2) and 'LayoutRefused: brand asset absent in 2 root(s)'",
      "pytest of test_upload_contract.py from C:/dev/ajb_workspace: 1 failed, 7 passed (same test)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "AC3 is recorded FAIL by the criterion's own wording (every test passes). The census names the three so the issuer can rule them out of the reader set or fix them in their owning cell."
}
```

## IRPT_YCDGEN-D2-W6-S3 -- the generator emits an invalid `interface` for the v2 union; the committed generated AnalysisReport.ts does not typecheck and two wire files are outside this order's paths

```json
{
  "id": "IRPT_YCDGEN-D2-W6-S3",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~6",
  "surfaced_at": "2026-10-08T17:41:00Z",
  "one_line": "The generator emits `export interface AnalysisReportWire {..} | {..}` for the v2 union, which is not valid TypeScript, so the committed generated AnalysisReport.ts fails the portal typecheck (35 syntax errors); wire/index.ts and wire/responses.ts also name the hand-added types and are outside this order's paths.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "spec_asserts": "YCD-v-6 R20: the committed AnalysisReport.ts equals the generator's output from v2, every consumer reads the generated union, the portal typechecks, and its InvestorReporting tests pass as they did. Order bars a gen-wire.ts edit and limits the write grant under contracts/wire/ to AnalysisReport.ts.",
  "world_is": "(1) renderModule tests `body.startsWith('{') && body.endsWith('}')` to choose `interface`; a union body `{...} | {...}` passes that test, so gen-wire.ts line ~421 emits `export interface AnalysisReportWire {...} | {...}`. bun typecheck (tsc -b --noEmit) on the regenerated file: 35 errors, all TS1109/TS1005/TS1011 in contracts/wire/AnalysisReport.ts lines 94-141. (2) Measured with a TEMPORARY, uncommitted edit that changes only that one keyword to `export type AnalysisReportWire = {`, typecheck of the whole portal is rc 0 with the consumers migrated here (adapt.ts, contracts/index.ts, coverage.test.ts; investor-reporting.ts needed no edit), but ONLY with two further temporary edits to files this order may not write: contracts/wire/index.ts (re-exports AnalysisReportAnyWire, AnalysisReportOpalSectionWire, AnalysisReportOpalWire, AnalysisSectionNotAvailableReason, no longer exported) and contracts/wire/responses.ts (imports AnalysisReportOpalWire and reads AnalysisReportWire['extraction_validation'|'undated_sections'|'extraction_coverage'], members only the YCHARTS branch has). (3) The committed branch state is therefore: AC1 PASS, typecheck FAIL (35 errors in AnalysisReport.ts, which also hide any semantic errors elsewhere), and the InvestorReporting suite has exactly one test that was green at d1b21c97 and is red here, iv-e-17.regenerated.test.ts 'IVE17-AC2 -- the regenerated wire carries every landed ask, and the portal typechecks clean', which runs tsc and fails on the same 35 errors. (4) Side finding: running the portal suite in the real tree executes iv-e-26.wire-regen and rewrites every file under contracts/wire/; the rewrite changed ExportBundle.ts, ExportReceipt.ts, HoldingsSnapshot.ts, index.ts and responses.ts, so those five already differ from the generator's output at d1b21c97. The worker restored all of them from HEAD (git status clean apart from the four paths in this order) and v6_checks.py tests runs both trees in temporary copies so it cannot recur.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "v6_checks.py typecheck: 'rc=2 ; 35 error line(s)' and '35 error(s) in src/pages/InvestorReporting/contracts/wire/AnalysisReport.ts'",
      "v6_checks.py tests: 'green at d1b21c97: 900 ; of those not green at head: 1' naming iv-e-17.regenerated.test.ts IVE17-AC2",
      "portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts renderModule, the `body.startsWith('{') && body.endsWith('}')` choice between interface and type",
      "temporary experiment: typecheck rc 0 with the interface->type keyword change plus the two wire/index.ts and wire/responses.ts edits described above (not committed; reproducible from the description)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "ARMED because draining the portal branch as it stands lands a tree that does not typecheck. Disarm: either do not drain dc88c4f7 plus this cell's portal commit until a cell with write grants on gen-wire.ts (union bodies emit `export type`), wire/index.ts and wire/responses.ts (drop the four hand-added names, derive the YCHARTS slice with Extract) has run, or amend this order's paths to include them and re-run. The consumer migration in this order is correct and complete against that fixed shape."
}
```

## IRPT_YCDGEN-D2-S1 -- dell2 F1 retry blocked by construction: the only Opal-served principal is Andrew's own sign-in

```json
{
  "id": "IRPT_YCDGEN-D2-S1",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-08T17:15:45Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "The dell2 F1 retry (Andrew 'HAVE DELL2 RETRY'; CTO ruling CTO_RULING_IRPT_YCDGEN_FWD1_DELL2_RETRY_20261008.md) cannot meet conditions 1 and 4 together: the one principal a seat can sign in as is served by the YCharts producer, and the only Opal-served principal is Andrew's own sign-in",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "spec_asserts": "The ruling counts a dell2-made run when it goes through the deployed portal route as an authenticated Cottonwood-allowed principal, on one real Cottonwood portfolio, ends in an Opal-made Overview read back, with zero YCharts calls measured.",
  "world_is": "infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py:121 OPAL_PRODUCER_PRINCIPALS = ('andrew@opalinvest.com',); producer_for (:126-131) sends every other principal to the YCharts path; :115-120 say the list changes only on Andrew's word and 'No other principal goes on this list'. The one seat-usable Cottonwood-allowed principal is svc-irpt-analysis@opalinvest.com (userType service, allowedFirmIds cottonwood; IRPT_MVP_Y/live_walk/svc_principal.py:30-60): a run as it would take the YCharts path, so condition 4 fails and a vendor call would be made. Signing in as Andrew is not a seat act. No real Cottonwood holdings file is held on dell2 (repo files are AAPL/VNQ test portfolios). UNMEASURED: whether the upload's symbol resolve contacts the provider on the Opal path (inferred from the provider lease at resident_worker.py:737-744, not traced).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "resident_worker.py:112-131 at dell2 CLOUD 8442ad9b0a",
      "svc_principal.py:30-60",
      "portal route map: api-client.ts:15,147,160-165; ProspectComposer.tsx:266-325; investor-reporting.ts:1325-1350"
    ]
  },
  "notes": "No run was made: running as the service principal would itself be a YCharts call. Unblocks on Andrew's word, one of: (a) add svc-irpt-analysis@opalinvest.com to OPAL_PRODUCER_PRINCIPALS for this run (a resident release) and name the real Cottonwood holdings file to submit; or (b) the organic arm, Andrew's own run. Result sent to 0.0.0_AB_MSTR~DELL2 per the ruling."
}
```

## IRPT_YCDGEN-D2-S2 -- round-close-check reads an empty expected to_id and refuses every round-6 proof

```json
{
  "id": "IRPT_YCDGEN-D2-S2",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-08T18:25:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "one_line": "round-close-check.py refuses all 19 round-6 proof instances with \"names to_id '<the order's own id>', not ''\": the expected to_id it compares against is empty",
  "spec_asserts": "round-close-check.py grades each complete order's proof instance against that order's to_id, so a well-formed instance whose to_id is the order's own id passes.",
  "world_is": "`python .tools/round-close-check.py --project IRPT_YCDGEN --round 6` at dell2 CLOUD 2c287dec89 (2026-10-08 ~18:2xZ): ORDERS 19 complete; PROOF-BAD 19 of 19, each line 'names to_id IRPT_YCDGEN.TO-YCD-<x>-6.<slug>, not ''' -- the instance's to_id is the order's file stem and the expected value is empty; PROOFS proof_ok=0 proof_bad=19; verdict=REFUSED. The same instances pass .tools/proof-of-spec-check.py (VALID rc=0 on u-6 and v-6 today). UNMEASURED: which code path yields the empty expected id (likely the tree task-orders/ layout vs a flat task_orders/ read).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "round-close-check.py output, 19 PROOF-BAD lines, verdict=REFUSED",
      "proof-of-spec-check.py VALID rc=0 on IRPT_YCDGEN.TO-YCD-v-6 instance @e02ad46806"
    ]
  },
  "notes": "Not a round-6 defect: the round's close also waits on FWD-1 (F1 release held to ~20:0xZ). Owner of the checker to confirm; this seat keeps working."
}
```

## IRPT_YCDGEN-D2-S3 -- the resident host has no Opal brand asset: every Opal-path Overview ends LayoutRefused

```json
{
  "id": "IRPT_YCDGEN-D2-S3",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-08T21:24:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "one_line": "The resident host has no Opal brand spec or logo, so the Opal layout refuses EVERY Opal-path Overview (svc's F1 run and Andrew's alike): F1 ended retained_for_retry class=LayoutRefused",
  "spec_asserts": "FWD-1: an Opal-made Overview renders for a listed principal on the resident host (CTO ruling d54e0b7515: real route, real portfolio, rendered read-back, zero YCharts calls).",
  "world_is": "F1 run 21:10:18-21:10:32Z as svc through CloudFront (f1_svc_release/F1_RUN_RECORD_20261008.json): login 200, upload NORMALIZED, submit QUEUED as REQ-8966d24ffefa1c28269ef26c. Resident journal (SSM b6145e25, 2db64430): 21:10:24 IRPT_RESIDENT_RESOLVE state=READY; 21:10:31 'Classification not found for ticker: $:CASH' then 'IRPT_RESIDENT_POLL retained_for_retry class=LayoutRefused code=-'. Host: the st25 root holds no brand*.json; unit env carries IRPT_PLAYWRIGHT_CORE only (no IRPT_BRAND_SPEC/IRPT_OPAL_LOGO). layout_overview.py:101-108 (_asset_path) finds the asset only via git roots or those env vars, and raises LayoutRefused('brand asset absent ...') otherwise; st24 differs from st25 only in the allow-list constant, so it refuses Andrew's runs identically. YCharts markers in the window (VENDOR_REQUESTS, STEP, WAF, READ_BACK, SESSION_ROTATION, ycharts.com): 0 of 40 lines. UNMEASURED: the exception text (the journal logs code=-); the match to line 108 is by the code path.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "F1_RUN_RECORD_20261008.json",
      "resident journal SSM b6145e25 + 2db64430 (read-only, inside the F1 shell window)",
      "infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py:101-116 at 3cf5d52a7b"
    ]
  },
  "notes": "CTO~DELL2 ruling msg 1664: next YCDGEN cell = a resident release carrying the brand asset (packaged into the root, or IRPT_BRAND_SPEC/IRPT_OPAL_LOGO set) under its own pair, after-read = one Opal-path layout renders; F1 retries after it. The retained SQS message keeps st25 in place until it dead-letters (an st24 retry would route svc to YCHARTS)."
}
```

## IRPT_YCDGEN-D2-W7-S1 -- The resident builder's --research filter (RESEARCH_EXT) omits .svg, so a --research build does not package the Opal logo and the resident host would s

```json
{
  "id": "IRPT_YCDGEN-D2-W7-S1",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~7",
  "surfaced_at": "2026-10-08T22:59:30Z",
  "one_line": "The resident builder's --research filter (RESEARCH_EXT) omits .svg, so a --research build does not package the Opal logo and the resident host would still refuse the Opal page; the logo only ships through an explicit --member.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "spec_asserts": "R21: the resident package builder's --research packages both brand files (tracked, non-test files under ycharts/research/); the Opal layout then renders from a package tree outside any git repository.",
  "world_is": "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py line 58: RESEARCH_EXT = ('.py', '.json', '.sh', '.md', '.cjs'); research_wanted() returns False for ycharts/research/brand/Opal-Capital-Logo-Full-Color.svg (w6_checks.py render prints 'builder research_wanted(svg)=False'). brand.json is packaged by --research (.json); the logo is not. The builder is outside this order's paths (not edited). AC3 packages the logo through the builder's own --member rule (ycharts/research/brand/Opal-Capital-Logo-Full-Color.svg=<repo path>), which renders.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "w6_checks.py render output: package=11 members (logo via --member: builder research_wanted(svg)=False) ... pdf=%PDF 41013 bytes 2 pages",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py:58 and :83-87 at 730e5cabf9"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Disarm either way: add '.svg' to RESEARCH_EXT in the builder (a cell with that path), or pass --member ycharts/research/brand/Opal-Capital-Logo-Full-Color.svg=infra/aws/lambda/investor-reporting/ycharts/research/brand/Opal-Capital-Logo-Full-Color.svg on the release build and read the package listing for the file before the apply. This seat keeps working."
}
```

## IRPT_YCDGEN-D2-W7-S2 -- build_brand_spec() output depends on the box: its logo.variants block is read from deck_generation/brand/logo_package (gitignored), which dell2 does n

```json
{
  "id": "IRPT_YCDGEN-D2-W7-S2",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~7",
  "surfaced_at": "2026-10-08T22:59:45Z",
  "one_line": "build_brand_spec() output depends on the box: its logo.variants block is read from deck_generation/brand/logo_package (gitignored), which dell2 does not hold, so the packaged brand.json carries formats {} and preferred null for all 6 variants; the laptop would write relative paths.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-w-6: brand.json is written byte-identically to what build_brand_spec() produces.",
  "world_is": "On this box deck_generation/brand/ is absent in the worktree and the main tree, build_brand_spec() returns missing = all 6 variants (w6_checks.py bytes prints 'logo variants missing on this box: 6 of 6'). brand.json is therefore byte-equal to the function's output HERE, but a laptop run would differ in logo.variants only. load_brand() reads only colors and typography from the spec (layout_overview.py _palette, brand['spec']['typography']), so the Opal page is unaffected; AC2 re-run on a box holding the logo package would report a bytes difference.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "w6_checks.py bytes output: brand.json=5996 bytes equals build_brand_spec() (logo variants missing on this box: 6 of 6)",
      "deck_generation/scripts/03_extract_brand_spec.py build_brand_spec() variants loop at 730e5cabf9",
      "layout_overview.py _palette and typography reads at 730e5cabf9"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No action needed for the Opal page. If a byte-identical-to-laptop spec is wanted, regenerate brand.json on the laptop and replace the file under a cell that names that."
}
```

## IRPT_YCDGEN-D2-W8-S1 -- the accepted ANALYSIS request record carries no server-recorded actor, so producer_for cannot read one; YCD-x-6 code arm stopped

```json
{
  "id": "IRPT_YCDGEN-D2-W8-S1",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~8",
  "surfaced_at": "2026-10-09T01:39:00Z",
  "one_line": "The accepted ANALYSIS request record carries no server-recorded actor (only the UPLOAD row does), so YCD-x-6's code arm is stopped and test case 1 (owner=advisor, actor=listed -> OPAL) cannot pass.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "YCD-x-6: the accepted ANALYSIS request the resident reads carries a server-recorded actor, so producer_for can read it when present; test case 1 (owner = an invented advisor, actor = a listed principal -> OPAL) passes.",
  "world_is": "x6_checks.py census (21 fields scanned): the only server-recorded acting principal in investor-reporting non-test code is intake/uploads.py:267 (original['acting_principal_id'], on-behalf UPLOAD# index row). The accepted analysis record built in ycharts/generate/acceptance.py DynamoAcceptance.accept has 5 top-level fields (identity, owner, browser_sha256, composition_ref, accepted_at), 6 identity fields, the queue message 4 (tenant, request_id, revision, composition_sha256), the job row 6: none is an actor. Path that would have to record it: SubmissionService.submit (submission_service.py:109 holds `principal`, the verified submitter) calls self.acceptance.accept(owner, browser, ref, ...) at :145 without passing it; accept() would take an `acting_principal_id` argument and write it into `record` (acceptance.py:107-112), and resident_worker.producer_for would then read record.get('acting_principal_id'). Premise to check before that cell is cut: on the analysis path the owner is already the submitter -- submission_service.py:115 refuses owner.principal_id != principal.principal_id (ACTUAL_SUBMITTER_REQUIRED) and prospect_submission.py:72-73,111 builds request_owner from the VIEWER (access.prospect_owner) -- so a listed filer's analysis is owned by the filer and producer_for already returns OPAL for it; the advisor-owned shape of E5 (served.py _create_owner, :1000-1051) is the UPLOAD/CREATE_INPUT owner, and the analysis only reaches an advisor owner when the advisor files it, who is not listed. Read in code, not run. The test file ycharts/generate/tests/test_producer_actor.py carries the proposed field as ACTOR_KEY and marks case 1 xfail(strict); x6_checks.py cases therefore prints FAIL (3 of 4).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "x6_checks.py census output: 'server-recorded actor on UPLOAD=1 (uploads.py:267); on ANALYSIS SUBMIT/accepted record/queue message/job row=0 of 21 fields (5+6+4+6)'",
      "infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py:107-112 (record), :166-168 (queue body), :114-116 (job row) at 0dc9addc92",
      "infra/aws/lambda/investor-reporting/ycharts/generate/submission_service.py:109,115,145 and prospect_submission.py:72-73,111 at 0dc9addc92",
      "x6_checks.py cases output: 'RESULT: cases FAIL (3 of 4 producer cases pass)'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "resident_worker.py was not edited (code arm stopped per the cell). If the issuer still wants the field, the cell needs paths acceptance.py and submission_service.py (and a decision on the premise above); then case 1 flips and strict xfail turns the suite red until the marker is removed."
}
```

## IRPT_YCDGEN-D2-S4 -- no partner firm has a FIRM_OPERATIONS-capable row; cottonwood has no FIRM_ADVISOR-capable row

```json
{
  "id": "IRPT_YCDGEN-D2-S4",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T01:56:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "one_line": "No registered partner firm has a row E5 can resolve as FIRM_OPERATIONS (0 admin users at every firm), and cottonwood has no FIRM_ADVISOR-capable row either: an on-behalf upload for cottonwood is impossible on current data",
  "spec_asserts": "E5 (served.py _advisor_owner) accepts an on-behalf owner of class FIRM_ADVISOR (an advisorId from the partner row's advisorKey) or FIRM_OPERATIONS (role/advisorRole admin with a verified firm), per resolve_prospect_owner (_scope/prospect.py:34).",
  "world_is": "advisor_census.py (read-only, counts only) 2026-10-09 ~01:54Z: 49financial 11 partner rows, 11 with advisorKey, 11 active users all role user, 0 admin; inflection 7 rows, 6 with advisorKey, 7 active role user, 0 admin; cottonwood 5 rows, 0 with advisorKey, 5 active role user, 0 admin. So FIRM_OPERATIONS is unreachable at every firm, and a cottonwood on-behalf filer (svc lists cottonwood) is always refused 'verified firm advisor or operations owner required'.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/ADVISOR_CENSUS_20261009.txt @c7ba00eea0",
      "_scope/prospect.py:34",
      "_scope/resolve.py:239-241"
    ]
  },
  "notes": "CTO~DELL2 ruling msg 2148: the seat-driven F1 moves to 49financial (svc's allowedFirmIds swapped cottonwood -> 49financial under a pair after st27). Whether any firm should carry an operations owner is a data question for the partner-onboarding owner, not this project."
}
```

## IRPT_YCDGEN-D2-S5 -- RESOLVES IRPT_YCDGEN-S16

```json
{
  "id": "IRPT_YCDGEN-D2-S5",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T04:30:00Z",
  "disposition": "DISMISSED_WITH_REASON",
  "one_line": "RESOLVES IRPT_YCDGEN-S16: the analysis POST's success reply leaked internal_correlation_id (ENVELOPE_STATUS)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "irpt-ycharts-generate release 1 (live 2026-10-08 10:06Z) projects the success status like the refusal path; after-read 4 PASS: the deployed status envelope carr"
    ]
  },
  "dismissal_reason": "irpt-ycharts-generate release 1 (live 2026-10-08 10:06Z) projects the success status like the refusal path; after-read 4 PASS: the deployed status envelope carries no internal_correlation_id (2.0.0_SA_COO~Y2 msg 1254, release1_ycg/RELEASE1_AFTER_READS.md).",
  "spec_asserts": "IRPT_YCDGEN-S16 as filed.",
  "world_is": "MEASURED: irpt-ycharts-generate release 1 (live 2026-10-08 10:06Z) projects the success status like the refusal path; after-read 4 PASS: the deployed status envelope carries no internal_correlation_id (2.0.0_SA_COO~Y2 msg 1254, release1_ycg/RELEASE1_AFTER_READS.md)."
}
```

## IRPT_YCDGEN-D2-S6 -- RESOLVES IRPT_YCDGEN-D2-S1

```json
{
  "id": "IRPT_YCDGEN-D2-S6",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T04:30:00Z",
  "disposition": "DISMISSED_WITH_REASON",
  "one_line": "RESOLVES IRPT_YCDGEN-D2-S1: the dell2 F1 retry was blocked by construction (only Andrew on the Opal list)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Superseded: Andrew approved svc on the list (ANDREW_DIRECT_20261008_175xZ...); the svc runs then measured E5 (rows D2-S4, D2-W8-S1) and the seat arm moved to 49"
    ]
  },
  "dismissal_reason": "Superseded: Andrew approved svc on the list (ANDREW_DIRECT_20261008_175xZ...); the svc runs then measured E5 (rows D2-S4, D2-W8-S1) and the seat arm moved to 49financial (CTO~DELL2 msg 2148; st28 @698651c9a9). Andrew's own run is unaffected (no allowedFirmIds).",
  "spec_asserts": "IRPT_YCDGEN-D2-S1 as filed.",
  "world_is": "MEASURED: Superseded: Andrew approved svc on the list (ANDREW_DIRECT_20261008_175xZ...); the svc runs then measured E5 (rows D2-S4, D2-W8-S1) and the seat arm moved to 49financial (CTO~DELL2 msg 2148; st28 @698651c9a9). Andrew's own run is unaffected (no allowedFirmIds)."
}
```

## IRPT_YCDGEN-D2-S7 -- RESOLVES IRPT_YCDGEN-D2-S3

```json
{
  "id": "IRPT_YCDGEN-D2-S7",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T04:30:00Z",
  "disposition": "DISMISSED_WITH_REASON",
  "one_line": "RESOLVES IRPT_YCDGEN-D2-S3: the resident host had no Opal brand asset, so every Opal-path Overview ended LayoutRefused",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "st27 LIVE (TO-APPLY-st27 complete @936c0db0b4): V1 @5632e869f3 read load_brand resolving /opt/irpt-resident/e606008994-st27/ycharts/research/brand/ from the run"
    ]
  },
  "dismissal_reason": "st27 LIVE (TO-APPLY-st27 complete @936c0db0b4): V1 @5632e869f3 read load_brand resolving /opt/irpt-resident/e606008994-st27/ycharts/research/brand/ from the running root, env brand vars [], logo 3853 bytes.",
  "spec_asserts": "IRPT_YCDGEN-D2-S3 as filed.",
  "world_is": "MEASURED: st27 LIVE (TO-APPLY-st27 complete @936c0db0b4): V1 @5632e869f3 read load_brand resolving /opt/irpt-resident/e606008994-st27/ycharts/research/brand/ from the running root, env brand vars [], logo 3853 bytes."
}
```

## IRPT_YCDGEN-D2-S8 -- RESOLVES IRPT_YCDGEN-D2-W6-S1

```json
{
  "id": "IRPT_YCDGEN-D2-S8",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T04:30:00Z",
  "disposition": "DISMISSED_WITH_REASON",
  "one_line": "RESOLVES IRPT_YCDGEN-D2-W6-S1: the generated AnalysisReport body could not equal the hand-edited committed type",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "YCD-v-6 regenerated the committed type from v2 and migrated its consumers; u6_checks regen PASS 134/134 (@e02ad46806); on portal DEV 38cc0ecf and CLOUD/box via "
    ]
  },
  "dismissal_reason": "YCD-v-6 regenerated the committed type from v2 and migrated its consumers; u6_checks regen PASS 134/134 (@e02ad46806); on portal DEV 38cc0ecf and CLOUD/box via drain @94d866956b.",
  "spec_asserts": "IRPT_YCDGEN-D2-W6-S1 as filed.",
  "world_is": "MEASURED: YCD-v-6 regenerated the committed type from v2 and migrated its consumers; u6_checks regen PASS 134/134 (@e02ad46806); on portal DEV 38cc0ecf and CLOUD/box via drain @94d866956b."
}
```

## IRPT_YCDGEN-D2-S9 -- RESOLVES IRPT_YCDGEN-D2-W6-S2

```json
{
  "id": "IRPT_YCDGEN-D2-S9",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T04:30:00Z",
  "disposition": "DISMISSED_WITH_REASON",
  "one_line": "RESOLVES IRPT_YCDGEN-D2-W6-S2: three reader tests red, unrelated to either AnalysisReport schema",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "u-6 AC3 amended to 'no reader newly red against CLOUD' (@39e5b55275); census PASS: 0 of 20 newly red; the reds are red on CLOUD too and belong to other cells (r"
    ]
  },
  "dismissal_reason": "u-6 AC3 amended to 'no reader newly red against CLOUD' (@39e5b55275); census PASS: 0 of 20 newly red; the reds are red on CLOUD too and belong to other cells (route counts, an absent gitignored brand asset).",
  "spec_asserts": "IRPT_YCDGEN-D2-W6-S2 as filed.",
  "world_is": "MEASURED: u-6 AC3 amended to 'no reader newly red against CLOUD' (@39e5b55275); census PASS: 0 of 20 newly red; the reds are red on CLOUD too and belong to other cells (route counts, an absent gitignored brand asset)."
}
```

## IRPT_YCDGEN-D2-S10 -- RESOLVES IRPT_YCDGEN-D2-W6-S3

```json
{
  "id": "IRPT_YCDGEN-D2-S10",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T04:30:00Z",
  "disposition": "DISMISSED_WITH_REASON",
  "one_line": "RESOLVES IRPT_YCDGEN-D2-W6-S3: the generator rendered a union body as 'export interface', so the portal did not typecheck",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "gen-wire.ts renders a top-level union as 'export type' (portal 1c306eb3; render diff 1 of 27 files); typecheck rc 0 on merged DEV 38cc0ecf (CTO~DELL2 msg 1366);"
    ]
  },
  "dismissal_reason": "gen-wire.ts renders a top-level union as 'export type' (portal 1c306eb3; render diff 1 of 27 files); typecheck rc 0 on merged DEV 38cc0ecf (CTO~DELL2 msg 1366); landed on DEV on Andrew's word.",
  "spec_asserts": "IRPT_YCDGEN-D2-W6-S3 as filed.",
  "world_is": "MEASURED: gen-wire.ts renders a top-level union as 'export type' (portal 1c306eb3; render diff 1 of 27 files); typecheck rc 0 on merged DEV 38cc0ecf (CTO~DELL2 msg 1366); landed on DEV on Andrew's word."
}
```

## IRPT_YCDGEN-D2-S11 -- RESOLVES IRPT_YCDGEN-D2-W7-S1

```json
{
  "id": "IRPT_YCDGEN-D2-S11",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T04:30:00Z",
  "disposition": "DISMISSED_WITH_REASON",
  "one_line": "RESOLVES IRPT_YCDGEN-D2-W7-S1: the builder's --research filter omits .svg, so the logo would not ship",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Ruled at the release: st26/st27 builds pass the logo (and brand.json) via --member; st27 gate 'added members 3 of 3'; V1 read the logo (3853 bytes) from the run"
    ]
  },
  "dismissal_reason": "Ruled at the release: st26/st27 builds pass the logo (and brand.json) via --member; st27 gate 'added members 3 of 3'; V1 read the logo (3853 bytes) from the running root.",
  "spec_asserts": "IRPT_YCDGEN-D2-W7-S1 as filed.",
  "world_is": "MEASURED: Ruled at the release: st26/st27 builds pass the logo (and brand.json) via --member; st27 gate 'added members 3 of 3'; V1 read the logo (3853 bytes) from the running root."
}
```

## IRPT_YCDGEN-D2-S12 -- RESOLVES IRPT_YCDGEN-D2-W8-S1

```json
{
  "id": "IRPT_YCDGEN-D2-S12",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T04:30:00Z",
  "disposition": "DISMISSED_WITH_REASON",
  "one_line": "RESOLVES IRPT_YCDGEN-D2-W8-S1: the accepted analysis record carries no actor field",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Closed on its census (CTO~DELL2 msg 2111): the analysis owner is forced to the submitter (submission_service.py:115), so producer selection by owner is correct "
    ]
  },
  "dismissal_reason": "Closed on its census (CTO~DELL2 msg 2111): the analysis owner is forced to the submitter (submission_service.py:115), so producer selection by owner is correct on that path; no code arm is owed. The census stays as the record.",
  "spec_asserts": "IRPT_YCDGEN-D2-W8-S1 as filed.",
  "world_is": "MEASURED: Closed on its census (CTO~DELL2 msg 2111): the analysis owner is forced to the submitter (submission_service.py:115), so producer selection by owner is correct on that path; no code arm is owed. The census stays as the record."
}
```

## IRPT_YCDGEN-D2-S13 -- RESOLVES IRPT_YCDGEN-W6-S1

```json
{
  "id": "IRPT_YCDGEN-D2-S13",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T04:30:00Z",
  "disposition": "DISMISSED_WITH_REASON",
  "one_line": "RESOLVES IRPT_YCDGEN-W6-S1: a finding of the superseded v1-additive u-6 attempt (df5280bce5)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Superseded by the recut on v2 (CTO~DELL2 msg 1250): v1 stays byte-frozen and the generator reads v2; u-6 and v-6 complete (@eabd287eb3)."
    ]
  },
  "dismissal_reason": "Superseded by the recut on v2 (CTO~DELL2 msg 1250): v1 stays byte-frozen and the generator reads v2; u-6 and v-6 complete (@eabd287eb3).",
  "spec_asserts": "IRPT_YCDGEN-W6-S1 as filed.",
  "world_is": "MEASURED: Superseded by the recut on v2 (CTO~DELL2 msg 1250): v1 stays byte-frozen and the generator reads v2; u-6 and v-6 complete (@eabd287eb3)."
}
```

## IRPT_YCDGEN-D2-S14 -- RESOLVES IRPT_YCDGEN-W6-S2

```json
{
  "id": "IRPT_YCDGEN-D2-S14",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T04:30:00Z",
  "disposition": "DISMISSED_WITH_REASON",
  "one_line": "RESOLVES IRPT_YCDGEN-W6-S2: a finding of the superseded v1-additive u-6 attempt (df5280bce5)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Superseded by the recut on v2 (CTO~DELL2 msg 1250): v1 stays byte-frozen and the generator reads v2; u-6 and v-6 complete (@eabd287eb3)."
    ]
  },
  "dismissal_reason": "Superseded by the recut on v2 (CTO~DELL2 msg 1250): v1 stays byte-frozen and the generator reads v2; u-6 and v-6 complete (@eabd287eb3).",
  "spec_asserts": "IRPT_YCDGEN-W6-S2 as filed.",
  "world_is": "MEASURED: Superseded by the recut on v2 (CTO~DELL2 msg 1250): v1 stays byte-frozen and the generator reads v2; u-6 and v-6 complete (@eabd287eb3)."
}
```

## IRPT_YCDGEN-D2-S15 -- RESOLVES IRPT_YCDGEN-W6-S3

```json
{
  "id": "IRPT_YCDGEN-D2-S15",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T04:30:00Z",
  "disposition": "DISMISSED_WITH_REASON",
  "one_line": "RESOLVES IRPT_YCDGEN-W6-S3: a finding of the superseded v1-additive u-6 attempt (df5280bce5)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Superseded by the recut on v2 (CTO~DELL2 msg 1250): v1 stays byte-frozen and the generator reads v2; u-6 and v-6 complete (@eabd287eb3)."
    ]
  },
  "dismissal_reason": "Superseded by the recut on v2 (CTO~DELL2 msg 1250): v1 stays byte-frozen and the generator reads v2; u-6 and v-6 complete (@eabd287eb3).",
  "spec_asserts": "IRPT_YCDGEN-W6-S3 as filed.",
  "world_is": "MEASURED: Superseded by the recut on v2 (CTO~DELL2 msg 1250): v1 stays byte-frozen and the generator reads v2; u-6 and v-6 complete (@eabd287eb3)."
}
```

## IRPT_YCDGEN-D2-S16 -- RESOLVES IRPT_YCDGEN-W6-S4

```json
{
  "id": "IRPT_YCDGEN-D2-S16",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T04:30:00Z",
  "disposition": "DISMISSED_WITH_REASON",
  "one_line": "RESOLVES IRPT_YCDGEN-W6-S4: a finding of the superseded v1-additive u-6 attempt (df5280bce5)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Superseded by the recut on v2 (CTO~DELL2 msg 1250): v1 stays byte-frozen and the generator reads v2; u-6 and v-6 complete (@eabd287eb3)."
    ]
  },
  "dismissal_reason": "Superseded by the recut on v2 (CTO~DELL2 msg 1250): v1 stays byte-frozen and the generator reads v2; u-6 and v-6 complete (@eabd287eb3).",
  "spec_asserts": "IRPT_YCDGEN-W6-S4 as filed.",
  "world_is": "MEASURED: Superseded by the recut on v2 (CTO~DELL2 msg 1250): v1 stays byte-frozen and the generator reads v2; u-6 and v-6 complete (@eabd287eb3)."
}
```

## IRPT_YCDGEN-D2-S17 -- cause of D2-S2: round-close-check reads the order id only from a <to_id> tag tree orders lack

```json
{
  "id": "IRPT_YCDGEN-D2-S17",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T04:35:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "one_line": "CAUSE of IRPT_YCDGEN-D2-S2: round-close-check.py read_orders takes an order's id only from a <to_id> tag, which tree task orders do not carry, so every tree proof is compared to ''",
  "spec_asserts": "round-close-check.py grades each complete order's proof instance against that order's own id.",
  "world_is": "MEASURED in code at box/dell2: .tools/round-close-check.py:134 builds o['id'] = tag(text, 'to_id') or ''; IRPT_YCDGEN task-orders/*.md carry no <to_id> element (their id is the file stem, which proof instances name as to_id); :165 then refuses every instance ('names to_id <stem>, not '''). Proposed one-line fix: tag(text, 'to_id') or os.path.basename(path)[:-3].",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/round-close-check.py:130-166 at box/dell2 a58150512c",
      "row IRPT_YCDGEN-D2-S2 (19 of 19 round-6 proofs PROOF-BAD)"
    ]
  },
  "notes": "The tool is outside this seat's lane; routed to 1.0.0_SA_CTO~DELL2 as the gate's owner. Until it lands, round 6 cannot read ROUND_CLOSE on this check."
}
```

## IRPT_YCDGEN-D2-S18 -- L9 round 6: f-6 AC5 MET, x-6 AC2 MET on the ruling

```json
{
  "id": "IRPT_YCDGEN-D2-S18",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T04:50:42Z",
  "one_line": "L9 round 6 (CTO msg 2459 route b): TO-YCD-f-6 AC5 MET -- the worker's FAIL was the issuer check counting the Condition key s3:prefix as an action (W1-S16); the fix @50ba89d585 only narrows the read to the Action list and still demands exactly s3:GetObject / s3:ListBucket; this seat's re-run prints 'f-6.AC5 RESULT: PASS'. TO-YCD-x-6 AC2 MET on the ruling, 3 of 4 as written -- this seat's re-run: '3 passed, 1 xfailed'; the xfail case (an advisor-owned request accepted from a listed actor) cannot arise because submission_service.py:115-116 refuses ACTUAL_SUBMITTER_REQUIRED when owner != submitter on first acceptance (CTO msg 2111).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/R6_L9_FAIL_ROW_DISPOSITIONS_20261009.md @7c202254ea",
      "git show 50ba89d585 (f-6.check.py: actions() reads the Action list only)",
      "infra/aws/lambda/investor-reporting/ycharts/generate/submission_service.py:115-116",
      "x6_checks.py cases re-run by this seat ~04:5xZ",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_YCDGEN_ROUND_6_L9_GRADE_20261009.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-YCD-f-6 AC5 and TO-YCD-x-6 AC2 (the two worker FAIL rows of round 6, graded at L9 per CTO msg 2459).",
  "world_is": "Both met: one on a fixed check re-run, one on a ruled census whose unreachable case is confirmed in the code."
}
```

## IRPT_YCDGEN-D2-S19 -- st28 F1: no 49financial research role; the Opal path reaches cottonwood only

```json
{
  "id": "IRPT_YCDGEN-D2-S19",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T09:45:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "one_line": "st28 F1 on 49financial: the Opal path cannot run for any firm but cottonwood -- the runner role may assume only irpt-cot-ycharts-research-role, and irpt-49f-ycharts-research-role does not exist",
  "spec_asserts": "FWD-1: the Opal engine serves a non-Andrew filer's Overview; st28 put svc on the allow list and on 49financial for that one run (CTO msg 2148).",
  "world_is": "MEASURED. F1 submit at 09:13:27Z (REQ-1f8b4cc4682f2d929cc70215) was accepted QUEUED; producer selection held (0 YCharts markers in the resident journal since 09:12). The resident journal logged 'IRPT_RESIDENT_POLL retained_for_retry class=ClientError' at 09:13:27Z and 09:28:27Z. CloudTrail at both seconds: sts:AssumeRole AccessDenied for assumed-role/irpt-ycharts-runner-role/i-0167fd745ad906a66 on arn:aws:iam::313476888478:role/irpt-49f-ycharts-research-role. iam get-role irpt-49f-ycharts-research-role: NoSuchEntity. The runner role's only AssumeRole statement (AssumeTheFirmResearchPrincipal) names irpt-cot-ycharts-research-role. irpt-generation redrive: maxReceiveCount 5, visibility 900 s, so the message goes to irpt-generation-dlq at about 10:28Z, and until then the request reads QUEUED to its filer.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "CloudTrail sts AssumeRole AccessDenied 2026-10-09T09:13:27Z and 09:28:27Z",
      "resident journal via SSM 2aa69757 and 14ca8aef",
      "iam get-role NoSuchEntity irpt-49f-ycharts-research-role",
      "runner role AssumeTheFirmResearchPrincipal -> irpt-cot only"
    ]
  },
  "notes": "Not a producer defect: OPAL was chosen. The per-firm research principal is provisioned for cottonwood only, so every other firm's Opal request will fail the same way. Remedy (to the CTO for round 7): mint the research role per allowed firm through the naming builder, with its read grants, and widen the runner's AssumeRole to those roles. X1/W2 proceed when irpt-generation reads 0/0 after the DLQ move."
}
```

## IRPT_YCDGEN-D2-S20 -- st29 F1: Opal produced the 49financial report; irpt-status refuses to serve it (packaged registry lag)

```json
{
  "id": "IRPT_YCDGEN-D2-S20",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T12:05:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "one_line": "st29 F1 on 49financial: the Opal engine produced the report (0 YCharts markers), but irpt-status refuses to serve it -- RetentionRefused 'invalid retention reference', because the Lambda's packaged registry still lists the research row as firms [cottonwood]",
  "spec_asserts": "FWD-1: a non-Andrew filer's Overview is produced by the Opal engine AND served (status READY, sections readable).",
  "world_is": "MEASURED. F1 REQ-5e4149d2863aea31cc87d660 was submitted at 12:00:26Z on st29 (f0ff4f1653, research row firms=3). Resident journal: RESOLVE READY 12:00:17Z; PDF render (pypdf FontBBox warnings) 12:00:32-33Z; POLL handled=1 at 12:00:39Z; 0 YCharts markers (SSM f02d8b3e). Portal status and sections at 12:00:39Z and 12:02:18Z: UNAVAILABLE / public_reason_code UNEXPECTED. CloudWatch /aws/lambda/irpt-status at 12:02:18Z: exception_type RetentionRefused, exception_text 'invalid retention reference', operation status-job. reporting_policies.json is staged in irpt-status (and irpt-ycharts-generate) at a pin whose research row names cottonwood only; the st29 fix reached the resident package alone.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "CloudWatch irpt-status corr-a9376ea80c21 RetentionRefused",
      "resident journal SSM f02d8b3e",
      "F1_RUN_RECORD_ST29_20261009.json / F1_READBACK_ST29_20261009.json (scrubbed)"
    ]
  },
  "notes": "Remedy: the irpt-status and irpt-ycharts-generate releases must stage reporting_policies.json at >= 23e39f11d7 (the research row with 3 firms). 2.0.0_SA_COO~Y2's IRPT_ANLREQ round-2 release 1 re-pins both functions (DECOMP_R2). The produced report persists after st29's X1; a served read can be re-tried once irpt-status carries the row, by a principal allowed on 49financial."
}
```

## IRPT_YCDGEN-D2-S21 -- the served read still refused after rev3: 'invalid retention reference' is a ref-shape check, not the firms check

```json
{
  "id": "IRPT_YCDGEN-D2-S21",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T14:30:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~G2",
  "one_line": "FWD-1 served read of REQ-5e4149d2 still refused after irpt-status rev3 staged the 3-firm research row: RetentionRefused 'invalid retention reference' is raised at retention.py _key (a ref SHAPE check), not at the firms check",
  "spec_asserts": "With the research row at 3 firms in irpt-status (IRPT_ANLREQ.TO-APPLY-Y1 rev3, read 6 fix half PASS), the owner read of the Opal-produced 49financial report is served.",
  "world_is": "MEASURED. sr1 window 2: W1 14:26:06Z; the owner read 14:26:15Z; status-job and analysis-report both UNAVAILABLE/UNEXPECTED. CloudWatch /aws/lambda/irpt-status at 14:26:1xZ: corr-a80db731f80e (status-job) and corr-93ba3a8a08da (analysis-report), exception RetentionRefused 'invalid retention reference'. In reports/retention.py that text is raised at :56 (_registered: revision not a str of 1..REVISION_MAX), :114 (reference: bad policy_revision) and :126 (_key: the ref must be exactly {retention_id, policy_revision}, policy_revision a str within REVISION_MAX, retention_id matching RETENTION_ID). The firms check raises a different text ('registered enforced policy required'), so the 3-firm row is no longer the blocker. The report was written by the st29 resident package (base pin 3d705e700f + named list), whose writer of the retention ref may predate irpt-status rev3's reader: a writer/reader skew on the ref's shape or revision.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "CloudWatch irpt-status corr-a80db731f80e, corr-93ba3a8a08da",
      "reports/retention.py :56, :114, :126 at box/dell2",
      "served read record SERVED_READ_REQ_5e4149d2_20261009.json (scrubbed)"
    ]
  },
  "notes": "Outside ~G2's lane (reports/retention.py and the report writers are the backend's). Routed to 2.0.0_SA_COO~Y2 and 1.0.0_SA_CTO~DELL2 with the correlation ids. To discriminate: read the stored ref of REQ-5e41's report (its keys and policy_revision length) against _key, using a principal that can decrypt irpt-requests/irpt-jobs."
}
```

## IRPT_YCDGEN-D2-S22 -- ARMED: irpt-status rev 4 crashes on every request (split ship, unexpected kwarg)

```json
{
  "id": "IRPT_YCDGEN-D2-S22",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~G2",
  "surfaced_at": "2026-10-09T16:25:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y2",
  "one_line": "irpt-status release 1 rev 4 (live 15:43:11Z) crashes at build() for every request: TypeError build_retained_repositories() got an unexpected keyword argument 'additional_policy_revisions' -- a split ship; every status/analysis read returns HTTP 500",
  "spec_asserts": "IRPT_ANLREQ.TO-APPLY-Y1 rev 4 changes only status_installed.py (registers the writer's OPAL_RESEARCH_REVISION) and the function keeps serving.",
  "world_is": "MEASURED. sr1 window 3 owner read 16:22:43Z: GET status and GET sections both HTTP 500 {message: <str:21>}. CloudWatch /aws/lambda/irpt-status: '[ERROR] TypeError: build_retained_repositories() got an unexpected keyword argument additional_policy_revisions' at status_installed.py:137 compose_ports, served.py:1452; 52 events 16:17:17Z-16:22:48Z (filter since 15:40Z). get-function-configuration: LastModified 2026-10-09T15:43:11Z, CodeSha256 VC/r14ka... The packaged composition.py (staged at an older pin) predates the kwarg that status_installed.py now passes.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "CloudWatch irpt-status TypeError x52",
      "lambda get-function-configuration 15:43:11Z VC/r14ka",
      "SERVED_READ_W3_REQ_5e4149d2_20261009.json (scrubbed)"
    ]
  },
  "notes": "ARMED: a live outage of every irpt-status read. Disarm = rollback to rev 3 (the pair's named rollback) by the release owner 2.0.0_SA_COO~Y2 under the CTO; then re-cut rev 4 with composition.py co-staged. Escalated 16:24Z to ~Y2 and CTO~DELL2."
}
```
