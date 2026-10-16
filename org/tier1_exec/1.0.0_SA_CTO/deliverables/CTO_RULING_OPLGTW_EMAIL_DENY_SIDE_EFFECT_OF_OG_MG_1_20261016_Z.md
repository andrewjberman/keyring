# CTO RULING -- the browser deny on Andrew's and the Bloomberg account's emails, a side effect of OG-mg-1 (2026-10-16 ~19:0xZ)

**By:** `1.0.0_SA_CTO~Z`. **On:** CRO~Z msg 35199, `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_BROWSER_DENY_LIST_CAUSE_20261016.md`
@25a55fbecb (live table read ~19:0xZ). It was surfaced by Andrew at COO~MP's terminal ~18:5xZ (msg 35193): `/sprint` and `/rivalfunds` answer
"this account is on the deny list".

## Cause, owned

- At ~11:22Z, OG-mg-1 Phase B made `andrew@` and `opalbloomberg@` RESTRICTED profiles. R1 and R2 are the halves I SIGNED
  (`NEVER_WIDEN_HALF_CTO_OG-mg-1_20261016.md`).
- Contract C2 writes an `email_deny` for every principal made restricted. The email-only browser routes refuse a denied email
  (`app/server.py:206-229`): `/login`, `/sprint*`, `/rivalfunds*` and `/yearinreview*`.
- **My half did not name this browser effect. It was a reachable consequence of the act I signed.** It is a NARROWING, not a
  widening, so no data was exposed, but it cut Andrew off from his own browser apps for about 7.5 hours.

## Ruling

1. **Now: reverse the side effect for the two Opal principals ONLY (shape b).** An audited operator act removes the `email_deny` record
   for exactly `andrew@opalinvest.com` and `opalbloomberg@opalinvest.com`. That is a literal two-key list, and it restores the
   pre-11:22Z state of those two keys.
   - `alyssa@` is UNTOUCHED: her deny predates today (restricted since 09-27) and is intended.
   - The restricted profiles and grants of R1 and R2 stay as signed.
   - Applier: an NFRA CloudOps lane, via `ops/schwab_entitlement_admin.py` or its audited equivalent.
   - Rollback per key: re-write the record (`deny-backfill` for that email).
   - Read-back: GetItem shows each key absent; one browser request per route by each account answers non-deny; Alyssa's record is
     still active.
   - **Halves:** it reverses part of a signed never-widen act, so it carries the same three halves. COO~O cuts the ask now.
     **My CTO half is SIGNED HERE** for exactly this two-key write set, on the read-backs above. It is invalid if the ask names any
     other key.
2. **Durable (shape a): give the email-deny guard a route class.** A restricted profile is then refused only on routes that serve the
   restricted data. That stops any future restricted grant to an Opal-internal principal from denying the browser again. It is a code
   cell for the next batched gateway release under COO~O, with a test that keeps Alyssa refused on today's four routes and lets a
   restricted master_admin through.
3. **Lesson for every never-widen half on a principal:** read the contract's side-writes (C2's `email_deny`) as part of the blast
   radius.
