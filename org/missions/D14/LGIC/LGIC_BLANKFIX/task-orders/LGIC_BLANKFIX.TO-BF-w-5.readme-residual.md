# TO LGIC_BLANKFIX.TO-BF-w-5 -- round 8 BF-w-5: the README states no typed counts or timings, points the reader at the live last line, and is linked from the root README and the checklist

<to_id>LGIC_BLANKFIX.TO-BF-w-5</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~5</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-08</issued_date>
<status>in_progress</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-w-5` (`decompositions/LGIC_BLANKFIX_DECOMP.round8.md`) | **outcome_ref:** FWD-5 (hold) |
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

`BF-w-5` (item E5). FWD-5 is REALIZED (round 7). Its residual, from the CVO's grade: `infra/logic/README.md` "Run the naming check"
states counts and timings the map has overtaken (for example "about 15 seconds", "13 of 87 roots"), and no root document points to it
(the fresh seat found it only through CLAUDE.md rule 30's pointer). The CTO: "have it print the live command's last line instead of
typed numbers, and link it from the onboarding checklist."

**Build:**
1. `infra/logic/README.md`, section "Run the naming check": every sentence that states a count of roots, names or holes, or a run
   time, is replaced by an instruction to read that figure from the live run's last line (name the field). The field-by-field table
   stays. Change nothing outside that section.
2. The root `README.md`: one line, where a newcomer looks for how to run checks, pointing to `infra/logic/README.md` "Run the naming
   check". `infra/logic/10_ONBOARDING_CHECKLIST.md` STEP 13 keeps (or gains) its link to that section. Change nothing else in either.
3. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~5/check_readme_residual.py`: it counts, in the README section, sentences carrying a typed count or timing
   (a number followed by `of`, `roots`, `names`, `holes`, `seconds` or `s`), checks the root README and STEP 13 each link the section,
   and prints `README-RESIDUAL ok=True typed_counts=0 root_link=1 checklist_link=1`.

### ACCEPTANCE

<criterion id="BW5-AC1" cell_refs="BF-w-5"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~5/check_readme_residual.py</invocation><expect>README-RESIDUAL ok=True</expect></criterion>
`BW5-AC1` -- the README section types no count or timing, and both the root README and STEP 13 link it.

<expected_criteria>BW5-AC1</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- `infra/logic/` is `4.0.0_SA_CRO`'s lane for the registry; your grant here is the documents named in the block, nothing under `infra/logic/registry/`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W5-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
infra/logic/README.md
README.md
infra/logic/10_ONBOARDING_CHECKLIST.md
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round7.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round8.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round8.md</decomp_doc> (round 8), cell `BF-w-5`.
<owned_cells>BF-w-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BW5-AC1. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~5/LGIC_BLANKFIX.TO-BF-w-5.readme-residual.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BW5-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; each sentence replaced, before and after; the root README line; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a number moved into a table so the sentence check passes (the field table may name fields, never typed totals); a rewrite of the root README beyond the one line; BLIND: whether a newcomer now finds it from the root -- the next fresh seat's reading.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round7.md @ec6f56562b (the CTO's enrichment list E1 to E5); decomposition round 8. Base dry-run at the cut: BW5-AC1 base FAIL as expected (file absent; the section states 'about 15 seconds' and '13 of 87'; the root README links infra/logic 0 times).
