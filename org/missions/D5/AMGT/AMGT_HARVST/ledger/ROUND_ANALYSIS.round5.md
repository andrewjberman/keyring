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

[AMENDED 2026-09-25 ~01:3xZ -- SEE THE AMENDMENT AT THE END OF THIS FILE. This section reads as though
round 6 waits on Andrew. IT DOES NOT: a FOURTH publisher, sa, sits at zero for an OUTAGE rather than a
refusal, and retrying it is a cell that waits on nobody. Read the amendment before cutting.]

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

## 7. THE ONE RESERVED CALL [**STRUCK 2026-09-25 ~03:1xZ -- SEE AMENDMENT 2. The card below asked
Andrew to affirm a status quo nobody had proposed changing. It is withdrawn, not answered.**]

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

**ROUND 5 IS CLOSED.** `2.0.0_SA_COO~Y` is unblocked to cut round 6 on section 6 as amended below.

---

# AMENDMENT 1, 2026-09-25 ~01:3xZ -- SECTION 6's PREMISE IS CORRECTED: ROUND 6 HAS A CELL THAT WAITS ON NOBODY

**Cause:** `2.0.0_SA_COO~Y`, msg 25827 (acked), answering section 6 within twenty minutes of it landing.
**ACCEPTED IN FULL.** It found the gap by asking a question I did not: **why do FOUR publishers sit at
zero `listing_hit` when only THREE refusals were ever recorded?**

**THE FOURTH IS `sa`, AND IT IS NOT A REFUSAL.** `Z-S14`'s own evidence line reads
`upstream_unavailable (HTTP 502 from seekingalpha.com, 24 accepted of which 3 genuinely new)`. **A 502 is
an OUTAGE, not an access decision.** bbg's verification challenge, ft's 403 on a search path and barrons'
post-auth rejection are all decisions a retry cannot move. **`sa` is the one a retry CAN.**

**And the chain explains the zero, which is what makes this actionable rather than hopeful.** `sa`'s 502
raised MID-LOOP, and at that vintage `_write_harvest_listings` sat AFTER the per-article loop, so every
listing page already captured for that job was discarded -- row `W15-S1`. That is why `sa` shows 44
silver ARTICLE rows and 0 `listing_hit` rows. **The persist now sits in a `finally` wrapping the loop
(`worker.py:223`, disarmed today in `Z-S24`), so a retry would both get further AND KEEP its pages.**

**MEASURED, WITH BOTH FIELDS NAMED -- section 4's ruling did its job in one hop:**
| field | barrons | bbg | ft | sa | wsj | denominator |
|---|---|---|---|---|---|---|
| silver `listing_hit` | 0 | 0 | 0 | **0** | 20 | **20** |
| silver article `discovered_for` | 15 | 19 | 14 | **44** | 26 | **118** |
| bronze `news_listing` | - | - | - | - | 2 (all wsj) | **2** |

**All five returned ARTICLES; only wsj kept LISTINGS.** And the bronze census is the check I would have
had to ask for and did not have to: **the four cannot be rebuilt from held data**, so a fetch is
genuinely required rather than assumed.

**SO SECTION 4's "DISCREPANCY" IS RESOLVED, and it was never a contradiction.** Both figures were true:
`sa` holds 0 `listing_hit` AND 44 article rows, in different tables, and the CAUSE is the persist
ordering now fixed. Naming the field was enough, exactly as section 4 ruled -- no investigation was owed
and none was spent.

**WHERE SECTION 6 WAS WRONG.** Its sentence "bbg is the ONE MOVABLE of the three refusals" is literally
true and was the wrong frame: **by scoping to the three REFUSALS I let the round read as Andrew-gated,
when a fourth publisher sits at zero for a cause no grant is needed to clear.** I had the 502 in front of
me -- it is in `Z-S14`, which I cited twice in this same analysis -- and I read it as one of the
"refused three different ways" rather than asking why the arithmetic gave four. **A count that does not
reconcile with its own causes is the tell, and I printed both numbers without subtracting them.**

**THE CUT, AS AMENDED:**
1. **RETRY `sa` -- a cell that waits on NOBODY.** No new access, no grant, no Andrew act, and the
   producer defect that discarded its pages is already fixed. This is round 6's first cell.
2. **It is PARTIAL-shaped BY CONSTRUCTION**, which is the shape I ruled at msg 25731: `sa` plus wsj is
   **2 of 5** and can never reach `data_status COMPLETE`. The PARTIAL shape is not a concession here, it
   is arithmetic.
3. **bbg remains the one movable of the three REFUSALS**, on Andrew's untaken offer of an act. Unchanged.
4. **ft and barrons remain not cuttable as access work.** Unchanged.
5. The remainder still recomputes against **48 rows / 8 UNDER_INVESTIGATION**, not 36 / 0.

**INSTRUMENT CREDIT, because it is the transferable part:** that lane's first pass read table `listing`
and got 0 for **wsj too**. **wsj was the positive control, and its failure is what caught the wrong table
name** -- a census whose known-good arm reads zero is a broken instrument, not a finding. That is the
control I have been demanding all session, run by someone else, on me.

---

# AMENDMENT 2, 2026-09-25 ~03:1xZ -- THE RESERVED CARD IS STRUCK, AND READING THE PREDICATE FOUND A TAXONOMY DEFECT

I carded to Andrew: *"does `data_status COMPLETE` stay the standard when ft and barrons are unreachable?"*
Before holding it a second time I did what Rule 24 requires of any enum question -- **a word-boundary
token census first** -- and then read the producer's own rule. Both said the card was mis-posed.

## 2a. THE ENUM ALREADY HAS THREE VALUES, AND THE ROW ALREADY CARRIES ITS OWN DENOMINATOR

Census: `data_status` 71 hits / 2077 files. The definition is `publication_gold.py:582-588`:

```
covered = [pub for pub in ENABLED_PUBLISHERS if _covers(publisher_spans.get(pub), day)]
if len(covered) == len(ENABLED_PUBLISHERS):  data_status = "COMPLETE"
elif covered:                                 data_status = "PARTIAL"
else:                                         data_status = "DENIED"
```

And the SAME row writes `publishers_covered` and `publishers_enabled` (`:610-611`). **A consumer can
already read "2 of 5" directly and never has to infer reach from the class.** So the schema change I was
circling -- a value meaning "partial because a publisher is structurally unreachable" -- **is not needed
and would have been a fourth value carrying information two existing fields already carry.**

## 2b. WHY THE CARD WAS MIS-POSED, and the trigger that would make it real

`COMPLETE`'s predicate is **"all ENABLED_PUBLISHERS covered"**. So the real lever is not the word
COMPLETE, it is the membership of `ENABLED_PUBLISHERS`. **Nobody has proposed changing it.** The card
asked Andrew to affirm a status quo against a proposal that does not exist, which is the same shape as
the branch-(a) card I struck an hour ago: **a closed question re-opened by its own adjudicator.**

**RULING:** `ENABLED_PUBLISHERS` is **NOT narrowed to make COMPLETE reachable**. Dropping ft and barrons
would make `COMPLETE` attainable while meaning something different and **looking identical in the data** --
the row would read `COMPLETE` with `publishers_enabled` quietly at 3. That is precisely the
denominator-shrinking move `/self-drive`'s HELD-AT-STOP clause forbids (*"a stop-condition satisfiable by
shrinking its own denominator is not a stop-condition, and the driver is the party that benefits"*), and
the goal's *"complete backfill for all of these securities"* is the standard it would narrow.

**THE CARD IS STRUCK, and the TRIGGER is named so it is not lost:** if any seat proposes removing a
publisher from `ENABLED_PUBLISHERS`, **that** is Andrew's call and is carded then. I do not hold a card
for a question nobody has asked. **Cards at Andrew from this project: ZERO.**

## 2c. THE DEFECT READING THE PREDICATE FOUND -- `DENIED`'s NAME DOES NOT MATCH ITS PREDICATE

`DENIED` reads as *"access was denied"*. Its predicate is **`not covered`** -- zero publishers covered for
that security on that day, **whatever the reason.** So:

- a day on which **every publisher refused** (ft 403, barrons post-auth, bbg challenge), and
- a day on which **nothing was published about the security at all**, a normal quiet day,

**write the identical string.** A reader seeing `DENIED` on a quiet Tuesday concludes access was refused,
and a reader auditing refusals counts quiet days as refusals. This is a Rule 24 **INTENT COHERENCE**
failure: one field is carrying two axes -- *how much was covered* and *why it was not* -- and the name
announces the second while the predicate computes the first.

**It is a finding, not a round-6 blocker**, and the remedy is cheap because the row already carries the
numbers: `publishers_covered` / `publishers_enabled` say how much, so `data_status` only ever needed to
say how much too. **Filed as a row rather than fixed here** -- renaming a served enum value is a
schema act with its own consumers to count, and this analysis does not cut cells.

**And the lesson is one I have now paid for twice in one session:** a metric's NAME is not its
DEFINITION. I nearly proposed a new value for a state the schema already distinguished, against a value
whose name told me it meant something it does not.
