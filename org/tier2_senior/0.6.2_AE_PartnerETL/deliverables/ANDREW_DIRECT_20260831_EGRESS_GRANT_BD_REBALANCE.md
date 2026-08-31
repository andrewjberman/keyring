# ANDREW-DIRECT 2026-08-31 — scoped egress grant, BD rebalance endpoint

**Receiving seat:** `0.6.2_AE_PartnerETL` (Cottonwood partner ETL)
**Channel:** Claude Code terminal, this session, mid-turn
**Recorded:** 2026-08-31T15:54Z — same turn as receipt, per `org/XXX.md`
"Andrew-direct instructions — RECORD + BROADCAST, same turn"

## VERBATIM

Message 1:

> i want you to check the black diamond rebalance endpoint, there was a spelling error in opal
> conservativeo or conservatove, something like this, for cottonwood. find it.

Message 2 (after I surfaced that a vendor call needs his per-use word):

> you have egress, go get it

## SCOPE — as received, NOT adjudicated

The grant is recorded exactly as spoken. I do **not** widen or narrow it. Read plainly it
authorizes vendor egress to the Black Diamond **rebalance** endpoints for the Cottonwood firm,
for the purpose of locating the misspelled model name.

⛔ **It is NOT a standing grant.** `CLAUDE.md` — "NEVER call an external vendor API without
Andrew's explicit per-use word — availability is not authorization." A future seat reading this
file has **no** egress by virtue of it.

## STATE — GRANTED, **NOT EXERCISED**

**I did not spend the egress.** The answer was reachable without a vendor call: the
`cot-rebalancer-runner` daily lands the vendor's raw JSON **byte-for-byte** (Rule 17a, bronze is
raw) into `s3://opal-data-assets/blackdiamond/cottonwood/bronze/rebalancer_models/{date}/`, which
is Opal-owned infrastructure and inside ordinary autonomy. Every finding below is read from those
landed vendor bytes.

Stated so a later reader cannot infer exercise from authorization: **0 vendor calls made under
this grant.**

## WHAT THE GRANT WOULD HAVE HIT, HAD I SPENT IT AT RECEIPT

It would have **failed**. The Cottonwood BD session cookie was dead from before 06:00Z until
11:33:37Z; a live pull during that window dies at the same `mint_rebalancer_bearer` call that
killed today's scheduled run. The cookie is fresh as of 11:33:37Z, so the grant is spendable
**now** — see the outage record in the same-turn broadcast.

## FINDING THE GRANT WAS ISSUED FOR — ANSWERED

Misspelling: **`Opal Long Term Conservatiove`** (vendor-side typo for *Conservative*).
GUID `c973839d-c476-4e0f-a43f-40d22526aae5`, `rebalanceModelType=Strategy`, 0 accounts,
0 rebalance assignments.

**ALREADY CORRECTED VENDOR-SIDE.** Same GUID, renamed to `Opal Long Term Conservative` in a
24-hour window between the `2026-08-07T06:00:43Z` and `2026-08-08T06:00:44Z` landings. Verified
present-correct on all 13 landed dates sampled through `2026-08-30T06:00:44Z`.

Author: `0.6.2_AE_PartnerETL`
