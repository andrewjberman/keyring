# NFRA_TOOLUNIFY Census SS2.A -- Deployed-AWS <-> graph PARITY -- 0.8.0_AE_CloudComp~A

**archetype:** TRACE
**secondary_archetypes:** DIAGNOSE, VALIDATE
**Date:** 2026-07-24
**Task Order:** NFRA_TOOLUNIFY.CENSUS (ad-hoc dispatch, off-main-fabric ~Z group; no TO file, MCP dispatch only)
**Status:** COMPLETE

---

## Objective

CTO~Z dispatched a 5-lane read-only estate census (`docs/briefs/NFRA_TOOLUNIFY_ESTATE_CENSUS_PLAN_20260724.md`)
to establish ground truth before any TOOLUNIFY ontology/architecture decision. My lane (SS2.A) owned
live-AWS vs graph (local `graph.json` + kuzu-from-Nessie) COUNT/coverage parity -- specifically grounding
two named disagreements (LAMBDA 333/191/live, COMPONENT 24/641) plus full paginated live counts across
Lambda/EventBridge/SFN/SQS/S3/DynamoDB/IAM and a populated-vs-declared reconciliation of the GLOBGRPH
7-layer taxonomy. Off-main-fabric: report to `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` only, no COO/MSTR.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-kuzu | `MATCH (n) RETURN n.node_type, count(*) ...` | PASS | full node-type census, 58 types, 20403 nodes, provenance header read (Nessie HEAD current, graph_nodes table flagged STALE>6h) |
| comp-kuzu | `MATCH (n:CloudNode) WHERE n.node_type='ReactComponent'/'Component' RETURN n LIMIT 3` | PASS | raw node dump revealed the file-grain vs symbol-grain split that explains the COMPONENT 641 figure |
| comp-kuzu | `MATCH (n:CloudNode) WHERE n.node_type='IAM_POLICY' RETURN n.node_id,...` | PASS | full 442-row dump, classified by ARN pattern -- found the inline-policy synthetic-pseudo-ARN conflation |
| comp-iam | `stats` | PARTIAL | TF-parsed (DESIRED) count only, 163 roles -- correctly not usable as a live-primary number, noted and moved past |
| comp-iam | `live` | PASS | disclosed its own population is kuzu-sourced (193 roles, 20.6h-old full-derive cohort) with an explicit "population cross-check UNAVAILABLE / taken on trust" self-flag -- directly explained the live(206)-vs-kuzu(193) IAM role gap |
| raw `aws lambda/events/stepfunctions/sqs/s3api/dynamodb/iam` list-* | rail-checked (see below) | PASS | fresh paginated live counts; every one full-aggregate-parsed, several independently re-derived a second way as a positive control |

`# rail-checked:` used for the raw live-AWS headcounts (Lambda/EB/SF/SQS/S3/DDB/IAM roles+policies): no
`comp-iam`/`comp-aws` subcommand performs a fresh unfiltered boto3 headcount for a cross-plane parity
census -- `comp-iam stats` is TF-DESIRED, `comp-iam live` is itself kuzu-sourced (confirmed by its own
provenance header), neither is a live primitive. Logged per Rule 21.

**What worked:** `comp-kuzu`'s raw node dump (not just counts) was the single highest-value move of the
session -- sampling actual `node_id`/`props` fields on `ReactComponent` vs `Component` and on `IAM_POLICY`
directly exposed two independent grain-conflation defects (component symbol-vs-file, IAM policy
customer-managed-vs-inline) that a bare count comparison would have left as "unexplained." `comp-iam live`'s
self-disclosed provenance ("population cross-check UNAVAILABLE... taken on trust") was itself the finding
for the IAM-role gap -- no extra digging needed once read.

**What failed:** none outright, but `aws <svc> list-* --query 'length(X)' --output text` under CLI
auto-pagination silently reduces PER PAGE (confirmed directly: printed `50`/`50`/`50`/`41` for Lambda
instead of one aggregate `191`) -- a live trap, not a tool failure, but it cost one retry and prompted a
full re-verification pass on every other count via full-aggregate JSON parsing after CTO~Z's warning (~C
hit the identical trap independently on EventBridge).

**Gap found:** no comp-tool currently does a fresh, unfiltered, live-AWS resource headcount for
cross-plane-parity purposes (comp-iam's two modes are TF-desired or kuzu-sourced-not-fresh-live; there is
no `comp-aws census --live` equivalent for Lambda/EventBridge/SFN/SQS/S3/DynamoDB counts). Flagging for
~D's tool-register lane (TOOLUNIFY SS2.D) -- this is exactly the kind of `reads[]` classification gap their
mission is scoped to catalog, not mine to fix.

Compiler-tools-log.md line appended.

---

## Work Completed

### 1. Local plane (graph.json) full census
Pulled the complete node-type breakdown of `.comp-graph/graph.json` (2255 nodes, `built_at`
2026-07-24T20:30:49.417799Z, stable and unchanged across the entire ~3h census window on re-check at
close): GOLD_SCRIPT 1365, LAMBDA 333, S3_ARTIFACT 321, ENDPOINT 138, EVENTBRIDGE 63, COMPONENT 24,
SQS_QUEUE 5, S3_BUCKET 4, STATE_MACHINE 1, SNS_TOPIC 1.

### 2. LAMBDA disagreement -- fully grounded at source
Traced `org/modules/graph/extract_s3.py:587-620`'s unbounded `rglob("*.py")` Lambda-name extraction.
Reproduced its logic against the live tree and cross-matched against graph.json's actual LAMBDA node
`file_path`s: **115 phantom nodes** from walking into `pip install -t .`-vendored dependency trees
(`portal_data_proxy/_build_tmp/` has a full vendored `openai` SDK -- a Rule-3 violation site; also
`v2_portal/`, `daily_agenda_generator/package/`, `trade-pipeline/`), plus **30 excess node-ID slots** from
uncorrected directory-name-vs-TF-canonical-name aliasing (29 physical Lambdas each claim 2 node IDs).
`333-115-30=188`, closing to source-map registry (192) and live/kuzu (191). Live AWS Lambda count verified
twice independently (page-sum 50+50+50+41=191; full-aggregate parse, 191 distinct names, 0 dupes) --
**exact match to kuzu.** Bonus finding: diffed live vs the CI source-map registry directly -- 4 live Lambdas
never registered (`m365-ms-ingest-liveness`, `opal-49f-served-guard`, `opal-cot-served-guard`,
`opal-inf-served-guard`), 5 registered Lambdas not deployed.

### 3. COMPONENT disagreement -- fully grounded at source
Sampled kuzu's `ReactComponent` (442) and `Component` (199) node types directly: `ReactComponent` is
SYMBOL-grain (`node_id="rc:<file>#<ComponentName>"`, multiple rows per file), `Component` is FILE-grain
(`node_id="component:<path>"`, `props:{"coarse":true}`). **442+199=641 exactly** -- the previously-reported
"641" sums two structurally different populations. Traced graph.json's 24 to `extract_api.py:5,192-198`:
scoped to `portal/src/pages/**/*.tsx` only (122 live files; `components/`'s 38 files + 88 other non-page
`.tsx` files are structurally invisible) AND filtered to files calling a detected API-endpoint wrapper.
Live cross-check: 210 total `.tsx` under `portal/src`, 122 under `pages/` -- neither graph.json's 24 nor the
naive "641" is the right single answer; kuzu's `Component`=199 is.

### 4. Paginated live AWS counts, full triangulation
Lambda/EventBridge/StepFunctions/SQS/S3/DynamoDB/IAM roles+policies, all full-paginated (not first-page
floors), each with an explicit UTC timestamp. Result: for every resource kuzu models under one unambiguous
node type (Lambda, EventBridge, SFN, SQS, S3 buckets, DynamoDB), **kuzu = live exactly**. EventBridge (141)
independently 3-way confirmed against `~C`'s separately-run paginated count and kuzu's stored value. IAM
roles: live=206 vs kuzu=193 -- the one place kuzu itself lags live, grounded via `comp-iam live`'s own
freshness self-disclosure (20.6h-old cohort, incremental pipe unverified). IAM policies: kuzu's 442
classified by ARN pattern -- 16 real customer-managed, 10 AWS-managed-attached, 416 using a synthetic
`role/.../inline/...` pseudo-ARN for inline policies (same grain-conflation pattern as COMPONENT, different
resource); live customer-managed=30 (verified untruncated), 21 attached / 9 orphaned -- residual 5-node gap
flagged as partially-explained, not fully closed.

### 5. GLOBGRPH 7-layer populated-vs-declared reconciliation
Read `docs/architecture/NFRA_GLOBGRPH_PRD.md` SS4.4 (41 declared node classes across L1-L7; PRD header text
says "40 total" -- a minor doc-internal count mismatch, noted). Classified all 41 against kuzu's live
node-type list: 14 exact-name match, 9 populated under a renamed/abbreviated variant, 18 with no analog
under any name -- including graph.json's single LARGEST category, GOLD_SCRIPT (1365 nodes, 60% of its
graph), which has zero exact-name presence in kuzu (nearest candidates `PipelineFunction`(1201)/
`PipelineScript`(133) differ from each other by an order of magnitude). Entire L7 unpopulated. Bigger
finding in the other direction: kuzu carries **34 node types entirely outside the declared vocabulary**,
totaling 17,950 of 20,403 nodes (88%) -- dominated by the M365 surface (5,669 nodes: MS_FILE/MS_FOLDER/
MS_USER/MS_SITE/MS_LIBRARY, corroborating `~C`'s parallel finding that M365 is a real populated plane, not
a stub) and an apparent `ts-semantic` code-analysis producer (11,587 nodes: Field/TypeDecl/Module/Prop/
JSXElement/JSXRender/PipelineFunction/PipelineScript/DataFetch). PRD's "UNCATEGORIZED=0 cert bar" holds
literally (no generic escape-hatch type exists) but not in spirit (88% of the graph is specifically-named
yet undeclared).

### 6. Deliverable
Wrote `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/A.md` (227 lines) +
`A.json` (machine-readable sidecar, validated parses) to disk per CTO~Z's commit-policy note (that path is
owned-paths-gated to CTO's BASE_EXEC lane -- I write to disk, CTO~Z commits into his own lane; I did not
attempt a commit there). Notified CTO~Z with the full headline-findings summary.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Used `# rail-checked:` override for raw live-AWS headcounts instead of forcing a comp-iam call | Neither `comp-iam stats` (TF-desired) nor `comp-iam live` (kuzu-sourced, self-disclosed non-fresh) performs the fresh live enumeration this census needs; forcing one would have produced a wrong-plane answer, not a right one |
| Re-verified every live count via full-aggregate JSON parsing after the per-page-`length()` warning, even ones already gathered via a safe method | CTO~Z's ask was explicit ("positive-control at least one count") and the stakes (the load-bearing LAMBDA verdict) warranted eliminating doubt rather than asserting the method was already safe |
| Did not chase the PanelCluster/ServedURL/C2Motif/C3System kuzu types or the GOLD_SCRIPT/PipelineFunction grain question to full resolution | Both are adjacent to base's (Iceberg substrate) or ~D's (tool-source mapping) boundary per the plan's own non-overlap rule; reported as grounded-partial / could-not-fully-verify rather than over-reaching into another lane's scope |
| Skipped the ms_heat EventBridge fold-in CTO~Z originally asked for | CTO~Z retracted the ask mid-session once ~C closed it independently with the same paginated data (141 rules, 0 heat matches) -- avoided duplicate work per his explicit instruction |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/A.md` | New census deliverable | No -- written to disk only; owned-paths-gated to CTO's lane, he commits per his own instruction |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/A.json` | New machine-readable sidecar | No -- same as above |
| `org/mcp/sessions/{session_id}.serial` | Session-keyed serial file (LD-0290) | N/A -- session-local, not a versioned artifact |
| `.comp-graph/.agent_context` | SERIAL context for auto-logging | N/A -- session-local |

No code, infra, or pipeline files touched -- this was a strictly READ-ONLY census per the plan's SS3.2
binding (no apply/deploy/re-point/regenerate/schema-change).

---

## Blockers

None. Fully event-driven this session: startup -> dispatch arrived -> ACKed -> executed -> delivered, no
waits on another agent's output.

---

## Current State

Census complete and delivered to `1.0.0_SA_CTO~Z` at 2026-07-24T23:39:25Z (MCP `DELIVERABLE READY`
message). Deliverable sits on disk, uncommitted, awaiting CTO~Z's consolidation commit into his BASE_EXEC
lane alongside the other 4 census lanes (base/~B/~C/~D). Both named load-bearing questions
(LAMBDA 333/191/live, COMPONENT 24/641) are fully mechanism-grounded with source citations
(`org/modules/graph/extract_s3.py:587-620`, `org/modules/graph/extract_api.py:5,192-198`) -- no further
action needed on either unless CTO~Z's consolidation surfaces a conflict with another lane's findings.
Three items are explicitly flagged could-not-fully-verify in `A.json` (5-node IAM policy residual,
4 unclear kuzu node-type purposes, no path-level COMPONENT join) -- none block the census acceptance bar,
which the deliverable's own closing section checks against SS2.A's stated criteria. Standing by,
event-driven, for CTO~Z's consolidation pass or a new dispatch.

---

## Next Steps

1. **Standing by** for `1.0.0_SA_CTO~Z` to consolidate the 5 census lanes into one estate map (his stated
   SS4 responsibility) -- no action pending on my side unless he routes a follow-up.
2. **[0.8.0_AE_CloudComp~D]** may find the "no comp-tool does a fresh live headcount" gap (Compiler Tools
   section above) directly relevant to the `reads[]`/`evaluation` classification their tool-register lane
   is building -- surfaced here for their awareness, not routed directly (off-main-fabric isolation: report
   to CTO~Z/CVO~Z only, no lane-to-lane MCP).
