# CODEBASE + MS EXTRACTOR-GAP MEASUREMENT (the remaining two substrates)

**Author:** `4.0.0_SA_CRO~B` · Step 2 of the approved plan. Companion to
@ANCHOR_CATALOG_EXTENSION_SPEC_STEP0 (which closes the CURRENT population; this sizes the missing ones).
**Routes to:** CVO (execution owner, CTO gate) same as step 0.

## 1. WHERE THE FOUR SUBSTRATES STAND (measured)

| substrate | graph nodes | C2 instances | state |
|---|---|---|---|
| **aws** | full (S3/DDB/IAM/events/SFN/Lambda/...) | 5,137 BACKEND | COVERED (step-0 closes its 102 residue) |
| **portal** | full (Field 4,969 / JSXElement 2,205 / ReactComponent 442 / TypeDecl 807 ...) | 1,001 FRONTEND | NODES + INSTANCES exist; step-0's Field anchor promotes them into the cover |
| **codebase** | **PIPELINE SLICE ONLY** (PipelineScript + PipelineFunction ~1,201, from data/ gold scripts -- currently mis-attributed BACKEND) | inside the 5,137 | **THIN: the rest of ajb_workspace (.tools ~90 comp executables, org/modules graph tooling, infra python) is NOT node-ified at all** -- no nodes -> no instances -> structurally invisible to the cover |
| **ms** | **MS_FILE 4,779 + MS_FOLDER 1,055 EXIST** (NFRA_MSGRAPH) | **ZERO** | nodes exist, NO C2 motif has ever run over them; the anatomy records ms as PARKED pending Andrew ("we can get to how ms...") |

## 2. WHAT EACH GAP REQUIRES (sized, distinct remedies -- Rule-24 state coherence: they do NOT move together)

**CODEBASE -- an EXTRACTOR BUILD (the larger of the two):**
- Node-ify the non-pipeline python/tooling surface at **module/function grain** via AST. The grain is
  already ruled: RCN-0006's `PYTHON_FIELD_GRAIN_FEASIBILITY` (CTO~D ruled (b)+(c)-as-policy) established
  Python FIELD-grain is not feasibly deterministic (`df["col"]` == `cfg["key"]` to the AST; no
  TypeChecker analogue) -- **module/function grain is the deterministic ceiling for python, and that is
  fine: the anchor model is node-keyed, not field-keyed.**
- New C2 motif specs for code motifs (tool->registration, module->consumer, script->emitted-artifact).
- Anchor candidates for the catalog: `Module` / `ToolExecutable` / `PyFunction`.
- Substrate relabel folds in: PipelineScript/Function move BACKEND -> `codebase` (they are repo files;
  their RUNTIME lambdas stay `aws` -- the node is the code, the runtime is the cloud resource).
- Sizing: ~25k tracked files; the ACTIVE python surface (.tools + org/modules + data scripts + infra
  python) is the extraction target, gated per RCG's ACTIVE computation rather than blanket.

**MS -- MOTIF SPECS OVER EXISTING NODES (the cheaper), BUT ANDREW-GATED:**
- The nodes already exist (5,834 MS nodes); what is missing is C2 motif specs (content motifs:
  containment, sharing, staleness) + anchor types (`MS_FOLDER` / site / drive as anchors).
- ⛔ **ms is PARKED on Andrew's own prior word** (the anatomy's parked note). Un-parking is HIS call --
  this spec sizes it; it does not start it.

## 3. CONSEQUENCE FOR THE CASCADE MATH
Step-0 gets the CURRENT population to ~100% deterministic. The codebase build then ADDS a population
(new instances over the tooling surface) that arrives pre-anchored (its extractors and anchors are
designed together -- the lesson of step-0: anchors designed WITH the extractor, not retrofitted). ms
adds its population when Andrew un-parks. **At every stage the denominators are printed per substrate,
so "coverage" is never quoted without which substrates are IN.**

## 4. NEXT
1. Step-0 executes at CVO (gate + parity permitting) -> aws+portal covered.
2. Codebase extractor build: needs a BUILD LANE (AE/DS) under CTO gate -- CRO hands this spec; COO staffs.
3. ms: sized here, HELD at Andrew's word.
4. Daily Kimi SVP carries the per-substrate coverage denominators from the first execution onward.
