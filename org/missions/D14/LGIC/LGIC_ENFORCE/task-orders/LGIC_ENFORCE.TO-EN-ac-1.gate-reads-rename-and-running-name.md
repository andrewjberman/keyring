# TO LGIC_ENFORCE.TO-EN-ac-1 -- round 23 EN-ac-1: the commit gate grades a rename against its source and reads a running name as EXISTING (FWD-8)
<to_id>LGIC_ENFORCE.TO-EN-ac-1</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~L1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>~L1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `EN-ac-1` (`decompositions/LGIC_ENFORCE_DECOMP.md` section 0x) | **outcome_ref:** FWD-8 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**The defect, read at HEAD.** `.tools/naming-gate.py` `judge()` sets `new = pre_text is None or not _in_pre(lit, pre_text)`: a literal
is NEW unless the graded file's OWN pre-image carries it. Two shapes that mint no name are therefore graded NEW and refused:

- (a) A RENAME. `safe-commit.sh` makes the diff with `git diff --cached --no-color --no-ext-diff -- <staged paths>`, so the source's
  deletion is outside the pathspec and an R100 rename reads as an added file (`--- /dev/null`) with no pre-image.
- (b) An ADOPTION. A Terraform import declares a resource that is already running. Its name is new text by construction.

Both are refused on two limbs: the placement row (`NEW and OUT-OF-PATTERN as <TYPE>`) and the firm-carrier clause (`hand-kept carrier of
'bd' ...`, which the audited placement override does not reach). `_carried_at_head()` is consulted only under RAISE and counts only
`GRADED_EXT` files, so it covers neither shape.

**The ruling (PRD v1.4, `org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md` lines 85-118; read them first).** The gate gains two
limbs and BOTH feed `new` before every branch that refuses, the carrier branch included:

1. A renamed file is graded against its SOURCE's HEAD bytes as the pre-image.
2. A literal whose EXACT name the census LIVE plane holds is EXISTING. The verdict text prints the plane's vintage and the node type it
   matched. A live read that fails, or that cannot print its vintage, leaves `new` exactly as it is today, so a failure stays
   distinguishable from a genuine negative (fail closed to the present behaviour).

EXISTING never means CONFORMANT: the name still reads OUT-OF-PATTERN or carrier WARN, and no registry row, R20 entry or name is minted.

**What exists to reuse (read, do not rewrite).**

- The live plane: `lib/opal_naming.py` `census_live(budget=600)` returns `(nodes, vintage, command)`, nodes being dicts of `type`,
  `name`, `arn`; it raises `CensusError` on a pull that did not scan every node type or printed no vintage or denominator. The gate
  already loads that module as `nm.mod` / `load_opal()`. Write no second reader.
- Rename detection: the whole-index status, `git diff --cached -M --name-status` run through `git_in(_diff_repo(), ...)` (NOT with the
  staged pathspec), gives `R<score>\t<source>\t<dest>` for a staged dest. The source's pre-image is `git show HEAD:<source>` (the
  existing code at `grade_file` already reads a HEAD pre-image this way for `f["old"]`).
- The seams: `grade_file()` reads `pre_text` from `f["old"]`; `judge(nm, path, lit, pre_text, waivers)` computes `new`;
  `_note_file`, `_note_place` and `grade_built()` also read `pre_text`, so the rename's source bytes must be THE `pre_text` the whole
  function sees, not a patch inside `judge()` alone. `self_test()` ends with the arms `built_self_test`, `pattern_self_test`,
  `place_self_test`, `override_self_test`.

**Client-data bound (0.0.0_AB_MSTR msgs 2712, 2739, 2758, 2796).** Search ONLY inside paths you name (`.tools/`, `lib/`, `infra/logic/`,
`org/missions/D14/LGIC/`), never the whole repo and never in history. Never open, search, copy or git show anything under
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/`, any `org/**/W73_S*_EVIDENCE.json`, or any cottonwood manifest.

### THE CELL

`EN-ac-1`. Build, in `.tools/naming-gate.py` only:

1. **Limb (a).** In `grade_file()`, when `f["old"] is None` and the path is a staged RENAME destination (whole-index
   `-M --name-status` reads `R<score> <source> <dest>`), set `pre_text` to `git show HEAD:<source>`. A failed git call, a source
   with no HEAD bytes, or a status that is not a rename leaves `pre_text` None exactly as today. A copy (the source still exists and
   no `R` row names the dest) is NOT a rename and stays NEW.
2. **Limb (b).** In `judge()`, compute `new` as today, then, ONLY when `new` is true and the literal would otherwise reach a refusing
   branch (it classifies to a type or is a hand-kept carrier), look its exact name up in the census LIVE plane. The read is LAZY (never
   on a commit with no such literal), ONCE per run (cache the nodes, the vintage and a failure), with `census_live(budget=300)`. A
   name held by a node sets `new = False` and appends to the row's why text, on ONE line:
   `RUNNING-LIVE <NODE_TYPE> 'name' read from the live plane, <vintage as printed>: EXISTING, not minted by this diff`.
   The verdict and counts then follow the existing EXISTING branches (WARN), never PASS-as-CONFORMANT.
3. **Fail closed.** Any exception from the live read (`CensusError`, `OSError`, a timeout, anything), or a vintage that is empty or
   reads UNREAD, leaves `new` true and appends `LIVE-READ-FAILED: <reason, first 120 characters>` to the REFUSE row's why text on one
   line. The verdict is the one printed today; nothing else changes.
4. **Two `--self-test` arms**, called from `self_test()`, no network (inject the live plane through a module-level function the arm
   replaces and restores): a RENAME arm and an ADOPT arm. Each prints `SELF-TEST <label> ...: ok` or `...: FAIL`, the labels containing
   the words `rename` and `adopt` respectively; the run still ends `NAMING-GATE-SELF-TEST: PASS` and exits 0 only when every arm
   holds. Existing arms are untouched.
5. `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/gate-rename-and-running-name.r23.result.md`: the four
   criteria's output whole, and the `--self-test` output whole.

The negative arm is FWD-8's, not yours to relax: a name running nowhere and written nowhere in the stored code is refused exactly as
today (the check proves it). `grade()`, the registry, `lib/opal_naming.py` and `safe-commit.sh` are not changed.

### ACCEPTANCE

<criterion id="AC1R23-AC1" cell_refs="EN-ac-1"><invocation>timeout 1500 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~L1/fixed_inputs/r23/check_en_r23.py rename</invocation><expect>PASS-R23-RENAME</expect></criterion>
`AC1R23-AC1` -- a staged rename of a file holding an OUT-OF-PATTERN firm-spelled name goes through the practice copy's real save check
with no REFUSE and at least one literal graded; the same bytes staged as a COPY are refused (the arm's difference control).

<criterion id="AC1R23-AC2" cell_refs="EN-ac-1"><invocation>timeout 1500 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~L1/fixed_inputs/r23/check_en_r23.py adopt</invocation><expect>PASS-R23-ADOPT</expect></criterion>
`AC1R23-AC2` -- a declaration of a name the live plane holds (picked at run time, OUT-OF-PATTERN, firm spelling `bd`) is admitted with
`RUNNING-LIVE`, the node type and the vintage date in its why text and no `LIVE-READ-FAILED`; a name running nowhere is refused as
`NEW and ...` exactly as today (the arm's difference control).

<criterion id="AC1R23-AC3" cell_refs="EN-ac-1"><invocation>timeout 1500 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~L1/fixed_inputs/r23/check_en_r23.py closed</invocation><expect>PASS-R23-CLOSED</expect></criterion>
`AC1R23-AC3` -- the AC2 declaration with the live read unreadable (the practice copy's `comp-find` exits 3) and again with a read that
prints no vintage is REFUSED, the why text carries `LIVE-READ-FAILED` and never `RUNNING-LIVE`.

<criterion id="AC1R23-AC4" cell_refs="EN-ac-1"><invocation>timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~L1/fixed_inputs/r23/check_en_r23.py selftest</invocation><expect>PASS-R23-SELFTEST</expect></criterion>
`AC1R23-AC4` -- `python .tools/naming-gate.py --self-test` prints a rename arm and an adopt arm, each `ok`, and ends PASS. A FOURTH
criterion, on the PRD's own wording (cell candidate E14 names "the two --self-test arms" as part of the cell): it cannot ride on AC1 to AC3
without making one of them compound.

<expected_criteria>AC1R23-AC1,AC1R23-AC2,AC1R23-AC3,AC1R23-AC4</expected_criteria>

Run every invocation from the root of your worktree. Each invocation's LAST printed line is the line the expectation is matched
against. Commit your artifacts first, then run the criteria against the committed bytes (the check builds its practice copy from your
committed HEAD, so an uncommitted gate is never graded). AC2 and AC3 read the live plane through `comp-find --corpus aws`: each takes
one to several minutes; do not shorten the timeout.

## BOUNDS

- **Grant.** The paths block below plus this order's file. Nothing in this prose grants a path.
- **No edit outside the grant.** `grade()`, `lib/opal_naming.py`, `infra/logic/registry/`, `.tools/safe-commit.sh`,
  `.tools/naming-apply-gate.py`, `org/mcp/naming-gate.enforce`, `org/mcp/naming-place.enforce` and the check file are never edited. No
  AWS write. The commit limb only.
- **Language.** Python 3.9 syntax, ASCII only in the file and its output, no new dependency.
- **Standing bar (read-only).** `python .tools/naming-gate.py --self-test` must end PASS before and after, and
  `python -m pytest lib/tests/test_opal_naming_fourth_verdict.py -q -p no:cacheprovider` must not newly fail.
- **Refusal clause.** If a criterion cannot be met as written, stop on it, write the reason in your report and a surprise row (id
  `LGIC_ENFORCE-D1-W1-S<k>`, `<k>` one above the highest `D1-W1-S` id in the channel at your write time; `surfaced_at` =
  `date -u +%FT%TZ` at filing) in
  `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` by textual splice at the end, and never weaken
  the check or its expected value.

<paths>
.tools/naming-gate.py
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/gate-rename-and-running-name.r23.result.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-ac-1.gate-reads-rename-and-running-name.proof_of_spec.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-ac-1.gate-reads-rename-and-running-name.md
</paths>

The block is your WRITE grant. You read and never edit anything outside it.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.23, round-23 cell `EN-ac-1` (section 0x).
<owned_cells>EN-ac-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AC1R23-AC1, AC1R23-AC2, AC1R23-AC3, AC1R23-AC4. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-ac-1.gate-reads-rename-and-running-name.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AC1R23-AC1 AC1R23-AC2 AC1R23-AC3 AC1R23-AC4 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-ac-1.gate-reads-rename-and-running-name.md`
BEFORE the `complete` flip. Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.
</proof_of_spec>

**REPORT:** the four checks' last lines whole; the `--self-test` output; the lines of code added; your commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no grant; the gate only reads the live plane through comp-find.
comp-adversary: RUN -- the cheapest passes are (1) treat every NEW literal as EXISTING (the AC2 absent-name control refuses), (2) treat a failed
read as EXISTING (AC3), (3) match the running name by substring (AC2's absent name is a prefix-sharing non-running name of the same
firm spelling), (4) admit a copy as a rename (AC1's control), (5) print RUNNING-LIVE without reading (AC2 requires the node type and the
vintage date the check read independently through census_live). BLIND: the check proves one running name of two node types and one rename
shape (R100); an R<100 rename and a type mismatch between the literal's class and the node's are read at review, not graded by an arm.
lane: the <paths> block IS the grant (worker RULING 1); nothing in the prose grants a path.
</preflight>

Source: `org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md` v1.4 @5cef7ba9ce (FWD-8), the CTO's L4 notification msg 3399 and cell
candidate E14. Cross-box call `XB-20261010T225240Z-dcb5`; seated by `0.0.0_AB_MSTR~DELL1` msg 3392. Base dry-run at the cut, by the
issuer, 2026-10-11 ~03:2xZ at HEAD a1e7e1cc38: AC1R23-AC1 base: FAIL as expected (the rename's name `bd-zz-r23-probe-role` REFUSED);
AC1R23-AC2 base: FAIL as expected (the running name `bd-49f-auto-login` REFUSED as `NEW and OUT-OF-PATTERN as IAM_POLICY`);
AC1R23-AC3 base: FAIL as expected (REFUSED without `LIVE-READ-FAILED`); AC1R23-AC4 base: FAIL as expected (no rename or adopt arm among 32
arms).
