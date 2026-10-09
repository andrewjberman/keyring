# ADVI_COTBKF: remediations, rounds 47 and 48

<sweep_watermark>2026-10-09T16:08Z</sweep_watermark>

Rounds 47-48 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~16:0xZ. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUNDS_47_48_DRAIN_END_20261009.md @b80e9e58b4 (msg 3614)`. No judgment criterion; both MAY-CLOSE.
W72-S1 closed in place (REMEDIATION_v31). Graduated, round label v49: 2 rows, OPEN. ARMED: 0 (D2-S72 is latent while rps is empty).
Correction to this seat's round-41 grade: it measured the served bytes, not the import closure on the mirror; D2-S72 is that miss.

```json
[
 {
  "id": "ADVI_COTBKF-D2-S72",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The LIVE cot gold B_00 (code/gold/B_00.canonical_holdings.py, deployed round 41, VersionId hU7ZrZTD...) imports opal_naming INSIDE _ff_worker (served :1362-1365: sys.path to ../../../../lib, then 'from opal_naming import lookup', then a tree token from a ../../../../data relpath). The cot code mirror carries NO opal_naming and NO NAMING_SCHEMA.json anywhere under code/ (issuer census: 0), and code/gold/lib/ holds 16 keys without it. So the day schwab/silver/rps/ fills and _ff_worker runs from code/gold/, the gold run raises ImportError (fail-closed, not silent). Unreachable today (rps 0 keys vs a positive control, round 42 drain). The same gap blocks the planned writer redeploy (row W75-S1: the writer now imports opal_naming at module level).",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S72",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUNDS_47_48_DRAIN_END_20261009.md @b80e9e58b4 (msg 3614)"
  ],
  "remedy": "Before schwab/silver/rps/ fills: the live B_00 and the writer resolve the own firm from the pinned scopes.json beside each script with no run-time opal_naming import (the issuer's recommendation), or ship opal_naming and NAMING_SCHEMA.json in the mirror; and every code/gold/ deploy checks its module's import closure on the mirror, not only its bytes.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v49",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v49"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W75-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "build_canonical_prices_v2.py read its registry only beside the writer (round 42: no lib/ or repo registry path); sweeping its keys onto legacy_address() makes it import lib/opal_naming (and its registry files) at module level. Served from s3 code/gold/ with only the files beside it, the import fails.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W75-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUNDS_47_48_DRAIN_END_20261009.md @b80e9e58b4 (msg 3614)"
  ],
  "remedy": "Carried by D2-S72: the writer redeploy (ADDENDUM 21) does not ship while its module-level opal_naming import has no copy in the mirror.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v49",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v49"
  },
  "closed": false
 }
]
```
