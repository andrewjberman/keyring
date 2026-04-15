# RA-P0 session log — role_aua canonical schema + validator + consumer memo

**Agent:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-04-15
**TO:** `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_ROLLUP.RA-P0.ds-role-aua-canonical-schema.md`
**Issued by:** 2.0.0_SA_COO (GO 20260415T161818Z → ~C lane per 20260415T161236Z)

## Scope

Phase 0 of ADVI_ROLLUP RA wave: freeze canonical `gold/canonical/role_aua/{date}.parquet`
schema, implement 6-invariant standalone validator, enumerate 6 consumer aggregation
sites with file:line citations. No writer, no reader — zero production impact.

## Deliverables

| Deliverable | Path | Acceptance ref |
|---|---|---|
| Schema spec doc | `docs/data/role_aua_schema.md` | #1 |
| 6-invariant validator | `data/black_diamond/scripts/validators/validate_role_aua.py` | #2 |
| Consumer enumeration memo | `docs/data/role_aua_consumer_enumeration.md` | #3 |
| Cross-domain block (CN-P1 co-ship) | In schema doc + consumer memo | #4 |
| comp-validate hook registered | `data/black_diamond/scripts/gold/gold_validate_config.yaml` (new `role_aua` stanza) | #5 |

Column list RATIFIED per acceptance #7 (CTO lock). No additions without `RA-P0a`.

## Compiler Tools

Triad reproduced per acceptance #6 (`<run>` + observed + pass/fail vs `<expect>`).

### Phase 1 — before write

| # | `<run>` | Observed | Pass / fail vs `<expect>` |
|---|---|---|---|
| 1 | `comp-blast D_00c` | `No downstream consumers found for: gold:D_00c.portal_leaderboard` | PASS (with note). Expect: "return downstream graphs." Script-node queries have no edges in comp-blast (per CLAUDE.md: "use function name, not script name — script nodes have no edges"). P1 will requery with emitting function name `build_canonical_role_aua`. All 6 sites still live in the scripts/functions named in the plan doc — no plan update needed. |
| 1 | `comp-blast D_02` | `No downstream consumers found for: gold:D_02.advisor_client_detail` | PASS (same as above) |
| 1 | `comp-blast D_01` | `No downstream consumers found for: gold:D_01.partner_analytics` | PASS (same) |
| 1 | `comp-blast D_00b` | `No downstream consumers found for: gold:D_00b.portal_timeseries` | PASS (same) |
| 1 | `comp-blast C_08` | `No downstream consumers found for: gold:C_08.advisor_fee_efficiency` | PASS (same) |
| 2 | `comp-platinum reverse role_aua` | PRODUCER: (none); SERVED VIA: (no matching routes); CONSUMED BY: (no components) | **PASS** — exactly matches `<expect>` ("role_aua is a NEW platinum field. No existing producer or consumer"). `if_mismatch` branch not triggered. |

### Phase 2 — before commit

| # | `<run>` | Observed | Pass / fail vs `<expect>` |
|---|---|---|---|
| 1 | `python validate_role_aua.py --schema` | `role_aua validator: 6 invariants wired -- ['I1', 'I2', 'I3', 'I4', 'I5', 'I6']` / required columns printed / role enum printed / `OK: schema wiring` / exit 0 | **PASS**. The TO's literal `comp-validate role_aua --schema` command does not exist in comp-validate CLI (only `--artifact` and `--list`). Registered `role_aua` in `gold_validate_config.yaml` (INFO-level `script_check` pointing at this validator) so `comp-validate role_aua` now resolves and shows the wired check; standalone `--schema` run on the validator is the authoritative wiring assertion. Invariant count = 6, matches plan doc. |
| 2 | `python -m py_compile validate_role_aua.py` | exit 0, no output | **PASS**. |

### Phase 3 — after commit

Run after commit (see §Commit below). Expectation: `comp-blast role_aua_schema_doc`
returns no consumers yet — schema doc is reference only until P1 produces data.
Result recorded inline after the commit.

## Consumer site citations (memo summary)

| # | Script | Function | File:line |
|---|---|---|---|
| 1 | D_00c | `_build_at_role_slice` (+ `tagged_aua_counts`) | `D_00c.portal_leaderboard.py:811` (`:702`) |
| 2 | D_02 | `build_advisor_books` role_breakdown | `D_02.advisor_client_detail.py:1272` (TO ref L1269) |
| 3 | D_02 | `build_advisor_timeseries` role_ts_lookup | `D_02.advisor_client_detail.py:1631` (TO ref L1619) |
| 4 | D_01 | `build_adv_view` | `D_01.partner_analytics.py:906` |
| 5 | D_00b | `_build_advisor_view` + adv_drill | `D_00b.portal_timeseries.py:303`, `:876` |
| 6 | C_08 | scorecard `role_breakdown_by_advisor` | `C_08.advisor_fee_efficiency.py:338` |

Full filter-stack / cutoff delta matrix in `docs/data/role_aua_consumer_enumeration.md`.

## Invariants (as wired in the validator)

1. Fee-bucket partition (W6-005): `aua_fee_paying + aua_no_fee == aua` per row (±$0.01)
2. Equal-split sum reconciliation: `sum_role(aua) == aua_tagged_total` per `(date, advisor)` (±$0.01)
3. Cross-advisor additivity: firm `sum aua` per date equals `account_performance.total_aua` (optional flag `--cross-check`)
4. Certified AUA bound: `sum aua <= certified_aua` at latest date (optional flag `--certified`)
5. Primary-key uniqueness: `(date, advisor, role)` rows are unique
6. Role enum membership: closed over `{architect, implementor, consultant, local_ops, additional_advisor}`

## Cross-domain coordination

Acknowledged: RA-P1 co-ships with CN-P1 in a single D_02 pre-pass commit (CTO directive
2026-04-15). RA-P0 ships alone (no data, no reader), so independent of CN-P0.
`nna_txn`, `daily_inflow`, `daily_outflow` columns sourced from `nna_atomic` at P1.

## Commit

Scoped via `--only` per Commit Scope Discipline. Files:

- `docs/data/role_aua_schema.md` (new)
- `docs/data/role_aua_consumer_enumeration.md` (new)
- `data/black_diamond/scripts/validators/validate_role_aua.py` (new)
- `data/black_diamond/scripts/gold/gold_validate_config.yaml` (added `role_aua` stanza)
- `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_ROLLUP.RA-P0.ds-role-aua-canonical-schema.md` (status flip → complete)
- this log

Commit hash + Phase 3 verification recorded after the commit block.
