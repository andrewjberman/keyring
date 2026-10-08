# TO LGIC_BLANKFIX.TO-BF-u-3 -- round 6 BF-u-3: a key ruling survives a file move -- matched on the key, the path a hint, a stale hint printed

<to_id>LGIC_BLANKFIX.TO-BF-u-3</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~4</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete -- proof-of-spec VALID (rc=0)</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-u-3` (`decompositions/LGIC_BLANKFIX_DECOMP.round6.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --all-roots` (the same as `python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json`)
runs every Terraform root the root map covers and prints the denominator of roots first. At the round-5 close it read
`roots_total=87 mapped=13 unmapped=74 completed=13 stopped=0 items=412 right=124 fix=248 not_asked=32 pattern=8 carded=0 refused=0
hole=0`; the whole output is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/ALL_ROOTS_round5_second_seat.txt`. One line per name: `KIND type current -> detail  [where]`, kinds `RIGHT`, `FIX`,
`NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`. Each unmapped root is printed `UNMAPPED <root> names=N`. The CTO's reading is
`org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round5.md` -- read it first.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`, the `census` command), `opal_naming_scope.py` (the roots and their
names), `opal_naming_rootmap.py` (`load_map`, `resolve`), `opal_naming_cadence.py`, `opal_naming_keyfill.py` (`fill_keys`,
`bucket_of`), `opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `check_root`, `_ruling_of`, the `lines`, `keys` and
`all` commands). The registry is `infra/logic/registry/` (`root_map.json`, `key_rulings.json`, `name_rulings.json`,
`event_rules.json`, `legacy_addresses.json`, `resources.json`, `systems.json`); only `4.0.0_SA_CRO` writes it. Read the modules
your cell touches or calls before you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code
and output; no new dependency; no AWS call and no network call. The bar: `python -m pytest lib/tests -q -p no:cacheprovider`
passes whole at the base (194 passed), and every `lib/tests/test_opal_naming_*.py` script prints `ok=True` at the base EXCEPT
`test_opal_naming_keyfill.py`, which is red (row `LGIC_BLANKFIX-S7`; cell `BF-u-4` repairs it). None may newly fail after your
build. A test you write asserts relations and the rows it needs by name, never a typed total of repository names, roots or
registry rows: those move every day, and the registry's lane is adding map entries during this round.

### THE CELL

`BF-u-3` (item E2; row `LGIC_BLANKFIX-S6`). A `key_rulings.json` row with `declared_in` matches only when the file that declares
the key is one of the listed repository paths (`_ruling_of` in `lib/opal_naming_rootcheck.py`). When IRPT_BCKEND moved
`backfill_covered_account_ids.py` into `export/tools/`, the `firms/` row stopped matching and the line printed as a hole until the
registry's lane retyped the path. The CTO: "Match on the key itself, with the path as a hint."

**Build** in `lib/opal_naming_rootcheck.py`:
1. The candidates for an item are the `declared_in` rows whose key equals the item's key. One candidate: it matches, whatever the
   path. Several: the one whose `declared_in` holds the item's file; else the one whose `declared_in` holds a file of the same base
   name; else none, and the line says "several key rulings carry this key and no hint names this file", naming the rows. The
   per-firm rows (`bucket_per`, `bucket_from`) and the (bucket, key) match keep their present order and meaning.
2. A STALE HINT is a match where the item's file is not in the row's `declared_in`. The line still prints its answer, and adds
   "the ruling's declared_in names <path>; the key is declared in <file>". The `all` command counts them: one field `stale_hints=N`
   added at the END of its `ALL-ROOTS` last line (no other field moves), and one `STALE-HINT` line per case before it.
3. The DIFFERENCE CONTROL in the test, on a registry the test writes to a temporary folder: one row, file moved -> matched with the
   stale hint; two rows with the same key, file moved, neither hint matching -> no match and the reason; two rows, one hint matching
   -> that row, no stale hint.

### AMENDMENT 1 (2.0.0_SA_COO~G, 2026-10-08) -- BU3-AC2's expectation corrected: the issuer's premise was wrong

The face said the estate run would count no stale hint "since every declared_in path exists". That is not the test item 2
defines. Item 2 counts a match where the item's file is not in the row's `declared_in`, and the slot's build found one on the
trunk: `bd-pipeline` `bronze/` in `infra/aws/lambda/bd-pipeline/bd-49f-freshness-probe/lambda_function.py:74` matches a row whose
`declared_in` names `infra/aws/lambda/opal-assets/opal-assets-ingest-mirror/lambda_function.py` (row `LGIC_BLANKFIX-W4-S2`). The
line's answer is unchanged; the hint is stale. That is a true report, and the rule that produced it stays as written: exempting a
match the item's own bucket confirms would hide exactly the drift this cell exists to show.

`BU3-AC2` therefore expects the field present at the end of the last line, whatever its count: `stale_hints=[0-9]+`. Report the
count and every `STALE-HINT` line. The stale row is the registry lane's to correct (`4.0.0_SA_CRO`, told by the issuer); its
correction is not this cell's. Nothing else in this order changes.

### AMENDMENT 2 (2.0.0_SA_COO~G, 2026-10-08) -- item 1 corrected: a candidate must agree on the bucket; no answer may move

Item 1 as the issuer wrote it took as candidates "the `declared_in` rows whose key equals the item's key", bucket unread. On the
trunk that re-paired `bd-49f-freshness-probe`'s `bronze/` (the probe reads `opal-data-bd`, lines 57 and 455; `4.0.0_SA_CRO` msg
107136) to the `opal-data-inf` row: the line now prints `-> orion/inflection/bronze/` where round 5 printed
`-> blackdiamond/49financial/bronze/` (`deliverables/0.9.0_WK_LGIC_BLANKFIX~2/all_roots_round5/bd-pipeline.txt:109`). The stale hint
AMENDMENT 1 called a true report was this mis-pairing. The defect is the order's, not the build's.

**Item 1 now reads:** the candidates for an item are the `declared_in` rows whose key equals the item's key AND whose bucket equals
the item's bucket wherever the item's bucket is known (`bucket_of`); a row of another bucket is never a candidate. Where the item's
bucket is not known, the key alone selects, as before. The rest of items 1 to 3 stands. Add to the DIFFERENCE CONTROL: two rows
with the same key and different buckets, the item's bucket known -> only its bucket's row is a candidate; the other bucket's row
alone -> no match.

`4.0.0_SA_CRO` has added an `opal-data-bd` `bronze/` row declared in the probe at line 74 (msg 107136); merge `CLOUD` into your
branch before you prove. **New criterion `BU3-AC3`:** the repeat check (merged from `BF-u-5`) reads `repeat=identical`, so no line
of a mapped root changes its answer from the round-5 saved runs. `BU3-AC2` keeps AMENDMENT 1's expectation; report the count and
every `STALE-HINT` line, each checked by hand against the bucket its file reads.

### ACCEPTANCE

<criterion id="BU3-AC1" cell_refs="BF-u-3"><invocation>python lib/tests/test_opal_naming_rootcheck.py</invocation><expect>ROOTCHECK-TEST ok=True</expect></criterion>
`BU3-AC1` -- a ruling matches on its key, and the path decides only between rulings of the same key.

<criterion id="BU3-AC2" cell_refs="BF-u-3"><invocation>python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json</invocation><expect>stale_hints=[0-9]+</expect></criterion>
`BU3-AC2` -- the estate run counts stale hints and prints the count at the end of its last line (AMENDMENT 1: the count is reported, not required to be 0).

<criterion id="BU3-AC3" cell_refs="BF-u-3"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_all_roots_round5.py</invocation><expect>repeat=identical</expect></criterion>
`BU3-AC3` -- no line of a mapped root changes its answer from the round-5 saved runs (AMENDMENT 2).

<expected_criteria>BU3-AC1,BU3-AC2,BU3-AC3</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_rootcheck.py
lib/tests/test_opal_naming_rootcheck.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round5.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round6.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round6.md</decomp_doc> (round 6), cell `BF-u-3`.
<owned_cells>BF-u-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BU3-AC1, BU3-AC2, BU3-AC3. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/LGIC_BLANKFIX.TO-BF-u-3.ruling-survives-move.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BU3-AC1,BU3-AC2,BU3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the before-and-after of the all command's last line; every STALE-HINT line; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a key matched to a ruling written for another file of the same key (several candidates fall back only to a same-base-name hint, else no match with the reason); a moved file silently matched with nothing printed (the stale hint is printed and counted); BLIND: a key whose spelling changes when its file moves.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round5.md @34ba4c1c90, amended @cbdf36254c (the CTO's enrichment list E1 to E6); decomposition round 6. Base dry-run at the cut: BU3-AC1 base PASS as expected (ran: ROOTCHECK-TEST ok=True cases=194; extended by the cell); BU3-AC2 base FAIL as expected (ran: ALL-ROOTS ok=True ... other_holes=0; the last line carries no stale_hints field).
