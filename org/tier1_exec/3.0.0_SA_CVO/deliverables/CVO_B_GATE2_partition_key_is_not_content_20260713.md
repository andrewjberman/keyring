# GATE-2 (CVO~B) — the partition KEY does not determine the partition CONTENT (6/69, measured)

**Author:** `3.0.0_SA_CVO~B` · 2026-07-13 · CONFIRMED-BY-MEASUREMENT (live S3)

## Why this matters

Base CVO's `(as_of, fold_mode)` remedy for the F1 chokepoint rests on a purity premise:

> `resolution == f(accounts_v2 partition, AOR_FOLD_ACTIVE)` — and nothing else.
> Two runs sharing both inputs produce a BYTE-IDENTICAL resolution, so reusing it is a correct cache.

The theorem is right. The **variable is wrong**: it keys on the partition's **NAME**, and the premise
silently requires that the name determines the **CONTENT**. It does not.

## Measurement (denominator on the retrieval)

`s3://opal-data-inf/silver/api_dims/accounts_v2/` — **69 partition objects examined**:

| partition | LastModified | |
|---|---|---|
| `snapshot_date=2026-04-28` | 2026-05-11 | REWRITTEN |
| `snapshot_date=2026-04-29` | 2026-05-11 | REWRITTEN |
| `snapshot_date=2026-05-07` | 2026-05-11 | REWRITTEN |
| `snapshot_date=2026-05-08` | 2026-05-11 | REWRITTEN |
| `snapshot_date=2026-05-09` | 2026-05-11 | REWRITTEN |
| `snapshot_date=2026-05-10` | 2026-05-11 | REWRITTEN |

**6 of 69 partitions were rewritten AFTER their own snapshot_date** (one backfill event, 2026-05-11).
Each partition is a **single fixed key** — `snapshot_date=<d>/data.parquet` — so a re-emit **overwrites
content in place**. The key repeats across different bytes.

## Consequence

A resolution built from partition `05-10` **before** the backfill carries `as_of=05-10`, `fold_mode=ACTIVE`.
A run **after** the backfill pins `as_of=05-10` (same partition) and `fold_mode=ACTIVE`. **Both fields match**
→ the guard **passes** → consumers attribute the **new** source content with a resolution derived from the
**old** content. Silently.

Same class, one level deeper: **a value that repeats across the thing it is meant to discriminate.**

## The key that dominates

Stamp `(source_content_digest, fold_mode)` — the **S3 ETag** of the accounts_v2 partition object the resolver
actually read, plus the mode. The ETag is free (it returns in the GET/HEAD the loader already performs).

| state | ETag+mode | |
|---|---|---|
| legit cache reuse (same content+mode, resolver skipped) | matches → RETURNS | no over-condemnation (base CVO's requirement) |
| A3 — folded artifact, run switch-OFF | mode differs → RAISES | my defect closes |
| **rewritten partition (same key, new bytes)** | **ETag differs → RAISES** | **neither other key catches this** |
| cross-day advanced source | ETag differs → RAISES | R1's arm preserved |
| weekend genuine non-advance, resolver RAN | matches → RETURNS | CTO's weekend-safety preserved |

`run-id` is a proxy for provenance and **over**-fires. The partition key is a proxy for content and
**under**-fires. **The digest IS the thing.**

## Honest limits

- The 6/69 rewrite is **real and measured**, but I have **not** demonstrated it co-occurring with a
  resolverless run. **LATENT hazard, not a demonstrated incident.**
- Production harm still **NOT demonstrated** (the nightly fires `mode: full`).
- I have **not** yet exercised an ETag-keyed guard. That mutant gets built once CTO rules the key.

## Doctrine (earned three times tonight)

**When a guard keys on a value, ask whether that value can REPEAT across the thing it is supposed to
discriminate.**
- `as_of` repeats across **runs** → the original F1 fail-open.
- `as_of` repeats across **modes** → A3.
- the partition key repeats across **content** → `(as_of, fold_mode)`.

Three instruments, one unexamined assumption each time: **that a NAME identifies a THING.**
Companion (base CVO): *an instrument's arms must be reachable from different TRUTHS, not merely produce
different outputs* — both-directions is not enough.
