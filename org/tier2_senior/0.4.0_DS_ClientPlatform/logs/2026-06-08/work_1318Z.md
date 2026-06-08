# 0.4.0_DS_ClientPlatform — work_1318Z (GLDINC P0.5 §5a confirm + one residual closed)

**archetype:** VALIDATE + SCRIBE

## Task (COO 131530Z RAVC2-ACCEPT + GLDINC-forward)

Confirm/finalize the P0.5 §5a restatement-trigger design-of-record (my silver-partition-
LastModified-vs-watermark unifying primitive). Parallel to AE's P0 validation, NO prod touch.
PRD says §5a "already substantially done in the two-axis addendum." Either confirm ratified-ready +
stand ready for P2, or close residual so P2 starts clean. RAVC2 one-liner either way.

## Method — re-derived against source, did NOT rubber-stamp "substantially done"

Read the full Andrew-approved PRD v0.2 (`ADHC_GLDINC_PRD.md`). §5a is present and sound at design
altitude: the unifying primitive (per-date restatement detection via partition-LastModified vs
watermark, current-version-only → R2-lifecycle-safe), 4 dirty-set cascade refinements, P1 anchor
verified. My co-ownership activates at **P2 = A_03 positions_cube (reconcile-on-injection)**, so I
checked §5a against A_03's ACTUAL inputs rather than accepting the design abstractly.

## FINDING — verified residual: monolithic-input detection gap, lands at P2

§5a's detector assumes **dated write-once partitions** (`silver/{x}/{date}.parquet`). A_03 reads
three restatement-relevant input classes:

| A_03 input | Shape | §5a detector applies? |
|---|---|---|
| `silver/transactions/` | dated partitions | YES |
| `silver/allocations/{date}.parquet` | dated partitions | YES |
| `silver/prices/canonical_prices.parquet` | **MONOLITHIC (all dates, one file)** | **NO** |

Confirmed canonical_prices is restatement-relevant (not just a valuation refresh): A_03 uses it for
unit derivation (`units = injectable_mv / canonical_price`, L656) + unrealized/cost-basis (L668). A
historical price restatement advances the monolithic file's LastModified but yields **no per-date
scope** — the partition detector can only say "prices changed somewhere," forcing a conservative
whole-history re-FIFO that defeats incrementalization. **This is a real design residual that hits the
very first reconcile phase (P2), not a build detail.** It pre-exists for P4 too (C_02/C_03 write
monolithic parquet — already flagged in §5 as an output-shape obstacle, now connected to detector
applicability).

## CLOSURE — proposed §5a refinement #5 (generalizes the primitive; closes P2)

**Per-date restatement detection — via partition-LastModified where the input is dated-partitioned;
via a per-date content-checksum manifest where it is monolithic.** On a monolithic-input LastModified
advance: read it, group by date, hash each date's rows, diff vs a stored per-date checksum manifest
(kept alongside the watermark) → recover the changed-date set → invalidate dependent FIFO positions /
cum-keys / frozen periods forward from `min(changed_dates)` — identical downstream to the dated-
partition path. Keeps the unified "did historical data change, and for WHICH dates" framing; restores
per-date scoping for non-partitioned inputs. Self-contained, no producer change, ships with P2.
**Future optimization** (not required for P2): have `build_canonical_prices_v2.py` emit a
`changed_dates.json` so scoping moves to the producer that knows — eliminates the re-hash, but the
content-checksum fallback needs nothing upstream.

## Verdict
§5a is substantially ratified-ready as the P0.5 doc-of-record; the unifying primitive + 4 refinements
hold. ONE verified residual (monolithic-input detector gap, materializes at P2 via canonical_prices)
is now **closed at the design level** (refinement #5 above). The PRD mechanical fold routes to CTO
(PRD owner; my §5 review was folded the same way at v0.2, commit 5b1b05804). P2 can start clean once
#5 is in the design-of-record. No prod touch; C1 honored. Standing ready for P2 kickoff.

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| Read/Grep (A_03 source) | A_03.positions_cube.py input-class + canonical_price usage | 3 input classes; canonical_prices monolithic + restatement-relevant (units+unrealized) |
| (design review) | §5a vs A_03 actuals | verified residual found + closed (refinement #5) |

work-cycle:0002
