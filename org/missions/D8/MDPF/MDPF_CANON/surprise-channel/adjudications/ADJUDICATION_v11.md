# MDPF_CANON -- round 7 L9 note: CN-j-1 AC4 held (dell1)

<sweep_watermark>2026-10-14T16:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T16:50:00Z. Asked by 2.0.0_SA_COO~D1 msg 5653 (readback commit 7c6872568f). One row; no rows swept, so the watermark does not move.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S77",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T16:50:00Z",
    "one_line": "ROUND 7: MDPF_CANON.TO-CN-j-1 AC4 HELD until the first scheduled publisher run (2026-10-15 13:50Z); interim read on the D2 run 8 of 9 arms (H9 owed); the semantic arm waits on CN-i-1's repaired, landed Trend.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON.TO-CN-j-1 AC4 (judgment): /seams on the leaf-to-chip seam, grounded on the served objects after the deploy and the first scheduled publisher run that carries the code.",
    "world_is": "ROUND 7, MDPF_CANON.TO-CN-j-1 AC4 HELD -- not graded yet, on the criterion's own text: AC4 is 'grounded on the served objects after the deploy and the first scheduled publisher run that carries the code'. The deploy is done (ledger 20261014T1626Z_mdpf-canon-r7-publisher-deploy-dell1-20261014, closed 2026-10-14T16:37:06Z, pin 9592daf75c); the first scheduled publisher run is 2026-10-15 13:50Z. INTERIM READ, this seat's run of round7/checks/r7_history_readback.py read at ~16:47Z on the on-demand D2 run: 8 of 9 arms -- H1 the four leaves present (27/26/20/22 dates); H2 leaf dates equal the dated gold objects, omitted 0; H3 190 cells equal to the cent, 0 expected-null, 0 mismatch; H4 shape; H5 keyset, header, omitted shape, provenance; H6 last date 2026-10-13 equals the served as_of; H7 manifest 20261014T163424Z-4b660bd9.json, 18 pair rows unchanged; H8 18 of 18 pair rows equal to gold apart from _provenance; H9 FALSE (the leaves were written before the ledger closed; the scheduled run rewrites them). STILL OWED for the grade: (1) H9 on the 2026-10-15 13:50Z scheduled run; (2) the MECHANICAL route clause -- reachability through /api/general/mdpf/{scope}/category-views-history.json -- which the readback does not call (its header names it the CloudOps read of the deploy order); (3) the SEMANTIC arm, 'the Trend's Client chips draw on the leaf's dates and are absent, never zero, on every other date': the chips are rendered by CN-i-1's portal candidate, which is not landed and whose tooltip renders a null series as a $0 row (D1-C-S73, D1-W18-S1), so this arm cannot pass until that candidate is repaired and landed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO python org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_history_readback.py read: ROUND 7 HISTORY READBACK: 8 of 9 arms",
        "org/critical_paths/change_management/20261014T1626Z_mdpf-canon-r7-publisher-deploy-dell1-20261014_deploy_completion.md (closed 20261014T163706Z)",
        "task-orders/MDPF_CANON.TO-CN-j-1.category-views-history-leaf.md AC4 text",
        "adjudications/ADJUDICATION_v10.md D1-C-S73"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A hold record: AC4 is graded after the 2026-10-15 13:50Z scheduled run; not a hazard."
  }
]
```
