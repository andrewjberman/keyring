# IRPT_YCDGEN -- DECOMPOSITION, ROUND 6 ADDENDUM A: the persist hop for the Opal form

```json
{
 "project": "IRPT_YCDGEN",
 "round": 6,
 "addendum": "A",
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
 "cell_ids": ["YCD-g-6", "YCD-h-6"]
}
```

**Why an addendum.** The round-6 decomposition (revision 1.0, frozen) covers hops 2, 3, 4, 6, 7 and 8, and no cell owns the persist step between
the producer's output and the READY state the server read needs. The a-6 worker filed IRPT_YCDGEN-W1-S6 (measured): `reports/resident_installed.py`
(`REPORT_SCHEMAS`, line 47) binds the resident validator to the v1 schema; `ycharts/generate/publisher.py` (107) and
`ycharts/generate/publication_worker.py` (47) accept only the vendor key set `{request_ref, vendor_artifact, effective_inputs, release}` and a
`pdf_ref` of family `ORIGINAL_VENDOR_PDF`. The parent file is not edited; this file is the issuer's disposition of the row, and the CTO is told in
the same turn.

## Cell

| cell | hop | writes | reads | depends on |
|---|---|---|---|---|
| `YCD-g-6` | 7-8 Persist | `reports/resident_installed.py`, `reports/tests/test_resident_installed.py`, `ycharts/generate/publisher.py`, `ycharts/generate/publication_worker.py`, `ycharts/generate/tests/test_publisher.py`, `ycharts/generate/tests/test_publication_worker.py` (base `infra/aws/lambda/investor-reporting/`) | v2 schema, `opal_producer.py` | s-6 and a-6 merged |

| `YCD-h-6` | 7 Render (page wording) | `ycharts/research/layout_overview.py`, `ycharts/research/tests/test_layout_overview.py` (base `infra/aws/lambda/investor-reporting/`) | `opal_producer.py` | a-6 and b-6 merged |

**Contract R8 (no vendor wording on the Opal page).** Under `pricing=False` (the Opal producer's mode) the printed Overview names no YCharts source: a builder-only element prints 'Not available in this version.' (reason NOT_IN_THIS_VERSION, as run.json and the document carry it), a vendor-call element the same, and the page footer credit does not read 'Data: YCharts'. With `pricing=True` (the research path) the page is unchanged. Source: worker row IRPT_YCDGEN-W1-S8 (measured: 65 BUILDER_ONLY and 22 call-sourced elements on the real map); PRD C-BRAND, C-BUILDERONLY.

**Contract R7 (persist the Opal form).** A document with `provider: OPAL_ENGINE` is persisted and the job reaches READY through a path that
accepts the Opal metadata key set `{request_ref, opal_artifact, effective_inputs, release}` (plus `computation_validation` and `sections` as the v2
schema carries them) and an artifact reference of its own family (the worker names the family in a surprise row; it is not `ORIGINAL_VENDOR_PDF`).
The resident validator validates an OPAL_ENGINE document against `AnalysisReport.v2.schema.json` and still validates a YCHARTS document against
the v1 members. The YCharts path is unchanged for every existing test. No code path accepts both key sets on one request.

## Edges and fan-out

g-6 depends on merged s-6 and a-6 (both merged). d-6 now also depends on g-6. `YCD-h-6` depends on merged a-6 and b-6 only. Its own chain: M = 2 for this addendum (g-6 and h-6 touch disjoint files and depend on nothing the other writes). Worker slots `~3` (g-6) and `~4` (h-6). The parent
fan-out line (2 of 2 chains) stands for its issuance; this addendum adds one chain: fanout: 2 of 2 chains, cap 8, reason: two independent hops.

## Four-postulate record (Rule 24)

MECE: the persist hop (7-8) had no owner in the parent's denominator (8 hops, 6 served, 1 unchanged, 1 empty); it moves from "served by hop 8's cells" to
its own cell. Same grain: three files of one persist path. Intent: g-6 one outcome (an Opal document reaches READY); h-6 one outcome (the Opal page names no vendor). State: the YCharts branch is not moved.

## Battery

Lenses as the parent: comp-schedule, comp-iam and comp-adversary DECLARED-NOT-APPLICABLE (thread round, no grant change); the resident host's role is
proved at the close run.
