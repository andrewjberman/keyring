# drive log -- 2.0.0_SA_COO~C2 -- 2026-10-11 12Z-13Z (desktop-n8rjv0a)

Counts, hashes and reason codes only.

- 12:0xZ | CB-bo-2 drained @e7890e1cff: 109 split-store partitions added 2026-10-10; 4 move 3,034 price points; all four are spin-offs on evidence independent of the store, every moved point before its date; all 30 drift account-days rest on them.
- 12:1xZ | CB-bn-1 drained @3a75bb973a: the withholding rule moves 2 of 1,691,729 account-days on 2 dates, on today's store state with the two runs' inputs proven equal. Round-66 packet @eb8de12cd9. The CVO graded CB66bn1-AC2 NOT MET on one limb: the comparison was not at the pin.
- 12:4xZ | tick 12. CB-bo-1 drained @e6645ff9cd: the build reads the split store at a named instant by object version and refuses an unpinned read (issuer run: REFUSED before any write); suite 866 passed, 12 skipped; the worker's Proof A at as_of 2026-10-09T11:52:52Z reproduces the served table, 0 of 1,691,729 differing, 32 held.
- 13:0xZ | issuer's hour-apart re-run of the valuation at as_of 2026-10-11T11:55:40Z: start 13:01:16Z, 60.6 minutes after the worker's first; the pin line identical; the price table's sha256 equal to both worker runs (issuer sha256sum of all three). Round-67 packet @2326dc3955. The CVO graded CB67bo2-AC2; round-close r67 MAY-CLOSE.
- 13:2xZ | CTO ROUND-68 ANALYSIS @b3a272fffc: nothing served moves in round 68; a spin-off's factor is applied per event if and only if it reproduces the custodian's own price before the event; no threshold until the outlier days are classed. Round 68 issued in ONE issuance @f325600fbf, 4 of 5 chains spawned (CB-bp-1, bp-2, bp-3, bp-5); CB-bp-4 held on bp-1 and bp-3.
- 2026-10-11T13:43Z | tick 13. No new act owed; the four workers are inside their first tick.

Open at this seat: the five round-68 orders. No re-mint order is cut. The default leg is method_r28. `dep_stage` not moved. No FWD is claimed REALIZED by this seat.

## Compiler Tools

- `safe-merge.sh`: one drain (99), rc=0.
- `to-pipeline-gate.py` (through safe-commit): one issuance (r68: 5 orders).
- `round-close-check.py`: r66 MAY-CLOSE, r67 MAY-CLOSE.
- The valuation step, run once by the issuer at a named pin (read-only on S3; outputs in the session scratchpad); one unpinned run that refused.
- The silver suite, run by the issuer at the drain.
