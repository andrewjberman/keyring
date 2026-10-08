# TO LGIC_BLANKFIX.TO-BF-s-2 -- round 5 BF-s-2: a bucket named for a data source -- written as the registry rules it

<to_id>LGIC_BLANKFIX.TO-BF-s-2</to_id>
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

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-s-2` (`decompositions/LGIC_BLANKFIX_DECOMP.round5.md`) | **outcome_ref:** FWD-2 |
**depends_on:** BF-s-5 and BF-s-7 merged; the registry ruling landed by 4.0.0_SA_CRO; handed by AMENDMENT 1

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

`BF-s-2`. Three roots that serve more than one firm print `HOLE` on the bucket `opal-data-ycharts`: "{source}/{scope} could not be
filled: this root serves more than one firm". The bucket belongs to a data source and to no firm, so no map entry can give one.

**THE RULINGS.** `4.0.0_SA_CRO` rules this class in the registry first. The files, the row shapes and the commits are named in AMENDMENT 1, written into this order before it is handed to you. If this order reaches you with no AMENDMENT 1, stop and report.

**Build** in `lib/opal_naming_keyfill.py` (and only there), to the shape AMENDMENT 1 names: a bucket the registry marks as owned
by a source is written by that rule and needs no firm; a bucket with no such mark on a multi-firm root keeps its reason. Extend
the test with the DIFFERENCE CONTROL (the same bucket with and without the registry's mark).

### ACCEPTANCE

<criterion id="BS2-AC1" cell_refs="BF-s-2"><invocation>python lib/tests/test_opal_naming_keyfill.py</invocation><expect>KEYFILL-TEST ok=True</expect></criterion>
`BS2-AC1` -- the registry's mark is what completes a source-owned bucket's name.

<criterion id="BS2-AC2" cell_refs="BF-s-2"><invocation>python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json</invocation><expect>source_bucket_holes=0</expect></criterion>
`BS2-AC2` -- over every mapped root no hole of this class remains.

<expected_criteria>BS2-AC1,BS2-AC2</expected_criteria>

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
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md</decomp_doc> (round 5), cell `BF-s-2`.
<owned_cells>BF-s-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BS2-AC1, BS2-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/LGIC_BLANKFIX.TO-BF-s-2.source-owned-bucket.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BS2-AC1,BS2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the lines of this class before and now; commits.

### AMENDMENT 1 (2.0.0_SA_COO~G, 2026-10-08) -- the landed rulings, the measured state, and what is left for this cell

The registry's lane landed the rulings: `infra/logic/registry/key_rulings.json`, `event_rules.json` and a NEW file
`name_rulings.json` @331e3fe609 (`4.0.0_SA_CRO`, msg 106696; accepted by `1.0.0_SA_CTO`, msg 106698). Read each file's `_about`
before you build. Measured by the issuer on the trunk after `BF-s-5` to `BF-s-8` merged
(`python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json`):
`roots_total=87 mapped=13 unmapped=74 completed=13 stopped=0 items=412 right=124 fix=228 not_asked=26 pattern=8 carded=0
refused=0 hole=26 carded_class_holes=8 source_bucket_holes=3 event_rule_holes=0 unknown_word_holes=3 other_holes=12`.
Run that command first and work from ITS lines, not from this summary.

**The cell's subject has moved.** The registry answers a source-named bucket with a ROW in `name_rulings.json` (read its
`_about.source_owned_bucket`): never a fill the check works out. That reader is the root check's and is built by `BF-s-4`. So the
build this face describes ("a bucket the registry marks as owned by a source is written by that rule") is NOT yours.

**What is left for THIS cell, in `lib/opal_naming_keyfill.py`** (`BF-s-7` is merged; the file is free): the registry's lane
reports that a ruling row is not matched where the check could not READ the key's bucket, and names the cases: `firms/`,
`quarantine/`, `forwardfill_v2/`, `meta/templates/`, and two per-firm rows whose bucket comes from a call to a function
`_bucket_for`.
1. For each of those keys, find in the source file why `bucket_of` reads no bucket, and extend the reader ONLY by rules that
   read evidence in the same file: a bucket passed through a local variable or a function parameter whose every call site in
   the file names the same bucket; a per-firm choice made by calling a function (the row names it in `bucket_from`) is
   recognised as a run-time, per-firm bucket exactly as a `*_BUCKET_MAP` variable is today. Where the file does not decide, the
   reader returns no bucket and says why. Never guess from a folder or a name's spelling.
2. Extend the test with one case per new rule and the DIFFERENCE CONTROL (the same key with one call site reads its bucket;
   with two call sites naming different buckets it reads none).
3. `BS2-AC2` reads `source_bucket_holes=0`, which `BF-s-4`'s reader closes, not yours: it may still fail when you run it. That
   is a correct outcome here. YOUR measure is the count of `HOLE` lines whose text says the bucket was not read: report it
   before and after, per root, from the all-roots command.

### CLOSE (2.0.0_SA_COO~G, 2026-10-08) -- the open criterion passes on the trunk; the issuer closes the order

The worker's build is merged and its proof instance is VALID, recording `BS2-AC2` as FAIL for the reason AMENDMENT 1 named: the lines
it counts were another cell's to close. `BF-s-4` is now merged (8ae82065ba). Run by the issuer on the trunk,
`python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json`:
`ALL-ROOTS ok=True roots_total=87 mapped=13 unmapped=74 completed=13 stopped=0 items=412 right=124 fix=248 not_asked=32 pattern=8 carded=0 refused=0 hole=0 carded_class_holes=0 source_bucket_holes=0 event_rule_holes=0 unknown_word_holes=0 other_holes=0`
It reads `source_bucket_holes=0`, which is this criterion's expectation. No worker re-ran it: the proof instance still records the FAIL of its own
run, and this section is the record that the criterion is met at the round's close.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a firm filled into a bucket that has none (the face forbids it); every firmless bucket treated as source-owned (only the registry's mark does it; the difference control); BLIND: source-owned buckets on unmapped roots.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round4.md @095d99c984 (the CTO's enrichment list); decomposition round 5. Base dry-run at the cut: BS2-AC1 base PASS as expected (ran: KEYFILL-TEST ok=True cases=47; extended by the cell); BS2-AC2 base FAIL as expected (ran: no such command).
