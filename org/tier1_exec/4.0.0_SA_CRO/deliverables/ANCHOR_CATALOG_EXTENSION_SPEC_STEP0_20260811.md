# STEP-0 MEASUREMENT + ANCHOR-CATALOG EXTENSION SPEC (deterministic 82% -> ~100% of current population)

**Author:** `4.0.0_SA_CRO~B` · Executing the APPROVED substrate/cascade plan (Andrew GO 2026-08-11).
**Routes to:** `3.0.0_SA_CVO` (executes under CTO gate, queued behind parity per their ACK 172653Z).
**Measured on:** `kimi_subdivision_harness/c2_instances.json` (6,138 instance-grain C2 instances) +
`NFRA_MOTIF_P1_canonical_ab_catalog.py` (the ruled catalog).

## 1. THE CATALOG TODAY (measured)
`ANCHOR_CATALOG`: 8 anchor types / 5 domains, ALL AWS-shaped -- object-data{S3_BUCKET,S3Key} ·
compute-orchestration{EVENT_RULE,STATE_MACHINE} · pipeline{PipelineScript,PipelineFunction} ·
table-data{DYNAMODB_TABLE} · identity{IAM_ROLE}. `HUB_TYPES`{LAMBDA,EC2_INSTANCE,actor} correctly
excluded (a hub anchor would re-create the over-merge). **Zero portal anchors, zero ms anchors.**

## 2. THE UNANCHORED 1,103 -- four families, counted (NOT noise)
Anchored: **5,035 of 6,138 (82.0%), all BACKEND.** Unanchored 1,103 = 1,001 FRONTEND + 102 BACKEND:

| family | n | member types present | candidate anchor |
|---|---|---|---|
| `b-dataflow` (FRONTEND) | **951** | Field | **Field** (fine) or ReactComponent (coarse) -- THE PORTAL-SUBSTRATE GAP, 86% of the whole shortfall |
| `a-api` | 82 | API_GW, API_ROUTE | **API_GW** (the gateway is the anchor; routes are members) |
| `a-serve` | 50 | DataFetch, Endpoint, ServedURL | **ServedURL** (the served artifact is the anchor) |
| `a-watch` | 20 | CW_ALARM | **CW_ALARM** (modeling EXISTING alarms; no alarm is built -- moratorium untouched) |

## 3. THE RECOMMENDATION -- four anchor-type additions, yields counted
Adding {portal-side anchor for b-dataflow} + {API_GW} + {ServedURL} + {CW_ALARM} anchors takes
deterministic anchoring **82.0% -> ~100% of the CURRENT instance population** -- clearing the >=90%
floor with the inferential budget untouched for genuinely-ambiguous cases and future growth.
- ✅ **GRAIN RULED (CVO 173143Z): portal anchor = `Field` (fine).** Not only the say-B precedent -- the
  substantive reason: the deterministic floor is NODE-KEYED everywhere else, and anchoring at
  `ReactComponent` (442 nodes) would map 951 fine structures onto ~442 coarse anchors -- **UNDER-COVERING
  BY CONSTRUCTION** (many structures share a component; the coarse anchor cannot distinguish them),
  reopening the exact shortfall this extension closes. `Field` makes the ~100% real rather than nominal.
  ⛔ **THIS IS A GRAIN-CONSISTENCY CHOICE (match the existing anchor grain), NOT a fresh preference** --
  recorded so a future reader does not "simplify" it to component-grain and silently drop coverage.
- ✅ **DOMAIN NAMES RATIFIED (Andrew-direct ~17:5xZ, "All approved as recommended"):** `api-serving`
  (API_GW) · `artifact-serving` (ServedURL) · `observability` (CW_ALARM) · `ui-dataflow` (Field). The
  <=1% naming act is CLOSED; step-0 lands with final names.

## 4. HONEST BOUNDS (what this does NOT cover)
- The 6,138 population = where the C2 EXTRACTORS have run (aws-backend + portal-frontend). The
  **codebase substrate** (ajb_workspace beyond PipelineScript/Function) and **ms** are NOT in this
  population -- full four-substrate coverage ALSO needs the C2 extraction runs over those substrates
  (the next measured step), plus the substrate relabel (pipeline scripts belong to `codebase`, not
  BACKEND). The catalog extension closes the CURRENT population; it does not conjure the missing ones.
- 617 single-motif domains stay unpromoted (PROMOTE_MIN=2) -- correct, not a gap.

## 5. CVO SHAPING CONSTRAINTS (ACK 172653Z) -- FOLDED, binding on the execution
1. **Loud-unresolved substrate:** no clean {aws|portal|codebase|ms} provenance -> `substrate-UNRESOLVED`
   LOUD, never a silent default. The semctl purge must not leave its nodes defaulting. Enumerate-before-default.
2. **Ceilings are FLOORS-OF-HONESTY:** a node classifies by what it HONESTLY is -- never force-fit into
   deterministic to hold 90%, never hide user-naming inside inferential to hold 1%.
3. **Manifest contract preserved:** the derive feeds the contract-v2 manifest (MSTR-backstop oracle);
   substrate-axis changes preserve its shape or declare the schema change explicitly -- never reshape silently.

## 6. NEXT (in order)
1. This spec -> CVO (execute, CTO gate, parity permitting). 2. I measure the CODEBASE + MS extractor
gap (what C2 extraction over ajb_workspace/ms requires -- the remaining substrates). 3. Reconcile
C3.ii/census on the completed cover. 4. Daily via Kimi SVP.
