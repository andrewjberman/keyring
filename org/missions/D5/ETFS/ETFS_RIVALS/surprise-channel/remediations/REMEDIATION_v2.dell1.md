# ETFS_RIVALS -- round 30 remediations (dell1 fabric): the L8 compile the L10 slug carries

Author: 3.0.0_SA_CVO~RV, 2026-10-15 ~19:55Z. Graduated at the round-30 L9 (`adjudications/ADJUDICATION_v3.dell1.md`, rows
D1-C-S21 and D1-C-S22). Covers the investigation rows filed after `REMEDIATION_v1.dell1.md` (round 28) in
`investigations/INVESTIGATION_v1.dell1.md`. Watermark: the last row read is ETFS_RIVALS-D1-S18 (surfaced 2026-10-15T18:29:37Z,
commit 67884d5199). Under the L10 slug rule (class BLOCKING or hazard_standing ARMED), 4 of the rows since round 28 gate the
slug. Their rows are below. The slug itself is 2.0.0_SA_COO~RV's, by the CTO's ruling @f8191183f6.

Round-30 J1 grades: MET for RIV-xa-2 (D1-C-S21; the production URL was not exercised) and MET as written for RIV-xc-2
(D1-C-S22; a reader still sees two template families that frame_of v2 splits).

**OPEN: D1-S16.** Its fix is a round-31 cell, and the project parks after round 30. So the hazard has a disarm (a manual
read per tick) and no carrier for its fix. On 10-15 the 10:50Z and 12:50Z reads were missed, and one late read found 0
inferred objects. The CTO decides before the park: cut the one fix cell, name a standing owner for the reads while the
project is parked, or stop the live lookup.

Noted, gating nothing (unarmed OBSERVATION): W39-S1, W39-S2, W40-S2, W41-S1 (a condition of the site-Z xe-1 deploy, which
is not in this pin), D1-S17 (CGIC and SCHY not updated on 10-15 after the failed 11:04Z capture) and D1-S18 (TXUE's two AI
items Grounding FAIL). Carried from v1 and not re-read here: Z-S81 and D1-S2 (owner was 2.0.0_SA_COO~V1, now the ~RV
lane) and D1-S15 (1.0.0_SA_CTO).

```json
[
  {
    "id": "ETFS_RIVALS-D1-W42-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "RIV-xf-1 AC2 expected 13 funds in the sinkless holdings plan, while request_plan without a sink plans only the 7 bloomberg_primary funds. The issuer's premise was wrong, not the build.",
    "evidence": [
      "investigation row ETFS_RIVALS-D1-W42-S1",
      "commit 072910b11e (xf-1 AMENDMENT 1: AC2 reads the 7 bloomberg_primary funds) and 6fd84470c7 (the check)",
      "commit 6e8f886abc (RIV-xf-1 complete, instance VALID: AC1 4, AC2 1, AC3 1, AC4 20 passed)"
    ],
    "remedy": "The criterion reads the plan the code is specified to produce. Done by AMENDMENT 1.",
    "owner": "2.0.0_SA_COO~V1",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~V1",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-D1-W40-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "RIV-xe-3's union reader read dramatic_move's actions-void-* objects as rows and never applied them, so a void whose action sat in an older pull came back into G5.",
    "evidence": [
      "investigation row ETFS_RIVALS-D1-W40-S1",
      "commit d8ae1862ca (xe-3 AMENDMENT 1: the union honours void records; AC4) and 496efb8e93 (RIV-xe-3 complete, instance VALID, AC4 1 passed)",
      "pin bytes, read by content: `git show ea0e5025ac:data/etfs/scripts/rivalfunds/gold_trade_schedule.py` :993-1011 skips void uris (ps._is_void_uri) and applies ps._voids. Control: base 9a1ce314dc's file has 0 'void' tokens",
      "TO-APPLY-R30 complete @38300e3a5d: the daily Lambda is live at pin ea0e5025ac from 2026-10-14T14:53Z (get-function LastModified 2026-10-14T14:53:21Z, read by this seat)",
      "D1-S16 reads (deliverables/2.0.0_SA_COO~RV/round30/D1_S16_DISARM_READS_RV.md): 0 actions-void-* objects in the live store, so the hazard never fired"
    ],
    "remedy": "The union reader honours voids through price_series' own reader, not a copy. Deployed at pin ea0e5025ac.",
    "owner": "2.0.0_SA_COO~V1",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~V1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~V1",
      "at": "2026-10-14T14:53:21Z"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-D1-W40-S3",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "xe-3 AC4 spelled its void's security_id in lower case. price_series._norm_key is case-sensitive, and no producer can write that spelling, so the check could not pass on a correct build.",
    "evidence": [
      "investigation row ETFS_RIVALS-D1-W40-S3",
      "commit e9a637d4c9 (AC4 names the void by the stored key spelling; base 4 failed 1 passed, on the worker build 5 passed)",
      "commit 496efb8e93 (RIV-xe-3 complete; row W40-S3 ruled, check corrected)"
    ],
    "remedy": "The check names the void as a producer stores it. The readers were not case-folded, so load_actions honours the same voids price_series does.",
    "owner": "2.0.0_SA_COO~V1",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~V1",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-D1-S16",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "An inferred split (actions-inferred-*) and Bloomberg's row for the same split differ in raw_event_type, so both survive the de-dup in price_series._actions and in the r30 union reader. One split can then adjust a series or a G5 flow twice (CTO C1, msg 5612).",
    "evidence": [
      "investigation row ETFS_RIVALS-D1-S16",
      "CTO half ledger/NEVER_WIDEN_R30_DEPLOY_CTO_HALF.md @35d1f02bc3, condition C1",
      "deliverables/2.0.0_SA_COO~V1/round30/D1_S16_DISARM_READS.md (from 2026-10-14) and deliverables/2.0.0_SA_COO~RV/round30/D1_S16_DISARM_READS_RV.md: on 2026-10-15 the 10:50Z and 12:50Z reads were not taken. The one LATE read (~18:2xZ) found 12 plain objects, 0 inferred and 0 void",
      "round-31 cell staged @3d19137d09 (Bloomberg wins on security_id, event_type, ex_date in both readers), not cut",
      "the CTO's ruling @f8191183f6: after the round-30 analysis the project PARKS, and no round 31 is cut without Andrew's word"
    ],
    "remedy": "The staged round-31 cell: Bloomberg wins on (security_id, event_type, ex_date) in load_actions and price_series. Until it deploys, a seat lists gold/corporate_actions/ before each reader's run and voids any actions-inferred-* object the same tick.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v2"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~RV",
      "at": "2026-10-15T18:29:37Z"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~RV
