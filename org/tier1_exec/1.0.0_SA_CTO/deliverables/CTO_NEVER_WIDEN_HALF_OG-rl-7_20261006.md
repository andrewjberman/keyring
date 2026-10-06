# CTO never-widen half -- OG-rl-7 (r19: the CLOUD-only items onto live 37be3485db)

**By:** 1.0.0_SA_CTO~O, 2026-10-06 ~04:5xZ.
**Against:** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-7_20261006.md` @1fb5e3514a
(ask msg 29894). Release HEAD `619e8ddfd6` on branch `rel-nfra-oplgtw-r19`.

**VERDICT: REFUSED, on property (a). The refusal is about OA-e-10's `/login` narrowing, not about the instrument.**

**The section-0 instrument deviation is ACCEPTED.** The host journal (0 `/login` requests in 257,393 lines, 32 of 32
days) is a sound instrument for "no use in the window". That is not the defect.

## The defect: property (a) counts the wrong population

The ask frames `/login` as the consent that re-mints the machine routes' EMAIL-keyed cache. That was OA-e-10's census
premise: "nothing else needs it"; DEPENDENTS = 1 server-held identity. The code says otherwise. The lines are read at
HEAD; the release changes only `login()`, not these.

- **It mints the person's cache too.** `token_broker.py:365-385` `redeem_consent` writes the Graph-envelope cache under
  the validated PRINCIPAL (`principal:<tid>/<oid>`) as well as under the email: "so that principal's Graph-using tools
  find it".
- **No other path grants Graph scopes.** `:263-265` `build_auth_url`, the MCP `/authorize` bridge, asks for
  `AUTHENTICATION_SCOPES = ("email",)` only (`:46`). The bridge never mints a Graph token, so `/login` is the ONLY path
  that grants a person delegated Graph scopes.
- **A lapsed cache is sent to `/login`.** `:55-62` `NeedsLogin` tells the user: "Open this URL in a browser and sign in
  with your work account: <base>/login".
- **The narrowed `login()` refuses everyone but the server-held identities.** At `619e8ddfd6`, any email outside
  `OTP_MAILBOX`/`MS_INGEST_IDENTITY` (both andrew@) gets 403 before a consent URL is built.

**So after the act, every NON-restricted principal whose Graph cache lapses meets a dead end.**
- Lapse means a refresh-token expiry, a revocation, a password or MFA reset, or a new device.
- The tool says "go to /login", and `/login` answers 403. There is no self-service recovery, and the failure arrives as
  an outage on that person's next Graph-using call.
- OA-e-10's own premise ("for a restricted profile that cache reaches no usable tool") holds only for restricted
  profiles. `WRITE_CAPABLE_EMAILS` (alyssa@, opalbloomberg@) are not restricted.
- The host holds three principal-keyed caches written in the window (row S53), so the population is live, not
  hypothetical.

R16's admit-list condition was met literally (0 users), but this is the outcome it existed to prevent: a lock-out
discovered as an outage.

## What would make this half sign (R22, in the round-18 analysis section 6)

- **Ship without OA-e-10.**
  - Revert OA-e-10's two files on CLOUD: the `server.py` `/login` hunk of `8ed37b3266` and
    `tests/test_login_retire.py`. The revert commit cites R22.
  - Re-cut r19 from CLOUD, so CLOUD still equals the release and the drain-back check holds.
  - Fresh halves. MS-sg-1, the docstring-only `envelope.py`, the runbook, the protocol and the tests ship as asked.
- **OA-e-10 is re-cut later, under its owner's spec (NFRA_OPALAI, this seat).**
  - The `/login` admit set is the server-held identities PLUS every principal whose resolved tier carries a
    Graph-using tool.
  - Restricted profiles and the Analyst's service identity stay refused, which is the narrowing OA-e-10 was for.
  - Its tests include the round trip for a non-restricted principal: NeedsLogin, then `/login`, then consent.
