# ENDPOINT (step 2, /endpoint --forward) -- OPAL_TICKET_VNEXT: typed requests, the Analysis Request first

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~16:3xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES. Placement: dell2 (laptop ruling 106359,
placement commit 98fcdce272).

**Brief:** `docs/briefs/d7-ticket-center-request-types-analysis-request-first-brief-20261007.md` @750ec86588 (21,275 bytes; author
`4.0.0_SA_CRO`, generated 2026-10-07, measured 15:15Z-15:4xZ). **Andrew's words:**
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261007_151xZ_TICKET_CENTER_D7_FORWARD_ON_DELL2_ANALYSIS_REQUEST_FIRST_ATTACHMENTS.md`.

**NOT READ (Phase 0 reads the brief only):** the task-order register; the project JSON beyond its row; the purpose document
`docs/architecture/D7_TICKET_VNEXT_PRD.md`; the service's code. Those are the PRD's (L4).

The ids are permanent. This is the first emission; no id is retired.

```
  FWD-1  Alyssa files an Analysis Request with a holdings file and opens the finished report from the same ticket
         DONE WHEN  EXERCISED -- on DEV, an Opal sign-in in Alyssa's role files one request (one household, one account, an Overview report, the default fee)
                    with a real holdings file and follows it to the report opened on the ticket; Alyssa's own first real request grades it again (the organic arm)
         ACCEPT     someone at Opal files the request with the file attached, the report is made from that file without anyone re-typing the holdings, and the
                    finished report opens from the ticket; it fails if anyone forwarded a file by email or chat at any step
         SOURCE     brief I.0 (the candidate thread), O1, O4

  FWD-2  A person at another firm cannot open the request or its file
         DONE WHEN  EXERCISED -- a sign-in belonging to a different firm (a test account at that firm, made for the purpose) tries both and is refused,
                    and the attempt can be repeated on demand for Andrew to watch
         ACCEPT     someone signed in for a different firm tries to open the ticket and its attached file and is refused both times; Andrew can ask to see it
                    done again at any time; a statement that it is refused does not count
         SOURCE     brief O2, finding F7, Part V

  FWD-3  The person filing learns at once when the file will not work, before anyone at Opal sees it
         DONE WHEN  EXERCISED -- a known-bad sheet (several accounts in one file, a totals row, a holding that cannot be priced) is turned back with what to
                    fix, and a known-good sheet goes through; Alyssa's own two test sheets grade it again when she supplies them (the organic arm)
         ACCEPT     a file that today would come back from Alyssa by email comes back from the form instead, saying what to fix; the good file files normally
         SOURCE     brief O3, finding F6 (9 of 31 requests needed a resubmission)

  FWD-4  The person who filed a request can work it and finish it themselves
         DONE WHEN  EXERCISED -- one Opal sign-in files a request, claims it and completes it, on DEV
         ACCEPT     the person who filed a request claims and completes that same request, on any type of ticket; nothing stops them because they filed it
         SOURCE     brief finding F4; Andrew 2026-09-30 ("that rule of no one can file and run their own ticket is nonsensical", all tickets)

  FWD-5  Someone working the queue sees every open request of every type in one place and can tell them apart without opening them
         DONE WHEN  EXERCISED -- an Opal person picks the next request to work from the queue alone
         ACCEPT     an Opal person reads each request's type and how long it has waited from the queue itself, and opens only the ones that are theirs
         SOURCE     brief O6

  FWD-6  When a request asks for commentary, the draft appears on the same ticket for an Opal person, and the ticket shows who sent the final commentary and when
         DONE WHEN  EXERCISED -- one request with commentary asked for: the draft read on the ticket and the sender recorded
         ACCEPT     an Opal person finds the draft beside the report on the ticket, reviews it, and anyone opening the ticket later can tell who sent the final
                    commentary to the advisor and when
         SOURCE     brief O5; NFRA_TRNSPT FWD-10 and FWD-11 seen from the ticket

  FWD-7  A second kind of request is added without rebuilding the Ticket Center
         DONE WHEN  EXERCISED -- a second type, defined by someone who did not build the first, is filed by a person
         ACCEPT     the second request type has its own questions and its own destination, someone files it, and the Analysis Request works exactly as before
         SOURCE     brief O7, finding F6; which type is second is decided after FWD-1 has run, on what the tickets show

  FWD-8  An advisor files an Analysis Request themselves and follows it to the finished report
         DONE WHEN  EXERCISED -- one advisor who has never seen the Ticket Center files a request with their own file, unaided
         ACCEPT     an advisor at a client firm files a request without being walked through it and opens the finished report from their ticket
         SOURCE     brief O8, call B
         WAIT       QUALIFIED: Andrew removed the client "Submit a Request" item in August. The client-facing surface returns only on his explicit word,
                    after FWD-1 has run on real requests. That word is the one wait this outcome carries.
```

## Calls in the brief (Part V), ruled at L2

| call | REC (the brief's) | ruling |
|---|---|---|
| A. One type or two (Alyssa's "YCharts Report" plus "Portfolio Commentary") | one type, "Analysis Request", with her "add commentary?" box | **ONE type.** Andrew named one; one request, one ticket, both results. FWD-6 is the commentary on that ticket |
| B. When advisors file for themselves | Alyssa only until the thread has run; advisor filing by his explicit word | **As REC.** FWD-8 carries it as a qualified wait (above) |
| C. Which type is second | none now; pick after the first type has run | **As REC.** FWD-7 names the bar, not the type |
| D. Account statements as attachments | no; a separate decision when he schedules it | **Out of scope.** Andrew: "TBD ... not currently scheduled" |

## What L4 must settle (carried, not outcomes)

- **The storage read** comes before any store is chosen (purpose document WS-1).
- **The firm fence** on the attachment store follows rule 30, with builder-output addresses.
- **F7 (tenant authorization)** is exercised before any client file is attached. **F4** is removed.
- **One door or two (F5):** the Analysis tab's upload contract, or a new door. REC from the brief: one door.
- **What `IRPT_YCDGEN` needs** to take a request it did not receive from its own page.
- **The unwiped holdings file's readers**, and whether the commentary side ever sees it unwiped (`NFRA_TRNSPT` wipes before its model
  call).
- **In this project:** only WS-1 and WS-2 of the purpose document. WS-3 to WS-6 are named out (brief II.3).

-- 1.0.0_SA_CTO~DELL2
