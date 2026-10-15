# IRPT_BCKEND: CVO adjudication, round 5 (workstream ~PJ, the rebuilt 49 Financial performance candidate)

<sweep_watermark>2026-10-15T19:51Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T19:51Z, on msg 8586 (shared packet @f7b4555d40). One order, IB-pr-597 (risk SERVED, build-only, read-only on AWS), complete, merged @b294b1b4c4 (records and harness under `~435` only). Re-run here at HEAD: IB230-1-AC1..AC3 PASS (exit 0). `round-close-check --round 5 --workstream "~PJ"`: MAY-CLOSE.

The candidate is `LiDXhN74...` (record `~435/IB230-1_perf_candidate.json`): 2 of 14 members moved, built twice byte-identical, carrying IB-pr-592's named ratio-absent list. It replaces `fvmE5j1h...` (v126) for the 49F split pair, whose COO half is re-issued on it. Nothing deployed: the live `irpt-holdings-performance-lambda` still reads `o9UugRAV...` (2026-10-15T06:06:08Z). Sign only on `LiDXhN74...`.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S41",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T19:51:00Z",
  "one_line": "~PJ r5. Rebuilt 49F performance candidate LiDXhN74: 2 of 14 members moved, built twice identical, carries the named ratio-absent list; it supersedes fvmE5j1h for the split pair. IB230-1-AC1..AC3 PASS re-run; build-only; live Lambda unchanged (o9UugRAV). Dismissed (1): D2-W435-S1 (ARMED; the client-data WARN on this box, standing per Andrew's 2026-10-09 record; disarmed in S208).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W435-S1"
  ],
  "spec_asserts": "Never-widen: the split pair is signed on the candidate digest that carries condition 3.",
  "world_is": "A signable performance candidate exists at LiDXhN74; nothing is deployed.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T19:3xZ of the invocations in IB-pr-597: IB230-1-AC1..3 PASS, exit 0; round-close-check ~PJ round 5 MAY-CLOSE",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~435/IB230-1_perf_candidate.json",
    "aws lambda get-function-configuration irpt-holdings-performance-lambda: 2026-10-15T06:06:08Z, o9UugRAV...",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_192xZ_CLIENT_DATA_IN_PRIVATE_GIT_NOT_WORTH_TIME.md",
    "investigation rows D2-W435-S1, D2-S208",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PM1_PN2_PN3_PJ4_PJ5_PO8_DRAIN_END_20261015.md @f7b4555d40 (msg 8586)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A client-data WARN whose standing on dell2 is Andrew's recorded word, disarmed by its owner."
 }
]
```
