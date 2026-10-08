# TO MDPF_DEMQUE.TO-DQ-t4 -- round 1 DQ-t-4: a locked, as-traded series lands in the input Cottonwood's price build already reads
<to_id>MDPF_DEMQUE.TO-DQ-t4</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~3</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `DQ-t-4` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 1) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-4`, hop 5 of the FWD-1 thread: once a Cottonwood security is locked and pulled, its as-traded daily closes reach the input that
Cottonwood's price build already reads, so the client's page can show them.

**The consumer (read it, do not edit it):** `data/cot/scripts/gold/build_canonical_prices_v2.py` -- `load_historical_prices()` (:281-288)
reads `s3://opal-data-cot/silver/historical_prices.parquet` (columns `ticker, date, close`) as its Tier 2 (`yahoo_finance`), and
`load_ticker_lookup()` (:290-298) reads `s3://opal-data-cot/config/ticker_lookup.json` (a JSON list of records with `asset_name` and
`ticker`; a record whose ticker is empty or `UNKNOWN` is ignored), keyed by Cottonwood's `asset_name`. Its asset spine comes from
`s3://opal-data-cot/silver/transactions/<date>.parquet`. Both Tier-2 objects are ABSENT live (measured 2026-10-08).

**Build** NEW `data/mdpf/scripts/demque/land_cot.py` with:

1. `plan(lock_rows, prices_by_symbol, cot_assets, existing_hist, existing_lookup) -> dict`:
   - `lock_rows`: list of dicts with keys `cusip, yahoo_symbol, valid_from, valid_to, method, observations_checked, observations_passed,
     median_abs_error, state, claim, locked_at, run_id, supersedes`; ONLY `state == "LOCKED"` rows land, and only dates inside
     `[valid_from, valid_to]`;
   - `prices_by_symbol`: `{symbol: DataFrame[date, close_served, as_traded_close]}`; the close written is `as_traded_close`;
   - `cot_assets`: DataFrame of Cottonwood's assets (from its transactions) used to find the `asset_name` for the lock's CUSIP or symbol --
     match by CUSIP when the frame carries one, else by symbol; a lock with no Cottonwood asset is listed in `unmatched`, never landed;
   - `existing_hist` / `existing_lookup`: what is live (empty when absent). NEVER rewrite or drop a row of a ticker already present; append
     new tickers only; an `asset_name` already mapped to a different ticker goes to `conflicts`, not overwritten;
   - returns `hist_rows_to_add` (DataFrame `ticker, date, close`), `lookup_to_add` (list of `{asset_name, ticker}`), `unmatched`,
     `conflicts`, and a printable `manifest` (keys it would write, row counts, tickers).
2. CLI: `python land_cot.py --locks L.jsonl --prices DIR` prints the manifest and WRITES NOTHING (dry-run is the default); `--apply`
   writes the two objects (read-modify-write, new tickers appended). **You never run `--apply`**: it is the issuer's act at the drain.
3. CLI `python land_cot.py --probe` (read-only): reads the latest object under `s3://opal-data-cot/silver/transactions/`, prints exactly
   `PROBE rows=<n> assets=<distinct asset_name> join_key=<cusip|symbol|asset_name-only> hist_exists=<yes|no> lookup_exists=<yes|no>`
   (`join_key` = the best identifier column the frame actually carries; `*_exists` from `HeadObject` on the two Tier-2 keys). rc 0. Print
   no account number, name or amount. boto3 default credentials; `ListObjectsV2` / `GetObject` / `HeadObject` only.
4. NEW `data/mdpf/scripts/demque/test_demque_land.py` (pytest, synthetic frames, S3 stubbed) with exactly these names:
   `test_only_locked_rows_inside_their_range_land`, `test_close_written_is_the_as_traded_close`,
   `test_existing_tickers_rows_are_never_rewritten`, `test_lookup_entry_maps_cot_asset_name_to_symbol`,
   `test_unmatched_security_is_listed_not_landed`, `test_default_run_writes_nothing` (no put without `--apply`).

The module imports nothing from another cell (the shapes above are fixed by the decomposition). Do NOT create `__init__.py` in
`data/mdpf/scripts/demque/` (the issuer adds it).

### ACCEPTANCE

<criterion id="DQ1-t4-AC1" cell_refs="DQ-t-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R1_CHECKS/dq_t4_tests.py</invocation><expect>LAND-OK</expect></criterion>
<criterion id="DQ1-t4-AC2" cell_refs="DQ-t-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R1_CHECKS/dq_t4_seam.py</invocation><expect>LSEAM-OK</expect></criterion>
`DQ1-t4-AC1` -- the landing rule, by the six named tests. `DQ1-t4-AC2` -- the seam against Cottonwood's live transactions: rows and
assets > 0 and the join key named.

<expected_criteria>DQ1-t4-AC1,DQ1-t4-AC2</expected_criteria>

Run each invocation from the worktree root. Both FAIL at the base: `LAND-BAD no file ...`, `LSEAM-BAD rc=127`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write (never `--apply`, never `PutObject`), no vendor call, no deploy.** Read-only S3 reads for the probe only.
- **Cottonwood (cot) is its own firm:** read only `opal-data-cot`; never read or write another firm's bucket.
- **You arm no timer, background task or OS task.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-W3-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file
  below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/land_cot.py
data/mdpf/scripts/demque/test_demque_land.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 1, the thread), cell `DQ-t-4`.
<owned_cells>DQ-t-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ1-t4-AC1, DQ1-t4-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~3/MDPF_DEMQUE.TO-DQ-t4.land-into-cottonwood-yahoo-tier.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ1-t4-AC1,DQ1-t4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE read-only S3 reads by the dell1 agent user; the drain's --apply (PutObject on two opal-data-cot keys) is read before it runs.
comp-adversary: DECLARED-NOT-APPLICABLE thread round.
risk: LOCAL -- code and tests; read-only probe. The --apply at the drain is SERVED and is the issuer's, under a never-widen half.
direct_act: false -- a worker order.
</preflight>

Source: PRD v0.2 FWD-1, C-PRICES, C-PRODUCERS; decomposition round 1 hop 5.
