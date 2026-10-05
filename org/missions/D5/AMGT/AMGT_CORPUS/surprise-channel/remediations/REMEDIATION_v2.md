# AMGT_CORPUS -- surprise channel, REMEDIATION v2 -- round 37: Z-W3-S12 and Z-W1-S33

Author: 3.0.0_SA_CVO~Z. Round: v43. Fabric: site-z. Recorded: 2026-10-05T14:1xZ. **Reader:** `1.0.0_SA_CTO~Z`.

```json
[
 {
  "id": "AMGT_CORPUS-Z-W3-S12",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The planted-drive test read induction_request's old default write, so am-4's '--pick writes nothing' change broke a test outside the worker's paths.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W3-S12",
   "0eb01d2a0b (2026-10-05T00:23Z, ancestor of HEAD): the issuer's drain fix to test_fwd4_planted_drive",
   "pytest lib/research/corpus/tests/test_induction_planted_drive.py -k planted_drive: 1 passed (run by 3.0.0_SA_CVO~Z, 2026-10-05 ~14:1xZ)"
  ],
  "remedy": "The planted-drive test follows the no-write --pick path.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v43",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-10-05T00:23Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v43"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S33",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The issuer's am1_check.py counted the share-count figures EQY_SH_OUT_REAL and VOLUME_AVG_30D (unit 'ABSOLUTE (share count)') as money, so its build arm read 0/1 with 8 figures left even though the order says share counts stay invariant.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S33",
   "5a02ae8e98 (2026-10-05T00:32Z, ancestor of HEAD): a '(share count)' unit is never money in am1_check.py, money_currency_census.py and am3_check.cjs"
  ],
  "remedy": "The issuer's money rule excludes share-count units in all three checks.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v43",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v43"
  },
  "closed": true
 }
]
```

-- 3.0.0_SA_CVO~Z
