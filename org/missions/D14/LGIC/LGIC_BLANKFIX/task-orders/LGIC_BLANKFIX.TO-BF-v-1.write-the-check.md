# TO LGIC_BLANKFIX.TO-BF-v-1 -- round 7 BF-v-1: the naming check written into the instructions -- census --all-roots, what its last line means, no --live on the newcomer path

<to_id>LGIC_BLANKFIX.TO-BF-v-1</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~4</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete -- proof-of-spec VALID (rc=0)</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-v-1` (`decompositions/LGIC_BLANKFIX_DECOMP.round7.md`) | **outcome_ref:** FWD-5 |
**depends_on:** BF-v-4 merged on this slot (its new field is explained here); handed by continuing the slot

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --all-roots` (the same as `python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json`)
runs every Terraform root the root map covers and prints the denominator of roots first. At the round-6 close it read
`roots_total=87 mapped=13 unmapped=74 completed=13 stopped=0 items=412 right=124 fix=248 not_asked=32 pattern=8 carded=0 refused=0
hole=0 ... stale_hints=0`; the whole output is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/ALL_ROOTS_round6.txt`. One line per name: `KIND type current -> detail  [where]`, kinds
`RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`. Each unmapped root is printed `UNMAPPED <root> names=N`. The
CTO's reading of round 6 is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round6.md`, on the CVO's grade `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND6_L9_GRADE_BU6_BU7_20261008.md` -- read the analysis first.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`, the `census` command), `opal_naming_scope.py` (the roots and their
names, `root_items`), `opal_naming_rootmap.py` (`load_map`, `resolve`), `opal_naming_cadence.py`, `opal_naming_keyfill.py`,
`opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `check_root`, `_ruling_of`, the `lines`, `keys` and `all`
commands). The registry is `infra/logic/registry/`; only `4.0.0_SA_CRO` writes it. Read the modules your cell touches or calls before
you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new dependency; no AWS
call and no network call. The bar: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at the base (194 passed), and
every `lib/tests/test_opal_naming_*.py` script prints `ok=True` at the base. None may newly fail after your build. A test you write
asserts relations and the rows it needs by name, never a typed total of repository names, roots or registry rows: those move every
day, and the registry's lane may add map entries during this round.

### THE CELL

`BF-v-1` (item E1). The CTO ruled (`org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round6.md`, "The one ruling the slug asks for"): FWD-5's check is
`python lib/opal_naming.py census --all-roots`, the only mode whose scope is every root and that runs to its totals. Round 6's
fresh seat could not find it: `infra/logic/README.md` names no command, and `infra/logic/10_ONBOARDING_CHECKLIST.md` STEP 13 (line
344) and the brief name commands carrying `--live`. "FWD-5 is met only when the written instructions name `census --all-roots` and
a fresh seat reaches its totals from them." A NEW seat runs it after your merge (`BF-v-2`), so write for a reader who has never
run it and has only the repository.

**Build** (documents and one checker):
1. `infra/logic/README.md`: a section headed `## Run the naming check` that names the command exactly, says it reads the
   repository only (no AWS, no skip list to write), how long it takes on this repository, and what its output means: the first
   line (the denominator of roots), each line kind (`ROOT`, `UNMAPPED`, `UNCOUNTED`, `STOPPED`, `STALE-HINT` and the per-name kinds),
   and EVERY field of the `ALL-ROOTS` last line, read from the code that prints it, not from this order. Say what `ok=True` does and
   does not mean (13 of 87 roots mapped at the round-6 close; the rest print names but are not graded).
2. `infra/logic/10_ONBOARDING_CHECKLIST.md` STEP 13: the first command a reader meets is `census --all-roots`; the `--live` command
   stays only as a separate, labelled step for a seat with AWS access. Change nothing else in the checklist.
3. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/check_instructions.py`: it checks both files contain the exact command, that the README section exists and
   carries no `--live`, that STEP 13's first fenced or backticked command is `census --all-roots`, and that every field name of the
   live `ALL-ROOTS` last line (run the command once) appears in the README section. Last line:
   `INSTRUCTIONS ok=True files=2 named=2 live_on_newcomer_path=0 fields=N unexplained=0`.

### ACCEPTANCE

<criterion id="BV1-AC1" cell_refs="BF-v-1"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/check_instructions.py</invocation><expect>INSTRUCTIONS ok=True</expect></criterion>
`BV1-AC1` -- the instructions name the check, keep --live off the newcomer path, and explain every field of the live last line.

<expected_criteria>BV1-AC1</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- `infra/logic/` is `4.0.0_SA_CRO`'s lane for the registry; your grant here is the two documents named in the block, nothing under `infra/logic/registry/`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
infra/logic/README.md
infra/logic/10_ONBOARDING_CHECKLIST.md
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round6.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round7.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round7.md</decomp_doc> (round 7), cell `BF-v-1`.
<owned_cells>BF-v-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BV1-AC1. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/LGIC_BLANKFIX.TO-BF-v-1.write-the-check.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BV1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; the README section as written; the STEP 13 diff; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a field list typed from this order instead of read from the live last line (the checker reads the live line); a command that works only with an AWS session (the README section carries no --live); a rewrite of steps the order did not name (STEP 13 only); BLIND: whether a newcomer understands it -- that is BF-v-2's judgment.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round6.md @ea45e82c70 (the CTO's enrichment list E1 to E5); decomposition round 7. Base dry-run at the cut: BV1-AC1 base FAIL as expected (file absent; README names the command 0 times, the checklist 0 times).
