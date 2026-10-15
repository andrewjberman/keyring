# TO NFRA_CTLPLN.TO-CT-ae-2 -- workstream CALENDAR round 2 (cell CT-ae-2): measure whether the hand-typed `NYSE_HOLIDAYS` sets in `mdpf-daily-trigger` and `mdpf-freshness-checker` match the library for 2026-2027 (row W94-S1; READ-ONLY, any fix routes to MDPF)

<to_id>NFRA_CTLPLN.TO-CT-ae-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~98</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>CALENDAR</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ae-2` (`decompositions/NFRA_CTLPLN_DECOMP.round15.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Read row `NFRA_CTLPLN-W94-S1` (Grep `"id": "NFRA_CTLPLN-W94-S1"` in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`). Round 14's `.tools/measure_calendar_copies.py` measured the vendored copies of `lib/trading_calendar.py` (4 found, none differs in 2026-2027). It did not count two Lambdas that carry their OWN hand-typed holiday set: `infra/aws/lambda/mdpf-pipeline/mdpf-freshness-checker/lambda_function.py` (`NYSE_HOLIDAYS` at about :144, `is_trading_day` at about :161) and `infra/aws/lambda/mdpf-pipeline/mdpf-daily-trigger/lambda_function.py` (`NYSE_HOLIDAYS` at about :179, `is_trading_day` at about :192). A hand-typed set that disagrees with the library mis-counts trading days, the false-stale hazard the CLAUDE.md hard stop names. The CTO ruled (round-14 analysis ruling 2): MEASURE them against the library for 2026 and 2027. A mismatch is fixed by importing the library at the function's next deploy, never by correcting the hand-typed copy, and the fix is MDPF's. This cell changes NO Lambda file, NO library and NO Terraform.

### BUILD

1. A NEW read-only tool `.tools/measure_inline_holiday_sets.py` (standard library; reads files only; no network; no AWS; never imports a Lambda module: those import `boto3`). It reads each Lambda file's `NYSE_HOLIDAYS` assignment through `ast` (`ast.literal_eval` of the assigned value; the set holds ISO date strings), and the library's closures for 2026 and 2027 the way `.tools/measure_calendar_copies.py` already does (import that tool's loader by path and reuse it; do not copy its code). It also checks the `is_trading_day` body of each Lambda reads only weekday and `NYSE_HOLIDAYS` (print `LOGIC-OK` or `LOGIC-DIFFERS <what>`; a function it cannot parse prints `LOGIC-UNREAD`). Per file it prints the path, the number of dates it holds for 2026 and 2027, and `SAME-2026-2027` or `DIFFERS-2026-2027 only_in_lambda=<dates> only_in_lib=<dates>`. A file it cannot read or parse prints `UNREADABLE <reason>` and counts as differing, never as equal. The LAST line is exactly `INLINE-HOLIDAY-SETS found=<n> same_2026_2027=<a> differs_2026_2027=<b> unreadable=<c> ok=<True|False>` where `ok` is True when `n == a + b + c` and `n >= 1`. Also search `infra/aws/lambda` with the Grep tool for any OTHER `NYSE_HOLIDAYS` or `is_trading_day` definition outside the two files and `trading_calendar.py` copies, include each in the measurement, and print what you searched.
2. Run it once and write its output to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~98/INLINE_HOLIDAY_SETS_MEASURE_20261014.txt`, then add under it a `READING` section of at most six lines: which functions hold a hand-typed set, whether any differs in 2026-2027, and the routing (a difference is MDPF's to fix at the next deploy by importing the library; no difference needs no cell). A claim in READING carries its source line from the output.
3. A NEW test `.tools/tests/test_measure_inline_holiday_sets.py` (standard library; temporary directories only) with arms: a fixture Lambda whose set equals a fixture library reads SAME; a fixture that drops one 2026 date reads DIFFERS with that date named; a fixture whose `NYSE_HOLIDAYS` is not a literal reads UNREADABLE and the arithmetic still closes; a fixture whose `is_trading_day` also tests another condition reads LOGIC-DIFFERS; an empty file set prints `found=0` and `ok=False`. Final line `MEASURE-INLINE-HOLIDAYS arms=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. Do not edit any Lambda file, any `trading_calendar.py`, or `lib/`. No aws, no network, no push. `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink. ASCII only; Python 3.12. CLAUDE.md and org/XXX.md are LOCKED. The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W98-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTae2-AC1" cell_refs="CT-ae-2"><invocation>python .tools/tests/test_measure_inline_holiday_sets.py</invocation><expect>ok=True</expect></criterion>
`CTae2-AC1` -- every arm of the tool's test passes (base: the file does not exist); report the whole last line with its denominator.

<criterion id="CTae2-AC2" cell_refs="CT-ae-2"><invocation>python .tools/measure_inline_holiday_sets.py</invocation><expect>INLINE-HOLIDAY-SETS found=</expect></criterion>
`CTae2-AC2` -- the tool reads the real library and the real Lambda files and prints its last line (base: the file does not exist); report the whole last line, including `found=` and `differs_2026_2027=`.
</proof_of_spec>

<expected_criteria>CTae2-AC1,CTae2-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~98/NFRA_CTLPLN.TO-CT-ae-2.inline-holiday-sets-measure.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTae2-AC1,CTae2-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round15.md</decomp_doc>
<owned_cells>CT-ae-2</owned_cells>
</decomp_ref>

<paths>
.tools/measure_inline_holiday_sets.py
.tools/tests/test_measure_inline_holiday_sets.py
org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~98/INLINE_HOLIDAY_SETS_MEASURE_20261014.txt
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a set that cannot be parsed counted as equal (it counts as differing); a Lambda module imported and executed (the tool reads source through `ast` only); a third hand-typed definition missed (the worker searches the Lambda tree and prints the search); BLIND: a holiday set built by a comprehension or read from a data file at run time, which `ast.literal_eval` cannot read (UNREADABLE, reported by name).
lane: the <paths> block IS the grant (worker RULING 1). Read-only on `infra/aws/lambda/` and `lib/`; these are dell1's MDPF functions, so any fix routes to MDPF through the CTO.
</preflight>

Base checks, dry-run by the issuer before the cut: CTae2-AC1 base: FAIL as expected (the file does not exist); CTae2-AC2 base: FAIL as expected (the file does not exist).
Source: CTO round-14 analysis ruling 2 (`ledger/ROUND_ANALYSIS.round14.md` @affd2fab43); row W94-S1.
