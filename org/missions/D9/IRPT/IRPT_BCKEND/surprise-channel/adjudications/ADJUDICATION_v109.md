# IRPT_BCKEND: CVO adjudication, round 2 (workstream ~PY, the irpt-ycharts-generate candidate rebuilt with the candidate map)

<sweep_watermark>2026-10-15T07:18Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T07:18Z, on msg 8168 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_2_PY_DRAIN_END_20261015.md` @37ebe5f8d7). One order, IB-pr-564, complete, merged @c324a93684, issued @be4b5f4545 to correct IB-pr-561. Read-only on AWS; nothing uploaded, applied or deployed. Re-run here at HEAD: IB205-1-AC1..AC3 PASS (exit 0 each). `round-close-check --round 2 --workstream "~PY"`: orders=1, proofs 1 of 1 ok, verdict=MAY-CLOSE.

**The r1 defect is gone, shown by running the r1 failing case against both candidates.** The r1 case is "an ENDPOINT member staged from a pin that predates `commentary_requested`".
- At the trunk-map pins r1 used: `submission.py`, `acceptance.py`, schema hold `commentary_requested` 0, 0, 0 (measured here).
- At the r2 record's pins (all @e7bb7e923a, the signed commit): 3, 3, 1 (measured here, equal to the record's counts), and each member's sha256 at the pin equals its `sha256_at_signing` (`submission.py` 18aba4f0..., matching the independent release read `0.9.0_WK_IRPT_BCKEND~312/IB152-1_release_read.json`). So no ENDPOINT byte moved against the signed pair; no re-sign is owed by the CTO's rule.
- Negative control on the new check: `p205_cells.py` run against the r1 record reads AC1 FAIL ("equals ... the wrong MfxpvRhV"), AC2 FAIL, AC3 FAIL; against the r2 record AC2 PASS. The new check refuses the r1 candidate by digest and requires the feature at each pin (`p205_cells.py:100-102`), so it cannot pass on the r1 mistake.

The candidate is `3+fMEJhQ8...`, 106 members, 4 moved against the live zip `5TRFZf6G...` (`acceptance.py`, `submission.py`, the schema, `composition_admission.py`); release 29's four members are byte-identical to live (no silent revert). The feature is not live (live members 0 per the issuer's count; call f61b still gates the apply, Andrew's execution ID). Held: D2-W405-S1 (ARMED, `~P2`): `composition_admission.py` (IRPT_ANLREQ cause commit 83eb798a08) rides and the signed pair does not name it; whether it rides inside that pair or needs its own half is the CTO's. D2-W408-S1 (ARMED, `~P2`): the trunk map's pins hold 0 counts; a later rebuild from trunk would drop the feature again until the map is re-pinned.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S17",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T07:18:00Z",
  "one_line": "Round 2 ~PY. The corrected candidate 3+fMEJhQ8 (candidate map at signed commit e7bb7e923a) carries commentary_requested: 3, 3, 1 at its pins vs 0, 0, 0 at the trunk-map pins r1 used (both measured here); each ENDPOINT member's sha256 equals the signed hash, so no re-sign is owed; release 29's members unmoved. IB205-1-AC1..AC3 PASS re-run; the new check run on the r1 record fails AC1..AC3 (negative control), so the r1 defect cannot pass it. Nothing applied; f61b gates. Dismissed (1): D2-S188 (ARMED, ~P2; the defect it records, the candidate omitting the feature, is fixed and verified here on the built bytes). Held: D2-W405-S1 (composition_admission.py rides outside the signed pair, CTO ruling owed), D2-W408-S1 (trunk map pins still predate the feature; a trunk rebuild would drop it again).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-S188"
  ],
  "spec_asserts": "Spine L9: a correction is accepted only when the failing case of the defect it corrects fails no more, read on the built bytes; never-widen re-signs only when ENDPOINT bytes move (CTO's rule).",
  "world_is": "A correct candidate exists for the IB-pr-456 apply and nothing has moved. Two carriers stay open: the extra member composition_admission.py (the CTO's call on whether the signed pair covers it) and the trunk source map's stale pins (D2-W408-S1), which would reproduce the r1 defect on any rebuild from trunk until re-pinned.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T07:1xZ of the invocations in IB-pr-564: IB205-1-AC1..3 PASS, exit 0 each",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 2 --workstream ~PY: orders=1 proof_ok=1 judgment=0 verdict=MAY-CLOSE",
    "git show e7bb7e923a:<member>: commentary_requested 3 (submission.py), 3 (acceptance.py), 1 (AnalysisSubmissionRequest.schema.json); sha256 18aba4f0..., abbdab49..., 1052343f... equal the record's sha256_at_signing",
    "git show at trunk-map pins 1eed34a8c0, 2f7cc7be42, 5be2acd7cc: commentary_requested 0, 0, 0",
    "negative control: p205_cells.py with REC pointed at 0.9.0_WK_IRPT_BCKEND~405/IB203-2_ycharts_generate_rebuild.json: IB205-1-AC1 FAIL, AC2 FAIL, AC3 FAIL; positive control on the r2 record: AC2 PASS",
    "18aba4f0792f... also in 0.9.0_WK_IRPT_BCKEND~312/IB152-1_release_read.json (4 hits)",
    "investigation rows D2-S188, D2-W405-S1, D2-W408-S1, D2-S189",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_2_PY_DRAIN_END_20261015.md @37ebe5f8d7 (msg 8168)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "S188's defect is corrected, verified against the r1 failing case on the built bytes and by negative control; the two open carriers are held with ~P2 for the CTO."
 }
]
```
