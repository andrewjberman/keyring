# IRPT_BCKEND: CVO adjudication, round 175 (workstream ~P)

<sweep_watermark>2026-10-13T07:16Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T07:16:00Z, on msg 6837 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_175_P_DRAIN_END_20261013.md`, 159c5a343b). Two orders, no judgment criterion. 8 rows dismissed below
(five of them earlier rows closed by the portal DEV landing); 1 graduates ARMED in `remediations/REMEDIATION_v52.md` (the per-firm package
census before the host-bundle pair).

```json
[
 {
  "id": "IRPT_BCKEND-C-S359",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T07:16:00Z",
  "one_line": "Dismissed: Round 175 (~P). D2-S129 and D2-S130 (the issuer's disarm and disposition records), D2-W359-S2 (a docstring that says nine members where the guard and the object carry twelve). Closed on the portal DEV landing, read by this seat: D2-W346-S2, D2-W346-S3 and D2-W350-S1 (ARMED; the fe-s-15 and fe-s-18 generators reproduce their committed outputs, IB-pr-500 and IB-pr-502 on DEV), D2-W346-S4 (the ExportBundle's selected_sections aligned, e50a1379), D2-W353-S5 (the frozen export envelope carries covered_account_ids, IB-pr-504 on DEV).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-S129",
   "IRPT_BCKEND-D2-W359-S2",
   "IRPT_BCKEND-D2-S130",
   "IRPT_BCKEND-D2-W346-S2",
   "IRPT_BCKEND-D2-W346-S3",
   "IRPT_BCKEND-D2-W350-S1",
   "IRPT_BCKEND-D2-W346-S4",
   "IRPT_BCKEND-D2-W353-S5"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "IB-pr-507 and IB-pr-508 are complete; drains 8db2eb22f5 and 89af2d14e4 on HEAD. The census read the DIRECTORY bundle, not the builder's per-firm package (the issuer's premise, ruled), so the host-bundle pair cannot be written yet. Portal DEV carries every IRPT_BCKEND candidate; PROD is unchanged.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-S129, D2-W359-S2, D2-S130, D2-W346-S2, D2-W346-S3, D2-W350-S1, D2-W346-S4, D2-W353-S5",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_175_P_DRAIN_END_20261013.md (159c5a343b, msg 6837)",
    "this seat's read 2026-10-13T07:1xZ: portal git fetch; origin/DEV e50a1379 (PROD 37aa1247 unchanged); DEV's log carries the rebased candidates by subject: f54d7ca6 (IB-pr-502, the fe-s-18 generator), 4c8dc57f (IB-pr-500, the fe-s-15 generator), 9427632a and 86293960 (IB-pr-495), c2a53576 and 58070e5c (IB-pr-504), 3c551adb (IB-pr-506), e50a1379 (the integration fix: selected_sections in the ExportBundle)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Records, a docstring note, and five rows closed by a DEV landing this seat read."
 }
]
```
