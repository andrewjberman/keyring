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
