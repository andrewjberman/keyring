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

## Open at close

Andrew's disclosure package (the only sovereign item). Then: Leg A apply, Leg B on his word,
T2.C schema gate, shell census, converter lag, cross-tree divergence census, BR1 Phase A brief.
