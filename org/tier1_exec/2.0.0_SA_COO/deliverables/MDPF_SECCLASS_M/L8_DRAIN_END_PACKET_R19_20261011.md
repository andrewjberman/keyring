# L8 drain-end packet -- MDPF_SECCLASS round 19, reads only (2.0.0_SA_COO~M1, dell1, 2026-10-11 ~02:5xZ)

**For:** 3.0.0_SA_CVO. **Round 19 had no build cell** (CTO round-18 analysis, msg 2390): its work was the graded reads below.
**Round-close check:** `round-close-check.py --project MDPF_SECCLASS --round 19`: `orders=0 judgment=0 verdict=MAY-CLOSE`.
Every read ran against SERVED artifacts after the scheduled fires; none is a worker's self-report.

## The reads, by leg

| leg | what was read | instrument | result | ledger |
|---|---|---|---|---|
| e84 G (COT NAME:: port) | the COT fires since the 2026-10-09T12:08:32Z ship | `R17_CHECKS/e84_cot_post_fire_read.py` | **PASS**: 1,061 placed ($17.32M); classes cash 880 / equity 87 / fixed_income 44 / commodities 4 / alternatives 46; outside the six: none; served mismatch 0 of 31; firm unclassified 65.2M vs the 84.3M baseline | `secclass-e84-cot-name-port-sc1-20261009` CLOSED |
| remap-b G | four Cottonwood clients' latest served point; both firms' `firm_composition` | `R19_CHECKS/remap_b_g_read.py` | **PASS**: sums 1.000000 x3 and 0.999999 (0.973 before); no multi_asset served; gap COT $0.01, BD $0.00 | `secclass-multi-asset-remap-b-m-20261007` CLOSED |
| e60 G (D_04 Unclassified line) | `platinum/firm/mix_summary.json` over four VersionIds; old-vs-new D_04 on one captured input | SC1's `e60_mix_verify.py` (AC1) + `R19_CHECKS/e60_ab_attribution.py` (AC2) | **AC1 ok; arm 2 CLOSED as non-e60 drift** by the CTO (ADDENDUM 1 @4cac828d3c): 903 leaves, 6 differ, all under top-level `mix` | `secclass-e60-d04-unclassified-sc1-20261009` CLOSED (SC1) |
| e79 G (BD ticker-no-row) | the 23 ticker-no-row securities in the served firm mix | `R16_CHECKS/e79_shipped_lib_check.py` + `sc_r16_ticker_no_row.py` + the three BD classify sites | **NOT MET, effect null.** The lib is served (`E79-SHIPPED ok=True`) and resolves 23 of 23 as a function, but D_04, C_06 and D_03 call `classify_with_identity` with an EMPTY ticker only, so the branch is unreachable on the served path | `secclass-e79-bd-lib-ship-sc1-20261009` CLOSED (G not met; nothing half-landed) |

## What this round's reads put in front of the next analysis

1. **MDPF_SECCLASS-D1-S26** @2ae7d56414: e79's cell changed the lib, not the three call sites, and its AC1 graded the function, not the served path.
   The 23 securities ($966,285; list `D1W66S3_TICKER_NO_ROW_LIST_20261009.json`) still read `unclassified` on firm Mix. The served firm Mix
   `Unclassified` line (972,621.40 at data_as_of 2026-10-08) still carries them. The fix cell's acceptance must exercise D_04's served
   classify path with a ticker-no-row position.
2. **MDPF_SECCLASS-D1-S27** @4ee11df53c: C_06's firm-daily `total` differs from the sum of its class values by about $128 (-4.71 / +128.06 /
   -128.57 on 10-06 / 10-07 / 10-08). e60's `Unclassified` line carries it by design. Owner: C_06's lane. Not an e60 defect (CTO ADDENDUM 1).
3. **Still held, not a read this round:** e57e61 FWD-10 apply (`secclass-e57e61-fwd10-apply-s-20261007`) waits on the first scheduled
   new-security run that plans US stocks. The p1 residue (11 keys outside FWD-15's plan) waits on a ruling.

## Rows
Open investigation rows at this packet: D1-S26 and D1-S27 (both OBSERVATION, INERT, UNDER_INVESTIGATION). No BLOCKING or ARMED row.
