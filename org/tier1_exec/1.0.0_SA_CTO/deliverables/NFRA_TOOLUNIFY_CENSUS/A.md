# NFRA_TOOLUNIFY Census -- Lane SS2.A: Deployed-AWS <-> graph PARITY

**author:** `0.8.0_AE_CloudComp~A` · 2026-07-24 · **status:** CENSUS complete, READ-ONLY
**census window:** 2026-07-24T21:41:13Z (dispatch) - 2026-07-24T23:35:27Z (final graph.json re-check)
**sidecar:** `A.json` (full tabular data, machine-readable)
**boundary:** live-AWS vs graph COUNT/coverage parity only. Iceberg/Nessie substrate = base's lane. Tool-to-source mapping = ~D's lane. Reporting disagreements, not fixing either graph.

---

## Headline verdict on the two load-bearing questions

1. **LAMBDA 333 (graph.json) vs 191 (kuzu) vs live: LIVE = 191. kuzu is CORRECT. graph.json is the outlier**, and the mechanism is fully source-grounded (not inferred) -- see F1.
2. **COMPONENT 24 (graph.json) vs 641 (kuzu, as previously reported): "641" is not a real number.** It is the sum of two structurally different kuzu populations (file-grain + symbol-grain) that should never have been added. See F2.

Both are **grounded mechanism findings**, not "unexplained candidate defects" -- source cited throughout.

---

## F1 -- LAMBDA: graph.json's 333 is inflated by two concrete, source-cited extractor defects

**Live AWS (ground truth):** 191 Lambda functions. Verified twice independently: (a) manual page-sum
50+50+50+41=191 from `aws lambda list-functions` under CLI auto-pagination text-mode, (b) full-aggregate
JSON parse of the complete paginated response, 191 distinct `FunctionName`s, 0 duplicates. Pulled
2026-07-24T22:29-22:31Z.

**kuzu:** 191 (`comp-kuzu "MATCH (n) RETURN n.node_type, count(*)..."`, DB built 2026-07-24T18:01:18Z, Nessie
HEAD current). **Matches live exactly.**

**graph.json:** 333 (`.comp-graph/graph.json`, built_at 2026-07-24T20:30:49.417799Z, stable across the
entire census window -- re-checked at close, unchanged).

**Mechanism, traced to source** (`org/modules/graph/extract_s3.py:587-620`): the LAMBDA-node builder does
`lambda_dir.rglob("*.py")` across the **entire** `infra/aws/lambda/` tree at **any depth**, excluding only
`__*.py` and paths containing the literal substring `layer`. It derives a "Lambda name" from
`parts[-2]` (the immediate parent directory two levels up from the matched `.py` file), with no bound on
recursion depth and no vendored-dependency exclusion.

Two Lambda source directories violate CLAUDE.md Rule 3 (`No pip install -t . into source dirs`) by
vendoring third-party packages directly inside their Lambda directory instead of a Layer:
`infra/aws/lambda/portal_data_proxy/_build_tmp/` (a literal build-temp dir containing a full vendored
`openai` SDK + deps) and `infra/aws/lambda/v2_portal/`, plus smaller vendor pockets in
`daily_agenda_generator/package/` and `trade-pipeline/`. Every unique subdirectory name inside those vendor
trees (`_internal`, `_utils`, `chat`, `audio`, `beta`, `webhooks`, ...) mints a phantom LAMBDA node under
this codepath. **Exact count: 115 phantom nodes**, reproduced by walking the live tree with the extractor's
own logic and cross-matched against the actual node `file_path`s in graph.json (depth>6 or
label-starts-with-underscore is a 100% precise discriminator here; verified by directly resolving two
sample node file_paths).

Separately, the same extractor creates **two node IDs for one physical Lambda** when the on-disk directory
name (snake_case) differs from the TF-canonical name (kebab-case / prefixed) -- e.g.
`infra/aws/lambda/bd_transaction_consolidator/lambda_function.py` produces both
`lambda:bd_transaction_consolidator` and `lambda:opal-bd-transaction-consolidator`. A `yang-` prefix
special-case is handled; 29 other pairs are not. **Exact count: 30 excess node-ID slots** (29 file_paths x
2 IDs each = 58, plus one triple, netting 30 excess over the true physical count).

`333 - 115 (vendored phantoms) - 30 (alias duplicates) = 188` -- within one of the CI source-map registry
(192) and live/kuzu (191). The residual is explained by registry drift, not the extractor:
`infra/aws/lambda/ci/lambda-source-map.json` (192 entries, working tree, uncommitted 2-line diff at read
time) has **4 live-deployed Lambdas never registered** (`m365-ms-ingest-liveness`,
`opal-49f-served-guard`, `opal-cot-served-guard`, `opal-inf-served-guard` -- a live Rule-4 CI-drift-detection
gap) and **5 registered Lambdas that are not deployed** (`bd-client-detail`,
`find-insure-serving-companies/-consolidate/-employees/-scoring`).

**Verdict: submodule blindness -- NO. Vintage -- NO (graph.json is fresh, 2h old, and stable). Extractor gap
-- YES, precisely two of them, both in `extract_s3.py`'s unbounded `rglob`.** kuzu and live need no
correction; graph.json's LAMBDA population is not trustworthy as a count until the extractor excludes
vendored-dependency trees and resolves its own aliasing.

---

## F2 -- COMPONENT: "641" is a category error, not a count

**kuzu carries TWO separate node types for the portal component surface**, confirmed by directly sampling
each (`comp-kuzu --json "MATCH (n:CloudNode) WHERE n.node_type='...' RETURN n LIMIT 3"`):

- **`Component` (199 nodes)** -- FILE-grain. `node_id = "component:portal/src/components/AccountDistributionChart.tsx"`,
  `props: {"coarse": true, "path": "..."}`. One node per component **file**, scoped to the whole
  `portal/src` tree (live count of all `.tsx` under `portal/src`: 210 -- kuzu's 199 is a plausible near-total
  of that, some gap likely test/type-only files not yet swept).
- **`ReactComponent` (442 nodes)** -- SYMBOL-grain. `node_id = "rc:portal/src/App.tsx#DashboardLayout"`,
  a **second, separate** row `"rc:portal/src/App.tsx#App"` from the **same file**. One node per exported
  component **identifier**, so a single file legitimately contributes multiple rows.

**442 + 199 = 641 exactly.** Someone (CTO~Z's first pass, per the plan doc) summed a symbol-grain
population and a file-grain population that structurally overlap -- every `ReactComponent` row's file
should also have a `Component` row for the same file. This is not "kuzu says 641 components exist"; it is
two different questions ("how many component symbols" and "how many component files") added together.
Neither 442 nor 199 alone is wrong; the sum is meaningless.

**graph.json's 24** is real but doubly narrow, traced to source
(`org/modules/graph/extract_api.py:5,192-198`, docstring line 5): it scans **only**
`portal/src/pages/**/*.tsx` (live count: 122 files -- `portal/src/components/`'s 38 files and the other 88
non-page `.tsx` files anywhere are structurally invisible to this extractor, regardless of content), **and**
within that scope a node is only created for a file that calls a detected API-endpoint-wrapper function.
COMPONENT here is a byproduct of API-route tracing, not a component inventory -- it was never designed to
answer "how many components exist."

**Verdict: not a vintage or submodule-blindness issue.** graph.json's undercount is a **declared, narrow
scope** (by design, for a different purpose than component-census). kuzu's "overcount" is a **grain
conflation introduced when reporting it**, not a defect in either underlying kuzu population. The correct
single-number answer to "how many portal components are there" is **kuzu's `Component` = 199** (file-grain,
full-tree), cross-checked against a live count of 210 `.tsx` files under `portal/src`.

---

## Paginated live AWS counts (the other MUST-CLOSE item)

All below are **full-paginated, aggregated totals** -- not first-page floors. Pulled 2026-07-24T22:29Z-22:43Z.
Every count was independently re-derived by a second method as a positive control after CTO~Z's
per-page-`length()`-reduction warning (see note below); all matched on the first pass.

| Resource | Live (paginated) | kuzu | graph.json | Agreement |
|---|---|---|---|---|
| Lambda functions | **191** | 191 | 333 | live=kuzu; graph.json inflated (F1) |
| EventBridge rules | **141** | 141 | 63 | live=kuzu; 3-way confirmed (this lane + ~C + kuzu) |
| Step Functions | **1** | 1 | 1 | full agreement |
| SQS queues | **12** | 12 | 5 | live=kuzu; graph.json partial (declarative-only extraction) |
| S3 buckets | **39** | 39 | 4 | live=kuzu; graph.json partial |
| DynamoDB tables | **37** | 37 | n/a | live=kuzu; graph.json has no DYNAMODB_TABLE type |
| IAM roles | **206** | 193 | n/a | live > kuzu by 13 -- see below |
| IAM policies, customer-managed | **30** | 442 (conflated) | n/a | see below |
| IAM policies, all scope | **1567** | -- | -- | raw `--query length()` under `--no-paginate` gave the documented page-floor of 100; full-paginated = 1567 |

**Pattern:** for every resource kuzu models with a single unambiguous node type (Lambda, EventBridge, SFN,
SQS, S3 buckets, DynamoDB), **kuzu = live, exactly, every time.** graph.json is the plane that diverges, and
only for the categories it derives from local static source-code analysis rather than a declarative
resource list. This directly answers the mission's framing question: **it is graph.json, not kuzu, that
"miscounts our own estate"** for the two flagged disagreements.

**IAM roles (206 live vs 193 kuzu):** the one resource class where **kuzu itself lags live**, not
graph.json. `comp-iam live`'s own provenance header discloses why: its 193-role population comes from a
"full-derive" cohort **20.6h old**, and explicitly states *"incremental pipe: NOT CHECKED (--pipe) -- the
'plus mutations since' half of the freshness claim is UNVERIFIED"* and *"population cross-check:
UNAVAILABLE (no --census) -- the graph population is TAKEN ON TRUST."* This is a genuine kuzu-staleness
gap for IAM roles specifically (13 roles created/changed since the last full derive), not present in the
other resource classes checked. graph.json has no IAM_ROLE node type at all.

**IAM policies (442 kuzu vs 30 live customer-managed):** grounded, not a vintage issue. Classified all 442
kuzu `IAM_POLICY` node_ids by ARN pattern: **16** are real customer-managed policy ARNs
(`arn:aws:iam::313476888478:policy/...`), **10** are AWS-managed policies actually attached somewhere, and
**416** use a synthetic pseudo-ARN kuzu invented for **inline policies**
(`arn:aws:iam::313476888478:role/<RoleName>/inline/<PolicyName>` -- real inline policies have no ARN at
all). So kuzu's `IAM_POLICY` conflates three structurally different AWS concepts under one node type -- the
same "grain conflation" pattern as F2, on a different resource. The residual gap (16 kuzu customer-managed
vs 30 live, of which 21 are attached) is only **partially** explained by attachment status (9 of the 30 are
confirmed unattached/orphaned) -- 5 remain unaccounted and are flagged as an open **candidate coverage
defect**, not resolved.

**Positive control on the counting method itself** (per CTO~Z's explicit ask after ~C hit the same trap on
EventBridge): `aws <svc> list-* --query 'length(X)' --output text` under CLI auto-pagination prints a
**separate reduction per page** (observed directly: `50` / `50` / `50` / `41` for Lambda, summing to the
correct 191 -- NOT one aggregate number). Every count in this report was taken from a **full-aggregate JSON
parse** (fetch all pages, `len()` the assembled list in Python), independently re-derived a second way for
Lambda/SF/SQS/S3/DynamoDB/EventBridge, with identical results both ways -- the method is not page-capped.

---

## The 7 GLOBGRPH layers: populated vs declared (`docs/architecture/NFRA_GLOBGRPH_PRD.md` SS4.4)

Full table in `A.json` -> `globgrph_7layer_reconciliation`. Summary across the PRD's **41** declared node
classes (the PRD's own header text says "40 total" -- the table itself has 41 rows; a minor doc-internal
inconsistency, noted for the record):

- **14 exact name match** in kuzu (API_ROUTE, LAMBDA, STATE_MACHINE, EC2_INSTANCE, EVENT_RULE, EVENT_SOURCE,
  SQS_QUEUE, SNS_TOPIC, S3_BUCKET, DYNAMODB_TABLE, SECRET, IAM_ROLE, IAM_POLICY, KMS_KEY)
- **9 populated under a renamed/abbreviated variant** (`Component`/`ReactComponent` for `PORTAL_COMPONENT`,
  `Hook` for `PORTAL_HOOK`, `Page` for `PORTAL_PAGE`, `ReactQueryKey` for `REACT_QUERY_KEY`,
  `ECS_TASK_DEFINITION` for `ECS_TASK_DEF`, `SCHEDULE` for `EVENTBRIDGE_SCHEDULE`, `API_GW` for
  `API_GATEWAY`, `S3Key` for `S3_DATA_KEY`, `Pipeline` for `PIPELINE`)
- **18 with no analog under any recognizable name** -- including, strikingly, **`GOLD_SCRIPT`**: graph.json's
  single largest node population (1365 nodes, 60% of its entire 2255-node graph) has **zero exact-name
  presence in kuzu**. The nearest candidates, `PipelineFunction` (1201) and `PipelineScript` (133), differ
  from each other by an order of magnitude, let alone from graph.json's 1365 -- three different grains for
  what should be the same "gold pipeline code" surface. This sits adjacent to base's Iceberg-substrate lane;
  flagging the count-parity gap here, not chasing the pipeline-internals mechanism (out of this lane's
  boundary).
- Entire **L7 (EXTERNAL_API / EXTERNAL_FEED / CLOUDFRONT_ORIGIN)** is unpopulated under any name.
- Five of **L1**'s nine classes (`PORTAL_BUNDLE`, `PORTAL_CONTEXT`, `PORTAL_UTIL`, `PORTAL_STORE`,
  `PORTAL_TYPE`) and all of **L5**'s script-taxonomy classes except `PIPELINE`
  (`BRONZE_SCRIPT`/`SILVER_SCRIPT`/`GOLD_SCRIPT`/`LAMBDA_SCRIPT`/`TRANSFORM`/`BACKFILL_SCRIPT`) are
  unpopulated under any name.

**The bigger finding runs the other direction.** kuzu carries **34 node types entirely outside the PRD's
declared vocabulary**, totaling **17,950 of its 20,403 nodes -- 88%** of the entire live kuzu population:

- **M365 surface (5,669 nodes: MS_FILE/MS_FOLDER/MS_USER/MS_SITE/MS_LIBRARY)** -- not in the PRD's layer
  taxonomy at all (no L8/M365 layer declared). This directly corroborates ~C's parallel lane finding: M365
  is a real, heavily-populated plane, not a stub -- it's simply absent from the governing schema. Surfacing
  for ~C's benefit, not duplicating their characterization work.
- **A TypeScript semantic-analysis layer (11,587 nodes: Field/TypeDecl/Module/Prop/JSXElement/JSXRender/
  PipelineFunction/PipelineScript/DataFetch)** -- almost certainly the plan doc's `ts-semantic` producer,
  entirely outside SS4.4.
- **386 nodes of organic AWS-infrastructure accretion** (LOG_GROUP, CW_ALARM, SECURITY_GROUP,
  INSTANCE_PROFILE, SERVICE_PRINCIPAL, S3_BUCKET_POLICY, VPC_ENDPOINT, ROUTE53_RECORD, LOAD_BALANCER,
  ECS_CLUSTER, CLOUDFRONT_DISTRIBUTION, CODEBUILD_PROJECT, IAM_USER, LAMBDA_LAYER) -- reasonable additions
  the estate has grown organically, simply never folded back into SS4.4.
- **159 nodes of unclear purpose** (`PanelCluster`, `ServedURL`, `C2Motif`, `C3System`) -- inferred, not
  source-confirmed, to be debt-scan/motif-analysis-related from adjacent filenames
  (`org/modules/graph/debtscan/canon_motif`). Flagged as **could-not-fully-verify**, not chased further
  (out of boundary / lower value than the grounded findings above).

**Cert-bar note:** the PRD states *"UNCATEGORIZED = 0 is the cert bar."* That is **literally true** -- no
kuzu node carries a generic `UNCATEGORIZED`/`OTHER`/`UNKNOWN` type. But the **spirit** of a closed vocabulary
does not hold: the graph has organically accreted 34 specifically-named types that were never folded back
into the governing schema, and they are not a rounding error -- they are 88% of the graph. Letter of the law
passes; spirit does not.

---

## Could-not-fully-verify (per SS3.4, printed as findings, not papered over)

1. The 5-node residual gap between kuzu's customer-managed-policy count (16) and live attached
   customer-managed policies (21) -- partially explained, not fully closed.
2. `PanelCluster` / `ServedURL` / `C2Motif` / `C3System` kuzu node types -- purpose inferred from adjacent
   filenames only, not source-confirmed producer.
3. Whether graph.json's 24 COMPONENT nodes are a strict path-level subset of kuzu's 199 `Component` nodes --
   not cross-joined (would need per-path matching); the mechanism-level finding (scope + filter) already
   fully explains the count gap without this join.

## Acceptance check (against SS2.A's own bar)

*"Every disagreement between live / kuzu / graph.json has a grounded cause or an explicit 'unexplained --
candidate coverage defect' with its denominator."* -- LAMBDA: grounded (F1). COMPONENT: grounded (F2). IAM
roles: grounded (kuzu staleness, cited from the tool's own disclosure). IAM policies: grounded (grain
conflation) with one honest residual flagged as a candidate defect with its denominator (5 of 30). GLOBGRPH
7-layer: fully reconciled, 41/41 classes dispositioned, undeclared population quantified and categorized
with one sub-category (159 nodes) flagged unexplained.
