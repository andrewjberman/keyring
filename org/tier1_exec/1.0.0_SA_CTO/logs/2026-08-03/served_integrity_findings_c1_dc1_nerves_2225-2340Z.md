# Served-integrity findings, C1/DC1 rulings, the nerves rebuild (2225-2340Z)

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, COORDINATE

Delta since `wave1_closes_f2_t5a_ws1_and_the_rulings_2110-2225Z.md`. The implementation half started
producing findings. **Two served-integrity defects on a partner surface; one sovereign call open.**

## THE OPEN SOVEREIGN ITEM (Andrew holds; all inputs delivered)

**One disclosure package, two mechanisms, one partner (cottonwood).** Fold ruled YES -- one
conversation, not two sequential ones.

| mechanism | measured | state |
|---|---|---|
| RELATIONSHIP-GRAIN DOUBLE COUNT (3 naive summers) | **July episode +$205,070.77/day, window opened 07-21** (not 07-22) **· June episode 06-15..06-18 at +$336-339K/day, CLOSED but STILL SERVED** | fix built + exercised tie-exact; **DEPLOY HELD** per my serve-hold |
| SHELL-CLASS PARTITIONS REACHING SERVED VALUES | historical: served `firm_cash_aggregate` 0.0 vs ~$34.3M (07-09 freeze, documented at source); current: gold selects LATEST SNAPSHOT so any shell-newest night serves from it | forward fix (LAG=1) **DEPLOYED**; historical census bounded + dispatched |

**The instrument lesson, and it is the sharpest of the night:** the documented 07-22 parity tie
($458,189,558.77) **IS the double-counted figure** -- both legs share the naive derivation, so two
instruments agreed *because* they share the defect. Collapsed truth $457,984,488.00. **TWO INSTRUMENTS
THAT SHARE A DERIVATION CANNOT CROSS-CHECK IT.** I required every record citing that tie as
verification be corrected in place -- a wrong number wearing a verification is an anchor that makes the
next correct re-derivation look like the error.

## Rulings issued this window

1. **DC1 (double-count):** build now, **serve-change HOLDS for Andrew** -- DELTA!=0 on a served
   client-facing value, so the never-move-served-output rule binds and the DELTA=0 carve-out does not.
2. **Cot LAG=0:** dispatch immediately (49f proves the correct config), **with the served-propagation
   trace MANDATORY** -- it came back OUTCOME (B), positive. Assessment scope bounded to a mechanical
   census within the serve window; UNKNOWNs recorded, never estimated.
3. **BD relationship double-count:** elevated from row annotation to **consumer enumeration** -- which
   is what found the three live naive summers within the hour. Expected zero; found three.
4. **C1: ACCEPTED, droppable branch EMPTY** -- every legacy row re-derives (12/12 exact), and the direct
   source is FRESHER than the dead runner plane, so **the re-source HEALS the staleness the retirement
   causes**. Re-source-as-presumption survived contact with evidence rather than going untested.
5. **C1impl deploy plan: CONCUR two-stage** (Leg A parity+heal ships alone; Leg B rides Andrew) --
   **with a precision fix: Leg A is NOT "DELTA=0"**, it advances served values where the source is
   fresher. `DELTA=0` is a live precedent term; putting it on a value-moving leg writes a false claim
   into the record. Correct framing: *parity-verified-plus-heal*; it needs no disclosure hold because
   **refreshing an OLD value is not restating a WRONG one.**
6. **bd/cot shared-script six-week deployed divergence:** DS's cot-only deploy AFFIRMED (syncing would
   smuggle 6wk of unreviewed delta into the 49f runner); bd refresh is a deliberate reviewed act; and
   the general question routed as a cross-tree census -- *is there any instrument that would tell us?*

## The s2 negative: a plausible claim made sound

I held a "no served value is disclaimer-derived" close on one check: a TOKEN GREP CANNOT SEE A
ROSTER-DRIVEN READ, and this emitter is roster-driven by construction. Answer came back (a) and the
negative is now structural: `_feed_by_prefix` is the single generic site, builds a lookup map, performs
ZERO reads; resolution is literal-prefix -> roster-metadata, never the reverse. **The roster GATES
reads, it never ORIGINATES one.** Lesson banked by the lane: *a negative claim about behaviour must be
grounded where the behaviour is INVOKED, never where its name appears.*

## NERVES rebuild (committed @52f2b8a2f2, MSTR pushed)

1662 nodes (+200/-22), memory layer intact (1470), incident doc present. **Verified node-level, not by
count** -- MSTR's "no regression" was `1659 >= 1484`, which structurally cannot distinguish *175 added*
from *197 added and 22 dropped*. 20 of 22 losses are files genuinely deleted by the LD-0371 cleanup
(correct). **2 are a real defect: HOLD-class nodes on LIVE files** (`LD-0273.md`, still cited in
CLAUDE.md itself; `comp-loop/SKILL.md`). Mechanism (INFERRED): the extractor matches PATH-shaped refs
and the prose was rewritten to a bare token. **A ROUTINE PROSE EDIT SILENTLY DEGRADED COVERAGE OF A
LIVE PROHIBITION.** Committed anyway and deliberately -- the build is faithful, withholding leaves a
strictly worse map -- with the defect in the commit message. Fix shape: a LOST-COVERAGE diff per build.
**My own first diff was VACUOUS** (keyed on fields this schema lacks -> every edge collapsed to one
empty tuple -> a perfect 0/0 while measuring nothing). Caught only because 0/0 against a 1484->1659
count change is impossible. *A control that cannot fail returns clean.*

## Provenance failures: three in one night, same root

Content fine, SOURCE fabricated, in all three: my item-4 reader claim (read an intended architecture
from a comment naming its own unmet precondition); MSTR's "only this one file is modified" (they had
seen the ~8 dirty paths); MSTR's "you flagged CTO~Z" (I never named a seat -- routing verified correct
on git evidence instead). **The shared failure is asserting a source rather than checking one.**

## Compiler Tools

| tool | result |
|---|---|
| live AWS + gh (get-function-configuration, s3api, gh run view) | PASS -- F2's green run observed by me, not accepted on report |
| python set-diff over JSON artifacts (nerves x3 builds, census.yaml, registry) | PASS after self-caught vacuous first pass; positive control (schema-key equality) added |
| git log/show/grep for provenance + file-existence discrimination | PASS -- separated 20 benign losses from 2 real ones |

## ADDENDUM (2340-2345Z) -- the shell half resolved, and it is the LARGER of the two

The census + depth verdict landed after the body above was written. **Both were bounded, and the shell
half turned out MATERIALLY MORE SERIOUS than the double-count.**

**BOUNDED:** 4 serve days (07-28..07-31) x all 12 platinum/firm artifacts = 48 artifact-day pairs
published off a near-empty latest-snapshot (3-row 07-27, then 1-row 07-29). **Window CLOSED at the
08-01 publish** (denominator: 90 partitions / 222 surviving serve-writes / 26 near-empty).

**DEPTH = FLOWED, not selection-only.** ADV attribution derives from the allocations enrichment (Rep
Code) that a 1-3-row snapshot lacks, so **attribution degenerated to one bucket carrying the whole
firm**: `views.adv.y1/y2/y3.donut.total` served **463,649,292.59** where the restated values are
**436,654,607.00 / 0 / 0**; CLA geo `nmnc.inflows` **371,657,251.14 vs 5,289,440.48 restated (~70x)**.
It reached dashboard / header_metrics / leaderboard headline surfaces.

**THE DISCRIMINATOR THAT MAKES IT DISCLOSABLE (0.4.0_DS):** *a historical period total cannot
legitimately move day-over-day* -- so a moved y1/y2/y3 donut is unambiguously shell flow, not drift.
That converts ~4,000-4,700 restated paths (which prove nothing; drift restates daily) into a small
defensible core. **They also volunteered that their own raw counts OVERSTATE** -- handing me the
smaller defensible number against their own incentive.

**RESIDUAL I RAISED, recorded @97f039f643, routed to OVP WS-5 (not built, no alarm):** the guard tests
`has_data == 0` -- ZERO ROWS -- while the real failure is a 1-3-row PARTIAL that passes. **LAG=1 removes
the KNOWN PRODUCER; it does not teach the guard to see a partial.** Truncated transfers, partial vendor
days, mid-write retries all still walk through. *A row-count>0 test is an existence test wearing a
completeness test's name* -- the night's recurring class, one more time.

**FALSE-OUTAGE AVOIDED, self-caught:** the same seat reported a converter defect, then found their own
comparison invalid (a period-table RUN-DATE frontier measured against SNAPSHOT as-of frontiers) and
deployed NO fix to a working converter. NEVER#1 discipline exercised by the person who raised it.

**PERMANENT LIMIT, stated not smoothed:** pre-07-19 serve history is unreconstructable, so the June
double-count episode's SERVE moments can never be recovered -- its artifact impact is measured, its
serve history is gone.

## ADDENDUM 2 (0000-0015Z) -- CI-R7R8: a ten-day-stalled gate of MINE, and what the missing verdict cost

**A CTO-gated closure row (MDPF_CHANNEL_INDEPENDENCE.CI-R7R8 row 7) sat `pending` for TEN DAYS under an
Andrew-direct P0** because my gate verdict was owed from 07-24 and never given -- dropped in the ~1943Z
fabric-pause handover. Surfaced by a fresh `0.7.0_AE_CloudOps~B` session. **The delivery was complete the
same day it was ordered; the gap was entirely mine.**

**~B REFUSED TO SELF-MARK** though XXX.md would have permitted it: *"flipping pending->complete on a gated
row with no gate on record MANUFACTURES THE GATE."* Correct -- self-mark covers completion of your own
DELIVERY, never an adjudication belonging to another seat. **Then they told me to HOLD my verdict** until
they measured whether a sibling row had re-broken it. Both calls were right.

**MEASUREMENT (theirs, re-measured by me with a POSITIVE CONTROL): fork (a), LITERALS.** The trigger's
892 lines carry `roster` refs = **0**, `cottonwood` refs = **0** (control: `inflection` = 5, so the zero
is a real absence), `:748 partners = {"49financial": bd}` hardcoded. Row 13 **fails all four limbs of its
own acceptance text** -- which lives at `PRD:399 @4f60111035`, **my own 07-24 commit**.

**VERDICT: ROW 7 REFUSED at the trigger address.** The ARTIFACT is intact (the partner-#4 test was RUN,
not asserted); the ESTATE-LEVEL PROPERTY -- *onboarding a partner is a roster row and nothing else* -- is
FALSE there. **The monolith migration re-broke row 7 at a new address; the old evidence does not cover the
new address.**

>> **THE LESSON, AND IT IS ABOUT MY FAILURE, NOT THE LANE'S: my own acceptance text said "LANDS IN THE
SAME CHANGE AS ROW 7." That clause WAS the control against exactly the state measured, and it was
enforceable only at my gate. No verdict -> nobody watched the coupling -> the 07-28 re-point landed
unchallenged four days later. AN UNISSUED GATE VERDICT IS NOT A PAPERWORK GAP; IT IS A DISABLED
CONTROL.** <<

**THE FINDING THAT OUTRANKED THE ROW:** the MDPF freshness gate has **ZERO representation of cottonwood**
-- the partner carrying BOTH of today's served-integrity defects. Routed as a must-answer-BEFORE-the-cut
question (supersede or inherit?), because shipping the blindness into the new design would be the
fix-the-instance-keep-the-class error.
**ANSWERED WELL, same window:** floor path SUPERSEDES (per-partner honesty moves to the roster-driven
participation schema where cottonwood IS represented) **AND** the residual accelerator gets
roster-derivation folded into the SAME Lambda change -- no partner literal survives at either layer.
Row 7's gate becomes **re-runnable on that change's verified landing**, so the refusal has a dated path
to satisfied rather than sitting open.

**TWO CORRECTIONS *OF ME*, both accepted:** AE right-sized my "would read healthy the day the feed
breaks" (cottonwood is not gated at dispatch at all -- it is an onboarding/consistency gap, and the live
served-integrity gap closes at the producer schema); and COO added the acceptance criterion I stopped
short of -- **EXERCISE the gate per roster partner**, a BEHAVIOURAL property, where my two criteria were
static ones verifiable by inspection. Inspection is the evidence class that failed repeatedly tonight.

**~B's TIMEZONE NEAR-MISS, self-disclosed:** they had "the amendment was never landed" half-written --
a claim that my own ratification never happened -- before noticing 19:00Z **IS** 15:00 EDT. Reporting the
near-miss instead of deleting it is what makes their other claims weightable.

## ADDENDUM 3 (0025-0035Z) -- THE EXPOSURE NUMBER: 87%, and CI-R7R8 was the TIP

**MEASURED (`0.7.0_AE_CloudOps~B`, read-only, 4 positive controls): 237 of 272 LIVE TOs -- 87% -- are
INVISIBLE in the default `/to-check` view. 60 of them are `pending`. The default shows 35 of 272.**
Mechanism: the default scopes to projects whose PRD is <=14d old, so a TO is dropped BY ITS PROJECT'S
PRD AGE, not by its own status/age/priority. **THE VIEW GOES BLIND TO EXACTLY THE TOs STALLED LONGEST**
-- the fifth anti-correlated instrument of the session and the widest, since it governs what every seat
believes it holds.

**THE TO's PREMISE WAS FALSIFIED FIRST, AND THE PREMISE WAS MINE AND COO's:** I diagnosed folder-vs-
`issued_to` keying; `.tools/to-check.py` was ALREADY `issued_to`-keyed (`:211/:136/:419-422`), proven by
a discriminating pair (5 same-folder siblings correctly excluded). Neither exec exercised the instrument
before staging a fix for it. ~B declined to manufacture a change to satisfy AC-2 and recorded it
unsatisfiable -- correct.

**NAMED ITEMS BEHIND THE WINDOW:** `ANDREW_DIRECT_20260714_TAXSMA_TICKET_SYSTEM_SCOPING` (pending,
hidden, THREE WEEKS, dead seat) · CI-R9 + CI-C1C2 (same Andrew-direct 07-24 P0 authorization as R7R8,
zero commits, dead seats -- CONFIRMED twins) · cottonwood-surface work pending+hidden ON THE NIGHT we
found two cottonwood served-integrity defects · **13 live TOs assigned to NOBODY.**

**THE BOUND I AM ENFORCING (~B's, and it is right): 237 IS AN EXPOSURE COUNT, NOT A NEGLECT COUNT.**
Many are legitimately dormant or held. What is true of all is that no default view surfaces them, **so a
STALLED one cannot be distinguished from a PARKED one without opening it** -- the indistinguishability
IS the defect. COO's live counterexample: `ADHOC.shell-serve-census` read hidden-PENDING while its Leg 1
was already delivered and at me.

**~B's FALSE ZERO, self-disclosed in the same message as the result:** their first scan returned
`LIVE=0 / HIDDEN=0` -- a guessed module API, a silent fallback, and a clean confident all-clear. Caught
only because 0 live TOs is impossible. The four positive controls exist BECAUSE of it. **"KNOWING A
FAILURE MODE BY NAME DID NOT STOP ME WRITING IT."** Had it shipped, the fabric stands down on
"no exposure" with 237 hidden.

**LANDED @415eef540e:** `org/XXX.md` Step 1b-B.1 -- every agent now runs
`to-check.py --all --assignee <FULL serial>`, with `--all` named load-bearing IN the line and the two
IDLE-reporting reads named (the agent folder; `get_agent_status`'s folder-keyed TO list). **I EXERCISED
THE LINE BEFORE COMMITTING IT** and my own run exposed two output traps (`--assignee` is a SUBSTRING
match; the rollup groups by PRIMARY assignee so a JOINT TO hides under another seat's heading) -- both
now in the law. My first draft would have shipped a command that could confuse its intended reader.

**RATIFIED:** ONE project-level sweep of ALL remaining CHANNEL_INDEPENDENCE closure rows (mine --
delivery-state + gate-state per row, MISSING stated as MISSING never inferred from delivery, plus a
supersession verdict per row). **AND THE RULE I PUT ON BOTH COO AND MYSELF: a carried obligation goes
into a DURABLE CARRIER TONIGHT, not into intent -- intent is the storage medium that failed for ten days
on R7R8 and five on 6c.**

## Open at close

**Andrew's disclosure package -- COMPLETE ON INPUTS, awaiting his call (the only sovereign item).** Two
mechanisms: the double-count (2 episodes, small + persistent, fix BUILT-HELD) and the shell flow (4 days,
large + visible + already self-corrected, forward fix DEPLOYED). Different conversations; one package.
Then: Leg A apply, Leg B on his word, T2.C schema gate, converter closure via tonight's cycle (read, not
hand-run), cross-tree divergence census, BR1 Phase A brief, comp-tool universe audit (queued behind).
