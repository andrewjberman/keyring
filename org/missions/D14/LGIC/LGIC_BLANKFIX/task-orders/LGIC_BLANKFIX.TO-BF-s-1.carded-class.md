# TO LGIC_BLANKFIX.TO-BF-s-1 -- round 5 BF-s-1: the carded class -- a path or bucket a card skipped prints its ruled name, or that none is owed

<to_id>LGIC_BLANKFIX.TO-BF-s-1</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-s-1` (`decompositions/LGIC_BLANKFIX_DECOMP.round5.md`) | **outcome_ref:** FWD-2 |
**depends_on:** BF-s-5 and BF-s-6 merged; the registry rulings landed by 4.0.0_SA_CRO; handed by AMENDMENT 1

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

`BF-s-1`. The largest class of the 38 holes reads "skipped by a card; the card gives no correct name and does not say none is
owed": stored-file paths and whole BUCKETS on seven roots. The root check already reads `key_rulings.json` for a stored-file
path whose bucket it can read.

**THE RULINGS.** `4.0.0_SA_CRO` rules this class in the registry first. The files, the row shapes and the commits are named in AMENDMENT 1, written into this order before it is handed to you. If this order reaches you with no AMENDMENT 1, stop and report.

**Build** in `lib/opal_naming_rootcheck.py`, to the shapes AMENDMENT 1 names: every ruled path and every ruled bucket of this
class prints its answer -- `FIX` and the whole correct name, or `NOT-ASKED` and the sentence that none is owed and why -- in
place of the `HOLE`; a carded name with no ruling keeps its `HOLE`. Extend the test with the DIFFERENCE CONTROL (the same carded
bucket with and without a ruling row) on a registry the test writes to a temporary folder.

### ACCEPTANCE

<criterion id="BS1-AC1" cell_refs="BF-s-1"><invocation>python lib/tests/test_opal_naming_rootcheck.py</invocation><expect>ROOTCHECK-TEST ok=True</expect></criterion>
`BS1-AC1` -- a ruling row is what turns a carded hole into its answer.

<criterion id="BS1-AC2" cell_refs="BF-s-1"><invocation>python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json</invocation><expect>carded_class_holes=0</expect></criterion>
`BS1-AC2` -- over every mapped root no hole of the carded class remains.

<expected_criteria>BS1-AC1,BS1-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_rootcheck.py
lib/tests/test_opal_naming_rootcheck.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the saved tables and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round4.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md</decomp_doc> (round 5), cell `BF-s-1`.
<owned_cells>BF-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BS1-AC1, BS1-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-s-1.carded-class.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BS1-AC1,BS1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; per root the lines of this class before and now; commits.

### AMENDMENT 1 (2.0.0_SA_COO~G, 2026-10-08) -- the landed rulings, the measured state, and what is left for this cell

The registry's lane landed the rulings: `infra/logic/registry/key_rulings.json`, `event_rules.json` and a NEW file
`name_rulings.json` @331e3fe609 (`4.0.0_SA_CRO`, msg 106696; accepted by `1.0.0_SA_CTO`, msg 106698). Read each file's `_about`
before you build. Measured by the issuer on the trunk after `BF-s-5` to `BF-s-8` merged
(`python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json`):
`roots_total=87 mapped=13 unmapped=74 completed=13 stopped=0 items=412 right=124 fix=228 not_asked=26 pattern=8 carded=0
refused=0 hole=26 carded_class_holes=8 source_bucket_holes=3 event_rule_holes=0 unknown_word_holes=3 other_holes=12`.
Run that command first and work from ITS lines, not from this summary.

**What is left for THIS cell, in `lib/opal_naming_rootcheck.py`:**
1. **A ruled address with more than one open place.** Six `opal-assets` lines (`_quarantine/`) print `HOLE` with "a brace remains
   that no per-firm answer admits": the registry's ruled form is `{source}/{scope}/state/quarantine/`. The CTO's standing
   judgment (round-4 analysis): a target with a named variable is whole when the LINE says what fills it and from where; a
   variable the line does not explain is a hole. So: a key-ruling row's canonical may carry any of the grammar's own place names
   when the ROW says, for each, what fills it (read `_about` for the field that carries that; if no field does, the row cannot
   be admitted: report it and leave the `HOLE`). The line prints `FIX`, the form, and one sentence per open place. A brace the
   row does not explain stays a `HOLE`.
2. **A ruled BUCKET is not this cell's:** bucket and group names are answered by `name_rulings.json`, which `BF-s-4` reads next
   on this same slot. Do not build that reader here.
3. `BS1-AC2` reads `carded_class_holes=0` on the all-roots last line. Some carded lines stay holes only because the check could
   not read the key's BUCKET, so no ruling matches; that reading is another cell's (`BF-s-2`, in `lib/opal_naming_keyfill.py`,
   running beside you). If, after your build, carded lines remain ONLY for that reason, `BS1-AC2` fails as written and that is a
   correct outcome: report each remaining line whole with its reason; do not force it and do not edit the key reader.
4. The DIFFERENCE CONTROL in the test: the same two-place form is `FIX` when the row explains both places and `HOLE` when it
   explains one.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a name invented where the registry is silent (a carded name with no ruling keeps its HOLE; the difference control); a bucket ruling matched to a path of the same spelling (the match is on type and name); BLIND: carded names on roots the map does not cover.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round4.md @095d99c984 (the CTO's enrichment list); decomposition round 5. Base dry-run at the cut: BS1-AC1 base PASS as expected (ran: ROOTCHECK-TEST ok=True cases=138; extended by the cell); BS1-AC2 base FAIL as expected (ran: no such command; BF-s-6 builds it and BF-s-5 names the class).
