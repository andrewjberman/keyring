# AMGT_HARVST task order -- `HVST-x-2` -- ROUND 9 cell 2 of 2: EXERCISE the timeline on REAL landed gold, and carry the round's JUDGMENT criterion

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-x-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~27</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on the read surface this cell touches; it arms nothing and deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- this cell needs S3 GET on opal-data-harvest's gold chatter_daily and chatter_event. A refusal is a BLOCKING row, never a workaround.
comp-adversary: RUN at L5 -- the adversary is an EMPTY RESULT read as a pass. AC1 exists to name which arm is exercisable BEFORE either is exercised.
</preflight>

## 0. THE STANDING CLAUSES

1. ⛔ **NO VENDOR CALL, and "LOCAL" HERE DOES NOT MEAN "NO NETWORK."** You WILL read our own S3 (Opal-owned, a
   permitted read, NOT a vendor act). **You will make no request to seeking-alpha, bloomberg, wsj, ft or
   barrons, and you will not invoke `lib/opal_data_harvest`'s `run` command at all.** If anything asks you to
   fetch from a publisher, STOP and file a BLOCKING row.
2. **NO S3 WRITE AND NO S3 DELETE, of any kind.** This cell READS gold and writes nothing to the bucket.
3. **NO GOLD BUILD.** Do not run the gold builder. You read what is landed.
4. **Scripts go in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~27/scripts/` --
   **never `.scratch/`**.
5. ⛔ **YOUR proof-of-spec INSTANCE MUST BE NAMED EXACTLY:**
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~27/AMGT_HARVST.TO-HVST-x-2.exercise-the-timeline-on-real-landed-gold.proof_of_spec.json`
   **and its `to_id` MUST be** `AMGT_HARVST.TO-HVST-x-2.exercise-the-timeline-on-real-landed-gold`.
   A gate globs for that exact stem and refuses anything else BEFORE any limb runs (decomp `s.14x`).

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~27/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CELL -- exercise what `w-3` built, on data that actually landed

`HVST-w-3` built `lib/research/harvest/timeline_api.py` and proved its SHAPE and its honest states against
CONSTRUCTED rows. **It was never exercised on real gold, which is why FWD-5 and FWD-6 are still NOT REALIZED.**
This cell exercises it.

⚠ **`timeline_api` IS PURE BY DESIGN** -- its own header: *"the caller hands in the rows (or a loader callable
the caller controls) ... This module never touches `store.py` or any AWS client."* **So YOU supply the loader**,
reading landed `chatter_daily` / `chatter_event` through this project's existing gold reader
(`lib/research/harvest/publication_gold`), and you change `timeline_api` not at all. **It is not in your
`<paths>`.**

## 2. AC1's QUESTION COMES FIRST, AND IT MAY BOUND THE REST OF THE CELL

⛔ **AN EMPTY RESULT IS NOT A PASS, and the issuer has already measured why this is a live risk:**
`publication_gold.EVENT_MIN_PUBLISHERS = 2` and **only `sa` has landed listing rows**, so `chatter_event` can
hold **ZERO rows for every security.** If you exercise FWD-6's arm against an empty set it will look like it
worked while proving nothing -- and the spec even blesses the empty render as "the correct, honest state."

⭐ **AND THE MEASUREMENT NOBODY HAS TAKEN IS YOURS:** round 7 measured **"1 of 89 securities with a non-empty
span"** and **never named WHICH security.** FWD-5 needs a day with `articles_total > 0`. **Name that security
from a read.** If it is NOT `992_HK_Equity` (Lenovo), then the spec's acceptance security and the only
exercisable one DIFFER -- **that divergence is itself the finding and belongs in a surprise row**, not smoothed
over by exercising whichever one happens to work.

## 3. WHAT FWD-5 AND FWD-6 ACTUALLY ASK (from `SPEC_SECTION_timeline.md` s.8 -- read it at HEAD)

- **FWD-5:** the day-by-day line dense from `2026-01-01` with `mention_score` plotted; pick a day carrying
  `articles_total > 0`; the day opens to its article list **ordered strongest first** (tier A before B before C
  before D, `mention_count` descending within a tier), each row showing headline, publisher, tier,
  in-headline/in-lead marks and time.
- **FWD-6:** event runs drawn as marked spans **each carrying its `lead_headline`**; opening one lists its
  articles in the same strongest-first shape.

## 4. BOUNDS

1. **Three criteria: two mechanical, ONE JUDGMENT.** No fourth.
2. **You do not change `timeline_api.py`, `publication_gold.py`, or any producer.** If the exercise reveals a
   defect in either, that is a surprise ROW and you keep working.
3. **Report an unexercisable arm as UNEXERCISABLE with its cause**, never as a pass and never as a failure of
   this cell.
4. **The judgment criterion carries its OUTPUT and NO VERDICT.** `3.0.0_SA_CVO` grades it at L9. Recording
   PASS or FAIL on it is REFUSED by the checker.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical + ONE judgment

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-x-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~27/scripts/ac1_which_arm_is_exercisable.py</invocation><expect>WHICH ARM IS EXERCISABLE, NAMED BEFORE EITHER IS EXERCISED, with denominators. Print: the number of securities carrying ANY chatter_daily row, out of the universe's 89; the number carrying at least one day with articles_total greater than 0, and THE SECURITY KEYS THEMSELVES for those (this is the "1 of 89" round 7 never named); the number of chatter_event rows that exist AT ALL, per security, out of the same denominator; and publishers_distinct's maximum observed value against EVENT_MIN_PUBLISHERS. Then state plainly, in one line each: FWD-5 arm EXERCISABLE or UNEXERCISABLE-and-why, FWD-6 arm EXERCISABLE or UNEXERCISABLE-and-why. A zero anywhere is reported WITH ITS CAUSE -- a bare zero reads as "no problem exists" and fails this criterion</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-x-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~27/scripts/ac2_fwd5_day_dissection.py</invocation><expect>FWD-5 EXERCISED ON LANDED GOLD, or UNEXERCISABLE with AC1's cause restated. If exercisable: name the security used and WHY that one (from AC1's read, not from the spec's assumption); print the dense day span (first day, last day, count of days returned) and prove there is no gap -- days returned equals days in range; pick a day with articles_total greater than 0, print that day's served article list IN ORDER, and prove the order is strongest-first by printing the (signal_tier, mention_count, published_utc) triple per row and showing the sort holds pairwise. Each row must show headline, publisher, tier, mention_in_title and mention_in_lead PRESENT-EVEN-WHEN-FALSE, and time. If the chosen security is NOT 992_HK_Equity, say so explicitly and file a row -- the spec's acceptance security differing from the only exercisable one is a finding, not a detail</expect></criterion>

  <criterion id="AC4" cell_refs="HVST-x-2" judgment="true"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~27/scripts/ac4_are_these_real_bursts.py</invocation><expect>JUDGMENT, PRESENTED AND NOT GRADED -- status UNVERIFIABLE-BY-INSTRUMENT with status_reason naming 3.0.0_SA_CVO at L9 as the oracle. ARE THE EVENTS SHOWN THE REAL COVERAGE BURSTS? For every chatter_event row that exists (if none exist, say so with AC1's cause and present the DAY-level question instead: do the highest mention_score days correspond to days a reader would call a burst?), print the span, its lead_headline, its articles_total and publishers_distinct, and BESIDE IT the headlines of the articles in that span. Then state, per span, whether the lead_headline plausibly names what the burst was about, and where it does not, say what the span actually looks like. Present the counts and the text; record NO verdict of your own</expect></criterion>
</proof_of_spec>

## 6. WHAT THIS CELL DOES NOT DO

It makes no vendor call and does not run the harvest producer. It writes nothing to S3 and builds no gold. It
changes no module. It does not fix anything it finds -- findings are rows.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. ⛔ **THE ANALYSIS CALLED THIS CELL "LOCAL" AND THAT IS RIGHT ON BLAST RADIUS BUT WRONG IF READ AS
   "IN-PROCESS."** `timeline_api` is PURE by design, so exercising it on REAL data requires a loader against
   landed gold -- an S3 READ. That read is Opal-owned and is not a vendor act, but **the order says so
   explicitly** rather than letting a later reader infer "LOCAL" meant no network. `comp-iam` is RUN rather than
   declared-not-applicable for the same reason.
2. **AC1 exists because an empty set passes a naive exercise.** Round 8 refused to cut FWD-6 for exactly this;
   this cell must NAME the exercisable arm before exercising anything.
3. **AC2 requires the security to be NAMED FROM A READ.** Round 7's "1 of 89" was never resolved to a key, and
   assuming it is Lenovo is the error I refused to make in round 8. If they differ, that is the finding.
4. **The judgment criterion is `AC4`, not `AC3`.** The id is kept for continuity with round 7's AC4, which was
   the same question one layer earlier (is the queried symbol corroborated by the row's own content).
5. **s.14x honoured:** all three invocations are single commands with **no shell operators**, so no escaping and
   no mirror-of-an-unrunnable-string. All three name scripts the criterion itself creates, which is s.14x's
   stated non-application for the run-it-first clause.

<risk>LOCAL</risk>
<status>pending</status>
<round>9</round>
<slot>~27</slot>
<fabric>site-z</fabric>
