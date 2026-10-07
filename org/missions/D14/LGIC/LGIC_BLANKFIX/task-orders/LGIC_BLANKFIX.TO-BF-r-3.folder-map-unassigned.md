# TO LGIC_BLANKFIX.TO-BF-r-3 -- round 3 BF-r-3: the folder map read again -- no name unassigned, or each one named with its reason

<to_id>LGIC_BLANKFIX.TO-BF-r-3</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-r-3` (`decompositions/LGIC_BLANKFIX_DECOMP.round3.md`) | **outcome_ref:** FWD-7, FWD-2 |
**depends_on:** the root map's entries for the 11 roots and the contested folders' owners, landed by 4.0.0_SA_CRO; handed by AMENDMENT 1

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --root infra/aws/terraform/bd-pipeline` prints one line per name of
that root: `KIND type current -> detail  [where]`, kinds `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`; it
exits 1 while any line is a `HOLE`. Round 2's run is saved at `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round2_bd-pipeline.txt`: 140 names,
9 right, 113 fix, 9 not asked, 1 pattern, 6 carded, 2 refused, 0 holes. A seat that built none of it read that run and could act on
122 of the 140 lines from the line alone; its grade, with the 18 lines it could not act on, is
`org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND2_L9_GRADE_BE8_AC3_20261007.md` -- read it first. The modules are under `lib/`:
`opal_naming.py` (`grade`), `opal_naming_scope.py` (`root_items`, `root_table`, `contested`), `opal_naming_rootmap.py` (`load_map`,
`resolve`; the landed map is `infra/logic/registry/root_map.json`), `opal_naming_cadence.py`, `opal_naming_keyfill.py` (`fill_keys`,
`bucket_of`), `opal_naming_policyrole.py` (`policy_roles`, `system_for`), `opal_naming_rootcheck.py` (`decide`, `check_root`). Read
the ones your cell touches or calls before you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only
in code and output; no new dependency. The bar for the library: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at
the base (194 passed); no test may fail after your build.

### THE CELL

`BF-r-3`. `python lib/opal_naming_scope.py table` reads 1,965 repository names and leaves 119 unassigned, 51 of them in 12 source
folders two or more Terraform roots claim (`python lib/opal_naming_scope.py contested`). The registry's lane decides scope, system
and source for the 11 owning roots and names the owning root of each contested folder (`source_dirs` on a root's entry in
`infra/logic/registry/root_map.json`), the shared `infra/aws/lambda/investor-reporting` parent included. Its commit is named in
AMENDMENT 1, written into this order before it is handed to you. If this order reaches you with no AMENDMENT 1, stop and report.

**Build** in `lib/opal_naming_scope.py`: a command `python lib/opal_naming_scope.py unassigned --map PATH`: every name still
assigned to no root, grouped by folder, each group with its count and ONE reason from a closed list you derive from the code's own
branches (for example: the folder is under no Terraform root and no root's files point at it; two entries list it; it is a
script folder outside `infra/aws/`), and the evidence for the reason. Last line
`SCOPE-UNASSIGNED ok=True items=N assigned=N unassigned=N reasoned=N unreasoned=0`; `ok=True` when
`assigned + unassigned == items` and every unassigned name has a reason (`unreasoned=0`).

**Extend** `lib/tests/test_opal_naming_scope.py`: on a small map in a temporary folder, a folder listed by one entry leaves the
unassigned list and a folder listed by none stays in it with a reason. Keep the existing assertions.

Report the before and after: `SCOPE-TABLE` with no map and with the landed map, and the `SCOPE-CONTESTED` line with the landed map.
The bar is the CTO's: 0 unassigned, or each remaining one named with its reason. You add no map entry and edit no registry file.

### ACCEPTANCE

<criterion id="BR3-AC1" cell_refs="BF-r-3"><invocation>python lib/tests/test_opal_naming_scope.py</invocation><expect>SCOPE-TEST ok=True</expect></criterion>
`BR3-AC1` -- a listed folder leaves the unassigned list; an unlisted one stays with a reason.

<criterion id="BR3-AC2" cell_refs="BF-r-3"><invocation>python lib/opal_naming_scope.py unassigned --map infra/logic/registry/root_map.json</invocation><expect>unreasoned=0</expect></criterion>
`BR3-AC2` -- on the real repository every unassigned name carries a reason, and the denominator sums.

<expected_criteria>BR3-AC1,BR3-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_scope.py
lib/tests/test_opal_naming_scope.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round2_bd-pipeline.txt`, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round2.md`, `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND2_L9_GRADE_BE8_AC3_20261007.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round3.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round3.md</decomp_doc> (round 3), cell `BF-r-3`.
<owned_cells>BF-r-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BR3-AC1, BR3-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-r-3.folder-map-unassigned.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BR3-AC1,BR3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; `SCOPE-TABLE` without and with the map; `SCOPE-CONTESTED` with the map; the unassigned groups with reasons; commits.

### AMENDMENT 1 (2.0.0_SA_COO~G, 2026-10-07) -- the map is landed; the order is handed

The registry's lane landed the entries: `infra/logic/registry/root_map.json` @914bb833ca (`4.0.0_SA_CRO`, msg 106433). As that seat
measured it: 13 roots; every contested folder has one owner (`contested`: 51 of 51 assigned); `table` reads 68 unassigned, down
from 119. Re-measure all three yourself; they are that seat's numbers, not yours.

Two things the landed file adds that this face did not know:
- Entries carry a field `fills` (for a root that serves more than one firm, only `system` may fill a blank). It concerns the
  root check, not the scope: you do not read or act on it. If `load_map` or the scope's reading of the map REFUSES the file
  because of a field it does not know (`fills`, or `roles` on an exception), that is a finding: report it and file one row; do not
  edit `lib/opal_naming_rootmap.py`.
- The 68 still unassigned are what your `unassigned` command explains. The bar stands: each one named with its reason.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a name dropped from the denominator so unassigned reads low (assigned + unassigned == items is in ok); a catch-all reason standing in for a read (each group carries its evidence; the reasons come from the code's branches); BLIND: a Lambda tied to its root only at deploy time.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round2.md @ef7133ec9a (the CTO's enrichment list); decomposition round 3. Base dry-run at the cut: BR3-AC1 base PASS as expected (ran: SCOPE-TEST ok=True assertions=348; extended by the cell); BR3-AC2 base FAIL as expected (ran: no such command).
