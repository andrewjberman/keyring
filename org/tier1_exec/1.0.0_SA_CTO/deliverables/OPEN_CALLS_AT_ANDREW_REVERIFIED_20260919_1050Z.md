# OPEN CALLS AT ANDREW -- **RE-VERIFIED**, `1.0.0_SA_CTO`, 2026-09-19 ~10:5xZ

**Why this record exists:** I have printed *"RESERVED cards at Andrew -- five, all unruled"* in **eight
consecutive tick logs** without running the `/open-calls` step that skill calls its own most damaging failure:
**verify each candidate is still open.** I ran it this tick. **Two of the six items I was carrying were wrong.**

---

## ⛔ CORRECTION 1 -- A CARD I WAS ABOUT TO FILE IS **WITHDRAWN**; ANDREW RULED ITS CLASS YESTERDAY

For three ticks I carried *"one card to Andrew, notification-grade"*: `IB-rtf-9`'s `K1b` is **the first binding
of a real advisor's key (`abby_horton`) to a `.test` principal** -- `0 of 11` `opal-partner-49financial` rows
bind that advisor today -- and he approved *"a bounded test principal"* without knowing that shape.

**MEASURED THIS TICK:** `0.0.0_AB_MSTR~Z` recorded an Andrew-direct on **card 6**, 2026-09-18 ~20:10Z
(@`ced1f5f84d`), **VERBATIM:**

> *"Dont get in the weeds with these, they are all test accounts, and we have mfa now anyway"*

⛔ **THAT IS A RULING ON THE CLASS MY CARD BELONGS TO, AND RAISING IT WOULD BE PRECISELY "GETTING IN THE WEEDS
WITH A TEST ACCOUNT."** **WITHDRAWN -- not filed.**

⚠ **I considered the narrow reading and rejected it on the merits, not on deference.** His subject was portal
test logins and rotation; mine is a test login carrying a **real advisor's book**, which is a different
property. But the properties that would make it more than a test account are **all absent by construction**:
`firmRole`/`advisorRole`/`advisorName` are deliberately omitted, the principal is deleted at round close
**verified by a failing read**, and the interval is bounded at **15 minutes** past the deletes (plus the
refresh-refusal I bound in my `IB-rtf-9` half). ⭐ **So the thing my card would have asked him to look at is
exactly the thing he said not to look at, and the only honest move is to decide it myself** -- which the
`/open-calls` skill says in terms: *"If you find yourself listing a decidable item, the finding is that you
should DECIDE it."*

## ⛔ CORRECTION 2 -- **"ALL FIVE UNRULED" WAS FALSE FROM ~06:3xZ, AND I HAD READ THE RULING MYSELF**

**Card 1 (the root `delete-bucket-policy` on the two LGIC firm buckets) HAD ITS ROUTE RULED THIS MORNING.**
Andrew-direct ~06:3xZ, recorded by `2.0.0_SA_COO~B` (`ANDREW_DIRECT_20260919_063xZ_STEP4_..._THEN_PROCEED.md`),
**VERBATIM:** *"i cant get to the console right now, i am remote. have an AE deal with it. if they cant for
whateve rreason, proceed and note it for later."*

⛔ **THE CARD IS NOT CLOSED -- the act still needs him at a console -- BUT "UNRULED" WAS WRONG, AND I KNEW IT.**
I acked that message, wrote **ADDENDUM 1** to my own `IB-rtf-5` sign-off half about it, and printed *"five
RESERVED cards, all unruled"* **in the very same tick log.**

⭐ **THE SHARPEST VERSION OF TONIGHT'S RECURRING CLASS: I was not ignorant of the ruling -- I had ACTED on it,
in the same document, in the same hour, and the SUMMARY LINE BESIDE MY OWN ANALYSIS STILL SAID UNRULED.**
⛔ **A STANDING STATUS LINE IS A CARRIED COUNT, AND A CARRIED COUNT GOES STALE EVEN AGAINST THE BODY OF THE
DOCUMENT IT SITS IN. Nothing checks a log against itself.**
**BAR ON MYSELF: the RESERVED line is re-derived from the card set each time it is printed, or it is not
printed. COST: the verify step the `/open-calls` skill already requires. NON-APPLICATION: none.**

---

## THE CARD SET AS IT ACTUALLY STANDS -- **5 items, 1 with a ruled route**

| # | card | state |
|---|---|---|
| 1 | **Root removal of the two LGIC firm buckets' access policy** (step 4; the only remaining gate on `IB-rtf-5`) | ⚠ **ROUTE RULED ~06:3xZ**, act OPEN -- AE attempted, `AccessDenied` on every held identity (the measured expectation: only the bucket owner's root escapes a policy denying every principal, and root is deliberately outside the exemption set). **Parked as "Andrew at the console when next present", with an owner and an un-park condition. NOT a defect.** |
| 2 | **Identity/data administrator for the Gateway** | OPEN -- blocks `G-C` -> `OG-v-4` |
| 3 | **Sprint audience VALUE** | OPEN -- wildcard `"*"` is NOT authorized |
| 4 | **`FWD-4` / whether `ANDREW_CARD.md` has been read** | OPEN -- stays APPLIED, **NOT REALIZED** |
| 5 | **Portal-paths grant VALUE** | OPEN, carried -- *"no rush"* approved |

⚠ **CARDS 2-5 ARE CARRIED FORWARD FROM PRIOR SESSIONS AND WERE NOT INDIVIDUALLY RE-VERIFIED THIS TICK.** The
sweep that caught cards 1 and 6 was a census of Andrew-direct records committed since 2026-09-18 midday; it
would only surface a ruling recorded in that window under that naming convention. ⛔ **So this table is
BETTER than the line it replaces and is NOT a clean bill: a ruling recorded elsewhere, or by another seat
under another name, would still be invisible to it.** Stated so the next reader does not inherit a
confidence this sweep did not earn.

**Terminology, on his own correction:** the act in card 1 is **"remove the bucket's access policy"** -- never
the bare AWS verb. The buckets themselves stay exactly as approved @`af794c77e3`.

**PUSH STATE at write time:** LOCAL; `origin/CLOUD` `4290315df9` (`ls-remote` read this tick).
