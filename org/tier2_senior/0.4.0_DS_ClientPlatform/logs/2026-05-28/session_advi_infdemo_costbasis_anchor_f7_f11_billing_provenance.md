# Session Log — 0.4.0_DS_ClientPlatform — 2026-05-28

**Agent:** 0.4.0_DS_ClientPlatform (Tier-2 DS, ClientPlatform / ADVI Inflection)
**Driver:** Andrew direct (IWM demo-prep, early-afternoon client demo) + CTO (1.0.0_SA_CTO) demo-batch dispatch
**Theme:** Inflection (IWM) demo-prep — Cost Basis panel reconciliation + several data-provenance investigations + F11 fee-sliced flows emit.

---

## Headline outcomes

1. **F4 Cost Basis reconciliation — SHIPPED + CVO-VERIFIED.** Root-caused the "Cost Basis by Year" over-statement, fixed INF_B_02 via canonical-holdings anchor, deployed + regenerated, CVO PASS.
2. **F11 fee-sliced windowed NNA — BUILT + VALIDATED + committed; deploy handed to CTO/AE.** New per-advisor `fee_breakdown` emit in INF_D_00c.
3. **5 data-provenance investigations answered** for Andrew's call (F7, F5, composition donut, account-67 NNA, HH226 unrealized/realized/billing, billing "TTM" mislabel).

---

## Thread 1 — F4: Cost Basis & Tax Status reconciliation (Peter Lee)

**Andrew Q:** "how do these numbers reconcile?" Unrealized card ($27.1M cost basis) vs Cost Basis by Year table ($274M) — ~10x apart.

**Findings (empirical, live S3):**
- The two panel halves come from DIFFERENT sources: Unrealized/Realized cards = Orion tax API (`silver/api_dims/tax_unrealized` / `tax_realized`); Cost Basis by Year = our canonical lots (`gold/lots/lots_latest.parquet`, INF_B_02).
- Andrew ground truth: entire Orion AUA = $205.53M. `gold/canonical/holdings_*` = $205.6M firm / $166.1M Peter (CORRECT, drives the AUA bar). The separate `gold/holdings/*` ($348M) is a divergent/stale artifact (not the lot-builder's source).
- **Root cause:** INF_B_02 builds FIFO lots from `silver/transactions` ONLY (no holdings input). Transaction history doesn't net to Orion's positions API → **3.15x unit over-retention** (Peter: 51.6M lot units vs 16.4M canonical). 90% = cash-sweep funds (no sell-side sweep-out txn), + 14,795 phantom (account,ticker) positions, + buy history predating the silver window. Chasing missing SELL_DESCs closes only ~6% — FIFO-from-txns structurally cannot tie to the positions API.

**Fix (canonical-anchor):** INF_B_02 now loads `gold/canonical/holdings_*` as the authoritative position anchor; uses FIFO lots only to ATTRIBUTE the position across purchase years. Per (account,ticker): drop if absent/H<=0 (kills phantom); scale traceable lots to H (proportional, preserves year+blended-cost); residual at canonical price for held-but-untraceable. Fail-open if anchor unavailable.
- **Commit b570b342a** (+ TO ADVI_INFDEMO.F4). Deployed CLOUD + S3 (safe-deploy MATCH). Regenerated `lots_latest` (INF_B_02 --upload) + advisor `book.json` (INF_D_02 --upload). HALT_ACK on push (4 routine pending msgs, no STOP).
- **Validated:** Peter by-year MV $165.2M vs canonical $166.1M (0.995x, was 3.15x); cost_basis $162.8M just below MV; +$2.43M gain.
- **CVO VERIFIED (a8be3399e):** 8,295/8,295 (account,ticker) units == canonical exact, 0 phantom. COO RAVC2-ACCEPTED.
- **Demo posture:** per-year breakdown SUPPRESSED for demo (CVO CONCERN: per-year attribution is best-effort under proportional scaling — Peter 2025 reads -$5.2M, 2026 holds 49%; TOTAL is correct). The reconciled total + AUA bar carry the panel.
- **Post-demo follow-on TO filed: ADVI_INFDEMO.F4-followon (commit 3765c054e)** — proper per-year attribution + $0.87M residual (21 lot-ticker!=canonical-ticker edge cases).

## Thread 2 — F11: fee-sliced windowed NNA emit

**Problem:** Exec Summary "Fees:" toggle didn't slice Inflows/Outflows/NNA for Inflection — leaderboard entry lacked `fee_breakdown` (49F has it). NOT a FE regression (RD/CTO confirmed).

**Explore findings:**
- Source data EXISTS for a TRUE split: `canonical_nna` (per-account flows) + `silver/api_dims/billing` (per-account `is_fee_earning`, 732/874 fee-earning), joinable on account_id. (49F's own split is partly a backfill heuristic, `no_flow_join`.)
- Inflection `timeseries.json` has NO real fee sub-streams (`nna_canonical_fee_paying/_no_fee` absent across 2194 pts) → the Lifetime Activity fee-split is SYNTHETIC (FE ratio). Option A would be the first REAL split.

**Built (Option A, commit ac95741d6):** INF_D_00c loads billing → `{account_id: is_fee_earning}`; in `compute_leaderboard_entries` partitions the SAME windowed `canonical_nna` attributed flows by fee status → `entry.fee_breakdown.{fee_paying,no_fee}` (mirrors 49F PlatinumFeeBreakdown). Sums by construction.
- **Validated (dry-run):** flow sum-invariant fee_paying+no_fee==all ALL PASS across QTD/YTD/MAX x 4 advisors; AUA split reconciles. ds-commit-gate PASS.
- **Status:** CTO+Andrew GO'd the ship; rollback-first deploy sequence given (CTO 1540Z). Andrew then reassigned the deploy to CTO/AE — **DS handed off the ship sequence.** Code committed local (ac95741d6, not pushed). FE ready (RD .003, emit target `platinum/firm/leaderboard.json`, no FE change).

## Thread 3 — provenance investigations (Andrew call-prep)

- **F7 (L3 tax-status bar absent at client level):** FRONTEND WIRING GAP, not data miss. `detail.json#summary.tax` DOES carry household taxable/tax_deferred/tax_free (hh 108: $2.86M, totalTaxAua>0). `l3Tax` adapter (AdvisorBookClientDetail.tsx:126-146) isn't mapping it. Gotcha: out-of-scope advisors have stale Apr-27 thin detail.json (no summary.tax) — test against fresh peter_lee hh. Answer + wire spec sent CTO + RD.
- **F3b (active_since/role):** both FE-side. `active_since` emitted ("2023-10-02") → FE wiring (RD wired d158fe85). Role emitted as `role_breakdown.{role}.pct_of_tagged`; Andrew ruled IWM has no explicit roles → chip hidden, no DS change.
- **F5 (Raeleen "newest relationship"):** correct — joint-max relationship_since 2026-04-23 (tie w/ Therese Gesell, Raeleen wins on AUA). CVO independently corroborated her hh 511 is a $0.01 shadow household (dedup item, post-demo). household_id is loosely chronological (Pearson 0.66) — only high IDs reliably newer; low/mid IDs all the ~2023-10 onboarding batch.
- **Composition donut empty (all IWM advisors):** NOT my regen. `composition.mix` lives in separate `composition.json` (INF_D_03), canonical keys + positive MVs intact (equity/fixed_income/cash/alternatives). INF_D_02 (what I regenerated) writes no composition. → FE fetch/merge wiring issue. Answered RD.
- **Account 67 NNA = $10.83 (vs $183K AUA):** CORRECT, not a calc bug. Account funded 2023-01-04 by a $108K "Internal Account Journal In" (intra-firm transfer), correctly EXCLUDED from NNA per the cashflow taxonomy (`orion_cashflow_taxonomy.yaml`: Internal Account Journal In -> bucket Internal; External Account Activity In -> NNA). Only external inflow was $10.83. AUA = market value (includes internal funding); NNA = external net-new only. Idiosyncrasy, not canary.
- **HH 226 (Judith Ozinga) Unrealized/Realized/Billing provenance:** all VENDOR (Orion), no modeling. Unrealized $790K / Realized $1.87M cost basis = SUM of per-account Orion tax-API figures (entirely acct 650 / the taxable Trust; 488 IRA + 67 Roth = $0, Orion doesn't track cost basis for tax-advantaged accts). We only sum to household + classify reg_type into buckets + AUA-weighted avg fee.

## Thread 4 — Billing "TTM" mislabel (Andrew suspected fee imputation)

- **Verified:** Orion fee data STARTS 7/1/2025 (snapshots before are NaN) — confirms Andrew's Q3-2025 recollection. NO imputation our side (orion_billing_dim.py pulls Orion "Billing Dim" query, default 3y window; build_billing_dim.py parses+sums raw; INF_D_02 sums latest snapshot per account to household).
- **`fee_amount` = Orion's actual "Billing Fee Amount," CUMULATIVE since 7/1/2025**, accruing each quarter (acct 650: $3.2K Q3'25 -> $6.1K -> $9.0K -> $11.8K). Total Fee $30,280 = sum of 3 accts (488 $17,516 + 650 $11,809 + 67 $954).
- **"Total Fee (TTM)" label is INACCURATE** — it's cumulative-since-7/1/2025 (~11 months, growing), NOT trailing-12-months. Flagged CTO (1605Z) + RD (1606Z) for FE relabel -> "Total Fee (since 7/1/2025)" + tooltip. No DS/gold change.

---

## Commits this session (author 0.4.0_DS_ClientPlatform)
- `b570b342a` — INF_B_02 canonical-anchor cost-basis fix + TO ADVI_INFDEMO.F4 (pushed CLOUD, deployed, regenerated).
- `3765c054e` — TO ADVI_INFDEMO.F4-followon (post-demo per-year attribution + residual). Local.
- `ac95741d6` — INF_D_00c F11 fee_breakdown emit. Local (deploy handed to CTO/AE).
(CVO verify of F4 = a8be3399e, CVO-authored.)

## Open / handoffs
- **F11 deploy:** CTO/AE own it (ac95741d6, rollback-first per CTO 1540Z). Acceptance: regen leaderboard.json + CVO sum-invariant verify.
- **F4-followon:** post-demo — proper per-year attribution + $0.87M ticker-normalization residual.
- **F7 wire:** RD wiring l3Tax adapter.
- **Billing TTM relabel:** RD FE relabel (CTO 1605Z).
- **Composition donut:** RD FE fetch/merge fix.
- **F10 (noted):** post-demo DS TO — day-by-day advisor revenue vs snapshot estimate (not yet authored).
- **Standing queue UNTOUCHED this session** (demo work took over): ADVI_DEMOV1.003/004/006, ADVI_VALFIN.010.
- **Stale gold/holdings/* ($348M) artifact:** confirm its consumer + retire (lower-pri, not lot-builder source).

## Notes
- Watcher: ran /watcher loop, multiple kill+relaunch cycles (auto-respawn-interrupt-lost handling); healthy at session end.
- MSTR pre-reboot-log directive (2026-05-27T14:53Z) was stale (reboot already happened); this log supersedes.

---

## UPDATE — end-of-session state (~1740Z, holding per Andrew)

### F11 (fee-sliced NNA) — SHIPPED + follow-ons
- **Leg 0 (original fee_breakdown, ac95741d6): LIVE + CVO-verified + CLOSED.** AE 0.6.1 deployed (QA->PROD, rollback armed); CVO PASS on live leaderboard.json (20 entries, sum-invariant exact, Peter MAX nna 108.68M = 102.89M fee + 5.79M no_fee). The Exec Summary Fees toggle re-slices inflows/outflows/nna.
- **Leg 1 (new_clients fee-split, 9950a3f2c): SHIPPED THIS SESSION (Andrew "just get clients fixed right now").** Was flattened (fee_breakdown.*.new_clients=None). Fix = any-fee-paying-account rule. I ran the gold regen (INF_D_00c --upload, rollback-first, backup _rollback/leaderboard.json.pre-F11newclients-20260528T173355Z), verified additive-only + sum-invariant (Peter MAX 198=184+14), AE 0.6.1 fired CF (I2UXSDO7FFZKPXRW9VXIZS1VQJ). LIVE.
- **Leg 2 (Lifetime Activity real daily fee sub-streams, 982394f01 LAMBDA inf-portal-advisor-publisher): BUILT+VALIDATED, DEFERRED POST-DEMO (Andrew).** Root cause of "Lifetime Activity vs Flows NNA varying" = timeseries fee-split was SYNTHETIC (no fee sub-streams emitted) while leaderboard split is real. Fix emits nna/inflows/outflows _canonical_{fee_paying,no_fee} via same billing is_fee_earning join (sum-invariant exact, 2194 pts). Deploy = Terraform Lambda (AE/CloudOps lane) + RD adapter switch off synthetic ratio. OPEN AUA-feasibility gate (COO 173202Z): leg-2 emits NNA-split but NOT total_aua_fee_paying/_no_fee -> AUA toggle would go inert; needs either real per-account daily AUA-MV split (option a) or RD per-metric hasFeeSplitSeries (option b). Feasibility read pending (post-demo).

### ETF retag (ADVI_INFDEMO — Andrew-direct ASAP) — SHIPPED + CVO PASS
- PFDE/PFOE/PCHI mistagged security_type=single_stock (showed under "Name" not "Basket"). Root cause: INF_D_07a classifier over-trusted Orion product_sub_type (vendor tags these ETFs 'Common Stock' under 'Stock/ETF'); no assets_v2 field discriminates -> asset NAME only signal.
- **Sweep caught a 4th: IDVZ** (the whack-a-mole COO warned of).
- Fix (f2f813348): ETF-recovery branch (Stock/ETF universe only) — tight name pattern (\bETF\b|EXCHANGE TRADED|\bFD TR\b|\bFUND TRUST\b) + ticker backstop. Validated: EXACTLY 4 flip single_stock->etf, ZERO false positives across 487 tickers. Committed+pushed+safe-deploy MATCH; ran regen (backup _rollback/firm_concentrations.json.pre-ETFretag-20260528T172352Z); CF fired (AE~A I4HAK7... + AE0.6.1 I5FNUW... — 2 redundant, harmless). CVO PASS (display-artifact; full-universe on DS attestation per ADVI light-touch). LIVE.
- Andrew also ran a parallel FE band-aid (RD overrides) for instant demo correction; RD pulls it now the data fix is live.

### Billing "TTM" mislabel — FLAGGED + RD RELABELED
- Andrew suspected fee imputation. Verified: NO imputation; fee_amount = raw Orion "Billing Fee Amount". Orion fee data STARTS 7/1/2025 (snapshots before = NaN; confirms Andrew's Q3-2025 recollection). The figure is CUMULATIVE-since-7/1/2025 (accrues quarterly: acct 650 $3.2K->6.1K->9.0K->11.8K), NOT trailing-12-months. "Total Fee (TTM)" label inaccurate.
- RD relabeled "Total Fee (TTM)" -> "Total Fee (since 7/1/2025)" (c9fab075). Value untouched.

### Account 67 NNA ($10.83 vs $183K AUA) — EXPLAINED (not a bug)
- Funded 2023-01-04 by $108K "Internal Account Journal In" (intra-firm transfer), correctly EXCLUDED from NNA per cashflow taxonomy. Only external inflow = $10.83. AUA=market value (incl internal funding); NNA=external-net-new only. Idiosyncrasy, not canary.

### HH 226 (Judith Ozinga) Unrealized/Realized/Billing provenance — call-prep
- All VENDOR (Orion tax + billing APIs). We only sum per-account -> household + classify reg_type buckets + AUA-weighted avg fee. No modeling. Unrealized $790K / Realized $1.87M cost basis = entirely acct 650 (taxable Trust); 488 IRA + 67 Roth = $0 (Orion doesn't track cost basis for tax-advantaged).

## Commits added this session-continuation
- `9950a3f2c` INF_D_00c new_clients fee-split (leg-1, SHIPPED+CF).
- `982394f01` inf-portal-advisor-publisher Lambda timeseries fee sub-streams (leg-2, DEFERRED post-demo).
- `f2f813348` INF_D_07a ETF-recovery classifier (SHIPPED+CF).
- TOs: `3765c054e` F4-followon; `a2c6d77d5` F11-followonB (timeseries); session-log `0a1acef96`.

## Open / handoffs (end of session)
- **F11 leg-2 (Lifetime Activity)**: DEFERRED post-demo. Lambda Terraform deploy (982394f01) + RD adapter switch + the AUA-split feasibility decision (option a real per-account daily AUA-MV vs option b RD per-metric). My feasibility read owed to COO post-demo.
- **F4-followon (ADVI_INFDEMO.F4-followon)**: post-demo per-year attribution + $0.87M ticker-normalization residual.
- **F10**: post-demo DS TO — day-by-day advisor revenue vs snapshot estimate (not yet authored).
- **Standing queue UNTOUCHED**: ADVI_DEMOV1.003/004/006, ADVI_VALFIN.010.
- **Stale gold/holdings/* ($348M) artifact**: confirm consumer + retire (lower-pri).
- **HOLDING per Andrew (~1740Z)** — no new work until his advice; watcher live for reachability.

### Demo-ready scorecard (going into the demo)
- PFDE/PFOE/PCHI/IDVZ ETF retag: LIVE (Basket).
- Fees toggle flow split (inflows/outflows/NNA): LIVE.
- New-clients fee-split: LIVE.
- Billing "Total Fee" relabel: LIVE (RD c9fab075).
- Cost Basis by Year reconciliation ($166M): LIVE (per-year breakdown suppressed; totals carry).
- Lifetime Activity NNA fee-split: SYNTHETIC (knowingly deferred post-demo).
