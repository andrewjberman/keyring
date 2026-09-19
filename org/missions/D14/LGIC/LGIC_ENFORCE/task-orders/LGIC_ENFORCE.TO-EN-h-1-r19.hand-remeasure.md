# TO LGIC_ENFORCE.TO-EN-h-1-r19 -- RE-MEASURE THE HAND SIDE, ACROSS ALL THREE SURFACES, AS ADDITIVE SIBLINGS

<to_id>LGIC_ENFORCE.TO-EN-h-1-r19</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>complete -- 0.9.0_WK_LGIC_ENFORCE~1, 2026-09-19. H1R19-AC1 PASS-H1-COVERAGE, H1R19-AC2 PASS-H1-VINTAGE, H1R19-AC3 PASS-H1-REDERIVED (rc 0 each, run against the committed record); H1R19-AC4 UNVERIFIABLE-BY-INSTRUMENT (judgment, for 3.0.0_SA_CVO at L9 -- no verdict from this worker). Artifacts at b4ad2b4d2e: HAND_REMEASURE_R19.json, build_hand_remeasure_r19.py, hand-remeasure.r19.result.md and the THREE additive siblings (GRADING_RULE.REMEASURED_R19.md, TENSION_RANKING.REMEASURED_R19.md, exercises/n6-grader-a.REMEASURED_R19.tsv); the three ORIGINALS unmoved, blobs identical at this cell's base 3ed034c144 and at HEAD. The hand side re-measured across ALL THREE surfaces at the machine side's own census vintage (54659987c0): 45/45/0, 88/86/2, 10/9/1, TOTALS 143/140/3 against round 9's 143/109/34. Denominators re-derived at write time (45 -- not the 43 two carriers at HEAD still state -- 88, 10). grade() never called; 3 disagreements survive and none is a hand-side defect (2 machine-side departures from the written rule, 1 instrument gap at tension rank 5, deliberately not re-quoted). proof-of-spec-check.py rc=0 VALID. Proof instance: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-h-1-r19.hand-remeasure.proof_of_spec.json</status>

---

## WORKER FACE

You are `0.9.0_WK_LGIC_ENFORCE~1`. Your worktree is `<WS>`, given in your identity line. Everything you
need is in this face; the record face below is not yours to read.

**THE JOB IN ONE SENTENCE.** `FWD-5` clause 3 says *"the totals agree with the ranking the naming work
produced by hand"*, the comparison does not close, and **30 of its 34 disagreements name the HAND side as
the defective one** -- so you re-measure the hand side, **as additive siblings that leave every original
byte-for-byte intact**, and re-run the comparison.

### THE POPULATION IS THREE SURFACES. THIS IS THE ONE THING THAT WILL COST YOU THE ROUND.

The analysis, the register and the outcome all say **"the HAND RANKING", singular.** It is three
artifacts, and round 9 measured each:

| surface key (use these exact keys) | carrier | compared | agree | disagree |
|---|---|---|---|---|
| `grading_rule_worked_cases` | `org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md` | 45 | 43 | 2 |
| `n6_grader_rows` | `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n6-grader-a.tsv` | 88 | 61 | 27 |
| `tension_ranking_surfaces` | `org/missions/D14/LGIC/LGIC_NAMING/deliverables/TENSION_RANKING.md` | 10 | 5 | 5 |

⛔ **A CELL THAT RE-MEASURES ONLY `TENSION_RANKING.md` DOES 10 OF 143 AND REPORTS A CLOSED COMPARISON
WITH EVERY FIGURE IT PRINTS CORRECT.** `H1R19-AC1` refuses that by subtraction from the declared set.

⚠ **`45` IS THE FIGURE, NOT `43`, AND TWO CARRIERS AT HEAD STILL SAY `43`** -- this project's own
`project.json` round-9 text and `LGIC_ENFORCE_ROUND8_ANALYSIS.md:151`. `43` was true at
`GRADING_RULE.md@51b0952d71`; the v1.9 re-cut `@fd6ce8c330` added `mdpf-lambda-lambda` and
`orion-orion-lambda-lambda`. ⭐ **If you inherit `43` from either carrier you have reproduced the exact
defect this round exists to close.** Re-derive it yourself and print your denominator.

### WHAT YOU WRITE

1. **Three additive siblings**, one per carrier, at the `<paths>` names below. ⛔ **THE ORIGINALS ARE
   READ-ONLY. NOT ONE BYTE.** Mutating them deletes the left-hand side of every *"HAND SIDE STALE"*
   comparison, which is the entire content of the finding.
2. **`HAND_REMEASURE_R19.json`** -- the record the arms grade. Shape:
   - `actor_base_sha` -- your worktree's base sha.
   - `surfaces{<key>}` -> `compared`, `agree`, `disagree`, `compared_keys` (non-empty list),
     `denominator_measured_at_write_time{instrument, value}`.
   - `revisions[]` -> `surface`, `carrier`, `sibling_path`, `census_vintage`.
   - `totals{compared, agree, disagree}` and `rerun_instrument`.
3. **`build_hand_remeasure_r19.py`** -- the builder that produced it. The record's `claim` is
   `measured`, so the instrument must exist and be named.
4. **`hand-remeasure.r19.result.md`** -- the narrative, including every disagreement that SURVIVES.

⛔ **MEASURE THE HAND SIDE AT THE SAME CENSUS VINTAGE THE MACHINE SIDE USED**, and say so per revision:
`NAMING_CENSUS_REPORT.r8.md` @`54659987c0`, *"the estate as of 2026-09-18 12:17:28 UTC"*. A hand figure
re-measured against a **different** vintage from the machine figure it is compared with **re-creates this
defect one layer down**, and no arm here can see it unless your record says which vintage it used.

<placeholders>WS</placeholders>

<criterion id="H1R19-AC1" cell_refs="EN-h-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r19/check_en_r19.py h1-coverage</invocation><expect>PASS-H1-COVERAGE</expect></criterion>

<criterion id="H1R19-AC2" cell_refs="EN-h-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r19/check_en_r19.py h1-vintage</invocation><expect>PASS-H1-VINTAGE</expect></criterion>

<criterion id="H1R19-AC3" cell_refs="EN-h-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r19/check_en_r19.py h1-rederived</invocation><expect>PASS-H1-REDERIVED</expect></criterion>

<criterion id="H1R19-AC4" cell_refs="EN-h-1" judgment="true"/>

<expected_criteria>H1R19-AC1, H1R19-AC2, H1R19-AC3, H1R19-AC4</expected_criteria>

**WIRING AT THE CUT -- AND EACH RED NAMES THE ACT THAT CLEARS IT.**

| criterion | at the cut | WHICH ACT CLEARS IT |
|---|---|---|
| `H1R19-AC1` | **FAIL** (confirmed by me at the cut) | **YOURS ALONE** -- writing your record. |
| `H1R19-AC2` | **FAIL** (confirmed) | **YOURS ALONE** -- your revisions and your base sha. |
| `H1R19-AC3` | **FAIL** (confirmed) | **YOURS ALONE** -- re-deriving the totals. |

⚠ **WHAT THE MECHANICAL ARMS DO AND DO NOT SEE.** They check that your population is COMPLETE across the
partition, that your denominators were re-derived at YOUR write time, that the originals did not move
between YOUR base and HEAD, and that your totals are not round 9's copied forward. ⛔ **They never check
whether a re-measured FIGURE IS CORRECT, and they never judge whether a revision is a real revision.** A
PASS means your record is complete and coherent -- never that a single figure is right. **That half is
`AC4`'s.**

**`H1R19-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether each hand-side revision is
**right at the bytes, across ALL THREE surfaces.**

⛔ **THAT PHRASING IS THE ROUND-8 PARTITION RULE.** The tempting bucket to police is `n6_grader_rows`,
which holds 27 of the 34 disagreements. ⭐ **But the mechanism -- a 2026-09-13 pin against a moved estate
-- is uniform over all three, so the criterion quantifies over the PARTITION.**

⭐ **THE BAR, and you may hold me to it:** every arm was driven against a HAND-BUILT CORRECT RECORD before
this order shipped, not only against mutants -- ⛔ **a mutant test cannot catch a vacuous pass (R-47)**:
an unsatisfiable predicate refuses every mutant exactly as loudly as a sound arm does. **Confirm the
instrument yourself first** -- `python .../check_en_r19.py selftest-arms` must print
`PASS-ARMS-DISCRIMINATE`, and **the run prints its own arm counts; this order does not quote them**
(`LGIC_LGCTFM-W1-S37`). *"Can a CORRECT artifact FROM THIS CELL ALONE satisfy this? Where the honest
answer is no, THE CRITERION IS THE DEFECT, NOT THE CELL."* **If you find one, file it BLOCKING and keep
working.**

## BOUNDS

- **Grant.** ⛔ **THE `<paths>` BLOCK BELOW IS THE GRANT AND EVERY PATH YOU MAY WRITE IS IN IT.** Nothing is granted in this prose.
- ⛔ **THE THREE ORIGINAL CARRIERS ARE READ-ONLY** -- `GRADING_RULE.md`, `exercises/n6-grader-a.tsv`, `TENSION_RANKING.md`. They are not in `<paths>` and `H1R19-AC2` measures their blobs at your base and at HEAD.
- ⛔ **EVERY PINNED FIXED INPUT IS READ-ONLY**, including `R19_BASE.json` and `check_en_r19.py`. You read the instrument; you do not edit it.
- ⛔ **DO NOT RE-GRADE THE MACHINE SIDE.** It was right in 30 of the 34 disagreements. Re-running `grade()` so it agrees with a stale hand side is the REFUSED reading -- the graded party grading its own reference.
- ⛔ **REPAIR NOTHING IN THE REGISTRY OR THE BUILDERS.** Round 13 recorded `no_repair` deliberately and this round does not reverse it.
- ⛔ **CLAUSE 2 IS NOT YOURS** (the unfillable forms, the 1298/1093 population). The analysis says *"Nothing else."*
- ⛔ **DO NOT RE-ISSUE THE 1303 CARDS.** They need an additive `writer` field and that is a different act. **But any card YOU write this round carries `owner` (the DECIDER, derived by a read your reason STATES) and, where that decider is not `permitted_agents` on the surface the remedy names, the `writer` too.**
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; preserve line endings exactly.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **No other order is open this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.18, round-19 cell `EN-h-1` (section 0s).
<owned_cells>EN-h-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `H1R19-AC1` through `H1R19-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-h-1-r19.hand-remeasure.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> H1R19-AC1,H1R19-AC2,H1R19-AC3,H1R19-AC4 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-h-1-r19.hand-remeasure.md` BEFORE the `complete` flip.
Result file `hand-remeasure.r19.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent. Your recorded invocation must match this order's literal text INCLUDING `timeout 900`.
`H1R19-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/HAND_REMEASURE_R19.json
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/build_hand_remeasure_r19.py
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-h-1-r19.hand-remeasure.proof_of_spec.json
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/hand-remeasure.r19.result.md
org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.REMEASURED_R19.md
org/missions/D14/LGIC/LGIC_NAMING/deliverables/TENSION_RANKING.REMEASURED_R19.md
org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n6-grader-a.REMEASURED_R19.tsv
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-h-1-r19.hand-remeasure.md
</paths>
<preflight>
lane: <paths> IS the grant and it is exhaustive -- the record, its builder, the proof instance, the result narrative, the THREE additive siblings, the shared channel and this order (for the status flip). Nothing is granted in BOUNDS prose. MEASURED AT THE CUT, not assumed: a file directly under deliverables/ with no <SERIAL> folder matches NOTHING in the tree-deliverables lane and stays refused (.tools/owned-paths-validate.py:102-103), so the three LGIC_NAMING sibling paths reach the worker ONLY through worker_grant -- the fifth additive clause, which admits exactly the <paths> a non-terminal order names. The grant is explicit and enumerated, never conventional. The three ORIGINAL carriers are deliberately absent from <paths> and are graded read-only by AC2.
contention: the channel is shared -- append-only, 14b's inversion applies, so do NOT isolate the channel write. One cell this round, so no sibling races the deliverables directory. The three sibling paths are new files in a CLOSED project's tree (LGIC_NAMING); no live cell of any project writes there, checked at the cut.
comp-schedule: RUN at the round-19 cut: no schedule is created or read.
comp-iam: RUN at the round-19 cut: no grant moves.
comp-adversary: RUN at the round-19 cut. The cheapest satisfying move is to read "the HAND RANKING" as the singular it literally says and re-measure TENSION_RANKING.md alone -- 10 of 143, every printed figure correct, comparison reported closed -- so AC1 derives the population BY SUBTRACTION from the base's declared set and refuses a missing surface by name. The second-cheapest is to inherit 43 worked cases from either carrier at HEAD that still says 43, which is this round's own defect reproduced -- so every surface must carry a denominator re-derived at the cell's write time, and the order states the trap with the commits that caused it. The third is to carry round 9's totals forward unchanged, which is indistinguishable from a re-run that found nothing -- so AC3 refuses a record whose triple reproduces round 9's on ALL THREE surfaces, which is the one result a copy produces and a genuine re-run of a revised hand side cannot. The fourth is to edit the originals in place, which would make every figure agree and silently delete the evidence -- so AC2 refuses sibling_path == carrier AND measures each original's blob at the ACTOR'S OWN BASE and at HEAD. What no mechanical arm here can see is whether a re-measured figure is CORRECT or whether a revision is real; stated on the order and routed to AC4 over ALL THREE surfaces.
</preflight>

Seating: slot `~1`, level 0, the ONLY order this round. Round 19 of LGIC_ENFORCE, issued by
`2.0.0_SA_COO~G` on decomposition v3.18 s.0s, from `1.0.0_SA_CTO`'s round-18 analysis @`a972a343bd` and
`3.0.0_SA_CVO`'s L9 @`cba8a69657`. Fixed inputs:
`deliverables/2.0.0_SA_COO~G/fixed_inputs/r19/`. Rulings carried: `S85`'s ONE CARRIER, the cut-time
criterion bar, `S106`'s criterion-level non-pairing, the round-8 partition rule, the additive-sibling
ruling (ENFORCE r16 / LGCTFM r10), the ACTOR'S-OWN-BASE additivity anchor (round-10 ruling, against
round 16's), the owner/writer sentence (round-18 analysis s.1), `W1-S37`, R-57, LD-0521.

---

## RECORD FACE

**Cut rationale.** The round-18 analysis s.4 names one cell and closes with *"Nothing else."* The
hand-side re-measure is the whole round, and it is cut **because it is not a wait**: FWD-5 clause 3's
remedy is an act a seat can take on demand, which is the discriminator that separated `LGIC_ENFORCE`
(CONTINUES) from `LGIC_LGCTFM` (HELD-AT-STOP) in the same ruling.

**The routing choice is disclosed, not assumed.** The three hand carriers belong to `LGIC_NAMING`, which
is COMPLETE/CLOSED. I ruled ADDITIVE SIBLINGS rather than in-place edits, for three reasons set out in
decomposition s.0s.2 -- the binding one being that FWD-5's ACCEPT names *"the ranking the naming work
produced by hand"*, so the surface must stay the naming work's, while an in-place edit would destroy the
discriminator that is the entire content of the 28 stale findings. It is an L5 routing choice inside the
analysis's scope and `1.0.0_SA_CTO` can overrule it cheaply; nothing waits on it.

**What I verified at the cut, rather than asserting:** all three arms RED; `selftest-arms` green over 11
mutants and 3 positive controls; the `<paths>` grant mechanism read at `owned-paths-validate.py:102-103`
rather than inferred from the lane's note; and the 45-not-43 trap measured against the two carriers at
HEAD that still say 43.
