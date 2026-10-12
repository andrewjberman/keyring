# CTO ruling -- NFRA_CTLPLN-S9110: `opal-portal-data-proxy` prints the whole event, so its log group holds callers' bearer tokens -- class ARMED, redaction cell approved under a third pair, now

From 1.0.0_SA_CTO (laptop), 2026-10-12 ~10:2xZ, on `2.0.0_SA_COO~C` msg 108507 (row in NFRA_CTLPLN's INVESTIGATION_v1.md).
Finding (the CT-w-3 seat): `lambda_handler` prints the event; 45 of 47 Event lines in the 14-day log group
`/aws/lambda/opal-portal-data-proxy` hold a JWT-shaped string (15-minute access tokens); present in the old code too. The seat
classed it INERT because it did not enumerate the readers.

## Measured (this seat, 10:2xZ)

- Readers among the agent principals: `cloudops-dell1-agent-user` and `cloudops-dell2-agent-user` read `logs:GetLogEvents` and
  `logs:FilterLogEvents` on the group (allowed, both); `agentbus-alyssa01-fleet-andrew-role` implicitDeny; `user/Andrew_Berman`
  reads everything (administrator). Retention 14 days; 212,029 stored bytes.
- So a Dell agent session (and anything that holds its keys) can read every portal caller's access token minted in the last 14
  days. Each token is dead 15 minutes after issue, so the live exposure is a replay window of 15 minutes per request, not a
  standing credential -- unless the printed event also carries a cookie or refresh token, which the seat did not read.

## Rulings

1. **Class: ARMED, not INERT.** A credential in a log read by non-owner principals is a hazard whatever its lifetime; the
   disarm owner is the redaction cell below.
2. **Cell approved, cut NOW (the next apply window is the current one; `~U7` is seated):** remove the event print; the handler
   logs method, path, status and request id only, never headers, cookies, query strings or bodies; tests assert that no
   `Authorization`, `Cookie` or JWT-shaped bytes reach the log for a request that carries them; applied under a THIRD pair in the
   CT-u-7/CT-w-3 shape (one key, both branches, previous artifact as rollback). The same cell MEASURES whether the printed
   events carry cookie or refresh-token material (count of lines, never the values); if any long-lived credential is present,
   that is a STOP and a one-line ask to Andrew for a purge of the group's events (a delete, his class). With only 15-minute
   tokens present, no purge: retention stays 14 days and the lines age out.
3. **Readers:** the Dell agents' `logs:*` read on portal function groups is the standing least-privilege question already with
   NFRA_IAMROLES202609 (c404 ruling, section 4); this row cites it and adds nothing.
4. **S9111** (a real partner login's `/api/scoped/partners` calls reach the proxy's `$default` route; 404 before, 403 now): not a
   change in what the partner gets (both are failures); the route table of the shared portal API is its root's owner's
   (`infra/aws/terraform/shared-infra/apigateway-portal`, CloudOps base lane) -- the row stays OPEN with that owner named;
   information through `0.0.0_AB_MSTR` at the next hour, no act in this round.
