# Research: a cloud graph for multi-agent coherence across boxes -- what the estate already has

**Author:** `4.0.0_SA_CRO` (Chief Research Officer), 2026-10-08 ~14:3xZ. **For:** Andrew.
**Order:** `ANDREW_DIRECT_20261008_133xZ_CLOUD_GRAPH_FOR_MULTI_AGENT_COHERENCE_REVIEW_PRIOR_ART.md` (same folder): review the
reel, then begin looking through the prior art and existing infrastructure: the cloud Kuzu, Nessie and Iceberg, and the
comp-tools that reach them. **Status:** research. Nothing was built or changed, apart from one hazard row (section 6).

**How this was read.** I ran four reads myself: the graph's freshness, its table list, its node and edge counts, and the
Dell policy files. Three read-only sub-searches did the rest: the Terraform and producer code, the comp-tools, and the
graph projects' records (about 220 files between them). A claim marked [READ] was read in a file or measured; [INFER]
is reasoning. A sub-search's finding I did not re-read myself is marked (sub-search).

---

## 1. Conclusion

1. **The reel and our estate solve different halves of one problem.** The reel shares FILE BYTES live: every machine
   mounts one cloud folder. Our boxes already share the estate's STRUCTURE through one cloud graph, every box reading
   the same served copy. What neither has is the third thing your overlap question needs: **live INTENT and ACTIVITY**,
   meaning which box and seat is working on which surface right now.
2. **The cloud graph is real, live and already box-neutral.** Kuzu is built in the cloud and served read-only over
   HTTPS. Read today: 29,586 nodes and 63,213 edges, rebuilt 49 minutes before the read. Every comp-tool reaches it the
   same way from any box with AWS credentials. Its storage is Iceberg tables behind Nessie, read by an always-on
   Trino. The laptop copies were retired on 2026-09-09.
3. **It models the estate, not the fabric.** There is no node for a seat, a box, a commit, a branch, a task order or a
   deploy in flight. Its update path is batch: a nightly full rebuild, plus incremental updates driven by AWS
   CloudTrail (minutes). It does not see a git commit or an agent's act at all.
4. **The closest prior art to "who is doing what" exists in parts, and every part stops short.**
   - `tool_activity` records agent serial, task order, tool and file touched. It has no box column, it is uploaded
     from the laptop only, at most every 3 hours, and its writer overwrites the same keys.
   - The event log `cse` has agent and deploy kinds, but they cover gateway calls and completed deploys, nightly.
   - The 2026-09 cloud-graph project (NFRA_CLDGRPH) set "two machines give the same answer" as an outcome. Its
     two-machine test was never run, and the project was closed on your word without that grade.
5. **So the build is an addition, not a new system.** Add one fabric layer to the same graph: box, seat, project,
   surface and the four verbs from yesterday's research (DECLARES, EDITS, HOLDS, MERGED). Feed it from records the
   boxes already write. Yesterday's map becomes queries on the graph you already serve. The reel's live file system
   is a different, much larger bet; section 4 says why it is not the first move.
6. **Three things need a decision before any build:** whether to build at all (yesterday's call A, still open);
   Kuzu's future (it is pinned at 0.11.3 and may no longer be maintained, not verified); and whether the Dells may
   write to the graph's bucket, which today they appear to be able to (section 6).

---

## 2. The reel, read against our estate

What he describes, as given (a stored description of the reel, not a word-for-word transcript):

| His claim | Our estate today |
|---|---|
| Every agent works on its own copy of files and cannot see the others' work live | True here. Each box has its own git working tree; another box's work is visible only after it publishes a branch (yesterday's research, section 2). |
| The git workaround means nothing is live until push and pull | True here, and measured: the laptop's shared tree was 891 commits behind origin last night until it was brought level. |
| Fix: one cloud folder mounted on every machine; bytes stream on demand; saves propagate in under 0.5 s | No equivalent. Our nearest is the agent bus between boxes (messages, not files) and S3 (objects, not a mounted folder). |
| Built on a coordination object that tracks every file version, with bytes in object storage | Our graph has this split already for structure: Nessie (version catalog) plus S3 (bytes). It is not used for working files. |
| Agents become ephemeral workers because all state is in the cloud | Partly true here: worker subagents are ephemeral, but each needs a git worktree on a box, and a seat's state is its box's tree. |

[INFER] His design removes the git step; ours keeps git as the record and needs a view of what is in flight before it
reaches git. A shared live folder would also remove the review boundary our rules depend on (a commit through the
gate, a lane per path, a merge by the integrator). Swapping the substrate is a different decision from seeing across it.

---

## 3. What exists, by layer

### 3.1 Storage and catalog [READ unless marked]

- **Bucket** `opal-313476888478-globgrph`, not versioned (sub-search: `shared-infra/s3.tf:313-371`).
- **Iceberg warehouse** under `warehouse/`, catalog **Nessie** (Fargate, always on, version store in DynamoDB tables
  `opal-globgrph-nessie-*`, branch `main` only, a nightly tag kept 13 months) (sub-search: `globgrph/nessie.tf`,
  `derive_runner.py:71, :436`).
- **Tables** in namespace `globgrph` (sub-search):

| Table | What one row is | Written by, when |
|---|---|---|
| `graph_nodes`, `graph_edges` | an estate thing and a relationship | nightly full overwrite at 02:00Z; an incremental Lambda in between, driven by CloudTrail |
| `graph_contracts` | a data-ownership contract | on load only |
| `cse` | an event: something changed (kinds git, agent, deploy, ide, ticket, doc, infra, api, approval, graph_head, promote) | nightly at 03:30Z, append-only |
| `tool_activity` (parquet in Glue) | one agent tool event: serial, role, task order, tool, file touched, session | laptop session-end hook, at most every 3 h |
| `code_heat` (parquet in Glue) | a file's last commit time and heat | a dev box |
| `obs_findings`, `fedobs_signals` | a finding from one of five observers | nightly at 04:30Z |

- **The head marker** `warehouse/_branch_head.main.json` names the current snapshot. Writing it starts the Kuzu rebuild.

### 3.2 Query engines [READ]

- **Kuzu, the served copy.** A worker task builds `projection/<vintage>/kuzu_nessie_db` when the head marker moves.
  `projection/current.json` points at the newest build. An always-on read-only server checks that pointer every 60 s
  and answers Cypher on `projection.opal-globgrph.local:8181`. The gateway at `mcp.opalinvest.dev/graph/cypher`
  proxies to it, with a bearer token read from secret `opal/mcp/graph-read-token`.
- **Measured today, 13:4xZ:** vintage 2026-10-08 12:54:23Z, writer `incremental_updater`, 29,586 nodes, 63,213 edges,
  411 edges skipped for a missing endpoint. The last full rebuild was 2026-10-04; last night's full rebuild did not
  publish ("REFRESHED LAST NIGHT: NO").
- **Schema:** one node table `CloudNode(node_id, arn, node_type, name, layer, drift_class, source, snapshot_ts, props)`
  and one edge table `CloudEdge(edge_type, layer, snapshot_ts, props)`. A kind is a property, not a label.
- **What the 59 node kinds are** (largest first): code motifs 6,683; SharePoint files 5,878 and folders 1,327; code
  fields, JSX, types, pipeline functions; 607 IAM policies, 283 roles, 233 Lambdas, 153 event rules, 41 buckets,
  34 EC2 instances. **No kind is a seat, a box, a commit, a branch, a task order, a project or a session.**
- **Trino** (Fargate, 2 vCPU / 8 GB, always on) at `trino.opal-globgrph.local:8080`, reachable inside the VPC only.
  It joins the graph tables, `code_heat`, `tool_activity` and the observer findings. From a box it is reached by
  launching a one-shot task, which takes about 3 to 4 minutes a query (`comp-heat federated`).

### 3.3 The comp-tools that reach it [READ by sub-search]

| Tool | Reads | Needs on a box |
|---|---|---|
| `comp-kuzu` | the served Kuzu, over HTTPS | AWS credentials that can read `opal/mcp/graph-read-token`; `.tools/aws`; Git Bash |
| `comp-find --corpus aws`, `comp-describe`, `comp-depth` | the same served Kuzu | the same |
| `comp-graph status` | the build pointer and manifest in S3; local trace caches | S3 read on the graph bucket |
| `comp-heat federated` | Trino, through a one-shot task | `ecs:RunTask`, `logs:GetLogEvents` |
| `comp-learns-status` | `served/comp_learns_status.json` (a nightly Trino product) | S3 read |
| `comp-icedrill` | S3 partition and version listings | S3 list |

None of these tools writes to the cloud graph. [INFER] Every read is box-neutral except the token: whether the Dells'
secrets grant (applied or not) admits `opal/mcp/graph-read-token` was not read.

---

## 4. Against the three things you joined

| Need | Have | Missing |
|---|---|---|
| **The reel: see each other's work live** | Structure is shared through one served graph, minutes behind AWS | Working files are not shared; nothing before a commit is visible across boxes |
| **Yesterday's overlap map: which surfaces have two boxes on them** | A graph engine and a query path every box can use; a surface vocabulary in the graph (Lambda, bucket, Terraform-declared resource, module) | Box, seat, task order and the four verbs as data; any record of edits, declarations or deploys in flight |
| **The graph as the control plane's foundation** | Versioning (Nessie), the head marker, read-only serving, a vintage on every answer | A fabric layer, and an update path faster than nightly for it |

The useful fit [INFER]: yesterday's "surface" can be the graph's own node. Two boxes that edit a Lambda's code and its
role in different folders meet on one node through an existing edge, which a file comparison cannot see. That was
yesterday's fourth blind spot, and the graph closes it.

---

## 5. What a build would add, in outline (not a design)

1. **One fabric layer in the same graph:** nodes BOX, SEAT, PROJECT, TASK_ORDER and COMMIT; edges DECLARES, EDITS,
   HOLDS and MERGED from a seat to an existing estate node. This is a new `layer` value on the existing two tables, so
   no new engine is needed.
2. **Feeds the estate already writes:** task orders' `<paths>` (DECLARES), git on each box's published branches
   (EDITS, MERGED), the change-management ledger (HOLDS), the device register (BOX). `tool_activity` would gain a box
   column and run on every box.
3. **Latency is the real design question.** The served copy moves when the head marker moves, and that is minutes.
   The fabric layer must move per commit. Options to weigh at the brief, not here: an event table appended per act
   (the `cse` pattern), the agent bus as the carrier, or a small live table outside Kuzu that the map reads.
4. **What stays the same:** agents still never write the estate graph (the 2026-06 rule); the fabric layer has its own
   writer.

What the reel's approach would add, for comparison: a mounted shared folder per box. That replaces git as the
working copy and asks every gate to move from commit time to save time. [INFER] It is not a step toward the overlap
map and should be judged as its own project if you want it.

---

## 6. Hazards and drift found on the way

1. **The Dells can write to the graph's bucket.** [READ] `dell_deploy_policy.json` allows `s3:PutObject` on
   `arn:aws:s3:::opal-*/*`, and the bucket name begins `opal-`. Its only S3 Deny is on `opal-data-*`. A Dell seat could
   therefore write the head marker (which starts a rebuild) or replace Iceberg table files. Not measured live; no
   bucket policy was read. Recorded as row `NFRA_CTLPLN-S31` in the control-plane surprise channel (commit
   `7163b27526`). The ruling is the control plane's.
2. **Kuzu's future is unsettled.** It is pinned at `kuzu==0.11.3` ("Cypher dialect is the contract") and the cloud
   worker refuses any other minor version (sub-search: `projection_worker.py:303`). The package assessment of
   2026-10-07 recalled that its makers archived the project in late 2025; that was not verified then, and it is not
   verified now. Any build on Kuzu should first settle that, because an archived engine at the centre of the control
   plane is a long-term risk.
3. **Last night's full rebuild did not publish.** The last full rebuild is 2026-10-04 (measured). The served copy is
   current only through incremental updates. Not investigated.
4. **The graph's two-machine outcome was never graded.** NFRA_CLDGRPH closed 2026-09-23 on your word "without
   claiming REALIZED"; its two-seat test on site Z reads absent (sub-search: `ROUND_ANALYSIS.round8.md:111-116`). No
   live project owns the graph since the 2026-08-25 spring clean; only the scheduled cloud parts run.
5. **Stale guidance in the tools.** `comp-which` suggests a Cypher form (`MATCH (n:LAMBDA) RETURN n.id`) that the
   schema does not support; the graph manifest still names retired local stores in three entries (sub-search).

---

## 7. Calls for Andrew

- **A. Build the box-activity map (yesterday's call A)?** REC: yes, and build it as a fabric layer of the cloud graph,
  not as a separate tool. Same first step as yesterday (on demand, read-only, no notification), with the graph as its
  store. On your word I write the brief as an addition to the control-plane project (NFRA_CTLPLN).
- **B. Kuzu's future before building on it?** REC: one bounded read of the Kuzu project's status now (its own
  repository and release page; a web read, not a download). If it is archived, the brief carries the engine as an open
  question (Kuzu as is, a maintained fork, or SQL over Trino) rather than a hidden dependency.
- **C. Should the Dells write to the graph's bucket?** REC: no write. Read is enough for every comp-tool. This is the
  control plane's to apply; I recorded it rather than ruling it.
- **D. The reel's live shared folder?** REC: not now. It solves a different problem (shared bytes) at the cost of the
  commit boundary every gate stands on. Revisit only if the map shows overlap that git timing alone causes.

---

## 8. Not read or not measured

- No live AWS policy simulation; no bucket policy on the graph bucket; whether the Dell secrets grant admits the graph
  read token.
- The Kuzu project's own status (archived or not).
- Why last night's full rebuild did not publish.
- Projection server and incremental-refresh code beyond their headers; the producers for the cse `git`, `ide`,
  `ticket` and `approval` kinds; the CSE, FEDOBS, COMPLEARN and COMPTEAM PRDs.
- Nothing on dell1, dell2 or site Z was read directly.
- The reel itself: only its stored description, which you pasted.
