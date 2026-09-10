# IRPT_BCKEND -- L5 decomposition -- round 1 -- v0.1.1

**v0.1.1** (2026-09-10 ~21:2xZ, `2.0.0_SA_COO~B`, amended BEFORE the cut, in the issuance commit) -- s.8 item 1: the live vendor arm is an express qualification in the face and an L10 read, never a mechanical criterion on the order. Cells, ids and edges unchanged.

```json
{
 "project": "IRPT_BCKEND",
 "directive": "D9",
 "fabric": "laptop",
 "round": 1,
 "decomp_version": "v0.1.1",
 "prd_ref": "org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md@62301f71e0",
 "prd_version": "v0.4",
 "brief_ref": "docs/briefs/investor-reporting-ir-bk-brief-20260910.md@2acf23d8fd",
 "endpoint_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_BCKEND_20260910.md",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-7", "FWD-8", "FWD-9", "FWD-10", "FWD-11"],
 "owns_grade": ["FWD-2", "FWD-7", "FWD-9", "FWD-10"],
 "cells": 19,
 "cell_id_shape": "IB-s-<n> (PRD candidate B<n>); IB-sb-3 (the split of B3)",
 "worker_serial": "0.9.0_WK_IRPT_BCKEND~<slot>",
 "cut_head": "8ace3a2596",
 "counterpart_decomp": "org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md"
}
```

**One carrier.** The PRD's CELL CANDIDATES row (`serves`, brief sections, contracts, paths, fixtures, acceptance clause draft) is the authoritative text of each cell and is inlined VERBATIM at L6 from the pin above. This document adds the ORDER, the ROOTS, the SEATING, the FENCE, the BATTERY and five L5 findings; it restates no PRD row and invents no surface. The PRD's eighteen candidates map to nineteen cells: B3 is split at its own grain (a LIBRARY every handler consumes, and a REPLAY BATTERY that can only run once every route exists).

---

## 1. THE RECTANGLE -- nineteen cells

| cell | PRD | serves (own / contrib) | write surface (new home) | verb | tf root | deploys | live arm |
|---|---|---|---|---|---|---|---|
| `IB-s-18` | B18 | all | `infra/aws/lambda/investor-reporting/_contracts/` (11 JSON Schemas + fixture pairs), `infra/aws/lambda/investor-reporting/README.md` + `PATH_MANIFEST.json` (every read/write path with its owner), `infra/aws/terraform/investor-reporting/README.md` (the nine roots, state keys), `data/assets/scripts/gold/investor_reporting/README.md`, the Part V dependency register | scaffold | none | no | no |
| `IB-s-17` | B17 | FWD-10 own, FWD-2 own, FWD-9 | `infra/aws/terraform/investor-reporting/core/` (KMS key; bucket `opal-data-ycharts` SSE-KMS with `firms/{firm_id}/...` prefixes + `quarantine/`; DynamoDB tables for requests, revisions, jobs/leases, outbox, checkpoints; SQS queues + DLQs carrying ids only); `infra/aws/lambda/investor-reporting/_keys/` (the key grammar library) | build+deploy | core | yes | no |
| `IB-s-5` | B5 | FWD-10 own, FWD-9 own, FWD-2 | `infra/aws/terraform/investor-reporting/core/firm_destination_policy.json` (versioned, owner-stamped), per-firm role/prefix IAM conditions in `core/`; `infra/aws/lambda/investor-reporting/_gate/` (the ingestion gate: sender evidence to firm, refuse-outside-policy) | build+deploy | core | yes | no |
| `IB-s-1` | B1 | FWD-1 contrib, FWD-7 own | `data/assets/scripts/gold/investor_reporting/directory_runner.py` (per-firm `DirectoryEntry` set to the FIRM's bucket, section 9 finding 1); `infra/aws/lambda/investor-reporting/directory/` (search + resolve handler); `infra/aws/terraform/investor-reporting/directory/` | build+deploy | directory | yes | no |
| `IB-s-2` | B2 | FWD-1 contrib, FWD-2 own, FWD-11 contrib | `infra/aws/lambda/investor-reporting/_scope/` (`ResolvedScope` resolver from the `X-User-*` headers the edge validator injects; the permitted account set + fingerprint) | build | directory | no | no |
| `IB-s-3` | B3 (library half) | FWD-2 own | `infra/aws/lambda/investor-reporting/_authz/` (reauthorize-before-serve on every handler, cache/idempotency key grammar per II.3, revoked-grant-vs-warm-cache, client names never keys) + unit fixtures | build | directory | no | no |
| `IB-s-4` | B4 | FWD-7 own | `infra/aws/terraform/investor-reporting/directory/` (the refresh schedule; `expiry/fallback` config); `infra/aws/lambda/investor-reporting/directory/refresh.py`; the controlled-clock harness under `deliverables/` | build+deploy | directory | yes | no |
| `IB-s-12` | B12 | FWD-5 contrib | `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (three partner joins, taxonomy, denominators, `HoldingsSnapshot` to the FIRM's bucket) | build+deploy | directory (its schedule) | yes | no |
| `IB-s-8` | B8 | FWD-4 contrib | `infra/aws/ec2/investor-reporting-ycharts/` (the runner: `getSession`/`probeSession`/`acquireSession`/`persistSession`/`withAuthenticatedPage`, lease/fencing, NO OTP branch); `infra/aws/terraform/investor-reporting/ycharts/` (separate host + role, applied STOPPED) | build+deploy | ycharts | yes | **yes** -- YCharts login |
| `IB-s-6` | B6 | FWD-9 own | `infra/aws/lambda/investor-reporting/intake/` (Graph delta poller, attachment persistence, checkpoint, lease, outbox, idempotency); `infra/aws/terraform/investor-reporting/intake/` (the poller Lambda; scheduler `cron(0/15 8-23 * * ? *)` America/New_York applied `state = DISABLED`) | build+deploy | intake | yes | **yes** -- the mailbox read |
| `IB-s-7` | B7 | FWD-9 own, FWD-4 contrib | `infra/aws/lambda/investor-reporting/intake/parse.py` (deterministic CSV/XLSX parse, findings, the correction state) | build | intake | no | no |
| `IB-s-9` | B9 | FWD-4 contrib | `infra/aws/lambda/investor-reporting/ycharts/generate/` (the seven-step recipe as an Opal async job; SUBMITTING before the side effect; owned-identity reconcile); `infra/aws/terraform/investor-reporting/ycharts/` (job dispatch) | build+deploy | ycharts | yes | **yes** -- YCharts calls |
| `IB-s-10` | B10 | FWD-4 contrib, FWD-3 contrib | `infra/aws/lambda/investor-reporting/ycharts/extract/` (typed sections with units, dates, page/coordinates; certification against the paired PDF) | build | ycharts | no | no (the real PDFs are a named gap) |
| `IB-s-11` | B11 | FWD-3 contrib | `infra/aws/lambda/investor-reporting/performance/` (Black Diamond 49F and COT separately; Orion INF; the normalizer to `PerformanceReport`); `infra/aws/terraform/investor-reporting/performance/` | build+deploy | performance | yes | **yes** -- BD / Orion calls |
| `IB-s-13` | B13 | FWD-8 contrib | `infra/aws/lambda/investor-reporting/narrative/` (events on the verified daily cumulative TWR; dated topic retrieval from `opal-news-trending-daily`, `opal-news-articles`, `opal-data-news-v2`; evidence-cited prose, contemporaneity stated); `infra/aws/terraform/investor-reporting/narrative/` | build+deploy | narrative | yes | no (Opal-owned sources) |
| `IB-s-14` | B14 | FWD-8 contrib, FWD-3 contrib, FWD-4 contrib | `infra/aws/lambda/investor-reporting/export/` (asset verification, `ExportBundle` freeze, the render worker executing the counterpart's `RenderPackage`, `ExportReceipt`, the reauthorized download route); `infra/aws/terraform/investor-reporting/export/` | build+deploy | export | yes | no |
| `IB-s-16` | B16 | FWD-10 own (the proof arms), FWD-7, FWD-6 contrib | `infra/aws/lambda/investor-reporting/ops/` (`StatusEnvelope` producer, correlation ids, source-completion manifests, the recovery runbook); `infra/aws/terraform/investor-reporting/ops/`; the seven-arm recovery battery under `deliverables/` | build+deploy | ops | yes | no |
| `IB-s-15` | B15 | FWD-11 contrib, FWD-2 own | `infra/aws/terraform/investor-reporting/api/` (`/api/scoped/investor-reporting/...` routes on API `7k3ed8px20` under authorizer `naqxlm`, integrations to the handlers by data source); the Opal principal class + permitted-firm catalogue in `_scope/`; **the CloudFront behavior** `/api/scoped/investor-reporting/*` -> `APIGateway-portal` with `viewer-request: auth-validator-edge` in `infra/aws/terraform/portal-auth/cloudfront-distribution.tf` (section 9 finding 2) | build+deploy | api (+ portal-auth, one behavior) | yes | no |
| `IB-sb-3` | B3 (battery half) | FWD-2 own | the end-to-end REPLAY BATTERY under `deliverables/`: swapped firm / advisor / account / relationship / report / PDF identifiers across EVERY deployed route incl. the PDF download, a revoked grant against a warm cache, an Opal principal vs a firm advisor on the same requests | verify | none | no | no |

**Outcome coverage, run not asserted: 10 of 10 `FWD-n` in the PRD header have >= 1 cell.** FWD-1: s-1 s-2 ; FWD-2: s-2 s-3 sb-3 s-15 s-17 ; FWD-3: s-10 s-11 s-14 ; FWD-4: s-7 s-8 s-9 s-10 s-14 ; FWD-5: s-12 ; FWD-7: s-1 s-4 s-16 ; FWD-8: s-13 s-14 ; FWD-9: s-5 s-6 s-7 s-17 ; FWD-10: s-5 s-16 s-17 ; FWD-11: s-2 s-15. Candidate coverage: 18 of 18 PRD candidates map to exactly one cell (B3 to two, at its own grain).

**Placement axis:** `laptop`, every cell (D9 whole to laptop, Andrew-direct 2026-09-10 ~18:5xZ).

**Cell vocabulary (Rule 24, a NOT-EVALUATED value present so non-evaluation is never a verdict):** `status` = DONE (graded) / IN-FLIGHT (landed, grade pending) / OPEN (not started) / HELD (blocked on a named decision, owner stated) / NOT-EVALUATED (this document did not measure it and says so). (i) MECE over {a cell's state between the cut and the close}; (ii) one grain, the cell; (iii) one axis, progress toward a grade; (iv) a CVO grade moves `status`, a ruling moves the PRD and never this file. At v0.1 every cell reads OPEN. The order is the truth; this column is bumped at a round close and is one round behind between them.

---

## 2. WHAT L5 ADDS PER CELL (the PRD row carries everything else)

- **`IB-s-18` is the ONE shared dependency beneath every other cell** (Rule 22): the eleven contract schemas are generated from the PRD's CONTRACTS table field sets so that this project's producers and the counterpart's typed client (its `F1` cell reads the same table at the same pin) validate against one carrier. The path/owner manifest and the dependency register are files every later cell APPENDS to. It deploys nothing and must be fast; three slots wait on it.
- **`IB-s-17` creates every tenant-scoped resource once**, in one root with one state, so no two worktrees ever apply the same state. Key grammar: tenant + account-set fingerprint + source/schema/config revisions + operation parameters; client names never keys.
- **`IB-s-5` names the `FirmDestinationPolicy` OWNER: `0.7.0_AE_CloudOps`.** Mechanism, not name: the policy binds its firm cardinality to `data/firm_registry.json` (that file's own law) with a completeness test that FAILS LOUD when the registry's enabled client firms and the policy's firms differ, so a new firm is a policy edit that cannot be forgotten, and CLAUDE.md s.5's "a new firm name is a GATE EDIT" has a carrier. Sender evidence: the original sender through the forwarding arrangement, never display From; unknown/spoofed/contradictory origin -> `quarantine/`, never a firm; an Opal-origin mail with no target-firm rule stays unresolved.
- **`IB-s-6`'s reuse source is UNRESOLVED (PRD v0.3).** One candidate exists in the estate and is handed to the cell to INSPECT, not to reuse: `infra/aws/ec2/opal-gateway/app/config.py` names `Mail.Read` (the gateway that reads Opal mail today). The cell records what permission model it uses and whether a certificate/app registration restricted to `opalbloomberg@opalinvest.com` exists; the effective grant is VERIFIED, never assumed from a filter (section 9 finding 3). Proof runs the poller against RECORDED Graph responses through a transport stub (delta, `nextLink`, `deltaLink`, Retry-After, restart mid-attachment); the live read is the qualified arm.
- **`IB-s-8` applies the host STOPPED.** The Playwright runner with the Kimi DOM fallback is proved on a local browser against the captured HAR flows; starting the host and logging in is the qualified arm.
- **`IB-s-9` proves the seven-step chain against a HAR-replay transport** (the captured request/response pairs, the 34-key vs 33-key body shapes, the 201 with `report_url`/`zip_url`), with `SUBMITTING` persisted before the side effect and the owned-identity reconcile driven through a duplicated event. The upload multipart field names are NOT captured and are not invented: the observed browser upload is the mechanism and the pure-HTTP upload stays a named gap.
- **`IB-s-10` cannot be certified against real PDFs because none exist** (PDF bodies absent from the packet). The cell builds the extractor and the certification harness against a SYNTHETIC PDF generated from the comparison field census, with a DIFFERENCE control (one changed number fails certification); the real-PDF arm is UNCOMPUTABLE-BY-CONSTRUCTION naming the specimens' arrival. The gap stays named on FWD-4 and FWD-8.
- **`IB-s-11` proves against the captured probe evidence** (`probe_performance.py` offline; the nine September 10 outcomes; the 119,975-byte Orion fixture shape) with the unit arm the endpoint binds: Orion summary DECIMAL vs daily PERCENTAGE, and a normalizer that treats them as one unit must FAIL the arm. It takes a `ResolvedScope` FIXTURE as input, which is why it does not wait on `IB-s-2`.
- **`IB-s-13` is the new seam the endpoint said L5 names: the topic/sentiment retrieval adapter is THIS project's** (`infra/aws/lambda/investor-reporting/narrative/`), reading the news producers' tables and bucket and changing nothing in them; ownership of the producers stays where it is.
- **`IB-s-14` executes a `RenderPackage` CONFORMING FIXTURE until the counterpart's package is terminal**; the swap to the real package is a configuration value, and the grade that reads both halves is FWD-8's at L9. The download route reauthorizes on every request even when the artifact exists.
- **`IB-s-16` is late by construction:** its seven recovery arms drive the deployed jobs of `IB-s-6`, `IB-s-9`, `IB-s-12` and `IB-s-14`, each shown to touch no second firm.
- **`IB-s-15` includes the CloudFront behavior** (section 9 finding 2). Routes on the portal API alone would leave `/api/scoped/investor-reporting/*` falling to behavior 0, the SPA default, which is a 200 from the wrong origin, not a 404. The cell's apply of `portal-auth` is a served-surface act under NEVER-2 with its own ledger entry; the existing 28 behaviors are untouched.
- **`IB-sb-3` is the exercised proof of FWD-2** and can only run once `IB-s-15` and `IB-s-16` are terminal, which is why it is a separate cell and the last one.
- **`IB-s-1` and `IB-s-12` are gold runners under CLAUDE.md rule 13** (`.tools/safe-deploy.sh`, the DS commit-to-QA-deploy lane). Whether a worker serial passes that guard is UNMEASURED (section 9 finding 4). Both cells run ad hoc for QA to a QA prefix first; the production schedule is the deploy act.

---

## 3. THE CHAIN READ -- computed from the edge set, not chosen

```
  edges (37, keyed to OBSERVED completion of the source cell):
    IB-s-18 -> IB-s-17   IB-s-18 -> IB-s-1    IB-s-18 -> IB-s-8    IB-s-18 -> IB-s-11
    IB-s-17 -> IB-s-5    IB-s-17 -> IB-s-6    IB-s-17 -> IB-s-8    IB-s-17 -> IB-s-9
    IB-s-17 -> IB-s-14   IB-s-17 -> IB-s-16
    IB-s-1  -> IB-s-2    IB-s-1  -> IB-s-4    IB-s-1  -> IB-s-12   IB-s-1  -> IB-s-15
    IB-s-2  -> IB-s-3    IB-s-2  -> IB-s-15   IB-s-3  -> IB-s-15
    IB-s-5  -> IB-s-6    IB-s-5  -> IB-s-16
    IB-s-6  -> IB-s-7    IB-s-6  -> IB-s-16
    IB-s-7  -> IB-s-9    IB-s-8  -> IB-s-9    IB-s-9  -> IB-s-10   IB-s-9  -> IB-s-16
    IB-s-10 -> IB-s-14   IB-s-10 -> IB-s-15
    IB-s-11 -> IB-s-13   IB-s-11 -> IB-s-15   IB-s-13 -> IB-s-14
    IB-s-12 -> IB-s-15   IB-s-12 -> IB-s-16
    IB-s-14 -> IB-s-15   IB-s-14 -> IB-s-16
    IB-s-16 -> IB-s-15   IB-s-15 -> IB-sb-3   IB-s-16 -> IB-sb-3

  heads releasable at spawn (no incoming edge) = 1 :  IB-s-18
  leaves (no outgoing edge)                     = 2 :  IB-s-4  IB-sb-3
  M, maximal paths through the edges            = 52
  edge-connected components                     = 1
  longest dependency depth (cells)              = 11 :
    IB-s-18 -> IB-s-17 -> IB-s-5 -> IB-s-6 -> IB-s-7 -> IB-s-9 -> IB-s-10 -> IB-s-14 -> IB-s-16 -> IB-s-15 -> IB-sb-3
  acyclic: checked (a cycle would have refused this section)
```

**THE BINDING FACTS.** (a) Every cell hangs off `IB-s-18` and fourteen hang off `IB-s-17`; those two are the shared dependencies Rule 22 warns about, so each carries its own criteria and is finished BEFORE anything that consumes it is handed out. (b) The DAG is one wide at the head, six wide at wave 3, and one wide for its last four waves (the export-ops-routes-battery pole). A fan-out chosen against the cell count spawns workers that idle on the head and on the tail; the useful width is the number of POLES a queue can drain in dependency order without waiting on another queue more than once, and that is four (section 5).

---

## 4. THE ROUND FENCE -- the dependency waves inside ONE issuance

| wave | cells | the fence's reason |
|---|---|---|
| 1 | `IB-s-18` | the foundation: schemas, homes, manifest, roots; deploys nothing |
| 2 | `IB-s-17` `IB-s-1` `IB-s-11` | the storage root; the directory runner + handler; the performance adapters (fixture scope) |
| 3 | `IB-s-2` `IB-s-4` `IB-s-5` `IB-s-8` `IB-s-12` `IB-s-13` | scope resolver; refresh harness; destination policy + gate; the runner host; holdings; narrative |
| 4 | `IB-s-3` `IB-s-6` | the enforcement library; the mailbox poller (on the policy and the storage) |
| 5 | `IB-s-7` | the parser (on the persisted-attachment record) |
| 6 | `IB-s-9` | generation (on the parser, the runner, the storage) |
| 7 | `IB-s-10` | extraction + certification |
| 8 | `IB-s-14` | export (on narrative, extraction, storage) |
| 9 | `IB-s-16` | ops + the seven recovery arms over the deployed jobs |
| 10 | `IB-s-15` | routes + Opal principal + the CloudFront behavior (on every handler) |
| 11 | `IB-sb-3` | the replay battery across every route |

The fence is a plan, not a commitment: no cell is deferred to a later round; a wave is the dependency order inside a queue and the order in which the COO hands cells across queues at the drain.

---

## 5. SEATING AND THE FAN-OUT L6 WILL CARRY

**All 19 cells are worker cells** (`0.9.0_WK_IRPT_BCKEND~n`, Opus at high effort by the worker agent type). Under RULING 1 (Andrew 2026-09-04 ~04:58Z) a worker's write surface is exactly the `<paths>` its order names; every infrastructure path above resolves to lane `CLOUD_OPS_OR_ETL` at HEAD and is reached only through the order. Live-plane reads and applies carry the launching seat's credentials; the invocation and its output are recorded verbatim in the proof instance.

```
fanout: 4 of 52 chains, cap 8, reason: four poles drain in dependency order, one per Terraform-state
        family so no two worktrees ever apply one state -- slot 1 core-and-ops (IB-s-18, IB-s-17,
        IB-s-5, IB-s-16, IB-sb-3: the foundation and storage first because every cell hangs off
        them, ops and the battery last because they exercise everything), slot 2 directory-and-
        entitlement (IB-s-1, IB-s-2, IB-s-3, IB-s-4, IB-s-12, IB-s-15), slot 3 intake-and-ycharts
        (IB-s-8, IB-s-6, IB-s-7, IB-s-9, IB-s-10), slot 4 performance-narrative-export (IB-s-11,
        IB-s-13, IB-s-14); the 52 maximal paths all pass through IB-s-18 and 43 through IB-s-17,
        so a fifth slot would idle on slot 1's first two merges; the cross-slot waits are hand-offs
        the COO sequences at the drain.
```

| slot | queue (dependency order) | cross-slot waits the COO sequences at the drain |
|---|---|---|
| `~1` | `IB-s-18` -> `IB-s-17` -> `IB-s-5` -> `IB-s-16` -> `IB-sb-3` | `IB-s-16` after `IB-s-6`, `IB-s-9`, `IB-s-12`, `IB-s-14` merge; `IB-sb-3` after `IB-s-15` merges |
| `~2` | `IB-s-1` -> `IB-s-2` -> `IB-s-3` -> `IB-s-4` -> `IB-s-12` -> `IB-s-15` | `IB-s-1` after `IB-s-18`; `IB-s-15` after `IB-s-10`, `IB-s-11`, `IB-s-14`, `IB-s-16` merge |
| `~3` | `IB-s-8` -> `IB-s-6` -> `IB-s-7` -> `IB-s-9` -> `IB-s-10` | `IB-s-8` after `IB-s-17`; `IB-s-6` after `IB-s-5` |
| `~4` | `IB-s-11` -> `IB-s-13` -> `IB-s-14` | `IB-s-11` after `IB-s-18`; `IB-s-14` after `IB-s-10` and `IB-s-17` |

Each hand-off is a fresh worktree from `HEAD` at hand-off time (`git worktree add -b wk-irpt_bckend-1-<n> /c/tmp/wk-irpt-1-<n> HEAD`), so a slot's later order sees every merge that landed before it. `.tools/terraform.exe` is gitignored and absent in a fresh worktree: the issuer provisions it into every slot's worktree at spawn (the ETFS_GUARDRAIL precedent), and every `.tf` file is committed LF.

---

## 6. TERRAFORM ROOTS, STATE AND THE DEPLOY DISCIPLINE

| root under `infra/aws/terraform/investor-reporting/` | state key (`opal-313476888478-terraform-state`) | cells | what it holds |
|---|---|---|---|
| `core/` | `investor-reporting/core/tfstate` | `IB-s-17` `IB-s-5` | KMS, bucket + prefixes + quarantine, DynamoDB, SQS, per-firm IAM conditions, the policy document |
| `directory/` | `investor-reporting/directory/tfstate` | `IB-s-1` `IB-s-4` `IB-s-12` | directory handler Lambda + role, the refresh and holdings schedules |
| `intake/` | `investor-reporting/intake/tfstate` | `IB-s-6` | the poller Lambda + role, the scheduler (DISABLED) |
| `ycharts/` | `investor-reporting/ycharts/tfstate` | `IB-s-8` `IB-s-9` | the runner host (STOPPED) + role + SSM document, the generation job |
| `performance/` | `investor-reporting/performance/tfstate` | `IB-s-11` | adapter Lambda + role |
| `narrative/` | `investor-reporting/narrative/tfstate` | `IB-s-13` | narrative Lambda + role (read-only on the news tables and bucket) |
| `export/` | `investor-reporting/export/tfstate` | `IB-s-14` | export worker + role, protected artifact prefix policy |
| `ops/` | `investor-reporting/ops/tfstate` | `IB-s-16` | status Lambda + role |
| `api/` | `investor-reporting/api/tfstate` | `IB-s-15` | routes on `7k3ed8px20` with authorizer `naqxlm`; the CloudFront behavior lives in `portal-auth`, applied by the same cell under its own ledger entry |

Lambdas: the `infra/aws/terraform/modules/yang-lambda` module, artifacts at `opal-313476888478-lambda-artifacts` under `investor-reporting/<function>.zip` built and uploaded by `infra/aws/lambda/ci/build-and-upload.sh`, every function registered in `infra/aws/lambda/ci/lambda-source-map.json`. Function names `irpt-<root>-<role>`; one role per root, least privilege, per-firm prefix conditions from `IB-s-5`. Every apply is `.tools/safe-apply.sh` under a change-management entry opened at the start and closed at completion, with the sentinel committed; served bytes verified against the built input (`CodeSha256` vs the zip), never by filename; `aws lambda update-function-code` never.

---

## 7. THE BATTERY -- run at L5, with each instrument's blindness stated

| instrument | disposition | result | what it does NOT cover |
|---|---|---|---|
| the chain read | RUN | 37 edges, 1 head, 2 leaves, M=52, 1 component, depth 11, acyclic (section 3) | it trusts this document's edges; a MISSING edge shows as false width; the edges were derived from the PRD's contract producer/consumer columns and the roots, not from code that does not exist yet |
| surface re-pin | RUN | 73 of 76 PRD paths (27 reuse rows expanded, fixtures, briefs) PRESENT at worktree HEAD `d0e72ccd56`; 3 of 3 NEW homes ABSENT, as they must be | existence only, not content; `comp-read` cannot tell a WRONG file |
| outcome + candidate coverage | RUN | 10 of 10 `FWD-n` served; 18 of 18 candidates mapped (section 1) | a served outcome is not a REALIZED one; four cells carry a qualified live arm (section 8) |
| `comp-schedule --budget 150` | RUN (20:2xZ) | WITHIN BUDGET 5 of 5 carriers; C1=92 C2=6 C3=12 C4=20 C5=335; 25 gates ARMED; 0 name IRPT, investor-reporting or any surface above; the moratoria that bind here are G-20 (no monitor), G-23 (cross-firm), G-24 (vendor egress) | a ledger of GATES, not prose obligations; 137 prose `blocking` fields are a reading list it does not grade |
| `comp-iam stats` + `roles` | RUN | 191 roles parsed, 188 services, 307 gaps estate-wide; the roles the cells REUSE AS PATTERNS exist on the DESIRED plane: `partners-lambda-role`, `bd-49f-auto-login-role`, `YChartsSessionCaptureLambdaRole`, `opal-assets-mdpf-portal-publisher-role`; ZERO investor-reporting roles exist | DESIRED plane only; the new roles cannot be graded until their `.tf` exists, so `comp-iam service <fn>` at Phase 1 and `comp-iam gaps` at Phase 2 are inlined on every deploying order |
| `comp-routes behaviors` | RUN | 28 CloudFront behaviors; every `/api/scoped/*` path is `APIGateway-portal` under `auth-validator-edge`; **NO behavior matches `/api/scoped/investor-reporting/*` at HEAD**, so it would fall to behavior 0 (`/*` -> the SPA) -- section 9 finding 2 | DESIRED plane (parsed Terraform + committed router source); a deployed drift reads identical |
| `comp-blast` on `auth-validator-edge/index.mjs` | RUN, BLIND | SUBJECT_ABSENT_FROM_CORPUS over 27,662 graph nodes (vintage 2026-09-10T12:24Z) | the graph carries no node for the edge validator; its consumers were read from `comp-routes` (28 behaviors) instead |
| `comp-read` on the validator, the scoped routes and the session-capture Lambda | RUN | the validator injects `X-User-*` headers and downstream Lambdas never parse JWTs; 14 `/api/scoped/advisor-intelligence/*` routes declared with CUSTOM auth; the session-capture Lambda is browser login + cookie capture and establishes no mail permission (PRD v0.3 is right) | shape and qualifiers, not behaviour; the Opal-principal class is NOT visible in the validator's qualifiers and `IB-s-2`/`IB-s-15` trace it at Phase 1 |
| live plane (`.tools/aws`, read-only) | RUN (20:1xZ) | bucket `opal-data-ycharts` ABSENT (HeadBucket 404); 0 of 37 DynamoDB tables carry an investor-reporting name; `opal-news-trending-daily` and `opal-news-articles` PRESENT; Secrets `ycharts/login/credentials`, `ycharts/session/current`, `ycharts/credentials`, `astn/kimi/api-key` PRESENT, 4 of 4 the brief names (of 10 secrets total) | names only; no value read; a secret's PRESENCE says nothing about its AWSCURRENT version, which `IB-s-8` reads at Phase 1 |
| `comp-adversary compose` on this document | RUN after it was written | see the commit message for the composed declaration's counts | it validates CITATIONS in this file, never the decomposition's correctness; DECLARED-NOT-APPLICABLE on the orders at the cut (the assignee's instrument at report time) |
| lane read (`owned-paths-validate.py --check-agent`, HEAD bytes) | RUN | this lane PERMIT on `decompositions/`, `project.json`, `org/projects/IRPT_BCKEND.json`; every `infra/aws/**` and `data/assets/scripts/gold/**` path is lane `CLOUD_OPS_OR_ETL`, a worker serial REFUSED at HEAD (no non-terminal order yet) -- the expected state before L6 | reads the DECLARED grant; the first spawn is the exercise |
| worker-executability | JUDGED, not exercised | 19 of 19 cells are a worker's; hazards: the gold-runner deploy lane (finding 4), an EC2 create (`IB-s-8`), a CloudFront apply (`IB-s-15`), four qualified live arms (section 8) | the first spawn is the test; a capability a worker lacks is a row, not a tool request |

---

## 8. BOUNDS THAT BIND EVERY ORDER, inlined at L6 where they touch a cell

1. **NO LIVE VENDOR CALL** (endpoint, verbatim: *"NO LIVE VENDOR CALL is authorized by this document -- availability is not authorization; a live YCharts, Black Diamond or Orion call needs Andrew's explicit per-use word"*; CLAUDE.md G-24). Four cells carry a live arm (`IB-s-6` the mailbox read, `IB-s-8` the YCharts login, `IB-s-9` the YCharts calls, `IB-s-11` the BD/Orion calls). Each proves its MECHANISM against recorded fixtures through a transport stub with a difference control, and NAMES the live arm in its face as an express qualification: *fires on Andrew's per-use word, recorded under `deliverables/`, and is read by the CTO at L10 against the exercised artifact*. It is deliberately NOT a mechanical criterion on the order (v0.1.1): the worker flips an order complete only when every mechanical criterion passes by output, so a live arm cut as a criterion would hold the order open on an act the worker is forbidden to take. This is the EXPRESS QUALIFICATION Rule 27 requires, on the outcome and with his word, and it is not a wait: the organic case is the negative arm, and a NOT_EVALUATED grade on that arm at the first close is the honest state (the ETFS_GUARDRAIL precedent).
2. **NO MONITOR, ALARM, SNS OR SES SEND** (G-20). The intake scheduler is the product's poller, not a monitor, and is applied `DISABLED`; enabling it is part of the qualified arm. Nothing in this project notifies anyone.
3. **CROSS-FIRM, both shapes** (G-23): per-firm prefixes + IAM conditions in the shared `opal-data-ycharts` bucket; the FIRM's own bucket for directory and holdings PLATINUM (finding 1); the `FirmDestinationPolicy` with a named owner; the firm fixed from the sender's domain at ingestion and immutable after; Global GRANTED to an Opal principal, never to a firm one; no new all-firm financial aggregate.
4. **Deploys** (NEVER-2, NEVER-9): `safe-apply.sh` only; ledger entry + committed sentinel; `CodeSha256` vs the zip; one root per slot; `aws lambda update-function-code` never. Every deploying order grants `org/critical_paths/change_management/` AND `org/critical_paths/.open_deploys/<slug>.json`.
5. **Andrew's four fixed constraints are not build choices:** the BDAPI-with-Kimi runner STYLE with NO OTP branch; the firm from the sender's domain at ingestion gated to enumerated destinations; the multitenant `api/scoped/` layout; terminated clients STAY VISIBLE under entitlement. Plus the endpoint's: units are part of meaning; unsupported positions never silently removed; no PUT of global YCharts preferences; no vendor call in render or preview; missing history is an answer; the narrative states contemporaneity and never causes; model targets never masquerade as observed holdings.
6. **No credential in any artifact, log, fixture or commit.** Secrets are read by name at runtime; a recorded fixture is scrubbed before it is committed; signed URL parameters are never logged.
7. **No served output is touched.** The 28 existing CloudFront behaviors, the 14 existing scoped routes and every existing bucket, table and Lambda are read, never edited; `IB-s-15` ADDS one behavior and its routes.
8. **The spec is FROZEN mid-round.** A cell that looks wrong to a worker is a ROW at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `IRPT_BCKEND-W<n>-S<k>`, never an edit; a seat's row carries no `W<n>`.
9. **Every invocation a criterion names terminates** under the worker's `timeout 120`; a whole-corpus sweep is never a criterion.

---

## 9. FIVE L5 FINDINGS, carried as seat rows at the issuance for the CTO's L10 read

1. **The PLATINUM destination for the directory and the holdings snapshot is re-homed from `opal-data-portal-v2` to the FIRM's bucket.** `comp-routes behaviors` reads `opal-data-portal-v2` as the origin of `/json-tiered/*` (behavior 19: direct, NO auth Lambda) and `/api/general/json-tiered/*` (behavior 18: `public-data-router`). A client directory carries names and account identities; a holdings snapshot carries values. Publishing either into a bucket with an unauthenticated CloudFront path is the cross-firm and PII exposure the estate's rule exists to refuse, whatever key it lands under. The existing firm-scoped AdvisorIntelligence data is served from the firm's bucket through `shared-advisor-router` (behaviors 2-4, 16, 27), which is the precedent. So `IB-s-1` and `IB-s-12` write to `<firm bucket per FIRM_BUCKET_MAP>/investor-reporting/...` and are served ONLY through this project's scoped handlers after `ResolvedScope`, never through a public tier. The PRD's SURFACE MANIFEST row naming `opal-data-portal-v2` is overturned by this finding; the row is carried, not edited.
2. **A new scoped prefix needs a CloudFront behavior, not only API routes.** No behavior matches `/api/scoped/investor-reporting/*` at HEAD; the default `/*` behavior serves the SPA. `IB-s-15` therefore carries one behavior in `infra/aws/terraform/portal-auth/cloudfront-distribution.tf` with `viewer-request: auth-validator-edge`, applied under its own ledger entry as a served-surface act.
3. **`IB-s-6`'s Graph reuse source is UNRESOLVED and one inspect candidate exists**: `infra/aws/ec2/opal-gateway/app/config.py` names `Mail.Read`. The cell inspects and records; nothing is assumed.
4. **Gold-runner deploys by a worker serial are UNMEASURED.** `IB-s-1` and `IB-s-12` land under `data/assets/scripts/gold/investor_reporting/`, a rule-13 DS surface whose S3 code deploy runs through `.tools/safe-deploy.sh`. A refusal there is a BLOCKING row on the deploying criterion and rides the drain-end read; the ad-hoc QA run is unaffected.
5. **`IB-s-10` has no real PDF to certify against.** The synthetic-PDF harness with a difference control is the mechanism proof; the real-PDF arm is `UNCOMPUTABLE-BY-CONSTRUCTION` naming the specimens' arrival, on FWD-4 and FWD-8 both.

---

## 10. CROSS-PROJECT SEAMS (no cell is jointly owned)

| seam | this project | the counterpart (its PRD candidate) | graded inside |
|---|---|---|---|
| eleven contracts | `IB-s-18` generates the schemas from the PRD CONTRACTS table @`62301f71e0` | F1 builds the typed client and consumer fixtures from the same table at the same pin | each owned outcome; a shape change needs matching producer and consumer fixtures |
| `RenderPackage` | `IB-s-14` executes it (a conforming fixture until the real one is terminal) | F9 produces it | FWD-8, FWD-3, FWD-4 |
| correction state | `IB-s-7` produces `needs-correction` findings | F6 renders and returns corrections | FWD-9, FWD-4 |
| `StatusEnvelope` | `IB-s-16` produces the nine states | the counterpart's status panel renders them | FWD-6 (the counterpart's), FWD-10 |
| Global | `IB-s-2`/`IB-s-15` the entitlement class and the permitted-firm catalogue | F10 the view and the dropdown | FWD-11 |
| the live routes | `IB-s-15` | the counterpart's typed client switches from its fixture adapter by one configuration value | FWD-1, 2, 11 |

---

## 11. WHAT THIS DECOMPOSITION DOES NOT DECIDE

- **The `<paths>` block of any order.** L6's, per order; under RULING 1 it IS the grant.
- **The Graph authentication implementation** (finding 3): `IB-s-6` inspects and records; the mechanism is chosen inside the cell within the bound "verified grant, one mailbox".
- **Table and queue shapes beyond the key grammar.** `IB-s-17`'s, within II.3.
- **Whether a worker serial passes `safe-deploy.sh`** (finding 4). The first attempt is the measurement.
- **When the counterpart's `RenderPackage` lands.** `IB-s-14` proves against a conforming fixture; the swap is graded at L9 inside FWD-8.
- **Any number the brief proposes** (the 15-minute poll, session-recovery bounds, retries): measured then declared by the cell that carries it, never ratified here.
- **The FWD-10 `FirmDestinationPolicy` OWNER's successor.** `0.7.0_AE_CloudOps` is named; a re-owner is a PRD addendum, not a decomposition edit.
