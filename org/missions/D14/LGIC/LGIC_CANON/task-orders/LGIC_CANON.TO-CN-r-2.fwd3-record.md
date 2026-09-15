# TO LGIC_CANON.TO-CN-r-2 -- FWD-3 graded from the record

<to_id>LGIC_CANON.TO-CN-r-2</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_CANON_PRD.md` v1.3 @5b2336a5e4 (ADMITTED; brief half signed by 4.0.0_SA_CRO, ratified-text half by 3.0.0_SA_CVO, both current) | **Decomp cell:** `CN-r-2` (round 1) | **outcome_ref:** FWD-3 | **depends_on:** -- (no edge; queue position 2 on slot ~3, after CN-r-1) | **slot:** ~3, queue position 2

---

## WORKER FACE

### THE CELL

`CN-r-2` -- FWD-3 from the record (PRD DEC-4; cell candidate C4). The pause lifted for both IRPT projects at card 1 of the nine-calls record, by name. FWD-3's ACCEPT: the person running a paused project *"can point at what ended the pause -- either nothing in their plan conflicts, or here is the list of things to change, or here is the other project whose answer decides theirs"*.

Write `org/missions/D14/LGIC/LGIC_CANON/deliverables/FWD3_FROM_RECORD.md`:
- One line per project, exactly `PROJECT IRPT_FNTEND: branch <b>` and `PROJECT IRPT_BCKEND: branch <b>`, where `<b>` is `nothing-conflicts`, `list-of-changes` or `derived`, with the row that ended the pause cited `path@commit` on the same line.
- IRPT_BCKEND's PRD version at HEAD, measured, on its own line: `IRPT_BCKEND PRD AT HEAD: <prd_version> (MEASURED)`, read from `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`.
- `CONTRADICTS ABSORBED: <n> of 3 (MEASURED)`, for its three CONTRADICTS: the `platinum/` prefix (R1); the gold parquet artifact between silver and the served JSON (R11, R14); the vendor PDFs' home (R4, partial). The PRD's DEC-4 says v0.14 @b8e98d5a4d carries none of them. Measure it; do not copy it. If it is still open, say so: the record must not read cleaner than the estate is.

**Read:** the nine-calls record (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260913_013xZ_NINE_CALLS_RULED_PAUSE_LIFTED_D10-2_DEMO_KEPT.md` @c6be748be7, card 1); `infra/logic/03_CONTRADICTION_REPORTS/IRPT_FNTEND.md` and `IRPT_BCKEND.md`; both IRPT PRDs (`org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`, `org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md`); the PRD's DEC-4.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="R2-AC1" cell_refs="CN-r-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py r2-branches</invocation><expect>VERDICT: PASS-R2-BRANCHES-CITED</expect></criterion>
`R2-AC1` -- each IRPT project's pause-ending row is cited with the branch it took.

<criterion id="R2-AC2" cell_refs="CN-r-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py r2-bckend</invocation><expect>VERDICT: PASS-R2-BCKEND-MEASURED</expect></criterion>
`R2-AC2` -- IRPT_BCKEND's PRD version at HEAD is stated as measured, with the absorption of its three CONTRADICTS.

<criterion id="R2-J1" cell_refs="CN-r-2" judgment="true"/>
`R2-J1` -- graded at L9 by 3.0.0_SA_CVO: the record supports the branch named for each project. RECORD; NO VERDICT.

<expected_criteria>R2-AC1, R2-AC2, R2-J1</expected_criteria>

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
org/missions/D14/LGIC/LGIC_CANON/deliverables/FWD3_FROM_RECORD.md
org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v3, cell `CN-r-2`, round 1 (sections 3 and 0c).
<owned_cells>CN-r-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `R2-AC1`, `R2-AC2`, `R2-J1`. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~3/LGIC_CANON.TO-CN-r-2.fwd3-record.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> R2-AC1,R2-AC2,R2-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `fwd3-record.r1.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~3, queue position 2. Round 1 of LGIC_CANON, its first issuance, cut from decomposition v3 by `2.0.0_SA_COO~G`, seated on this project by `1.0.0_SA_CTO` @52ea4c8cac on Andrew-direct ~16:1xZ ("parallelize harder"). The fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/`.
