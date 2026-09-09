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
  }
]
```
