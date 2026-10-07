# TO ADVI_COTBKF.TO-CB-e-1 -- round 5 CB-e-1: the three Commonwealth calendar readers refuse a calendar that does not cover their dates

<to_id>ADVI_COTBKF.TO-CB-e-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~17</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-e-1` (`decompositions/ADVI_COTBKF_DECOMP.round5.md`) |
**outcome_ref:** FWD-3, FWD-9 (rows S9, W12-S1) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-e-1`: three Commonwealth scripts measure distances in NYSE trading days through `lib/trading_calendar.py`:
`data/assets/scripts/silver/commonwealth_account_links.py`, `data/assets/scripts/analysis/commonwealth_price_census.py` and
`data/assets/scripts/analysis/commonwealth_price_need.py`. When `pandas_market_calendars` is absent (it is absent on this box, dell2),
the module falls back to `NYSE_HOLIDAYS_FALLBACK`, which lists holidays for 2024-2027 only, and `trading_calendar.calendar_source()`
returns `NYSE/hardcoded-fallback-2024-2027`. Every holiday before 2024 then counts as a trading day, with no error. Measured: the
account-links result on dell2 differs from the laptop's on 3 of 1,450 accounts for exactly this reason (row S9). The Commonwealth
tables reach back to 2013.

You make each of the three scripts **refuse to run** in that state: before it computes anything, when the calendar's covered years do
not include every year of the dates the script is about to measure, it exits non-zero and prints one line beginning exactly
`CALENDAR-UNCOVERED ` followed by the uncovered year span (for example `CALENDAR-UNCOVERED 2013..2023 source=NYSE/hardcoded-fallback-2024-2027`).
No silent run. A calendar that covers the dates (the laptop's, with the package) runs as today.

**Shape.** Put the decision in ONE new module, `data/assets/scripts/silver/commonwealth_calendar_guard.py`, imported by all three
(one rule, never three copies). Derive the covered years from the calendar module, never type them in the guard:
`calendar_source()` names the source; with the fallback the covered years are the years present in `NYSE_HOLIDAYS_FALLBACK`; with the
package, treat every year as covered. Do NOT edit `lib/trading_calendar.py`: the shared fix is another project's cell (laptop
`1.0.0_SA_CTO` ruling B, 08:5xZ), and your guard must keep working after it lands.

**Where the check sits in each script:** after the script knows the date span it will measure (the transactions' earliest and latest
date, or the census window) and before the heavy work or any output write. The script must not write an output file when it refuses.

**Tests** `data/assets/scripts/silver/tests/test_commonwealth_calendar_guard.py` (no AWS, no data files): a stubbed calendar covering
2024-2027 refuses a 2013-2023 span and names `2013..2023`; the same stub admits a 2024-2026 span; a stub standing for the package admits
2013-2026 (the difference control: the same span, two calendars, opposite answers).

**HOLD you work under (laptop `1.0.0_SA_CTO` ruling A, 08:5xZ):** nothing dated before 2024 is produced on this box through the calendar
until the shared fix lands. So never run the three scripts to completion with an output you keep: the criterion's check runs them with
all output in a temporary directory that is deleted on exit, and after your change they refuse before writing anything.

### ACCEPTANCE

<criterion id="CB5e1-AC1" cell_refs="CB-e-1"><invocation>python "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/checks/check_e1_calendar_refusal.py"</invocation><expect>CALENDAR-REFUSAL refused=3 of 3</expect></criterion>
`CB5e1-AC1` -- on dell2 as it is, each of the three scripts exits non-zero and prints its `CALENDAR-UNCOVERED` line (the check counts them).

<criterion id="CB5e1-AC2" cell_refs="CB-e-1"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_calendar_guard.py</invocation><expect>passed</expect></criterion>
`CB5e1-AC2` -- the guard on stubbed calendars, with the difference control above.

<expected_criteria>CB5e1-AC1,CB5e1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scratch under `.scratch/`, uncommitted.
- **No S3 write, no `--apply`, no edit to `lib/trading_calendar.py`, no package install** (a PyPI install is egress off Opal infrastructure).
- **Rule 13:** DS-lane scripts; your commit is a candidate.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W17-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_calendar_guard.py
data/assets/scripts/silver/tests/test_commonwealth_calendar_guard.py
data/assets/scripts/silver/commonwealth_account_links.py
data/assets/scripts/analysis/commonwealth_price_census.py
data/assets/scripts/analysis/commonwealth_price_need.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round5.md</decomp_doc> (round 5), cell `CB-e-1`.
<owned_cells>CB-e-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB5e1-AC1, CB5e1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~17/ADVI_COTBKF.TO-CB-e-1.calendar-refusal.proof_of_spec.json`, validated with
`python .tools/proof-of-spec-check.py <instance> CB5e1-AC1,CB5e1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the CALENDAR-REFUSAL line with each script's CALENDAR-UNCOVERED line, the test count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE code only; no schedule touched.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; denominator 0 principals; BLIND: none needed.
comp-adversary: RUN -- the guard must not be a second calendar (covered years derived from trading_calendar, never typed); the check must persist nothing (ruling A); BLIND: deployed runtimes importing these scripts (none known; the laptop census of the 103 importers is ruling B's).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-4 analysis @e363a194ed, E1 and section 1; rows S9, W12-S1, S10; laptop `1.0.0_SA_CTO` rulings A-B 08:5xZ (msg 178).
