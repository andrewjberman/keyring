# TO LGIC_BLANKFIX.TO-BF-w-4 -- round 8 BF-w-4: the 24 held map entries -- landed where the code decides their fields, the rest named

<to_id>LGIC_BLANKFIX.TO-BF-w-4</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-w-4` (`decompositions/LGIC_BLANKFIX_DECOMP.round8.md`) | **outcome_ref:** FWD-7 |
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

`BF-w-4` (item E4; row `LGIC_BLANKFIX-S10`). Round 7's `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/MAP_ENTRIES_round7.json` holds 74 entries; 50 landed (written by
`4.0.0_SA_CRO` @9b9928ea92) and 24 carry `UNDECIDED` fields. The CRO's round-7 rulings `org/tier1_exec/4.0.0_SA_CRO/deliverables/ROOT_MAP_ROUND7_RULINGS_20261008.md` (read it whole) release
some: the CompDiff family of 7 takes `system: advi` and each root's firm as its scope; the home-value convention is ratified (with 5
product roots still held); `W3-S10` is adopted. The two empty roots (`canonical-schwab-si2-schedule`, `opal-assets-absence`) stay
named: the CRO recommends retiring them as dead Terraform.

**Build** in your deliverables folder:
1. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/MAP_ENTRIES_round8.json`: `{"roots": {...}}` with one entry for EACH of the 24 roots round 7 held (read the
   round-7 file: an entry is held when a field other than `_cite` reads `UNDECIDED`), in `infra/logic/registry/root_map.json`'s shape, every field
   cited (`_cite`) or left `UNDECIDED` with what was read. Apply the CRO's rulings; decide the rest from the code.
2. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/check_entries_land_round8.py`: for each entry, merged alone into a temporary copy of the CURRENT
   `infra/logic/registry/root_map.json`, `load_map` decides LANDS / HELD / REFUSED as in round 7; then every landing entry is merged together and the
   `all` command runs once on that copy. It prints one line per root and the merged `ALL-ROOTS` line, then last:
   `ENTRIES-LAND ok=True entries=N land=N held=N refused=0 undecided_fields=N merged_ok=True`; `ok=True` when `refused=0`,
   `land + held == entries`, `entries` equals the round-7 file's held count, and the merged run prints `ok=True`.

### ACCEPTANCE

<criterion id="BW4-AC1" cell_refs="BF-w-4"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/check_entries_land_round8.py</invocation><expect>ENTRIES-LAND ok=True</expect></criterion>
`BW4-AC1` -- every held entry lands or names what holds it, none is refused, and the landing ones run whole on the current map.

<expected_criteria>BW4-AC1</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- Your whole build lives in your deliverables folder, which the tree convention grants; the block below names only the investigation file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W3-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>

org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round7.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round8.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round8.md</decomp_doc> (round 8), cell `BF-w-4`.
<owned_cells>BF-w-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BW4-AC1. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/LGIC_BLANKFIX.TO-BF-w-4.held-entries-land.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BW4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; land/held/undecided against round 7's 24/47; each entry still held and what holds it; the merged ALL-ROOTS line; the entries file's path for 4.0.0_SA_CRO; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a field filled from a folder's spelling (each decided value cites its line); an entry dropped so the counts look better (entries is checked against round 7's held count); a ruling of the CRO's misapplied (the rulings file is quoted where used); BLIND: names that live only in AWS.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round7.md @ec6f56562b (the CTO's enrichment list E1 to E5); decomposition round 8. Base dry-run at the cut: BW4-AC1 base FAIL as expected (file absent; the round-7 file holds 24 entries with UNDECIDED fields).
