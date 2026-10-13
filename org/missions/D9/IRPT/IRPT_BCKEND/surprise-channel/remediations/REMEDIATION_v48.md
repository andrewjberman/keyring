# IRPT_BCKEND: remediations, round 171 (workstream ~P)

<sweep_watermark>2026-10-13T04:13Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T04:13:00Z. Follows ADJUDICATION_v72. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_171_P_DRAIN_END_20261013.md` (ae247549bf, msg 6776). No judgment criterion.
Graduated, round label v172: 3 rows, OPEN; ARMED 2.
- D2-W348-S2 (ARMED, owner `1.0.0_SA_CTO~DELL2`): the holdings re-pin also turns on TARGET serving and narrows three enums. Branch A or B is the
  CTO half's.
- D2-W350-S1 (ARMED, owner `2.0.0_SA_COO~P2`): which fe-s-18 bytes are the truth.
- D2-W348-S1 (DISARMED, owner `2.0.0_SA_COO~P2`): the dead-path attribute mismatch, a repair cell later.
Still ARMED in v47: D2-W345-S3 (the temp-file leak: the fix is merged; the host bundle is not redeployed; the files on the host are
uncounted because the runner host is stopped).

```json
[
 {
  "id": "IRPT_BCKEND-D2-W348-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "The irpt-holdings schema re-pin carries more than the one optional account_id member the order describes: the built copy also admits two opt-in TARGET blocks that the function serves on include=target, and drops multi_asset from three asset_class enums. Build only; nothing uploaded or applied.",
  "evidence": [
   "investigation row D2-W348-S2",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_171_P_DRAIN_END_20261013.md"
  ],
  "remedy": "The irpt-holdings schema re-pin carries more than account_id: it admits the two opt-in TARGET blocks (so include=target starts serving them) and drops multi_asset from three asset_class enums. The CTO half rules Branch A (land as built, with the TARGET serving and the enum narrowing named as served changes, and the readers of those members read through) or Branch B (restore). Nothing applied.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v172",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v172"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~P2",
   "at": null
  }
 },
 {
  "id": "IRPT_BCKEND-D2-W350-S1",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "REFUSED per the order's refusal clause: fe-s-18/gen-fixtures.ts cannot reproduce the committed fe-s-18 maps. The committed maps are mutually inconsistent, and the HEAD generator rewrites a committed map before it throws.",
  "evidence": [
   "investigation row D2-W350-S1",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_171_P_DRAIN_END_20261013.md"
  ],
  "remedy": "The fe-s-18 committed maps are mutually inconsistent, and the HEAD generator rewrites a map before it throws. Decide which committed bytes are the truth, then repair the generator to reproduce them (with row D2-W346-S3, OPEN in v47).",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v172",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v172"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~P2",
   "at": null
  }
 },
 {
  "id": "IRPT_BCKEND-D2-W348-S1",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The irpt-holdings build (re-pin of the HoldingsSnapshot schema copy only) carries a pre-existing attribute mismatch that the r278 instrument reads on the BUILT zip and on the LIVE zip alike: the packaged served.py (pin 74a62fb) passes load_report_owner to enforce.Enforcer, whose packaged copy (pin 21eca74) has no such keyword. The order's refusal clause stops the release; nothing was changed.",
  "evidence": [
   "investigation row D2-W348-S1",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_171_P_DRAIN_END_20261013.md",
   "row D2-S123 (disarm evidence)"
  ],
  "remedy": "The pre-existing attribute mismatch in the staged pin pair (served.py at 74a62fb46c passes load_report_owner to an enforce.Enforcer that does not accept it), live and built alike, in irpt-holdings and irpt-directory-search (row D2-W349-S1 folds in). It is ruled a dead path and non-STOP (row D2-S123). The repair cell is the issuer's, later.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v172",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v172"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~P2",
   "at": "2026-10-13T04:13:00Z"
  }
 }
]
```
