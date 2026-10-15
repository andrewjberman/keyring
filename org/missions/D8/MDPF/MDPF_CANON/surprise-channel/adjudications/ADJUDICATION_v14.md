# MDPF_CANON -- round 7 L9 note: CN-j-1 AC4 still held after the scheduled run (dell1)

<sweep_watermark>2026-10-14T16:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-15T14:05:00Z. Follows the hold row MDPF_CANON-D1-C-S77 (ADJUDICATION_v11). One row; no rows swept, so the watermark does not move.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S80",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T14:05:00Z",
    "one_line": "ROUND 7: MDPF_CANON.TO-CN-j-1 AC4 HELD. The scheduled 13:50Z run reads 9 of 9 arms (H9 now true), but the authenticated route and the Trend chip arm wait on the CN-i-2 Trend landing on portal DEV, which has not happened.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON.TO-CN-j-1 AC4 (judgment): /seams on the leaf-to-chip seam, grounded on the served objects after the deploy and the first scheduled publisher run that carries the code.",
    "world_is": "ROUND 7, MDPF_CANON.TO-CN-j-1 AC4 HELD, one of three owed items now closed. (1) CLOSED: this seat's run of round7/checks/r7_history_readback.py read at ~13:59Z on the first scheduled run (manifest 20261015T135048Z-5a1d60b7) reads 9 of 9 arms. The four leaves carry 28/27/21/23 dates, one more each than the D2 run; H3 has 198 cells equal and 0 mismatches; H6 has the last leaf date equal to the served as_of 2026-10-14 on all four; H8 has 18 of 18 pair rows equal to gold; and H9 has all four leaves written after the ledger close 20261014T163706Z. (2) OWED: the authenticated route. The deploy ledger's L5 leg read HTTP 401 on all four /api/general/mdpf/<scope>/category-views-history.json paths without a session, and deferred the session-holding read to CN-i-1's landing. (3) OWED: the semantic arm, 'the Trend's Client chips draw on the leaf's dates and are absent, never zero, on every other date'. The chip code is CN-i-2's repair at portal fd5433a3, graded MET as MDPF_CANON.TO-CN-i-1 AC4 in ADJUDICATION_v13, but it is not on portal origin/DEV ad7c100b5c or origin/PROD c3b21a40e2. Read by content, not ancestry: git diff fd5433a3 origin/DEV over its three files is 347 insertions and 102 deletions, and src/lib/trendGrouping.ts is absent on DEV. Items (2) and (3) are graded together on the landed page.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO python org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_history_readback.py read: ROUND 7 HISTORY READBACK: 9 of 9 arms (manifest 20261015T135048Z-5a1d60b7)",
        "org/critical_paths/change_management/20261014T1626Z_mdpf-canon-r7-publisher-deploy-dell1-20261014_deploy_completion.md leg L5 (401 on all four scopes; the authenticated read deferred to CN-i-1's landing)",
        "portal: git diff --stat fd5433a3 origin/DEV -- src/api/portal-proxy.ts src/lib/trendGrouping.ts src/pages/ModelPortfolios.tsx: 3 files, 347 insertions, 102 deletions (origin/DEV ad7c100b5c, fetched 2026-10-15 ~13:59Z)",
        "adjudications/ADJUDICATION_v11.md MDPF_CANON-D1-C-S77; adjudications/ADJUDICATION_v13.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A hold record: AC4 is graded when the CN-i-2 Trend lands on portal DEV; not a hazard."
  }
]
```
