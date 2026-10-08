# TO LGIC_BLANKFIX.TO-BF-s-7 -- round 5 BF-s-7: the cross-firm sweep's remainder -- each refused line read, each unchecked key given its reason on the line or checked

<to_id>LGIC_BLANKFIX.TO-BF-s-7</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-s-7` (`decompositions/LGIC_BLANKFIX_DECOMP.round5.md`) | **outcome_ref:** FWD-1 over all roots |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --root ROOT` prints one line per name of a Terraform root:
`KIND type current -> detail  [where]`, kinds `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`; it exits 1 while
any line is a `HOLE`. Two roots read with no hole and were graded by a seat that built none of the check (`bd-pipeline`, 142
names; `investor-reporting/directory`, 18). The run over all 13 roots the root map covers reads 412 names and 38 holes on 9
roots: the table is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/ALL_MAPPED_ROOTS_round4.txt` and each root's whole output is under
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/all_roots_round4/`. The CTO's reading is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round4.md` -- read it first.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`), `opal_naming_scope.py`, `opal_naming_rootmap.py`,
`opal_naming_cadence.py`, `opal_naming_keyfill.py` (`fill_keys`, `bucket_of`, the `crossfirm` command),
`opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `check_root`, `map_key`, the `lines` and `keys` commands). The
registry is `infra/logic/registry/` (`root_map.json`, `key_rulings.json`, `event_rules.json`, `legacy_addresses.json`,
`resources.json`, `systems.json`); the map is `infra/logic/registry/root_map.json`. Read the modules your cell touches or calls before
you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new dependency; no
AWS call and no network call. The bar: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at the base (194 passed)
and every `lib/tests/test_opal_naming_*.py` script prints `ok=True`; none may fail after your build. A test you write asserts
relations and the rows it needs by name, never a typed total of repository names or registry rows: those move every day.

### THE CELL

`BF-s-7`. `python lib/opal_naming_keyfill.py crossfirm --map infra/logic/registry/root_map.json` reads 79 stored files over 13 roots: 31
checked, 48 unchecked, 3 refused. Two things are open. (a) The 3 refused are all `bd-pipeline`: two
`code/bronze/cot_bronze_ingest.py` (a registry key ruling now answers them, and the root check prints them `FIX`) and
`schwab/08242234/silver/fact_rps`, which the key reader refuses ("the path word schwab names a source other than the entry's")
while the root check prints it `RIGHT`. The two modules disagree on one key. (b) The 48 unchecked say only that the firm could
not be checked.

**Build** in `lib/opal_naming_keyfill.py`:
1. `fill_keys` and the `crossfirm` command read `infra/logic/registry/key_rulings.json` the way the root check does (read
   `opal_naming_rootcheck`'s loader and match rule and call or mirror them; do not write a different rule): a key a ruling
   answers is `RULED`, not refused and not unchecked.
2. The Schwab key: find by reading why the key reader refuses a key the grader calls conformant. A path whose own first segment
   is a source the registry knows names ITS source; that is not a conflict with the root's source. Fix the conflict test so a
   key is refused for a FIRM other than its bucket's firm, and for a source only where the registry says the bucket belongs to
   one source and the path names another. State in your report exactly what the test was and is.
3. Every unchecked key carries ONE reason from a closed list on its line: `bucket-names-no-firm` (a shared store: name the
   bucket), `bucket-not-read` (say why: no literal, or several candidates), `bucket-chosen-at-run-time` (name the variable),
   `no-path-word-names-a-firm` (nothing to check). The last is a CHECKED key with nothing to refuse, not an unchecked one: count
   it under `checked`.
4. Last line `KEYFILL-CROSSFIRM ok=True roots=N keys=N checked=N ruled=N unchecked=N refused=N`, summing to `keys`, with a table
   of the unchecked by reason.
**Extend** `lib/tests/test_opal_naming_keyfill.py`: one case per reason; the DIFFERENCE CONTROL for the source test (a path naming
its own registry source in a firm's bucket is not refused; a path naming another FIRM is).

### ACCEPTANCE

<criterion id="BS7-AC1" cell_refs="BF-s-7"><invocation>python lib/tests/test_opal_naming_keyfill.py</invocation><expect>KEYFILL-TEST ok=True</expect></criterion>
`BS7-AC1` -- each reason is reachable, and a path naming its own source is not a cross-firm refusal.

<criterion id="BS7-AC2" cell_refs="BF-s-7"><invocation>python lib/opal_naming_keyfill.py crossfirm --map infra/logic/registry/root_map.json</invocation><expect>ruled=</expect></criterion>
`BS7-AC2` -- the real sweep: every key is checked, ruled, refused or unchecked with one named reason.

<expected_criteria>BS7-AC1,BS7-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W3-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_keyfill.py
lib/tests/test_opal_naming_keyfill.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the saved tables and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round4.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md</decomp_doc> (round 5), cell `BF-s-7`.
<owned_cells>BF-s-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BS7-AC1, BS7-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/LGIC_BLANKFIX.TO-BF-s-7.crossfirm-remainder.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BS7-AC1,BS7-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the unchecked table by reason; every refused line whole; what the source test was and is; the root check's last line on bd-pipeline before and after (it must not change); commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a refusal loosened until nothing is refused (the difference control keeps another firm's path refused); unchecked keys relabelled checked to shrink the count (only the no-path-word reason moves, and the face says why); two modules still disagreeing on one key (the report states both answers for the three refused keys); BLIND: a bucket's live owner.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round4.md @095d99c984 (the CTO's enrichment list); decomposition round 5. Base dry-run at the cut: BS7-AC1 base PASS as expected (ran: KEYFILL-TEST ok=True cases=47; extended by the cell); BS7-AC2 base FAIL as expected (ran: the last line carries no ruled field).
