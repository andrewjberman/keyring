# LGIC_BLANKFIX -- remediations, round 4

<sweep_watermark>2026-10-08T01:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-08 ~01:0xZ. Graduated at this compile (ADJUDICATION_v3.md): 1 row, INERT, not closed.
Carried open from REMEDIATION_v1.md: W2-S2 (the test's load-time override of one worked case).

```json
[
  {
    "id": "LGIC_BLANKFIX-S5",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The proof-of-spec checker raises and exits 2 when a proof instance names a directory as an artifact path. A crash is not a verdict: an issuer cannot tell a refused instance from a broken tool, and a worker got past it by listing 13 files one by one.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 20e21c5078 (34 rows, 0 ARMED) row S5",
      "adjudication row LGIC_BLANKFIX-C-S12"
    ],
    "remedy": "P2. The checker's owner makes a directory path a stated refusal (or a stated acceptance) with rc and wording of its own, and adds the case to the checker's self-test. Done when a proof instance naming a directory gets a verdict line and no traceback.",
    "owner": "1.0.0_SA_CTO",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v5"
    },
    "closed": true
  }
]
```
