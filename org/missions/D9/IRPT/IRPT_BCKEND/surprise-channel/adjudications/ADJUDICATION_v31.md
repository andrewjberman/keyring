# IRPT_BCKEND -- project sweep 15 L8/L9 adjudication, part 2a (round 72 ~P)

<sweep_watermark>2026-10-07T21:49Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~21:5xZ. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_72_P_DRAIN_END_20261007.md @72208311d5` (msg 1120). Round 72's four orders (IB-pr-355..358) are
complete with 0 judgment criteria; IB-pr-353 is superseded by IB-pr-356. IB-pr-350 (round 69, the receipt back-fill, laptop applier) is
still pending, and while it is open the row gate refuses new remediation rows, so this part dismisses what it can. 6 round-72 rows: 5
dismissed by the 2 rows below. Held for graduation at IB-pr-350's drain (part 2b, REMEDIATION_v24): W145-S2, W145-S5, S381, S382, S384,
S369, W152-S1, W162-S1, W163-S1 and now W165-S2 (ARMED, disarm owner 2.0.0_SA_COO~P2: the full bun suite rewrites 27 tracked
contracts/wire/*.ts files, so a worker running it before tsc reads a false FAIL or stages the regenerated files). ARMED after this part:
S334, W140-S1, W145-S2, W165-S2.

```json
[
  {
    "id": "IRPT_BCKEND-C-S303",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T21:58:00Z",
    "one_line": "W164-S1 (ARMED: custody_read.py missing from the irpt-export-render build list) is dismissed as discharged by AMENDMENT 1 @169e6c8150.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-W164-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The issuer, the row's disarm owner, added custody_read.py to the export function's member list in AMENDMENT 1 @169e6c8150. This seat read the line at dell2 HEAD: lambda-source-map.json:4632 lists custody_read.py beside retained_export.py and submit_service.py. A zip built from HEAD now carries the module; the route stays unreleased until its own pair (IB-pr-351, 352, 355), so nothing served moved.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_BCKEND-W164-S1",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_72_P_DRAIN_END_20261007.md @72208311d5",
        "infra/aws/lambda/ci/lambda-source-map.json:4632 \"custody_read.py\" (this compile's read, dell2 CLOUD, 2026-10-07 ~21:5xZ)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An ARMED build-list gap closed at source by its disarm owner, with the line read at HEAD."
  },
  {
    "id": "IRPT_BCKEND-C-S304",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T21:58:00Z",
    "one_line": "W164-S2 (the operation is built to the Entry's call signature), W164-S3 (the issuer's AC2 slice defect, fixed by AMENDMENT 1), W165-S1 (the custody read sits outside parseIrEnvelope) and W165-S3 (the route-table row was ahead of routes.json until IB-pr-355 landed) are dismissed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-W164-S2",
      "IRPT_BCKEND-W164-S3",
      "IRPT_BCKEND-W165-S1",
      "IRPT_BCKEND-W165-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W164-S2: the Entry invokes every operation as (request, scope, event, ctx); the face's two-argument form was a description, and the built signature is the only callable one. W164-S3: the checker sliced ROUTES at the brace inside {exportId}; AMENDMENT 1 @169e6c8150 fixed the slice, and IB72-1-AC2 PASSES on the issuer's re-run at 5c3067c649. W165-S1: the portal reads the custody answer as the bare body or the envelope's data and checks kind, id and revision against the request, with a refusal envelope proved; it is a placement note pending a data adapter in envelope.ts. W165-S3: both halves of the route declaration are now in one tree (IB-pr-355 @5c3067c649, IB-pr-356 @85c56b2381).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_BCKEND-W164-S2, IRPT_BCKEND-W164-S3, IRPT_BCKEND-W165-S1, IRPT_BCKEND-W165-S3",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_72_P_DRAIN_END_20261007.md @72208311d5"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Notes on signatures, a fixed check defect, and a cross-cell order that both drains settled."
  }
]
```
