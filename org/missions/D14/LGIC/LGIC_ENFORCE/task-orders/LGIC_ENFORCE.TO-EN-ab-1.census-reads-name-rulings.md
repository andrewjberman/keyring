# TO LGIC_ENFORCE.TO-EN-ab-1 -- round 22 EN-ab-1: the census reads name_rulings.json; a ruled name reads RULED, never carded
<to_id>LGIC_ENFORCE.TO-EN-ab-1</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `EN-ab-1` (`decompositions/LGIC_ENFORCE_DECOMP.md` section 0w) | **outcome_ref:** FWD-5 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**Where the project stands.** LGIC_ENFORCE is CLOSED (7 of 7 outcomes REALIZED). This is one follow-up cell the CTO ruled after the
close (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_LGIC_NAME_RULINGS_READ_BY_CENSUS_NOT_GRADE_20261009.md`, row
`LGIC_ENFORCE-D1-S1`). It corrects a reading of FWD-5's census; no outcome changes.

**The instruments.** `python lib/opal_naming.py census [--live] [--repo] [--names FILE] [--not-judged FILE] [--report PATH]` judges
names with `grade()` in `census_judge()` (`lib/opal_naming.py`). A RAISE (a name `grade()` cannot read) stops the run with exit 3,
unless the name is CARDED in the `--not-judged` JSON list (`{name, plane, card}`; R-29). `infra/logic/registry/name_rulings.json`
holds 119 rows (`name`, `type`, `canonical` OR `none_owed`, `evidence`, `owner`): each answers a name the check could not answer.
`lib/opal_naming_rootcheck.py` already reads it: `NAME_RULINGS_FILE` and `load_name_rulings()` (:106-120), matched on (name, type).
Reuse that reader; write no second one. The registry is `4.0.0_SA_CRO`'s; nothing here edits it. Python 3.9 syntax, ASCII only,
no new dependency. The bar: `python -m pytest lib/tests -q -p no:cacheprovider` (196 passed, 1 skipped at the base) must not newly
fail. The check is `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r22/check_en_r22.py`
(read-only; read it before you build).

**Client-data bound (0.0.0_AB_MSTR msgs 2712, 2739, 2758, 2796).** Search ONLY inside paths you name (lib/, infra/logic/,
org/missions/D14/LGIC/), never the whole repo and never in history. Never open, search, copy or git show anything under
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/, any org/**/W73_S*_EVIDENCE.json, or any cottonwood manifest.

### THE CELL

`EN-ab-1`. The CTO's ruling, verbatim in substance: `grade()` stays the pure grammar and never reads `name_rulings.json`. The
CENSUS looks up each RAISE name in `name_rulings.json`; a name with a ruling row is reported as `RULED <rule id>`, citing that row,
neither carded nor counted as breaking the pattern. The census prints how many names are RULED beside the judged and carded totals.
A ruling row naming a name the census never sees is printed as STALE. Close when the three names (`calculated-group` IAM_GROUP,
`astn/kimi/api-key` SECRET, `restricted-prefix-get-put-list` IAM_POLICY) read RULED with their rule ids, and a name with no ruling
row still cards.

The ruling names the census as `lib/opal_lgctfm.py`; the census that judges and cards is `census()`/`census_judge()` in
`lib/opal_naming.py` (the issuer's reading, stated so it can be overruled; the ruling's point -- the census, not `grade()` -- is
unchanged).

**Build** in `lib/opal_naming.py` (the census only; `grade()` untouched) and its test `lib/tests/test_opal_naming.py`:
1. In `census_judge()`, when `grade()` RAISEs on an item, look the (name, type) up in `name_rulings.json` (via
   `opal_naming_rootcheck.load_name_rulings()`). A match prints `CENSUS RULED <plane> <type> <name> -- name_rulings.json#<row index>
   <canonical or none_owed>` and adds a row with verdict `RULED`; the run continues. No match: unchanged (card if carded, else STOP).
   The rule id is the row's 0-based index in the file's `name_rulings` list.
2. The census summary line (`CENSUS: COMPLETE ...`) and the report's denominators carry `ruled=<n>`.
3. After judging, for a `--live`/`--repo` run, print `CENSUS STALE name_rulings.json#<i> <type> <name>` for each ruling row whose
   (name, type) no item of the run carried, and their count. A `--names` run prints no STALE lines (it sees only its names).
4. Test arms: a ruled RAISE reads RULED with its index; an unruled RAISE still stops; `grade()` on a ruled name still raises.
5. `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/census-rulings.r22.result.md`: the check's output
   whole, and one `--live --repo` census run's RULED and STALE counts.

### ACCEPTANCE

<criterion id="AB1R22-AC1" cell_refs="EN-ab-1"><invocation>timeout 1500 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r22/check_en_r22.py ruled</invocation><expect>PASS-R22-RULED</expect></criterion>
`AB1R22-AC1` -- the three ruled names read `CENSUS RULED ... name_rulings.json#<their index>`, the unruled name cards, `ruled=3`
is printed, and without a card the unruled name still STOPS the run.

<expected_criteria>AB1R22-AC1</expected_criteria>

Run every invocation from the root of your worktree. Each invocation's LAST printed line is the line the expectation is matched
against. Commit your artifacts first, then run the criteria against the committed bytes.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file. Nothing in this prose grants a path.
- **No edit outside the grant.** `grade()` is not changed; no registry edit (`infra/logic/registry/` is read-only); no AWS write;
  `org/mcp/naming-place.enforce` and the check file are never edited.
- **Refusal clause.** If the criterion cannot be met as written, stop on it, write the reason in your report and a surprise row (id
  `LGIC_ENFORCE-D1-W1-S<k>`, `<k>` one above the highest in the channel at your write time; `surfaced_at` = `date -u +%FT%TZ` at
  filing) in `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` by textual splice, and never
  weaken the check or its expected value.

<paths>
lib/opal_naming.py
lib/tests/test_opal_naming.py
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/census-rulings.r22.result.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-ab-1.census-reads-name-rulings.proof_of_spec.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-ab-1.census-reads-name-rulings.md
</paths>

The block is your WRITE grant. You read and never edit anything outside it.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.22, round-22 cell `EN-ab-1` (section 0w).
<owned_cells>EN-ab-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AB1R22-AC1. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-ab-1.census-reads-name-rulings.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AB1R22-AC1 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-ab-1.census-reads-name-rulings.md`
BEFORE the `complete` flip. Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.
</proof_of_spec>

**REPORT:** the check's lines whole; the `--live --repo` run's ruled and stale counts; your commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no grant; the census only reads the live plane through comp-find.
comp-adversary: RUN -- the cheapest pass puts the lookup in grade() (refused by the ruling; the order's test arm asserts grade() still raises on a ruled name), or treats every RAISE as RULED (arm B requires an unruled name to still stop the run without a card). A hand-typed index: the check reads each row's index from the file. BLIND: the check uses a --names run; STALE reporting over the live plane is read from the result file at the drain, not graded by the arm.
lane: the <paths> block IS the grant (worker RULING 1); nothing in the prose grants a path.
</preflight>

Source: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_LGIC_NAME_RULINGS_READ_BY_CENSUS_NOT_GRADE_20261009.md`; seated by
`0.0.0_AB_MSTR~DELL1` msg 2948. Base dry-run at the cut, by the issuer: AB1R22-AC1 base: FAIL as expected (arm A rc=3, the ruled name
`calculated-group` RAISEs and stops the run: `R1.f: 'calculated' is in no vocabulary`).
