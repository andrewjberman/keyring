# TO NFRA_CTLPLN.TO-CT-ad-3 -- workstream CALENDAR round 1 (cell CT-ad-3): measure which Lambda-vendored copies of `lib/trading_calendar.py` exist and whether their holiday sets differ from the library's in 2026-2027 (row W12-S1; READ-ONLY, no deploy)

<to_id>NFRA_CTLPLN.TO-CT-ad-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~94</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>CALENDAR</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ad-3` (`decompositions/NFRA_CTLPLN_DECOMP.round14.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Read row `NFRA_CTLPLN-W12-S1` (Grep `"id": "NFRA_CTLPLN-W12-S1"` in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`). The library `lib/trading_calendar.py` (about 304 lines) is the one frontier for trading days. Copies of it are vendored inside Lambda function folders under `infra/aws/lambda/`; the row says three differ (163 lines against 304). A stale copy in a deployed function would mis-count trading days. The CTO ruled (round-13 analysis section 3 ruling 3): this round only MEASURES which copies exist and whether their holiday sets differ from the library's in 2026 and 2027. The sync, if one is needed, rides each function's next deploy and is cut later, never as an out-of-band copy. This cell changes NO copy, NO library and NO Terraform.

At the issuer's cut, a file search for the name finds four copies: `infra/aws/lambda/bd-pipeline/bd-served-vintage-alarm/trading_calendar.py`, `infra/aws/lambda/opal-assets-absence-check/trading_calendar.py`, `infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/trading_calendar.py`, `infra/aws/lambda/opal-assets/advi-49f-gold-dispatch/trading_calendar.py`. The row says three, so the count is itself part of the measurement: enumerate every file named `trading_calendar.py` or a clearly renamed vendored copy (search the Lambda folders with the Grep tool for the function name that defines the holiday set in the library) and print the denominator.

### BUILD

1. A NEW read-only tool `.tools/measure_calendar_copies.py` (standard library; reads files only; no network; no AWS). For the library and each copy it prints one line: path, line count, sha256 of the LF-normalised bytes, and the holiday dates (NYSE full-day closures) it yields for the years 2026 and 2027 by loading the file's own code in a clean namespace through `importlib` from its path (a copy that cannot be imported prints `IMPORT-FAILED <reason>` and counts as differing, never as equal). It then prints, per copy, `SAME-2026-2027` or `DIFFERS-2026-2027 only_in_copy=<dates> only_in_lib=<dates>`. The LAST line is exactly `CALENDAR-COPIES found=<n> same_2026_2027=<a> differs_2026_2027=<b> import_failed=<c> ok=<True|False>` where `ok` is True when `n == a + b + c` and `n >= 1` (the measurement is complete; it does not say the sets match).
2. Run it once and write its output to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~94/CALENDAR_COPIES_MEASURE_20261014.txt`, then add under it, in your own words, a short `READING` section of at most six lines: which functions hold a copy, whether any copy differs in 2026-2027, and what that means for the next step (deploy cells only if a set differs). A claim in READING carries its source line from the output.
3. A NEW test `.tools/tests/test_measure_calendar_copies.py` (standard library; temporary directories only) with arms: two identical fixture calendars read SAME; a fixture that drops one 2026 holiday reads DIFFERS with that date named; a fixture that raises on import reads IMPORT-FAILED and `ok=False` is NOT printed for it alone (the arithmetic still closes); an empty folder set prints `found=0` and `ok=False`. Final line `MEASURE-CALENDAR-COPIES arms=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. Import only by path into a throwaway namespace; do not `pip install`, do not regenerate `lib/tests/gen_nyse_closures.py`, do not edit any `trading_calendar.py`. No aws, no network, no push. `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink. ASCII only; Python 3.11. CLAUDE.md and org/XXX.md are LOCKED. The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W94-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTad3-AC1" cell_refs="CT-ad-3"><invocation>python .tools/tests/test_measure_calendar_copies.py</invocation><expect>ok=True</expect></criterion>
`CTad3-AC1` -- every arm of the measure tool's test passes (base: the file does not exist); report the whole last line with its denominator.

<criterion id="CTad3-AC2" cell_refs="CT-ad-3"><invocation>python .tools/measure_calendar_copies.py</invocation><expect>CALENDAR-COPIES found=</expect></criterion>
`CTad3-AC2` -- the tool reads the real library and every real copy and prints its last line (base: the file does not exist); report the whole last line, including `found=` and `differs_2026_2027=`.
</proof_of_spec>

<expected_criteria>CTad3-AC1,CTad3-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~94/NFRA_CTLPLN.TO-CT-ad-3.calendar-copies-measure-and-holiday-set-diff.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTad3-AC1,CTad3-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round14.md</decomp_doc>
<owned_cells>CT-ad-3</owned_cells>
</decomp_ref>

<paths>
.tools/measure_calendar_copies.py
.tools/tests/test_measure_calendar_copies.py
org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~94/CALENDAR_COPIES_MEASURE_20261014.txt
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a copy that cannot be imported counted as equal (arm 3 forces it to count as differing); a count of three where four exist (the tool prints the denominator); a holiday set read from a copy's cached or stale module instead of its own bytes (importlib from the path into a fresh namespace); BLIND: a vendored copy renamed so no file-name search finds it (the worker also searches the Lambda folders for the defining function's name and says what it searched).
lane: the <paths> block IS the grant (worker RULING 1). Read-only on `infra/aws/lambda/` and `lib/`.
</preflight>

Base checks, dry-run by the issuer before the cut: CTad3-AC1 base: FAIL as expected (the file does not exist); CTad3-AC2 base: FAIL as expected (the file does not exist).
Source: CTO round-13 analysis section 3 ruling 3 (`ledger/ROUND_ANALYSIS.round13.md` @7d271cb57b); row W12-S1. `Z-S3` (regenerate the closure table before 2028) stays carried.
