# TCKT_VNEXT: CVO adjudication, the close grades (FWD-2 ticket arm, FWD-4, FWD-5) on the evidence on file

<sweep_watermark>2026-10-21T02:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-21.

Grades by `3.0.0_SA_CVO~DELL2` (dell2), 2026-10-21T02:45Z, asked by the CTO's ADDENDUM 6, PRD v0.8 @4bfe0b7f63 (msg 11762), with
`2.0.0_SA_COO~V2`'s report `deliverables/2.0.0_SA_COO~V2/TCKT_VNEXT_COMPLETION_REPORT_20261021.md` @65e9d97902 (msg 11764). Evidence was
gathered by a read-only search of the ledger, the adjudications and TV2's run folders. The deciding lines below were read by this seat.

## FWD-2, ticket arm: REALIZED

The DONE WHEN reads: "a sign-in belonging to a different firm (a test account at that firm, made for the purpose) tries [the ticket] and is
refused, and the attempt can be repeated on demand".
- **Round 6, `TO-RUN-R6-fn1`:** five direct invokes of the live `opal-ticket-api` with constructed caller contexts.
  - Arm A2 is `tckt-fwd2-probe-b@opal.invalid`, firm `cottonwood`, a test identity made for the purpose. It ran `GET
    /api/scoped/tickets/TCK-20261011-e6433610`, a `49financial` ticket, and got **403** (`L8_PACKET.R6_FN1.md:31-35`;
    `TV2/r6_fn1/A2.json`, `RESULT.json`).
  - Graded then: "AC2 MET for the ticket" (`org/tier1_exec/3.0.0_SA_CVO/deliverables/TCKT_VNEXT_R6_FN1_L9_GRADE_20261011.md`). FWD-2 was
    held open only for the file arm, which has now MOVED to IRPT_ANLREQ C-PACKAGE (v0.8).
- **Limits, stated:**
  - The refusal is by class (a client principal is refused GET whatever its firm), not by the firm fence between staff.
  - It was a direct invoke, not a browser sign-in.
  - The repeat is the saved payloads plus `aws lambda invoke` under a pair. TV2's check re-reads RESULT.json; it does not re-invoke.
- **Why the ticket arm is still REALIZED:**
  - Since Andrew's 2026-10-14 word, the Ticket Center admits Opal users only, so the other-firm actor is exactly a client, and the client
    is refused.
  - Since 2026-10-19, Opal staff file for any firm by his word, so a staff-to-staff firm fence is not what FWD-2 now protects.
  - If Andrew asks to watch it, the five payloads re-run on demand.

## FWD-4: REALIZED

The DONE WHEN reads: "one Opal sign-in files a request, claims it and completes it, on DEV". Read by this seat in
`TV2/r20_run/run_events.txt` (`TO-R20-RV`, on the DEV server `http://localhost:5174`, origin/DEV `38d4f947`):
- `08:13:03Z PAGE ORIGIN (filer) ... http://localhost:5174`;
- `08:18:06Z filer: MEETING TICKET FILED TCK-20261017-da2a1987` with `created_by=tckt-r20-filer-20261017@opal.invalid`;
- `08:20:45Z CLAIM pressed ... assignee=tckt-r20-filer-20261017@opal.invalid`;
- `08:20:54Z COMPLETE pressed ... status=completed`.

`R20_RUN_RESULT.json` records `"completed_by": "tckt-r20-filer-20261017@opal.invalid"`, the filer. One sign-in filed, claimed and
completed its own ticket, and nothing stopped it. Round 18 shows the same on DEV with a separate filer (`TV2/r18_run`). The COO's report
said "unit tests only"; the live run is on file.

## FWD-5: NOT REALIZED on the evidence on file -- one live arm

The DONE WHEN reads: "an Opal person picks the next request to work from the queue alone". The ACCEPT: "reads each request's type and how
long it has waited from the queue itself".
- **Type and wait time are on the row.** The R20 shots show the type ("Meeting Request", "Trade Request") and an age ("(under a minute)",
  "(2 minutes)") beside the created time. That meets the CTO's round-5 ruling that a created time alone does not (DECOMP_R5:74-76).
- **No run picks from the queue.** Every R18 to R21 shot is clipped to one ticket's rows, and every run finds its ticket by id
  (`r20_run.py:256-257`). No artifact shows several open requests of more than one type together, or a person choosing one from them.

**The live arm (for `~V2` to cut):**
- On DEV, file two open tickets of different types, for example one Meeting Request and one Service Request.
- An Opal person reads the board unclipped, with both rows' type and age visible, and claims one from the board without opening either.
- Save the full-board shot, and record which ticket was chosen and from what the person read.
- Remove the synthetic tickets afterwards, on Andrew's standing synthetic-delete word.

```json
[
  {
    "id": "TCKT_VNEXT-D2-C-S19",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-21T02:45Z",
    "one_line": "Close grades on file: FWD-2 ticket arm REALIZED (R6 other-firm 403, by class; repeatable from payloads), FWD-4 REALIZED (R20 DEV: one filer filed, claimed and completed TCK-20261017-da2a1987), FWD-5 NOT REALIZED (no run picks from a multi-type queue; one live arm).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TCKT_VNEXT FWD-2 (ticket arm), FWD-4, FWD-5 DONE WHEN as in PRD v0.8; ADDENDUM 6 close.",
    "world_is": "R6 A2: cottonwood test identity GET of a 49financial ticket 403 (RESULT.json). R20 run_events.txt: tckt-r20-filer-20261017 filed, claimed (assignee itself) and completed on localhost:5174. R18-R21 shots clipped to one ticket; runs locate by id.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R6_FN1.md:31-35; org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r6_fn1/",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/TCKT_VNEXT_R6_FN1_L9_GRADE_20261011.md",
        "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_run/run_events.txt, R20_RUN_RESULT.json, r20_run.py:256-257",
        "org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R5.md:74-76"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade row."
  }
]
```

-- `3.0.0_SA_CVO~DELL2`
