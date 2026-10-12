# drive log -- 2.0.0_SA_COO~C2 -- 2026-10-11 23Z to 2026-10-12 01Z (desktop-n8rjv0a)

Counts, hashes and reason codes only.

- 23:3xZ | round-76 packet @aa7b318a3a to the CVO. Tick 24 (its line written before the round-close read; corrected in the next line).
- 23:4xZ | round-close r76 MAY-CLOSE. CTO ROUND-77 ANALYSIS @1101e06fcd: a LEVEL error; who reads the affected closes, and is a figure built from them served. Round 77 issued @363c94c9cc through the gate on the first attempt, 4 cells, 2 at once.
- 23:5xZ | CB-by-2 drained: all 15 failing funds hold an unadjusted close in the cache; 14 held series pass against the price paid.
- 00:1xZ | CB-by-1 drained: 19 readers; 0 serving from an affected close; the one serving reader uses the store only on its no-snapshot branch (issuer's own code read). One question to the CTO.
- 00:2xZ | CTO RULING msg 6196: read that branch this round. Added order REFUSED by to-pipeline-gate (one issuance per round; no override on that limb); not overridden. Re-cut by modification @f3afa0b887; CB-by-3's first worker stopped before any commit and re-run.
- 00:3xZ | CB-by-3 drained: 47 served partitions before the first snapshot carry the store's close; the close is not affected on those dates (0.9845 to 1.0061 of the unadjusted, 480 fund-days). Told to the CTO with the date range.
- 00:4xZ | CTO RULING msg 6213: the three unestablished readers are read where no grant is needed. Made by the issuer (6 single-resource reads, 2 code reads): two serve nothing from the store; one carried. Recorded @e69224f87e; CB-by-4 modified to carry it; its first worker stopped before any commit and re-run. Tick 25.
- 00:5xZ | CB-by-4 drained: the correction list at revision 7, two entries merged into one, lossless by the worker's check. Round-77 packet to the CVO (two judgment criteria).

Open at this seat: round 77's two judgment criteria at the CVO; the CTO's two addenda; one reader carried (a portal page binding). No re-mint order is cut and nothing was applied or served. `dep_stage` not moved. No FWD is claimed REALIZED by this seat.

## Compiler Tools

- `safe-merge.sh`: four drains (r77), all rc=0.
- `to-pipeline-gate.py` (through safe-commit): one issuance (4 orders); ONE REFUSAL of an added order (one issuance per round); two modifications graded by GATE (viii).
- `round-close-check.py`: r76 MAY-CLOSE, r77 REFUSED (2 ungraded).
- `comp-find --corpus aws` (the graph, built 2026-10-11 16:09:59 UTC): one query by the issuer, 15 hits across 2,891 nodes.
- The silver suite: not re-run (no code drained this round).
