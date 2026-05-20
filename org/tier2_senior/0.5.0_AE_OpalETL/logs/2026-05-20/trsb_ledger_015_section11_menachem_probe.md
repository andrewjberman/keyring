# TRSB_LEDGER.015 — TRSB section 11 Menachem Phase-0 probe

**Date:** 2026-05-20
**Agent:** 0.5.0_AE_OpalETL~B
**TO:** `org/tier2_senior/0.5.0_AE_OpalETL~B/task_orders/TRSB_LEDGER.015.ae-section11-menachem-probe.md`
**Type:** non-mutating probe — no writes, no SES changes, no deploy.

---

## Current State

- **TRSB_LEDGER.015 COMPLETE.** All three Phase-0 facts (P1/P2/P3) established by direct
  read. Findings routed to COO~B (CC CTO~B). Both conditional follow-ons turn out NOT
  needed — see P2 + P3.

## P1 — andrew@opalinvest.com trade-users row (verbatim)

Direct `aws dynamodb get-item` on table `trade-users` (key schema: `email` HASH;
confirmed via `config.py` `USERS_TABLE='trade-users'`). Full row, every attribute,
DynamoDB-typed verbatim:

```json
{
  "active":     { "BOOL": true },
  "created_at": { "S": "2026-01-06T00:00:00Z" },
  "email":      { "S": "andrew@opalinvest.com" },
  "groups":     { "L": [ { "S": "approvers" }, { "S": "executors" } ] },
  "name":       { "S": "Andrew Berman" },
  "role":       { "S": "dev" }
}
```

6 attributes: `active` (BOOL), `created_at` (S), `email` (S — HASH key), `groups`
(L of S — `["approvers","executors"]`), `name` (S), `role` (S = `dev`). No other
attributes. §11-A (.016) replicates this exact shape for menachem@ — `email` ->
`menachem@opalinvest.com`, `name` -> `Menachem` (matches the portal-auth profile name),
`created_at` -> the seed date; `active`/`groups`/`role` identical.

## P2 — SES verification state

`aws ses get-identity-verification-attributes` + `aws sesv2 get-account`:

| Identity | VerificationStatus |
|----------|--------------------|
| `opalinvest.com` (domain) | **NOT a verified identity** — absent from the response (no domain-level verification) |
| `andrew@opalinvest.com` | Success (verified) |
| `menachem@opalinvest.com` | **Success — already verified** |

SES account: `ProductionAccessEnabled: false` -> **SES is in SANDBOX**; `SendingEnabled: true`.

**Answer to "does section 11-B need a verification step": NO.** `menachem@opalinvest.com`
is already a verified SES identity. SES is in sandbox (can send only to verified
identities), but menachem@ is verified, so the trade-workflow-handler can send execution-
path email to menachem@ without any new verification action. The section 11-C SES step is
effectively already satisfied — .017 can add menachem@ as a recipient directly.

## P3 — portal-auth account

`menachem@opalinvest.com` **HAS** a portal-auth account. Lookup method: scan of the
portal-auth users table `opal-users-v2` (the live v2 table — keyed `PK`/`SK`, `PK` =
`USER#{userId}`; the older `opal-users` is email-keyed and carries `firmId: "null"`).

menachem@ `opal-users-v2` row (passwords redacted):
- `PK`: `USER#usr_6ce8f8fdb8de` / `SK`: `PROFILE` / `userId`: `usr_6ce8f8fdb8de`
- `email`: `menachem@opalinvest.com` / `name`: `Menachem`
- **`firmId`: `opal-capital`** — resolves to the opal-capital scope (matches andrew@'s v2 row)
- `role`: `admin` / `status`: `active` / `tier`: `advisor`
- `lastLogin`: 2026-05-18T20:54:50Z (active account); `migratedFrom`: opal-users

**Answer: YES — menachem@ has a portal-auth account resolving `firmId` to `opal-capital`.**
section 11-D (portal-auth provisioning) is NOT needed; nothing to surface to Andrew for
account creation.

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `aws dynamodb describe-table` / `get-item` (trade-users) | OK | P1 — full andrew@ row. Key schema confirmed `email` HASH. |
| `aws ses get-identity-verification-attributes` + `aws sesv2 get-account` | OK | P2 — menachem@ verified; SES sandbox. |
| `aws dynamodb describe-table` / `get-item` / `scan` (opal-users, opal-users-v2) | OK | P3 — menachem@ portal-auth account confirmed in opal-users-v2, firmId=opal-capital. comp-* N/A — DDB rows + SES are not graph-modeled (probe TO). |

## Next Steps

- `[2.0.0_SA_COO~B]` Findings routed (CC CTO~B). On these: GO section 11-A (.016 — seed
  the menachem@ trade-users row, P1 shape) + section 11-B (.017 — executed-email recipient;
  P2 says no verification step needed). section 11-D is NOT needed (P3 = account exists).
- `[0.5.0_AE_OpalETL~B]` Standing by for the .016/.017 GO.
