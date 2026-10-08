# IRPT_BCKEND -- round 65 ~Y L8/L9 compile and remediations (round label v78)

<sweep_watermark>2026-10-08T17:52Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-08 ~18:0xZ. L8 input:
`org/missions/D9/IRPT/IRPT_BCKEND/ledger/IRPT_BCKEND_ROUND65_Y_L8_COMPILE.md @87a95c6fca` (msg 1360). 1 of 1 order terminal:
`IRPT_BCKEND.TO-IB-yr-651` cancelled by issuer ruling (branch B of the release-2 pair), drained @3f64c8cd2c, 0 judgment criteria;
`round-close-check.py --round 65` reads MAY-CLOSE. Three rows graduate OPEN below. No row is dismissed, so no adjudication file is
minted. ARMED after this compile: S392 disarmed by ruling; S334 and W165-S2 unchanged.

This seat's reads (dell2, 2026-10-08 ~17:5xZ):
- `aws lambda get-function-configuration irpt-ycharts-generate` -> CodeSha256 `ZspX0qD2bCkF...` (release 1), LastModified
  2026-10-08T17:44:54Z (the rollback), Successful. No `irpt-ycg-release2` entry in `.open_deploys/`; its completion file is present.
- D2-W156-S2 holds on the code at HEAD. `_authz/served.py:905-922` passes `access.prospect_owner()` as the guard's owner for an
  internal subject. `_scope/interactive_access.py:123-137` builds that owner from `current()`, so `owner.principal_id` equals the
  actor's. `intake/uploads.py:241-248` sets `on_behalf` only when they differ. X-1's on-behalf branch is therefore unreachable on the
  served route as merged, and D2-W156-S1's grant question is moot until X-1 is recut.

S392 (`2.0.0_SA_COO~M2`, BLOCKING, ARMED) graduates below as well: the gate holds the slug until it is dispositioned. Its armed state
(the 2026-10-09 13:30Z default rollback) is disarmed by the CTO's AMENDMENT 2 @a0d336b0ab (HOLD), counter-signed @9cf13be89a; every
weekday fire now runs under the per-fire NO-WORSE rule. e56 acceptance 1 stays NOT MET; its root cause goes to dell1 ~M1.

```json
[
 {
  "id": "IRPT_BCKEND-D2-W156-S1",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "cloudops-dell2-agent-user is denied kms:Decrypt on irpt-requests' CMK, so a release-2 admit's UPLOAD# record could not be read back or deleted from this seat; the order stopped before after-reads 1-5 and rolled back to release 1.",
  "evidence": [
   "investigation row IRPT_BCKEND-D2-W156-S1 (0.9.0_WK_IRPT_BCKEND~156)",
   "org/missions/D9/IRPT/IRPT_BCKEND/ledger/IRPT_BCKEND_ROUND65_Y_L8_COMPILE.md @87a95c6fca",
   "live irpt-ycharts-generate CodeSha256 ZspX0qD2... at 17:44:54Z (3.0.0_SA_CVO read, 2026-10-08 ~17:5xZ)"
  ],
  "remedy": "Moot until X-1 is recut (D2-W156-S2). The recut's release names who reads back and deletes the admit's record, and with which grant, before any write.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v78",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v78"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W156-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "On the served analysis-inputs route the guard's owner for an internal subject is built from the actor, so uploads.create() never takes X-1's on-behalf branch; the unit tests pass an advisor-derived owner the live guard never builds.",
  "evidence": [
   "investigation row IRPT_BCKEND-D2-W156-S2 (0.9.0_WK_IRPT_BCKEND~156)",
   "_authz/served.py:905-922, _scope/interactive_access.py:123-137, intake/uploads.py:241-248 at dell2 CLOUD HEAD (3.0.0_SA_CVO read, 2026-10-08 ~17:5xZ)"
  ],
  "remedy": "Recut X-1 so the served route resolves the on-behalf owner (the advisor the filer acts for) before create(), with a test that drives served.py rather than handing create() an owner.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v78",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v78"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-S392",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "The first Holdings fire on the SC-e-62/e56 r4 bundle landed 1 of e56's 5 tabled 49financial class moves; 233 of the 238 precheck CUSIPs serve by name or ticker basis, not their CUSIP row. By the COO half's own rule 49financial took Branch B (rollback by 2026-10-09 13:30Z by default). Served totals reconcile to 0.00 and unclassified is 167 at pin and served, so nothing served is worse than the pin.",
  "evidence": [
   "investigation row IRPT_BCKEND-S392 (2.0.0_SA_COO~M2)",
   "org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SECCLASS_E62_E56_IR_BUNDLE_CTO_HALF_20261007.md AMENDMENT 2 @a0d336b0ab: HOLD Branch B; per-fire NO-WORSE rule from 2026-10-09; e56 acceptance 1 stays NOT MET",
   "COO half counter-signature @9cf13be89a (13:30Z default withdrawn) and AMENDMENT 2.1 @0210ff5d27"
  ],
  "remedy": "Disarmed by ruling: no default rollback; each weekday fire is graded by the NO-WORSE rule (per-fire pin, four checks, Branch B per failing firm) with one record line per fire in the COO half. Still OPEN: the CUSIP row reaching the served run (local precheck vs served run disagree), routed to dell1 2.0.0_SA_COO~M1 via 0.0.0_AB_MSTR~DELL2; the fix ships under its own pair.",
  "owner": "2.0.0_SA_COO~M2",
  "round": "v78",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~M2",
   "round": "v78"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~M2",
   "at": "2026-10-08T17:20:29Z"
  }
 }
]
```
