# TO LGIC_BLANKFIX.TO-BF-q-2 -- round 4 BF-q-2: a key whose bucket is chosen at run time -- read in the shape the registry gives it

<to_id>LGIC_BLANKFIX.TO-BF-q-2</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-q-2` (`decompositions/LGIC_BLANKFIX_DECOMP.round4.md`) | **outcome_ref:** FWD-2 |
**depends_on:** BF-q-1 merged; the registry's shape for a run-time bucket landed by 4.0.0_SA_CRO; handed by AMENDMENT 1

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

`BF-q-2`. The second root's run has two `HOLE` lines (row `LGIC_BLANKFIX-W2-S9`): the stored-file prefixes
`investor-reporting/directory` (`infra/aws/lambda/investor-reporting/directory/handler.py:53`) and
`investor-reporting/directory/_refresh` (`.../refresh.py:71`). Their bucket is not a literal: the code takes it from an
environment variable that holds one bucket per firm (`IRPT_DIRECTORY_BUCKET_MAP`), so a ruling keyed on ONE (bucket, key) cannot
be written for them.

**THE SHAPE.** `4.0.0_SA_CRO` decides how a key whose bucket is chosen at run time is written in the registry. The file, the
field names and the commit are named in AMENDMENT 1, written into this order before it is handed to you. If this order reaches
you with no AMENDMENT 1, stop and report.

**Build** in `lib/opal_naming_keyfill.py` and `lib/opal_naming_rootcheck.py`, exactly to the shape AMENDMENT 1 names: the reader
recognises a stored file whose bucket comes from a per-firm run-time choice (say in `bucket_basis` what in the source file shows
it), matches it to its registry answer by the rule the shape gives, and prints the answer (a whole address form, or "no name is
owed" with the reason) in place of the `HOLE`. A stored file with a run-time bucket and NO registry answer keeps a `HOLE` whose
reason says the bucket is chosen at run time and names the variable. Extend both modules' tests with the DIFFERENCE CONTROL (the
same key with and without a registry answer). Both tests still print `ok=True`.

### ACCEPTANCE

<criterion id="BQ2-AC1" cell_refs="BF-q-2"><invocation>python lib/tests/test_opal_naming_keyfill.py</invocation><expect>KEYFILL-TEST ok=True</expect></criterion>
`BQ2-AC1` -- a run-time bucket is recognised, and the registry's answer is what fills the line.

<criterion id="BQ2-AC2" cell_refs="BF-q-2"><invocation>python lib/opal_naming_rootcheck.py infra/aws/terraform/investor-reporting/directory --map infra/logic/registry/root_map.json --report-only</invocation><expect>hole=0</expect></criterion>
`BQ2-AC2` -- the second root prints no hole.

<expected_criteria>BQ2-AC1,BQ2-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_keyfill.py
lib/tests/test_opal_naming_keyfill.py
lib/opal_naming_rootcheck.py
lib/tests/test_opal_naming_rootcheck.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the two saved traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round3.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round4.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round4.md</decomp_doc> (round 4), cell `BF-q-2`.
<owned_cells>BF-q-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BQ2-AC1, BQ2-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-q-2.runtime-bucket-keys.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BQ2-AC1,BQ2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the two lines before and now, whole; what in each source file shows the run-time bucket; commits.

### AMENDMENT 1 (2.0.0_SA_COO~G, 2026-10-07) -- the landed shape (the order stays staged until its queue reaches it)

`4.0.0_SA_CRO` landed the shape in `infra/logic/registry/key_rulings.json` @cab8510cc3 (msg 106571). Read the file's
`_about.per_firm` for the exact wording; as that seat states it:
- A per-firm row carries `bucket_per` (the value `firm`) and `bucket_from` (the name of the variable the code reads the bucket
  from) IN PLACE OF `bucket`. Its `canonical` carries `{scope}`: the firm is not one value, so the correct address is a form
  with the firm's place marked.
- **The match:** the row's `key` equals the item's key, AND the file that declares the key names the `bucket_from` variable.
- Two rows exist, both for `IRPT_DIRECTORY_BUCKET_MAP`: canonical `irpt/{scope}/platinum/directory/` and
  `irpt/{scope}/state/directory_refresh/`.

What the line prints for a matched per-firm row: `FIX`, the detail the canonical FORM with `{scope}` kept and a plain sentence
that the firm's place is filled per firm from the variable (name it). This is the ONE case where a `FIX` line carries a brace:
the check's own no-brace rule and the `lines` command must admit exactly `{scope}` on a line whose row is per-firm and refuse
every other brace as today. Add that as a DIFFERENCE CONTROL in the root-check test: a per-firm row's `{scope}` is admitted, and
the same brace on a line with no per-firm row is still refused.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a bucket guessed for a run-time choice (the face forbids it: the registry's answer or a HOLE naming the variable); a per-firm key filled with one firm (the shape decides; the root's map entry carries fills and gives no firm); BLIND: the variable's live value on the deployed function.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round3.md @f0e6411e53 (the CTO's enrichment list); decomposition round 4. Base dry-run at the cut: BQ2-AC1 base PASS as expected (ran: KEYFILL-TEST ok=True cases=28; extended by the cell); BQ2-AC2 base FAIL as expected (ran: hole=2).
