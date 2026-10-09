# IRPT_YCDGEN -- DECOMPOSITION, ROUND 6 ADDENDUM N: the producer is chosen by the accepted ACTING principal

```json
{
 "project": "IRPT_YCDGEN",
 "round": 6,
 "addendum": "N",
 "prd_ref": "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (v0.10 @5a04dc8c4a)",
 "prd_version": "v0.10",
 "endpoint_outcomes": ["FWD-1"],
 "round_scope": ["FWD-1"],
 "author": "2.0.0_SA_COO~G2",
 "cells": 1,
 "chains": 1,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "parent_decomp": "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6M.md",
 "cell_ids": ["YCD-x-6"]
}
```

**Why an addendum.** The st26 F1 attempt (2026-10-09 01:25Z, ledger irpt-ycdgen-f1-st26-20261008) was refused at the upload by IRPT_BCKEND's
E5 (served.py:1012-1020, release 3, live since 2026-10-08 21:26Z): a filer whose allowedFirmIds lists the tenant must name the firm advisor
(`advisor_email`), and the upload is then OWNED by that advisor (served.py:1022-1050 -> `_scope/prospect.py:41`, owner.principal_id = the
advisor's email). `resident_worker.producer_for` (:126-133) chooses the producer from `owner.principal_id`, so every on-behalf request --
svc's F1 and Andrew's own on-behalf runs alike -- routes to YCHARTS. 1.0.0_SA_CTO~DELL2 ruling msg 2067: producer_for reads the accepted
ACTING principal recorded on the request, never a request field; a test for owner-advisor plus actor-svc. Then st27 under a fresh pair, then F1.

## Cell

| cell | hop | writes | reads | depends on |
|---|---|---|---|---|
| `YCD-x-6` | resident producer switch (C-SWITCH) | `ycharts/generate/resident_worker.py` (`producer_for`), its tests; IF the accepted request record carries no server-recorded actor, the acceptance path that records it (named by the worker's census, cut as a ruling before any edit outside resident_worker) | the accepted request / job record shapes, `intake/uploads.py:267` (`acting_principal_id` on on-behalf uploads), `prospect_submission.py` | none open |

All paths under `infra/aws/lambda/investor-reporting/`.

**Contract R22 The Opal producer is chosen by the accepted acting principal.** `producer_for` reads the acting principal the SERVER
recorded at acceptance (the authenticated actor of the submit), never a client-sent value and never the owner when an actor is recorded;
with no recorded actor it reads the owner as today. A request owned by a firm advisor and accepted from a listed actor takes OPAL; an
advisor-owned request accepted from an unlisted actor takes YCHARTS; the listed owner with no actor takes OPAL, as today.

## Edges and fan-out

M = 1. fanout: 1 of 1 chain, cap 8, reason: one producer-switch cell. Its release (st27) is its own never-widen pair.

## Four-postulate record (Rule 24)

MECE over {actor recorded, actor absent} x {listed, unlisted}. Same grain: one accepted request. Intent: one outcome (the producer follows
who acted). State: the YCharts path, the allow list and E5's ownership rule are unchanged; only the producer's key moves.

## Battery

comp-schedule and comp-iam DECLARED-NOT-APPLICABLE (no schedule, no grant). comp-adversary DECLARED-NOT-APPLICABLE (the gap was measured in
code at served.py:1022-1050, prospect.py:41, resident_worker.py:126-133, and ruled by the CTO, msg 2067).
