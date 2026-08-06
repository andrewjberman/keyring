# Andrew-direct 2026-08-06 — dual-identity Opal Gateway sessions (site Z / MSTR~Z terminal)

**Channel:** MSTR~Z terminal, site Z. **Recorded by:** 0.0.0_AB_MSTR~Z, same turn.
**Status:** intent recorded; execution GATED on the interactive OAuth leg (Andrew's).

## Verbatim

> "Is it possible to have two differnet terminal sessions active, with each authenticated
> through a different channel?"

> "I would lke to be able to have you as my proxy as andrew@opalinvest.com, but we have
> another long-running session as whatever the opalbloomberg MS account is"

## Answer: YES. Grounded, not inferred.

1. **Client tokens are keyed by SERVER NAME.** `~/.claude/.credentials.json` -> `mcpOAuth`
   is keyed `<serverName>|<urlHash>`. This box ALREADY holds two independent entries against
   the SAME gateway URL: `m365|f0290cd11c5b2644` and `opal|f0290cd11c5b2644` -- same hash
   (same URL), separate accessToken/refreshToken/scope. Two names = two identities, on one
   machine, today. This is existing live proof, not a proposal.
2. **The gateway authenticates PER CALLER.** `app/graph.py:1` -- "Every call uses a specific
   user's delegated token"; `app/config.py:28` -- delegated scopes requested "on each user's
   behalf". The gateway does not pin one identity for tool calls; it acts as whoever OAuth'd.
3. **Per-session isolation exists.** `~/.claude.json` carries a `projects` map (4 scopes) with
   per-project `mcpServers`, so each session can be shown only its own server entry.

## Consequence for tier (a feature here, not a blocker)

`app/tier.py:27-29`: READ_ONLY (default + fail-closed floor) / STANDARD_EMPLOYEE /
MASTER_ADMIN ("andrew@ + systems allowlist"). An Opal Bloomberg identity lands at
READ_ONLY or STANDARD, NOT master_admin -- which is exactly right for a concierge that is
specified read-only everywhere except its own Teams replies.

## What this does NOT separate (honest limit)

Two gateway subsystems use the gateway's OWN server-held delegated token for a FIXED
identity (Andrew), regardless of which client calls: `/otp/fetch` against the fixed OTP
mailbox (`config.py:162-169`) and the ms_ingest path (`config.py:179-182`,
MS_INGEST_IDENTITY). Anything routed through those stays Andrew. The Teams concierge duty
(poll_addressed_teams_messages + replies) does not use them, but "fully separate identities"
would be an overclaim and is not asserted here.

## Why this surfaced today (the catch)

0.0.3_BG is specified as the point of contact on the "Opal Bloomberg" Teams account
(prompt.md:3-6; refs/TEAMS_DUTY.md:1,23-24). The gateway on this box answers `whoami` as
**Andrew Berman / Andrew@opalinvest.com**, and `poll_addressed_teams_messages` takes only
(since_iso, top) -- NO account parameter; its contract returns "the user's Teams chats".
Launching the concierge as configured would have polled Andrew's private DMs as its inbound
surface and replied to colleagues AS Andrew. First launch HELD on that basis.

## Fortunate timing

Today's `opal` -> `opal-gateway` re-key (LD-0382 site-Z leg) ORPHANED the existing token:
the credential key derives from the server name, so `opal-gateway|<hash>` has no entry and a
fresh OAuth is required on next restart. LD-0382 pre-accepted that re-auth; this record adds
the MECHANISM. The reconnect is required anyway, so standing up the second identity now
costs no extra interactive step.

## Plan (execution order)

1. `opal-gateway` -> re-auth as **andrew@opalinvest.com** (this proxy session).
2. Add `opal-gateway-bbg` -> same URL, OAuth as the **Opal Bloomberg** MS account.
3. Scope each to its session via per-project `mcpServers`.
4. Re-point 0.0.3_BG's prompt/refs at `opal-gateway-bbg`.
5. **Acceptance test:** `whoami` on the concierge's server returns the Opal Bloomberg
   account -- the exact check that caught this. Launch only after it passes.

## Needs Andrew (agent cannot do these)

- The Opal Bloomberg MS account UPN, and confirmation it exists with delegated consent.
- Both OAuth flows are interactive browser logins.
