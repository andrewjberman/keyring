# IRPT_YCDGEN -- DECOMPOSITION, ROUND 6 (THREAD, in-house generation): the Opal Overview, no pricing, end to end

```json
{
 "project": "IRPT_YCDGEN",
 "round": 6,
 "prd_ref": "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (v0.5 @e6a801f7f0; RATIFIED; prd-signoff ADMITTED)",
 "prd_version": "v0.5",
 "analysis_ref": "none: first round of the v0.2+ in-house endpoint; the rectangle is PRD section 2's hops",
 "endpoint_outcomes": ["FWD-1"],
 "round_scope": ["FWD-1", "FWD-15 (read half only)", "FWD-9 (trace in run.json)", "FWD-6 (three clocks in run.json)"],
 "author": "2.0.0_SA_COO~Y",
 "cells": 5,
 "chains": 2,
 "join_cells": 0,
 "frozen": false,
 "revision": "0.1-draft",
 "cell_ids": ["YCD-b-6", "YCD-a-6", "YCD-c-6", "YCD-e-6", "YCD-d-6"]
}
```

**Status: DRAFT, not frozen.** Frozen at the L6 cut. Held on one external edge: S20 (the Opal form of `AnalysisReport`, the CTO's
act, `CTO_DESIGN_ANALYSISREPORT_OPAL_PRODUCER_FORM_20261005.md`, "NOT LANDED"). Cells YCD-c-6, YCD-e-6 and YCD-d-6 read it.

## 1. Surveyed surfaces (measured by an Explore read, 2026-10-05 ~21:0xZ; paths are repo-relative)

Base `infra/aws/lambda/investor-reporting/`.
- Producer: `ycharts/research/layout_overview.py` (`compute_all` 651, `build` 901, `render` 953, `finish` 989), `held_data.py`, `runner.py`
  (`read_holdings` 443 reads accepted holdings: DynamoDB `irpt-requests` -> `ARTIFACT#` row -> S3 blob with sha256 check).
- Classification client: `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` `ETFClassifier` (`get_classification`,
  `classify_holdings`). `layout_overview.py` today reads the table by its own `_scan_classifications` (702), not through the client.
- Served worker: `ycharts/generate/resident_worker.py` `ResidentAssembly.execute` (480), selection seam between `store.claim()` (522)
  and the `ResidentGenerationWorker(...).run()` build (529). Principal: `record["owner"]["principal_id"]`. No allow list exists.
- Contract: `_contracts/AnalysisReport.schema.json` v1 (vendor_artifact, read_back required); consumers `ops/owned_report.py`,
  `ycharts/generate/publisher.py`, `portal/src/pages/InvestorReporting/contracts/{wire/AnalysisReport.ts,adapt.ts}`.
- Lanes: `ycharts/research/**` and `ops/**` are `IRPT_COMPLETION_Y`; `generate/{resident_worker,publisher,...}.py` are
  `IRPT_Y_ACCESS_INTEGRATION_P`; `_contracts/**` is `IRPT_COMPLETION_P`; the portal is `POD_DE_ANY`; the classification client is
  `MDPF_SECCLASS_FAST_M_AE` (read only here).

## 2. Contracts of the round

- **R1 Classification through the client.** Every security's printed name, asset class and sub asset class is read through
  `ETFClassifier`. A holding with no row prints as not yet classified (C-CLASSIFY). The scan path is removed from the Overview path.
- **R2 C-V1.** Return, risk, benchmark and risk-free elements print `NOT_AVAILABLE` with reason `NOT_IN_THIS_VERSION`. No price read.
  Weights are the accepted dollar amounts renormalized over the holdings with an amount.
- **R3 Opal producer entry.** One new module `research/opal_producer.py`: `produce(request_ref, firm, store) -> run_record`. It reads
  the accepted holdings (`runner.read_holdings`' reader, imported, not copied), calls the layout's `build`/`render`, writes the
  artifact and `run.json` v2 (per-element `method`, `inputs`, `coverage`, `status`, `reason`; each input's as-of date; clocks
  `reading`, `computing`, `rendering` in seconds) under C-STORE's two registered addresses. Nothing is fetched from outside.
- **R4 Read side.** `ops/owned_report.py` and the status path accept `provider: OPAL_ENGINE` documents (S20's form) and keep
  rejecting a v1 document missing `vendor_artifact`; an absent member is never read as a pass.
- **R5 Page.** The Analysis tab's wire type and adapter accept the Opal form; sections render from `status/method/coverage`.
- **R6 Switch (C-SWITCH).** In `execute`, a server-side allow list of principal ids (starts with Andrew's sign-in only) chooses
  the Opal producer; every other principal takes the YCharts path unchanged; no client flag selects.

## 3. THE CELLS (cut by write set; each owns files no other cell writes)

| cell | hop | writes | reads | depends on |
|---|---|---|---|---|
| `YCD-b-6` | 4 Classify, 6 Compute | `ycharts/research/layout_overview.py`, `ycharts/research/tests/test_layout_overview.py` | classification client | none |
| `YCD-a-6` | 3 Read, 7 Render+record | `ycharts/research/opal_producer.py` (new), `ycharts/research/tests/test_opal_producer.py` (new) | `runner.py`, `layout_overview.py` | b-6 merged |
| `YCD-c-6` | 8 Open (server) | `ops/owned_report.py`, `ops/tests/test_owned_report.py` | S20 schema | a-6 merged; **S20 landed** |
| `YCD-e-6` | 8 Open (page) | `portal/src/pages/InvestorReporting/contracts/wire/AnalysisReport.ts`, `contracts/adapt.ts`, and their tests | S20 schema, c-6's shape | c-6 merged; **S20 landed** |
| `YCD-d-6` | 2 Select | `ycharts/generate/resident_worker.py`, `ycharts/generate/tests/test_resident_worker.py` | `opal_producer.py` | a-6 merged; **S20 landed**; IRPT_BCKEND release path with a never-widen half |

Hookups for the issuer at the merge: none known. The deploy of `d-6` and the portal DEV landing of `e-6` are the issuer's acts, not a cell's.

## 4. Chains and fan-out

Edges: b-6 -> a-6 -> d-6, and b-6 -> a-6 -> c-6 -> e-6. Two maximal paths, sharing b-6 and a-6: M = 2. Workers: `~1` = b-6, a-6, d-6;
`~2` = c-6, e-6 (starts when a-6 merges). Cap 8; N = 2, reason: two dependency-independent tails after a-6.

## 5. Four-postulate record (CLAUDE.md rule 24)

- MECE over the declared domain "PRD section 2 hops 2-8 less hop 5": the hops 2, 3, 4, 6, 7, 8 each map to one cell above; hop 3 and
  hop 7 share `a-6` (one module); hop 8 splits server/page by write set. Hop 1 is unchanged and is not a cell. Hop 5 (Data) has no
  first-version content under C-V1 beyond what hop 4 reads, so it owns no cell. Denominator: 8 hops, 6 served by cells, 1 unchanged, 1 empty by C-V1.
- Same grain: each cell is one module's write set. Intent coherence: each cell has one outcome (classify+compute; produce; read; page; select).
- State coherence: a cell's merge moves its files only; the allow list's content is `d-6`'s sole state; no cell moves served output
  (the issuer's deploy does).

## 6. Battery

- `comp-schedule`: DECLARED-NOT-APPLICABLE -- thread round, no scheduled job in this round (C-SCHEDULE binds the later refresh).
- `comp-adversary`: DECLARED-NOT-APPLICABLE -- thread round; the lens runs on the enrichment round that touches its surface.
- `comp-iam`: RUN-AT-CELL -- the producer runs on the resident host (not a Lambda), so the Lambda grant tool's neighborhood does not
  contain its role; blindness stated. The question (can that role read `etf-classifications` and write the two firm-store
  addresses) is carried as a mechanical criterion of `a-6`, proved by one real read and one real write at the drain.

## 7. Issuer's close act

One real Overview for the reference Cottonwood portfolio through the Opal producer, signed in as Andrew, with `run.json` read back
and the report opened on the page (FWD-1).

## 8. Not in round 6

The scheduled refresh and the mart (FWD-8, FWD-13, FWD-14); price-based content (C-V1); Comparison and Multi (FWD-4); classification
of unknown securities (FWD-15's write half); the typo and swap checks (FWD-16); the side-by-side and the release (FWD-7, FWD-11).
