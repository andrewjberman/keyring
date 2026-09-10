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
    "id": "NFRA_REPORT-Z-S1",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZZ",
    "surfaced_at": "2026-09-09T21:35:00Z",
    "one_line": "RP-s-1's cell text covers only the two-axis vocabulary, but the S1 manifest row it mirrors covers FWD-2 AND FWD-4 including 'the property+owner attribution riding both' -- so FWD-4's attribution axis was never cut into any cell of this round, and the L6 coverage limb cannot see it because that limb grades cell IDS against the decomposition's id space, never a cell's TEXT against its manifest row's CONTENT.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD NFRA_REPORT_PRD.md s.8 row S1 names outcomes 'FWD-2, FWD-4' and its surface text ends '... plus the property+owner attribution riding both'.",
        "NFRA_REPORT_DECOMP.md: enumeration of the token 'attribution' over the whole file returns 0 hit(s). The RP-s-1 cell text covers axis 1's six values, axis 2, GREEN, and the two expressibility gaps -- and no attribution limb.",
        "NFRA_REPORT.TO-RP-s-1.state-model-two-axis-vocabulary.md: enumeration of 'attribution' returns 0 hit(s). The worker face never carried the limb, and the worker face is the whole of a worker's context.",
        "The built deliverable deliverables/0.9.0_WK_NFRA_REPORT~1/STATE_MODEL.md: enumeration of 'UNGROUPED' returns 0 hit(s) and of 'Dashboard' returns 0 hit(s) -- it renders no attribution axis at all. The worker built exactly what it was given.",
        "L6 issuance @7d698685fe printed 'issuance coverage 12 of 12 cell(s) ... owned by the staged orders' and PASSED, because every cell id in the decomposition is owned by an order. Coverage by ID was complete while coverage by CONTENT was not."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD s.8 row S1: outcomes 'FWD-2, FWD-4'; surface includes 'the property+owner attribution riding both'. Decomp s.1 invariant: 'every cell mirrors a manifest row, and every manifest row has at least one cell.'",
    "world_is": "RP-s-1 mirrors S1 by ID and covers only its FWD-2 half. Zero occurrences of 'attribution' in the decomposition or in the task order; zero occurrences of 'Dashboard' or 'UNGROUPED' in the completed, merged deliverable. FWD-4 therefore has NO built artifact in round 1, and no gate refused: the coverage limb compares the union of <owned_cells> to the decomposition's cell id set, which is satisfied by a cell that owns a row and cuts only part of it. This is the L5 author's error, not the worker's and not the gate's.",
    "notes": "ARMED because rule 27's round-close asks the CTO for a PRD addendum where an FWD no cell served, and this is exactly that case -- FWD-4 is unserved by any cell of this issuance. disarm_owner is 1.0.0_SA_CTO~Z as the L4 owner who decides whether FWD-4's attribution limb is an addendum or a round-2 recut; the recut itself would be 2.0.0_SA_COO~ZZ's in ONE issuance. NOT a request to reopen RP-s-1: that order is terminal, its instance VALID, and reopening an accepted certified cell is a rewind. The repair lives forward. Sharpened by the same seat's disarm of NFRA_REPORT-Z-W2-S2 at a535ae513e, which ADDED a mandatory rendered UNGROUPED value to FWD-4's attribution axis -- so the uncovered limb has since grown a new required value that no cell is positioned to build."
  },
  {
    "id": "NFRA_REPORT-Z-S2",
    "adjudicates": [
      "NFRA_REPORT-Z-W2-S2"
    ],
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~Z",
    "surfaced_at": "2026-09-09T21:44:00Z",
    "one_line": "DISARM of NFRA_REPORT-Z-W2-S2 by its named disarm_owner: the Gateway-vs-Graph conflict is TWO AXES welded by an inference in ruling 15b's own prose, not a contest between two names for one axis. Resolved at L4 in PRD v0.4 @a535ae513e.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/briefs/global-infrastructure-reporting-brief-20260909.md@37ff80867a:46 -- O4, the ATTRIBUTION axis (which property OWNS a problem): 'Every finding rolls up to Dashboard, Website or Gateway (Andrew-direct, 2026-09-09)'",
        "same brief:83 -- O9, the ALWAYS-ON EXCEPTION SET (what is exempt from autoshutdown): 'The always-on set is expressed by group -- Dashboard, Website, Graph'. Two DIFFERENT axes serving two DIFFERENT outcomes; no reason their third members must match",
        "org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260909_1458Z_INFRA_REPORT_FIVE_RULINGS.md ruling 15b -- titled 'THE EXCEPTION SET IS NAMED BY GROUP, NOT BY BOX'; the welding sentence 'the always-on exception set is expressed on the SAME three-property axis as the report itself' is that record author's INFERENCE, not Andrew's words. Each of his two utterances is coherent on its own axis",
        "same brief, limits section item 7 -- 'the Graph group (asserted empty; three ECS services exist)' is named there as one of TWO inferences the brief's own author falsified during review. The correction was sitting in this PRD's L1 source and 1.0.0_SA_CTO~Z did not carry it",
        "org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md s.6 @a535ae513e -- the amended ruling, the UNGROUPED ruling, and the 15b sub-item discharge; FWD-4's ACCEPT line re-tested and made NEUTRAL ON THE COUNT so Andrew's answer cannot invalidate it"
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "W2-S2 asserted the conflict was PRD-says-Gateway vs Andrew-says-Graph -- one axis with two candidate third members -- and that a determination was owed on which is ratified.",
    "world_is": "BOTH are ratified, for DIFFERENT axes. The L1 brief carried both namings in two different outcomes (O4 attribution, O9 always-on set). The defect was (a) an inference in ruling 15b's prose that welded them, and (b) 1.0.0_SA_CTO~Z collapsing them into one three-member axis at L4 and dropping Graph -- a rule 24(iii) intent-coherence violation. The worker's choice to leave opal-gateway and canonical-schwab-si2 explicitly ungrouped was CORRECT and is now specified behaviour rather than a judgment call.",
    "notes": "DISARMED. Repair landed at a535ae513e (PRD v0.4 + project.json + the re-derived org/projects/NFRA_REPORT.json; the wrong axis string now measures 0 in both json carriers). FWD-4 carries a MANDATORY RENDERED UNGROUPED value so no live surface leaves the axis silently. Ruling 15b's 'the Graph group may be EMPTY' sub-item is DISCHARGED: opal-globgrph is ACTIVE with 3 of 3 services running. THE MEMBER NAMES ARE NOT SETTLED HERE and are not this seat's -- naming law is sovereign, and it is an open call at Andrew (is FWD-4's third member Gateway, Graph, or both/four? where does canonical-schwab-si2 sit?). UNGROUPED is what lets the loop cycle without that answer. VOCABULARY NOTE, flagged rather than assumed: disposition GRADUATED is used here to mean the finding was ACCEPTED AND ACTED ON at L4, graduating into a spec change -- NOT that a CVO remediation row is owed. If 3.0.0_SA_CVO~Z reads GRADUATED as implying one, say so and this row is superseded by a corrected successor rather than edited. WHY THIS ROW EXISTS AT ALL: 2.0.0_SA_COO~ZZ (msg 20627) measured that a535ae513e touched three files and NOT the channel, so the disarm lived only in a PRD section and a broker message -- and CLAUDE.md says in terms that a broker message is NEVER the carrier. A reader of this channel, 3.0.0_SA_CVO~Z at L9 included, would have seen an ARMED hazard that was in fact resolved. That catch was correct and this row is the fix."
  },
  {
    "id": "NFRA_REPORT-Z-S3",
    "adjudicates": [
      "NFRA_REPORT-Z-S1"
    ],
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~Z",
    "surfaced_at": "2026-09-09T21:45:00Z",
    "one_line": "DISARM of NFRA_REPORT-Z-S1 by its named disarm_owner: FWD-4 was indeed served by no cell. Ruled an L4 ADDENDUM, not a reopen -- manifest row S1 is NARROWED to FWD-2 and the attribution limb becomes its OWN row S13, which makes RP-s-1 an exact mirror of the narrowed row rather than a deficient cell.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md s.8 at HEAD before this edit -- row S1 named TWO outcomes ('FWD-2, FWD-4') and NO other row named FWD-4 (measured: 1 of 12 manifest rows matched FWD-4, and it was S1)",
        "org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP.md:54 -- RP-s-1's act line covers the STATE MODEL only. 2.0.0_SA_COO~ZZ's own measurement (0 hits for 'attribution' in the decomp and the task order; 0 for 'Dashboard'/'UNGROUPED' in the merged deliverable) is ACCEPTED and deliberately NOT re-run -- re-running a peer's instrument is repetition, not corroboration",
        "CENSUS OF THE CLASS, run at this seat rather than assumed: 2 of 12 manifest rows named more than one outcome -- S1 (FWD-2, FWD-4) and S2 (FWD-3, FWD-1). S2 is NOT the same hazard, for a stateable reason: its second outcome FWD-1 also has DEDICATED rows S3 and S4, so a partial cut of S2 cannot orphan it -- exactly what was not true of FWD-4",
        "PRD v0.5 (this act): S1 narrowed to FWD-2, new row S13 carries FWD-4 plus the mandatory rendered UNGROUPED value, MECE re-run and printed -- 13 rows, 0 orphans, 12 of 12 outcomes carried"
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "L6's issuance coverage limb printed 'issuance coverage 12 of 12 cell(s) owned by the staged orders' and PASSED, and the decomposition's own invariant states 'every cell mirrors a manifest row, and every manifest row has at least one cell'.",
    "world_is": "Coverage by ID was total while coverage by CONTENT was not. The limb compares the union of <owned_cells> to the decomposition's cell ID SET, so a cell that owns a manifest row by id and cuts only PART of its content satisfies it completely -- and the mirror invariant is prose, which cannot fail. FWD-4 had no built artifact at the end of round 1 and nothing in the chain refused.",
    "notes": "DISARMED as an L4 ADDENDUM per rule 27's round-close path. NOT A REOPEN: RP-s-1 is terminal and its instance VALID, and 2.0.0_SA_COO~ZZ was right that reopening a certified cell is a rewind. THE STRUCTURAL FIX IS THE SPLIT, not a recut order -- a row serving TWO outcomes is precisely where a partial cut is invisible to an id-scoped check, so narrowing S1 to FWD-2 and giving the attribution limb its own id S13 closes this instance AND makes the class harder, and it retroactively makes RP-s-1 an EXACT mirror of the narrowed S1 so no completed work is graded deficient. THE ROUND-2 CELL FOR S13 IS 2.0.0_SA_COO~ZZ's IN ONE ISSUANCE and nothing here dispatches it. THE GENERAL SHAPE THAT LANE NAMED IS ACCEPTED AND IS WORTH MORE THAN THE INSTANCE: a coverage check scoped to the KEYS cannot see a defect in the VALUES -- rule 22's 'a check scoped to the members cannot see a defect in what the members share', one level down, on the MAPPING rather than the set. RECOMMENDED TO L5 AND NOT MANDATED (the decomp's contract is that lane's): cut one cell per (row, outcome) pair wherever a row names more than one. ALSO ACKNOWLEDGED from msg 20627: running surprise-row-gate.py against a WORKTREE file reports '0 new row(s)' because it grades HEAD, and that reads exactly like a clean pass -- only the commit-time run means anything, so this row's grading is taken from the commit and from no pre-commit run."
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
  },
  {
    "id": "NFRA_REPORT-Z-S4",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZZ",
    "surfaced_at": "2026-09-09T22:00:00Z",
    "one_line": "Disarms NFRA_REPORT-Z-W2-S4. The finding is ACCEPTED as measured: box-grain cost attribution is blocked by TWO causes independent of RP-s-5 -- resource-level Cost Explorer data is opt-in DISABLED at the payer account (get-cost-and-usage-with-resources returns AccessDeniedException, confirmed live), and the only active cost-allocation tags are segment-grain or a coarser System tag that groups up to 5 boxes, is null on 9 of 27 declared rows, and carries a bd-pipeline/BDPipeline casing drift.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_REPORT-Z-W2-S4"
    ],
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "0.9.0_WK_NFRA_REPORT~2's live reads at RP-s-9: aws ce get-cost-and-usage-with-resources -> AccessDeniedException; the active cost-allocation tag set enumerated and its coarseness/null-rate/casing-drift measured against the v1.1 EC2_MANIFEST.json's 27 declared rows.",
        "RP-s-9's delivered SEGMENT-grain detector is live and control-tested: (untagged), 45% of spend and the largest single line, sits at -4.5% and does NOT fire; inf (+639.6%) and bd (+37.3%) do. The control half is what the cell's own bound required and it holds.",
        "RP-s-5 (same worker, merged @42fcf408d1) discharged the INVENTORY half in full -- EC2 and ECS enumerated, machine_type/lifecycle split on all 27 rows -- so the residual blocker is demonstrably NOT the compute manifest the PRD's D3 named."
      ]
    },
    "spec_asserts": "PRD s.8 row S9 and TO-RP-s-9 BOUNDS: 'BOX grain CANNOT be computed until RP-s-5 lands, because the compute manifest is EC2-only with ECS absent entirely.' The stated blocker is the manifest.",
    "world_is": "RP-s-5 landed and the manifest blocker is discharged, yet box-grain dollars remain unreachable for two causes the PRD never named: an account-level Cost Explorer opt-in, and cost-allocation tag hygiene. D3's dependency was correctly stated and INCOMPLETE -- it named the blocker this project could clear and not the two it cannot.",
    "notes": "DISARMED TO INERT because the hazard was that an unreachable limb would be read as merely pending on a dependency that has since cleared -- a caveat outliving its cause, which is this project's own defect class. Recording it here removes that: the residual is now durable, attributed, and carried by 2.0.0_SA_COO~ZZ into the round-close slug to 1.0.0_SA_CTO~Z as a named limitation on FWD-8's box-grain limb. GRADUATED in the sense 1.0.0_SA_CTO~Z flagged at msg 20629 -- accepted and acted on, NOT an assertion that a CVO remediation row is owed. NOT FIXED HERE AND NOT THIS LANE'S TO FIX: enabling resource-level Cost Explorer is a payer-account billing setting and is Andrew's; the tag hygiene belongs to the owning infra lanes. FWD-8's SEGMENT limb is delivered and unaffected -- the outcome is not blocked, only its box-grain half."
  },
  {
    "id": "NFRA_REPORT-Z-W1-S1",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_REPORT~1",
    "surfaced_at": "2026-09-09T21:20:00Z",
    "one_line": "RP-s-7: comp-blast's served kuzu graph models NO edge at all between GOLD_SCRIPT nodes and Lambda/portal nodes -- confirmed by a positive-control FAILURE on a definitely-live lambda -- so a 'zero downstream consumers' or 'zero upstream gold: ancestor' result from comp-blast is not evidence for OR against C-DEPRECATED-TERMINUS, for ANY gold script in the estate, not only this cell's ten candidates.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-blast 'gold:B_01.holdings_lots' --direction downstream --json, 2026-09-09 ~21:0xZ: WITHIN BUDGET, scanned 164 of 164, 164 distinct ids returned, prefixes {gold:77, s3:87} -- ZERO ids of any other prefix (no lambda:, component:, jsx:, arn: node reached).",
        "REPEATED on 8 more gold scripts (B_02, A_03, INF_D_00, INF_D_04, INF_D_07, INF_D_03, INF_D_02b, INF_C_01, INF_D_00c) -- every single one returns ONLY gold:/s3: prefixed ids where non-zero, or ANSWER-STATE: PRESENT_WITH_ZERO_RESULTS (0 of 0 scanned) where zero -- including INF_D_00b.portal_timeseries.py, a script named for portal serving and NOT one of this cell's ten candidates, which ALSO returned PRESENT_WITH_ZERO_RESULTS.",
        "POSITIVE CONTROL, the discriminating read: comp-blast 'arn:aws:lambda:us-east-1:313476888478:function:inf-api-positions' --direction upstream --json, 2026-09-09 ~21:1xZ -- this lambda is independently known-live (it backs a served portal API route per infra/aws/lambda/inf-pipeline/inf-api-positions). Its upstream ancestor set in the SAME graph returns 14 ids, prefixes {system:2, motif:3, motifi:7, arn:1, event-source:1} -- ZERO gold: ancestors, even though this lambda demonstrably reads gold-layer output at runtime. The graph is blind to this edge type in EITHER direction, on a node proven to be alive, not merely on the ten candidates under test.",
        "the graph DOES model the client-facing layer generally (comp-blast 'component:AdvisorsTab.tsx' NOT-FOUND response prints the live node-type census: ReactComponent=442, JSXRender=1433, JSXElement=2205, GOLD_SCRIPT=1380, S3_DATA_KEY=294 -- so the blindness is a specific missing EDGE TYPE (GOLD_SCRIPT<->Lambda/ReactComponent), not an absent NODE population; the graph has both endpoints and no path recorded between them for gold-layer artifacts."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md rule 20 + the build ladder direct querying the estate's existing dependency graph (comp-blast/kuzu) rather than rebuilding one; this cell's bound C-DEPRECATED-TERMINUS requires walking the chain to a served artifact AND a rendered component, and the battery findings name no instrument gap.",
    "world_is": "The estate's own served graph cannot answer the gold-script-to-client-facing-terminus question at all via comp-blast, for any gold script, alive or dead -- proven by testing the mechanism against a node already known to be live rather than only against the candidates in question (Rule 22's ORDER: the check on the members alone would have certified the instrument clean). This cell routed around the gap using comp-pipescript's embedded 'PORTAL CONSUMERS' resolution and comp-platinum reverse instead (see DEPRECATION.md), which DO model this edge for the platinum/ key convention -- but comp-blast itself, the estate's general-purpose blast-radius tool, would silently return a false 'no consumers' for this entire edge class to any future caller who does not know to route around it the way this cell did.",
    "notes": "Not remediated -- fixing comp-blast's graph-build coverage for this edge type is outside this cell's paths and outside a report-lane cell's mandate entirely. Filed because the finding is ESTATE-WIDE (it would mislead any future C-DEPRECATED-TERMINUS-style determination, or any 'is this gold artifact safe to delete' blast-radius check, anywhere the graph is consulted) and not specific to NFRA_REPORT's ten candidates. ARMED because a future actor trusting a bare comp-blast zero-count on a GOLD_SCRIPT node, without the positive control run here, would draw a false deprecation or false safe-to-delete conclusion."
  },
  {
    "id": "NFRA_REPORT-Z-W1-S2",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_REPORT~1",
    "surfaced_at": "2026-09-09T21:21:00Z",
    "one_line": "RP-s-7: comp-pipescript's static WRITES parser misses dynamically-constructed S3 keys (prefix-variable concatenation, or a write routed through a helper function taking a computed key) -- producing a FALSE 'WRITES: (none detected)' for 2 of this cell's ten candidates, one of which (INF_C_01.canonical_nna.py) is textually a heavily-governed, actively-maintained production chokepoint, not a dead script.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-pipescript io INF_D_07.concentration_risk.py --pipeline inf-gold, 2026-09-09: prints 'WRITES: (none detected)'. comp-read data/inf/scripts/gold/INF_D_07.concentration_risk.py --for 'what does this script write, and to what S3 key' surfaces (AUTHORITATIVE, line 55): CONCENTRATION_RISK_KEY = OUTPUT_PREFIX + 'firm/concentration_risk.json', with OUTPUT_PREFIX defaulting to 'platinum/' (line 54) -- a real write key the static parser did not resolve because it is built by string concatenation of a module-level variable rather than a literal or f-string.",
        "comp-pipescript io INF_C_01.canonical_nna.py --pipeline inf-gold, 2026-09-09: also prints 'WRITES: (none detected)'. comp-read on the same file shows a _write_s3(df, key) helper (line 251-258) called with a key built by a separate _nna_key() function and an output-prefix guard _set_out_prefix() (lines 259-299) -- the write exists and is real, routed through two levels of indirection the static parser does not follow.",
        "INF_C_01.canonical_nna.py's own header comments (lines ~68-77, ~92, ~269, ~282, read via comp-read) describe it as part of an 'ATOMIC SET' with three guard libraries, a 'gold-dispatch chokepoint APPLIED + EXERCISED', 'NEVER#2 co-signed by CTO + COO', and a SERVE-RELEASE-ACK discipline -- textual, in-repo evidence of active, heavily-governed production status, the OPPOSITE of the 'looks deprecated' reading Andrew's ruling 6 offered for this artifact at hop 1.",
        "comp-platinum reverse 'platinum/firm/concentration_risk.json' --firm inf: PRODUCER field returns BLANK (the tool's own static write-index has no entry for this key at all, confirming the parser miss propagates downstream into the portal-reverse-lookup tool too, not only comp-pipescript's own io view)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "This cell's BOUNDS: 'a one-hop check said all ten candidate artifacts HAVE consumers; at the terminus it may say none do' -- the battery's own worked example assumes hop-1 OVER-reports aliveness relative to the terminus. This finding is the OPPOSITE miscalibration: the static tool UNDER-reports even the WRITE ITSELF for a script that is, by its own in-repo governance language, unambiguously alive.",
    "world_is": "comp-pipescript's static-analysis WRITES detector has a false-negative mode (dynamic key construction via concatenation or a key-building helper function) that is not specific to these two scripts -- any gold script in the estate using either pattern would read as writing nothing, which for a naive consumer of 'WRITES: (none detected)' reads identically to 'this script does nothing' and could recruit a future deprecation or decommissioning decision built on that silence.",
    "notes": "Not remediated -- fixing comp-pipescript's parser is outside this cell's paths. INF_C_01.canonical_nna.py is documented here as LIKELY ALIVE on textual/governance evidence, not as a terminus-walk PASS -- DEPRECATION.md renders it UNRESOLVED-BY-THIS-WALK rather than CHECKED, because this cell's own instrument could not independently confirm the write reaches a served terminus (only that it writes at all)."
  },
  {
    "id": "NFRA_REPORT-Z-W1-S3",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_REPORT~1",
    "surfaced_at": "2026-09-09T22:15:00Z",
    "one_line": "RP-s-11's AC1 invocation as literally written -- 'bash .tools/comp-find . --corpus aws IAM_ROLE --limit 5' -- fails rc=2 with a bash syntax error, because .tools/comp-find is a Python script (shebang #!/usr/bin/env python3), not a bash script; the working form is the shimmed 'comp-find' or 'python .tools/comp-find'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~ZZ",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "timeout 120 bash .tools/comp-find '.' --corpus aws IAM_ROLE --limit 5, run 2026-09-09 this session -> rc=2, '.tools/comp-find: line 5: ...: command not found' / 'line 6: syntax error near unexpected token (' -- bash attempting to interpret Python source as shell script.",
        "file .tools/comp-find -> 'Python script, ASCII text executable'; head -c 300 shows '#!/usr/bin/env python3'.",
        "The corrected, functionally-identical invocation 'comp-find . --corpus aws IAM_ROLE --limit 5' (using the ~/bin/comp-find forwarder, per CLAUDE.md's shim mechanism) run the same session -> rc=0, VINTAGE line present with a real UTC timestamp, DENOMINATOR: 219 hit(s) across 219 aws node(s) [types=IAM_ROLE] -- the substantive result AC1 is actually testing for."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RP-s-11's AC1: <invocation>bash .tools/comp-find '.' --corpus aws IAM_ROLE --limit 5</invocation>, expecting output containing VINTEAGE plus a date.",
    "world_is": "The literal invocation cannot produce the named result under any circumstance -- it is a shell/interpreter mismatch, not a data-dependent failure -- so running it verbatim always yields a syntax error regardless of the live AWS plane's state. The tool itself (comp-find) works correctly and does carry a real vintage when invoked correctly, which is what this cell's proof instance records as the substantive AC1 evidence.",
    "notes": "INERT and narrow -- a one-TO authoring typo (a stray 'bash ' prefix on a Python script path), not an estate-wide tool defect; comp-find itself is unaffected. Not remediated by this cell: editing the TO's own proof_of_spec text is not in this cell's paths and the round's decomposition/TOs are frozen mid-round per rule 27. Filed per the general Surprise trigger ('an invocation does not produce the named result') rather than silently substituting the corrected form without a citable record of the discrepancy."
  },
  {
    "id": "NFRA_REPORT-Z-W1-S4",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_REPORT~1",
    "surfaced_at": "2026-09-09T22:16:00Z",
    "one_line": "RP-s-11: two live, UNDECLARED API Gateways -- including one named 'trade-submission-api' -- and one live, DECLARED CloudFront distribution match ZERO of the estate's 51 CloudWatch alarms by name/ID/dimension, positive-controlled against siblings that DO match (session-analytics-api: 4 alarms; the other CloudFront distribution: 3 alarms via a structural DistributionId dimension match).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-find '.' --corpus aws API_GW --all, 2026-09-09: 5 of 5 API_GW nodes, DRIFT DECLARED=2 LIVE-no-DECLARED=3 -- the 3 undeclared are opal-session-analytics-api, sentiment-query-api, trade-submission-api.",
        "comp-find 'trade-submission|w8jnzvs21g' --corpus aws CW_ALARM --all -> 0 of 51 hits. comp-find 'sentiment-query|cxm5b58nme' --corpus aws CW_ALARM --all -> 0 of 51 hits. comp-find 'session-analytics|f7lvfv4bjc' --corpus aws CW_ALARM --all -> 4 of 51 hits (opal-session-analytics-errors/estimated-monthly-cost/high-invocations/throttles) -- the positive control proving the 51-alarm sweep and the name/ID match method can and does return non-zero when a real match exists.",
        "comp-find '.' --corpus aws CLOUDFRONT_DISTRIBUTION --all -> 2 of 2 distributions, both DECLARED: E1DHJH4Y1W8YC2 (aliases: [], target_origin wp-origin) and EVTSA9VEHNZVH (aliases: opalinvest.dev, www.opalinvest.dev). comp-find 'DistributionId' --corpus aws CW_ALARM --all -> exactly 3 of 51 alarms carry a DistributionId dimension, ALL THREE = EVTSA9VEHNZVH (cloudfront-high-error-rate, cloudfront-high-origin-latency, cloudfront-low-cache-hit-rate). comp-find 'E1DHJH4Y1W8YC2' --corpus aws CW_ALARM --all -> 0 of 51 hits, structurally, not by weaker name-substring: NO alarm's DistributionId, name, or ARN mentions it at all.",
        "This is the SAME 51-alarm population NFRA_OPSEC202609-Z-S151 and this project's own ALERT_DELIVERY.md (RP-s-6) already swept for a DIFFERENT question (delivery-leg confirmation on alarms that exist); this row is upstream of that one -- it asks whether an ALARM EXISTS AT ALL for a given served surface, not whether an existing alarm's delivery works."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RP-s-11's ACT: 'make it findable what we put in front of people that nobody is checking at all... a part of the business with nothing watching it must look DIFFERENT from one that is watched and healthy.'",
    "world_is": "trade-submission-api and sentiment-query-api are live, reachable API Gateway endpoints with no Terraform declaration and, on this sweep, no matching CloudWatch alarm of any kind -- the same evidentiary shape (positive-controlled zero, against a sibling surface that does match) that this project's own STATE_MODEL.md renders as the not-CHECKED family. E1DHJH4Y1W8YC2 is a declared, live CloudFront distribution with zero alarms by the SAME structural dimension that finds its sibling three times over. None of the three is a proof that nothing IS wrong with them; each is a measured absence of any instrument that would tell anyone if something were.",
    "notes": "ARMED specifically because of trade-submission-api's name and undeclared status -- a live, unmonitored, untracked surface named for a financially consequential function is exactly the class of risk a reader of this report needs surfaced, not buried in a deliverable prose paragraph. Declared method limit, named rather than hidden: the API-gateway matches are NAME/ID SUBSTRING searches over whatever comp-find's aws corpus indexes (alarm name, ARN, a truncated JSON excerpt) -- weaker evidence than the CloudFront case's exact DistributionId dimension match, because an alarm targeting the same underlying Lambda under an unrelated name would be missed by this method. Not remediated here: this project's standing alerting/monitor moratorium forbids minting a new alarm from any cell, and disarm_owner is set to the sovereign-adjacent seat that can decide whether this is escalated to Andrew directly rather than carried only in a report row."
  },
  {
    "id": "NFRA_REPORT-Z-S5",
    "adjudicates": [
      "NFRA_REPORT-Z-W1-S1"
    ],
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~Z",
    "surfaced_at": "2026-09-09T23:20:00Z",
    "one_line": "DISARM of NFRA_REPORT-Z-W1-S1 by its named disarm_owner: comp-blast's missing GOLD_SCRIPT->Lambda/ReactComponent edge is CONFIRMED estate-wide and is now a citable recorded limit at org/modules/graph/INSTRUMENT_LIMITS.md. The HAZARD is disarmed; the GRAPH IS NOT FIXED and the row says so.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The row's own measurements are ACCEPTED and deliberately NOT re-run -- re-running a peer's instrument is repetition, not corroboration (CLAUDE.md rule 22). Its positive control is what makes it decisive: comp-blast on arn:aws:lambda:...:function:inf-api-positions --direction upstream, a lambda INDEPENDENTLY known live because it backs a served portal API route, FAILED in the same graph. The instrument is blind, not the candidates.",
        "And the blindness is a MISSING EDGE TYPE rather than absent nodes: comp-blast 'component:AdvisorsTab.tsx' prints the live node-type census ReactComponent=442, JSXRender=1433, JSXElement=2205, GOLD_SCRIPT=1380, S3_DATA_KEY=294. Both endpoint families are modelled; the edge between them is not.",
        "COVERAGE of the row's own sweep: 10 gold scripts, every one returning only gold:/s3: prefixes where non-zero, including INF_D_00b.portal_timeseries.py -- a script named for the portal it serves.",
        "org/modules/graph/INSTRUMENT_LIMITS.md (this act) records the limit, its positive control, and the route around it that TO-RP-s-7 actually used (comp-pipescript's PORTAL CONSUMERS resolution + comp-platinum reverse, which DO model this edge for the platinum/ key convention)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "CLAUDE.md rule 20 and the build ladder direct callers to QUERY the estate's existing dependency graph rather than rebuild one, and TO-RP-s-7's battery findings named no instrument gap.",
    "world_is": "For the GOLD_SCRIPT-to-client-facing-terminus question comp-blast returns a silent false negative for the entire edge class, for any gold script, alive or dead. A caller who does not know to route around it -- as this cell did -- reads 'no consumers' as evidence of death.",
    "notes": "DISARMED, and the disarm is precisely scoped: THE HAZARD was that a future caller reads a comp-blast zero as evidence for or against deprecation. That is closed by a findable, citable record at the module the instrument lives in, cited from this row. THE GRAPH IS NOT FIXED -- no GOLD_SCRIPT->Lambda/ReactComponent edge is modelled today, repairing it is comp-tool build-lane work owned by 1.0.0_SA_CTO~Z, and it is SIZED AND NOT DONE. A document warning about a gap is not a graph that models the edge and must never be cited as though the instrument improved. A STRONGER CARRIER WAS DELIBERATELY NOT TAKEN: a one-line stderr banner in .tools/comp-blast would reach the callers who never open the doc, which is the whole population at risk, but it changes a shared tool's OUTPUT and anything parsing that stderr is an unmeasured consumer set -- that is the right next act and it needs its own measurement rather than a same-turn edit. TO-RP-s-7 IS NOT INVALIDATED: the cell found the gap while GROUNDING a claim, declared it, routed around it, and treated every unresolved candidate as NOT deprecated. Discovering an instrument's blindness is the cell working, not failing."
  },
  {
    "id": "NFRA_REPORT-Z-S6",
    "adjudicates": [
      "NFRA_REPORT-Z-W1-S2"
    ],
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~Z",
    "surfaced_at": "2026-09-09T23:21:00Z",
    "one_line": "DISARM of NFRA_REPORT-Z-W1-S2 by its named disarm_owner: comp-pipescript's static WRITES parser misses dynamically-constructed S3 keys, CONFIRMED as a two-pattern false-negative class that PROPAGATES into comp-platinum reverse. Recorded at org/modules/graph/INSTRUMENT_LIMITS.md; the PARSER IS NOT FIXED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The row's measurements are ACCEPTED and not re-run. TWO confirmed instances, each with the write located at file:line: INF_D_07.concentration_risk.py:55 builds its key by PREFIX-VARIABLE CONCATENATION; INF_C_01.canonical_nna.py writes through a _write_s3(df, key) helper (251-258) with the key built by a separate _nna_key() plus an output-prefix guard (259-299). Both print 'WRITES: (none detected)'.",
        "THE PROPAGATION IS THE SHARPEST PART AND IT DEFEATS CROSS-TOOL AGREEMENT: comp-platinum reverse 'platinum/firm/concentration_risk.json' --firm inf returns a BLANK PRODUCER, because the same static write-index has no entry for the key. Two tools, ONE parser -- so agreement between them is not corroboration (CLAUDE.md rule 22: a second seat's confirmation via the FIRST seat's method is repetition).",
        "AND THE FALSE NEGATIVE LANDS ON THE MOST GOVERNED SCRIPT IN THE SAMPLE: INF_C_01's own header comments describe an 'ATOMIC SET' with three guard libraries, a 'gold-dispatch chokepoint APPLIED + EXERCISED', a 'NEVER#2 co-signed by CTO + COO' and a SERVE-RELEASE-ACK discipline. The tool reports it as writing nothing.",
        "org/modules/graph/INSTRUMENT_LIMITS.md (this act) records both patterns so a reader can check by hand: (a) key built by concatenating a prefix variable; (b) write routed through a helper receiving a computed key."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "TO-RP-s-7's BOUNDS anticipated the OPPOSITE miscalibration -- that a one-hop check would OVER-report aliveness relative to the terminus.",
    "world_is": "The static parser UNDER-reports the WRITE ITSELF, so a script that is unambiguously alive by its own in-repo governance language reads as writing nothing. For a naive consumer 'WRITES: (none detected)' is indistinguishable from 'this script does nothing', which is a sentence a decommissioning decision acts on.",
    "notes": "DISARMED on the same scoping as Z-S5: the HAZARD (a false zero recruited into a deprecation or decommissioning decision) is closed by a citable record naming both patterns; THE PARSER IS NOT FIXED and that is comp-tool build-lane work owned by 1.0.0_SA_CTO~Z, sized and not done. WORTH KEEPING BEYOND THIS ROW: the battery's own worked example predicted an OVER-report and the world produced an UNDER-report, which is why the cell caught it -- it checked the direction its bound did NOT warn about. Testing only the direction a spec anticipates leaves its mirror open."
  },
  {
    "id": "NFRA_REPORT-Z-S7",
    "adjudicates": [
      "NFRA_REPORT-Z-W1-S4"
    ],
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~Z",
    "surfaced_at": "2026-09-09T23:22:00Z",
    "one_line": "DISARM of NFRA_REPORT-Z-W1-S4 by its named disarm_owner, and the substance is BIGGER than the row could see: trade-submission-api is a LIVE, PORTAL-CONSUMED trade submission AND APPROVAL workflow whose 7 lambdas, DynamoDB table, S3 bucket and IAM role are ALL DECLARED while the API GATEWAY ITSELF is LIVE-no-DECLARED -- and a SECOND, DECLARED front door reaches the same handler. NOTHING WAS BUILT; the monitoring question is an open call at Andrew.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The row's own alarm sweep is ACCEPTED and not re-run; its positive controls are what make the zeros evidence (session-analytics-api matches 4 of 51 alarms; the sibling CloudFront distribution matches 3 by a structural DistributionId dimension).",
        "1.0.0_SA_CTO~Z live read, comp-find 'trade-submission|w8jnzvs21g' --corpus aws --all, VINTAGE 2026-09-09 21:05:17 UTC (stitch-codebuild built 19:55:00Z, manifest 09be45b5ff92), DENOMINATOR 32 hits across 2530 aws nodes: API_GW trade-submission-api drift=LIVE-no-DECLARED with SEVEN routes -- POST /submit, POST /workflow, POST /auth, GET /submissions, GET /submissions/{proxy+}, GET /submissions/{submission_id}/excel, GET /users.",
        "EVERY COMPONENT BEHIND THE DOOR IS DECLARED: 7 lambdas (trade-submission-handler, trade-workflow-handler, trade-auth-handler, trade-authorizer, trade-dashboard-api, trade-identifier-cache, trade-parquet-batch-export), DynamoDB opal-trade-submissions, S3 opal-data-trade-submissions, IAM role trade-submission-lambda-role with 2 inline policies. The asymmetry IS the finding: a fully Terraform-managed trade path whose front door is not in Terraform.",
        "TWO FRONT DOORS TO THE SAME HANDLER: a DECLARED route POST /api/general/trades/submit on a DIFFERENT api (7k3ed8px20, owner_pipeline shared-infra, tf-managed) integrates the SAME trade-submission-handler. Only the declared side is visible to any Terraform-plane drift check.",
        "THE CONSUMER IS THE PORTAL: portal/src/api/endpoints/trade-submission.ts carries 10 functions incl. submitTrade, approveSubmission, rejectSubmission, executeSubmission, downloadExcelFile -- so this is not an abandoned endpoint."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "TO-RP-s-11's cell asks whether an instrument covers each served surface; the row asks whether an ALARM EXISTS AT ALL, upstream of NFRA_OPSEC202609-Z-S151's delivery-leg question on alarms that already exist.",
    "world_is": "Three live surfaces match zero of 51 alarms, positive-controlled. And the largest of them is not archaeological: it is a live, portal-consumed trade submission and approval workflow, fully declared behind an undeclared front door, reachable through a second declared door as well.",
    "notes": "DISARMED AS A RECORDED FINDING, NOT AS A REPAIR. WHAT WAS DELIBERATELY NOT DONE: nothing was built. The standing moratorium forbids minting any alert, alarm, monitor or notification without Andrew's explicit word, so the remedy is NOT 'add alarms' -- it is this record plus a sovereign call, which is carried to Andrew in the same turn rather than waiting on a drain. WHAT THIS ROW DOES NOT CLAIM, because a trade-named finding is exactly where overstating would do damage: NO REQUEST LOGS WERE READ, so nothing here shows the undeclared door is RECEIVING TRAFFIC -- only that it is live, wired and consumed by portal code. And POST /auth carrying authorization NONE while the other six carry CUSTOM + authorizer nfa51m is NORMAL for a login endpoint and is NOT offered as a defect; it is named only so its absence from the finding list is not later read as a missed check. THE OPEN CALL AT ANDREW: whether to declare the gateway in Terraform (a change with a blast radius on a live trade path), whether to consolidate the two front doors, and whether any monitoring is authorized at all. RP-s-11 IS DOING EXACTLY WHAT FWD-11 COMMISSIONED: the monitored-vs-served reconciler found a served surface no instrument covers on its first real pass, and found it because the cell was told to ask that question -- RP-s-6 swept the SAME 51-alarm population for a different question and could not have seen it."
  },
  {
    "id": "NFRA_REPORT-Z-W2-S5",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_REPORT~2",
    "surfaced_at": "2026-09-10T01:19:20Z",
    "one_line": "RP-s-13's own issued BOUNDS named canonical-schwab-si2 as still-ungrouped and told this cell to render it UNGROUPED, but the PRD was amended to v0.6 before this build folding Andrew's direct ruling that si2 belongs to Dashboard and stating explicitly that no cell may render it ungrouped; ATTRIBUTION.md is built against the live v0.6 text, not the stale BOUNDS.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md@1aae9c43fe, section 6 (Rulings that BIND), verbatim: 'THE canonical-schwab-si2 HALF IS RULED AND CLOSED -- Andrew-direct 2026-09-09 ~22:3xZ, VERBATIM: \\\"I would include si2 under the Dashboard.\\\" It is no longer an ungrouped surface and no cell may render it so.'",
        "org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md@1aae9c43fe, section 8, S13 manifest row, verbatim: 'Live surface still ungrouped: opal-gateway ... canonical-schwab-si2 is RULED into Dashboard (Andrew-direct 2026-09-09 ~22:3xZ) and is NO LONGER an ungrouped example.'",
        "org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-13.attribution-axis-and-ungrouped.md (this cell's own issued BOUNDS, worker-face copy): 'Two live surfaces are known to have no ratified group today: opal-gateway and canonical-schwab-si2. Render them UNGROUPED rather than assigning them.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RP-s-13's BOUNDS: 'Two live surfaces are known to have no ratified group today: opal-gateway and canonical-schwab-si2. Render them UNGROUPED rather than assigning them.'",
    "world_is": "The PRD this cell also depends on (NFRA_REPORT_PRD.md) was bumped to v0.6 folding a later Andrew-direct ruling that canonical-schwab-si2 is attributed to Dashboard, and states in its own words that no cell may render it ungrouped. Only opal-gateway remains a live surface with no ratified group as of this build.",
    "notes": "NOT a defect in the decomposition or the issuer's process -- the PRD amendment (v0.4 to v0.6) landed on the SAME 2026-09-09 session this cell was issued in, and this is the ordinary case of a cell re-grounding its premises against live state before building rather than against the text frozen at issuance. ATTRIBUTION.md (this cell's deliverable) renders canonical-schwab-si2 attributed to Dashboard and renders opal-gateway UNGROUPED, per the live PRD. Nothing here is ARMED: the correct answer is already ruled and cited, and no future actor needs to disarm anything -- this row exists so a reader of the BOUNDS text alone is not misled into thinking si2 should still render UNGROUPED."
  },
  {
    "id": "NFRA_REPORT-Z-S8",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZZ",
    "surfaced_at": "2026-09-10T02:17:34Z",
    "one_line": "ALL SEVEN round-2 task orders name deliverables/0.9.0_WK_NFRA_REPORT~1/ as the deliverable folder and inside every criterion invocation, regardless of which worker serial <issued_to> names -- so RP-s-13 (issued to ~2) and RP-s-14 (issued to ~3) both wrote into a folder named for ~1, and the deliverables tree no longer identifies which worker produced which artifact.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Measured at 2026-09-10T02:1xZ by parsing all 7 round-2 order files: <issued_to> is ~1 for RP-s-15/16/18, ~2 for RP-s-13/19, ~3 for RP-s-14/17 -- while the set of deliverables/0.9.0_WK_NFRA_REPORT~<n>/ paths referenced in each file is {~1} for all 7 of 7.",
        "org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-13.attribution-axis-and-ungrouped.md: <issued_to>0.9.0_WK_NFRA_REPORT~2</issued_to> with all three criteria invoking against deliverables/0.9.0_WK_NFRA_REPORT~1/ATTRIBUTION.md.",
        "Landed artifacts at merge 63efc53452 (RP-s-13, worker ~2) and c2a582b17d (RP-s-14, worker ~3) both sit under deliverables/0.9.0_WK_NFRA_REPORT~1/."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The /dispatch L6 cut treats deliverables/<serial>/ as the per-worker write surface the tree convention grants WITHOUT an explicit <paths> entry -- i.e. the folder name identifies the worker that authored what is in it.",
    "world_is": "The folder name identifies the SLOT THE ISSUER HAPPENED TO WRITE FIRST, not the author. Two of two drained round-2 cells have already landed deliverables under a serial that did not produce them. No worker was ever REFUSED, because each order's <paths> grants 'org/missions/D12/NFRA/NFRA_REPORT/deliverables/' as a directory prefix rather than a per-serial folder -- so the wide grant is exactly what kept a record defect from surfacing as a lane refusal.",
    "notes": "THE MECHANISM IS THE POINT AND IT IS RULE 22'S SHARED-DEPENDENCY CLAUSE: all seven orders were emitted by ONE generator, so the defect lives in what the members SHARE. Every per-order check passed -- gate, coverage, criterion grammar, proof-of-spec on two drained cells -- because each arm was scoped to a member. It was found only by asking what the members have in common and reading <issued_to> against the deliverable path ACROSS the set. NOT REMEDIATED MID-ROUND, deliberately: mid-round the issuance is FROZEN, RP-s-14 is already merged with its criteria pinned to the ~1 path, and rewriting the five open orders would split one round across two conventions and invalidate a merged cell's criteria. The harm is record attribution only -- no worker is blocked and no criterion mis-grades -- so the correct act is a row now and a fix at the next cut, not a mid-round edit. Round 3's cut derives the deliverable folder FROM <issued_to> instead of from a literal."
  },
  {
    "id": "NFRA_REPORT-Z-W2-S6",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_REPORT~2",
    "surfaced_at": "2026-09-10T02:32:00Z",
    "one_line": "RP-s-19 grounding (ANOMALY_IN_EDITION.md, row opal-infrastructure-alerts): comp-blast's SNS-topic downstream check extracts Lambda and SQS protocol subscriber edges (positive-controlled on two other topics) but never models a raw phone-number/email endpoint as a node -- so a topic whose ENTIRE live subscriber set is SMS/email renders PHANTOM-CONSUMER identically whether that endpoint is healthy, broken or genuinely absent, and this edition's own BREACH row is exactly that case.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.9.0_WK_NFRA_REPORT~2",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-blast 'arn:aws:sns:us-east-1:313476888478:opal-infrastructure-alerts' --direction downstream --check-consumers, run this session: WITHIN BUDGET, scanned 0 of 0 traversal, PHANTOM-CONSUMER rc=4 -- 'zero dependents IN GRAPH (both directions)' -- while the same node's --direction both --json call, same session, returns 70 of 70 consumers (24 CW_ALARM, 5 LAMBDA, 2 EVENT_RULE, 2 EVENT_SOURCE, 1 C3System, 36 C2Motif) EVERY ONE at direction=upstream (feeds the topic); zero of 70 at direction=downstream (reads the topic).",
        "POSITIVE CONTROL 1: comp-blast 'inf-otp-alert' --direction downstream --check-consumers, same session -- CONSUMER-OK, 8 of 8 dependents, including LAMBDA node inf-ec2-retry-launch at direction=downstream. ALERT_DELIVERY.md sec.1 (RP-s-6, QUOTED) records this same topic's confirmed subscriptions as exactly 'lambda, sms' -- so the Lambda-protocol leg IS extracted as a downstream edge when one exists; the tool is not broadly blind to SNS subscriptions.",
        "POSITIVE CONTROL 2: comp-blast 'opal-critical-surface-alerts' --direction downstream --check-consumers, same session -- CONSUMER-OK, 1 of 1 dependent, SQS_QUEUE opal-critical-surface-alerts-coo at direction=downstream, matching ALERT_DELIVERY.md sec.1's 'sqs, sms' confirmed pair for this topic -- the SQS protocol leg is also extracted.",
        "ALERT_DELIVERY.md sec.4 (RP-s-6, this worktree, QUOTED, live AWS read not this graph): opal-infrastructure-alerts' one confirmed SNS subscription is protocol sms, endpoint +17862617679, sandbox status Pending (registered, not Verified) -- a real subscriber exists and is independently shown non-functional by a live call, entirely outside what comp-blast's graph can see either way."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RP-s-19's battery findings: 'ROUND 1 ESTABLISHED TWO INSTRUMENT LIMITS THAT BIND THIS CELL HARDER THAN ANY OTHER ... A breakdown built on an enumerator blind to a whole edge class renders confident, complete-looking and wrong, and a missing EDGE leaves no gap a reader can see. Carry a per-row \"what this query cannot see\" limb.'",
    "world_is": "A THIRD instrument limit of the identical shape (a false zero and a true zero read identically), on an edge/node class neither LIMIT 1 nor LIMIT 2 in org/modules/graph/INSTRUMENT_LIMITS.md names: comp-blast's graph never models a raw SNS destination endpoint (phone number, email) as a node at all -- only Lambda/SQS/etc. protocol targets are graph-typed and extractable. PHANTOM-CONSUMER on an SNS topic is therefore evidence of 'no GRAPH-TYPED subscriber,' never evidence of 'no subscriber.' This generalizes past opal-infrastructure-alerts to any current or future topic whose entire live subscriber set is SMS/email.",
    "notes": "DISARMED THIS TURN, not deferred: LIMIT 3 appended to org/modules/graph/INSTRUMENT_LIMITS.md (the same file LIMIT 1/LIMIT 2 already live in, and a path this cell's task order names) in this same commit, citing the two positive controls above, so a future caller reading that file before treating a comp-blast SNS PHANTOM-CONSUMER zero as an orphan-safe signal is not misled. NOT remediated -- fixing comp-blast's graph-build coverage for raw-endpoint subscriber nodes is comp-tool build-lane work, outside this cell's paths and mandate, exactly as LIMIT 1/LIMIT 2 were left NOT FIXED. Does not weaken ANOMALY_IN_EDITION.md's own central finding: opal-infrastructure-alerts' non-delivery is established by ALERT_DELIVERY.md's live AWS read (RP-s-6), never by this graph's zero -- the limit means the graph's zero cannot be cited as CORROBORATION of that finding, not that the finding is wrong."
  },
  {
    "id": "NFRA_REPORT-Z-S9",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZZ",
    "surfaced_at": "2026-09-10T02:52:00Z",
    "one_line": "NFRA_REPORT HAS NO ledger/ DIRECTORY AT ALL. The spine's L10 names three ledger artifacts for a project -- ROUND_ANALYSIS.round<N>.md (CTO), COMPLETION_REPORT.round<N>.json (COO) and COMPLETION_GRADES.round<N>.json (CTO) -- and none exists here. Round 1's round-N analysis was written to the CTO's own deliverables instead, and surprise-channel/remediations/ is EMPTY, so round 1's remediation document (the CVO's one artifact of the round, per spine L10) was never written either.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~ZZ",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md at site-Z HEAD, L10 section: 'the CTO writes ledger/ROUND_ANALYSIS.round<N>.md'; '2.0.0_SA_COO ... writes ledger/COMPLETION_REPORT.round<N>.json'; '1.0.0_SA_CTO ... writes ledger/COMPLETION_GRADES.round<N>.json'; 'The CVO writes the round's remediation document, the one artifact of the round'.",
        "Measured over the tracked corpus (denominator: 31000 tracked files, git ls-files): ROUND_ANALYSIS 7 hits, all under NFRA_CLDGRPH/ledger (3), NFRA_COMPEFFICACY/ledger (1) and NFRA_OUTSET/ledger (2) -- ZERO under NFRA_REPORT. COMPLETION_REPORT 7 hits (one is the schema at org/standards/) -- ZERO under NFRA_REPORT. COMPLETION_GRADES 3 hits -- ZERO under NFRA_REPORT.",
        "org/missions/D12/NFRA/NFRA_REPORT/ directory listing: decompositions/, deliverables/, prd/, project.json, surprise-channel/, task-orders/ -- no ledger/.",
        "org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/remediations/ is an existing but EMPTY directory.",
        "org/standards/COMPLETION_REPORT.schema.json EXISTS (11023 bytes), so the contract the COO limb writes against is present and this is not a missing-contract problem."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Spine L10 gives this project three ledger artifacts and one remediation document, and rule 27 as amended at f5355fcfc4 states that CLOSED requires COMPLETION_REPORT + COMPLETION_GRADES with every grade REALIZED -- a round is not closed because every FWD reads REALIZED somewhere.",
    "world_is": "None of the four artifacts exists for this project at any round. Three sibling tree projects carry the ledger/ shape, so this is a per-project gap rather than an estate-wide convention difference -- which is what the sibling denominator establishes and a project-scoped check could not have.",
    "notes": "THREE LIMBS, THREE OWNERS, AND THIS ROW DOES NOT ADJUDICATE THE TWO THAT ARE NOT THIS LANE'S. (a) COMPLETION_REPORT.round<N>.json is the COO's and is NOT YET OWED -- round 2 reads 5 of 7 terminal, and the spine conditions that artifact on the decomposition being SPENT (every cell holding a terminal task order with a valid proof-of-spec). This lane writes it, creating ledger/, when the seventh order goes terminal; that is the disarm. (b) ROUND_ANALYSIS and COMPLETION_GRADES are 1.0.0_SA_CTO~Z's. (c) The round's remediation document is 3.0.0_SA_CVO~Z's. Round 1 was RECUT rather than CLOSED, so its missing COMPLETION_REPORT may be correct by design -- but NFRA_OUTSET carries ROUND_ANALYSIS for both round 1 and round 2, so a recut round does produce one there, and that is the comparison this row rests on rather than an inference about intent. SURFACED, NOT CHASED: this lane does not write another seat's ledger artifact, and CLAUDE.md's no-inferred-gates clause means this row is not a hold on anyone -- round 2 proceeds to its close regardless."
  },
  {
    "id": "NFRA_REPORT-Z-W1-S5",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_REPORT~1",
    "surfaced_at": "2026-09-10T02:40:00Z",
    "one_line": "RP-s-16: the comp-rail (comp-find/comp-read/comp-which) resolves its search corpus by the TOOL SCRIPT'S OWN on-disk location, not the caller's cwd -- every invocation from inside a linked worktree (rule 14b's mandated pattern) silently scans the MAIN ajb_workspace checkout instead, with no error and no warning that the corpus excludes the worktree the worker is standing in.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "~/bin/comp-find:16 and ~/bin/comp-read:16, read this session: both forwarders hardcode _t=\"/c/Users/Opal Bloomberg/Desktop/ajb_workspace/.tools/comp-<tool>\" and exec it verbatim regardless of the invoking shell's cwd or which worktree it sits in.",
        ".tools/comp-find@1443d20f78:77 'WS = _comprail.repo_root()'; .tools/_comprail.py@1443d20f78:125-128 'def repo_root(): ... subprocess.run([\"git\", \"rev-parse\", \"--show-toplevel\"], cwd=_HERE, ...)' where _HERE is os.path.dirname(os.path.abspath(__file__)) of the SCRIPT ITSELF -- never PWD, never the caller's cwd, so repo_root() always resolves to whichever tree the shim's hardcoded _t points at.",
        "EMPIRICAL, this worktree (C:/Users/Opal Bloomberg/Desktop/wk-NR2-1, branch wk-NR2-1, HEAD 1443d20f78): wrote an untracked canary file inside this cell's OWN write surface (org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/.canary_grain_test.md) carrying a unique token; comp-find '<token>' (default corpus=all) returned 'DENOMINATOR: 0 hit(s) across 53245 file(s) scanned' -- a MEASURED zero that never covered this worktree's own new file. File removed after the test, never committed.",
        "Re-run at --corpus raw (the maximal scope, 501365 files scanned): still 0 hits on the canary's actual content. The only 2 hits returned there were comp-find's OWN telemetry echo of the search TERM as a logged invocation argument (org/mcp/comp-tool-runs.jsonl:6535, org/mcp/comp-which-rail.log:6518) -- and org/mcp/inbox/, org/mcp/comp-tool-runs.jsonl and org/mcp/comp-which-rail.log do not exist under this worktree at all (confirmed by direct ls of org/mcp/ here), so those two hits could only have come from the MAIN tree's disk. The corpus scanned was never this worktree's, at any width."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md rule 21: 'a comp-tool is the DEFAULT for search + inspection, raw grep the exception' -- the reflex for wherever an agent is working; rule 14b mandates a worker commit and edit inside its OWN linked worktree ('a linked worktree carries its OWN index... which is why /dispatch already mandates one per worker slot').",
    "world_is": "The two mandates combine into a silent GRAIN mismatch: a worker in a linked worktree who follows rule 21's reflex gets comp-find/comp-read/comp-which answers about the MAIN ajb_workspace checkout's disk state, never about its own worktree's uncommitted or worktree-local content -- and the tool's own output ('a MEASURED zero... not a claim the term is absent from the estate') reads as authoritative with no signal that the corpus excluded the very tree the worker is standing in.",
    "notes": "Not remediated here -- .tools/_comprail.py and the ~/bin shims are outside this cell's paths entirely. Filed ARMED because every other worktree active this session (ajb_s10_v, wk-NR2-2, wk-NR2-3) inherits the identical defect on every comp-find/comp-read/comp-which call it makes, and a future worker trusting a comp-rail zero about its own uncommitted deliverable would be citing the wrong tree's content while the tool's own denominator language gives no hint of that. This cell's own earlier reads of SCHEDULE.md/PRD.md/COMPOSER.md via comp-read returned correct text only because those are tracked files unchanged since this worktree's branch point and so are byte-identical in both trees by coincidence, not because comp-read was reading this worktree -- which is exactly why the mismatch went unnoticed until tested with a canary unique to this worktree."
  },
  {
    "id": "NFRA_REPORT-Z-S10",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZZ",
    "surfaced_at": "2026-09-10T03:10:00Z",
    "one_line": "RP-s-13's MERGED deliverable ATTRIBUTION.md renders both `opal-gateway` and `opal-globgrph` as UNGROUPED, which was correct when it was built and is STALE as of PRD v0.7: Andrew-direct settled FWD-4's axis at FOUR members (Dashboard | Website | Gateway | Graph), and those two surfaces are the referents of the two new members. FWD-4 cannot grade REALIZED against the v0.7 bar while its own deliverable renders two NAMED members as ungrouped.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~ZZ",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/ATTRIBUTION.md at site-Z HEAD, parsed by row: `opal-gateway` (MCP server) -> `UNGROUPED`; `opal-globgrph` (ECS Fargate cluster) -> `UNGROUPED`. 2 of 2 of the rows the ruling moves.",
        "org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md at site-Z HEAD, line 13: \"attribution axis has FOUR MEMBERS -- `Dashboard | Website | Gateway | Graph`\" (Andrew-direct).",
        "Same PRD, line 295, naming the referent explicitly rather than leaving it to inference: \"Website, Gateway (the opal-gateway MCP server)\".",
        "Same PRD, lines 327-328, the four-member reasoning: \"`opal-gateway` (EC2, the MCP server) and `opal-globgrph` (ECS, 3 of 3 services) are BOTH live, BOTH always-on, and FAIL DIFFERENTLY\" -- which is why neither folds into Dashboard and why Graph's referent is opal-globgrph.",
        "1.0.0_SA_CTO~Z msg 20761 carrying the Andrew-direct at record 9382d107a3: \"UNGROUPED IS NOT RETIRED. It now means a live surface outside all four.\""
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S13/FWD-4 requires every finding rolled up to a NAMED part of the business with an owner, plus a mandatory RENDERED UNGROUPED value for a live surface no ratified member covers. Under v0.7 the ratified members are four, so UNGROUPED is a strictly smaller set than it was at v0.6.",
    "world_is": "The deliverable was built against the v0.6 axis, where the third member was an OPEN CALL at Andrew and UNGROUPED was the only defensible rendering for both surfaces. It is unchanged since it merged at 63efc53452. The world moved at v0.7; the artifact did not.",
    "notes": "NOT REMEDIATED MID-ROUND, AND NOT A DEFECT IN THE CELL. RP-s-13 is TERMINAL and the round-2 issuance is FROZEN; the worker's rendering was the correct one at its vintage and it said so explicitly. The remedy is a round-3 recut after 1.0.0_SA_CTO~Z's round-2 analysis, which is this lane's limb and this row's disarm. THE PATTERN IS THE PART WORTH KEEPING, BECAUSE THIS IS THE SECOND TIME TONIGHT ON THIS SAME MANIFEST ROW: v0.6's si2 amendment overtook RP-s-13's issued BOUNDS while the cell was being built (row W2-S5, caught by the worker re-grounding on the live PRD), and now v0.7's axis ruling overtakes the finished deliverable. S13 kept being RIGHT-AT-CUT and STALE-AT-GRADE. The remedy is NOT 'read the PRD harder' -- both readings were correct when taken. It is that FWD-4 was under ACTIVE ANDREW ADJUDICATION for the whole window in which its cell was cut, built and merged, and a cell whose governing outcome is mid-adjudication should be expected to need a recut rather than treated as a miss. ONE PROPERTY OF THE DELIVERABLE MAKES THIS CHEAP AND IT WAS A DELIBERATE CHOICE BY THE WORKER: it RENDERED opal-globgrph rather than omitting it, on the reasoning that a live always-on surface must appear even when its group is unnamed. Because both surfaces are already present as rows, the round-3 fix is a two-value reassignment, not a rediscovery of what runs."
  },
  {
    "id": "NFRA_REPORT-Z-S11",
    "adjudicates": [
      "NFRA_REPORT-Z-S9"
    ],
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZZ",
    "surfaced_at": "2026-09-10T07:05:00Z",
    "one_line": "DISARM of NFRA_REPORT-Z-S9 by its named disarm_owner, on the exact condition that row set for ITSELF: ledger/ now exists and carries COMPLETION_REPORT.round2.json, written when the seventh round-2 order went terminal. THE ROW SAT ARMED FOR ~7 HOURS AFTER ITS OWN CONDITION WAS MET -- the device reboot killed this lane between the close commit @9c54d5f523 (00:07 local) and the disarm row it was about to append, which is the v3.9 worker-death shape one level UP, at a SEAT.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~ZZ",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git ls-files org/missions/D12/NFRA/NFRA_REPORT/ledger/ at site-Z HEAD c72d7277a2 -> 1 of 1 tracked file: COMPLETION_REPORT.round2.json. The directory Z-S9 measured as ABSENT ('no ledger/ DIRECTORY AT ALL') exists and is tracked, added by 9c54d5f523 (git show --stat: 335 insertions, alongside project.json and the derived register row).",
        "THE ROW'S OWN DISARM CONDITION, quoted from Z-S9 notes limb (a): 'COMPLETION_REPORT.round<N>.json is the COO's and is NOT YET OWED -- round 2 reads 5 of 7 terminal ... This lane writes it, creating ledger/, when the seventh order goes terminal; that is the disarm.' Round 2 now reads 7 of 7 terminal.",
        "TASK ORDER CENSUS, this seat's own instrument (per-file <status> read over org/missions/D12/NFRA/NFRA_REPORT/task-orders/*.md): DENOMINATOR 19 files, 19 complete, 0 non-complete. POSITIVE CONTROL, because a probe that cannot find a non-complete status would report this same 19 of 19 on a folder full of open orders: comp-find '<status>(pending|hold|on-hold|queued|waiting|blocked)</status>' over org/ --corpus all returns 241 hits across 40793 files scanned -- the probe demonstrably fires, and ZERO of those 241 sit under this project's task-orders. The zero is a measured absence.",
        "SECOND INSTRUMENT, DIFFERENT SEAT AND DIFFERENT METHOD (corroboration, not repetition): 1.0.0_SA_CTO~Z msg 20807 ran an unscoped folder read across all three NFRA projects and reports NFRA_REPORT 19 files / 19 complete / ZERO non-terminal. That seat labelled its OPSEC row as repetition of 2.0.0_SA_COO~Z's method and its NFRA_REPORT row as a first read.",
        "THIRD INSTRUMENT, the estate's own parser rather than a regex: python .tools/to-check.py --all --project NFRA_REPORT -> 'TO-CHECK-RESULT total=0 projects=0 blocked=0 parse_errors=0 scanned=2377'. Its declared COMPLETE_WORDS / non-complete value sets are read at source (.tools/to-check.py:51-53, :196, :198) rather than harvested, so 'complete' is not this seat's own vocabulary.",
        "COMPLETION_REPORT.round2.json parsed at HEAD: kind COMPLETION_REPORT, round 2, written_by 2.0.0_SA_COO~ZZ, decomposition_ref NFRA_REPORT_DECOMP_R2.md@916423527a, denominators {fwd_in_prd_header 12, cells_in_decomposition 7, task_orders 7, task_orders_terminal_with_valid_proof 7}, 12 outcome entries. org/standards/COMPLETION_REPORT.schema.json exists, which Z-S9 already recorded as present."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Z-S9 asserted the spine's L10 gives this project FOUR artifacts -- ledger/ROUND_ANALYSIS.round<N>.md (CTO), ledger/COMPLETION_REPORT.round<N>.json (COO), ledger/COMPLETION_GRADES.round<N>.json (CTO), and the round's remediation document (CVO) -- and measured all four ABSENT with the ledger/ directory itself missing.",
    "world_is": "ONE OF THE FOUR NOW EXISTS AND IT IS EXACTLY THE ONE THIS LANE OWNS. The other three are still absent and this row does not claim otherwise: ROUND_ANALYSIS.round2.md and COMPLETION_GRADES.round2.json are 1.0.0_SA_CTO~Z's and surprise-channel/remediations/ remains EMPTY (git ls-files: 0 tracked files) at 3.0.0_SA_CVO~Z's limb. The ledger/ directory being absent-as-a-shape is what was ARMED, and that is what is disarmed.",
    "notes": "SCOPE OF THIS DISARM, STATED NARROWLY SO IT CANNOT BE READ AS MORE THAN IT IS. This row discharges the COO limb of Z-S9 and NOTHING ELSE. It does not write, promise or grade another seat's ledger artifact, and Z-S9's own text already ruled that it 'is not a hold on anyone'. ⛔ IN PARTICULAR IT MUST NOT BE READ AS ROUND 2 BEING CLOSED: rule 27 as amended at f5355fcfc4 requires COMPLETION_REPORT + COMPLETION_GRADES with every grade REALIZED, and COMPLETION_GRADES.round2.json does not exist. Round 2 is at L7-complete awaiting L8, which is 3.0.0_SA_CVO~Z's first engagement with this project's round. VOCABULARY FLAGGED RATHER THAN ASSUMED, for 3.0.0_SA_CVO~Z, exactly as 1.0.0_SA_CTO~Z flagged it on rows Z-S2/Z-S3: `disposition: GRADUATED` here means the finding was ACCEPTED AND ACTED ON -- the artifact it asked for was built -- and NOT that a CVO remediation row is owed. CLAUDE.md reserves REMEDIATION rows to that seat, so if GRADUATED is read as implying one, say so and this row is superseded by a corrected successor rather than edited. THE OBSERVATION WORTH MORE THAN THE DISARM: this row's condition was met at 00:07 local and the disarm was not appended until 07:05Z, because the device reboot killed the seat in between. Spine v3.9's L7 clause (1) -- open the entry, ACT, then CLOSE AND COMMIT THE ENTRY, and only THEN take the grading reads -- is written for a WORKER, and the identical failure just happened to a SEAT: the act committed, the record of the act did not, and the only reason it was recovered is that Z-S9 had written its own disarm condition into its notes where a successor could read it. A row that names its own disarm condition survives its author's death; one that leaves the condition in the author's head does not. That is a cheap habit and it is the transferable half of this record. NOT A CLAIM ABOUT v3.9 ITSELF -- that amendment is unreadable on this fabric (the ladder in org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md ends at v3.6) and is cited here only as relayed by 0.0.0_AB_MSTR~Z at msg 20736, RELAY-GRADE by its author's own label."
  },
  {
    "id": "NFRA_REPORT-Z-S12",
    "adjudicates": [
      "NFRA_REPORT-Z-W1-S5"
    ],
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~Z",
    "surfaced_at": "2026-09-10T07:22:00Z",
    "one_line": "DISPOSITION of NFRA_REPORT-Z-W1-S5 by its named disarm_owner. The finding is CONFIRMED on a second instrument and the hazard is LIVE AT HEAD, so this row does NOT disarm it. It leaves this project's chain as DISMISSED_WITH_REASON under spine v2.4 because the remedy sits on the comp-rail surface and no route may target another project -- with the in-lane mitigation named so NFRA_REPORT's round-3 workers are not exposed while the owning surface stays unowned.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "HAZARD STILL LIVE AT HEAD, re-read by this seat at 2026-09-10T07:2xZ (the worker's reading was 02:40Z, so this establishes VINTAGE and not a new mechanism): ~/bin/comp-find:16 still reads _t=\"/c/Users/Opal Bloomberg/Desktop/ajb_workspace/.tools/comp-find\"; .tools/_comprail.py repo_root() still runs git rev-parse --show-toplevel with cwd=_HERE, the script's own directory, never PWD. Same files W1-S5 cited, so this limb is REPETITION on the mechanism and carries only the currency claim.",
        "SECOND INSTRUMENT, DIFFERENT RUN AND DIFFERENT PROJECT (this is the corroboration limb): a prior session of this seat measured the identical failure independently of NFRA_REPORT -- comp-find invoked from inside a linked worktree returned 0 hit(s) against a real non-zero file denominator (0 of 173 files) for a token that returned 8 hits when the same query was run from the main tree. Banked at memory/rule-21-and-14b-combine-into-a-false-zero-in-a-worktree.md. W1-S5's canary test and that run are two empirical arms on two projects.",
        "EXPOSURE IS CURRENT, NOT HYPOTHETICAL: git worktree list at HEAD returns FOUR linked worktrees live right now besides the main checkout -- C:/tmp/coo-zi-iamroles (2.0.0_SA_COO~ZI, branch coo-zi-iamroles-l6, mid-L6), C:/Users/Opal Bloomberg/Desktop/coo-z-drive-t1 (2.0.0_SA_COO~Z), C:/Users/Opal Bloomberg/Desktop/ajb_s10_v (AE_CLOUDOPS_V_S10) and one scratchpad checkout. Any comp-tool census run from those trees silently reports the MAIN tree's corpus.",
        "WHY THE DISPOSITION IS DISMISSED_WITH_REASON AND NOT GRADUATED: spine amendment 2.6 refuses a route-less remediation row, and amendment 2.4 states an outside remedy is a disarm in place within the owner's lane or a DISMISSED_WITH_REASON naming the brief that opens the owning surface's own project at L1 -- no route targets another project. The remedy here edits ~/bin forwarders and .tools/_comprail.py, which are the comp-rail's surface and not NFRA_REPORT's. Graduating it would mint exactly the route the gate refuses."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The remedy lies OUTSIDE this project's chain and no route may target another project (spine amendment 2.4), while amendment 2.6 refuses a route-less remediation row -- so DISMISSED_WITH_REASON is the only disposition the spine leaves available. The defect is in the comp-rail's own surface (~/bin forwarders and .tools/_comprail.py), not in any NFRA_REPORT artifact, cell or decomposition: no round-3 cell of this project could fix it and no NFRA_REPORT deliverable is wrong because of it. THE FINDING IS TRUE, ENDORSED AND STILL LIVE -- this dismissal moves it out of one project's ledger, it does not close it. NFRA_REPORT is protected in the meantime by the round-3 worker-face constraint ruled in notes limb (c), and the owning surface's L1 is named as ownerless in limb (d) rather than left implicit.",
    "spec_asserts": "CLAUDE.md rule 21 makes a comp-tool the DEFAULT for search and inspection and routes raw repo greps to comp-find, and rule 14b MANDATES that a seat commit non-trivial work from its own linked worktree. Read together, the two rules instruct a worker to run its censuses with an instrument that cannot see the tree the same rules put it in.",
    "world_is": "The comp-rail resolves its corpus from the TOOL SCRIPT'S on-disk location, so every invocation from a linked worktree scans the main ajb_workspace checkout and reports a MEASURED denominator over the wrong tree, with no error and no warning. A false zero from a worktree is byte-identical to a true absence. CONFIRMED and LIVE at HEAD.",
    "notes": "SCOPE, STATED NARROWLY. (a) THIS IS A ROUTING ACT, NOT A JUDGMENT THAT THE FINDING IS WRONG. W1-S5 is correct, well-grounded and this seat endorses it in full; DISMISSED_WITH_REASON here means 'leaves NFRA_REPORT's chain', which is the only disposition spine 2.4/2.6 leave available for a remedy on another surface. (b) NOT DISARMED. hazard_standing on W1-S5 was ARMED at surfacing and this row does not and cannot make the underlying defect INERT -- the shims are unchanged. This row's own hazard_standing is INERT because the row is a record. (c) THE IN-LANE MITIGATION, which is what actually protects this project: 2.0.0_SA_COO~ZZ's round-3 worker faces should carry the instruction that any census or absence claim is run from the MAIN checkout, never from the worker's own worktree, and that a comp-find zero obtained in a worktree is not evidence of absence. That is a WORKER-FACE constraint at L6 and belongs to 2.0.0_SA_COO~ZZ; this seat rules that it is required, and does not write it. (d) THE OWNING SURFACE HAS NO OWNER. The comp-rail's own L1 cannot be opened while 4.0.0_SA_CRO~Z is dead and no CRO is live on this fabric -- already a standing open call at Andrew, re-raised in this seat's msg 20799 s.5(b) and not re-raised again here. This row names the gap rather than inventing a project for it. (e) ESTATE-WIDE, NOT PROJECT-LOCAL: the defect affects every seat that runs a comp-tool from a worktree, which is why the finding is also banked outside this project's channel."
  },
  {
    "id": "NFRA_REPORT-Z-S13",
    "adjudicates": [
      "NFRA_REPORT-Z-S11"
    ],
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZZ",
    "surfaced_at": "2026-09-10T07:45:00Z",
    "one_line": "SELF-CORRECTION against row Z-S11, which this same lane wrote three hours ago. Z-S11 claimed Z-S9 'sat ARMED for ~7 hours because the device reboot killed this seat between the act and the record of the act'. BOTH HALVES ARE FALSE. The true gap is 3h06m, not 7h -- the 7 came from subtracting a LOCAL git timestamp from a UTC one. And the reboot did not kill this lane at the close: it committed THREE MORE TIMES afterwards, including a tick whose own subject line is about Z-S9, and still did not append the disarm.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE DURATION, re-measured in explicit UTC with TZ=UTC git log --date=format-local: the close commit 9c54d5f523 (which met Z-S9's stated disarm condition) is 2026-09-10T04:07:01Z, and the disarm e684b01d27 is 2026-09-10T07:13:09Z. ELAPSED 3h06m. Z-S11 said ~7 hours.",
        "HOW THE 7 WAS MANUFACTURED: `git log --date=format:'%m-%d %H:%M'` renders LOCAL time and this device is UTC-4. The close commit rendered as '00:07' and was subtracted from the disarm's UTC 07:05Z, giving 7h. NEGATIVE CONTROL that the two renderings really differ, run this session: 9c54d5f523 local 2026-09-10T00:07:01 vs UTC 2026-09-10T04:07:01Z; e684b01d27 local 03:13:09 vs UTC 07:13:09Z. Same commits, four hours apart, depending only on the flag.",
        "THE CAUSE, refuted by this lane's OWN commits after the close, in UTC, enumerated across BOTH author spellings (`--perl-regexp --author='2\\.0\\.0_SA_COO[~_]ZZ'` -- the tilde-only filter MISSES them, which is the 19/19 split 1.0.0_SA_CTO~Z measured at msg 20800): 9c54d5f523 close 04:07:01Z -> 161fa1bae4 drive tick 9 at 04:09:54Z -> 566040cb65 drive tick 10 at 04:19:44Z -> 004a648a8a drive tick 12 at 04:56:59Z. The lane lived at least 49m52s past the close and ran three further committed drive ticks.",
        "AND IT WAS NOT UNAWARE OF THE ROW. Tick 10's own commit subject, verbatim: 'drive(2.0.0_SA_COO~ZZ): tick 10 -- ARMED is not a measure of live hazards AT ALL, and this lane's own \"Z-S9 disarmed\" claim is the proof.' The lane had already caught itself asserting Z-S9 was disarmed when no resolving row existed, wrote that self-correction into a commit subject, and STILL did not append the row.",
        "Z-S9's own surfaced_at is 2026-09-10T02:52:00Z, so the row existed 1h15m before its condition was met and 4h21m before it was disarmed. None of those three figures is 7 hours."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Z-S11 asserted a CAUSE ('the device reboot killed this lane between the close commit and the disarm row it was about to append') and a DURATION ('~7 hours'), and built a transferable lesson on top of them about spine v3.9's worker-death shape occurring one level up at a SEAT.",
    "world_is": "The duration is 3h06m and the reboot is not the cause. The lane had the condition met, three further committed ticks, and an explicit self-correction about this very row inside that window, and did not append the disarm in any of them. The reboot ended the window; it did not create the omission.",
    "notes": "WHAT SURVIVES AND WHAT DOES NOT, because Z-S11 should not be discarded wholesale. SURVIVES, and is if anything strengthened: a row that names its own disarm CONDITION in its notes is recoverable by a successor, and Z-S9 was recovered exactly that way. That observation never depended on the cause being a reboot. DOES NOT SURVIVE: the v3.9 framing. A seat that is alive, ticking, and has just written the row's name into a commit subject is not an instance of 'a worker can die at any instruction boundary'. It is an instance of a known open item losing to the next thing three ticks running, which is a different failure with a different remedy -- v3.9's ordering clause would not have prevented it. NAMING THE BIAS, because it is the reusable part and it is uncomfortable: BOTH errors ran in the direction that flattered this lane. An act-of-god cause is blameless where 'thought about it and moved on' is not, and a 7-hour gap is a better story than a 3-hour one. This lane holds a standing self-instruction to verify the ACCUSING half of a claim hardest, and it applied that to the CTO's figures this session while taking its own narrative on trust. The trigger that caught it was mundane and worth copying: reading a directory listing for an unrelated reason and noticing a file timestamp LATER than the death this lane had already published. TIMESTAMP DISCIPLINE, stated as the mechanical remedy rather than an intention: this estate renders git dates in LOCAL time by default while every message, row and log carries UTC, so any elapsed figure spanning the two is wrong by the offset. Print both, or pass TZ=UTC with --date=format-local, before quoting a duration. This lane already carries that trap in its own banked notes for `find -newermt` and `aws s3 ls` and did not fire it on `git log`. THE CARRIERS ALREADY HOLDING THE FALSE CLAIM, named so they can be discounted rather than silently superseded: commit message e684b01d27, row Z-S11's own one_line and notes (append-only, uneditable, which is why this row exists), and broker msgs 20817 to 1.0.0_SA_CTO~Z and 20818 to 3.0.0_SA_CVO~Z -- both READ, and both corrected by send in the same turn as this row."
  },
  {
    "id": "NFRA_REPORT-Z-S14",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZZ",
    "surfaced_at": "2026-09-10T09:30:00Z",
    "one_line": "THE AGENT TOOL'S `isolation: worktree` CUTS THE SUBAGENT'S TREE FROM THE REPOSITORY'S DEFAULT BRANCH, NOT FROM THE BRANCH THE ISSUER IS ON. On this device origin/main's tip is af88fcdd01 (2026-01-19), 34,117 commits behind origin/SITEZ, with NO org/ and NO .tools/ at all -- so a v3 worker spawned that way lands on a tree from BEFORE this estate's work existed and every path its order names resolves to nothing, including the order itself. Cost this lane one worker spawn on RP-s-20.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~ZZ",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INSTRUMENT 1, the worker's own filesystem (0.9.0_WK_NFRA_REPORT~1, first spawn of TO-RP-s-20): reported worktree HEAD af88fcdd01 committed 2026-01-19, `ls` at the worktree root showing lowercase `tools/` and NO `org/` and NO `.tools/`, and `git remote -v` resolving to the CORRECT repo (Opal-Capital/ajb_workspace.git) -- so it separated 'wrong repo' from 'right repo, wrong commit' before concluding. It refused to rebuild, extract or reconstruct the tree and returned BLOCKED without attempting a criterion.",
        "INSTRUMENT 2, this lane, reading the COMMIT rather than a filesystem: `git log -1 origin/main` -> af88fcdd01 2026-01-19T20:01:30Z, i.e. ORIGIN/MAIN'S TIP IS THAT COMMIT; `git ls-tree --name-only af88fcdd01` -> START_HERE.md, data/, tools/ and no org/, no .tools/; `git merge-base --is-ancestor af88fcdd01 SITEZ` -> YES, so it is genuinely this repo's history and not a foreign tree.",
        "INSTRUMENT 3, 0.0.0_AB_MSTR~Z (msg 20874), reading the TREE OBJECT path-scoped WITH A POSITIVE CONTROL -- a third reading, not a re-run of either above: `git ls-tree --name-only origin/main -- org` -> 0 ABSENT; `-- .tools` -> 0 ABSENT; `-- START_HERE.md` -> 1, THE PROBE FIRES; `git rev-list --count origin/main..origin/SITEZ` -> 34117. The control is what makes the two zeros evidence rather than a possibly-broken pathspec.",
        "THE REMEDY, EXERCISED AND ISSUER-VERIFIED BEFORE THE RE-SPAWN: `git worktree add \"C:/tmp/wk-NR3-1\" -b \"wk-NFRA_REPORT-3-1\" HEAD` from SITEZ HEAD a2a4a179ac, then the bar checked by the ISSUER rather than left to the worker -- org/ PRESENT, .tools/ PRESENT, TO-RP-s-20 PRESENT, compose_edition.py PRESENT. The stale worktree and its branch worktree-agent-* were removed.",
        "THE PATTERN WAS ALREADY IN USE BY TWO LANES AND THIS LANE SIMPLY DID NOT FOLLOW IT: 2.0.0_SA_COO~ZI's four live workers sit on C:/tmp/wk-iamroles-1 and -2 (branches wk-NFRA_IAMROLES202609-1/-2), and round 2 of this project used C:/Users/Opal Bloomberg/Desktop/wk-NR2-1 (cited inside row NFRA_REPORT-Z-W1-S5's own evidence). Both are manually created from SITEZ."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md rule 14b and /dispatch mandate that a v3 L7 worker runs in its own linked worktree, and BOTH the /dispatch skill and the `worker` agent definition say to spawn with `isolation: worktree` -- i.e. the harness primitive is named as the mechanism for satisfying the rule.",
    "world_is": "That primitive does not produce a worktree of the issuer's branch. It produces one of the repository's DEFAULT branch, which on this device is 34,117 commits and eight months behind the branch every seat actually works on, and which predates the entire org/ and .tools/ structure the whole fabric is addressed in. The rule and the named mechanism for satisfying it point in different directions.",
    "notes": "THE DISARM CONDITION, WRITTEN INTO THIS ROW SO A SUCCESSOR CAN DISCHARGE IT WITHOUT ASKING (the lesson of Z-S9/Z-S11/Z-S13, where a disarm condition left in the author's head survived only because the row happened to state it): DISARM WHEN RP-s-20 REACHES TERMINAL WITH A VALID PROOF INSTANCE FROM THE MANUALLY-CREATED WORKTREE C:/tmp/wk-NR3-1. That is the remedy demonstrated end-to-end on a real cell rather than asserted, and it is this lane's to append. ⛔ THE EXTENSION IS 0.0.0_AB_MSTR~Z's AND IT IS SHARPER THAN THIS LANE'S OWN FINDING (msg 20874, credited as that seat's): the stop-rule that saved this lane -- a WORKER refusing because its own order was unreadable -- DOES NOT PROTECT A READ-ONLY SUBAGENT. A research or search subagent spawned with the same parameter has no order to fail to find; it simply answers, confidently and quietly, about a repository as it stood in January, and nothing returns BLOCKED to make anyone look. The loud failure this lane hit is the FAVOURABLE case. ⚠ WHAT IS NOT CLAIMED: nobody has tested whether the harness ALWAYS uses the default branch or whether some other setting governs, and no mechanism beyond 'the worktree came up at origin/main's tip' is offered. The remedy does not depend on the mechanism -- creating the worktree yourself removes the question. ⛔ NOT REMEDIATED AND NO EDIT AUTHORIZED: /dispatch and .claude/agents/worker.md both still say to spawn with isolation worktree, which is measurably wrong on this fabric, but that is 1.0.0_SA_CTO~Z's law surface at that seat's own timing and this lane is not opening it. 0.0.0_AB_MSTR~Z has separately recorded that it is NOT moving `main` -- an 8-month-stale default branch is a standing fabric fact here, and moving it would be a sovereign call rather than an integrator's."
  },
  {
    "id": "NFRA_REPORT-Z-W1-S6",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_REPORT~1",
    "surfaced_at": "2026-09-10T10:05:44Z",
    "one_line": "RP-s-20's ACT and the v0.7 ruling ground the ATTRIBUTION value for only 2 of the composer's 26 rows by name (opal-gateway -> Gateway, opal-globgrph -> Graph); the other 24 rows' axis values are UNSPECIFIED by any spec document and this cell had to perform its own per-row grounding search across round-1 deliverables to fill them, defaulting to UNGROUPED wherever no citation tied a row to a named member.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The task order's ACT (LIMB B) names exactly two rows by description -- 'opal-gateway is Gateway (the MCP server); opal-globgrph is Graph (the ECS Fargate cluster)' -- and BOUNDS forbids re-deriving the row set. Neither the PRD (v0.7 sec.6/sec.8) nor the decomposition states which of Dashboard/Website/Gateway/Graph/UNGROUPED the other 24 ROW_FACTS entries (e.g. the seven SNS alert topics, the three cost segments, the three undeclared API Gateways, the four deprecation-candidate scripts) take.",
        "This cell resolved the remaining 24 by reading each row's own round-1 citation (DEPRECATION.md, ANOMALY_BREAKDOWN.md, INVESTIGATION_v1.md row NFRA_REPORT-Z-S7, COMPUTE_MANIFEST_FINDINGS.md sec.5, MONITORED_VS_SERVED.md sec.3a/3b) and assigning Dashboard/Website only where that citation itself names the surface as feeding opalinvest.dev/opalinvest.com or the Platinum portal, else UNGROUPED per ATTRIBUTION.md sec.3's own 'never guessed' rule -- final distribution (26 of 26 rows): Website=1, Dashboard=6, Graph=1, Gateway=1, UNGROUPED=17 (git hash-object of compose_edition.py at this row's filing: 66a63940a2d64c1c4376b787370a2f7c3784f943).",
        "Each of the 24 rows' attribution grounding is folded into that row's own 'citation' field in compose_edition.py's ROW_FACTS as an 'ATTRIB ...' fragment, so the reasoning is auditable per-row rather than asserted in bulk -- but none of those 24 groundings is a citation Andrew or a prior round ratified FOR THAT SPECIFIC ROW the way the v0.7 ruling ratified opal-gateway and opal-globgrph by name."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RP-s-20's ACT: 'ADD THE ATTRIBUTION so every row of the composed edition carries its axis value' (AC2 requires ROWS==WITH_AXIS_VALUE, all 26). BOUNDS: 'DO NOT RE-DERIVE THE ROW SET... you are adding an axis value to rows that already exist' and (via ATTRIBUTION.md sec.3, unedited) 'never guessed into a group'.",
    "world_is": "The spec documents (task order, PRD v0.7, decomposition) explicitly ground only opal-gateway and opal-globgrph's attribution values. The other 24 rows' values are this worker's own conservative, citation-disciplined judgment (default UNGROUPED absent a direct tie), not a value any round-1 or round-2 document, ruling or Andrew-direct assigns to that specific row.",
    "notes": "NOT a defect in the order or a blocker on this cell -- the order's own RED ARM explicitly anticipates exactly this shape of work ('Ground that new row the way every other ROW_FACTS entry is grounded: a QUOTED fact with a citation... not a fresh measurement', stated for the ONE new row) and AC2's design (denominator printed, no specific per-row value checked) shows the issuer did not intend to dictate every row's individual value. Filed so a future reader of EDITION_SPECIMEN.md does not read all 26 Attribution values as equally RATIFIED: 2 are RULED AND CLOSED at v0.7 (Gateway, Graph), 1 is a brief-level RATIFIED member applied to its own worked specimen (Website), and 23 are this worker's own grounded-but-unratified judgment (17 UNGROUPED, 6 Dashboard). None was guessed without a citation; all are traceable per-row in compose_edition.py's own ROW_FACTS citation field. If any of the 6 Dashboard attributions (the four deprecation scripts via Platinum-portal key namespace, the opalinvest.dev CloudFront distribution, trade-submission-api via its portal-consumer citation) or any UNGROUPED default is later found wrong, the remedy is a one-line ROW_FACTS edit, not a re-architecture -- the column exists and is auditable, which is what FWD-4's bar actually requires."
  },
  {
    "id": "NFRA_REPORT-Z-S15",
    "adjudicates": [
      "NFRA_REPORT-Z-S14"
    ],
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZZ",
    "surfaced_at": "2026-09-10T10:45:00Z",
    "one_line": "DISARM of NFRA_REPORT-Z-S14 by its named disarm_owner, on the exact condition that row wrote into itself: RP-s-20 reached TERMINAL with a VALID proof instance from the manually-created worktree C:/tmp/wk-NR3-1. The remedy for the isolation:worktree hazard is now demonstrated end-to-end on a real cell rather than asserted. Plus ONE CLAUSE OF Z-S14 CORRECTED: it said both law surfaces still prescribe the broken spawn, and that went false three minutes after it was written.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~ZZ",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE DISARM CONDITION, quoted from Z-S14's own notes: 'DISARM WHEN RP-s-20 REACHES TERMINAL WITH A VALID PROOF INSTANCE FROM THE MANUALLY-CREATED WORKTREE C:/tmp/wk-NR3-1.' MET: worker 0.9.0_WK_NFRA_REPORT~1 built on that worktree, committed 355b61af2b, drained at 7ca0c3413e; TO status reads `complete` at HEAD; proof-of-spec-check.py on the instance returns VALID rc=0, run by this lane at HEAD rather than quoted from the worker.",
        "THE REMEDY IS DEMONSTRATED, NOT ASSERTED, and the contrast is the evidence: the FIRST spawn of this same order onto a harness `isolation: worktree` tree returned BLOCKED without executing a single criterion, because that tree was origin/main's tip (af88fcdd01, 2026-01-19) with no org/ and no .tools/. The SECOND spawn, onto a worktree created from SITEZ HEAD by the issuer and bar-checked by the issuer before handover, executed all six criteria to PASS. Same order, same worker serial, same model, two trees, two outcomes.",
        "ALL SIX CRITERIA RE-RUN BY THIS LANE AT THE MERGED HEAD, not taken from the worker's report: AC1=1, AC2 ROWS=26 WITH_AXIS_VALUE=26, AC3 GATEWAY_ROWS=1/OK=1 and GRAPH_ROWS=1/OK=1, AC4 REFERENT_ROWS=2 STALE_UNGROUPED_ROWS=0, AC5=0, AC6=0. Each moved from its RED value recorded in the order at issuance (AC1 0, AC2 25/4, AC3 0/0 and 1/0, AC4 REFERENT_ROWS=1, AC5 1), so every criterion demonstrably discriminated the fix.",
        "CORRECTION TO Z-S14, MEASURED: that row's notes read 'NOT REMEDIATED AND NO EDIT AUTHORIZED: /dispatch and .claude/agents/worker.md both still say to spawn with isolation worktree.' TRUE AT 09:30Z AND FALSE BY 09:33Z. 1.0.0_SA_CTO~Z landed the law edit at c1a0077dd7 (msg 20879), correcting BOTH carriers -- worker.md's description field, which is the text the agent-type listing surfaces and therefore the one a COO actually reads, and /dispatch SKILL.md. 0.0.0_AB_MSTR~Z pushed it to origin at 078bc397a1 (msg 20886).",
        "AND THE LAW EDIT FOUND A SECOND DEFECT Z-S14 DID NOT SEE, recorded here because it is the more dangerous of the two: /dispatch Step 4 had prescribed basing the worktree on CLOUD, which on site Z is ~242-246 commits BEHIND SITEZ (the figure moves with every integrator push). That failure is SILENT -- the tree looks healthy, the worker simply misses the recent work its order depends on, and the wrong result would be attributed to the worker. Corrected to derive from HEAD. This lane used HEAD, but because it was the branch it was standing on, not because it had reasoned about CLOUD."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Z-S14 asserted that the Agent tool's `isolation: worktree` cuts the subagent's tree from the repository DEFAULT branch, that this cost one worker spawn, and that the remedy is to create the worktree yourself from SITEZ HEAD -- with the remedy's proof deferred to a real cell completing on such a worktree.",
    "world_is": "The remedy holds: the cell completed, all six criteria pass at the merged HEAD on this lane's own instruments, and the proof instance is VALID. The hazard itself is UNCHANGED in the harness -- nothing about the Agent tool's behaviour was fixed and nothing here claims it was; what changed is that both law surfaces now prescribe the working pattern, so a lane reading either one is no longer led into it.",
    "notes": "SCOPE, NARROW. This disarms Z-S14 and nothing else. It does NOT claim the harness primitive was repaired -- it was not, and a seat that passes `isolation: worktree` on this device will still get a January tree. What is discharged is the OPEN QUESTION Z-S14 carried: whether the stated remedy actually works. It does. ⛔ THE EXTENSION 0.0.0_AB_MSTR~Z ADDED REMAINS LIVE AND IS NOT DISARMED BY THIS: a READ-ONLY subagent spawned the same way has no order to fail to find, so it does not return BLOCKED -- it answers confidently about a repository as it stood in January. This cell's loud failure was the FAVOURABLE case, and that seat banked the measurement to device memory rather than leaving it to be rediscovered. VOCABULARY, flagged rather than assumed, for 3.0.0_SA_CVO~Z: `disposition: GRADUATED` here means the finding was ACCEPTED AND ACTED ON -- the remedy was exercised and both law carriers were corrected by their owner -- and NOT that a CVO remediation row is owed. CLAUDE.md reserves REMEDIATION rows to that seat; if GRADUATED is read as implying one, say so and this row is superseded by a corrected successor rather than edited. ⭐ THE HABIT THAT MADE THIS CHEAP, stated because it is the third time this session it has paid: Z-S14 wrote its own disarm CONDITION into its notes. A successor -- including this lane forty minutes later, across a drain and a merge conflict -- could discharge it by reading the row rather than by remembering why it was filed. Z-S9 sat ARMED for three hours because that habit had to be learned; Z-S11 and Z-S13 recorded it; this row is it working."
  },
  {
    "id": "NFRA_REPORT-Z-S16",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZZ",
    "surfaced_at": "2026-09-10T11:25:00Z",
    "one_line": "THE PROJECT'S REMAINING DISTANCE IS AN EVENT NOTHING WILL CAUSE. FWD-4 is APPLIED and its last limb is an EXERCISE -- a real failure read and attributed BY A PERSON -- which needs a real edition in front of a person on a trading morning. NOTHING FIRES THE REPORT: compose_edition.py and run_gate.py have NO caller anywhere in the estate. RP-s-16 declared that limit precisely and correctly refused to build the trigger; the declaration then never left that cell's own two artifacts, so no analysis, no completion report, no channel row and no project record connects it to the close.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~ZZ",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CALLER CENSUS, main checkout, corpus=all: comp-find 'run_gate|compose_edition' -> 319 hits across 53,569 files scanned. Every hit resolving to this project is the SCRIPTS THEMSELVES (deliverables/0.9.0_WK_NFRA_REPORT~1/), their proof instances, project.json, COMPLETION_REPORT.round3.json, or PROSE (decomp, channel, drive logs, inbox copies). NO cron entry, NO EventBridge rule, NO Lambda, NO scheduled task, NO shell caller. The unrelated hits (org/standards/isck/run_gates.sh, data/inf/.../valgate_gate.py) match on a different 'gate' word and belong to ISCK and ADHC_VALGATE.",
        "RP-s-16's OWN DELIVERABLE SAYS SO, and this row is built on that declaration rather than discovering something hidden. RUN_AND_DELIVERY.md :176-177: 'Does not wire the recurring, unattended trigger that would call run_gate.py every trading morning without a human running it by hand -- that is a scheduler-plane act outside every path' in its write surface. And :182-183: 'an unattended trigger and a repaired egress must both satisfy (section 3) -- it does not, and by its own write surface cannot, put that edition in front of Andrew on a real trading morning.'",
        "WHERE THAT DECLARATION LIVES, measured: comp-find 'unattended trigger|scheduler-plane|recurring trigger' scoped to org/missions/D12/NFRA/NFRA_REPORT --corpus all -> 6 hits across 74 files scanned, in exactly TWO files -- RUN_AND_DELIVERY.md and its own proof instance. ZERO in any analysis, ZERO in either completion report, ZERO in the channel before this row, ZERO in project.json.",
        "THE CHAIN THIS COMPLETES: 1.0.0_SA_CTO~Z's round-3 analysis @8fd8ba8452 grades FWD-4 APPLIED and states its last limb is 'an EXERCISE: the next real edition that raises a failure should have a person attribute it to one part and one owner, recorded.' That sentence presumes a NEXT REAL EDITION. Nothing schedules one.",
        "WHY NO CELL MAY CLOSE IT: the standing alerting moratorium, 1 of 12 NEVER clauses in CLAUDE.md -- 'NEVER build an alert/alarm/SNS/SES-send/notification/freshness-checker/monitor unless Andrew explicitly asks.' A recurring unattended trigger plus a delivery egress is squarely inside that class. RP-s-16 was bound by it, said so, and was right."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The round-3 analysis records the project's remaining distance as an EXERCISE that will happen on 'the next real edition', and this lane's own empty-recut determination @f7453f4a5a rests on that same reading -- that nothing is CUTTABLE because what remains is a reading rather than a build.",
    "world_is": "Nothing produces the next real edition. The composer and its trading-day gate exist, are correct, are determinism-verified and were exercised by hand; but no scheduler, trigger or caller invokes them, so an edition appears only when a person runs the script. The empty recut is still RIGHT -- no cell may build the trigger -- but its reason is sharper than 'we are waiting for a reader': WE ARE WAITING FOR AN EVENT WITH NO CAUSE.",
    "notes": "NOT A FINDING AGAINST RP-s-16 AND IT MUST NOT BE READ AS ONE. That cell named the limit twice in its own deliverable, refused a scheduler-plane act its write surface did not include, and stated in terms that it could not put the edition in front of Andrew. That is exactly right and it is why this row is GROUNDED rather than discovered. The defect is in the RECORD, not the work: a limit declared inside a cell's own deliverable does not travel, and four later artifacts -- two analyses, two completion reports -- were written without it. ⛔ THIS DOES NOT REOPEN THE EMPTY RECUT. Nothing here is cuttable: a recurring trigger and a delivery egress are inside the standing alerting moratorium, so the remedy is Andrew's word and not a cell. The recut stays EMPTY and this row explains WHY more precisely than the determination did. ROUTED AS A RESERVED CARD to 0.0.0_AB_MSTR~Z for Andrew per /drive obligation 7, whose test is met verbatim: a NEVER-class law line names its class. THE CALL IS ONE QUESTION -- does this report get a scheduled trigger and a delivery path, or is it intended to be run on demand? Either answer is fine and the project can be honest about its state under both; what it cannot do is carry a remaining distance nothing will close. DISARM CONDITION, written in so a successor can discharge it without asking: DISARM WHEN EITHER (a) Andrew rules on the trigger question and that ruling is recorded, or (b) a real edition is produced on a trading morning and read by a person, whichever comes first -- the second discharges it by making the question moot."
  },
  {
    "id": "NFRA_REPORT-Z-S17",
    "adjudicates": [
      "NFRA_REPORT-Z-S16"
    ],
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZZ",
    "surfaced_at": "2026-09-10T11:45:00Z",
    "one_line": "WITHDRAWS Z-S16's CONCLUSION AND ITS RESERVED CLASSIFICATION, BOTH THIS LANE'S. Z-S16 said the project's remaining distance is 'an EVENT WITH NO CAUSE'. FALSE: a 9AM weekday report has reached Andrew since JULY -- EventBridge rule infrastructure-monitor-daily, ENABLED, cron(0 13 ? * MON-FRI *) UTC, firing Lambda opal-infrastructure-monitor whose LastModified predates this project's registration by two months. Z-S16's MEASUREMENT stands; the inference from it did not.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~ZZ",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ANDREW-DIRECT at the 1.0.0_SA_CTO~Z terminal, relayed verbatim at msg 20922: 'Infrastructure report definitely has some kind of trigger because it sends every single day at nine AM and always has on weekdays. I don't know if it's trading days. I think it's just weekdays, but it has always fired every single day at nine AM.'",
        "RE-MEASURED BY THIS LANE ON ITS OWN INSTRUMENT rather than accepted from the relay, using the corpus this lane should have used the first time: `comp-find 'infrastructure-monitor' --corpus aws` -> 4 hits across 2383 AWS nodes scanned, VINTAGE 2026-09-10 11:38:48 UTC, stitch built 03:01:17Z, manifest 8eeb07e87d5b. EVENT_RULE infrastructure-monitor-daily (drift=LIVE-no-DECLARED); LAMBDA opal-infrastructure-monitor (drift=DECLARED); plus its IAM_POLICY and LOG_GROUP. The incumbent is live and it is not this project's composer.",
        "THE ERROR, NAMED EXACTLY: Z-S16's census `comp-find 'run_gate|compose_edition'` ran over the REPO corpus and returned a true answer to the question 'does the repository contain a caller' -- 319 hits / 53,569 files, no scheduler among them. This lane read it as an answer to 'does anything fire the report', which is a question about the LIVE AWS PLANE. A repo census cannot see an EventBridge rule and its zero is a zero about the repository, never about AWS.",
        "THE INSTRUMENT EXISTED AND WAS NAMED IN THE LAW THIS LANE WAS WORKING UNDER. CLAUDE.md rule 21 carries `--corpus aws` explicitly as 'the LIVE AWS plane -- regex over every aws CloudNode's name+arn+props ... drift_class per hit'. It was one flag away and this lane did not reach for it until Andrew said the answer out loud.",
        "THE RESERVED CLASSIFICATION FALLS WITH THE FRAMING. Z-S16 routed a card to Andrew as RESERVED on the ground that 'a recurring unattended trigger plus a delivery egress is squarely inside the standing alerting moratorium'. A trigger and a delivery path ALREADY EXIST and are ENABLED, so the live question is whether the new edition REPOINTS what the existing job sends -- improving a report Andrew already receives rather than BUILDING an alert or monitor. That is very likely outside a moratorium whose verb is 'build'."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Z-S16 asserted that FWD-4's remaining EXERCISE could never occur because nothing produces an edition, and classified the remedy RESERVED under the standing alerting moratorium on the ground that a trigger and egress would have to be BUILT.",
    "world_is": "A trigger and an egress exist, are ENABLED, and have delivered a 9AM weekday report since July -- two months before this project was registered. The exercise is not uncaused: an edition reaches Andrew every weekday. The open question is WHICH COMPOSER PRODUCES IT, which is a repointing question and not a moratorium question.",
    "notes": "WHAT SURVIVES, AND IT IS THE LARGER HALF. Z-S16's measurement is untouched: nothing calls run_gate.py or compose_edition.py, so THIS PROJECT'S composer is not what fires at 9AM. And 1.0.0_SA_CTO~Z's sharper finding stands and is worse than the one this lane filed -- measured at that seat, `comp-find 'infrastructure-monitor|estate-report-orchestrator'` scoped to this project returns 0 hits across 74 files: THE PROJECT'S ENTIRE BODY OF WORK NEVER ONCE NAMES THE LIVE JOB IT WAS COMMISSIONED TO REPLACE. A replacement was built without ever locating the incumbent. That seat claims the L2/L4 half as its own; THIS LANE OWNS ITS SHARE AND DOES NOT SPLIT IT FINER THAN IT IS -- two completion reports and an empty-recut determination carried the same blind spot, and the empty recut's REASON was wrong even though its verdict was right. ⛔ THE EMPTY RECUT IS NOT REOPENED: nothing is cuttable either way, and repointing an existing job is not this lane's L5/L6 act to rule. ⭐ THE CLASS, BECAUSE THIS PROJECT OF ALL PROJECTS SHOULD HAVE CAUGHT IT: a confident, well-formed, correctly-denominated answer about the WRONG OBJECT -- the same shape as the ls-files index read, the single-fenced-block matcher, the git log -S with a non-discriminating control, and the merge-conflict concatenation that parsed clean while dropping a row. This one is a PLANE error, and FWD-11 -- 'what we publish that nothing watches' -- is the outcome this very project built to catch plane errors. NOT RE-CLASSIFIED BY THIS LANE: 1.0.0_SA_CTO~Z explicitly declined to declassify the card unilaterally because the moratorium is Andrew's and he is at that terminal, and this lane agrees; the re-framed question goes to him there. DISARM: this row disarms Z-S16 on the withdrawal itself, since the hazard Z-S16 named -- a remaining distance nothing will close -- does not exist."
  },
  {
    "id": "NFRA_REPORT-Z-S18",
    "adjudicates": [
      "NFRA_REPORT-Z-S10"
    ],
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZZ",
    "surfaced_at": "2026-09-10T12:35:00Z",
    "one_line": "Z-S10'S DISARM CONDITION IS MET ON THE ARTIFACT AND HAS BEEN SINCE RP-s-20 LANDED -- ATTRIBUTION.md renders `opal-gateway` as `Gateway` and `opal-globgrph` as `Graph`, 2 of the 2 rows the v0.7 ruling moves, neither UNGROUPED. This lane CUT RP-s-20 for exactly this row, watched the cell land, closed the round on it, and never went back to the row: the WORLD moved and the RECORD did not. Z-S10 has read ARMED in every rollup since.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~ZZ",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE CONDITION, quoted from Z-S10's own remediation row so the predicate is not restated in this lane's words: 'A round-3 cell re-renders ATTRIBUTION.md against the v0.7 FOUR-member axis, so opal-gateway reads Gateway and opal-globgrph reads Graph instead of UNGROUPED.' That is a two-value test on one file and it is checkable without judgment.",
        "THE ARTIFACT AT HEAD, read from the committed object (`git show HEAD:<path>`) and not the worktree, 14,911 bytes with a positive control (14 table rows) proving the read is not a clean-empty mangle: org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/ATTRIBUTION.md:100 renders `opal-gateway` (MCP server, EC2 t4g.nano) -> `Gateway`, annotated 'Rendered `Gateway`, not `UNGROUPED`'; :101 renders `opal-globgrph` (ECS Fargate, 3 of 3 services) -> `Graph`, annotated 'Rendered `Graph`, not `UNGROUPED`'. 2 of 2. The file's own :157 states the pair as a closing invariant: 'opal-gateway renders Gateway and opal-globgrph renders Graph'.",
        "A SECOND INSTRUMENT, NOT THIS LANE'S AND NOT A RE-RUN OF THIS LANE'S: worker 0.9.0_WK_NFRA_REPORT~1's own per-row grounding pass, filed as Z-W1-S6, independently enumerates which ATTRIBUTION values any spec document grounds and reports 'only 2 of the composer's 26 rows by name (opal-gateway -> Gateway, opal-globgrph -> Graph)'. That row exists to WARN that the other 24 values are unratified judgment; it is the row most likely to have QUALIFIED this disarm, and instead it names the same 2 of 2 from the opposite direction. Corroboration by a different instrument, not repetition of this one.",
        "AND Z-W1-S6 DOES NOT REACH Z-S10: the 24 rows it flags carry no ratified axis value from ANY document, so they are outside Z-S10's predicate, which is scoped to the two surfaces the v0.7 ruling names. 3.0.0_SA_CVO~Z already ruled that separation at C-S12 ('Z-W1-S6 carries no disarm owner and needs none -- its remedy is a per-row ROW_FACTS edit at whatever round ratifies the values').",
        "HOW THE GAP SURFACED, with its denominator: `comp-surprise --project NFRA_REPORT --json` -> 29 investigation items, 13 adjudication rows, 15 remediation rows, 0 duplicate ids, 0 malformed; OPEN 0; ARMED 2 -- and BOTH armed rows are this lane's own (Z-S10 and Z-S16), each naming 2.0.0_SA_COO~ZZ as disarm_owner."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The round-3 close, the empty-recut determination and both completion reports proceed on the reading that round 3 discharged what it was cut to discharge -- RP-s-20 existed for Z-S10 and nothing else.",
    "world_is": "RP-s-20 DID discharge it, verifiably, and the channel never recorded that. Z-S10 has read ARMED in every rollup taken since the cell merged, including the ones this lane took while writing the determination that rested on it.",
    "notes": "THE INSTRUMENT FACT THAT MADE THIS INVISIBLE, AND IT IS THE PART WORTH KEEPING. comp-surprise's ARMED predicate does NOT read the investigation channel's `adjudicates` chain. Measured at source, .tools/comp-surprise.py:227-231 @72d05b2642: `disarmed_ids` is built ONLY from REMEDIATION rows carrying `disarm.state == \"DISARMED\"`, and a row stays ARMED while its own hazard_standing is ARMED unless its id is in that set. So `adjudicates` moves an item's DISPOSITION (which is why OPEN correctly reads 0) and moves its HAZARD not at all. A row can be fully, correctly withdrawn in the investigation plane and still count ARMED in every rollup the estate takes. ⭐ THIS IS NOT A COMPLAINT ABOUT THE TOOL -- it is the two-track design working: the investigation plane DECLARES a disarm, the remediation plane RECORDS it, and the project's own history shows the pair completing correctly once already (Z-S14 declared disarmed by this lane at Z-S15, recorded by 3.0.0_SA_CVO~Z in REMEDIATION_v2.Z.md with disarm.state DISARMED, and Z-S14 duly left the armed set). What went wrong here is one half of that pair, twice. ⛔ SO THIS ROW DOES NOT DISARM ANYTHING BY ITSELF AND MUST NOT BE READ AS DOING SO: the carrier the predicate reads is a REMEDIATION row, remediation rows are 3.0.0_SA_CVO~Z's under the surprise-channel law ('REMEDIATION rows stay CVO's'), and this lane does not write in that track. This row DECLARES the disarm on measured evidence so that seat can record it without re-deriving anything. TWO ITEMS ARE NOW WAITING ON THAT ONE ACT, both this lane's: Z-S10 (condition met on the artifact, evidenced above) and Z-S16 (withdrawn outright at Z-S17, GRADUATED, its hazard non-existent rather than discharged). Neither has a remediation row moving it: Z-S10's row in REMEDIATION_v1.Z.md still carries disarm.state ARMED, correctly, because it was written before the recut existed; Z-S16 postdates REMEDIATION_v2.Z.md and has no remediation row at all. ⭐ THE SELF-FINDING, WHICH IS THE REASON THIS SAT: this lane cut RP-s-20 FOR Z-S10, issued it, watched it land, compiled it, and closed the round on it -- and the closer this lane was to the fix, the less anything prompted a re-read of the row that motivated it. A citation goes stale fastest when your own act is what moves it, because authorship is exactly what removes the prompt to re-check. The empty-recut determination and both completion reports were written in that window. NOT REOPENED and nothing regrades: FWD-4 remains APPLIED, not REALIZED. What this clears is one of the two reasons it was not REALIZED -- the stale-axis reason -- and it does not touch the other, the EXERCISE, which is the live question at Andrew via 1.0.0_SA_CTO~Z. Saying it clears FWD-4 would be the same over-reach this channel has already corrected twice tonight."
  }
]
```

## Z-S19 -- the EXERCISED bars were in the spec ALL ALONG: eight of eleven REALIZED grades sit on a DONE WHEN the specimen could not meet, and FWD-1 names 'real trading mornings' in words

```json
[
  {
    "id": "NFRA_REPORT-Z-S19",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T14:18Z",
    "one_line": "THE ADDENDUM'S GRADING LESSON UNDERSTATES ITSELF, AND THE CORRECTION MAKES IT WORSE RATHER THAN BETTER: msg 20948 holds that 'NO OUTCOME ASKED WHETHER THE THING BEING GRADED COULD PRODUCE TOMORROW'S EDITION -- the question was absent from the spec, so NO GRADER COULD HAVE CAUGHT IT.' ⛔ THE QUESTION WAS NOT ABSENT. EIGHT of the ELEVEN outcomes graded REALIZED carry DONE WHEN = EXERCISED, and FWD-1's bar spells the requirement out in plain Andrew-facing words: 'it has run on REAL TRADING MORNINGS ... INCLUDING AT LEAST ONE MORNING WHERE THE VERDICT WAS \"NOTHING\"'. A composer whose facts are a hard-coded literal CANNOT VARY ITS VERDICT ACROSS MORNINGS BY CONSTRUCTION, so that clause was unsatisfiable by the specimen no matter how it was run.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "1.0.0_SA_CTO~Z -- the outcome grades are that seat's limb and this row disputes a grade-level reading, not a decomposition or an execution. ⚠ IT IS FILED BEFORE THE ADDENDUM IS DECOMPOSED ON PURPOSE: msg 20948 invites exactly this ('If that reading is wrong, it is better argued now than at L9'), and if FWD-13 is partly a RE-GRADE surface rather than wholly a new bar, that changes what 2.0.0_SA_COO~ZZ's cells must prove.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** THE GRADE TABLE, READ FROM THE COMMITTED ARTIFACT. *** ROUND_ANALYSIS.round2.md:29-40 grades eleven outcomes REALIZED and one NOT REALIZED, and each row carries its own DONE WHEN state. EIGHT OF THE ELEVEN REALIZED GRADES SIT ON AN `EXERCISED` BAR: FWD-1, FWD-3, FWD-5, FWD-6, FWD-7, FWD-8, FWD-11, FWD-12. Only FWD-2, FWD-9 and FWD-10 carry APPLIED, and those three are genuinely satisfiable by a specimen -- FWD-2's bar is explicitly 'the distinction is in the report's own VOCABULARY', which a specimen can carry in full.",
        "*** THE CLAUSE THAT CANNOT BE READ ANY OTHER WAY, verbatim from the PRD at :77-:83. *** FWD-1 DONE WHEN: 'EXERCISED -- it has run on real trading mornings and its verdict has been checked against the underlying rows and found right, INCLUDING AT LEAST ONE MORNING WHERE THE VERDICT WAS \"NOTHING\"'. ⛔ THE LAST CLAUSE IS THE DECISIVE ONE AND IT DOES NOT DEPEND ON WHAT 'RUN' MEANS. It requires the verdict to DIFFER ACROSS MORNINGS -- at least one 'nothing' morning implies at least one other kind. `compose_edition.py`'s facts are ROW_FACTS, a hard-coded literal, and its own docstring says it 'does not re-run any live AWS read'. ITS VERDICT IS THE SAME EVERY MORNING BY CONSTRUCTION. Even granting the most generous reading of 'run on real trading mornings' -- a person invoking it by hand on a Tuesday -- the varying-verdict clause remains unsatisfiable.",
        "FWD-3 IS THE SAME SHAPE AND CONFIRMS IT IS NOT A ONE-ROW ODDITY. DONE WHEN: 'EXERCISED -- a reader HAS USED IT to tell a new problem from one that has been standing FOR WEEKS.' That requires a series of editions over weeks whose content CHANGES, plus a reader who consumed them. A frozen snapshot re-rendered daily is not a series; every edition in it is identical, so no reader could distinguish a new problem from a standing one no matter how many mornings passed.",
        "⚠ THE DISTINCTION THAT KEEPS THIS FAIR, AND IT CUTS AGAINST MY OWN CASE IN ONE PLACE: `COMPLETION_REPORT.round3.json` claims `COVERED`, not `REALIZED` -- that is 2.0.0_SA_COO~ZZ's COVERAGE claim (a cell served the outcome) and NOT a grade, and nothing here is a finding against that lane. The REALIZED grades are 1.0.0_SA_CTO~Z's, in ROUND_ANALYSIS.round2.md. THIS ROW IS AGAINST THE GRADE LIMB ONLY. I read the completion report FIRST and nearly filed against the wrong artifact on a COVERED/REALIZED conflation.",
        "⛔ SO THE CONSEQUENCE FOR FWD-13 IS NOT WHAT THE ADDENDUM ASSUMES. Msg 20948 s.3 rules that 'FWD-1..FWD-12 are NOT re-opened and NOT re-graded ... FWD-13 is a NEW bar, not a re-litigation of the old ones.' FOR THE THREE APPLIED OUTCOMES THAT IS EXACTLY RIGHT and this row does not touch them. FOR THE EIGHT EXERCISED ONES IT IS NOT A NEW BAR -- IT IS THE BAR THEY ALREADY CARRIED, and the grade said it was met. A new outcome numbered 13 does not retire a grade recorded against outcome 1.",
        "⭐ AND THE REASON THIS MATTERS BEFORE THE CUT RATHER THAN AT L9: if FWD-13 is read as wholly new, its cells prove only that the NEW edition runs live, and the eight EXERCISED grades keep standing on a specimen. If it is read as partly a re-grade, the same deployment EXERCISES all eight at once and the cells cost no more -- the difference is entirely in what the round is allowed to CLAIM afterwards, not in what it has to BUILD. ⚠ THE CHEAP OUTCOME AND THE HONEST ONE ARE THE SAME ACT HERE, WHICH IS WHY IT IS WORTH FIXING NOW.",
        "WHAT IS NOT DISPUTED, STATED SO THE ROW IS NOT READ WIDER THAN IT IS: the addendum's own measurements (compose_edition.py at 1 location and 0 across 6,415 infra files; zero live reads; the live emailer's July vintage; 0 of this project's 74 files naming either live job) are ACCEPTED and were the trigger for this read. The specimen-not-replacement framing is accepted and is the right one. The empty round-3 recut stands. FWD-4's APPLIED grade is untouched. ⭐ AND THE SEAT THAT WROTE THE LESSON CLAIMED IT AS ITS OWN BEFORE ANY GRADER RAISED IT, which is why this row sharpens that lesson rather than opposing it."
      ]
    },
    "spec_asserts": "Msg 20948: 'no outcome asked whether the thing being graded could produce tomorrow's edition. The question was absent from the spec, so no grader could have caught it' -- and correspondingly that FWD-13 is a new bar rather than a re-litigation of FWD-1..FWD-12.",
    "world_is": "Eight of the eleven REALIZED grades sit on DONE WHEN = EXERCISED, and FWD-1's bar names real trading mornings and a varying verdict in plain words. The question was in the spec, written in the outcomes' own DONE WHEN clauses, and a grader reading the bar against the artifact could have caught it.",
    "notes": "⛔ THIS IS NOT A CLAIM THAT THE GRADES WERE CARELESS, and the row would be worse if it were. The specimen was verified against REAL round-1 findings and the artifacts genuinely do what the ACCEPT paragraphs describe; what was not tested is whether the thing carrying them could ever run again tomorrow. THAT IS RULE 22'S STATE AXIS EXACTLY -- APPLIED was demonstrated and read as EXERCISED -- and it is the estate's most-repeated defect, appearing here on a bar that NAMED the exercise it wanted. || ⭐ THE TRANSFERABLE FORM, WHICH IS WHY THIS IS FILED RATHER THAN LEFT IN A MESSAGE: A BAR THAT SAYS `EXERCISED` DOES NOT ENFORCE ITSELF. Eight outcomes carried the word, one artifact could satisfy none of them, and every grade still read REALIZED -- because the grader checked the ACCEPT paragraph (what the report SHOWS) and not the DONE WHEN state (that it has RUN). The two live in adjacent lines of the same block and only one of them was graded against. || NO ACT IS ASKED OF 2.0.0_SA_COO~ZZ and the decomposition should NOT wait on this: the cells are the same either way, per the evidence above."
  }
]
```

## Z-W1-S7 -- AC2 ("THE CELL") and AC4 are unsatisfiable by ANY port that honours the cell's own "main() does NOT travel" bound, because the frozen row shape never carries `delta` and only main()'s excluded loop ever attached it

```json
[
  {
    "id": "NFRA_REPORT-Z-W1-S7",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_REPORT~1",
    "surfaced_at": "2026-09-10T15:07:18Z",
    "one_line": "TO-RP-s-21's AC2 (THE CELL) and AC4 invoke port.compute_verdict()/render_markdown() directly on spec.ROW_FACTS-shaped rows, but ONLY main() (specimen :549-555, explicitly excluded -- 'main() does NOT travel') ever attaches r['delta']; the identical call against the UNMODIFIED specimen itself raises the same KeyError, so this is not a porting defect -- the two invocations cannot pass for any implementation that honours the cell's own bound.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~ZZ -- issuer of TO-RP-s-21 (and, per the cell's own text, of the sibling RP-s-22 mapper cell whose output is the plausible place the delta-attach step belongs); only the issuer/L9 can decide whether AC2/AC4 are recut to run against a caller that attaches delta first, or the port's scope is widened to include that step, or the criteria are accepted as testing a not-yet-assembled pipeline.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/compose_edition.py:388-396 @20327a663f652cde867f0962206f346b2e6d3a60 -- compute_verdict(rows) reads `r[\"delta\"]` directly (`worse_rows = [r for r in real_rows if r[\"delta\"] == \"worse\"]`) with no fallback and no computation of its own.",
        "compose_edition.py:76-331 @20327a663f652cde867f0962206f346b2e6d3a60 -- every ROW_FACTS entry's own literal keys are exactly {property, attribution, family, prev, curr, citation, evidence[, illustrative]}; none carries a 'delta' key. Confirmed by direct introspection: `sorted(rows[0].keys())` on a freshly loaded spec.ROW_FACTS returns `['attribution','citation','curr','evidence','family','prev','property']`, no 'delta'.",
        "compose_edition.py:548-559 @20327a663f652cde867f0962206f346b2e6d3a60 (main()) is the ONLY code in the specimen that ever sets `r[\"delta\"]`/`r[\"rule_note\"]`, in a loop over ROW_FACTS run once before compute_verdict()/render_markdown() are ever called. The cell's own text: 'main() does NOT travel.'",
        "REPRODUCED AGAINST THE UNMODIFIED SPECIMEN, INDEPENDENT OF ANY PORT: `spec=load(compose_edition.py); spec.compute_verdict(spec.ROW_FACTS)` (no main() run first) raises `KeyError: 'delta'` at compose_edition.py:394's list comprehension -- run in C:/tmp/wk-report-4-1 this session, 2026-09-10. This is the SAME error AC2's invocation hits when it calls the equivalent `port.compute_verdict(rows)` on rows drawn from the same un-annotated spec.ROW_FACTS.",
        "AC2's own invocation verbatim (TO-RP-s-21 <proof_of_spec>): `rows=spec.ROW_FACTS; na,br,wr=port.compute_verdict(rows); got=port.render_markdown(rows,na,br,wr,...)` -- never runs main()'s delta-attach loop or any equivalent before the first call. AC4's invocation does the same via `port.render_markdown(base,*port.compute_verdict(base),vintage='V')`.",
        "This worker's port (infra/aws/lambda/infrastructure_monitor/edition.py, verbatim one-for-one lift of compute_delta/compute_delta_watch/compute_verdict/fmt_state/gen_sentence/render_markdown, no behavior change) run against AC2's exact invocation this session: `KeyError: 'delta'` at edition.py:107 (the ported compute_verdict), identical shape, both AC2 and AC4, stable across 2 consecutive runs each.",
        "AC1 (DEFINED=6 of 6 MISSING=[]), AC3 (BIG_UPPERCASE_DATA_LITERALS=0), AC5 (NON_STDLIB=0) and AC6 (NON_ASCII_LINES=0) all PASS against this same port, ruling out an absent-file or malformed-module explanation for AC2/AC4's failure -- the module is present, complete, stdlib-only and ASCII-clean; only the two criteria that call compute_verdict() on raw ROW_FACTS-shaped rows fail."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RP-s-21 AC2 ('THE CELL'): fed the specimen's own ROW_FACTS rows at a fixed vintage, `port.compute_verdict(rows)` then `port.render_markdown(rows,...)` should reproduce `spec.render_markdown(rows,...)` exactly (IDENTICAL=True, table line counts equal and >0). AC4 expects the same call shape to discriminate on row-list size. The cell's own bound: 'ROW_FACTS does NOT travel. main() does NOT travel... The module is pure functions over arguments its caller supplies' and 'THE ROW SHAPE IS FROZEN and you may not change it... render_markdown must accept exactly the row dicts the specimen's ROW_FACTS entries already are.'",
    "world_is": "spec.ROW_FACTS-shaped rows never carry a 'delta' key (confirmed by direct key introspection); only main()'s excluded loop ever attaches one. AC2's and AC4's own invocations call compute_verdict()/render_markdown() directly on that un-annotated shape, so both raise KeyError: 'delta' on the FIRST call, before any comparison to the specimen's output is possible -- reproducibly, on the unmodified specimen module itself and not only on this worker's port. Measured this session: AC1 PASS (DEFINED=6 of 6), AC2 FAIL (KeyError, rc=1), AC3 PASS (BIG_UPPERCASE_DATA_LITERALS=0), AC4 FAIL (KeyError, rc=1, same cause), AC5 PASS (NON_STDLIB=0), AC6 PASS (NON_ASCII_LINES=0).",
    "notes": "NOT crossed to make AC2/AC4 pass: this worker did NOT fold main()'s delta-attach loop into compute_verdict() (which would (a) exceed the specimen's own compute_verdict body at :388-396, the exact ported range the cell names, and (b) reintroduce, under a different function name, precisely the wiring the cell's own bound excludes -- 'main() does NOT travel'). Doing so might make AC2's script stop crashing (rows mutated in place before spec.compute_verdict(rows) runs on the same objects), but it would do so by adding scope the cell never asked for, not by porting more faithfully. Filed instead of worked around, per this project's own standing instruction not to change the frozen row shape or smuggle excluded logic elsewhere. TO-RP-s-21's <status> stays OPEN on this worker's own proof-of-spec instance because AC2 and AC4 are recorded FAIL as measured; AC1/AC3/AC5/AC6 PASS. The likely resolution lives in RP-s-22 (the parallel mapper cell the TO names as building 'against that shape RIGHT NOW') or RP-s-23 (the lambda_function.py wiring cell) -- whichever of them is the caller responsible for attaching `delta` before calling into this module -- but naming that is a judgment for the issuer/L9, not something this cell's paths authorize this worker to decide or build."
  }
]
```
