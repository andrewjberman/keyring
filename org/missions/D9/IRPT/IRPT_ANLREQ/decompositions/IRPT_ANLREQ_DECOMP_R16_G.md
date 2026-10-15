# IRPT_ANLREQ round 16, workstream ~G (ENGINE) -- decomposition: the priced figures print, and the priced page keeps the Opal wording

Issuer `2.0.0_SA_COO~G2`, 2026-10-15.

**Input:** the engine compose read `AR-g-54` (the map statistic defect: `p2.e08`, `p2.e13`, `p6.e22` carry `statistic` null), the price stage `AR-g-86` (merged `1c84d38bf4`) and its worker's row `IRPT_ANLREQ-D2-W186-S1` (a priced page prints YCharts wording and the time-budget line, against the Opal page rule R8), the issuer's reference builds for both.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **Map statistic defect (`AR-g-88`).** The read proposed changing the map (one statistic per element, or a split per column), which changes the pinned map's bytes and moves its pin. The three elements already name their statistics in `columns`; the layout reads only the single `statistic`. Reading `columns` in the engine fixes all three with no map change, so no pin moves. A table gets a dict with human labels (`Total return 1Y`, `Max drawdown all`) and `n/a` for a column the series is too short for (a 15-year return is never shown for a 2-year series); a chart gets the list of the values worked out; none workable is the first column's own reason. The trace `coverage` is the share of columns worked out.
- **Priced page wording (`AR-g-89`).** `build`'s `pricing` argument is the PAGE wording (False is the Opal form), and the values come from `computed`. The row offered two repairs, the producer passing `False` to `build` or the layout's `pricing=True` branch made Opal-safe. The first is two arguments and leaves the layout's YCharts path alone; taken.
- **The check missed it.** `ar_g86_checks.py` graded only the count of NOT_IN_THIS_VERSION lines on the priced page, not its footer or vendor wording. `ar_g89_checks.py` grades the wording (no `YCharts`, no `time budget`, the Opal credit on every page, the figure printed). Recorded as the issuer's gap, not the worker's.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-88` | `layout_overview.py`: `_column_statistics`, `_column_label`, `COLUMN_NA`, the `columns` branch of `_compute_own_series`; `tests/test_layout_own_series_columns.py` (8 named tests) | those two files + the worker's folder | WORLD (floor of an infrastructure path; source and tests only) |
| `AR-g-89` | `opal_producer.py`: the two `lo.build` calls take `False`; `tests/test_opal_producer_page_wording.py` (4 named tests) | those two files + the worker's folder | WORLD |

## Edges and chains

- TWO independent chains: disjoint write sets (`layout_overview.py` and its test, `opal_producer.py` and its test). `AR-g-89`'s page checks run through the producer on a map of its own, so they do not depend on `AR-g-88`; either may merge first.

## Cut after this one

The wiring of the real readers and of T-1 into the resident; the swap for an unpriced symbol; the benchmark and risk-free series; the YCharts-snapshot and non-computed series elements; the ONE resident release r32 (inputs listed in `IRPT_ANLREQ_DECOMP_R14_G.md` and R15).

## Four-postulate record

(i) Domain: the elements of the Overview that need the portfolio's own series, and the page that prints them. (ii) One compute branch; one page flag. (iii) One intent each: the figures print; the page keeps the Opal wording. (iv) What this cut does NOT move: the map and its pin, the renderer, the chain, the adapters, any deployed byte.

fanout: 2 of 2 chains, cap 8, reason: two cells on disjoint files; slots 188 and 189.
