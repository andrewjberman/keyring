# IRPT_ANLREQ -- decomposition, round 23D: THE J2 CLOSE (the packager records the request id on the filer's ticket), workstream Y round 26 (issuer 2.0.0_SA_COO~Y2)

**Input:** `AR-y-280` (SUBMIT-FORM takes an analysis_request, drained @96b1a95596) stopped its step 3 with row `IRPT_ANLREQ-D2-W101-S1`: the packager's PACKAGE body carries `report_id` and no request id (`ycharts/research/opal_packager.py` :208-209), although `handle_commentary_ready` holds the request id (:146); the ticket service writes `package.report_ref` (opaque) and never the top-level `report_ref.request_id` that the drafter and REPORT use. The CTO's ruling (A) (msg 7204): "`svc-irpt-packager` records `report_ref` once". Two cells, one interface (the PACKAGE body gains optional `request_id` and `request_revision`; the service writes the top-level `report_ref` once; a different id is 409).

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-284` | SERVER: `package_ticket` validates `request_id` and `request_revision` and records the top-level `report_ref` once (idempotent for the same id, 409 for another), the authorization change stated | the ticket service file and one new test file | WORLD |
| `AR-y-285` | PACKAGER: the PACKAGE payload carries `request_id` and `request_revision`; the already-attached idempotence still reads the four pointers only | `ycharts/research/opal_packager.py` and one new test file | WORLD |

## Edges and chains

- None blocking the builds (the interface is fixed in each order). Both go into the one never-widen pair for the partner-firm filing (with `AR-y-280` and `AR-y-281`): the Lambda leg of the ticket service, the resident leg carrying the packager, and the portal's DEV landing. The packager runs in the resident, whose host files are `~G2`'s lane: the issuer relays that to the CTO if a lane gate refuses the worker.

fanout: 2 of 2 chains, cap 8, reason: two independent halves of one contract against a fixed interface.
