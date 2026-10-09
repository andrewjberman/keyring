# TO LGIC_ENFORCE.TO-EN-z-5 -- round 20 EN-z-5: row D1-W2-S12: one planted PATTERN-name commit on a QA branch, read for its grade
<to_id>LGIC_ENFORCE.TO-EN-z-5</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~2</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `EN-z-5` (`decompositions/LGIC_ENFORCE_DECOMP.md` section 0u) | **outcome_ref:** FWD-5 |
**depends_on:** EN-z-4 (same slot; reads the gate EN-z-4 leaves)

---

## WORKER FACE

### CONTEXT

**Where the project stands.** LGIC_ENFORCE has 6 of 7 outcomes REALIZED. FWD-5 (PRD `org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md`, the FWD-5 card
at line 132; cell E9 at line 402) reads: anyone can run the check over the whole estate -- the stored code AND what is actually
running -- and get a ranked list of every name that breaks the pattern, each with its correct form, totals shown; the totals agree with
the ranking the naming work produced by hand; and a name the check cannot read STOPS the run loudly rather than being filed as breaking
the pattern. The CTO's grade (`org/missions/D14/LGIC/LGIC_ENFORCE/ledger/FWD5_GRADE_FROM_BLANKFIX_FWD9_20261008.md`, last section): the stored-code half is MET (86 of 86 roots, 0 holes); round 20 owes the live
plane, the hand-ranking compare, the loud stop, and two gate rows (D1-W2-S9, D1-W2-S12).

**The instruments.** `python lib/opal_naming.py census [--live] [--repo] [--names FILE] [--not-judged FILE] [--report PATH]`
judges names with `grade()`; the live plane is `comp-find --corpus aws` (about 8 s); a RAISE (a name `grade()` cannot read) stops
the run with exit 3, unless the name is CARDED in the `--not-judged` JSON list (`{name, plane, card}`; R-29). `python
lib/opal_naming.py census --all-roots` (about 45 s) is the stored-code check; at the base `133bf5f7a4` it prints `ALL-ROOTS ok=True
roots_total=86 mapped=86 unmapped=0 ... hole=7 ...`. The commit gate is `.tools/naming-gate.py` (`--diff FILE`, `--self-test`),
called by `.tools/safe-commit.sh`; `lib/opal_naming_rootcheck.py place(name, typ, root)` returns a dict whose `kind` is one of RIGHT,
FIX, NOT-ASKED, PATTERN, CARDED, REFUSED, HOLE. The registry is `infra/logic/registry/`; only `4.0.0_SA_CRO` writes it. The switch
file `org/mcp/naming-place.enforce` is PRESENT and no cell touches it. Python 3.9 syntax, ASCII only, no new dependency. The checks
are `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r20/check_en_r20.py` (read-only; read it before you build -- each arm states exactly what it reads).

### THE CELL

`EN-z-5` (row `LGIC_BLANKFIX-D1-W2-S12`: "`place()` now returns PATTERN for the 14 per-firm names ... the commit-gate behaviour
on such a name is otherwise unmeasured"; ruled: "one planted pattern-name commit on a QA branch, read for its grade").

**Build:**
1. Choose one name that `lib/opal_naming_rootcheck.py place(name, typ, root)` places as PATTERN (a per-firm stored-file key, whose
   firm place is a variable). Record `planted_name`, `planted_type`, `planted_root` (the arguments that give PATTERN).
2. Make the QA branch from your worktree's HEAD: `git branch qa/lgic-enforce-r20-s12 HEAD`, then `git switch
   qa/lgic-enforce-r20-s12`. Add ONE file that carries the name on an added line in the shape its root's code uses, and commit it
   with `.tools/safe-commit.sh` (the real gate). Keep the commit's whole output in your result. Then `git switch` back to your
   worktree branch. The QA commit never reaches your worktree branch; never merge or push it.
3. `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/PATTERN_COMMIT_R20.json`: `qa_branch`, `planted_name`, `planted_type`, `planted_root`, `place_kind` ("PATTERN"),
   `commit_sha` (or null with `refused: true` and `commit_rc` when the gate refused the commit), `gate_summary` (the
   `NAMING-GATE:` line), `grade_line` (the gate's `NAMING ...` line for the name, or `NONE` with a `row_id` of the surprise row you
   file saying the gate graded nothing for it).
4. `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/pattern-commit.r20.result.md`: the commit output whole and what the grade means.

### ACCEPTANCE

<criterion id="Z5R20-AC1" cell_refs="EN-z-5"><invocation>python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r20/check_en_r20.py s12</invocation><expect>PASS-R20-S12</expect></criterion>
`Z5R20-AC1` -- place() gives PATTERN for the recorded name; the commit exists on the QA branch only (or its refusal is recorded); the grade line names the name or a row says the gate graded nothing.

<expected_criteria>Z5R20-AC1</expected_criteria>

Run every invocation from the root of your worktree. Each invocation's LAST printed line is the line the expectation is matched
against. Commit your artifacts first, then run the criteria against the committed bytes.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file. Nothing in this prose grants a path.
- **No edit outside the grant.** No AWS write (the live plane is read through `comp-find --corpus aws` only), no `terraform` command,
  no registry edit, no rename of any resource; `org/mcp/naming-place.enforce` and `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r20/check_en_r20.py` are never edited.
- **Refusal clause.** If a criterion cannot be met as written, stop on it, write the reason in your report and a surprise row (id
  `LGIC_ENFORCE-D1-W<n>-S<k>`, `<n>` your slot, `<k>` one above the highest in the channel at your write time; `surfaced_at` =
  `date -u +%FT%TZ` at filing; a row filed on dell1 carries the `-D1-` coordinate or the row gate refuses it) in
  `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` by textual splice, and never weaken a check or an expected value. A fact in this order the repository contradicts is
  also one row; keep working on what it does not block.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/PATTERN_COMMIT_R20.json
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/pattern-commit.r20.result.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/LGIC_ENFORCE.TO-EN-z-5.pattern-name-commit.proof_of_spec.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-z-5.pattern-name-commit.md
infra/aws/lambda/zz-lgic-enforce-r20-s12/*
infra/aws/terraform/zz-lgic-enforce-r20-s12/*
</paths>

The block is your WRITE grant. You read and never edit anything outside it.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.20, round-20 cell `EN-z-5` (section 0u).
<owned_cells>EN-z-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Z5R20-AC1. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/LGIC_ENFORCE.TO-EN-z-5.pattern-name-commit.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Z5R20-AC1 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-z-5.pattern-name-commit.md` BEFORE the
`complete` flip. Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.
</proof_of_spec>

**REPORT:** the planted name and its place() kind; the commit output; the grade line; the last line of every criterion whole; your commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no grant, no AWS call.
comp-adversary: RUN -- a name that is not a PATTERN: the check re-runs place() on the recorded arguments. The planted commit leaking into the trunk: the check refuses a commit reachable from HEAD. A grade invented in the record: the commit must exist and add the name. BLIND: the check does not re-run the commit gate on the QA commit; it reads the recorded summary, and the drain reads the result's whole commit output.
lane: the <paths> block IS the grant (worker RULING 1); nothing in the prose grants a path.
</preflight>

Source: `org/missions/D14/LGIC/LGIC_ENFORCE/ledger/FWD5_GRADE_FROM_BLANKFIX_FWD9_20261008.md` re-grade 2026-10-09 ~15:2xZ (`1.0.0_SA_CTO~DELL1`, msg 2639), round-20 list; decomposition section 0u. Base dry-run at
the cut, by the issuer at base 133bf5f7a4: Z5R20-AC1 base: FAIL as expected (PATTERN_COMMIT_R20.json absent).

## AMENDMENT 1 (2026-10-09 ~16:4xZ, issuer 2.0.0_SA_COO~B1) -- the s12 arm's row_id shape

Row `LGIC_ENFORCE-D1-W2-S153` (BLOCKING): the `s12` arm required `row_id` to match `LGIC_ENFORCE-[A-Z0-9]+-S\d+$`, which no
worker row id (`LGIC_ENFORCE-D1-W<n>-S<k>`, the id this order itself requires) can match. The defect is the issuer's check, not
the cell. Ruled: the arm now reads `LGIC_ENFORCE-(?:[A-Z0-9]+-)+S\d+$` AND requires that id to be a row in the channel. The
criterion, its invocation and its expectation are unchanged. Re-run by the issuer before the commit: the worker's committed record
(e572a18bce) PASSES the amended arm; the pre-amendment arm FAILS it; the base still FAILS (record absent). Gate limb that grades
this modification: none (to-pipeline-gate grades a NEWLY-ADDED order; this order declares `<placeholders>NONE</placeholders>`).
