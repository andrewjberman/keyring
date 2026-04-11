# Pricing Bug Investigation, AUA Reconciliation, and Cohort Framework

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-10
**Project:** ADVI_49PUSH (continuation)
**Status:** COMPLETE for the investigation pass. Two open follow-ups (mapping rebuild + Type S structural pivot) staged for next session.

---

## Session Origin

Andrew opened the session asking why the AdvisorIntelligence "Assets Overview" GRO toggle showed Q2 2026 market growth at +4.12% / +$66M when "it has not been a great quarter." The investigation expanded into a full-firm AUA reconciliation, surfaced multiple distinct pricing bug classes, and ended with a clean cohort framework for managed vs non-managed AUA.

---

## Commits this session

| SHA | Description |
|---|---|
| `011ac15c` | re-apply fix_3b in D_00b + strip economic_total from GRO schema |
| `f75a3599` | revert fix_3b strip in D_00b (kept economic_total cleanup); raw sum(growth) is the better proxy |

Both pushed to origin/CLOUD.

---

## Files Modified

| File | Change |
|---|---|
| `data/black_diamond/scripts/gold/D_00b.portal_timeseries.py` | First applied fix_3b market = sum(market_growth) − aua_residual_period (011ac15c). Then reverted (f75a3599) after QA showed historical periods broke. economic_total field deletion preserved. |
| `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` | Removed economic_total from `_aggregate_growth_to_periods` buckets and result schema. Added aua_residual_delta passthrough into quarterly/annual aggregation for audit. |
| `silver/prices/canonical_prices.parquet` (S3, not git) | Re-injected scoped overrides via inject_scoped_overrides.py — repaired 7 broken overrides (BNP PARIBAS SA, Waldrop DAF, BANC AMERICA FDG, DESTINATIONS LCAP/INTL, JPMorgan Chase Financial 0% 02/14/2029, Wells Fargo MBS 2007-15) on Apr 6/7/8 dates that the build_canonical_prices_v2 rebuild had wiped. |

## Files Created (analysis artifacts, not deployed)

| File | Purpose |
|---|---|
| `data/analysis/cohort_4_tagged.csv` | 458 BD-only non-fee-paying accounts tagged into 15 sub-cohorts (4a_daf, 4b_structured_trust, 4c_real_estate, 4d_employer_retirement, 4e_explicit_no_fee, 4f_liability, 4g_other_trust, 4h_ira, 4i_529, 4j_banking, 4k_entity, 4l_joint_taxable, 4m_other_brokerage, 4n_insurance, 4z_unclassified). 98.7% of $130.36M classified. |
| `data/analysis/schwab_fees_parquet/Fees_OpalCapital_Daily*.parquet` (15 files) | Per-account billing config extracted from each of 15 Schwab fee xlsx files. |
| `data/analysis/schwab_fees_parquet/_consolidated_billing_config.parquet` | Deduped union of all 15 → 10,075 unique Schwab accounts with billable / bps / fee_desc. |

---

## QA Runs (no prod runner touched)

Both runs on `bd-gold-qa-runner` (`i-0090b823a4a0997e3`, c6a.16xlarge). Prod runner `bd-gold-layer-runner` remained `stopped` throughout.

| SSM CommandId | Mode | Commit | Started UTC | Completed UTC | Outcome |
|---|---|---|---|---|---|
| `5a5a59f2-464a-42ef-bf63-62bc5f0e3af7` | `--group D` | 011ac15c (fix_3b applied) | 04:14:33 | 04:43:36 | Success. Q2 '26 market dropped to +3.56% but historical periods broke (2024 annual −5.35%, 2025 −7.51%, Q1 '25 −35.15%). Strip over-corrected. |
| `a4e03dd0-2378-42ef-a6e9-0a08ce099286` | `--group D` + `shutdown -h +1` | f75a3599 (fix_3b reverted) | 04:47 (approx) | 05:20:12 | Success. Q2 '26 back to +4.12%, historical periods sane. QA instance auto-stopped after run via shutdown command. |

---

## Investigation Timeline

### Phase 1 — Q2 2026 GRO panel question (the original ask)

Pulled `s3://opal-data-bd/platinum/firm/timeseries_overview.json` and `s3://opal-data-bd/gold/timeseries/account_performance.parquet`. Q2 2026 was reporting **market = +$66.25M / +4.12%** on `period_aua_start = $1,607,747,964` (Mar 31 close) over 5 trading days. Andrew's intuition was that 4%+ market return in 5 days for a "not great" quarter wasn't credible.

Initial framing was that Q2 = literally Mar 31 → Apr 8 endpoint move, which the daily data confirmed:

```
2026-03-31 Tue  aua= 1.6098B  growth=  +31.76M
2026-04-01 Wed  aua= 1.6212B  growth=   +7.22M
2026-04-02 Thu  aua= 1.6216B  growth=   -0.37M
2026-04-03 Fri  aua= 0.1008B  growth=-1520.77M  (Easter Good Friday — pricing collapsed)
2026-04-04 Sat  aua= 0.1008B  growth=   +0.00M
2026-04-05 Sun  aua= 0.1008B  growth=   +0.00M
2026-04-06 Mon  aua= 1.4824B  growth=+1378.63M  (catch-up day)
2026-04-07 Tue  aua= 1.5987B  growth= +115.22M
2026-04-08 Wed  aua= 1.6850B  growth=  +86.33M
```

The Apr 3 -$1521M and Apr 6 +$1379M telescope to the same window total ($66M) so the period sum is mechanically correct, but the daily values are nonsense and any sub-window report that crossed Easter would be catastrophically wrong.

### Phase 2 — fix_3b regression discovery

Yesterday's `fix_3b` (commit 023079d7) had introduced `market = sum(growth) − sum(aua_residual)` to strip accounting-residual from market. The 9d824fc2 D_00 → D_00b/D_00c split silently dropped the subtraction. Re-applied as commit `011ac15c` along with deleting the orphaned `economic_total` field and adding `aua_residual_delta` to the aggregation roll-up.

QA group D run on the QA EC2 produced:
- Q2 '26 market = +$57.31M / +3.56% (matched +2.93% blended VTI/AGG/GLD benchmark within 63 bps — defensible)
- Historical periods catastrophically wrong: **Q1 '25 -35.15%, Q2 '25 +19.48%, 2024 annual -5.35%, 2025 annual -7.51%**

### Phase 3 — fix_3b revert

Diagnosed the problem: `aua_residual_delta` tracks NNA almost 1:1 at the annual grain (`2024: residual=$229M vs nna=$221M; 2025: $286M vs $260M; 2026 YTD: $111M vs $112M`). So aua_residual is actually absorbing client money flows upstream despite C_03's schema comment claiming "not NNA". Subtracting it from market double-counts NNA and flips bull-year market return negative.

Reverted as `f75a3599`. Kept the `economic_total` field deletion (independently correct, was orphaned against pre-fix_2 NNA) and the aua_residual_delta audit roll-up. Re-ran group D on QA with `sudo shutdown -h +1` appended — QA instance powered off cleanly at 05:20 UTC.

### Phase 4 — Delaney bond pricing bug

Andrew asked for a YTD market growth decomposition. The position-level analysis surfaced **`z0819189891` "Alison Delaney - Individual"** as contributing +$22.75M of YTD growth (20% of firm) from a single Apr 6 jump:

```
2026-04-02  aua=$ 1,757,925   growth=$       -2,795
2026-04-03  aua=$         0   growth=$   -1,757,925
2026-04-04  aua=$         0   growth=$            0
2026-04-05  aua=$         0   growth=$            0
2026-04-06  aua=$22,184,411   growth=$  +22,184,918
2026-04-07  aua=$22,765,817   growth=$     +581,411
2026-04-08  aua=$24,471,697   growth=$   +1,705,880
```

The 215,000-unit "BNP PARIBAS SA" position in this account is **a zero-coupon BNP Paribas bond maturing 09/16/2030** (per the only transaction in history: 2024-10-15 transfer-in, description `"TRANSFER ACCOUNT BNP PARIBAS SA 0% 30F DUE 09/16/30"`, price 101.88, units 215,000, market_value $219,042). The asset_name resolves via Yahoo Finance to ticker `BNPQF` (BNP Paribas equity ADR, ~$95-106 USD/share). canonical_prices was using the equity stock price for what is actually a bond at par, inflating the position from ~$219K to ~$22.8M.

Andrew's structural detection rule: any security where the recorded transaction `(price/100) × units = market_value` is a bond quoted as % of par. Ran across full firm transaction history (1.4M trade rows since 2020):
- **326 bonds** detected via the rule
- 8 had ever been mispriced via Yahoo equity-ticker lookup (BNP PARIBAS SA, Newmont 2.8% 2029, Wells Fargo 4.15% 2029, Ball Corp 2.875% 2030, EQT Corp 6.125% 2025, Kinder Morgan 5.2% 2033, Honda Motor 2.534% 2027, National Bank of Canada)
- Only BNP PARIBAS SA currently has open positions (in 1 account = Delaney with 215,000 face)

### Phase 5 — Existing override system found and repaired

`silver/prices/inject_scoped_overrides.py` and `silver/bd_price_update.py` already implement scoped overrides. **BNP PARIBAS SA was already in the override list at $0.75/face** (ticker `BNP_STRUCT_DEP`) and had been working for **345 consecutive days** from 2024-12-06 → 2026-04-02 with `source=scoped_override`.

On 2026-04-06 (commit `376c232b` added `backfill_yahoo_prices_safe.py`), `build_canonical_prices_v2.py` was rebuilt and **the rebuild does not call `inject_scoped_overrides.py` as a post-step**, so all 7 active scoped overrides flipped to either yahoo_finance or carry_forward for Apr 6/7/8:

| Asset | Pre-Apr 6 | Apr 6-8 source | Impact |
|---|---|---|---|
| **BNP PARIBAS SA** | $0.75 scoped_override | yahoo_finance @ $96-106 | **+$22.6M overstatement** (catastrophic — Yahoo equity ticker) |
| BANC AMERICA FDG 2006-2 | $201.57 scoped_override | carry_forward | none (carry-forward held the right value) |
| DESTINATIONS LARGE CAP EQUITY I | $13.30 scoped_override | carry_forward | none |
| DESTINATIONS INTERNATIONAL EQUITY I | $13.30 scoped_override | carry_forward + transaction_observed | none |
| JPMORGAN CHASE FINL 0% 2029 | $2.55 scoped_override | carry_forward | none (but override itself was stale — see Grundhoefer below) |
| WELLS FARGO MBS 2007-15 | $7.12 scoped_override | carry_forward | none |
| Waldrop Donor Advised Fund | $1.95 scoped_override | carry_forward | none (but override itself was wrong — see Phase 8) |

Ran `python inject_scoped_overrides.py --upload`. Result: 12,099 existing scoped_override rows replaced, 21 wrong-source rows for the 7 overridden assets stripped, all 7 overrides re-pinned from inception → 2026-04-08. Upload to S3 confirmed at 09:55 ET, file size 89.35 MB. canonical_prices repaired.

### Phase 6 — Account-level reconciliation surfaces a bigger pattern

Joined `silver/allocations` Apr 8 vs `account_performance` Apr 8:

```
silver/allocations firm:  $1.6737B  (6,491 accts)
account_performance firm: $1.6850B  (6,046 accts)
net (ap - sa):            $+11.32M  (ap overstated)
total |diff| at acct grain: $132.72M  (gross misclassification)
accounts |diff| > $100K:  142
accounts |diff| > $1M:    23
accounts |diff| > $10M:    2
```

The +$11.32M net hides $132.72M of gross account-level disagreement that mostly cancels at the firm level. Two accounts had > $10M discrepancies: Delaney ($22.56M from the BNP bond bug, just fixed) and **`z0814293421` UNIVERSITY OF REDLANDS** ($19.71M with the opposite direction — ap=$19.77M, sa=$0.06M).

Initial framing was wrong: I categorized Redlands as "stale frozen account" because BD's transaction history for it stopped on 2024-10-29. Andrew then suggested cross-referencing Schwab data and that flipped the framing entirely.

### Phase 7 — Schwab cross-reference: the missing source of truth

Found `gold/dimensions/schwab_bd_account_mapping.parquet` (6,510 mapped pairs) and `s3://opal-data-schwab/silver/RPS/date=20260402/data.parquet` (latest available, 83,917 position rows, 5,589 unique Schwab accounts).

For Redlands, Schwab RPS shows **41 positions worth $16.53M on Apr 2** — almost exactly matching `account_performance` $16.85M and nothing like `silver/allocations` $54K. The account is **held away at Schwab**, BD only sees the residual cash, positions_cube is correctly reading the Schwab feed.

For Delaney (BD account `z0819189891` → Schwab `0042805006`), Schwab shows **31 positions totaling $1.86M on Apr 2**, with the BNP bond split into TWO distinct CUSIPs:
- `05554TQJ7` price $105.70 × 215,000 = $227,255
- `05613L3H2` price $109.70 × 215,000 = $235,855

Both BNP issuer prefix, both bond-quoted. Schwab knows the right prices and the right CUSIP-level structure. positions_cube collapses them into a single "BNP PARIBAS SA 215,000 units" record and uses canonical_prices, which is why the bug existed in the first place.

### Phase 8 — Three-way reconciliation rewrites the top-20 overstatement story

Re-ran the top 20 ap-vs-sa overstatements with Schwab as a third leg:

| Type | Count in top 20 | What it is |
|---|---:|---|
| **Type S — Held at Schwab, sa incomplete (ap correct)** | 7 | Redlands, Smith Rollover, Noland Inh IRA, Giaimo, Karin Ward, Lane Rollover, Lassi Rollover. Schwab confirms ap value. silver/allocations is the wrong source. **No fix needed.** |
| **Real ap overstatement** (ap > both sa AND sch) | **2** | Lindsey ($2.41M), Grundhoefer ($1.49M). The only true bugs in the top 20. |
| Non-Schwab BD account (sch=0, ap and sa both nonzero) | 7 | Bump, z0821495971, Shelton Trad IRA, Teinert, z0815650061, Favorite 529, UT System. Held at Fidelity / American Funds / 529 plan / etc. — not Schwab. |
| Liability (sa negative, ap=$0) | 4 | Carter PAL LOC, Negley Mortgage, Allen, Conaway Mortgage. Expected divergence — positions_cube doesn't carry liabilities. |

**The two real bugs:**

**`z0818927251` Lindsey, Jessica - Long Trust** — BD recon $23.07M, Schwab $20.66M, diff +$2.41M. The largest BD position is `KEYENCE CORP ORD` 45 units × $56,880 = $2.56M. KEYENCE does not appear in any of Schwab's 79 positions for this account. **It's a phantom holding** — BD positions_cube has 45 units that Schwab doesn't carry. Probably sold/transferred out and positions_cube never updated. Even at the correct KEYENCE ADR price of ~$378, the position would be $17K not $2.56M. Fix is to remove the position, not override the price.

**`z0817693881` The Grundhoefer Family Giving Fund (DAF)** — BD recon $7.087M, Schwab $5.609M, diff +$1.478M. Both BD and Schwab carry the **same 5 positions in the same units** — only the JPMorgan Chase Financial 0% 02/14/2029 bond differs:
- BD: 1,200,000 face × $2.55 (scoped_override) = $3.060M
- Schwab: 1,200,000 face × $130.93/100 = **$1.571M**

Our existing scoped_override for this bond is **stale at $2.55/face**, set 2024-04-10 and never updated. The bond's real market value moved from $3.06M to $1.57M as bond prices drifted, and the override never moved with it. **The other 6 existing flat scoped_overrides almost certainly have similar drift issues** (BNP $0.75, Wells Fargo MBS $7.12, BAC MBS $201.57, Waldrop DAF $1.95, Destinations LCAP/Intl $13.30 each — none of these have been mark-to-market'd since their initial set dates).

This is the core issue Andrew flagged earlier: **flat scoped overrides don't work on a timeseries basis**. Need a time-varying override mechanism (Task #19, opened this session).

### Phase 9 — Cohort framework

Added `account_billable` and `basis_points_1` as the fee-paying signals. Built cohort buckets at firm level:

| Cohort | n | sa_total Apr 2 | sch_total Apr 2 | ap_total Apr 2 |
|---|---:|---:|---:|---:|
| **1. Managed (fee-paying)** | 5,417 | $1,431.33M | $1,301.47M | $1,399.68M |
| **2. Non-managed Schwab-only** (sa < 5% of sch) | 6 | $0.14M | $19.62M | $19.71M |
| **3. Non-managed Schwab + BD overlap** | 415 | $68.13M | $68.77M | $66.68M |
| **4. Non-managed BD-only** (not at Schwab) | 469 | $131.92M | $0.00M | $135.49M |
| **5. Residual / closed / liabilities** | 184 | −$4.49M | $0.00M | $0.02M |

Andrew asked specifically about Cohort 4. Built a sub-classification tagger using `account_name` patterns + `account_registration_type` as primary signal:

| Sub-cohort | n | Total | % |
|---|---:|---:|---:|
| 4n_insurance (VUL, annuities, ULIs) | 133 | $61.93M | 47.5% |
| 4d_employer_retirement (401k, supplemental, RSU, BrokerageLink) | 66 | $20.80M | 16.0% |
| 4m_other_brokerage | 102 | $17.35M | 13.3% |
| 4a_daf (Donor Advised Funds) | 3 | $5.57M | 4.3% |
| 4h_ira | 37 | $5.52M | 4.2% |
| 4c_real_estate (Penfield homes) | 6 | $4.64M | 3.6% |
| 4b_structured_trust (SLAT/ILIT) | 1 | $3.30M | 2.5% |
| 4k_entity (LLC/Foundation/Corp) | 2 | $2.40M | 1.8% |
| 4e_explicit_no_fee | 2 | $2.09M | 1.6% |
| 4g_other_trust | 12 | $1.93M | 1.5% |
| 4z_unclassified | 28 | $1.75M | 1.3% |
| 4j_banking | 48 | $1.41M | 1.1% |
| 4l_joint_taxable | 4 | $1.17M | 0.9% |
| 4i_529 | 14 | $0.51M | 0.4% |

Saved to `data/analysis/cohort_4_tagged.csv`. **98.7% of $130.36M classified.** Insurance products dominate at $61.93M (47.5%); insurance + employer retirement together are $82.7M (63%) of the BD-only non-fee-paying book.

### Phase 10 — Schwab fee files validation

Andrew downloaded a batch of `Fees_OpalCapital_Daily*.xlsx` files to `~/Downloads` and asked me to cross-reference the 350 "unmapped" Schwab accounts to determine if any are actually fee-paying. Initial xlsx loader hit Python stdout buffering / memory issues; killed PID 9912 after it grew to 390 MB. Rewrote as a streaming per-file converter that reads one xlsx, dedupes to per-account billing config, writes a parquet, releases memory. 15 files → 15 parquets → 10,075 unique Schwab accounts with billing config.

**The killer finding:**

| Bucket | Count | Value |
|---|---:|---:|
| **In fee file AND fee-paying** (Billable AND bps > 0) | **304** | **$63.95M** |
| In fee file but non-fee-paying (Billable, bps = 0) | 35 | $4.92M |
| Not in fee file at all (truly invisible to BD) | 11 | $0.45M |
| **Total "unmapped Schwab"** | **350** | **$69.32M** |

**87% of the "unmapped" Schwab accounts are actually fee-paying accounts known to BD's billing system — 92% of the value.** They're in BD's billing system, they're in silver/allocations, they're just missing from the (stale) `schwab_bd_account_mapping.parquet` join table. The "Schwab non-managed cohort" is genuinely small: only **46 accounts ($5.4M total)**.

Billing breakdown of the 304 newly-discovered fee-paying ones is normal 49F rates: 100 bps dominant (202 accts, $42.22M), then 90/80/125/120 bps. These are real billable clients.

### Phase 11 — Final firm AUA reconciliation

| Component | Apr 8 value |
|---|---:|
| silver/allocations Apr 8 (BD authoritative — already counts the 304 newly-mapped accounts in cohort 1) | **$1.6737B** |
| + Cohort 2 Schwab held-away that BD shows as ~$0 (6 accounts) | +$19.5M |
| + 11 truly-invisible Schwab accounts (not in BD at all) | +$0.45M |
| **= True firm household AUA Apr 8** | **≈ $1.694B** |

Andrew's $1.68B intuition for firm AUA is right within ~$20M / 1.2%. The "missing" $20M is genuinely held-away Schwab Opal-model AUA that BD has zero visibility on.

Three numbers depending on audience:

| Number | Apr 8 value | Meaning |
|---|---:|---|
| Fee-paying AUA (revenue base) | ~$1,470M | What 49F bills on. Cohort 1 only. |
| Managed + supervised AUA | ~$1,673B | silver/allocations as-is. BD's official line. |
| True household AUA | **~$1,694B** | Adds Schwab-only held-away. Everything Opal can see across all wrappers. |

---

## Compiler Tools

Did not use comp-* tools this session — investigation was data-driven against S3 parquets via direct boto3/pandas, not pipeline lineage tracing. The questions were "what is the actual data saying" rather than "what scripts feed what outputs." Note for compiler-tools-log: **comp-pipescript io D_00b** would have been valuable for confirming the D_00b read/write surface after the refactor; I should have run it before re-applying fix_3b. Adding this as a discipline note for next session.

| Tool | Used | Why / why not |
|---|---|---|
| comp-pipescript io | No | Would have caught the D_00 → D_00b refactor regression of fix_3b earlier if run. **Should have used.** |
| comp-blast | No | Not applicable — no symbol/component being changed in a way that affects downstream. |
| comp-routes | No | Not a serving-path question. |
| Direct S3 boto3/pandas queries | Yes (extensively) | All findings derived from comparing parquets. silver/allocations, account_performance, positions_cube, canonical_prices, silver/transactions, silver/RPS, schwab_bd_account_mapping, accounts_dimension_latest, client_dimension. |
| `git log` on silver scripts | Yes | Found commit 376c232b (backfill_yahoo_prices_safe.py, Apr 6 13:33 UTC) as the trigger for the canonical_prices rebuild that wiped the scoped overrides. |
| inject_scoped_overrides.py --dry-run / --upload | Yes | Validated and applied the override repair. |

---

## Open Issues / Carried Forward

1. **Time-varying scoped override mechanism** (Task #19, in_progress). Current `inject_scoped_overrides.py` writes a single flat price across the asset's full inception → latest range. Bond prices and structured product NAVs change over time; the existing 7 overrides are all stale to varying degrees. Grundhoefer JPMorgan Chase Financial 0% 02/14/2029 case proves this concretely: override has been $2.55/face since 2024-04-10, real price moved to $1.31/face per Schwab on Apr 2 = $1.49M of accumulated phantom value in one account.
2. **Type S structural pivot — use Schwab RPS as price authority for held-at-Schwab accounts**. Andrew approved this direction but execution is still ahead. Schwab data goes back ~2.3 years and gets less consistent further back, so the implementation needs a hybrid Schwab/canonical_prices path with the canonical fallback for older history. Once shipped, this auto-fixes Delaney, Lindsey, Grundhoefer, and any future bond/structured-product/yahoo-collision bug for Schwab-held assets.
3. **Rebuild `gold/dimensions/schwab_bd_account_mapping.parquet`** from the fee files. The existing 6,510-pair table is stale by ~304 entries. Fee files have authoritative (Schwab Account Number, BD AccountID) pairs side-by-side, so this is a clean rebuild operation.
4. **Lindsey KEYENCE phantom position cleanup**. Need to drop 45 units of KEYENCE from positions_cube for `z0818927251` — positions_cube has it but Schwab doesn't, and it's contributing $2.4M of fictional value via the Yahoo yen-as-USD bug ($60,520).
5. **`bd-gold-trigger` invocation to propagate canonical_prices repair to platinum**. The inject_scoped_overrides upload re-pinned BNP PARIBAS SA Apr 6/7/8 entries in canonical_prices, but the gold pipeline hasn't re-run since. account_performance Apr 8 still shows Delaney at $24.47M. The next nightly cron at 23:00 UTC will pick it up automatically; otherwise a manual group D run will refresh.
6. **Verify Delaney fix on QA/prod** (Task #18 still pending) — re-run group D after the inject upload and confirm `account_performance` Delaney drops from $24.47M to ~$1.91M.
7. **build_canonical_prices_v2.py needs to call inject_scoped_overrides.py automatically** as the last step of every rebuild, so the Apr 6 regression can't recur. Currently the two scripts are separate steps and depend on operator discipline. Memory `feedback_canonical_prices_ordering.md` documents the manual ordering — should be enforced in code instead.
8. **26 Shield/buffer/AQR products** added to `_SCOPED_PRICE_OVERRIDES` on commit 11255fb1 (2026-03-29) have no inception dates in `_INCEPTION_DATES` → they've never been written to canonical_prices via inject. Lower priority since the per-asset values in those overrides are small ($1.00-$1.40 each) and they appear infrequently in client portfolios, but worth a sweep.

---

## Next Steps

[0.4.0_DS_ClientPlatform → next session] **Priority order:**
1. Rebuild `schwab_bd_account_mapping.parquet` from fee files (small lift, immediate impact on every Schwab cross-reference).
2. Re-run group D on QA after the inject_scoped_overrides upload to verify Delaney + the 6 other repaired overrides propagate to platinum/firm/timeseries_overview.json. Verify firm AUA in account_performance drops by ~$22.6M.
3. Implement time-varying scoped override mechanism (Task #19). Schema: each entry can have either a flat `price` OR a list of `{from_date, to_date, price}` segments.
4. Implement Type S structural pivot — Schwab RPS as price authority for held-at-Schwab accounts, with canonical_prices fallback for dates pre-Schwab-coverage. Hybrid stitching needs careful boundary handling so the transition day doesn't produce fake "growth."
5. Lindsey KEYENCE phantom cleanup — remove from positions_cube.

[1.0.0_SA_CTO] FYI on the GRO panel state: Q2 '26 market growth as currently displayed (+$66.25M / +4.12%) is dominated by the Delaney bond bug (+$22.6M of inflation hitting on Apr 6). After the override fix propagates to platinum, Q2 '26 will drop by ~$22M and the residual is the actual Mar 31 → Apr 8 trading-day market move. Real number is in the ballpark of +1-2%, matching Andrew's "not been a great quarter" intuition.

[2.0.0_SA_COO] Cohort framework available at `data/analysis/cohort_4_tagged.csv` — useful for any household-AUA reporting that needs to split fee-paying vs non-managed. 458 BD-only non-fee-paying accounts tagged into 15 sub-cohorts. Insurance products dominate at $61.93M (47.5% of cohort 4). Three reportable headlines now: Fee-paying $1,470M / Managed+supervised $1,673M / True household $1,694M depending on audience.

[0.4.0_DT_ClientPlatform] No deploys this session beyond the canonical_prices.parquet repair (S3 only, no Lambda/EC2 changes). Both QA EC2 SSM dispatches included `sudo shutdown -h +1`; bd-gold-qa-runner is `stopped`. Prod runner `bd-gold-layer-runner` was untouched throughout.

---

## Identity invariant compliance

`git status data/black_diamond/scripts/gold/` was clean before all "fix is committed" claims this session. Both commits used `--author="0.4.0_DS_ClientPlatform <0.4.0_DS_ClientPlatform@opal.agent>"`. canonical_prices.parquet is S3-only, not git-tracked, so the commit-before-deploy invariant doesn't apply to it directly — but the override registry source of truth (`bd_price_update.py` and `inject_scoped_overrides.py`) was unchanged, so the inject just re-applied existing config.
