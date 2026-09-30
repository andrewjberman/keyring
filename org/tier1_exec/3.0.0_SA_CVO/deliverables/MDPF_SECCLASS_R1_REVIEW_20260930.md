# MDPF_SECCLASS -- round 1: L8 compile and L9 review (`3.0.0_SA_CVO`)

**Packet:** `2.0.0_SA_COO~M` 103107, `DRAIN_END_R1_20260930.md` @ee54196616. **Orders:** TO-SC-k1, k2, t1, t2, t3, t4,
all `complete` at HEAD, all `<risk>WORLD`, proofs VALID. **Carriers:** `ADJUDICATION_v1.md` (C-S1..C-S3) and
`REMEDIATION_v1.md` (S2, S1, W2-S3, W3-S3), co-committed. **Watermark:** 2026-09-30T02:45Z.

## L9

No order carries a JUDGMENT criterion (0 occurrences in 6 files). L9 is vacuous; the mechanical grades are the
issuer's re-runs on CLOUD, listed in the packet.

## What this seat read live (2026-09-30 02:4xZ)

| read | result | bears on |
|---|---|---|
| `get-item` PHYS | commodities / Metals / classified_by seed / instrument_kind fund | W3-S1, W1-S1 resolved; release step 1 landed |
| `get-item` GLD | commodities / Metals / seed / fund | a pre-existing seed row unchanged by the backfill |
| `scan` (one page, 2,309 rows) | classified_by: seed 137, scheduled 1,934, absent 238 | the backfill's 1,934 rows agree with the ledger; 238 rows violate C-WRITER's two-value rule |
| the same scan | instrument_kind: absent 2,163, fund 135, single_security 11 | FWD-8 is far from met (W2-S3) |
| `build_bd_assets_dim.py:164-165` | the private-map read is gone | W3-S2 resolved |
| t4 proof controls | planted bd-securities read caught (FIRED-AS-EXPECTED); determinism STABLE | the thread trace discriminates |

## Rows: 9, all compiled

| row | disposition | basis |
|---|---|---|
| S2 (ARMED) | graduated to 2.0.0_SA_COO~M, stays ARMED | cottonwood has no ticker-keyed source; IB-mr-251 waits on it |
| S1 | graduated, INERT | 238 rows with no classified_by (measured) |
| W2-S3 | graduated, INERT | instrument_kind absent on 2,163 rows (measured) |
| W3-S3 | graduated, INERT | fourth classify site; served positions.json coarse |
| W3-S1 (BLOCKING), W1-S1 | dismissed, resolved | PHYS is a seed row |
| W3-S2 (ARMED) | dismissed, fixed in t2 | no private-map read at HEAD |
| W2-S1, W2-S2 | dismissed | design notes with a home (S12/S13; the contract's definitions) |

## What you should have asked but did not

- **238 rows carry no `classified_by`.** C-WRITER says every row is `seed` or `scheduled`. The scan says 238 are
  neither. CTO 103050 ruled the constituents seeder "any other writer", which settles who may write, not what the
  rows already there should say. Until they are labelled, FWD-4's census cannot use `classified_by` as its
  discriminator, and the "seed always wins" rule has no value to read on them.
- **The backfill is bd-securities' classification under a new name.** All 1,934 scheduled rows came from the fork's
  values (Andrew's word admits this for new rows). GLD-class corrections the seed carries do not reach them; a ticker
  the fork had wrong is now wrong in the canonical table with `classified_by = scheduled`. FWD-3's one-edit exercise
  should pick one such ticker.
- **The thread halves predate the backfill.** The packet says so itself: t1-t3's censuses read 3,699 unclassified BD
  holdings, most of which the backfill has since classified. The re-census before fresh halves is the right order;
  this seat will not sign a thread half whose figures were read before 02:2xZ.

## Not verified by this seat

The 0-overwrite claim of the backfill beyond GLD and PHYS; the t1-t3 censuses; the BD page trace (read from the proof's
controls, not re-run).

-- 3.0.0_SA_CVO
