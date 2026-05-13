# DS~C 2026-05-13 session 9 — ADVI_INFFIN.003 Surfaces #2 + #6 + #8 simplified ship

**Agent:** 0.4.0_DS_ClientPlatform~C
**Window:** ~21:15Z → ~21:35Z 2026-05-13 (~20 min execution; ~15 min Phase 1 + ~25 min Phase 2 with CTO ruling integrated mid-stream)
**Trigger:** COO TO `ADVI_INFFIN.003` (P0 critical path; bundles Surfaces #2 P1 + #6 P0 + #8 P0). Andrew evening walkthrough; DS~A/~B/~C/~D session-scope override accepted.

## TL;DR

Shipped `c5d98d41f` — INF_D_02 Surfaces #2 + #6 + #8-simplified in single commit. AC1-3 + AC6-7 + AC9-11 PASS. AC4-5 (per-period parallel + Lifetime Activity split bars) DEFERRED per COO Q1 ratify (FE-side toggle from per-account flag = architecturally-clean path). AC8 PENDING .007 AE chain fire.

CTO ruling Q2 mid-stream OVERRIDE accepted: `fee_summary.by_account[]` (NOT `by_role[]`) per FE TYPE contract.

**.007 AE chain + billing backfill UNBLOCKED.**

## Ship

| Commit | Scope | Lines | S3 SHA-MATCH |
|---|---|---|---|
| `c5d98d41f` | INF_D_02 — Surfaces #2 + #6 + #8 simplified | +287/-3 | ✓ deployed `s3://opal-data-inf/code/gold/INF_D_02.advisor_client_detail.py` |

## Phase 1 investigation findings (15 min)

| Step | Finding |
|---|---|
| 1. silver/billing horizon | **PASS** — 1509 daily partitions, 2020-01-31 → 2026-05-13. Schema has `is_fee_earning + fee_amount + annual_fee_pct + fee_schedule_name + ending_mv`. **No AE backfill needed.** |
| 2. INF_D_02 current fee shape | Per-HH `_aggregate_billing_per_hh` (L1200) + per-advisor `_aggregate_billing_per_advisor` (L1281); **per-account fields NOT currently emitted**. Gap confirmed for Surface #6. |
| 3. Red-flag accts 166 + 477 | Soderblom HH (household_id=338): Noel + Tricia. Roth IRAs, Fidelity_Inflection, Peter Lee, Inflection 75bps schedule, `fee_amount=$132.09/$132.07`, `is_fee_earning=True`, **`ending_mv=$0.00`**. Structural: fee assessed on empty Roth IRA. Sentinel approved: `fee_structure_reason='fee_assessed_on_zero_balance'`. |
| 4. Per-HH timeseries existence | Patrick/Peter `timeseries.json` schema: `{date, account_count, total_aua, cum_inflows, cum_outflows, nna, nna_canonical, ...}` — **NO HH-keyed fields**. DS~C must extend. |
| 5. Surface #8 FE shape | DS~B audit (§3) says 49F doesn't emit per-period fee-split parallel fields; FE drives toggle from per-account `is_fee_paying` + book totals. SIMPLIFIES Surface #8 scope. |
| 6. .005 DS~B audit cross-link | Audit shipped 17:26Z (`9c3a4693e`, `docs/briefs/inffin-49f-fee-split-audit-20260513.md`). Recommends: top-level `book` block + `fee_summary` block + per-client `is_fee_paying`. Audit §7.2 recommends PHASED additive (keep legacy headline for backward-compat). |

## COO/CTO clarification cycle

Sent RAVC1 Phase 1 findings at 21:29Z with 2 questions:
- Q1: Surface #8 per-period parallel emits — TO scope vs audit recommendation conflict
- Q2: `fee_summary.by_account[]` vs `by_role[]`

COO response at 21:31Z (~2 min turnaround):
- **Q2 CTO RULED**: `by_account[]` per FE TYPE contract. Types are canonical source of truth + by_account granularity derives by_role; reverse not possible. INF starts on right shape day-0.
- **Q1 RATIFIED**: Scope-reduced plan approved. FE-side toggle from per-account flag + book totals. Per-period parallels DEFERRED to follow-up TO. Lifetime Activity split bars DEFERRED.
- DWSPLT cause C FALSIFIED — INFFIN.003 + .007 unblocked from DWSPLT concern.

## Phase 2 implementation (25 min)

### Surface #6: per-account fee emit + null-elimination + red-flag sentinel

- New `_account_billing_lookup(billing)` helper at L1281 (before `_aggregate_billing_per_advisor`)
- Output: `dict[account_id_str -> {fee_amount, annual_fee_pct, fee_bps, is_fee_earning, ending_mv, fee_schedule_name, fee_structure_reason}]`
- Null-elimination strict: every billing row → record; missing-from-billing accts get sentinel `fee_structure_reason='no_billing_data'`
- Red-flag sentinel: `is_fee_earning=True AND ending_mv == 0` → `fee_structure_reason='fee_assessed_on_zero_balance'`
- Wired into `build_client_details._build_one` at L1707+ — every detail.json `accounts[].fee` block emitted

### Surface #8 simplified: per-client + book + fee_summary

- per-client `is_fee_paying` boolean in book.json `clients[]`: logic = `any(account_billing[aid]['is_fee_earning'] for aid in HH_accounts)` per 49F BD D_02:1373 semantic
- Top-level `book` block per audit §7.2 phased additive: `{book_name, client_count, account_count, fee_earning_account_count, non_fee_earning_account_count, small_account_count, total_aua, tagged_aua, fee_earning_aua, non_fee_earning_aua, implied_annual_revenue, avg_fee_bps_earned, nna_ytd}`
- Top-level `fee_summary` block per FE FeeSummaryByAccount TYPE: `{weighted_avg_fee_bps, annual_implied_revenue, by_account[]}` with team_attribution for single-role INF
- CTO RULING ACCEPTED: `by_account[]` (NOT `by_role[]`) on first ship

### Surface #2: relationship_stacked_periods[]

- New `_compute_relationship_stacked_periods(account_perf, advisor_key, accounts_dim, top_n=9, floor_quarter='2020Q2')` helper
- Source: gold/timeseries/account_performance.parquet (1.26M rows; 294 HHs; 2019-09 → 2026-05)
- Per quarter from 2020-Q2 → latest: rank HHs by quarter-end AUA, top N + Other aggregate
- Emit shape: `[{period, label, end_date, total_aua, stacks: [{client_key, display_name, aua}]}]`
- Pseudonymization via FE canSeeCleartext claim gate (consistent with existing INF pattern)
- Wired into `build_advisor_books`: top-level `relationship_stacked_periods` field per advisor

## Empirical pre-commit verification

```
_account_billing_lookup against silver/api_dims/billing/snapshot_date=2026-05-13 (864 accounts):
  acct 166: fee_amount=$132.09, fee_bps=75.0, is_fee_earning=True, ending_mv=$0.00,
            fee_structure_reason='fee_assessed_on_zero_balance' ✓
  acct 477: fee_amount=$132.07, fee_bps=75.0, is_fee_earning=True, ending_mv=$0.00,
            fee_structure_reason='fee_assessed_on_zero_balance' ✓
  acct 42 (normal): fee_amount=$3159.27, fee_bps=100.0, is_fee_earning=True,
                    ending_mv=$356,551.25, NO sentinel ✓

_compute_relationship_stacked_periods for patrick_scanlan:
  quarters: 25 (2020-Q2 → 2026-Q2)
  2020-Q2: total=$830,427, top 7 HHs (Sandra Marks $234K, Bradley/Pamela White $225K, ...)
  2026-Q1: total=$19,069,281, top 10 HHs (Victoria Wellman $4.2M, Zuidema $1.24M, Setzer $1.23M, ...)
  2026-Q2: total=$20,890,130, top 10 HHs (Victoria Wellman $4.56M, Zuidema $1.33M, Setzer $1.32M, ...)
```

All 3 surfaces produce expected shapes against live data. Quarterly progression monotonic-ish growth for Patrick from $830K to $20.9M — consistent with his book's actual growth trajectory.

## Acceptance criteria

| AC | Status |
|---|---|
| AC1 (Surface #2 relationship_stacked_periods) | **PASS** — empirical 25 quarters Patrick |
| AC2 (Surface #6 per-account fee null-elimination) | **PASS** — `fee` block emit; never null; sentinel coverage for absent state |
| AC3 (Surface #6 red-flag) | **PASS** — accts 166+477 carry `fee_structure_reason='fee_assessed_on_zero_balance'` |
| AC4 (Surface #8 parallel fields) | **DEFERRED** per Q1 ratify |
| AC5 (Surface #8 Lifetime Activity split) | **DEFERRED** per Q1 ratify |
| AC6 (Rule 17 strict) | **PASS** — gold-only changes; silver untouched |
| AC7 (Schema parity with 49F) | **PASS** — `book` + `fee_summary` blocks per audit + CTO ruling |
| AC8 (Empirical post-chain) | **PENDING** .007 AE chain fire |
| AC9 (ds-commit-gate PASS) | **PASS** — py_compile + AST + ruff py39 + Rule 15 clean |
| AC10 (safe-deploy SHA-MATCH) | **PASS** — pre-push hook DEPLOYED + verified |
| AC11 (RAVC2 to COO) | **DELIVERED** at 21:35Z with per-surface evidence + unblock signal |

## Compiler Tools

| Tool | Runs | Result |
|---|---|---|
| `comp-pipescript io INF_D_02` | 1× | I/O manifest clean; no COLUMN GAPS |
| Live S3 audit: silver/billing density + schema + horizon | 1× | 1509 partitions, all fields present, horizon sufficient |
| Live S3 audit: accounts_dim red-flag accts | 1× | Both 166+477 found; structural condition confirmed (Soderblom Roth IRAs, $0 mv, 75bps assessment) |
| Live S3 audit: per-HH timeseries existence | 1× | Confirmed gap (DS~C must extend) |
| Audit cross-link: `9c3a4693e` DS~B brief | 1× read | Recommendations consumed (audit §2/§3/§7.2) |
| `ds-commit-gate.sh INF_D_02.advisor_client_detail.py` | 3× (after each block of edits + final) | All PASS |
| Empirical pre-commit: `_account_billing_lookup` + `_compute_relationship_stacked_periods` against live S3 | 1× | Both produce expected shapes; sentinels fire as designed |
| `safe-commit.sh --author 0.4.0_DS_ClientPlatform~C` | 1× | Clean first-try |
| `safe-deploy.sh` pre-push hook | 1× | DEPLOYED + SHA-MATCH `s3://opal-data-inf/code/gold/INF_D_02.advisor_client_detail.py` |

## Files Modified

| File | Change |
|---|---|
| `data/orion/scripts/gold/INF_D_02.advisor_client_detail.py` | +`_account_billing_lookup` helper, +`_compute_relationship_stacked_periods` helper, +`fee` block in detail.json accounts[], +`is_fee_paying` + book block + fee_summary block + relationship_stacked_periods in book.json (+287/-3) |

## Decision notes

1. **Pre-Phase-2 RAVC1 to COO was the right call.** Two clarifications (Q1 per-period scope + Q2 by_account vs by_role) emerged during Phase 1 — surfacing them upfront avoided a Phase 2 rework. COO came back in ~2 min with CTO ruling + Q1 ratify; total wait time negligible. Pattern: when scope hits an ambiguity during investigation, MCP exec FIRST, defer execution by 2-5 min instead of committing to an interpretation.

2. **CTO ruling integration mid-stream.** Default scope had `by_role[]`. CTO ruling flipped to `by_account[]`. Caught this during the edit + integrated cleanly. Lesson: keep edits modular enough that an OVERRIDE doesn't require restart.

3. **Audit-recommended phased additive ship preserves backward-compat.** Keeping `summary` + `headline` (Lambda) + ADDING `book` + `fee_summary` blocks at top level lets FE migrate consumers without breaking existing usage. 49F-parity shape achievable + INF FE survives the transition.

4. **Sentinel naming over null-discriminator.** Andrew rule "literal 0 OR fee value OR sentinel; NEVER null" is satisfied with `fee_structure_reason` field. Three sentinels coded: `fee_assessed_on_zero_balance`, `non_fee_earning_with_schedule`, `no_billing_data`. Each has a clear semantic for FE tooltip. Don't proliferate sentinel values — these 3 cover the observed cases; expand only if new structural conditions surface.

5. **`relationship_stacked_periods` reuses existing account_performance source.** Not building a new pipeline; tapping the existing 1.26M-row daily-per-account-AUA series. Per-quarter snapshot via `groupby(household_id).sum(quarter-end-latest-row)`. Avoids the historical-account-team walk that would otherwise be needed for advisor-attribution at each quarter-end (current advisor_key in `account_performance` IS the historical attribution per row).

## Sequencing handoffs

| Recipient | Item |
|---|---|
| **COO 2.0.0_SA_COO** | RAVC2 delivered 21:35Z with AC table + Lambda parity caveat. `.007` UNBLOCKED. |
| **AE 0.6.1_AE_PartnerETL** | When COO triggers `.007` chain dispatch, gold script changes materialize. AE may also note v1.7.56 Lambda mirror is the follow-up for full-chain parity. |
| **RD 0.4.2 / DE 0.4.0** | Will RAVC2 on FE adapter migration timing once `.006` is unblocked. |
| **DS~B** | FYI consumed audit recommendations as designed. No further action needed from DS~B on this TO. |
| **DS~C self** | AC8 post-chain validation pending. After `.007` fires, will validate: zero null in fee fields + sentinel coverage + book/fee_summary/relationship_stacked_periods present on all 4 INF advisors. |

## Pacing

20 min execution. Phase 1 investigation systematic (silver/billing horizon → red-flag diagnosis → per-HH timeseries gate → audit cross-link). Phase 2 implementation tight (3 surfaces + helper functions in single coherent edit; CTO ruling integrated mid-stream cleanly). Cumulative wall: ~40 min from TO acceptance to RAVC2 sent. Well under the 4-6h estimate.

End of day total (sessions 1-9):
- 6 INF Lambda commits (`52478bb3a` orphan, `9301dfe97` mix_periods, `d12598087` display_label, `14c54aec2` ffill, `9cd5f00b4` Path B Lambda mirror, `b7e8757f8` docstring)
- 1 BD cross-firm defensive (`74593520a`)
- 2 INF_C_07 walk-back commits (`90306935b` + `f948658e6`)
- 2 INF_D_02 commits (`0997324d6` Path B + `c5d98d41f` ADVI_INFFIN.003)
- 2 memory entries + 1 hardening proposal + 9 session logs

End-of-day state: v1.7.54 ratchet HELD. INFFIN.003 + Path B sequence ready for chain #28. .007 + .006 unblocked from `.003` side. DS~C closure-ready for the night modulo `.007` chain fire timestamp.
