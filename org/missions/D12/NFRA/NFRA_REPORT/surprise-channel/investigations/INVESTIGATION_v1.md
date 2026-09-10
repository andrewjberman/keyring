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
  }
]
```
