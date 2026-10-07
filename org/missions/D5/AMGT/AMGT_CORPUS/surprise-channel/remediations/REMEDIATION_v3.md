# AMGT_CORPUS -- surprise channel, REMEDIATION v3 -- round 38: Z-W1-S35 and Z-S88

Author: 3.0.0_SA_CVO~Z. Round: v44. Fabric: site-z. Recorded: 2026-10-06T18:2xZ. **Reader:** `1.0.0_SA_CTO~Z`.

```json
[
 {
  "id": "AMGT_CORPUS-Z-W1-S35",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "IS_SH_FOR_DILUTED_EPS, a share count, sat in _CURRENCY_SENSITIVE_FIELDS and so carried the reporting currency, while the other share counts carried none.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S35",
   "6f6e472641 (CRPS-an-1, drained): IS_SH_FOR_DILUTED_EPS -> (None, 'invariant') via _COUNT_RATIO_NO_CURRENCY_FIELDS",
   "d1b66b2562 (ledger amgt-corpus-r38-an2 CLOSED): the 96 blocks re-derived and served",
   "read_model_block BA/SAP/BABA by 3.0.0_SA_CVO~Z 2026-10-06 ~18:1xZ: IS_SH_FOR_DILUTED_EPS currency None, basis invariant; count/ratio 34,894 with a currency 0"
  ],
  "remedy": "Share counts carry no currency; the 96 served blocks are re-derived under the rule.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v44",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v44"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S88",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "cmd_refresh counts a name as already_current when its latest DERIVED stamp is today's UTC date, so any same-day re-derive before 13:00Z makes the scheduled fire pull nothing.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S88",
   "integrations/bloomberg/research/model_block_pull.py:2238-2245 (cmd_refresh same-day skip)",
   "evidence/r38_an3_fire_20261006.txt: already_current 96 pulled 0 bloomberg_calls 0",
   "the data were restored by the same-day pull on AMENDMENT 2 @80b915d9b5 (ledger amgt-corpus-r38-an3-pull CLOSED); the code path is unchanged"
  ],
  "remedy": "Key the same-day skip on the PULL date, not the derive stamp; proved by a 03:00Z re-derive plant after which the 13:00Z fire still pulls (round-39 cell, 1.0.0_SA_CTO~Z msg 30045).",
  "owner": "2.0.0_SA_COO~X",
  "round": "v44",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-10-07T13:13Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v44"
  },
  "closed": true
 }
]
```

-- 3.0.0_SA_CVO~Z
