# IRPT_ANLREQ -- decomposition, round 46, workstream ~TX (issuer 2.0.0_SA_COO~T2)

**Input:** the round-45 records (four READ cells, all instances VALID, `r45_checks.py rec` OK): `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~210/FWD5_TICKET_SERVICE_FENCE_MAP.md` (34 rows), `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~211/FWD5_REPORT_SIDE_BINDING_MAP.md` (38 rows), `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~212/FWD5_FRONT_DOOR_AND_PORTAL_MAP.md` (58 rows), `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~213/FWD4_PER_HOP_FAILURE_MAP.md` (35 rows over 21 hops). The CTO's parallelization ruling, Move 2 (msg 8742): "FWD-5's cross-firm tests on the paths that run today; then FWD-4's per-step failure surfacing, as gates and owned rows, never a new alarm (the standing moratorium)". Write surface: "tests and the pipeline's own refusal paths in the commentary and request lanes".

**Round 45 measured:** report side, 16 `REFUSES-UNTESTED` reads (a refusal in code with no test that fails when it is removed); ticket service, one untested route (POST meeting) and four `ADMITS` findings that are design questions (pickup notice recipient taken from the request body, the `svc-analyst-intake` list unscoped, an internal PROFILE row with no `allowedFirmIds` admitting every firm, two OPAL_GLOBAL admissions by documented design); FWD-4, 24 of 35 hop rows `SILENT` and a failure note on the ticket needing a ticket-service route (a design question). The ADMITS rows are not cells here: they are owned rows for the ticket-service owner and the CTO (surprise channel), because a change of who the service admits is not a test.

**Round shape.** Round 46 builds the tests for the `REFUSES-UNTESTED` reads that run today (five cells, tests only, new files), the parameterized mint a seat-driven second-firm exercise needs (build only; the run is a later WORLD act under a pair), and one read for the FWD-4 design question. The FWD-5 driver (the script that signs in as the second-firm principal and tries the ticket and each package file) is round 47, after the mint contract exists.

## Cells

| cell | outcome | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-ty-51` | FWD-5 | FWD-5 tests: the report repository refuses another firm's report, history and artifact | `test_cross_firm_report_reads.py` | LOCAL |
| `AR-ty-52` | FWD-5 | FWD-5 tests: the owned request and analysis readers refuse another firm, PDF routes included | `test_cross_firm_owned_reads.py` | LOCAL |
| `AR-ty-53` | FWD-5 | FWD-5 tests: the commentary draft store, the retention gate and the owner-read guard refuse another firm | `test_cross_firm_draft_store_get_ref.py`, `test_cross_firm_retention_gate.py`, `test_cross_firm_owner_reads_guard.py` | LOCAL |
| `AR-ty-54` | FWD-5 | FWD-5 tests: the report index, the packager's draft read and the retained export refuse another firm | `test_cross_firm_report_index_get.py`, `test_cross_firm_packager_read.py`, `test_cross_firm_retained_export_get.py` | LOCAL |
| `AR-ty-55` | FWD-5 | FWD-5 test: the ticket service refuses a meeting write from a caller out of the ticket's scope | `test_cross_firm_meeting_scope.py` | LOCAL |
| `AR-ty-56` | FWD-5 | FWD-5 build: a mint helper for a scoped principal of a second firm | `fwd5_mint.py`, `test_cross_firm_mint.py` (deliverables ~219) | LOCAL |
| `AR-ty-57` | FWD-4 | FWD-4 design read: the ticket service's service-principal write routes and what the portal shows | `FWD4_TICKET_WRITE_ROUTES_MAP.md` (deliverables ~220) | LOCAL |

## Edges and chains

- Seven independent chains: no cell consumes another's output and no two write the same file (each owns new files under distinct paths). M = 7.
- A one-line hookup: none; tests are discovered by pytest, nothing is imported by another cell.

fanout: 7 of 7 chains, cap 8, reason: seven independent cells with disjoint new files; five test files sets, one build, one read.
