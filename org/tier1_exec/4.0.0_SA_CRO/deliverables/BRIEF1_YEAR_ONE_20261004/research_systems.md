# Systems timeline and infrastructure growth -- research for the management brief

Prepared for 4.0.0_SA_CRO~2026, 2026-10-04. The research was read-only. Repos read: the workspace on branch CLOUD (55,609 commits, first commit 2025-11-18) and the portal submodule (3,561 commits on all branches, first commit 2025-11-12).

How each date was set: dates are git author dates (YYYY-MM-DD). **MEASURED** means a command printed the value. **INFERRED** means the value comes from a commit subject or record prose, not from a served artifact. **ABSENT** means no evidence was found. Each value carries a commit hash or a deploy-ledger file name. Ledger files are in `org/critical_paths/change_management/`.

## 1. Systems

```json
{"systems": [
 {"system": "News scanner / News Intelligence",
  "plain_description": "Reads hundreds of financial news articles a day, scores sentiment and trending topics, and feeds the News Intelligence panel on the portal.",
  "first_code_date": "2025-11-18", "first_code_commit": "38057ad7e9 (repo import: tools/news_scanner + infra/aws/lambda/news_scanner); the code is older than the repo -- its README says 'Last Updated 2025-11-13, Phase 1-2 Operational', and a session log dated 2025-11-17 is included",
  "live_date": "2025-11-22", "live_evidence": "07b2ef9367 '[news_scanner] ... production verification'; portal 64ed071e 2025-11-18 'Add News Intelligence Dashboard'. v2 'semantic news' pipeline: Layer-4 Portal Publisher Lambda deployed 2026-02-17 (23fc59424d); the whole pipeline moved under Terraform as news-v1.0.0 on 2026-02-20 (7bd902849f); news-v2.9.x shipped in May 2026; ledger news-scanner-semantics-20260916 CLOSED (8f9e6eec30)",
  "claim": "first_code MEASURED (the true origin is earlier: INFERRED); live INFERRED (commit subject)",
  "notes": "This is the only system that predates the repo. It was rebuilt as a multi-layer pipeline in Feb 2026 (news_semantic_clustering 2026-02-12, layer3 curation 2026-02-13/20, Seeking Alpha scrapers 2026-02-17/19)."},
 {"system": "Client/advisor portal (opalinvest.dev)",
  "plain_description": "The web portal where advisors and the team see market, portfolio and client data.",
  "first_code_date": "2025-11-12", "first_code_commit": "portal ddb7271a",
  "live_date": "2026-01-04", "live_evidence": "portal a0de9996 'Merge DEV to PROD: CloudFront API CDN deployment'; login system 2025-12-29 (portal 1dcc2a55); www.opalinvest.dev added to CORS 2026-01-19 (e1c35071d1); automatic deploy on every PROD push from 2026-03-23 (portal 8f5b18ce); 200 release tags, from portal-v2.1.0 (2026-02-26) to portal-v2.1.199 (2026-10-04)",
  "claim": "first_code MEASURED; live INFERRED (merge subject); release tags MEASURED",
  "notes": "The first CI/CD pipeline (2025-12-29, a2bf8e90) was turned off on 2026-01-03. The PROD auto-deploy dated 2026-03-23 is the one in use now."},
 {"system": "Agent fabric -- multi-agent org (serials, tiers, task orders)",
  "plain_description": "An organisation of AI agents with job titles (CTO, COO, CVO, CRO, engineers) that plan, build and check the work, and commit it under their own names.",
  "first_code_date": "2026-03-02", "first_code_commit": "8129d3fcb3 'add hierarchical multi-agent organization structure'; 2dd0d281b0 'issue 21 context-seeding task orders'",
  "live_date": "2026-03-02", "live_evidence": "e36a3901b5 is the first commit authored by an agent serial (1.0.0_SA_CTO). Agents authored 83% of March commits and 97-100% of commits every month since April",
  "claim": "MEASURED", "notes": "Before this, 'Agent #1..#4' sessions ran in January 2026 (9fa8719df1, 2026-01-03) with no serial identities."},
 {"system": "Agent message broker (MCP 'opal-agent-comms', org/mcp/server.py)",
  "plain_description": "The internal messaging switchboard the agents use to register, report status and hand work to each other.",
  "first_code_date": "2026-03-26", "first_code_commit": "d331613ad7 (server.py 1,022 lines + broker + monitor)",
  "live_date": "2026-03-26", "live_evidence": "Committed as already-running scripts ('commit org/mcp server, broker, and monitor scripts'). Messages persisted from 2026-04-09 (fe0d861da4)",
  "claim": "first_code MEASURED; live INFERRED", "notes": "server.py is 2,611 lines today."},
 {"system": "Tier-0 governance control plane + decision ledger",
  "plain_description": "A supervising agent (MSTR) and a numbered log of decisions (LD-xxxx) that records what Andrew decided and why.",
  "first_code_date": "2026-05-22", "first_code_commit": "e9546d7003 (Phase 1); 695ed58e4c (Phase 2 control plane)",
  "live_date": "2026-05-22", "live_evidence": "f0680c55ab 'CY-0001 -- first /govern cycle'",
  "claim": "MEASURED", "notes": "Ledger records at month end: 140 (May), 233, 371, 491, 617 (Sep)."},
 {"system": "Canonical workflow L1-L10 + worker subagents",
  "plain_description": "A fixed ten-step process that takes every project from brief to verified result, with one owner per step and disposable worker agents doing the build steps.",
  "first_code_date": "2026-09-01", "first_code_commit": "847c2ffa7c (org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md); 64605ad4a0 (task-order issuance gate)",
  "live_date": "2026-09-03", "live_evidence": "c3602bcf1a 'law(spine v3.0): subagent workers, one issuance'; first worker-subagent commit e7dda3d93c (0.9.0_WK_NFRA_COMPEFFICACY~2) the same day; first L10 round close 5a11f076d0 (NFRA_CLDGRPH)",
  "claim": "MEASURED", "notes": "771 distinct worker-subagent serials since then; they authored 3,482 commits in September."},
 {"system": "comp-* compiler tools (.tools/comp-*)",
  "plain_description": "Over 100 in-house tools that let agents search, map and check the code and the cloud quickly and with stated confidence.",
  "first_code_date": "2026-04-07", "first_code_commit": "98dd7b1f1e (compiler modules ported); first .tools/comp-* shim 2026-04-15 (comp-incrparity)",
  "live_date": "2026-06-15", "live_evidence": "f61a9be866 comp-which router + 8a7008ba8b comp-tool-hud.sh rail hook (search routed through the tools); comp-state 2026-07-14 (c7aca92002); comp-find 2026-08-05 (6ec915fa96)",
  "claim": "MEASURED (dates); 'live' = mandated use, INFERRED", "notes": "98 distinct tools at HEAD (104 files)."},
 {"system": "Dependency graph (org/modules/graph + comp-aws cloud graph)",
  "plain_description": "A map of how every pipeline, Lambda, bucket and permission connects, so a change can be checked for knock-on effects before it is made.",
  "first_code_date": "2026-04-07", "first_code_commit": "98dd7b1f1e (graph_compiler.py, execution_graph.py); 08fb9ffc89 2026-04-08 (trace compiler)",
  "live_date": "2026-06-11", "live_evidence": "28d45eb2b2 graph-call-manifest populated; comp-aws cloud-graph PRD 2026-06-01 (d425e072fb); nightly rebuild workflow 2026-07-07 (e32896edd0). Today's build (2026-10-04 12:48 UTC) models 2,816 AWS resources",
  "claim": "first_code MEASURED; live INFERRED", "notes": ""},
 {"system": "Deploy-completion ledger (change management)",
  "plain_description": "Every cloud change opens a record before it starts and closes it only after proof, so no deploy is left half-done.",
  "first_code_date": "2026-06-12", "first_code_commit": "a1506a0a4f (.tools/deploy_ledger.py); 5226efca92 (critical-paths ledger)",
  "live_date": "2026-06-12", "live_evidence": "First entries are 20260612T2024Z..T2125Z; 1,334 files today",
  "claim": "MEASURED", "notes": "Before June 2026, deploys were recorded only as 'ci: record deploy' commits."},
 {"system": "Opal gateway (M365 MCP gateway -> opal-gateway)",
  "plain_description": "A secure server that lets Claude use Opal's Teams, email, YCharts, Schwab and portal data under each person's own permissions.",
  "first_code_date": "2026-06-10", "first_code_commit": "ac3d904820 (NFRA_OPLMCP macro-project created)",
  "live_date": "2026-06-23", "live_evidence": "ledger 20260623T1731Z_oplmcp02-golive-cutover CLOSED 18:04Z (OIDC listener swap = go-live); Teams tools 2026-06-24 (11b816d785); YCharts tools 2026-07-01 (ledger ycharts-enable); renamed opal-gateway and live 2026-07-30 (b808187499); Schwab project NFRA_OPLGTW 2026-09-14",
  "claim": "MEASURED (ledger close line)", "notes": "A TLS skeleton was live-verified on 2026-06-16 (ledger oplmcp03-closed503)."},
 {"system": "mcp.opalinvest.dev site -- /sprint and /rivalfunds pages, mcportal operator console",
  "plain_description": "A company-sign-in website on the gateway showing the daily operating dashboard, the rival-funds research page and (in build) the MCP admin console.",
  "first_code_date": "2026-08-28", "first_code_commit": "97b8103069 (app/sprint_view.py on opal-gateway)",
  "live_date": "2026-08-28", "live_evidence": "ledger 20260828T1758Z_opal-gateway-sprint-view CLOSED 18:18Z (unauthenticated GET https://mcp.opalinvest.dev/sprint redirects to Microsoft login). /rivalfunds: ledger 20260930T1013Z_etfs-rivalfunds-thread-r1 CLOSED 15:33Z (39 resources). mcportal console: registered 2026-09-24 (8105cd4f0e), first gateway release ledger 20260925T1636Z",
  "claim": "MEASURED (ledger)", "notes": "The page title 'Opal Daily Operating Dashboard' was not found in infra/, .tools/ or daily_reports/. The mcportal submodule is not checked out, so its history is ABSENT."},
 {"system": "Daily sprint engine (.tools/daily-sprint.py)",
  "plain_description": "Writes the day's plain-English highlight reel of what shipped, from git and the project records.",
  "first_code_date": "2026-08-20", "first_code_commit": "a731dfa57b (engine + skill + first DAILY_SPRINT_2026-08-20.md)",
  "live_date": "2026-09-11", "live_evidence": "Web view 2026-08-28 (see the site row). Cloud scheduled generator: ledger 20260911T2002Z_daily-sprint-generator-first-apply CLOSED (21:30 Eastern schedule; leg L7 'THE JOB RUNS', served page read back)",
  "claim": "MEASURED", "notes": ""},
 {"system": "Deck generation (deck_generation/)",
  "plain_description": "Builds branded slide decks from a written prompt.",
  "first_code_date": "2026-03-26", "first_code_commit": "439297bc16",
  "live_date": "2026-06-18", "live_evidence": "66f53175a6 'close(DECK_CLAUDE): CLOSED COMPLETE' (Andrew: 'everything is complete'); /deck-gen skill 2026-06-15 (d17d45be07)",
  "claim": "first_code MEASURED; live INFERRED (closure record, not a served artifact)", "notes": "Commits: 10 in Mar, 54 in Jun, 5 in Sep."},
 {"system": "Bloomberg integration (integrations/bloomberg)",
  "plain_description": "Pulls Bloomberg terminal data into Opal's data and tools automatically.",
  "first_code_date": "2026-07-11", "first_code_commit": "cb02a6799b (NFRA_BBGTMNL terminal-device PRD); OPAL_BBGTML intake 2026-07-15 (8b7b53c957)",
  "live_date": "2026-07-15", "live_evidence": "63a5b8bdd2 'ENABLE LIVE' + first enabled dry run PASSED (fb02342b85); Bloomberg tunnel ledger 20260730T2220Z CLOSED 2026-07-30; consolidated into integrations/bloomberg 2026-08-12 (1ed08a1960, 'BOTH live bindings re-pointed and verified')",
  "claim": "MEASURED (commit/ledger); INFERRED that the 07-15 intake counts as 'Bloomberg live'", "notes": "Earliest Bloomberg mention is a data fix on 2026-01-18. Bloomberg commits per month: 27 (May), 39 (Jul), 134 (Aug), 308 (Sep)."},
 {"system": "YCharts reporting",
  "plain_description": "Generates client comparison and stress-test reports from YCharts data, now from the cloud.",
  "first_code_date": "2026-05-20", "first_code_commit": "2e81955ba3 (YALP_MDSRC live YCharts capability test)",
  "live_date": "2026-07-01", "live_evidence": "a24316e56a /ycharts-report PDF generator skill; ledger 20260701T2228Z_ycharts-enable CLOSED (6 read-only YCharts tools on the gateway); cloud recipes ledger 20260911T0333Z_ycharts-three-recipes",
  "claim": "MEASURED", "notes": "IRPT_YCDGEN (direct-API generation) was registered 2026-10-03."},
 {"system": "Investor Reporting (IRPT) backend",
  "plain_description": "The cloud engine behind advisor investor reports: client directory, permissions, performance data and branded exports.",
  "first_code_date": "2026-09-10", "first_code_commit": "f603d1a3b0 (registered IRPT_BCKEND in D9)",
  "live_date": "2026-09-10", "live_evidence": "f44cab8208 core root APPLIED (17 resources), ledger 20260910T2240Z_irpt-bckend-s17; about 40 IRPT deploy ledgers by 2026-09-11",
  "claim": "cloud deploy MEASURED; served to advisors ABSENT (project.json status=active)", "notes": "3,697 IRPT commits in 25 days. A portal page named 'Investor Reporting' has existed since 2026-01-22 (portal 13d8bb93)."},
 {"system": "Terraform / AWS infrastructure-as-code",
  "plain_description": "Cloud resources defined in versioned code so they can be reviewed, reproduced and rolled back.",
  "first_code_date": "2026-01-03", "first_code_commit": "0a44521fb6 (multi-account Terraform modules)",
  "live_date": "2026-02-02", "live_evidence": "0c85796c8a 'First Lambda migrated to Terraform - pilot migration successful' (plan shows No changes); news pipeline fully under Terraform 2026-02-20; CloudFront imports 2026-04-15 (CDRS_TFIMPT); safe-apply gate 2026-05-20 (05d764e60e)",
  "claim": "MEASURED (commit body)", "notes": "First Lambdas in the repo date from 2025-11-18 (news_scanner, finbert, market_query). Portal data-proxy Lambda 2025-12-01 (4e21579a73)."},
 {"system": "LGIC naming canon (infra/logic)",
  "plain_description": "One rulebook and generator for where every pipeline stores data and what every cloud resource is named.",
  "first_code_date": "2026-09-12", "first_code_commit": "845abef6c9 (infra/logic minted); e729fd6f30 (02_DOCTRINE 20 rules)",
  "live_date": "2026-09-15", "live_evidence": "lib/opal_naming.py 2026-09-14 (a925c8a642); ledger 20260915T0334Z_lgic-enforce-fence-49financial",
  "claim": "MEASURED", "notes": ""},
 {"system": "Surprise channel",
  "plain_description": "An append-only log where any agent records an unexpected finding and keeps working, so problems are captured without stopping the line.",
  "first_code_date": "2026-08-06", "first_code_commit": "6c50710afd (THE_SURPRISE_CHANNEL doctrine)",
  "live_date": "2026-08-21", "live_evidence": "c409aeda2c channel minted; 01834861ff 'FIRST REAL USE' the same day",
  "claim": "MEASURED", "notes": ""},
 {"system": "End of Day Teams automation (LDO-001)",
  "plain_description": "Drafts Andrew's End of Day Teams update from the daily sprint and posts it only after his SMS approval; also a Teams assistant.",
  "first_code_date": "2026-10-01", "first_code_commit": "3a360e8f33 (EOD update draft job); 044c3e0c6d + 54d3748545 2026-10-02 (Lambda Durable Object module + tenant)",
  "live_date": "2026-10-02", "live_evidence": "ledger 20261002T0535Z_ldo-001-teams-assistant CLOSED 14:15Z (25 adds); register 79fd2f0f6f: 'Served since 2026-10-02 (gateway /hx/teams live 19:23:40Z; first End of Day post 20:31:23Z)'",
  "claim": "MEASURED (ledger + register)", "notes": "Idea to live in about 1 day."},
 {"system": "[discovered] Black Diamond pipeline + Advisor Intelligence + medallion data lake",
  "plain_description": "Daily ingestion of custodian and Black Diamond data into bronze/silver/gold tables that feed the Advisor Intelligence page.",
  "first_code_date": "2026-01-15", "first_code_commit": "1c9543620e (BD pipeline + gold layer); portal 162c44fd (Advisor Intelligence page)",
  "live_date": "2026-01-15", "live_evidence": "portal page merged to DEV on 2026-01-15 (a9dba42a); bronze/silver/gold rename 2026-02-24 (9eac0a7849)",
  "claim": "first_code MEASURED; live INFERRED", "notes": "ADVI is the largest project family: 102 project files."},
 {"system": "[discovered] Cross-device agent bus + second fabric",
  "plain_description": "Lets agents on two machines exchange work, so two agent teams can run in parallel.",
  "first_code_date": "2026-07-02", "first_code_commit": "fbe9a95cdb (NFRA_AGENTBUS PRD)",
  "live_date": "2026-07-02", "live_evidence": "6d25c4165b 'S2 COMPLETE ... proven on LIVE'; earliest SITEZ subject 2026-07-29 (5b451a1b12); device split of directives 2026-08-19",
  "claim": "INFERRED", "notes": ""},
 {"system": "[discovered] Opal MCP tool index + Opal Analyst (opal_ai)",
  "plain_description": "One catalog so every Opal data property can be queried from Claude, and a Teams-facing analyst agent built on it.",
  "first_code_date": "2026-09-17", "first_code_commit": "9da61cab00 (NFRA_MCPINDEX registered); opal_ai submodule 2026-09-24 (69288c8ca0)",
  "live_date": "2026-09-25", "live_evidence": "ledgers nfra-mcpindex-* from 2026-09-26 and nfra-mcportal-r2-gateway-release 2026-09-25",
  "claim": "INFERRED", "notes": "OPAL_ANALYST first appeared 2026-08-10 (1ac23a7e11)."},
 {"system": "[discovered] Security-analysis research pack (AMGT_RESAPP)",
  "plain_description": "Pre-fills an analyst's research pack (model block, company description, segments) from Bloomberg and filings.",
  "first_code_date": "2026-09-10", "first_code_commit": "772c796a3f",
  "live_date": "ABSENT", "live_evidence": "status=active; Bloomberg-backed deploy ledgers 2026-09-19 and 2026-09-22",
  "claim": "first_code MEASURED; live ABSENT", "notes": "2,552 commits in 25 days."}
]}
```

## 2. Growth series

```json
{"growth": {
 "commits_per_month_workspace": {"method": "git log CLOUD, author date month, count", "claim": "MEASURED",
   "data": {"2025-11":19,"2025-12":63,"2026-01":531,"2026-02":905,"2026-03":937,"2026-04":2567,"2026-05":4220,"2026-06":4544,"2026-07":7882,"2026-08":10538,"2026-09":19407,"2026-10 (4 days)":3997}},
 "commits_per_month_portal": {"method": "git -C portal log --all", "claim": "MEASURED",
   "data": {"2025-11":67,"2025-12":108,"2026-01":415,"2026-02":363,"2026-03":242,"2026-04":508,"2026-05":271,"2026-06":113,"2026-07":107,"2026-08":168,"2026-09":947,"2026-10":252}},
 "agent_share_of_commits_pct": {"method": "author matches N.N.N_ serial", "claim": "MEASURED",
   "data": {"2026-01":0,"2026-02":0,"2026-03":83,"2026-04":97,"2026-05":100,"2026-06":100,"2026-07":99,"2026-08":100,"2026-09":100}},
 "active_agent_authors_per_month": {"method": "distinct commit authors; seat_instances = standing serials including ~lane copies; workers = 0.9.0_WK_* subagents", "claim": "MEASURED",
   "seat_instances": {"2026-03":28,"2026-04":53,"2026-05":44,"2026-06":42,"2026-07":58,"2026-08":104,"2026-09":127,"2026-10":31},
   "worker_subagents": {"2026-09":666,"2026-10":119}},
 "agent_serial_folders_month_end": {"method": "git ls-tree of org/tier*/ at the last commit of each month (serial-named dirs)", "claim": "MEASURED",
   "data": {"2026-02":0,"2026-03":32,"2026-04":43,"2026-05":48,"2026-06":51,"2026-07":53,"2026-08":98,"2026-09":127,"2026-10-04":129}},
 "comp_tools_month_end": {"method": "distinct .tools/comp-* names (.py/.sh suffix folded) in ls-tree at month end", "claim": "MEASURED",
   "data": {"2026-03":0,"2026-04":4,"2026-05":12,"2026-06":33,"2026-07":89,"2026-08":99,"2026-09":98}},
 "skills_month_end": {"method": ".claude/skills dirs in ls-tree", "claim": "MEASURED",
   "data": {"2026-04":0,"2026-05":15,"2026-06":33,"2026-07":52,"2026-08":67,"2026-09":84,"2026-10-04":85}},
 "terraform_month_end": {"method": ".tf files under infra/ and component dirs under infra/aws/terraform/ in ls-tree", "claim": "MEASURED",
   "tf_files": {"2025-12":4,"2026-01":30,"2026-02":61,"2026-03":77,"2026-04":149,"2026-05":206,"2026-06":275,"2026-07":390,"2026-08":413,"2026-09":521,"2026-10-04":550},
   "tf_components": {"2026-02":12,"2026-03":16,"2026-04":22,"2026-05":26,"2026-06":44,"2026-07":56,"2026-08":61,"2026-09":68}},
 "lambda_source_dirs_month_end": {"method": "dirs under infra/aws/lambda/ in ls-tree (repo source, not the live count)", "claim": "MEASURED",
   "data": {"2025-11":6,"2025-12":10,"2026-01":44,"2026-02":77,"2026-03":76,"2026-04":84,"2026-05":91,"2026-06":88,"2026-07":97,"2026-08":87,"2026-09":94}},
 "aws_footprint_today": {"method": "comp-find --corpus aws '.', node_type bands; graph built 2026-10-04 12:48 UTC (graph, not a direct AWS read)", "claim": "MEASURED (graph vintage)",
   "data": {"total_nodes":2816,"LAMBDA":232,"S3_BUCKET":41,"DYNAMODB_TABLE":47,"EVENT_RULE":153,"SCHEDULE":30,"EC2_INSTANCE":34,"IAM_ROLE":279,"SECRET":114,"API_ROUTE":241}},
 "deploy_ledger_entries_per_month": {"method": "change_management files with a YYYYMM prefix (the ledger started 2026-06-12)", "claim": "MEASURED",
   "data": {"2026-06":137,"2026-07":273,"2026-08":173,"2026-09":562,"2026-10 (4 days)":156}},
 "portal_prod_releases_per_month": {"method": "portal tags portal-v2.1.N by creator date", "claim": "MEASURED",
   "data": {"2026-02":4,"2026-03":16,"2026-04":49,"2026-05":35,"2026-06":24,"2026-07":26,"2026-08":20,"2026-09":18,"2026-10":8}},
 "project_codes_active_per_month": {"method": "registered codes (382 = org/projects/*.json names plus tree dirs) found in commit subjects that month", "claim": "MEASURED",
   "active": {"2026-03":25,"2026-04":50,"2026-05":80,"2026-06":88,"2026-07":136,"2026-08":99,"2026-09":73,"2026-10":36},
   "new_first_seen": {"2026-03":25,"2026-04":47,"2026-05":60,"2026-06":62,"2026-07":95,"2026-08":53,"2026-09":35,"2026-10":1}},
 "registered_projects_and_prds_month_end": {"method": "ls-tree counts", "claim": "MEASURED",
   "flat_project_json": {"2026-03":26,"2026-04":75,"2026-05":136,"2026-06":201,"2026-07":294,"2026-08":346,"2026-09":383},
   "tree_projects": {"2026-09":34,"2026-10-04":35},
   "prds_docs_architecture": {"2026-03":12,"2026-04":30,"2026-05":32,"2026-06":70,"2026-07":138,"2026-08":183,"2026-09":187}},
 "task_order_files_added_per_month": {"method": "files added under **/task_orders/** or **/task-orders/** (path-level; renames count again)", "claim": "INFERRED (approximate)",
   "data": {"2026-03":280,"2026-04":659,"2026-05":498,"2026-06":248,"2026-07":288,"2026-08":410,"2026-09":1647,"2026-10":253}},
 "decision_ledger_month_end": {"method": "LD-* files in org/tier0/ledger", "claim": "MEASURED",
   "data": {"2026-05":140,"2026-06":233,"2026-07":371,"2026-08":491,"2026-09":617}}
}}
```

What the series show: commits roughly doubled every two months, from 937 in March to 19,407 in September. Agents authored almost every commit from April on. The number of active project codes peaked in July (136), then fell to 73 in September while output kept rising. The work moved into fewer, deeper projects once the canonical workflow and the one-project-per-seat rule arrived.

## 3. Milestones for the management timeline

1. **2025-11-18**: The workspace opens. The news scanner is already running, and its News Intelligence dashboard is on the portal (the portal repo started 2025-11-12).
2. **2026-01-04**: The portal goes to production behind CloudFront. A login system had been added on 2025-12-29.
3. **2026-01-15**: The Black Diamond data pipeline and the Advisor Intelligence page.
4. **2026-02-02 to 02-20**: The first Lambda is managed by Terraform. The rebuilt news pipeline goes fully under infrastructure-as-code.
5. **2026-03-02**: The AI agent organisation is founded. Agents wrote 83% of March commits.
6. **2026-03-23 to 03-26**: The portal deploys itself on every PROD push. The agent message broker and the deck generator are added.
7. **2026-04-07 to 04-15**: The compiler tools and the dependency graph. There were 98 tools by August.
8. **2026-05-22**: Governance layer: a supervising agent and the decision ledger.
9. **2026-06-12**: Every cloud change now goes through a deploy record that must be proven before it closes (1,334 records to date).
10. **2026-06-23**: The Opal gateway goes live: Teams and email in Claude. YCharts was added on 07-01.
11. **2026-07-15 to 07-30**: Bloomberg terminal data flows in automatically (intake, then the tunnel).
12. **2026-08-28 / 09-11**: The daily operating dashboard goes live at mcp.opalinvest.dev/sprint. From 09-11 it is written automatically every night in the cloud.
13. **2026-09-01 to 09-03**: The ten-step canonical workflow and disposable worker agents. 771 workers so far; September output was 19,407 commits.
14. **2026-09-10 to 09-15**: The Investor Reporting backend is deployed to the cloud, and the LGIC naming canon is enforced.
15. **2026-09-30 / 10-02**: The /rivalfunds research page goes live, then the End of Day Teams assistant. The assistant went from idea to live in about one day.

## 4. Gaps and caveats

- **News scanner origin.** The news scanner is older than both repos. Its real first date is before 2025-11-18 (README dated 2025-11-13), and git does not show it.
- **Moved paths.** `--diff-filter=A` reports a moved path at the date of the move. This affects `integrations/bloomberg` (2026-08-12 is a consolidation date) and `.tools/comp-*` (the compiler logic is older, from 2026-04-07 in `org/modules`). I used the earlier evidence where I found it.
- **Submodules not checked out.** `mcportal` and `opal_ai` are not initialized locally, so their own histories are ABSENT. I did not find the page title "Opal Daily Operating Dashboard" in infra/, .tools/ or daily_reports/. It probably lives in the gateway-rendered HTML or in mcportal.
- **What "live" means.** For local tools (comp-*, daily-sprint, broker, surprise channel), "live" means first use or a mandate, not a production service. For IRPT and AMGT, being served to end users is ABSENT: both projects are still `active`.
- **Deploy records before June.** The deploy-ledger series starts 2026-06-12, so it cannot be compared with earlier months. Earlier deploys appear only as "ci: record deploy" commits.
- **Lambda counts.** The Lambda source-dir counts are repo directories, not live functions. The live figure (232 Lambdas, 2,816 AWS resources) comes from the dependency graph built 2026-10-04 12:48 UTC, not from a direct AWS read.
- **Project-code counts.** These cover only the 382 registered codes found in commit subjects. Hyphenated ids such as LDO-001 and unregistered codes are not counted.
- **Task-order counts.** These are approximate: they are path-level, so a renamed file is counted again.
- **Commit volume.** Commit volume is not output. September includes 3,482 worker commits, and many commits are records and governance. October covers 4 days only.
- **Dates.** Dates are author dates in the committer's local time zone. Ledger times are UTC.
