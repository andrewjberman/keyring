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

## IRPT_CUSTDY-S2 -- issuer rulings at the round-1 drain: W1-S1 ruled, W2-S1 ruled, W4-S1 routed to IRPT_BCKEND

```json
{
  "id": "IRPT_CUSTDY-S2",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T08:42:00Z",
  "one_line": "Issuer rulings at the round-1 drain on IRPT_CUSTDY-W1-S1, W2-S1 and W4-S1.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "drains 737839f762 (CU-a-3), 06a44e56bd (CU-a-4), 9dd85cec00 (CU-a-1), 36c37ef88d (CU-a-2); every proof instance VALID at its branch head",
      "drain hygiene on data/assets/scripts/gold/irpt_custody/: py_compile 4/4 OK, ruff py39 'All checks passed!', pytest 36 passed, four self-tests all True"
    ]
  },
  "disposition": "GRADUATED",
  "spec_asserts": "Decomposition round 1: hop 1 reads the advisor from the IRPT_BCKEND directory (PRD S01); hop 5 renders through irpt-export-render (PRD S07); the client-report contract leaves figure rules to the cell.",
  "world_is": "W1-S1 RULED (issuer, inside its decomposition): the advisor-to-accounts source is the firm ownership map (d08_firm_ownership_map.py), joined to the directory; CU-a-1's --ownership input is accepted. The PRD's S01 text and a naming-registry row for the map's address are the CTO's (carried in the drain-end message). W2-S1 RULED: the five figure rules stated in client_report_figures.py are accepted for round 1 as written; any change is an enrichment item. W4-S1 ROUTED: the render path takes a frozen export bundle plus a portal print route and the template only by name (render_export.cjs:228), so no client-report document can be rendered through it as it stands; the request goes to IRPT_BCKEND's export lane (2.0.0_SA_COO~P2). Hop 5's real render waits on that; the layout to local HTML is built and tested."
}
```

## IRPT_CUSTDY-S3 -- the real advisor pick crashes: 482 of 7022 granted accounts refused by the custodian-key projection

```json
{
  "id": "IRPT_CUSTDY-S3",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T08:52:00Z",
  "one_line": "The issuer's real run of CU-a-1 --pick crashes on live data: 482 of 7022 distinct granted accounts in the live ownership map are refused by the custodian-key projection, and the tool raises instead of counting them as uncovered.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell2 2026-10-07 ~08:4xZ: python data/assets/scripts/gold/irpt_custody/advisor_client_list.py --pick --as-of 2026-09-30 --ownership s3://opal-data-bd/platinum/49financial/ownership_map.json -> SILVER master=08242234 date=2026-09-30 partition=present rows=103863; SILVER master=08335338 ... rows=107469; then ids.IdRefused: a raw key must be a non-empty value; got str(len=4, opaque-text) at book_of (advisor_client_list.py:226) via ids.project (infra/aws/lambda/investor-reporting/_ids/ids.py:389)",
      "census over the same map (schema_version 1, LastModified 2026-10-07T05:27:37Z, 472562 bytes): 190 advisors, 24082 grant entries, every raw value str len 11; distinct accounts 7022, projected 6540, refused 482 (all the same IdRefused), advisors with >=1 refused account 31 of 190",
      "the freshest ownership map is the opal-data-bd copy; the opal-data-portal-v2 advi copy is LastModified 2026-08-21T15:03:25Z"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Decomposition round 1, issuer act 1: CU-a-1 --pick on real data prints the census and the pick; an account that cannot be shown covered excludes its advisor (CTO ruling msg 103).",
  "world_is": "Hop 1 does not run on real data: the crosswalk maps 482 raw accounts to a value the id minter refuses, and CU-a-1 lets the refusal escape. Under the CTO's rule such an advisor is ineligible anyway, so the repair is to count a refused account as uncovered and print the count in the census. The round is frozen: this is round 2's first item. Why 482 accounts do not resolve through the custodian-key seam is not measured."
}
```

## IRPT_CUSTDY-S4 -- the firm bucket opal-data-49financial is fenced from dell2

```json
{
  "id": "IRPT_CUSTDY-S4",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T09:12:00Z",
  "one_line": "The dell2 user is explicitly denied s3:ListBucket on the firm bucket opal-data-49financial, which holds the returns gold hop 3 reads and the client_report gold and report_template state this project writes.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell2 ~09:1xZ: python org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/read_returns_gold_partition.py --master 08335338 --day 2026-09-30 -> AccessDenied ... cloudops-dell2-agent-user is not authorized to perform: s3:ListBucket on resource: arn:aws:s3:::opal-data-49financial with an explicit deny in a resource-based policy",
      "builder output: opal_naming.address('irpt', lookup('08335338')['firm'], 'gold', 'account_return_daily', 'date=2026-09-30') = s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/date=2026-09-30"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Decomposition round 1 constraint 5 and the issuer's acts: hop 3 reads the returns gold and --apply writes client_report gold and the report_template state under the firm's address.",
  "world_is": "Every read and write of this project under the firm bucket is fenced from dell2. Per 1.0.0_SA_CTO~DELL2's standing rule (msg 213) the read goes to the laptop as the committed script above; the fence is never widened from dell2. Round 2 builds on fixtures; every real read or write under the firm bucket is a laptop act until NFRA_CTLPLN round 4."
}
```

## IRPT_CUSTDY-S5 -- E3 held: no portal node_modules on dell2

```json
{
  "id": "IRPT_CUSTDY-S5",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T09:12:30Z",
  "one_line": "Round-2 item E3 (the ClientReportDocument template in portal/src/pages/InvestorReporting/render/) cannot be built or checked on dell2: the portal has no node_modules here and installing them is npm egress.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell2 ~09:1xZ: portal HEAD 8ddfe409 = origin/DEV; `ls portal/node_modules` -> absent; portal/package.json typecheck = 'tsc -b --noEmit'; no *.test.* under portal/src/pages/InvestorReporting/render/",
      "1.0.0_SA_CTO round-1 analysis @822468e309 section 3 E3 criterion (3): the page lane's typecheck and the template's test pass; NFRA_CTLPLN v0.14 C-KIT-PYTHON: no Dell installs from PyPI (the kit carries python packages from the laptop)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Round-2 ENRICHMENT LIST E3, cut in round 2's one issuance on dell2.",
  "world_is": "E3 is held out of round 2's issuance on dell2 (the issuer's ruling, recorded in the round-2 decomposition): its build and both its checks need the portal toolchain. It is cut when the bring-up kit carries portal node_modules to dell2, or on the CTO's placement of the cell on the laptop."
}
```

## IRPT_CUSTDY-W6-S1 -- the order's per-figure `source` object collides with the contract's fees.source label

```json
{
  "id": "IRPT_CUSTDY-W6-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~6",
  "surfaced_at": "2026-10-07T09:22:21Z",
  "one_line": "CU-b-3 asks every figure to carry source {table, partition, rows}, but the round-1 contract already gives fees a `source` that is the string SCHWAB_TXN_FEE_ROWS; the worker moved the label into fees.source.label.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.md:81 fees: {amount, source: SCHWAB_TXN_FEE_ROWS, is_billed_fee: UNKNOWN}",
      "data/assets/scripts/gold/irpt_custody/client_report_figures.py (this worker's branch wk-IRPT_CUSTDY-6) FEES_KEYS keeps order amount, source, is_billed_fee; source is now a dict carrying label",
      "grep of the worktree for SCHWAB_TXN_FEE_ROWS and client_report_figures: no code consumer outside the module and its tests (the issuer's template join is not yet built)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CU-b-3 build item 2: every figure carries `source`: {table, partition, rows}. The round-1 contract: fees.source is the label SCHWAB_TXN_FEE_ROWS.",
  "world_is": "Both cannot hold on the fees figure. Reading taken: the order's later, explicit rule wins and the contract's label is kept as fees.source.label; the round-1 fees test is edited for exactly that. Also taken where the order is silent: market_value, each holding row and each activity row carry a source (rows 1 for a single row); the returns partition is `date=<d>` or `date=<first>..date=<last>`; an as-of whose quarter opens before 2024-01-01 is refused rather than computed. The issuer or CTO may overrule: the label move is one dict key in build_documents."
}
```

## IRPT_CUSTDY-W5-S1 -- the refused 'None' is a stringified null in IRPT_BCKEND's bundled seam file

```json
{
  "id": "IRPT_CUSTDY-W5-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~5",
  "surfaced_at": "2026-10-07T09:20:43Z",
  "one_line": "The 'None' that the id projection refuses is a stringified null in IRPT_BCKEND's bundled custodian_key_seam.json (826 index values, 482 of 7022 live granted accounts refused); ids.py:387-388 guards `is not None` and lets the string through. The issuer routes the fix to IRPT_BCKEND.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell2 ~2026-10-07T09:20:43Z: python data/assets/scripts/gold/irpt_custody/none_source.py --ownership s3://opal-data-bd/platinum/49financial/ownership_map.json -> NONE-SOURCE file=infra/aws/lambda/investor-reporting/_ids/data/custodian_key_seam.json:48 owner=IRPT_BCKEND refused=482 distinct=7022 via_none=482 (the first of the 482 refused accounts; every one of the 482 has a seam index value equal to the string 'None')",
      "infra/aws/lambda/investor-reporting/_ids/data/custodian_key_seam.json @e27b2bce34: index has 6202 entries, all str; 826 are 'None', 0 are JSON null; its _written_by is '0.9.0_WK_IRPT_BCKEND~1 / IRPT_BCKEND.TO-IB-rte-6' (git: 47f21dab95)",
      "s3://opal-data-assets/blackdiamond/49f/silver/dim_account_xref/date=2026-09-16/data.parquet (the file's named source), read-only: 6202 rows, schwab_account_id isna()=826, equal to the string 'None'=0 -- so the stringification happened when the seam file was written (the writing script is not in the repo; the commit adds only the artifact)",
      "infra/aws/lambda/investor-reporting/_ids/ids.py:387-389 @e27b2bce34: `mapped = idx.get(str(raw).strip())` / `if mapped is not None: return base(\"account\", mapped)` -- the guard passes the string 'None' to the mint, which raises IdRefused (_check_raw)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Round-1 analysis E1 and decomposition constraint 1: the advisor pick runs on the live ownership map; the projection resolves a granted account or refuses it by a reason the tool can name.",
  "world_is": "482 of 7022 distinct granted accounts (31 of 190 advisors) are refused by the projection because the bundled seam file maps their custodian key to the string 'None' (the cross-reference has no Schwab id for them: 826 null rows of 6202). CU-b-1 counts them as UNCOVERED / PROJECTION_REFUSED and no longer raises; those advisors stay ineligible. The durable fix is in IRPT_BCKEND's files (omit null-mapped keys from the seam artifact, and guard the string in projection_with_seam so the account is returned raw and graded UNPROJECTED-ID rather than refused); CU-b-1 edits neither."
}
```

## IRPT_CUSTDY-S6 -- S4's FILE landed: returns gold present for 2026-09-30 (6854 accounts); figures need a second laptop FILE

```json
{
  "id": "IRPT_CUSTDY-S6",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T09:56:00Z",
  "one_line": "S4's laptop FILE landed: the 2026-09-30 returns-gold partition is present with 6854 rows and 6854 distinct accounts, but the FILE carries presence only, not figures, so round-3 E2 is graded from a second laptop-run FILE that holds the figures.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_CUSTDY/IRPT_CUSTDY_returns_gold_20260930.json @ef5ea44568 (laptop 3.0.0_SA_CVO; relayed by 0.0.0_AB_MSTR~DELL2 msg 286): uri s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/date=2026-09-30, read_at 2026-10-07T09:30:48Z, objects 2 (data.parquet rows 6854, 19 columns, account_column account_id; manifest.json), distinct_accounts 6854, error null",
      "the probe (read_returns_gold_partition.py @b97c663aa9) reads counts and column names only, by design"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Round-2 analysis @10e64fe9df gate 'S4 FILE lands' -> E2: hop 3 on the real returns, graded from the FILE (QTD, YTD, 1Y at 2026-09-30; SI held; each figure names its rows).",
  "world_is": "The gate opened, and the returns data hop 3 needs exists for the as-of. The figures themselves must be computed where the firm bucket is readable: E2 is cut as a read-only wrapper the laptop runs (the standing rule, msg 213), writing the chosen advisor's client-report documents to a FILE that is then graded. S4 stays open until that FILE lands."
}
```

## IRPT_CUSTDY-W7-S1 -- the order's masking test ('no run of 8 or more digits in the file') cannot hold on a client-report document

```json
{
  "id": "IRPT_CUSTDY-W7-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~7",
  "surfaced_at": "2026-10-07T10:06:54Z",
  "one_line": "the order's masking test ('no run of 8 or more digits in the file') cannot hold on a client-report document; the worker tests for an unmasked ACCOUNT number instead",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "whole-file 8-digit-run search on the fixture output: float fractions, master 08335338, _20260811 match (0 account numbers)",
      "data/assets/scripts/gold/irpt_custody/hop3_real_run.py unmasked_runs (branch wk-IRPT_CUSTDY-7)",
      "data/assets/scripts/gold/irpt_custody/client_report_figures.py lineage and classification_vintage fields"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order CU-c-1 item 6: 'no unmasked account (no run of 8 or more digits in the file)'.",
  "world_is": "The order's file-level test (no run of 8+ digits) fires on three things the documents must carry: every float figure (a fraction such as 0.0660583070761045), the Schwab master number in lineage.schwab_partitions (08335338, 8 digits), and the dated classification_vintage filename (..._20260811.json). So CU8-AC1's masking test is written on the account number it is for: unmasked_runs() walks the strings and integers, skips a float's fraction, a registry master and a _<digits> filename token, and fails on any other 8+ digit run; the tests also assert no fixture raw account string appears. This narrows the literal wording and the worker records it rather than weakening silently."
}
```

## IRPT_CUSTDY-W7-S2 -- on dell2 the wrapper reads the ownership map and the directory, and is denied only at the firm bucket's silver

```json
{
  "id": "IRPT_CUSTDY-W7-S2",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~7",
  "surfaced_at": "2026-10-07T10:06:54Z",
  "one_line": "on dell2 the wrapper reads the ownership map and the directory, and is denied only at the firm bucket's silver/returns read; the largest advisor's book shows 308 NOT_IN_DIRECTORY and 114 PROJECTION_REFUSED accounts before any figure is built",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell2 run 2026-10-07T10:0xZ, wrapper at branch wk-IRPT_CUSTDY-7, summary line HOP3-REAL-RUN ... uncovered=422 error=AccessDenied",
      "error text: explicit deny in a resource-based policy on s3:ListBucket opal-data-49financial for the dell2 agent user"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order CU-c-1: on dell2 the wrapper records the AccessDenied in the file and exits nonzero.",
  "world_is": "The order says the wrapper records AccessDenied on dell2. Measured: the real CLI run on dell2 for the advisor with the most granted accounts completed the ownership-map read (opal-data-bd) and the directory read, resolved the book, and was denied (explicit deny in a resource-based policy, s3:ListBucket on opal-data-49financial) at the coverage read, so the file carries error=AccessDenied and 422 uncovered accounts (308 NOT_IN_DIRECTORY, 114 PROJECTION_REFUSED), 0 households."
}
```

## IRPT_CUSTDY-S7 -- drain red: the none_source test fails after IRPT_BCKEND's seam fix changed ids.py

```json
{
  "id": "IRPT_CUSTDY-S7",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T10:24:00Z",
  "one_line": "Drain red at 1312dbea80: test_none_source_names_the_seam_line (round 2, CU-b-1) fails at HEAD because IRPT_BCKEND's seam fix @b43f82c155 made ids.py return the raw account for a 'None' mapping, so none_source.py's fixture no longer produces a refusal to trace.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell2 ~10:2xZ, HEAD 1312dbea80: python -m pytest -q data/assets/scripts/gold/irpt_custody/tests -> 1 failed, 64 passed, 1 xfailed; FAILED tests/test_advisor_projection_refused.py::test_none_source_names_the_seam_line at line 114 (assert last.endswith(':%d owner=FOO_BAR refused=1 distinct=4 via_none=1'))",
      "IRPT_BCKEND drain @b43f82c155 (2.0.0_SA_COO~P2 msg 299): ids.py ~388 returns the raw account for an empty, 'None' or 'nan' mapping; the test passed at its own drain 1c925383a4, before that change"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Round 2 CU-b-1: none_source.py names where the 'None' value is made; its fixture test prints NONE-SOURCE file=... via_none=1.",
  "world_is": "The 'None' source is fixed upstream, so the tracer's fixture premise no longer holds against HEAD's ids.py. The tool did its job (W5-S1 -> E-P8). Next round's repair batch: retire none_source.py or re-point its test at a fixture projection that still refuses; this round does not re-cut it."
}
```

## IRPT_CUSTDY-S8 -- E2 graded from the real hop-3 run on dell2: QTD/YTD/1Y OK, sources 124/124, SI NO_DATA (no anchor), 4 not in directory

```json
{
  "id": "IRPT_CUSTDY-S8",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T10:50:00Z",
  "one_line": "E2 graded on dell2 from the real hop-3 run (the fence on opal-data-49financial lifted ~10:44Z): 10 households, 14 accounts; QTD/YTD/1Y OK on 14/14 accounts; every figure names its source; but SI is NO_DATA everywhere (no inception anchor), and 4 granted accounts are NOT_IN_DIRECTORY.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell2 ~10:46Z, HEAD after f4ccdbf04e: python data/assets/scripts/gold/irpt_custody/hop3_real_run.py --advisor matthew_gooch --as-of 2026-09-30 --out <scratchpad file, not committed: real client figures> -> HOP3-REAL-RUN advisor=matthew_gooch as_of=2026-09-30 households=10 accounts=14 uncovered=4 held_si=0 error=none, rc 0, 666158 bytes",
      "graded from that file: accounts QTD OK 14/14, YTD OK 14/14, 1Y OK 14/14, SI NO_DATA 14/14; households QTD OK 10/10, YTD OK 10/10, 1Y OK 7 NO_DATA 3, SI NO_DATA 10/10; figures with a source {table, partition, rows}: 124/124; uncovered 4, all NOT_IN_DIRECTORY; numbers of 8+ digits other than the two masters: 19 distinct, 0 matching any ownership-map account",
      "1.0.0_SA_CTO~DELL2 msg 358 / 0.0.0_AB_MSTR~DELL2 msg 367: cloudops-dell2-agent-user reads opal-data-49financial gold from ~10:44Z; relay 346 withdrawn by this seat"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Round-2 analysis E2 (round 1's E4 criteria): QTD, YTD, 1Y at 2026-09-30 computed; SI held under HOLD A where inception is before 2024; each figure names its rows.",
  "world_is": "Criteria 1 and 3 hold on real data (household 1Y is NO_DATA in place for 3 of 10, the households carrying an uncovered account). Criterion 2 is vacuous: no SI is held because no SI anchor resolves (inception column absent from the accounts the wrapper builds; gold manifest first_data_date not used) -- with HOLD A lifted for 2010-2027 this is now the SI gap, a next-round item beside moving the hold floor to 2010. S4 and S6 close on this run: the fenced read is no longer fenced and the figures FILE exists on dell2."
}
```

## IRPT_CUSTDY-W10-S1 -- CU-d-2 on real data: the 4 NOT_IN_DIRECTORY accounts have no Schwab key; 0 documents move

```json
{
  "id": "IRPT_CUSTDY-W10-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~10",
  "surfaced_at": "2026-10-07T11:10:00Z",
  "one_line": "CU-d-2 on real data: the 4 NOT_IN_DIRECTORY accounts of matthew_gooch are not in the custodian key seam, so none can be built; they move from reason NOT_IN_DIRECTORY to NO_SCHWAB_KEY and 0 documents move from uncovered to reported.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell2 ~11:08Z, branch wk-IRPT_CUSTDY-10 after the CU-d-2 edit: python data/assets/scripts/gold/irpt_custody/check_directory_gap.py --advisor matthew_gooch --as-of 2026-09-30 -> UNCOVERED NO_SCHWAB_KEY=4 / DIRECTORY-GAP advisor=matthew_gooch granted=18 not_in_directory=4 reported=14 all_reported=True, rc 0",
      "read-only probe through hop3_real_run.real_inputs() (no figures printed): of the advisor's 18 granted ownership-map accounts, 14 are in the custodian_key_seam index (5376 entries) and resolve to a Schwab key; the 4 not in the directory (masked ****9851, ****0041, ****7341, ****9421) are not in the seam index and schwab_key() returns None for each; none of the advisor's 12 map relationships is an acct:<id> singleton, so the OWNERSHIP_MAP name rule would have had no key for them either",
      "the same 14 accounts and 10 households as round 3 (row IRPT_CUSTDY-S8: households=10 accounts=14 uncovered=4); the wrapper's gap rule is exercised on fixtures only (tests/test_hop3_directory_gap.py), where an account with Schwab data and no directory entry gets a document named OWNERSHIP_MAP or ACCOUNT_ONLY"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CU-d-2 cell text and the CTO ruling: an account NOT_IN_DIRECTORY still gets its report, named from the ownership map; 'those 4 got no report' is the gap to close; CU11-AC2 reports the counts (all_reported=True).",
  "world_is": "On the chosen advisor the gap is not a directory gap alone: the 4 accounts have no Schwab key at all (absent from the custodian key seam, so no silver or returns gold can be read for them), so no report can be built whatever the directory holds. They stay uncovered, now under NO_SCHWAB_KEY, still counted (not_in_directory=4 of=18). all_reported=True holds because no granted account WITH Schwab data lacks a document. Whether these 4 accounts exist at Schwab under another key (a seam coverage gap) is not measured here and is the open question for the next cut."
}
```

## IRPT_CUSTDY-W9-S1 -- the Schwab silver has no dim_account; the custodian's account open date is fact_acc.date_opened

```json
{
  "id": "IRPT_CUSTDY-W9-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~9",
  "surfaced_at": "2026-10-07T11:18:02Z",
  "one_line": "the order names Schwab silver dim_account for rule 1's custodian date; the silver has no such table, the account record is fact_acc and its open date is the column date_opened",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell2 2026-10-07 ~10:5xZ: client_report_figures.py --coverage --master 08335338 --master 08242234 --as-of 2026-09-30 -> 20 and 19 silver tables, no dim_account; fact_acc present, 566 partitions to 2026-10-06",
      "fact_acc at date=2026-10-06 (master 08335338): 7601 rows, columns include date_opened (0 nulls in the 7601), date_of_birth, account_status; date_opened sample values are ISO dates"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order CU-d-1 THE CELL: Schwab silver `dim_account` under opal-data-assets/schwab/<master>/silver/ (look for an open/inception date column -- that is rule 1's custodian date when present).",
  "world_is": "No dim_account table. Rule 1's custodian date is read from fact_acc.date_opened at the --as-of partition (client_report_figures.custodian_open_dates), after the accounts file's 4th column. The same table is the one a01_runner.py and a06_dim_identity_crosswalk.py already read as the account universe."
}
```

## IRPT_CUSTDY-W9-S2 -- on the real run the custodian's open date wins rule 1 for 14 of 14 accounts and SI is still NO_DATA on all 14 (the linker finds no return that early)

```json
{
  "id": "IRPT_CUSTDY-W9-S2",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~9",
  "surfaced_at": "2026-10-07T11:18:03Z",
  "one_line": "matthew_gooch at 2026-09-30: all 14 accounts resolve a rule-1 anchor from fact_acc.date_opened, and all 14 SI figures are still NO_DATA, because the linker needs a return at or before the window's first day and the gold has none that early",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell2 ~11:1xZ: python data/assets/scripts/gold/irpt_custody/si_anchor_probe.py --accounts-from-advisor matthew_gooch --as-of 2026-09-30 -> SI-ANCHOR advisor=matthew_gooch accounts=14 rule1=14 rule2=0 rule3=0 no_anchor=0 labels_ok=True; every ACCOUNT line shows si_status=NO_DATA",
      "linker outcome on each of the 14 SI cells (parity_period_returns.link_account_period, read with a spy on ppr.link, nothing committed): UNAVAILABLE-NO-COVERAGE 14 of 14. 2 anchors (2022-03-29, 2022-04-29) are before the returns gold's first partition 2024-07-08; for the other 12, with the linker's base value supplied as Opal's own prior-day value (0.0 on each), the account's first linkable return is 3,3,3,5,6,13,26,29,47,54,121,348 days after the window's first day (an account is opened, then funded later)",
      "client_report_figures.py base_value() and the bd_bmvs it passes are this cell's own change: without them the linker took the anchor branch (base value unknown) and the window opened on the anchor itself; for a rule-2 anchor (first_data_dates() = the first positive-value day, whose own return is null) the first linkable return is the next day, so the base value must be supplied or a rule-2 SI could never compute (inferred, no rule-2 account in this advisor's book to measure)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order CU-d-1: SI is computed (status OK) for a rule-1 or rule-2 anchor on or after 2010-01-01; E1 of the round-3 analysis (SI NO_DATA on every account because no anchor resolved).",
  "world_is": "The anchor now resolves for 14 of 14, so the first half of E1 is closed, but the SI figure is not: the CTO's order (custodian date first) puts every one of this advisor's accounts on a date earlier than the gold can link from, so SI stays NO_DATA, in place and labelled, never zero. Not weakened and not worked around here: moving the window to the first funded day would call a data-start date `since inception`, which the ruling forbids. The rule-2 path computes on fixtures (test_si_anchor.py) but no account of this advisor reaches it. The question for the issuer/CTO is whether rule 1 should yield to rule 2 when the custodian date is earlier than the gold's first linkable return."
}
```

## IRPT_CUSTDY-W9-S3 -- retiring the 2024 floor turns two hop3 tests and the hop3 self-test red; hop3_real_run.py and test_hop3_real_run.py are outside this order's paths

```json
{
  "id": "IRPT_CUSTDY-W9-S3",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~9",
  "surfaced_at": "2026-10-07T11:18:04Z",
  "one_line": "with HELD_CALENDAR_FIX retired, hop3_real_run's fixture (a 2019 first data date, expected held) now gives SI NO_DATA, so test_hop3_real_run.py::test_file_shape and ::test_si_held_for_a_pre_2024_inception fail and `hop3_real_run.py --self-test` prints held_ok=False",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~K2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "worktree wk-IRPT_CUSTDY-9, python -m pytest -q data/assets/scripts/gold/irpt_custody/tests -> 3 failed, 87 passed, 1 xfailed; the 3: test_advisor_projection_refused.py::test_none_source_names_the_seam_line (already row IRPT_CUSTDY-S7), test_hop3_real_run.py::test_file_shape (held_si=1 expected, held_si=0 got), test_hop3_real_run.py::test_si_held_for_a_pre_2024_inception (NO_DATA, expected the held status)",
      "python data/assets/scripts/gold/irpt_custody/hop3_real_run.py --self-test -> HOP3-REAL-RUN-SELFTEST file_ok=True masked_ok=True held_ok=False error_written_ok=True",
      "hop3_real_run.py lines 226 (HELD_FIRST_DATA = 2019-03-15), 178 (_count_held reads crf.STATUS_HELD), 323-326 (held_ok); client_report_figures.py keeps STATUS_HELD as an alias of NOT_AVAILABLE only so these still import"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order CU-d-1: update round 2's tests (test_client_report_figures.py, test_client_report_held_si.py) only where the retired floor or the new field requires; they must pass.",
  "world_is": "Those two files now pass (39 with test_si_anchor.py). Two more tests and one self-test, in files this order cannot write, assert the retired hold on a 2019 date, and 2019 is on the calendar now. They need HELD_FIRST_DATA moved before 2010 (rule 3 -> NOT_AVAILABLE) and the held_si count and status checks re-pointed at NOT_AVAILABLE. ARMED because the drain's test run goes red on them until a cell that owns hop3_real_run.py makes that edit."
}
```

## IRPT_CUSTDY-W9-S4 -- AC3 cannot read green inside this order's paths: two CU-d-2 tests in tests/test_hop3_directory_gap.py assert 'today's documents carry no si_anchor', which CU-d-1 itself makes false

```json
{
  "id": "IRPT_CUSTDY-W9-S4",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~9",
  "surfaced_at": "2026-10-07T11:48:03Z",
  "one_line": "CU10-AC3 reads SUITE passed=108 failed=2: tests/test_hop3_directory_gap.py::test_account_line_prints_name_source_and_absent_anchor_without_failing and ::test_a_present_si_anchor_prints_its_date_and_rule expect si_anchor=ABSENT on every account line, and every account document now carries si_anchor, so the file is outside this order's <paths> and the two tests cannot be fixed here",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~K2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "worktree wk-IRPT_CUSTDY-9 after merging CLOUD and implementing amendments 1 and 2: python data/assets/scripts/gold/irpt_custody/tests/run_suite_check.py -> SUITE dir=data/assets/scripts/gold/irpt_custody/tests passed=108 failed=2 errors=0 skipped=0 xfailed=1 (rc=1)",
      "the 2: test_hop3_directory_gap.py line 83 (`assert \"ACCOUNT ****3333 name_source=OWNERSHIP_MAP si_anchor=ABSENT\" in acct_lines`, the comment on the next line reads 'today's documents carry no si_anchor') and line 97 (the stubbed third account is built from a real document whose accounts now all carry si_anchor, so printed[2] reads si_anchor=<date> rule=<n>, not ABSENT)",
      "hop3_real_run.py _si_anchor_text (lines 228-234) prints ABSENT only when the document lacks the field; client_report_figures.build_documents has written `si_anchor` on every account since CU-d-1's first pass (e25f6f33ab)",
      "with the field present the ABSENT assertions are false by construction; the fix is to the two tests (build the absent case by deleting the field from a copy of a document, as the second test already stubs the present case), which belong to a cell whose grant includes test_hop3_directory_gap.py"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order CU-d-1 amendment 1: after merging CLOUD the whole irpt_custody suite reads 0 failed and 0 errors (CU10-AC3); the grant names hop3_real_run.py and tests/test_hop3_real_run.py but not tests/test_hop3_directory_gap.py.",
  "world_is": "CU10-AC3 is not met as written: failed=2, both in a file this order cannot write (CU-d-2 landed them expecting the field absent until CU-d-1 landed). Per the refusal clause the tests are not weakened, skipped or edited. ARMED because the drain's suite run goes red on them once this branch merges. Disarm: add tests/test_hop3_directory_gap.py to this order's paths (or to a successor order) so the two ABSENT assertions can be re-expressed as 'absent only when the document lacks the field'; everything else in CU10-AC1 and CU10-AC2 holds."
}
```

## IRPT_CUSTDY-W9-S5 -- amendment 2 branch (c) as written ('holdings exist before Opal's first partition') cannot be read literally; implemented as 'holdings exist, or the zero read is unconfirmed, between the open date and the first funded day'; the real probe takes 153 s

```json
{
  "id": "IRPT_CUSTDY-W9-S5",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~9",
  "surfaced_at": "2026-10-07T11:48:03Z",
  "one_line": "amendment 2 (c) says 'holdings exist before Opal's first partition' but nothing before Opal's first partition can be read; branch c is implemented as holdings present (or the zero read unconfirmed) on the silver positions days from the open date up to the first funded day, and the real probe run measured 153 s wall time",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "task order file @09f7e2ab87, AMENDMENT 2 bullets (b) 'the open date precedes Opal's first partition' and (c) 'holdings exist before Opal's first partition' -- (b) and (c) cannot both describe an open date before the first partition, and holdings before it are unreadable",
      "client_report_figures.resolve_si_anchor_branch / _holdings_before_first: Opal's first partition = the master's earliest silver positions partition; (a) needs open >= that, first funded >= open, a positions partition for EVERY trading day in [open, first), and zero non-zero-quantity/value rows for the account on them; any holding, any missing trading-day partition, or an unreadable partition -> (c) (rule 2); an open date before the first partition, or an unknown first partition -> (b)",
      "dell2 ~11:4xZ: python data/assets/scripts/gold/irpt_custody/si_anchor_probe.py --accounts-from-advisor matthew_gooch --as-of 2026-09-30 -> rc=0, wall 2m33s (153 s), SI-ANCHOR advisor=matthew_gooch accounts=14 rule1=12 rule2=2 rule3=0 no_anchor=0 branch_a=12 branch_b=2 branch_c=0 branch_rule2=0 branch_rule3=0 branch_none=0 labels_ok=True (12 a, 2 b: as the order expected)",
      "the 153 s is above the 120 s bound the worker standard names for a criterion run; the cost is the positions-partition reads for the 12 branch-a accounts (one read per trading day between open and first funding, cached per master/day)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Amendment 2: branch (c) 'holdings exist before Opal's first partition' -> rule 2 as (b); CU10-AC2 runs the probe on dell2.",
  "world_is": "(c) is read as the only measurable thing: holdings on the days between opening and first funding (or an unconfirmable read). On real data no account lands in (c), so the reading changes no reported figure; the CTO or issuer should confirm or restate it. The probe's wall time is 153 s, so a timeout 120 wrapper would record rc=124; the criterion was run under timeout 600 and its output is recorded in the proof."
}
```

## IRPT_CUSTDY-S9 -- round 4 drained: SI OK 14/14 on the real run; W9-S3 and W9-S4 disarmed; suite 110/0

```json
{
  "id": "IRPT_CUSTDY-S9",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T12:10:00Z",
  "one_line": "Round 4 drained and graded on the real run: SI is OK on 14/14 accounts and 10/10 households (12 under branch (a) 'since inception (first funded <date>)', 2 under rule 2); W9-S3 and W9-S4 disarmed by CU-d-1 amendments 1 and 3; the suite reads 110 passed, 0 failed on CLOUD.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "drains: e05799d167 (CU-d-3), 7361085932 (CU-d-2), 208a3ceedf (CU-d-1, amendments 1 @2063cabae7, 1b @ce710b5144, 2 @09f7e2ab87, 3 @021117b977)",
      "dell2 ~12:0xZ on HEAD 208a3ceedf: tests/run_suite_check.py -> SUITE ... passed=110 failed=0 errors=0 skipped=0 xfailed=1; py_compile 10/10; ruff clean",
      "dell2 ~12:0xZ: hop3_real_run.py --advisor matthew_gooch --as-of 2026-09-30 -> HOP3-REAL-RUN ... households=10 accounts=14 uncovered=4 held_si=0 not_in_directory=4 of=18 error=none; from its file (not committed: client figures): SI OK accounts 14/14, households 10/10; si_anchor rule 1 OK 12, rule 2 OK 2; labels 'since inception (first funded' 12, 'first date Opal holds' 2; uncovered NO_SCHWAB_KEY 4"
    ]
  },
  "disposition": "GRADUATED",
  "spec_asserts": "Round-3 analysis @ec25e39844 E1-E3 and the CTO's W9-S2 ruling (msg 423); rows W9-S3 and W9-S4 ARMED with disarm_owner 2.0.0_SA_COO~K2.",
  "world_is": "E1: every account prints its anchor and rule, SI computes for every rule-1/rule-2 anchor on or after 2010 with the ruled labels, and a test fails on a rule-2 'inception' label. E2: the advisor's 4 NOT_IN_DIRECTORY accounts are counted with their denominator (4 of 18) but cannot be reported: they have no custodian key, so no Schwab data (W10-S1). E3: suite green on CLOUD. W9-S3 is disarmed by amendment 1 (hop3 tests re-expressed) and W9-S4 by amendment 3 (directory-gap tests re-expressed); both were seams between round-4 cells, not defects."
}
```

## IRPT_CUSTDY-W13-S1 -- CU-e-1 on real data: all 4 unkeyed accounts of matthew_gooch classify NOT_HELD (found=0, not_held=4); no seam-

```json
{
  "id": "IRPT_CUSTDY-W13-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~13",
  "surfaced_at": "2026-10-07T12:47:19Z",
  "one_line": "CU-e-1 on real data: all 4 unkeyed accounts of matthew_gooch classify NOT_HELD (found=0, not_held=4); no seam-cell candidate exists, because Schwab silver holds none of them under any identifier.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell2 12:47Z on branch wk-IRPT_CUSTDY-13: python data/assets/scripts/gold/irpt_custody/unkeyed_lookup.py --advisor matthew_gooch --as-of 2026-09-30 -> UNKEYED-LOOKUP advisor=matthew_gooch accounts=4 found=0 not_held=4 classified=4, rc 0; 39 silver surfaces (19 + 20 tables of masters 08242234 and 08335338, partition 2026-09-30 or the latest before it), 8 identifiers per account (raw key, digits, no-leading-zeros, pad8-12, opaque id, seam key and seam values, census row), 0 matches",
      "census cause for each of ****9851, ****0041, ****7341, ****9421: BD_KEY_ABSENT_FROM_EVERY_BRIDGE_SOURCE in IRPT_BCKEND's IB64-1_directory_coverage.json (key in none of dim_account_xref 53 partitions, dim_advisor_fee_role 53 partitions, fact_bd_allocation@2026-08-18, fact_taxsma_report@2026-07-17)",
      "positive control: a real silver account_id from 08335338.fact_acc prefixed with z and fed to lookup_account classed FOUND_UNDER_OTHER_KEY, naming the silver columns that hold it (so a NOT_HELD is a search that could find)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CU-e-1: each of the 4 accounts is classed FOUND_UNDER_OTHER_KEY (a seam-cell candidate for IRPT_BCKEND) or NOT_HELD; the split is reported, not graded.",
  "world_is": "The split is 0 found / 4 not held. The seam holds none of the 4 and Schwab silver (both masters, every table's key columns at 2026-09-30) holds none, so no seam row can fix them: these 4 accounts have no Schwab record on dell2's reachable silver at the as-of. Search scope stated: the as-of partition per table (or the latest before it), key columns account_id, mstracct_number, custdian_id and the unlabelled col_1..col_6 of fact_fam and fact_slm; an earlier-partition holding of a since-closed account would not be seen."
}
```

## IRPT_CUSTDY-W13-S2 -- A NOT_HELD gap account has no directory household, so its not_covered account document sits in a household doc

```json
{
  "id": "IRPT_CUSTDY-W13-S2",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~13",
  "surfaced_at": "2026-10-07T12:47:19Z",
  "one_line": "A NOT_HELD gap account has no directory household, so its not_covered account document sits in a household document of its own that carries no household_returns or lineage; the document is added in run(), not build_file().",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/irpt_custody/client_report_figures.py validate_document @CLOUD 9ca7469fc3 requires ACCOUNT_KEYS (returns, market_value, holdings, activity, fees, si_anchor) on every account and TOP_KEYS (household_returns, lineage) on every document; that file is outside this order's paths, so a not_covered account cannot be a validate_document-conforming document",
      "data/assets/scripts/gold/irpt_custody/si_anchor_probe.py reads acct['si_anchor'] and acct['returns']['SI'] on every account build_file returns; check_directory_gap.py counts reported + uncovered == granted, so a NOT_HELD account is counted once, in the data and not in uncovered (tests/test_unkeyed_lookup.py test_a_not_held_account_is_in_the_report_data_as_not_covered_with_its_reason_and_no_figures asserts it is not in uncovered)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CU-e-1 item 2: a NOT_HELD account renders in its client's report DATA (the account document, under its household) as \"not_covered\": {\"reason\": ...} with no figures.",
  "world_is": "A gap account's household is its own singleton (ownership-map or account-only name), so its household document holds that one account document {account, not_covered}. hop3_real_run.run() appends these documents after build_file() (so si_anchor_probe, which iterates build_file's documents, is unaffected) and the summary line gains not_covered=<n> only when n>0. A consumer that iterates every account of the file expecting returns (a portal render of the file) must skip an account carrying not_covered; none exists in this repo's irpt_custody tree."
}
```

## IRPT_CUSTDY-S10 -- drain red: the none_source tracer test fails again after IRPT_BCKEND made the seam guard case-insensitive

```json
{
  "id": "IRPT_CUSTDY-S10",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T12:58:00Z",
  "one_line": "Drain red on CLOUD after 5b85219599: test_none_source_names_the_seam_line fails again because IRPT_BCKEND IB-pr-348 (11ba48fdc7) made the seam guard case-insensitive, so the round-4 re-pointed fixture value 'none' no longer refuses; no refusing spelling remains to re-point onto.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell2 ~12:5xZ on HEAD 5b85219599: tests/run_suite_check.py -> SUITE ... passed=125 failed=1 errors=0; FAILED tests/test_advisor_projection_refused.py::test_none_source_names_the_seam_line (line 117)",
      "git log infra/aws/lambda/investor-reporting/_ids/ids.py: 11ba48fdc7 0.9.0_WK_IRPT_BCKEND~149 fix(IRPT_BCKEND IB-pr-348): seam guard treats every spelling of none/nan/null as unmapped (after CU-d-3's re-point @e05799d167)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Round 4 E3 (CU-d-3): the irpt_custody suite reads 0 failed on CLOUD; the tracer fixture re-pointed to a value the fixed ids.py still refuses.",
  "world_is": "The upstream guard now covers every null-like spelling, which is what the tracer was built to find; the tracer test has nothing left to provoke. Repair for the next round's batch: retire the refusal-tracing test (keep none_source.py as a historical tool) -- re-pointing again is not possible."
}
```

## IRPT_CUSTDY-W12-S1 -- hop3_real_run.py for the real render's input takes longer than the 120 s criterion bound on dell2 (rc=124 twice, then rc=0 under a 1500 s bound)

```json
{
  "id": "IRPT_CUSTDY-W12-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~12",
  "surfaced_at": "2026-10-07T12:49:47Z",
  "one_line": "hop3_real_run.py for the real render's input takes longer than the 120 s criterion bound on dell2 (rc=124 twice, then rc=0 under a 1500 s bound)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell2, worktree wk-IRPT_CUSTDY-12: `timeout 120 python data/assets/scripts/gold/irpt_custody/hop3_real_run.py --advisor matthew_gooch --as-of 2026-09-30 --out .scratch/hop3.json` -> rc=124, no file written; the same again -> rc=124",
      "faulthandler dump at 40 s: the process is inside botocore ListObjectsV2 via client_report_figures.py:308 read <- :710 _holdings_before_first <- :754 resolve_account_anchors <- :861 build_documents (the CU-d-1 anchor probe; ownership map and directory reads had already succeeded, so dell2 is NOT denied)",
      "same command run detached under timeout 1500 -> `HOP3-REAL-RUN advisor=matthew_gooch as_of=2026-09-30 households=10 accounts=14 uncovered=4 held_si=0 not_in_directory=4 of=18 error=none`, rc=0; the file (kept under .scratch/, uncommitted) was then rendered by CU15-AC2",
      "row IRPT_CUSTDY-W9-S5 measured the same probe at 153 s"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order's AC2 text says to run hop3_real_run.py first and names no bound; the worker rule bounds every criterion invocation at 120 s with one retry.",
  "world_is": "The prerequisite run exceeds 120 s on this device (it reads S3 partitions one by one). I retried it once under the 120 s bound as the rule says, then ran it a third time detached under 1500 s because AC2 cannot exist without its file; the AC2 invocation itself (the bun render) ran under timeout 120 and passed. The issuer should state a longer bound for this prerequisite in any order that names it."
}
```

## IRPT_CUSTDY-W12-S2 -- the order's input shape lists `name_source` on each account, but client_report_figures.py's ACCOUNT_KEYS (and the real hop3 documents) do not carry it

```json
{
  "id": "IRPT_CUSTDY-W12-S2",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~12",
  "surfaced_at": "2026-10-07T12:49:47Z",
  "one_line": "the order's input shape lists `name_source` on each account, but client_report_figures.py's ACCOUNT_KEYS (and the real hop3 documents) do not carry it",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "client_report_figures.py ACCOUNT_KEYS = [account, registration, returns, market_value, holdings, activity, fees, si_anchor]; validate_document refuses any other key set (line 957-958)",
      "hop3_real_run.py FILE_KEYS carries `name_sources` ({masked account: source}) at the FILE level, not per account",
      "portal types.ts types `name_source?` as optional on the account; the fixture carries it per the order face; the renderer never reads it"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order CU-e-2 worker face: accounts: {account, registration, name_source, returns, si_anchor, market_value, holdings, activity, fees}.",
  "world_is": "A real document has no per-account name_source, so any consumer that requires it would refuse every real document. The template does not use it and types it optional; whoever wires the client-report kind (IRPT_BCKEND) should read name_sources from the run file or drop the field from the contract text."
}
```

## IRPT_CUSTDY-S11 -- round 5 drained: 18 of 18 accounts in the report data (14 SI OK, 4 not covered); template rendered a real household

```json
{
  "id": "IRPT_CUSTDY-S11",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T13:10:00Z",
  "one_line": "Round 5 drained and graded on the real run: all 18 granted accounts of the chosen advisor are in the report data -- 14 covered with SI OK, 4 not covered with the reason NOT_HELD; the 49F template rendered a real household; the portal candidate passed CTO review with one note.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "drains: 5b85219599 (CU-e-1), 8029bc6635 (CU-e-2 workspace side); portal 99addd80 on wk-IRPT_CUSTDY-12-portal",
      "dell2 ~13:0xZ on HEAD f16e89faa9+: hop3_real_run.py --advisor matthew_gooch --as-of 2026-09-30 -> HOP3-REAL-RUN ... households=10 accounts=14 uncovered=0 held_si=0 not_in_directory=4 of=18 not_covered=4 error=none; from its file (not committed): 18 account documents, 14 with SI OK, 4 with not_covered reason 'NOT_HELD: no Schwab record under any identifier of this account'",
      "CU-e-1 real: UNKEYED-LOOKUP advisor=matthew_gooch accounts=4 found=0 not_held=4 classified=4 (39 silver tables, 8 identifiers, positive control fired); CU-e-2 real: REAL-RENDER households=1 accounts=2 periods=4 si_labels=2 not_ok_noted=30 bd_field_names=0",
      "1.0.0_SA_CTO~DELL2 msg 581: review of 99addd80 PASS; note -- the template renders no not_covered account yet; DEV landing waits on Andrew (106221)"
    ]
  },
  "disposition": "GRADUATED",
  "spec_asserts": "Round-4 analysis @16d9b128c0 E1 (each unkeyed account measured, classed, not-covered rendered in the data) and E2 (the 49F template on a real client; C-SHAPE; typecheck, eslint and test).",
  "world_is": "E1 holds on real data. E2 holds for its mechanical criteria (C-SHAPE is the CVO's judgment). Carried to the next round, not rows: the template's not_covered rendering (CTO note), the tracer test retirement (S10), and the 30 'not described' holdings in the real render (class and sector null until the issuer's describe() join)."
}
```

## IRPT_CUSTDY-W14-S1 -- the order asks for a not-covered account added to render/fixtures/clientreport.firm-a.json, but the existing client-report-document test is coupled to that fixture and cannot pass with it; the not-covered document is built inline in the new test instead

```json
{
  "id": "IRPT_CUSTDY-W14-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~14",
  "surfaced_at": "2026-10-07T13:39:52Z",
  "one_line": "the order asks for a not-covered account added to render/fixtures/clientreport.firm-a.json, but the existing client-report-document test is coupled to that fixture and cannot pass with it; the not-covered document is built inline in the new test instead",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "measured in worktree: appending {account: ****9999, not_covered: {reason}} to the fixture's accounts and running `bun --no-install test .../client-report-document.test.tsx` gave 10 of 10 tests failing (a mixed household with one not-covered account crashes the covered render path); the fixture was restored byte-for-byte from a backup before any commit",
      "client-report-document.test.tsx asserts `1 + FIXTURE.accounts.length` returns tables (a), the exact three SI-row list (b) and the literal `5 / 5` page counter (i); a third account that prints no returns table and its own page cannot satisfy those even if the mixed render were supported (reasoned from the assertions, not run)",
      "the producer never emits a mixed household: validate_document admits a not-covered account only in a household whose accounts are ALL not-covered, so a mixed fixture is also not a shape the contract produces",
      "portal e355d193 on wk-IRPT_CUSTDY-14-portal: ClientReportDocument branches on isNotCoveredReport; not-covered.test.tsx holds the synthetic not-covered household inline (6 pass); the existing test file is unchanged (16 pass over the clientreport directory)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order CU-f-1 build step 4: add one not-covered account to render/fixtures/clientreport.firm-a.json (synthetic); the existing test must still pass.",
  "world_is": "The two clauses cannot both hold: the fixture is one covered household that the existing test counts account by account, and the order's paths do not include that test. The fixture file is unchanged. If the CTO wants the not-covered account in a fixture FILE, it is a second fixture (a separate not-covered household document) read by the new test, which needs that path in a later order's grant."
}
```

## IRPT_CUSTDY-W14-S2 -- data/assets/scripts/gold/irpt_custody/tests/test_advisor_projection_refused.py::test_none_source_names_the_seam_line fails on the CLOUD checkout independent of this order

```json
{
  "id": "IRPT_CUSTDY-W14-S2",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~14",
  "surfaced_at": "2026-10-07T13:39:52Z",
  "one_line": "data/assets/scripts/gold/irpt_custody/tests/test_advisor_projection_refused.py::test_none_source_names_the_seam_line fails on the CLOUD checkout independent of this order",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "`python -m pytest -q data/assets/scripts/gold/irpt_custody/tests` in the worktree at fed55f91cc plus CU-f-1: 138 passed, 1 failed, 1 xfailed; the one failure is test_advisor_projection_refused.py:117 (assert False)",
      "the same single test run from C:/dev/ajb_workspace (the CLOUD checkout without my changes): `-k none_source_names` -> 1 failed, 5 deselected, same line 117, so the failure predates CU-f-1; the file is outside this order's paths and was not touched"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Repo-wide hygiene runs at the drain (round 6 order CU-f-1): the irpt_custody suite is expected green.",
  "world_is": "One test in a neighbouring file is red on base; it is not caused by validate_document or hop3_real_run. Whoever owns advisor_client_list / its seam message should read it."
}
```

## IRPT_CUSTDY-W14-S3 -- CU-f-3: the SI probe cost was a sequential per-day read of silver positions, not a listing a manifest can replace; no manifest holds silver holdings, so the probe now reads the needed days once, concurrently, row-filtered in arrow

```json
{
  "id": "IRPT_CUSTDY-W14-S3",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~14",
  "surfaced_at": "2026-10-07T14:29:19Z",
  "one_line": "CU-f-3: the SI probe cost was a sequential per-day read of silver positions, not a listing a manifest can replace; no manifest holds silver holdings, so the probe now reads the needed days once, concurrently, row-filtered in arrow",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "baseline on dell2 (hop3_timed_check, before any change): HOP3-TIMED advisor=matthew_gooch seconds=148.2 within_120=False households=10 accounts=14 si_ok=14 si_labels_rule1=12 si_labels_rule2=2",
      "per-call timing of S3Store reads in that run: 851 reads, of which 309 are silver dim_position day reads (84 s, sequential, 0.27 s each = day-prefix list 0.05 + get 0.15 + pandas decode 0.13) from _holdings_before_first, 434 are account_return_daily reads (threaded, ~10 s wall), 65 fact_trn reads; the day-prefix list inside S3Store.read (the faulthandler site, ~line 308) is one narrowed list per day, 0.05 s, not the cost",
      "the returns gold manifest at 2026-09-30 carries table, asof, rows, day_quality_census, return_basis_census, carried_days, first_data_date (6863 accounts), method, thresholds, address, landed -- no field about silver holdings, so the zero-holdings read cannot come from it",
      "more workers alone did not help (60 days: 4 workers 11.6 s, 16 workers 13.9 s, 32 workers 13.1 s) because the pandas conversion of ~83k rows per day dominates; the fix cuts each day to the probe accounts in pyarrow (is_in over the distinct ids) before to_pandas",
      "after: HOP3-TIMED advisor=matthew_gooch seconds=62.2 within_120=True households=10 accounts=14 si_ok=14 si_labels_rule1=12 si_labels_rule2=2; the prefetch phase measured 6.9 s in an instrumented run (total 68.2 s, of which unkeyed_lookup.build_context 29.6 s and the returns load 14.1 s are outside this order's paths)",
      "data/assets/scripts/gold/irpt_custody/client_report_figures.py: _prefetch_probe_days, _account_filter, _probe_span; S3Store/LocalStore.read take an optional `keep`; tests/test_si_anchor_bounded.py 9 passed; full irpt_custody tests 147 passed, 1 xfailed, 1 failed (the inherited test_none_source_names_the_seam_line, W14-S2)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order CU-f-3 / ruling W12-S1: the time is in the SI anchor probe's S3 listing; the probe should read a manifest or a narrowed prefix instead of listing S3.",
  "world_is": "The listing is already narrowed per day and costs 0.05 s; the time is 309 sequential day reads (list + get + pandas decode) of silver positions, and no manifest holds that data. The probe now reads the union of the [open, first funded) days once with 16 workers and cuts each day to its accounts in arrow, which is the 'narrowed read' the ruling asks for in effect. Two costs outside this order's paths remain in the 62 s: unkeyed_lookup.build_context (~25-30 s, hop3_real_run's not-covered lookup) and the returns load (~14-22 s). Run-to-run time moves with the network (the unchanged code measured 148, 133 and 194 s on dell2; the final code 62.2 and 68.2 s)."
}
```

## IRPT_CUSTDY-S12 -- round 6 drained: hop 3 inside 120 s with SI labels unchanged; not-covered accounts validated and rendered, each in its own household; suite 0 failed

```json
{
  "id": "IRPT_CUSTDY-S12",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T14:58:00Z",
  "one_line": "Round 6 drained and graded on the real run: hop 3 for the chosen advisor runs inside 120 s with SI labels unchanged; not-covered accounts validate with their reason, each in its own household; the tracer test is retired and the suite reads 0 failed on CLOUD.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "drains: 0143c19ac1 (chain B, CU-f-2), 65511fc814 (chain A, CU-f-1 + CU-f-3; tree check 10 needed, 0 dropped, 0 foreign); portal e355d193 on wk-IRPT_CUSTDY-14-portal (not on DEV)",
      "proofs VALID: CU-f-1 (CU16-AC1, CU16-AC2), CU-f-3 (CU17-AC1, CU17-AC2), CU-f-2 (CU18-AC1)",
      "issuer real run dell2 ~14:35Z: HOP3-TIMED advisor=matthew_gooch seconds=85.9 within_120=True households=10 accounts=14 si_ok=14 si_labels_rule1=12 si_labels_rule2=2 (worker before 148.2 s; after 62.2 s, 68.2 s)",
      "issuer real run dell2 ~14:37Z: HOP3-REAL-RUN ... households=10 accounts=14 not_in_directory=4 of=18 not_covered=4 error=none; from its file (scratchpad, not committed): 14 household documents, 14 distinct household ids, 4 not-covered accounts each alone in its document with a non-empty reason, validate_document admits 14 of 14",
      "CLOUD @65511fc814: SUITE passed=147 failed=0 errors=0 skipped=0 xfailed=1; py_compile OK; hop3_real_run --self-test all ok"
    ]
  },
  "disposition": "GRADUATED",
  "spec_asserts": "Round-5 analysis @f6160117ce E1 (not-covered end to end: validate admits with reason, template renders it, never under another household), E2 (tracer retired, suite 0 failed), E3 (hop 3 within 120 s, SI labels unchanged).",
  "world_is": "E1, E2 and E3 hold on real data and on CLOUD. Issuer rulings on the worker rows: W14-S1 ACCEPTED (the not-covered portal test builds its synthetic document inline because the existing test is coupled to the shared fixture; the criterion is met). W14-S2 RESOLVED by CU-f-2's retirement at 0143c19ac1 (CLOUD suite 0 failed). W14-S3 ACCEPTED (the premise -- a listing, a manifest as the fix -- did not hold; the bound is met by a one-pass concurrent arrow-filtered read; labels unchanged). FWD-1 thread still NOT LIVE: hop 5's served render waits on IRPT_BCKEND and the template's DEV landing (Andrew)."
}
```

## IRPT_CUSTDY-S13 -- an empty accounts array reads as covered and renders a 3-page shell (CTO note on 4c10b488, non-blocking)

```json
{
  "id": "IRPT_CUSTDY-S13",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T15:26:00Z",
  "one_line": "An empty accounts array reads as covered in the client-report template and renders a 3-page shell; the producer never writes one today (CTO review note on portal 4c10b488, non-blocking).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "1.0.0_SA_CTO~DELL2 msg 759: PASS on 4c10b488 (with e355d193); note: 'an empty accounts array reads as covered and renders a 3-page shell. The producer never writes one today.'",
      "hop3_real_run real output 2026-10-07 ~14:37Z: 14 household documents, none with an empty accounts array"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The template renders a household's accounts: covered ones with figures, not-covered ones with their reason; a mixed document is refused by name (round 7 E1).",
  "world_is": "A household document with zero accounts is neither refused nor marked: it takes the covered path and renders an empty 3-page shell. Inert today because hop3_real_run never emits one; carried to the round-7 analysis as a candidate refusal alongside the mixed-document error."
}
```

## IRPT_CUSTDY-S14 -- round 7 E2 cannot reach READY as cut: five breaks on hop 5 (no custody writer, accept KeyError, as_of_date, print page refuses custody-report, render host reads PROD)

```json
{
  "id": "IRPT_CUSTDY-S14",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T17:30:00Z",
  "one_line": "Round 7 E2 (hop 5 served) cannot reach READY as cut: no route writes a CUSTODY_REPORT to the retained store, the export's accept step reads report.dates.actual_end (absent on a custody document), the export wants as_of_date while hop 3 writes as_of, and the print page refuses custody-report -- and the render host loads the PROD portal, so a DEV landing alone does not reach it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "issuer read at HEAD: infra/aws/lambda/investor-reporting/export/submit_async.py:137 `business_date = resolved[\"report\"][\"dates\"][\"actual_end\"]` on the non-platinum branch (last change b66691eb1b); test_submit_custody_report.py calls serve_submit directly and never passes accept",
      "issuer read at HEAD: export/narrative_submit.py custody_report_as_of requires `as_of_date`; data/assets/scripts/gold/irpt_custody/client_report_figures.py documents carry `as_of`",
      "issuer read at HEAD: portal/src/pages/InvestorReporting/render/PrintEntry.tsx:102-104 -- readReportKind refuses ?kind=custody-report by name (IB-pr-336 note); ClientReportDocument is on wk-IRPT_CUSTDY-14-portal @4c10b488 only",
      "Explore read (local, not live AWS): reports/repository.py:135 ReportRepository.persist has callers for PERFORMANCE and ANALYSIS only; docs/contracts/investor-reporting/v1/routes.json has no custody write route",
      "Explore read: render host opens https://opalinvest.dev/investor-reporting/print (export/main.tf:95); portal deploy.yml runs on PROD pushes only, DEV->PROD is promote-to-prod.yml",
      "Explore read: IRPT_BCKEND round-68 drain row S382 -- no authenticated Opal principal exists to drive a new export to READY"
    ]
  },
  "disposition": "DECOMP_INVALIDATING",
  "spec_asserts": "Round-6 analysis @881e552c2e section 1: 'the server half of hop 5 is served' (IB-pr-349 carries IB-pr-336); E2 = one CUSTODY_REPORT export per household requested through the real API, each reaching READY, after E1 lands on portal DEV.",
  "world_is": "The Lambda is deployed, but the journey breaks at five points before READY: (1) no writer puts a custody document into the retained store; (2) accept KeyErrors on report.dates.actual_end; (3) as_of vs as_of_date; (4) PrintEntry refuses custody-report and does not mount ClientReportDocument; (5) the render host prints from the PROD portal, so DEV is not enough. (1), (2), (4) and the principal are IRPT_BCKEND's surface; (3) is IRPT_CUSTDY's (a one-key adapter). E2 is not cut; routed to 1.0.0_SA_CTO~DELL2 for a ruling."
}
```

## IRPT_CUSTDY-S15 -- break 3 closed: the custody document carries as_of_date; the export's own reader accepts 14 of 14 real documents

```json
{
  "id": "IRPT_CUSTDY-S15",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T18:10:00Z",
  "one_line": "Break 3 of S14 closed: the custody household document carries as_of_date, the export's own custody_report_as_of accepts every real document, and the old key is refused by both consumers.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "drain d488869311 (CU-g-4, 9 paths, 0 dropped); proof VALID (CU19-AC1 6 passed, CU19-AC2 4 pass 0 fail); portal 6d84304d on wk-IRPT_CUSTDY-16-portal (on 4c10b488, not on DEV)",
      "issuer re-run in the worktree: clientreport bun directory 24 pass 0 fail across 4 files; tsc -b --noEmit rc 0",
      "CLOUD @d488869311: SUITE passed=153 failed=0 errors=0 xfailed=1; hop3_real_run --self-test all ok",
      "issuer real run dell2 ~18:0xZ: HOP3-REAL-RUN advisor=matthew_gooch as_of=2026-09-30 households=10 accounts=14 not_covered=4 error=none; from its file (scratchpad, not committed): 14 documents, export narrative_submit.custody_report_as_of returns 2026-09-30 for 14 of 14, old key present on 0, validate_document admits 14 of 14"
    ]
  },
  "disposition": "GRADUATED",
  "spec_asserts": "CTO round-6 ADDENDUM 1 @c3addc6f25 Ruling 1: the custody document carries as_of_date as the export contract names it; no consumer reads two names.",
  "world_is": "Holds on real data and against the export's own function. The template refuses an as_of-only document by name (MissingAsOfDateError), the validator likewise. Breaks 1, 2, 4 (IRPT_BCKEND P-c1..c3) and 5 (PROD promote) remain; P-c3 should mount ClientReportDocument from 6d84304d's tree, since 4c10b488 (on DEV) still reads as_of."
}
```

## IRPT_CUSTDY-W17-S1 -- the input PDF's charts are raster images with no text layer, so a chart's series cannot be extracted; they were read from the rendering

```json
{
  "id": "IRPT_CUSTDY-W17-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~17",
  "surfaced_at": "2026-10-08T23:01:00Z",
  "one_line": "The input PDF's charts are raster images with no text layer, so a chart's series cannot be extracted; they were read from the rendering.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "PyMuPDF page.get_image_info on the input's overview and accounts-summary pages: each chart region is one raster image; page.get_text returns no legend, axis or series text inside it",
      "data/assets/scripts/gold/irpt_custody/bd_field_map.py (wk-IRPT_CUSTDY-17 on aa5dbdf463): lists each chart as one field; the map's chart-series rows carry bd_source_basis read-from-rendering (2 of 70 rows)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CU-g-3a step 1: the extractor enumerates every figure-bearing field of each base, 'a column header, a labelled figure, a chart series'.",
  "world_is": "A chart series is not machine-readable in this PDF. The extractor stops at the chart (one field each); the series rows (portfolio line, benchmark lines, ending value line, net additions line, class shares, per-holding segments) were read from the rendered page by the worker, so they carry the weakest evidence basis in the map."
}
```

## IRPT_CUSTDY-W17-S2 -- the portal submodule is empty in the worker worktree; ClientReportDocument.tsx was read from the main checkout

```json
{
  "id": "IRPT_CUSTDY-W17-S2",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~17",
  "surfaced_at": "2026-10-08T23:01:00Z",
  "one_line": "The portal submodule is empty in the worker worktree; ClientReportDocument.tsx was read from the main checkout.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ls of C:/tmp/wk-irpt-custdy-17/portal: empty; comp-find --name 'ClientReportDocument*' over the worktree: 0 hits across 65565 files",
      "C:/dev/ajb_workspace/portal at git HEAD dbeb6764: src/pages/InvestorReporting/render/clientreport/ClientReportDocument.tsx and types.ts exist; types.ts carries as_of_date and the not-covered types, so it is the CU-g-4 vintage"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CU-g-3a: compare the layout with ClientReportDocument.tsx (read only); the worker's whole context is the worktree.",
  "world_is": "The worktree carries no portal checkout, so the template was read from the main checkout's portal at dbeb6764 (read only, never edited). The comparison in LAYOUT_BASELINE_CU-g-3.md is against that file."
}
```

## IRPT_CUSTDY-W17-S3 -- the screenshot is the Run Report dialog, not a template page, so the layout baseline comes from the PDF alone and one Run Report basis (Portfolio) is exercised

```json
{
  "id": "IRPT_CUSTDY-W17-S3",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~17",
  "surfaced_at": "2026-10-08T23:01:00Z",
  "one_line": "The screenshot is the Run Report dialog, not a template page, so the layout baseline comes from the PDF alone and one Run Report basis (Portfolio) is exercised.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "the screenshot in Downloads (read in place): the dialog titled Run Report with a Portfolio / Relationship radio, Portfolio selector, Date Range, As of Date and Advanced Settings; no report page is shown",
      "the PDF's page headers: the entity label on pages 2 to 4 is the portfolio, then each account; no relationship-level page exists"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CU-g-3a: 'Compare it (the layout baseline) with the PNG' and Andrew's word 'slice the Performance client statement on Black Diamond's Run Report bases'; the PNG is 'the template as Andrew sees it'.",
  "world_is": "The PNG shows the dialog that produces the report, so there is nothing to compare page-for-page. The worker read 'bases' as the report's six titled sections (the order's own definition, plus the cover) and mapped the dialog's nine controls separately (10 rows, counted apart). If Andrew meant the dialog's Portfolio / Relationship BASIS, this input exercises Portfolio only; a Relationship-basis report would add a level above the portfolio pages."
}
```

## IRPT_CUSTDY-W17-S4 -- the Write tool turns a typed backslash-u escape into the real character, so two new .py files arrived with non-ASCII bytes and CRLF line endings

```json
{
  "id": "IRPT_CUSTDY-W17-S4",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~17",
  "surfaced_at": "2026-10-08T23:01:00Z",
  "one_line": "The Write tool turns a typed backslash-u escape into the real character, so two new .py files arrived with non-ASCII bytes and CRLF line endings.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "byte scan of bd_field_map.py and bd_leak_check.py right after the Write calls: non-ASCII bytes in both (at least 10 in the first and 6 in the second: superscripts, dashes, a right single quote) and CRLF endings; after the worker's rewrite to escape text: 0 non-ASCII bytes in both",
      "CLAUDE.md section 4: no non-ASCII in production code"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Writing a Python file with the Write tool, with a unicode escape sequence typed in the source text, yields an ASCII file that carries the escape.",
  "world_is": "The tool decodes the escape before writing, so the file holds the character itself. A worker who needs a non-ASCII constant in a .py file must write chr() or build the escape with chr(92) after the write, and byte-scan the file before commit."
}
```

## IRPT_CUSTDY-W18-S1 -- the live generate function has no custody submission path: CUSTODY_FACTORY_REQUIRED on every non-prospect body

```json
{
  "id": "IRPT_CUSTDY-W18-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~18",
  "surfaced_at": "2026-10-09T01:46:00Z",
  "one_line": "The live irpt-ycharts-generate (release 5, CodeSha256 4HEH1aDN) refuses every non-prospect submission with CUSTODY_FACTORY_REQUIRED: no live path creates a retained custody submission, so CU-g-5 cannot start and no AWS write was made.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "live read, 2026-10-09 ~01:4xZ: aws lambda get-function irpt-ycharts-generate -> CodeSha256 4HEH1aDNa39+vwLFK24SldMOBit/hiBKF4aQjlsU1zk=, Handler generate_installed.lambda_handler, LastModified 2026-10-09T01:34:40Z; the code zip downloaded and read (100 members)",
      "live zip generate_installed.py, class RoutedSubmissionService.submit: 'input_id' in payload -> prospect branch, else 'raise CustodyFactoryRequired(\"CUSTODY_FACTORY_REQUIRED\")' (1 raise site); the docstring says 'the custody branch, which still refuses CustodyFactoryRequired'",
      "live zip: custody_submission.py is a member and carries additional_policy_revisions (1 site, the E11 edit of TO-IB-yr-691), but 0 other zip members import custody_submission; generate_installed.py has 0 occurrences of additional_policy_revisions, so its repositories() (the one the handler uses) requests no irpt-custody-x10-v1 revision either",
      "repo box/dell2 3fbfac4179: custody_submission / build_accepted_custody_entry referenced only by ycharts/generate/tests and export/tests/test_custody_writer_composed.py; AcceptedCustodyReader / AcceptedCustodyNormalizer have no runtime installer (intake/custody_portfolio.py, _scope/accepted_custody.py are read by tests and by generate_installed's docstring only)",
      "docs/contracts/investor-reporting/v1/routes.json @3fbfac4179: the only submission route is POST /api/scoped/investor-reporting/analysis (irpt-ycharts-generate); the persist route POST .../custody-report needs a retained REQUEST_COMPOSITION custody artifact (custody_persist.py _check_request: schema irpt-analysis-composition.v1, lane CUSTODY, owner schema custody-owner-v1)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CU-g-2a and decomp addendum 2: 'irpt-ycharts-generate release 5 (E11) LIVE: submissions request irpt-custody-x10-v1'; 'Find how a submission is created and retained in the live stack'; the gate state measured by the issuer says the submission path is live.",
  "world_is": "Release 5 is live, but E11 edited custody_submission.py, a module the deployed handler never installs. The live handler routes a body without input_id to CustodyFactoryRequired, a named NOT_READY refusal, and its own retained repositories request no custody revision. So there is no product path that retains a custody submission, and the persist route has nothing to be pointed at (its retained_request must be a custody-owner-v1 / CUSTODY-lane composition). Nothing was written to AWS: not the submission (the path is a known refusal, so the call was not made) and not the persist. Also unread: how an Opal-operator bearer for the CUSTOM authorizer is obtained; the after-reads cited in the order (IB90-1, p90_cells) read AWS control-plane state and send no authenticated scoped request, and the render-token pattern (auth_p2_foreign_token_probe.py) mints a render principal, not an Opal operator. What would unblock: IRPT_BCKEND wires a custody service into generate_installed (an accepted-custody reader, build_accepted_custody_entry, the custody revision on its repositories) and releases it, and names the operator-credential route for a scoped POST. Criteria CU21-AC1 and CU21-AC2 cannot be met as written; CU21-AC3 (offline) was not built, to avoid a verifier for a path that does not exist."
}
```
