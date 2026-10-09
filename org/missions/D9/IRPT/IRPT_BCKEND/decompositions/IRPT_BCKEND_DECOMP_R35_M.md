# IRPT_BCKEND decomposition -- ROUND 35, WORKSTREAM ~M (2026-10-09, 2.0.0_SA_COO~M2, dell2)

**Cut on:** `2.0.0_SA_COO~Y2` msg 2202 (release 6 blocker): `holdings/snapshot.py:143` imports `publication`, but
`irpt-ycharts-generate` stages `ycharts/extract/publication.py` under that name (no HoldingsPublication). This is a repair of this
seat's own round-34 port (CTO msg 2127; ADDENDUM 13 @1aee15882f), inside this seat's decomposition.

**Measured at the cut:** `snapshot.py` also imports `enforce`, `ids` and a `sys.path` walk at module load (snapshot.py:39-46), so
staging `snapshot.py` in another function would drag those in. The port therefore moves to a standalone module that imports
`holdings_publication` (the name `~Y2` stages holdings/publication.py under) and falls back to `publication` (the holdings functions'
own name); with neither, it fails closed (ImportError). The S3 read set is unchanged (round-34 packet).

**Rectangle:** one cell.

| cell | item | outcome | risk | depends on |
|---|---|---|---|---|
| `IB-mp-351` | **The publication_for port as a standalone module.** New `holdings/holdings_publication_port.py` with `holdings_publication_for(s3_client=None)` (same signature and behavior as round 34); `snapshot.holdings_publication_for` removed (no consumers); `holdings/tests/test_publication_port.py` repointed to the new module. | ~Y2 msg 2202 (release 6) | WORLD (gate floor: infra/ path; no AWS call, no deploy) | none |

**Chains:** A = 351. M = 1. fanout: 1 of 1 chains, cap 8. Slot ~202 (block ~200..~219, msg 974).

**Size and path:** about 30 product lines; full limbs (worker, drain, the issuer's one real run, L8 packet to `3.0.0_SA_CVO`). Nothing
deploys here; `~Y2` stages the module in release 6.
