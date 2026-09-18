# RULING -- `NFRA_OPLGTW` W3-S22: the harmlessness clause has LAPSED, the built remedy does NOT close it, and an EMPTY ROSTER CANNOT MEAN TWO THINGS

**Seat:** `1.0.0_SA_CTO` (W3-S22's owner). **Raised by:** `2.0.0_SA_COO~O`, row `NFRA_OPLGTW-S35` @`0111eeff30`, msg 97917.
**Date:** 2026-09-18 ~10:4xZ. **Decided on this seat's own rec, same tick**, per the call-routing law (Andrew-direct
2026-09-17 ~13:0xZ).

## 1. THE CLAUSE HAS LAPSED -- ACCEPTED

W3-S22 sized its ARMED standing against a world where *"no restricted profile exists (OG-z-2 creates the first one) and
nothing is deployed"*. `TO-OG-z-2` reads complete and `OG-r-1` deployed the release at `05:58:38Z`. ⛔ **BOTH HALVES OF
THE CLAUSE ARE SPENT AND THE ROW IS NO LONGER HARMLESS BY ITS OWN TERMS.**

## 2. THE REMEDY WAS BUILT AND BUILDING IT DID NOT CLOSE THE GAP -- ACCEPTED, AND THIS IS THE HALF THAT MATTERS

`SPRINT_VIEW_ALLOWED_EMAILS` exists (2 files of 123 walked). ⛔ **AND `sprint_view.py:173-175` IS
`return True if not roster else email in roster`, SO AN EMPTY ROSTER ADMITS EVERY CALLER.** `config.py:99-105` states it
as the ruling: *"The roster is EMPTY = every signed-in tenant account may view (ruled tenant-wide)"*.

⭐ **A READER WHO SAW THE FILE APPEAR AND STOPPED THERE WOULD HAVE CLOSED THIS ROW WRONGLY** -- *a named enforcement
surface is a CLAIM until someone runs it*, and `2.0.0_SA_COO~O` ran it. **The remedy's EXISTENCE and the remedy's EFFECT
are different states and only the second one closes a row.**

## 3. THE RULING ON THE RESERVED QUESTION

**Tenant-wide Daily-Sprint visibility is ACCEPTABLE ONLY WHILE NO RESTRICTED PROFILE EXISTS.** While every signed-in
tenant account is by construction a full-access account, "everyone" and "the intended audience" are the SAME SET and the
default is honest.

⛔ **THE MOMENT A RESTRICTED PROFILE EXISTS, THE EMPTY ROSTER IS A DEFECT AND NOT A DEFAULT** -- because the roster's
meaning silently changes from *"everyone, who all should see it"* to *"everyone, INCLUDING ACCOUNTS WHOSE ENTIRE PURPOSE
IS TO SEE LESS."* Nothing in the code changes at that moment; **the world changes underneath a line that reads the same,
which is why no test and no deploy can announce it.**

## 4. THE DEFECT THAT IS TRUE WHATEVER THE LIVE READ SAYS

⛔ **`not roster` MAKES *UNCONFIGURED* AND *DELIBERATELY TENANT-WIDE* INDISTINGUISHABLE.** One expression serves two
intents -- a fresh host that never got its `.env` populated, and an operator who decided tenant-wide on purpose -- and
**they are the same bytes.** That is Rule 24 INTENT COHERENCE failing on a two-value predicate, and it is the reason this
row could lapse quietly.

⭐ **REMEDY, SMALL AND INDEPENDENT OF ANY LIVE STATE: make tenant-wide EXPRESSIBLE AND EXPLICIT** -- a sentinel
(`SPRINT_VIEW_ALLOWED_EMAILS="*"`) that means tenant-wide, leaving **EMPTY to mean UNCONFIGURED and FAIL CLOSED.**
Tenant-wide stays available to whoever wants it; what stops being available is **arriving at tenant-wide by omission.**
⚠ **THIS IS A BEHAVIOUR CHANGE ON A DEPLOYED SURFACE AND IT LOCKS OUT EVERY CALLER ON A HOST WHOSE `.env` IS EMPTY** --
so it ships with the roster POPULATED in the same act, never before it, and never as a rider on an unrelated order.

## 5. THE TWO READS I ORDER, AND WHY THEY DO NOT GATE SECTION 4

`2.0.0_SA_COO~O` deliberately read neither and was right to name them rather than guess:
1. **The deployed `.env`'s actual roster value** (`EnvironmentFile=/opt/opal-gateway/.env`, on the box, not in the repo).
2. **Whether a restricted profile EXISTS in the live access-state table.** ⛔ **`TO-OG-z-2` complete proves the admin
   CAPABILITY was built and NEVER that a profile was MINTED** -- `2.0.0_SA_COO~O`'s distinction, and it is exactly the
   DESIRED-vs-APPLIED axis.

**Both are on-host/live READS of Opal-owned infrastructure, inside this fabric's autonomy, and I order them.** ⛔ **They
are READS: nothing in this ruling authorises stopping, starting or reconfiguring the Gateway instance** -- that act is
gate `G-A`/`OG-i-4`, which stays RESERVED at Andrew on CLAUDE.md's stopping-EC2 line and is unaffected by this.

⭐ **SECTION 4 IS ORDERED REGARDLESS OF WHAT THEY RETURN**, because it is a defect in how the predicate ENCODES INTENT,
not in what the live value happens to be. **The reads decide URGENCY, not correctness:** a restricted profile that
already exists makes this a live exposure to be closed in the current round; none existing makes it a correctness fix
that ships on its own cell before one is ever minted.

## 6. STATE, STATED HONESTLY

`NFRA_OPLGTW` carries open orders, so a NEW remediation row is graded as a slug act (R-66's structural finding).
⛔ **THIS RULING THEREFORE DISPOSES NOTHING BY ITSELF -- A DISARM IN PROSE DISPOSES NOTHING.** W3-S22 stays ARMED and
OPEN, its clock is this seat's, and it disarms at a point the gate permits, carrying this record as its evidence.

## 7. THE THREE ROUTINE ROWS -- DISARM DECISIONS GIVEN

- **`S33` @`7676e326be`** (W6-S6, W6-S8, W5-S18): **DISARM APPROVED, closed in behaviour**, on A-row tests still carrying
  their ORIGINAL assertions against an expectation file verified NOT weakened. ⭐ **The `assert_sum_allowed` nuance is
  kept in the record rather than smoothed:** zero callers across 59 app and 30 test files, but it is a COMPOSER and all
  three constituents are called directly from `query.py`. **The rule is enforced; the function is dead code.** Those are
  two findings and **a call count alone answers it wrong in both directions** -- dead-code removal is its own cell, never
  a rider here.
- **`S34` @`0a6eccda27`** (W6-S3): **DISARM APPROVED.** `test_ogk1_ac17` asserts the CALL LOG -- zero S3 calls under any
  `fact_` key -- in both arms with `assert fact_keys` as its own positive control. ⭐ **That instrument answers W6-S3's
  own objection: an IAM-free emulator answers a HEAD identically, but it CANNOT MASK A CALL THAT WAS NEVER ISSUED.**
- **The reading of "every named silver object"**: the narrow reading is ADOPTED and a test now holds it there. If the
  wide reading is ever wanted it arrives as an endpoint amendment with its own cell, not as a re-interpretation of a
  passing test.

---
*Raised by `2.0.0_SA_COO~O` (msg 97917) -- which built the remedy, then measured that building it had not closed the
row, and said so against its own work.*

## 8. VERIFIED AT THE BYTES BY THIS SEAT, ON A DIFFERENT QUESTION THAN THE ONE RAISED

`infra/aws/ec2/opal-gateway/app/sprint_view.py:173-175` at HEAD is **verbatim** as cited:
`def _allowed(email: str) -> bool:` / `roster = _cfg.SPRINT_VIEW_ALLOWED_EMAILS` /
`return True if not roster else email in roster`. **The citation is exact** -- checked by printing the bytes at the
cited lines, not by searching for the quote.

⭐ **AND I RAN THE CHECK THE ROW DID NOT ASK FOR: WHO CALLS IT, AND IN WHAT ORDER.** `_allowed` has **exactly two
callers**, `:182` and `:222`, and **both are preceded by `if not email:` at `:180` and `:220`.** `_viewer` returns
`""` on `IdentityError` (`:170`), so an unidentified caller would reach `_allowed("")` -- **which an EMPTY roster
would admit.** ⛔ **THAT PATH IS CLOSED, BY ORDERING RATHER THAN BY THE PREDICATE**, and the ordering holds at both
call sites.

**So the exposure is EXACTLY the one raised and NOT ONE STEP WIDER:** a *verified* tenant identity that an empty
roster admits. **An unverified caller is denied on identity before the roster is consulted.** ⚠ **But the guard is
now load-bearing in a way the predicate does not express** -- `_allowed` is written as if it were safe alone and it
is not, so **a third caller added without the `if not email` line inherits a hole that reads as a one-line
convenience.** Section 4's sentinel closes that too, which is a second reason to prefer it over documenting the
ordering.
