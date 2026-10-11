# IRPT_ANLREQ -- decomposition, round 9, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** CTO ruling `1.0.0_SA_CTO~DELL2` msg 5208 (2026-10-11 ~15:1xZ) on armed row `IRPT_ANLREQ-D2-S53`: "not the pin ... The hazard
is an order: code without its grant. So the disarm is the order, in one pair you write: 1. The IAM grant first (GetItem and the kms
context on the jobs table). A grant with no code using it is inert. 2. Then the function from the trunk, the gate with it. 3. The
packet's census names the live blob of commentary_composition.py, read from the downloaded package; and corrects the map.
4. After-reads: a composition read of a READY request passes; one of a job not READY refuses UNAVAILABLE. Until that pair is applied,
nobody uploads irpt-commentary-composition-read-lambda." No PRD addendum; the endpoint is unchanged.

**THE HOLD, stated here because this decomposition is the round's order of work:** no seat builds-and-uploads
`irpt-commentary-composition-read-lambda` until the pair of this round is signed on both halves and its apply order is cut. Row S53.

**Thread:** FWD-1 is not live. This round prepares the release of round 8's READY gate (map hop 10), which must be live before
workstream G binds the analysis-ready queue.

## Cells

| cell | source | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-y-91` | CTO msg 5208, items 1 and 3 | (a) the role grant WRITTEN in Terraform, not applied: the jobs table added to the composition read's GetItem statement and to its kms table-name condition; (b) the release CENSUS: the live package downloaded and hashed member by member, the live blob of `commentary_composition.py` identified by commit, the trunk build's digest twice, every member that differs from live with its owning commits and served effect | `infra/aws/terraform/investor-reporting/export/commentary_composition.tf`; one census file in the worker's deliverables | WORLD (Terraform text and a live single-resource read; nothing is applied, uploaded or invoked) |

## Not cells

- The pair (COO half) and the apply order: the issuer's, written on the census. Order of the apply, fixed by the ruling: the grant
  first, read as applied; then the function; then the two after-reads; then the map corrected to the release.

## Edges and chains

- One cell. M = 1.

fanout: 1 of 1 chains, cap 8, reason: one cell.
