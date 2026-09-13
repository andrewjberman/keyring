# IRPT_FNTEND ROUND 4 -- L8 COMPILE AND L9 ADJUDICATION

**Author:** `3.0.0_SA_CVO` (Chief Validation Officer). **Input:** `2.0.0_SA_COO~F`'s drain-end packet (msg 96384):
five orders drained -- FE-s-25, FE-s-26, FE-s-27, FE-s-28 issued, FE-s-18 carried. **Push state:** LOCAL; this seat
does not push. **Pause:** lifted for both IRPT projects by Andrew, card 1, `c6be748be7`.

**Every figure below is this seat's own read** unless it is marked as another seat's. The COO's packet was treated
as input to re-derive, not as a verdict to inherit: every order's `<status>` was read (5 of 5 `complete`), every
proof instance read (every mechanical row PASS, exactly one judgment row each naming this seat), every manifest PNG
viewed, and the portal read at the drained vintage `c2eb8eb4` through `git show` because its worktree carries 16
dirty paths.

---

## 0. SCOPE, AND DEBT THIS SEAT OWNS

**L10 is read PER ROUND.** The spine defines L8's input as "new investigation rows ... and no others", so this
record compiles and dispositions round 4's rows, and the slug that follows closes round 4.

**ROUNDS 2 AND 3 REACHED L10 WITHOUT THIS SEAT'S L8/L9.** `1.0.0_SA_CTO` wrote both round analyses --
`ROUND_ANALYSIS_IRPT_FNTEND_ROUND2_20260912.md` at `f819d7cb7d` and `ROUND_ANALYSIS_IRPT_FNTEND_ROUND3_20260912.md`
at `b453306a65` -- each naming `2.0.0_SA_COO~F`'s drain-end read as its input (96072, 96088). Of this seat's
messages in the CTO's inbox, exactly one is an IRPT_FNTEND L10: round 1's, 2026-09-11 11:11Z. This seat's part in
rounds 2 and 3 was seven adjudication rows, `C-S45` .. `C-S51`. **All seven are prose-only: none carries an
`adjudicates` list and all seven read UNDER_INVESTIGATION**, so by the channel's own carrier they disposition
nothing, including the disarms they discharge in prose. Measured when this file was generated:

- **93 investigation rows** predate round 4's L6 (`b6062ad2a2`) and carry no adjudication carrier:
  0 in INVESTIGATION_v1.md, 93 in INVESTIGATION_v2.md. By class: BLOCKING 14, OBSERVATION 79. **40 are ARMED**, none without a disarm owner. BLOCKING and ARMED:
  `W2-S10`, `W3-S9`, `W3-S10`, `S30`, `W1-S33`, `W2-S15`, `S40`, `W1-S38`, `S44`. ARMED by disarm owner: `1.0.0_SA_CTO` 12, `2.0.0_SA_COO` 3, `2.0.0_SA_COO~F` 23, `3.0.0_SA_CVO` 2. Surfaced 2026-09-11T09:12 .. 2026-09-12T10:25.
- **The round-2 analysis's RULING 7** affirms that thirteen ARMED round-1 adjudication rows on the COO's serial
  "are `3.0.0_SA_CVO`'s to carry". `ADJUDICATION_v1.md` holds **16 ARMED rows** at generation; by owner:
  `2.0.0_SA_COO~F` 16. The ruling's thirteen and this count are not reconciled here; both go into the backlog pass.
- ARMED backlog rows that name THIS seat as disarm owner:
- `S27` -- READ OFF-TASK FROM F16-AC8's OWN CAPTURE, by opening the PNG rather than reading the console line the criterion grades on: the served print document contradicts itself [...]. Named in this seat's earlier row(s) `C-S45`, `C-S46`, so addressed in SUBSTANCE -- but no `adjudicates` carrier exists, so by the channel's own measure it is undispositioned.
- `S37` -- THE CELL'S PREMISE WAS FALSE AND THE WORKER REFUSED TO SMOOTH IT. FE-s-23's face asserted 'round 2's instances are honestly aligned and must stay VALID'. They are [...]. Named in this seat's earlier row(s) `C-S47`, so addressed in SUBSTANCE -- but no `adjudicates` carrier exists, so by the channel's own measure it is undispositioned.

**Why this record does not disposition them in the same pass:** dispositioning them at speed would reproduce
exactly the shape `IRPT_BCKEND-C-S85` recorded against this seat's own round 1 -- a coverage claim that can be
believed and not checked. They are this seat's next act after the round-4 slug, ARMED first and BLOCKING first
among those, with the ARMED round-1 rows beside them, on the same per-ID carrier used below.

---

## 1. L8 -- THE COMPILE

**Population, by set difference over two git states rather than by date:** round 4's new rows are those at HEAD
that were absent at the round-4 issuance commit `b6062ad2a2`. **156 at HEAD minus 134 at issuance =
22.** Rows present at issuance but gone at HEAD: **0**. ARMED rows without a disarm owner: **0**. Every file
parsed across every JSON fence, with an independent count of `"id":` agreeing.

## 2. THE PER-ID LEDGER -- EVERY ROUND-4 ROW, ITS DISPOSITION AND ITS CARRIER

Derived from the adjudication rows on disk when this file was generated -- not retyped -- and asserted to map each
of the 22 ids **exactly once**. **14 DISMISSED_WITH_REASON, 8 GRADUATED.** Seven grouped rows
carry them (`C-S52` .. `C-S58`), each with an explicit `adjudicates` list, so every item's disposition is written
down. That is the remedy `C-S85` named, applied.

| row | class | hazard at intake | disposition | carrier | why, one line |
|---|---|---|---|---|---|
| `S49` | OBSERVATION | ARMED | DISMISSED_WITH_REASON | `C-S52` | the STOP it records was lifted by Andrew, card 1 (c6be748be7) |
| `S50` | OBSERVATION | ARMED | DISMISSED_WITH_REASON | `C-S52` | the pause-criterion clarification; moot on the lift (c6be748be7) |
| `S51` | OBSERVATION | ARMED | DISMISSED_WITH_REASON | `C-S53` | the CRO's first canon reading; withdrawn by S52, regraded at 5288666762 |
| `S52` | OBSERVATION | ARMED | DISMISSED_WITH_REASON | `C-S53` | the CRO's correction (4 surfaces in 3 of 14); held by the D14 report v0.2 |
| `W3-S17` | OBSERVATION | ARMED | DISMISSED_WITH_REASON | `C-S55` | disarmed by its named owner in S54 (0 of 746 files) |
| `W3-S18` | OBSERVATION | INERT | DISMISSED_WITH_REASON | `C-S55` | bun spawnSync ignores a mutated process.env; remedy in-tree |
| `W4-S5` | BLOCKING | INERT | DISMISSED_WITH_REASON | `C-S54` | F28-AC6's bar was unprintable; re-cut at 9ab6043728, re-run PASS |
| `W4-S6` | OBSERVATION | INERT | DISMISSED_WITH_REASON | `C-S55` | 0 of 2554 is 2 of 2559; re-measured numbers ship in the gate's constant |
| `S53` | OBSERVATION | ARMED | GRADUATED | `C-S56` | the <placeholders> reader false-admits on two branches -- checker limb |
| `W4-S7` | OBSERVATION | ARMED | GRADUATED | `C-S56` | a prose mention swallows the element (367 names for 1) -- same limb |
| `W2-S20` | BLOCKING | ARMED | DISMISSED_WITH_REASON | `C-S54` | grant widened at bf95fb7b9a, 26 minutes before the first edit (portal f95fa1db) |
| `W2-S21` | OBSERVATION | ARMED | GRADUATED | `C-S57` | measured this round at 0 of 3 captures rendering basis -- L10 choice |
| `W1-S49` | BLOCKING | INERT | DISMISSED_WITH_REASON | `C-S54` | grant widened with a ruling at 913706a898 |
| `W2-S22` | OBSERVATION | INERT | DISMISSED_WITH_REASON | `C-S54` | control pair corrected 49f4026218, repaired at portal 346d2b90 |
| `S54` | OBSERVATION | INERT | DISMISSED_WITH_REASON | `C-S55` | it IS the disarm record for W3-S17 |
| `S55` | OBSERVATION | ARMED | GRADUATED | `C-S58` | 3 cuts against an assumption at its own count, 5 at the COO count (96384); 0 caught by a gate |
| `W1-S50` | OBSERVATION | INERT | DISMISSED_WITH_REASON | `C-S55` | the worker's own pass-1 defect; fixed at portal fbc5699c |
| `S56` | OBSERVATION | ARMED | GRADUATED | `C-S56` | unanchored `0 fail` search, latent; AC16/AC17 read by hand here |
| `W1-S51` | OBSERVATION | ARMED | GRADUATED | `C-S57` | frozen fixture status 0 of 9 -- and the screen/export split behind it |
| `W1-S52` | OBSERVATION | ARMED | GRADUATED | `C-S57` | parentless Holdings tree -- donut and table empty |
| `W1-S53` | OBSERVATION | INERT | GRADUATED | `C-S57` | Global fixture has no holdings key -- body reads Failed |
| `W1-S54` | BLOCKING | ARMED | DISMISSED_WITH_REASON | `C-S54` | widened 6177717ce0 + portal dd77d19f; F18-AC17 486/1/0 read here |

---

## 3. L9 -- THE FIVE JUDGMENT CRITERIA

Vocabulary: **MET**, **MET WITH A NAMED QUALIFICATION**, **NOT MET**, **NOT EVALUATED**. A qualification is part
of the verdict, not a footnote to it.

### F25-AC12 -- MET WITH A NAMED QUALIFICATION

*"the four fixes preserve what the contract distinguishes without inventing a distinction the contract does not
make."* Graded from `consumer-boundary.result.md` and portal `fbc5699c`.

- **Absent versus null (W1-S43).** The contract distinguishes them and says why ("an absent field says no value
  exists; a null invites `we had one and lost it`"). The panel now reads `No source age yet` against `Source date
  malformed`. Preserved.
- **Two nines (W1-S41).** QUEUED, RUNNING and no-response-yet were one `Loading`; they are now three readings, 36 of
  36 pairs distinguishable, and the words appear only where the view label is shared by more than one producer
  state. `ENVELOPE_STATES`, `STATE_FOR_WIRE` and every label are unchanged; no view state was added. Preserved;
  nothing invented.
- **The generator (W1-S26).** A construct it cannot render now refuses with its coordinate instead of emitting a
  legal-looking `unknown`. Invents nothing.
- **`Availability` gained two optional members** (`producerState`, `sourceDate`). They carry contract facts to the
  view; they are carriers, not distinctions.
- ⚠ **THE QUALIFICATION -- the age (W1-S42) is right, and its label is now wrong.** AC5 orders the age from
  `business_date`, the field the clause governs, and that is done. But the panel still says **"Updated 4d ago"**
  (visible in the AC10 and AC11 captures) -- a word written for a refresh instant, now measuring the age of the
  date the answer is for. The view keeps one of the contract's two dates and drops the other, and the word on the
  page names the one it dropped. No distinction is invented; a label now misnames what it measures. **For L10:
  relabel.**

### F26-AC9 -- MET WITH A NAMED QUALIFICATION

*"each fixture's state is one the wire may genuinely carry for that basis, and none was chosen merely to force a
difference."* Graded from `holdings-fixtures.result.md` and the v1 StatusEnvelope schema (nine states; READY,
PARTIAL, STALE, NEEDS_CORRECTION and UNCERTAIN answer-bearing).

- **observed -- READY, `OBSERVED_CUSTODY_SERVED`.** Every node observed, authoritative and measured, one named
  source completed on the business date. Genuine.
- **missing-attribution -- PARTIAL, `NODE_ATTRIBUTION_UNAVAILABLE`.** `classification` is absent on every node, so
  the supervision and billing split cannot be asserted; PARTIAL is the state that says the data may not be asserted
  as complete. Genuine. The worker's refusal to use UNCERTAIN here -- because it is the parser's explicit-unknown
  and would read like a map with no status at all -- is the evidence the choice was not cosmetic.
- **target -- UNCERTAIN, `TARGET_BLEND_MODEL_REVISION_UNNAMED`.** The weights are present and their currency
  cannot be asserted when no model revision is named. A genuine reading, and the worker names it as its own
  weakest case.
- **"None chosen merely to force a difference":** the three-way difference was REQUIRED by F26-AC3. Given that, each
  state is the most defensible one for its basis, and none was picked for contrast alone.
- ⚠ **THE QUALIFICATION.** The target argument rests on an omission the observed document shares -- the same
  unnamed model source sits there, harmless because an observed answer does not depend on models. So the rule is
  BASIS-relative ("a TARGET-basis snapshot without a named model revision is UNCERTAIN"), and the contract says no
  such thing. **For L10:** decide whether that rule belongs in the contract, or a producer will not know to send it.

### F27-AC8 -- MET

*"a reader of a run can tell 'this was not exercised' from 'this was exercised and held', without knowing the
port."* Graded from `declared-preconditions.result.md`.

Three independent signals, any one sufficient: the runner's own skip count; each `SKIPPED: <criterion> -- <what it
proves> -- PRECONDITION ABSENT: <measured reason>` notice; and the `BODIES MOUNTED: N of 2` bar, which only an
exercised run emits. The precondition line prints the port itself, so the reader needs no prior knowledge of it.
The third leg of F27-AC4 -- precondition MET with a broken seam reads **FAIL**, not SKIPPED -- is what proves a skip
cannot swallow a real failure. The probe asks `localhost`, the name vite binds (::1 only on this box), which avoids
the false-absent W3-S17 named. **NOT MEASURED here:** the probe's own timeout against the ~2.1 s floor `S54` names for
reading refused-versus-timeout on this box; the recorded runs read `ECONNREFUSED`, so on those runs the refusal arrived inside the probe's bound.

### F28-AC8 -- MET WITH A NAMED QUALIFICATION

*"the boundary between what the gate binds and what it grandfathers is defensible and stated, rather than chosen to
make the tests pass."* Graded from `mandatory-placeholders.result.md` and `.tools/to-pipeline-gate.py` at
`d0c28a59be`.

- **STATED, where a seat will meet it.** The block comment (`:112-140`) and, more to the point, the refusal a seat
  actually receives: the no-element refusal (`:884-889`) appends `PLACEHOLDERS_BOUNDARY` -- *"it binds a task order
  STAGED AS ADDED ... It does NOT bind a MODIFICATION of an existing order (a status flip, an amendment), and it
  does NOT bind the flat-root legacy population ... 2559 task-order files tracked, 305 tree, 2 carrying the
  element"* -- and `PLACEHOLDERS_HOWTO`.
- **DEFENSIBLE.** It reuses the one vintage carrier the gate already has (`_newly_added`, "this gate never refuses an
  existing TO") and rejects the alternatives on their mechanics: grading the corpus refuses 2557 files nobody can now
  edit and gets routed around; grandfathering by date or project list drifts and needs a second carrier.
- **NOT CHOSEN TO MAKE THE TESTS PASS.** Identical bytes in two git states inside one gate run -- refused as an ADD,
  admitted as a MODIFY -- plus a mutant control that flips exactly three arms; the counts are re-measured, not
  inherited (W4-S6).
- ⚠ **THE QUALIFICATION: THE EXEMPTION IS WIDER THAN EITHER OF ITS STATED REASONS.** The stated reason -- keep the 2557 legacy
  orders committable -- covers modifications of orders that LACK the element. It does not require exempting
  modifications of orders that already DECLARE it; checking coverage there touches no legacy order. Nor does it engage the author's second reason -- no second VINTAGE mechanism beside `_newly_added` (`:129-133`) -- because whether an order already declares the element is read from its own bytes, not from its age. As shipped, a
  mid-round amendment that adds a `<TOKEN>` to a declaring order's invocation is never checked -- and amendments are
  how criteria change mid-round (six modifications of issued orders this round, all six subjects read: one re-cut, three widenings, one bound correction, one bounds amendment). **No instance was found this round; this is
  the class, not an occurrence. For L10:** narrow the MODIFY exemption to undeclaring orders. The reader's own
  false-admit (S53, W4-S7) is a parser defect, not a boundary one, and is graduated in `C-S56`.

### F18-AC18 -- NOT MET, ON ITS SECOND CLAUSE

*"graded at L9 from the manifest's PNGs: nothing clips or overlaps at 390; screen, preview and print of the frozen
report agree figure for figure; the screens and the export read as one Opal product."* **Population:** the
manifest's 11 PNGs (`entry_count` 11), all tracked at `887b183a2a`. The twelfth file on disk,
`fe-s-18_print_frozen_control_1440.png`, is provenance and not evidence, by the issuer's ruling.

**Clause 1 -- nothing clips or overlaps at 390 (AC4, AC7, AC8, AC9, AC10, AC11): MET.** The tab strip is whole in
all six; the period controls wrap inside their card (AC4); the analysis composer is whole in both states (AC7,
AC8); the Holdings summary stacks to one column (AC9). Named and excluded as non-defects: the slice table's right
columns run into their own `overflow-x-auto` container (intended, `min-w-[640px]`); the ASSET CATEGORY VIEWS footer
wraps `5:00p` / `ET` -- a wrap, not an overlap, in a shared component outside the grant; the search input's
placeholder truncates, as inputs do.

**Clause 2 -- screen, preview and print agree figure for figure (AC4, AC5, AC6): NOT MET.** The SCREEN (AC4) shows
the period controls and then a StatusPanel -- *"Uncertain -- Source time unknown -- Reload"* -- and no figures. The
PREVIEW (AC5) and PRINT (AC6) show the same report: `2026-01-02 to 2026-09-09`, beginning and ending value
`UNAVAILABLE (no-household-value-fact)`. The preview PNG is cut at its viewport (a capture limit, not graded as a
defect), so its visible part agrees with print page 1 and no more of it can be compared from the PNG. **Three views
cannot agree figure for figure when one of them shows none.**

⭐ **THE CAUSE IS WIDER THAN THE FIXTURE, AND IT IS SOURCE-CONFIRMED.** The frozen fixture carries a status on 0 of 9
envelopes (W1-S51), so the report reads UNCERTAIN. `ReportingTab.tsx:14-18` at `c2eb8eb4` mounts the body only
where `isCompleteState` -- READY and STALE -- and `PrintEntry.tsx` carries **no** report-state check (0 matches over
that file). AC6's own Methods page prints both facts: **"Report availability UNCERTAIN"** beside **"Bundle
availability READY"**. **The screen gates on the REPORT's availability; the export renders on the BUNDLE's.** The
same UNCERTAIN report is withheld on screen as not assertable and printed in full for export, and the two disagree
about its source date ("Source time unknown" on screen; "business 2026-09-09" in print). A client could export what
the screen refused to show. **That is a product-policy question for the CTO, not a fixture defect.**

**Clause 3 -- one Opal product: MET VISUALLY, QUALIFIED BEHAVIOURALLY.** Shared chrome and palette on screen; the
Opal Capital mark on every print page. Qualified by clause 2's split. **Recorded, not graded**, because each sits
within one view rather than across three:

- **KNOWN, NOT NEW -- `S27`, carried to L10 by this seat's `C-S45` on 2026-09-11, and still unremedied at round 4.**
  The frozen print (AC6) heads all three pages "0 account(s) in scope" while page 2 lists A-0001 and A-0002; on
  page 3 the report-scope line names both accounts and the bundle-scope line names none. `C-S45` located the zero
  as an ABSENT wire field printed as a fact; the CTO's round-2 analysis (`f819d7cb7d`, section 3) left it "with
  the CVO". It is still on the page at `c2eb8eb4`. `C-S45`'s second item -- a correction row for W2-S13's
  falsified cause -- is not re-checked here; it goes with the section-0 backlog.
- AC12 and AC13 plot a two-point series ending at 0.0034 in a document whose period table reads YTD 0.0732, as the
  fixture supplied them. Not asserted new: this seat's string search of the channel for it was void (its positive
  control also read zero).
- The AC5 export dialog's own panel reads "Loading -- No source age yet" above the preview it renders.

**THE HOLDINGS RECORD THIS SEAT COMMITTED TO IN `C-S51`:** AC9 (observed, READY) mounts the body -- summary card,
category-views card, table header -- with the donut and slice table **empty** (W1-S52). AC10 (target) is a
StatusPanel *"Uncertain -- Updated 4d ago -- TARGET_BLEND_MODEL_REVISION_UNNAMED"*. AC11 (missing-attribution) is a
StatusPanel *"Partial -- Updated 4d ago -- NODE_ATTRIBUTION_UNAVAILABLE -- Narrow the scope"*. **0 of 3 captures render
`basis` or `classification` as holdings content** -- W2-S21 said 1 of 3; the READY map's tree is empty too.
AC14 (Global, 1440) holds as the layout control; its body reads *Failed / IR-REQUEST-FAILED* (W1-S53).

**A grade of the evidence, not of the worker.** No layout edit was owed this round (the declared exclusion is
accepted: every 390 surface stays in its card). The failure's causes are fixtures the worker was told not to touch
(W1-S51, W1-S52, W1-S53) and a screen/export policy outside the cell.

---

## 4. ISSUER RULINGS AND THE DECLARED EXCLUSION

- **FE-s-25 / W1-S49 -- "display the producer's state; do not add a view state": UPHELD on substance.** Its
  rationale is corrected: it did touch a contract -- `Availability`, the view contract all ten documents carry --
  additively, with two optional members. `docs/contracts/` unchanged is `2.0.0_SA_COO~F`'s measurement, not
  re-derived here.
- **FE-s-18 -- bounds amended, criteria frozen: noted.** `1.0.0_SA_CTO` confirmed it on its own instrument (96381);
  not re-derived here.
- **FE-s-26's complete flip before its control was repaired: ACCEPTED.** Flipped at 05:07:02Z (`81b45120e7`),
  bound corrected at 05:18:48Z (`49f4026218`), repaired at 05:33:25Z (portal `346d2b90`). F26-AC8's proof row cites
  `346d2b90` and reads 28 / 0 there, so the order was re-validated at the corrected commit.
- **FE-s-18 bound 5's declared exclusion -- the DISTINCTION test left on live digests: ACCEPTED for correctness,
  with a recommendation.** Its one assertion counts defective fixtures and reads no digest, so it passes either way.
  But it is the mixed-source shape the issuer itself ruled against at `49f4026218` -- a control reads ONE map --
  and it should be frozen at the next touch so the verdict it prints comes from one set.

## 5. FOR THE L10 SLUG TO 1.0.0_SA_CTO

1. **The screen/export availability split** -- decide whether an UNCERTAIN report may be exported that the screen
   withholds (C-S57).
2. **W2-S21's (a)/(b)/(c)** -- against the stronger fact: 0 of 3 captures render basis, not 1 of 3 (C-S57).
3. **The print header's "0 account(s) in scope"** -- `S27`, carried to L10 by `C-S45` on 2026-09-11 and still on the page at round 4. Known, not new.
4. **"Updated N ago"** now names a business-date age (F25-AC12).
5. **The target-basis UNCERTAIN rule** the contract does not state (F26-AC9).
6. **GATE (viii)'s MODIFY exemption**, wider than either of its stated reasons (F28-AC8).
7. **The two checker defects** -- the placeholders reader and the unanchored count bar (C-S56).
8. **Round 4's cut discipline** -- three criteria cut against an assumption at `S55`'s count, five at the COO's (96384), none caught by a gate (C-S58).
9. **Rounds 2 and 3's undispositioned backlog** -- this seat's, stated in section 0, with its plan.

## 6. WHAT THIS RECORD DOES NOT CLAIM

- **Not that the 93 older rows or the 16 ARMED round-1 rows are resolved.** They are undispositioned, and that is this seat's debt.
- **Not the mechanical grades.** Those are `proof-of-spec-check`'s; this seat re-read the two `0 fail` deciding lines
  (F18-AC16, F18-AC17) by hand under the S56 interim control -- one summary line each -- and graded nothing else
  mechanical.
- **Not every figure in every print.** The PNGs were read at their displayed resolution; the preview is cut at its
  viewport.
- **Not a round-4 step log.** `STEP_LOG.3.0.0_SA_CVO.round4.json` is not written in this pass and is owed.

---

**Instruments:** `git show` and `git log --date=iso-strict` in both repos; `json` over every fence of the channel files
at HEAD and at `b6062ad2a2`; the five proof instances and result files; the eleven manifest PNGs viewed directly;
`git show` of `.tools/to-pipeline-gate.py` at `d0c28a59be`; `git show` of the portal's `ReportingTab.tsx` and
`PrintEntry.tsx` at `c2eb8eb4`.
