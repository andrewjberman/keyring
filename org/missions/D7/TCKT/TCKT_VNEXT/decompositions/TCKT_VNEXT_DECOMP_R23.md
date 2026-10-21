# TCKT_VNEXT round 23 -- FWD-4 exercised once on DEV (`2.0.0_SA_COO~V2`, dell2, 2026-10-21)

**Authority:** the CTO's PRD v0.7 ADDENDUM 6 @df3eb8dc43 (the project closes on FWD-2 ticket arm, 4, 5, 7, 10 and 11; "an outcome the evidence on file cannot grade goes to one live arm, cut by `~V2`") and his msg 11766: "cut it now; unit tests cannot meet an EXERCISED bar". **No PRD change.** FWD-4's DONE WHEN (PRD line 47): "EXERCISED -- one Opal sign-in files a request, claims it and completes it, on DEV"; ACCEPT: the person who filed a request claims and completes that same request, on any type of ticket.

## Enrichment list and what each item becomes
| # | item | cell | kind | write surface | risk |
|---|---|---|---|---|---|
| 1 | one synthetic internal sign-in files a ticket of a non-analysis type (Service Request), claims it, completes it, on DEV; the claimer and completer read back equal to the filer; the ticket and the filer row read ABSENT after cleanup | `R23-f4-1` | RUN (the applier `0.7.0_AE_CloudOps~TV2`) | one `opal-tickets` item (created, claimed, completed, then deleted by key); one `opal-users-v2` row (created, then deleted) | WORLD |

## What the cell does
`R23-f4-1`: on the portal DEV served at `http://localhost:5174` (the one DEV origin; the pattern of `TO-R18-RUN`), ONE synthetic filer `tckt-r23-filer-20261021@opal.invalid` (an `opal-users-v2` row, `userType test-filer`, one token of at most 20 minutes, in memory only) opens New Ticket, selects Service Request and firm `cottonwood`, files it, presses Claim on its own ticket, then Complete, with a shot of each step; the whole ticket item is saved BEFORE any removal; after the token `exp` the ticket (by key) and the filer row are deleted and read ABSENT. Where the page offers no Claim or Complete control to the filer on its own ticket, that is shot and reported as a finding and the two calls are made once by HTTPS with the same token, labelled `direct` in the result. The check `R20_CHECKS/r23_fwd4_check.py` holds the record's side (one address as requester, assignee and the actor of the created, claimed and completed events); the shots are the CVO's judgment.

## Chains and fan-out
**M = 1 chain:** {`R23-f4-1`}. **Fan-out: 1 of 1 chain, cap 4, reason:** one applier order (it holds the credentials a worker does not), no worker.

## Rule 24 record
The run's states: (the page offers Claim and Complete to the filer / does not) x (the claim returns 200 / a 403 or 409) x (the complete returns 200 / refuses) x (the ticket and the row removed / left). The check admits only (claimed and completed by the filer, status completed, both removed); a refusal of the claim or the complete on the filer's own ticket is the PRD's FWD-4 failing and is a STOP reported with the status and body, never worked around.
