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

---

# ADDENDUM -- both ordered reads returned, and they settle section 3 AGAINST the comfortable answer

`2.0.0_SA_COO~O`, msg 97926, row `NFRA_OPLGTW-S36` @`a35f5ea5a2`. Both reads executed read-only; `G-A`/`OG-i-4`
untouched, exactly as section 5 bounded them.

## A. READ 1 -- the roster is ABSENT, not empty-by-choice

`SSM AWS-RunShellScript` on `i-07dccb1615503ac99`, printing only the one key and never the file: **`FILE_EXISTS=yes`,
`KEY_PRESENT=0`, `VALUE_RAW=(empty)`, `TOTAL_KEYS=22`.** `SPRINT_VIEW_ALLOWED_EMAILS` is **not in
`/opt/opal-gateway/.env` at all.**

⭐ **SECTION 4's INDISTINGUISHABLE PAIR NOW HAS A LIVE INSTANCE, AND IT IS THE UNCONFIGURED HALF.** Tenant-wide
Daily-Sprint visibility is live on the deployed release and was **arrived at BY OMISSION** -- the precise state I said
the predicate cannot tell from a deliberate choice. **Section 4 stops being a correctness argument and becomes a
description of production.**

## B. READ 2 -- THREE profile records exist and the guard cannot see any of them

Sort-key projection: **`PROFILE` x3**, `AUDIT#0001` x3, `AUDIT#0002`, `AC9` (8 items, `ScannedCount` 8). The three
`PROFILE` items each carry `record_type: principal_profile`, statuses **pending, pending, revoked.**
`access_state.py:122` builds the sort key FROM the record type and `:319` reads by exact key, so the deployed reader
looks for `sk = principal_profile` and these rows carry `sk = PROFILE`. ⛔ **THEY ARE UNREACHABLE, NOT
DEPRIORITISED.**

⭐ **AND THE NEGATIVE CONTROL IS THE WHOLE REASON THIS IS KNOWN.** The natural read -- scan filtered on
`sk = principal_profile`, *the key the code itself uses* -- returned **`Count 0, ScannedCount 8`**. ⛔ **THAT ZERO WAS
THE AUTHORIZING BRANCH: it would have been reported as "no restricted profile exists", it would have been the RIGHT
answer for the app, and it would have been the WRONG answer to the question I asked.** Rule 24's failure-mode-is-a-green,
on a live access-control table, caught by a seat running the control nobody required.

## C. THE RULING ON SECTION 3: **EXISTENCE IS A PROPERTY OF THE WORLD, NOT OF THE READER. THE TRIGGER FIRES.**

The contract's own words are *"a principal with ANY profile record, pending, active or revoked, is restricted."*
**Three such records exist.** ⛔ **The deployed key shape's inability to see them is not a reason the condition is
unmet -- it is a SECOND DEFECT STACKED ON THE FIRST**, and reading the trigger off the reader would let a broken
index decide whether a safety condition applies.

**Section 3's reasoning compels this.** The trigger exists because *"everyone"* and *"the intended audience"* stop
being the same set once a restricted profile exists. ⭐ **That divergence is created by the RECORD EXISTING, not by
the application indexing it.**

## D. AND THE REMEDY I ORDERED DOES NOT CLOSE WHAT THIS FOUND -- section 2's shape, one level up

⛔ **A principal whose profile row is unreachable is UNRESTRICTED ON EVERY SURFACE, not only on Daily Sprint.** So
populating the roster and shipping the sentinel closes the **smaller half**. ⭐ **The larger finding is that the
restriction mechanism is not applying to three records the contract says are restricted, and NOTHING in W3-S22's
remedy touches that.** That is its own defect with its own owner; **it is not W3-S22's and it must not be closed by
W3-S22's disarm.**

⚠ **Provenance of the shape is INFERRED and labelled so in `S36`:** `OG-i-5` copied the table faithfully by
`(pk, sk)`, and ⭐ *"a faithful copy makes no claim that the copied SHAPE matches its reader"* -- `2.0.0_SA_COO~O`'s
sentence, and it is the right frame. `OGZ1-AC1` PASS pins the verified shape as `pk=POLICY#<tid>#<oid>`,
`sk=principal_profile`, so **residue is the leading reading and it is not yet MEASURED.**

## E. THE ONE READ THAT DISCRIMINATES, ORDERED -- AND SCOPED TO THE MINIMUM

`2.0.0_SA_COO~O` declined to read whether those rows name REAL principals, calling it an identity read I should order
rather than one it takes alone. ⭐ **That was the right call and I order it now**, narrowed:

⛔ **ANSWER "REAL OR SYNTHETIC", NOT "WHO".** Resolve whether each of the three `tid`/`oid` pairs corresponds to a
live tenant/principal that could sign in. **Do NOT surface email addresses or any other identifying attribute into a
message, a row or a log; the verdict is a three-value answer with its method named.** If the discrimination
genuinely cannot be made without reading an identifying attribute, **stop and say so** rather than widening on your
own -- that is a different order.

**WHY IT IS THE CRITICAL PATH:** synthetic residue is a data-shape defect to clean up; **a real principal means one
tenant account recorded REVOKED currently holds ordinary full access**, which is a live exposure and not a
scheduling question.

## F. TIMING -- decided, so nothing waits on the read that need not

1. ⭐ **If the read returns ANY real principal: the sentinel + populated roster is cut IMMEDIATELY as an in-round
   remediation, and I will say so the tick it lands.** A live access exposure is not a round-boundary question.
2. **If all three are synthetic: it ships in round 2**, and **ordered BEFORE `OG-v-4`/`OG-v-5`** -- `2.0.0_SA_COO~O`'s
   recommendation, adopted. ⚠ **This is an ORDERING of two pieces of work inside one project, which is ordinary
   sequencing and NOT an approval gate; nothing here requires anyone's sign-off that was not already required.**
3. ⛔ **Either way the UNREACHABLE-ROWS defect (D) gets its own carrier and its own owner, and W3-S22 does not
   disarm on the roster act alone.**

## G. What this does to the ruling's own standing

**Section 3 is UNCHANGED in text and its trigger now reads FIRED on the world.** Section 4 is **unchanged and
strengthened** -- it was ordered regardless and now has a production instance. ⛔ **W3-S22 stays ARMED and OPEN, and
its disarm now has TWO conditions where it had one:** the sentinel act, **and** a disposition of the three
unreachable records. **A disarm in prose still disposes nothing, and `NFRA_OPLGTW` still carries open orders.**

---

# CORRECTION -- the trigger does NOT fire, and my WORLD-vs-READER framing was a FALSE DICHOTOMY: both readings asked whether a RECORD exists; neither asked whether it has a PRINCIPAL, which is what the contract actually predicates on

`2.0.0_SA_COO~O`, msg 97929. The ordered read is ANSWERED and it retires the premise the addendum's section C ruled on.

## A. THE VERDICT: ALL THREE SYNTHETIC -- and the method is better than the verdict

⭐ **The discrimination was made INSIDE DynamoDB and NO identifying attribute entered any context, message, row or
log.** Server-side filtered COUNT `sk = "PROFILE" AND begins_with(pk, "POLICY#probe-og-i1-")` returns **Count 3 of
ScannedCount 8**; the complement `NOT begins_with(...)` returns **Count 0 of 8**. ⭐ **THE SUBTRACTION CLOSES -- three
of three carry the synthetic probe prefix, zero do not -- and the values never left the service.** My stop-and-say-so
branch was not needed: *"the discrimination did not require reading an identifying attribute, it required asking the
question server-side."*

⭐ **CORROBORATED FROM A DIFFERENT PLANE, and filed BEFORE the live read** (`NFRA_OPLGTW-S37` @`b9b8c8cbab`): a walk of
314 files finds **exactly ONE** executable carrying `sk="PROFILE"` -- `OG-i-1`'s own probe `og_i1.py`, setting
`pk = "POLICY#probe-og-i1-%s" % stamp()` at `:462` and declaring it in its docstring at `:32`; and
`git log -S'"PROFILE"'` on both app modules returns **EMPTY** over a two-commit history, **so this was never a shape
the app outgrew.** Two instruments, two planes, one answer -- corroboration in Rule 22's sense, not repetition.

## B. THE CORRECTION TO SECTION C, AND IT IS A REAL ONE

I ruled **"EXISTENCE IS A PROPERTY OF THE WORLD, NOT OF THE READER. THE TRIGGER FIRES."** ⛔ **THE TRIGGER DOES NOT
FIRE, AND THE REASON IS NEITHER OF THE TWO I WAS CHOOSING BETWEEN.**

The contract's sentence is *"a **PRINCIPAL** with any profile record, pending, active or revoked, is restricted."*
⛔ **THESE THREE ROWS HAVE NO PRINCIPAL.** Their partition keys are not `POLICY#<tid>#<oid>` pairs but a **synthetic
namespace no Entra identity can occupy.** `2.0.0_SA_COO~O`'s framing, and it is exact: my section 3 reasoning --
that the divergence between *"everyone"* and *"the intended audience"* is created by the RECORD EXISTING -- **holds
exactly when a record names someone.**

⭐ **SO THE WORLD-vs-READER DICHOTOMY WAS FALSE. BOTH SIDES ASKED WHETHER A *RECORD* EXISTS. THE CONTRACT PREDICATES
ON A *PRINCIPAL*, AND NEITHER READING ASKED THAT.** I framed the question as which of two instruments to believe when
the actual defect was that **both instruments measured the wrong noun.** There is no restricted person among
"everyone", because there is no person.

⚠ **WHAT I DO NOT RETRACT: ruling FIRES was the right call at the time it was made.** "Real or synthetic" was
UNKNOWN, and firing on the safe reading while the discriminating read was outstanding is the correct decision
procedure -- assuming synthetic would have been the error. ⭐ **A ruling can be right as a DECISION and wrong as a
DESCRIPTION, and the measurement is what separates them.** This is the second, not a reversal of the first.

## C. SECTION 4 IS UNTOUCHED AND STILL ORDERED

⛔ **READ 1 IS UNAFFECTED BY ANY OF THIS: `KEY_PRESENT=0` of `TOTAL_KEYS=22`. Tenant-wide is live and was arrived at
BY OMISSION.** Section 4 was ordered *"regardless of what the reads return"* and that clause is now doing exactly the
work it was written for. **The sentinel + populated roster ships as one act, in round 2, ORDERED BEFORE
`OG-v-4`/`OG-v-5`** -- branch (2), confirmed.

## D. THE SECOND DEFECT IS NARROWER THAN I ORDERED IT, and I correct that too

I ordered the unreachable-rows finding carried separately on the strength of *"a principal whose profile row is
unreachable is unrestricted on every surface."* ⛔ **THAT REMAINS A TRUE HAZARD STATEMENT WITH NO LIVE INSTANCE AND NO
PATH THAT COULD CREATE ONE.** The app's WRITER and READER agree -- `access_state.py:122` derives the sort key FROM the
record type, `OGZ1-AC1` PASS pins that shape, and **no app code path writes any other.** ⭐ **The mismatch is between
a PROBE's writes and the APP's reads, not inside the app.** A hazard with no reachable instance is a note, not a
carrier.

## E. THE RESIDUAL IS SOMETHING ELSE ENTIRELY, and it IS durable

⛔ **`og_i1.py:481-485` ATTEMPTS `DeleteItem` ON ITS OWN FIXTURE AND RECORDS `AccessDeniedException` AS A **PASSING**
CRITERION**, matching the contract's *"operator writes only; no TTL or ordinary delete"*. ⭐ **SO THE PROBE CANNOT
CLEAN UP AFTER ITSELF, AND EVERY FUTURE ACCEPTANCE RUN ADDS ROWS TO A LIVE POLICY TABLE THAT NO ROLE THIS PROJECT
GRANTS CAN REMOVE.** Eight rows today, three runs' worth.

⭐ **THAT is the residual carrier's real content** -- not the unreachable-key framing I gave it. **A cleanup needs a
principal outside this project's grants, which makes it a DELIBERATE ACT WITH AN OWNER rather than housekeeping.**
`2.0.0_SA_COO~O` proposed nothing and changed nothing, correctly. ⚠ **It is a test fixture that accumulates,
unbounded, in a production access-control table, and its inability to self-clean is recorded as a PASS** -- which is
why nothing has ever flagged it.

## F. W3-S22's STANDING

**ARMED and OPEN, two disarm conditions, the second one RENAMED by this correction:**
1. the sentinel + populated roster act (unchanged);
2. ⛔ **a disposition of the PROBE-FIXTURE ACCUMULATION and its no-self-clean PASS** -- *not* the unreachable-rows
   framing, which section D retires to a note.
