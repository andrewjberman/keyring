# TCKT_VNEXT decomposition -- ROUND 2 (thread repair), 2026-10-11, issuer 2.0.0_SA_COO~V2, dell2

**Authority:** the CTO's round-2 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUND_2_20261011.md`
@bbba700c22 (msg 3968), section 4, answering the round-1 slug `ledger/L10_SLUG_R1.md` @23e3126092. No PRD addendum; no half re-opens.
FWD-1 is NOT REALIZED, so round 2 is still a thread round. The rectangle is the analysis's five-item enrichment list; item 2 splits
into a build cell and an apply cell.

| cell | builds | list item | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `R2-rn-1` | the FWD-1 seat-arm runner, repaired: the request id comes from the submission's answer, or from the firm's request list when the answer carries none; it never polls a value it sent; it polls that `REQ-<24 hex>` id, reads `stage` until GENERATED or RELEASED, records the id on the ticket and opens the report from the ticket. Nothing is run against AWS | 1 | FWD-1 | NOT-EVALUATED | dell2 worker, slot ~8 | WORLD by path floor (reads an infra file); nothing applied | worker | -- |
| `R2-rr-1` | ticket_center `POST /api/scoped/tickets/{ticketId}/report` refuses a `request_id` that does not match `REQ-[0-9a-f]{24}` with a typed code; a well-formed id is stored. Code and tests only | 2 (build) | FWD-1 | NOT-EVALUATED | dell2 worker, slot ~9 | WORLD by path floor (a Lambda handler); nothing applied | worker-light | -- |
| `R2-rr-2` | the apply of `R2-rr-1` to opal-ticket-api on DEV under its own never-widen pair; both arms read live | 2 (apply) | FWD-1 | NOT-EVALUATED | applier seat (0.7.0_AE_CloudOps lane) | SERVED | -- | R2-rr-1 drained; the pair signed |
| `R2-tr-1` | one seat-arm journey end to end on DEV with `R2-rn-1`'s runner, under a re-signed pair that names data-refresh in its radius with a zero-call read carrying a positive control; precheck irpt-status CodeSha256 `6idtFvAm...` (anything else is a STOP naming the apply owed); every live worktree's `.open_deploys/` read and unioned first; test ticket `TCK-20261009-67ab7f27` closed or marked in the same run | 3 | FWD-1 | NOT-EVALUATED | ISSUER + applier seat | WORLD | -- | R2-rn-1, R2-rr-2, the irpt-status precheck |
| `R2-cw-1` | a seat claims then completes `TCK-20261009-a1052909` on the DEV board through the browser crawler; the board is read after (Andrew, "crawl that instead", open call `-fbb1`) | 4 | FWD-1 (board) | NOT-EVALUATED | ISSUER (browser act) | SERVED | -- | -- |
| `R2-ts-1` | by default no ticket_center test can reach a real SES send or a real users-table read (rows D2-W1-S4, D2-W7-S1): a guard in `tests/conftest.py` | 5 | FWD-1 (hygiene) | NOT-EVALUATED | dell2 worker, slot ~10 | WORLD by path floor (test files under infra); nothing applied | worker-light | -- |

**Chains (M = 3):** {`R2-rn-1`, `R2-rr-1` -> `R2-rr-2`, all three -> `R2-tr-1`}; {`R2-cw-1`}; {`R2-ts-1`}. Inside the first chain
`R2-rn-1` and `R2-rr-1` share no edge and no file, so they take two slots. `R2-cw-1` takes no worker (a worker has no browser).
**Fan-out: 3 workers of 3 chains, cap 8.**

**Write sets (disjoint):** `R2-rn-1` its own deliverables folder only. `R2-rr-1` `lambda_function.py`, the new
`tests/test_report_ref_shape.py`, and request-id LITERALS in existing tests. `R2-ts-1` the new `tests/conftest.py` and the new
`tests/test_no_real_aws.py` only; it edits no existing test file.

## Rule 24 record

- **MECE over the analysis's section 4.** Domain: its five numbered items. By subtraction: item 1 -> `R2-rn-1`; item 2 -> `R2-rr-1` +
  `R2-rr-2`; item 3 -> `R2-tr-1`; item 4 -> `R2-cw-1`; item 5 -> `R2-ts-1`. Nothing of section 4 is uncovered. Section 2's three asks
  of this seat (the W6-S2 disposition row, the round-close-check tool-gap row, rows S3 and S4 to `2.0.0_SA_COO~Y2`) are issuer acts,
  not cells.
- **Same grain:** one cell is one write set or one live act.
- **State coherence: what no cell moves.** The authorizer, IAM, the IRPT read plane, any real user's access. No `kms:Decrypt` grant
  is added for any seat principal. `R2-rr-2` and `R2-tr-1` are cut when their pairs are signed; no order for them exists before that.

## Battery

comp-schedule, comp-iam: DECLARED-NOT-APPLICABLE for the three worker cells (no schedule, no IAM, nothing applied). comp-adversary:
the refusal arms (a malformed id, the sent-token shape, an ambiguous request list, a refusal envelope read as a read) are the
adversarial arms and sit on the faces. `comp-blast`, `comp-routes` and `comp-cache` are owed at the `R2-rr-2` pair, where a served
route changes, not at this cut.

Dry-run at the base (box/dell2, 2026-10-11 ~03:4xZ): rn-submit-id, rn-stage, rn-ticket, rr-shape, ts-guard FAIL absent as expected;
tc-regress PASS as expected (passed=147).

## ADDENDUM 1 (2026-10-11 ~04:0xZ) -- round 2 gains a page cell, by CTO ruling msg 4026 on row TCKT_VNEXT-D2-S24

The portal's ticket link opened the accepted request record, not a report (row D2-S24 @655e71ea5a). The CTO ruled (a): "the ticket
link opens the finished report; round 2 gains the page cell", and that it "outranks everything left in round 2". The CTO also ruled
(msg 4015, then 4026) that `R2-tr-1`'s oracle is the read the ticket's own link performs returning the report; the served request read
carries no `stage`, so `R2-rn-1`'s stage poll does not grade the journey and the runner takes that oracle in the `R2-tr-1` pair.

| cell | builds | list item | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `R2-pg-1` | portal Ticket Center: `openReport` reads the finished report for the ticket's request id by the read the Investor Reporting page uses for a generated analysis; a report not yet generated shows a stated waiting state; the request record is never presented as the report. The candidate goes to the CTO before portal DEV | ruling 4026 | FWD-1 | NOT-EVALUATED | dell2 worker, slot ~11 | LOCAL | worker | -- |

**Edge added:** `R2-pg-1` -> `R2-tr-1` (the re-run is graded on the link this cell repairs). Chains stay M = 3; the first chain gains
this cell. Write set: `portal/src/pages/TicketCenter/` (four files), disjoint from every other cell.

Dry-run at the base (portal DEV dbeb6764ea): pg-open FAIL absent as expected; pg-existing PASS as expected (pass=4).
