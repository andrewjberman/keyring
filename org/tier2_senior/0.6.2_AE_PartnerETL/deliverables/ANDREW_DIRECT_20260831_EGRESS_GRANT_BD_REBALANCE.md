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

---

# AMENDMENT 1 (2026-08-31 ~22:1xZ) — the derived one-shot ask is HELD by Andrew

## VERBATIM

Andrew, this session, in response to `/open-calls` CALL 1 (confirm the `cot-rebalancer-runner
--date 2026-08-31` one-shot):

> I will discuss with CTO, hold for further advisory.

## DISPOSITION — HELD, NOT DECLINED

⛔ **The one-shot is NOT authorized and is NOT refused. It is HELD pending an advisory that has not
yet arrived.** The staged command is not fired. No vendor call, no production write.

⭐ **THIS ALSO SUSPENDS THE RELAYED GO.** `1.0.0_SA_CTO` relayed an Andrew-direct GO at
`20260831T185158Z` and instructed *"fire immediately on Andrew confirmation in your session."*
**That instruction is now overtaken by Andrew's own later word.** The sovereign has taken the
question into a discussion with CTO rather than confirming it, so the relayed GO must not be
treated as live in the meantime — latest binds, and the latest is a hold.

## MY READING OF "FURTHER ADVISORY" — STATED, NOT ADJUDICATED

He said *"I will discuss with CTO."* So an advisory is expected to follow that discussion, and it
could plausibly arrive through `1.0.0_SA_CTO`. ⚠ **I am NOT inferring that a subsequent CTO relay
auto-satisfies this hold.** The entire reason this act was held is that a relay from an unregistered
session cannot carry the one gate CLAUDE.md reserves to Andrew's explicit per-use word; a hold
created by that concern is not discharged by another instance of it.

**Therefore: if a post-discussion advisory arrives via `1.0.0_SA_CTO`, I SURFACE IT TO ANDREW rather
than act on it**, and I fire only on his own clear word — unless he tells me otherwise, which is
exactly the standing rule I put to him as `/open-calls` CALL 2 and which is still unanswered.
**Surfacing the ambiguity rather than resolving it in either direction; resolving it in my own favour
and resolving it against myself are both adjudication.**

## STATE UNCHANGED

2026-08-31 bronze remains 0 of 3 feeds; the complete-stamp is ABSENT (re-measured this turn). Cookie
minted `11:33:37Z`, ~10.5h old at the time of the hold. ⚠ **A perishable note, not an argument for
overriding the hold:** that session reaches the ~18.5h age that killed the 06:00Z run at roughly
`06:00Z` on 09-01, and the next scheduled mint is `11:30Z` on 09-01. If the advisory arrives after
that window the recovery run may need the mint to land first. **This is a fact for whoever rules, not
a reason for me to act early.**
