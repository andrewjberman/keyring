# AMGT_HARVST -- ROUND 5 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-25 ~01:0xZ

**Inputs:** the round-4 analysis @`2b196119f8` and its two appended corrections; the round-5 cut,
`AMGT_HARVST_DECOMP.md` section 16 (v1.4, "AN ISSUANCE OF NOTHING, and the read that earns it");
`AMGT_HARVST/project.json`'s blocking field, re-measured by `2.0.0_SA_COO~Y` ~20:3xZ after Andrew's
~17:5xZ access grant; my own resolver read of the channel at 01:0xZ.

**No slug answers this round, and that is correct rather than a gap.** Round 5 issued ZERO orders, so
there are no task orders for L8 to compile or L9 to grade. The round-N analysis is still owed, because
`2.0.0_SA_COO~Y` cannot cut round 6 without it -- and that lane has been IDLE waiting on this artifact.
**The wait is mine, not that lane's.**

**GRADE ACCEPTED. The issuance of nothing is the correct act and it earns its pre-authorization.**

---

## 1. ROUND 5 DID EXACTLY WHAT ROUND 4 ASKED, AND THE CONDITION ON ITS OWN LEGALITY WAS MET

Round 4 section 5 did not authorize an empty round outright. It authorized one **conditionally**: *"an
issuance of nothing is also a legal L6 act **if the coverage read closes it**."* So the grade turns on
whether the read closed the question, not on whether the remainder was zero.

**It closed it, and with the right instrument.** Round 4 warned that answering coverage from a
per-publisher bronze total would be "the wrong-domain move this same analysis credits the CVO for
avoiding". Section 16b did not do that. It read the **silver article census -- 86 parquet objects, ROWS
DENOMINATOR 97** -- and asked the question at the grain the question is actually about: rows whose
`discovered_for` contains `992_HK_Equity`. **14 -- seeking-alpha 3, wsj 11.** Per publisher overall:
barrons 15, bbg 19, ft 14, sa 23, wsj 26. So barrons, bbg and ft hold **48 rows for other securities and
ZERO for Lenovo**.

That is the difference between "all five publishers have bytes on disk" (round 4's 479-object
measurement, which it explicitly refused to read as coverage) and "three of them have nothing for the
name in question". **The round answered the question round 4 asked, in the domain round 4 named.**

## 2. AND IT REFRAMED THE VENDOR QUESTION INSTEAD OF ANSWERING IT YES -- the strongest part of the round

Section 16b's run report closes the other half: all five publishers were asked for Lenovo in ONE
invocation and each reached its own recorded terminal outcome -- sa stopped on an HTTP 502 with 3
genuinely new; **bbg took a verification challenge on the job's own first fetch**; **ft returned HTTP 403
from its search endpoint**; wsj expired, re-authenticated and accepted 11; **barrons expired,
re-authenticated SUCCESSFULLY, and its replayed first attempt was still rejected.**

**SO THE THREE ARE NOT UNMEASURED. They were asked, and access was refused three different ways.** The
discriminator the round states is the one that matters and I adopt it as this analysis's own: **only
bbg's failure is plausibly session-shaped.** A fresh session does not change a 403 on a search path, and
it demonstrably did not change barrons, whose re-authentication already succeeded once with the
rejection following it.

**This retires a sentence of mine.** Round 3's analysis said "three of five are unmeasured" and round 4
withdrew it as unsupportable. Round 5 replaces it with a per-publisher cause. `FWD-1` stays **NOT
REALIZED**, and for the first time its remaining cause is stated per publisher rather than as one
sentence about sessions.

## 3. THE SUBTRACTION IS SOUND, AND ITS THIRD TERM HAS AGED -- round 6 subtracts from TODAY

Section 16a's Rule-24 record is properly shaped: a printed denominator (round 4's three-item list),
three MINUS terms, remainder ZERO, and an explicit refusal to invent a cell. Two of its three terms are
still exactly right (`Z-S3`'s wording bound is carried, not cuttable; the coverage question is answered
and recorded as `Z-S14`).

WARN: **The third term has moved, and round 6 must not reuse it.** Section 16a subtracts "the channel,
measured at **36 rows, 0 non-terminal**". Measured by me at 01:0xZ through the gate's own resolver
(`_latest_dispositions('.', 'AMGT_HARVST')`, error arm empty): **48 rows -- GRADUATED 19,
DISMISSED_WITH_REASON 21, UNDER_INVESTIGATION 8.**

**This is NOT a defect in round 5.** The figure was true at its vintage and twelve rows have landed
since. It is a statement about what round 6 subtracts from: **the remainder is recomputed against 48 and
8, not against 36 and 0.** A subtraction is only as current as its youngest term, and this one now has a
term from a different hour.

WARN: **And a caution that round 4's own corrections already paid for twice:** `hazard_standing` over these
48 rows reads INERT 23 / ARMED 25, and **that field records what a row SAID WHEN FILED -- it is never a
current-state field.** The 25 is not 25 live hazards. Only the resolver's dispositions answer that, which
is why they are the figure above.

## 4. ONE DISCREPANCY I AM PLACING RATHER THAN RESOLVING -- two coverage metrics disagree about SA

The blocking field (COO~Y, ~20:3xZ) says **four publishers hold zero `listing_hit` rows -- barrons, bbg,
ft, sa; only wsj has any.** Section 16b says, on `discovered_for`, that **sa holds 3 Lenovo rows.**

**These are different fields over possibly different populations and I will not collapse them into one
sentence.** A metric's NAME is not its DEFINITION, and "does publisher X cover this security" has at
least two live readings here that disagree on SA specifically. It matters because my own adjudication
@`0d568cdf51` quoted the `listing_hit` form, and because a round-6 cell scoped to "the publishers at
zero" would include or exclude SA depending on which field it reads.

**Ruling: round 6's cell names the FIELD it counts, with its denominator, or it is not cuttable.** No
work is owed to resolve the discrepancy first -- naming the field is enough, and doing it in the cell is
cheaper than an investigation.

## 5. `FWD-1`, and what is held OUTSIDE this project

`FWD-1` **NOT REALIZED**. `FWD-5`/`FWD-6`'s spec is complete and its build is Andrew's call. Section 16c
states plainly that **every item this project can finish alone is finished**, across two consecutive
rounds at zero egress and zero writes -- each closing an item with a measurement rather than an argument.
**That is the honest shape for this project right now and I am not manufacturing a round to disguise it.**

What remains is held outside the project: the timeline BUILD cell (Andrew, the AMENDED spec); further
publisher access (Andrew -- and `Z-S14` now says a session-shaped act addresses at most ONE of the three
refusals); the served chatter switch (a never-widen pair, the gold read grant, RESAPP's retirement
window); and the sibling project's unadjudicated S3-delete breach, which this project measured itself
clear of.

## 6. ROUND 6 -- `2.0.0_SA_COO~Y`'s to cut, PARTIAL-SHAPED

My standing ruling (msg 25731) holds: **round 6 is cuttable and MUST be PARTIAL-shaped.** `data_status
COMPLETE` needs all five publishers to cover the day, so a bbg-only cell cannot reach COMPLETE however
well it executes, and the COMPLETE shape is its own later outcome.

**The cut, as this analysis leaves it:**
1. **bbg is the ONE MOVABLE of the three refusals**, and it is movable on Andrew's own words -- *"If
   there is an issue with getting BBG access let me know and we can troubleshoot that."* **That is an
   OFFER of an ACT, not a grant and not a decision**, and it is untaken. It is carded to him.
2. **ft and barrons are NOT cuttable as access work.** A 403 on a search path and a post-auth rejection
   are not reached by authorization, and `Z-S14` is the row that says so.
3. **Any cell counting "publishers at zero" names its FIELD and its denominator** (section 4 above).
4. **The remainder is recomputed against 48 rows / 8 UNDER_INVESTIGATION**, not against 36 / 0.
5. **An issuance of nothing remains legal** if that subtraction is again zero. Round 5 proved the shape
   is honest; it does not need re-arguing.

## 7. THE ONE RESERVED CALL, and it is genuinely Andrew's

**Does `data_status COMPLETE` stay the standard when ft and barrons are unreachable by any
authorization?** Recorded at `CTO_ADJUDICATION_AMGT_RESAPP_20260925T0040Z.md` @`0d568cdf51`. Reserved
with its citation: the goal's own words are *"complete backfill for all of these securities"* and *"Only
when all of this is done for every single security ... is the goal complete"* -- **redefining COMPLETE
narrows the standard the GOAL is measured against, and a driver may not move its own stop-condition.**
REC if he wants one: keep COMPLETE, let round 6 close PARTIAL with the two publishers named, so the gap
stays visible rather than defined away.

## 8. Instrument note -- the resolver's failure arm nearly handed me a clean zero

`_latest_dispositions` takes `(root, code)`. I first called it with a ROWS LIST and it returned
`(None, [], 0, 'git ls-files raised expected str, bytes or os.PathLike object, not list')` -- **a
well-formed tuple whose count element is `0`.** Read without the error element, that is "the channel has
0 open rows", which is both wrong and exactly the conclusion I was looking for. **The error string is the
only thing separating a real zero from a reader that could not see.** Populate the failure arm before
quoting any count from this resolver; the correct call returned 48 rows and 8 UNDER_INVESTIGATION.

---

**ROUND 5 IS CLOSED.** `2.0.0_SA_COO~Y` is unblocked to cut round 6 on section 6 above.
