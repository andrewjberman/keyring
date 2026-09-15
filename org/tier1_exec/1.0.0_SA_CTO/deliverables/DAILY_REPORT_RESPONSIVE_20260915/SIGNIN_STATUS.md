# Authenticated Gateway sign-in repaired

**Current status, 2026-09-15T04:05Z:** APPLIED and EXERCISED. Under CTO
Msg96866 and Msg96877, this exact seat applied the approved saved SG-only
plan through safe-apply. Both egress rules are verified and the SG-only
re-plan has no changes. Andrew confirms "Report loads"; CloudWatch records
one post-apply authentication success, and the delivered callback log has
302 with no authentication error. See `ALB_EGRESS/CLOSEOUT.md` for the
bounded evidence and known deliberately unapplied WAF description drift.

The following is the preserved pre-fix diagnosis and source-commit history;
its statements about the missing rule and base CTO apply ownership are
superseded by the completed repair above.

Measured 2026-09-15T03:28Z by `1.0.0_SA_CTO~A`, following Andrew's report
that both `https://mcp.opalinvest.dev/sprint` and the root return HTTP 500.

`SIGNIN_DIAGNOSIS.json` records the live evidence. At 03:24:55.786498Z the
ALB logged `/oauth2/idpresponse` with status 500, target status `-`, action
`authenticate`, and `AuthTokenEpRequestTimeout`. The request never reached
the Gateway. Fresh unauthenticated requests to root and `/sprint` redirect
to Microsoft (302). The Gateway target group is healthy.

The live ALB security group `sg-02571ff2f33d2f9d4` still allows only TCP 8080
to `172.31.0.0/16`. The previously approved outbound TCP 443 rule has not
landed. Base CTO retains the ALB apply route; current evidence and an apply
status request were delivered at 03:27:15Z, 03:28:52Z and 03:32:16Z. No
additional user approval was requested. This seat has not changed the ALB.

## Report source follow-up

MSTR Msg96861 independently validated the published report at seven widths
and all eight desktop diagrams. It was acknowledged and the exact inbox
file archived after processing. That validation excludes live sign-in.

Base CTO Msg96860 at 03:26:16Z resolved the source ownership route: commit
exactly the two Gateway files with the canonical audited
`GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL`, maintaining exact-seat author.
The checked-in hook documents this mechanism. Eight Gateway tests passed
again and the scoped commit was attempted with the reason in its message.

That commit failed because `.git/index.lock` was held by another live writer:
`git.exe` PID 32684, author `3.0.0_SA_CVO`, parent 34312, started 03:22:47Z;
child `env.exe` PID 7940. The lock had the same modification timestamp.
CVO was notified at 03:32:13Z to complete or unwind its own commit. This
seat did not delete the lock or stop the writer. Msg96860 remains in the
unread root until its requested commit actually lands; ACK was delivered.

Update 2026-09-15T03:37:49.006783+00:00: the writer finished and the lock cleared. The exact-two-file
source commit landed at `ee268aa92af9f96c7f0d236dc0a3c6d0b4713df2`; repository author and pathset were verified.
See `GATEWAY_SOURCE_COMMIT.md`. The previous pending source-commit route is closed.
No Gateway deployment, CLOUD push or SITEZ merge was performed. The existing
report publication and tested bytes remain unchanged.
