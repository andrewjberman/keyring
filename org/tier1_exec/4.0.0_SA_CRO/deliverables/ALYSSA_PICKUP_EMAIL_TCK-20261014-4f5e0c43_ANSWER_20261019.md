# Why alyssa@opalinvest.com got "Your request has been picked up -- mine" (TCK-20261014-4f5e0c43)

Author `4.0.0_SA_CRO~TCKT` (dell2), 2026-10-19, on Andrew's order relayed by `0.0.0_AB_MSTR~DELL2` msg 11015 (from ms, bus
d0fc6aa6). Research only; nothing changed. M = measured, I = inferred.

## Answer

1. **What request created the ticket: none. It was a unit-test fixture, never a real ticket.** (M)
   - `infra/aws/lambda/ticket_center/tests/test_authz_matrix.py:277-279`: the test submits a ticket titled `"mine"` as the
     fixture user `INTERNAL2 = {"email": "alyssa@opalinvest.com", ...}` (`:105`), then claims it. The ticket lived only in
     the test's in-memory table.
   - `TCK-20261014-4f5e0c43` is absent from `opal-tickets` (35 of 35 rows scanned) and from every `opal-ticket-api` log line in the
     2026-10-14 15:00Z-20:00Z window (paged read).

2. **What triggered the notice: worker `0.9.0_WK_TCKT_VNEXT~41` running that test file directly
   (`python .../test_authz_matrix.py`) at about 2026-10-14 19:36Z (3:36 PM ET), from its own machine.** (M)
   - The claim calls `notify_client_isolated(..., "pickup")` (`lambda_function.py:1658`). On 2026-10-14, the recipient
     was the ticket's stored requester email (`_client_recipients` at 480ba3a237: `return [requester.email]`). So the
     notice went to the fixture's real address.
   - The tests' SES guard (`tests/conftest.py`) applies only under pytest. A direct `python <file>` run skipped it and
     sent through real SES, from `tickets@opalinvest.dev`.
   - The worker filed this itself 29 seconds after the send: surprise row `TCKT_VNEXT-D2-W41-S6`, `surfaced_at`
     2026-10-14T19:37:23Z, BLOCKING/ARMED. The row reads: "my by-path run printed one WE_CLIENT_SENT kind=pickup line with
     a real SES message_id from tickets@opalinvest.dev"
     (`org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md:2443`).
   - The row prints a different fixture ticket id (`TCK-20261014-8279bd23`). The test makes a new random id on every
     submit. One run claims several tickets, so it can send more than one notice; Alyssa's is the `"mine"` one (I: the
     row names one send; the run may have sent others to other fixture addresses).
   - The production ticket API (`opal-ticket-api`) logged nothing between 19:30Z and 19:45Z that day (M), which rules it
     out.
   - CloudTrail cannot confirm or deny this either way: it records no SES send at all, including a known one at
     2026-10-15 21:42:00Z (positive control, M).

3. **Should she receive these at all: no.** (M for the code, I for intent)
   - This email: no. It came from a test and was never a real request.
   - Real "picked up" notices: they are CLIENT-facing ("Your request has been picked up"). They go to the requester of a
     partner-firm ticket. Alyssa is Opal staff: the ticket routing names her as an assignee for service, other and
     analysis requests (`infra/aws/terraform/ticket-center/main.tf:429-450`), not as a client.
   - Since 2026-10-15 (`8398ba291b`, R19-L1), the client notice goes only to an address in `CLIENT_NOTICE_CONTACT_MAP`. That
     map is `{}` live today (read 2026-10-19). So no client notice goes to anyone until a contact row is added.

## Is the leak closed?

- **Disarmed (M):** `bb06ea5777` (2026-10-14 15:58 ET, the same worker) added `tests/_no_live.py`. It blocks every
  SES send in a direct run, and `test_no_live_by_path.py` checks that every file's entry point installs it.
- **Left open:**
  - (a) The row `TCKT_VNEXT-D2-W41-S6` still reads `disposition: UNDER_INVESTIGATION`. No adjudication closes it. Owner:
    `3.0.0_SA_CVO~DELL2`.
  - (b) Test fixtures still use real staff addresses (`alyssa@opalinvest.com`; others in `test_authz_matrix.py`). Any
    future unguarded path mails a real person. Recommendation: fixtures use SES simulator addresses
    (`success@simulator.amazonses.com`), as the `~AQ2` sitting scripts already do. Owner: TCKT_VNEXT's issuer,
    `2.0.0_SA_COO~V2`.
