# IRPT_YCDGEN -- DECOMPOSITION, ROUND 6 ADDENDUM B: the retained artifacts and the Analysis tab's wording

```json
{
 "project": "IRPT_YCDGEN",
 "round": 6,
 "addendum": "B",
 "prd_ref": "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (v0.6; ENDPOINT unchanged since v0.5 @e6a801f7f0)",
 "prd_version": "v0.6",
 "endpoint_outcomes": ["FWD-1"],
 "round_scope": ["FWD-1"],
 "author": "2.0.0_SA_COO~Y",
 "cells": 2,
 "chains": 2,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "parent_decomp": "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6.md",
 "cell_ids": ["YCD-i-6", "YCD-j-6"]
}
```

**Why an addendum.** Two more measured gaps in the live thread surfaced at the g-6 and e-6 drains. The parent (R6) and R6A are not edited; this file is the issuer's
disposition of the rows, and the CTO is told at the drain-end read.

- **YCD-i-6** disposes of worker rows IRPT_YCDGEN-W3-S8 and W3-S11 (measured by the g-6 worker): the Opal report PDF family `OPAL_REPORT_PDF` is named by the merged
  publisher but registered nowhere (the reporting policy `irpt-x10-v1` holds 13 families, none of them it), the a-6 producer writes the PDF straight to S3 and never
  retains it as an artifact, and a full OPAL_ENGINE document can exceed the job store's 32 KiB checkpoint (`WORKER_CHECKPOINT_SIZE`), with no spill on the Opal path.
- **YCD-j-6** disposes of worker row IRPT_YCDGEN-W2-S14 (measured by the e-6 worker): `NativeSections.tsx` and the typed contracts still print 'Certified sections',
  'Extraction validation:' and 'Vendor attribution:' for an Opal report and show neither method nor coverage.
- Worker row W3-S9 (`resident_worker.py:513-519` reopens a READY job through `provenance.extraction_evidence_ref`, which an Opal report lacks) is d-6's file and is
  carried by an amendment to the d-6 order, not by a cell here.

## Cells

| cell | hop | writes | reads | depends on |
|---|---|---|---|---|
| `YCD-i-6` | 7 Persist (artifacts) | `infra/logic/registry/reporting_policies.json`, `lib/tests/test_irpt_destination.py`, `ycharts/research/opal_producer.py` + test, `ycharts/generate/publisher.py`, `ycharts/generate/publication_worker.py` + tests (base `infra/aws/lambda/investor-reporting/`) | g-6 (merged) | none open |
| `YCD-j-6` | 8 Open (page wording) | `portal/src/pages/InvestorReporting/tabs/analysis/NativeSections.tsx`, `contracts/index.ts`, `contracts/wire/index.ts`, `contracts/wire/consumed.ts`, `contracts/wire/responses.ts`, `api/endpoints/investor-reporting.ts`, `portal/scripts/native-sections-opal-exercise.mjs` (new) | e-6's portal commit (unlanded) | e-6 done (portal branch) |

Contracts R9 (i-6) and R10 (j-6) are inlined in their orders. Write sets are disjoint from each other and from d-6 (`resident_worker.py` and its test).

## Edges and fan-out

i-6 and j-6 are independent (a Python/registry chain and a portal chain); d-6 (round 6) runs beside i-6 on disjoint files and waits on neither. M = 2.
fanout: 2 of 2 chains, cap 8, reason: a registry-and-persist chain and a portal chain.

## Four-postulate record (Rule 24)

MECE: R6A's denominator (8 hops, persist moved to its own cell) is extended: the persist hop's artifacts (family, retention, checkpoint) and the page hop's wording each
get a cell; the 11 red portal tests are a pre-existing baseline (measured on unedited DEV: 40 pass, 11 fail), owned by nobody in this round. Same grain: one write set
each. Intent: i-6 one outcome (the Opal artifacts are retained and the checkpoint is small); j-6 one (the tab's words are the Opal form's). State: the YCharts path and the v1 tab are unmoved.

## Battery

comp-schedule, comp-iam and comp-adversary DECLARED-NOT-APPLICABLE (thread round, no grant change); the resident host's role (write of the retained artifacts, read of
`etf-classifications`) is proved at the close run.
