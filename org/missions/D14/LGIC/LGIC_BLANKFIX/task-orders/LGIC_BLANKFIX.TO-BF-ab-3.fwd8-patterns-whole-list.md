# TO LGIC_BLANKFIX.TO-BF-ab-3 -- round 13 BF-ab-3: FWD-8: the whole list read, every code pattern shown as a pattern; a pattern shown as a name fails the read

<to_id>LGIC_BLANKFIX.TO-BF-ab-3</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>13</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `BF-ab-3` (`decompositions/LGIC_BLANKFIX_DECOMP.round13.md`) | **outcome_ref:** FWD-8 |
**depends_on:** BF-ab-2 (same slot, same file)

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

`BF-ab-3`. FWD-8 (PRD): "a pattern with a blank meant to be filled in later is shown as a pattern, never as a broken name and
never as a correct one; a reader going through the full list finds none presented either way"; DONE WHEN "the whole list read, and every
pattern in it found shown as a pattern". The PRD's backlog names "the fifteen pattern rows"; the round-12 census reads pattern=25 over
86 roots (`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ALL_ROOTS_round12.txt`). A pattern prints as `PATTERN <type> <current> -> a code pattern, not a name; variable '<v>'  [file:line]`.

**Build:**
1. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_fwd8_patterns.py`: over every mapped root's lines (`python lib/opal_naming_rootcheck.py --map infra/logic/registry/root_map.json <root>`, or `check_root` imported), every item
   whose CURRENT value carries a code pattern (a `%s`/`%d`-style placeholder, a `{name}` or `${name}` blank, an f-string field) is
   found, and the check asserts each prints as PATTERN -- none as FIX, RIGHT, HOLE or NOT-ASKED. It prints one line per violation, then
   last: `FWD8-PATTERNS ok=True roots=N items=N patterns=N shown_as_pattern=N shown_as_name=0`. The NEGATIVE ARM, inside the check: a
   planted pattern item presented as a FIX line is caught (the run counts it as shown_as_name and would fail).
2. If the read finds a real pattern shown as a name, fix the decision in `lib/opal_naming_rootcheck.py` with a test case.

### ACCEPTANCE

<criterion id="BAB3-AC1" cell_refs="BF-ab-3"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_fwd8_patterns.py</invocation><expect>FWD8-PATTERNS ok=True</expect></criterion>
`BAB3-AC1` -- the whole list read: every code pattern is shown as a pattern; a pattern shown as a name fails the read.

<criterion id="BAB3-AC2" cell_refs="BF-ab-3"><invocation>python lib/tests/test_opal_naming_rootcheck.py</invocation><expect>ROOTCHECK-TEST ok=True</expect></criterion>
`BAB3-AC2` -- the root check's test holds.

<expected_criteria>BAB3-AC1,BAB3-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource;
  `org/mcp/naming-place.enforce` is never deleted or edited.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-D1-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; a row filed on dell1 carries the `-D1-` coordinate
  or the row gate refuses it) in the investigation file, and do not weaken the test or the expected value. A fact in this order that
  the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_rootcheck.py
lib/tests/test_opal_naming_rootcheck.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under
`infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round12.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round13.md`, and the `lib/` modules and `.tools/` scripts your block does
not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round13.md</decomp_doc> (round 13), cell `BF-ab-3`.
<owned_cells>BF-ab-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BAB3-AC1, BAB3-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-ab-3.fwd8-patterns-whole-list.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BAB3-AC1,BAB3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last lines whole; patterns found per root; any fix made; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a pattern detector so narrow it finds nothing (the checker prints the denominator of items and patterns, and the negative arm proves it can fail); a pattern counted as a name or a name as a pattern; BLIND: patterns assembled at run time that never appear literally.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round12.md @b45108c324 (`1.0.0_SA_CTO~DELL1`, msg 2324), item item 3 (FWD-8); decomposition round 13. Base dry-run at the cut, by the
issuer at base b89f2f09c4: BAB3-AC1 base: FAIL as expected (file absent); BAB3-AC2 base: PASS as expected (ROOTCHECK-TEST ok=True).
