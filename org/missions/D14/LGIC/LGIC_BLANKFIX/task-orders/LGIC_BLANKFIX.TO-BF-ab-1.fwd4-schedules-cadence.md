# TO LGIC_BLANKFIX.TO-BF-ab-1 -- round 13 BF-ab-1: FWD-4 group C: every schedule's listed new name carries a cadence word its own expression decides; one schedule renamed from the list alone

<to_id>LGIC_BLANKFIX.TO-BF-ab-1</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>13</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `BF-ab-1` (`decompositions/LGIC_BLANKFIX_DECOMP.round13.md`) | **outcome_ref:** FWD-4 |
**depends_on:** none (slot ~1)

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --all-roots` (the same as `python lib/opal_naming_rootcheck.py all
--map infra/logic/registry/root_map.json`) runs every Terraform root the root map covers and prints the denominator of roots
first; `infra/logic/README.md` "Run the naming check" explains its lines and fields. At this cut, on the base your worktree is
made from, it reads: `ALL-ROOTS ok=True roots_total=86 mapped=86 unmapped=0 completed=86 stopped=0 items=2599 right=670 fix=1636 not_asked=268 pattern=25 carded=0 refused=0 hole=0 carded_class_holes=0 source_bucket_holes=0 event_rule_holes=0 unknown_word_holes=0 other_holes=0 stale_hints=0 uncounted=1 counted_at_caller=17`. The round-12 close is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ALL_ROOTS_round12.txt`. The CTO's coverage read of round 12 is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round12.md` -- read it first:
FWD-4 and FWD-8 were never served, and this round serves them. The PRD is
`org/missions/D14/LGIC/LGIC_BLANKFIX/prd/LGIC_BLANKFIX_PRD.md` (FWD-4 and FWD-8 DONE WHEN and ACCEPT, lines 51-90; C-CADENCE line 118). The round-12 drain end is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ROUND12_DRAIN_END.md`.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`, the `census` command), `opal_naming_scope.py` (the roots, their
names, `root_items`, the UNCOUNTED reader and `UNCOUNTED_REASONS`), `opal_naming_rootmap.py`, `opal_naming_cadence.py`,
`opal_naming_keyfill.py`, `opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `place`, `check_root`, `_ruling_of`,
`all_roots`, `HOLE_OWED`, the `lines`, `keys` and `all` commands). The gates: `.tools/naming-gate.py` (commit time),
`.tools/naming-apply-gate.py` (plan time), called by `.tools/safe-commit.sh` and `.tools/safe-apply.sh`. The registry is
`infra/logic/registry/`; only `4.0.0_SA_CRO` writes it. Read the modules your cell touches or calls before you build. Import with
`sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new dependency; no AWS call and no network
call. The bar: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at the base (193 passed, 1 skipped), and every
`lib/tests/test_opal_naming_*.py` script prints `ok=True` at the base. None may newly fail after your build. A test you write
asserts relations and the rows it needs by name, never a typed total of repository names, roots or registry rows: those move
every day, and the registry's lane may add rows during this round. **The switch file `org/mcp/naming-place.enforce` is PRESENT since
@4d2bfc6dfd:** the placement refusal is live on every commit and apply. No cell deletes, moves or edits it; exercise the gates
only in a temporary copy, and never write a real override audit row.

### THE CELL

`BF-ab-1`. FWD-4 (PRD): "the list gives a schedule's new name with how often it runs filled in ... a person who reads the
schedule itself agrees with the word the list chose"; DONE WHEN "one schedule ... renamed from the list alone". C-CADENCE: "a row the
expression cannot decide is listed, not guessed". Per root, `python lib/opal_naming_rootcheck.py --map infra/logic/registry/root_map.json <root>` prints one line per name; a schedule prints as
`FIX EVENT_RULE <current> -> <new name with cadence word>  [file:line]` (e.g. `bd-49f-keepalive-sched -> blackdiamond-49f-keepalive-sched-15min`,
`infra/aws/terraform/bd-pipeline/bd-49f-interim.tf:148`), and RIGHT when already conforming. `lib/opal_naming_cadence.py` reads a
schedule's expression.

**Build:**
1. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_fwd4_cadence.py`: over every mapped root, every schedule-kind line (EVENT_RULE and any scheduler/schedule type the
   lines print) is read; for each, the cadence word in the listed name is compared with the word `opal_naming_cadence` decides from that
   schedule's own `schedule_expression` read at the line's file. Rows the expression cannot decide are LISTED (never guessed); a word
   that disagrees with its expression is a MISMATCH. It prints one line per disagreement or undecided row, then last:
   `FWD4-CADENCE ok=True schedules=N agree=N undecided=N mismatch=0`; `ok=True` when `mismatch=0` and every schedule is agree or
   listed undecided. If the read finds a mismatch caused by the cadence reader, fix it in `lib/opal_naming_cadence.py` with a test case.
2. The EXERCISE, "renamed from the list alone": `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/exercise_fwd4_rename.py` takes ONE schedule's list line and nothing else, writes
   the rename into a temporary copy of its `.tf` file (never the repository), and runs the real `.tools/naming-gate.py --diff` on that
   copy's diff: the renamed name grades CONFORMANT and the placement step does not refuse it. It prints the list line it used, the diff,
   and last: `FWD4-RENAME ok=True name=<new> grade=CONFORMANT`. No apply, no AWS: a live rename of a schedule is a deploy with its own
   pair and is not this cell's act.

### ACCEPTANCE

<criterion id="BAB1-AC1" cell_refs="BF-ab-1"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_fwd4_cadence.py</invocation><expect>FWD4-CADENCE ok=True</expect></criterion>
`BAB1-AC1` -- every listed schedule's cadence word agrees with its own expression, or is listed as undecided.

<criterion id="BAB1-AC2" cell_refs="BF-ab-1"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/exercise_fwd4_rename.py</invocation><expect>FWD4-RENAME ok=True</expect></criterion>
`BAB1-AC2` -- one schedule renamed from its list line alone grades CONFORMANT on the real gate.

<criterion id="BAB1-AC3" cell_refs="BF-ab-1" judgment="true"/>
`BAB1-AC3` (judgment) -- 3.0.0_SA_CVO reads three schedules the checker printed (one per cadence word kind if there are several) against their own expressions: does a person reading the schedule agree with the word the list chose? You record the paths and NO verdict.

<expected_criteria>BAB1-AC1,BAB1-AC2,BAB1-AC3</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource;
  `org/mcp/naming-place.enforce` is never deleted or edited.
- The judgment criterion gets its artifact paths and NO verdict from you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-D1-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; a row filed on dell1 carries the `-D1-` coordinate
  or the row gate refuses it) in the investigation file, and do not weaken the test or the expected value. A fact in this order that
  the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_cadence.py
lib/tests/test_opal_naming_cadence.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under
`infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round12.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round13.md`, and the `lib/` modules and `.tools/` scripts your block does
not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round13.md</decomp_doc> (round 13), cell `BF-ab-1`.
<owned_cells>BF-ab-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BAB1-AC1, BAB1-AC2, BAB1-AC3 (BAB1-AC3 judgment: recorded UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming `3.0.0_SA_CVO`). Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-ab-1.fwd4-schedules-cadence.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BAB1-AC1,BAB1-AC2,BAB1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last lines whole; schedules, agree, undecided, mismatch; the one schedule renamed and its grade; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a cadence word guessed where the expression is silent (undecided rows are listed, the checker asserts it); a rename exercised in the repository or applied (temporary copy only, no AWS); BLIND: schedules whose expression is set at run time.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round12.md @b45108c324 (`1.0.0_SA_CTO~DELL1`, msg 2324), item item 1 (FWD-4 group C); decomposition round 13. Base dry-run at the cut, by the
issuer at base b89f2f09c4: BAB1-AC1 base: FAIL as expected (file absent); BAB1-AC2 base: FAIL as expected (file absent).
