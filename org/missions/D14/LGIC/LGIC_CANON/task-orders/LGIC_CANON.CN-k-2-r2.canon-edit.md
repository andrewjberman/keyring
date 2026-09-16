# TO LGIC_CANON.CN-k-2-r2 -- the canon carries the verdict vocabulary, the severity order, R20 on every axis, the citation rule and the pipeline-instance rule

<to_id>LGIC_CANON.CN-k-2-r2</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-16</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_CANON_PRD.md` v1.3 @5b2336a5e4 (ADMITTED; both halves SIGNED and `current`, re-read at the recut) | **Decomp cell:** `CN-k-2` (round 2, decomposition v4) | **outcome_ref:** FWD-1, FWD-5 (instrument) | **rulings:** A-1, A-2, A-4, A-9 | **depends_on:** nothing | **slot:** ~1, queue position 1, level 0

---

## WORKER FACE

### THE CELL

`CN-k-2` -- the canon edit. Round 1 graded FWD-1 SHORT, and the CVO's finding C-S9 is why: the five-of-five
verdict agreement round 1 measured was agreement between judges who shared a scale the CANON DID NOT CARRY. Round 2
puts the scale in the canon, so a later agreement measures the canon rather than the brief. Edit `infra/logic/02_DOCTRINE.md`:

1. **The axis verdict vocabulary (A-1).** State the five axis verdicts the estate uses -- `CONFORMS`,
   `DECLARED-EXCEPTION`, `DEPARTS-RECOMMENDED`, `UNDETERMINED`, `VIOLATES` -- as the canon's own closed set.
2. **The SEVERITY ORDER (A-1).** State them ORDERED, least severe to most, in a passage the canon names
   `SEVERITY ORDER`, and say for each of the two non-obvious placements WHY it sits where it does. A plane's overall
   reading is the most severe verdict across its five axes. `CN_SEVERITY.md` beside the checker is the issuer's
   statement of the same order; where your text and it differ, say so in a surprise row rather than silently picking one.
3. **R20 on EVERY axis (A-2).** R20's own block must name all five axes A1 to A5. Today it does not, and a rule that
   reads as global while being stated once is the defect: a judge cannot tell which axis it was meant to reach.
4. **The citation rule (A-2).** A verdict cites the DECIDING rule -- the one rule the verdict rests on -- not every
   rule in the neighbourhood. State it, using the phrase DECIDING RULE so it is greppable.
5. **ONE pipeline-instance rule (A-9).** Add exactly one rule whose heading names PIPELINE INSTANCE, which fixes what a
   pipeline family carries -- its directory, its master row's label, its resource set, its table names and its partition
   form. The onboarding checklist's steps 3, 7, 8 and 9 read it; they are `CN-o-3`'s and you do not edit them.

⛔ **DO NOT TOUCH THE GENERATED NAMING SECTION.** Everything between the two marker comments is rendered by
`render_naming_section.py` from the schema and the registry. Your criterion K2-AC6 exists to prove you did not.

**Read:** `infra/logic/02_DOCTRINE.md` (the whole canon; R20 at :483, R1 at :112, the five axes at section 2); the
round-1 analysis s.2 rulings A-1, A-2, A-4 and A-9 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/LGIC_CANON_ROUND1_ANALYSIS.md @26ae876d23`); `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/CN_SEVERITY.md`; the CVO's finding C-S9 in
`org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v1.md`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="K2-AC1" cell_refs="CN-k-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py k2-vocab</invocation><expect>PASS-K2-VOCAB-CARRIED</expect></criterion>
`K2-AC1` -- the canon carries all five axis verdicts as its own closed set.
<criterion id="K2-AC2" cell_refs="CN-k-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py k2-severity</invocation><expect>PASS-K2-SEVERITY-ORDERED</expect></criterion>
`K2-AC2` -- a SEVERITY ORDER passage places every one of the five, in order.
<criterion id="K2-AC3" cell_refs="CN-k-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py k2-r20-axes</invocation><expect>PASS-K2-R20-ON-EVERY-AXIS</expect></criterion>
`K2-AC3` -- R20's own block names all five axes.
<criterion id="K2-AC4" cell_refs="CN-k-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py k2-citation</invocation><expect>PASS-K2-CITATION-RULE-STATED</expect></criterion>
`K2-AC4` -- the canon states the citation rule and names a DECIDING RULE.
<criterion id="K2-AC5" cell_refs="CN-k-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py k2-instance</invocation><expect>PASS-K2-INSTANCE-RULE-ONCE</expect></criterion>
`K2-AC5` -- exactly one rule heading names PIPELINE INSTANCE.
<criterion id="K2-AC6" cell_refs="CN-k-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py k2-render-fresh</invocation><expect>PASS-K2-GENERATED-SECTION-UNTOUCHED</expect></criterion>
`K2-AC6` -- the generated naming section is untouched: the render still reads FRESH.
<criterion id="K2-J1" cell_refs="CN-k-2" judgment="true"/>
`K2-J1` -- graded at L9 by 3.0.0_SA_CVO: the severity order's two non-obvious placements are argued, not asserted, and the pipeline-instance rule is one a checklist step can actually execute. RECORD; NO VERDICT.

<expected_criteria>K2-AC1, K2-AC2, K2-AC3, K2-AC4, K2-AC5, K2-AC6, K2-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_CANON/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are READ-ONLY.** `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/` holds round 2's checker `check_canon_r2.py` (every mechanical criterion calls it) and its inputs. Never edit any of them. ⚠ If a fixed input is itself DEFECTIVE, that is a BLOCKING surprise row and you keep your hands off it -- LGIC_ENFORCE round 2 lost an hour to a corrupt fixture, and the worker that filed a row instead of editing around it is the reason the defect was found in the fixture rather than papered over in the code.
- **Nothing live moves.** No cell of this project renames a live name, writes to AWS, runs Terraform, or calls anything off Opal infrastructure. Every `.py` you touch passes `.tools/commit-gate.sh` (safe-commit runs it).
- **Surprises** go to `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_CANON-W1-S<k>`. Keep working after filing. **Re-read the channel immediately before you write** -- rows land from other cells and an id minted from an earlier read collides silently. **`class` takes exactly TWO values, `OBSERVATION` or `BLOCKING`**; a third is refused by the corpus limb at `/class`, measured 2026-09-16.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context. Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Pins by commit.** Every artifact your proof instance cites names the commit that carries it: commit the artifact first, then the proof in a later commit. Never `PENDING-THIS-COMMIT`.

<paths>
infra/logic/02_DOCTRINE.md
org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v4, cell `CN-k-2`, round 2 (section 0d).
<owned_cells>CN-k-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `K2-AC1`, `K2-AC2`, `K2-AC3`, `K2-AC4`, `K2-AC5`, `K2-AC6`, `K2-J1`. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/LGIC_CANON.CN-k-2-r2.canon-edit.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> K2-AC1,K2-AC2,K2-AC3,K2-AC4,K2-AC5,K2-AC6,K2-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `canon-edit.r2.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~1, queue position 1. Round 2 of LGIC_CANON, the recut of `1.0.0_SA_CTO`'s round-1 ANALYSIS (`org/tier1_exec/1.0.0_SA_CTO/deliverables/LGIC_CANON_ROUND1_ANALYSIS.md @26ae876d23`, msg 97317) on `3.0.0_SA_CVO`'s L10 slug; issued by `2.0.0_SA_COO~G`, which holds LGIC_CANON under Andrew-direct 2026-09-16 ~05:2xZ. Decomposition v4 @2b987c131d, section 0d. Distinct-worker constraints: the three judges are blind to each other and to `CN-k-2`'s author; `CN-j-7` judged nothing; `CN-o-4`'s worker did not write `CN-o-3`.
