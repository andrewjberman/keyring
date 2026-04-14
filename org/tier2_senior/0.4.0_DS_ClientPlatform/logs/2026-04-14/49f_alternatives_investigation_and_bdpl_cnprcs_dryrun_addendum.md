# Session Log — 49F Alternatives investigation + BDPL_CNPRCS dry-run addendum

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-14
**Mode:** Direct Andrew session (no MCP comms until final CTO handoff at end of session)
**Projects touched:** BDPL_CNPRCS (PRD updated), BDPL_ASTDIM (brief contributions), ad-hoc Schwab sync

---

## Starting question

Andrew asked why 49 Financial's portal-reported "Alternatives" dropped from $84-93M a few days ago to $61.8M on the 2026-04-10 gold run, when the historical monthly range has been $65-90M. He also asked whether silver/allocations carries a certified AUA reference for alts / structured notes / insurance.

## What I found

### No silver-certified Alternatives reference
`silver/allocations/*.parquet` is relationship/account-level (92 columns), carries `account_market_value` and `cash_market_value`, but has **no asset-class column**. It DOES carry account-level classification via `account_type` (Insurance 101 accts, Annuity 4, TermLife 15 for 49F), `account_category` (Insurance 4), `account_registration_type` (INSURANCE_OTHER 100). These classify the account registration, not the holdings. Insurance+Annuity+TermLife accts sum to $62.1M for 49F — coincidentally close to the gold Alternatives $61.8M on 04-10, but they're different universes.

Portal Alternatives is entirely derived downstream in `D_03.composition_artifacts.py`, `D_00b.portal_timeseries.py`, `C_06.client_mix_timeseries.py` via `classify_series` → `ETFClassifier` (DynamoDB) + `B_01b.classify_new_securities.py` keyword heuristics.

### The BD Asset_OpalCapital_dimTable is the missing join-reference
Andrew staged 16 xlsx exports covering 2020-03-06 → 2026-04-13 (pre2024/asset_dim/2026 folders). Combined: 3.93M transactions, 10,634 unique AssetIDs. Carries per-txn: TransactionID, Relationship ID, AccountID, Asset SuperClass, Class, Segment, AssetID, Asset Name, Symbol, Ticker, CUSIP, Alternative Identifier, Trade Date, Settle Date, Entry Date, Price, Transaction Type/Sub Type, Action, External Flow, Has Contra Account, Contra Account Number, Description, Last Dividend, Coupon Rate, First/Last Payment Date, Custodial Cost Basis Sync.

Join-key coverage analysis on 2024-25 slice (8,790 assets):
- AssetID: 100% (but NOT stable across BD reclassifications — NBN case has 2 AssetIDs for 1 CUSIP after BD moved it from Equities/Small Cap Core → Equities/Financials)
- Symbol: 100%
- CUSIP: 88.4%, essentially unique (1 duplicate in 7,767), ticker→CUSIP has zero conflicts → **best durable join key**
- TransactionID: 100%, immutable → **best enrichment key**
- Ticker: 69.5% — missing on structured notes + annuities
- Alternative Identifier: 12.3%
- Asset Name: 98.9% (fuzzy, case-variable)

### BD does NOT have an "Alternatives" SuperClass
49F 04-10 matched $1,641M of $1,653M holdings_lots to asset_dim. BD SuperClass distribution:
```
Equities                 $1,223M  (74.6%)
Fixed Income             $  319M  (19.4%)
To Be Classified         $   70M  ( 4.3%)
Cash & Cash Equivalents  $   21M  ( 1.3%)
Unclassified             $    5M  ( 0.3%)
DIVERSIFIER              $    2M  ( 0.1%)
```
BD classifies equity-linked Shield/Buffer notes as `Equities` (tracks underlying exposure). Annuities and structured products land in `To Be Classified`. There is no 1:1 mapping from BD SuperClass to our current "alternatives" bucket.

### Per Andrew 2026-04-14: "Everything in BD's TBC = Alternatives in our book"
Inspected top 40 TBC holdings for 49F. Content mix:
- $27M structured notes (Shield/Buffer/Point-to-Point/Barrier)
- $3-4M CITs (BD-internal cusip prefix)
- $1.6M target-date funds
- $228K annuities + scattered
- $500K private funds / Blackstone BXPE / Variant Alternative Income
- $561K options
- $24M issuer-ADR equities misclassified (BNP $23M, Atlas $1.1M, Eventide $823K, etc.)
- $10M balanced/multi-asset funds

Per Andrew: treat all of it as alternatives. The $23M BNP was his observation — flagged as a probable bond not a $23M equity ADR position.

### BNP Paribas phantom diagnosis (and scan)
- Account z0819189891, asset_name "BNP PARIBAS SA", CUSIP 05613L3H2, 215,000 face-value units, cost $1.02/unit (101.88% of par). Real MV ≈ $219K.
- Gold tagged with ticker `BNPQF` (equity ADR). `build_canonical_prices_v2.py` → Yahoo → $107.01 → MV = 215,000 × $107.01 = **$23.0M phantom**.
- Scan for similar pattern (cost<$5, current_price>$20, yahoo_finance source, size>$100K): confirmed 3 real bond phantoms, ~$24.3M total — BNP $23.0M → $219K, WFC 4.15% 01/24/2029 $860K → $9K, NEWMONT 2.8% 10/01/2029 $595K → $4K.
- All three are corporate bonds whose parent-issuer equity ticker cross-contaminated Yahoo price lookup. CUSIP-primary price resolution (WP-5) structurally fixes.

### Rotation-visibility via asset_dim (missing link for phantom FIFO)
Asset_dim carries 25,985 non-cash rotation-OUT events in the 2024-25 slice across 22,241 unique (account_id, asset_id) pairs — ACAT Out (4,304), EF Transfer Out (10,631), JNL-SHORT (4,011), FTP-DEBIT (2,237), plain Transfer Out (422). Most are already captured in our silver/transactions via matching Transaction Type = "Transfer Out" → caught by FIFO SELL_TYPES. The real gap isn't the event, it's the `(account_id, asset_name)` keying in `adhc_histry_005_phantom_schwab.py` (10,832 phantoms / $177M). Name-drift across corporate actions / share-class changes / fund renames breaks matching. CUSIP-keyed FIFO (WP-9) structurally fixes.

Contra Account is populated on only 5,795 of 2.3M txns (almost all mgmt-fee rebates + cash journals) — NOT the Schwab-counterparty bridge I initially hoped.

### Firm-level reconciliation — I was wrong, corrected
Initial framing claimed +$208M overstatement. **This was incorrect.** I was comparing silver/allocations ($1,682M) against raw `gold/holdings_lots` SUM ($1,890M) — the raw internal stage, not the pipeline output. Corrected:
```
Silver authoritative:          $1,681,963,293
Gold pipeline (firm_mix_views): $1,624,913,423
Delta:                          -$57,049,871  (-3.39%)
  of which cash (silver only):  -$40,496,558
  residual non-cash:            -$16,553,313  (-1.01%)
```
Andrew's "always within a couple percent" description matches the pipeline-output number. The pipeline already drops the 2,073 orphan accounts ($237M) from raw holdings_lots via architect-lookup + AP gate + ghost exclusion. Orphans aren't inflating firm AUA.

Walked back the WP-10 brief framing. The real residual to chase is $17M non-cash + $40M cash structurally addressable via WP-5.

### Orphan deep-dive — dedup hypothesis collapsed
Of the 2,073 gold-only orphans ($237M):
- 149 validated by Schwab RPS 04-10 ($36.1M) — real Schwab-only positions
- 1,277 share relationship_id with silver under different account_id ($206.4M) — my initial "account-ID renumbering" hypothesis
- 796 truly orphaned relationships ($30.7M)

Position-level test on Waldrop rel z0880615 (14 accounts, 7 orphan + 7 silver-joint): **zero exact unit matches** between any orphan and silver-side twin. "Waldrop DAF" vs "NATIONAL CHRISTIAN CHARITABLE" (both DAFs but distinct vehicles), "Waldrop Investments LLC" vs "WALDROP INVESTMENTS LLC-CORPORATION" (LLC reorganized to C-corp). Names similar, positions different — these are DIFFERENT real accounts.

Mitchell rel z0880629 similar: orphan z0814305081 (100 positions, Kensington/JHQTX/PIMIX institutional shares) vs joint z0812974881 (25 positions, Vanguard/Janus/SPDR short-duration ETFs + T-bills). ZERO position overlap. Legacy 401(k) recordkeeper account + current Schwab brokerage cash-mgmt sleeve, same client, both real at different points in time.

**Per Andrew:** the $200M of orphans is presumed to exist somewhere in silver under different account_ids — we just can't see it from our current vantage. Do NOT auto-retire. The architect-filter correctly handles them for firm aggregations.

### Cash strategy — dual classification, fold-at-read
Per Andrew's note: Opal treats cash as fixed_income in downstream taxonomy.
- Write-site: synthetic CASH lot in holdings_lots with `asset_class='cash'`, `bd_super_class='Cash & Cash Equivalents'`, `price=1.00`, `price_quality='cash_par'`.
- Read-site (D_03, D_00b, C_06): config constant `CASH_FOLD_INTO='fixed_income'` (default) → mix aggregator folds cash into fi before bucketing. Flip to `None` to break cash out separately.
- Non-destructive: frontend untouched, classify_series paths untouched, short-term Treasury ETFs (SHV/BIL/SGOV) unaffected (they have CUSIPs + BD SuperClass='Fixed Income' already).
- Cash source: silver/transactions cumulative flows per account_id (append-only replay). Daily `gold/cash_balances/{YYYY-MM-DD}.parquet` write-once immutable.
- Net effect for 49F: fixed_income $345M → $385M under fold; total AUA matches silver $1.68B exactly.

### Schwab sync bootstrapped
Found canonical Schwab delivery path via user.config in the SI2 Desktop client ClickOnce install:
- Account-scoped destination: `C:\Users\AndrewBerman\OneDrive - Opal Capital\Documents\Schwab Data Delivery\08242234\` (49F master account)
- Default directory: `C:\Users\AndrewBerman\Downloads\schwab_downloads` (overridden per account)

Wrote `data/black_diamond/scripts/bronze/sync_schwab_onedrive_to_s3.py` — idempotent scan/diff/upload from OneDrive → `s3://opal-data-schwab/01_raw/`. Mirrors RPS to `bronze/rps/` as well. Hit AccessDenied initially (bucket policy requires `x-amz-server-side-encryption=AES256`); user patched the script to add `ExtraArgs={'ServerSideEncryption': 'AES256'}`. Re-ran successfully.

Outcome: 70 new files uploaded covering trade dates 2026-04-06, 07, 08, 09, 10, 13 (all ~13 extensions). Ran bronze→silver converters:
- silver/RPS: advanced from 04-02 to 04-13 (6 new partitions, 82-83K positions each)
- silver/TRN: 9 new partitions including backfilled gaps
- silver/ACC: converter failed on duplicate `state` columns — low priority, deferred

Re-ran reconciliation against fresh Schwab RPS 04-10: 149/163 mapped orphans validated within 5%, vs 152/163 against the stale 04-02 RPS. Validation picture barely changed — **fresh Schwab data didn't close the gap**, confirming the orphans aren't a Schwab data-lag issue.

### Unused mapping coverage check
Schwab RPS 04-10 has 5,610 accounts ($1.49B). BD↔Schwab mapping has 6,952 schwab_account_ids. Only 15 Schwab RPS accts ($2.7M, 0.18%) are NOT in the mapping → the map is essentially complete on the Schwab side. A gold orphan without a mapping really does mean "not a Schwab account" with very high confidence.

### Multi-signal lifecycle classifier
Cross-referenced orphans against:
- `last_seen_in_fees` from schwab_bd_account_mapping.parquet
- Last Trade Date in asset_dim 2020-03-06 → 2026-04-13

Of 2,073 orphans ($237M):
- 151 with signal within 180d ($24.2M) — KEEP_active
- 23 with signal in 180-365d ($22.0M) — MONITOR
- 123 stale >365d ($16.7M) — QUARANTINE candidate
- 1,776 with NO signal anywhere (no fee record, no txn, no Schwab RPS, no silver) ($174.2M) — DARK

Per Andrew's final direction: do not auto-retire DARK. Could represent legitimate AUA at non-Schwab custodians BD lost visibility on. Keep in holdings_lots, rely on architect-filter for firm aggregation correctness. Lifecycle classifier becomes a `position_status` tag for analytics hygiene, not an AUA correction mechanism.

## What I did

1. **Investigation work** (all local, no commits):
   - Staged 3.93M-txn asset_dim combined parquet locally at `C:\Users\AndrewBerman\AppData\Local\Temp\altvaln\asset_dim_combined.parquet`
   - Pulled silver/allocations, gold/holdings_lots, gold/positions_cube, gold/firm_mix_views.json, gold/firm_composition.json, silver/RPS, silver/transactions, silver/fees for 04-07 through 04-10 for 49F slicing
   - Ran reconciliation, join-key coverage, position-overlap, lifecycle classifier, phantom valuation scan

2. **Brief authored**: `org/tier2_senior/0.4.0_DS_ClientPlatform/briefs/2026-04-14_asset_dim_and_canonical_prices_refactor.md` — 11 work packages, 8 open questions. Brief evolved across session as findings refined: WP-9 added for CUSIP-keyed FIFO, WP-10 reframed twice (first from "drop 200M" to lifecycle classifier, then further back to "orphans are hygiene not AUA fix"), WP-11 for scoped overrides, cash strategy added inside WP-5 with dual-classification framing.

3. **Schwab sync script written + run**: `data/black_diamond/scripts/bronze/sync_schwab_onedrive_to_s3.py`. User added SSE-AES256 ExtraArgs. 70 files uploaded; silver RPS/TRN now through 04-13.

4. **PRD edits** (CTO's PRD, not mine): `docs/architecture/BD_CANONICAL_PRICES_CLASSIFICATION_REFACTOR.md`:
   - Added project-wide dry-run guardrail section above Work Packages
   - WP-3, WP-5, WP-6, WP-9 all converted to DRY-RUN mode — parallel-path output to `_dryrun`/`_v2`/`_v3` suffixed S3 locations
   - Each affected WP gained diff-report requirement + explicit "Cutover (OUT of scope)" line + 30-day parallel-running acceptance bar
   - `ticker_overrides.json` deletion EXPLICITLY removed from WP-6 scope per Andrew
   - WP-9 `NAME_ALIASES` + silver-allocations phantom gate removal EXPLICITLY deferred per Andrew

5. **CTO handoff**: MCP message sent at 20:43 UTC with summary of all findings + PRD changes + one open question on whether to push dry-run guardrail into BDPL_ASTDIM (my read: no, that project is additive-only).

## What I did NOT do

- Did not touch production code or production S3 paths.
- Did not commit any of the investigation work to git (all session-scoped local temp files, explicitly not committed).
- Did not send messages to any other agent besides the final CTO handoff (per Andrew's opening constraint).
- Did not execute the tactical 3-bond scoped-override TO (already authorized but not fired — waiting for the separate ad-hoc TO).
- Did not touch BDPL_ASTDIM — AE owns, already has GO, structurally additive.

## Open items for next session

- Await CTO response on whether BDPL_ASTDIM gets the same dry-run guardrail (flagged in handoff).
- Once BDPL_ASTDIM W4 ships (silver/bd_assets.parquet live), WP-4 (DS) unblocks → can start CUSIP enrichment on gold/holdings_lots.
- WP-7 (phantom diagnostic) can start immediately post-BDPL_ASTDIM W4, parallel with WP-4.
- Schwab ACC converter bug (duplicate `state` column) — fix when priority slot opens; not blocking 49F analysis.
- The 1,776 DARK orphans ($174M) — advisor-confirmation loop is an unscoped follow-on; currently tagged-and-held, not actively reviewed.

## Files touched this session

**Written (new):**
- `data/black_diamond/scripts/bronze/sync_schwab_onedrive_to_s3.py`
- `org/tier2_senior/0.4.0_DS_ClientPlatform/briefs/2026-04-14_asset_dim_and_canonical_prices_refactor.md`
- `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-14/49f_alternatives_investigation_and_bdpl_cnprcs_dryrun_addendum.md` (this file)

**Edited:**
- `docs/architecture/BD_CANONICAL_PRICES_CLASSIFICATION_REFACTOR.md` (dry-run addendum across WP-3/5/6/9)

**Not committed to git.** Andrew will handle commit routing per org protocol.

## Reconciliation bottom line

49F gold/pipeline firm AUA is -3.4% under silver authoritative on 04-10. Broken down:
- -$40.5M from cash not being modeled in gold (structurally closable via WP-5 cash refactor; non-destructive; configurable fold into fixed_income for current taxonomy)
- -$16.6M (1.01%) from mixed causes — multi-custodian plan sleeves (PCRA pattern), per-account tail noise, bond-price drift on non-phantom bonds, partial position misses

BDPL_CNPRCS + BDPL_ASTDIM together close the full gap, all in dry-run mode. No production path decommissioned in this project cycle.
