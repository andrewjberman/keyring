# ADVI_COTBKF decomposition -- ROUND 64 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11T09:37Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` ROUND-64 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_64_20261011.md` @5cc2574c67 (msg 4579), answering `3.0.0_SA_CVO` REMEDIATION_v36 @877c95fb20.
Section 4 is this round's rectangle: four items, one cell each.

**Where the project stands (the analysis, section 1).** The Cottonwood `account_return_daily` mint is served, truthful and about 94%
blank: 105,559 of 1,691,729 account-days carry a return, because an account-day holding any unpriced position is not measured and
75.8% of position rows carry no value. The coverage is the work.

**Rule 24.** Domain: the four items of section 4 -> four cells, none depending on another.

## Measured constraints (issuer)

1. **Items 1 to 3 are read-only.** No code, test, manifest or served key changes in them. Item 3 may END in a re-mint of affected
   days; that would be a later cell under its own pair, not this round.
2. **The price-source ruling is already on record** in the PRD (issuer read of lines 217 to 219: Yahoo Finance for equity, ETF and
   fund securities; Bloomberg at site Z for fixed income and other). Item 1 measures against it and adds no source. Bloomberg pulls
   go only through their queue.
3. **No other firm's data is read** by any cell (CLAUDE.md section 5).
4. **Client data in the private git is not worth more time** (Andrew-direct 2026-10-09, record
   `ANDREW_DIRECT_20261009_192xZ_CLIENT_DATA_IN_PRIVATE_GIT_NOT_WORTH_TIME.md`); the cells still keep account ids and account figures
   out of their records because nothing in them needs one.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bl-1` | price coverage on 2026-05-06 by kind: unpriced securities and positions, whether the custodian's own data or a store this build already reads holds a price, and the ruled source per kind | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~90` |
| `CB-bl-2` | what the PRD promises for the returns table: is income part of the outcome; one paragraph with its lines | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~91` |
| `CB-bl-3` | the 24 emptied-account days with an absolute return above 1%: outflow, prior value, which disagrees, by class, and each class sized among the other 1,733 | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~92` |
| `CB-bl-4` | the older mint tests supply a stamped manifest; the test-only `REQUIRE_STAMPED` switch leaves the adapter and the conftest | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~93` |

**Fan-out:** `4 of 4 chains, cap 8`. `CB-bl-2` and `CB-bl-4` are DIRECT-ACT cells (LOCAL, small, mechanical only); `CB-bl-1` and
`CB-bl-3` carry a judgment criterion and take L8 to L10.
