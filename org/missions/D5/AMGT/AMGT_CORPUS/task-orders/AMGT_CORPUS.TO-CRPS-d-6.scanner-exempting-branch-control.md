# AMGT_CORPUS task order -- `CRPS-d-6` -- ROUND 2: a control for the branch that EXEMPTS -- the read-only census's test-file exemption gets a positive control and is justified by measurement (fixture-rooted origins), so an unknown-origin write in a test file COUNTS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-d-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates of the census (C1=23 C2=5 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell writes nothing to S3 and reads only the repository.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 2. Work ONLY in your worktree (its absolute path is in your prompt).
- **First act:** print `git rev-parse --abbrev-ref HEAD`, and test that `lib/research/corpus/readonly_proof.py` and
  `lib/research/corpus/tests/test_readonly_proof.py` exist. If either is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_CORPUS~3;`.
- **NEVER INSTALL. NEVER CALL A VENDOR API OR THE CLAUDE API. NEVER TOUCH THE LIBRARY. NEVER DELETE ANYTHING** -- this
  cell runs `--code-census` only; it does NOT run `--negative-control` (that copies 300 MB and is round 1's evidence).

## 1. THE CELL, inlined in full -- `CRPS-d-6` (manifest row R11 enriched; serves FWD-9)

**FWD-9, verbatim:** *"Nothing this project runs can write to, move or delete anything in the team's library. DONE WHEN
EXERCISED -- ... a census of the project's own code prints zero write, move, delete or open-for-write calls against any
path under the library root, with the denominator of files scanned."*

**THE FINDING THIS CELL ANSWERS (1.0.0_SA_CTO~Z's round-1 analysis s.2; 3.0.0_SA_CVO~Z's row `AMGT_CORPUS-Z-C-S4`):**
`readonly_proof.py:301` reads `reaches = LIBRARY in origins or (not is_test and UNKNOWN in origins)`, with `is_test` set at
`:282` from `"tests" in Path(filename).parts or Path(filename).name.startswith("test_")`. The instrument is fail-CLOSED
for library code and fail-OPEN for test files. Of 27 flagged calls at HEAD, 10 non-test sites are a positive
determination and SEVENTEEN test sites read `origins ['unknown']` / `reaches_library False` -- a DEFAULT, not a
measurement. The positive control (`:469-472`) plants `open(library_root() / "x", "w")` into `positive_control.py`, which
is NOT a test file, so it takes the DETECTING branch: **the exempting branch has no control at all.** The analysis's words:
*"The cell is a planted violation IN A TEST FILE which must be detected, or the exemption justified."* This cell does BOTH.

**RULED -- what you build in `lib/research/corpus/readonly_proof.py` (the `--code-census` arm only):**
1. **A second positive control that exercises the EXEMPTING branch:** plant `open(library_root() / "x", "w")` into a file
   named `test_plant_control.py` inside a temp directory named `tests/` (outside the repo, beside the existing plant),
   census it with the same scanner, and print `positive_control_test_file flagged 1`. A LIBRARY-origin write in a test
   file MUST be flagged (`LIBRARY in origins` already precedes the exemption -- this control proves it at the bytes rather
   than by reading).
2. **The exemption justified by MEASUREMENT, not by default:** a new origin class `"tmp-fixture"` for a target rooted in
   pytest's `tmp_path` / `tmpdir` / `tmp_path_factory` (a parameter of those names, or a local bound from one of them
   through the existing def-use walk), so that a test-site write whose root is a fixture resolves to `['tmp-fixture']` and
   is exempt BECAUSE it was measured. A test-site write whose origin is genuinely `unknown` now COUNTS: `:301` becomes
   `reaches = LIBRARY in origins or (UNKNOWN in origins and not (is_test and origins == {TMP_FIXTURE}))` -- or the
   equivalent stated in your own words in the docstring: the ONLY exemption is a measured fixture root. Print, in the
   per-site lines, the new origin, and in the totals `test_sites T tmp_fixture_sites M test_unknown_sites 0` -- 0 is a
   MEASUREMENT at HEAD (every one of the 17 is fixture-rooted: `(tmp_path / 'loose.txt')`, `folder = tmp_path / name`,
   `resolved_dir = tmp_path / 'Resolved Co'`, `empty_home = tmp_path / 'empty-home'` ...); if any site is NOT
   fixture-rooted, it counts as a library-reaching UNKNOWN and `library_write_calls` reads > 0 -- which is a FINDING you
   report, never a number you tune away.
3. **The difference control:** `--code-census --plant-unknown-in-test` additionally plants
   `def compute(): return object()\ndef test_x():\n    open(compute(), "w")\n` into a `test_plant_unknown.py` under the
   temp `tests/` dir and censuses it: `test_unknown_sites 1` and the plant's line printed with `reaches_library True`.
   Without the flag the census is unchanged.
4. **Totals printed FIRST and LAST** (`files_scanned`, `write_like_calls`, `library_write_calls`, `positive_control flagged`,
   `positive_control_test_file flagged`, `test_sites`, `tmp_fixture_sites`, `test_unknown_sites`), so `tail -60` never
   drops them (row `AMGT_CORPUS-Z-S10`).
5. **`tests/test_readonly_proof.py`** gains: the test-file plant is flagged; a `tmp_path`-rooted write in a test module
   resolves to `tmp-fixture` and is not counted; an unknown-origin write in a test module IS counted; the existing 91
   tests still pass.

**What this cell does NOT do:** no change to the negative-control arm; no change to the origin rules for non-test code;
no new exemption of any kind; no deletion of the temp plants (they are left, as the existing plant is, with
`left_for_operator_cleanup True`).

## 2. WHERE THIS CAME FROM
Round 2, decomposition v2.0, chain C, the only cell on this slot; the one instrument-repair cell of the round (the
verification diet). Nothing reads its output.

## 3. SURFACES

<paths>
lib/research/corpus/readonly_proof.py
lib/research/corpus/tests/test_readonly_proof.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-d-6.scanner-exempting-branch-control.md
</paths>

**READ-ONLY:** every other `lib/research/corpus/` file. Scratch in `.scratch/d6/`. Commit with
`bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~3 <0.9.0_WK_AMGT_CORPUS~3@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **Pure ASCII source, LF, Python 3.9-compatible.**
- **Tests:** offline under the poison; the plants are written to `tempfile.gettempdir()` only.
- **Surprise rows:** `AMGT_CORPUS-Z-W3-S<k>`, `disarm_owner` `2.0.0_SA_COO~X`. **REFUSE a criterion you cannot satisfy as
  written**, and report it with your measurement -- a test site that is NOT fixture-rooted is exactly the finding this
  cell exists to surface.

## 5. PROOF OF SPEC (each invocation LITERAL; each runs under your `timeout 300`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-d-6"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests/test_readonly_proof.py -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-d-6"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.readonly_proof --code-census 2>&1 | tail -60</invocation><expect>(?s)files_scanned [1-9]\d*.*library_write_calls 0\b.*positive_control flagged 1\b.*positive_control_test_file flagged 1\b.*test_sites [1-9]\d* tmp_fixture_sites [1-9]\d* test_unknown_sites 0\b</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-d-6"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.readonly_proof --code-census --plant-unknown-in-test 2>&1 | tail -60</invocation><expect>(?s)test_unknown_sites 1\b</expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the census on the real package with BOTH controls fired and the exemption measured; AC3
  the difference control (reason: a `0` that cannot become `1` on a planted violation is not a measurement).

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-d-6.scanner-exempting-branch-control.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` returns rc 0.
3. Flip `<status>` to `complete` only if every criterion passes. Commit via safe-commit with the pathspec of exactly the
   files you changed plus the instance.
4. Report ONCE: the AC2 totals line, the per-site origins of the test sites, and AC3's planted line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the analysis names two acceptable answers (detect the plant, or justify the exemption); this cell does
both because a justified exemption without a detecting control is still a default, and a detecting control without a
justification would force every fixture write into a false positive. The three earlier scanner rounds (Z-S7..S9) are
disarmed by evidence in row Z-S12; this cell does not re-open them.

<status>pending</status>
<round>2</round>
<slot>~3</slot>
<fabric>site-z</fabric>
