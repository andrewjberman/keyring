# AMGT_RESAPP task order -- `AMGT-rk-63` -- `test_generation_and_pool_routes.py`'s two orphaned assertions are repaired to the six-value FIELD-ONLY `ceo_profile_reading` contract `AMGT-rk-43` introduced, replacing the retired two-value SENTENCE-PARSED contract they still check

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-63</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~63</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits one test file only; it arms no cron, alarm, monitor or
  cadence, reads no schedule and writes none.
comp-iam: DECLARED-NOT-APPLICABLE -- this order performs NO live AWS act: `ceo_profile_reading` is a pure function
  (no I/O), and the `pool` fixture writes to a LOCAL TEMP DIRECTORY the test harness controls, never S3.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~63`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~63;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-63` (R15-M1; row `AMGT_RESAPP-Z-W39-S5` / `Z-S181`; test repair)

**The analysis row, verbatim (`ROUND_ANALYSIS.round14.md` @93cb6416e4 s.2.2, `:71-76`):** *"`rk-61`'s orphaned test
repair -- owner named. Per s.1: UNASSIGNED. RULED: round 15 cuts a narrow order carrying a grant on exactly
`lib/research/api/tests/test_generation_and_pool_routes.py`, criterion = the two assertions that today check the
retired two-value `NOT_CONFIRMED_NOTHING_FOUND` sentence-parsed contract now check the six-value field-only contract
`rk-43` introduced, proof = the full file's battery green at the worker's branch HEAD. Cell R15-M1."*

**Row `AMGT_RESAPP-Z-W39-S5`** (filed by `0.9.0_WK_AMGT_RESAPP~39`, DISARMED by this seat's own row
`AMGT_RESAPP-Z-S181`, disposition GRADUATED): *"the two pre-existing failures in test_generation_and_pool_routes.py
(test_13, test_13b: 'NOT_SEARCHED' == 'NOT_CONFIRMED_NOTHING_FOUND') are the SAME drift already carried to the slug
by W61-S1 and W49-S3 ... owner: the CTO's round-15 analysis."* This cell IS that owner's remedy.

**THE MEASURED STATE, at HEAD (cite these lines; do not re-derive from memory -- RE-RUN and confirm before you
touch anything):**
- `lib/research/api/scoped_amgt.py:2360-2459`, `ceo_profile_reading(profile)`: the CURRENT, LIVE contract (comment
  block `:2360-2366` names `AMGT-rk-43` as the author, R14-E1). Reads the object's OWN FIELDS --
  `status`, `query`, `basis`, `absence_class` -- never a parsed sentence. Returns ONE of SIX values
  (`CEO_READING_*` constants, `:2367-2372`): `CONFIRMED` (status RESOLVED, url set, `:2416-2422`); `NOT_SEARCHED`
  (status ABSENT, `query` is `None`, `:2423-2429`); `SEARCH_FAILED` (status ABSENT, query set, `basis` starts with
  the literal prefix `"the SERP primitive raised"`, `:2431-2437`); `SEARCHED_LINKS_UNREADABLE` (status ABSENT,
  query set, `absence_class == "CANNOT_SAY"`, `:2439-2445`); `SEARCHED_NOTHING_FOUND` (status ABSENT, query set,
  `absence_class == "NOTHING_FOUND"`, `:2446-2452`); `UNREADABLE_OBJECT` (not a dict, or any other combination,
  `:2453-2459`, `reading_basis` prints the fields it saw). `urls_returned` is parsed from `basis` via
  `_SERP_URL_COUNT_RE = re.compile(r"returned (\d+) url")` for INFORMATION ONLY, never an input to the reading
  (`:2374`, `:2413-2415`).
- `lib/research/api/tests/test_generation_and_pool_routes.py:474-502`, `test_13_management_is_M1_with_the_pool_average_at_the_same_as_of`:
  the fixture at `:488` sets `"ceo_public_profile": {"status": "ABSENT", "basis": "the SERP returned 0 url(s) --
  nothing found"}` -- NO `query` key, so `profile.get("query")` reads `None` and the function returns
  `NOT_SEARCHED`, not the `NOT_CONFIRMED_NOTHING_FOUND` the assertion at `:499` expects. This fixture, as written,
  describes a legacy two-value-contract shape; a search visibly RAN (the basis text says "the SERP returned 0
  url(s)"), so the FAITHFUL field-level fixture for "a search ran and found nothing" needs `query` set and
  `absence_class` = `"NOTHING_FOUND"`.
- `lib/research/api/tests/test_generation_and_pool_routes.py:505-513`, `test_13b_the_ceo_profile_reading_separates_the_two_absences`:
  BOTH the `nothing` fixture (`:508`) and the `cannot` fixture (`:509`) set only `status` and `basis` -- neither
  sets `query`, so BOTH resolve to `NOT_SEARCHED` under the live function, not the two DIFFERENT retired values the
  assertions at `:510-511` expect; `reading(None)["reading"]` (`:513`) is asserted `NOT_CONFIRMED_INSTRUMENT_CANNOT_SAY`,
  but the live function returns `UNREADABLE_OBJECT` for `reading_basis == "the object is not a dict"` (`:2403-2409`)
  -- `NOT_CONFIRMED_INSTRUMENT_CANNOT_SAY` does not exist anywhere in the live function; and `:512` asserts a
  `reading_basis` substring, `"parsed from ceo_public_profile.basis"`, that also does not exist in any of the six
  live `reading_basis` strings (`:2419`, `:2426`, `:2434`, `:2442`, `:2449`, `:2455-2457`) -- confirming these two
  tests are orphaned against an EARLIER version of the function, not merely a renamed enum.
- **MEASURED NOW, both failures reproduced at this cut:** `python -m pytest
  lib/research/api/tests/test_generation_and_pool_routes.py -q` -> `2 failed, 22 passed` (24 total), both failures
  `AssertionError: assert 'NOT_SEARCHED' == 'NOT_CONFIRMED_NOTHING_FOUND'`.

**RULED, what you build (edit ONLY the two named tests; no other test in this 24-test file moves):**

1. **`test_13_management_is_M1_with_the_pool_average_at_the_same_as_of`, line 488 fixture and line 499 assertion.**
   Add `"query": "A"` and `"absence_class": "NOTHING_FOUND"` to the `ceo_public_profile` dict at line 488 (keeping
   `"status": "ABSENT"` and the existing `"basis"` text unchanged -- this is the field-level shape that makes the
   fixture internally consistent with what its own basis text already says: a search ran, nothing was found).
   Change line 499's assertion from `== "NOT_CONFIRMED_NOTHING_FOUND"` to `== "SEARCHED_NOTHING_FOUND"` (the live
   six-value constant for exactly this field combination).

2. **`test_13b_the_ceo_profile_reading_separates_the_two_absences`, lines 505-513, FULL REWRITE exercising all six
   values of the live contract directly (never re-deriving the function's logic -- assert against the literal
   return values read from section 1 above):**
   ```python
   def test_13b_the_ceo_profile_reading_separates_the_two_absences():
       # row AMGT_RESAPP-Z-W39-S5 / Z-S181 / round-15 R15-M1: AMGT-rk-43 replaced the sentence-parsed two-value
       # contract (NOT_CONFIRMED_NOTHING_FOUND / NOT_CONFIRMED_INSTRUMENT_CANNOT_SAY) with a six-value FIELD-ONLY
       # contract read from status/query/absence_class/basis (scoped_amgt.py:2377-2459). This battery exercises
       # that contract directly, one fixture per value, by SUBTRACTION over the docstring's own table.
       reading = scoped_amgt.ceo_profile_reading

       confirmed = reading({"status": "RESOLVED", "url": "https://www.sap.com/x"})
       assert confirmed["reading"] == "CONFIRMED"
       assert confirmed["reading_basis"] == "status=RESOLVED url=set"

       not_searched = reading({"status": "ABSENT", "query": None, "basis": None})
       assert not_searched["reading"] == "NOT_SEARCHED"
       assert not_searched["reading_basis"] == "status=ABSENT query=null"
       assert not_searched["urls_returned"] is None

       failed = reading({"status": "ABSENT", "query": "A", "basis": "the SERP primitive raised ConnectionError"})
       assert failed["reading"] == "SEARCH_FAILED"
       assert failed["reading_basis"] == "status=ABSENT query=set basis starts with 'the SERP primitive raised'"

       nothing = reading({"status": "ABSENT", "query": "A", "absence_class": "NOTHING_FOUND",
                           "basis": "the SERP returned 0 url(s)"})
       assert nothing["reading"] == "SEARCHED_NOTHING_FOUND"
       assert nothing["urls_returned"] == 0
       assert nothing["reading_basis"] == "status=ABSENT query=set absence_class=NOTHING_FOUND"

       cannot = reading({"status": "ABSENT", "query": "A", "absence_class": "CANNOT_SAY",
                          "basis": "the SERP returned 2 url(s) and none on boeing.com -- ABSENT is the honest result"})
       assert cannot["reading"] == "SEARCHED_LINKS_UNREADABLE"
       assert cannot["urls_returned"] == 2
       assert cannot["reading_basis"] == "status=ABSENT query=set absence_class=CANNOT_SAY"

       unreadable_status = reading({"status": "WEIRD", "query": "A", "absence_class": None})
       assert unreadable_status["reading"] == "UNREADABLE_OBJECT"
       assert unreadable_status["reading_basis"] == "status=WEIRD query=set absence_class=None"

       not_a_dict = reading(None)
       assert not_a_dict["reading"] == "UNREADABLE_OBJECT"
       assert not_a_dict["reading_basis"] == "the object is not a dict"
   ```
   Run this EXACT function body verbatim (do not paraphrase or "improve" it) -- every literal string above is
   copied from `ceo_profile_reading`'s own source at the cited lines and must byte-match what the function
   actually returns; if any assertion in the block above does NOT match your own fresh read of the function at
   your branch HEAD, that is a STOP-and-row (the function drifted between this order's cut and your spawn), never
   a silent edit to make it pass.

**What this cell does NOT change:** `lib/research/api/scoped_amgt.py` (read only -- `ceo_profile_reading` is not
touched, only the tests that exercise it); any OTHER test function in `test_generation_and_pool_routes.py` (22 of
24 already pass and must still pass, unchanged); any fixture helper (`_officer`, `pool`) used by other tests.

**THE VALIDATION BAR:** this is a pure-function unit-test repair with no security population and no live call;
proven entirely by the file's own battery, offline.

## 2. WHERE THIS CAME FROM

**ROUND 15**, decomposition s.23 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-14 analysis
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round14.md` @93cb6416e4 s.2.2 (`:71-76`) and s.3 (`:104`
row R15-M1); the row `AMGT_RESAPP-Z-W39-S5` (surfaced by `0.9.0_WK_AMGT_RESAPP~39`) and its disarm
`AMGT_RESAPP-Z-S181` (filed by `2.0.0_SA_COO~Z`, `/canonical-drive` tick 2026-09-19 ~17:0xZ, naming "owner: the
CTO's round-15 analysis"). PRD v0.13 @1699960261: no FWD or `C-` contract is touched (a test-only repair; no PRD
addendum this round).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/tests/test_generation_and_pool_routes.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~63/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-63.ceo-profile-reading-test-repair.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (read `lib/research/api/scoped_amgt.py`
  freely -- you must read it fresh at your own branch HEAD to confirm section 1's citations still hold); this
  block governs WRITES. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~63 <0.9.0_WK_AMGT_RESAPP~63@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every
  `.py` you commit passes `.tools/commit-gate.sh` (py_compile + ds-precommit + ruff py39) inside safe-commit.

## 4. BOUNDS

**NO LIVE AWS ACT, NO DEPLOY, NO VENDOR CALL.** PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF.** **NO
alarm, monitor, SNS/SES-send, notification or freshness checker.** No non-ASCII in anything you write. **PUSH:
never.** Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular, never edit
`ceo_profile_reading` itself to make an assertion pass; the function is the fixed reference, the tests move to
match it.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- the file's total test count
(24) is re-measured at spawn by AC1; it may have moved if a sibling cell landed first (none should touch this
file).
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W63-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-63"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/api/tests/test_generation_and_pool_routes.py -q 2>&1 | tail -10</invocation><expect>a final line "24 passed" (or "N passed" with N equal to the file's total test count re-measured at spawn) and 0 failed -- both test_13 and test_13b pass under the repaired assertions, and the other 22 (or N-2) pre-existing tests in the file are UNCHANGED and still pass</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-63"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/api/tests/test_generation_and_pool_routes.py::test_13b_the_ceo_profile_reading_separates_the_two_absences -v 2>&1 | tail -10</invocation><expect>"PASSED" for this one test, isolated from the rest of the file -- proves the rewrite is self-contained and does not depend on ordering or state from another test in the module</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-63"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import sys
sys.path.insert(0, '.')
from lib.research.api import scoped_amgt
vals = set()
fixtures = [
    {'status': 'RESOLVED', 'url': 'https://www.sap.com/x'},
    {'status': 'ABSENT', 'query': None, 'basis': None},
    {'status': 'ABSENT', 'query': 'A', 'basis': 'the SERP primitive raised ConnectionError'},
    {'status': 'ABSENT', 'query': 'A', 'absence_class': 'NOTHING_FOUND', 'basis': 'x'},
    {'status': 'ABSENT', 'query': 'A', 'absence_class': 'CANNOT_SAY', 'basis': 'x'},
    {'status': 'WEIRD', 'query': 'A', 'absence_class': None},
]
for f in fixtures:
    vals.add(scoped_amgt.ceo_profile_reading(f)['reading'])
vals.add(scoped_amgt.ceo_profile_reading(None)['reading'])
print('distinct_readings', len(vals), 'of 6 expected', sorted(vals))
"</invocation><expect>distinct_readings 6 of 6 expected, the sorted list being exactly ['CONFIRMED', 'NOT_SEARCHED', 'SEARCHED_LINKS_UNREADABLE', 'SEARCHED_NOTHING_FOUND', 'SEARCH_FAILED', 'UNREADABLE_OBJECT'] -- confirms test_13b's six fixtures (section 1's rewrite) are NOT accidentally collapsing two branches onto the same value, i.e. the battery genuinely covers all six, not fewer with duplication</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-63"><invocation>cd "$(git rev-parse --show-toplevel)" && git diff --stat -- lib/research/api/tests/test_generation_and_pool_routes.py && echo "---" && git diff --name-only -- lib/research/api/scoped_amgt.py</invocation><expect>the stat line names exactly one file, test_generation_and_pool_routes.py, with some insertions/deletions; the second command (scoped_amgt.py) prints NOTHING -- confirms the fixed reference function was never touched, only the tests moved to match it</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~63/AMGT_RESAPP.TO-AMGT-rk-63.ceo-profile-reading-test-repair.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, naming the file's final total test count.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>15</round>
<slot>~63</slot>
<fabric>site-z</fabric>
