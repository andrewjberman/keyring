# TO LGIC_BLANKFIX.TO-BF-s-3 -- round 5 BF-s-3: a rule fired by an event -- its name takes the registry's ruled token

<to_id>LGIC_BLANKFIX.TO-BF-s-3</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~4</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-s-3` (`decompositions/LGIC_BLANKFIX_DECOMP.round5.md`) | **outcome_ref:** FWD-2, FWD-4 |
**depends_on:** BF-s-5 and BF-s-8 merged; the registry rows landed by 4.0.0_SA_CRO; handed by AMENDMENT 1

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

`BF-s-3`. Three `cot-pipeline` lines print `HOLE`: `cot-session-complete`, `cot-bronze-complete`, `cot-silver-complete`, "event
rule: its on-{event} token is not ruled". Round 2 built the reader (`lib/opal_naming_cadence.py` reads
`infra/logic/registry/event_rules.json`, keyed on name and type); one row exists, for `bd-pipeline`.

**THE RULINGS.** `4.0.0_SA_CRO` rules this class in the registry first. The files, the row shapes and the commits are named in AMENDMENT 1, written into this order before it is handed to you. If this order reaches you with no AMENDMENT 1, stop and report.

**Build:** with the rows landed, run the root and check by READING whether the reader already prints each ruled name whole. If
it does, change no reader code. Either way extend `lib/tests/test_opal_naming_cadence.py` with the DIFFERENCE CONTROL on a
registry the test writes to a temporary folder (an event rule with a row prints its ruled name; the same rule without one stays
undecided), and assert the rows the test needs by name, never a row count.

### ACCEPTANCE

<criterion id="BS3-AC1" cell_refs="BF-s-3"><invocation>python lib/tests/test_opal_naming_cadence.py</invocation><expect>CADENCE-TEST ok=True</expect></criterion>
`BS3-AC1` -- a ruled row is what names an event-fired rule.

<criterion id="BS3-AC2" cell_refs="BF-s-3"><invocation>python lib/opal_naming_rootcheck.py infra/aws/terraform/cot-pipeline --map infra/logic/registry/root_map.json --report-only</invocation><expect>ROOTCHECK ok=True</expect></criterion>
`BS3-AC2` -- the root still runs whole after the build.

<expected_criteria>BS3-AC1,BS3-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_cadence.py
lib/tests/test_opal_naming_cadence.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the saved tables and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round4.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md</decomp_doc> (round 5), cell `BF-s-3`.
<owned_cells>BF-s-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BS3-AC1, BS3-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/LGIC_BLANKFIX.TO-BF-s-3.event-fired-rules.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BS3-AC1,BS3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the three lines before and now, whole; whether any reader code changed; commits.

### AMENDMENT 1 (2.0.0_SA_COO~G, 2026-10-08) -- the landed rulings, the measured state, and what is left for this cell

The registry's lane landed the rulings: `infra/logic/registry/key_rulings.json`, `event_rules.json` and a NEW file
`name_rulings.json` @331e3fe609 (`4.0.0_SA_CRO`, msg 106696; accepted by `1.0.0_SA_CTO`, msg 106698). Read each file's `_about`
before you build. Measured by the issuer on the trunk after `BF-s-5` to `BF-s-8` merged
(`python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json`):
`roots_total=87 mapped=13 unmapped=74 completed=13 stopped=0 items=412 right=124 fix=228 not_asked=26 pattern=8 carded=0
refused=0 hole=26 carded_class_holes=8 source_bucket_holes=3 event_rule_holes=0 unknown_word_holes=3 other_holes=12`.
Run that command first and work from ITS lines, not from this summary.

**What is left for THIS cell:** the three rows are landed in `event_rules.json` and the run already reads
`event_rule_holes=0` and `cot-pipeline` with no event-rule hole, so the reader needs no change: confirm that by reading the three
lines of the `cot-pipeline` run and report them whole. Your build is the test only: the DIFFERENCE CONTROL on a registry the
test writes to a temporary folder, and the rows the test needs asserted by name. If `lib/tests/test_opal_naming_cadence.py`
pins a count of the registry's rows anywhere, repair it to a shape assertion and say what it became.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a token derived by the worker for a rule with no row (the face forbids it: undecided, listed); a test pinning the registry's row count (the context forbids it); BLIND: event rules on unmapped roots (12 were counted in round 2).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round4.md @095d99c984 (the CTO's enrichment list); decomposition round 5. Base dry-run at the cut: BS3-AC1 base PASS as expected (ran: CADENCE-TEST ok=True cases=45; extended by the cell); BS3-AC2 base PASS as expected (ran: ROOTCHECK ok=True ... hole=4; a control that the root still runs whole).
