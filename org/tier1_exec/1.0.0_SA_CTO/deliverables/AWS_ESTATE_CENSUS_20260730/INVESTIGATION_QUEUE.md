# Investigation queue — DISPATCHED to 0.7.0_AE_CloudOps 2026-07-30 ~18:5xZ (Andrew-direct)

**Mandate (Andrew verbatim):** "go through each item, using our research and notations, to
effectively scan for a kill list, checking to make sure these resources are truly deprecated.
we want to know about any dependencies that actually are material, but their role here is
essentially confirming what can be deleted." 0.7.0 CONFIRMS; Andrew executes the verdicts.
Dispatch: MCP 20260730T~185xZ; method requirements C-3/C-6/C-10/C-11 attached; Aug-1 etfs
gate + identity_2 caution + wsd-49f pending-decision flagged.

**Protocol (Andrew-direct 2026-07-30):** "Items like this that we mention will require
investigation later will be assessed at the completion of our work and issued to 0.7.0."
This file accrues them with context so the dispatches write themselves. Distinct from DELETE
GATES (cheap traces the census runs itself, same-session) — this queue is the deferred,
deeper work. Append-only; # = queue id.

| # | Item | Context / question | Source ruling |
|---|---|---|---|
| Q-1 | **Schwab SI2/SDD behavior map** | Box-as-token-minter hypothesis; token lifecycle; every assets/schwab writer + trigger; box lifecycle vs ENABLED crons; end-to-end ingestion paths | batch-2 #11 (dispatch already DRAFTED: `SEMANTIC_NOTES/dispatch_0.7.0_schwab_ingestion_brief.md` — Andrew sends directly) |
| Q-2 | **mdpf bucket dissolution investigation** | "Probably should not exist" — map mdpf content into assets(medallion)+portal(platinum); design the dissolve | batch-2 #8 |
| Q-3 | **etfs migration assessment** | Mission-critical (ETF rebate ops): ingestion/storage robustness assessment + assets-overlap clash review (definitions/functions/pipelines) BEFORE migration | batch-2 #9 |
| Q-4 | **pm vs portfolio twin analysis** | Same lambda family, same product (Portal Portfolio Management, C4 interactive-products); identify essential functions in each or confirm one is a pure deprecated twin (pm 242MB/87 objs PFDE+PFOE; portfolio 92KB/10 objs PFDE; PFOE/ cold 5.5mo) | batch-3 #16/#17 |
| Q-5 | **lambda-artifacts hygiene review** | Keep presumed; low priority; 31 per-pipeline prefixes incl. relics (demov1, exec-summary 04-27); version-retention policy | batch-3 #20 |
| Q-6 | **Shared-reader organization** | The recurring 6-lambda portal-core set (market-overview-tiered, portal-data-proxy, finbert-batch, regime-classifier, session-analytics, infrastructure-monitor) reads "everything" per the graph — Andrew: "this should be a lot more organized and defined." Also resolves the graph's shared-module attribution inflation | batch-3 #21 note |
| Q-7 | **trade parquet batch-export leg** | Dead since 01-21 while submissions flow; revive or retire | batch-2 #14 |
| Q-8 | **astn output-quality review** | CEO digest quality; project ASTN_WSJFT | batch-2 #10 |
| Q-9 | **Unmapped-lambda sweep** | 4 found incidentally (news trio + inf-silver-chain); full live-vs-source-map join at compute layer | census |
| Q-10 | **INF_D_04 platinum-read violation** | gold producer reads platinum/advisors/ (comp-dataflow gate BLOCKING find); DS lane | census |
| Q-11 | **inf cold silver categories** | accounts_dim/orion-rest/api_dims/transactions/performance_dim (Apr–May): superseded by migration or paused? | batch-1 #3 |
| Q-12 | **[ANDREW-APPROVED, EXECUTING as A1/A2/A3 -- FIRST PRIORITY]** TF-block removal for deleted buckets | analytics-dashboard + cloudfront-logs still DECLARED — resurrection hazard at next apply (C-6 two-legged-delete law) | zero-edge pass |
| Q-13 | **smartx-v2 validation + code archive + delete execution** | Semantic coverage check vs assets/smartx redesigned taxonomy; archive deploy*/scripts/lambda-deploy to assets archive; then delete | batch-2 #12 |
| Q-14 | **portal-v2 target-vs-current gap** | Measure distance to the /platinum-only target (C-2); feeds migration program | batch-1 #5 |
| Q-15 | **[STEP 1/5 DONE @0817abd006 (rules DISABLED+verified); STEPS 2-5 NEED AN AE LANE]** news-av full teardown package | bucket + 7 seeking-alpha lambdas + 2 scraper EC2 + triggers + AMI-rotation keyword; Andrew ruled "almost surely all ready for deletion"; TF-managed = AE executes | batch-3 #15 |
| Q-16 | **market-update/fred teardown package** | stop fred-data-ingestion first (bucket name in code), then bucket + 2 us-east-2 fred alarms; zombie-flow specimen | batch-3 #19 |
| Q-17 | **49F converter-ops cleanup register execution** | Andrew ruling (s.6 verbatim, ledgered): high-confidence-dead + decision-class lists from 0.7.0 map s.9; GATED items behind the wsd-49f frontier decision | 0.7.0 behavior map |
| Q-18 | **MDPF etf ACTUAL-holdings rewiring** | Condemned: wsd-49f estimate feeder + mdpf/feeds/partner_held_etf. Design: wire mdpf_aggregate_aua etf_decomposition to the actual-holdings dailies (opal-data-etfs); retire the estimate leg; identity_2 live-gate caution (preserve the WRITE before deleting); folds into Q-2 dissolution | mdpf condemnation |
| Q-19 | **served-key trail selector migration** | When platinum serving moves to portal-v2, opal-served-key-write-trail selectors must move with it (currently pinned to opal-data-{inf,bd,cot}/platinum/firm/) | card 27 |
| Q-20 | **INFRPT daily-report cleanup** | infrastructure-daily-snapshot 'is a mess we meant to clean up with INFRPT project'; keep-ruled bucket, producer needs the deferred cleanup | batch-5 #32 |
| Q-21 | **opalinvest-portal -> portal-v2 origin consolidation** | The SPA-shell origin is a live default CF behavior; Andrew wants those assets IN the portal bucket; design = CF re-origin + asset migration + Q-19 trail selectors interplay | batch-5 #35 |
| Q-22 | **[ANDREW-RULED: 'all of it can go' -- scope caveat superseded]** orion-crawl-harness EC2 disposition | Writer of the now-deleted crawl-catalog; box + crawl-harness TF stack remain, unruled | batch-5 #33 |
| Q-23 | **opal-sessions system decommission** | Andrew: decommission completely. Set: table (backup-capture first; delete DENIED at permission layer, needs GO) + opal-session-analytics lambda + 4 /analytics/* routes + portal ingest calls. Shared role survives | ddb batch-1 #1 |
| Q-24 | **Terraform ALL globgrph resources** | Andrew: 'summarily terraformed' -- nessie _objs/_refs tables + any other LIVE-no-DECLARED globgrph pieces; plus the ECS->DDB derive gap fix so the graph sees its own substrate | ddb batch-1 #3 |
| Q-25 | **ETFS-ownership canonicality (P0)** | 'so many ETFS ownership tables now, one of them is canonical and complete, i just dont know which' -- P0 at DDB handoff; post-Aug-1 only | ddb batch-2 #14 |
| Q-26 | **bd-securities reader census** | portal-consumption not confirmed (2/28 checked); close with the reader-census recipe; alt hypothesis = deprecated bd-gold txn-engine security-ID source | ddb batch-2 #9 |
| Q-23-AMEND | opal-pii-lookup DELETE joins the Q-23 execute-ready set (backup->delete->verify; PII retention of the backup is part of the ruling) | ddb batch-2 #10 |
| Q-27 | **user-permissions investigation** | Andrew: 'definitely needs further investigation'. 12 items, KMS, zero edges + zero env refs on the AUTHZ surface; code-level census required (C-16) | ddb batch-3 #17 |
| Q-28 | **opal-users deprecation disposition** | Deprecation RULED (v2 is official); delete-vs-retain not authorized -- auth-surface caution, needs a code-level reader census first | ddb batch-3 #15 |
| Q-29 | **trade-users + parquet-batch-export teardown** | Andrew: proto of the trade product, 'gotten rid of alongside the deprecated parquet output... should be investigated though'. MUST NOT sweep by name -- opal-trade-submissions + trade-security-identifiers are LIVE and KEPT | ddb batch-5 #30 |
| Q-30 | **opal-firms/offices/invitations disposition** | Confirmed unused scaffold w/ fictional data (join to users-v2 fails); ALSO the estate's only PROVISIONED tables -- delete, or keep + switch billing mode | ddb batch-5 #35-37 |
| Q-31 | **opal-pm-snapshots delete (producer-first)** | Never adopted (TTL off + 0 items); gate on the live opal-pm-snapshot-handler code path before dropping the table | ddb batch-5 #34 |
| Q-32 | **FIRMSEP bypass control -- exist-or-not decision** | 100% failed delivery AND mis-specified pattern (~250K legitimate matches/day). Repairing delivery alone creates a 250K/day page storm. Moratorium applies: decide whether the control exists and in what form BEFORE touching SNS | EventBridge walk |
