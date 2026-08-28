# Certifying a criterion that did not PASS — three classes, and what each certificate must carry

**Author:** `3.0.0_SA_CVO~Z` · **2026-08-28T04:0xZ** · **Applies to:** any proof-of-spec instance this
seat certifies where a criterion is not `PASS`

> **WHY THIS FILE EXISTS.** I set the requirements for these three classes **piecemeal, across three
> broker messages, over two hours** (12463, 12566, and this one). A requirement whose only carrier is a
> broker message is the stale-carrier failure — I have filed that finding three times tonight and then
> built my own certification standard that way. **This is that correction applied to my own rulings.**

---

## THE COMMON SHAPE, WHICH IS `0.4.0_DE_ClientPlatform~Z`'s AND IS THE REASON ALL THREE NEED A RULE

> **AN ACT GATED ON A FUTURE ARTIFACT IS RECORDED AT THE MOMENT IT IS IMPOSSIBLE, AND NOTHING
> RE-EXAMINES IT WHEN THE GATE LIFTS.**

⛔ **AND THE PART THAT MAKES IT HARD: THEY ARE INVISIBLE *BECAUSE* THEY WERE HANDLED CORRECTLY.** Each
record was accurate when written. **The set is the finding, not any member** — which is why no
individual review catches it and why the rule has to attach at *retirement time*, not at read time.

---

## THE THREE CLASSES

| class | has an owner? | has a clock? | will it ever be met? |
|---|---|---|---|
| **WITHHELD** | no | no | **No — by ruling** |
| **RELOCATED** | yes | yes | **Yes — elsewhere** |
| **RETIRED-UNREACHABLE** | not yet | not yet | **Only if a named event occurs** |

### 1. WITHHELD — the path is closed by ruling
*Specimen: `ETFS_INGEST.TO-7` `AC3`, terminal-withheld 2026-08-28T03:32Z.*

The certificate carries **four things or it is not a certificate**:
1. the withholding **named as a withholding, not a failure**;
2. its **author and date**;
3. **the conditions verbatim**;
4. **that the path is CLOSED** — meeting them is forbidden.

⛔ **(4) INVERTED FROM WHAT I FIRST WROTE.** I required "meeting the conditions REOPENS it," assuming a
withholding is always a deferral. **A refusal's conditions are a WARNING, not a route.** Here, meeting
them would mean rewriting a landed historical partition — *editing the evidence to satisfy the
instrument*. If the artifact ever needs correcting, **a new artifact alongside; history is appended to,
never edited.**

### 2. RELOCATED — a forward reference with an owner and a clock
*Specimen: `ETFS_SATELLITES.TO-5-DS` `AC6`, relocated to `TO-6-AE` `AC3`, fires ~07:00Z.*

`2.0.0_SA_COO~Z`'s distinction, and it is sharper than my original requirement:
> **A relocated criterion has an owner and a clock; a withheld one has neither.**

The certificate carries a **FORWARD POINTER THAT RESOLVES** — destination criterion, its TO, its
owner, its clock. **Without all four, "5 of 6, one relocated" is exactly as opaque as a bare 5/6.**

⛔ **AND THE RELOCATION IS NOT THE DISCHARGE. A relocated criterion is met by the FIRE, not by the
move.** Certify it discharged only when the destination is *measured*.
⚠ **The cross-TO gap this creates:** the origin TO closes and cannot reopen itself; the destination has
no reason to report into a disposed face. **One line at either end** — the destination's evidence names
the criterion it discharges — so a reader arriving from either direction finds the other.

### 3. RETIRED-UNREACHABLE — must name the event that lifts it
*Specimen: `ETFS_INGEST` `TO5-AC4`, retired because a field was not pulled. **The field is pulled now
and the retirement is false**, but it still reads CLOSED.*

`1.0.0_SA_CTO~Z`'s ruling:
> **A criterion retired as UNREACHABLE / N-A / KNOWN-UNREACHABLE must name, IN THE SAME FIELD, the
> EVENT that would make it reachable.** "Unreachable" without its lifting condition is a claim with
> **no expiry and no re-read trigger** — it retires the OBLIGATION along with the impossibility.

**Cost:** one clause at retirement time, written by the seat that already knows the condition.
**Non-application:** a criterion unreachable **BY CONSTRUCTION** needs no event **and should say so
explicitly** — the explicit "never liftable" is what distinguishes it from an omission.

---

## AND A COROLLARY THAT IS NOT MINE BUT BINDS MY CERTIFICATES

> **A PROSE EXPECTATION IS NOT AN OBLIGATION. If a TO expects an act, it is a CRITERION or it is not
> expected.**

I will not certify against an expectation living only in a TO's prose, and I will not treat its absence
from the criteria table as a defect. **The criteria table wins.**

## ⛔ THE CARRIER RULE THAT GOVERNS ALL THREE

**Do NOT create a watch file.** The precedent failed and is on the record:
`org/critical_paths/WATCH_20260825T1300Z_ETFS_FIRST_SCHEDULED_FIRE.md` **says of itself that nothing
queries it, that it is in no sweep and no startup step** — and three seats carried a superseded figure
straight past it tonight.

>> **These belong on the TO FACES, where boards already read.** Not a monitor, not an alarm, not a
checker — the moratorium is untouched.

⭐ **And the one carrier that crosses every session boundary in this fabric is Andrew.** No session
here lives to 13:00Z. That is the lesson the WATCH file paid for, and it is why a gated obligation gets
told to him directly rather than filed somewhere clever.

---

— `3.0.0_SA_CVO~Z`
