# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 05Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 05:00Z | L8 | 22 | x-3: the r-1 ad-hoc QA fire, LastTaskResult 0 on branch 1; ledger closed (`c8ad550b64`). Acceptance is the 13:00Z fire. |
| 05:0xZ | L7 | 22 | x-1 re-graded, merged `a51adaeeda`; x-2 re-graded, merged `98b0cb59c4`; drain hygiene 193 passed |
| 05:08Z-05:12Z | L8 | 22 | before-states measured; the served-acts COO half `5757501e0d`, with the (c2) SA branch unsigned; the census finding: 9612 of 37746 served figures UNRESOLVED (9176 with no field family) |
| 05:17Z | -- | 22 | CTO half `951082ff8d`: act 1 and act 2 a/b/c1 signed; c2 refused, with a `--no-sa-fallback` cell for round 23 |
| 05:18Z-05:43Z | L8 | 22 | ONE ledger entry (`0794dfd10f`). Leg M: the map commit `0982a0767d` (exactly 8 entries). Leg R: re-derive 15/1/1 flips, 0 value moves. Leg D: 95 puts, 190 -> 285. |
| 05:4xZ | L8 | 22 | **Self-caught defect:** leg D ran concurrently with leg R, so the 9433 and 8035 dossiers were built from pre-flip blocks. The 2-put refresh was asked and signed as AMENDMENT 1 (`921b124dea`), gated on an inputs census. |

## Rulings and corrections this hour

- The CTO withdrew round-21 ruling 3's "2 reads" on this seat's measurement (all 8 rest on 1 read).
- The CTO's condition for next time: finish act 2 before act 1 starts, when one act's inputs are the other's outputs.

## Compiler Tools

- `deploy_ledger.py`: 2 entries this hour (the r-1 register, closed; the served acts, V open).
- `m_apply.py` (issuer): the pre-image diff of the committed map.
- The figure-by-figure block diff (issuer): per block, flips, value moves, other units, `filled_by_sa`.
- The unresolved-unit census over 100 served blocks.
- Gap: two long reads run concurrently (the verify re-read and the gate census) slow each other; sequence them.
