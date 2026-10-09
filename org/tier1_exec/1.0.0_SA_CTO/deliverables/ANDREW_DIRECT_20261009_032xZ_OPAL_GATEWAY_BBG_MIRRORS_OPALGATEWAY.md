# ANDREW-DIRECT 2026-10-09 ~03:2xZ (1.0.0_SA_CTO~O terminal, site Z) -- opal-gateway-bbg mirrors opalgateway

He gave this in-session at the `1.0.0_SA_CTO~O` terminal, right after
`ANDREW_DIRECT_20261009_032xZ_BLOOMBERG_ACCOUNT_GETS_BLACKDIAMOND_LIST_FEES.md`, which it subsumes.

## His words, VERBATIM AND ENTIRE

> "opal-gateway-bbg should be an exact copy of opal-gateway for now, just make it mirror whatever is on opalgateway for consistency, eventually we will make rules but not yet"

## What it rules, at the width written

| Item | Reading |
|---|---|
| The identity | `opal-gateway-bbg` signs in as `opalbloomberg@opalinvest.com`. `opalgateway` signs in as Andrew. Same URL, different principal. |
| Tools | `opalbloomberg` holds whatever Andrew's principal holds. Andrew's identity is UNSCOPED in `app/identity_scope.py`: it is in neither the seed nor the overlay. So `opalbloomberg` leaves identity scoping. Its `_SEED` entry and its two overlay rows go, and the five-row widening is moot. |
| Data | `opalbloomberg`'s data grants equal Andrew's. This reverses this seat's v2.2 item-2 correction, which gave it no data grant. |
| "for now ... eventually we will make rules but not yet" | Per-identity rules for this account are deferred. The mirror is today's state. It is not a permanent design. |

## Not said

- Nothing about other principals.
- Nothing about the Bloomberg queue (CLAUDE.md: Bloomberg pulls go only through their queue).

## Consequence to measure, not a new ask

An UNSCOPED identity's `/login` consent asks the full `GRAPH_SCOPES` envelope (`identity_scope.py:124`). The current
`opal-gateway-bbg` token was consented under the scoped set. The Microsoft 365 tools may refuse until the Bloomberg account
consents to the wider set. The release's read-back measures this. If they refuse, the act is a fresh sign-in in the BG
seat's window, and it is named then, with its evidence.
