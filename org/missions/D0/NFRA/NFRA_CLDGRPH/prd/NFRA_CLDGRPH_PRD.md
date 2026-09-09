# NFRA_CLDGRPH -- Cloud-resident KuzuDB projection + gateway traversal: agents traverse ONE cloud graph, and no machine is in the compile business

```json
{
 "project": "NFRA_CLDGRPH",
 "directive": "D0",
 "fabric": "laptop",
 "prd_version": "v0.5",
 "step": 4,
 "brief_ref": "docs/briefs/globgrph-cloud-compile-and-gateway-traversal-20260901.md@dfd24a010b",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8"],
 "status": "RATIFIED"
}
```
*PRD_HEADER block -- schema `org/standards/PRD_HEADER.schema.json`. First fenced block in the file by contract; it is what the COO monitor and the step-6 gate's limb 5 read. `status: RATIFIED` = step 5 may proceed (Andrew ratified the endpoint and rulings R1-R4 on 2026-09-02). `fabric: laptop` is Andrew's word -- 2026-09-02 ~19:3xZ at this terminal, verbatim "laptop" -- and the register row (`org/missions/D0/NFRA/NFRA_CLDGRPH/project.json`; generated flat index `org/projects/NFRA_CLDGRPH.json`) carries the same key; the gate compares the two.*

**Limb:** L4 of `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`. **Brief:** `docs/briefs/globgrph-cloud-compile-and-gateway-traversal-20260901.md` @dfd24a010b (`4.0.0_SA_CRO`, step 1, mode NEW). **Fabric:** laptop (Andrew-direct 2026-09-02 ~19:3xZ, verbatim "laptop"; directive D0 member; criterion (b), infra local). **Status:** PRD v0.4 -- `1.0.0_SA_CTO~A` -- 2026-09-03 ~05:3xZ -- LANDED AT THE TREE HOME as L4 of the second, parallel canonical run (Andrew-direct at this terminal ~05:1xZ, record @8e134cc126; L3 tree registration @36157989a9); step-2 ENDPOINT RATIFIED by Andrew-direct at this terminal (2026-09-02 ~17:5xZ "I agree with all of these"; ~18:3xZ "I agree with all your recs"); step 5 decomp LANDED by `2.0.0_SA_COO` @05d2c89158 (13 cells, no TO cut); v0.2 adds the PRD_HEADER block and s.7 so the step-6 gate's limb 5 (@689960ce16) admits a TO against this PRD. **Directive:** D0 Agent Infrastructure. **Macro:** `NFRA`. **Step-2 record + assessment:** `org/tier1_exec/1.0.0_SA_CTO~A/deliverables/ENDPOINT_FORWARD_GLOBGRPH_CLOUD_COMPILE_20260902.md` @082c90a610. **Surprise channel (Rule 27):** `3.0.0_SA_CVO~A` (this run's L8-L10 seat); rows at `org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/`.

## ENDPOINT (step 2, /endpoint --forward)

*Brief: docs/briefs/globgrph-cloud-compile-and-gateway-traversal-20260901.md @dfd24a010b
(4.0.0_SA_CRO, 2026-09-01 19:49Z). Emitted by 1.0.0_SA_CTO~A 2026-09-02; RATIFIED by Andrew
2026-09-02 ~17:5xZ; FWD-2 amended in place on his word ~18:3xZ. FWD-n ids are PERMANENT and
never reused; a retired outcome leaves its number vacant.*

*"the graph" here means the KuzuDB projection -- the copy agents query -- not the Nessie/Iceberg
tables it is projected from (Andrew-direct 2026-09-02 ~17:5xZ, verbatim: "this is the kuzudb
projection, and ... every time you reference the 'graph', that is what you are referring to").*

```
  FWD-1  Anyone can ask how the estate is wired and get an answer without ever
         building, refreshing or stitching the graph themselves
         DONE WHEN  EXERCISED -- someone who has never run a graph tool has asked
                    and been answered
         ACCEPT     a person who has never built the graph asks a question about
                    how things connect and gets the answer in the time an ordinary
                    lookup takes, with no step where they refresh or rebuild
                    anything first, and no wait they could blame on a build
         SOURCE     brief Part I O1; Part III bars 1 and 2

  FWD-2  The graph gets newer on the estate's own schedule -- nightly in full and
         within minutes of any cloud change -- never because someone asked
         DONE WHEN  EXERCISED -- the schedule has fired on its own at least once
                    and the next morning's answers carry that night's date
         ACCEPT     left completely alone overnight, the graph is newer in the
                    morning than it was the evening before; a change made in the
                    cloud during the day shows up without anyone asking for a
                    refresh; and no question anyone asks is ever the reason a
                    rebuild starts
         SOURCE     brief Part I O2; Part IV F1 (the nightly window already has
                    five members), F4 (nothing schedules the projection today), F10
         AMENDED    2026-09-02 in place, id unchanged (Andrew: "I agree with all
                    your recs", /open-calls CALL 1 rec (b)); the ratified 17:5xZ
                    text read "on the nightly clock"

  FWD-3  Anyone reading an answer can tell how old it is, from the answer itself,
         in plain words
         DONE WHEN  APPLIED -- the age is printed in plain language wherever an
                    answer is given
         ACCEPT     a reader who knows nothing about how the graph is built can
                    say from the answer alone "this is as of last night" (or
                    whenever it is), without looking up what any label means
         SOURCE     brief Part I O3; Part III bar 3

  FWD-4  There is a ceiling on how old any answer can be, and the ceiling belongs
         to the system, not to how carefully the reader checks
         DONE WHEN  EXERCISED -- a full cycle has passed with nobody enforcing the
                    ceiling by hand and no answer served older than it
         ACCEPT     nobody can be handed an answer older than the last scheduled
                    refresh, however careless they are about reading the fine
                    print; the oldest answer available is set by the schedule,
                    not by the reader's diligence
         SOURCE     brief Part I O3b; Part IV F11 (attributed to 3.0.0_SA_CVO,
                    msg 92472), F5 (answers served about a day and a half behind
                    on today's design)

  FWD-5  A new machine or a new person can ask graph questions on arrival,
         having never held or built the database
         DONE WHEN  EXERCISED -- a machine that has never held the graph has
                    asked and been answered
         ACCEPT     setting up a second computer adds a reader, not a build;
                    somebody on a fresh machine gets the same answer as everyone
                    else on their first try
         SOURCE     brief Part I O4; Part III bar 6; Part IV F9 (the P4
                    build-once-distribute ancestor)

  FWD-6  Nobody chooses a refresh mode
         DONE WHEN  APPLIED -- the full-versus-incremental choice no longer
                    appears anywhere an ordinary user works
         ACCEPT     there is no question a person can be asked, and no command
                    they can be told to type, about which kind of refresh to run;
                    someone who has never heard of the difference cannot make the
                    wrong choice, because there is no choice
         SOURCE     brief Part I O5; Part II (the ratified split becomes
                    invisible, not wrong)

  FWD-7  The estate keeps one graph story, and the per-machine copy is retired
         rather than kept alongside
         DONE WHEN  EXERCISED -- two people on different machines have asked the
                    same question at the same moment and received the same
                    answer, after the local copy was switched off
         ACCEPT     turning off every developer machine does not change what the
                    graph says; two people asking the same question at the same
                    moment get the same answer; and there is no second, older
                    copy anyone could still be reading from
         SOURCE     brief Part I O6; Part III bar 4; Part II boundary (a PORT
                    WITH A RETIREMENT, or a violation of the no-shadow-pipeline
                    rule); Part V item 3

  FWD-8  An operator can see that last night's refresh happened, and can see
         when it did not, without rerunning anything
         DONE WHEN  EXERCISED -- the answer has been read on a real morning, and
                    a night that did not run reads differently from one that did
         ACCEPT     an operator asking "did the graph refresh last night" gets a
                    plain yes or no with a time, and a missed night looks
                    different from a completed one; nobody has to run anything
                    to find out
         SOURCE     brief Part I O7; Part IV F6 (today's status surface points at
                    the wrong artifacts); Part VII item 3 (a rule being ENABLED
                    is not a run having happened)
         MECHANISM  RULED 2026-09-02 (s.6 R4): a PULL-style status READ of the
                    projection pointer's own manifest. No alarm, SNS, checker or
                    monitor. Not in conflict with the standing moratorium.

  NOT AN OUTCOME OF THIS PROJECT -- graph COVERAGE (whether every real thing in
  the estate is in the graph at all). Brief Part IV F12: a fresh graph that lacks
  a node is still silent about that node; coverage has a separate owner and a
  separate filed record (ADVI_PERFRP-S18 @3eb00f5905). A step-10 row citing
  coverage against any FWD above is misrouted, not a scope change.
```

## 1. The arc

It starts from a measured fact the brief established and this PRD does not re-measure: the PRODUCER side of the estate graph is already in the cloud and already on a schedule (nightly derive, an intraday incremental updater, the stitch and three producers, all landing in Nessie/Iceberg tables and all ending at one branch-head marker), and the ONE thing still local is the KuzuDB projection -- a 47 MB embedded database that nothing schedules, that whichever agent arrives first rebuilds, and that today can serve answers a day and a half behind its source while every label on it is honest. **Stage 1** makes the projection a consumer of the marker: the write that already ends every producer becomes the event that starts the projection worker, which runs the incremental engine the estate already certifies and publishes a versioned artifact with its vintage to S3. **Stage 2** stands up the serving plane -- a small always-on service on the existing globgrph cluster holding the current artifact and answering Cypher inside the VPC, with the gateway as a thin proxy through its existing integration framework -- so a seat, a new machine, or a second device reaches the graph the way it reaches any other governed integration. **Stage 3** is the retirement: the local projection and the local full/incremental rebuild commands go away, the estate's query tool becomes a thin client that prints the vintage in plain words, and the operator status surface is repointed at the artifact that is actually served. It ends when the eight outcomes above read at their bars -- six exercised, two applied -- and there is no second, older copy anyone could still be reading from.

## 2. Purpose -- what DONE means

Anyone in the estate can ask how things are wired and get an answer that is at most a schedule old, without having built, refreshed or waited for anything; turning every developer machine off changes nothing about what the graph says; and an operator can tell, without rerunning anything, whether last night's refresh happened.

## 3. Territory -- what this owns, and what it only relies on

**Owns:** where the KuzuDB projection is COMPILED (the worker and its trigger), where it is SERVED FROM (the serving plane and its artifact/pointer contract), how an agent REACHES it (the gateway path and the thin client), the vintage bound and its plain-words rendering, the operator status read, and the RETIREMENT of the local copy.

**Relies on, unchanged, and must not reopen** (brief Part II, adopted):

| surface | owner | relationship |
|---|---|---|
| the AWS derive (live scan -> graph tables), nightly + incremental | `NFRA_GLOBGRPH` (CLOSED-COMPLETE 2026-06-16) | upstream; untouched |
| Nessie / Iceberg warehouse + catalog, the branch-head marker (`_provenance.stamp_marker`) | `NFRA_GLOBGRPH` | the source of truth AND the trigger; untouched |
| the stitch derive + graphuni producer fold | `NFRA_GLOBGRPH` P2-STITCH / `NFRA_GRAPHUNI` | upstream; already cloud + nightly |
| the `full` / `inc` split semantics, O-1 serve-labeled-stale | `NFRA_KUZUSPLIT` (RATIFIED 2026-07-17) | survives intact, moves INSIDE the worker; invisible to agents (FWD-6) |
| gateway extension framework (IntegrationSpec, AuthKinds, audited runner) | `NFRA_INTEGRATIONS` | relied on; a new integration is ADDED through its 5-step checklist, the framework is not modified |
| gateway auth / OAuth-AS, single-worker pin | gateway PRD (OPLMCP.06 / CTO D5a) | relied on; the gateway never hosts the database |
| ECS cluster `opal-globgrph` (Nessie + Trino services live) | `NFRA_GLOBGRPH` | the serving plane is one more small service on it |
| partner/client GraphQL | `D6_OPAL_ANALYST` | a DIFFERENT consumer; not this |

**Sibling projects:** `NFRA_GLOBGRPH` · `NFRA_KUZUSPLIT` · `NFRA_GRAPHS` · `NFRA_GRAPHUNI` · `NFRA_INTEGRATIONS` · `D6_OPAL_ANALYST`.

## 4. Acceptance properties

Each is disputable, none carries a number, and each names the outcome it discharges.

1. **A never-compiled seat gets an answer.** Someone at a seat that has never run a graph tool asks how two things are connected and gets the answer in the time an ordinary lookup takes, with no refresh step. (FWD-1)
2. **The graph moves without being asked.** Left alone overnight it is newer in the morning; a cloud change made during the day is visible without anyone requesting a refresh; and no question is ever the cause of a rebuild. (FWD-2)
3. **Age reads in plain words.** From the answer alone, a reader who knows nothing about the build can say when the graph is from. (FWD-3)
4. **The ceiling holds by itself.** Over a full cycle with nobody enforcing it by hand, no one is handed an answer older than the last scheduled refresh. (FWD-4)
5. **A fresh machine is a reader, not a builder.** A machine that has never held the database asks and gets the same answer as everyone else on its first try. (FWD-5)
6. **There is no refresh choice to get wrong.** No command or question about which kind of refresh to run exists where an ordinary user works. (FWD-6)
7. **One story, no older copy.** With every developer machine off, two people on two machines ask the same question at the same moment and get the same answer, and there is no local copy left that either could have read instead. (FWD-7)
8. **"Did it refresh last night" is a read, not a rerun.** An operator gets a plain yes or no with a time, and a missed night looks different from a completed one. (FWD-8)
9. **The port carried nothing it should have fixed.** The known key-handling defect in the loader is closed at the port, not inherited by it. (s.6 R10)

## 5. Out of scope

- **Graph COVERAGE** -- whether every real thing is in the graph at all (brief F12; filed separately as `ADVI_PERFRP-S18`). A fresher graph is not a more complete one.
- The AWS derive, the Nessie/Iceberg tables, the stitch derive, the incremental updater and the marker contract -- relied on, not modified.
- The `full`/`inc` split semantics and the O-1 ruling -- preserved, relocated inside the worker.
- Any alarm, alarm class, SNS send, freshness checker or monitor. FRESHGUARD's watchdog and per-producer alarm legs stay torn down on their own ruling (@858554332d, Andrew (A) remove all Class-A); this project does not re-arm them and does not build a sibling.
- The gateway's authorization model -- relied on; agent traversal is registered through the existing framework, not by changing it.
- Client-facing GraphQL (`D6_OPAL_ANALYST`).
- The comp-trace layer cache (`.comp-graph/graph.json`) -- a different artifact with a different mechanism (brief F11 bound 2).
- Trino as a graph engine, and any re-dialecting of consumers (s.6 R6).
- Benchmarks and timings beyond the one measurement the decomp needs to size the worker (s.6 R5).

## 6. Rulings that BIND

- **R1 -- Andrew-direct 2026-09-02 ~17:5xZ (CTO~A terminal):** FWD-1..FWD-8 ratified as written; *"the graph"* throughout = the KuzuDB projection, not the Nessie/Iceberg tables.
- **R2 -- Andrew-direct 2026-09-02 ~18:3xZ (`/open-calls` CALL 1):** FWD-2 widened in place to the estate's own schedule (nightly in full, within minutes of any cloud change).
- **R3 -- Andrew-direct 2026-09-02 ~18:3xZ (CALL 2):** the SERVING PLANE is a small ALWAYS-ON service on the existing `opal-globgrph` ECS cluster holding the current artifact and swapping on pointer advance; the gateway (`i-07dccb1615503ac99`, t4g.nano, `--workers 1` mandatory) is a THIN PROXY through the IntegrationSpec pattern and never the host. This is a scoped exception to the GLOBGRPH s.0 serverless-light lock on the same footing as Nessie warm (GLOBGRPH PRD s.2a Item-1); the cost delta lands on the NFRA accounting line (s.5a class).
- **R4 -- Andrew-direct 2026-09-02 ~18:3xZ (CALL 3):** FWD-8's mechanism is a PULL-style status READ of the projection pointer's own manifest (the repoint of the mis-aimed `comp-graph status`, brief F6). No alarm, SNS, checker or monitor. FRESHGUARD's alarm legs remain torn down.
- **R5 -- CTO 2026-09-02 (architecture):** the projection's TRIGGER is the branch-head marker write -- an S3 event notification on `warehouse/_branch_head.main.json` -> an SQS queue with DLQ (the item2b pattern) -> a worker running the existing `kuzu_incremental_refresh` logic (copy current, apply delta, count-guard, fall back to the full load on a large delta) -> a versioned artifact + `_build_manifest` on S3, ONE pointer object advanced last. NOT the CloudTrail queue (that is one writer of five) and NOT a cron of its own (the marker is the commit point, artifact-first-marker-last, so the projection can never run ahead of Nessie). Measured input for sizing: 45 marker stamps / 102 incremental invocations in the 24h to 2026-09-02 ~18:0xZ; the worker's runtime (Lambda vs ECS task) is decided by the MEASURED full-fallback duration, not the document claim.
- **R6 -- CTO 2026-09-02:** Cypher is preserved and Kuzu remains the engine. Every consumer (`comp-kuzu`, `comp-blast`, `comp-find --corpus aws`) writes Cypher against `CloudNode`/`CloudEdge`; Trino is a SQL engine over the same tables and is not a graph engine. Re-dialecting consumers would be a second project.
- **R7 -- standing (CLAUDE.md s.5, NEVER shadow pipeline):** this is a PORT WITH A RETIREMENT. The local `kuzu_nessie_db`, the local `kuzu_nessie_load` / `kuzu_incremental_refresh` invocation paths and the `comp-kuzu-full` / `comp-kuzu-inc` local rebuild commands RETIRE when FWD-7 reads EXERCISED; indefinite coexistence is the duplicate output path the rule forbids. The decomp names the retirement cell and its order relative to the serving plane.
- **R8 -- inherited:** GLOBGRPH PRD s.0 Andrew-locked decisions stand; s.2b F5 read-your-own-writes doctrine stands (verification of one's own change goes to the served artifact / live AWS, never the graph); s.2b F6 the marker is the HEAD oracle.
- **R9 -- inherited + recorded:** `NFRA_KUZUSPLIT` O-1 (serve-labeled-stale, never full, for the incremental path) stands as WORKER-INTERNAL behaviour. `NFRA_KUZUSPLIT` O-4 / P4 (build-once-distribute) was never specifically ruled (the 2026-07-17 relay said "proceed per PRD rec" against a call carrying no rec) and is SUPERSEDED by this project with a wider ask.
- **R10 -- CTO 2026-09-02:** the `kuzu_nessie_load` node/edge key asymmetry (substrate card @5da9e7fffc, verdict QUALIFIED) is FIXED at the port, not carried. The port is the moment.
- **R11 -- inherited (CLAUDE.md Rule 20; NFRA_GRAPHS s.4):** READ path is the agent default; the WRITE path is scheduled or triggered. This project closes the last place where an agent's read silently triggers a write.
- **R12 -- placement:** LAPTOP. D0 is one of the six named laptop holds (Andrew-direct 2026-08-27 ~00:0xZ) and criterion (b) "ontology/infra work should generally always be on this device" applies.

**Open for the decomp (inputs, not rulings):** the worker runtime once the full-fallback duration is measured; the SQS batch window; network reachability from the gateway to the serving service (VPC / subnet / SG, brief Part V item 5 -- unmeasured); IAM for the worker and the service; which existing AuthKind an agent traversal fits (brief Part V item 4); the pointer object contract and its atomicity; how the thin client renders vintage in plain words (FWD-3); the retirement sequencing (R7); and the one measurement (KUZUSPLIT P0-INSTRUMENT) that sizes the worker. None of these is a decide-first specification question: each resolves by a measurement or by reading an existing framework, and each is carried by a `verify` row (S10-S13) or by a cell the decomposition owns -- the PRD carries no open decision into L5.

- **R13 (addendum v0.5, 2026-09-09, `1.0.0_SA_CTO`): no globgrph task family references a MUTABLE image tag; every image act's change-management entry names every family that pulls the tag it moves.** The PRD half of S31's remedy; the law half stands at CLAUDE.md NEVER-2 (@`b00a69a676`). Binds S18 and every later image act on this chain.

## 7. SURFACE MANIFEST (step 4 -> step 5)

**Provenance, read before citing any cell.** The rows below are `2.0.0_SA_COO`'s step-5 rectangle (`org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_CLDGRPH_DECOMP_20260902.md` s.1 @05d2c89158), **lifted into this PRD as gate on 2026-09-02 ~19:2xZ** at that seat's offer (msg 92706: *"lift it into s.7 verbatim or amend it as gate"*). v0.1 of this PRD was authored from a template that carried no manifest section; the decomp therefore built the manifest itself, and the PRD adopts it so the two carriers hold ONE id space. **Every pin and measurement in the `evidence` column is the COO's unless marked `CTO~A`**; this seat re-read the OWNS mapping (postulate i) and the acceptance references and changed nothing in them.

**Amended as gate, exactly two cells, both to the contract's `verb` enum (`port | classify | wire | align | retire | verify`):** S9 `fix-at-port` -> `align` (the loader is aligned to the key rule at the port; R10 unchanged); S10 `measure` -> `verify` (a measurement is the `verify` act on an `unmeasured` row). Lanes expanded from the decomp's short forms to full serials. Nothing else differs from @05d2c89158.

**Domain (postulate i):** the s.3 **OWNS** cell, six items. RELIES-ON items appear only as `depends_on`; out-of-scope only as `bound`.

```
  OWNS item                                     rows
  where it is COMPILED (worker + trigger)       S1, S2
  where it is SERVED FROM (plane + contract)    S3, S4
  how an agent REACHES it (gateway + client)    S5, S6
  the vintage bound + plain-words rendering     S6 (render), S3 (the bound)
  the operator status read                      S7
  the RETIREMENT of the local copy              S8
  FORWARD   every OWNS item has >=1 row ......... 6 of 6 covered, 0 uncovered   (COO, re-read CTO~A)
  REVERSE   every work row maps to an OWNS item . S1-S8 all map; S9 maps to acceptance 9 (R10)
  OUTCOMES  every FWD-n has >=1 owned surface ... 8 of 8 (FWD-1 S4/S5; FWD-2 S1/S2; FWD-3 S3/S6;
                                                  FWD-4 S2; FWD-5 S4/S5; FWD-6 S6; FWD-7 S3/S4/S8; FWD-8 S7)
  S10-S13 are INPUTS the s.6 "Open for the decomp" list names -- verify rows, not work.
  CAVEAT (postulate i): 6 of 6 certifies coverage of the OWNS cell AS WRITTEN; a manifest can be
  MECE over a domain that is itself incomplete (the ETFS_GUARDRAIL S13/Orion instance, same day).
```

| id | outcome | surface | claim | evidence | lane | verb | depends_on | acc | bound |
|---|---|---|---|---|---|---|---|---|---|
| S1 | FWD-2 | S3 event notification on `warehouse/_branch_head.main.json` -> SQS + DLQ | **absent** | comp-trigger: NO MATCH; lens BLIND on S3-notification triggers by its own disclosure. CTO~A: the marker is stamped by `_provenance.stamp_marker` (`infra/aws/globgrph/_provenance.py:194` @c778e3c3d1); 45 stamps / 102 updater invocations in the 24h to 2026-09-02 ~18:0xZ (CloudWatch) | `0.7.0_AE_CloudOps` | wire | S12 | 2 | **R5: the marker write is the commit point.** NOT the CloudTrail queue (one writer of five), NOT a cron. item2b pattern (`infra/aws/terraform/globgrph/item2b.tf:175`) |
| S2 | FWD-2, FWD-4 | worker running the existing incremental engine -- `infra/aws/globgrph/kuzu_incremental_refresh.py` | measured | 350 lines @aebe0d0a67 | `0.7.0_AE_CloudOps` | port | S1, S10 | 2, 4 | **KUZUSPLIT O-1 (serve-labeled-stale, never full) survives as WORKER-INTERNAL** (R9). Runtime Lambda-vs-ECS is decided by S10, never by the document |
| S3 | FWD-3, FWD-7 | versioned artifact + `_build_manifest` + ONE pointer object on S3 | **absent** | contract not yet written; PRD names it as open | `0.7.0_AE_CloudOps` | wire | S2 | 3, 7 | **artifact-first, pointer-last** -- the projection can never run ahead of Nessie. Pointer atomicity is an open input (S11). Bucket versioning is Andrew-locked OFF (GLOBGRPH s.0 #5), so the pointer is the one mutable object |
| S4 | FWD-1, FWD-5, FWD-7 | small always-on service on the existing `opal-globgrph` ECS cluster | **absent** | cluster ACTIVE, 2 services / 3 tasks (CRO brief F2; re-read CTO~A 2026-09-02 via `comp-find --corpus aws`, `active_services: 2`, 96 globgrph nodes / 2,100). Cluster resource `infra/aws/terraform/globgrph/nessie.tf:14`; service pattern `:196` | `0.7.0_AE_CloudOps` | wire | S3, S11, S12 | 1, 5, 7 | **R3: scoped exception to GLOBGRPH s.0 serverless-light**, same footing as Nessie warm. Cost delta -> NFRA line. **The gateway is NEVER the host** |
| S5 | FWD-1, FWD-5 | gateway traversal registered via `IntegrationSpec` (existing framework) | **absent** | framework proven by 2 live integrations (`opal_portal`, `ycharts`): `infra/aws/ec2/opal-gateway/app/integrations/registry.py:23-35` @c778e3c3d1 | `0.7.0_AE_CloudOps` | wire | S4, S13 | 1, 5 | **The framework is NOT modified** -- a new integration through its 5-step checklist. Gateway `i-07dccb1615503ac99` t4g.nano, `--workers 1` MANDATORY: thin proxy only. `ENABLED_INTEGRATIONS` flip is CTO-arch-gated (`registry.py:34`) |
| S6 | FWD-3, FWD-6 | `.tools/comp-kuzu` becomes a thin client that prints vintage in plain words | measured | 28 lines @0215abf3ec; target today `infra/aws/globgrph/kuzu_cli.py:30` -> `_canonical.CANONICAL_DB_PATH` (`_canonical.py:42`) | `0.8.0_AE_CloudComp` | port | S4 | 3, 6 | **FWD-6: no refresh choice may exist where an ordinary user works.** Plain-words rendering is an open input |
| S7 | FWD-8 | operator status read -- repoint `comp-graph status` at the projection pointer's manifest | **absent** | brief F6: it reports on the WRONG artifacts today ("kuzu_db 81d", "stitch_graph 38d"); source `org/modules/graph/graph_status_cli.py:214-232` @c778e3c3d1 (CTO~A) | `0.8.0_AE_CloudComp` | wire | S3 | 8 | ⛔ **R4: a PULL-style READ. NO alarm, SNS, checker or monitor.** FRESHGUARD alarm legs stay torn down (@858554332d) |
| S8 | FWD-7 | RETIREMENT: local `kuzu_nessie_db`; `kuzu_cli.py`; `.tools/comp-kuzu-full`; `.tools/comp-kuzu-inc`; the `_canonical.py:344-420` rebuild/labeled-stale seam and its `kuzu_nessie_db.fallback.jsonl` sink | measured | `kuzu_cli.py` 179 @834c87c00a; `comp-kuzu-full` 16 + `comp-kuzu-inc` 17 @7288d12675; `_canonical.py` 647 @c778e3c3d1 (CTO~A) | `0.8.0_AE_CloudComp` | retire | S4, S6 | 7 | ⛔ **R7: PORT WITH A RETIREMENT.** Indefinite coexistence IS the duplicate output path CLAUDE.md s.5 forbids. Fires when FWD-7 reads EXERCISED -- not before, not never |
| S9 | acceptance 9 | `kuzu_nessie_load.py` node/edge key asymmetry | measured | 417 lines @e445642c5f; substrate card @5da9e7fffc verdict QUALIFIED, defect at `:150` vs `:184` (re-locate by content) | `0.7.0_AE_CloudOps` | align | S2 | 9 | **R10: FIXED AT THE PORT, not carried.** The port is the moment; a ported defect is a defect shipped twice |
| S10 | -- | **the full-fallback duration of the projection** (KUZUSPLIT P0-INSTRUMENT) | **unmeasured** | PRD names it the first measurement owed | `0.7.0_AE_CloudOps` | verify | -- | -- | ⛔ **SIZES S2.** Four figures from three sources exist for two different operations and CRO deliberately refused to reconcile them. **Do not pick one -- measure** |
| S11 | -- | gateway -> serving-service network reachability (VPC / subnet / SG) | **absent** | brief Part V item 5: UNMEASURED | `0.7.0_AE_CloudOps` | verify | -- | -- | If unreachable, S5's whole shape changes. Verify BEFORE S4 is built, not after |
| S12 | -- | IAM for the worker and the serving service | **unmeasured** | -- | `0.7.0_AE_CloudOps` | verify | -- | -- | ⛔ **comp-iam CANNOT answer "is this denied?"** -- silence from it is not "allowed"; run `comp-iam refresh-census` before any APPLIED-plane read |
| S13 | -- | which existing `AuthKind` an agent traversal fits | **unmeasured** | brief Part V item 4 | `0.7.0_AE_CloudOps` | verify | -- | -- | An answer here is a precondition for S5, not a detail of it |
| S14 | FWD-2, FWD-4 | (by reference, decomposition v0.3 CG-s-14 @`2dd381d969`'s recut) the DERIVER reports READ STATE honestly: a failed `get_bucket_notification_configuration` is UNREADABLE, never zero; the S3_BUCKET-[TRIGGERS]->LAMBDA edge derived from the declared resources as a second source | DONE | TO-CG-C-3 @b5bc1c8b27 (round 3) | `0.8.0_AE_CloudComp` | align | S2 | 2, 4 | listed here for the ONE id space; the decomposition carried it first |
| S15 | FWD-2 | (by reference, decomposition v0.3 CG-s-15, the round-3 analysis @`2dd381d969` item 2) the SHARED IMAGE rebuilt from a HEAD carrying the C-3 fix, change-managed under NEVER-2, THIS PROJECT's three families pinned by DIGEST | DONE | TO-CG-D-1 @33f93a5215 + the eight-address apply (S40); 3 of 7 families pinned | `0.7.0_AE_CloudOps` | port | S14 | 2 | the four OTHER families are S18 below |
| S16 | FWD-2 | (by reference, decomposition v0.4 CG-s-16, the CTO's answer 94158) the derive task role GRANTED `s3:GetBucketNotification` in Terraform, change-managed | DONE | TO-CG-D-12; D1-AC5 read 171 TRIGGERS edges on the live graph after it | `0.7.0_AE_CloudOps` | wire | -- | 2 | the real cause of S20's zero (W1-S7) |
| S17 | FWD-7 | **ADDENDUM v0.5.** THE INSTRUCTION PLANE'S ROUTE BACK to the retired local surface: `org/modules/graph/graph-call-manifest.yaml` `cloud.refresh.full` (:219) and `cloud.refresh.incremental` (:233) whose `canonical_call` is `comp-kuzu --mode ...`, and the `:1783` subcommand list (`--mode auto/inc/full`, `--db-path`); `.tools/tool_index.py` help x6; `org/modules/graph/comp_aws_cli.py:2857,2866`; `comp_similar.py:591` (`corpus_db == kuzu_nessie_db`) | measured | the client REFUSES `--mode` (`kuzu_cli.py: error: unrecognized arguments: --mode`, exercised at C-S22); Rule 20 sends every seat to the manifest before an infra change (W2-S23, the row placed at 94456/A4.3) | `0.8.0_AE_CloudComp` | retire | S8 | 7 | (1) both refresh entries retired under the file's own `retired_aliases` convention with a successor entry naming the served graph; `:1783` carries no `--mode`/`--db-path`; the six help texts and the three code sites name the served graph; a refresh phrasing through `comp-which` routes to no retired entry, beside a positive control. (2) FWD-7's PERSON half: a seat on site Z asks D-8's fixed question through the public gateway inside D-8's window and matches the laptop's answer byte-for-byte under one vintage -- the roadmap's allocation; MODELLED on machines until then. **Bound:** no rebuild path re-created; W2-S27 (`projection_client` takes neither a db path nor a parameter dict) is the constraint every repoint meets |
| S18 | FWD-2, FWD-4 | **ADDENDUM v0.5.** THE FOUR `:latest` PRODUCERS: `comp-learns-producer`, `cse-producer`, `fedobs-producer`, `resource-summaries-producer` still reference `opal-globgrph-derive-runner:latest` (S31's pins half) | measured | the four `.tf` files under `infra/aws/terraform/globgrph/` carry the tag on the DECLARED plane (this seat); 3 of 7 pinned on the APPLIED plane by the CVO's `describe-task-definition` (C-S24) | `0.7.0_AE_CloudOps` | port | S15 | 2, 4 | 7 of 7 ACTIVE globgrph families reference the image by DIGEST, read live by `describe-task-definition` after the apply, under a NEVER-2 entry naming every family the act touches; **R13** is the rule. **Bound:** no image is rebuilt by this row -- a pin is a task-definition revision and nothing else moves |
| S19 | FWD-7 | **ADDENDUM v0.5.** THE RESIDUAL LOCAL STORES beside the projection: `infra/aws/globgrph/kuzu_db` (+ `kuzu_load.py`, the June-2026 scratch builder, 1,166 nodes of this graph) and `kuzu_ac7.db` (NFRA_GLOBGRPH.ITEM-3), with their manifests (`kuzu_load.py:278` stamps merge attempts as `edge_count`, S53) | measured | present at this seat (`ls -d`) and at the CVO; reachable by NO client path (0 readers of 982 files, C-S22); held do-NOT-delete by the CVO's P7 (`DIAL_RECORD_comp-kuzu_20260804.md`) | `0.8.0_AE_CloudComp` | classify | -- | 7 | each store's DISPOSITION recorded with its owner and reason (retire with a tombstone / archive under its own project / keep with a NAMED reader); the P7 hold lifted or re-stated by its author on the record; `comp-find` over the tool homes still 0 readers beside a positive control; NOTHING deleted before the disposition lands; a store that STAYS carries a manifest field a consumer can reject on (S53) |
| S20 | FWD-7 (by this PRD's arc, *no machine is in the compile business*; not by the letter of the graph, Andrew's 2026-09-02 definition = the KuzuDB projection) | **ADDENDUM v0.5.** THE STITCH GRAPH: `infra/aws/globgrph/comp_debt.py:215`'s stitch leg opens `kuzu_stitch_db` locally and REFUSES where absent (W2-S17); `kuzu_stitch_load.py:124` stamps merge attempts as `edge_count` (S53) | measured | `kuzu_stitch_db` present at this seat with its manifest; `comp-debt` REFUSED on the stitch surface in D-7's census (W2-S17) | `0.8.0_AE_CloudComp` | classify | S19 | 7 | the stitch graph's HOME decided and recorded: either it JOINS the projection (derived cloud-side and served -- a later round's cells) or it is DECLARED a local scratch artifact outside the graph, with `comp-debt`'s refusal text naming the decision and the local builder's manifest carrying its claim (S53); no local rebuild path to the PROJECTION is created by either answer |

**Ordering carried from the decomp (s.2 there), the one that is a RULING:** S10-S13 measure first; STAGE 1 S1 -> S2 -> S9 -> S3; STAGE 2 S4 -> S5 -> S6; STAGE 3 S7, then **S8 LAST** (R7).

**Three notes that travel with this section:**
1. **Both 2026-09-02 holds on step 6 are CLOSED** (decomp s.5 named them): `comp-adversary` admission RC5 GREEN @5dbca15a4a (second pass, corroborated by CTO + CVO~A on different instruments); the `fabric` key written ~19:3xZ (note 3). This section makes the PRD conformant to the L6 gate's limb 5; it does not produce a cuttable TO by itself -- L6 is `2.0.0_SA_COO~A`'s.
2. **The lifted evidence is the COO's.** A relayed measurement that loses its origin becomes a second apparent carrier of one claim; the origin stays on every cell.
3. **`fabric` key -- RETIRED 2026-09-02 ~19:3xZ.** Andrew-direct at the `1.0.0_SA_CTO~A` terminal, verbatim **"laptop"**, in reply to the one-line call. `org/projects/NFRA_CLDGRPH.json` now carries `fabric: laptop` (+ `fabric_ruling` with the verbatim and record path); the header above and the row agree, and the step-6 gate's layer 3 (`.tools/to-pipeline-gate.py:169-216`) no longer refuses on this key. No step-6 hold remains (note 1).

## Change log

- **v0.5 2026-09-09 ~15:1xZ `1.0.0_SA_CTO`** -- L10 ADDENDUM on `3.0.0_SA_CVO`'s round-4 slug @`23fb03b1cd` (`ledger/ROUND_ANALYSIS.round4.md`, `ledger/COMPLETION_GRADES.round4.json`: 7 REALIZED, FWD-7 NOT_REALIZED). s.7 gains S14-S16 by reference (the recut cells CG-s-14/15/16, all DONE, so the two carriers hold one id space) and FOUR NEW rows S17-S20: the instruction plane's route back through `comp-kuzu --mode` (S17, with FWD-7's person half as its clause 2), the four `:latest` producers (S18), the residual local stores (S19), the stitch graph (S20). s.6 gains R13 (no mutable image tag). THE TEST THIS EARNS: a retirement has THREE planes -- executable, instruction, residue -- and a manifest that places only the first passes every cell and leaves a live instruction to re-create the path. `endpoint_outcomes` unchanged at eight; the cost-attribution capability placed at 94456/@`1266d65641` is CORRECTED to an L1 brief candidate at `4.0.0_SA_CRO` (no outcome here names cost; a row with no outcome is a phantom cell). dep_stage EXECUTING -> ROUND_CLOSE on this commit; the recut is `2.0.0_SA_COO~A`'s.
- **v0.4 2026-09-03 ~05:3xZ `1.0.0_SA_CTO~A`** -- LANDED AT THE TREE HOME `org/missions/D0/NFRA/NFRA_CLDGRPH/prd/` as L4 of the canonical workflow, second parallel run (Andrew-direct 05:1xZ, record `ANDREW_DIRECT_20260903_051xZ_PARALLEL_CANONICAL_FLOW_NFRA_CLDGRPH_WITH_COOA_CVOA.md` @8e134cc126; L3 registration @36157989a9). `docs/architecture/NFRA_CLDGRPH_PRD.md` retired to a redirect stub. s.7 notes 1 and 3 brought current (both 2026-09-02 step-6 holds closed); the s.6 decomp-inputs list stated as measurement-resolved, not decide-first; surprise channel = `3.0.0_SA_CVO~A` at the tree root. No outcome, ruling or manifest row changed.
- **v0.3 2026-09-02 ~19:3xZ `1.0.0_SA_CTO~A`** -- `fabric` RULED by Andrew-direct at this terminal, verbatim "laptop"; register row key written; s.7 note 3 retired; header gloss updated. R12 now rests on his word for this project, not only on the D0 hold.
- **v0.2 2026-09-02 ~19:2xZ `1.0.0_SA_CTO~A`** -- PRD_HEADER block (first fenced json) + s.7 SURFACE MANIFEST lifted from the COO decomp @05d2c89158 as gate (two verbs normalized to the contract enum; lanes to full serials); status RATIFIED. Reason: the step-6 gate's limb 5 (@689960ce16) refuses a TO against a PRD without either; the template gained both @75ead40079 after v0.1 was authored ("the gate got ahead of the carrier", `1.0.0_SA_CTO` 92701).
- **v0.1 2026-09-02 ~18:5xZ `1.0.0_SA_CTO~A`** -- registered + PRD from `_PRD_TEMPLATE.md`; ENDPOINT pasted from the ratified step-2 output with FWD-2 amended on Andrew's word; rulings R1-R12.
