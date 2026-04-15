# Session log — 0.4.0_DS_ClientPlatform~B (2026-04-15)

**TO:** `ADVI_ROLLUP.RA-P3.ds-role-aua-d00c-leaderboard-cutover` (Wave 4 Phase 3)
**Companion (CN-P3):** HOLD pending nna_atomic backfill (see Cross-domain section)

## Startup

Continued ~B session 28. Registered, inbox watcher live, comp-graph context updated
to `TO_ID=ADVI_ROLLUP.RA-P3+CN-P3`. Got the GO BLAST from COO (paired with CN-P3),
with one routing inversion correction (TOs ARE ~B-dialed; verified by `grep issued_to`).

## Acceptance flex (Rule 7) — APPROVED

**(a) what:** Acceptance #2 retargeted from "leaderboard.json Travis architect AUA matches D_02
summary.json role_breakdown.architect within $0.01" to "leaderboard.json Travis architect
AUA matches sum-by-role of `gold/canonical/role_aua/{latest}.parquet` within $0.01."

**(b) why:** Dependency RA-P2 (D_02 consumer cutover) is still status=`pending`.
Verified from `gold/logs/single_D_02_20260415_190511.log`: D_02 ran with RA-P1 SHADOW
WRITE only ("=== Step 1b: role_aua shadow ===") and continues to compute role_aua
locally for downstream consumers. Cross-consumer parity vs a pre-cutover sibling
would fail by construction per the drift table in
`docs/data/role_aua_consumer_enumeration.md` (D_00c canonical ON/ON/ON vs D_02
ON/partial/ON).

**(c) original vs substituted:** as in (a). CTO approval at 21:43Z
(`20260415T214328Z_1.0.0_SA_CTO_..._APPROVED___RA-P3_CN-P3_substitute_parity.md`),
no 60-sec hold required. Cross-consumer convergence formally retargeted to a
Wave 4 closeout gate after ALL consumers cut over (P3 + RA-P2/CN-P2 + RA-P2b);
COO authoring that gate TO.

## Code change

`data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py` (75 insertions, 4 deletions):

1. Import `CANONICAL_ROLE_AUA_PREFIX` from `lib.s3_layout`.
2. Add `_load_canonical_role_aua_latest()` — single-partition loader returning
   `DataFrame[date, advisor, role, aua]` for the latest available date. Falls
   back to empty (legacy path preserved) when no canonical partition exists.
3. Add `role_aua` to `load_for_leaderboard()` ThreadPoolExecutor (max_workers
   bumped 7→8) and pass through `data['role_aua']` to `build_employee_leaderboard`.
4. Add `role_aua` kw arg to `build_employee_leaderboard` signature with docstring
   note explaining scope (top-level AUA only — counts and fee_paying/no_fee
   bucket AUAs untouched).
5. After `at_role_breakdown` and the `if billable_account_ids is not None:` block
   complete, when `role_aua` is non-empty, **override**:
   - `tagged_aua_counts[advisor] = sum(role_aua.aua group by advisor at latest date)`
   - `at_role_breakdown[adv][role]['aua'] = role_aua.aua at (adv, role, latest date)`
6. Print line emits override count for log auditability:
   `role_aua override: tagged_aua_counts=N advisors, at_role_breakdown overrides=K (advisor,role) pairs from canonical date YYYY-MM-DD`.

The override is structural — no new aggregation, no new filter logic. Falls back
silently to the legacy `account_team`-derived values when no role_aua canonical
artifact is present (defensive — `_load_canonical_role_aua_latest` returns an
empty DataFrame when prefix is empty, and `if role_aua is not None and not role_aua.empty`
guards the override block).

**What I did NOT change:** `at_role_breakdown_fee_paying`, `at_role_breakdown_no_fee`,
`at_role_combination_breakdown`, account_count, client_count, NNA, inflows, outflows.
Those remain on the legacy account_team / canonical_nna paths. RA-P3 scope is
top-level AUA only per TO objective text.

**Note on RA-P1 producer state:** inspected the canonical artifact at
`s3://opal-data-bd/gold/canonical/role_aua/2026-04-13.parquet` (330 rows, single
date partition). `aua` column populated for all 164 advisors × up to 5 roles.
`aua_fee_paying = 0.0` for ALL rows in this snapshot (RA-P1 producer hasn't yet
wired the billable split), but I DON'T consume those columns here — `aua` (the
total) is what I read. Any RA-P1 producer fix lands transparently to D_00c
downstream of this commit.

## Cross-domain — CN-P3 hold (separate Rule 7 pre-flag)

CN-P3 was paired with RA-P3 in COO's GO. CN-P3 is HOLD pending CN-P1 backfill:
- `aws s3 ls s3://opal-data-bd/gold/canonical/nna/` = **2294 partitions** (back to ~2018).
- `aws s3 ls s3://opal-data-bd/gold/canonical/nna_atomic/` = **1 partition** (2026-04-13).

D_00c aggregates NNA over windows {3M, 6M, 1Y, 2Y, 3Y, MTD, QTD, YTD, MAX} via
`_compute_tagged_window_metrics(canonical_nna, ..., w_start, w_end)` filtering on
date. With only one partition in `nna_atomic`, every window collapses to a single
day — leaderboard NNA would shrink ~90× for 3M and worse for longer windows.

Pre-flag #2 fired to CTO + COO at 21:48Z
(`20260415T214804Z_..._CN-P3_BLOCKED__nna_atomic_only_1_partition`). Local edit
to D_00c CN-side reverted. Awaiting CTO redline; preferred path is HOLD CN-P3
until ~D's CN-P1 backfill completes.

RA-P3 is unaffected — role_aua canonical is consumed at LATEST date only (not
over windows), so a single partition is sufficient.

## Compiler Tools

| Phase | Run | Observed | vs `<expect>` |
|---|---|---|---|
| 1 | `comp-pipescript io D_00c` | Reads include CANONICAL_NNA_PREFIX (legacy `gold/canonical/nna/`); does NOT yet include role_aua canonical (it's the cutover work itself). Writes EMPLOYEE_LEADERBOARD → D_04. | INTERPRETED PASS — TO if_mismatch wording ("If role_aua not in reads, RA-P1 shadow write hasn't landed — STOP") was about producer existence (RA-P1 wrote `gold/canonical/role_aua/2026-04-13.parquet` per ls; producer landed). The "reads include role_aua" expectation logically refers to *post-cutover* state — that's what this TO produces. |
| 1 | `grep -n '_build_at_role_slice\|tagged_aua_counts' D_00c.portal_leaderboard.py` | `_build_at_role_slice` at L811 (def + invocations L873/876/877); `tagged_aua_counts` at L272/482/666/702/944. | PASS — sites identified; no rename since P0 memo. |
| 1 | inspect `gold/canonical/role_aua/2026-04-13.parquet` | 330 rows (164 advisors × up to 5 roles); cols include `aua`, `aua_fee_paying`, `aua_no_fee`, `aua_tagged_total`. Travis Penfield: arch $78.80M, impl $6.37M, cons $0.51M, addl $0.18M. Sum = $85.86M. `aua_fee_paying = 0` for all rows (RA-P1 partial). | PASS — `aua` column populated; sufficient for cutover. |
| 1 | `aws s3 ls gold/canonical/nna_atomic/` (CN-P3 gate check) | 1 partition only (2026-04-13). | **FAIL — triggered Rule 7 pre-flag #2; CN-P3 held; RA-P3 proceeds independently.** |
| 2 | `python -m py_compile D_00c.portal_leaderboard.py` | Exit 0. | PASS. |
| 2 | `python -c "import ast; ..."` AST parse | `build_employee_leaderboard` has 50 statements, 9 args including `role_aua`. | PASS — structural sanity. |
| 2 | parity vs canonical SOURCE (substituted #2) | By construction: `at_role_breakdown[Travis]['architect']['aua'] = round(role_aua.aua[Travis,architect,2026-04-13], 2) = $78,804,510`. `tagged_aua_counts[Travis] = $85,862,970`. | PASS — by construction. Cannot diff post-rerun artifact this session (gold rerun would be needed; ship + signal AE pattern preferred). |
| 3 | `comp-blast D_00c` | (deferred to post-commit per phase mandate) | — |

## Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py` | RA-P3 cutover: load + override `tagged_aua_counts` and `at_role_breakdown[adv][role].aua` from canonical role_aua latest partition. +75/-4 lines. |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_ROLLUP.RA-P3.ds-role-aua-d00c-leaderboard-cutover.md` | Status `staged → pending` with substituted-acceptance note + CTO approval cite. |

## What I did NOT do (scope honesty)

- Did NOT push to CLOUD or upload to S3 (deferred to a single push-and-deploy sequence after `comp-blast` post-commit Phase 3 verification + a coordinated decision with COO on whether to trigger a single-D_00c gold run for artifact-level acceptance).
- Did NOT cut over `at_role_breakdown_fee_paying` or `at_role_breakdown_no_fee` AUA (would require correctly-populated `aua_fee_paying`/`aua_no_fee` in canonical role_aua; producer currently emits 0).
- Did NOT touch CN-P3 — local edit reverted; pre-flag fired with HOLD recommendation.
- Did NOT proceed under unverified acceptance — Rule 7 pre-flag fired before cutting code, CTO approval received before commit.

## MCP traffic

| Time (Z) | Direction | Party | Subject |
|---|---|---|---|
| 21:37 | OUT | 2.0.0_SA_COO | ACK GO BLAST — initial scope split (incorrect) |
| 21:40 | IN  | 2.0.0_SA_COO | CORRECTION — RA-P3+CN-P3 ARE ~B-dialed |
| 21:40 | OUT | 2.0.0_SA_COO | ACK CORRECTION — flipping pending |
| 21:42 | OUT | 1.0.0_SA_CTO | RULE 7 PRE-FLAG #1 — RA-P2/CN-P2 not landed; substitute parity vs source |
| 21:43 | IN  | 1.0.0_SA_CTO | APPROVED — substitute parity vs canonical SOURCE |
| 21:43 | IN  | 2.0.0_SA_COO | ACK go on P3 pair |
| 21:48 | OUT | 1.0.0_SA_CTO | RULE 7 PRE-FLAG #2 — CN-P3 BLOCKED on nna_atomic backfill |
| 21:48 | OUT | 2.0.0_SA_COO | FYI pre-flag #2 — CN-P3 hold; RA-P3 proceeds |

## Next

- `comp-blast D_00c` post-commit (Phase 3 mandate).
- Coordinate with COO on push + S3 upload + bd-gold-trigger single mode for D_00c
  (or attach to the next nightly chain).
- MCP COMPLETE to COO with commit hash + cross-consumer table (deferred to
  post-rerun; structural acceptance now satisfied per CTO substitution).
- CN-P3: standing by for CTO redline. If HOLD confirmed, will close CN-P3 with
  blocker note and re-fire when nna_atomic backfill lands.
- B1–B8 SECONDARY validator sweep: deferred until P3 push lands (avoid context
  ping-pong; B-TO validation is the next coherent slice).
