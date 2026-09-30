# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 12Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 12:00Z | L8 | 24 | z-1 served act measured on a temp map: 84 entries, 10 fields; excluding BP/NG, 553 figures to measured and 49 still, which equals the projection |
| 12:0xZ | L7->L8 | 24 | z-4 re-graded and merged `6d6d142812`, as below |
| 12:09Z | L8 | 24 | rows `Z-W4-S6`..`S9` ruled `5bb98d6f80` |
| 12:18Z | L8 | 24 | COO half of the z-1 act pair `ab84e2b6df`; asked of `1.0.0_SA_CTO~Z` (27133) |
| 12:25Z | L8 | 24 | CTO half `4acf8806ce` SIGNED (4 conditions) |
| 12:28Z-12:40Z | L8 | 24 | the act-start gate passed; legs a-c closed, as below |
| 12:44Z | L8 | 24 | leg d started (27 dossiers) |

**z-4 re-grade:**
- AC1 `sites 14 encoded 14 raw 0`; AC2 76 passed; posc VALID; the `crosswalk.py` diff is a marker comment only;
- no working-tree scheduled task runs these producers;
- the channel conflict was resolved structurally (125 rows);
- the drain tip reads 394 passed, and `field_map.json` is clean.

**The m2 measurement** (`checks/round24/m2_measure.py`), per figure through the producer's own readers:
- 565 unit changes, 553 of them to measured, and 0 measured-to-other;
- 115 sign changes: 103 UNRESOLVED -> POSITIVE, 12 reason text, 0 contradicting their value.

**The act-start gate:** the closure diff `04b89561ce..HEAD` read empty, and the map equaled its committed bytes.
- Ledger `amgt-corpus-r24-unit-closures` opened `a974d07eb1`.
- **Leg a:** 84/10/0/0/0, exact.
- **Leg b:** map `6caac02338`, after waiting out two peer merges.
- **Leg c:** 28/28 blocks match, with 565 unit and 115 sign changes as expected and 0 value, case or other changes. The derive
  `vintage` stamp was first counted as "other" and "case", then diagnosed field by field and excluded.

## Compiler Tools

- `y4_measure.py` (round 23) re-used; new: `m2_measure.py`, `c_verify.py`.
- Gaps:
  - the first `c_verify` counted the derive timestamp as content;
  - `safe-commit` refused twice during peer merges (waited, never touched).
