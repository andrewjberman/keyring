# ADHC_GLDINC.CENSUS-XT — Cross-tree assembly-shape census

**Author:** 0.6.0_AE_PartnerETL
**Date:** 2026-06-12
**TO:** `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADHC_GLDINC.CENSUS-XT.ae-cross-tree-assembly-shape-census.md` (issued 5ccf1412a)
**Governing ruling:** CTO 20260611T230400Z — A_01-nondeterminism class adjudication: the true discriminator is the **parallel-load ASSEMBLY SHAPE** (completion-order append = CLASS-N; index-slot = CLASS-I), NOT the `keep='last'` grep.
**Discipline:** code-read only, **ZERO runs** (shadow harness stays the runtime detector).

---

## Classification rubric (per CTO ruling + TO Phase-2)

- **CLASS-N** (the real A_01/A_04 defect class): completion-order append (`dfs=[]` + `.append(fut.result())` inside an `as_completed` loop) **AND** an order-sensitive downstream dedup (`drop_duplicates(..., keep='last'/'first')` — or a subset `drop_duplicates` with no `keep=`) that is **not** preceded by a fully-ordering `sort_values`. Both lines cited.
- **CLASS-I** (deterministic): any of —
  - **index-slot** assembly (`dfs=[None]*len(keys)`; `dfs[futures[future]]=result`);
  - **`pool.map(...)`** (yields in input order, not completion order);
  - **named-future fan-out** (`fut_perf=submit(...)`, `fut_tax=submit(...)` — results placed by name);
  - **keyed-dict** assembly (`results[k]=data`);
  - **write-only / compute-only pool** (workers write per-key to S3 or return stats; no cross-task data assembly);
  - completion-order append whose downstream consumption is **order-insensitive** (commutative groupby/sum aggregation, counting-dedup, or a `keep=` dedup over a fully `sort_values`-ordered frame).
- **SINGLE-SOURCE**: no parallel assembly. (None in the candidate set — every candidate matched the Phase-1 grep, i.e. all contain a concurrency primitive; non-candidate scripts are trivially single-source and out of census scope.)

---

## Phase-1 enumeration (grep, before classification)

```
grep -rln "as_completed\|ThreadPoolExecutor\|ProcessPoolExecutor\|imap_unordered" \
  data/inf/scripts/gold/ data/cot/scripts/gold/ \
  data/black_diamond/scripts/gold/C_*.py data/black_diamond/scripts/gold/D_*.py
```

Candidate counts (`.py` only; `__pycache__/*.pyc` and `*.legacy` excluded):

| Tree | Candidates |
|---|---|
| `data/inf/scripts/gold/` | 16 |
| `data/cot/scripts/gold/` (+ `lib/`) | 27 + 2 = 29 |
| `data/black_diamond/scripts/gold/` C_*/D_* | 14 |
| **Total** | **59** |

---

## Table 1 — `data/inf/scripts/gold/` (16)

| # | Script | Assembly site(s) | Class | Reasoning |
|---|---|---|---|---|
| 1 | INF_09.generate_partner_analytics.py | L333-339 `as_completed`→`dfs.append` | CLASS-I | Completion-order append, but concat feeds groupby/sum; no order-sensitive dedup. Deterministic output. |
| 2 | INF_A_03.positions_cube.py | L262/269 expand pool; L339/352 write pools | CLASS-I | `*_parts` built in a sequential loop (L253-256); expansion is numpy; write pools order-irrelevant; output `sort_values('date')` L296/318. |
| 3 | INF_B_01.holdings_lots.py | L169-175 `as_completed`→`process_one_date` (returns counts) | CLASS-I | Per-date keyed write-pool; no cross-date assembly. |
| 4 | INF_B_01b.classify_new_securities.py | L79-82 `as_completed`→tickers | CLASS-I | Ticker classification/union; order-insensitive. |
| 5 | INF_C_02.client_performance.py | L274-277 `pool.map(load_one_perf, dates)`→append; L406 `keep='last'` | CLASS-I | `pool.map` preserves date order; L406 dedup runs on a `sort_values(['household_id','date'])`-ordered frame → deterministic. |
| 6 | INF_C_03.account_performance.py | L190-193 + L222 `pool.map`→append; L258 `keep='last'` | CLASS-I | Same: `pool.map` ordered + `sort_values(['date','account_id'])` before dedup → deterministic. |
| 7 | INF_D_00b.portal_timeseries.py | L140-146 + L473-483 `as_completed`→`*_parts.append` | CLASS-I | Parts feed period-groupby aggregation; no order-sensitive dedup. |
| 8 | INF_D_00c.portal_leaderboard.py | L173-179 `as_completed`→`dfs.append` | CLASS-I | Concat → leaderboard aggregation; `drop_duplicates('household_id')` L733/908 are map-dedups; order-insensitive. |
| 9 | INF_D_00d.cumulative_chart.py | L140-146 `as_completed`→`dfs.append` | CLASS-I | Concat → cumulative aggregation + latest-snapshot `drop_duplicates('household_id')`; order-insensitive. |
| 10 | INF_D_00f.advisor_nna_canonical.py | L119-125 `as_completed`→`dfs.append` | CLASS-I | Concat → nna aggregation; `drop_duplicates()` L182 on acct→hh map; order-insensitive. |
| 11 | INF_D_02.advisor_client_detail.py | L183-189 `as_completed`→`dfs.append`; L2316-2321 `as_completed`→`_build_one(hh_id)` keyed writes | CLASS-I | Per-household independent keyed outputs; all fee `keep='last'` (L1340/1533/1603) preceded by `sort_values('effective_date'/'period_end')` → deterministic. |
| 12 | INF_D_03.composition_artifacts.py | L664 `pool.map`→`_date_lots[_d2]` keyed; L769-771 `_write_one` write-pool | CLASS-I | Keyed-dict + write-only; order-irrelevant. |
| 13 | INF_D_04.client_portal_summary.py | L369-375 `as_completed`→`dfs.append`; L780 `sort_values([...]).drop_duplicates('account_id',keep='last')` | CLASS-I | `keep='last'` on a fully `sort_values(['account_id','period_end'])`-ordered frame → max period_end per account, deterministic. |
| 14 | INF_D_04b.client_publishers.py | L363-365 `as_completed`→`_publish_one` write-pool | CLASS-I | Per-household keyed writes. |
| 15 | **INF_D_06.cash_drag.py** | L273-278 `as_completed`→`frames.append`; **L383 `drop_duplicates(subset=['account_id','trade_date','trans_amount'])`** (default `keep='first'`) | **CLASS-N** | Completion-order append feeding a subset dedup with no `keep=` and no preceding full sort → survivor of multi-snapshot duplicates depends on thread-completion order. **Materialization caveat:** benign IF the duplicate rows are byte-identical across snapshots (CTO adjudicates). |
| 16 | INF_D_09.account_timeseries.py | L271-273 `as_completed`→`_publish_one` write-pool; L289-293 cache `keep='last'` | CLASS-I | Per-account keyed tasks (no parallel key collision); cache-vs-new resolved by concat position (`_cache` first, `_new_df` second, L289), not completion order. |

**inf tally:** CLASS-N **1** (D_06) · CLASS-I 15 · SINGLE-SOURCE 0.

---

## Table 2 — `data/cot/scripts/gold/` (29)

| # | Script | Assembly site(s) | Class | Reasoning |
|---|---|---|---|---|
| 1 | A_00.accounts_dimension.py | L214-219 index-slot (`dfs=[None]*len`; `dfs[futures[future]]=...`); L231 `keep='last'`(txn_id) | CLASS-I | Index-slot deterministic. |
| 2 | **A_01.advisor_assignments.py** | L175-181 `dfs.append(fut.result())` (`as_completed`); **L192 `keep='last'`(txn_id), L231 `keep='last'`(trade_date), L373 `keep='last'`(account_id,trade_date)** | **CLASS-N** | Completion-order append + order-sensitive SCD dedups. bd twin dispositioned-benign in A/B/E adjudication. |
| 3 | **A_02.fee_rate_history.py** | L141-147 `dfs.append` (`as_completed`); **L194 `keep='last'`(trade_date), L269 `keep='last'`(account_id,trade_date)** | **CLASS-N** | Completion-order append + order-sensitive fee-SCD dedups. bd twin dispositioned-benign. |
| 4 | A_03.positions_cube.py | L883-890 index-slot; L913 `keep='last'`(txn_id) | CLASS-I | Index-slot deterministic. Twin of bd A_03 (deployed-fixed 5d2fca51). |
| 5 | **A_04.client_dimension.py** | L112-115 `dfs.append(fut.result())` (`as_completed` over `sorted(keys)`); **L120 `keep='last'`(txn_id)** | **CLASS-N** | `sorted(keys)` orders submission, NOT completion; append is completion-order + order-sensitive txn_id dedup. **KEY CROSS-FIRM FINDING:** bd A_04 was fixed to index-slot (9a89926fd, GLDINC keep-full); cot A_04 was NOT mirrored (firm separation) → **unfixed twin**. |
| 6 | build_canonical_prices_v2.py | L100-114 index-slot (load_transactions); L578-593 `results[idx]=result` index-slot (resolve_worker); L133 `keep='last'`(txn_id) | CLASS-I | Both assemblies index-slot deterministic. |
| 7 | B_00.canonical_holdings.py | L1249-1254 + L1354-1361 `as_completed`→`all_stats.append` | CLASS-I | Compute-pools return stats; data written inside per-date workers; no cross-date assembly. |
| 8 | B_01.holdings_lots.py | L248-251 index-slot; L264 `keep='last'`(txn_id) | CLASS-I | Index-slot. Twin of bd B_01 (deployed-fixed 5d2fca51). |
| 9 | B_02.canonical_lots.py | L798-803 `as_completed`→`all_stats.append`; write-pools | CLASS-I | Stats-only assembly; per-date keyed. |
| 10 | B_03.account_gains.py | L767-772 `as_completed`→`all_stats.append` | CLASS-I | Stats-only; the `keep='last'`(txn_id) L351/543 run WITHIN per-pair workers over deterministic inputs. |
| 11 | C_00.canonical_performance.py | L194-197 `pool.map(_load_one, dates)`→append | CLASS-I | `pool.map` input-order preserving; `drop_duplicates(['_date_str','relationship_id'])` L260 on ordered frame. |
| 12 | C_01.canonical_nna.py | L851/912-917 `as_completed`→`all_stats.append`; L512/640 `frames.append` sequential | CLASS-I | Stats-pool + sequential frame build; `nlargest(...,keep='first')` L393 deterministic. |
| 13 | C_01b.role_aua_backfill.py | L260-262 `as_completed`→`_process` (returns stats) | CLASS-I | Compute-pool per-date; `grouped.drop_duplicates([date,advisor,role])` L144 inside deterministic per-date work. |
| 14 | C_02.client_performance.py | L121-126/162-167/235-242 `as_completed`→`dfs.append`; L380-384 named fan-out | CLASS-I | Perf-partition appends feed relationship-level groupby aggregation; no order-sensitive dedup on the concat (`drop_duplicates('account_id')` L152/215/266 are on the separately-loaded dim). |
| 15 | C_03.account_performance.py | L121-126 `as_completed`→`dfs.append`; L188-190 named fan-out | CLASS-I | Aggregation + `sort_values`; dim `drop_duplicates('account_id')` L208 only. |
| 16 | C_06.client_mix_timeseries.py | L598 compute-pool; L713-716/819-822 write-pools | CLASS-I | Per-date keyed compute + write. |
| 17 | C_08.advisor_fee_efficiency.py | L619-623 index-slot (`nna_dfs=[None]*len`); L835-839 write-pool; `keep='last'` L139/162 = `sort_values('effective_date').drop_duplicates(keep='last')` | CLASS-I | Index-slot + sort-ordered dedups deterministic. |
| 18 | D_00.portal_aggregates.py | L304-318 named fan-out (fut_perf/fut_fee/fut_cdim/fut_adim/fut_tax) | CLASS-I | Results placed by named future, deterministic. |
| 19 | D_00b.portal_timeseries.py | L337-343/473-483 `as_completed`→`parts.append`; L696 `pool.map`; L1302 named fan-out | CLASS-I | Parts feed period aggregation; dim dedups order-insensitive. |
| 20 | D_00c.portal_leaderboard.py | L94-100/140-146 `as_completed`→`dfs/parts.append`; L1206 named fan-out | CLASS-I | `melted.drop_duplicates` are counting-dedups (distinct (account,advisor) pairs); order-insensitive for the metric. |
| 21 | D_01.partner_analytics.py | L442-448 index-slot (`dfs=[None]*len`; `dfs[futures[f]]=f.result()`); L334 named fan-out | CLASS-I | Index-slot deterministic. |
| 22 | D_02.advisor_client_detail.py | L152-157 write-pool; L433 named fan-out; L1623-1629/1718-1724 `as_completed`→`parts.append`; fee `keep='last'` L1039/1170 sort-ordered | CLASS-I | Write/keyed + sort-ordered dedups. |
| 23 | D_03.composition_artifacts.py | L197-202/740/811/853 write-pools | CLASS-I | Per-key writes. |
| 24 | D_04.client_portal_summary.py | L248-253 write-pool; L266-272 read-pool→`results[k]=data` keyed; L1618-1624 `as_completed`→`parts.append` | CLASS-I | Keyed-dict + write-only + composition aggregation. |
| 25 | E_20.cross_script_validation.py | reads into `results['<script>']` keyed dict | CLASS-I | Validation reads keyed by script name. |
| 26 | E_24.rebuild_fee_scorecard.py | L200-206 `as_completed`→`dfs.append`→concat | CLASS-I | Completion-order append but feeds scorecard aggregation; no order-sensitive dedup. |
| 27 | validate_platinum_consistency.py | L87-93 `as_completed`→`results[key]=data` keyed dict | CLASS-I | Keyed by S3 key, deterministic. |
| 28 | lib/nna_flows.py | L115-122 index-slot (`dfs=[None]*len`); L408-417 index-slot (`tagged=[None]*len`, "preserving sorted-key order"); `keep='last'`(txn_id L159, composite L198) | CLASS-I | Index-slot + GLDINC-P1-hardened to reproduce the oracle byte-for-byte (explicit order-determinism comments L149/L169). |
| 29 | lib/schwab_flows.py | L124-127 index-slot (`dfs=[None]*len`) | CLASS-I | Index-slot deterministic. |

**cot tally:** CLASS-N **3** (A_01, A_02, A_04) · CLASS-I 26 · SINGLE-SOURCE 0.

---

## Table 3 — `data/black_diamond/scripts/gold/` C_*/D_* completeness pass (14)

(A_*/B_*/E_* already adjudicated — out of scope.)

| # | Script | Assembly site(s) | Class | Reasoning |
|---|---|---|---|---|
| 1 | C_00.canonical_performance.py | L194-197 `pool.map(_load_one, dates)`→append | CLASS-I | `pool.map` input-order preserving. |
| 2 | C_01.canonical_nna.py | L851/914 `as_completed`→`all_stats.append`; L512/640 `frames.append` sequential | CLASS-I | Stats-pool; `nlargest(...,keep='first')` deterministic. |
| 3 | C_01b.role_aua_backfill.py | L260-262 `as_completed`→stats | CLASS-I | Compute-pool per-date. |
| 4 | C_02.client_performance.py | L121-126/162-167/235-242 `as_completed`→`dfs.append`; L380 named fan-out | CLASS-I | Relationship aggregation; no order-sensitive dedup on concat (dim `drop_duplicates('account_id')` only). |
| 5 | C_03.account_performance.py | L121-126 `as_completed`→`dfs.append`; L188 named fan-out | CLASS-I | Aggregation + `sort_values`; dim `drop_duplicates('account_id')` L208. |
| 6 | C_06.client_mix_timeseries.py | L600 compute-pool; L715/821 write-pools | CLASS-I | Per-date keyed. |
| 7 | C_08.advisor_fee_efficiency.py | L619-623 index-slot (`nna_dfs=[None]*len`); L835 write-pool; `keep='last'` L139/162 sort-ordered | CLASS-I | Index-slot + deterministic dedups. |
| 8 | D_00.portal_aggregates.py | L304 named fan-out | CLASS-I | Named futures. |
| 9 | D_00b.portal_timeseries.py | L337-343/473-483 `as_completed`→`parts.append`; L1302 named fan-out | CLASS-I | Period aggregation. |
| 10 | D_00c.portal_leaderboard.py | L94-100/140-146 `as_completed`→`dfs/parts.append`; L1206 named fan-out | CLASS-I | Counting-dedups order-insensitive. |
| 11 | D_01.partner_analytics.py | L443-448 index-slot; L336 named fan-out | CLASS-I | Index-slot deterministic. |
| 12 | D_02.advisor_client_detail.py | L152-157 write-pool; L433 named fan-out; L1623-1629/1718-1724 `as_completed`→`parts.append`; fee `keep='last'` L1170/1834/1874/1984 sort-ordered | CLASS-I | Write/keyed + sort-ordered dedups. |
| 13 | D_03.composition_artifacts.py | L197-202/740/811/853 write-pools | CLASS-I | Per-key writes. |
| 14 | D_04.client_portal_summary.py | L248-253 write-pool; L266-272 read-pool keyed; L1618-1624 `as_completed`→`parts.append` | CLASS-I | Keyed/write + composition aggregation. |

**bd C/D tally:** CLASS-N **0** · CLASS-I 14 · SINGLE-SOURCE 0. **Clean completeness pass** — the bd defect was isolated to A_04 (already fixed).

---

## CLASS-N summary (4 total) + fix routing

| Finding | Tree | Confidence / disposition |
|---|---|---|
| **cot A_04** (client_dimension) | cot | **HIGH — actionable.** Unfixed twin of bd A_04 (fixed to index-slot 9a89926fd). The exact shape bd deemed worth fixing. **DORMANT** — cot is not-yet-incrementalized (lib/nna_flows confirms "cot has no live load_flows cache state yet"), so this is a **prophylactic** landmine for cot's first incremental cutover, not a live served-output defect today. |
| cot A_01 (advisor_assignments) | cot | MEDIUM — shape-positive; bd twin dispositioned-**benign** in A/B/E adjudication (duplicate-key rows byte-identical / output not order-bearing). Likely no fix; CTO confirms. |
| cot A_02 (fee_rate_history) | cot | MEDIUM — shape-positive; bd twin dispositioned-**benign**. Likely no fix; CTO confirms. |
| inf INF_D_06 (cash_drag) | inf | MEDIUM — shape-positive (completion-order append + subset `drop_duplicates`, no `keep=`/no preceding sort). **Caveat:** benign IF multi-snapshot duplicate rows are byte-identical. CTO adjudicates materialization. |

**Fix routing (do NOT fix in this TO — per TO scope + CLAUDE.md Rule 13 firm separation):**
- cot findings (A_04 / A_01 / A_02): any fix deploys **ONLY** to `opal-data-cot` — never mirrored/synced from bd. Cross-firm refs are commit- and IAM-blocked. The index-slot conversion is the standard remedy (mirror bd A_04's 9a89926fd pattern: `dfs=[None]*len(keys)` + `dfs[futures[future]]=...`). cot A_04 is the only one with bd-fix precedent; A_01/A_02 await CTO benign/non-benign call.
- inf finding (D_06): inf-tree fix, routes to the inf gold lane. Remedy = either index-slot the read or add `keep=`+full-sort to the dedup (or confirm byte-identical dups → no-op).
- **never-widen treatment** is per movement: an index-slot conversion that produces DELTA=0 served output (the bd A_04 "keep-full" precedent) takes no dual-sign-off hold; only a nonzero served delta takes full CTO+COO sign-off.

**Coordination:** DS has a sibling TO (AST-DEDUP commit-time detector). Delivery timed so CTO adjudicates both together.
