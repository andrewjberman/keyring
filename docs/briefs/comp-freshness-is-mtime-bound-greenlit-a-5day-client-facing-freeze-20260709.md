# comp-freshness is bound to mtime, and it reported GREEN through a 5-day client-facing freeze

**Date:** 2026-07-09 | **Author:** 0.6.0_AE_PartnerETL | **Routed to:** 1.0.0_SA_CTO, 3.0.0_SA_CVO
**Status:** ELEVATED into the freshness-integrity program as the reference case (CTO 20260709T090845Z)
**Class:** existence-proxy / master-principle -- *bind to the CONTENT property, never the existence proxy*

## The finding, in one line

`comp-freshness chain bd` returned **PASS** on `bd_silver_allocations` at a moment when all seven of
its most recent partitions (2026-07-03 .. 2026-07-09) were **0-row stubs**, and the 49F portal had
been serving a frozen AUA for five straight days because of exactly those stubs.

## The evidence

Run at 2026-07-09T09:0xZ, mid-incident, before any repair:

```
bd_silver_allocations | s3://opal-data-bd/silver/allocations/ | 2026-07-09T00:18:27+00:00 | 8.7h | 48h | PASS
```

Ground truth at that same moment (row counts, read from the parquet):

```
silver/allocations/2026-07-02:  6,833 rows
silver/allocations/2026-07-03:      0 rows   <- 46,277-byte degenerate partition
silver/allocations/2026-07-04:      0 rows
silver/allocations/2026-07-05:      0 rows
silver/allocations/2026-07-06:      0 rows
silver/allocations/2026-07-07:      0 rows
silver/allocations/2026-07-08:      0 rows
silver/allocations/2026-07-09:      0 rows
```

The prefix's newest object was 8.7 hours old, so the `age_h < fail_at_h` predicate was satisfied and
the tool reported PASS. The freshness check is bound to the **last-modified timestamp of the newest
object in the prefix**. A pipeline writing a 0-row stub on schedule is, to `comp-freshness`,
indistinguishable from a pipeline that is perfectly healthy. In fact it is *worse than silence*: a
pipeline that stopped writing entirely would have tripped the age threshold and alarmed.

## Why this is the highest-leverage instance in the estate

The 49F incident had four independent existence-proxy masks inside the producer
(`download_export`'s `<100` byte check, a holdings-only content floor, `emit_bronze_sentinel`'s
`head_object`, and `_already_landed`'s `head_object`). Those are now fixed (commit `9d44d6af5`).

But `comp-freshness` is different in kind: **it is the tool we reach for to ask "is this stale?"**
It is the instrument, not the mechanism. An instrument bound to a proxy does not merely fail to
detect the problem -- it *manufactures confidence that there is no problem*. Every agent that ran
`comp-freshness chain bd` during those five days was told the allocations feed was healthy, and had
no reason to look further. A freshness tool that greenlights a 0-row stub is worse than no freshness
tool at all.

This is also the reason the freeze survived five days with a live, monitored, alarmed pipeline: the
per-table absence alarm (ADVI_BDAPIMIG P1-C `bd-49f-freshness-probe`, `SilverAgeHours`) is built on
the *same* mtime predicate. It, too, read GREEN. The whole detection layer was proxy-bound.

## The fix

Bind freshness to a CONTENT property, not to `LastModified`:

1. **Row count is the primitive.** A partition's freshness verdict must incorporate "does this
   partition have >= N rows", not only "when was it written". For parquet this is cheap -- the row
   count is in the file footer metadata; it does not require reading the data.
2. **A 0-row newest partition is STALE by definition**, no matter how recent its mtime. It should
   fail louder than an absent partition, because it is actively masking.
3. **Prefer the producer's own attestation where one exists.** `cot_bronze_ingest` now writes a
   completeness sidecar (`forwardfill_v2/{table}/_complete/{date}.json`, recording `has_data_rows`)
   after a successful land. Freshness checks should consult that attestation rather than re-deriving
   trust from object metadata.
4. **Apply the same treatment to `bd-49f-freshness-probe`'s `SilverAgeHours`** and to any other
   alarm whose predicate is an object timestamp.
5. Consider a `comp-freshness --content` mode first (announce-then-enforce, per the NFRA_COMPRAIL
   pattern), then make it the default once the noise profile is understood.

## Scope beyond bd

`comp-freshness chain <pipeline>` is used across bd / inf / cot. Every artifact it watches is
exposed to the same blind spot: any producer that can emit a well-formed empty (or truncated --
see the companion finding on the unrealized 500,000-row cap) artifact on schedule will read GREEN
indefinitely. The `bd_silver_*` rows are simply where we caught it.

## Grounding

- `comp-freshness chain bd` output, 2026-07-09T09:0xZ (PASS on `bd_silver_allocations`).
- Row counts read from `s3://opal-data-bd/silver/allocations/*.parquet` via pandas at the same time.
- Parent incident: the 49F portal served a cert frozen at `2026-07-02` (`certified_aua =
  $1,837,159,865.68`) because C_02's BRANCH-A floor skipped every degenerate cert from 07-03 on.
- Producer fixes + the master principle: commit `9d44d6af5`; deploy ledger
  `org/critical_paths/change_management/20260709T0855Z_bd-49f-empty-stub-asof-lag-root-fix_deploy_completion.md`.
- Companion finding: `docs/briefs/bd-unrealized-export-500k-row-cap-finding-20260709.md`.
