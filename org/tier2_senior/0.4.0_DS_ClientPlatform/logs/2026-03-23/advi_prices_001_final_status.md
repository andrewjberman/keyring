# ADVI_PRICES-001: Final Session Status — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-23
**Branch:** CLOUD
**Status:** COMPLETE — awaiting AE gold rerun for post-fix verification

---

## What We Found

The original problem was a +$68M net gap between our gold holdings_lots and BD silver allocations ($211M gross overshoot / $143M gross undershoot). After same-date alignment the net narrowed to +$25.6M, but the gross picture was worse than initially reported.

Full diagnostic investigation (8 scripts, 4 hypotheses tested) decomposed the gap into three distinct root causes:

| Root Cause | Gross Impact | Mechanism |
|---|---|---|
| **Phantom lots (incomplete BD transaction feed)** | +$352M overshoot | BD's transaction feed never sent exit events for ~1,600 accounts. Accounts are removed from BD's allocation snapshot but FIFO has no sell transactions to close the lots. 73% of phantom positions have zero sells in all history. |
| **Pricing divergence (canonical vs BD)** | +$97M over / -$141M under = -$44M net | Bidirectional. Our canonical prices (transaction-observed + yahoo + carry-forward) differ from BD's vendor pricing. Active accounts, 2.5 days average staleness. |
| **Structural gaps (allocation-only, insurance, non-investment)** | -$35M undershoot | Accounts with AUA in BD allocations but no transaction history (held-away, 529 plans, insurance wrappers, bank accounts). By design — no fix possible via FIFO. |

The phantom +$352M is extremely concentrated: the top 25 accounts hold $164M (77%). Patterns identified:
- 17 of the top 25 have BD AUA = $0, account_type = nan (BD has fully removed these accounts)
- 12 accounts share the z0814* prefix (custodian/feed-source cluster)
- A 2023Q1 sell-stop cohort (76 accounts, 27% of partial-sells) suggests a BD feed discontinuity
- One derivatives account (z0818693751) contributes $55.9M alone due to options expiry handling
- Plan-type accounts (TIAA, 529, TermLife) are 3-5x overrepresented in phantoms

---

## What We Fixed

### Code Changes (10 commits on CLOUD)

**1. Temporal guard spillover fix** (`4278798e`)
- Script 03: FIFO sell processing now accumulates sell volume blocked by the temporal guard and applies it in a second pass ignoring dates
- Fixes derivatives/options where BD records buy dates after exercise/expiry
- Impact: ~$56M recovered (one account)

**2. Allocation-authority phantom lot reconciliation** (`c50877b0`)
- Script 03: post-FIFO step loads silver/allocations for the snapshot date and force-closes lots in phantom accounts
- Rule 1 (BD-zeroed): alloc AUA < $100 — force-close all lots unconditionally
- Rule 2 (BD-diminished): alloc AUA >= $100 but lot MV > 2x AUA and lot MV > $50K — force-close all lots
- Impact: clears the top 25 accounts (~$164M of $212M phantom excess)

**3. Phantom account exclusion in positions_cube** (`7dd2432b`)
- Script 02: loads allocation and excludes accounts with AUA < $100 from all output partitions
- Rule 1 only (no prices in positions_cube for Rule 2 — $10M residual accepted)
- Ensures scripts 05 (client_performance), 05b (account_performance), 06b (mix_timeseries) also get clean data

**4. Taxonomy expansion** (`f1b3f33d`) — `Redemption` added to SELL_TYPES, 5 CA subtypes added. Near-zero current impact (176 Redemption rows, 0 rows for the 5 CA types). Insurance against future BD data changes.

**5. Diagnostic scripts** (4 commits) — recon_lots_vs_allocations.py, taxonomy enumeration, name mismatch test, FIFO replay, undershoot/overshoot deep dives, zero-sell/partial-sell pattern analysis, concentration analysis. Reusable for ongoing monitoring.

### Hypotheses Tested and Eliminated

| Hypothesis | Result |
|---|---|
| Missing exit transaction types | DISPROVEN — zero unrecognized exit-like types in data |
| Asset name mismatch in FIFO grouping | DISPROVEN — 0 real matches across top 5 accounts |
| Dedup dropping sell transactions | MINOR — 94 rows, 16,980 units. Not the primary driver |
| Sells with NaN/zero units | NEGLIGIBLE — 2 rows |
| DRIP inflation (reinvestment lots) | DISPROVEN — DRIP is 0.4% of buy volume |

---

## Expected Post-Fix Numbers

AE is running the gold layer with the updated scripts 02 and 03. Expected results:

| Metric | Before | After (estimated) |
|---|---|---|
| Phantom lot overshoot | +$352M | ~+$140M (Rule 1+2 clear ~$212M, temporal guard clears ~$56M, overlap reduces total) |
| Pricing divergence (net) | -$44M | -$44M (untouched, active accounts) |
| Structural gaps | -$35M | -$35M (untouched, by design) |
| **Cross-date net gap** | **+$68M (+4.3%)** | **TBD — recon will confirm** |
| **Same-date net gap** | **+$25.6M (+1.6%)** | **TBD — expect significant reduction** |

The remaining ~$140M phantom overshoot is the long tail: hundreds of smaller accounts where BD's transaction feed is incomplete. The concentration analysis showed 82% of phantom excess is in the top 10% of accounts — the rules target exactly those accounts. The tail accounts below the $50K threshold are intentionally left alone to avoid false positives on small accounts with normal pricing variance.

---

## What's Left (not DS scope)

**1. AE: Verify gold rerun results** — run recon_lots_vs_allocations.py after gold layer completes. This is the definitive post-fix number.

**2. AE: Investigate the 2023Q1 sell-stop cohort** — 76 partial-sell phantom accounts all had their last sell in Q1 2023. This points to a BD feed discontinuity or processing change. Understanding what happened could recover additional phantom excess.

**3. AE: Investigate the z0814* custodian cluster** — 12 of the top 25 phantom accounts share this prefix. Likely a single custodian or feed source where exit events were never routed to the transaction feed.

**4. COO: Decide disposition of remaining gaps:**
- Pricing divergence (-$44M net): accept as methodology difference, or invest in price alignment?
- Structural gaps (-$35M): accept as known limitation, or build synthetic allocation-only MV layer?
- Remaining phantom tail (~$140M): lower the $50K threshold in Rule 2, or investigate upstream?

**5. DT: Push 10 commits on CLOUD to remote.**

---

## Files Modified

| File | Change | Commit |
|------|--------|--------|
| `data/black_diamond/scripts/gold/03_build_holdings_lots.py` | Taxonomy expansion, temporal guard fix, allocation-authority reconciliation | `f1b3f33d`, `4278798e`, `c50877b0` |
| `data/black_diamond/scripts/gold/02_build_positions_cube.py` | Phantom account exclusion (Rule 1) | `7dd2432b` |
| `docs/data/transaction_type_canonical_reference.md` | 6 new types added | `f1b3f33d` |
| `data/black_diamond/scripts/diagnostics/recon_lots_vs_allocations.py` | Created | `9b039259` |
| `data/black_diamond/scripts/diagnostics/diag_txn_taxonomy_enumeration.py` | Created | `9b039259` |
| `data/black_diamond/scripts/diagnostics/diag_phantom_asset_name_mismatch.py` | Created | `2d0dcad9` |
| `data/black_diamond/scripts/diagnostics/diag_phantom_fifo_replay.py` | Created | `62ce146d` |
| `data/black_diamond/scripts/diagnostics/diag_undershoot_accounts.py` | Created | `2a4153c0` |
| `data/black_diamond/scripts/diagnostics/diag_overshoot_accounts.py` | Created | `2a4153c0` |
| `data/black_diamond/scripts/diagnostics/diag_phantom_zero_sells_patterns.py` | Created | `1fb5bcfe` |
| `data/black_diamond/scripts/diagnostics/diag_phantom_partial_sells_patterns.py` | Created | `1fb5bcfe` |
| `data/black_diamond/scripts/diagnostics/diag_phantom_concentration.py` | Created | `3fbd79db` |

---

## Next Steps

1. **[0.6.0_AE_PartnerETL] Gold rerun in progress** — scripts 02 (FULL rebuild) and 03 (--upload --date 2026-03-19) running now
2. **[0.6.0_AE_PartnerETL] Run post-fix recon** — `python recon_lots_vs_allocations.py --date 2026-03-19 --output-dir /tmp/recon/`
3. **[0.4.0_DT_ClientPlatform] Push 10 commits to remote** — pending COO/Andrew approval
4. **[2.0.0_SA_COO] Review post-fix numbers and decide on remaining gap disposition**
