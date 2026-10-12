# One active outsider classed internal — and it reads as a person — 0.7.0_AE_CloudOps~TV2

**archetype:** READ (census)

**Date:** 2026-10-12
**Task Order:** TCKT_VNEXT.TO-READ-R9-ct1.active-internal-rows-by-domain-and-the-twin-dell2 (read at `b7352275da`)
**Status:** COMPLETE — AC1 `CT-COUNT-OK active_internal=21 opal=20 non_opal=1`

---

## The count, first, because it is not zero

```
active internal rows (firmId opal-capital, status exactly 'active')   21
  on an Opal domain                                                   20   (19 opalinvest.com + 1 reserved)
  on a NON-OPAL domain                                                 1   <<<
  of which on a reserved test domain (counted separately)              1
20 + 1 == 21
```

**The one non-Opal row reads as a PERSON.** Digest `1af514167abb`, domain `thewhitelabelcreative.com`,
`userType` null, **firm list ABSENT** — so `_profile_scope` returns *no scope* and the caller reads **every
firm**, with no clamp at all. `updatedAt` 2026-10-01, never on any of the 27 tickets.

Per the CTO's msg 6240 this goes to that seat **before any pair is put**. It is the thing msg 6236 called
"an outsider classed internal estate-wide".

It is **not** the row from round 8. That one was `whitelabelcreative.com` and **disabled**;
this one is `thewhitelabelcreative.com` and **active**. Two similarly-named external domains, two rows.

### Which domains I counted as Opal's, and why

`opalinvest.com` (21 of 56 PROFILE rows, the staff domain, and the domain of the two staff addresses that
actually act on tickets) and `opalinvest.dev` (Opal's tooling domain — the d7/d8/dt battery identities sit on
it, though it carries **zero** PROFILE rows, itself consistent with round 7's finding that those six have no
users row).

A reserved test domain (`.test`, `.invalid`, `.example`) is counted **separately and placed on the Opal
side**: RFC 2606 keeps those unregistrable by anyone, so a row on one cannot be an outside company, and the
CTO's question is whether an *outsider* is classed internal.

`opal.agent` is the agent-serial convention in this repo's commits — not a mail domain, zero PROFILE rows,
so it never enters the count.

---

## Two classification errors of mine, same root, caught before writing

**The root: deciding whether an address is a person by something other than the form of the address.**

1. **Round 7's domain test** (`domain == opalinvest.com` ⇒ person) hid **two** rows, not one: round 8's
   disabled person *and* this active outsider. Both were filed as "non-human or test identity". This order
   already knew the test was wrong and forbade reusing it — rightly.
2. **Today's, in reverse:** I marked non-human on `userType`, which flagged **five staff developers**
   (plain given names carrying `userType "Dev"`) as non-human. That would have put **a person's address
   forward as a twin candidate** — the one thing the order explicitly forbids.

Corrected rule, used throughout: **a plain alphabetic local-part is a person, whatever the userType says**;
non-human needs a marker *in the form* — a hyphenated handle, a tooling prefix, digits, or a reserved domain.
Result: 17 persons, 4 non-human, summing to 21.

---

## A third false `ABSENT`, from a projection I did not check

My first pass reused the round-8 scan and reported **all 21 firm lists as `ABSENT`**. That scan never
projected `allowedFirmIds`. Listing the attributes the scan actually returned exposed it; the re-scan finds
four classes — **18 ABSENT, 1 LIST(6), 1 LIST(1), 1 STRING-OTHER** — matching round 7's independent
per-row `get_item` values row for row.

This is the third time this session that reading a field a query never returned produced a confident wrong
value (the KEYS_ONLY index in round 7, the un-projected scan in round 8's reuse, and this). The habit that
catches it is cheap: **print the attribute set the query returned before trusting any field in it.**

---

## The twin

```
twin candidates (non-human by form, one PROFILE row, active, firm list ABSENT or EMPTY)   2
  3e5db3675c91   opalinvest.com   null   ABSENT   a three-word role phrase ending in "internal"
  686bd73cd5e9   opalinvest.com   null   ABSENT   a service prefix plus a short token
FIRST CHOICE: 3e5db3675c91
```

Preferred because it reads as a **verification identity** rather than a service subject on a live outward
path; presenting a verification handle in a constructed context is the less entangled choice even for a
read-only GET. Both local-parts were inspected specifically so a hyphenated *human* name could not be
mistaken for a handle, and each was confirmed to have exactly one PROFILE row by the service's own
email-index query.

**Excluded:** `35cb8f292b44` (firm list `STRING-OTHER` — and a non-list value is already refused today at
`_profile_scope:391`, my row `S49`) and `00817d2ce20a` (`LIST(len=1)`, not ABSENT/EMPTY). No person is a
candidate.

---

## Sign-in's test, printed

File `infra/aws/opalinvest_dev/lambda/auth-handler/src/auth.ts`, blob
`0dbd69957da0dc8c8133a3a2d9458ee7187b87ba`.

```
106   if (user.status !== 'active') {
107     throw new Error('Account disabled');
255   if (user.status !== 'active') {      // MFA redemption re-check
538   if (user.status !== 'active') {      // refresh; mirrors login's guard exactly
```

**Still tied to the deployed sign-in**, as in round 8 and by the same three reads: live `CodeSha256`
`mzQH2HZl…` equals the source map's artifact hash, and the `src` tree has **0 changed files** since the
recorded deploy commit.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| dynamodb scan ×2 | users, projected, no filter | PASS | the **re-scan** is what every firm list comes from |
| read of the returned attribute set | before trusting a field | PASS | **caught 21 false `ABSENT`** |
| dynamodb query email-index ×2 | one per candidate | PASS | exactly 1 PROFILE row each |
| dynamodb scan | tickets, dates only | PASS | control matched 5 fields for a digest that does appear |
| git rev-parse / sed | auth.ts blob + three line ranges | PASS | quote and provenance together |
| get-function-configuration | sign-in handler | PASS | still tied |
| `r9_checks.py ct-count` | after each correction | PASS | **three refusals first** — all mine |

**AC1 refused the file three times and each was a real defect:** an at-sign in my own prose (an illustrative
agent-serial address); a reserved-domain *third bucket* that broke the required sum; and a dict where the
order specified a list. On the third I read the check's source rather than guess a fourth time.

---

## Decisions Made

1. **Put the non-zero count first**, as the order and msg 6240 require.
2. **Stated the Opal domains and the reason before counting**, and derived them from what the table and the
   repo actually use rather than asserting.
3. **Placed the reserved domain on the Opal side** on the RFC 2606 argument, counted it separately, and said
   so — then fixed the arithmetic when AC1 showed I had made it a third exclusive bucket.
4. **Re-read every class by form**, as ordered, and fixed my own reverse error on `userType`.
5. **Inspected the two candidate local-parts** so a hyphenated human name could not be taken for a handle.
6. **Chose the less entangled twin** and named the alternate with its reason.
7. **Read the check's source** after the third refusal instead of iterating blind.

---

## Files Modified

| File | Commit |
|------|--------|
| `deliverables/r9_ct1/ACTIVE_INTERNAL_ROWS_BY_DOMAIN_20261012.json`, proof_of_spec, this log, TO status | this commit |

No AWS write, nothing invoked, no ledger entry.

---

## Blockers

None owed by this seat. The non-zero count is the CTO's before any pair is put.

---

## Current State

Of 21 active internal rows, 20 sit on an Opal or reserved domain and **one does not**: an active,
unclamped, person-shaped row on an external company domain carrying the internal firm id. Sign-in would
admit it, since its status is `active`; the ticket service admits it too, since a row exists; and its ABSENT
firm list means no firm clamp applies to it anywhere.

---

## Next Steps

1. `1.0.0_SA_CTO~DELL2` rules on the one non-Opal active internal row — before any pair is put.
2. The next release's proof can use twin `3e5db3675c91`; no person's address is ever used.
