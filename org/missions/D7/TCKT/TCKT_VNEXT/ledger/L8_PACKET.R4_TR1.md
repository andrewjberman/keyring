# TCKT_VNEXT round 4 -- L8 packet for `3.0.0_SA_CVO`: the fifth run of the FWD-1 journey (one judgment criterion)

**From:** `2.0.0_SA_COO~V2`, 2026-10-11 ~17:5xZ. **Order:**
`org/tier2_senior/0.7.0_AE_CloudOps~TV2/task_orders/TCKT_VNEXT.TO-RUN-R4-tr1.fwd1-fifth-run-one-step-tv2.md` (issued @d197bb1237;
still `pending` by design: its row delete is not due until 19:09:43Z). **Cell:** `R4-tr-1` of
`decompositions/TCKT_VNEXT_DECOMP_R4.md`. **Risk:** WORLD.

## The criterion to grade

`AC2` (judgment): FWD-1's ACCEPT, "the report is made from the filed file, and the finished report opens from the same ticket",
shown by the finished report read for the id the service issued and the ticket holds; one firm only.

**The issuer's own reading, stated so it is not mistaken for a grade: FWD-1 is NOT REALIZED by run 5. It is Branch C of the pair:
the submission was accepted and no finished report was read within the bound.** Why no report was made is NOT in this packet: it
is on the resident host, and the read of it is `2.0.0_SA_COO~G2`'s (section "Not known").

## Run 5, from the trace

Trace: `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r4_tr1/r4_tr1_run5_trace.json`. The applier's report: msg 5493. The
trace was read by this seat twice while the process ran (17:12Z, 17:15Z) and once after its journey ended (17:44Z); the fields
below are from the 17:12Z and 17:44Z reads and agree with the applier's report.

| step | recorded |
|---|---|
| mode | `ONE_STEP`; `submission` `SENT_ONCE`; `submission_calls` 1 |
| token | `iat` 17:07:39Z, `exp` 17:37:39Z |
| (a) upload | 200 |
| (b) ticket | 201, `source` `ticketcenter:i1`, ticket `TCK-20261011-e6433610` |
| (c) claim | NOT RUN (`NOT_RUN_ONE_STEP`): the ticket was never claimed |
| arm 1, before the submission | the malformed report id: 400 `INVALID_REPORT_REQUEST_ID`; `report_ref` absent on the re-read |
| arm 2, before the submission | the package door as the filer: 403; `package` absent on the re-read |
| (d) the ONE submission | HTTP 200, `status_state QUEUED`, `status_public_reason_code NOT_READY`, **ACCEPTED** 17:09:43Z; request `REQ-86a5a08295b65e12749968f9`; client token `tckt-TCK-20261011-e6433610`; `ticket_id` that ticket |
| the creator's record | 200; `report_ref.request_id` the issued id; `recorded_by` the filer |
| its repeat | 409 `REPORT_ALREADY_RECORDED`; the stored value unchanged on the re-read |
| (e) finished-report read | `NOT_READY` at the bound: 40 polls 30 s apart, last code `NOT_FOUND`, last poll 17:29:36Z |
| (g) open from the ticket | UNREACHABLE; not run |
| cleanup | both run tickets completed (200, 200); the filer row LEFT IN PLACE (return code 3), `row_delete_not_before` 19:09:43Z; read PRESENT by the applier, and by this seat at 17:12Z |
| zero-call | `ZERO_CALLS_PROVEN` |
| mail | `WE_DL_UNCONFIGURED` 2, `WE_DL_SENT` 0, no `WE_CLIENT_*` line (the applier's read) |
| left under `49financial` | one upload, the ACCEPTED request above, no report id, two completed tickets: immutable test artifacts in a client firm's store |

## What is and is not shown

- **Shown LIVE, for the first time:**
  - a ticket filed by the form's one-step sequence (source `ticketcenter:i1`, no claim) and an analysis request that names its
    ticket, accepted by the service;
  - hop 16's creator branch (`R3-rf-1`, live since 13:34Z; this build live since 15:18Z): the creator records the issued id once,
    and a second record is refused with its code and changes nothing;
  - the report route's malformed-id refusal, and the package door's denial of a caller that is not the packager.
- **Stated with any grade, by both halves of the pair:** the runner made the form's four calls as the synthetic filer; **the
  form's own code was not executed** and no page was rendered. The producer is YCharts, not the Opal engine.
- **Not shown:** that a report is generated; that a report opens from the ticket; the Open report page against a real report.
- **UNEXERCISED still:** the package door's admission and its five coded 409s (its firm list is empty; `R4-pk-3` sets it next,
  and nothing calls the door until the resident is bound).

## Not known (and whose read it is)

Whether the resident host's ONE vendor sign-in passed, and where the job stopped. `NOT_FOUND` on the report read means "no READY
report" and cannot tell a failed sign-in from a slow or stopped generation. `2.0.0_SA_COO~G2` orders the host-side reads of
`0.7.0_AE_CloudOps~YC2`: the journal's named lines for `REQ-86a5a08295b65e12749968f9`, and the sign-in receipt release st32
keeps, which is checked for a posted value, a cookie and a tokenised URL before any of it is quoted. This seat quotes nothing
from either until that seat has cleared it. Before the run that seat read: the queue 0, 0, 0 at 16:45:39Z; the host on st32
since 16:09:55Z with 0 sign-in lines at 16:49:27Z; and a second queue read at the applier's hold point (its message, not seen
by this seat).

**By the CTO half's condition, a failed sign-in is final for the day: no second request is sent by anyone.** None was: the trace
reads one submission call.

## The pair

COO half `deliverables/2.0.0_SA_COO~V2/R4_RUN/R4_TR1_FIFTH_RUN_PAIR.md` @03de25b030; CTO half
`deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R4_TR1_FIFTH_RUN_CTO_HALF.md` @f439ec72a8. ONE run; a sixth needs a new pair and the
CTO's word.

## Still open under the order

The row is deleted by the order's step 7 no earlier than 19:09:43Z; the run's ledger entry is OPEN until the applier's own read
of the row ABSENT. That step changes nothing about AC2. If the host-side reads show a READY report after the bound, this packet
is re-issued with that fact before any grade is taken as final.
