# IRPT_ANLREQ -- decomposition, round 45, workstream ~TX (issuer 2.0.0_SA_COO~T2)

**Input:** the CTO's parallelization ruling, Move 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md`, msg 8742), on Andrew's go: `2.0.0_SA_COO~T2` takes IRPT_ANLREQ FWD-5 ("another firm never sees the request, the package or the commentary") and FWD-4 ("a broken hop never silently stops the request"): "FWD-5's cross-firm tests on the paths that run today; then FWD-4's per-step failure surfacing, as gates and owned rows, never a new alarm (the standing moratorium)". Write surface: "tests and the pipeline's own refusal paths in the commentary and request lanes". No PRD addendum: both are ENDPOINT outcomes of the admitted PRD (`prd/IRPT_ANLREQ_PRD.md:59-68`).

**Measured before the cut:** about 84 test-file hits across the estate already assert a firm or tenant mismatch (`comp-find` for `cross_firm|other_firm|TENANT_MISMATCH|FIRM_MISMATCH`, 2026-10-15), including `infra/aws/lambda/ticket_center/tests/test_fence_other_firm.py`; the FWD-5 DONE WHEN is EXERCISED ("a sign-in at another firm tries the ticket and each package file and is refused every time, repeatable on demand"). What is not known is which of the request's own paths have such a test and which do not, so round 45 maps before it builds.

**Round shape.** Round 45 is four READ cells that each write one cited-line record checked by `R45_CHECKS/r45_checks.py` (every citation a real line, every quote near it, a closed verdict set, the denominator equal to the rows). Round 46 cuts the BUILD cells from the records: a test for each `REFUSES-UNTESTED` row, a refusal for each `ADMITS`, the surfacing of each `SILENT` hop as a gate or an owned row.

## Cells

| cell | outcome | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-tx-41` | FWD-5 | FWD-5 map: where the ticket service lets another firm in or keeps it out: a cited-line record `FWD5_TICKET_SERVICE_FENCE_MAP.md` | the worker's deliverables folder only | LOCAL |
| `AR-tx-42` | FWD-5 | FWD-5 map: where the report side binds a read to the request's firm: a cited-line record `FWD5_REPORT_SIDE_BINDING_MAP.md` | the worker's deliverables folder only | LOCAL |
| `AR-tx-43` | FWD-5 | FWD-5 map: the front door and the portal, and what a seat-driven other-firm sign-in needs: a cited-line record `FWD5_FRONT_DOOR_AND_PORTAL_MAP.md` | the worker's deliverables folder only | LOCAL |
| `AR-tx-44` | FWD-4 | FWD-4 map: what each hop's failure does today and whether the ticket says so: a cited-line record `FWD4_PER_HOP_FAILURE_MAP.md` | the worker's deliverables folder only | LOCAL |

## Edges and chains

- Four independent chains: no cell consumes another's output and none writes a file another writes. M = 4. FWD-1 stays `~Y2`'s thread; FWD-3's commentary lane (workstream `~T`) is closed for now.

fanout: 4 of 4 chains, cap 8, reason: four independent read cells with disjoint outputs.
