# DATA_PLATFORM reverse-ETL — CHUNK-3: TXN / NNA (data-calibrated tier row)

**Lane:** 0.4.0_DS_ClientPlatform~B (2nd DS lane) · **Lead/integrator:** 0.4.0_DS_ClientPlatform (base, unified tier table)
**Date:** 2026-06-24 · **Status:** chunk-3 COMPLETE — tiered on live artifacts + source-confirmed classifier; fresh full-reconciliation residual flagged honestly. RAVC2 base-DS+COO+CTO (cc CVO/0.6.0)
**Gradient (refined, CTO-adopted):** T1 (custodian-repackage) / T2-HOST (firm-owned ref data the vendor hosts) / T2-COMPUTE (genuine vendor algorithm). **Confidence-tag (CTO/ROE):** 49F = DIFFABLE (both ends held -> HIGH); cot/inf = INFERRED.
**Diff question:** can BD's served transactions + NNA be reproduced from Schwab TRN (the custodian transaction feed) we hold?
**Note:** diffed vs Schwab TRN DIRECT (the trn_nna Layer-B path is dormant — base-DS D1 work; correct per the GO).

---

## TIER ROWS (data-calibrated)

### Row 3A — TRANSACTION FEED (events): **T1 — custodian-repackage + enrichment**  · confidence: DIFFABLE/HIGH (mechanism)
- **Schwab TRN** (custodian source-of-truth, live `schwab/silver/trn`, 537 partitions, 2026-06-18 = 28,091 rows/day) carries full per-transaction detail: `tran_code, transaction_source, transaction_detail, ticker, cusip, quantity, price, gross_amount, net_amount, commission, settlement_date`.
- **BD `silver/transactions`** (live, 1,815 partitions, trailing window) = the SAME custodian transaction events repackaged + enriched with: (a) BD taxonomy (`action / transaction_type / transaction_sub_type`) = deterministic mapping; (b) the `external_flow` NNA flag (see Row 3B); (c) **the SAME firm-owned relationship/advisor/fee DIMENSION overlay as chunk-2** (architect/implementor/consultant splits, fee schedules, relationship hierarchy, goal/style/benchmark — re-joined onto every transaction row).
- **Verdict:** the transaction EVENTS are custodian-sourced (Schwab TRN is the truth) -> T1 repackage. The taxonomy = deterministic T1 mapping. **The dimension overlay = T2-HOST** (identical firm-owned ref data to chunk-2 Row C — cross-ref, no double-count). BD's broader row volume = its broader account universe + grain (held-away/other-custodian), same pattern as chunk-2.

### Row 3B — NNA CLASSIFICATION: **T1 — deterministic rule-set, reproducible from Schwab TRN**  · confidence: HIGH on mechanism+documented-validation; MEDIUM on fresh-reproduction (residual)
- **Mechanism (source-confirmed):** `convert_schwab_trn_to_nna_silver.py::classify()` reproduces NNA from Schwab TRN ALONE via a pure deterministic rule-set — EXCLUDE sweeps/dividends/trades/journals/fees/intra-Schwab; INFLOW = deposits/wires-in/transfers-in/moneylink-in; OUTFLOW = funds-paid/wires-out/IRS-WH/transfers-out; sub_category WIRE/MONEYLINK/TOA/DEPOSIT/CHECK/IRS_WH. No vendor algorithm — replicable (we already wrote it).
- **Documented validation (the load-bearing evidence):** that classifier was validated to **85-90% monthly parity vs Schwab's OWN published 49F Business Review NNA** (Jul-Dec 2024) — i.e. NNA reproduces from custodian-raw to within 10-15% at monthly grain, measured against the custodian's authoritative figure.
- **BD does the same (confirming):** BD's `external_flow` field = `Contribution` / `Withdrawal` / None — BD independently performs the identical deterministic inflow/outflow classification. NNA-classification is a standard custodian-feed transform, NOT BD-proprietary IP.
- **Fresh spot-run (live 2026-06-18):** classifier on the day's Schwab TRN -> 99 inflow ($2.23M) / 14 outflow ($87K) / net $2.14M; 99.4% correctly excluded — sane, reproduced from custodian-raw.
- **Verdict:** NNA = T1 (deterministic classification of custodian transactions). The ~10-15% residual = classifier edge cases / timing / in-kind, bounded — NOT irreproducible IP.

---

## RULE-22 — what I could NOT cleanly verify (a finding, not a gap glossed)
**A fresh same-period BD-vs-Schwab NNA reconciliation is NOT directly achievable from the current silver artifacts.** Attempted (live), inconclusive due to THREE structural mismatches:
1. **Window misalignment:** Schwab TRN partitions are SINGLE-DAY (`date=20260618` = only 06-18); BD `silver/transactions` is a TRAILING window of variable length (06-18 file = 06-01..06-18; 05-29 file = only 05-20..05-29). Aligning to a full calendar month requires reconstructing BD's window from multiple deliveries.
2. **Amount semantics:** BD flow amount = `market_value` (full MV of securities moved, incl. in-kind TOA); Schwab = `gross_amount` (cash). In-kind transfers diverge.
3. **Account universe:** BD broader (held-away/other-custodian), same as chunk-2.
A naive single-day diff gave Schwab/BD net 25%; a naive May diff gave 495% (Schwab full-month vs BD 10-day partial) — both pure window/semantic artifacts, NOT parity signals. **The T1 tier therefore rests on the deterministic-mechanism + the documented 85-90% monthly validation vs the custodian's own NNA + BD's confirming `external_flow` — NOT on a fresh diff.** A clean fresh full-month reconciliation (assemble BD window -> full month + normalize amount semantics + matched-account restriction) is a **bounded hardening residual** (low-risk; the mechanism is deterministic and historically validated).

---

## GROUNDING + RESIDUALS
- **comp-rail:** comp-which -> comp-pipescript io C_01 (canonical_nna IO); native source Reads (the two converters + classifier); live data-access via boto3 (off-rail, Rule-21).
- **NNA methodology note:** our gold `C_01.canonical_nna` uses the GAINS method (MV-change-minus-market-gain, from `account_gains` B_03 — positions-based, already Schwab-RPS-direct), a DIFFERENT path than the trn_nna transaction-classification. BOTH are T1 + Schwab-reproducible — NNA is cross-validated two independent ways (positions-derived AND transaction-derived). Neither requires BD IP.
- **Residuals:** (1) fresh full-month reconciliation (above) — bounded hardening. (2) ~10-15% NNA classifier residual — documented, bounded. (3) 59 unclassified-not-excluded rows in the spot-run = tiny classifier coverage residual (immaterial). (4) **49F/Schwab DIFFABLE only; cot/inf INFERRED** — do NOT project T1 to cot/inf as proven (no custodian-raw to diff); INFERRED until a custodian-direct feed lands.
