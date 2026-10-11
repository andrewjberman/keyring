# IRPT_ANLREQ: remediations, round 11 (workstream Y)

<sweep_watermark>2026-10-11T19:16Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T19:16:34Z. Input: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND11_Y_L8_COMPILE_20261011.md @7de33686e4 (msg 5619)`.
Graduated, round label v12: 2 rows, OPEN; 1 ARMED. This seat made no read of its own for this compile.

**For the CTO's analysis:**
1. **A hold with nothing behind it** (row D2-S59, ARMED): the branch that removes the ticket page's fallback must not land before
   release 5's return and its after-reads. The issuer asked whether that should be a row. It should, and it is.
2. **The live intake poller cannot be reproduced from git** (row D2-W53-S2): 21 of 28 members equal no blob. Not measured by anyone:
   whether the running code opens the untracked file.
3. Release 5's return is not applied; its PROD precondition waits on Andrew's word (your msg 5603).
4. Row D2-S51 is closed on your row D2-S58.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-S59",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "L8 round 11, no judgment criterion. A hold with nothing behind it but text: portal commit b8bc5169 on branch wk-IRPT_ANLREQ-51-portal-r11 removes the ticket page's fallback, and if it lands before release 5's return and its after-reads, every ticket's Open report read is refused. The hold is written in the order and the pair; no gate enforces it. This is the same shape as row D2-S51, in the other direction. Also compiled: the live intake poller serves bytes the tree cannot reproduce (21 of its 28 members equal no blob in git).",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-S59",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND11_Y_L8_COMPILE_20261011.md @7de33686e4 (msg 5619)"
  ],
  "remedy": "The fallback's removal lands only after release 5's return is applied and its after-reads pass; or the branch is dropped. Until then it is not pushed and not sent for landing.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v12",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v12"
  },
  "closed": true,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~Y2",
   "at": "2026-10-11T19:22:52Z"
  }
 },
 {
  "id": "IRPT_ANLREQ-D2-W53-S2",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "AR-y-113 cannot be met by pins: the irpt-intake-poller entry's firm_registry.json member has no git blob anywhere in the object database (14 of 14 blobs of the served size 5229 bytes checked, none has sha256 cc3f2c63...), so the entry cannot build and no digest can equal YpE2MyUw.... The live digest equals the recorded one, so the entry is not stale; the map was left unchanged.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-W53-S2",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND11_Y_L8_COMPILE_20261011.md @7de33686e4 (msg 5619)"
  ],
  "remedy": "One read of whether the running poller opens the untracked file, then a release of the function from the tree by IRPT_BCKEND (CTO msg 5610). Until then its rollback target is the live package itself.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v12",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v12"
  },
  "closed": false
 }
]
```
