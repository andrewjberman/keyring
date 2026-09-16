# TO LGIC_CANON.CN-j-4-r2 -- judge C, blind, on the SECOND tree, from the canon alone

<to_id>LGIC_CANON.CN-j-4-r2</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~4</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-16</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_CANON_PRD.md` v1.3 @5b2336a5e4 (ADMITTED; both halves SIGNED and `current`, re-read at the recut) | **Decomp cell:** `CN-j-4` (round 2, decomposition v4) | **outcome_ref:** FWD-1 | **rulings:** A-1, A-13 | **depends_on:** CN-k-2 | **slot:** ~4, queue position 1, level 1

---

## WORKER FACE

### THE CELL

`CN-j-4` -- judge C. You judge a pipeline tree against the canon, BLIND: you do not read any other judge's output,
and no other judge reads yours.

Your tree is `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/CN_TREE_INFLECTION.md`. Your rule source is `infra/logic/02_DOCTRINE.md` ALONE -- not the ledger's
dispositions, which are another seat's verdicts on the same planes, and not the migration briefs.

Write `org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/r2/judge-c.tsv`, one row per plane in your tree, tab-separated, with a header row:

    plane<TAB>A1<TAB>A2<TAB>A3<TAB>A4<TAB>A5<TAB>rules<TAB>reach<TAB>why

- the five axis columns each carry exactly one verdict from `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/CN_SEVERITY.md`;
- `rules` names the canon rule each verdict rests on -- the DECIDING rule, per the canon's citation rule;
- `reach` names any of A-13's seven rules (`org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/CN_SEVEN_RULES.json`) this plane engages, or is empty;
- `why` is one sentence.

⛔ **A PRINTED `NOT REACHED` IS A CORRECT ANSWER.** Read `CN_SEVEN_RULES.json`'s `_about` before you start: R21 is
marked `reachable_today: false` because no conformant `state/` plane exists anywhere in the estate (row
`LGIC_CANON-S4`). If you cannot reach a rule, say so; do not stretch a plane to fit one.

**Read:** `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/CN_TREE_INFLECTION.md`; `infra/logic/02_DOCTRINE.md`; `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/CN_SEVERITY.md`; `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/CN_SEVEN_RULES.json`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="J4-AC1" cell_refs="CN-j-4"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py j4-axes</invocation><expect>PASS-J4-EVERY-AXIS-JUDGED</expect></criterion>
`J4-AC1` -- every row carries all five axis verdicts.
<criterion id="J4-AC2" cell_refs="CN-j-4"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py j4-cites</invocation><expect>PASS-J4-EVERY-VERDICT-CITES</expect></criterion>
`J4-AC2` -- every row cites at least one canon rule.
<criterion id="J4-AC3" cell_refs="CN-j-4"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py j4-reach</invocation><expect>PASS-J4-REACH-PRINTED</expect></criterion>
`J4-AC3` -- the seven-rule reach is printed with its denominator.
<criterion id="J4-J1" cell_refs="CN-j-4" judgment="true"/>
`J4-J1` -- graded at L9 by 3.0.0_SA_CVO: each verdict rests on the rule it cites, and an UNDETERMINED is a real hole in the canon rather than a parked hard case. RECORD; NO VERDICT.

<expected_criteria>J4-AC1, J4-AC2, J4-AC3, J4-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_CANON/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are READ-ONLY.** `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/` holds round 2's checker `check_canon_r2.py` (every mechanical criterion calls it) and its inputs. Never edit any of them. ⚠ If a fixed input is itself DEFECTIVE, that is a BLOCKING surprise row and you keep your hands off it -- LGIC_ENFORCE round 2 lost an hour to a corrupt fixture, and the worker that filed a row instead of editing around it is the reason the defect was found in the fixture rather than papered over in the code.
- **Nothing live moves.** No cell of this project renames a live name, writes to AWS, runs Terraform, or calls anything off Opal infrastructure. Every `.py` you touch passes `.tools/commit-gate.sh` (safe-commit runs it).
- **Surprises** go to `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_CANON-W4-S<k>`. Keep working after filing. **Re-read the channel immediately before you write** -- rows land from other cells and an id minted from an earlier read collides silently. **`class` takes exactly TWO values, `OBSERVATION` or `BLOCKING`**; a third is refused by the corpus limb at `/class`, measured 2026-09-16.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context. Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Pins by commit.** Every artifact your proof instance cites names the commit that carries it: commit the artifact first, then the proof in a later commit. Never `PENDING-THIS-COMMIT`.

<paths>
org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/r2/judge-c.tsv
org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v4, cell `CN-j-4`, round 2 (section 0d).
<owned_cells>CN-j-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `J4-AC1`, `J4-AC2`, `J4-AC3`, `J4-J1`. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~4/LGIC_CANON.CN-j-4-r2.judge-c.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> J4-AC1,J4-AC2,J4-AC3,J4-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `judge-c.r2.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~4, queue position 1. Round 2 of LGIC_CANON, the recut of `1.0.0_SA_CTO`'s round-1 ANALYSIS (`org/tier1_exec/1.0.0_SA_CTO/deliverables/LGIC_CANON_ROUND1_ANALYSIS.md @26ae876d23`, msg 97317) on `3.0.0_SA_CVO`'s L10 slug; issued by `2.0.0_SA_COO~G`, which holds LGIC_CANON under Andrew-direct 2026-09-16 ~05:2xZ. Decomposition v4 @2b987c131d, section 0d. Distinct-worker constraints: the three judges are blind to each other and to `CN-k-2`'s author; `CN-j-7` judged nothing; `CN-o-4`'s worker did not write `CN-o-3`.
