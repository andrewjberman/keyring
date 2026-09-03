# NFRA_CLDGRPH -- L5 decomposition and battery (COO~A) -- v0.1, the tree decomposition of the second parallel run

**Author:** `2.0.0_SA_COO~A` · 2026-09-03 ~06:0xZ · **L5 of `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` (spine v2.3 @`e9b196b29a`). NO TASK ORDER IS CUT BY THIS FILE.**
**Authority for the run:** Andrew-direct at the `1.0.0_SA_CTO~A` terminal 2026-09-03 ~05:1xZ, record `org/tier1_exec/1.0.0_SA_CTO~A/deliverables/ANDREW_DIRECT_20260903_051xZ_PARALLEL_CANONICAL_FLOW_NFRA_CLDGRPH_WITH_COOA_CVOA.md` @`8e134cc126` (seats: `1.0.0_SA_CTO~A` L2-L4, this lane L5-L6, `3.0.0_SA_CVO~A` L8-L10).
**Input (the manifest):** PRD v0.4 @`25c66d3358`, `../prd/NFRA_CLDGRPH_PRD.md` s.7 SURFACE MANIFEST, rows S1-S13; header `endpoint_outcomes` FWD-1..FWD-8, `status: RATIFIED`, `fabric: laptop`. **Row:** `../project.json` @`36157989a9` (`dep_stage: PRD` at write).
**Lineage:** the flat decomposition `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_CLDGRPH_DECOMP_20260902.md` @`05d2c89158` (`2.0.0_SA_COO`, 13 cells, 6 of 6 OWNS, no TO cut) -- its s.1 rectangle became PRD s.7 at v0.2 and is this file's input by way of the PRD, never directly. What this file ADDS to it: the tree cell ids, the status axis with its NOT-EVALUATED value, the placement axis, dependency edges keyed to OBSERVED completion, the L5 battery run at this vintage, every evidence pin re-read at HEAD, and the CLOSING-PASS cells the spine v2.3 close requires (an outcome whose DONE WHEN is an act after the work is met by a closing-pass task order whose specification is that act). What it does NOT change: no manifest row, no outcome, no ruling, no lane.
**Handoff out of this limb:** `dep_stage: DECOMP`, flipped by the row owner (`1.0.0_SA_CTO~A`, lane `TREE_PROJECT_ROW`) on this commit, as the COMPEFFICACY row was flipped @`867d313020`. L6 consumes this file through `<decomp_ref>`; a defect in it surfaces at L7 as a `DECOMP_INVALIDATING` row and routes back here.

**Method note, stated as a choice (spine s.4, "the choice to use the decomposition method's validator at L5" binds by reading):** the rectangle is the PRD's s.7 manifest -- MEASURED by the base COO on 2026-09-02, re-read by `1.0.0_SA_CTO~A` at v0.2-v0.4, re-pinned at HEAD by this seat (s.3). No `workflows/atom_decomposition/runs/` directory is opened for it and the sealed-mutant self-check is not run: the spine says no seat waits on it, the COMPEFFICACY precedent @`e8641a324c` made the same choice, and this decomposition is falsified where the spine says it is -- at L7, by a worker's row.

---

## 0. What moved between the flat decomposition (2026-09-02) and HEAD (2026-09-03), read before any cell

Every surface in the manifest's `evidence` column was re-read at HEAD `c2c2127f31` (s.3 has the instrument). Four pins moved and one surface is GONE; none changes a row's `claim`, two change a cell's `status`:

| surface | manifest pin (PRD s.7) | at HEAD | consequence |
|---|---|---|---|
| `.tools/comp-kuzu-full`, `.tools/comp-kuzu-inc` (S8 retirement targets) | 16 + 17 lines @`7288d12675` | **ABSENT** -- retired @`dffbee781c` by `NFRA_COMPEFFICACY` cell COMPEFFICACY cell t-22 (the wrappers, 2026-09-02) | **S8 is PARTLY DONE BY A SIBLING PROJECT.** The cell stays OPEN for what remains: the local `kuzu_nessie_db`, `kuzu_cli.py`, the `_canonical.py` rebuild/labeled-stale seam and its fallback sink. Stated here so nobody re-retires a file that is not there. |
| `infra/aws/globgrph/_canonical.py` (S8 seam) | 647 @`c778e3c3d1`, seam at `:344-420` | **746** @`173dd335f4` (CE-G-5, the freshness layer under a budgeted client, 2026-09-03 ~05:2xZ) | the seam moved; re-locate by content (`ensure_fresh`, the mkdir mutex, the stale label). **AND the engine S2 ports now carries CE-G-5's behaviour** (no orphaned rebuild; serve-stale-immediately with the age on the line). S2's bound below says what to do with it. |
| `infra/aws/globgrph/kuzu_cli.py` (S6 target, S8 retirement) | 179 @`834c87c00a` | **189** @`173dd335f4` | same commit; same consequence |
| `.tools/comp-kuzu` (S6) | 28 @`0215abf3ec` | **30** @`dffbee781c` | the wrapper retirement touched it; S6's port starts from 30 lines |
| everything else (S1-S5, S7, S9-S13 pins) | as in s.7 | unchanged: `kuzu_incremental_refresh.py` 350 @`aebe0d0a67`; `kuzu_nessie_load.py` 417 @`e445642c5f`; `graph_status_cli.py` 360 @`ee49b14381`; `registry.py` 67 @`2781aac326`; `item2b.tf` 199 @`e0a3d7fd87`; `nessie.tf` 215 @`d8d0d7d26d`; `_provenance.py` 641 @`996fcad53e` (MARKER_KEY at `:96`) | -- |

The PRD's s.7 `evidence` column is the L4 owner's to re-version; this file does not edit it. `1.0.0_SA_CTO~A` is told in the handoff message, as information, not as a route.

---

## 1. The rectangle

**Domain (postulate i):** the PRD s.3 **OWNS** cell, six items -- the same domain as the flat decomposition and PRD s.7 -- **plus the CLOSING PASS**, six cells, one per outcome whose `DONE WHEN` is `EXERCISED` (FWD-1, 2, 4, 5, 7, 8). The extension is the spine v2.3's word (L10, "The close"), not this seat's: an outcome whose bar is an act after the work is met by a closing-pass task order whose specification IS that act, and the COO's COMPLETION_REPORT must show a cell for it or read UNCOVERED. Declared here so the domain is stated before the cells are counted.

```
  OWNS item                                     cells                          (manifest rows)
  where it is COMPILED (worker + trigger)       CG-s-1 · CG-s-2                 S1, S2
  where it is SERVED FROM (plane + contract)    CG-s-3 · CG-s-4                 S3, S4
  how an agent REACHES it (gateway + client)    CG-s-5 · CG-s-6                 S5, S6
  the vintage bound + plain-words rendering     CG-s-6 (render), CG-s-3 (bound) S6, S3
  the operator status read                      CG-s-7                          S7
  the RETIREMENT of the local copy              CG-s-8                          S8
  acceptance 9 (R10, fixed at the port)         CG-s-9                          S9
  INPUTS the s.6 open-list names (verify rows)  CG-s-10 · CG-s-11 · CG-s-12 · CG-s-13   S10-S13
  THE CLOSING PASS (spine v2.3 close)           CG-x-1 · CG-x-2 · CG-x-4 · CG-x-5 · CG-x-7 · CG-x-8
  DENOMINATOR: 6 of 6 OWNS items covered, 0 uncovered; 19 cells (13 manifest + 6 closing-pass), 0 RETIRED;
               19 of 19 map to an OWNS item, to acceptance 9, to a named input, or to an EXERCISED outcome.
  OUTCOMES: 8 of 8 have >=1 cell -- FWD-1 s4/s5/x-1 · FWD-2 s1/s2/x-2 · FWD-3 s3/s6 · FWD-4 s2/x-4 ·
            FWD-5 s4/s5/x-5 · FWD-6 s6/s8 · FWD-7 s3/s4/s8/x-7 · FWD-8 s7/x-8.  (FWD-3 and FWD-6 are APPLIED bars: no closing-pass cell.)
  RELIES-ON appears only as depends_on or bound; out-of-scope only as bound. No cell is owned by a Tier-0 or Tier-1 seat.
```

**Cell ids** follow `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1 (`PREFIX-<1-4 lowercase>-<digits>`): `CG-s-<n>` IS manifest row S<n> (1:1, ids permanent); `CG-x-<n>` IS the closing pass for FWD-<n> (numbered by the outcome, so the gaps at 3 and 6 are deliberate). All 19 tested against `.tools/proof-of-spec-check.py:377 CELL_ID_RE` before writing (s.3). A bare `S<n>` carries no hyphen and is NOT a cell id to the checker -- `<owned_cells>` names `CG-` ids only.

**Cell vocabulary (Rule 24, with a NOT-EVALUATED value so non-evaluation is never a verdict) -- the same five values as the COMPEFFICACY decomposition, reused verbatim because renaming a shared enum is the defect:**
- `claim` (the manifest's column, unchanged): **measured · absent · unmeasured** -- the evidence state of the SURFACE.
- `status` (this file's column): **DONE** (a terminal task order with a VALID proof-of-spec, or ruled) · **IN-FLIGHT** (a task order open, or a deliverable landed with its proof pending) · **OPEN** (not started) · **HELD** (blocked on a named decision, owner stated) · **NOT-EVALUATED** (this decomposition did not measure it and says so).
- **(ii) same grain:** one row per manifest surface, one row per exercised outcome; never a file, never a task order.
- **(iii) intent coherence:** `claim` answers "what does the world hold at this surface"; `status` answers "how far has this project moved it". Two axes, two columns, never one.
- **(iv) state coherence -- which values one remedy does NOT move:** a worker's VALID proof instance + its own `<status>` flip moves `status` to DONE and nothing else; a `DECOMP_INVALIDATING` row at L9 moves a cell to HELD or adds a cell here (v0.2), never a `claim`; a PRD version bump by the L4 owner moves a `claim` or a pin, never a `status`; the CTO's COMPLETION_GRADES move no cell (they grade outcomes); the integrator's push moves nothing here (push state is a MEASURED field of every DONE test, read by `ls-remote` + `is-ancestor`, never a cell).

### 1a. The manifest cells -- `CG-s-n` IS `S<n>` (surface, claim, lane, verb and bound as PRD s.7 states them; here the STATE, the placement, and the edges)

| cell | = | outcome (+acc) | claim | status now | evidence at HEAD (instrument, s.3) | lane | placement | depends_on -> released by (OBSERVED) | closes on |
|---|---|---|---|---|---|---|---|---|---|
| CG-s-1 | S1 S3 event notification on `warehouse/_branch_head.main.json` -> NEW SQS queue + DLQ | FWD-2 (acc 2) | **absent** | OPEN | DESIRED plane: `aws_s3_bucket_notification` = **0 hits across 32 files** in `infra/aws/terraform/globgrph` (10 binary unsearched); the resource type exists in 6 other TF trees (the pattern is proven, not novel). LIVE plane: the only globgrph queues are `opal-globgrph-incremental-events` + `-dlq` (item2b, fed by the CloudTrail rule, FIRED 17,983x/7d) -- R5's "one writer of five", NOT S1's queue. comp-trigger: BLIND on S3 notifications by its own disclosure -- S1 is unresolved by that instrument. MARKER_KEY is DEFINED in FIVE files (`_provenance.py:96`, `cse_store.py:87`, `derive_runner.py:389`, `fedobs_observe.py:50`, `iceberg_parity.py:56`) -- the five writers R5 names | `0.7.0_AE_CloudOps` | laptop | CG-s-12 -> the verify deliverable names the principal set the queue policy must admit (a DONE proof) | a marker stamp lands ONE message on the new queue: message id + receive timestamp in the deliverable, DLQ empty; a second stamp lands a second (the control that can fail) |
| CG-s-2 | S2 worker running `kuzu_incremental_refresh.py` | FWD-2, FWD-4 (acc 2, 4) | measured | OPEN | 350 lines @`aebe0d0a67`, unchanged since 2026-07-08. **BOUND ADDED AT L5:** the engine it ports now carries CE-G-5 @`173dd335f4` (`_canonical.py` 746: no orphaned rebuild, serve-stale-immediately with the age); R9 keeps O-1 worker-internal -- S2's port DECIDES, in its deliverable, whether CE-G-5's layer is worker-internal (ported) or local-only (retired with S8) and says which; silence is a surprise row | `0.7.0_AE_CloudOps` | laptop | CG-s-1 -> the queue message observed; CG-s-10 -> the duration with its denominator in S10's deliverable (it SIZES the runtime, Lambda vs ECS) | the worker consumes one real marker message and produces the delta artifact; the count-guard and the full-fallback path each exercised once on the record |
| CG-s-3 | S3 versioned artifact + `_build_manifest` + ONE pointer object on S3 | FWD-3, FWD-7 (acc 3, 7) | **absent** | OPEN | no contract exists (PRD names it open); bucket versioning Andrew-locked OFF (GLOBGRPH s.0 #5) so the pointer is the one mutable object; pointer atomicity is CG-s-11's question only if the service reads it over the network -- otherwise it is an S3 read-after-write question the deliverable answers with a control | `0.7.0_AE_CloudOps` | laptop | CG-s-2 -> a delta artifact exists | artifact-first, pointer-last EXERCISED: a pointer never names an artifact that is not fully present (a planted partial write is refused/ignored by the reader -- the control that can fail); the manifest carries vintage in plain words (FWD-3's source) |
| CG-s-4 | S4 small always-on service on ECS cluster `opal-globgrph` | FWD-1, FWD-5, FWD-7 (acc 1, 5, 7) | **absent** | OPEN | RE-MEASURED at this seat on the aws corpus (a different instrument from the CRO brief): cluster `opal-globgrph` `active_services: 2`; 7 task definitions (nessie:5, trino:6, derive-runner:6, comp-learns:1, cse:1, fedobs:1, resource-summaries:1); DB built 2026-09-03T00:36:15Z. Cluster resource `nessie.tf:14` (215 lines @`d8d0d7d26d`), service pattern `:196` | `0.7.0_AE_CloudOps` | laptop | CG-s-3 -> pointer exists; CG-s-11 -> reachability verdict; CG-s-12 -> IAM delta named | the service answers one Cypher query inside the VPC against the CURRENT artifact and swaps on a pointer advance (a second artifact published, the answer's vintage changes -- the control) |
| CG-s-5 | S5 gateway traversal registered via `IntegrationSpec` | FWD-1, FWD-5 (acc 1, 5) | **absent** | OPEN | `registry.py` 67 @`2781aac326` (2 live integrations, `ENABLED_INTEGRATIONS` CTO-arch-gated `:34`); `opal-gateway-role` (10 statements, DESIRED) holds NOTHING on the globgrph bucket and no ECS/service-discovery action -- so either the proxy needs no new grant (pure HTTP inside the VPC) or S12 names the delta; the deliverable says which | `0.7.0_AE_CloudOps` | laptop | CG-s-4 -> the service answers; CG-s-13 -> the AuthKind named | a seat that is not the gateway host issues one traversal through the gateway and gets the service's answer; the framework file diff is the 5-step checklist only (the bound that can fail) |
| CG-s-6 | S6 `.tools/comp-kuzu` becomes a thin client printing vintage in plain words | FWD-3, FWD-6 (acc 3, 6) | measured | OPEN | 30 lines @`dffbee781c`; target today `kuzu_cli.py:30` -> `_canonical.CANONICAL_DB_PATH` (189 @`173dd335f4`); plain-words rendering is an open input resolved by this cell's deliverable, not decided here | `0.8.0_AE_CloudComp` | laptop | CG-s-4 -> the service answers (a client needs a server) | the client has NO refresh flag, mode or prompt (FWD-6: enumerate the CLI surface and show the absence); every answer line carries the age in plain words (FWD-3); the local DB path is not read |
| CG-s-7 | S7 operator status read: repoint `comp-graph status` at the pointer's manifest | FWD-8 (acc 8) | **absent** | OPEN | `graph_status_cli.py:214-232` (360 @`ee49b14381`) reports "kuzu_db 81d / stitch_graph 38d" -- the wrong artifacts (brief F6, attributed) | `0.8.0_AE_CloudComp` | laptop | CG-s-3 -> a manifest exists to read | R4: a PULL read; "did it refresh last night" prints yes/no + a time; a NIGHT THAT DID NOT RUN reads differently -- planted by pointing at a stale manifest (the control). NO alarm, SNS, checker or monitor (CLAUDE.md s.5) |
| CG-s-8 | S8 RETIREMENT of the local copy: `kuzu_nessie_db`, `kuzu_cli.py`, the `_canonical.py` rebuild/labeled-stale seam + `kuzu_nessie_db.fallback.jsonl` sink | FWD-7 (acc 7) | measured | **OPEN -- PARTLY DONE BY A SIBLING** (s.0: the two wrappers are ABSENT @`dffbee781c`, COMPEFFICACY cell t-22 of `NFRA_COMPEFFICACY`; not this project's act, not re-done here) | `kuzu_cli.py` 189 + `_canonical.py` 746 @`173dd335f4`; the seam re-located by content | `0.8.0_AE_CloudComp` | laptop | CG-s-4 + CG-s-6 -> DONE; **CG-x-5 -> a fresh machine has been ANSWERED (a reader exists before the builder is removed)** | R7 read as a bar, not a precondition: S8 STARTS when a reader exists and CLOSES when CG-x-7 passes (two machines, same answer, local copy off). Retiring earlier breaks the estate's only graph; never retiring is the shadow pipeline |
| CG-s-9 | S9 `kuzu_nessie_load.py` node/edge key asymmetry, aligned at the port | acc 9 (R10) | measured | OPEN | 417 lines @`e445642c5f`; substrate card @`5da9e7fffc` QUALIFIED, defect at `:150` vs `:184` (re-locate by content) | `0.7.0_AE_CloudOps` | laptop | CG-s-2 -> same task order or the one after; never after CG-s-3 | a control at the two sites that FAILS on the pre-port bytes and PASSES on the ported ones (R10: the port is the moment) |
| CG-s-10 | S10 the FULL-FALLBACK DURATION of the projection (KUZUSPLIT P0-INSTRUMENT) | -- (sizes CG-s-2) | **unmeasured** | OPEN -- **ROUND 1** | four figures from three sources for two operations; CRO refused to reconcile them; this file inherits the refusal | `0.7.0_AE_CloudOps` | laptop (the measurement may RUN in AWS; the seat is laptop) | -- | a measured duration with its instrument, environment, input size and denominator; a second run for variance; NEVER one of the four existing figures |
| CG-s-11 | S11 gateway -> serving-service network reachability (VPC / subnet / SG) | -- (shapes CG-s-4/5) | **absent** | OPEN -- **ROUND 1** | 4 globgrph SGs LIVE + DECLARED (derive-runner, incremental-updater, nessie, trino); the gateway is `i-07dccb1615503ac99` t4g.nano; no SG or route between them is declared anywhere this seat read | `0.7.0_AE_CloudOps` | laptop | -- | a reachability verdict from BOTH ends (a probe from the gateway host to a listener in the cluster's subnet, and the SG/route rules read), with the negative control (a port that must NOT be reachable) |
| CG-s-12 | S12 IAM for the NEW worker and the NEW serving service | -- (feeds CG-s-1/4/5) | **unmeasured** | OPEN -- **ROUND 1** | DESIRED: `opal-globgrph-incremental-updater` (sqs 4 actions + s3 5 actions on `opal-313476888478-globgrph`), `nessie-task` (dynamodb 12 + s3 5), `nessie-execution` (ecr + logs), `opal-gateway-role` (10 statements, none on globgrph) -- 15 globgrph-family roles enumerated of 180 parsed. **comp-iam cannot answer "is this denied?"** -- silence is not "allowed" | `0.7.0_AE_CloudOps` | laptop | -- | `comp-iam refresh-census` FIRST (24h TTL; 664h stale measured 2026-09-01), then the APPLIED read; the delta (new role / new statements) written as DESIRED Terraform with `comp-iam gaps` after, and simulate on ONE ARN per call (a batched multi-ARN simulate poisons verdicts) |
| CG-s-13 | S13 which existing `AuthKind` an agent traversal fits | -- (precondition of CG-s-5) | **unmeasured** | OPEN -- **ROUND 1** | brief Part V item 4; `registry.py` + the integrations standard | `0.7.0_AE_CloudOps` | laptop | -- | the AuthKind named with the framework line that defines it, and the one it does NOT fit stated with why |

### 1b. The closing pass -- `CG-x-n` IS the EXERCISED bar of FWD-n (spine v2.3 close; cut at L6 like any other cell, each a task order whose spec IS the act)

| cell | outcome | DONE WHEN (verbatim from the PRD ENDPOINT) | the act the task order specifies | status now | lane | placement | depends_on -> released by | closes on |
|---|---|---|---|---|---|---|---|---|
| CG-x-1 | FWD-1 | EXERCISED -- someone who has never run a graph tool has asked and been answered | a named seat with no graph history asks one wiring question through the client; the answer, its time-to-answer and the absence of any refresh step recorded | OPEN | `0.8.0_AE_CloudComp` | laptop | CG-s-5, CG-s-6 -> DONE | the record shows the asker, the question, the answer, the vintage line, and that no build ran (process table / log negative control) |
| CG-x-2 | FWD-2 | EXERCISED -- the schedule has fired on its own at least once and the next morning's answers carry that night's date | one unattended night: the marker write fired the worker, the pointer advanced, a morning query carries that night's vintage | OPEN | `0.7.0_AE_CloudOps` | laptop | CG-s-3 -> DONE; one calendar night | the pointer's manifest vintage is later than the previous evening's AND no seat invoked anything (the invocation log read, denominator printed) |
| CG-x-4 | FWD-4 | EXERCISED -- a full cycle has passed with nobody enforcing the ceiling by hand and no answer served older than it | over one full refresh cycle, every served answer's age is read against the schedule's ceiling | OPEN | `0.7.0_AE_CloudOps` | laptop | CG-x-2 -> DONE | the oldest age served in the cycle <= the ceiling, from the service's own log; the control: a planted stale artifact is NOT served |
| CG-x-5 | FWD-5 | EXERCISED -- a machine that has never held the graph has asked and been answered | a machine with no `kuzu_nessie_db` on disk (site Z, or a fresh checkout with the path absent, proven by an `ls`) asks and is answered on the first try | OPEN | `0.8.0_AE_CloudComp` | laptop (the READER may be site Z; the seat is laptop) | CG-s-5, CG-s-6 -> DONE | the absence of the local DB proven before the ask, then the answer; same answer as a laptop seat for the same question |
| CG-x-7 | FWD-7 | EXERCISED -- two people on different machines have asked the same question at the same moment and received the same answer, after the local copy was switched off | after CG-s-8's switch-off, two seats on two machines ask the same question inside one minute | OPEN | `0.8.0_AE_CloudComp` | laptop + site Z as the second reader | CG-s-8 -> switched off | identical answers with identical vintage lines; no local DB on either machine (proven); this closes CG-s-8 |
| CG-x-8 | FWD-8 | EXERCISED -- the answer has been read on a real morning, and a night that did not run reads differently from one that did | the status read taken on a real morning after CG-x-2's night, and once against a night known not to have run | OPEN | `0.8.0_AE_CloudComp` | laptop | CG-s-7, CG-x-2 -> DONE | both readings recorded; they differ; nothing was rerun to obtain either (the invocation log as negative control) |

---

## 2. The arc as an ordering, and the ROUNDS L6 cuts from it

```
  ROUND 1   MEASURE FIRST -- none is build, each decides a shape       CG-s-10 (its own seat instance: it runs a full load)
            (STAGE 0 of the flat decomposition, unchanged)             CG-s-11 · CG-s-12 · CG-s-13 (reads; one seat instance, or three)
        |   released by: four DONE proofs. CG-s-11 can INVALIDATE CG-s-5's shape; CG-s-10 SIZES CG-s-2.
        v
  ROUND 2   STAGE 1: the projection becomes a CONSUMER of the marker   CG-s-1 -> CG-s-2 (+ CG-s-9 in the same port) -> CG-s-3
        |   released by: an artifact + pointer exist on S3 (observed on S3, never on a dispatch)
        v
  ROUND 3   STAGE 2: the serving plane + the reach                     CG-s-4 -> CG-s-5 -> CG-s-6
        |   released by: a non-host seat gets an answer through the gateway; the client has no refresh choice
        v
  ROUND 4   STAGE 3 + THE CLOSING PASS                                 CG-s-7 · CG-x-1 · CG-x-5 · CG-x-2 (one night) -> CG-x-4 (one cycle) · CG-x-8
                                                                       then CG-s-8 (switch-off) -> CG-x-7 (closes S8)   S8 IS LAST (R7)
        |
        v
  THE CLOSE  every cell DONE with a VALID proof -> ledger/COMPLETION_REPORT.round<N>.json (this lane) -> COMPLETION_GRADES (1.0.0_SA_CTO~A) -> CLOSED (R6, mechanical)
```

⛔ **THE TWO ORDERINGS THAT ARE RULINGS, NOT PREFERENCES:** (R7) CG-s-8 after a working CG-s-4 + CG-s-6 and a fresh-machine read (CG-x-5), closing on CG-x-7 -- retiring early breaks the estate's only graph, never retiring is the shadow pipeline; (R10) CG-s-9 inside the port, never after CG-s-3 -- a ported defect is a defect shipped twice.
⭐ **AND ROUND 1 SITS FIRST DELIBERATELY:** CG-s-11's verdict can change CG-s-5's whole shape and CG-s-10's number decides CG-s-2's runtime. Building STAGE 1 before those two are measured is guessing with a task order.
**Rounds are L6's grain, not a promise:** a round's task orders are tight, single-cell where a cell is a build, and every round ends at L8-L10 (`3.0.0_SA_CVO~A` rows, dispositions, the one slug) before the next round's dispatches -- looping in order is the point.

---

## 3. `<preflight>` -- the L5 battery: the mandatory core + the admitted lenses this seat ran, at their vintages

```
<preflight>
comp-schedule: RUN -- the compiled gate view at 2026-09-03 ~05:5xZ: GATES ARMED 19 across 5 carriers (C1 sentinel denominator 21 -> 5;
  C2 deploy-ledger 2 -> 2; C3 moratoria 12 -> 12; C4 scope-guard 20 SEMI-DECIDABLE -> 0; C5 project-blocking 336 NOT-DECIDABLE -> 0);
  138 prose `blocking` fields NEEDS-READ (listed, never counted); 0 armed gates name NFRA_CLDGRPH, globgrph, kuzu, opal-gateway,
  IntegrationSpec, comp-graph or KUZUSPLIT (case-insensitive over the 130-line view; no match = a MEASURED zero, denominator above).
comp-iam: RUN -- DESIRED plane (Terraform) only: 180 roles parsed / 187 services / 1,074 operations / 306 gaps estate-wide; the
  globgrph family = 15 roles + opal-gateway-role enumerated by name; the three roles CG-s-12 starts from read in full (statements
  6 / 2 / 1 / 10). BLIND ON THIS SUBJECT BY CONSTRUCTION: the worker and the service are NEW principals, so the DESIRED plane holds
  nothing for them yet; and comp-iam cannot answer "is this denied?" -- the APPLIED read (refresh-census, then simulate one ARN per
  call) is CG-s-12's own act at L7, not this seat's. Two NOTE lines about module-namespaced orchestrator/scheduler labels: out of scope.
comp-adversary: RUN -- `comp-adversary compose` on THIS file after writing; rc, the cited-commit and cited-path counts and the
  declared exclusions are recorded in the commit message and in s.5 below. The tool is CLEARED @bbba0db0e9; this run is from a seat that
  did not fix it.
comp-trigger: RUN -- 140 events-rules + 18 schedules scanned, us-east-1, 7-day fired window: 'kuzu' NO MATCH; 'globgrph' 5 matches
  (cloudtrail-mgmt -> SQS opal-globgrph-incremental-events FIRED 17,983x; derive-runner-nightly cron(0 2); comp-learns-producer-nightly
  cron(0 4); fedobs-producer-nightly cron(30 4); cse-producer-nightly scheduler). BLIND on S3-notification triggers BY ITS OWN
  DISCLOSURE, and R5's trigger IS one -- so CG-s-1 is UNRESOLVED by this instrument and is resolved by the two reads below.
comp-find --corpus aws 'opal-globgrph' --budget 300 --all: RUN -- 70 hits across 2,100 aws nodes; DB built 2026-09-03T00:36:15Z (age
  5.3 h at read); WITHIN BUDGET 11.55 s (CE-G-5 @173dd335f4 has landed: the default-budget hazard on this corpus is gone).
  ECS_CLUSTER 1 (active_services 2) · ECS_TASK_DEFINITION 7 · SQS_QUEUE 2 (incremental-events + dlq, DECLARED) · SECURITY_GROUP 4
  (DECLARED) · LAMBDA 1 · EVENT_RULE 4 · SCHEDULE 1 · IAM_ROLE 15 · IAM_POLICY 28 · LOG_GROUP 5 · DYNAMODB_TABLE 2 (both
  LIVE-no-DECLARED: opal-globgrph-nessie-_objs / -_refs -- NFRA_GLOBGRPH's drift, carried with its owner, not this project's).
comp-find 'aws_s3_bucket_notification' infra/aws/terraform/globgrph: RUN -- 0 hits across 32 files (10 BINARY unsearched): CG-s-1's
  `absent` holds on the DESIRED plane too. Estate-wide the resource type appears in 6+ other TF trees (served-guard, opal-assets x3,
  portal-notifications, shared-infra): the pattern is proven, the instance is absent.
comp-find '_branch_head' infra/aws/terraform/globgrph infra/aws/globgrph: RUN -- 32 hits across 130 files (64 ephemeral-floor + 15
  binary unsearched); MARKER_KEY DEFINED in 5 files (R5's five writers, named in CG-s-1).
comp-read --enumerate 'CELL_ID_RE' .tools/proof-of-spec-check.py: RUN -- 5 hits, the regex at :377; all 19 ids in s.1 tested against it
  before writing: 19 MATCH; the manifest's bare S<n> tokens: 0 MATCH (by design).
comp-read --enumerate (pins): RUN -- every s.7 surface re-read at HEAD c2c2127f31 (s.0): 12 surfaces, 2 ABSENT, 3 moved, 7 unchanged.
comp-blast · comp-dataflow · comp-pipescript · comp-denytest: NOT RUN AT L5 -- no code is changed by this file; each is a per-cell
  preflight at L6 for the task order whose cell touches its subject (comp-blast on _canonical.py / kuzu_cli.py for CG-s-6/8;
  comp-denytest only when CG-s-12 proposes an IAM change -- no population before that).
</preflight>
```

---

## 4. What this decomposition REFUSES to assume

- **CG-s-10 is unmeasured and no figure is picked.** The CRO's refusal to reconcile four figures from three sources is inherited; the cell measures.
- **CG-s-4's cluster state is now MEASURED at this seat on the aws corpus, not carried** -- the CRO brief's number and this read AGREE on a different instrument (2 services); the task definitions and SGs are this seat's addition.
- **CG-s-1's `absent` is now a two-plane zero** (DESIRED: 0 of 32 TF files; LIVE: the only queues are item2b's) plus one instrument's declared blindness -- three reads, two of them discriminating.
- **CG-s-8 is not re-done for what a sibling already retired.** The wrappers are gone @`dffbee781c` under `NFRA_COMPEFFICACY`; this file names what remains and nothing more.
- **CE-G-5's freshness layer is not silently ported or silently dropped.** CG-s-2's bound makes the port SAY which; a silent choice is a surprise row.
- **No IAM change is proposed here**, so `comp-denytest` has no population -- a truthful non-application at the subject grain, not a skipped lens.
- **The closing-pass cells are not padding.** Each is an act the PRD's own DONE WHEN line names; without a cell the COMPLETION_REPORT would read UNCOVERED on six of eight outcomes by its own schema, and a report that reads UNCOVERED on a spent decomposition is the report doing its job -- this file prefers to give it a cell to count.
- **The site-Z reader in CG-x-5 / CG-x-7 is a READER, not a placement change.** Every cell's placement is laptop (R12; the row's `fabric`); a second machine reading the served graph is what FWD-5 and FWD-7 are FOR.

---

## 5. Holds, and whose they are; what L6 cuts first

1. **The push hold** -- `0.0.0_AB_MSTR`'s window on Andrew's word (04:13Z "stop pushing until i say so"); every commit of this run is LOCAL until his push word. Not a cell; the push-state field of every DONE test reads LOCAL until then, and says so.
2. **The L4 frame 93149** (`[PRD LANDED] NFRA_CLDGRPH v0.4 @25c66d3358`) reads OFFER-EXHAUSTED on the ledger and never reached this lane's filesystem inbox; the notifier re-offers on its own clock and this seat READ-acks it from its Msg-ID when it lands. **The pickup proceeded on the MEASURED artifact** (the PRD at its tree path, header + endpoint + manifest conforming, committed) per `/canonical-flow` Step 2 -- a notification is the handoff mechanism, the artifact is the handoff.
3. **No seat of class `0.7.0_AE_CloudOps` is live** at write (12 live agents read at ~05:5xZ: `0.8.0_AE_CloudComp` base HOLD after CE-G-5, `~A` idle after CE-T-2, no `0.7.0`). ROUND 1 is CloudOps-lane work: seating is this lane's act (`/mstr-spawn`, pre-flight 1pt/1a/1b/1c/1d clean, an Andrew-launched seat presumptively RESERVED).
4. **`comp-adversary compose` on this file -- RUN, rc 0** at read-vintage HEAD @`07288006e5` 2026-09-03T06:11:07Z (`--no-packet`; stage 4 disabled by the caller and disclosed as such): pins found 22 commits / 6 repo paths / 8 `file:line` cites / 16 tool mentions; cited commits **22 attempted / 22 VERIFIED / 0 UNVERIFIABLE**; cited paths **6 attempted / 6 stable / 0 flagged**; uncited siblings 264 (cap 25 declared); 3 hex runs not parsed as pins by design (the gateway instance id, the account id, and the bare HEAD `c2c2127f31` in s.0 -- a real pin the parser misses when written without `@`, named here so the validator does not read it as a digest); comp-state drift excerpt 400 commits / 2,802 records; 5 declared exclusions (v1 contract). Declaration kept in the author's scratchpad; the numbers are the record.
5. **THE L6 `<issued_to>` FORK -- one card at Andrew, from both CTO terminals (93205 base, 93210 ~A), NOT a halt on L5.** Andrew at the `3.0.0_SA_CVO~A` terminal ~06:05Z (record @`7da3befc20`, verbatim *"not acceptable, CLDGRPH needs to be run entirely by this fabric CVO~A COO~A CTO~A"*) read against his 05:1xZ word (@`8e134cc126`, *"in addition to any agents needed for dispatched TOs"*) and gate (i) of `.tools/to-pipeline-gate.py:96,166` (a `_SA_` `<issued_to>` on a new tree TO is REFUSED; installed on his word @`716a9bc7ce` call 3). Surfaced by `3.0.0_SA_CVO~A` (93194), not adjudicated by any seat. The CTO's REC on the card = reading (a): the ~A lanes own every exec limb, no base seat touches this project, L7 workers are Tier-2 seats this lane SPAWNS FRESH for the run (nothing shared with `NFRA_COMPEFFICACY`), gate (i) stands. **RULED (a) BY ANDREW ~06:1xZ, at BOTH lane terminals before this file was committed:** at the `3.0.0_SA_CVO~A` terminal, verbatim *"yeah obviously COO~A needs to /mstr-spawn the workers for 6-7"* (record @`858fc08951`); at the `1.0.0_SA_CTO~A` terminal, the same ruling in his words (record `org/tier1_exec/1.0.0_SA_CTO~A/deliverables/ANDREW_DIRECT_20260903_061xZ_RULING_A_COOA_SPAWNS_TIER2_WORKERS_AT_L6.md`). **Consequence at this seat:** L7 workers are NEW Tier-2 lane letters this lane spawns for this run (`/mstr-spawn` is a COO function at base or lane); no `_SA_` serial is ever an `<issued_to>`; gate (i) never fires; nobody edits it. The card is answered; this hold is DISCHARGED by his word and kept here as the record of the fork.

**WHEN L6 OPENS (the next act at this seat, this session): ROUND 1.** Two task orders, both to the CloudOps lane, both `verify` cells, GO paired at cut: **TO-CG-V-1** = `CG-s-10` alone (it runs a full load and owns a seat for the duration), **TO-CG-V-2** = `CG-s-11` + `CG-s-12` + `CG-s-13` (three reads, one seat instance, each criterion its own control). Each carries `<decomp_ref>` at this file's commit, `<owned_cells>` naming the `CG-` ids, a measured `<preflight>` (comp-schedule RUN, comp-iam RUN or DECLARED-NOT-APPLICABLE with the reason on its own line, comp-adversary compose rc 0 with its numbers), `<proof_of_spec>` with criterion ids minted at cut, `<issued_to>` one Tier-2 serial, through `.tools/to-pipeline-gate.py` + `to-proof-of-spec-check.sh`. Surprises are ROWS at `../surprise-channel/investigations/INVESTIGATION_v1.md` (lane ANY), read by `3.0.0_SA_CVO~A` at L8; `dep_stage: EXECUTING` is the row owner's flip on the first task order.
