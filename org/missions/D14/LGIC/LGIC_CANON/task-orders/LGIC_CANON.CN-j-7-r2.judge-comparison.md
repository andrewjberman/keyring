# TO LGIC_CANON.CN-j-7-r2 -- the comparison over judges C, D and E, every disagreement traced to a canon coordinate

<to_id>LGIC_CANON.CN-j-7-r2</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~7</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-16</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_CANON_PRD.md` v1.3 @5b2336a5e4 (ADMITTED; both halves SIGNED and `current`, re-read at the recut) | **Decomp cell:** `CN-j-7` (round 2, decomposition v4) | **outcome_ref:** FWD-1 | **rulings:** A-13 | **depends_on:** CN-j-4, CN-j-5, CN-j-6 | **slot:** ~7, queue position 1, level 2

---

## WORKER FACE

### THE CELL

`CN-j-7` -- the comparison. You did not judge, and you must not have: a scorer never scores its own work.

Read `judge-c.tsv`, `judge-d.tsv` and `judge-e.tsv` under `org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/r2` and write `org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/r2/judge-compare-r2.md`.

1. **Agreement and disagreement, per plane per axis.** Every disagreement gets its own row, marked `DISAGREE`, and
   every such row TRACES to a canon coordinate -- a rule id, an axis id, or a channel row id -- naming WHERE the canon
   left room for two readings. A disagreement you cannot trace is itself the finding: say so on the row.
2. **The seven-rule reach (A-13), printed with its denominator**, over the union of C and D, and separately for E.
   The output must carry an explicit `NOT REACHED` partition; an empty reach is a result, never an omission.
3. **THE ARM'S ANSWER, and it is what this cell is for.** C and D had the severity order; E did not. State whether E's
   verdicts diverge from C's and D's in the way the severity order would predict. If they do NOT diverge, round 1's
   five-of-five agreement was agreement on the CANON and C-S9's worry is answered. If they DO, the canon was carrying
   less of the scale than the agreement suggested. Say which, with the rows that show it.

⛔ **Do not resolve a disagreement by picking a winner.** Your job is to locate it in the canon, not to adjudicate it;
adjudication is `3.0.0_SA_CVO`'s at L9.

**Read:** `org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/r2/judge-c.tsv`, `org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/r2/judge-d.tsv`, `org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/r2/judge-e.tsv`; `infra/logic/02_DOCTRINE.md`;
`org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/CN_SEVEN_RULES.json`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="J7-AC1" cell_refs="CN-j-7"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py j7-traced</invocation><expect>PASS-J7-EVERY-DISAGREEMENT-TRACED</expect></criterion>
`J7-AC1` -- every disagreement row traces to a canon coordinate, and the comparison actually ran.
<criterion id="J7-AC2" cell_refs="CN-j-7"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py j7-reach</invocation><expect>PASS-J7-SEVEN-RULE-REACH-PRINTED</expect></criterion>
`J7-AC2` -- all seven rules are named and a NOT REACHED partition is printed.
<criterion id="J7-AC3" cell_refs="CN-j-7"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py j7-blind</invocation><expect>PASS-J7-JUDGES-MUTUALLY-BLIND</expect></criterion>
`J7-AC3` -- no judge's file names another judge's file -- the blind held.
<criterion id="J7-J1" cell_refs="CN-j-7" judgment="true"/>
`J7-J1` -- graded at L9 by 3.0.0_SA_CVO: the arm's answer follows from the rows shown, and a no-divergence finding is not read as proof of agreement it did not test. RECORD; NO VERDICT.

<criterion id="J7-AC4" cell_refs="CN-j-7"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py j7-e-vocab</invocation><expect>PASS-J7-E-VOCAB-FROM-CANON</expect></criterion>
`J7-AC4` -- every verdict value judge E used OCCURS in the canon E read, by a whole-word census with its denominator printed. THIS IS THE NEGATIVE ARM'S OWN MEASUREMENT and it lives here because a control must never self-grade (RULING R-8 c, row `LGIC_CANON-S6`): E was briefed with NO severity order, so a verdict value E used that the canon does not carry means E got it somewhere else, and that is the finding rather than a failure of E.

<expected_criteria>J7-AC1, J7-AC2, J7-AC3, J7-AC4, J7-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_CANON/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are READ-ONLY.** `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/` holds round 2's checker `check_canon_r2.py` (every mechanical criterion calls it) and its inputs. Never edit any of them. ⚠ If a fixed input is itself DEFECTIVE, that is a BLOCKING surprise row and you keep your hands off it -- LGIC_ENFORCE round 2 lost an hour to a corrupt fixture, and the worker that filed a row instead of editing around it is the reason the defect was found in the fixture rather than papered over in the code.
- **Nothing live moves.** No cell of this project renames a live name, writes to AWS, runs Terraform, or calls anything off Opal infrastructure. Every `.py` you touch passes `.tools/commit-gate.sh` (safe-commit runs it).
- **Surprises** go to `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_CANON-W7-S<k>`. Keep working after filing. **Re-read the channel immediately before you write** -- rows land from other cells and an id minted from an earlier read collides silently. **`class` takes exactly TWO values, `OBSERVATION` or `BLOCKING`**; a third is refused by the corpus limb at `/class`, measured 2026-09-16.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context. Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Pins by commit.** Every artifact your proof instance cites names the commit that carries it: commit the artifact first, then the proof in a later commit. Never `PENDING-THIS-COMMIT`.

<paths>
org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/r2/judge-compare-r2.md
org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v4, cell `CN-j-7`, round 2 (section 0d).
<owned_cells>CN-j-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `J7-AC1`, `J7-AC2`, `J7-AC3`, `J7-AC4`, `J7-J1`. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~7/LGIC_CANON.CN-j-7-r2.judge-comparison.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> J7-AC1,J7-AC2,J7-AC3,J7-AC4,J7-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `judge-comparison.r2.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~7, queue position 1. Round 2 of LGIC_CANON, the recut of `1.0.0_SA_CTO`'s round-1 ANALYSIS (`org/tier1_exec/1.0.0_SA_CTO/deliverables/LGIC_CANON_ROUND1_ANALYSIS.md @26ae876d23`, msg 97317) on `3.0.0_SA_CVO`'s L10 slug; issued by `2.0.0_SA_COO~G`, which holds LGIC_CANON under Andrew-direct 2026-09-16 ~05:2xZ. Decomposition v4 @2b987c131d, section 0d. Distinct-worker constraints: the three judges are blind to each other and to `CN-k-2`'s author; `CN-j-7` judged nothing; `CN-o-4`'s worker did not write `CN-o-3`.
