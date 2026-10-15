# IRPT_BCKEND: CVO adjudication, round 1 (workstream ~PY, the IB-pr-456 irpt-ycharts-generate candidate rebuilt on the live R29c bytes)

<sweep_watermark>2026-10-15T07:18Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T07:18Z, on msg 8168 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PY_DRAIN_END_20261015.md` @a23f2ddb5b). One order, IB-pr-561, complete, merged @6f019c40ee. Read-only on AWS; nothing uploaded, applied or deployed.

**Grade: the candidate is DEFECTIVE and REJECTED. Its three criteria PASS, and that PASS is not acceptance.** Re-run here at HEAD: IB203-2-AC1..AC3 PASS (exit 0 each); `round-close-check --round 1 --workstream "~PY"`: MAY-CLOSE. Those criteria could not see the defect: the r1 record (`deliverables/0.9.0_WK_IRPT_BCKEND~405/IB203-2_ycharts_generate_rebuild.json`) carries no pin and no `commentary_requested` count for any ENDPOINT member, so AC2 graded the consistency of flags, not the feature's presence. The candidate `MfxpvRhV...` must never be applied.

**The issuer's disclosure is ACCURATE, measured here.** The trunk source map stages the three ENDPOINT members of `irpt-ycharts-generate` at pins that predate the feature: `submission.py` @1eed34a8c0, `acceptance.py` @2f7cc7be42, `AnalysisSubmissionRequest.schema.json` @5be2acd7cc each hold `commentary_requested` 0 times (git show at the pin). The r1 record's own `submission.py` hash (`82c47bd0...`) differs from its `sha256_at_signing` (`18aba4f0...`), the trace of building from the old pin. The record's conclusion "ENDPOINT bytes moved, re-sign owed" was that pin artifact, as disclosed; CTO row S187's premise is withdrawn by S188. The correction is round 2 (v109).

This is round 1 closing as SUPERSEDED output: MAY-CLOSE stands for the order as run, and the round's deliverable (the candidate) is replaced by IB-pr-564's (S189). Held: D2-W405-S1 (ARMED, `~P2`: `composition_admission.py` rides, ruling owed), D2-S188 (ARMED, `~P2`: the correction row; dispositioned in v109 once the corrected candidate is verified).

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S16",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T07:18:00Z",
  "one_line": "Round 1 ~PY. REJECTED candidate: IB-pr-561's rebuild MfxpvRhV dropped commentary_requested because the trunk source map pins the three ENDPOINT members at commits that predate it (0 occurrences each at 1eed34a8c0, 2f7cc7be42, 5be2acd7cc, measured here). IB203-2-AC1..AC3 PASS re-run, but the record holds no pin or count for those members, so the criteria could not discriminate; a PASS here is not acceptance and MfxpvRhV must never be applied. The issuer's disclosure is accurate. Superseded by IB-pr-564 (v109). Dismissed (1): D2-S187 (withdrawn premise, corrected by S188). Held: D2-W405-S1, D2-S188.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-S187"
  ],
  "spec_asserts": "A value must carry its claim (CLAUDE.md section 4): a criterion that cannot see the property it grades yields no measured PASS for that property; spine L9: a defective candidate is graded as such, never by its criteria's exit code alone.",
  "world_is": "The r1 candidate is wrong and replaced; nothing was uploaded or applied. The defect's class: a check that graded the record's self-consistency, not the built bytes. Its fix (read each member at its pin and require the feature) is in IB-pr-564's check.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T07:1xZ of the invocations in IB-pr-561: IB203-2-AC1..3 PASS, exit 0 each",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 1 --workstream ~PY: orders=1 proof_ok=1 judgment=0 verdict=MAY-CLOSE",
    "infra/aws/lambda/ci/lambda-source-map.json irpt-ycharts-generate staged_from pins: submission.py 1eed34a8c0, acceptance.py 2f7cc7be42, AnalysisSubmissionRequest.schema.json 5be2acd7cc; git show at each pin: commentary_requested 0, 0, 0",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~405/IB203-2_ycharts_generate_rebuild.json: endpoint_members carry no pin or count; submission.py sha256_now 82c47bd0... vs sha256_at_signing 18aba4f0...",
    "investigation rows D2-S187, D2-S188, D2-W405-S1, D2-S189",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PY_DRAIN_END_20261015.md @a23f2ddb5b (msg 8168)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "S187's premise is withdrawn by its author's correction S188. The defective candidate is rejected here and superseded; the correction row and the composition_admission ride are held with ~P2."
 }
]
```
