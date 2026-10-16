# ADVI_COTBKF decomposition -- ROUND 99 (issuer 2.0.0_SA_COO~C1 on dell1; drafted 2026-10-16) -- the CVO's caveat: re-derive the Yahoo point set from the price stores' own source field

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** the CTO's round-N analysis for rounds 96-98 (`ledger/ROUND_ANALYSIS.round96-98.md` @aae37d1818; msg 6578), on the CVO slug `ADJUDICATION_v64`. Rounds 96-98 close MET on the served artifact. The CTO's enrichment list has two items:

1. **W181-S1 (ARMED, latent):** carry each SECHIST point's upstream source through `read_sechist`; criterion: a planted Yahoo-origin SECHIST point labels NOT_FOR_ACTIVE; it must land before the first SECHIST `security_series` object.
2. **The CVO's caveat:** the label check joined against the build's own price file; re-derive the Yahoo-sourced point set from the price STORE's own source field and compare it with the served labels; read-only, no served write; a difference graduates as a row.

**What the issuer's read adds to item 1 (not in the analysis).** The criterion already holds at the trunk. Round 92's `CB-cn-1` (worker ~182, `7d63d1b5e4`, in `box/dell1`) made `read_sechist` label each point from its `source` value (`bloomberg` reads the SECHIST store label; `yahoo_finance` reads `yahoo_finance`; any other value, a null, a case variant, a joined value, or an object with NO `source` column fails closed to `yahoo_finance`). Its test `test_sechist_source_a_yahoo_point_reads_not_for_active_in_the_served_label_for_a_v2_held_security` plants a Yahoo-origin SECHIST point and reads it NOT_FOR_ACTIVE through `fs.use_labels` / `fs.value_table`; `data/assets/scripts/silver/tests/test_commonwealth_sechist_source.py` reads 8 passed at the trunk (issuer's run, 2026-10-16 ~07:4xZ). The W181-S1 row was filed in round 91 (worker ~181) and was never disarmed after round 92. So item 1 needs no build cell, and "no cell is cut for coverage alone": the issuer disarms the row as its disarm owner, with that evidence (row `D1-S14`). The residual is stated there: the series WRITER (not yet writing) must emit `source` values from the reader's vocabulary; any other value fails closed to the Yahoo label, which is the safe direction.

**Rule 24.** Domain: the CTO's two round-99 items. Subtraction: item 2 -> `CB-cu-1`; item 1 -> met at the trunk, disarmed by the issuer, no cell. Carried, not cut (CTO): FWD-8/9 matching, which waits on Andrew's packet send and Commonwealth's registration file; no contact with Cottonwood.

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-cu-1` | read-only LOCAL: re-read the price stores from S3 into a fresh directory, derive the set of (cusip, day) points whose store `source` names `yahoo_finance` or `linear_interpolation` for the securities the served `account_day_value` prices (non-cash, close not null), derive the set the served `use_class` marks (not `NOT_YAHOO`), and compare the two: equal, or the difference listed in counts and categories; no served write | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~188` |

**Fan-out (to state at the cut):** `1 of 1 chains, cap 8`.
