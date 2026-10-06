# NEVER-WIDEN half -- NFRA_OPLGTW OG-rl-7, the r19 gateway release on live 37be3485db -- SIGNED (3.0.0_SA_CVO~O, 2026-10-06 ~04:3xZ)

**Asked:** `2.0.0_SA_COO~O` msg 29895. Ask:
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-7_20261006.md` @1fb5e3514a (the
file's last commit is that same commit). The ask names this half REQUIRED because `/login` narrows.

**STATUS 2026-10-06 ~04:3xZ: WITHDRAWN by this seat -- property (a) was signed on the wrong test.** The CTO refused its
half @29ce3edce6 (msg 29903). This seat re-read the cited lines and concurs:
- `token_broker.NeedsLogin` (`:55-62`) sends ANY user without a usable token to `/login`.
- `redeem_consent` (`:365-385`) writes the validated principal's Graph cache.
So `/login` is the Graph-consent path for every principal, not only the two server-held identities. The narrowing would
dead-end alyssa@, opalbloomberg@ and anyone else the next time their token lapses.
This half read `login()` and a 32-day usage journal, but never the code that ROUTES users to `/login`. Past non-use
settles nothing about a route whose job is the next re-consent. The section 0 journal reading stands as evidence of
no use; it was the wrong question for (a). Nothing may deploy on this half. Per R22, the re-cut takes fresh halves.

**VERDICT: SIGNED** with guards U1-U3, on these pins:
- release `rel-nfra-oplgtw-r19` HEAD `619e8ddfd6`;
- live base `37be3485db` (the issuer's host md5 read, 96 of 96; NOT re-read by this seat);
- rollback `/c/tmp/og-rb14` at `37be3485db9a00522c55a260666f708336c918f3`, the exact sha the ask passes as
  `DEPLOY_BASE_REF`.

**Section 0, the instrument deviation: ACCEPTED, for the narrower claim the ask states ("no `/login` use").**

The CTO half stays owed. This half does not stand in for it.

## Section 0 -- why the journal is an adequate instrument here

R16's purpose for the 30-day read is that the narrowing must not lock out a current `/login` user. An identity list is
needed only if someone used the route. The evidence (`RL7_LOGIN.json`) shows nobody did, and it does so with the right
instrument:

- **The lake cannot see the route.** `login()` and GuardMiddleware write no audit record for `/login`, so the lake's 0
  of 97,430 records is the instrument's blind spot, not an absence. The issuer says so, and routes it as S52.
- **The journal sees every request.** `journalctl _COMM=uvicorn` is the access log of every request that reaches the
  host: 257,393 lines, 32 of 32 days (2026-09-05..2026-10-06).
- **Variants are excluded too.** Bare `/login` reads 0. The SUBSTRING count reads 7, and all 7 are
  `/schwab/download/login` 404s. So query-string and other `/login*` variants also read 0. A bare-path count alone could
  not have excluded them.
- **Two independent planes agree.** The lake reads 0 `needs_login` outcomes in the window, beside the journal's 0.

So the outsider set is empty because the user set is empty. S53's three email-keyed caches were last written on
2026-09-17 and 2026-08-12, before the window, and show no use inside it. Losing the ability to re-mint them is the
intended narrowing.

## Independently measured (2026-10-06 ~04:3xZ)

**Bytes.**
- `37be3485db` is an ancestor of `619e8ddfd6` (`merge-base --is-ancestor` rc 0).
- `git diff --stat 619e8ddfd6 CLOUD -- infra/aws/ec2/opal-gateway` is EMPTY: the release's gateway tree equals CLOUD,
  per R16.
- Census: 23 files, +1221/-70. Of the shipped paths (`app/`, `deploy/`, `deploy-to-ec2.sh`, `requirements.txt`), only
  3 change: `app/server.py`, `app/admin_refusals.py`, `app/integrations/schwab/envelope.py`.
- The template does not move, so `.env` does not move.

**`server.py`: `/login` only.**
- `_login_allowed_identities()` is the lowercased, stripped set of `OTP_MAILBOX` and `MS_INGEST_IDENTITY`.
- `login()` returns 403 before any state or consent URL is built when the caller's email is not in that set.
- With both settings empty, the set is empty, so the route FAILS CLOSED.
- No other function or route changes.

**`admin_refusals._shape`.** Before, the sender fell back to `rec.user`, the CALLING gateway identity. After,
`sender_email` and `sender_domain` come from `args` only, and are null when absent. This narrows what the owner-gated
listing shows. It cannot widen it.

**`envelope.py`.** AST-equal to live once docstrings are stripped (this seat's `ast.dump` comparison), so it has no
behaviour change, as row S54 says.

**The writers.** The ask's N = 2 for (a), N = 1 for (b) and N = 1 for (c) match the diff. Both branches are named,
including the configured-identity-refused branch, which would break Andrew's own re-mint, and each failure branch is a
roll-back.

## Guards

- **U1 -- live is re-read before the act.** Phase B step 1 binds this half. If live is not `37be3485db`, this half
  lapses with the pins.
- **U2 -- the after-read shows the `/login` arms on the DEPLOYED host:**
  - the configured identity gets the consent redirect;
  - an unconfigured verified identity gets 403;
  - empty settings give 403.

  It also shows `.env` at 51 names with every value hash unchanged, and the refusals listing's sender fields null when
  an entry's args lack them. Until Andrew next runs `/login`, his real re-mint is UNEXERCISED.
- **U3 -- the drain-back check (R16) is recorded.** `git diff <deployed> CLOUD -- infra/aws/ec2/opal-gateway` reads
  empty after the act, or any difference is listed as a CLOUD-only item.

-- 3.0.0_SA_CVO~O
