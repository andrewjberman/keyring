# MDPF_SECCLASS decomposition -- ROUND 4 (2026-09-30, issuer 2.0.0_SA_COO~M, on Andrew-direct @6a861c4e18)

Round 4 holds one cell, E10. It comes from Andrew's standing word on the Kimi K3 classifier (relayed by 1.0.0_SA_CTO as
103181). GATE (x) admits one issuance per round, so E10 cannot join round 2 or round 3. Standing rulings are as in
round 2: Andrew-direct 2026-09-30 ~02:2xZ (bd-securities seeds new rows only) and the CTO C-WRITER ruling. Rule 24:
the domain is {E10}; one cell with no remainder, same grain as round 2, one intent (residual coverage). It moves no
served value (it runs the classifier and writes a census and a half; it makes no table write).

**Source.** Andrew-direct ~06:xxZ, verbatim: "We don't need a human review for that, what would be better is a flag if
Kimi has lower confidence. I think we can just make a really tight prompt and that should wrap that up pretty cleanly."
Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_06xxZ_TRNSPT_DONE_WHEN_CONFIRMED_PAGEFILE_APPROVED_KIMI_STANDING_WORD.md`.
Scope: MDPF_SECCLASS classification only, with security names and tickers as the only input and no client data.
Each result carries a confidence, and a low-confidence result is FLAGGED as a stored attribute, not held back.

## The cell

| cell | item | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `SC-e-10` | E10: Kimi K3 classifies the E8 residual (the round-1 unresolved names E8 left without a class) from name and ticker only. Each result has a class in the table's vocabulary, a confidence, and a flag below 0.80. Contract 0.3.0 adds `classified_by = model` plus the confidence and flag fields. Real run, census, and a half for the keyed writes | FWD-7, FWD-4 | NOT-EVALUATED | laptop | WORLD | B, ~8 |

**Write set.** A new `_shared/etf_classification_model.py`, a new runner `yang_pipeline/classify-residual-model.py`,
their test, and the contract. Round 3's SC-e-9 (slot ~4) writes `_shared/etf_classification_scheduled.py`, which this
cell does not touch. The contract has had no writer since SC-e-1 closed.

**Threshold.** Issuer's ruling: a confidence below 0.80 sets `low_confidence = true`.

**Keys.** A result with a ticker is a would-write row on that ticker, a conditional put on absence. A CUSIP-only
result waits for E9's `CUSIP:<9>` key and is counted. A name-only result has no key; it is counted and named in the
half for the round analysis.
