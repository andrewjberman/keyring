# TO LGIC_BLANKFIX.TO-BF-w-1 -- round 8 BF-w-1: FWD-6 built -- the creation-time refusal as designed: place() extracted, called by the commit and apply gates under its own switch, arms A to G exercised

<to_id>LGIC_BLANKFIX.TO-BF-w-1</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete -- proof-of-spec VALID (rc=0)</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-w-1` (`decompositions/LGIC_BLANKFIX_DECOMP.round8.md`) | **outcome_ref:** FWD-6 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --all-roots` (the same as `python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json`)
runs every Terraform root the root map covers and prints the denominator of roots first; `infra/logic/README.md` "Run the naming
check" explains its lines and fields. At the round-7 close it read `roots_total=87 mapped=63 unmapped=24 completed=63 stopped=0
items=1598 ... hole=285 carded_class_holes=205 source_bucket_holes=14 event_rule_holes=7 unknown_word_holes=0 other_holes=59
stale_hints=0 uncounted=301`; the whole output is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/ALL_ROOTS_round7.txt`. The CTO's reading of round 7 is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round7.md` -- read
it first. Its ruling for FWD-2: no ceiling short of the full list; order (1) uncounted to 0, (2) holes by root, largest first, (3)
the held map entries; every round reports `hole` and `uncounted` before and after, with their denominators.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`, the `census` command), `opal_naming_scope.py` (the roots, their
names, `root_items`, the UNCOUNTED reader), `opal_naming_rootmap.py`, `opal_naming_cadence.py`, `opal_naming_keyfill.py`,
`opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `check_root`, `_ruling_of`, the `lines`, `keys` and `all`
commands). The registry is `infra/logic/registry/`; only `4.0.0_SA_CRO` writes it. Read the modules your cell touches or calls before
you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new dependency; no AWS
call and no network call. The bar: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at the base (194 passed), and
every `lib/tests/test_opal_naming_*.py` script prints `ok=True` at the base. None may newly fail after your build. A test you write
asserts relations and the rows it needs by name, never a typed total of repository names, roots or registry rows: those move every
day, and the registry's lane may add rows during this round.

### THE CELL

`BF-w-1` (item E1). The design `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/FWD6_DESIGN_round6.md` was accepted at round 7's L9 (`org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND7_L9_GRADE_BV2_BV3_20261008.md`: BV3-AC2 MET; 18 of 18 HOLE
texts owned; arms C and D re-run). Read it whole -- its decision rule, its owner table, its mode and its exercise arms A to G -- and
the CRO's patterns file it answers (`org/tier1_exec/4.0.0_SA_CRO/deliverables/PRE_WRITE_REFUSAL_PATTERNS_20261008.md`). Build it as written; where the code contradicts the design, file one
row and follow the code.

**Build:**
1. `place()` in `lib/opal_naming_rootcheck.py`: the root check's own per-item decision extracted, not re-written; `decide()` and
   `check_root()` call it, so every existing output is unchanged (the issuer re-runs the repeat check and the `all` command against
   the base at the drain). Each HOLE text carries its owner from the design's table.
2. `.tools/naming-gate.py` (commit time) and `.tools/naming-apply-gate.py` (plan time) call `place()` for each NEW stored name per
   the design's decision rule and its live hole ratchet. The mode is the design's own switch file, `org/mcp/naming-place.enforce`:
   present -> the gate refuses with the design's text (what is owed and to whom); absent -> it prints the same text and the gate's
   verdict is unchanged. **The switch file is not created in this round.** It lands absent: turning it on changes every seat's
   commits, which is not this cell's act. A test seam, if the gate needs one, may only turn the refusal ON, never off (the patterns
   file's lesson on environment downgrades).
3. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/exercise_fwd6_arms.py`: it runs arms A to G as the design states them against the real gate scripts, on
   hand-built diffs and copies in a temporary folder, with the switch present or absent as each arm needs, and never leaves a switch
   file or a temporary file in the repository. It prints one line per arm (expected, got) and last:
   `FWD6-ARMS ok=True arms=7 held=7`. Extend the gates' own `--self-test` with the new step's arms.

### ACCEPTANCE

<criterion id="BW1-AC1" cell_refs="BF-w-1"><invocation>python lib/tests/test_opal_naming_rootcheck.py</invocation><expect>ROOTCHECK-TEST ok=True</expect></criterion>
`BW1-AC1` -- place() is the root check's decision and the root check still passes.

<criterion id="BW1-AC2" cell_refs="BF-w-1"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/exercise_fwd6_arms.py</invocation><expect>FWD6-ARMS ok=True</expect></criterion>
`BW1-AC2` -- arms A to G each give the design's expected result on the real gates.

<criterion id="BW1-AC3" cell_refs="BF-w-1"><invocation>python .tools/naming-gate.py --self-test</invocation><expect>NAMING-GATE-SELF-TEST: PASS</expect></criterion>
`BW1-AC3` -- the commit gate's own self-test passes with the new step's arms.

<criterion id="BW1-AC4" cell_refs="BF-w-1" judgment="true"/>
`BW1-AC4` (judgment) -- `3.0.0_SA_CVO` reads the build and the arms' record against FWD-6's DONE WHEN (PRD lines 67-73): has a deliberately unplaceable name been tried and stopped, and a placeable one let through, and is the person told what they owe? You record the artifacts' paths and NO verdict.

<expected_criteria>BW1-AC1,BW1-AC2,BW1-AC3,BW1-AC4</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- The judgment criterion gets its artifact paths and NO verdict from you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_rootcheck.py
lib/tests/test_opal_naming_rootcheck.py
.tools/naming-gate.py
.tools/naming-apply-gate.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round7.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round8.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round8.md</decomp_doc> (round 8), cell `BF-w-1`.
<owned_cells>BF-w-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BW1-AC1, BW1-AC2, BW1-AC3, BW1-AC4 (judgment: recorded UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming `3.0.0_SA_CVO`). Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-w-1.fwd6-build.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BW1-AC1,BW1-AC2,BW1-AC3,BW1-AC4` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three last lines whole; each arm's expected and got; the switch file's state at your last commit (absent); the diff stat of both gates; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a second decision written beside the root check's (place() is extracted; existing outputs are unchanged); a refusal that is on without its switch (arm G); a seam that can turn the refusal off; a switch or temp file left in the repository (the exercise cleans up and the issuer checks); BLIND: commit-time cost across many roots -- named, not measured, unless you measure it.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round7.md @ec6f56562b (the CTO's enrichment list E1 to E5); decomposition round 8. Base dry-run at the cut: BW1-AC1 base PASS as expected (ran: ROOTCHECK-TEST ok=True cases=213; extended by the cell); BW1-AC2 base FAIL as expected (file absent); BW1-AC3 base PASS as expected (ran: NAMING-GATE-SELF-TEST: PASS; extended by the cell).
