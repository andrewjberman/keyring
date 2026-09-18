# TO LGIC_LGCTFM.TO-LT-c-2-r2 -- THE CARD NAMES ITS OWN SUBJECT, and touches NOTHING else

<to_id>LGIC_LGCTFM.TO-LT-c-2-r2</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `LT-c-2` (decomposition v1.3 s.12) | **outcome_ref:** FWD-4's READABILITY, never its closure | **depends_on:** `LT-a-2-r2` -- SECOND of slot ~1's queue

---

## WORKER FACE

### THE CELL

`LT-c-2`. **`ANDREW_CARD.md` names no run.** A regex for a run id over it returns ZERO matches; it
identifies its own subject only as *"graph built 2026-09-17 18:16 UTC"*. **Five run directories share that
subject and one of them carries a DIFFERENT tension count** (180 against the other four's 179). The card
ranks a 179-row order, so it is not that run -- but nothing IN the card says so, and the only thing
separating it from a different run in the same directory is that its order happens to be 179 rows long.

You add the subject pin. **That is the whole cell.**

### THIS CELL EXISTS BECAUSE ITS REMEDY NEEDS A GRANT THE ISSUER DOES NOT HAVE

Row `S12` named the remedy: one line in the card. Row `S16` recorded why it had not been done --
`.tools/owned-paths-validate.py` clause 4 (`ADHC_OWNPTH.004`) **refuses an ISSUER's edit inside a worker's
deliverables folder**, measured twice on this exact file. **The remedy was never impossible; it needed a
CELL whose `<paths>` names the card.** That is this order, and the path is granted below.

### WHAT YOU ADD

Into the card's **"## The subject"** section, on its face:

- the **run id** `20260918T011619Z-8db9eb1`
- that run's **contract content hash** `33204e29839de89af81fb293317cce3ccdf2266d`
- **the INSTRUMENT that produced the hash** -- the words `git hash-object`, because
  ⛔ **A HASH WITHOUT ITS INSTRUMENT IS TWO NUMBERS**: a plain `sha1` of the same bytes reads
  `9c5cdb873f00a599bb00166831a91646fea97990`, and the issuing seat briefly read that as a mismatch against
  a hash it had already published
- a pointer to the adjudication that confirmed the ranking: commit `662d53b793`

**Verify the hash yourself with the named instrument before you write it** --
`git hash-object workflows/legacy_transform/blackdiamond-49financial/20260918T011619Z-8db9eb1/contract.json`
-- and run the NEGATIVE CONTROL beside it on the OTHER candidate run, `20260918T002711Z-caf0983`, which
returns `3ffedfed35c05a1820d594c85c2b416c0441aa0f`. A hash that merely matches proves nothing without the
second read.

### WHAT YOU MUST NOT TOUCH, AND IT IS A GRADED REFUSAL

⛔ **THE RANKING TABLE AND THE RECOMMENDATION LINE DO NOT MOVE.** `c2-frozen` pins the table at 11 rows and
sha1 `837b46cc6dde4912ab31de9d2ba664c5dc1284e6` and the recommendation paragraph at sha1
`b5513d671f10da2bced39b311c9989cc1d1796df`, and **it reads PASS at the cut** -- it is a GUARD, so it
refuses your work only if you change either.

**WHY, and it is not caution -- it is row `S6`'s own condition.** The card's RECOMMENDATION overstates by
one: it says *"the two rows touching a live, client-facing surface"* where, measured over 179 tensions,
the answer is **ONE** (`T-0001`, client_facing AND live). `S6` set the condition that this correction reach
the decision-maker **BESIDE the card "rather than as a silent rewrite"** -- and it did, by
`1.0.0_SA_CTO`'s adjudication `@662d53b793` under Andrew-direct, with the card itself never altered.

⛔ **SO REWRITING THAT LINE NOW WOULD BE THE EXACT ACT `S6` EXISTS TO PREVENT**, on a document sitting with
a decision-maker who has not yet read it. You add a POINTER to the adjudication. He may overturn any part
of it, and a card he finds silently edited is a card he cannot trust.

**Read:** rows `LGIC_LGCTFM-S6`, `S12`, `S16` and `S19` whole; `CARD_SUBJECT_PIN.md` in
`deliverables/2.0.0_SA_COO~G/`, which is the issuer's own record of this same pin and whose figures you
should re-derive rather than copy; `R2_BASE.json`'s `card` and `graded_run_round_1` blocks. If `LT-a-2`'s
re-derivation record contradicts any figure here, that contradiction is a surprise ROW and you say so
rather than resolving it silently.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="C2R2-AC1" cell_refs="LT-c-2"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_lt_r2.py c2-names-run</invocation><expect>PASS-C2-CARD-NAMES-ITS-RUN-AND-HASH</expect></criterion>

<criterion id="C2R2-AC2" cell_refs="LT-c-2"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_lt_r2.py c2-frozen</invocation><expect>PASS-C2-RANKING-AND-RECOMMENDATION-UNCHANGED</expect></criterion>

<criterion id="C2R2-AC3" cell_refs="LT-c-2"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_lt_r2.py c2-pointer</invocation><expect>PASS-C2-CARD-POINTS-AT-THE-ADJUDICATION</expect></criterion>

<criterion id="C2R2-AC4" cell_refs="LT-c-2" judgment="true"/>

<expected_criteria>C2R2-AC1, C2R2-AC2, C2R2-AC3, C2R2-AC4</expected_criteria>

**AT THE CUT, MEASURED BY THE ISSUER:** `C2R2-AC1` and `C2R2-AC3` read **FAIL** -- the card names neither
the run nor the adjudication today. **`C2R2-AC2` reads PASS and is a GUARD, not a target** -- the ranking
and the recommendation are unchanged now and must stay so, which is why that arm can only be broken by
your own edit.

**`C2R2-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the pin makes the card's subject
UNAMBIGUOUS to a reader who has never seen this project -- a run id and a hash are necessary and may not be
sufficient -- and whether the added text reads as part of the card rather than as an annotation bolted to
someone else's document.

**THE CHECKER'S CONTROLS:** `selftest-arms` drives 28 arms, **10 POSITIVE-SATISFIABILITY** against
simulated correct records -- including one that adds the pin to a copy of the real card and requires
`c2-frozen` to still PASS, which is the arm that proves a correct pin is achievable at all. Run it first.
An arm a correct edit cannot satisfy is a BLOCKING surprise row quoting the arm and its output.

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** The `<paths>` block below -- which INCLUDES `ANDREW_CARD.md`, a CROSS-WORKER grant made
  deliberately and the reason this cell exists -- plus
  `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/` and this order's own file.
  Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **THE CARD IS THE ONLY FILE IN `~3/` YOU MAY TOUCH**, and within it you may only ADD. No line of the ranking table, the recommendation paragraph, the rule quote or the evidence section changes.
- ⛔ **YOU DO NOT CORRECT THE RECOMMENDATION.** It is wrong by one and that is known, recorded and adjudicated. See the WORKER FACE.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md`, appended by **TEXTUAL SPLICE** to the fence that PARSES AS A LIST. ⛔ **NEVER RE-DUMP THE ARRAY.** Id `LGIC_LGCTFM-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time.
- **Commit before you grade.**
- **Nothing live moves.** No apply, no AWS write, no deploy.

<paths>
org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~3/ANDREW_CARD.md
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.3, round-2 cell `LT-c-2` (section 12).
<owned_cells>LT-c-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `C2R2-AC1` through `C2R2-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-c-2-r2.card-names-its-subject.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> C2R2-AC1,C2R2-AC2,C2R2-AC3,C2R2-AC4 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-c-2-r2.card-names-its-subject.md` BEFORE the `complete` flip.
Result file `card-names-its-subject.r2.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`C2R2-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the hash you computed, the instrument you used, the negative control's differing hash, and the table and recommendation sha1s before and after your edit.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-2 cut: no schedule is created or read by this cell.
comp-iam: RUN at the round-2 cut: no grant moves in the cloud. A CROSS-WORKER REPO GRANT does move and is stated rather than implied -- this cell writes a file inside 0.9.0_WK_LGIC_LGCTFM~3's deliverables folder, which is exactly the surface owned-paths clause 4 refuses to an ISSUER. The grant is in the <paths> block and nowhere else, and it names ONE file rather than that folder.
comp-adversary: RUN at the round-2 cut: the adversarial control is c2-frozen, a GUARD that reads PASS at the cut and can only be broken by this cell's own edit. It exists because the tempting act here -- correcting a recommendation known to be wrong by one -- is precisely the act row S6 set a condition against, on a document sitting unread with a decision-maker.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/0.9.0_WK_LGIC_LGCTFM~1/ is granted by the tree convention. Within the granted card the cell may only ADD -- a BOUND the grant cannot express, so the order states it and the frozen arm enforces it.
contention: the channel is written by LT-a-2 EARLIER IN THIS SAME QUEUE and by LT-n-2 on slot ~2 concurrently; the card itself is written by no other open order in any LGIC project at the cut. This order is second in its queue precisely so that LT-a-2's re-derivation record exists before the pin is written, in case that record contradicts a figure pinned here. See LT-a-2's contention note for this round's splice-versus-re-dump experiment.
</preflight>

Seating: slot `~1`, level 1, SECOND of a two-order queue (`LT-a-2-r2` -> `LT-c-2-r2`). Round 2 of LGIC_LGCTFM, issued by `2.0.0_SA_COO~G` on decomposition v1.3 s.12, from `1.0.0_SA_CTO`'s round-1 analysis item 3. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/` (`check_lt_r2.py`, 11 subcommands and a 28-arm self-test with 10 positive-satisfiability arms; `R2_BASE.json` pinning `d0d4c6065f` and the card's two refusal hashes). Rulings carried: R-40, and rows S6, S12, S16, S19.
