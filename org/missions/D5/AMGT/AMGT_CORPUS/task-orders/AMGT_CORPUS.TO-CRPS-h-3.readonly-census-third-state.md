# AMGT_CORPUS task order -- `CRPS-h-3` -- ROUND 6: the read-only code census names its THIRD state -- an unresolved write is listed as unresolved, never counted as reaching the library, and the exit predicate does not weaken

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-h-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 1 drift candidate, on data/black_diamond; 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- a static code census; nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 6. Serves **FWD-9**: "a census of the project's own code prints zero
write, move, delete or open-for-write calls against any path under the library root, with the denominator of files scanned".

## 1. THE CELL -- `CRPS-h-3`

**Where this came from.** `lib/research/corpus/readonly_proof.py`'s `code_census` gives each write-like call a set of origins
(`LIBRARY`, `UNKNOWN`, `TMP_FIXTURE`, ...) and sets `reaches_library = LIBRARY in origins or (UNKNOWN in origins and not
(is_test and set(origins) == {TMP_FIXTURE}))`, then prints `library_write_calls` as the sum of `reaches_library`. The live
census (`python -m lib.research.corpus.readonly_proof --code-census`) reads files_scanned 39, write_like_calls 43,
library_write_calls 4, and all four are in `lib/research/corpus/induction_run.py` (:462, :464, :688, :690), origin UNKNOWN,
through `deliverables_dir = deliverables_dir or DELIVERABLES_DIR`. So the one number says "reaches the library" for calls whose
target is unresolved: UNRESOLVED is not REACHES.

**RULED -- what you build:**
- Every census row gains `state`: `library` when `LIBRARY` is among its origins; else `unresolved` when `UNKNOWN` is, outside the
  existing tmp-fixture exemption; else `clear`. Precedence exactly in that order; `reaches_library` stays on the row unchanged.
- `library_write_calls` counts `state == library` only.
- The totals (printed first and last, as now) gain ONE line
  `tristate library <a> unresolved <b> clear <c> write_like_calls <n>` with `a+b+c == n`, and ONE line per unresolved row:
  `unresolved_site <path>:<line> <call> origins <origins>`.
- The EXIT PREDICATE does NOT weaken: rc 0 only if the positive controls flag AND `library + unresolved == 0`. The existing
  `--plant-unknown-in-test` difference control now moves `unresolved` (not `library`) from 0 to 1, and still fails closed.
- `lib/research/corpus/tests/test_readonly_proof_tristate.py` (new): one planted call per state; the precedence (LIBRARY with
  UNKNOWN is `library`); the tristate sum; rc stays non-zero with one unresolved site.

## 3. SURFACES

<paths>
lib/research/corpus/readonly_proof.py
lib/research/corpus/tests/test_readonly_proof_tristate.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-h-3.readonly-census-third-state.md
</paths>

READ-ONLY: every other module, including `induction_run.py` (its four sites are LISTED, not changed). Scratch `.scratch/h3/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. The existing tests in `lib/research/corpus/tests/test_readonly_proof.py` keep passing
  unmodified; if one asserts the old summed meaning, REFUSE with the test name rather than editing it.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W3-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-h-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round6/h3_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-h-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round6/h3_AC2.sh</invocation><expect>(?m)^tristate library 0 unresolved \d+ clear \d+ write_like_calls \d+$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-h-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round6/h3_AC3.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe: the live census prints the tristate line with library 0; AC3 the bound: the
  corpus suite still passes.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-h-3.readonly-census-third-state.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's tristate line and every `unresolved_site` line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-5 analysis s.5 item 4 @`37217d8053` ("UNRESOLVED is not REACHES. Positive control already works").
FWD-9's grade after this cell rests on a reader of the four listed sites (the L9/L10 read); this cell does not resolve them.
Checks dry-run at the base: AC1 FAIL (no such file), AC2 FAIL (no tristate line), AC3 bound.

<risk>LOCAL</risk>
<status>pending</status>
<round>6</round>
<slot>~3</slot>
<fabric>site-z</fabric>

**WORKER CLOSE (`0.9.0_WK_AMGT_CORPUS~3`):** AC1 PASS (9 passed in test_readonly_proof_tristate.py); AC2 PASS (live census prints `tristate library 0 unresolved 4 clear 43 write_like_calls 47` with the 4 unresolved_site lines all in induction_run.py at :462/:464/:688/:690, listed not changed); AC3 PASS (317 passed in lib/research/corpus/tests, existing reaches_library assertions untouched).

<status>complete</status>
