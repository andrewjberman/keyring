# IRPT_BCKEND: CVO adjudication, round 177 (workstream ~P)

<sweep_watermark>2026-10-13T08:35Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T08:35:00Z, on msg 6865 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_177_P_DRAIN_END_20261013.md`, aa1ffa367e). Two orders, no judgment criterion, nothing applied. The
four 'unattributed' live members are CRLF copies of repository blobs, so D2-W361-S3 closes. 7 rows dismissed below; 1 graduates to the CTO in
`remediations/REMEDIATION_v54.md` (two unread bucket-policy writes by dell1's agent on the 49 Financial bucket).

```json
[
 {
  "id": "IRPT_BCKEND-C-S361",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T08:35:00Z",
  "one_line": "Dismissed: Round 177 (~P). D2-W363-S1 (the four 'unattributed' live members are CRLF copies of repository blobs, 0 lines differing as LF: resources.json at f185873e, reporting_policies.json at f60e6f1d), D2-W362-S1 (BLOCKING; the check demanded a replaced member for cottonwood, which the rule gives nothing; amended @f33aa02571), D2-W362-S2 (the apply restamps each object's S3 metadata, per the packet), D2-W362-S3 (the candidate keeps the live schema copy's CRLF), D2-W362-S4 (the amendment applied), D2-S132 (the issuer's disposition and disarm record), and REMEDIATION_v53's D2-W361-S3 (ARMED; disarmed on D2-W363-S1: the bytes are explained, and the pair carries them unchanged, named by path and sha256).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W363-S1",
   "IRPT_BCKEND-D2-W362-S1",
   "IRPT_BCKEND-D2-W362-S2",
   "IRPT_BCKEND-D2-W362-S3",
   "IRPT_BCKEND-D2-W362-S4",
   "IRPT_BCKEND-D2-S132",
   "IRPT_BCKEND-D2-W361-S3"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "IB-pr-510 and IB-pr-511 are complete (order files read); drains d5124284a0 and 06a7bd1525 and check amendment f33aa02571 are on HEAD. The minimal per-firm packages are BUILT (49financial 3 members replaced, inflection 2, cottonwood none); nothing is uploaded or applied. The COO half is signed; the CTO half is not. The apply waits on the runner host's next scheduled Online.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W363-S1, D2-W362-S1, D2-W362-S2, D2-W362-S3, D2-W362-S4, D2-S132, D2-W361-S3",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_177_P_DRAIN_END_20261013.md (aa1ffa367e, msg 6865)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Explained bytes, a check amended, readings the packet carries, and a disarmed row closed."
 }
]
```
