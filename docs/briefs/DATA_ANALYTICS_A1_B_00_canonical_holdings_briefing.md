# B_00 -- canonical_holdings -- DATA_ANALYTICS layer briefing

**Script:** `data/black_diamond/scripts/gold/B_00.canonical_holdings.py`
**Output:** `gold/canonical/holdings/{date}.parquet` (+ `gold/canonical/holdings_gaps/{date}.parquet` diagnostic, + `gold/canonical/watermarks.json`)
**Layer / order:** Group B (canonical), order 100; catalog line 84. Reads positions_cube (A_03, implicit FUNC-key), Schwab RPS silver, the CUSIP bridge (silver/unrealized + silver/realized), schwab_bd_account_mapping, canonical_prices (S_00), accounts_dimension (A_00).
**Essential status (Andrew's framework):** ESSENTIAL -- AGNOSTIC-core. `canonical_holdings` -> B_02, B_03, C_02, D_04 (Group-D / transitive closure -> ADVI/MDPF). The reconciled point-in-time holdings snapshot -- the reference shape every firm with a custodian needs.
**Author/project:** 0.4.0_DS_ClientPlatform / ADVI_GLDOPS (2026-04-06).
**Briefing by:** 0.4.0_DS_ClientPlatform, 2026-06-25 (Andrew-direct A1 layer-walk, B-tier). Source-grounded (file:line) + deployed-context.

---

## 1. What it does

Merges the **BD FIFO positions** (`positions_cube`, A_03) with the **Schwab RPS daily custodial snapshot** into one authoritative holdings table per date, reconciling the two feeds per (account, asset). Schwab is joined via a CUSIP bridge (unrealized + realized -> asset_name) and the schwab<->bd account mapping. For dates without Schwab coverage (weekends/holidays), all positions fall back to `source='bd'`.

## 2. Architecture / data flow

1. **CUSIP bridge** (`build_cusip_bridge`, L258) -- map Schwab CUSIP -> bd asset_name via silver/unrealized (primary) + silver/realized (extended).
2. **Per-date reconcile** (`reconcile_date`, L465): merge bd vs schwab on (account, asset); tolerance `threshold = max(TOLERANCE_ABS=0.01, TOLERANCE_PCT=0.001 * schwab_units)` (L510).
3. **Source classification** (L524-532): default `bd` (BD-only); `reconciled` = has_bd & has_schwab & agrees-within-tolerance; `schwab_override` = has_bd & has_schwab & disagree; `schwab` = Schwab-only gap-fill; `bd_stale` = bd FIFO position the custodian does NOT confirm (a "FIFO ghost", L515).
4. **Custodian-authoritative resolution** (L553-565): `bd_stale` -> 0 (ghost dropped to the gaps diagnostic, L744); `reconciled` / `schwab_override` / `schwab` all take **Schwab units** -- `schwab_authoritative = source.isin(['schwab','reconciled','schwab_override'])` (L565). For any Schwab-covered account, **Schwab is the custodian of record and wins.**
5. **Split + write** (L1143-1154): Schwab-reconciled dates vs non-Schwab (weekend/holiday) dates processed separately; the weekend dates reuse the prior Schwab-reconciled canonical instead of raw BD.

## 3. Recompute posture -- WATERMARK + 14-day rolling reprocess (NOT SCD-incremental)

- **Catalog = `B_00|...|--upload --force-recent-days 14`** (line 84). B_00 is NOT in `INCREMENTAL_CAPABLE` (=A_00,A_02,C_06) and the `--incremental` flag is parse-gated to that set only (DH-2, L264). B_00's model is different: a **watermark** (`gold/canonical/watermarks.json`) skips already-processed older dates, and **`--force-recent-days 14`** deliberately rebuilds the trailing 14 days every run (a restatement window -- late-arriving Schwab files / back-dated corrections land within 14 days).
- This is a HEALTHY date-partitioned model (it does NOT rebuild 2020-present nightly), with an explicit, bounded restatement window. Not a full-recompute offender like A_04. The 14-day window is a deliberate correctness choice (custodian files settle/restate within ~2 weeks), not waste.
- Note the io ROLLING-WINDOW flag (canonical_holdings appears in both READS and WRITES): that is the prior-run self-read for the weekend/holiday carry (L1149) + the watermark skip -- a true rolling pattern, not a false positive.

## 4. The A_03-redundancy confirmation (cross-links the A_03 cutover decision)

This is the **source mechanism** behind my A_03 Option-A recommendation (ETFS/A1 cross-finding, commit 5f61747c1): A_03 injects a current-snapshot RPS reconciliation into `positions_cube`. But B_00 **re-reconciles the SAME Schwab RPS feed** against positions_cube and makes **Schwab the custodian of record** (L565) -- so for the Schwab (49F) book, B_00's output is already effectively snapshot-native from RPS regardless of what A_03 injected upstream. A_03's injection is therefore **redundant for the Schwab book** (B_00 supersedes it). This is SOURCE-CONFIRMED at B_00 L524-565 (not inferred). It is the grounding for "remove A_03's redundant injection" (Option A) being the smaller, de-risking fix -- the canonical holdings do not lose the Schwab reconciliation, because B_00 performs it.

## 5. Tech debt / smells

- **NAME_ALIASES hardcode (L75-79):** maps `OPAL DIVIDEND INCOME ETF` / `EVENTIDE HIGH DIVIDEND ETF` -> `POLEN DIVIDEND INCOME ETF`, and an identity self-map for the international ETF. These are real vendor name-history aliases (ETF rebrands), but a hardcoded 3-entry dict in gold is fragile -- belongs in a silver name-canonicalization map or a config. Note for A2 (a mild FIRM-SPECIFIC-thin smell; the names are Opal-ETF-specific).
- **CUSIP bridge depends on silver/unrealized + silver/realized** for asset_name resolution -- a position whose CUSIP is in neither bridge source is `is_unresolvable` and its bd_stale is kept as `bd` (L546) rather than ghost-dropped. Defensible (don't drop a position you can't bridge), but it means bridge-coverage gaps silently pass through as bd-sourced.
- `datetime.utcnow()` (L97) -- deprecation-warns on newer Python; cosmetic on the py39 runner.

## 6. What's GOOD (keep)
- **Custodian-authoritative reconciliation** is the correct design: the custodian (Schwab) is the source of truth for what an account holds; bd FIFO is the cross-check, and FIFO ghosts (positions the custodian doesn't confirm) are correctly zeroed to the gaps diagnostic rather than served.
- **Bounded restatement window** (`--force-recent-days 14`) instead of either a naive full-rebuild or a no-restatement incremental -- matches custodian settle/restate cadence.
- **Tolerance-based agreement** (abs OR pct) rather than exact-match -- robust to rounding between the two feeds.

## 7. Actions

| When | Action | Owner |
|---|---|---|
| A2 | Move `NAME_ALIASES` (L75-79) to a silver name-canonicalization map / config (de-hardcode the Opal-ETF rebrands) | DS (+ silver) |
| A3 cutover (gated) | Use this B_00-reconciliation confirmation as the grounding for A_03 Option-A (remove A_03's redundant RPS injection -- B_00 supersedes it for the Schwab book) | DS / Andrew cutover-go |
| -- | Recompute: NO action -- watermark + 14-day restatement is healthy + deliberate | -- |

## 8. Status / ledger row

- **Tag: ESSENTIAL / AGNOSTIC-core** (the reconciled snapshot; feeds B_02/B_03/C_02/D_04 -> portal).
- **Recompute: HEALTHY** (watermark skip-old + bounded 14-day restatement; not a full-recompute offender).
- **Cross-finding: source-confirms the A_03 redundancy** (B_00 is custodian-authoritative on the same RPS feed) -- the Option-A grounding.

### Ledger entry (supersedes the v0.1 INFERRED B_00 row)
| Script | Output | Consumers | Tag | Recompute | Notes |
|---|---|---|---|---|---|
| B_00.canonical_holdings | gold/canonical/holdings/{date} (+holdings_gaps, +watermark) | B_02, B_03, C_02, D_04 | ESSENTIAL / AGNOSTIC-core | watermark + 14d restatement (HEALTHY) | custodian-authoritative bd<->Schwab-RPS reconcile (Schwab wins, L565); SOURCE-CONFIRMS A_03 RPS-injection redundancy; NAME_ALIASES hardcode -> silver (A2) |
