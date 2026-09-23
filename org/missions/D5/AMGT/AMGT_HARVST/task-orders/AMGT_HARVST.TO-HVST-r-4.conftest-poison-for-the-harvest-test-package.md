# AMGT_HARVST task order -- `HVST-r-4` -- ROUND 2: a package-level `conftest` poison on `SessionManager.refresh` and `subprocess.run` for the whole `lib/opal_data_harvest` test package, so an omitted per-test patch cannot reach a real process; CODE ONLY, no network

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-r-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~14</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on lib/opal_data_harvest (C1=23 C2=7 C3=12 C4=21 C5=334); this cell arms nothing and deploys nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the poison makes a real call impossible rather than merely unauthorised.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~14`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/` and every EXISTING path in section 3 exist. If any is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~14;`.
- **NEVER RUN AN INSTALL. NEVER CALL A PUBLISHER OR AWS. NEVER RUN THE HARVESTER CLI's `run` OR `upload-*`.**

## 1. THE CELL, inlined in full -- `HVST-r-4` (manifest row H3, outcome FWD-3)

**WHY THIS CELL EXISTS.** Round 1 produced **FOUR instances of one class**: a test harness reaching the real session path
inside a phase specified NO-NETWORK. Two are on the record as rows `AMGT_HARVST-Z-W10-S3` and `-Z-W10-S5`; in the worst
one a real browser-harvester subprocess ran for about 346 seconds. Every instance was caught by accident, by the worker
noticing, never by a control.

**THE RULING THIS CELL IMPLEMENTS** -- `1.0.0_SA_CTO~Z`, ratifying this seat's REC, in the round-1 analysis @`f869aa705c`
and its ruling @`e78837e32e`:

> a package-level `conftest` poison on `SessionManager.refresh` and `subprocess.run` for the whole
> `lib/opal_data_harvest` test package, so an omitted per-test patch cannot reach a real process at all.

And its reason, which is the part that decides the design: **per-test discipline is the WRONG LAYER. It fails open,
silently.** A poison at the package layer fails CLOSED and LOUD.

**RULED -- what you build:**
1. **A `conftest.py` for the `lib/opal_data_harvest` test package** (at the location pytest actually collects for those
   test files -- determine it by measurement, and print how you determined it):
   - an **autouse** fixture, applying to EVERY test in the package, that replaces
     `lib.opal_data_harvest.auth.SessionManager.refresh` and `subprocess.run` (the module object's attribute, never a
     dotted-string target) with functions that RAISE a loud, named error;
   - the error text names the poison, the call site and the fact that a real process or network call was attempted.
2. **An OPT-OUT that is explicit and narrow**, for any test that legitimately needs the real attribute: a marker (for
   example `@pytest.mark.allow_real_session`) which the fixture honours. **A test that opts out must say so in its own
   name or docstring.** If no existing test needs it, still provide the marker and prove it works.
3. **THE POSITIVE CONTROL, which is what makes this a proof rather than an absence** (`3.0.0_SA_CVO~Z`'s bar, adopted by
   the CTO): a test that DELIBERATELY calls each poisoned attribute and asserts it RAISES. Without it, a green suite is
   consistent with the poison being absent.
4. **No existing test's behaviour changes.** Every suite in the package keeps its exact pass and fail counts.

**What this cell does NOT do:**
- it does NOT explain row `-Z-W10-S3`'s mechanism (a dotted-string monkeypatch target that no-ops for some module
  attributes and not others). **The poison CONTAINS that hazard; it does not root-cause it, and the row stays ARMED.**
  Say so in your report rather than implying the row is closed;
- it changes no production code path;
- it touches no other test package.

## 2. WHERE THIS CAME FROM
Round 2, decomposition v1.1 @04a235adb7 section 10a, cell 4 of 5. Independent of the other four.

## 3. SURFACES -- what you may read and write

<paths>
lib/opal_data_harvest/conftest.py
lib/opal_data_harvest/test_poison_control.py
lib/opal_data_harvest/test_retrieval_provenance.py
lib/opal_data_harvest/test_bronze_capture.py
lib/opal_data_harvest/test_silver_from_bronze.py
lib/opal_data_harvest/test_legacy_upload.py
lib/opal_data_harvest/test_harvest_grammar.py
lib/opal_data_harvest/test_worker.py
lib/opal_data_harvest/test_catalog.py
lib/opal_data_harvest/test_verification.py
lib/opal_data_harvest/auth.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~14/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-r-4.conftest-poison-for-the-harvest-test-package.md
</paths>

- **You may CREATE `conftest.py` and `test_poison_control.py`, and EDIT an existing test only to add an opt-out marker
  where it genuinely needs the real attribute.** `auth.py` is READ-ONLY: read it to find the right attribute, never edit
  it. AC3 fails if any production module changes.
- Scratch goes in `<your worktree>/.scratch/r4/`.
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~14 <0.9.0_WK_AMGT_HARVST~14@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **CODE ONLY, TESTS ONLY. Pure ASCII.**
- **Every pre-existing count holds.** Measured at this cut: `test_retrieval_provenance` 18 passed,
  `test_bronze_capture` 12, `test_silver_from_bronze` 16, `test_legacy_upload` 6, `test_harvest_grammar` 7,
  `test_catalog` 5, `test_worker` 2 failed and 18 passed, `test_verification` 1 failed and 3 passed. **The two
  pre-existing failures are NOT yours to fix and their counts must not GROW.**
- **Surprise rows:** `AMGT_HARVST-Z-W14-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC0" cell_refs="HVST-r-4"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in test_retrieval_provenance test_bronze_capture test_silver_from_bronze test_legacy_upload test_harvest_grammar test_worker test_catalog test_verification; do echo "$t :: $(python -m pytest lib/opal_data_harvest/$t.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>BEFORE any edit, eight baseline lines recorded; measured at the cut: 18 passed; 12 passed; 16 passed; 6 passed; 7 passed; 2 failed 18 passed; 5 passed; 1 failed 3 passed</expect></criterion>
  <criterion id="AC1" cell_refs="HVST-r-4"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/opal_data_harvest/test_poison_control.py -v --color=no -p no:cacheprovider 2>&1 | tail -12</invocation><expect>every arm passes and no "failed" -- including one arm per poisoned attribute that DELIBERATELY calls it and asserts it RAISES, and one arm proving the opt-out marker restores the real attribute</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-r-4"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in test_retrieval_provenance test_bronze_capture test_silver_from_bronze test_legacy_upload test_harvest_grammar test_worker test_catalog test_verification; do echo "$t :: $(python -m pytest lib/opal_data_harvest/$t.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>each line's passed and failed counts EQUAL its AC0 line: the poison changed no existing test's outcome, and neither pre-existing failure grew</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-r-4"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r4/ac3.py</invocation><expect>"outside_allowed []" -- only conftest.py, test_poison_control.py and any test file that needed an opt-out marker changed; NO production module changed (not auth.py, not worker.py, not publishers.py, not __main__.py, not silver_from_bronze.py, not uploads.py, not transport.py, not harvest_grammar.py); and every changed file prints "compiles True crlf 0 non_ascii 0"</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-r-4"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r4/ac4.py</invocation><expect>"collected_conftest &lt;path&gt;" naming the conftest pytest actually loads for this package (measured, not assumed), and "autouse True" for the poison fixture</expect></criterion>
</proof_of_spec>

Write `.scratch/r4/ac3.py` (diff from `git merge-base HEAD SITEZ` over `lib`, an allowed set, and a compile, CRLF and
non-ASCII print per changed file) and `.scratch/r4/ac4.py` (prove WHICH conftest pytest loads for this package, and that the
fixture is autouse -- for example through `--collect-only` plus a fixture listing, never by assuming a path).

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~14/AMGT_HARVST.TO-HVST-r-4.conftest-poison-for-the-harvest-test-package.proof_of_spec.json`.
2. Grade with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4`, which must return rc 0.
3. Flip to `complete` only if every criterion passes.
4. Commit with `--only`.
5. Report once, and say plainly that row `-Z-W10-S3`'s mechanism remains unexplained.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **AC4 exists because the last four instances of this class were all "I patched something that was not the thing".**
   A conftest at the wrong path is exactly that failure again, one layer up, and it would leave the suite green.
2. **The opt-out is required even if nothing needs it today**, so the next test that legitimately needs a real session has
   a named door instead of deleting the fixture.
3. **The row stays ARMED by construction**, and the worker is told to say so, because a containment reads like a fix in a
   later summary.

<status>pending</status>
<round>2</round>
<slot>~14</slot>
<fabric>site-z</fabric>
