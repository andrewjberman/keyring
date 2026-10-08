# TO LGIC_BLANKFIX.TO-BF-s-4 -- round 5 BF-s-4: first-segment words the canon does not hold -- a real path is ruled, a pattern is printed as a pattern

<to_id>LGIC_BLANKFIX.TO-BF-s-4</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-s-4` (`decompositions/LGIC_BLANKFIX_DECOMP.round5.md`) | **outcome_ref:** FWD-2, FWD-8 |
**depends_on:** BF-s-1 merged; the registry rulings landed by 4.0.0_SA_CRO; handed by AMENDMENT 1

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

`BF-s-4`. Four lines print `HOLE` because a word is in no vocabulary: stored-file prefixes `bbg/` (`investor-reporting/core`) and
`firms/` (`investor-reporting/export`), the group name `calculated-group` (`investor-reporting/performance`) and the secret
`astn/kimi/api-key` (`investor-reporting/ycharts`). For each the question is the CTO's: is it a real stored path, group or
secret, or a pattern in the code? A real one gets a registry ruling; a pattern is printed as a pattern and never as a name.

**THE RULINGS.** `4.0.0_SA_CRO` rules this class in the registry first. The files, the row shapes and the commits are named in AMENDMENT 1, written into this order before it is handed to you. If this order reaches you with no AMENDMENT 1, stop and report.

**Build** in `lib/opal_naming_rootcheck.py`, to what AMENDMENT 1 names for each of the four: a ruled name prints its answer; a
name the registry marks as a code pattern prints `PATTERN` with the registry's sentence; a name with neither keeps its `HOLE`.
Extend the test with one case per branch and the DIFFERENCE CONTROL for the pattern mark.

### ACCEPTANCE

<criterion id="BS4-AC1" cell_refs="BF-s-4"><invocation>python lib/tests/test_opal_naming_rootcheck.py</invocation><expect>ROOTCHECK-TEST ok=True</expect></criterion>
`BS4-AC1` -- a registry mark is what makes a line a pattern, and a ruling what makes it a name.

<criterion id="BS4-AC2" cell_refs="BF-s-4"><invocation>python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json</invocation><expect>unknown_word_holes=0</expect></criterion>
`BS4-AC2` -- over every mapped root no hole of this class remains.

<expected_criteria>BS4-AC1,BS4-AC2</expected_criteria>

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
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md</decomp_doc> (round 5), cell `BF-s-4`.
<owned_cells>BF-s-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BS4-AC1, BS4-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-s-4.unknown-first-words.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BS4-AC1,BS4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the four lines before and now, whole; commits.

### AMENDMENT 1 (2.0.0_SA_COO~G, 2026-10-08) -- the landed rulings, the measured state, and what is left for this cell

The registry's lane landed the rulings: `infra/logic/registry/key_rulings.json`, `event_rules.json` and a NEW file
`name_rulings.json` @331e3fe609 (`4.0.0_SA_CRO`, msg 106696; accepted by `1.0.0_SA_CTO`, msg 106698). Read each file's `_about`
before you build. Measured by the issuer on the trunk after `BF-s-5` to `BF-s-8` merged
(`python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json`):
`roots_total=87 mapped=13 unmapped=74 completed=13 stopped=0 items=412 right=124 fix=228 not_asked=26 pattern=8 carded=0
refused=0 hole=26 carded_class_holes=8 source_bucket_holes=3 event_rule_holes=0 unknown_word_holes=3 other_holes=12`.
Run that command first and work from ITS lines, not from this summary.

**What is left for THIS cell, in `lib/opal_naming_rootcheck.py` (the order stays staged until `BF-s-1` is merged on this slot):**
1. **`name_rulings.json` has no reader.** It answers a name that is not a stored-file path: a bucket, a group, a secret (4 rows,
   6 lines of the run). Build the reader: a line whose (name, type) matches a row prints `FIX` and the row's `canonical`, or
   `NOT-ASKED` and the row's `none_owed` sentence. This is also what closes the three `source_bucket` lines
   (`opal-data-ycharts`, ruled `opal-data-irpt`): the registry answers a source-named bucket with a row, never a fill.
2. The stored-file prefixes among the unknown words (`bbg/`, `firms/`) are answered in `key_rulings.json`; where one still prints
   `HOLE` because its bucket was not read, that is `BF-s-2`'s (the key reader). Report it; do not force it.
3. A name the registry marks as a code pattern prints `PATTERN` with the registry's sentence: read `_about` of both files for
   how a pattern is marked; if neither file has such a mark, build nothing for it and say so.
4. `BS4-AC2` reads `unknown_word_holes=0`; add to your report the `source_bucket_holes` count, which your reader should also
   bring to 0.

### AMENDMENT 2 (2.0.0_SA_COO~G, 2026-10-08) -- the issuer's error: this order runs on slot ~2

The issuance cut this order to slot `~1` and the issuer then spawned it on slot `~2`, where the root check's file was free. The
lane gate read `<issued_to>` and refused the slot-`~2` worker's commit (row `LGIC_BLANKFIX-W2-S15`), correctly. The order is
re-pointed: `<issued_to>` and every deliverables path on this face now name `0.9.0_WK_LGIC_BLANKFIX~2`. Nothing else changes.

### AMENDMENT 3 (2.0.0_SA_COO~G, 2026-10-08) -- handed; the measured state; one more reader on the same file

`BF-s-1` and `BF-s-2` are merged (their orders stay open on criteria your build serves). Measured by the issuer on the trunk:
`python lib/opal_naming.py census --all-roots` reads `items=412 right=124 fix=237 not_asked=27 pattern=8 refused=0 hole=16
carded_class_holes=2 source_bucket_holes=3 event_rule_holes=0 unknown_word_holes=3 other_holes=8`. Run it first and work from its
lines.

Your build is AMENDMENT 1's items 1 to 4 (the reader for `name_rulings.json`), and one more in the same file:

5. **A ruled address with more than one open place.** Six `opal-assets` lines (`_quarantine/`) print `HOLE` with "a brace remains
   that no per-firm answer admits". The registry's lane gave the row a field for exactly this: `fills` on a `key_rulings.json`
   row (@3c76aa613b; read `_about.row_fields`): an object with one entry per open place, keyed by the place's name without
   braces, each value one sentence saying what fills the place and where the code gets it. Build: a key-ruling row whose
   `canonical` carries open places is admitted when `fills` has an entry for EVERY place in the canonical and no other; the line
   prints `FIX`, the form, and each place's sentence from `fills` (never from `evidence`). A canonical with an open place and no
   matching `fills` entry stays `HOLE`. The per-firm rows (`bucket_per`, `bucket_from`) are unchanged. The `lines` command's
   brace rule admits these lines the same way and refuses every other brace.
6. The DIFFERENCE CONTROL for item 5, on a registry the test writes to a temporary folder: the same two-place row is `FIX` with
   both `fills` entries and `HOLE` with one. The test `lib/tests/test_opal_naming_rootcheck.py` has a case from an earlier order
   asserting that a two-place canonical is `HOLE`: keep that assertion for a row WITHOUT `fills`, and say in your report what you
   changed in it.
7. Lines you are NOT expected to close: stored files whose bucket the code does not decide in its own file (`quarantine/`,
   `firms/`, `bronze/`, `bronze/eclipse/`): the registry's lane is deciding how those are keyed. If `BS4-AC2`
   (`unknown_word_holes=0`) fails ONLY because `firms/` or `bbg/` still waits on that, record the FAIL, leave the status pending
   and report each remaining line whole with its reason.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a real stored path printed as a pattern to clear a hole (only the registry's mark does it; the difference control); a word added to a vocabulary by the worker (no registry file is in the grant); BLIND: the same words on unmapped roots.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round4.md @095d99c984 (the CTO's enrichment list); decomposition round 5. Base dry-run at the cut: BS4-AC1 base PASS as expected (same test; extended by the cell); BS4-AC2 base FAIL as expected (ran: no such command).
