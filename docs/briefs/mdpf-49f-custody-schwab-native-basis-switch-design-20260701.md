# MDPF 49F Custody — Schwab-Native Basis Switch (design brief for CTO arch-gate)

**Author:** 0.5.0_AE_OpalETL (mdpf-infra + Schwab-ingest owner) | **Sovereign:** Andrew (ruled 2026-07-01) | **Implement lane:** 0.4.0_DS_ClientPlatform (owns the WS-E build) | **Arch-gate:** 1.0.0_SA_CTO | **Verify:** 3.0.0_SA_CVO
**Class:** methodology change to a SERVED CRITICAL SURFACE (MDPF 49F custody → served client AUA). Full gate chain, no shortcuts.

> **ADDENDUM — RETRACTION (2026-07-01T21:45Z, CTO-confirmed):** the "delta-3 coherence fix" (scope model/sma to `custodian==Schwab`) is **RETRACTED / DROPPED — PATH A**. Grounded (Rule 22): the WS-B `custodian` column is hardcoded `None` (feeder L169, 100% None) so the mechanism was false, AND the accepted v0.9 basis already subtracts model(all)/sma(all) from Schwab-restricted custody + serves a coherent residual → model(all) is already the Schwab universe → the scope is a NO-OP. My prior "~$156M held-away in model/sma" premise was ungrounded (no source; contradicted by the structural clincher) and is retracted; if held-away exists it's in the DIRECT-custody leg, which the RPS Schwab-only basis correctly excludes. **The served basis is `non_model = straight-RPS(Schwab, ticker!='CASH') − model(all) − sma(all)`** (DS~A magnitude: +$180–203M, positive/stable), with a fail-closed seam (custodian-scope auto-engages if the col ever populates + hard residual fail-close). Cash rule locked: exclude `ticker=='CASH'` ($1,591,210,618.75 @06-24), identical across WS-E + leg-2 gate + CVO parity. Anything below that references the (now-dropped) coherence-scope is superseded by this addendum.

## 0. Andrew rulings (2026-07-01, verbatim intent)
1. Switch MDPF 49F custody to a **Schwab-native basis**.
2. **Assets-only — eschew cash. "Straight RPS."** (Simplification over the earlier RPS+bank-sweep-cash design — no cash source to reconcile.)

## 1. Why (the provenance finding)
MDPF's `partner_custody_total` (the served 49F custody) is computed by `build_mdpf_wse_49f_non_model_aua.py` (v0.9, 2026-05-20) as: `sum(account_market_value)` over **`bd/silver/allocations`** (BD-canonical, liability-excluded), **restricted to Schwab via the `bd/silver/fees` custodian crosswalk**, cross-checked vs `gold/aua_certification`. **The `fees` crosswalk froze at 06-25 → the served AUA froze 6 days.** The BD-allocations input is actually fresh (through 06-29); the FEES crosswalk is the break. My Schwab RPS silver never feeds this path (CTO~B "ruled the crosswalk over RPS silver", v0.9). NO logic change on 06-24 (git-confirmed; the served $1.65B = the v0.9 "49F_total $1,654.3M" baseline, stable since 05-20).

**The switch removes the frozen dependency at the root:** a Schwab-native basis reads the RPS position snapshot directly — no BD allocations, no fees crosswalk, no cert cross-check.

## 2. New logic
```
partner_custody_total(49F) = sum( RPS position Market_Value )
                             over schwab/silver/rps/date={D}  (49F account 08242234 delivery)
```
- **Source:** `opal-data-bd/schwab/silver/rps/date={D}/data.parquet` (my Schwab-ingest lane; the CRS{D}.RPS positions).
- **Schwab-scoped by construction:** the RPS delivery IS 49F's Schwab-custodied accounts — no fees crosswalk needed (the crosswalk existed only to restrict the BD full-book to Schwab; RPS is already Schwab-only).
- **Assets-only:** positions Market_Value; the ~2% Schwab bank-sweep cash is **excluded by design** (Andrew ruling 2). The 16 money-market *positions* in RPS remain counted (they're positions, not sweep).
- **Retire from this path:** the BD-allocations read, the fees-crosswalk, and the `gold/aua_certification` cross-check (all BD-basis; not applicable to the Schwab-native number). The certified_aua cross-check must be REMOVED or replaced (it asserts against the BD figure, which the new basis intentionally differs from — leaving it in would hard-raise).

## 3. Basis consequence (the one-time step — Andrew accepts)
| Date (06-24) | Old (BD-canonical, served) | New (straight RPS) | Delta |
|---|---|---|---|
| partner_custody_total | ~$1.650B | **$1.591B** | **−$59M (−3.6%)** |
Decomposition of the −3.6%: **~2.0% = bank-sweep cash** (intentionally dropped, $36.2M) + **~1.6% = coverage/valuation** (BD tracks ~157-account-net differences + minor valuation timing vs the Schwab position snapshot). **One-time documented methodology step at cutover** (Andrew accepts — assets-only Schwab-native is the cleaner single-source number going forward). *History re-baseline = OPTIONAL (Andrew to confirm accept-the-step vs recompute-history-for-a-smooth-chart; leaning accept).*

## 4. Validation (NOT parity-to-BD — the bases differ by design)
The old proof-of-parity ("RPS+cash == BD") is retired with the cash. The validation is instead: **RPS is a clean, complete, smooth Schwab-native asset series.** Evidence (grounded, this session):
- 06-22→06-30 RPS custody: $1.627B / $1.601B / $1.591B / $1.597B / $1.595B / $1.604B / $1.608B — smooth, all day-over-day moves <1.6%; ~91,200 positions, ~5,890 accounts stable throughout.
- The −3.6% vs BD is fully decomposed (§3) — no unexplained residual.
- **CVO live-verify bar:** deployed WS-E reads `schwab/silver/rps` correctly + the served 49F custody == the straight-RPS sum for the date, on the running pipeline (not asserted).

## 5. Dependencies + sequencing
- **RPS silver must be current** for the new basis to serve fresh → the Schwab silver roll-forward (06-26/06-29/06-30) is RE-SCOPED from "MDPF fix" to **"populate the Schwab-native source-of-record"** (ledger 20260701T1800Z re-scoped by COO). It now genuinely feeds the basis.
- FLOW: this brief → **CTO arch-gate** → **DS** swaps `compute_partner_custody_total` (read RPS silver; drop allocations/fees/cert) in `build_mdpf_wse_49f_non_model_aua.py` → **CVO** multi-day live parity-verify → deploy.
- **Interim freeze** (parallel, COO/Andrew lane): the current-basis MDPF stays frozen until the switch ships UNLESS COO/0.6.0 advance the `bd/silver/fees` crosswalk past 06-25 as a stopgap. Not a dependency of this switch.

## 6. Open items for the gate
- (a) CTO: confirm dropping the `gold/aua_certification` cross-check is acceptable (it's BD-basis; incompatible with Schwab-native) — or define a replacement Schwab-native sanity check.
- (b) Andrew: accept-the-step vs re-baseline history (§3).
- (c) DS: the exact `compute_partner_custody_total` swap + whether the non_model_aua downstream math (certified_aua − model) needs the certified_aua term redefined on the Schwab basis.

*Grounded 2026-07-01 against build_mdpf_wse_49f_non_model_aua.py (v0.9), bd/silver/{allocations,fees}, gold/aua_certification, schwab/silver/rps, raw CRS RPS. Author: 0.5.0_AE_OpalETL.*
