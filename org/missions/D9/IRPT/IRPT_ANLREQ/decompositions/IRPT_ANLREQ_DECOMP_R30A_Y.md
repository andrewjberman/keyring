# IRPT_ANLREQ -- decomposition, round 30A: THE FWD-1 CONSOLIDATED RELEASE BUILDS (four legs), workstream YU round 30 (issuer 2.0.0_SA_COO~Y2)

**Input:** the release census `AR-y-295` (drained @8929ccbc4e; record `deliverables/0.9.0_WK_IRPT_ANLREQ~113/r28/FWD1_RELEASE_CENSUS.json`): five packages, ten members, four legs in order. The census found the release-21 start state stale (the live `irpt-ycharts-generate` moved at 2026-10-13T22:48:27Z), the resident builder at the pin unable to package the packager and the calendar, and the checker `intake/yfinance_check.py` unimported by any production module (excluded from this release). The never-widen pair cannot be written without the built artifacts: each leg's package is BUILT here, staged outside the repository, compared with the LIVE package member by member, and re-hashed by the checker. Nothing is uploaded, applied or deployed by these cells.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-297` | LEG L1: the `opal-ticket-api` zip (`lambda_function.py` only: AR-y-280, -281, -284), delta against the live package, rollback VersionId, Terraform note | the worker's record folder, the surprise channel file; the staged zip outside the repository | LOCAL |
| `AR-y-298` | LEG L2: the `irpt-status` zip (`status.py`, three words, AST words-only), delta, rollback | as above | LOCAL |
| `AR-y-299` | LEG L3: the `irpt-ycharts-generate` zip built against the package live NOW (reader r19.3, portfolio, uploads, security_resolution, plus the calendar added), delta, rollback | as above | LOCAL |
| `AR-y-300` | LEG L4: the resident tarball from one scratch input at pin `0485393f3a` (six replaced members, the packager and the calendar added, a minimal builder edit), host script, delta against the release-19 tarball, tests in a scratch tree | as above | LOCAL |

## Edges and chains

- Four independent chains (each package is built and compared alone); no cell reads another's output. The order the legs MOVE in (L1 before L4; the calendar with the portfolio member; the words before the legs that emit them; the resident before the Lambda) is the pair's, from the census record, not the builds'.
- Not in this round: the never-widen pair (the issuer, after the four records), the apply orders (appliers `0.7.0_AE_CloudOps~AQ2` for the Lambdas and `~YC2` for the resident, named in the pair), the synthetic-advisor drive, the checker's wiring (dell1's via MSTR).

fanout: 4 of 4 chains, cap 8, reason: four independent package builds, one per served package; each reads the live package of its own function and shares no write surface.
