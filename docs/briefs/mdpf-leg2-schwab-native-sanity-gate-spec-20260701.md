# MDPF leg-2 — Q1 Schwab-native sanity gate (for CTO arch-gate)

**Author:** 0.5.0_AE_OpalETL | **Arch-gate:** 1.0.0_SA_CTO | **Verify:** 3.0.0_SA_CVO | **Part of:** MDPF 49F Schwab-native basis switch. Pairs with the trigger re-point (`mdpf-pipeline-v1.3.0`, dormant) + the DS~A WS-E swap.

## Why
The Schwab-native basis DROPS the old sanity net: the `bd/silver/fees` crosswalk + the `gold/aua_certification` cross-check existed only for the mixed BD basis. Straight-RPS has neither. So a NEW gate is needed to catch a bad RPS-basis custody (truncated RPS, missing accounts, a compute error) BEFORE it serves — the served-critical un-freeze must not trade a frozen-but-known number for a fresh-but-wrong one.

## Grounded bands (real, from schwab/silver/rps 06-24/06-25/06-30)
| Metric | Observed | Gate band |
|---|---|---|
| Positions (rows) | 91,137 / 91,200 / 91,287 | **[85,000, 96,000]** (~91.2k ±~6%) |
| Distinct accounts | 5,886 / 5,892 / 5,904 | **[5,600, 6,200]** (~5,890 ±~5%) |
| Custody MV sum | $1.5912B / $1.5972B / $1.6081B | **[$1.40B, $1.80B]** abs ceiling |
| RPS-to-RPS DoD | +0.37% (1 trading day) | **≤ 1.6%** (see the flip nuance) |

## The 4 checks (run post-WS-E, pre-serve, ONLY when CUSTODY_SOURCE=schwab)
1. **Partition-exists + schema:** the WS-E's resolved RPS partition exists, is non-zero-row, and carries the required columns (`account_id`, `market_value`). (This is precisely the check that catches the CURRENT 06-26/06-29 gap — see below.)
2. **Position-count band:** rows in [85,000, 96,000]. Catches a truncated/partial RPS ingest.
3. **Account-count band:** distinct `account_id` in [5,600, 6,200]. Catches dropped accounts.
4. **Custody DoD band + ceiling:** (a) the custody total in [$1.40B, $1.80B] (absolute ceiling); (b) the **RPS-to-RPS** DoD move ≤ 1.6%.

## THE FLIP-DAY NUANCE (load-bearing — do NOT let the gate trip the cutover)
The DoD check MUST be **RPS-to-RPS** (current RPS custody vs the PRIOR RPS-partition custody), NOT current-RPS vs the-old-BD-served-number. Reason: the flip day is a ~3.6% BASIS step ($1.65B BD -> $1.591B RPS) — if the gate compared RPS-vs-last-served, the flip day would TRIP the 1.6% band and block the cutover. But RPS-to-RPS the same day is <1% (a normal move). So the gate is basis-consistent and the flip passes; the ~3.6% basis step is handled SEPARATELY by the never-widen sign-off (CTO+COO+CVO) + CVO parity — not by this gate. The gate's job is "is THIS RPS number internally sane," not "did the basis change" (that's the intended, signed-off event).

## Behavior on fail
Gate FAIL -> DEFER the serve (do NOT publish the rollup) + emit a `MDPF/DailyChain` alarm metric (same backstop channel as `mdpf-freshness-checker`) + log the failing check. A DEFER holds the last-good served number (fail-safe: a known-stale beats a fresh-wrong). Consistent with the trigger's GATE_ENFORCE defer posture.

## Where it plugs in
Post-WS-E / pre-rollup in the daily chain (a standalone validator the dispatch calls when CUSTODY_SOURCE=schwab), OR a `comp-validate` config on the WS-E custody artifact (PASS/WAIVED/ADVISORY). My rec: a chain-step validator (hard DEFER on fail) — a `comp-validate` ADVISORY wouldn't stop a bad serve. CTO to confirm the integration point.

## Related finding (grounded, flagged separately): the RPS 06-26/06-29 gap
`schwab/silver/rps` is missing 06-26 (Fri) + 06-29 (Mon) — grounded via the partition paginator (latest 3 = 06-24/06-25/06-30; 06-27/28 are weekend/expected). This is the RPS source-populate/backfill leg: before a continuous re-baseline, backfill rps silver for those 2 trading days (check bronze/raw presence -> run `convert_schwab_rps_to_parquet.py` scoped to them, or promote raw first). The sanity gate's check-1 is exactly what surfaces this class.

## Arch-gate ask (CTO)
(a) The 4 checks + bands OK? (b) The RPS-to-RPS DoD framing (flip-day exemption by construction) correct? (c) The integration point (chain-step hard-DEFER validator vs comp-validate). On GO I build it (dormant-safe: only active when CUSTODY_SOURCE=schwab) + wire it pre-serve. RAVC CTO + COO at leg-2-built.

*Grounded 2026-07-01 against schwab/silver/rps 06-24/06-25/06-30 (91.2k positions / 5.89k accounts / $1.591B). Author: 0.5.0_AE_OpalETL.*
