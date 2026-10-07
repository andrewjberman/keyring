# TO LGIC_BLANKFIX.TO-BF-e-3 -- round 2 BF-e-3: a stored file's line carries its bucket -- a match is on bucket and key, never the key alone

<to_id>LGIC_BLANKFIX.TO-BF-e-3</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-e-3` (`decompositions/LGIC_BLANKFIX_DECOMP.round2.md`) | **outcome_ref:** FWD-1, FWD-4 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**Where the project stands.** Round 1 built one command: `python lib/opal_naming.py census --root infra/aws/terraform/bd-pipeline`
prints one line per name of that root, each of kind `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED` or `HOLE`, and exits 1 while any
line is a `HOLE`. Its last run is saved at `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round1_bd-pipeline.txt`: 140 names, 10 right, 101 fix,
6 not asked, 1 pattern, 6 carded, 16 holes. The modules, all under `lib/`: `opal_naming.py` (`grade(name, type) -> (verdict,
canonical)`, `census_repo()`, `census_tf_names()`), `opal_naming_scope.py` (`root_items(root)`), `opal_naming_rootmap.py`
(`load_map`, `resolve`; the landed map is `infra/logic/registry/root_map.json`), `opal_naming_cadence.py` (`word_for`, `cadences`),
`opal_naming_keyfill.py` (`fill_keys`), `opal_naming_rootcheck.py` (`decide`, `check_root`). Read the ones your cell touches or
calls before you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new
dependency. The bar for the library's own suite: `python -m pytest lib/tests/test_opal_naming.py -q -p no:cacheprovider` fails six
named tests at the base (see `lib/tests/test_opal_naming_fourth_verdict.py` for the list); no test that passes at the base may fail.

### THE CELL

`BF-e-3`. Three defects of round 1's key classes. (a) Two lines are `HOLE`: `code/bronze/cot_bronze_ingest.py`, a Cottonwood file
named in two Lambdas of a 49 Financial root (`bd-49f-fees-runner/lambda_function.py:43`, `bd-49f-runner/lambda_function.py:59`).
(b) `silver/prices/canonical_prices.parquet` at `bd-price-update/lambda_function.py:441` was classed `LEGACY` on the registry row
`cottonwood-silver-canonical-prices`, whose bucket is `opal-data-cot`, though the Lambda's bucket is `opal-data-bd` (49 Financial):
the match was on the key path alone (row `LGIC_BLANKFIX-W3-S2`). (c) A census item carries no bucket at all.

**Build** in `lib/opal_naming_keyfill.py`:
1. `bucket_of(item) -> (bucket or None, basis)`: the bucket the key at `item["where"]` is used with, read from the SAME source
   file: a bucket-name literal (`opal_naming._BUCKET_NAME_RE`, and a name that is a bucket in the registry or starts `opal-data-`)
   in the same call or assignment as the key, else the file's single bucket literal or single bucket constant when the file has
   exactly one. When the file has several candidates and the key's own statement does not pick one, return `None` with a basis
   listing the candidates. Never guess from the folder name.
2. `fill_keys(items, root_entry)` rows gain `bucket` and `bucket_basis`. `LEGACY` now requires the legacy entry's `bucket` to equal
   the item's bucket; a key whose path matches a legacy entry of a DIFFERENT bucket is NOT legacy and its basis says so. A key
   whose bucket belongs to a different firm than the root entry's scope (read the firm of a bucket from the registry, as
   `opal_naming._buckets_of_firms` does) is class `REFUSED-CROSS-FIRM` with both firms named in the basis: it is never filled
   with this root's firm. Classes are now tested in this order: `PATTERN`, `LEGACY`, `REFUSED-CROSS-FIRM`, `ADDRESS`,
   `UNDECIDED`. Keep the existing path-token conflict check as a second route into `REFUSED-CROSS-FIRM` (it replaces that
   `UNDECIDED` case).
3. `python lib/opal_naming_keyfill.py dir ...` keeps its arguments; its last line becomes
   `KEYFILL-DIR ok=True dir=... rows=N address=N legacy=N pattern=N refused=N undecided=N raising=N with_bucket=N`, the five
   classes summing to `rows`.

**Extend** `lib/tests/test_opal_naming_keyfill.py`: the DIFFERENCE CONTROL: the same key path is `LEGACY` when its bucket equals
the legacy entry's bucket and is not `LEGACY` when its bucket differs; a key in another firm's bucket is `REFUSED-CROSS-FIRM`;
`bucket_of` on three small source texts (one literal in the call; one file-level constant; two candidates and no pick). Last line
`KEYFILL-TEST ok=True cases=N`.

`REFUSED-CROSS-FIRM` is a new class value: it is the registry's cross-firm separation stated on a line, not a new rule. Whether
the Cottonwood file under this root is a real cross-firm reference is NOT yours to decide or fix: print it and report it.

### ACCEPTANCE

<criterion id="BE3-AC1" cell_refs="BF-e-3"><invocation>python lib/tests/test_opal_naming_keyfill.py</invocation><expect>KEYFILL-TEST ok=True</expect></criterion>
`BE3-AC1` -- the bucket is what decides a legacy match, and another firm's bucket is refused, not filled.

<criterion id="BE3-AC2" cell_refs="BF-e-3"><invocation>python lib/opal_naming_keyfill.py dir infra/aws/lambda/bd-pipeline --root bd-pipeline --map infra/logic/registry/root_map.json</invocation><expect>with_bucket=</expect></criterion>
`BE3-AC2` -- the real source folder: every blank key classed, each with its bucket or the reason none was read.

<expected_criteria>BE3-AC1,BE3-AC2</expected_criteria>

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

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round1_bd-pipeline.txt`, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round1.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round2.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round2.md</decomp_doc> (round 2), cell `BF-e-3`.
<owned_cells>BF-e-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BE3-AC1, BE3-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/LGIC_BLANKFIX.TO-BF-e-3.key-carries-bucket.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BE3-AC1,BE3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the root's rows by class with each row's bucket and basis; what became of the three named keys; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed; the cell reads schedule text.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a 49 Financial key classed legacy on a Cottonwood row (the bucket now gates LEGACY; the difference control is one path under two buckets); a Cottonwood key filled with the 49 Financial firm (REFUSED-CROSS-FIRM is tested before ADDRESS; cross-firm law); a bucket guessed from the folder name (the face forbids it; None with candidates listed); BLIND: a bucket passed in at run time through an environment variable -- reported as no bucket read.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round1.md @e40eddd4e8 (the CTO's enrichment list); decomposition round 2. Base dry-run at the cut: BE3-AC1 base PASS at the base (the round-1 test; it must still pass after the build, with the new cases); BE3-AC2 base FAIL as expected (ran at the cut: the last line carries no with_bucket field).
