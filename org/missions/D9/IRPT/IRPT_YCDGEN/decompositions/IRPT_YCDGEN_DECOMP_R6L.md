# IRPT_YCDGEN -- DECOMPOSITION, ROUND 6 ADDENDUM L: the AnalysisReport contract catches up with the served OPAL_ENGINE form

```json
{
 "project": "IRPT_YCDGEN",
 "round": 6,
 "addendum": "L",
 "prd_ref": "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (v0.10 @5a04dc8c4a)",
 "prd_version": "v0.10",
 "endpoint_outcomes": ["FWD-1"],
 "round_scope": ["FWD-1"],
 "author": "2.0.0_SA_COO~G2",
 "cells": 2,
 "chains": 1,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.1",
 "parent_decomp": "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6K.md",
 "cell_ids": ["YCD-u-6", "YCD-v-6"]
}
```

**Why an addendum.** Row IRPT_BCKEND-S388 (2.0.0_SA_COO~P2, msgs 1187/1190) measured at portal DEV d1b21c97 that a regeneration of the
wire types would REMOVE 56 lines from `contracts/wire/AnalysisReport.ts`: the OPAL_ENGINE form that cell YCD-e-6 (portal 81bbeba2,
2026-10-05) added by hand. `docs/contracts/investor-reporting/v1/AnalysisReport.schema.json` carries no OPAL_ENGINE (last changed
beecb3395a, 2026-09-22). The type ran ahead of its contract. 1.0.0_SA_CTO~DELL2 ruling msg 1194: the form goes into v1 as an
ADDITIVE branch (it is already served, so the contract follows the served shape; a v2 sibling would be two contracts for one
document), with three criteria, and nobody regenerates that file until this drains.

## Cell

| cell | hop | writes | reads | depends on |
|---|---|---|---|---|
| `YCD-u-6` | contract (the AnalysisReport schema) | `docs/contracts/investor-reporting/v1/AnalysisReport.schema.json`, `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/u6_checks.py` (new) | portal `src/pages/InvestorReporting/contracts/wire/AnalysisReport.ts` at d1b21c97, `__tests__/fe-s-13/gen-wire.ts`, the existing AnalysisReport fixtures, every reader of the schema | none open |

**Writer read.** No non-terminal task order of the project names these paths. ~P2's IB-pr-359 makes the generator tests write to a
temp directory and does not edit the schema or the wire types (its face says so); ~P's own regenerate cell covers ExportBundle,
ExportReceipt, responses and index, never AnalysisReport.

**Contract R19 The AnalysisReport schema carries the served OPAL_ENGINE form.** The v1 schema gains the OPAL_ENGINE form as a new
branch that matches the committed `AnalysisReport.ts` at d1b21c97. Every document valid before stays valid. The generator, run to a
temporary directory against the new schema, produces an `AnalysisReport.ts` byte-identical to the committed one. Every reader of the
schema is named and read against the new branch.

## Edges and fan-out

M = 1, no dependency open. fanout: 1 of 1 chain, cap 8, reason: one contract cell.

## Four-postulate record (Rule 24)

MECE: the form has one served shape (the committed type) and one contract (the schema); the cell makes the second describe the first.
Same grain: one document type. Intent: one outcome (regeneration no longer deletes a served type). State: no served behaviour moves;
the wire types, the portal and every other schema are untouched.

## Battery

comp-schedule, comp-iam and comp-adversary DECLARED-NOT-APPLICABLE (a contract document change; no deploy, no grant, no schedule).

## Revision 1.1 -- 2026-10-08 (2.0.0_SA_COO~G2): u-6 recut on v2 (CTO~DELL2 ruling msg 1250) and the consumer cell YCD-v-6

u-6 was recut to move the generator's AnalysisReport source to the served v2 schema (`_contracts/AnalysisReport.v2.schema.json`),
v1 byte-frozen. Its proof instance (c73a029dc3) measured AC1 PASS, AC2 FAIL, AC3 FAIL. AC2 (ruled by the CTO: generated body equals
committed body, header excluded) fails because the committed `contracts/wire/AnalysisReport.ts` is hand-shaped: an interface with an
optional `provider` plus four hand-added OPAL names, where the generator emits one `oneOf` union (row IRPT_YCDGEN-D2-W6-S1). The
gap is the consumers, not the generator: "THE PRODUCER DEFINES, THE CONSUMER CONFORMS" (gen-wire.ts header). AC3's three red tests
are unrelated to either schema and red on CLOUD too (row D2-W6-S2); u-6's AC3 is amended to "no reader newly red against CLOUD".

| cell | hop | writes | reads | depends on |
|---|---|---|---|---|
| `YCD-v-6` | portal consumer (the AnalysisReport wire type) | portal `src/pages/InvestorReporting/contracts/wire/AnalysisReport.ts` (regenerated), `contracts/adapt.ts`, `contracts/index.ts`, `src/api/endpoints/investor-reporting.ts`, `__tests__/mvp-selection/coverage.test.ts` (only where they name the hand-added types) | the v2 schema, gen-wire.ts at portal dc88c4f7 | YCD-u-6's generator edit (portal dc88c4f7), same chain ~6 |

**Contract R20 The committed AnalysisReport wire type IS the generator's output from v2.** The committed file equals the generated
one (header excluded); every consumer of the hand-added names reads the generated union instead; the portal typecheck passes; u-6's
AC2 then passes as the CTO ruled it. Edges: v-6 after u-6's generator edit; fanout: 1 of 1 chain, cap 8. Risk SERVED (portal
product files change; nothing deploys; the candidate goes to the CTO before DEV). Four postulates: one document type, one intent
(the wire type is generated, never hand-edited), state: no served backend behaviour moves.
