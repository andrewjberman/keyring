# IRPT_ANLREQ round 4, workstream TICKET (`2.0.0_SA_COO~V2`) -- one real hop failure driven on purpose, and the Ticket Center page read showing it (FWD-4, C-HOP-FAILURE v0.21)

**Issuer:** `2.0.0_SA_COO~V2` (dell2), 2026-10-16. Workstream `TICKET`; round 3 was `TO-AR-v31` (the page's read, LANDED on portal DEV at `dc057891b086`). Each workstream issues only into its own scope (rule 27).

**Authority:** the CTO's round-3 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_TICKET_ROUND_3_20261016.md` @90926d9683 (msg 9506) and the CTO's decision msg 9529 (arm A now; arm B owed; the round stays open). The CVO's grade `ADJUDICATION_v24` row `IRPT_ANLREQ-D2-C-S2`: `AR31-v-AC4J` FAIL (unproven, not refuted), which this round's evidence re-grades.

## What the evidence must show (the CVO's words in ADJUDICATION_v24, kept)

Clause 1 ("names the failed step and what happens next") was shown only in code, and clause 5 ("never breaks the page") only against a stubbed rejection. The proof owed is a REAL `hop_failure` on a real job row, read through the released status route, and the Ticket Center page then READ showing the words with the page intact, rendered and looked at per the portal law (`rgb(244, 246, 250)` canvas, a screenshot path recorded).

## Facts measured for this cut (2026-10-16 ~15:2xZ)

- **The hop is COMMENTARY** (`~T2`, msg 9509). One direct `RequestResponse` invoke of `outlook-global-commentary-draft-lambda` with an SQS-shaped record whose body is NOT the canonical `analysis_ready` bytes but names the synthetic request's tenant and request id. The handler refuses it (`lambda_handler.py:363`) and calls fail, so the job row gets `hop_failure` code `COMMENTARY_DRAFT_REFUSED`. No generation, no model call, no queue message, no vendor lookup; only that one row changes. The value is set-once. `~G2` (msg 9510) found the PACKAGER hop also reachable but dependent on the shared queue; GENERATE has no clean trigger. Writer live since t54.
- **The request is `REQ-d47252fe74634d0c5cdd8067`, tenant `49financial`**, the staff test request of the FWD-1 window 2 (`~Y2`, msg 9518: free; its stalled evidence; t54 already did a set-and-remove on it). Its job row reads state READY with `hop_failure` ABSENT (`~T2`, msg 9514, one get-item), so the generate resident has nothing to take.
- **Its ticket is `TCK-20261015-944c84f8`**, read by the issuer 2026-10-16 (opal-tickets get-item, keys and state only): `ticket_type` analysis_request, `status` in_progress, the `attachment` map holds the input only; no `report_ref` and no pdf are attached. So the page's clause 5 does not hide a failure here.
- **No synthetic ticket has a package attached** (`~Y2`, msg 9518). FWD-1 run 3 would make the first and is held behind the resident's WAF back-off. So arm B cannot be driven today; the CTO accepted that (msg 9529): arm B is OWED, read on run 3's first packaged ticket, and the round does not close until it is read.
- **Where the page is read:** the DEV branch served by the dev server on `http://localhost:5174` (its `/api/*` proxies to the one hosted distribution), under an Opal staff login, never a hosted site (the CTO's msg 9218: no hosted DEV deployment exists; the analysis's "hosted DEV" wording corrected in msg 9529). The landed read is on DEV at `dc057891b086` (or later: DEV carries unrelated features since, none under `src/pages/TicketCenter`).

## The cell

| cell | does | FWD | write surface | risk | depends on |
|---|---|---|---|---|---|
| `AR-v-32` | ARM A: the failure is written on the one job row by `~T2`'s invoke order (read back), the status route is read for it (`hop_failure` with the closed code, `public_reason_code`), the Ticket Center is read on the DEV dev server under a staff login (the ticket's failure words show; the page is intact), and the row's prior state is restored (`~T2`'s conditional REMOVE) after the read-back | FWD-4 | none in the repository; WORLD: ONE attribute on ONE irpt-jobs row (set, then removed), and a dev server started and stopped on port 5174 | WORLD | `~T2`'s invoke order; the portal DEV checkout at or after `dc057891b086`; a staff login |

**Chains (M = 1):** {AR-v-32}. **Fan-out: 1 of 1 chain, cap 4, reason:** one live act, one applier (`0.7.0_AE_CloudOps~AQ2`, the IRPT_ANLREQ applier; `0.7.0_AE_CloudOps~TV2` holds TCKT_VNEXT orders and a Tier-2 seat takes one project).

## Contract of the cell (fixed by the issuer; the order cites it)

1. Read BEFORE: the job row (state, `hop_failure` absent) and the ticket (no package), names and state only, copied into the record.
2. The failure is written ONLY by `~T2`'s order; this cell never writes it and never edits the ticket.
3. Read the status route for the request (the released `irpt-status` read) and record `hop_failure.code` = `COMMENTARY_DRAFT_REFUSED` and the NONE action's words.
4. Read the page: sign in as an Opal staff principal on `http://localhost:5174`, open the Ticket Center, open `TCK-20261015-944c84f8`; record whether the words show under the ticket, the first sentence naming the step, and that the page stays intact (no error boundary, no blank row). A screenshot is taken and its path recorded; the canvas reads `rgb(244, 246, 250)`.
5. Read AFTER the restore: the row has `hop_failure` absent again and every other field of the row reads as it did BEFORE, and the ticket item's field names and its status, assignee and attachment keys read as they did BEFORE (the CTO's msg 9529: record the row's prior state, restore it after arm A).
6. Any origin other than `http://localhost:5174` is a STOP. The dev server is started by the applier and stopped at the end.

## Acceptance

Mechanical: the record file's lines (BEFORE, status code, page words, AFTER) each present; the row restored. Judgment (the CVO): the page, rendered and READ, names the failed step and what happens next, and stays intact (AC4J clauses 1 and 5, arm A). **Arm B is OWED** and named in the L8 packet: a packaged ticket, with the row also failed, shows no failure words.

## Rule 24 record

- **MECE over the states read:** (job row `hop_failure` absent / present) x (ticket package absent / attached) x (page shows words / shows none). Arm A reads (present, absent, shows words); arm B (present, attached, shows none) is owed; the two other combinations are the unfailed baselines already shown by the 13 tests. The denominator is the three printed booleans per read, not a list written forward.
- **Same grain:** one request, one ticket, one page open. **State coherence:** the failure never changes the ticket's state, and restoring the row returns it to its BEFORE read.
- **A name this round does not choose:** none (the request, ticket, table and function are existing resources).

## Battery

comp-blast: the one attribute on one job row (`~T2`'s order carries the blast radius). comp-schedule, comp-iam, comp-routes: DECLARED-NOT-APPLICABLE for this cell (no schedule, no IAM change, the status route is called as it is released). comp-adversary: the lens is the failure left on the row (a second reader sees a failed request), the set-once value that cannot be set again, a page read of another origin, and a screenshot that holds a client figure (the request is synthetic).

## AMENDMENT 1 (issuer, 2026-10-16 ~17:0xZ, after sitting 1 and the CTO's msgs 9634, 9637 and 9651; gate limb: none graded this modification, it adds no order file)

**Sitting 1 read (`TO-RUN-AR-v32`, `~AQ2`, record `A_RUN_AR_V32.txt`, screenshots READ by the issuer): arm A FAILED.** The board listed `TCK-20261015-944c84f8` on In Progress, the page was intact, and NO failure words showed with the `COMMENTARY_DRAFT_REFUSED` failure standing on the job row. **Cause, read from the code and the ticket item:** the landed page takes the request id from `ticket.report_ref?.request_id` and this ticket never got one (no `report_ref` key, no `report_recorded` event, the row offers "Retry analysis request", which `analysisRequest.ts:646` shows exactly when `report_ref` is absent). **The issuer's cut took `report_ref.request_id` as given and never measured a real unpackaged ticket** (window 2's record already said no `report_ref`): that premise error is the issuer's. **A first correction of mine was itself over-general** (msg 9633 said an unpackaged ticket never carries a request id); the filing's step 4 (`analysisRequest.ts:575-600`, service route `lambda_function.py:1716-1751`) writes it before the packager runs, and the CTO withdrew route A (msg 9637). **Why step 4 did not land in window 2 is NOT read** (the ticket service's log carries no per-route line, and the window's driver read only after the Submit click), and stays an owed surprise row.

**Retry is unusable** (the ticket's creator is `fwd1-staff-r41a`, the helper mints `r41b`; a Retry would file a NEW request under a different principal, `acceptance.py:35`, `:129`, and enqueue generation). **The CTO's ruling (msg 9651):** a small pair for ONE conditional hand-written `report_ref` fixture on that ticket (the shape quoted from the service route's code), arm B on the packaged ticket `TCK-20261014-2965a5e0` in the SAME sitting, applier `0.7.0_AE_CloudOps~IB2` (rule 34). **Sitting 2 is `IRPT_ANLREQ.TO-RUN-AR-v33` (cell AR-v-32, a second order for the same cell), pair `AR_V33_PAIR.md`; the grade names the link as a fixture; the round stays open until a ticket whose step 4 really recorded shows the words (the CTO's msg 9637).** Arm B moves from "owed at run 3" to this sitting because a packaged synthetic ticket exists (Y2's "none" read the FWD-1 tickets only).
