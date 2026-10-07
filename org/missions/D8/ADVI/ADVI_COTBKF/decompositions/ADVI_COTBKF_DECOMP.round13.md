# ADVI_COTBKF decomposition -- ROUND 13 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-07 ~15:1xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-12 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_12_20261007.md` @9a9384d247 (msg 742): CB12l1-AC3
NOT MET -- the shared rule `commonwealth_crosswalk.SIGN` has no `leu` (cash in lieu), so a fraction sold for cash is never subtracted; 13
of 13 snapshot differences equal their pair's `leu` quantity; 515 `leu` rows over 69 accounts. E1: every type signed (census first), then
the rebuild. E2: the crosswalk re-scored on the fixed rule.

**Rule 24.** Domain: E1, E2. Subtraction at the cut, measured by the issuer:
- **There are TWO signing tables, not one.** `commonwealth_crosswalk.py:80-82` (`SIGN`: 12 plus types, 5 minus) and
  `commonwealth_account_links.py:83-87` (`HOLDING_SIGN`: 17 plus, 13 minus). They disagree: `HOLDING_SIGN` signs `leu` -1 and also
  `trci`, `trco`, `ss`, `si`, `cs`, `so`, `LOX`, `LISU`, `LICASU`, `TRCISU`, `BYX`, `LIX`, `pyd`, which `SIGN` omits; `SIGN` signs `ci`, `12b1`,
  which `HOLDING_SIGN` omits. `commonwealth_daily_holdings.py` imports `SIGN`. The defect class is two rules for one property.
- **Issuer's ruling (inside the decomposition):** E1 makes ONE signing table, decided from the census, that the crosswalk, the account
  links and the daily holdings all import. E2's before/after diff covers BOTH applied tables the old rules produced -- `crosswalk`
  (FWD-8) and `account_links` (FWD-9) -- read-only. A served copy that changes is a later packet with its own never-widen halves;
  DELTA=0 needs none. E1 and E2 are one chain (E2 consumes E1's table).

## The cells

| cell | what | serves | risk | chain / slot |
|---|---|---|---|---|
| `CB-m-1` | the transaction-type census; ONE signing table (`leu` -1; `ileu` decided from its quantity-bearing row) imported by all three scripts; daily holdings rebuilt, with fractional residuals counted over ALL accounts | FWD-3 (CB12l1-AC3) | LOCAL | A, `0.9.0_WK_ADVI_COTBKF~29` (first) |
| `CB-m-2` | the crosswalk and the account links re-run on the one table and diffed against the APPLIED tables: class counts before and after, every changed row listed | FWD-8, FWD-9 | LOCAL | A, `0.9.0_WK_ADVI_COTBKF~29` (second) |

**Write sets:** CB-m-1 -- `data/assets/scripts/silver/commonwealth_signs.py` (new), `commonwealth_tx_types.py` (new, analysis),
`commonwealth_crosswalk.py`, `commonwealth_account_links.py`, `commonwealth_daily_holdings.py` (each: import the one table, nothing else),
their tests. CB-m-2 -- `data/assets/scripts/analysis/commonwealth_rule_change_diff.py` (new) + its test. **Fan-out:** `1 of 1 chains, cap 8`.
