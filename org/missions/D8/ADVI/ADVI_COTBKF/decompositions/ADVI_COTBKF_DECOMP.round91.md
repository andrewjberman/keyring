# ADVI_COTBKF decomposition -- ROUND 91 (issuer 2.0.0_SA_COO~C1 on dell1; drafted 2026-10-15) -- close the last armed guard row: does the as-traded Yahoo close reach the served label?

**Status: DRAFT -> ISSUED in one issuance.**

**Numbering.** The CTO (msg 6238) asked for the `commonwealth_daily_valuation.py` L329 guard in "your next round, BEFORE the CRM window"; the second CRM window waits on Andrew's exact key and joins whichever round is next when the key arrives. This is round 91; the CRM window is then round 92 (not the "round 91" of my earlier messages).

**Cut on:** CTO msgs 6237/6238 and Andrew's call `3adb` (a), VERBATIM from the record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_205xZ_CALLS_BCCC_3ADB_BBD5.md` @cb7075dd11: "Call 3adb: yeah sure." (option (a), the swap: served Yahoo-priced days for securities held in V2 stay, labelled; each security's points are replaced the day its Bloomberg series lands; nothing new is drawn from Yahoo for active names). Armed rows: `ADVI_COTBKF-D1-W173-S3` and `D1-S2` (this seat's), which say the as-traded valuation reads a Yahoo Close cache with no `use_class` filter.

**What the code already does (read by the issuer at HEAD 7608f2c550; the cell must MEASURE it, not assume it).** `commonwealth_daily_valuation.apply_price_basis` (L303) substitutes Yahoo Close points for the store's `yahoo_finance` points, keyed by ticker, and `as_traded_store` (L258) keeps each replaced row's `source` label as `yahoo_finance` (it copies the row and changes `price` and `basis` only); re-derived `linear_interpolation` rows keep their label too. `commonwealth_fwd3_serve.use_labels` / `porting_labels` label every holding row priced on a `YAHOO_SOURCES` label by its security's class (round 89, `7608f2c550`). If the served holding frame carries `source`, then an as-traded Yahoo price is already labelled `NOT_FOR_ACTIVE` for an active security, and under call `3adb` (a) that is exactly the required behaviour: the day stays, labelled. The armed row would then be answered by a test, not by new code. If it is NOT so, the cell fixes it.

**Rule 24.** Domain: msgs 6237/6238 and call 3adb. Subtraction: the L329 reader -> CB-cm-1; the L574 and sweep_regrade L1602 split-ratio reads -> excluded by the CTO's ruling (msg 6175: corporate-action facts, not prices); the served move -> none (under (a) no value moves: the label only; the CTO's msg 6238 point 2: the served pair needs a per-account value DELTA of 0 plus the new label field, built only if a value would move); the per-account default-run data build -> not cut (nothing moves). Uncovered: none.

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-cm-1` | prove, on stubs that run the REAL `apply_price_basis` and the REAL served label path end to end, that a holding priced on an as-traded Yahoo close (replaced point and re-derived point) reads `NOT_FOR_ACTIVE` for a V2-held security and `INACTIVE_USE` for any other, that a point left on the store basis and never Yahoo reads `NOT_YAHOO`, and that the Yahoo-cache read itself has a fail-closed class; FIX the path only if a test fails; then state in a record the exact set of lines that read a Yahoo price into an account value, each labelled or not | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~181` |

**Fan-out (to state at the cut):** `1 of 1 chains, cap 8`.
