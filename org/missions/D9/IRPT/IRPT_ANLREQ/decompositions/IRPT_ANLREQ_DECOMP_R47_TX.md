# IRPT_ANLREQ -- decomposition, round 47, workstream ~TX (issuer 2.0.0_SA_COO~T2)

**Input:** the CTO's ruling on row IRPT_ANLREQ-D2-S134 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FOUR_LANES_END_TO_END_20261015.md` ADDENDUM 7, msg 8834): the four cross-firm admissions round 45 found in the ticket service are fixed by `2.0.0_SA_COO~V2` (TCKT_VNEXT round 19, contract `org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R19.md`), and "your FWD-5 tests are the acceptance (red now, green after). Next issuance keeps fan-out at 4, not 7." No PRD addendum: a defect fix inside the admitted PRD's FWD-5 (`prd/IRPT_ANLREQ_PRD.md:65-68`).

**Round shape.** Three ACCEPTANCE test files, one per fixed item (notice recipient, intake list scope, fail-closed profile scope), written RED against the code at the base and turning GREEN when V2's release lands; and one GATE test for item 4 (the register of global admissions), green today, red when an admission is added without a register row. Round 46 (`AR-ty-51..57`) covered the reads that were already bound but untested and built the scoped second-firm mint; the FWD-5 driver that signs in as the second-firm principal is round 48, after V2's release and the mint run.

## Cells

| cell | outcome | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-tz-61` | FWD-5 | FWD-5 acceptance tests (red): the client notice goes to the ticket firm's contact, never to a body address | `test_cross_firm_notice_recipient.py` | WORLD (path floor; tests only) |
| `AR-tz-62` | FWD-5 | FWD-5 acceptance tests (red): svc-analyst-intake lists only the firms it is configured for | `test_cross_firm_intake_list.py` | WORLD (path floor; tests only) |
| `AR-tz-63` | FWD-5 | FWD-5 acceptance tests (red): a staff profile with no firm scope reads no firm | `test_cross_firm_profile_scope.py` | WORLD (path floor; tests only) |
| `AR-tz-64` | FWD-5 | FWD-5 gate: every global (every-firm) admission in code is a row of V2's register | `test_cross_firm_global_register.py` | WORLD (path floor; tests only) |

## Edges and chains

- Four independent chains: each cell owns one new file under `infra/aws/lambda/ticket_center/tests/`; none consumes another's output. M = 4.
- Green-after acceptance (run by the issuer, not a worker): when V2 reports each round-19 cell merged, the issuer runs the matching file with the `tests` mode of `R46_CHECKS/r46_checks.py` against the merged code; row S134 disarms when all four read green.

fanout: 4 of 4 chains, cap 4, reason: the CTO's word (msg 8834) keeps fan-out at 4 for the dell2 CPU budget; four independent new files.
