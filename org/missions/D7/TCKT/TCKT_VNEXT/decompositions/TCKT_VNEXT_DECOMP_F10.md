# TCKT_VNEXT decomposition -- WORKSTREAM F10 (FWD-6 brought forward), 2026-10-08, issuer 2.0.0_SA_COO~V2, dell2

PRD `org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md` ADDENDUM 1 @f8c019c28f (`1.0.0_SA_CTO~DELL2`, msg 1789). It is a
sequencing addendum that re-opens no half. Andrew-direct record @a4fdb78bbe: the AI investment commentary is the priority.
NFRA_TRNSPT FWD-10 hop H5 (C-TICKET) = this project's FWD-6.

**Workstream, not a round.** Round 1 (`TCKT_VNEXT_DECOMP.md`) stays frozen on TV-r-1. Its write set on `ticket_center/` is
drained and merged, so F10's write set does not overlap any open order.

**Rectangle: the H6 -> H5 contract** (`deliverables/2.0.0_SA_COO~V2/FWD10_H6_H5_TICKET_WRITE_CONTRACT.md` @a8410fcca3, DRAFT
until `~T2` accepts). The service side is in section 3 of that contract; the measured gaps are in its section 1.

| cell | builds | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|
| `F10-l-1` | Ticket service: (1) a `svc-commentary` principal class (sub + userType service), MATRIX `CREATE` only, and on CREATE it may write `analysis_request` only; (2) `draft_commentary` + `report_request_id` declared as type data on the `analysis_request` definition, accepted only from `svc-commentary`, validated, stored (`report_ref = {request_id}`), and `draft_commentary` kept out of the DL notice; (3) the 2026-08-12 finding held closed on the write path, as tests | FWD-6 | NOT-EVALUATED | dell2 worker | WORLD (path floor: a Lambda handler; the worker applies nothing) | worker | -- |
| `F10-d-1` | Deploy F10-l-1's code: an apply order to `0.7.0_AE_CloudOps~DELL2` (Andrew-direct msg 1758). Ledger opened and closed. After-reads: the deployed bytes against the build, the 08-12 read on the deployed function (no authorizer context -> 403; a body-asserted identity is not stamped), and an existing-type create byte-identical | FWD-6 | NOT-EVALUATED | ISSUER cuts the apply order; the applier applies | WORLD | -- | F10-l-1 drained |
| `F10-r-1` | The seat-driven arm: one `svc-commentary` CREATE through the deployed route carrying a draft, read back from the ticket; a different-type create and a LIST by `svc-commentary` refused | FWD-6 | NOT-EVALUATED | ISSUER | WORLD | -- | F10-d-1 closed; O1 (the token) landed |

Status vocabulary: NOT-EVALUATED / BUILT / SERVED / REALIZED. FWD-6's organic arm is the drafter's first real draft (~T2's H6)
and is recorded, never waited on.

## External requests (not cells)

- **O1, the `svc-commentary` token** (issuer TO-D, laptop; the precedent is `svc-analyst-intake`). The CTO routes it through
  MSTR (msg 1789). F10-r-1 waits on it; the build does not.
- **The contract's acceptance by `2.0.0_SA_COO~T2`** (sent 22:24Z). It does not gate the build: the service side is this project's.
  An amendment that changes section 2 re-cuts F10-l-1 before its drain.

## Write set

- `F10-l-1` (slot ~3): `infra/aws/lambda/ticket_center/lambda_function.py`;
  `infra/aws/lambda/ticket_center/tests/test_commentary_write.py` (new). READ only: the other files in `tests/`.
- No Terraform hookup. The CREATE route exists, `svc-commentary` rides the existing authorizer, and `ROUTING_MATRIX`
  `analysis_request` exists. F10-d-1 is a code-only apply (the Lambda artifact).

**Chains.** A = F10-l-1 (slot ~3) -> F10-d-1 (issuer -> applier) -> F10-r-1 (issuer, + O1). Fan-out 1 of 1, cap 8.

## Rule 24 record

- **MECE over a declared domain.** Domain: the contract's section 3 items 1-5. By subtraction:
  - items 1-4 = F10-l-1 (principal, fields, firm check, DL exclusion);
  - item 5 (the 08-12 read) = F10-l-1 as tests at build, plus F10-d-1 on deployed bytes;
  - the token = O1;
  - the live write = F10-r-1;
  - the drafter (H6) is NFRA_TRNSPT's.
  - Remainder: "who sent the final commentary and when" (FWD-6's second clause). It is not in the CTO's addendum scope, so it is
    filed as surprise row D2-S6 and not built here.
- **Same grain.** One worker cell per write set; the served acts are the issuer's and the applier's.
- **Intent coherence.** l = the service admits exactly one new writer for exactly one shape; d = it reaches the served API;
  r = it is exercised once.
- **State coherence: what no cell moves.**
  - The four untyped types, the client submit path, the internal CREATE behaviour for humans, and the report route are unchanged.
  - No notification is added. The DL email gains no field.
  - No IAM, Lambda permission or Terraform change. Nothing on IRPT.

## Battery

- `comp-schedule`: DECLARED-NOT-APPLICABLE -- no schedule, hold or gate is created or consumed.
- `comp-iam`: DECLARED-NOT-APPLICABLE -- no IAM change. `svc-commentary` is an application-level principal class read from the
  existing authorizer context.
- `comp-adversary`: DECLARED-NOT-APPLICABLE at the cut. The adversarial read of the authorization change is F10-AC3 (the 08-12
  finding as tests) plus F10-d-1's deployed read.
- `comp-routes behaviors` / `comp-blast`: the round-1 reads stand. The route set is unchanged (`/api/scoped/tickets/*` #12), and
  comp-blast fails on dell2 (no secret read), so that blindness is restated.
- Drain checks (on no face): `commit-gate.sh` on the touched `.py`; the whole ticket-center suite once after the merge
  (`test_authz_matrix.py`, `test_analysis_request.py`, `test_we_dl_notice.py`, `test_client_notify.py`,
  `test_directory_resolution.py`).
