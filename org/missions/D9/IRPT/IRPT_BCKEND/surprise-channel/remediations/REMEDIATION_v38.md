# IRPT_BCKEND -- rounds 106 and 108 remediations (~P)

<sweep_watermark>2026-10-09T12:14Z</sweep_watermark>

Graduated at the rounds-106/108 L8 (ADJUDICATION_v49.md), round label v109: 2 rows, OPEN.

```json
[
  {
    "id": "IRPT_BCKEND-D2-S46",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "9 investor-reporting _contracts tests fail at box/dell2 HEAD: the public-route count (21 vs 22, the AR-y-22 /original route), the paired-seam response contracts, and export-receipt fixtures missing covered_account_ids.",
    "evidence": [
      "investigation row IRPT_BCKEND-D2-S46",
      "clean worktree at box/dell2 HEAD ~11:5xZ: pytest _contracts -> 9 failed, 171 passed, 13 skipped"
    ],
    "remedy": "Bring the 9 investor-reporting _contracts tests back to green at HEAD: the public-route count (22 with /original), the paired-seam response contracts, and the export-receipt fixtures' covered_account_ids -- one owner, each failure named to its causing cell.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v109",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v109"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-D2-W268-S1",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The order's release packet needs a built zip that carries the change, but lambda-source-map.json pins irpt-status's three changed members to older commits; the map is not in <paths>, so the census is built at a scratch candidate map (BAU_SOURCE_MAP_OVERRIDE) and the packet hands the applier the rows to commit.",
    "evidence": [
      "investigation row IRPT_BCKEND-D2-W268-S1",
      "infra/aws/lambda/ci/lambda-source-map.json functions.irpt-status.staged_from: served.py @74a62fb46c, entry.py @eb70303e8f, owned_report.py @62880e9bfc (its _staged_from_note: 'These pins are the owning cells' to release: drop a row to ship that member's pending change')"
    ],
    "remedy": "Build the irpt-status release narrow on IRPT_ANLREQ release 1's live bytes after its after-reads close, with every re-pinned member owned in lambda-source-map.json (CTO ADDENDUM 17), not from a scratch candidate map.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v109",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v109"
    },
    "closed": false
  }
]
```
