# NFRA_REPORT -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`);
the gate `.tools/surprise-row-gate.py` validates every NEW row (schema
`org/surprise_channel/schemas/investigation_item.schema.json`, identity, folder == project, the allocator
coordinate). Lane `ANY`.
**Id grammar (site-Z fabric):** a worker's row is `NFRA_REPORT-Z-W<n>-S<k>` (`<n>` = its slot, `<k>` next
unused within that coordinate); a seat's row is `NFRA_REPORT-Z-S<k>`; the CVO's adjudication rows live in
`../adjudications/` as `NFRA_REPORT-Z-C-S<k>`. **Append-only during the round.** Never edit an existing row.
**This file opened by** `0.9.0_WK_NFRA_REPORT~2` at `RP-s-5` (`TO-RP-s-5`) -- the first rows in this
project's channel. Denominator at this write: **3 rows**, all `~2`'s (`S1`, `S2`, `S3`).

```json
[
  {
    "id": "NFRA_REPORT-Z-W2-S1",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_REPORT~2",
    "surfaced_at": "2026-09-09T20:20:00Z",
    "one_line": "RP-s-5: the live EC2 fleet (32 instances, us-east-1, full sweep) exceeds the 27-service declared manifest by 10 undeclared instances -- 8 remain undeclared after this cell's two backfills (bd-gold-detail-generator, estate-report-runner's churned id).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws ec2 describe-instances --region us-east-1 (no instance-id filter) run 2026-09-09T20:10Z -- 32 of 32 Reservations/Instances returned; cross-checked 0 of 0 in us-east-2 and us-west-2 the same session",
        "infra/aws/ec2/EC2_MANIFEST.json services (27 keys) at HEAD 7ea739b7b5 -- 25 of 27 rows carried a non-null instance_id (24 of 25 distinct, one by-design duplicate bd-allocations/bd-price-runner), of which 22 of 24 resolved live and 2 of 24 did not (orion-crawl-harness, estate-report-runner)",
        "the 10 live instances with no matching manifest row: 1 extra i-07ebae29a16e43ed1 (Name=seeking-alpha-scraper), 7 extra under Name=historical-prices-fetcher (i-0416edf7e4b901380, i-094c504a4384f9c47, i-025cba31603a6c8a6, i-032fa1babe1abe48a, i-0ec91038b9a2c73a6, i-088e7fa9323bac1b9, i-03c397afaa967d978), 1 x i-074bfc40ee049dc62 (Name=bd-gold-detail-generator, backfilled into the manifest by this cell), 1 x i-0584e17d283fa7ef4 (Name=estate-report-runner, backfilled into the manifest by this cell replacing the stale i-0512bd3cbaf602b7f)",
        "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~2/COMPUTE_MANIFEST_FINDINGS.md s.2 -- the full reconciliation table and the historical-prices-scheduler Lambda note (EC2_MANIFEST.json historical-prices-fetcher._note) consistent with a launch-fresh-instance-per-run mechanism"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RP-s-5 carries the L1 brief's MEASURED STARTING STATE as '27 declared services' and does not name any undeclared live compute; the cell's ACT is to make the manifest answer what compute is run.",
    "world_is": "The live AWS account runs at least 32 EC2 instances in us-east-1; 8 of them (after this cell's own two backfills) match no manifest row by instance_id, all under Name tags the manifest already declares (historical-prices-fetcher x7, seeking-alpha-scraper x1) -- the declared set undercounts live compute, and RP-s-9's box-grain cost anomaly (conditioned on this cell per PRD D3) inherits that undercount if not read past the manifest.",
    "notes": "Not remediated: no evidence names which (if any) of the 8 is canonical for its Name tag, and terminating/relabelling any of them is outside RP-s-5's EC2/ECS-enumeration-only bound. Carried for RP-s-9 and for whichever seat owns historical-prices-scheduler's launch behavior."
  },
  {
    "id": "NFRA_REPORT-Z-W2-S2",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_REPORT~2",
    "surfaced_at": "2026-09-09T20:21:00Z",
    "one_line": "RP-s-5's always-on-by-group naming (Dashboard, Website, Graph, per ruling 15b verbatim) conflicts with two OTHER canonical artifacts of this same project that both render the third name as 'Gateway' -- and 'Gateway' and 'Graph' are confirmed to be two DIFFERENT, both-real compute surfaces.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260909_1458Z_INFRA_REPORT_FIVE_RULINGS.md:313,365 -- Andrew verbatim, batch 6: 'should be named separately id say by group (Dashboard, Website, Graph)'; ruling 15b's own surrounding prose (:369-371) discusses 'no graph-ops box' and '7 unused opal-globgrph-* security groups', i.e. Graph = the graph-database infra",
        "org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md s.6 (rulings that bind), first ruling: 'the three properties are Dashboard (the entire serverless system feeding opalinvest.dev), Website, Gateway (the opal-gateway MCP server)' -- names the third group Gateway, not Graph, and glosses it explicitly as the opal-gateway MCP server",
        "org/projects/NFRA_REPORT.json (generated_at 2026-09-09T19:35:31Z) name field: 'across three properties (Dashboard, Website, Gateway)' -- the registered project record independently repeats 'Gateway'",
        "this cell's own live ECS enumeration (aws ecs list-clusters/describe-clusters/list-services/describe-services --region us-east-1, 2026-09-09T20:10Z): 1 of 1 cluster opal-globgrph, ACTIVE, 3 of 3 services (globgrph-nessie/trino/serving) running, desiredCount=1 each, 0 of 0 scheduled scaling actions -- confirming 'Graph' has real, always-on compute distinct from opal-gateway (EC2 i-07dccb1615503ac99, t4g.nano, confirmed running live, systemd opal-gateway.service behind an ALB)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RP-s-5 BOUNDS: 'Andrew's ruling 15b: the always-on exception set is named BY GROUP, not by box' and names the three groups '(Dashboard, Website, Graph)', citing ruling 15b directly.",
    "world_is": "Two other artifacts of the SAME project (the L4 PRD this decomposition mirrors, and the registered project record generated from it) both name the third group 'Gateway' and gloss it as the opal-gateway MCP server -- a different, also-real, also-running EC2 box from the opal-globgrph ECS cluster ruling 15b's own prose and this cell's live read both point to. A reader building the always-on report off the PRD's wording would group opal-gateway under the third name and never look for opal-globgrph; a reader following ruling 15b verbatim (as this cell does) finds opal-globgrph but has no named group for opal-gateway.",
    "notes": "Carried open per TO-RP-s-5's own BOUNDS ('OPEN SUB-ITEM, carried not resolved'); this cell followed the TO's literal wording (Dashboard/Website/Graph) in its deliverable's s.5 table and left opal-gateway and canonical-schwab-si2 explicitly ungrouped rather than guessing which of the two readings is authoritative. Full table: org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~2/COMPUTE_MANIFEST_FINDINGS.md s.4a/s.5."
  },
  {
    "id": "NFRA_REPORT-Z-W2-S3",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_REPORT~2",
    "surfaced_at": "2026-09-09T20:22:00Z",
    "one_line": "TO-RP-s-5's carried premise 'the manifest is itself 2014.2h old' (L1 brief vintage) is stale as of this cell's re-grounding: the manifest's own _last_updated is ~62 minutes old, not ~84 days, because an intervening opal-gateway deploy touched the file after the brief's vintage.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/EC2_MANIFEST.json (worktree, pre-this-cell's-edit) top-level _last_updated: '2026-09-09T19:08:11Z'",
        "date -u run at 2026-09-09T20:10:24Z (this session) -- ~62 minutes after _last_updated, not ~2014 hours",
        "git log -1 --format='%H %ci' -- infra/aws/ec2/EC2_MANIFEST.json -> commit 9f76655b9f, 2026-09-09 15:08:18 -0400 (=19:08:18Z), subject 'Deploy EC2 opal-gateway @ 7bd89b5d71' -- an operational deploy record write, not a full re-sync, landed after the L1 brief's cited vintage @37ff80867a"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RP-s-5, MEASURED STARTING STATE, carried not re-derived: 'the manifest is itself 2014.2h old.'",
    "world_is": "At this cell's re-grounding the manifest's own _last_updated timestamp is approximately 1 hour old, because an unrelated opal-gateway deploy commit wrote to the same file's top-level timestamp after the brief's vintage. The brief's number was correct when measured; it does not describe the file's age at TO-RP-s-5's execution time.",
    "notes": "INERT: this cell's ACT (the schema fix, the ECS enumeration, the always-on grouping) does not depend on the manifest's age, so nothing here changed as a result. Recorded per CLAUDE.md rule 22's STATE axis (DESIRED/APPLIED/EXERCISED are not a description) and re-grounding discipline."
  },
  {
    "id": "NFRA_REPORT-Z-W2-S4",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_REPORT~2",
    "surfaced_at": "2026-09-09T21:10:00Z",
    "one_line": "RP-s-9: box-grain cost attribution is blocked by a payer-account Cost Explorer setting (resource-level data opt-in DISABLED, confirmed live) and by cost-allocation tag coarseness/drift -- both independent of RP-s-5's manifest fix and outside this project's write surface, so RP-s-5 landing does NOT fully unblock box grain as the original bound's stated reason implied it would.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~ZZ",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws ce get-cost-and-usage-with-resources --time-period Start=2026-09-01,End=2026-09-09 --granularity DAILY --metrics UnblendedCost --group-by Type=DIMENSION,Key=RESOURCE_ID --filter '{\"Dimensions\":{\"Key\":\"SERVICE\",\"Values\":[\"Amazon Elastic Compute Cloud - Compute\"]}}' run 2026-09-09 this session -> AccessDeniedException: 'Resource-level data granularity is an opt-in only feature. You can be enable this feature from the PAYER account's Cost Explorer Settings page.'",
        "aws ce list-cost-allocation-tags --status Active run 2026-09-09 this session -> exactly 7 active tags (System, Pipeline, Owner, Partner, Macro, Project, Environment), unchanged from the L1 brief's 2026-07-07 measurement; none is a per-instance-unique key",
        "aws ec2 describe-instances --region us-east-1 (Tags) run 2026-09-09 this session -> System=bd-pipeline shared by 5 declared EC2 rows (bd-allocations, bd-gold-layer-runner, bd-transactions, bd-assets, bd-fees); System=InflectionPipeline shared by 4 (inf-gold-layer-runner, inf-gold-qa-runner, inf-exporter, inf-bronze-runner); System absent (null) on 9 of 27 declared rows (all 8 live historical-prices-fetcher instances + canonical-schwab-si2); bd-gold-qa-runner tagged System=BDPipeline (differently cased from its 5 bd-pipeline siblings)",
        "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~2/COST_ANOMALY.md s.2/s.2a -- the full reasoning and the System-tag intermediate-grain table cross-referenced against RP-s-5's EC2_MANIFEST.json v1.1"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RP-s-9's original BOUNDS: 'BOX grain CANNOT be computed until RP-s-5 lands, because the compute manifest is EC2-only with ECS absent entirely' -- attributing the entire box-grain block to the manifest. The coordinator's addendum on this same TO asked this cell to state plainly if box grain is now fully reachable given RP-s-5 landed.",
    "world_is": "RP-s-5 discharged the INVENTORY half of the box-grain blocker (a complete, schema-clean EC2+ECS list with machine_type/lifecycle). It did not and could not discharge the COST-ATTRIBUTION half: AWS Cost Explorer's resource-level (per-instance) cost API is opted OUT at the payer account, and the only active cost-allocation tags are segment-grain or a coarser-than-box 'System' sub-segment with 9 of 27 rows untagged and a casing drift splitting one real segment into two. Literal box-grain cost (one figure per EC2 instance or ECS service, tested against its own trailing-30-day price) remains unreachable today, for reasons that have nothing to do with RP-s-5.",
    "notes": "Not remediated: enabling payer-account resource-level CE data, fixing the System tag casing drift, and retiring the stale M365MCPGateway cost tag (found in the same sweep, s.2a of the deliverable) are all outside this cell's <paths> and outside comp-schedule's battery finding for this project. Disarm owner is the L6 issuer (2.0.0_SA_COO~ZZ), who owns whether a future round routes this to a billing/Terraform-tag owner."
  }
]
```
