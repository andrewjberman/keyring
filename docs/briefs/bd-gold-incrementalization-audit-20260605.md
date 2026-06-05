# bd-gold Incrementalization Audit (ADHC_GLDINC Phase 0) — 2026-06-05

**Author:** 0.6.0_AE_PartnerETL (lead) · co-lead 0.4.0_DS (data-semantics axis) ·
**Type:** exploratory/analysis-only (no pipeline changes, no ad-hoc runs) ·
**Substrate:** the 27 gold scripts + the R3 perf_report + the validated 14-phase DAG in `gold_dispatch.sh`.

## Thesis + honest headline
bd-gold reprocesses the ENTIRE dataset (2020→present, ~1,764 daily txn files) every night; ideally compute scales with the daily delta. **The honest read: this is NOT a clean ground-up rebuild NOR a few-scripts win — it's a TIERED HYBRID.** ~14 of 27 scripts are already-incremental or cleanly incrementalizable (the per-date and per-entity layers — the bulk of compute + ALL of the 76GB memory floor); ~7 are FULL-RECOMPUTE-INHERENT (firm-level aggregates/rankings/distributions) that can only be made cheaper-to-read, not delta-reduced. **Realistic target: incrementalize the per-date + per-entity + memory-floor layers (large compute + memory win on typical-delta nights), keep the firm-aggregate floor as full-recompute. The single biggest structural prize is A_03 — its 76 GB is a materialization convenience, not an inherent aggregation; breaking it drops the memory floor below r6i.4xlarge (compounds R3).**

## 1. Phase/DAG map (the 14-phase validated dependency graph)
From `gold_dispatch.sh` PARALLEL CHAIN DISPATCH (the authoritative dependency structure; serialized where memory-bound):
```
A1: A_00 ‖ A_02 ‖ A_03            (dimensions + positions cube — independent)
A2: A_01 ‖ A_04
B1: B_00                          (canonical_holdings — serialized; B_01 reads its dynamic-keyed output)
B2: B_01                          (holdings_lots FIFO — serialized; B_00‖B_01 stacked 1.38 TB RSS → paging)
B3: B_01b                         (classify_new_securities → DynamoDB bd-securities, B_02 reads)
B4: B_02                          (canonical_lots)
B5: B_03 ‖ C_05
C1: C_00 ‖ C_01                   C2: C_02   C3: C_03   C4: C_04 ‖ C_07   C5: C_06 ‖ C_08
D1: D_00 ‖ D_00c ‖ D_03 (gate aua_certification)   D2: D_00b ‖ D_01 (gate role_aua)   D3: D_02   D4: D_04
```
Layering: **A** = dimensions/cube (silver→gold) · **B** = canonical holdings/lots/gains (per-date) · **C** = performance/NNA/analytics (per-date + cumulative + scorecards) · **D** = portal-serving artifacts (firm-level + per-entity fan-out). Note the B-serialization is memory-forced (the same RAM-paging that R3 found), not a logical dependency for all of it.

## 2. Per-script classification (27 scripts)
Verdicts: **CA** = CLEAN-APPEND · **IWR** = INCREMENTAL-WITH-RECONCILE · **FRI** = FULL-RECOMPUTE-INHERENT. "built" = increment already implemented.

| Script | computes | transform nature | reads full history? | verdict |
|---|---|---|---|---|
| A_00 accounts_dimension | 1-row/account metadata dim | agg(latest-per-acct)+join | full OR watermark | **IWR (built)** — merge_incremental works |
| A_01 advisor_assignments | SCD-2 advisor team/split | window (per-acct change-detect) | full | **IWR** — per-acct splice; not built |
| A_02 fee_rate_history | SCD-2 fee bps/schedule | window (per-acct SCD) | full (fees) | **IWR** — per-acct splice; not built |
| **A_03 positions_cube** | daily open-position cube | window(cumsum)+**expansion**+inject | full (cum_units mandatory) | **IWR** — 76 GB = all-at-once pair×day materialization, NOT inherent (see §3) |
| A_04 client_dimension | household rollup dim | agg(per-household)+join | full only for 90d-active flag | **IWR** — only trailing 90d needed |
| B_00 canonical_holdings | per-date reconciled holdings | join(BD⋈Schwab)+row | per-date + **sealed watermark** | **CA (built)** |
| B_01 holdings_lots | FIFO lot snapshot/date | window(FIFO)+rebalance(inject) | full (FIFO lot history) | **IWR** — per-position FIFO state; not built |
| B_01b classify_new_securities | LLM-classify new securities | row (set-diff) | watermark-incremental | **CA (built)** |
| B_02 canonical_lots | per-date canonical tax lots | join(BD⋈Schwab lots)+row | per-date | **CA** |
| B_03 account_gains | AUA-change decomposition | row/agg (per-acct) | per-date (+1 prior day) | **CA (built)** |
| C_00 canonical_performance | relationship daily perf + cum | agg+join+**cumsum** | full (cum) | **IWR** — carry prior cum |
| C_01 canonical_nna | per-acct NNA + nna_atomic cum | row+join (+cumsum) | per-date / full (atomic) | **IWR** — nna/{date} is CA; nna_atomic cum is reconcile |
| C_01b role_aua_backfill | (advisor,role) AUA split | row+melt+agg, per-date | per-date (skip-existing) | **CA** |
| C_01c role_aua_flow_join | join flows into role_aua | row+agg+join, per-date | per-date | **CA** |
| C_02 client_performance | relationship timeseries | join+agg+**cumsum**, monolithic | full | **IWR** — cum carry + single-file overwrite |
| C_03 account_performance | account timeseries | join+**cumsum dense-grid**, monolithic | full | **IWR** — cum carry + single-file overwrite |
| C_04 validate_aua | per-date AUA validation | agg+setdiff, per-date | per-date | **CA** |
| C_05 client_tax_liability | latest-snapshot tax view | agg of latest lots | latest snapshot only | **FRI** (no date axis; cheap-ish) |
| C_06 client_mix_timeseries | per-rel asset-mix timeseries | per-date agg, per-rel merge | watermark-incremental | **CA (built)** — the proven template |
| C_07 advisor_attribution | advisor team attribution | **modal+global thresholds+learned pairing** | latest snapshot | **FRI** (global population) |
| C_08 advisor_fee_efficiency | fee detail + scorecard | PIT join+agg+**percentile/regression** | per-date / full-window | **IWR** — detail CA; scorecard full-window |
| D_00 portal_aggregates | firm aggregates/snapshots | agg+join (+small rank) | full (totals+TTM NNA) | **FRI** (firm cross-section) |
| D_00b portal_timeseries | firm timeseries chart | agg+window+rank | full (whole time axis) | **FRI** (cumulative + top-N) |
| D_00c portal_leaderboard | advisor leaderboard | **ranking+OLS**+agg | full + MAX window | **FRI** (firm-wide ranking) |
| D_01 partner_analytics | distribution dashboards | agg+distribution stats+rank | full (only ~8 boundary dates used) | **FRI** (full cross-section per period; date-pushdown read = the only win) |
| D_02 advisor_client_detail | ~8,000 per-entity files | agg+SCD-PIT+window+rank | full (per-entity timeseries) | **IWR** — dirty-entity set; only changed entities need rewrite |
| D_03 composition_artifacts | per-entity composition | agg+rank(top-9) | latest snapshot | **IWR** — dirty-entity (latest holdings) |
| D_04 client_portal_summary | ~5,300 platinum consolidations | join/merge/pass-through | mostly pre-built gold JSON | **IWR** — change-detect by upstream S3 LastModified |

Tally: **CA = 8** (5 built) · **IWR = 12** · **FRI = 7**.

## 3. THE BINDING CONSTRAINT — A_03.positions_cube (the 76 GB / 128 GB-box reason)
**Finding: the 76 GB peak is NOT an inherent full-population aggregation — it is a materialization convenience.** A_03's FIFO cumulative-units is **per-(account,asset)** (independent across positions). The memory hog is `expand_pairs_to_daily()` building the entire pair×day cross-product (~300 M rows) in ONE DataFrame "all at once" (the code's own annotation, ~line 1559) before partitioning by date. Evidence it's not inherent: `_expand_one_pair()` is already a pure per-pair function, and `build_single_date()` already produces one day cheaply from the snapshot (`groupby.cum_units.last()`, `units>0`). The genuine incrementalization blockers are **bounded/periodic, not per-row**: (1) forward-fill of dormant buy-and-hold positions to today (a position with no recent txn must still appear), (2) global synthetic injection (RPS/realized/unrealized) that rewrites cum_units on specific injection dates, (3) the latest-allocations phantom/alive gate. **Implication: a stateful per-pair cum-unit store + forward-fill-only-changed + reconcile-on-injection-dates drops the memory floor below r6i.4xlarge → an even smaller/cheaper box (R3 follow-on "R3c").** This is the single highest-leverage structural change.

## 4. Existing primitives to leverage (don't reinvent)
- `--incremental` (date-watermark, currently gated to `--single A_00`/`C_06`) + `--from <id>` (resume by A/B/C/D dependency group). Sealed-day watermarks already in B_00, B_01b, C_06.
- **Proven incremental templates already in-repo:** B_00 (sealed-day watermark + per-date append), B_01b (watermark + PK-keyed new-only), **C_06 (watermark + `date>watermark` + per-relationship JSON merge — the textbook pattern to replicate for the per-entity fan-out)**.
- A_00's `merge_incremental()` (folds a new batch into the existing dimension, recomputing only household-min dates over the merged set) is the SCD template for A_01/A_02.

## 5. Correctness / reconcile (where it gets subtle)
- **Cumulative columns (C_00/C_02/C_03, C_01 nna_atomic):** carry last cum-value per key + add today's delta. RECONCILE: account-reassignment between relationships makes cumulatives recompose from *current* membership — so a blind append is wrong on reassignment days; needs a dirty-relationship trigger + periodic full re-derive. C_02/C_03 also write a **monolithic single parquet** (output-shape obstacle — must move to partitioned or read-modify-append).
- **A_03 / B_01 FIFO state:** late-arriving/restated transactions mutate historical lots → a persisted FIFO state must be invalidatable per-position; reconcile = full re-FIFO on a periodic cadence + on detected restatement. Synthetic-injection dates always re-run the whole-book pass.
- **Per-entity fan-out (D_02/D_03/D_04):** the dirty-set = entities whose underlying rows changed in the new account_performance dates (or changed latest holdings). RECONCILE: the embedded firm-ranking (D_02 implementor leaderboard), firm composition (D_03), and firm pass-throughs (D_04) still recompute fully; stale-entity prefix-deletion must still run.
- **Hidden full-scan:** `load_flows_from_transactions()` (shared by C_01/C_02/C_03) reads the ENTIRE silver transaction set every run regardless of date args — an engineering full-scan, not an inherent dependency. Highest-leverage shared I/O fix (3 scripts at once), zero correctness change.

## 6. Roadmap + ROI (phased: biggest win × lowest risk first)
| Phase | Change | Win | Risk |
|---|---|---|---|
| **P1** | `load_flows_from_transactions()` → date-windowed/watermarked read (C_01/C_02/C_03) | pure I/O cut on 3 scripts; no correctness change | LOW |
| **P2** | **A_03 positions_cube → stateful per-pair cum-unit store + forward-fill-changed + reconcile-on-injection** | **drops the 76 GB memory floor → box smaller than r6i.4xlarge (compounds R3); A_03 545s→delta-scaled** | MED-HIGH (FIFO state + injection reconcile; `build_single_date` is the proven cheap path) |
| **P3** | D_02 + D_04 dirty-entity-set fan-out (rewrite only changed entities) | D_02 is the #2 wall long-pole (746s) + ~8,000-file fan-out; D_04 change-detectable by S3 LastModified | MED (dirty-set derivation + periodic full reconcile) |
| **P4** | Cumulative-carry for C_00/C_02/C_03 (+ B_01 per-position FIFO state) | cuts the C-layer + B_01 (1180s #1 long-pole) | MED (reassignment reconcile + monolithic→partitioned output) |
| **leave FRI** | C_05, C_07, D_00, D_00b, D_00c, D_01 — firm aggregates/rankings/distributions | optimize reads only (date-pushdown for D_01); cannot delta-reduce | n/a |

**Realistic compute reduction:** on a typical small-delta night, P1-P4 could cut the per-date + per-entity compute substantially (the long poles B_01/D_02/A_03 = ~44% of wall are all in the incrementalizable set), PLUS the A_03 memory-floor drop. But the firm-aggregate floor (D_00b timeseries, D_00c ranking, C_07, D_00/D_01) is irreducible full-recompute — so this is a **hybrid ~50-70%-on-typical-nights win + a memory-floor structural drop, not a 90%+ elimination.** The A_03 memory win (P2) is the standout because it changes the BOX SIZE (compounds R3 directly), independent of wall time.

**Greenlight recommendation:** YES to a build PRD, scoped as the P1→P2→P3 sequence (P1 quick I/O win to validate the watermark plumbing, P2 the memory-floor prize, P3 the fan-out long-pole). P4 + the FRI read-optimizations as a follow-on. Each phase independently shippable + validatable on the scheduled nightly (no ad-hoc runs), revert-per-phase. Coordinate the reconcile-correctness design (cumulative reassignment, FIFO restatement, dirty-set completeness) with 0.4.0_DS — that's where the data-semantics rigor binds.

---

# ADDENDUM — two-axis optimization (Andrew framework 2026-06-05)
Per `docs/briefs/gold-rightsizing-optimization-framework-20260605.md`. This materially upgrades the §2 verdicts and the §6 honest headline.

## A1. Temporal-freeze-baseline re-examination of the 6 FULL-RECOMPUTE-INHERENT scripts
The freeze-baseline test: a firm aggregate/ranking/distribution that reads all history nightly is usually **frozen-closed-baseline + incremental-open-period + periodic-rebaseline = IWR**, not inherent. Applying it dissolves most of my "irreducible floor":

| Script | Phase-0 | freeze-baseline re-exam | New verdict |
|---|---|---|---|
| **D_00b portal_timeseries** | FRI | **Canonical case.** Closed periods of the firm timeseries are immutable → freeze as materialized baseline; nightly recompute only the OPEN current period + append; rebaseline at period boundary. Top-N per closed date is frozen; only the open tail re-pivots. Currently reads ALL canonical_nna partitions nightly = the biggest single freeze win. | **IWR (freeze-baseline)** |
| **D_00c portal_leaderboard** | FRI | Per-advisor windowed sums (3M…MAX): freeze each closed sub-period's per-advisor sufficient-statistic, nightly add open-period delta, then **re-rank across advisors (cheap O(N_adv) pass)**. OLS: carry frozen Σx/Σy/Σxy/Σx²/n + open-period updates → closed-form refit. The "ranking is global" objection dissolves — ranking is cheap; the expensive full-history window aggregation is what freezes. | **IWR (freeze + cheap re-rank/refit)** |
| **D_01 partner_analytics** | FRI | Distributions/percentiles at PERIOD-ENDS. Closed period-ends (Q1/Q2/months) are immutable → freeze their artifacts (computed once); nightly recompute only the CURRENT open period-end's cross-section. + the date-pushdown read win. | **IWR (freeze per-period-end)** |
| **D_00 portal_aggregates** | FRI | Trailing-window NNA (TTM/QTD/YTD) reads full history → freeze closed-period cumulative NNA, incremental open-period. The current AUA total is already a current-snapshot read (latest only), not a history scan. | **IWR (freeze windowed NNA)** |
| **C_05 client_tax_liability** | FRI | No date axis (latest-snapshot lot aggregation) — temporal-freeze does NOT apply. BUT snapshot-delta does: only positions whose lots changed since the prior snapshot need re-aggregation. Cheap (8s) so low priority. | **IWR (snapshot-delta)** |
| **C_07 advisor_attribution** | FRI | The genuinely population-global one: firm-wide true-architect thresholds + modal voting + a learned implementor→architect pairing table — a new account can cross a threshold / shift the learned table. BUT the learned pairing + thresholds are stable period-over-period → freeze them (recompute weekly), nightly only apply modal/threshold logic. Cheap (13s) so lowest priority. | **IWR-marginal (freeze learned table)** |

**Result: 0 of the 6 remain truly FULL-RECOMPUTE-INHERENT.** The "irreducible firm-aggregate floor" from §6 largely DISSOLVES under freeze-baseline — D_00b/D_00c/D_01 (the expensive all-history firm readers) become open-period-only nightly + a once-per-period rebaseline. The only genuinely-population-global residue is C_07's threshold/pairing core, which is both freezable (weekly) and cheap.

**Restatement/reconcile rigor (0.4.0_DS axis):** late-arriving/restated data for a FROZEN period invalidates the baseline → a **restatement trigger** must re-freeze the affected closed period (detect via a frozen-period-input watermark / checksum; re-run that period's baseline). The periodic full rebaseline is the standing drift-catch. This is the subtle correctness core — design it explicitly with 0.4.0.

## A2. Machine-sizing as a cost function (not "smallest box")
Objective = **minimize Σ(runtime × machine_rate)**, fit per-script + chain on the **perf_history archive** (just shipped — accruing from tonight). Break-even (Andrew): 1 hr @ $3 = $3; a $2/hr box wins only if < 1.5 hr. So the right-size box is the OUTPUT of the cost model, not a fixed target.
- **R3 (tonight's r6i.4xlarge) = a first-order point** on the CURRENT full-recompute algorithm — cut wasted cores at the same algorithm. Tonight's nightly gives the first r6i.4xlarge perf_history point; combined with the c6i.16xlarge history = 2 points to seed the runtime-vs-machine regression.
- As GLDINC incrementalizes (axis 1), the working set shrinks → BOTH the memory floor (smaller box) AND runtime drop together → re-fit the cost model after each phase; the cost-optimal box co-moves smaller, and shorter runtime also improves Spot economics (less interruption exposure). A_03 (P2) is the canonical synergy — it moves both factors at once.

## A3. Revised roadmap (folds both axes)
- **P0.5** (new, analysis): the freeze-baseline reclassification above → feeds the cost model the algorithm-axis options for the firm-level scripts (previously written off as inherent). Restatement-trigger design with 0.4.0_DS.
- **P1–P4** unchanged in order, but each phase now also emits a perf_history-fitted cost-model update (axis 2) so the box choice is re-derived, not assumed. D_00b freeze-baseline (formerly "leave FRI") joins as a high-value phase (it's the biggest all-history firm reader).
- **Sizing method throughout:** the cost model (A2) decides the box at each phase; R3 is the t=0 baseline point on the frontier.

**Upgraded honest headline:** with freeze-baseline, the win is LARGER than the original ~50-70% framing — the firm-level all-history readers (D_00b/D_00c/D_01) are incrementalizable too, so a typical-delta night recomputes only the open period + changed entities + a periodic rebaseline. The genuinely-irreducible residue shrinks to C_07's cheap global core. R3 + GLDINC are one joint (algorithm × machine) cost-optimization, exactly per the framework.
