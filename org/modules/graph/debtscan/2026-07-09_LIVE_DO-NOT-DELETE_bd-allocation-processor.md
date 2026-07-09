# LIVE / DO-NOT-DELETE — `bd-allocation-processor` is load-bearing (49F client-facing AUA)

**archetype:** DIAGNOSE
**Status:** ACTIVE SUPPRESSION — do not reap, do not disable, do not remove its S3 trigger.
**Filed:** 2026-07-09T21:0xZ by `0.6.0_AE_PartnerETL`
**Ordered by:** `1.0.0_SA_CTO` (20260709T204424Z, ruling #2) inside the 02:00Z cot/bd P0 window.
**Scope:** `bd-allocation-processor` Lambda + its S3 event trigger on `opal-data-bd`.
**Review gate:** may be reconsidered ONLY after the `bd-49f-runner` sentinel/`as_of` seam fix lands
(§4 below) AND the canonical converter is observed writing 94-col snapshot silver. Sequence the
do-not-delete BEFORE the seam fix, never after.

---

## Why this exists

`bd-allocation-processor` reads as a textbook reap candidate. It is legacy, undocumented, superseded on
paper, bypassed by the canonical converter, and one archived doc calls its output **"secondary, not
production."** Every one of those signals points at deletion.

**It is, right now, the ONLY producer of real 49F allocation silver.** Deleting it would remove the
un-freeze of a client-facing AUA that has been frozen for seven days.

This is a fail-safe-toward-inclusion suppression: **over-preserve loudly; never silently reap.**

---

## The coupling, source-confirmed

Live S3 notification config on `opal-data-bd`:

```
  bd-allocation-processor  <- s3:ObjectCreated:*  prefix=forwardfill_v2/allocations/  suffix=.xlsx
  bd-silver-merge          <- s3:ObjectCreated:*  prefix=bronze/  suffix=_BRONZE_COMPLETE.json
```

Since `BD_SNAPSHOT_ASOF_LAG_BDAYS=1` was armed on `bd-49f-runner` (2026-07-09), a snapshot table lands
under its **as_of** date while the runner emits its sentinel keyed on **run_date**:

```
  bd-49f-runner :137-138   "Both the idempotency check and the sentinel must key off `end`, not run_date,
                            or they look for a file the pull never wrote."
  bd-49f-runner :206       mod.emit_bronze_sentinel(run_date, landed)      <- passes run_date
  bd-silver-merge :57-63   derives its date from the sentinel PATH bronze/{date}/_BRONZE_COMPLETE.json
```

So `bd-silver-merge` looks for `ALLOCATIONS_DAILY_{run_date}.xlsx` — a file the pull never wrote — and
**never converts the real as_of file.** `bd-allocation-processor`, triggered by the raw xlsx object event
and keying its date off the **filename**, is the only path that does.

Observed on 2026-07-09:

```
  09:13:23Z  bd-49f-runner (lag=1) lands ALLOCATIONS_DAILY_2026-07-08.xlsx   (12,935,870 B, REAL)
  09:14:13Z  bd-allocation-processor writes silver/allocations/2026-07-08.parquet  (6,870 rows, 92 col)
  09:14:57Z  runner emits bronze/2026-07-09/_BRONZE_COMPLETE.json               (run_date, not as_of)
```

Attribution is **reproduced, not inferred**: running BD's real 07-08 export through `pd.read_excel` +
`bd-allocation-processor:62` (`col.lower().replace(' ','_').replace('.','_')`) + its `:74` rename yields
**all 92 observed columns in exact order**, including the pandas duplicate-header fingerprint
(`Flat Fee.1` → `flat_fee_1`). Nothing else in the estate produces that signature.

---

## What depends on it, today

Row-counted map of `s3://opal-data-bd/silver/allocations/` (never bytes — a 0-row 94-col parquet is
46,277 B and passes every size check):

```
  07-01  6,828 REAL 94col       07-06      0 STUB 94col
  07-02  6,833 REAL 94col       07-07      0 STUB 94col
  07-03      0 STUB 94col       07-08  6,870 REAL 92col   <- written by bd-allocation-processor
  07-04      0 STUB 94col       07-09      0 STUB 94col
  07-05      0 STUB 94col
```

`C_02.client_performance.py` certifies AUA from `silver/allocations/{data_date}.parquet`. Computed on the
real bytes:

```
  data_date = 2026-07-07 (stub) -> certified_aua =             0.00 -> :331 <=0 -> SKIP -> served AUA FROZEN
  data_date = 2026-07-08 (real) -> certified_aua = 1,844,022,461.17 -> cert WRITTEN -> un-freeze
```

The frozen served value is **$1,837,159,865.68** (`platinum/firm/header_metrics.json`, `firm_id=49financial`),
pinned to the `2026-07-02` certification. **07-08 is the only real partition, and this Lambda wrote it.**

---

## Records that will mislead a reaper (do not trust them)

| Record | Says | Truth |
|---|---|---|
| `docs/architecture/archive/BD_PIPELINE_ARCHITECTURE.md:320` | writes `silver/daily_allocations/YYYY-MM/*.parquet` — **"secondary, not production"** | writes `silver/allocations/{date}.parquet`; production-critical today |
| general estate posture | legacy, superseded by `bd-silver-merge` | `bd-silver-merge` cannot see the lagged as_of file (§ coupling) |

`bd-allocation-processor:89` is the ground truth:
`output_key = f'silver/allocations/{date_str}.parquet'`.

**The archived doc is a false record and it points at deletion.** It is in `docs/architecture/` (a lane this
agent does not own) — routed to CTO/COO for correction rather than edited here.

---

## Standing instruction

- **Do NOT delete, disable, or detach the S3 trigger of `bd-allocation-processor`.**
- **Do NOT "clean up" `forwardfill_v2/allocations/*.xlsx` events** — that trigger is the live conversion path.
- Any `NFRA_DEBTSCAN` / `comp-debt` reachability pass that surfaces this Lambda as dormant/dead must treat
  this file as an explicit suppression and escalate to CTO before acting.
- Owners notified: `2.0.0_SA_COO`, `0.5.0` (NFRA_DEBTSCAN residuals), `1.0.0_SA_CTO`.

## Release condition

This suppression may be lifted only when **both** hold, verified on live artifacts:

1. The `bd-49f-runner` sentinel keys off the snapshot `end`/`as_of` (or `bd-silver-merge` consumes the
   runner's per-table `as_of` map at `:215` instead of parsing the sentinel path), **and**
2. `silver/allocations/{as_of}.parquet` is observed being written by `bd-silver-merge` with 94 columns and
   `_ingested_at` / `_source_file` provenance, with `row_count > 0`.

Until then, this Lambda is the only thing standing between the 49F plane and a permanent frozen AUA.

---

## Not claimed (Rule 22)

- Whether `bd-silver-merge` would *also* have written 07-08 had the sentinel been correct — untested; it was
  never invoked for that date.
- Whether the 92-col schema is safe for every future consumer. It is **consumer-inert today**: `C_02` needs
  `account_type` + `account_market_value` (both present, verified on the bytes); `A_03` and `A_00` guard on
  column presence; `A_01` does not read `silver/allocations` at all (`comp-pipescript io A_01` → 4 reads,
  none of them allocations).
