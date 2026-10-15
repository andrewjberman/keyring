# IRPT_ANLREQ -- decomposition, round 43, workstream T (issuer 2.0.0_SA_COO~T2)

**Input:** the CTO half of the commentary deploy (msg 8577, `deliverables/1.0.0_SA_CTO~DELL2/R42_DEPLOY_COMMENTARY_LOGGER_AND_FIGURES_CTO_HALF.md` @667daf91c8), condition 4: "a test feeds `figures_block` a dollar amount, a name and an account id, and shows all three dropped."

**Measured by the issuer before the cut** (2026-10-15 ~19:3xZ, on the merged `drafter.py`): the ticker pattern `^[A-Z0-9][A-Z0-9.\-]{0,9}$` ADMITS `12345678` and `A1234567` (both match; neither is in the estate's classification table of 11,361 tickers), so an
eight-character account number written as a holding's ticker would reach the Kimi prompt; `model_names` admits any string of at most 80 characters, so a client name written there would too. Condition 4, run as written, would fail on the consumer as merged at `d44932acb5`.
`AAPL` and `BRK.B` are in the table.

## Cells

| cell | source | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-t-33` | CTO half condition 4 + the measured gap | `figures_block` admits a `top_holdings` ticker ONLY if it is in the estate's classification table (`classification.load_classifications()`), and a `model_names` entry ONLY if it is among the request's own `comparison_keys` (the catalogue keys that already reach the prompt); anything else is dropped and counted. Three new tests in the existing figures test file, including the condition-4 test: a dollar amount, a name and an account id fed to the projection are all dropped, with a clean control that survives. Fakes only. | `data/transcripts/scripts/commentary/drafter.py`, `data/transcripts/scripts/tests/test_commentary_figures.py` | LOCAL |

## Not cells

- The deploy packet's pin moves to the merge of this cell; the issuer amends the packet and the applier order is cut on the new pin.

## Edges and chains

- One cell. M = 1. DIRECT-ACT (about 40 product lines, LOCAL).

fanout: 1 of 1 chains, cap 8, reason: one direct-act cell on a disjoint write set.
