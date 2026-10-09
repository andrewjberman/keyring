# TO LGIC_BLANKFIX.TO-BF-w-2 -- round 8 BF-w-2: uncounted to 0 -- names built in locals, modules, variables and other resources resolved from the repository, the rest named with why it cannot be

<to_id>LGIC_BLANKFIX.TO-BF-w-2</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~4</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-w-2` (`decompositions/LGIC_BLANKFIX_DECOMP.round8.md`) | **outcome_ref:** FWD-2 |
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

`BF-w-2` (item E2; first in the CTO's FWD-2 order). Round 7's `BF-v-4` made the census print a name it cannot read as
`UNCOUNTED <type> <attribute> = <expression> -- <reason>` (reasons `local`, `var`, `module`, `json`, `interpolation`); the trunk reads
`uncounted=301` (module 214, local 41, var 25, interpolation 21). The CTO: "a name the census cannot count cannot be judged, so 301
uncounted names are the floor of the problem" -- uncounted to 0 first, or each named with a reason.

**Build** in `lib/opal_naming_scope.py` (and its test) only:
1. Resolve from the repository wherever it decides the value: a `module` call to a module in this repository (follow its `source`
   path) whose name is built from an input variable -> the caller's argument, when that is a literal or itself resolves; a `var.`
   with a literal `default` or a value in the root's own `*.tfvars` / `*.auto.tfvars(.json)`; a chain of `local` values; an
   interpolation that names another resource of the root whose name attribute is a literal (`aws_s3_bucket.x.id` -> that bucket's
   name). A resolved name becomes an ordinary item, `where` at the line that gives the literal, graded like any other.
2. What the repository cannot decide stays UNCOUNTED, its reason one of a closed set you write down in the module with one line each
   (for example: set only at apply time, computed by AWS, a module outside this repository, a `count`/`for_each` key with no literal
   domain). No residual line keeps a bare `module` / `local` / `var` / `interpolation` reason.
3. The DIFFERENCE CONTROL in the test, on `.tf` text it writes to a temporary folder: a module call with a literal argument resolves;
   a var with a default resolves; a local chain resolves; a reference to another resource's literal name resolves; an apply-time value
   stays UNCOUNTED with its reason.
4. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/check_uncounted_delta.py`: it reads the `ALL-ROOTS` last line of `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/ALL_ROOTS_round7.txt` (the before), runs the
   `all` command once (the after), counts the residual UNCOUNTED lines by reason, and prints, last:
   `UNCOUNTED-DELTA ok=True before=N after=N hole_before=N hole_after=N mapped=N residual_reasons=N bare_reasons=0`; `ok=True` when
   `after < before`, no residual line carries a bare reason, and the live run prints `ok=True`.

### ACCEPTANCE

<criterion id="BW2-AC1" cell_refs="BF-w-2"><invocation>python lib/tests/test_opal_naming_scope.py</invocation><expect>SCOPE-TEST ok=True</expect></criterion>
`BW2-AC1` -- the difference control: module, var, local, reference resolve; an apply-time value stays with its reason.

<criterion id="BW2-AC2" cell_refs="BF-w-2"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/check_uncounted_delta.py</invocation><expect>UNCOUNTED-DELTA ok=True</expect></criterion>
`BW2-AC2` -- uncounted falls, and what remains says why the repository cannot decide it.

<expected_criteria>BW2-AC1,BW2-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_scope.py
lib/tests/test_opal_naming_scope.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round7.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round8.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round8.md</decomp_doc> (round 8), cell `BF-w-2`.
<owned_cells>BF-w-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BW2-AC1, BW2-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/LGIC_BLANKFIX.TO-BF-w-2.uncounted-to-zero.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BW2-AC1,BW2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; uncounted before and after by reason; hole before and after (newly counted names are graded, so it may rise); every root whose count moved; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a name counted from a guess (a resolved name's where is the line that gives the literal); a residual hidden by a vague reason (bare reasons are counted and must be 0); holes rising silently (hole before and after are printed); BLIND: names whose literal lives only in AWS.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round7.md @ec6f56562b (the CTO's enrichment list E1 to E5); decomposition round 8. Base dry-run at the cut: BW2-AC1 base PASS as expected (ran: SCOPE-TEST ok=True assertions=728; extended by the cell); BW2-AC2 base FAIL as expected (file absent; the trunk reads uncounted=301).
