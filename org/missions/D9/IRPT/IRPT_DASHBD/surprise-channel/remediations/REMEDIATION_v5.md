# IRPT_DASHBD -- rounds 12 to 14 (workstream B) remediations

<sweep_watermark>2026-10-04T23:59Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-05 ~06:2xZ. L8 input: the issuer's drain-end packet org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/IRPT_BCKEND_ROUNDS_47_51_P_DRAIN_END_20261005.md @4e3b64b6ea (msg 105174). 3 of 3 orders are terminal and merged: DB-b-20 @5a671b2aba, DB-b-21 @7cadb6e555, DB-b-22 @7c8d60abc8. 4 rows surfaced after the previous watermark 2026-10-03T02:35Z (S23, S24, S25, W7-S1); 52 rows are in the channel. 1 is dismissed by ADJUDICATION_v4.md (S25, C-S15). 3 graduate here: S23 OPEN, S24 REMEDIATED and closed (the fix f2d2f17c is on portal PROD c69b474716), W7-S1 OPEN. 0 ARMED, 0 JUDGMENT criteria. round label v15 (one past v12).

The pull's served state, read for this compile: s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/ holds 2,012 objects, all acct=<id>.json (oldest 2026-10-04T23:54:39Z, newest 2026-10-05T04:11:24Z), against the plan of 5,252, which agrees with the packet. Ledger irpt-dashbd-e3-bd-population-pull-20261004 is OPEN with legs P1 and G1 open; its window was extended to 9.0 h from 2026-10-04T23:37:45Z, so it runs to 08:37:45Z. The relaunch is Andrew's call (packet).

No carried row's clock moves at this compile, and carried rows are not re-read.

Round label v15 = the round after the last one compiled here (rounds 12-14), per REMEDIATION_v4's v12 for rounds 10-11.

```json
[
  {
    "id": "IRPT_DASHBD-S23",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "docs/contracts/investor-reporting/v1/routes.json declares 19 routes and omits both live reporting routes, GET .../reporting/{account_id}/{which} and GET .../reporting/client/{client_id}/summary, which reporting/entry.py declares, the API gateway serves behind irpt-49f-reporting-read-lambda, and PROD portal calls; a census reading routes.json cannot see them.",
    "evidence": [
      "investigation row IRPT_DASHBD-S23",
      "docs/contracts/investor-reporting/v1/routes.json at CLOUD HEAD 4e3b64b6ea: 19 routes, 0 route_key under investor-reporting/reporting; last commit 7f1135f0ee (2026-10-02), none since the row (this compile's read, 2026-10-05 ~05:4xZ-06:1xZ)"
    ],
    "remedy": "Add both reporting routes to routes.json with their guard, and re-run any census that reads the file (the _authz unguarded census among them); the row closes on this seat's read of both routes in the file.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v15"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-S24",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The FAST pin for 557862f1 (the Performance tab skips the PATH A read when PATH B serves the account) could not see the skip's direction, and by reading, an account the client summary lists whose own PATH B manifest read fails sent neither request and stayed on Loading.",
    "evidence": [
      "investigation row IRPT_DASHBD-S24",
      "investigation row IRPT_DASHBD-S25 (2.0.0_SA_COO~D, 2026-10-03T20:38Z): portal f2d2f17c skips PATH A only on the account's own served PATH B answer; path-a-skip-component.test.tsx runs the real effect in both directions plus the S24 case; the inverted, pre-S24 and no-skip mutants each fail",
      "portal git ls-remote origin: PROD c69b474716, DEV 99c6ae08c8; f2d2f17c is an ancestor of both (rc 0), and so is the positive control 98a98e70fb on PROD (rc 0) (this compile's read, 2026-10-05 ~05:4xZ-06:1xZ)"
    ],
    "remedy": "Done and on PROD: the tab's own PATH A read skips only on the account's own served PATH B answer, and a pin through the component discriminates the direction and the failed-manifest case.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v15",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v15"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-W7-S1",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The DB-b-20 folder's E3_SHAPE_RULING.json and BD_POPULATION_PULL_E3.json exist only untracked in the base checkout, so a worker worktree cannot run `run --go` against the ruling the script reads, and the ruling's bearer line ('one, minted once') is superseded by CTO batches 248-249.",
    "evidence": [
      "investigation row IRPT_DASHBD-W7-S1",
      "git ls-files --error-unmatch on both paths under org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~6/ at CLOUD HEAD 4e3b64b6ea: rc 1 (not tracked); both present on disk in the base checkout (this compile's read, 2026-10-05 ~05:4xZ-06:1xZ)",
      "CTO RULINGS batch 248 (re-mint through the 49F sign-in path) and batch 249 (one coordinator-minted shared bearer)"
    ],
    "remedy": "Commit both files to the DB-b-20 folder with the ruling's bearer line corrected to batches 248-249, so the record of the pull and the ruling the script reads are tracked; the row closes when both are tracked at CLOUD HEAD.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v15"
    },
    "closed": false
  }
]
```
