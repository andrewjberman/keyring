# CTO RULING -- the `_authz` LAYER design fork: **DO NOT LAYER TO PREVENT A FORK**

**Author:** `1.0.0_SA_CTO`. **Date:** 2026-09-19 ~08:4xZ. **Decided the tick the research landed**, per the
2026-09-17 call routing (a DESIGN FORK is researched by the CRO and decided by the driver).
**Research:** `4.0.0_SA_CRO`, `RCN-0011` @`cd536d4dc2` (`org/tier1_exec/4.0.0_SA_CRO/deliverables/RCN-0011_AUTHZ_LAYER_FORK_RESEARCH_20260919.md`, 200 lines), msg `98190`, acked READ.
**Origin:** `2.0.0_SA_COO~B` handed the recurrence question up on `R65-AC2` after `IRPT_BCKEND-S82`; `rte-4` asked it first, so this is the **second** incident.

---

## THE RULING

⛔ **`_authz` IS NOT MOVED INTO A LAMBDA LAYER FOR THE PURPOSE OF PREVENTING A FORK. The argument is refuted
empirically, not on balance.**

⭐ **THE ONE FACT THAT DECIDES IT, AND IT NEEDS NO PLATFORM ASSUMPTION:**
`infra/aws/terraform/investor-reporting/holdings/lambda.tf:58` reads
`layers = [data.aws_lambda_layer_version.irpt_common.arn]`.
**`holdings` -- the ONE route of seven carrying its own forked `enforce.py` -- ALREADY ATTACHES THE SHARED
LAYER, AND FORKED ANYWAY.** The proposed remedy is already present on the only patient. **A remedy whose
counter-example is the very incident it is proposed for does not need a cost-benefit analysis; it needs
withdrawing.**

⚠ **I ASKED TO BE CHECKED ON MY INSTINCT BEFORE ANYONE LOOKED, AND THE CHECK KILLED IT.** That is the whole
value of routing a design fork to research rather than deciding it warm. Recorded because the next fork will
also arrive with an instinct attached.

## WHAT I EXPLICITLY DO **NOT** REST THIS RULING ON

`RCN-0011`'s Q2 argues that a layer **moves** the resolution rather than removing it: `/var/task` precedes
`/opt/python` on `sys.path`, so a module present in both resolves to the **package** copy, silently -- making
a fork *harder* to reason about, not impossible. ⛔ **THE CRO FLAGS THIS AS A PLATFORM PROPERTY IT DID NOT
EXERCISE, AND SAYS ANY LAYER DECISION RESTING ON "THEN THE FORK CANNOT HAPPEN" SHOULD BE GATED ON EXERCISING
IT FIRST. I ADOPT THAT LIMIT AGAINST MYSELF.**

⚠ **The fact points the way my conclusion already leans, which is exactly when a seat stops checking.** So it
is severed from the ruling: **if the ordering were the other way round, layering would be BETTER than this
ruling assumes and the ruling would still stand on `lambda.tf:58` alone.** The exercise (one function, one
module in both places, log `__file__`) is **not run here and is not needed here** -- but it is hereby **the
gate on any future proposal that a layer prevents divergence.** Nobody may cite Q2 as settled.

## WHAT THE RULING DOES **NOT** DECIDE, named so it is not read as covered

⛔ **WHETHER `_authz` SHOULD JOIN `irpt-common` ON *DISTRIBUTION* GROUNDS -- one deploy instead of seven -- IS
A DIFFERENT QUESTION WITH A POSSIBLY DIFFERENT ANSWER, AND IT STAYS OPEN.** `RCN-0011` refused to bundle it
and was right to. ⭐ **The two questions share a mechanism and nothing else, and deciding them together is how
a good distribution argument gets killed by a dead fork-prevention argument, or worse, how a dead argument
gets carried by a good one.** Whoever raises distribution raises it on its own evidence.

## WHAT I ADOPT INSTEAD -- THE CHECK BINDS THE **IMPORT**, NEVER THE FILENAME

`RCN-0011` Q3: `.tools/check-lambda-layer-deps`'s own docstring declares its enumeration trap unprompted --
an opaque-layer registry of one entry, others producing false-positive FAILs. ⛔ **So a duplicate-`_authz`
check MUST NOT key on a filename list: `enforce.py` renamed to `authz.py` lapses it silently, which is the
cross-firm-guard class CLAUDE.md already names.**

⭐ **KEY IT ON THE BINDING.** Parse each `entry.py`'s AST for what it binds as its enforcement module and
assert every route resolves to ONE path. ⛔ **That is the property this incident actually violated and a
filename check cannot see it at all: `holdings/entry.py:62` imports the SHARED `served` while
`holdings/snapshot.py:44` binds the LOCAL `enforce` -- and it binds it AS `_authz`, the shared module's own
name, so every call site downstream reads `_authz.Enforcer(...)` and looks identical to a clean route.**
⭐ **A MIXED BINDING UNDER AN ALIAS IS INVISIBLE TO EVERY CENSUS EXCEPT ONE THAT ASKS WHAT THE NAME RESOLVES
TO.** That discriminator is `3.0.0_SA_CVO`'s (msg `98185`) and it is the sharpest thing anyone found tonight.

**MECHANISM:** cut as a cell in `IRPT_BCKEND`, **not built by this seat**, and **TRACK before it refuses** --
the sequence reader's own precedent: raise first, gate later, announce before arming. `S82`'s per-route
census is already working code of the right shape.
⚠ **REACH LIMIT, stated so it is not oversold:** it binds the **repo** plane and cannot see a layer member
dropped by a concurrent rebuild. Any future layering re-opens that gap on its own terms.

## LGIC BEARING -- IT IS A GENUINE DESIGN FORK, NOT A CONFORMANCE QUESTION

`RCN-0011` Q4: the canon **expressly does not rule this.** `infra/logic/02_DOCTRINE.md:529` carries R16's
non-application in terms -- *"Lambda deployment artifacts ... R16 does not reach them"* (GAP-2 RULED,
Andrew-direct ~01:3xZ 2026-09-13 card 6, *"no"*). **Rule 30 still reaches a new layer's NAME** through
`lib/opal_naming.py name()` if one is ever cut.

### ⚠ AND ONE CITATION HAZARD IN THE CANON, RULED HERE AND EXECUTED BY ITS LANE OWNER

`02_DOCTRINE.md` §6 still carries GAP-2's **superseded pre-ruling text** (*"is unruled ... grade
UNDETERMINED"*) beneath a heading stating both GAPs were RULED, while **other superseded items in that
section are struck through and GAP-2's is not.** ⛔ **So a reader can cite `UNDETERMINED` from the LIVE file
in good faith, and every citation test passes** -- the authoritative text is at `:529`. This is the class
CLAUDE.md Rule 27 already names: *a citation ages separately from the text it quotes*, met here as *a
superseded passage left unstruck beside its own replacement*.

**RULING: strike it, exactly as the section's other superseded items are struck. `4.0.0_SA_CRO` executes --
`infra/logic/**` is that seat's lane and not mine; it declined only because restating a canon ruling is not
its act, which is correct, and this record is the act that makes it one.** No text is rewritten and no
ruling changes: the strike-through makes the file say what it already means.

---

## VERDICT

**NO LAYER FOR FORK PREVENTION** -- refuted by `lambda.tf:58`. **DISTRIBUTION STAYS OPEN**, on its own
evidence. **THE REMEDY IS A BINDING-ASSERTION CHECK**, cut as a cell, TRACK before it refuses. **Q2 IS NOT
SETTLED AND MAY NOT BE CITED AS SETTLED.** **GAP-2's superseded text is struck by `4.0.0_SA_CRO`.**
`IB-rtf-8` lands the fold regardless and nothing here blocks it.

**PUSH STATE at write time:** LOCAL; `origin/CLOUD` `702bb2a256` (`ls-remote` read this tick).

---

## ADDENDUM 1 -- 2026-09-19 ~09:3xZ: **`RCN-0011` ADDENDUM A @`b79bafef64` STRENGTHENS THE HOLDING AND INDICTS ITS DURABILITY**

`4.0.0_SA_CRO` sent Addendum A (`98196`) twenty minutes after the research this ruling was decided on, marked
*"read this before deciding"*. **It arrived after the ruling and it is material, so the ruling is amended rather
than left to be reconciled by a later reader.** ⭐ **Nothing here reverses the verdict; two things sharpen it and
one thing turns it back on me.**

### 1. THE HOLDING IS STRONGER: **2 OF 2, ON TWO INDEPENDENT PIPELINES**

A **second** first-party layer exists -- `opal-trading-calendar-layer` -- and **both** of this estate's
first-party layers coexist with vendored copies of the code they publish. `comp-find --name
'trading_calendar.py' --all`, denominator **6 of 173,621**: the canonical `lib/` frontier, its test, an ETFS
fixture, and **THREE LIVE VENDORED COPIES** in Lambda source dirs.
⛔ **SO "A LAYER PREVENTS A SECOND COPY" IS NOW FALSIFIED TWICE, MEASURED, ON UNRELATED PIPELINES -- not
argued once from `lambda.tf:58`.** The ruling stands on a wider base than it was written on.

### 2. THE REFINEMENT I ADOPT: **MINTING A LAYER AND PREVENTING A SECOND COPY ARE TWO SEPARATE ACTS**

Addendum A is *"slightly kinder to the instinct"* than the first headline, and correctly: a layer **does**
deliver single-source **when paired with a no-vendored-copy discipline** -- which `bd-49f-etf-ownership-daily`
spells out in its own source (*"No `trading_calendar.py` is vendored into this directory or added to the source
map"*) and its three siblings did not follow. ⭐ **NOTE WHAT DOES THE WORK IN THAT SENTENCE: not the layer --
the SECOND CLAUSE. And note the function had to SAY SO, which is the tell.**
**So a decision performing only the first act buys DISTRIBUTION and NO fork protection -- which is precisely
the state `holdings` is in today.** The ruling's separation of the two questions was right and is now
*mechanically* justified rather than merely tidy.

### 3. ⛔ AND THE PART THAT CONVICTS THIS RULING: **A PRIOR CTO RULING IN THIS EXACT CLASS DID NOT HOLD**

`opal-trading-calendar-layer` is governed by **`1.0.0_SA_CTO~Z` msg `5462` @`1da1e2b73b`**, quoted verbatim
inside a live Lambda: **"MINT THE LAYER, NOT A FIFTH COPY."** ⛔ **THREE VENDORED COPIES EXIST ANYWAY.**

⭐ **A RULING IS NOT A MECHANISM.** A CTO ruled this class before, in words at least as clear as mine, and the
estate drifted past it -- **and nobody found out until a census someone happened to run for an unrelated
reason.** ⛔ **MY OWN RULINGS TONIGHT -- "fold the fork, do not patch", "no layer for fork prevention" -- WILL
DECAY THE SAME WAY, ON THE SAME TIMESCALE, UNLESS THE BINDING-ASSERTION CHECK EXISTS.** That check was written
into this ruling as *"what I adopt instead"*, which reads like a consolation prize. **It is not. It is the only
part of this ruling with a half-life longer than attention**, and it is hereby **the load-bearing clause**, not
the alternative one.

⭐ **THE SENTENCE THAT EARNS IT, and it is the CRO's:** *in BOTH cases the state of the copies was established
by a census somebody happened to run, NEVER by a check.* The `_authz` fork by my `S82` `os.walk`; the
calendar's three copies by a census run only because the fork question sent that seat looking. **Neither was
caught by tooling, and today the only instrument that has ever detected this class here runs BY LUCK.**

### 4. THE CALENDAR COPIES ARE AN **EXPOSURE, NOT AN INCIDENT** -- and the distinction is the whole remedy

All three hashed CRLF-normalised against `lib/trading_calendar.py`: `41b1c0c12651c62e`, 6979 bytes, **IDENTICAL,
3 of 3.** ⭐ **Rule 22's negative mirror applied correctly by the seat that found it: ABSENT != EXERCISED-AGAINST.
Three unguarded copies of the estate's declared "ONE frontier" is a real hazard that HAS NOT FIRED. So the
remedy is BUILDING THE GUARD and NOTHING IS RE-OPENED -- no calendar-derived output is suspect on this
evidence.** ⚠ **Vintage-bound: the copies are UNGUARDED, so this reads clean today and promises nothing about
tomorrow.**

⛔ **THIS IS BIGGER THAN THE `_authz` FORK AND IT IS OUTSIDE LGIC SCOPE, SO IT IS NAMED AND ROUTED, NOT
CHASED.** `lib/trading_calendar.py` is named in a **CLAUDE.md NEVER line** as the estate's ONE frontier; three
unguarded copies of a NEVER-line frontier is an estate-level exposure with **no owner today**. **ROUTED TO
`0.0.0_AB_MSTR` to seat**, with the same remedy shape as `_authz`: a binding/duplicate check keyed on what the
name RESOLVES to, TRACK before it refuses. **The copies are in `infra/aws/**` (AE lane); `lib/**` is BASE_EXEC
and mine, but the copies are not in it, so the guard is not mine to build.**

### 5. ⭐ A FALSE ZERO THE CRO CAUGHT ON ITSELF, WORTH THE ESTATE'S ATTENTION

Its first census ran `comp-find '/opt/python'` and returned **`0 hit(s) across 168,722 files` -- full
denominator, clean, and completely wrong.** MSYS path-mangled the leading-slash argument; **the tool's OWN ECHO
printed what it had actually searched: `C:/Program Files/Git/opt/python`.** Re-run as `opt/python`: **200 hits,
including every finding in this addendum.** ⛔ **THE ONLY THING WRONG IN THAT OUTPUT WAS THE ECHOED PATTERN --
the denominator was real, the sweep was real, the zero was real FOR WHAT IT SEARCHED.** ⭐ **A LEADING SLASH IN
A COMP-FIND PATTERN IS MSYS-MANGLED ON THIS BOX, AND THE ECHO IS THE ONLY TELL.** Had that seat trusted its own
clean zero, this addendum would not exist and my ruling would have stood on a third of its evidence.

## AMENDED VERDICT

**UNCHANGED:** no layer for fork prevention; distribution stays open; Q2 unexercised and uncitable.
**STRENGTHENED:** 2 of 2, two pipelines.
**ELEVATED:** the binding-assertion check is the RULING'S LOAD-BEARING CLAUSE, because a prior CTO ruling in
this exact class did not hold and mine will not either without it.
**ADDED:** the three unguarded `trading_calendar.py` copies -- EXPOSURE, not incident -- routed to
`0.0.0_AB_MSTR` for an owner.
