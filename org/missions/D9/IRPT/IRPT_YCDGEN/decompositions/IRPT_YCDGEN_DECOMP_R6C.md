# IRPT_YCDGEN -- DECOMPOSITION, ROUND 6 ADDENDUM C: the installer wiring and the whole thread proved with fakes

```json
{
 "project": "IRPT_YCDGEN",
 "round": 6,
 "addendum": "C",
 "prd_ref": "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (v0.6; ENDPOINT unchanged since v0.5 @e6a801f7f0)",
 "prd_version": "v0.6",
 "endpoint_outcomes": ["FWD-1"],
 "round_scope": ["FWD-1"],
 "author": "2.0.0_SA_COO~Y",
 "cells": 1,
 "chains": 1,
 "join_cells": 1,
 "frozen": true,
 "revision": "1.0",
 "parent_decomp": "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6.md",
 "cell_ids": ["YCD-k-6"]
}
```

**Why an addendum.** With every hop cell of R6, R6A and R6B merged, two worker rows are left that no cell owns and that make the thread unrunnable on the resident host:

- **IRPT_YCDGEN-W1-S11** (d-6's worker, measured): `ResidentAssembly` now takes an optional `opal_stores(principal, record)` keyword and
  `reports/resident_installed.py:269` does not pass it, so a listed principal's job raises `ValueError OPAL_STORES_REQUIRED` and is never served.
  Release order: wire the installer first, then put Andrew's principal id in the allow list.
- **IRPT_YCDGEN-W3-S15** (i-6's worker, measured): `opal_producer.produce` retains the PDF only when its caller injects `stores["artifacts"]`, and the
  returned `artifact_ref` has to reach the checkpoint; nothing injects it or hands the ref on.

No test yet drives one request through the whole merged path (select, produce, persist, READY, read). The seams between six independently built cells
are exactly where the thread will fail, so this cell is the JOIN: it wires the installer and proves the path with fakes before the issuer's one real run.

## Cell

| cell | hop | writes | reads | depends on |
|---|---|---|---|---|
| `YCD-k-6` | 2-8 (join) | `reports/resident_installed.py`, `reports/tests/test_resident_installed.py`, `ycharts/generate/resident_worker.py`, `ycharts/generate/tests/test_resident_worker.py`, `ycharts/generate/tests/test_opal_thread_integration.py` (new) (base `infra/aws/lambda/investor-reporting/`) | every merged round-6 cell | all of R6, R6A, R6B (merged) |

**Contract R11 (the installer supplies the Opal stores; the whole path runs).** (1) `reports/resident_installed.py` passes `opal_stores` to
`ResidentAssembly`. The factory builds, from the installed bindings and only for a principal on the allow list, the stores `opal_producer.produce`
takes: the accepted-holdings reader (the one `runner.read_holdings` implements), the classifier (`ETFClassifier` over the `etf-classifications` table),
the firm-store put for the run record, the reporting repository's `artifacts` (retained PDF), and the clock. A principal off the list builds none of them
(no client is constructed). (2) The `artifact_ref` `produce` returns reaches the publisher's checkpoint, so the job reaches READY with a retained PDF.
(3) One test drives `ResidentAssembly.execute` for a listed principal with fake stores through select, produce, persist and READY, then reads the report
back through `OwnedAnalysisReader.sections`; and the same request from an unlisted principal takes the YCharts path. Nothing live: fakes only.
The allow list keeps its inert placeholder; the issuer sets the real principal id at release.

## Edges and fan-out

Single cell after all others merged: M = 1. fanout: 1 of 1 chain, cap 8, reason: the join cell, serial after the round's other cells.

## Four-postulate record (Rule 24)

MECE: the thread's hops 2-8 each have an owner cell in R6/R6A/R6B; the joins between them (the installer's supply of stores, the hand-off of the retained ref)
had none and are this cell's. Same grain: one write set of five files. Intent: one outcome (the merged path runs end to end on fakes). State: the YCharts
path and the placeholder allow list are not moved.

## Battery

comp-schedule, comp-iam and comp-adversary DECLARED-NOT-APPLICABLE (thread round, no grant change). The resident host role's real access (read
`etf-classifications`; write the firm store and the retained families) is proved at the issuer's close run.
