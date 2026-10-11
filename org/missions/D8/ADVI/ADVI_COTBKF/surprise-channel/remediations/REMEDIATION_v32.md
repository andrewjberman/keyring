# ADVI_COTBKF: remediations, round 46

<sweep_watermark>2026-10-09T15:44Z</sweep_watermark>

Graduated at round 46's L9 (ADJUDICATION_v35.md), round label v47: 2 rows, OPEN.

```json
[
 {
  "id": "ADVI_COTBKF-D2-S71",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The cot price writer's ticker_overrides went from FAIL-CLOSED to FAIL-OPEN: the base did 'from lib.ticker_overrides import YF_OVERRIDES, TICKER_CORRECTIONS' (an import error stops the run); _load_ticker_overrides() now returns empty dicts plus a WARN when the file is unresolved. A redeploy that misses ticker_overrides.py beside the writer (the deployed mirror holds it at code/gold/lib/, not code/gold/) would silently drop 757 overrides and 1 correction and price those tickers wrong.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S71",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_46_DRAIN_END_20261009.md @f723ea78df (msg 3587)"
  ],
  "remedy": "Before the writer redeploy: restore the fail-closed load (an unresolved ticker_overrides raises and stops the run, never empty dicts), with a test that the run stops when the file is absent; and ship ticker_overrides.py beside the writer, registry first (ADDENDUM 18).",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v47",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v47"
  },
  "closed": true
 },
 {
  "id": "ADVI_COTBKF-D2-W73-S3",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The 7 pre-existing source_firm tests copy only the writer (+ scopes.json) into a temp dir with no ticker_overrides beside it, so a hard failure on an unresolved ticker_overrides would break them; the writer instead applies no YF overrides/corrections, prints WARN, and stamps the input absent (census NOT-CLEAN). In production this would silently drop 757 overrides + 1 correction from the ticker mapping if the file is not shipped beside code/gold.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W73-S3",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_46_DRAIN_END_20261009.md @f723ea78df (msg 3587)"
  ],
  "remedy": "Carried by the row above: the redeploy pair names ticker_overrides.py beside the writer and reads back its 757 overrides and 1 correction from the deployed run.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v47",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v47"
  },
  "closed": true
 }
]
```
