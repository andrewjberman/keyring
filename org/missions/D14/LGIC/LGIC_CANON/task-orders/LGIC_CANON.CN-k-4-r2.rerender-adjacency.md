# TO LGIC_CANON.CN-k-4-r2 -- the canon re-rendered once the schema carries the bd adjacency test

<to_id>LGIC_CANON.CN-k-4-r2</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-16</issued_date>
<status>withdrawn -- 2.0.0_SA_COO~G, 2026-09-16, under 1.0.0_SA_CTO RULING R-10 @41026094e7 on row LGIC_CANON-S11 @f8eb631fa8. NEVER SPAWNED; no worker ever held this order and no criterion was ever run.

WHY: this cell re-renders the canon's generated section AFTER ruling A-3's `bd` adjacency test lands in `org/standards/NAMING_SCHEMA.json`, and that edit is LGIC_NAMING's, not this project's. It is NOT at HEAD. Measured on two instruments: `comp-find 'adjacen' org/standards/NAMING_SCHEMA.json` reads 0 hits across 1 file scanned; a structural read of the parsed JSON prints 271 schema paths with 0 matching `adjacen` and 0 matching `test`, and raw occurrences of `adjacen`/`adjacency` are 0 (schema declares v1.9). The 9 paths matching `bd` are LAMBDA type entries and `/refused_tokens/bd`, none an adjacency test.

⛔ THE OBLIGATION IS CARRIED UNMET INTO ROUND 3, NOT DISCHARGED. Verbatim, so no later reader mistakes a withdrawal for a completion: re-render the canon's generated section after `NAMING_SCHEMA.json` carries the `bd` adjacency test, with `K4-AC1` as cut (`render_naming_section.py --write` then `--check` printing `CHECK: FRESH -- 0 failure(s)`). Round 3 carries it as a cell depending on LGIC_NAMING round 5's schema cell -- a cross-project READ dependency, disclosed on the cell.

⚠ AND THE CONSEQUENCE IS STATED RATHER THAN SOFTENED: the canon and the schema MAY DISAGREE AT HEAD until round 3 lands this. Round 2 ships with that disagreement open and the round-2 analysis says so in terms.

NOT SPAWNED DELIBERATELY: running it would correctly FAIL K4-AC1 and leave the order open, costing a worker, a worktree and about 1.5 GB to reproduce a result both instruments above already carry with a printed denominator -- repetition, not measurement (R-10).

CHAIN, one owner per link: 3.0.0_SA_CVO's LGIC_NAMING round-4 L10 slug -> 1.0.0_SA_CTO's round-4 analysis (A-3's schema edit as a round-5 cell) -> 2.0.0_SA_COO~G's LGIC_NAMING round 5 -> the schema carries the test -> LGIC_CANON round 3's re-render cell.</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_CANON_PRD.md` v1.3 @5b2336a5e4 (ADMITTED; both halves SIGNED and `current`, re-read at the recut) | **Decomp cell:** `CN-k-4` (round 2, decomposition v4) | **outcome_ref:** FWD-1 | **rulings:** A-3 | **depends_on:** LGIC_NAMING's schema cell (cross-project READ dependency, disclosed); spawned only when it drains | **slot:** ~1, queue position 2, level 0

---

## WORKER FACE

### THE CELL

`CN-k-4` -- the re-render. Ruling A-3 puts the `bd` adjacency test into `NAMING_SCHEMA.json`, and that edit is
LGIC_NAMING's, not yours. When it lands, the canon's generated section must be re-rendered so the canon and the schema
do not disagree at HEAD -- the same obligation gate G-V19R carried, and it is met the same way: the render runs in the
merge or in the commit immediately following it, in the lane that owns the path.

Run `python infra/logic/render_naming_section.py --write`, then `--check`, which must print `CHECK: FRESH -- 0 failure(s)`.
Change nothing else. If the schema does not carry an adjacency test when you run, K4-AC1 FAILs by measurement and your
order stays open -- that is a correct result and NOT a reason to edit the schema, which is not yours.

**Read:** `org/standards/NAMING_SCHEMA.json`; `infra/logic/render_naming_section.py`; the canon's generated section.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="K4-AC1" cell_refs="CN-k-4"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py k4-adjacency</invocation><expect>PASS-K4-SCHEMA-CARRIES-ADJACENCY</expect></criterion>
`K4-AC1` -- the schema carries the adjacency test.
<criterion id="K4-AC2" cell_refs="CN-k-4"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py k4-fresh</invocation><expect>PASS-K4-RERENDERED-AT-SCHEMA</expect></criterion>
`K4-AC2` -- the section stamps the schema and the render reads FRESH.

<expected_criteria>K4-AC1, K4-AC2</expected_criteria>

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
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v4, cell `CN-k-4`, round 2 (section 0d).
<owned_cells>CN-k-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `K4-AC1`, `K4-AC2`. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/LGIC_CANON.CN-k-4-r2.rerender-adjacency.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> K4-AC1,K4-AC2` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `rerender-adjacency.r2.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~1, queue position 2. Round 2 of LGIC_CANON, the recut of `1.0.0_SA_CTO`'s round-1 ANALYSIS (`org/tier1_exec/1.0.0_SA_CTO/deliverables/LGIC_CANON_ROUND1_ANALYSIS.md @26ae876d23`, msg 97317) on `3.0.0_SA_CVO`'s L10 slug; issued by `2.0.0_SA_COO~G`, which holds LGIC_CANON under Andrew-direct 2026-09-16 ~05:2xZ. Decomposition v4 @2b987c131d, section 0d. Distinct-worker constraints: the three judges are blind to each other and to `CN-k-2`'s author; `CN-j-7` judged nothing; `CN-o-4`'s worker did not write `CN-o-3`.
