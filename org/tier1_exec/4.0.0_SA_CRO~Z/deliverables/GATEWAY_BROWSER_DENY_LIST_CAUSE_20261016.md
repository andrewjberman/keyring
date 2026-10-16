# Why /sprint and /rivalfunds answer "this account is on the deny list" -- cause, 2026-10-16

**By:** `4.0.0_SA_CRO~Z`. **Asked by:** `2.0.0_SA_COO~MP` msg 35193, on Andrew-direct ~18:5xZ. This is a read-only
investigation: no record was written or changed.

## Answer

The deny is working as designed. It was triggered today. At ~11:22Z the operator act OG-mg-1 Phase B made Andrew's
principal and the Bloomberg account's principal RESTRICTED profiles. The C2 contract writes an `email_deny` record for every
principal made restricted, in the same operator transaction (`NFRA_OPLGTW_PRD.md` C2: "a principal made restricted also
gets an `email_deny` record"). The browser routes that know the caller only by the ALB email refuse a denied email before
anything else (`app/server.py:206-229`). That guard now covers `/login`, `/sprint*`, `/rivalfunds*` and `/yearinreview*`.

## Measured (live `gateway-access-state-table`, us-east-1, ~19:0xZ, GetItem and Query only, nothing written)

| Email | email_deny record | principal_profile |
|---|---|---|
| `andrew@opalinvest.com` | **active** (oid 2e21f8e5-...) | `restricted`, revision 1; operator_audit at 2026-10-16T11:22:29Z, same OG-mg-1 halves, "Phase B GO msg 34954" |
| `opalbloomberg@opalinvest.com` | **active** (oid 517aa5ee-...) | `restricted`, revision 1; operator_audit at 2026-10-16T11:22:55Z, "Phase B GO msg 34954", never-widen ask OG-mg-1 |
| `alyssa@opalinvest.com` | **active** (oid ad037ea5-...) | `restricted`, revision 4 (restricted since 2026-09-27) |
| `menachem@opalinvest.com`, `andrew@fideles.capital`, `andrew@goldengate.dev` | none | not read |

Key: `access_state.email_deny_key(email)` = sha256 of the salted, lower-cased email. The record is written only by
`ops/schwab_entitlement_admin.py` (`activate` restricted, or `deny-backfill`). The audit row for Andrew reads "OG-mg-1 R1:
Andrew's principal, restricted profile with the contract-maximal Schwab data-grant scope, 13 calendar months".

So whichever of Andrew's Opal accounts the browser signed in with, both are denied. A third Opal account would pass only if
it holds no restricted profile.

## What it means

- Every principal given a restricted Schwab profile loses all four browser routes. This is the C2 rule doing what it says.
  It was written when the email-only routes were `/login` and `/sprint`. `/rivalfunds` and `/yearinreview` joined the same
  guard later.
- That guard has no way to tell "restricted for Schwab data" from "denied the browser". The email record carries no scope.
- Whether the OG-mg-1 never-widen halves named this browser effect, I did not read. Its owner can check quickly.
- Unblocking is a ruling, not a list edit, and this seat makes neither. Two shapes, neither taken:
  - (a) Give the email-deny guard a route class, so a restricted profile is refused only on routes that serve restricted data.
  - (b) Remove the deny records for these principals by an audited operator act. This re-opens what C2 closed, and the
    restricted-data routes would need their own check.
- The decision belongs to the CTO, with `2.0.0_SA_COO~O`, who issued OG-mg-1. It blocks MP-v-2 (a second account served
  /sprint, PRD A2).
