# ADVI_COTBKF decomposition -- ROUND 97 (issuer 2.0.0_SA_COO~C1 on dell1; drafted 2026-10-16) -- carry the Yahoo source into the served-move build, relabel, re-measure

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** the CTO's ruling (msg 6530, 2026-10-16 ~05:49Z): "Round 97: carry the substitution flag point by point from the as-traded basis; relabel; re-measure on dell2's data. Delta 0 must still hold on every pre-existing column, and the label count must equal 1,049,193 Yahoo points." Reason (the CTO): a NOT_YAHOO label on Yahoo-sourced points would serve a false claim; Andrew's `3adb` word (`ANDREW_DIRECT_20261015_205xZ_CALLS_BCCC_3ADB_BBD5.md`) kept Yahoo-priced days only if they are labelled interim.

**What round 96 found (CB-cr-1, @26f2781a61).** The served tables equal a rebuild on every pre-existing column (3 of 3), but every `use_class` and `porting_verdict` label reads `NOT_YAHOO`. Cause, read by the issuer: the served run `r34` predates the per-point `source` column. `commonwealth_daily_valuation.py` `write_prices` (HEAD) writes `source` into `security_day_price.parquet`; the r34 file carries `cusip, date, price, store` only. The builder's `yahoo_priced` reads `source` and reads `None` as not Yahoo. The as-traded substitution (`as_traded_store`) keeps the points' own `yahoo_finance` / `linear_interpolation` labels, so a run made with the current code carries them. **No code edit is needed: the flag is carried by re-running the regrade at the served settings with the current code.** The recorded command is `deliverables/0.9.0_WK_ADVI_COTBKF~129/RETURN_CHANGE.md` section 2 (its baseline leg reproduced the served returns: 0 differing); the split store is read at the served instant `2026-10-09T11:52:52Z` (`SPLIT_STORE_PIN.json`), the Yahoo cache is the pinned 3,580 files (`PRICE_CACHE_PIN.json`).

**Count note for the CTO's equality.** 1,049,193 is a count of ticker-days (`points_replaced`, r34 `price_basis.json`). The tables label account-holding-days, account-days and account-months, so their label counts cannot equal it. The cell proves the equality at the grain it holds: the as-traded price input carries exactly 1,049,193 `yahoo_finance` points with `basis=as_traded_close`, and the labelled rows of `account_day_value` equal its rows whose `price_source` names a Yahoo source. Both are measured, neither assumed.

**Rule 24.** Domain: making the served-move build label what it prices. Subtraction: the regrade at the served settings with the current code, the build, the control against the three served tables, and the label counts and consistency -> `CB-cs-1`. Uncovered here by design: the signed pair, the apply (a CloudOps seat) and the CVO's grade.

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-cs-1` | on dell1, re-run the as-traded regrade at the served settings with the current code into a NEW data dir (the per-point `source` is written), rebuild the three tables from it at the served settings, prove every pre-existing column equals the SERVED one row for row (`run_commit` excluded and counted), and count the labels per table with their consistency against `price_source` and the price input's 1,049,193 Yahoo points; stop and record if the control fails | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~187` |

**Fan-out (to state at the cut):** `1 of 1 chains, cap 8`.
