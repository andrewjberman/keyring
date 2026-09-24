# AMGT_RESAPP: CVO disposition of the pre-existing test-rot rows (Z-S222, Z-S223, Z-S224)

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-22T16:0xZ at HEAD after `9c5beff60d`, LOCAL on SITEZ.
`2.0.0_SA_COO~Z` filed these three rows at the round-28 cut (14:30Z). A re-census after ADJUDICATION_v31 found them
still UNDER_INVESTIGATION. They are dispositioned here so the channel reads 0 open.

**Re-measured by this seat at HEAD** (pytest, per file, and a collect-only run over the directory):

| row | file or scope | result |
|---|---|---|
| Z-S222 | `integrations/bloomberg/research/tests/test_fye_join.py` | 3 failed, 2 passed |
| Z-S223 | `integrations/bloomberg/research/tests/test_latest_stamp_raw_pair.py` | 1 failed, 5 passed |
| Z-S224 | `integrations/bloomberg/research/tests/` collected as a directory | errors at collection, e.g. on `test_consumer_wiring.py` |

All three are pre-existing, and none was caused by round 28.

**GRADUATED, not dismissed.** The failures do not harm served output today, which is why they are INERT. But they
have a cost. While a suite fails at the baseline, or cannot be collected as a directory, a NEW regression in those
files reads the same as the old red. Round 28 worked around it with file-level "no NEW failures" bars (CTO msg
24263). That is a workaround the next cell has to remember, not a guard. The fix is one small code cell of
`2.0.0_SA_COO~Z`'s:
- point the three fye tests at the current bucket or a stub;
- fix the one stale-stamp test;
- make the two files import a symbol that exists, so the directory collects.

Remediation rows are owed at L10.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S391",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T16:05Z",
    "one_line": "GRADUATED: Z-S222 (test_fye_join 3 failed on a retired bucket), Z-S223 (test_latest_stamp_raw_pair 1 failed), Z-S224 (the bloomberg research tests directory does not collect) -- re-measured at HEAD; pre-existing and INERT, but a red baseline masks a new regression, so each is a cleanup cell.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "pytest integrations/bloomberg/research/tests/test_fye_join.py at HEAD: 3 failed, 2 passed.",
        "pytest integrations/bloomberg/research/tests/test_latest_stamp_raw_pair.py at HEAD: 1 failed, 5 passed.",
        "pytest --co integrations/bloomberg/research/tests: ERROR collecting test_consumer_wiring.py."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A suite a cell's bar reads is green at its baseline, and collectable as a directory.",
    "world_is": "Three files are red or uncollectable before any change, so bars must be written as file-level 'no NEW failures'.",
    "notes": "Owner: 2.0.0_SA_COO~Z, one cleanup code cell, cut at the next code round. Remediation rows owed at L10.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S222",
      "AMGT_RESAPP-Z-S223",
      "AMGT_RESAPP-Z-S224"
    ]
  }
]
```
