# IRPT_ANLREQ round 11, workstream ~G (ENGINE) -- decomposition: the shared total-return helper that the four price adapters import

Issuer `2.0.0_SA_COO~G2`, 2026-10-15.

**Input:** the price-adapter facts read `AR-g-69` (merged `d1de2f0cd6`; record `deliverables/0.9.0_WK_IRPT_ANLREQ~176/r9/PRICE_ADAPTER_FACTS.json`; a read at base 421dd68001, proof VALID there; two of its 82 cites (`price_source.py` lines 14 and 85, now 15 and 92) drift on the main tree because my own repair `AR-g-70` moved that file afterwards: the answers are unchanged, and the worker-owned record is not edited by this seat), CTO msg 8377, PRD v0.14 FWD-7.

## What the read decided (ruled by the issuer)

- **One formula (q2):** `level_0 = 100` at the first retained date, `level_t = level_(t-1) * (1 + r_t)` with `r_t` each source's DAILY total-return fraction (DEMQUE `total_return`; Bloomberg `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS / 100`; Yahoo `(P_t + D_t) / (P_(t-1) / s_t) - 1` from the as-traded Close with Dividends and Splits, never Adj Close; YCharts `L_t / L_(t-1) - 1` from the served cumulative level).
- **Adapter cells (q4), numbers as the worker listed them:** `AR-g-80` shared helper (this cut); `AR-g-81` Bloomberg history; `AR-g-82` DEMQUE store; `AR-g-83` yfinance; `AR-g-84` YCharts session transport. All four import `tr_level` and take their clients as arguments.
- **Host reality (q3):** the resident host runs Python 3.12; pandas, pyarrow and yfinance are NOT in any tracked requirement of the host (pyarrow is used lazily by the layout; the r31 release check expects `yfinance_check.py` absent). The adapters are built against fakes and need
  the host dependencies installed by a CloudOps act under a pair in the release. `lib/trading_calendar.py` is not in the resident tarball (only `lib/opal_naming.py`): the T-1 date must be handed to the producer by the caller or the calendar module added to the package member list in the release cell.
- **YCharts (q1):** the CRO's measured path uses the secret `ycharts/credentials`, which the resident runner role does not hold; the resident's own session secret is `ycharts/session/current`. The YCharts adapter is built on the session transport and its use in production waits on a CTO ruling about the grant; Yahoo is the first round pick, so the report is not blocked on it.
- **DEMQUE (q2):** the resident has no read grant on the store's bucket (an estate-wide read): the estate tier uses the Bloomberg history only until the CTO rules on that grant.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-80` | `ycharts/research/tr_level.py` (NEW): `chain_levels(daily_returns, base=100.0)` and `returns_from_levels(pairs)`; stdlib only; 10 checked cases and a test file | `tr_level.py`, `tests/test_tr_level.py`, the worker's folder | WORLD (the floor of an infrastructure path; source and tests only, nothing deployed) |

## Edges and chains

- ONE chain here. The four adapter cells (each its own file pair: `price_adapter_bbg.py`, `price_adapter_demque.py`, `price_adapter_yfinance.py`, `price_adapter_ycharts.py`) are FOUR independent chains behind it, cut when this merges (they import it).
- Other open chains of this workstream: `AR-g-67` (ticket stamp, slot 179) and `AR-g-68` (door Keep, slot 178).

## Four-postulate record

(i) Domain: the one total-return formula (FWD-7). (ii) One module. (iii) One intent. (iv) What this cut does NOT move: any deployed byte, any host dependency, any grant, any adapter.

fanout: 1 of 1 chain for workers per cut (AR-g-80 worker slot 180), cap 8, reason: one small pure module; the four adapters depend on it, and slots 178 and 179 hold the two source cells of round 10.
