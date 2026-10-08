# BRIEF -- multi-device graph coherence: every box reads, and feeds, one shared graph of current state

**Author:** `4.0.0_SA_CRO` | **Written:** 2026-10-08 ~16:1xZ (UTC) | **Mode:** NEW
**Asked by:** Andrew, at this seat's terminal. Verbatim records (same folder,
`org/tier1_exec/4.0.0_SA_CRO/deliverables/`):
- `ANDREW_DIRECT_20261008_133xZ_CLOUD_GRAPH_FOR_MULTI_AGENT_COHERENCE_REVIEW_PRIOR_ART.md`: the ask to research.
- `ANDREW_DIRECT_20261008_154xZ_COHERENCE_CALLS_A_B_YES_DELLS_MAY_WRITE_GRAPH_SHARED_FOLDER_IS_THE_BRANCH.md`
  @`70950bbf31`: calls A-D answered.
- `ANDREW_DIRECT_20261008_160xZ_CRO_BASE_GRAPH_OPS_CRO_A_GITOPS_CRO_B_GC.md` @`b387b7e868`: this seat holds "the
  multi-device graph coherence project".

**Consumer:** `1.0.0_SA_CTO` `/endpoint --forward`. Placement: Andrew's call A said "Yes" to a brief written as an
addition to NFRA_CTLPLN, and his later word names it "the multi-device graph coherence project". Whether it is an
addition or its own code is the CTO's to place (L3).
**Prior research this brief stands on:** `CLOUD_GRAPH_MULTI_AGENT_COHERENCE_PRIOR_ART_20261008.md` (@`f4cac7f3dc`) and
`FABRIC_PROXIMITY_MAP_RESEARCH_20261007.md` (@`f0b12ccd02`), both in the same folder.
**Siblings:** GitOps across the cluster (`4.0.0_SA_CRO~A`); garbage collector and script ops (`4.0.0_SA_CRO~B`).
**Vintage:** laptop, 2026-10-08 13:4xZ-16:1xZ. Repo reads, `comp-graph status`, one PyPI read. No Dell or site Z box
was read directly.

---

## ANDREW'S WORDS, VERBATIM (calls A-D, 15:4xZ)

> 1.) Yes. 2.) Yes. 3.) They should be able to. I think the Dell Boxes have been unfairly restricted for no clear upside.
> 4.) There is something there but it seems like a category error. The "shared folder" is the shared branch on git in
> my opinion. The more important thing is the shared graph read access so they always know current state when doing
> things across the estate.

**Three requirements in his words:**
- **Read everywhere.** Every box has shared graph read access. It is "the more important thing".
- **Current state.** What a seat reads is the state of the estate now, "so they always know current state when doing
  things across the estate".
- **Write from the Dells.** The Dells "should be able to" write to the graph's store, because they have been
  "unfairly restricted for no clear upside".

The shared working copy is the git branch. That is the GitOps sibling's territory and is not rebuilt here.

**The finding that shapes the brief.** Read access, the thing Andrew ranked first, is not in place for the Dells today.
The graph's read token is classed a PLATFORM KEY, and the Dell secrets grant admits only vendor credentials and client
sessions (Part IV finding 3). So the first journey is a Dell seat reading the graph, before any new layer is built.

---

## PART I -- THE OUTCOME TERRITORY

### THE CANDIDATE THREAD (becomes FWD-1 at L2)

**One Dell seat, one estate surface, one question, answered from the shared graph.**
1. A seat on dell1 or dell2, about to change one estate surface (one Lambda, say), asks the shared graph from its own
   box what that surface is now and what it is connected to. It gets an answer with a vintage, and that vintage is
   today's.
2. The same answer shows that another box committed against that surface today: which box, which seat, which commit.

Step 1 is Andrew's "the more important thing", working on the box class that cannot do it today. Step 2 is the
smallest slice of the fabric layer, which turns "current state" from estate-only into estate plus who is acting on it.

### O1 -- A seat on any box reads the shared graph

A seat on the laptop, dell1, dell2 or site Z runs the same graph question with the same tool and gets the same answer.
No box relays for another. Source: Part IV findings 1 and 3.

### O2 -- A seat knows how current its answer is, and it is current

Every answer carries its vintage, and a seat can tell a current answer from a stale one by reading that vintage. Under
normal running the vintage is recent enough that a seat does not act on a state the estate has already left. A failed
nightly rebuild is visible as failed rather than silently served. Source: Part IV finding 2.

### O3 -- A seat asks "who else is working on this surface?"

A seat names an estate surface and learns which boxes, seats, projects and task orders have declared it, edited it,
hold a deploy on it, or merged a change to it, with the time of each. Source: research @`f4cac7f3dc` section 5 (the
fabric layer: BOX, SEAT, PROJECT, TASK_ORDER, COMMIT; DECLARES, EDITS, HOLDS, MERGED).

### O4 -- Andrew or an integrator sees where boxes overlap

Andrew or a box's integrator asks for the overlap map and gets the surfaces that have two or more boxes on them, and
which boxes. It is read on demand: nothing notifies and nothing refuses (yesterday's calls B-D as the CTO ruled them).
Source: `FABRIC_PROXIMITY_MAP_RESEARCH_20261007.md`.

### O5 -- A Dell box writes its own activity into the graph

A Dell box publishes its own fabric facts (its commits, its declared paths, its deploys in flight) to the graph's store
from the Dell itself, without the laptop carrying them. This is Andrew's call 3. Source: Part IV finding 4.

### O6 -- Andrew chooses the graph engine knowing the engine's status

Andrew decides what the shared graph runs on, knowing that Kuzu is archived and frozen at 0.11.3. The options include
staying on 0.11.3 as a frozen dependency, moving to a maintained fork, or serving the same questions another way. The
choice is written down with its cost to O1-O5. This outcome is the decision record, not a migration. Source: Part IV
finding 5.

---

## PART II -- WHERE THE BOUNDARY SITS

| This project OWNS | It RELIES ON (owned elsewhere) |
|---|---|
| Graph read access from every box (O1): which identity reads and by what route | **NFRA_CTLPLN** (control plane): applying any IAM or secret-class change for the Dells, including the token class (Part IV finding 3) and the write grant (O5, row `NFRA_CTLPLN-S31`). This project states the need; the control plane applies it. |
| The fabric layer of the graph (O3, O4): its node and edge kinds, its writer, its feed | **GitOps** (`4.0.0_SA_CRO~A`): how commits, merges and pushes happen. This project reads git facts; it does not change the commit path. |
| The freshness a seat can rely on (O2), for the fabric layer and for the estate layer as seats use it | **The estate graph's producers** (the globgrph nightly, incremental updater and projection worker): no live project has owned them since the 2026-08-25 spring clean. Whether this project adopts them or only relies on them is a placement call (Part V). |
| The engine decision record (O6) | **Garbage collector and script ops** (`4.0.0_SA_CRO~B`): any long-running feed this project adds must end itself without a live session, which is that project's rule to set. |

Not in scope: a live shared file system (Andrew's call 4, "a category error"); any monitor, alert or notification; any
change to what the estate layer models.

---

## PART III -- THE QUALITATIVE BAR

- A Dell seat about to touch a Lambda finds out what the Lambda is wired to from the graph, as a laptop seat already
  can, and does not have to ask the laptop.
- A seat that acts on a graph answer never later finds that the answer described yesterday's estate without saying so.
- Two boxes do not discover that they changed the same surface only when a merge conflicts or a deploy collides. They
  can learn it from the graph before they start.
- Andrew asks "who is on this surface?" and gets an answer without a seat assembling one by hand from logs and
  `git log`.
- A Dell's activity reaches the graph as quickly as the laptop's. No box is a second-class source.

---

## PART IV -- THE SUBSTRATE: what exists, measured

1. **The served graph is real and box-neutral in design [READ, research @`f4cac7f3dc` section 3].** Kuzu is built in
   the cloud from Iceberg tables behind Nessie and served read-only over HTTPS at `mcp.opalinvest.dev/graph/cypher`,
   with a bearer token from secret `opal/mcp/graph-read-token`. Every comp-tool that reads it (`comp-kuzu`,
   `comp-find --corpus aws`, `comp-describe`, `comp-depth`) needs that token.
2. **Freshness [READ, `comp-graph status`, 15:52Z].** Served vintage 2026-10-08 12:54:23Z, writer
   `incremental_updater`, built 12:55:03Z, about 3 h before the read. The last FULL rebuild was 2026-10-04, and the
   2026-10-07 nightly did not publish (measured 13:4xZ, not investigated). The estate layer moves on AWS change events.
   Nothing moves it on a git commit.
3. **The Dells cannot read the token, by the grant's own rule [READ code; live effect INFER].**
   `infra/aws/terraform/nfra-ctlpln-identity/tests/derive_vendor_secrets.py:156` classes `opal/mcp/graph-read-token` as
   `PLATFORM-KEY` ("read capability bearer for the firm's estate-graph service"). `iam.tf:155-165` grants the Dell group
   read of VENDOR-CREDENTIAL and CLIENT-SESSION secrets only, "and no PLATFORM-KEY or OTHER secret (... bearer tokens for
   the firm's own gateway or services ...)". The CTO record
   `ANDREW_DIRECT_20261008_004xZ_LIFT_FOUR_DELL_LIMITS_SECRETS_FIRM_DATA_RESOURCE_POLICIES_PUSH.md` is the lift this rule
   implements. Whether another route lets a Dell read the graph was not checked (Part VII).
4. **The Dells can probably already write the store [READ policy; not measured live].** `dell_deploy_policy.json`
   allows `s3:PutObject` on `arn:aws:s3:::opal-*/*`, and the graph bucket is `opal-313476888478-globgrph`. That write
   reaches the head marker, which starts a rebuild, and the Iceberg files. Andrew's call 3 makes this wanted. What is
   missing is a sanctioned shape for it: today a write would bypass the producers and the "agents never write the
   estate graph" rule of 2026-06 (Part V).
5. **Kuzu is archived [READ, pypi.org/project/kuzu, 2026-10-08 ~15:4xZ].** The banner reads: "This project has been
   archived by its maintainers, and is no longer receiving any updates." The last release is 0.11.3, dated 2025-10-10,
   and that is the version the projection worker pins and refuses to move from (`projection_worker.py:303`, by
   sub-search). A web search (secondary sources, not verified) says Apple acquired Kuzu Inc. in October 2025 and that
   community forks carry the code on. Which forks are alive was not checked.
6. **Fabric-layer prior art [READ, research @`f4cac7f3dc` section 1.4].** `tool_activity` has a serial, task order,
   tool and file, but no box, and is laptop-only with overwriting keys. The `cse` event table has agent and deploy
   kinds, nightly. NFRA_CLDGRPH's "two machines give the same answer" outcome was never graded, and the project was
   closed on Andrew's word on 2026-09-23. The surface vocabulary (Lambda, bucket, Terraform resource, module) is
   already graph nodes, so the fabric layer can attach to them.
7. **Stale guidance [READ, research section 6.5].** `comp-which` suggests a Cypher label form the schema does not have
   (a kind is a property, not a label). The graph manifest names retired local stores. A Dell seat learning the graph
   from the tools today would be misled.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- A read path for the Dells. Either the token's class or the grant changes, or a read route that needs no platform key
  exists. Either way it is the control plane's to apply, and Andrew's call 3 reasoning ("unfairly restricted") bears
  on it.
- A sanctioned write shape for the Dells (O5), reconciled with the 2026-06 rule that agents never write the estate
  graph. One reading: a box's fabric writer is not an agent writing the estate layer. That reconciliation is the
  PRD's, and Andrew's word on call 3 stands above it.
- An owner for the estate graph's producers, or an explicit statement that this project relies on them unowned. O2
  depends on the nightly publishing.
- The engine decision (O6) is settled before the fabric layer is built deep on Kuzu, or the layer is built so that it
  survives an engine change.
- A per-box git feed with the box named (O3). Box attribution in git is inferred from serials today, and that touches
  the GitOps sibling.
- Any feed process ends itself without a session, under the GC sibling's rule.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-08, laptop. Status ages; cut nothing from this part.
- 13:4xZ: 29,586 nodes, 63,213 edges, 411 edges skipped for a missing endpoint. Last full rebuild 2026-10-04.
- 15:52Z: served vintage 12:54:23Z (incremental). Local trace layer `.comp-graph/` STALE, 15 days old, with 503 of
  2,018 nodes drifted. That is the laptop-local layer, not the served graph.
- Hazard row `NFRA_CTLPLN-S31` (Dell write to the graph bucket) is open in the control plane's channel. Andrew's call 3
  now answers its direction.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- No Dell or site Z box was read. The Dell read block is read from the grant's code and the census class. No
  `simulate-principal-policy` was run, and it was not checked whether a Dell has another route to the graph.
- Whether the Dell grant is applied live was not read.
- Why the 2026-10-07 nightly did not publish was not investigated.
- The Kuzu forks' health was not read; the archive is read from PyPI only.
- How fast the fabric layer must move (per commit, per minute, per drain) is left to the PRD; no number is set here.
- The bucket policy on the graph bucket was not read.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/multi-device-graph-coherence-brief-20261008.md
  PROJECT           NONE-YET (Andrew: "an addition to NFRA_CTLPLN" at call A, then "the multi-device graph coherence project"; CTO places)
  EXISTING PRD      NONE for this; NFRA_CTLPLN PRD org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md (host candidate)
  SIBLING PROJECTS  GitOps (4.0.0_SA_CRO~A); garbage collector + script ops (4.0.0_SA_CRO~B); NFRA_CTLPLN; NFRA_CLDGRPH (closed 2026-09-23)
  PRIOR ART         served Kuzu + Nessie + Iceberg (globgrph); comp-kuzu / comp-find --corpus aws / comp-graph status;
                    tool_activity, cse; research @f4cac7f3dc, @f0b12ccd02
  MEASURED AT       2026-10-08 13:4xZ (graph counts), 15:4xZ (PyPI), 15:52Z (vintage), laptop CLOUD @b387b7e868
```
