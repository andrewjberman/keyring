# TO NFRA_CTLPLN.TO-CT-k-1 -- workstream KIT round 1 CT-k-1 (URGENT): the trading calendar's fallback covers 2010 on, and an uncovered year raises

<to_id>NFRA_CTLPLN.TO-CT-k-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~12</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>KIT</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-k-1` (`decompositions/NFRA_CTLPLN_DECOMP.kit1.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-k-1`, the CTO's RULING B (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_FOR_THE_DELLS_20261007_0850Z_TRADING_CALENDAR_AND_ROW_IDS.md`,
msg 106080), verbatim:
"1. NYSE closures from 2010-01-01 generated on the laptop from the installed package and committed as the fallback's data, with the
generating command and the package version in the file's header, and one check that the generated set equals the package's answer for
every year it covers. 2. `calendar_source()` fails closed: a date outside the years the active source covers raises, naming the source
and the year. A silent trading-day answer for an uncovered year is the defect." And: "The cell's first read is a census: of the 103
importing files, which run in a deployed runtime that lacks the package today, because fail-closed changes what those do the next time
they are rebuilt."

**The defect, reproduced on the laptop at the cut:** `lib/trading_calendar.py` uses `pandas_market_calendars` when it imports, else a
hardcoded holiday set for 2024-2027. With the package forced off (`_USE_PMC = False`), `is_trading_day('2015-01-01')` returns `True`
and `is_trading_day('2012-10-29')` returns `True` (New Year's Day; the first Hurricane Sandy closure). Both Dells lack the package, so
every count over a pre-2024 date there is wrong, with no error. The laptop has `pandas_market_calendars` 5.4.0.

**What exists:** `lib/trading_calendar.py` (197 lines; the estate's ONE trading-day definition; the public functions and
`calendar_source()` are listed in its docstring; `NYSE_HOLIDAYS_FALLBACK` is a `frozenset[str]` of ISO dates, with the alias
`_NYSE_HOLIDAYS_FALLBACK`; Lambdas vendor this ONE file, so it must stay a single importable file with no new import beyond the
standard library and the optional package), and `lib/tests/test_trading_calendar.py` (22 tests, all passing at the cut).

**FIRST READ (before you change anything; it is half the deliverable):** the census of importers. Find every tracked file that imports
or vendors the module (`import trading_calendar`, `from trading_calendar`, `lib.trading_calendar`, `_trading_day_calendar`, a copied
file of the same name, and any packaging list that names it); print the count (the Dells reported 103; yours is the measurement). For
each, classify by a table you write into your deliverables folder as `TRADING_CALENDAR_IMPORTERS.md`: `LOCAL-TOOL` (a CLI or script run
on a box), `LAMBDA` (packaged into a function: name the function and the packaging file), `EC2-OR-CONTAINER` (a pipeline script run on
an instance or task), `TEST`, `DOC-OR-OTHER`; and, for each deployed kind, whether its runtime carries `pandas_market_calendars`
(read its requirements file, layer or packaging list; `UNKNOWN` is a value, counted, never guessed) and whether it passes dates before
2024 or after 2027 (read the call sites; `UNKNOWN` allowed). The table's last lines give the denominators and the list of deployed
importers that LACK the package: those are the ones whose behaviour changes at their next rebuild.

**Build, all inside `lib/trading_calendar.py` unless named otherwise:**

1. `lib/tests/gen_nyse_closures.py` -- the generator. For each year from 2010 through the last year the fallback covers today (2027),
   it asks `pandas_market_calendars` for the NYSE's FULL-DAY closures on weekdays: every weekday in the year that is not in the
   calendar's valid trading days (this catches regular holidays AND special closures such as a storm or a day of mourning; an early
   close is a trading day and is not a closure). It prints the set as Python source, grouped by year with the count per year, and can
   write it into the module between two marker comments (`# BEGIN GENERATED NYSE CLOSURES` / `# END GENERATED NYSE CLOSURES`).
2. The module's `NYSE_HOLIDAYS_FALLBACK` becomes that generated set (2010-2027), with a header comment above it naming the generating
   command, the package version (5.4.0) and the date. The 2024-2027 members must be exactly the ones the file holds today unless the
   package disagrees: if it does, STOP and file a BLOCKING row naming each differing date; do not pick a side. Two new module
   constants, derived from the data: `FALLBACK_FIRST_YEAR` and `FALLBACK_LAST_YEAR`. The alias `_NYSE_HOLIDAYS_FALLBACK` stays.
3. Fail closed. A new exception `CalendarCoverageError(ValueError)`. When the ACTIVE source is the fallback, every public function
   that answers about a date raises it for a date whose year is outside `FALLBACK_FIRST_YEAR..FALLBACK_LAST_YEAR`, naming the source
   and the year (for a range function, any date of the range; `prev_trading_day` and the functions built on it raise if the walk
   would leave the covered years). When the active source is the package, behaviour is unchanged. `calendar_source()` keeps its
   no-argument form and returns the covered range in its string for the fallback (`NYSE/hardcoded-fallback-2010-2027`), and gains an
   optional `date` argument that raises the same error for an uncovered year. Check every in-repo reader that compares the OLD
   provenance string `NYSE/hardcoded-fallback-2024-2027` literally (search for it): list each in your report; you edit none outside
   your grant, and a reader that would break is ONE surprise row.
4. `lib/tests/test_nyse_fallback_equals_package.py` -- per year 2010-2027, the committed set's members for that year equal the
   package's closures for that year, computed the generator's way; prints one line per year and LAST
   `NYSE-FALLBACK years=18 equal=<k>/18 first=2010 last=2027 closures=<n> ok=<True|False>`. It also asserts the 2012-10-29 and
   2012-10-30 storm closures and the 2018-12-05 day of mourning are members (special closures are the ones a rule-based list misses).
5. `lib/tests/test_trading_calendar_fail_closed.py` -- with the package forced off inside the test (set the module's `_USE_PMC` to
   False, restore after): 2015-01-01 is not a trading day; 2012-10-29 is not a trading day; 2015-01-02 is; a 2009 date raises
   `CalendarCoverageError` naming 2009; a 2028 date raises; a range from 2009-12-30 to 2010-01-05 raises;
   `calendar_source()` reads `NYSE/hardcoded-fallback-2010-2027`; and with the package ON, a 2009 date answers without raising. LAST line
   `CALENDAR-FAIL-CLOSED cases=<k>/8 ok=<True|False>`.

### ACCEPTANCE

<criterion id="CTk1-AC1" cell_refs="CT-k-1"><invocation>python lib/tests/test_nyse_fallback_equals_package.py</invocation><expect>NYSE-FALLBACK years=18 equal=18/18 first=2010 last=2027</expect></criterion>
`CTk1-AC1` -- the committed fallback equals the package's answer for every year it covers. The same line must read `ok=True`.

<criterion id="CTk1-AC2" cell_refs="CT-k-1"><invocation>python lib/tests/test_trading_calendar_fail_closed.py</invocation><expect>CALENDAR-FAIL-CLOSED cases=8/8 ok=True</expect></criterion>
`CTk1-AC2` -- without the package, a pre-2024 holiday is no longer a trading day and an uncovered year raises instead of answering.

<criterion id="CTk1-AC3" cell_refs="CT-k-1"><invocation>python -m pytest lib/tests/test_trading_calendar.py -q -p no:cacheprovider --color=no</invocation><expect>22 passed</expect></criterion>
`CTk1-AC3` -- the control on the real neighbour: the module's own 22 tests still pass. If a test asserts the old provenance string,
that test is in your grant: update that one assertion and say so; the count stays 22.

<expected_criteria>CTk1-AC1,CTk1-AC2,CTk1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No deploy, no push, no AWS call, no package install, no network fetch.** The data comes from the package installed on this box.
- `lib/trading_calendar.py` stays ONE file, ASCII only, importable with the standard library alone when the package is absent.
  No change to any public function's signature beyond the optional `date` argument; no change of behaviour when the package is active.
- You edit no importer. A deployed importer that will start raising is reported in the census table, not patched.
- Every `.py` you touch passes `.tools/commit-gate.sh` (the commit runs it). The commit gate runs ruff: avoid ambiguous
  single-letter names such as `l`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W12-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or the
  expected value.

<paths>
lib/trading_calendar.py
lib/tests/gen_nyse_closures.py
lib/tests/test_nyse_fallback_equals_package.py
lib/tests/test_trading_calendar_fail_closed.py
lib/tests/test_trading_calendar.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: every importer, every packaging or requirements file, `lib/README.md`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.kit1.md</decomp_doc> (workstream KIT, round 1), cell `CT-k-1`.
<owned_cells>CT-k-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CTk1-AC1, CTk1-AC2, CTk1-AC3. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~12/NFRA_CTLPLN.TO-CT-k-1.trading-calendar-fail-closed.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CTk1-AC1,CTk1-AC2,CTk1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three last lines; the census (importer count, count per class, the deployed importers that lack the package, the
UNKNOWN count); closures per year; any 2024-2027 date where the package and the old set differ; every literal reader of the old
provenance string; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing; the importers' own schedules are read in the census, not changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a fallback generated wrongly and trusted (per-year equality against the package, with three named special closures asserted); a fail-closed change that takes down a deployed consumer at its next rebuild (the census names every deployed importer lacking the package BEFORE anything is deployed; this cell deploys nothing); a silent answer surviving in one function (eight cases incl. a range and the package-on control); a provenance string compared literally elsewhere (searched, listed, rowed); BLIND: an importer's runtime that cannot be read from the repo (UNKNOWN counted) and the Dells themselves, which run the fix only after they pull the trunk.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: CTO RULING B (file above, msg 106080); CLAUDE.md hard stop "NEVER call a pipeline stale/broken until you resolve the TRADING
CALENDAR" (one frontier: `lib/trading_calendar.py`); decomposition KIT round 1. Base dry-run at the cut: CTk1-AC1 and
CTk1-AC2 base FAIL as expected (neither file exists; the defect itself reproduced: package off, 2015-01-01 reads a trading day);
CTk1-AC3 base PASS as expected (ran: 22 passed).
