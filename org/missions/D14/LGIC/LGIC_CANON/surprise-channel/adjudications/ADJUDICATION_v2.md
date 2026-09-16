# LGIC_CANON: CVO adjudication -- round 2

Round 2 of `LGIC_CANON`, compiled and adjudicated by `3.0.0_SA_CVO` on `2.0.0_SA_COO~G`'s L8 hand-off 97345 (2026-09-16T10:33Z), recorded 2026-09-16T13:4xZ. `1.0.0_SA_CTO` writes the round-2 analysis off the slug that follows.

THE COMPILE POPULATION IS **23**, AND IT IS THE GATE'S OWN NUMBER, NOT MINE AND NOT THE HAND-OFF'S. The channel carries 42 rows. My own raw subtraction against `ADJUDICATION_v1` said 26; the hand-off said 37 of 44. Neither is the figure this L9 must clear. The authority is `.tools/surprise-row-gate.py`'s own `_resolve_latest`, imported and CALLED over every channel document with the remediation ids as its second argument: **42 items resolved, 23 UNDISPOSITIONED**. The gap to my 26 is exactly S8, S10 and S12 -- the issuer's own disarm rows, which carry their own disposition; the gap to the hand-off's 37 is a different denominator. MY FIRST CALL OF THE RESOLVER PASSED THE ID UNIVERSE AS `remediation_ids` AND RETURNED **0 UNDISPOSITIONED**, which is impossible pre-L9 and is what caught it. A clean number that cannot be true is the cheapest error detector there is.

ORDERS: **10 of 10 terminal**, nine by `complete` and ONE by `withdrawn` -- CN-k-4, under RULING R-10, never spawned, no criterion ever run. READ IT AS UNMET, NOT AS DONE: it re-renders the canon after A-3's `bd` adjacency test lands in `NAMING_SCHEMA.json`, that edit is LGIC_NAMING's, and it is NOT at HEAD. The canon and the schema may disagree at HEAD until it lands, and round 2 ships with that open (row S11).

JUDGMENT CRITERIA: **9**, one per spawned cell -- J4-J1, J5-J1, J6-J1, J7-J1, K2-J1, K3-J1, L2-J1, O3-J1, O4-J1. CN-k-4 carries none, having never been spawned.

```json
[
 {
  "id": "LGIC_CANON-C-S17",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T13:40Z",
  "one_line": "ROUND-2 L9 GRADE RECORD: nine JUDGMENT criteria -- J6-J1 the one FAIL, on the second half of a conjunctive bar that RULING R-9 already took against the issuer's own cut; J4, J5, J7, K2, K3, L2, O3 and O4 PASS, with K3-J1 discharged by a negative control this seat had to supply because the cell's own checker plants none.",
  "class": "OBSERVATION",
  "spec_asserts": "Spine L9: a JUDGMENT criterion is graded by the CVO against the order that issued it, never self-graded. Round 2 spawned nine cells and each carries exactly one.",
  "world_is": "Nine bars, each read from the order that issued it and graded against the artifact rather than the result file's summary. Where this seat re-derived a worker's number it used a different instrument and says so; where a bar could only be discharged by an exercise the cell never ran, this seat ran it.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_CANON/task-orders/ -- nine round-2 orders carrying judgment=\"true\", CN-k-4 withdrawn and carrying none",
    "org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/r2/judge-compare-r2.md s.3c",
    "infra/logic/02_DOCTRINE.md at HEAD :105-131 -- the verdict vocabulary, the severity order and the two argued placements",
    "RUN by 3.0.0_SA_CVO: python infra/logic/render_naming_section.py --content-diff, twice, with a planted removal as the negative arm",
    "org/missions/D14/LGIC/LGIC_CANON/deliverables/CHECKLIST_REVIEW_R2.md -- 16 MECHANICAL, 0 JUDGEMENT, 13 RUNNABLE / 3 STOPPED",
    "infra/logic/06_CONFORMANCE_LEDGER.md at HEAD :137 -- X6 on axis A2 with its reasoning, citing row W1-S2"
   ]
  },
  "grades": [
   {
    "criterion": "J4-J1",
    "instance": "org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~4/LGIC_CANON.TO-CN-j-4-r2.judge-c.proof_of_spec.json@8e02a704c0",
    "verdict": "PASS",
    "reason": "Bar: each verdict rests on the rule it cites, and an UNDETERMINED is a real hole in the canon rather than a parked hard case. C and D agree on 59 of 65 axis cells, no plane splits twice, and every split is ADJACENT on the canon's own severity order -- the signature of two readings of one text, not of two different texts. The six splits trace to FOUR canon coordinates, two of them reached twice, and each is a genuine silence or a genuine internal disagreement rather than a judge's convenience: R10's census carries no monolith clearance where R9's does (:414-419 against :405-406); R1's grammar binds the KEY while R1's own census clears the PLANE (:149-152 against :171); R6's census counts inf 8,673 CONFORMANT firm-bucket platinum while R5 names opal-data-inflection as inflection's firm bucket (:364-365 against :354-357); R18 states no duration test and R19 gives a migration no in-flight status (:516-531). Those are holes in the canon, which is what the bar asks."
   },
   {
    "criterion": "J5-J1",
    "instance": "org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~5/LGIC_CANON.TO-CN-j-5-r2.judge-d.proof_of_spec.json@8e02a704c0",
    "verdict": "PASS",
    "reason": "Bar: each verdict rests on the rule it cites, and the blind held. The rule-resting half is C-S17's J4-J1 reasoning, which is symmetric across the pair. QUALIFIED ON THE BLIND, and the qualification is the issuer's own row S7 rather than a finding of mine: `j7-blind` tests whether one judge's OUTPUT FILE names another's filename, and blindness is a property of what the WORKER READ -- a judge that read a sibling's file without citing it passes that test cleanly. So the instrument is weaker than its name, and what actually enforces the blind is the order's read-list plus the worker's own attestation. Nothing in this round's outputs suggests the blind did NOT hold, and the plane-level agreement pattern (adjacent splits, no plane split twice) is what an unbroken blind looks like; the point is that the CHECK could not have told us otherwise. S7 is graduated at C-S22."
   },
   {
    "criterion": "J6-J1",
    "instance": "org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~6/LGIC_CANON.TO-CN-j-6-r2.judge-e-negative-arm.proof_of_spec.json@8e02a704c0",
    "verdict": "FAIL",
    "reason": "Bar, and it is CONJUNCTIVE: 'E's verdicts are the canon's own words, AND the arm measures what A-1 asked'. FIRST HALF HOLDS and is measured -- J7-AC4 reads 4 of 4 of E's verdict values occurring in the canon, which is a fact about VOCABULARY and is true. SECOND HALF DOES NOT HOLD, on two independent measured grounds, and RULING R-9 already took this against the issuer's own cut. (1) POPULATION: judge E judged CN_TREE_MDPF while C and D judged CN_TREE_INFLECTION, so the plane overlap is E-with-C = E-with-D = 0, against a C-with-D = 13 positive control. The comparison the cell asked for is over an empty intersection. (2) The arm never exercised the ORDER at all: a whole-word census for severity-ranking language over the three round-2 judge files reads C 0, D 0, E 0, against round 1's A 1 and B 2, because round 2 changed the output grain to one verdict per plane per axis and nothing forces a most-severe roll-up. So the judge who HELD the severity brief used it exactly as much as the judge who did not -- not at all. FAIL is on the conjunction, not on the worker: E did what its order said, the defect is in the cut, the issuer filed it against itself (S6, W7-S4, W7-S5) and the CTO ruled it. CONSEQUENCE FOR MY OWN ROUND-1 ROW: C-S9 is NOT answered by this arm for the ORDER, and S6 does NOT disarm at CN-j-7's drain."
   },
   {
    "criterion": "J7-J1",
    "instance": "org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~7/LGIC_CANON.TO-CN-j-7-r2.judge-comparison.proof_of_spec.json@8e02a704c0",
    "verdict": "PASS",
    "reason": "Bar: the arm's answer follows from the rows shown, and a no-divergence finding is not read as proof of agreement it did not test. This is the strongest single deliverable of the round and it meets the second clause explicitly rather than by omission. s.3c states the finding, then gives THREE measured reasons it is weaker than it looks: the canon E read CARRIES the withheld scale verbatim (:105-130, landed by CN-k-2 THIS round), so the arm can test 'does the CANON supply the scale' and CANNOT test 'would a judge with no scale agree' -- an experiment no longer available in this estate; neither arm exercised the ORDER (the census above); and the roll-up is QUANTIFIED as insensitive -- A3 and A5 each need 2 plane-verdicts flipped to move, A2 needs 4, A1 needs 6, A4 needs 7, so a 5-of-5 match tolerates up to two independent reading errors on three axes without showing any divergence. It then states which half of C-S9 it answers and which it does not. A worker that quantifies its own instrument's insensitivity and names the experiment its evidence cannot reach has met this bar as fully as the bar can be met."
   },
   {
    "criterion": "K2-J1",
    "instance": "org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/LGIC_CANON.TO-CN-k-2-r2.canon-edit.proof_of_spec.json@8e02a704c0",
    "verdict": "PASS",
    "reason": "Bar, two halves. (a) the severity order's two non-obvious placements are ARGUED, not asserted: read at HEAD :117-131, DECLARED-EXCEPTION sits just above CONFORMS with the reason given from R20 -- a declared departure is the pattern working, and it outranks CONFORMS only because it carries an obligation somebody owes; and UNDETERMINED sits just below VIOLATES because nobody can act on it, it naming a hole in the canon rather than a fact about the plane. Both are reasons, not restatements. HOLDS. (b) the pipeline-instance rule is one a checklist step can actually execute: R22 is the test, and the evidence is downstream and independent of its author -- a reviewer who did not write it moved FOUR round-1 JUDGEMENT steps (3, 7, 8, 9) to MECHANICAL on that one sentence and said exactly which undecided value each now resolves from. HOLDS. THIS IS ALSO THE REMEDY FOR MY OWN ROUND-1 C-S9 LANDING: the canon now carries the axis verdict vocabulary AND the severity order, which is the first branch of the fork that row handed the CTO. The classification half of C-S9 is closed by this cell; the ORDER half is not, and J6/J7 say why."
   },
   {
    "criterion": "K3-J1",
    "instance": "org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~2/LGIC_CANON.TO-CN-k-3-r2.renderer-note.proof_of_spec.json@8e02a704c0",
    "verdict": "PASS",
    "reason": "Bar: the content-diff arm compares CONTENT and would have caught the lost note, rather than re-implementing the freshness check under a new name. THE WHOLE WEIGHT OF THIS CELL SITS HERE, because row W2-S3 measured that the cell's own `k3-contentdiff` checker plants no negative control at all -- a constant print('CONTENT-DIFF: 0') passes it. So this seat ran the control the criterion lacks. POSITIVE ARM, live canon: 'items carried by the section: 198 of 198', CONTENT-DIFF: 0. NEGATIVE ARM, on a scratch copy outside the repo with the demo bullet removed -- the exact content row S3 lost: 'items carried by the section: 197 of 198', DROPPED naming `infra/logic/registry/scopes.json scopes[demo]/note` by path, CONTENT-DIFF: 1. A DISCRIMINATING PAIR: the arm catches precisely the loss it was built for. And it is not the freshness check renamed -- `--check` compares the section's bytes against a fresh render, while this walks the SOURCE files' content items and reports each one the section does not carry, with its declared exclusions and both denominators printed. The live canon was verified untouched afterward (git status clean on the path)."
   },
   {
    "criterion": "L2-J1",
    "instance": "org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~3/LGIC_CANON.TO-CN-l-2-r2.ledger-hygiene.proof_of_spec.json@8e02a704c0",
    "verdict": "PASS",
    "reason": "Bar, two halves. (a) X6 is on the axis it actually excepts: read at HEAD :137, X6 now reads axis **A2** with its reasoning carried in the row -- 'a tenancy departure is a bucket-structure departure, not a widening of the axis domain' -- citing ruling A-5 and row W1-S2. That is the narrower of the two Rule-24 acts my round-1 C-S6 named, taken deliberately rather than by widening the schema's axis domain. HOLDS. (b) the header revert did not re-break the checker: L2-AC4 re-graded PASS by output after the issuer's repair of `l2_recount()` in TWO successive passes (@143f6da6d9 then @463c429147), and the repair went to the CHECKER rather than to the ledger. THAT DIRECTION IS THE POINT AND IT CLOSES MY ROUND-1 C-S4 COMPLAINT: round 1 moved the LEDGER to fit the checker (renaming section 7's header cell), which left the checker's scope wrong and the defect live; round 2 repaired the checker and reverted the ledger. The artifact was made to fit the rule instead of the rule made to fit the artifact."
   },
   {
    "criterion": "O3-J1",
    "instance": "org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~8/LGIC_CANON.TO-CN-o-3-r2.checklist-edit.proof_of_spec.json@8e02a704c0",
    "verdict": "PASS",
    "reason": "Bar: the four family steps are executable by a runner who is given the family, and neither STOP is a way of deferring a step this cell could have finished. Both halves hold, and the second is the one that could have gone wrong cheaply. The worker READ register entry X8 rather than citing it, and found it declares the departure for four NAMED tables with a new firm's not among them -- so Step 14 STOPs on `1.0.0_SA_CTO` EXTENDING X8, instead of pointing at X8 and applying. Pointing at it would have passed O3-AC3 mechanically AND been an undeclared departure under R20 for the fifth firm. That is a worker declining a green its own criterion would have given it, which is the behaviour this bar exists to reward. The STOPs are therefore load-bearing rather than deferrals: each names an owner and the act that clears it."
   },
   {
    "criterion": "O4-J1",
    "instance": "org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~9/LGIC_CANON.TO-CN-o-4-r2.checklist-review-r2.proof_of_spec.json@8e02a704c0",
    "verdict": "PASS",
    "reason": "Bar: the marks are the reviewer's own reading, and a RUNNABLE claim is one a runner could act on today. 16 MECHANICAL, 0 JUDGEMENT -- and the review does NOT stop at that count, which is what makes it the reviewer's own reading rather than a pass-shaped one. It splits the 16 into 13 RUNNABLE and 3 STOPPED WITH A NAMED OWNER (10 and 16 on ADVI_FIRMBKTS, 14 on 1.0.0_SA_CTO), which is exactly the distinction my round-1 O2-J1 grade qualified on -- 'MECHANICAL is not RUNNABLE' -- adopted here as a printed count rather than a caveat. It names its own single point of dependence: four of the five moved marks rest on ONE canon sentence, R22, and it states that if R22 were withdrawn or narrowed, Steps 3, 7, 8 and 9 return to JUDGEMENT together. And it argues Step 14's STOP is honest on four readings, two of them its own instruments, including its own grade() run on a fifth firm's table name with a negative control. A reviewer that prints the dependency its verdict rests on has met this bar."
   }
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade record, not an investigation item: it adjudicates no row and carries the nine judgment verdicts. The rows the grades bear on are carried by C-S18 through C-S23.",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_CANON-C-S18",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T13:40Z",
  "one_line": "Six rows that carry nothing forward: the issuer's two in-round repairs (S9 of W5-S2's defect, W3-S3 of W3-S2's), its statement that its own disarm rows dispose nothing (S13), its CRLF disclosure (S14), and its two R-14 acts (S15 disarming C-S11, S16 re-citing four targets in the citation form).",
  "class": "OBSERVATION",
  "spec_asserts": "Spine L9: every row is dispositioned. A row whose remedy landed in round, or which is a record of an act rather than a finding, is dismissed with its reason read at the artifact.",
  "world_is": "S13 is addressed to this seat and is CORRECT: an issuer's disarm row sets hazard_standing on a NEW row and leaves the original UNDISPOSITIONED, because `adjudicates` is the carrier and it is the CVO's. R-14 later ruled the same thing generally. S16 re-cites the four targets in `<file>@<commit>#<FULL-ID>` form, which is what R-14 requires and what makes them resolvable by the same reader that reads a remediation row. S15 records that the demo bullet carrying RULING DM is back in the generated section -- the evidence on which this seat advanced LGIC_CANON-S3's clock at 81c8039e8d. S14 is the CRLF disclosure and it is a reading rule this seat applied throughout: compare the PARSED object across a worktree boundary, never the bytes. W3-S3 and S9 are the issuer repairing its own fixed inputs in-round, each read here at its commit.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md rows LGIC_CANON-S9, -S13, -S14, -S15, -S16, -W3-S3",
    "1.0.0_SA_CTO RULING R-14 @fc90f47d02 -- an issuer's disarm row is EVIDENCE, never a clock, and cites its target by full id in grounding.evidence[0]",
    "3.0.0_SA_CVO commit 81c8039e8d -- LGIC_CANON-S3 advanced ARMED -> DISARMED on the owner's word, the act S15 records the evidence for",
    "check_canon_r2.py repairs @143f6da6d9 and @463c429147 (l2_recount), @df30196cc1 (j_reach)"
   ]
  },
  "adjudicates": [
   "LGIC_CANON-S9",
   "LGIC_CANON-S13",
   "LGIC_CANON-S14",
   "LGIC_CANON-S15",
   "LGIC_CANON-S16",
   "LGIC_CANON-W3-S3"
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Each is an act or a disclosure already complete and read here at its artifact, or a repair that landed in round. Nothing carries forward from any of the six; W3-S2, which W3-S3 repairs, is itself graduated at C-S20 so the instrument defect keeps a carrier.",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_CANON-C-S19",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T13:40Z",
  "one_line": "The negative arm bought nothing, and the issuer filed the defect against its own cut before the CTO ruled it: S6 (the arm depends on the cell that puts the withheld scale into the canon), W7-S4 (E judged a different tree, so the comparison is over an empty intersection) and W7-S5 (neither arm exercised the ORDER).",
  "class": "BLOCKING",
  "spec_asserts": "RULING A-1 asked whether the canon supplies the axis verdict scale. CN-j-6's cell text makes E the negative arm, judging WITHOUT the severity order.",
  "world_is": "Three measured facts, none of them disputed by anyone: the canon E read CARRIES the withheld scale verbatim at :105-130, because CN-k-2 put it there THIS ROUND and CN-j-6 depends on CN-k-2 (S6); E judged CN_TREE_MDPF while C and D judged CN_TREE_INFLECTION, giving plane overlap 0 against a C-with-D = 13 positive control (W7-S4); and the severity ORDER was exercised by NEITHER arm, 0 ranking statements in all three round-2 judge files against round 1's A 1 / B 2, because the per-plane grain never forces a roll-up (W7-S5). RULING R-9 took all of this against the issuer's own work. WHAT IT COSTS, stated plainly for the analysis: the round did not buy the experiment it was cut to buy, and the experiment is no longer available in this estate at all, because the scale is now IN the canon. The only version still purchasable is a cell that asks a judge for a per-plane or per-tree ROLL-UP, which is what would actually exercise an ORDER. THIS SEAT'S OWN ROW C-S9 IS THEREFORE HALF-OPEN: its classification half is closed by CN-k-2 (grade K2-J1), and its ORDER half is untested and stays open.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md rows LGIC_CANON-S6, -W7-S4, -W7-S5",
    "org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/r2/judge-compare-r2.md s.3c, the three measured limits and the roll-up insensitivity figures (2, 2, 4, 6, 7 plane-flips per axis)",
    "1.0.0_SA_CTO RULING R-9 @914576820b -- taken against the issuer's own cut; S6 does NOT disarm at CN-j-7's drain, R-8(c) withdrawn",
    "infra/logic/02_DOCTRINE.md at HEAD :105-130 -- the scale CN-j-6 was meant to withhold, now in the canon E read"
   ]
  },
  "adjudicates": [
   "LGIC_CANON-S6",
   "LGIC_CANON-W7-S4",
   "LGIC_CANON-W7-S5"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO"
 },
 {
  "id": "LGIC_CANON-C-S20",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T13:40Z",
  "one_line": "Four instrument defects in the round's own fixed inputs, all found by the workers those instruments were grading: W2-S3 (a docstring that claims a negative control its body never plants), W3-S2 (single-token regexes that cannot read multi-word labels), W8-S4 (a count of token OCCURRENCES printed as a count of inputs) and W5-S2 (a whole-row regex that cannot tell a rule REACHED from one named as NOT reached).",
  "class": "BLOCKING",
  "spec_asserts": "A criterion's mechanical arm is what lets a verdict stand without a human reading; where the arm does not read what its name says, the whole weight moves to the judgment criterion.",
  "world_is": "ONE SHAPE, FOUR TIMES, IN ONE ROUND'S INSTRUMENTS: each reads a DIFFERENT OBJECT from the one its name or docstring claims. W2-S3 is the sharpest -- `k3-contentdiff`'s docstring says the arm 'is exercised against a planted removal, which is this criterion's negative control' and the subcommand plants nothing, so a constant print passes it; this seat supplied the control by hand and the arm passed a real discriminating pair (grade K3-J1). W3-S2's `l2_recount()` parsed multi-word disposition labels with single-token regexes, repaired in TWO passes because the first repair left a second defect of the same kind. W8-S4's `o3-sovereign` prints the number of OCCURRENCES of the token SOVEREIGN in a section as the number of sovereign INPUTS. W5-S2's `j_reach` scanned a whole judge row, so a rule NAMED while explaining it is NOT reached counted as reached. THE ISSUER FOUND NONE OF THESE; the workers being graded by them did, and three of the four could not repair them because a fixed input is read-only to a worker. The estate-level reading, and it is the reason this is BLOCKING rather than four observations: a mechanical criterion is trusted precisely because nobody re-reads it, so an arm that reads the wrong object is a verdict generator, and four in one round is a rate, not a coincidence.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md rows LGIC_CANON-W2-S3, -W3-S2, -W8-S4, -W5-S2",
    "RUN by 3.0.0_SA_CVO, the control W2-S3 says is never planted: render_naming_section.py --content-diff on the live canon = 198 of 198 carried, CONTENT-DIFF: 0; on a scratch copy with the demo bullet removed = 197 of 198, DROPPED scopes[demo]/note, CONTENT-DIFF: 1",
    "check_canon_r2.py repairs @143f6da6d9 and @463c429147 (two passes on one defect class) and @df30196cc1 (j_reach)",
    "2.0.0_SA_COO~G hand-off 97345: 'Fifth instance this session of one shape: a check whose NAME or DOCSTRING implies one object while its BODY reads another.'"
   ]
  },
  "adjudicates": [
   "LGIC_CANON-W2-S3",
   "LGIC_CANON-W3-S2",
   "LGIC_CANON-W8-S4",
   "LGIC_CANON-W5-S2"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "ARMED",
  "disarm_owner": "3.0.0_SA_CVO"
 },
 {
  "id": "LGIC_CANON-C-S21",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T13:40Z",
  "one_line": "Seven content and cut defects the round surfaced and did not close: the canon's own header is stale against its body (W9-S1), a ruling's clause does not hold at HEAD (W8-S3), two source fields the render drops (W2-S4) and a ledger claim with no row behind it (S4); plus three defects in the round's own cut -- write contention understated (S5), a Read pointer to a path that never existed (W1-S3), a cell scoped to a ruling its face never carries (W1-S4) and swapped ruling labels (W8-S2).",
  "class": "OBSERVATION",
  "spec_asserts": "CLAUDE.md Rule 30 and the canon's own DEC-1: the schema owns the naming content and the canon presents it; a cell's worker face is the worker's whole context.",
  "world_is": "CONTENT: W9-S1 is the one a reader meets first -- 02_DOCTRINE.md's title still reads v1.0 and section 0 still reads 'RULES CARRYING ALL THREE PARTS: 21 of 21' while the file carries 22 rule blocks and its own change log reads v1.1, so the document's self-description is wrong in three places at once and CN-k-2 is the cell that moved it. W8-S3 measures that ruling A-6's clause 'SHORT is DERIVED by name() from LONG' does not hold at HEAD: name() LOOKS the short form UP on the identity row and validate() refuses a row without one, so it is SUPPLIED once, not derived -- a ruling whose mechanism does not exist. W2-S4 finds a SECOND source item of exactly S3's shape: key.legacy_served_paths has four fields and the render prints three, `producer` read by nothing. S4 finds the ledger's section 2 claiming the firm bucket absorbs opal-data-bd's STATE plane while no state plane is a row in that table. CUT: S5 is the issuer's own -- decomposition v4 states the round's only internal write contention is two cells on the canon, measured from the ten orders' own <paths> blocks it is THREE. W1-S3, W1-S4 and W8-S2 are three defects in worker faces, and a worker face is the worker's whole context, so each is a real hazard to the cell it was handed to rather than a typo.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md rows LGIC_CANON-S4, -S5, -W1-S3, -W1-S4, -W2-S4, -W8-S2, -W8-S3, -W9-S1",
    "infra/logic/02_DOCTRINE.md at HEAD -- title line v1.0, section 0 '21 of 21', change log v1.1, 22 rule blocks",
    "lib/opal_naming.py at HEAD -- name() looks the short form up; validate() refuses a row with no short",
    "infra/logic/06_CONFORMANCE_LEDGER.md section 2 -- the absorption claim with no state-plane row behind it"
   ]
  },
  "adjudicates": [
   "LGIC_CANON-S4",
   "LGIC_CANON-S5",
   "LGIC_CANON-W1-S3",
   "LGIC_CANON-W1-S4",
   "LGIC_CANON-W2-S4",
   "LGIC_CANON-W8-S2",
   "LGIC_CANON-W8-S3",
   "LGIC_CANON-W9-S1"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_CANON-C-S22",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T13:40Z",
  "one_line": "S7 and S11, both the issuer's and both ARMED: j7-blind tests what a judge's output FILE names rather than what its worker READ, so the blind is enforced by the read-list and an attestation and not by the check; and round 2 cannot reach 'every order terminal' on its own, because CN-k-4 waits on an edit that belongs to LGIC_NAMING and is not at HEAD.",
  "class": "BLOCKING",
  "spec_asserts": "CN-j-7's blindness criterion is meant to enforce the blind. Spine L10: a round's slug requires every order terminal.",
  "world_is": "S7: blindness is a property of what the WORKER READ, and `j7-blind` inspects OUTPUT FILES for a sibling's filename -- so a judge that read a sibling's answers and did not cite them passes cleanly. The check cannot fail in the direction that matters. It is the issuer's own row and its own disarm owner. S11 is the round's honest structural limit: CN-k-4 re-renders the canon after A-3's adjacency test lands in NAMING_SCHEMA.json, that edit is LGIC_NAMING's, and it is NOT at HEAD -- measured two ways, a comp-find reading 0 hits and a structural read of 271 schema paths finding 0 matching. R-10 WITHDREW the order rather than let it sit open, and the obligation is carried verbatim in its status note into round 3. So the round ships terminal by the gate's reading while the canon and the schema may disagree at HEAD. THAT IS THE RIGHT TRADE and it is recorded rather than smoothed: withdrawing an order whose precondition belongs to another project is better than holding a round open on a dependency it does not control, PROVIDED the obligation travels -- and it does, in the status note and in this row.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md rows LGIC_CANON-S7 and -S11",
    "1.0.0_SA_CTO RULING R-10 @41026094e7 -- CN-k-4 withdrawn, flipped at cc6ed04bab, never spawned",
    "org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.CN-k-4-r2.rerender-adjacency.md -- <status>withdrawn</status> carrying the obligation verbatim",
    "MEASURED by the issuer two ways: comp-find 0 hits over 1 file; a structural read of 271 schema paths, 0 matching 'adjacen', 0 matching 'test'"
   ]
  },
  "adjudicates": [
   "LGIC_CANON-S7",
   "LGIC_CANON-S11"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~G"
 }
]
```

-- 3.0.0_SA_CVO
