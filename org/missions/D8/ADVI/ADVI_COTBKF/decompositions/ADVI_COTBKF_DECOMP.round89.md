# ADVI_COTBKF decomposition -- ROUND 89 (issuer 2.0.0_SA_COO~C1 on dell1; drafted 2026-10-15) -- the use_class guard in the served returns, built with one switch

**Status: DRAFT -> ISSUED in one issuance, after round 88 closes.**

**Cut on:** `1.0.0_SA_CTO~DELL1` msgs 6161 and 6175 (round 89 = the four `use_class` guards; per SECURITY, no second price path; Yahoo split ratios are corporate-action facts and stay OUTSIDE the guard;
"whether already-served days are blanked now, or kept labelled interim until each security's Bloomberg series lands, is Andrew's reading of his own word" = call `dell1-20261015T194123Z-3adb`; "Build round 89 so both
branches are one switch. Apply the served move only after his answer, under its pair"; a fix that changes a served value (`fwd3_serve`) "goes under a never-widen pair that prices the move per account"). Source of the gap:
round 87's `CB-ci-2` record `deliverables/0.9.0_WK_ADVI_COTBKF~173/READERS_RECORD.json` (4 readers feed an account's value with no `use_class` filter) and row `ADVI_COTBKF-D1-W173-S3` (ARMED, disarm owner this seat)
with its standing statement `D1-S2`. Andrew's word, VERBATIM: "Active accounts should get BBG pricing exclusively, inactive accounts are fine with yahoo finance." PRD v0.11, no addendum.

**What the four sites become, after the CTO's rulings (stated so no cell is cut for a reader the ruling removed):**
| site | ruling | cell |
|---|---|---|
| `commonwealth_daily_valuation.py` L329 (the as-traded Yahoo close substituted into account-day values) | in the guard | `CB-ck-1` |
| `commonwealth_daily_valuation.py` L574 (Yahoo split RATIOS) | OUT of the guard: corporate-action facts, not prices (msg 6175 point 2) | none |
| `commonwealth_sweep_regrade.py` L1602 (the same split-ratio read) | OUT of the guard, same ruling | none |
| `commonwealth_fwd3_serve.py` L687 (the index read for the `porting_verdict` label only) | in the guard: the served tables gain the `use_class` label and the switch; the SERVED apply waits for Andrew's answer and a pair | `CB-ck-1` (build) |

**Rule 24.** Domain: the two CTO messages. Subtraction: guard for the as-traded price read -> CB-ck-1; the served label and the one switch -> CB-ck-1; the per-account pricing of the move for the pair -> CB-ck-2 (a read of what each branch would change, counts only); the splits sites -> excluded by ruling; the served apply -> not this round (Andrew's call 3adb, then a pair). Uncovered inside this project: none.

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ck-1` | `commonwealth_fwd3_serve.py` appends a `use_class` label (LAST column) to the three served tables the way `porting_verdict` is built, and takes `--yahoo-active-policy interim\|blank` (default `interim`: values unchanged, label added; `blank`: every holding priced on a Yahoo-sourced price whose CUSIP is NOT_FOR_ACTIVE is blanked through the existing `--hold-cusips` mechanism); the manifest records the policy and the class branch; local build only, no S3 write | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~178` |
| `CB-ck-2` | the move priced per active account under each branch: counts of account-days, months and accounts that `blank` would blank, and of rows that only gain the label under `interim`; read-only on a local default run; counts only | FWD-3 | LOCAL | CB-ck-1 | `0.9.0_WK_ADVI_COTBKF~178` (same queue) |

**Fan-out (to state at the cut):** `1 of 1 chains, cap 8` (ck-2 consumes ck-1's switch; one worker's queue).
**Not in this round:** applying either branch to the served Cottonwood tables; that waits for Andrew's reading (call 3adb) and a never-widen pair, which `CB-ck-2`'s counts feed.
