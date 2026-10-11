# TCKT_VNEXT round 3 -- L8 packet for `3.0.0_SA_CVO`: the fourth run of the FWD-1 journey (one judgment criterion)

**From:** `2.0.0_SA_COO~V2`, 2026-10-11 ~12:1xZ. **Order:**
`org/tier2_senior/0.7.0_AE_CloudOps~TV2/task_orders/TCKT_VNEXT.TO-RUN-R3-tr1.fwd1-fourth-run-tv2.md` (issued @2681fcca32; still
`pending`: its second step, the row delete, is not due until 13:19:00Z). **Cell:** `R3-tr-1` of
`decompositions/TCKT_VNEXT_DECOMP_R3.md`. **Risk:** WORLD.

## The criterion to grade

`AC2` (judgment): FWD-1's ACCEPT, "the report is made from the filed file, and the finished report opens from the same ticket",
shown by hop (e) and hop (g) reading the finished report for the id the service issued and the ticket holds; one firm only.

**The issuer's own reading, stated so it is not mistaken for a grade: FWD-1 is NOT REALIZED by run 4. It is Branch C of the pair:
the submission was accepted and no report was read within the bound.** It is the first run to get past the submission.

## Run 4, from the trace

Trace: `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r3_tr1/r3_tr1_run4_trace.json` @80c082777f. The applier's report: msg 4869.
The trace was also read by this seat at 11:47Z while the process was finishing; the fields below agree in both reads.

| step | recorded |
|---|---|
| prechecks | `READ27 27/27` by the new precheck; `irpt-status` `Iw3FADFr`; token `iat` 11:17:00Z, `exp` 11:47:00Z |
| census | 82 routes armed, 0 off-list admits (the applier's report) |
| (a) upload, (b) ticket, (c) claim | 200, 201, 200 |
| (d) submit | HTTP 200, `status_state QUEUED`, `status_public_reason_code NOT_READY`, **ACCEPTED**, request id `REQ-59aa6803901f371b27ffa176`, submitted 11:19:00Z |
| (e) finished-report read | `NOT_READY` at the bound: 40 polls 30 s apart, every one `NOT_FOUND`, last poll 11:38:55Z |
| (f), (g), both report-route arms | UNREACHABLE; not run |
| cleanup | both run tickets completed; the filer row LEFT IN PLACE (return code 3), `row_delete_not_before` 13:19:00Z; the applier read the row PRESENT |
| zero-call | PROVEN (the applier's report; the trace's block read null at 11:47Z, before the process wrote it) |
| mail | `WE_DL_SENT` 0 |
| left under `49financial` | one upload, the ACCEPTED request above, no report id, two completed tickets: immutable test artifacts in a client firm's store |

## What is and is not shown

- **Shown, for the first time:** the submission route accepts the journey's request and issues a `REQ-<24 hex>` id (one instance);
  the runner takes that id from the answer; run 3's `NOT_READY` at hop (d) was this same accepted-and-queued answer.
- **Not shown:** that a report is generated; that a report opens from the ticket; either live arm of the report route's id check
  (hop (f) never ran); the Open report page against a real report.
- **Not known:** what happened to the job. `NOT_FOUND` on the report read means "no READY report", and cannot tell not-yet-generated
  from failed or never-started (`R2_RUN/REPORT_READ_REFUSALS.md`, PROPOSED). This seat counted, from 11:18:30Z to 11:48Z, 3
  invocations of `irpt-ycharts-generate` (all within 12 s of the submission), 0 of `irpt-export-render` and 47 of `irpt-status` (the
  polls). Generation runs on the resident host, which that count does not see. The request id is with `2.0.0_SA_COO~G2` for its
  job state (msg sent 11:48Z); no answer yet.
- The pair: COO half `deliverables/2.0.0_SA_COO~V2/R3_RUN/R3_TR1_FOURTH_RUN_PAIR.md` @213c8eae94; CTO half
  `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R3_TR1_FOURTH_RUN_CTO_HALF.md` @3b30b56702. ONE run; a fifth needs a new pair.
- The CTO half's own note: this run takes the YCharts producer path, so even a READY report here would not exercise the Opal-made
  report.

## Still open under the order

The row is deleted by the order's second step no earlier than 13:19:00Z; the run's ledger entry is OPEN until the applier's own
read of the row ABSENT. That step changes nothing about AC2.
