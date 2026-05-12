# DS~C 2026-05-12 — Brief #12 IWM + INFCONCDRILLFI + INFNMNCPERSPEC + cross-lane coordination

**Agent:** 0.4.0_DS_ClientPlatform~C
**Window:** ~17:43Z → ~20:40Z 2026-05-12 (~3 hr cooperative session, three substantive commits + two cross-lane routes)
**Trigger sequence:**
1. DE 0.4.0_DE_ClientPlatform Brief #12 (`20260512T184745Z`, INFLBIWMALIGN — IWM leaderboard vs book.json $253K-vs-$510K mismatch).
2. Andrew-forwarded RD 0.4.2 INFCONCDRILL adjustment #2 (`20260512T1856xxZ` via inbox-watch — include fixed_income funds in firm_concentrations).
3. Andrew-forwarded RD 0.4.2 brief `e5f8bf19` (`2026-05-12_timeseries_chart_nmnc_period_specific_DS_briefing.md`) — INFNMNCPERSPEC first-year all-NMNC bug.
4. Andrew-forwarded RD 0.4.2 brief `2026-05-12_49f_capital_gains_ttm_correction_DS_briefing.md` — BD pipeline scope, routed to DS~D.
5. Andrew-forwarded RD 0.4.2 brief `abfc0ccb` `2026-05-12_distribution_nna_drill_DS_briefing.md` — DS~D-routed; cross-lane diff review on the value-semantic + city-drill fix.

## TL;DR

Three substantive INF gold ships + two cross-lane routings, all gates-clean and SHA-MATCH deployed. Sentinel-ready hard invariants on the IWM leaderboard alignment (post-fix `sum(advisor AUA) ≈ $203M`) and the NMNC/NMEC classification (post-fix `nmnc + nmec = firm AUA` per-period, period-specific in-window logic). Six DS~C commits queued for next `gold-d` (AE 0.6.1 pinged). Two DS~D commits stacked on top of mine on `INF_D_04` (last-write-wins, sentinel-correct via 'Other' absorption I suggested in the diff review).

## Ship roster

| Time (ET) | Commit | Scope | Lines |
|---|---|---|---|
| ~14:57 | `56c1082bc` | DE brief #12 INFLBIWMALIGN — IWM leaderboard via account_team path; firm-bucket append removed | +32/-86 |
| ~15:56 | `c2382cc01` | RD INFCONCDRILLFI — bond funds in firm_concentrations | +30/-14 |
| ~16:24 | `61448b75c` | RD `e5f8bf19` INFNMNCPERSPEC — per-period NMNC/NMEC classification | +162/-57 |

Total: 3 commits, +224/-157 lines, all `s3://opal-data-inf/code/gold/` SHA-MATCH verified.

## Per-commit detail

### Brief #12 — INFLBIWMALIGN (`56c1082bc`, 14:57 ET)

**Symptom (Andrew):** Advisors-tab leaderboard "Inflection Wealth Management $253K / 404 / 207" but clicking through to IWM Book Overview shows TOTAL AUA $510K / 39 / 11. Andrew confirms $510K is canonical.

**Root cause:** Two divergent advisor-routing schemes in `INF_D_00c.portal_leaderboard.py`.

- Individual advisors (Peter/Patrick/Joe) grouped on `account_team.advisor_key` (INF_C_07 output), `_placeholder = {'new_accounts_rep', 'inflection_wealth_management'}` EXPLICITLY EXCLUDED IWM.
- IWM firm-bucket append (~L905-976) sourced from `holdings[rep_bucket=='firm']` + `accounts_dim[rep_bucket=='firm']` — different population (404/207 from rep_bucket vs 39/11 from account_team).

These two paths used to be aligned but diverged after INF_C_07 became the canonical attribution path. Per workspace memory `project_inflection_iwm_catchall_bucket.md`, IWM-as-catchall is INTENTIONAL — the question was just which routing scheme defines it.

**Canonical-reconciliation arithmetic confirmed `account_team` is the right source:**
```
Peter $165.21M + Joe $16.43M + Patrick $20.87M + IWM_book $510K  = $203.02M  (matches dashboard.json#headline.total_aua)
Peter $165.21M + Joe $16.43M + Patrick $20.87M + IWM_lb $253K    = $202.76M  ($260K short)
```

**Fix (DE Option A — recommended): treat IWM as a regular advisor entry.**

1. `_placeholder = {'new_accounts_rep', 'inflection_wealth_management'}` → `{'new_accounts_rep'}` at the `acct_counts`/`hh_counts` loop (~L774). IWM now appears in `indiv_dim`.
2. `_at_placeholder = {'new_accounts_rep', 'inflection_wealth_management'}` → `{'new_accounts_rep'}` at the individual-entry loop (~L808). IWM joins `_at_indiv` → main `for advisor_key in sorted(all_advisors)` loop emits canonical $510K/39/11 via `aua_by_adv['inflection_wealth_management']`.
3. **Firm-bucket entry append (was ~L905-976, ~70 lines) removed entirely.** Legacy block computed `firm_nna` / `firm_acct_count` / `firm_hh_count` / `firm_lifecycle_aua` / `firm_role_breakdown` / `firm_perf` from `rep_bucket=='firm'` filters and appended a `primary_role='firm'` entry. All dead post-Option-A.
4. **Preserved**: `firm_aua` orphan accumulation (~L828) — `_orphan_aua = sum(v for k, v in aua_by_adv.items() if k not in _at_indiv and k != 'new_accounts_rep')`. Defensive backstop if a future `advisor_key` escapes the named-advisor universe.

**Schema-flip flagged to DE for FE smoke:** IWM's `primary_role` flips `'firm'` → `'rep'`; `roles` from `['firm']` → `['rep']`. DE ran smoke-grep on portal/src — **CLEAN** (no `primary_role === 'firm'` branches anywhere). RAVC4 closed.

### INFCONCDRILLFI — bond funds in firm_concentrations (`c2382cc01`, 15:56 ET)

**Symptom (Andrew):** top_holdings panel shows HTRB / BAGIX / BSIIX (combined ~19% of firm AUA, all fixed_income mutual funds) but none appear in Concentration Risk treemap. Brief §4 said "equity-class only" — wrong call.

**Root cause:** `INF_D_07a.firm_concentrations.py:319` filter:
```python
equity_mask = annotated['product_category'].fillna('').astype(str).str.strip() == 'Equity'
```
Dropped `product_category == 'Bond'` before bucket selection.

**Fix:** Single-line filter change at the in-scope mask:
```python
included_mask = annotated['product_category'].fillna('').astype(str).str.strip().isin({'Equity', 'Bond'})
```

Variable rename `eq` → `included` (4 references); log line now reports by-category counts so sentinels surface mix shifts.

**Why this works without additional filtering:**
- Money Market dropped by the new `product_category` filter.
- Bond MFs/ETFs (HTRB / BAGIX / BSIIX) → `product_sub_type` indicates MF/ETF → `_classify_security_type` returns `'mutual_fund'` or `'etf'` → survives the existing line ~368 `isin({single_stock, etf, mutual_fund})` filter. `_classify_asset_class` correctly tags `'fixed_income'`.
- Individual bonds → `product_sub_type` not in classifier sub-type sets → `security_type='other'` → dropped at the same line ~368 filter.
- Alternatives unchanged (`product_category='Equity'` with alternatives keyword in `mstar_asset_class`).

Schema unchanged — `asset_class` field already in emit; values `'fixed_income'` now flow alongside `'equity'`/`'alternatives'`. FE green color (per MIX_PIE) handles automatically.

**INFCONCDRILL lane history today (3 commits, 4 hours):**
- `0d1043b90` initial INFCONCDRILL top-25 (RD brief)
- `0fa96cd99` bucketed top-10 per security_type (RD adjustment #1)
- `c2382cc01` bond funds included (RD adjustment #2 — this commit)

### INFNMNCPERSPEC — per-period NMNC/NMEC classification (`61448b75c`, 16:24 ET)

**Symptom (Andrew 16:13Z screenshot):** First 4 quarterly bars (Q2 2020 → Q1 2021) stack as 100% NMNC including the firm's starting $58.5M AUM. Andrew verbatim: "if the first period there is 58m and the next period is 65, then 58m in Q3'20 should be blue to signify existing".

**Root cause (different from brief's hypothesis):** `INF_D_00b.portal_timeseries.py` `_build_lifecycle_periods` at L290-291 used a **rolling 365d-from-period-end window**, not a "doesn't appear in prior period" check:
```python
window_start = snap_date - pd.Timedelta(days=LIFECYCLE_WINDOW_DAYS)  # 365 days
nmnc_mask = aua_snap['inception_date'] >= window_start
```

Because `cp_first_seen` for every HH visible at firm `data_start` equals `data_start` (cp data bounds the inception date observation), every HH passed the rolling 365d window for the first ~5 quarters → 100% NMNC. Empirical (pre-fix):
```
2020-Q2: total $58.5M  nmnc $58.5M (100%)  nmec $0
2020-Q3: total $65.2M  nmnc $65.2M (100%)  nmec $0
2020-Q4: total $78.6M  nmnc $78.6M (100%)  nmec $0
2021-Q1: total $73.7M  nmnc $73.7M (100%)  nmec $0
...
2026-Q1: total $188.2M nmnc $16.3M (8.7%)  nmec $171.9M  (only fully correct at Q1 '26)
```

**Fix (per brief recipe):**

1. `_period_specs_for_freq` extended from 3-tuples `(period_str, label, p_end)` → 4-tuples `(period_str, label, p_start, p_end)`. Quarterly: `p_start` = quarter start. Monthly: month start. Annual: Jan 1. Partial-current-period extension preserved (p_start = standard period start of the period containing `end`). Single caller updated.

2. `_build_lifecycle_periods`:
   ```python
   data_start_ts = pd.Timestamp(cp['date'].min())
   hh_inc['is_pre_existing'] = (
       hh_inc['inception_date'].isna() | (hh_inc['inception_date'] <= data_start_ts)
   )
   # Per period P with [p_start, p_end]:
   nmnc_mask = (
       (~aua_snap['is_pre_existing'])
       & aua_snap['inception_date'].notna()
       & (aua_snap['inception_date'] >= p_start)
       & (aua_snap['inception_date'] <= p_end)
   )
   nmec_mask = ~nmnc_mask
   ```
   HHs visible at observation start = pre-existing (always NMEC). HHs with NaT inception (data-quality gap) default to pre-existing per brief recommendation.

3. **Sum invariant preserved:** `nmnc + nmec = sum(aua_snap.aua) = firm AUA at snap_date`.

4. `build_lifecycle_periods` now returns `(quarters, months, years, categories, meta)` where meta = `{data_start_date, pre_existing_pct, first_seen_fallback_pct, nmnc_classification}`. main() threads meta into `chart._meta` so downstream + portal sentinels detect classification drift.

**Bug 2 scope reduction:** `months[]` (73 entries) + `years[]` (7 entries) already exist in artifact post Brief #5 INFLIFECYCLE Bug B (`8fa237b73` this morning). They were ALSO 100% NMNC due to the same Bug 1 cascade. Phase 1 cascade-clears Bug 2 — monthly bars and summary card cells light up once chain redeploys.

## Cross-lane coordination

### 49F `capital_gains_ttm` brief — routed to DS~D

**Brief:** `org/tier2_senior/0.4.2_RD_AdvisorIntelligence/briefs/2026-05-12_49f_capital_gains_ttm_correction_DS_briefing.md`. RD requested BD pipeline `capital_gains_ttm` field receive the same TTM-locked correction DS~B applied to INF in `2e5539bac`.

**Not my lane** — BD/49F scope, not Inflection. Explicit deferral per Andrew SYNC #2.

**Routed to:**
- **Primary**: DS~D (most recent active BD lane per `8bb342de4` Brief #9 Part B). MCP delivered the 4 emit-site grep (`D_00:537`, `D_02:925`, `D_02:2417`, `D_04:2480`) + pattern reference + cross-firm AC.
- **CC**: DS~B as pattern-source author (`2e5539bac` INF TTM-locked correction).
- **RD ACKed**: BD has `gold/timeseries/account_performance.parquet` with the analog `unrealized_gain` daily series (open Q #2 closed).

DS~D ACKed; queued behind SCHWAB-BUCKDR Phase 6 chain validation. ETA tomorrow morning unless Andrew prioritizes earlier.

### INF NNA donut + city drill (RD `abfc0ccb`) — diff review for DS~D

**Brief:** `org/tier2_senior/0.4.2_RD_AdvisorIntelligence/briefs/2026-05-12_distribution_nna_drill_DS_briefing.md` (commit `abfc0ccb`). Two bugs in `INF_D_04` NNA donut + drill:
- Bug A: state-level `value` shows AUA-magnitude ($173M for WA, not the expected ~$336K state NNA flow).
- Bug B: `views.nna.current.geo.drill[state].by_city` empty.

Brief routed to DS~D per Andrew. DS~D MCP'd me asking for INF_D_04 context.

**Critical finding I surfaced:** 49F's `views.nna.current.geo.donut.segments[].aua` field is a **misnomer** — actually carries `period_inflows - period_outflows` (= net NNA), not real state AUA. Empirical verified live:
```
49F views.nna.current.geo.donut.segments[0]:
  {key:'tx', aua:21806530.38, value:21806530.38, period_inflows:48877535.93, period_outflows:27071005.55}
# 48877535.93 - 27071005.55 = 21,806,530.38 = aua = value -> net NNA, not real state AUA
```

My Phase 1 mirror (`97796c0ac`) had sourced `aua_by_group` from `views.geo.current.donut.segments[].aua` (REAL state AUA, $173M for WA) and emitted that as `value` AND `aua` on the NNA segment. So INF NNA donut has `value=real_state_AUA` ($173M for WA) — diverged from 49F's misnomer in a DIFFERENT direction than the brief expected.

**Brief abfc0ccb is forward-correct** (cleaner than 49F's current state):
- `value` = state NNA $ (donut slice)
- `aua` = state AUA $ (informational sidecar)

Sent DS~D a full context message + concrete patch recommendations + a tightening on the un-citied account handling: **absorb un-citied accounts into the per-state `Other` city bucket** alongside the top-20 truncation residual. Single absorption point makes `sum(by_city[*].total) == segment.value` exact rather than tolerance-based.

**DS~D shipped (post my diff review):**
- `7bcaac70e` Bug A value-flip + Bug B drill builder (+173/-36)
- `55e37ebcb` un-citied 'Other' absorption + state='Other' skip (+11/-3)

Both my tightenings landed cleanly. Hard sentinel: `sum(by_city[*].total) == segments[state].value` per state. DS~D AE-pinged separately; my gold-d dispatch covers both their commits via last-write-wins on INF_D_04.

### Gold-d dispatch consolidation

Six DS~C commits queued for chain ingestion + two DS~D commits stacked on `INF_D_04`. Pinged AE 0.6.1 for a `gold-d` (not solo SSMs) covering everything in one ~20min run rather than 4-5 separate dispatches:

| Commit | Script | Brief |
|---|---|---|
| `97796c0ac` | INF_D_04 | RD `b7b15c35` Gap A NNA value-field |
| `6967d27f7` | INF_D_04 | RD `b7b15c35` Gap E nna_clients.json |
| `eea448321` | INF_D_04 | DE brief #10 fee_earning_account_count |
| `56c1082bc` | INF_D_00c | DE brief #12 IWM leaderboard |
| `c2382cc01` | INF_D_07a | RD INFCONCDRILLFI bond funds |
| `61448b75c` | INF_D_00b | RD `e5f8bf19` INFNMNCPERSPEC |
| `7bcaac70e` | INF_D_04 | RD `abfc0ccb` Bug A + B (DS~D) |
| `55e37ebcb` | INF_D_04 | RD `abfc0ccb` 'Other' absorption (DS~D) |

RD 0.4.2 has 5 smokes queued (NMNC, INFCONCDRILLFI, IWM, NNA donut semantics, NNA city drill); will RAVC2 batch post-chain. DS~D writing today's session log + queueing 49F TTM after.

## Compiler Tools

| Tool | Runs | Result |
|---|---|---|
| `ds-commit-gate.sh` | 3× (one per substantive commit) + 1× session log | All PASS — py_compile + ds-precommit + ruff py39 clean |
| `safe-commit.sh --author 0.4.0_DS_ClientPlatform~C` | 3× | All clean. Brief #12 first attempt aborted on staged-index contamination (`record-terraform-deploy.sh` audit log + AE 0.7 session log); cleaned via `git reset HEAD -- <extras>` and re-ran. Other 2 first-try clean. |
| `safe-deploy.sh` pre-push hook | 3× | All DEPLOYED + SHA-MATCH verified to `s3://opal-data-inf/code/gold/` |
| Manual `aws s3 cp` + `hashlib.sha256` SHA verify | 3× | MATCH `7a004eb5…b44b` (Brief #12); `2d7adee5…fb94` (INFCONCDRILLFI); `942f11a6…005c` (INFNMNCPERSPEC) |
| Live S3 diagnostic `s3://opal-data-inf/platinum/firm/partner_analytics_quarterly.json` | 2× | Confirmed Phase 1 NNA value-field semantic divergence + 49F misnomer empirical (cross-firm `aua = net_NNA, not real AUA` on NNA-cohort donut) |
| Live S3 diagnostic `s3://opal-data-inf/platinum/firm/timeseries_chart.json` | 1× | Confirmed 100% NMNC first year + months[] / years[] already shipped post brief #5 |
| Cross-firm reference `s3://opal-data-bd/platinum/firm/partner_analytics_quarterly.json` | 1× | 49F's NNA-cohort `aua`/`value`/`period_inflows`/`period_outflows` shape confirmed |

No owned-paths blocks. No commit gate failures. No SHA mismatches. No pre-commit hook bypasses.

## Inbox watcher hygiene

| Incident | Resolution |
|---|---|
| Initial boot exit-143 on first inbox-watch launch | Documented zombie-short-circuit pattern. Killed PPID=1 zombie `487080` + child `490143`. Relaunched via PATH wrapper. |
| Second exit-143 mid-session | Found orphan `564152` (PPID=1, prior session leftover). Killed; relaunched tracked watcher. |
| All other relaunches | Clean (proper Bash-tool `run_in_background: true` discipline; no shell `&` form). |

## Decision notes (worth keeping)

1. **Mirror vs codify.** Brief abfc0ccb is the cleaner forward-correct semantics; 49F's actual artifact has a misnomer that my Phase 1 mirrored. **Lesson: when mirroring, dump the source artifact and read the field SHAPE, not just the keys.** I checked the keys list against 49F and emitted the same field names but with a DIFFERENT source (real state AUA vs 49F's net-NNA-via-misnomer). Field-name agreement is necessary but not sufficient — value semantics need explicit confirmation too. Worth adding "field semantics" to the comp-validate sentinel pack when DS~D's commit lands.

2. **Cross-lane review beats unilateral cleanup.** DS~D's brief was routed-to-them by Andrew; I had context but not lane ownership. The right move was full-context handoff + diff review at their request, NOT taking it back. Result: DS~D ships cleanly with my tightening (un-citied 'Other' absorption → exact sentinel) on top of their plan. Both lanes happy, sentinel hardened, no contention. Pattern: full context up front prevents back-and-forth churn.

3. **Single chain > solo SSMs.** Six commits queued + two stacked = one `gold-d` dispatch covers all 8 in ~20min. AE only fires once; RD smokes once. Solo SSMs would have been 4-5 firings + 4-5 smoke windows. Reduces dispatch coordination overhead to near-zero.

4. **Pre-flag the misnomer in the RAVC narrative.** When I pinged AE for gold-d, I pre-flagged for RD that the chain would surface NNA donut state values at **AUA magnitude** (per my Phase 1 mirror). Then when DS~D shipped the forward-correct fix on top, I updated RD with the timing change ("DS~D's semantic fix already in HEAD; chain picks up real NNA-flow values $K-range not $M-range AUA"). Two messages = clean status visibility for RD; no surprise reading the artifact post-chain.

5. **Bug-class diagnostic-first cadence is reinforced.** Brief #12 root-cause was confirmed by live S3 cross-reference + grep before any code edit (Option A vs Option B trade-off was a code-level decision). INFNMNCPERSPEC root-cause was confirmed by live `timeseries_chart.json` dump + reading the rolling-365d window logic, NOT trusting the brief's "doesn't appear in prior period" hypothesis. The actual bug was different from the brief's hypothesis; the diagnostic surfaced it. Worth amplifying — `aws s3 cp ... | python -c "..."` is the cheapest debug step in this codebase.

## Sequencing handoffs

| Recipient | Item |
|---|---|
| **AE 0.6.1 / AE 0.7** | Gold-d dispatch (or full) covers 6 DS~C INF_D_* commits + 2 DS~D INF_D_04 commits via last-write-wins. ETA whenever AE bandwidth allows; non-urgent. |
| **RD 0.4.2_RD_AdvisorIntelligence** | 5-smoke batch RAVC2 post-chain: (1) timeseries_chart NMNC first-year NMEC-dominant, (2) firm_concentrations bond funds (HTRB / BAGIX / BSIIX), (3) leaderboard IWM $510K / 39 / 11, (4) NNA donut state values (signed $K range), (5) NNA city drill (Everett/Bellevue/Spokane etc.). |
| **DE 0.4.0_DE_ClientPlatform** | Post-chain: clients-tab-slim em-dash fallback clears for `fee_earning_account_count`; Advisors-tab IWM row $510K / 39 accounts; Distribution tab NNA donut signed values render. |
| **DS~D 0.4.0_DS_ClientPlatform~D** | RAVC2 to me on the NNA donut empirical pre/post; routed 49F TTM brief lands tomorrow morning post-SCHWAB-BUCKDR. |
| **DS~C self (idle)** | Standing by for chain redeploy + RD's 5-smoke batch. ADVI_ROLLUP.SL-P2 still awaits explicit COO GO (reader-visible promotion). No pending work. |

## Pacing

~3 hour cooperative session. Three substantive ships averaging ~75 line-changes each, plus two cross-lane routings (49F TTM → DS~D, NNA donut+drill diff review for DS~D). No retraction churn; no scope creep; no shared-index commit-scope incidents (the one staged-index contamination caught by `safe-commit.sh` was AE 0.7's working tree, properly skipped via `git reset HEAD --`).

Cooperative tempo notable today: DS~D + DS~C + RD + DE + AE 0.6.1 all coordinating on the same S3 artifact (`partner_analytics_quarterly.json`) without contention because last-write-wins is structurally enforced via SHA-MATCH pre-push + AE's single-chain dispatch. The 49F misnomer surfaced during cross-lane review IS the kind of thing solo work would have missed.
