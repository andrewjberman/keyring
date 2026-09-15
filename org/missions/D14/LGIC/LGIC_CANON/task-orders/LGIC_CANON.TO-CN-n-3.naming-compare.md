# TO LGIC_CANON.TO-CN-n-3 -- the naming comparison

<to_id>LGIC_CANON.TO-CN-n-3</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~7</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_CANON_PRD.md` v1.3 @5b2336a5e4 (ADMITTED; brief half signed by 4.0.0_SA_CRO, ratified-text half by 3.0.0_SA_CVO, both current) | **Decomp cell:** `CN-n-3` (round 1) | **outcome_ref:** FWD-4 | **depends_on:** CN-n-1 and CN-n-2 (this order when both have drained) | **slot:** ~7, queue position 3

---

## WORKER FACE

### THE CELL

`CN-n-3` -- the naming comparison (PRD DEC-5; cell candidate C7). Two workers did one naming job for 49 Financial, blind to each other: `org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/naming-a.tsv` and `org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/naming-b.tsv`. Compare both with the canonical key, `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/CN_NAMING_KEY.json` (the builders' outputs, slot-aware).

Write `org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/naming-compare.md`, with one line per item, exactly `ITEM <id>: PASS` or `ITEM <id>: FAIL -- <which worker, and what differed>`. PASS means BOTH answers equal the canonical value for that job, surface and slot.
- A sanctioned LONG form (`49financial` in a bucket name or a key's scope segment) or SHORT form (`49f` in a resource name) is NEVER a failure.
- A refused token (`bd`, in any slot), an alias, or a sanctioned form in the wrong slot IS a failure.
- Item n6 is the refused-token trap.

**Read:** the two answer files; the key; `org/standards/NAMING_SCHEMA.json`; `infra/logic/registry/scopes.json`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="N3-AC1" cell_refs="CN-n-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py n3-equal</invocation><expect>VERDICT: PASS-N3-BOTH-CANONICAL</expect></criterion>
`N3-AC1` -- both outputs equal the canonical value fixed at L6 for each job, surface and slot.

<criterion id="N3-AC2" cell_refs="CN-n-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py n3-trap</invocation><expect>VERDICT: PASS-N3-TRAP-CAUGHT</expect></criterion>
`N3-AC2` -- the refused or wrong-slot item is caught in both.

<criterion id="N3-AC3" cell_refs="CN-n-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py n3-sanctioned</invocation><expect>VERDICT: PASS-N3-SANCTIONED-KEPT</expect></criterion>
`N3-AC3` -- a sanctioned LONG or SHORT form is never counted as a failure.

<criterion id="N3-AC4" cell_refs="CN-n-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py n3-blind</invocation><expect>VERDICT: PASS-N3-MUTUALLY-BLIND</expect></criterion>
`N3-AC4` -- neither worker's base commit carries the other's answer file.

<expected_criteria>N3-AC1, N3-AC2, N3-AC3, N3-AC4</expected_criteria>

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
org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/naming-compare.md
org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v3, cell `CN-n-3`, round 1 (sections 3 and 0c).
<owned_cells>CN-n-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `N3-AC1`, `N3-AC2`, `N3-AC3`, `N3-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~7/LGIC_CANON.TO-CN-n-3.naming-compare.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> N3-AC1,N3-AC2,N3-AC3,N3-AC4` BEFORE the `complete` flip.
Result file `naming-compare.r1.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~7, queue position 3. Round 1 of LGIC_CANON, its first issuance, cut from decomposition v3 by `2.0.0_SA_COO~G`, seated on this project by `1.0.0_SA_CTO` @52ea4c8cac on Andrew-direct ~16:1xZ ("parallelize harder"). The fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/`.
