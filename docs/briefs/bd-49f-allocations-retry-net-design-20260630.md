# 49F BD allocations RETRY-NET — design brief (generalize the holdings DATEMODE-B pattern to allocations)

**Author:** 0.6.0_AE_PartnerETL | **Date:** 2026-06-30 | **Project:** ADVI_BDAPIMIG.P1 (component B durable) | **Status:** PROPOSAL — needs CTO (pattern arch) + cot-lane (shared-code co-owner) sign-off before implement; DEPLOY post-23:00Z-serve.

## Root cause (grounded)

Tonight's 49F P0 (silver/allocations empty 06-26+ -> C_02 would certify $0): the BD DataMining
allocations REST export, asked for a date D before D's data is ready (T-1 timing), returns a
**header-only ~4,592-byte XLSX** (the "freshest available date" is < D). `cot_bronze_ingest.py`
landed that stub over the good partition. Two gaps in the shared ingest:

1. `download_export` (line 344) only rejects `len(payload) < 100` bytes. A 4,592B header-only stub
   passes that floor and is treated as a valid export.
2. `ingest_table` (line 439) applies the completeness floor + reject + sidecar **only when
   `table == "holdings"`**. For `table == "allocations"` it lands whatever comes back,
   unconditionally — no completeness check, no sidecar, no retry-net sweep. **Allocations is
   entirely unprotected.**

Net: a T-1/header-only allocations export overwrites a good valued partition with a stub, silently
-> silver stub -> C_02 certifies $0 (the BRANCH-A floor caught the $0 downstream, but the stub
should never have landed).

## The existing pattern (CTO-blessed, ADVI_COTETL DATEMODE-B, 364eb1b24 / 150804Z) — HOLDINGS only

- **Completeness floor** `_holdings_nonzero_mv_fraction(xlsx) >= HOLDINGS_COMPLETENESS_FLOOR(0.5)`;
  in `ingest_table`, sub-floor -> REJECT (return None, **don't land**, prior valued snapshot stays).
- **Completeness sidecar** `forwardfill_v2/holdings/_complete/{date}.json`, written ONLY after a
  successful priced land (CTO ordering invariant: sidecar-exists ⟹ land-succeeded).
- **Valued-re-pull sweep** `backfill_holdings_net`: each run re-pulls the last
  `RETRY_NET_LOOKBACK_BDAYS(5)` business days not complete-per-sidecar (floor-gated -> self-heals
  the moment BD prices), + an **e2 defect alarm** for a day older than `CADENCE_BDAYS(2)` still
  incomplete (real BD source defect -> SNS).

## Proposed fix — generalize the SAME pattern to allocations (and, for free, all 4 tables)

The allocations failure mode is a **header-only / ~zero-data-row** stub. The robust, firm-agnostic
completeness signal is **data ROW COUNT below a conservative absolute floor** (a healthy 49F
allocations export ≈ 6,800 account rows; a stub ≈ 0; both firms' real allocations are
hundreds-to-thousands of rows, so a low absolute floor never rejects a real export).

**Preferred shape — parameterize the existing functions by table (one source of truth, covers all
4 tables):**

- `_table_completeness(table, xlsx_bytes) -> float` dispatcher:
  - `holdings` -> existing `_holdings_nonzero_mv_fraction` (unchanged).
  - `allocations` (and `transactions`/`realized`) -> a **non-empty-data-row fraction / count** signal
    (rows-with-a-populated-key-field). Returns a normalized metric comparable to a floor.
- `_completeness_floor(table)` -> per-table floor (holdings 0.5 nonzero-MV; allocations a row-count
  floor, env-overridable `BD_ALLOC_ROW_FLOOR`, default 50). Defaults firm-agnostic.
- `ingest_table`: replace `if table == "holdings"` with `if table in COMPLETENESS_GUARDED_TABLES`
  -> compute metric, sub-floor -> REJECT (return None, don't land — **the key protection: never
  overwrite a valued partition with a stub**), else land + write the sidecar.
- **Sidecar prefix generalized** `forwardfill_v2/{table}/_complete/{date}.json` (holdings path byte-
  identical; allocations/others get their own).
- **Sweep generalized** `backfill_table_net(table, ...)` (refactor of `backfill_holdings_net`); the
  bd-49f-runner calls it per guarded table after the daily pull. e2 alarm per table.

**Lower-risk fallback (if CTO prefers minimal churn to the holdings path):** ADD parallel
`_allocations_*` functions + a `backfill_allocations_net` mirroring holdings, leaving the
CTO-blessed holdings code untouched (some duplication, zero holdings-path risk). CTO's call.

## Grounding the concurrency question (CTO 201027Z — "ground before mirroring blind")

CTO asked whether the inf perf-parallelize **bounded-concurrency governor** should fold into the
49F runner. **Grounded: NO.** The 49F BD pull is **4 sequential single-report DataMining exports**
(transactions/allocations/realized/unrealized), not a per-entity fan-out (the inf freeze ROOT was
313 clients × 8 windows ≈ 2,504 serial calls). 49F has **no serial-vs-rate-limit gap** — there is
nothing to parallelize. The durable 49F fix is THIS completeness retry-net + the existing
session-hardening (keepalive / deferred auto-login), **not** a concurrency governor. (Folding the
governor blind would add risk with zero benefit.)

## Firm-separation (CLAUDE.md NEVER#1)

Shared cot/bd code (Model-B). The change is **firm-agnostic** — a row-count floor of ~50 never
rejects a real export for EITHER firm, and protects BOTH firms' allocations equally. No data-plane
crossing; floors env-overridable per-firm if a firm ever needs a different bound. The
`_assert_firm_separation()` guard and the explicit env-var contract are untouched.

## Blast radius + deploy (comp-blast / comp-grep grounded)

- Consumers of the shared script: `test_retry_net.py` (EXTEND — add allocations stub-reject +
  sweep cases), `cot_backfill_date_probe.py`, `dump_enriched_templates.py`, `probe_holdings_nzf.py`
  (reuse functions — keep signatures stable / additive).
- Deploy targets (Model-B): `s3://opal-data-cot/code/bronze/` (cot-exporter EC2) **and**
  `s3://opal-data-bd/code/bronze/` (bd-49f-runner Lambda). Both, same commit.
- **Sequencing:** implement + extend tests + deploy to both code paths **AFTER tonight's 23:00Z
  serve + the co-verify is clean** — do not destabilize the pull pipeline in the pre-serve window.
  This is the BDAPIMIG.P1 durable phase, not tonight's gate.

## Acceptance

1. A header-only/T-1 allocations export is REJECTED at-pull (return None, NOT landed); the prior
   valued partition stays. Proven by a unit test feeding a header-only xlsx.
2. A rejected stub-day is re-pulled on a subsequent run and lands the moment BD has the data
   (sweep self-heal), proven by the sweep test.
3. An allocations day older than cadence still missing fires the e2 defect alarm (egress-verified).
4. The holdings DATEMODE-B path is byte-for-byte behavior-preserved (regression test green).
5. Deployed to both code paths; comp-freshness chain bd PASS on the next scheduled run.
