# Graph coherence -- four loose ends, measured 2026-10-09 ~04:4xZ, routed to their owners

**By:** `4.0.0_SA_CRO`, the lead of the graph coherence build (Andrew-direct ~16:5xZ 2026-10-08), on Andrew's ask at this
terminal ~04:3xZ 2026-10-09 to assess where the graph work stands. Status record of the build:
`GRAPH_COHERENCE_BUILD_20261008.md` (same folder). The fold-in to the served graph is live (GRAPH_OVERLAY.TO-APPLY-1, first
publish 2026-10-09T00:49:09Z; the 03:31:25Z build carries 4,352 COMMIT, 544 SURFACE, 401 SEAT, 29 PROJECT, 4 BOX nodes).

| # | Loose end | Measured | Owner |
|---|---|---|---|
| 1 | Site Z writes no activity records | `comp-activity boxes --hours 24`: sitez claim `inferred` only, last record 2026-10-08T14:46:34Z; site Z commit 7a37c5b906 (10-09 04:28Z, NFRA_MCPINDEX decomp) is absent from `comp-activity who` on its file. Fix: `bash .tools/git-hooks/install-fabric-activity.sh` on site Z, then one `comp-activity boxes` reading `sitez ... measured`. | `0.0.0_AB_MSTR` (relay to `0.0.0_AB_MSTR~Z`) |
| 2 | The Dells' graph read is APPLIED, never EXERCISED | `close(NFRA_CTLPLN.TO-APPLY-14)` @aae065fc40 says "APPLIED, not EXERCISED, until each Dell runs one graph query"; no later commit records one. Fix: on dell1 and on dell2, `comp-kuzu "MATCH (n:CloudNode) RETURN count(*)"` and quote its VINTAGE line. | `2.0.0_SA_COO~C` (issuer of TO-APPLY-14) |
| 3 | `placement-check.py:90` places Dell projects on the laptop | Row `NFRA_CTLPLN-S32`, still UNDER_INVESTIGATION; `.tools/placement-check.py:90` still reads `d.get("fabric")`, never `placement`. | `2.0.0_SA_COO~C` (built the tool, @ed7e23c2a2) |
| 4 | Row `NFRA_CTLPLN-S31` (Dell write to the graph bucket) is open | UNDER_INVESTIGATION; Andrew's call 3 (~15:4xZ 2026-10-08, record `ANDREW_DIRECT_20261008_154xZ_...`): "They should be able to." Fast fix F5: no Deny. Disposition it on that word. | `2.0.0_SA_COO~C` (the row's `disarm_owner`) |

Not loose ends: the engine (Andrew ruled (a), Kuzu, ~17:4xZ; a LadybugDB trial only on his ask), the comp-tool mapping
(`comp-activity`, @b29432fc1d), and an overlap page (only if Andrew wants one).
