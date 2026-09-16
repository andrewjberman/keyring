# TO LGIC_CANON.CN-o-3-r2 -- the checklist: sovereign inputs named, the family given to steps 3/7/8/9, two STOPs with owners

<to_id>LGIC_CANON.CN-o-3-r2</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~8</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-16</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_CANON_PRD.md` v1.3 @5b2336a5e4 (ADMITTED; both halves SIGNED and `current`, re-read at the recut) | **Decomp cell:** `CN-o-3` (round 2, decomposition v4) | **outcome_ref:** FWD-5 (instrument) | **rulings:** A-6, A-7, A-8, A-9, A-10 | **depends_on:** CN-k-2 (the pipeline-instance rule) | **slot:** ~8, queue position 1, level 1

---

## WORKER FACE

### THE CELL

`CN-o-3` -- the checklist edit. Round 1's review marked 5 of 16 steps JUDGEMENT: a step where somebody has to
invent an answer is a step the checklist cannot run. Four of those five share one cause -- the checklist fixes a
pipeline's homes, formats, compute and name grammar but NOT its contents -- and `CN-k-2`'s pipeline-instance rule
supplies exactly those contents. Edit `infra/logic/10_ONBOARDING_CHECKLIST.md`:

1. **Steps 3, 7, 8 and 9 take the pipeline FAMILY as a given input (A-9).** Each names the family and reads its
   contents from the canon's pipeline-instance rule instead of asking the runner to choose. The word `family` must
   appear in each of those four steps.
2. **The sovereign inputs are named where the inputs are given (A-10).** An input the run may NOT choose marks itself
   `SOVEREIGN` in the INPUTS section, not in a step. A reader who meets it first in step 12 has already guessed.
3. **Step 10 carries a STOP naming ADVI_FIRMBKTS (A-8).** A NEW firm mints no legacy served key; the router repoint
   that lifts this STOP is ADVI_FIRMBKTS's, and the STOP names that owner so the checklist does not read as blocked on
   nobody.
4. **Step 14 carries a STOP citing register entry X8 (A-7).** The four `opal-partner-<LONG>` tables are a DECLARED
   departure forced by the auth handler and the IAM grant -- `grade()` reads all four OUT-OF-PATTERN and a rename would
   break sign-in. `4.0.0_SA_CRO` authors X8 in the register; you CITE it. If X8 does not exist when you run, O3-AC3
   FAILs by measurement and that is a correct result.
5. **Step 6's second block (A-6):** LONG is sovereign and SHORT is derived by `name()`; the step says so once.

⛔ **You do not mark steps MECHANICAL or JUDGEMENT.** That is `CN-o-4`'s, by a worker who did not write this, and a
checklist that marks itself proves nothing.

**Read:** `infra/logic/10_ONBOARDING_CHECKLIST.md`; `infra/logic/02_DOCTRINE.md` (the pipeline-instance rule
`CN-k-2` adds); `org/missions/D14/LGIC/LGIC_CANON/deliverables/CHECKLIST_REVIEW.md` (round 1's review, for the five JUDGEMENT steps and their reasons);
the round-1 analysis s.2 rulings A-6, A-7, A-8, A-9 and A-10 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/LGIC_CANON_ROUND1_ANALYSIS.md @26ae876d23`).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="O3-AC1" cell_refs="CN-o-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py o3-family</invocation><expect>PASS-O3-FAMILY-STEPS-TAKE-INPUT</expect></criterion>
`O3-AC1` -- steps 3, 7, 8 and 9 each name the family.
<criterion id="O3-AC2" cell_refs="CN-o-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py o3-step10-stop</invocation><expect>PASS-O3-STEP10-STOP-NAMES-OWNER</expect></criterion>
`O3-AC2` -- step 10's STOP names ADVI_FIRMBKTS.
<criterion id="O3-AC3" cell_refs="CN-o-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py o3-step14-stop</invocation><expect>PASS-O3-STEP14-STOP-CITES-X8</expect></criterion>
`O3-AC3` -- step 14's STOP cites register entry X8.
<criterion id="O3-AC4" cell_refs="CN-o-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py o3-sovereign</invocation><expect>PASS-O3-SOVEREIGN-INPUTS-NAMED</expect></criterion>
`O3-AC4` -- the INPUTS section marks its SOVEREIGN inputs.
<criterion id="O3-J1" cell_refs="CN-o-3" judgment="true"/>
`O3-J1` -- graded at L9 by 3.0.0_SA_CVO: the four family steps are executable by a runner who is given the family, and neither STOP is a way of deferring a step this cell could have finished. RECORD; NO VERDICT.

<expected_criteria>O3-AC1, O3-AC2, O3-AC3, O3-AC4, O3-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_CANON/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are READ-ONLY.** `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/` holds round 2's checker `check_canon_r2.py` (every mechanical criterion calls it) and its inputs. Never edit any of them. ⚠ If a fixed input is itself DEFECTIVE, that is a BLOCKING surprise row and you keep your hands off it -- LGIC_ENFORCE round 2 lost an hour to a corrupt fixture, and the worker that filed a row instead of editing around it is the reason the defect was found in the fixture rather than papered over in the code.
- **Nothing live moves.** No cell of this project renames a live name, writes to AWS, runs Terraform, or calls anything off Opal infrastructure. Every `.py` you touch passes `.tools/commit-gate.sh` (safe-commit runs it).
- **Surprises** go to `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_CANON-W8-S<k>`. Keep working after filing. **Re-read the channel immediately before you write** -- rows land from other cells and an id minted from an earlier read collides silently. **`class` takes exactly TWO values, `OBSERVATION` or `BLOCKING`**; a third is refused by the corpus limb at `/class`, measured 2026-09-16.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context. Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Pins by commit.** Every artifact your proof instance cites names the commit that carries it: commit the artifact first, then the proof in a later commit. Never `PENDING-THIS-COMMIT`.

<paths>
infra/logic/10_ONBOARDING_CHECKLIST.md
org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v4, cell `CN-o-3`, round 2 (section 0d).
<owned_cells>CN-o-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `O3-AC1`, `O3-AC2`, `O3-AC3`, `O3-AC4`, `O3-J1`. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~8/LGIC_CANON.CN-o-3-r2.checklist-edit.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> O3-AC1,O3-AC2,O3-AC3,O3-AC4,O3-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `checklist-edit.r2.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-2 cut 2026-09-16 -- --budget 540, WITHIN BUDGET, scanned 5 of 5 carriers in 300.7 s; REACHED-DENOMINATORS C1=276 C2=7 C3=12 C4=21 C5=334; GATES ARMED 26, and 0 of them names LGIC_CANON (grep count 0 over the run). Round 2's own gates are G-C (worker admission, checked at each spawn) and, for `CN-k-4` only, LGIC_NAMING's schema cell. NOT COUNTED, and the tool says so itself: C4 is SEMI-DECIDABLE and C5 NOT-DECIDABLE, so the 21 scope_guards and the 136 non-null `blocking` prose fields are a READING LIST rather than gates.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 2's write set (the canon, the renderer, the checklist, the ledger, the recount script and records under deliverables/): no operation, policy, principal or resource is added.
comp-adversary: RUN at the recut on the round-1 analysis @26ae876d23 -- the analysis's cited commits and paths verified at the cut; blindness stated: the analysis carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). `infra/logic/**` is lane PLATFORM_LOGIC_DOCS and admits no COO by enumeration; a worker reaches it ONLY through this block, which is why every canon, renderer, checklist and ledger path this cell touches is named here explicitly.
write-surface: MEASURED at the cut. The `<paths>` of every non-terminal LGIC_NAMING and LGIC_ENFORCE order (15 orders, printed denominator) were intersected with this round's four write surfaces; the intersection is EMPTY. Internal contention is `CN-k-2` and `CN-k-4` on the canon, which share ONE slot sequenced.
</preflight>

Seating: slot ~8, queue position 1. Round 2 of LGIC_CANON, the recut of `1.0.0_SA_CTO`'s round-1 ANALYSIS (`org/tier1_exec/1.0.0_SA_CTO/deliverables/LGIC_CANON_ROUND1_ANALYSIS.md @26ae876d23`, msg 97317) on `3.0.0_SA_CVO`'s L10 slug; issued by `2.0.0_SA_COO~G`, which holds LGIC_CANON under Andrew-direct 2026-09-16 ~05:2xZ. Decomposition v4 @2b987c131d, section 0d. Distinct-worker constraints: the three judges are blind to each other and to `CN-k-2`'s author; `CN-j-7` judged nothing; `CN-o-4`'s worker did not write `CN-o-3`.
