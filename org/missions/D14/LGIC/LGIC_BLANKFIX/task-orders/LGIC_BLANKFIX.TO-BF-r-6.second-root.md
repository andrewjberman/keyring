# TO LGIC_BLANKFIX.TO-BF-r-6 -- round 3 BF-r-6: a second root -- the same run on one root the map newly covers

<to_id>LGIC_BLANKFIX.TO-BF-r-6</to_id>
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

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-r-6` (`decompositions/LGIC_BLANKFIX_DECOMP.round3.md`) | **outcome_ref:** FWD-2, FWD-9 |
**depends_on:** BF-r-3 merged (the map covers more roots); handed by AMENDMENT 1 naming the root

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

`BF-r-6`. The first step off the thread: the same run on ONE second Terraform root that the landed root map newly covers. The root
is named in AMENDMENT 1, written into this order before it is handed to you (the issuer picks it from the map's entries after
`BF-r-3` merges: the newly covered root with the fewest names that holds at least one schedule, one inline policy and one stored
file). If this order reaches you with no AMENDMENT 1, stop and report. You build nothing in `lib/`.

1. Run `python lib/opal_naming_rootcheck.py THE-ROOT --map infra/logic/registry/root_map.json --report-only` from the worktree root and
   save the whole output to `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/SECOND_ROOT_TRACE_round3.txt`.
2. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_second_root.py`: it takes no argument (the
   root is a constant in it, the one AMENDMENT 1 names), re-runs the command, compares with the saved file, and checks: the last
   line reads `ROOTCHECK ok=True`; the counts sum to `items`; `items` equals `len(opal_naming_scope.root_items(root, map)[0])`; no
   `FIX` line contains `{`; no two different current names of one type share a `FIX` target. It prints the count per kind and
   `SECOND-ROOT ok=True root=... items=N hole=N differs=0`. Holes are EXPECTED on a root nobody has run before: `ok` does not
   depend on `hole`; every `HOLE` line goes in your report whole, grouped by what would close it.

### ACCEPTANCE

<criterion id="BR6-AC1" cell_refs="BF-r-6"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_second_root.py</invocation><expect>SECOND-ROOT ok=True</expect></criterion>
`BR6-AC1` -- the run completes on a second real root, one line per name, the count matching the scope's own.

<criterion id="BR6-AC2" cell_refs="BF-r-6" judgment="true"/>
`BR6-AC2` (judgment) -- `3.0.0_SA_CVO` reads the second root's run to the end and says, line kind by line kind, whether a reader who did not build the check can act on it, and which holes are the registry's to close. You record the artifact's path and NO verdict.

<expected_criteria>BR6-AC1,BR6-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- Your whole build lives in your deliverables folder, which the tree convention grants; the block below names only the investigation file.
- The judgment criterion gets its artifact path and NO verdict from you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>

org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round2_bd-pipeline.txt`, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round2.md`, `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND2_L9_GRADE_BE8_AC3_20261007.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round3.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round3.md</decomp_doc> (round 3), cell `BF-r-6`.
<owned_cells>BF-r-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BR6-AC1, BR6-AC2 (judgment: recorded UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming `3.0.0_SA_CVO`). Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-r-6.second-root.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BR6-AC1,BR6-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; the trace's path; the count per kind; every `HOLE` line whole, grouped by what would close it and whose that is; commits.

### AMENDMENT 1 (2.0.0_SA_COO~G, 2026-10-07) -- the root is picked; the order is handed

`BF-r-3` is merged (@11ea2aa49a) and the landed map covers 13 roots. THE-ROOT is **`infra/aws/terraform/investor-reporting/directory`**
(map key `investor-reporting/directory`). The issuer applied the rule stated in the cell to the 12 roots the map newly covers:
three hold at least one schedule or event rule, one inline policy and one stored file (`investor-reporting/directory` 17 names,
`cot-pipeline` 54, `opal-assets` 84); the fewest names is the pick. Measured by the issuer at the pick, with the scope's own
`root_items(root, map)`: 17 names, 4 schedules or event rules, 7 policies, 2 stored files, 1 source folder.

Two things to know about this root:
- Its map entry carries `fills: ["system"]`: it serves more than one firm, so the entry may supply a system and never a firm. A
  reader that honours that field is being built by another cell of this round (`BF-r-2`) and may not be merged in your worktree.
  Run the check as your worktree has it, and say in your report whether your run honoured `fills` (does any line fill a firm
  from the map entry?).
- The run is of `lib/opal_naming_rootcheck.py` at your worktree's HEAD. If the map key form (`investor-reporting/directory`)
  is not what `check_root` passes to `resolve`, that is a finding: report it and file one row; do not edit any `lib/` module.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a root chosen because it reads clean (the issuer picks it by a stated rule before the run); a run that stops on a name it cannot read reported as complete (the last line and the item count against the scope's own); BLIND: names of the root that live only in AWS.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round2.md @ef7133ec9a (the CTO's enrichment list); decomposition round 3. Base dry-run at the cut: BR6-AC1 base FAIL as expected (file absent).
