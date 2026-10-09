# IRPT_BCKEND -- round 35 ~M remediations (round label v36)

<sweep_watermark>2026-10-09T02:42Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-09 ~02:4xZ. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/ledger/IRPT_BCKEND_ROUND35_M_L8_COMPILE.md @7edd214b96`
(msg 2218). TO-IB-m35-351 complete; drain 49cecd310d in box/dell2 HEAD; port test 6 passed (this seat's run). The packet filed 0 rows; this
seat files D2-S20 from its own staged-zip check and graduates it here. Committed under the audited per-compile override the laptop CTO
approved (msg 107640 via MSTR msg 2188) for lanes measured all-terminal: every ~M order (TO-IB-m*) reads complete or superseded at HEAD.

```json
[
  {
    "id": "IRPT_BCKEND-D2-S20",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Release 6 of irpt-ycharts-generate will FAIL the symbol-closure check on a false positive: round 35's port keeps a `try: from holdings_publication import HoldingsPublication / except ImportError: from publication import HoldingsPublication` fallback, and in that function `publication` is ycharts' own module, which defines no HoldingsPublication, so symbol_closure.py flags the fallback line even when the right module is staged.",
    "evidence": [
      "infra/aws/lambda/investor-reporting/holdings/holdings_publication_port.py:8-11 (the fallback)",
      "infra/aws/lambda/investor-reporting/ycharts/extract/publication.py (classes: PublicationRefused only; no HoldingsPublication)",
      "this seat's synthetic zip staged as release 6 stages it (the port, holdings/publication.py AS holdings_publication.py, ycharts' publication.py): org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r71/symbol_closure.py -> 'MISSING holdings_publication_port.py:11 imports HoldingsPublication from publication', modules=3 pairs=2 missing=1, FAIL"
    ],
    "remedy": "Either drop the fallback in the copy irpt-ycharts-generate stages (import holdings_publication only, so a staging miss fails loud at build), or teach symbol_closure.py to skip an ImportFrom inside a try whose handler catches ImportError when the try branch resolves. Prove it with the same synthetic zip reading PASS before release 6's build.",
    "owner": "2.0.0_SA_COO~Y2",
    "round": "v36",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y2",
      "round": "v36"
    },
    "closed": false
  }
]
```
