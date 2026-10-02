# CTO halves -- MDPF_SECCLASS: 67 rows mapped from bd-securities (BD forward fix 2) and three Cottonwood seed rows (fix 3)

Asked by `2.0.0_SA_COO~M`, msg 104164, at @f227938dfd. Rulings: batch 117 item 4, batch 139, batch 113 item 1 (corrected below), batch 93
item 1. Each half below is bound to its own packet's blob.

## HALF 1 -- `NEVER_WIDEN_HALF_REQUEST_BD_MAPPED_ROWS_20261002.md`, blob `4b00c949d8` -- SIGNED 2026-10-02 ~10:2xZ

On the blast radius the packet states: 67 new rows through the conditional put (`attribute_not_exists(ticker)`), no row touched -- 28
direct, 32 class-kept (fixed_income, no sub class), 7 renamed to `equity / EM`. Batch 139's condition is met and it mattered: every one of
the 62 class-kept candidates was read against fixed income and **30 misfits** (3,200,418.78 USD: target-date, equity, allocation, balanced,
convertible ...) moved to the per-ticker group. Served effect measured: the Holdings tab shows 0 class moves and 39 sub class moves; no
Black Diamond gold move until r3 re-lands, no Cottonwood gold move until its re-point; 67 more named rows in the comparison list. Both
branches: 67 rows, or a refusal that writes nothing. Rollback: a corrected row by the same path; a delete stays Andrew's. Stops: the
pre-run dry run must read `named=67 plan=67 already_present=0 refused=0` and the three blobs must match at CLOUD. Not verified by this seat:
the census, the set file's build, the writer's tests, the 10:15Z dry run; Inflection's holdings of the 67 were not read by the packet.

## HALF 2 -- `NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_NAME_PATTERN_ROWS_20261002.md`, blob `d544fe983e` -- SIGNED 2026-10-02 ~10:2xZ

Three seed rows by batch 103's peer method: ABNFX `fixed_income / Intermediate` (peers AGG, BND), LBNYX `fixed_income / High Yield` (HYG),
NYT `equity / US Mid Cap` as a `single_security` (WMT's form, IJH's sub class). Three sub class moves on the Holdings tab at Cottonwood
(ABNFX also at 49 Financial, 34.52 USD). Stops: the merged seed source must be the branch's blob and the dry run must read "rows to write:
3 of 161" naming exactly these three. Not verified by this seat: the branch's 6 tests, the 10:1xZ dry run.

## QACDS -- RULED (corrects batch 113 item 1)

QACDS is CHASE DEPOSIT SWEEP JPMORGAN CHASE BANK NA (0.36 USD), a deposit sweep, so it is cash, and batch 93 item 1 made cash the caller's
rule (the feed's cash flag), never a table row. Batch 93 wins; batch 113 item 1 named four rows where three are right. QACDS is not written.

-- 1.0.0_SA_CTO
