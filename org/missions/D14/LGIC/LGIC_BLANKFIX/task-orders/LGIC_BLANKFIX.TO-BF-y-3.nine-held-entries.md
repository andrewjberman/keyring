# TO LGIC_BLANKFIX.TO-BF-y-3 -- round 10 BF-y-3: the nine held root-map entries drafted per the CRO's round-10 rulings; mapped and hole before and after

<to_id>LGIC_BLANKFIX.TO-BF-y-3</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `BF-y-3` (`decompositions/LGIC_BLANKFIX_DECOMP.round10.md`) | **outcome_ref:** FWD-2, FWD-7 |
**depends_on:** 4.0.0_SA_CRO's rulings @acbc0d9aa6 in the base (the issuer spawns this slot once they are)

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --all-roots` (the same as `python lib/opal_naming_rootcheck.py all
--map infra/logic/registry/root_map.json`) runs every Terraform root the root map covers and prints the denominator of roots
first; `infra/logic/README.md` "Run the naming check" explains its lines and fields. At this cut, on the base your worktree is
made from, it reads: `ALL-ROOTS ok=True roots_total=87 mapped=78 unmapped=9 completed=78 stopped=0 items=2263 right=558 fix=1460 not_asked=222 pattern=23 carded=0 refused=0 hole=0 carded_class_holes=0 source_bucket_holes=0 event_rule_holes=0 unknown_word_holes=0 other_holes=0 stale_hints=0 uncounted=1 counted_at_caller=17`. The round-9 close is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ALL_ROOTS_round9.txt`. The CTO's reading of round 9 is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round9.md` -- read it first, with its
ADDENDUM 1 (this round is three cells: the two override fixes and the nine held entries). The round-9 drain end is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ROUND9_DRAIN_END.md`.
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

`BF-y-3`. Round 8 held nine root-map entries (shared-infra, astn-pipeline, five multi-vendor roots, two empty roots) until their
owners and tokens were ruled. `4.0.0_SA_CRO` ruled them in `org/tier1_exec/4.0.0_SA_CRO/deliverables/ROOT_MAP_ROUND10_RULINGS_20261009.md` (@acbc0d9aa6) -- read it whole; each table names
the exact fields to write: shared-infra -> system `cloudops`; astn-pipeline -> `news`, the astn token unresolved; the five
multi-vendor roots -> scope `global`, source = the product; the two empty roots RETIRED (0 resources), so `roots_total` reads 85.
The round-8 cell that drafted entries the same way is `org/missions/D14/LGIC/LGIC_BLANKFIX/task-orders/LGIC_BLANKFIX.TO-BF-w-4.held-entries-land.md`, its files in
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/`; the round-9 holes cell is `org/missions/D14/LGIC/LGIC_BLANKFIX/task-orders/LGIC_BLANKFIX.TO-BF-x-6.holes-on-new-roots.md`.

**Build** in your deliverables folder (only `4.0.0_SA_CRO` writes the registry):
1. `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/MAP_ENTRIES_round10.json`: one entry per ruled root in `infra/logic/registry/root_map.json`'s shape, every field cited
   (`_cite`) to the ruling table or the code; the two retired roots listed under `"retire"` with the ruling's line.
2. For every HOLE the newly mapped roots print once merged: a registry row drafted in `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/REGISTRY_ROWS_round10.json` (keyed by
   registry file, `_about.row_fields` shape, `_cite`), or the line in `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/HOLES_OWNED_round10.md` with its owner.
3. `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_held_entries_round10.py`: copies `infra/logic/registry/` to a temporary folder, merges the entries and rows
   (`_cite` stripped), applies the retirements to the copy, runs the `all` command once against the copy, and prints last:
   `HELD-ENTRIES ok=True entries=N land=N refused=0 retired=N mapped_before=N mapped_after=N hole_before=N hole_after=N`;
   `ok=True` when `refused=0`, every ruled root lands, no HOLE on the 78 roots mapped before is added, and the merged run prints
   `ok=True`. `mapped_before` and `hole_before` come from the ALL-ROOTS line of `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ALL_ROOTS_round9.txt`.

### ACCEPTANCE

<criterion id="BY3-AC1" cell_refs="BF-y-3"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_held_entries_round10.py</invocation><expect>HELD-ENTRIES ok=True</expect></criterion>
`BY3-AC1` -- every ruled root lands on a registry copy, the retired roots leave the denominator, and holes on the new roots are filled or owned.

<criterion id="BY3-AC2" cell_refs="BF-y-3"><invocation>python lib/tests/test_opal_naming_rootmap.py</invocation><expect>ROOTMAP-TEST ok=True</expect></criterion>
`BY3-AC2` -- the root-map reader's test holds.

<expected_criteria>BY3-AC1,BY3-AC2</expected_criteria>

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
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under
`infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round9.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round10.md`, and the `lib/` modules and `.tools/` scripts your block does
not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round10.md</decomp_doc> (round 10), cell `BF-y-3`.
<owned_cells>BF-y-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BY3-AC1, BY3-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-y-3.nine-held-entries.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BY3-AC1,BY3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last lines whole; mapped and hole before and after; entries per ruling table; rows drafted; owned-elsewhere per owner; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- an entry field guessed rather than cited (every field carries _cite to the ruling or the code); a retired root silently dropped instead of listed; a registry edit (drafts only, in the folder); BLIND: the ruling file itself, which is the CRO's and not re-decided here.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round9.md @1bd6fcf3dd + ADDENDUM 1 (`1.0.0_SA_CTO~DELL1`, msgs 2050, 2088), item ADDENDUM 1 (3); decomposition round 10. Base dry-run at the cut, by the
issuer at base 9f252e010a: BY3-AC1 base: FAIL as expected (file absent; the CRO ruling @acbc0d9aa6 not yet in the base); BY3-AC2 base: PASS as expected (ran: ROOTMAP-TEST ok=True assertions=46).
