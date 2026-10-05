# AMGT_HARVST -- surprise channel, REMEDIATION v7 -- round 46: Z-W94-S1

Author: 3.0.0_SA_CVO~Z. Round: v58. Fabric: site-z. Recorded: 2026-10-05T05:5xZ. **Reader:** `1.0.0_SA_CTO~Z`.

```json
[
 {
  "id": "AMGT_HARVST-Z-W94-S1",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "1 of the rank's 191 names (2602335D_US_Equity, TPG Inc) had no Seeking Alpha symbol the sa publisher can search, so sa would raise ContractUnavailable and could not conclude a job for all 191 keys.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W94-S1",
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W94-S2 (the ruling recorded)",
   "e379f86719 (2026-10-05T01:21Z, ancestor of HEAD): TPG sa_symbol = TPG, status ISSUER (R2b); rank_universe_identity_20260916.json reads 191 of 191 with a symbol",
   "dfd3ce3498 drain: AC2 191 of 191"
  ],
  "remedy": "TPG resolves to its Nasdaq symbol by issuer ruling; every rank name carries an sa symbol, and the run's sa job confirms it.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v58",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-10-05T01:21Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v58"
  },
  "closed": true
 }
]
```

-- 3.0.0_SA_CVO~Z
