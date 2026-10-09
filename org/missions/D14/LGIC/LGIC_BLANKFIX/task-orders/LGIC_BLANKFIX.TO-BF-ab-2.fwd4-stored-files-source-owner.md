# TO LGIC_BLANKFIX.TO-BF-ab-2 -- round 13 BF-ab-2: FWD-4 group D: every stored file's listed new location reads with its source and owner; one move read from the list alone

<to_id>LGIC_BLANKFIX.TO-BF-ab-2</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>13</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `BF-ab-2` (`decompositions/LGIC_BLANKFIX_DECOMP.round13.md`) | **outcome_ref:** FWD-4 |
**depends_on:** none (first on slot ~2)

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

`BF-ab-2`. FWD-4 (PRD): "the list gives ... a stored file's new location with where it came from and whose it is filled
in"; DONE WHEN "one ... stored file ... renamed from the list alone". A stored file prints as `FIX S3Key <current> -> <new location>
[file:line]` (e.g. `code/silver/convert_fees_to_silver.py -> blackdiamond/49financial/code/silver/convert_fees_to_silver.py`); the
line does not today state its source and owner in words -- they are only implied by the path's tokens.

**Build** in `lib/opal_naming_rootcheck.py` (its line output) and its test:
1. A `FIX S3Key` line (and `RIGHT S3Key`) states, after the new location, `source=<system> owner=<firm or system>` read from the same
   ruling or key class that produced the location (never inferred from the folder name); a key whose source or owner the rulings do not
   decide says `source=UNDECIDED` / `owner=UNDECIDED`, never a guess. Every other line kind and the ALL-ROOTS line are unchanged.
2. Cases in `lib/tests/test_opal_naming_rootcheck.py`: a key with a ruling prints its source and owner; the DIFFERENCE CONTROL, a key
   with no deciding row prints UNDECIDED.
3. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_fwd4_stored_files.py`: over every mapped root's lines, every stored-file line is read; it prints last:
   `FWD4-STORED ok=True files=N with_source_owner=N undecided=N`, `ok=True` when every line carries both fields; and it prints ONE
   file's move read from its list line alone (current key, new key, source, owner) with no rename applied (a live move is a data act
   with its own pair).

### ACCEPTANCE

<criterion id="BAB2-AC1" cell_refs="BF-ab-2"><invocation>python lib/tests/test_opal_naming_rootcheck.py</invocation><expect>ROOTCHECK-TEST ok=True</expect></criterion>
`BAB2-AC1` -- a stored-file line states its source and owner; an undecided key says UNDECIDED.

<criterion id="BAB2-AC2" cell_refs="BF-ab-2"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_fwd4_stored_files.py</invocation><expect>FWD4-STORED ok=True</expect></criterion>
`BAB2-AC2` -- every stored file's list line reads with a source and an owner, and one move is read from the list alone.

<expected_criteria>BAB2-AC1,BAB2-AC2</expected_criteria>

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
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round13.md</decomp_doc> (round 13), cell `BF-ab-2`.
<owned_cells>BF-ab-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BAB2-AC1, BAB2-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-ab-2.fwd4-stored-files-source-owner.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BAB2-AC1,BAB2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; files, with source and owner, undecided; the one move read; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a source or owner inferred from the folder name (read from the ruling or key class; UNDECIDED otherwise); a move applied to S3 (read only); another line kind changed (the test and the full naming sweep hold); BLIND: keys built at run time.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round12.md @b45108c324 (`1.0.0_SA_CTO~DELL1`, msg 2324), item item 2 (FWD-4 group D); decomposition round 13. Base dry-run at the cut, by the
issuer at base b89f2f09c4: BAB2-AC1 base: PASS as expected (ROOTCHECK-TEST ok=True; extended by the cell); BAB2-AC2 base: FAIL as expected (file absent; S3Key lines carry no source/owner field).
