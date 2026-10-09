# ADVI_COTBKF round 46 -- L9 grade

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~15:4xZ. Packet `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_46_DRAIN_END_20261009.md @f723ea78df (msg 3587)`. Rows D2-S70, D2-S71.

| criterion | verdict | evidence |
|---|---|---|
| CB46at1-AC2: beside-module first, then repo root, for EVERY repo-file input, the import included; unresolved never the own firm; the census prints each resolved path from the served file's metadata | MET as written | The diff 14a6fd3343..8bd569d91e adds one `resolve_repo_file`. It covers `scopes.json` (beside only, per round 42's test h) and `ticker_overrides`, the import included, beside first and then the repo. An unresolved input stamps `absent`. The census prints `INPUT name=.. path=.. how=.. firm=..` from `opal_input_resolution`, and `INPUT-RESOLUTION absent` (NOT-CLEAN) when the metadata is missing |

**BLOCKING (D2-S71):** the same change made `ticker_overrides` fail OPEN. The old `from lib.ticker_overrides import` stopped the run when the
file was missing. The new loader returns empty dicts and a WARN, so a redeploy that misses the file would silently drop 757 overrides and
serve wrong prices. Restore the fail-closed load before the redeploy, as well as shipping the file beside the writer.
