# ADVI_COTBKF: remediations, round 44

<sweep_watermark>2026-10-09T14:55Z</sweep_watermark>

Round 44 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~14:5xZ. L8 input: the round 44 packet @0e628a61f8 (msg 3508); CB-ar-1
complete, 0 judgment criteria, MAY-CLOSE, no worker rows. This seat's row ADVI_COTBKF-D2-S67 graduates OPEN, round label v45: the pin check (and an
older prices prefix) builds S3 keys by splitting literals past the naming gate, against rule 30. ARMED: 0.

```json
[
 {
  "id": "ADVI_COTBKF-D2-S67",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "commonwealth_cot_price_rewrite.py builds two S3 keys by splitting literals so the commit-time naming gate cannot read them: PFX = '/'.join(['silver', 'pri' + 'ces']) (:76) and PIN_KEY = '/'.join(['code', 'gold', 'scopes' + '.json']) (:251, commented 'joined: the naming gate refuses the typed literal'). CLAUDE.md rule 30: a builder refusal is a missing registry row to add, never a hand-typed workaround; a split literal is a typed address the gate cannot see.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S67",
   "data/assets/scripts/silver/commonwealth_cot_price_rewrite.py:76",
   "data/assets/scripts/silver/commonwealth_cot_price_rewrite.py:251"
  ],
  "remedy": "Take both keys from lib/opal_naming address() (adding the registry rows the builder refuses on: the prices family and the code/gold pin), drop the split literals, and have the issuer state in its next order face that a gate refusal is answered with a registry row, never a joined literal.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v45",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v45"
  },
  "closed": true
 }
]
```
