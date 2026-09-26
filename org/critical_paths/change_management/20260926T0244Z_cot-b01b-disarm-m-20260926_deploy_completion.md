# Deploy Completion Record
**Date opened:** 2026-09-26T02:44:29.392351+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T024715Z
**Deploy:** Disarm: restore COT B_01b S3 to prior version (empty-prefix no-op) after the CLOUD push 079fbf7d8e auto-deployed the fixed script outside grant @930e0f3 (CTO msg 101088)
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D1 | s3-prefix | opal-data-cot code/gold/B_01b.classify_new_securities.py -> prior version jRtJ.LnIa1n06jeUVSV2jVF8spFVR.S4 | new latest version whose bytes equal jRtJ... (ETag eedfd1d1...) and read-back shows HOLDINGS_LOTS_PREFIX | s3api copy-object of versionId jRtJ.LnIa1n06jeUVSV2jVF8spFVR.S4 -> new latest nSr3.NM7HCW0e83wNvVPeWnSSm.sPf5M, ETag eedfd1d1c5deb0c7e9e9e6100bbd3f77 (= prior; prior bytes == e20b0990d5~1 source); read-back line 35/92 HOLDINGS_LOTS_PREFIX; displaced auto-deployed version PbDCWhVVLw9jXXqxRP2Fma3i2hrAuzmp (02:39:19Z, ETag 28b33a17...) retained; watermark gold/manifests/classify_watermark.json 404 = no upload ran | CLOSED 20260926T024640Z |

## Log

- 20260926T024429Z OPENED by 2.0.0_SA_COO~M with 1 leg(s)
- 20260926T024640Z LEG D1 closed: s3api copy-object of versionId jRtJ.LnIa1n06jeUVSV2jVF8spFVR.S4 -> new latest nSr3.NM7HCW0e83wNvVPeWnSSm.sPf5M, ETag eed
- 20260926T024715Z CLOSED -- all 1 legs proven
