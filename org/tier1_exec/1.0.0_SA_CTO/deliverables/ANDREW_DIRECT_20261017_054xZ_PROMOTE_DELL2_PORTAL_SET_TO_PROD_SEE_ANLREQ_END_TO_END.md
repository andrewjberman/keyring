# ANDREW-DIRECT 2026-10-17 ~05:4xZ -- promote the dell2 portal work to PROD; see the Analysis Request end to end

- **Seat:** 1.0.0_SA_CTO~DELL2 terminal.
- **Andrew's words, verbatim:** "i want to get all this stuff promoted to PROD, on the portal, are we in position where analysis request type issue is fixed? I really want to see that process end to end"

## What his word covers (read by this seat at 05:4xZ, nothing wider)

His word is the approval for client-facing PROD under CLAUDE.md Agent Autonomy. It covers the dell2 portal work built this session.

1. **Already on DEV, not on PROD:** the following dell2 candidate branches (origin/DEV 4d4dc68cae against origin/PROD fa21a303d8):
   - anlreq-advisor-login-email
   - anlreq-filing-notice
   - anlreq-ticket-commentary-pdf-reader
   - asof-date-only-no-invented-clock
   - irpt-fwd10-partial-history-sentence
   - irpt-series-mirror-contract-031
   - ticket-hop-failure-read-dev
2. **Ticket Center:** cand/dell2/tckt-meeting-form-prod-recut (row 8b35, approved), the Meeting Request form and outcome line. In its place, tckt-meeting-and-trade-form and tckt-meeting-outcome-visibility do not go to PROD.
3. **The revision fix:** TO-AR-y-383, cand/dell2/anlreq-report-ref-revision-string. It goes to DEV and then PROD once built and green.
4. **The Performance tab:** cand/dell2/irpt-49f-performance-template-mount and cand/dell2/irpt-performance-holdings-panels. This word is the approval of row f1bb for DEV. PROD follows after ~C2's C5 read shows Cottonwood served on the build, because that verification is owed by the change itself.

## Not covered (his own earlier words)

- **The Trade Request form:** "we should not push this til we actually have a functioning channel for that".
- **cand/dell2/anlreq-commentary-always-requested:** it was reverted from PROD on 10-15 under CTO ruling msgs 8530 and 8534. It is not re-promoted without a new word.
- **Other boxes' candidates (dell1, laptop):** they are not this box's to promote.

## End to end

Andrew's own filing TCK-20261017-5af976ff already reached READY on PROD. Only the ticket record step was refused ("revision must be a string"). After the fix is on PROD, one Retry on that ticket records the report, and he opens it from Ticket Center. A fresh filing then runs the whole path on the fixed build.
