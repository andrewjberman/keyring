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
  }
]
```
