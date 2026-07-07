# VERIFY #24 -- target: s3_layout.py

- is_real: **True**
- confidence: **confirmed**
- corrected_severity: high

## Reasoning
CONFIRMED real defect (silent cross-dating of the authoritative reconciliation reference). Traced a concrete, documented triggering path.

MECHANISM (source-grounded):
- E_21:113 `nna_key = _latest_partition(CANONICAL_NNA_PREFIX)` returns the lexicographically-last `.parquet` under `gold/canonical/nna/`. Because filenames are `{YYYY-MM-DD}.parquet` (s3_layout.py:109-112 `canonical_nna_key`), lexicographic == chronological, so it always returns the NEWEST date partition regardless of `target_date`.
- E_21:114-117 assigns `nna_day = nna_all` wholesale, comment "latest partition IS one date." There is NO `nna_all[nna_all['date']==target_date]` filter and NO `canonical_nna_key(target_date)` load anywhere.
- `target_date` is derived independently: `--date` arg (line 87) or `cp['date'].max()` (line 89) from client_performance. These two dates are only guaranteed equal in a coherent default nightly.
- E_21:137-140 sums `nna_day['nna_txn'|'daily_inflow'|'daily_outflow']` into `firm.*_canonical`; E_21:168-174 does the per-advisor equivalent. Both branches fire because C_01 always writes those columns (C_01 docstring 23-27; `_worker_04b` writes nna_txn/daily_inflow/daily_outflow, line 395 + 413). The reference JSON stamps every one of these as `target_date` (line 184).

CONCRETE TRIGGER (documented usage): `python3 E_21... --date 2026-04-01 --upload` while the newest `gold/canonical/nna/` partition is 2026-04-07. Result: `reference.target_date='2026-04-01'` but `firm.nna_txn_canonical/daily_inflow_canonical/daily_outflow_canonical` (and top-advisor nna_txn/daily_inflow/daily_outflow) report 2026-04-07's flows. The `--date <historical>` form is explicitly documented (line 14) and IS the historical-reconciliation use-case this tool exists for. Also fires in any nightly where C_01 (NNA) lags while C_02 (client_performance) advances (target_date follows cp.max()).

ADVERSARIAL REFUTATION ATTEMPTS, ALL FAILED: (a) columns absent -> refuted, C_01 writes nna_txn/daily_inflow/daily_outflow; (b) guard elsewhere -> none, nna_day used raw at 138-140 and 170; (c) always date-aligned -> only in the coherent default (no-`--date`) nightly; the documented historical `--date` form defeats alignment by construction; (d) cot doesn't produce NNA -> refuted, C_01 has explicit COT snapshot-first NNA wiring, so firm-level canonical fields populate for cot (advisor-level may be sparse due to cot's Unassigned architect, but firm-level 137-140 fires regardless).

FAILURE MODE: silent wrong-output (not a crash). The value written is a real NNA number for the WRONG date, mislabeled target_date. DE/RD comparing the portal's target_date NNA against this 'authoritative' reference (lines 9-10) either see a false discrepancy or have a genuine portal error masked by the coincidentally-close latest-partition number.

SEVERITY high (not critical): it corrupts a validation/diagnostic reference, not served customer data, and the DEFAULT coherent nightly (no `--date`, C_01==C_02 max date) does not fire. But it silently poisons the ground-truth used to catch other portal bugs and defeats the tool's core date-specific purpose precisely on the `--date` historical form it documents, so high is warranted; medium would be the floor.
