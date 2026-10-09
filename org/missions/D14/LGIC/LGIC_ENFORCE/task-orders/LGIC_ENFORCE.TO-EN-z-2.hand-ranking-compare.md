# TO LGIC_ENFORCE.TO-EN-z-2 -- round 20 EN-z-2: FWD-5 item 2: the r20 run's totals set beside the naming work's hand ranking, each difference explained
<to_id>LGIC_ENFORCE.TO-EN-z-2</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `EN-z-2` (`decompositions/LGIC_ENFORCE_DECOMP.md` section 0u) | **outcome_ref:** FWD-5 |
**depends_on:** EN-z-1 (same slot; reads its report)

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

`EN-z-2` (FWD-5 clause 3: "the totals agree with the ranking the naming work produced by hand"). The hand ranking is THREE
surfaces, and round 19 re-measured all three at the round-8 census vintage
(`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/HAND_REMEASURE_R19.json`: `grading_rule_worked_cases` 45/45/0, `n6_grader_rows` 88/86/2, `tension_ranking_surfaces` 10/9/1,
totals 143/140/3). The comparison now runs against THIS round's census, `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NAMING_CENSUS_REPORT.r20.md` (EN-z-1's output).

**Build:**
1. `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/build_hand_compare_r20.py`: for every compared key of each of the three surfaces (the SAME key sets as round 19's record),
   the hand verdict (from the round-19 REMEASURED siblings named in that record) against the machine verdict of the r20 run (its
   row for that name; where the r20 run has no row for the name, `grade()` on it, and the record says which).
2. `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/HAND_COMPARE_R20.json`: `census_report` (the r20 report's repo-relative path), `surfaces{key}` -> `compared`, `agree`,
   `disagree`, `compared_keys`, `differences[]` (`key`, `name`, `hand_verdict`, `machine_verdict`, `explanation`), and `totals`.
   Every difference carries an explanation: which side is wrong and why, read at the bytes; or that the estate moved between the
   two readings, naming what moved.
3. `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/hand-compare.r20.result.md`: the totals of the r20 run beside the hand totals, and every difference with its explanation.
Do not re-grade the hand side and do not edit the round-19 siblings or the LGIC_NAMING originals.

### ACCEPTANCE

<criterion id="Z2R20-AC1" cell_refs="EN-z-2"><invocation>python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r20/check_en_r20.py compare</invocation><expect>PASS-R20-COMPARE</expect></criterion>
`Z2R20-AC1` -- all three surfaces, round 19's key sets exactly, counts adding up, one explained difference per disagreement, machine verdicts read from the r20 run.

<criterion id="Z2R20-AC2" cell_refs="EN-z-2" judgment="true"/>
`Z2R20-AC2` -- whether each explanation is right at the bytes, across all three surfaces (for `3.0.0_SA_CVO` at L9).

<expected_criteria>Z2R20-AC1, Z2R20-AC2</expected_criteria>

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
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/build_hand_compare_r20.py
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/HAND_COMPARE_R20.json
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/hand-compare.r20.result.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-z-2.hand-ranking-compare.proof_of_spec.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-z-2.hand-ranking-compare.md
</paths>

The block is your WRITE grant. You read and never edit anything outside it.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.20, round-20 cell `EN-z-2` (section 0u).
<owned_cells>EN-z-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Z2R20-AC1, Z2R20-AC2. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-z-2.hand-ranking-compare.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Z2R20-AC1,Z2R20-AC2 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-z-2.hand-ranking-compare.md` BEFORE the
`complete` flip. Commit the artifact first, then pin it; never PENDING-THIS-COMMIT. Z2R20-AC2 is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; no verdict.
</proof_of_spec>

**REPORT:** compared, agree and disagree per surface and in total; each difference with its explanation; the last line of every criterion whole; your commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no grant, no AWS call.
comp-adversary: RUN -- comparing only the largest surface (10 or 88 of 143): the check holds the three key sets to round 19's by set equality. Copying round 19's verdicts forward: machine verdicts must equal the r20 run's rows. A difference waved through: each needs an explanation. BLIND: whether an explanation is TRUE is not mechanical; that is Z2R20-AC2, judgment, for the CVO.
lane: the <paths> block IS the grant (worker RULING 1); nothing in the prose grants a path.
</preflight>

Source: `org/missions/D14/LGIC/LGIC_ENFORCE/ledger/FWD5_GRADE_FROM_BLANKFIX_FWD9_20261008.md` re-grade 2026-10-09 ~15:2xZ (`1.0.0_SA_CTO~DELL1`, msg 2639), round-20 list; decomposition section 0u. Base dry-run at
the cut, by the issuer at base 133bf5f7a4: Z2R20-AC1 base: FAIL as expected (HAND_COMPARE_R20.json absent).
