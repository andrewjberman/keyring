# RA-P2 Phase 1 pre-flight memo (pre-rerun)

**Agent:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-04-15
**TO:** `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_ROLLUP.RA-P2.ds-role-aua-d02-consumer-cutover.md` (staged, gated on ~D's RA-P1 landing)
**Authorization:** COO GO 20260415T171059Z — "pre-rerun productive work for ~C".

Note for audit trail: RA-P1 was reassigned ~C → ~D per CTO 2026-04-15 for single-agent co-ship discipline with CN-P1. ~C picks up at P2.

## Phase 1 compilers

### 1. `comp-pipescript io D_02`

READS (15): `ACCOUNT_PERFORMANCE`, `ACCOUNT_TEAM`, `ADVISOR_ASSIGNMENTS`, `ADVISOR_FEE_DETAIL_PREFIX`, `CANONICAL_NNA_PREFIX`, `CLIENT_DIMENSION`, `CLIENT_TAX_LIABILITY`, `FEE_RATE_HISTORY`, `HOLDINGS_LOTS_PREFIX`, `REL_ARCHITECT_LOOKUP`, `account_aua_timeseries_key`, `advisor_book_key`, `advisor_timeseries_key`, `client_aua_timeseries_key`, `client_detail_key`.

WRITES (3): `IMPLEMENTOR_LEADERBOARD`, `advisor_mix_timeseries_key`, `client_detail_key → D_04`.

**Observed vs `<expect>`:** `gold/canonical/role_aua/` NOT yet in D_02 READS. This is the EXPECTED staged state — RA-P1 (shadow writer) lives on ~D's lane and has not committed yet. When RA-P1 lands and the nightly rerun produces `gold/canonical/role_aua/{date}.parquet`, a subsequent `comp-pipescript io D_02` (after my P2 code changes) will show `role_aua` as a new READ. Old filter-stack inputs (`ACCOUNT_TEAM`, `ADVISOR_FEE_DETAIL_PREFIX`) remain — they feed non-role code paths that P2 does NOT touch.

`if_mismatch` branch not triggered — the absence of role_aua in reads is the documented pre-RA-P1 state, not a mismatch.

### 2. `grep role_breakdown|role_ts_lookup`

Callsites in `data/black_diamond/scripts/gold/D_02.advisor_client_detail.py`:

| Ref | Grep line | Function | Role |
|---|---|---|---|
| P0 memo / TO | L1269 | `build_advisor_books` role_breakdown | Cutover target #1 |
| Actual | **L1272-1310** (comment at 1272, dict init 1276, assignment 1282, emit 1310) | same | minor +3 line drift |
| P0 memo / TO | L1619 | `build_advisor_timeseries` role_ts_lookup | Cutover target #2 |
| Actual | **L1616 comment, L1631 dict init, L1654 assignment, L1695 lookup-read** | same | minor -3 / +12 line drift |

Both callsites still present, same functions, same grain. Minor line-number drift is within normal session-to-session churn; does not indicate scope movement.

`if_mismatch` branch not triggered.

### 3. RA-P0 memo site-enumeration re-confirmation

Cross-reference vs `docs/data/role_aua_consumer_enumeration.md`:

| # | Memo citation | Current (verified) | Match |
|---|---|---|---|
| 2 | `D_02.advisor_client_detail.py:1272` (fn start :1037) | L1272 + fn start L1037 | ✓ |
| 3 | `D_02.advisor_client_detail.py:1631` (fn start :1448, assignment :1654) | L1631 + fn start L1448 + assignment L1654 | ✓ |

Both D_02 sites from the P0 memo still live exactly where the memo pointed. The other 4 sites (D_00c, D_01, D_00b, C_08) are out of scope for P2 per TO `<objective>` — deferred to P3/P4/P5.

## Cutover plan (ready-to-execute at P2 flip)

When ~D's RA-P1 lands and the nightly produces `gold/canonical/role_aua/{date}.parquet`:

1. Add a lib helper or inline read: `role_aua_df = pd.read_parquet(s3_key("gold/canonical/role_aua", date))` in D_02 main. Filter to `date == latest_date` for build_advisor_books; iterate per-date for build_advisor_timeseries.

2. **build_advisor_books (L1272 area):** replace the `role_breakdown` dict construction loop with a groupby/pivot on `role_aua_df` for the advisor: `role_breakdown[role] = { 'aua': row.aua, 'aua_tagged_total': row.aua_tagged_total, 'aua_fee_paying': row.aua_fee_paying, 'aua_no_fee': row.aua_no_fee, 'account_count': existing_account_count_map[advisor][role], ... }`. `account_count` stays on the old path for P2 (canonical does not carry it at ratified column list; W6-005 account_count remains a groupby on the existing dedup).

3. **build_advisor_timeseries (L1631 area):** replace `role_ts_lookup[(date, advisor, role)] = float(r['total_aua'])` construction with `role_ts_lookup = dict(zip(zip(role_aua_df.date, role_aua_df.advisor, role_aua_df.role), role_aua_df.aua))`. The lookup-read at L1695 is unchanged — schema-compatible.

4. Non-role code paths (books, non-role summary fields, timeseries non-role metrics) MUST NOT be modified. Acceptance #5 = zero-byte diff on those paths.

## Outstanding gates before RA-P2 can flip `staged` → `pending`

- [ ] ~D commits RA-P1 (role_aua shadow writer) + CN-P1 co-ship.
- [ ] Nightly rerun produces `gold/canonical/role_aua/{YYYY-MM-DD}.parquet` — confirm via `aws s3 ls s3://opal-data-bd/gold/canonical/role_aua/`.
- [ ] `comp-validate role_aua --artifact <parquet>` exits 0 on that artifact (acceptance #4 from RA-P2).

## Signal

Phase 1 pre-flight clean. Plan is ready. Standing by for RA-P1 commit → rerun artifact landing → `staged` → `pending` flip.
