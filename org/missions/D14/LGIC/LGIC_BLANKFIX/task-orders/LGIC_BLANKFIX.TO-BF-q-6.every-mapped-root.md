# TO LGIC_BLANKFIX.TO-BF-q-6 -- round 4 BF-q-6: the run over every root the folder map covers -- its totals, the same from a second seat

<to_id>LGIC_BLANKFIX.TO-BF-q-6</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-q-6` (`decompositions/LGIC_BLANKFIX_DECOMP.round4.md`) | **outcome_ref:** FWD-9 |
**depends_on:** BF-q-5 merged with both roots reading no hole; handed by continuation

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --root ROOT` prints one line per name of a Terraform root:
`KIND type current -> detail  [where]`, kinds `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`; it exits 1 while
any line is a `HOLE`. Round 3's runs are saved: `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round3_bd-pipeline.txt` (140 names: 114 fix, 12 not
asked, 9 right, 3 pattern, 2 refused, 0 holes) and `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/SECOND_ROOT_TRACE_round3_investor-reporting-directory.txt`
(17 names: 13 right, 2 fix, 2 holes). The CTO's reading of both is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round3.md` -- read it first.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`, the source-literal classifier), `opal_naming_scope.py`,
`opal_naming_rootmap.py`, `opal_naming_cadence.py`, `opal_naming_keyfill.py` (`fill_keys`, `bucket_of`),
`opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `check_root`, `map_key`; it reads
`infra/logic/registry/key_rulings.json`). The registry is `infra/logic/registry/`; the root map is `infra/logic/registry/root_map.json`.
Read the modules your cell touches or calls before you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only;
ASCII only in code and output; no new dependency; no AWS call and no network call. The bar for the library:
`python -m pytest lib/tests -q -p no:cacheprovider` passes whole at the base (194 passed); no test may fail after your build.

### THE CELL

`BF-q-6`. The first whole run off the thread: the same check over EVERY root the root map covers (13 at the cut; read the count
from the map, do not type it). You build nothing in `lib/`.

Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/all_mapped_roots.py`: for each root in the map, in sorted order, it runs
`opal_naming_rootcheck.check_root` with the map (report-only, capturing the output), and prints one line per root: the root, its
`ROOTCHECK` last line, and whether the run COMPLETED (a root whose run raises or prints no last line is `STOPPED`, with the
exception's text; it is counted, never dropped). Then totals over the completed roots: names and each kind's count. It saves the
per-root outputs under `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/all_roots_round4/` and the table as
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/ALL_MAPPED_ROOTS_round4.txt`. Last line
`ALL-ROOTS ok=True roots=N completed=N stopped=N items=N right=N fix=N not_asked=N pattern=N carded=N refused=N hole=N`;
`ok=True` when `completed + stopped == roots`, each completed root's counts sum to its `items`, and its `items` equals the
scope's own count with the map. `ok` does NOT depend on `hole`, `refused` or `stopped`: holes are expected on roots nobody has run.
Run it twice and require the two last lines to be identical (print `repeat=identical` or the difference).
In your report: every `STOPPED` root with its reason, and the `HOLE` lines grouped by what would close them and whose that is.

### ACCEPTANCE

<criterion id="BQ6-AC1" cell_refs="BF-q-6"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/all_mapped_roots.py</invocation><expect>ALL-ROOTS ok=True</expect></criterion>
`BQ6-AC1` -- every mapped root is run or counted as stopped, the totals sum, and a second run gives the same totals.

<expected_criteria>BQ6-AC1</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- Your whole build lives in your deliverables folder, which the tree convention grants; the block below names only the investigation file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>

org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the two saved traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round3.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round4.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round4.md</decomp_doc> (round 4), cell `BF-q-6`.
<owned_cells>BF-q-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BQ6-AC1. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-q-6.every-mapped-root.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BQ6-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; the table; every stopped root with its reason; the holes grouped by what would close them; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a root that stops dropped from the totals (completed + stopped == roots; a stopped root printed with its exception); totals that move between two runs (the script runs twice and compares); holes hidden to make the first whole run look clean (ok does not depend on them; they are grouped in the report); BLIND: roots the map does not cover -- 48 of 61 at the cut.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round3.md @f0e6411e53 (the CTO's enrichment list); decomposition round 4. Base dry-run at the cut: BQ6-AC1 base FAIL as expected (file absent).
