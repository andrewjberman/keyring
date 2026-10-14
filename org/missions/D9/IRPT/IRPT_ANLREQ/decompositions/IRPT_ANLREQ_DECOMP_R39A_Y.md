# IRPT_ANLREQ -- decomposition, round 39A: THE RELEASE-29 BUILDS (the Shares words and the ordinary-viewer authorizer), workstream ZD round 39 (issuer 2.0.0_SA_COO~Y2)

**Input:** two drained cells, both BUILT and NOT RELEASED: `AR-y-306` (the ordinary-viewer authorizer: `_scope/ordinary_viewer.py` NEW, `reports/generate_installed.py` wired over the two canonical readers; the upload door and the owned-input analysis route admit a FIRM_ADVISOR or FIRM_OPERATIONS viewer for its own firm only) and `AR-y-308` (the words for `SHARES_PRICE_SOURCE_NOT_COMPOSED` in `intake/uploads.py` and `ops/status.py`, byte-equal). Release 28 is live (L2 `irpt-status` MIVrDbv+, L1 `opal-ticket-api` C/Rt/Fn, L4 the resident root `0485393f3a-r28`, L3 `irpt-ycharts-generate` reAjAQOV). Release 29 moves, by package: `irpt-status` (L2: `status.py`), `irpt-ycharts-generate` (L3: `uploads.py`, `generate_installed.py`, and the added `ordinary_viewer.py`), the resident (L4: `uploads.py`, `status.py`). No census cell: the delta is two cells and the packages are known from release 28 (the resident carries `generate_installed.py` too, but the module is imported lazily and the door runs in the Lambda, so the resident does not move it: the pair states that choice).

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-309` | LEG L2: the `irpt-status` zip (`status.py`, one word entry, AST words-only), delta against the live package, rollback VersionId | the worker's record folder, the surprise channel file; the staged zip outside the repository | LOCAL |
| `AR-y-310` | LEG L3: the `irpt-ycharts-generate` zip built against the package live NOW (`uploads.py`, `generate_installed.py`, plus the added `ordinary_viewer.py`), import closure, delta, rollback | as above | LOCAL |
| `AR-y-311` | LEG L4: the resident tarball over the r28 root (`uploads.py`, `status.py`), the host script, the three host scripts and the staged sums, tests in a scratch tree | as above | LOCAL |

## Edges and chains

- Three independent chains. The pair (the issuer's) states the order of the legs: L2 first (the words before the door emits them), then L4, then L3 (the authorization change last); and the partner-advisor run after L3 (a sitting under the pair, with a synthetic FIRM_ADVISOR of 49financial). Not in this round: the pair, the apply orders, the Shares price-source READ cell (the next enrichment).

fanout: 3 of 3 chains, cap 8, reason: three independent package builds, one per served package; each reads the live package of its own function and shares no write surface.
