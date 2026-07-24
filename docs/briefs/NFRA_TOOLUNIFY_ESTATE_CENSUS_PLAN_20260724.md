# NFRA_TOOLUNIFY — ESTATE CENSUS PLAN (audit-first)

**author:** `1.0.0_SA_CTO~Z` · 2026-07-24 · **status:** CENSUS (pre-PRD, pre-architecture)
**sovereign:** Andrew-direct 2026-07-24 — *"our goal here is consolidation and packaging… a unified set,
with clear denominators, and clear coverage disclaimers"* · *"figure out how to reconcile to the truth …
the bridge from the user's local device to the federated cloud surface"* · *"survey the state of the cloud
and work our way backward to the tools … establish our real estate completely first before … how we will
architect the ontology and associated state bridges"* · *"let's first get this audit in, and then we can
decide how we want to handle it."*
**vintage:** all CTO~Z measurements below taken this session @ `721b68f7bb`, live/source, not quoted.
**predecessor brief:** `docs/briefs/NFRA_TOOLUNIFY_BRIEF_20260724.md` (CVO~Z). This plan is the AUDIT phase
that must land before that brief's §3 register + §5 ruling are written.

---

## §0 · What this is, and what it is NOT

This is a **read-only census of the complete real estate**, run in parallel across 5 lanes, consolidated by
CTO~Z into one grounded estate map. The map feeds the *later* decision on how to architect the unified
ontology + state bridges. **Sequencing is sovereign-set: establish the estate COMPLETELY first.**

**NOT in this phase — do none of it:** no PRD, no ontology design, no tool re-point, no artifact
regeneration, no crosswalk, no schema change, no applies/deploys. A census that mutates the thing it
measures is disqualified. **A frozen artifact is a FINDING to record, never a thing to "fix" by
regenerating** (regenerating stamps a fresh mtime over a frozen census and destroys the evidence —
`estate-coverage-resolver.json`, `stitch_graph.json`, `graph_contracts` are all in this class).

---

## §1 · The grounded estate map (CTO~Z first pass — your census extends this, it does not repeat it)

**THE FEDERATED CLOUD TRUTH is one platform — `NFRA_GLOBGRPH`:** a **Nessie-git-branched Iceberg
lakehouse**, live (`_branch_head.main.json` committed 2026-07-24T15:04Z, writer `incremental_updater`
Lambda; **46 Nessie refs**). kuzu is **not a second graph** — `kuzu_nessie_db` is a materialized Cypher
projection of a Nessie snapshot (`comp-kuzu`/`comp-aws`/`comp-blast` read it).

| Surface | Grounded state @ 721b68f7bb |
|---|---|
| Iceberg core (`warehouse/globgrph/`) | `graph_nodes` (fresh 15:04Z), `graph_edges` (02:08Z), `graph_contracts` (**FROZEN 06-16**), `resource_summaries` |
| Iceberg obs/ontology layers | `fedobs_*` (signals/findings/coverage/coevolution), `cse_ingest`(+staging,+test), `code_heat`, **`ms_heat`** (M365), `tool_activity`, `axes_history`, `snap_ingest` |
| globgrph bucket prefixes | `producers/`(graphuni, ts-semantic), `served/`, `contracts/`(graph_contracts.yaml 06-16), `stitch/`(**`stitch_graph.json` FROZEN 07-07 = the 17-day silent producer**), `snapshots/`(daily tarballs since 06-08), `cse-seed/`, `code/`, `build-source/` |
| Catalog / query | Glue DBs {globgrph, opal_mcp, cloudtrail_forensics, default}; Athena WGs {opal_mcp, primary}; Nessie catalog in DynamoDB `opal-globgrph-nessie-_objs`/`_refs` |
| Served / live AWS | ~38 S3 buckets · 36 DynamoDB tables · Lambda/EventBridge/SF/SQS (**counts page-truncated — a lane job**) |
| M365 | `m365-mcp-gateway` EC2 (EC2_MANIFEST:444) + `ms_heat` Iceberg table (producer/content unmapped) |
| **LOCAL device end** | `.comp-graph/graph.json` = a **local working-tree scan** (2,255 nodes, `file_path`+`source_sha`, `built_at`, rebuilt on read). node types: GOLD_SCRIPT 1365, LAMBDA 333, S3_ARTIFACT 321, ENDPOINT 138, EVENTBRIDGE 63, COMPONENT 24, … Read by comp-blast/trace/xref/gitdrill/surface-check. **NOT in the cloud truth.** |
| **git-committed history** | surfaced **nowhere** — no COMMIT node type in graph.json, no git/commits table in the warehouse, `incremental_updater` does not ingest commits. Queried ad-hoc only (comp-gitdrill/comp-symbols). |

**THE BRIDGE MODEL the census serves (target frame, not to be built yet):** one entity identity observed at
three states along a promotion axis — **LOCAL** (working-tree scan) → **COMMITTED** (git, both repos, DEV/
PROD/CLOUD grain) → **DEPLOYED** (the federated cloud truth). The **drift between adjacent states is the
instrument.** The cloud end is built; the LOCAL↔COMMITTED span is open.

**THE FRAGMENTATION (why TOOLUNIFY exists):** 91 `comp-*` executables read across **all five source classes
with no bridge reconciling them** — kuzu(←Nessie, deployed) · local `graph.json`(working tree) ·
Iceberg-direct(`comp-icedrill`/`comp-fedobs`/pyiceberg) · live-AWS(boto3) · floating-JSON(stale). Different
vintages, populations, grains.

---

## §2 · The 5 census lanes — non-overlapping scopes

Each lane: **MISSION → MUST-CLOSE QUESTIONS → METHOD → BOUNDARY (non-overlap) → DELIVERABLE → ACCEPTANCE.**
Deliverable path for every lane: `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/<lane>.md`
(`mkdir -p` it). Structured tables; every count prints its **denominator + vintage**; machine-readable
sidecar (`.json`/`.yaml`) where the data is tabular.

### §2.base — `0.8.0_AE_CloudComp` — Iceberg/Nessie globgraph CORE (integration owner)
- **MISSION:** completely characterize the versioned-truth substrate — every Iceberg table + the derive
  pipeline that maintains it.
- **MUST CLOSE:** the full Iceberg table inventory (name, namespace, schema/col-count, snapshot count, last
  write, **producer, trigger, cadence, and whether anything watches it on failure**); the Nessie ref/branch
  topology (46 refs — what are they?); the `incremental_updater` Lambda (what it reads → writes, its
  trigger, its failure mode); **why `graph_contracts` is frozen 06-16 and `stitch_graph.json` frozen 07-07**
  (mechanism, not just the date — is the producer hard-failing, hook-exits-0, or by-design?); the
  `producers/`/`snapshots/`/`served/` prefix roles.
- **METHOD:** `comp-icedrill`, `comp-fedobs`, pyiceberg `StaticTable`, live `aws glue`/`s3`/`dynamodb`,
  `comp-freshness`. Ground the derive Lambda at `infra/aws/lambda/globgrph/`.
- **BOUNDARY:** you own the **Iceberg/Nessie truth substrate + its producers**. You do NOT map how tools
  *consume* it (that's ~D) or reconcile live-AWS parity (that's ~A).
- **ACCEPTANCE:** every Iceberg table has a named producer + named failure-watcher, or is declared
  FROZEN-BY-DESIGN with the mechanism proven. The two frozen tables' mechanisms grounded at source.

### §2.A — `0.8.0_AE_CloudComp~A` — Deployed-AWS ↔ graph PARITY
- **MISSION:** measure the live cloud vs both graph projections; find where our own model miscounts our own
  estate.
- **MUST CLOSE:** **paginated** live counts (Lambda, EventBridge rules, Step Functions, SQS, S3, DynamoDB,
  IAM roles/policies) — the first-page floors CTO~Z hit (50/100) are NOT totals; the real **`LAMBDA 333
  (graph.json) vs 191 (kuzu) vs <live>` disagreement** — which plane is wrong, and why (submodule blindness?
  vintage? extractor gap?); the same for COMPONENT (24 vs 641); the 7 GLOBGRPH layers' (§4 of the GLOBGRPH
  PRD) actual populated-vs-declared node classes.
- **METHOD:** `comp-aws`, `comp-lambdamap`, `comp-kuzu`, live `aws … --no-paginate`/paginated loops,
  `comp-iam` (remember: `comp-iam` models `(action)` not `(action,resource)` and **fails GREEN** on a new
  resource — Rule 22a; for parity you only need counts, but never cite comp-iam for a resource-scoped claim).
- **BOUNDARY:** you own **live-AWS vs graph COUNT/coverage parity**. You do NOT characterize the Iceberg
  tables (base) or the tools (~D). Report the disagreement as a finding; do not "fix" either graph.
- **ACCEPTANCE:** every disagreement between live / kuzu / graph.json has a grounded cause or an explicit
  "unexplained — candidate coverage defect" with its denominator.

### §2.B — `0.8.0_AE_CloudComp~B` — LOCAL + COMMITTED bridge span
- **MISSION:** characterize the open end of the bridge — the local working-tree scan and the un-surfaced git
  history for **both** repos.
- **MUST CLOSE:** exactly what `graph.json` captures (working-tree only? committed? the `source_sha` field —
  is it a git blob hash, and does it enable LOCAL↔COMMITTED drift detection?); prove the git-history gap
  (nothing ingests commits — confirm CTO~Z's negative or refute it); **scope what surfacing full git history
  would take** — both repos, and the branch grain (workspace `CLOUD`/`main`, portal `DEV`/`PROD`); what the
  portal repo contributes that the workspace scan misses.
- **METHOD:** read `org/modules/graph/trace_graph.py` (the graph.json builder) + `comp_gitdrill.py` at
  source; `git log`/`rev-list` on both repos for magnitude; `.comp-graph/graph.json` structure.
- **BOUNDARY:** you own **LOCAL(working-tree) + COMMITTED(git)**. You do NOT touch the DEPLOYED cloud truth
  (base/~A). Scope-only on git-surfacing — design nothing.
- **ACCEPTANCE:** a grounded statement of what the LOCAL and COMMITTED planes contain today, the drift
  mechanism `source_sha` does/doesn't enable, and a sized (not designed) gap for surfacing git.

### §2.C — `0.8.0_AE_CloudComp~C` — M365 / Microsoft surface
- **MISSION:** determine whether M365 is a real plane or a stub.
- **MUST CLOSE:** the `m365-mcp-gateway` EC2 (what it exposes, what graph.microsoft scopes); the `ms_heat`
  Iceberg table (producer, content, cadence, what "heat" it measures — Teams? mail? SharePoint?); what of
  M365 is **modeled as graph nodes vs merely queryable via the gateway**; is there an M365 plane in the 7-
  layer taxonomy at all.
- **METHOD:** `EC2_MANIFEST.json`, `infra/aws/ec2/m365-mcp-gateway/`, `comp-heat`, the `ms_heat` Iceberg
  table via pyiceberg, live gateway config (do NOT call external M365 APIs — census the surface, don't
  exercise it; vendor-egress discipline holds).
- **BOUNDARY:** you own **M365/Microsoft ONLY**. Do not stray into general AWS (~A) or the Iceberg core's
  non-M365 tables (base).
- **ACCEPTANCE:** a verdict — M365 is {a populated plane / a single heat table / a stub} — with the producer
  and content grounded, or an explicit "could not determine, here is what's missing."

### §2.D — `0.8.0_AE_CloudComp~D` — Tool → source MAP (the register seed)
- **MISSION:** for all 91 `comp-*` tools, establish **which surface + vintage each reads** — the
  fragmentation, measured per tool. This is the WS-1/WS-2 seed of the CVO~Z brief's TOOL REGISTER.
- **MUST CLOSE:** per tool — `reads[]` (each input typed: LIVE-AWS / KUZU-CANONICAL / SOURCE-SCAN /
  ICEBERG-DIRECT / FROZEN-SNAPSHOT / DERIVED-CACHE / CONFIG), `writes[]`, `binding` (ANSWER-BEARING vs
  GUARD/ROUTING/LABEL/CONFIG), `evaluation` (RUNTIME vs DERIVED), `failure_mode` (LOUD / FAIL-OPEN /
  SILENT-EMPTY). Use **import-closure + AST/call-site**, not string presence — the predecessor method was
  25% wrong (producer-vs-consumer, guard-vs-source). `reads[]`/`role_flags[]` are **LISTS** — a tool reading
  both kuzu and a floating artifact must show both, or it hides a coverage gap.
- **METHOD:** resolve each wrapper's transitive module closure; classify by call site. Re-ground the brief's
  known cases: reproduce the **3 false positives as negatives** (`comp-manifest-check`, `comp-graph`,
  `comp-stitch-refresh`) and **find the known-missed member** (`nerves_resolve.py:73`). An instrument that
  cannot find a known-present instance is broken and reporting silence.
- **BOUNDARY:** you own the **tool→source mapping**. You do NOT re-characterize the surfaces themselves
  (base/~A/~B/~C own those) — you consume their names and map tools onto them.
- **ACCEPTANCE:** ≥ the 91 tools rowed; zero `UNKNOWN` in `reads[]`/`evaluation`/`failure_mode` without a
  named reason; the denominator + its exclusions printed in the artifact; the 3 FPs and 1 FN case landed.

---

## §3 · Cross-lane discipline (binding on all 5)

1. **ISOLATION — report to `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY.** You are an off-main-fabric census
   group under CTO~Z jurisdiction. **Do NOT interact with the main fabric** — no COO, no MSTR, no other
   lanes, no main-fabric channels. The wider fabric is paused; your census is exempt and read-only. At
   startup write your serial file (LD-0290) and register under your full suffixed serial.
2. **READ-ONLY.** No apply, deploy, re-point, regenerate, schema change. Frozen artifact = record it, never
   regenerate it.
3. **GROUNDING (CLAUDE.md law, condensed):** every count prints its **denominator + vintage**. Live-primitive
   for APPLIED truth; `comp-iam` **fails GREEN** on a new `(action,resource)`. **Page-truncation is a lie** —
   `aws lambda list-functions` caps at 50/page; paginate or you report a floor as a total. **Timestamps:
   host is UTC-4** — use explicit-`Z`; a zero from a time-windowed query needs a positive control. **Freshness
   is trading-day-frontier, not wall-clock** — but for a *tool/graph* artifact the frontier is HEAD-advance /
   the producer's cadence, not the market calendar; still, never call a producer dark on an age alone —
   resolve its cadence first. Ground the MECHANISM, not the symptom (Rule 22): a causal claim is INFERRED
   until source/graph-confirmed. **comp-tool localizes; the raw call verifies** — two-stage.
4. **OUTPUT:** structured markdown to the deliverable path above + a machine-readable sidecar where tabular.
   Print what you could NOT determine as a finding — could-not-verify is a result, not a gap to paper over.

## §4 · Verification & consolidation
- **Verification:** `3.0.0_SA_CVO~Z` holds the bar on each lane's deliverable (the instrument measuring the
  estate is measured by someone who did not build it). Route ratified/standard-level implications to CTO~Z.
- **Consolidation:** `1.0.0_SA_CTO~Z` merges the 5 into one complete estate map → that map, verified, is the
  input to the "how we handle it" decision (the PRD, the two-plane-vs-unified ruling, the bridge
  architecture). No lane designs the architecture; the census earns the right to.
