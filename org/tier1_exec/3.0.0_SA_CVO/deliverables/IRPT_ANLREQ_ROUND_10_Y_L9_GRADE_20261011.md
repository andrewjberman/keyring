# IRPT_ANLREQ round 10, workstream Y -- L9 grade of AR103-y-AC2 (the return census for release 5)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T18:15:32Z. Row IRPT_ANLREQ-D2-S57.
**Input:** `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND10_Y_L8_COMPILE_20261011.md @5b24152a97 (msg 5519)`. **Artifact:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r10/RETURN_CENSUS_IRPT_STATUS.json (blob 83fe9f0ab6)`.

**Verdict: AR103-y-AC2 MET.** Two limits are stated below; neither moves the verdict.

## Limb 1: every row that changes a served answer names the reader that decides on PROD

The census has 16 moved members: 5 change a served answer, 11 are read INERT (10 measured, 1 inferred). This seat read the deciding
line of each of the 5 on portal PROD (37aa1247), not the census's quotation of it.

| member | what changes | PROD reader | this seat's read |
|---|---|---|---|
| owned_requests.py | history page gains a key; each row gains two | `owned-requests.ts` | **Refuses.** Lines 61 and 80 hold exact key sets |
| owned_report.py | the report answer gains one key | `adapt.ts`, by `envelope.ts:193` | Admits. No key-set check on that answer |
| entry.py, served.py | a new refusal reason | `public-status.ts:25` | Admits. Any upper-case reason parses |
| prospect_dates.py | a null-dated section is served | `prospect-dates.ts:41-47` | Admits |

So the census is right that ONE reader on PROD refuses the new answer, the history reader, and that it is the precondition.

**The check for a reader the census did not name.** A search of PROD `src` for the three routes and their reader functions
returns the Investor Reporting page's files and the endpoint module, and nothing else. The ticket page on PROD imports the endpoint
module but has no reader of the report or the history. No unnamed PROD reader was found.

## Limb 2: no INERT member changes what a caller is served

- **acceptance.py (the one inferred row).** Its claim is that no packaged module calls `accept`. Read at the pin: the two callers
  are `export/entry.py` and the submission service, and neither is among the entry's 49 members. The inference holds.
- **loaders.py.** The worker compared the ownership read on both packages with a bucket map derived from the registry, and said
  the live function's environment was not read. This seat read it: the live map holds 3 firms; the one firm the change names maps
  to the same bucket as before, that bucket is not in the canonical list, and no key override is set, so the key is the old key.
- **The other 9** rest on the worker's two-package runs, which this seat did not re-run.

## Two limits

1. **The census read portal DEV at 9ca634c6. DEV is now 3ebc35eb**, which carries the ticket page's reader of the report route, and
   that reader sends the ticket id. The census sentence "no portal caller sends ticket_id" is true of PROD and no longer true of DEV.
   It does not change the PROD precondition. It does mean the pair's after-reads should name the ticket page as a second reader once
   DEV's ticket page reaches PROD.
2. Readers outside the portal repository were not searched, by the worker or by this seat.
