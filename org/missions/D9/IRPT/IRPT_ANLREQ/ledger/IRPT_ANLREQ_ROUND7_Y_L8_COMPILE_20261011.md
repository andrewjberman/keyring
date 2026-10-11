# IRPT_ANLREQ rounds 5, 6 and 7, workstream Y -- L8 COMPILE: the map, the form's record step, and the report bound to its ticket

Compiled by the issuer `2.0.0_SA_COO~Y2` on dell2, 2026-10-11. Rounds 5 and 6 were single direct-act cells (no packet of their own);
round 7 is two cells. Decompositions: `decompositions/IRPT_ANLREQ_DECOMP_R5_Y.md`, `..._R6_Y.md`, `..._R7_Y.md`.
`python .tools/round-close-check.py --project IRPT_ANLREQ --round 7` after the last merge (1cd9c5c8d4): 9 orders in scope, 8 complete,
proof_ok 8, proof_bad 0, verdict MAY-CLOSE (which order is the ninth was not read).

Claim words: MEASURED = this seat ran or read it; WORKER = the worker's run, not re-run here; INFERRED = said so.

## 1. State at this compile

- **Live service:** irpt-status revision 6, `6idtFvAm...` (MEASURED 13:53Z). NOTHING from rounds 3 to 7 is live on the service.
- **Portal DEV** `cece88f603`: rounds 3 and 6 Ticket Center changes are on it (MEASURED by `ls-remote` after the integrator's receipts).
  UNEXERCISED: no real filing has run the round-6 step. **Portal PROD** `37aa1247ee`: none of it.
- **Thread:** `n`. The map of where it stops: `deliverables/2.0.0_SA_COO~Y2/trace/FWD1_HOP_MAP.md`.
- The source map builds the live bytes (MEASURED: `Y33-DIGEST-OK` at 13:1xZ and again before the last service merge).

## 2. Round 5 -- TO-AR-y-51, the FWD-1 hop trace (read-only; CTO msg 4860)

21 hops: LIVE 8, BUILT_NOT_LIVE 10, NO_CODE 1, NOT_DETERMINED 2 (WORKER; this seat spot-read hops 1, 3, 16 and re-ran the form
check and the proof). THIS SEAT'S DEFECT: the order defined a portal hop as live only on PROD; FWD-1 reads "on DEV". Corrected in the
map's `for FWD-1` column. Read on DEV the journey stops at hops 7, 8, 9, 11, 12, 13, 14, 16. The CTO ruled no closer (msg 4919) and cut:
the attach release to workstream G; hop 16 to TCKT_VNEXT and to this lane (rounds 6 and 7 below).

## 3. Round 6 -- TO-AR-y-61, the one-step form records the request id on the ticket (CTO msg 4946)

- Built: after the analysis post answers, `recordTicketReport(ticket_id, {request_id, revision?})`; a fourth step line; retry re-sends
  and then records. MEASURED: 4 named tests pass; TicketCenter folder 46 pass; tsc rc 0; eslint 0 errors.
- CTO approved (msg 4978); landed on DEV by the integrator as `cece88f603` after TCKT_VNEXT's R3-rf-2 apply was read (msg 5074).
- Stated limits: the refusal line shows the client's raw error text (a follow-on cell, named by the CTO, not cut); NOT RENDERED by
  anyone; a retry answering the SAME request id is INFERRED from the acceptance code, not measured.

## 4. Round 7 -- the report is bound to its ticket (CTO msgs 4955, 4984, 5045)

**TO-AR-y-71 (service), merged @31d02ad19c.** `analysis-report` takes an optional query member `ticket_id`. After the caller is admitted
to the request (owner, tenant, retention: unchanged and first), a request whose acceptance record stores a DIFFERENT `ticket_id` is
refused with the new public reason `REPORT_TICKET_MISMATCH`. Not sent, or none stored: today's answer. A caller not admitted reads the
same answer with a right ticket, a wrong one, or none (a named test).
- MEASURED: 7 named tests pass; `ops/tests` 313 passed (WORKER) / the binding file re-run by this seat; `_contracts` 2 failed and
  `_authz` 4 failed, the base counts (this seat at 089992e785 before the amendments; WORKER after).
- ONE line in another lane's file, by CTO ruling 5045 and with `2.0.0_SA_COO~P2`'s yes (msg 5078): `"REPORT_TICKET_MISMATCH"` added to
  `BOUNDARY_ADDITIONS` in `_authz/served.py`. MEASURED at the drain: `git diff --numstat` of that file reads `1 1`; nothing under
  `infra/aws/lambda/ci/` moved. EIGHT functions package the file (named in the order's AMENDMENT 2); each meets the value at its next
  re-pin, where its pair lists it.
- **The reader census the morning's release lacked:** `deliverables/0.9.0_WK_IRPT_ANLREQ~52/r7/PUBLIC_REASON_READERS.json`, 80 rows
  (WORKER): service 17; portal 31 at PROD, 32 at DEV. No portal RUNTIME reader refuses the new value at either commit. One portal
  contract-set test refuses until a generated list is regenerated (row `IRPT_ANLREQ-D2-W52-S7`), done in the portal cell below.

**TO-AR-y-72 (portal), records merged @1cd9c5c8d4; candidate `wk-IRPT_ANLREQ-51-portal-r7` @5f64f409b0, NOT on DEV.** The Open control
sends the ticket's id; the mismatch shows "This ticket's recorded report belongs to another ticket, so it is not shown." with no
waiting state; the generated reason set carries the new value. MEASURED: 3 named tests pass; TicketCenter 49 pass; tsc rc 0; eslint 0
errors. WORKER: the reason-codes test went from 1 failing to 0.

**THE ORDERING, and it is the morning's failure in reverse (MEASURED by reading):** LIVE irpt-status revision 6 refuses any query
member but `selected_tenant` (`ops/entry.py:164-165` at pin `361c44fa9d`, `UNEXPECTED_OWNED_READ_QUERY`). If the portal candidate
reaches DEV before the service carries AR-y-71, every ticket's Open report read is refused. So: service first, then this portal
change, on a measured read of the live function. Put to the CTO (msg 5099) and the integrator told not to land it on approval alone.

## 5. What is owed, and by whom

| item | owner | condition |
|---|---|---|
| The portal history reader on PROD (release 5's ordering condition) | Andrew's word (a client-facing page) | - |
| Release 5's re-release (packet `deliverables/2.0.0_SA_COO~Y2/release5/NEVER_WIDEN_PAIR_ANLREQ_RELEASE5_RERELEASE_IRPT_STATUS.md`) | this seat, then the CTO half | the row above; the packet must now ALSO carry AR-y-71 (a changed `owned_report.py`, `entry.py`, `served.py`) or state that it does not: it was written for build `Iw3FADFr`, which predates round 7 |
| The count of requests with no stored `ticket_id` (CTO msg 4955) | a laptop read at that release | NOT MEASURED |
| The portal candidate of AR-y-72 on DEV | the integrator, on the CTO's ruling | live irpt-status carries AR-y-71 |
| A rendered read of the form's record step and a retry answering the same request id | on the CTO's word that a fresh request may go | UNEXERCISED |

## 6. Rows of these rounds

`IRPT_ANLREQ-D2-W52-S5` (hop 16, confirmed by this seat's code read), `-W51-S8` (the shared revision helper; accepted by the CTO),
`-W52-S6` (the boundary line; resolved by the ruled grant), `-W52-S7` (the portal contract-set test; resolved on the candidate branch,
which is not on DEV: it stays ARMED until that branch lands).

## 7. This seat's defects in these rounds

- The trace order's wrong definition of "live" for a portal hop; a summary of the trace that left out two stops.
- Two messages refused at 152 words.
- The re-release packet is stale against round 7 (section 5, second row): flagged here, not yet rewritten.
