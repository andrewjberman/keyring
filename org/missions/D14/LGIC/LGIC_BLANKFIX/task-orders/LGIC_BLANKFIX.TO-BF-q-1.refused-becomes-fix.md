# TO LGIC_BLANKFIX.TO-BF-q-1 -- round 4 BF-q-1: the two refused lines become fixes -- a registry ruling outranks the path-word refusal

<to_id>LGIC_BLANKFIX.TO-BF-q-1</to_id>
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

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-q-1` (`decompositions/LGIC_BLANKFIX_DECOMP.round4.md`) | **outcome_ref:** FWD-1 |
**depends_on:** BF-q-3 merged; the key ruling for (opal-data-bd, code/bronze/cot_bronze_ingest.py) landed by 4.0.0_SA_CRO; handed by AMENDMENT 1

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

`BF-q-1`. Two lines of the thread print `REFUSED`: `code/bronze/cot_bronze_ingest.py`, named in
`infra/aws/lambda/bd-pipeline/bd-49f-fees-runner/lambda_function.py:43` and `bd-49f-runner/lambda_function.py:59`, "a file named for
cottonwood (cot) is kept in this firm's bucket opal-data-bd ... ask the owner of the code". `1.0.0_SA_CTO` measured and ruled
(`org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round3.md`): the same bytes sit in both firms' buckets; it is one ingest script copied into each
firm's bucket under a firm-named file. Nothing needs asking: the file is owed a name with no firm in it, and the line is a `FIX`.

**THE RULING ROW.** `4.0.0_SA_CRO` lands one row in `infra/logic/registry/key_rulings.json` for
(`opal-data-bd`, `code/bronze/cot_bronze_ingest.py`) with its whole correct address. Its commit is named in AMENDMENT 1, written
into this order before it is handed to you. If this order reaches you with no AMENDMENT 1, stop and report.

**Build** in `lib/opal_naming_rootcheck.py`:
1. A stored file that matches a key-ruling row on (bucket, key) takes the row's answer BEFORE the cross-firm refusal is
   considered: with `canonical`, `FIX` and the whole address. The check makes no AWS call: the ruling is how the registry
   says the two firms' copies are one script.
2. The refusal stays for a stored file with NO ruling row: its line is unchanged.
3. Extend `lib/tests/test_opal_naming_rootcheck.py`: the DIFFERENCE CONTROL: the same Cottonwood-named key in the 49 Financial
   bucket prints `FIX` with a ruling row and `REFUSED` without one; a key whose BUCKET is another firm's still prints
   `REFUSED` when no row matches. `ROOTCHECK-TEST ok=True` still.

### ACCEPTANCE

<criterion id="BQ1-AC1" cell_refs="BF-q-1"><invocation>python lib/tests/test_opal_naming_rootcheck.py</invocation><expect>ROOTCHECK-TEST ok=True</expect></criterion>
`BQ1-AC1` -- a ruling row is what turns the refusal into a fix, and a key with no row is still refused.

<criterion id="BQ1-AC2" cell_refs="BF-q-1"><invocation>python lib/opal_naming_rootcheck.py infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json --report-only</invocation><expect>refused=0 hole=0</expect></criterion>
`BQ1-AC2` -- the real root prints no refused line and no hole.

<expected_criteria>BQ1-AC1,BQ1-AC2</expected_criteria>

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

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the two saved traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round3.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round4.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round4.md</decomp_doc> (round 4), cell `BF-q-1`.
<owned_cells>BF-q-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BQ1-AC1, BQ1-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-q-1.refused-becomes-fix.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BQ1-AC1,BQ1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the two lines before and now, whole; commits.

### AMENDMENT 1 (2.0.0_SA_COO~G, 2026-10-07) -- the ruling is landed and the reader already honours it; the cell is a test repair and a control

`4.0.0_SA_CRO` landed the row: `infra/logic/registry/key_rulings.json` @cab8510cc3, (`opal-data-bd`,
`code/bronze/cot_bronze_ingest.py`) -> `blackdiamond/49financial/code/bronze/bronze_ingest.py` (msg 106571). Measured by the issuer
on the trunk with that row: the two lines ALREADY print `FIX ... -> blackdiamond/49financial/code/bronze/bronze_ingest.py`, and
the run reads `items=140 right=9 fix=116 not_asked=12 pattern=3 carded=0 refused=0 hole=0`. Round 3's reader matches a key ruling
before it considers the refusal, so step 1 of the cell is already true: check it by reading the code, and change the reader only
if the reading shows a path where the refusal is considered first.

So `BQ1-AC2` is a CONTROL here (it passes before you build and must still pass after). What you BUILD is in the test:
1. **Repair two assertions that are red on the trunk.** `python lib/tests/test_opal_naming_rootcheck.py` prints two `FAIL` lines
   ("loads four rows", "one canonical row and three none_owed rows") and `ok=False`: they compare against an exact count of the
   registry's rows, which is now seven. Make them hold on a registry that grows: assert the SHAPE (every row has a key; each
   carries exactly one of `canonical` or `none_owed`; a row has `bucket`, or `bucket_per` and `bucket_from`; the rows this test
   needs by name are present) and no typed total. Do not delete them. Say in your report what each became.
2. **Add the DIFFERENCE CONTROL of step 3 of the cell**, on a small registry the test writes to a temporary folder, never the
   real file: the same Cottonwood-named key in the 49 Financial bucket prints `FIX` with a ruling row and `REFUSED` without
   one; a key whose BUCKET is another firm's prints `REFUSED` when no row matches.
3. Leave the per-firm rows (`bucket_per`, `bucket_from`) unread by the reader: another order of this round builds that.
`BQ1-AC1` is the build criterion: it FAILS at the base (`ROOTCHECK-TEST ok=False`) and must pass.

**A correction to this order's record face:** its base dry-run line says `BQ1-AC1` passed at the base with 113 cases and `BQ1-AC2`
failed with `refused=2`. Neither was re-run at the cut; both were carried from an earlier run, and both were already wrong at
the cut because the registry row sat uncommitted in the shared tree. Measured after the cut: `BQ1-AC1` FAIL (`ok=False`),
`BQ1-AC2` PASS (`refused=0 hole=0`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- the refusal removed for every Cottonwood-named key, ruled or not (the difference control keeps REFUSED where no row matches); a row of another bucket matched (the match is on bucket and key); BLIND: whether a third bucket holds a copy -- not measured by anyone.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round3.md @f0e6411e53 (the CTO's enrichment list); decomposition round 4. Base dry-run at the cut: BQ1-AC1 base PASS as expected (ran: ROOTCHECK-TEST ok=True cases=113; extended by the cell); BQ1-AC2 base FAIL as expected (ran: refused=2 hole=0).
