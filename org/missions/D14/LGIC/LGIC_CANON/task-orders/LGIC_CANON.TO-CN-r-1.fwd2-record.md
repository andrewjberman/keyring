# TO LGIC_CANON.TO-CN-r-1 -- FWD-2 graded from the record

<to_id>LGIC_CANON.TO-CN-r-1</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_CANON_PRD.md` v1.3 @5b2336a5e4 (ADMITTED; brief half signed by 4.0.0_SA_CRO, ratified-text half by 3.0.0_SA_CVO, both current) | **Decomp cell:** `CN-r-1` (round 1) | **outcome_ref:** FWD-2 | **depends_on:** -- (level 0; spawned at issuance) | **slot:** ~3, queue position 1

---

## WORKER FACE

### THE CELL

`CN-r-1` -- FWD-2 from the record (PRD DEC-3; cell candidate C3). FWD-2 is graded from the record, not re-staged: no new sitting is asked of Andrew. Its ACCEPT, verbatim: *"he works down the whole list in one sitting; every case has enough beside it to decide on without going and looking something up; the ones he has already decided are already filled in"*.

Write `org/missions/D14/LGIC/LGIC_CANON/deliverables/FWD2_FROM_RECORD.md`:
- Three lines, exactly `CLAUSE 1:` (one sitting), `CLAUSE 2:` (enough beside every row) and `CLAUSE 3:` (the pre-decided rows pre-filled), each followed by its evidence cited as `path@commit`, where the path exists at that commit.
- Read `infra/logic/04_SCOPE_TICKLIST.md` at HEAD, and quote its v0.2 TICKED line, *"Nothing on this table is open"*, citing `infra/logic/04_SCOPE_TICKLIST.md@<commit>`.

**The evidence the PRD names:** the nine-calls record, `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260913_013xZ_NINE_CALLS_RULED_PAUSE_LIFTED_D10-2_DEMO_KEPT.md` @c6be748be7 (card 3, "defaults"; rows 17 and 18 by his word); the table @6dab0d76a7; rows 14 to 16 pre-filled from his 2026-08-25 word. Tie each clause to its evidence. You grade nothing: the L9 grader decides (R1-J1).

**Read:** the record and the table above; the PRD's DEC-3.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="R1-AC1" cell_refs="CN-r-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py r1-clauses</invocation><expect>VERDICT: PASS-R1-CLAUSES-EVIDENCED</expect></criterion>
`R1-AC1` -- each of FWD-2's three ACCEPT clauses stands beside evidence cited `path@commit` that resolves.

<criterion id="R1-AC2" cell_refs="CN-r-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py r1-ticked</invocation><expect>VERDICT: PASS-R1-TICKED-QUOTED</expect></criterion>
`R1-AC2` -- the table's v0.2 TICKED state is quoted and cited at a commit where that text stands.

<criterion id="R1-J1" cell_refs="CN-r-1" judgment="true"/>
`R1-J1` -- graded at L9 by 3.0.0_SA_CVO: the evidence supports each clause. RECORD; NO VERDICT.

<expected_criteria>R1-AC1, R1-AC2, R1-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_CANON/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Nothing live moves (PRD DEC-9).** No cell of this project moves data, repoints a trigger, edits a bucket policy, writes to AWS, runs Terraform, or calls anything off Opal infrastructure.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/` holds this round's (`check_canon_r1.py`, the checker every criterion calls, and the fixtures its criteria name). Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_CANON-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Pins.** Pin every artifact your proof cites by the commit that carries it, never `PENDING-THIS-COMMIT`: a later commit touching the instance leaves such a pin stale (rows LGIC_NAMING-S18, W1-S7 and W2-S6 carry the class).
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
org/missions/D14/LGIC/LGIC_CANON/deliverables/FWD2_FROM_RECORD.md
org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v3, cell `CN-r-1`, round 1 (sections 3 and 0c).
<owned_cells>CN-r-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `R1-AC1`, `R1-AC2`, `R1-J1`. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~3/LGIC_CANON.TO-CN-r-1.fwd2-record.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> R1-AC1,R1-AC2,R1-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `fwd2-record.r1.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the cut -- --budget 540, 5 of 5 carriers scanned within budget (27.3 s used), 25 gates armed, 0 lines naming LGIC_CANON. This project registers G-C (worker admission, checked after this issuance), G-R (CLEARED: the registry is at HEAD, LGIC_ENFORCE cell r-1 @a925c8a642), G-N (Andrew's: C6 is not cut until a genuinely new firm exists) and G-V19R (the generated naming section re-rendered in whichever merge lands second, CN-k-1's drain or GROUP V19's).
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 1's write set: three documents and one render script under infra/logic/, and records under this project's deliverables/; no cell adds an operation, a policy, a principal or a resource, so the lens would receive an empty input.
comp-adversary: RUN at the cut on the PRD at v1.3 (@5b2336a5e4), read-vintage HEAD @2373f96073 -- 12 of 12 cited commits verified; 18 cited paths, 12 stable, 6 flagged (2 GONE, this project's to mint: 10_ONBOARDING_CHECKLIST.md and render_naming_section.py; 4 MOVED: 02_DOCTRINE.md and 06_CONFORMANCE_LEDGER.md @c9048873d1, SEQUENCE.yaml, NAMING_SCHEMA.json v1.8). Blindness stated: T11, the PRD carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). infra/logic/ sits in lane PLATFORM_LOGIC_DOCS and a path directly under deliverables/ in TREE_DELIVERABLES; each is admitted to this worker only by this order's <paths>.
</preflight>

Seating: slot ~3, queue position 1. Round 1 of LGIC_CANON, its first issuance, cut from decomposition v3 by `2.0.0_SA_COO~G`, seated on this project by `1.0.0_SA_CTO` @52ea4c8cac on Andrew-direct ~16:1xZ ("parallelize harder"). The fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/`.
