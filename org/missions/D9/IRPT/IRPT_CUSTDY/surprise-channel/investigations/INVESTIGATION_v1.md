# IRPT_CUSTDY -- surprise channel, INVESTIGATION v1 (dell2 placement)

**Opened by:** `2.0.0_SA_COO~K2` at the round-1 issuance. **Home:** the project tree's channel; the gate `.tools/surprise-row-gate.py`
validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`). Lane `ANY`. A seat's row is
`IRPT_CUSTDY-S<k>`; a worker's is `IRPT_CUSTDY-W<n>-S<k>`. **Append-only during the round.** Never edit an existing row.

## IRPT_CUSTDY-S1 -- the render path's input is a portal export request; whether it renders a client-report document is unmeasured

```json
{
  "id": "IRPT_CUSTDY-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T08:12:00Z",
  "one_line": "The PRD's S07 marks the render on irpt-export-render as held, but that path renders portal pages through a minted token, and whether it can render a client-report document is unmeasured.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_CUSTDY/prd/IRPT_CUSTDY_PRD.md v0.2 @c2bc15f427 section 6 row S07: claim 'held', verb 'wire'",
      "infra/aws/terraform/investor-reporting/export/b2_render.tf lines 1-17 at dell2 HEAD: submit-export mints a render token into SSM /irpt/render-token/<ATT-id> and dispatches a render host that renders the read functions' render ports",
      "aws lambda get-function irpt-export-render, 2026-10-07 ~07:5xZ: Active, LastModified 2026-10-06T01:35:28Z"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.2 S07: the render on the IRPT_BCKEND export path is held; round 1 wires the template to it.",
  "world_is": "The path exists and is live, but its input is a portal export request, not a document. Cell CU-a-4 reads the path's input contract from source and reports accepts_document; a gap is routed by the issuer to IRPT_BCKEND's COO at the drain, never written into IRPT_BCKEND's paths."
}
```

## IRPT_CUSTDY-W4-S1 -- the render path takes a portal export request and a bundle by key, not a client-report document or a template body

```json
{
  "id": "IRPT_CUSTDY-W4-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~4",
  "surfaced_at": "2026-10-07T08:22:22Z",
  "one_line": "The irpt-export-render path cannot take a client-report document or a template body as it stands (accepts_document=False); the issuer routes the gap to IRPT_BCKEND's COO at the drain.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/investor-reporting-export/render_export.cjs:228-252 @3d0ecacb0b: the host's inputs are IRPT_BUCKET, IRPT_BUNDLE_KEY (a frozen bundle read back from S3 by key), IRPT_OUTPUT_KEY, IRPT_EXPORT_ID, IRPT_ATTEMPT_ID, IRPT_PRINT_ROUTE, IRPT_PORTAL_ORIGIN, IRPT_TEMPLATE (a NAME, default 'performance-landscape-letter', used only to pick kind analysis|performance at :240); the render is page.goto(print route + renderToken) then page.pdf() at :204 and :220",
      "infra/aws/terraform/investor-reporting/export/b2_render.tf:1-17 @3d0ecacb0b and infra/aws/lambda/investor-reporting/_render_identity/carriage.py:21-44: submit-export mints the render token into SSM /irpt/render-token/<ATT-id>; the command document carries only that name",
      "portal/src/pages/InvestorReporting/fixtures/wire/requests/submit-export.request.json (main tree, read only): the request body keys are authorized_report_revisions (report_id/revision/authorization_ref), selected_sections (ids), narrative_packet_ref, approved_assets, versions (template_version 't-2' is an opaque string), render_options, live_vendor_request_during_render; no key carries a document, a document address or a template body",
      "python data/assets/scripts/gold/irpt_custody/report_render_request.py --render-path -> accepts_document=False evidence=infra/aws/ec2/investor-reporting-export/render_export.cjs:228"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.2 S07 / decomp item 4: the render on the IRPT_BCKEND export path is held and round 1 lays the template into it; CU-a-4 reports whether a client-report document can be rendered through it as it stands.",
  "world_is": "It cannot, as it stands. Missing, exactly: (1) a submit-export request field, or a bundle member, by which a client-report document (or its S3 address under the firm's own prefix) reaches the bundle freeze; (2) a render-host input that carries a template body or the template's address (IRPT_TEMPLATE and versions.template_version are names, not content); (3) a print-route page that lays a client-report document out by a data template (the host only opens the portal's own print route; the portal print page was not read here, as the worktree has no portal checkout, so whether it can is UNMEASURED). The local HTML from report_render_request.py is the look; the real render through irpt-export-render waits on these three. Nothing in IRPT_BCKEND's paths was changed."
}
```

## IRPT_CUSTDY-W1-S1 -- the directory entry carries no advisor field; CU-a-1 reads the advisor from the ownership map

```json
{
  "id": "IRPT_CUSTDY-W1-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~1",
  "surfaced_at": "2026-10-07T08:25:00Z",
  "one_line": "The directory entry carries no advisor field, so the PRD's S01 claim (advisor list from the directory) fails as written; the advisor-to-accounts map is the separate ownership map, which CU-a-1 consumes instead.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/investor_reporting/directory_runner.py:450-516 @30f94c3ab1: _entry emits ids (firm/client/account/relationship), display_name, masks, permitted_scope, termination, access, revision and cohort with hierarchy_path []; no advisor or rep key; build_49f (531-641) reads dim_account and dim_relationship and joins no rep column",
      "infra/aws/lambda/investor-reporting/_scope/resolve.py:347-376 @30f94c3ab1: advisor_grant reads ownership['advisors'][advisor_id]['accounts'|'relationships'] -- the advisor lives in the ownership map, projected into the directory id space by _ids.projection_for_firm",
      "data/assets/scripts/gold/runners_49f/d08_firm_ownership_map.py:1-40 @30f94c3ab1: the producer of platinum/<firm>/ownership_map.json (schema_version 1, advisors keyed by slug); its docstring declares the SERVED map carries the Black Diamond z-id grammar, which _ids/data/custodian_key_seam.json projects (IRPT_BCKEND-W1-S22)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CU-a-1 and PRD v0.2 S01: the advisor and household live in a directory entry; the list is read from the directory (held, brief F1).",
  "world_is": "A DirectoryEntry holds households (RELATIONSHIP or ACCOUNT entries) and opaque account ids but no advisor. CU-a-1 therefore joins the firm's ownership map (--ownership, REQUIRED: the map's address is not in the naming registry so no default is typed; the edge validator reads it from the firm's platinum/ area) to the directory through _ids.projection_for_firm; nothing was invented. Unmeasured here: that the live 49 Financial map's z-id grants all resolve through the seam to directory accounts (the list prints directory_missing=<n> and the census prints it per advisor) and the live key and bucket of the map; the issuer's first real run measures both. Also an interpretation to confirm: an advisor with ANY uncovered account is excluded whole (the order's test 5), not merely that household."
}
```

## IRPT_CUSTDY-W2-S1 -- CU-a-2 chose one reading of five open figure rules

```json
{
  "id": "IRPT_CUSTDY-W2-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~2",
  "surfaced_at": "2026-10-07T08:29:35Z",
  "one_line": "The client-report contract leaves five figure rules open; CU-a-2 chose one reading of each and states it in the module docstring.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/irpt_custody/client_report_figures.py module docstring, THE RULES THIS BUILD STATES (this worker's branch wk-IRPT_CUSTDY-2)",
      "data/assets/scripts/gold/runners_49f/parity_period_returns.py:link -- SI with no anchor returns UNAVAILABLE-NO-ANCHOR, a window that is undefined",
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py:247 COLUMNS -- the gold carries total_return_daily and market_value_eod, not the linker's r_net/r_gross"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Decomposition contract: statuses OK|NO_DATA|WINDOW_NOT_RULED; household_returns by the same linking; account 'last 4 only in any printed output'; fees = Schwab fee rows labelled SCHWAB_TXN_FEE_ROWS; SI window per the linker.",
  "world_is": "Readings taken where the contract is silent. (1) SI with no inception anchor maps to WINDOW_NOT_RULED (window null), every other UNAVAILABLE-* to NO_DATA; SI anchor = accounts-file inception, else the gold manifest first_data_date. (2) The gold's total_return_daily feeds the linker as r_net and r_gross (it is gross of advisory fees). (3) A household return links a daily series weighted by prior-day market_value_eod and is OK only when every member account is OK. (4) The document's account field carries the last 4 only, not just the printed lines. (5) Fee amount is the signed sum of fee-class rows (a charge is negative) and is null when a QTD trading day has no fact_trn partition. The issuer or CTO may overrule any of the five; each is one function in the module.",
  "notes": "Real-neighbour read: --coverage on masters 08335338 and 08242234 at as_of 2026-09-30 both read_ok=True, as_of_covered=True (latest 2026-10-05). The worker ran no --apply and wrote no S3 object."
}
```
