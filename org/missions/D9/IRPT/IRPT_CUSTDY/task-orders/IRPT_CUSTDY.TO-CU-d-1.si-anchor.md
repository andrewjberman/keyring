# TO IRPT_CUSTDY.TO-CU-d-1 -- round 4 CU-d-1 (E1): the SI anchor -- custodian inception, else Opal's first data date labelled as such, none before 2010

<to_id>IRPT_CUSTDY.TO-CU-d-1</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~9</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~K2</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-d-1` (`decompositions/IRPT_CUSTDY_DECOMP.round4.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (the decomposition fixes the `si_anchor` field)

---

## WORKER FACE

### THE CELL

`CU-d-1`, item E1 of the CTO's round-3 analysis: the since-inception (SI) anchor. On real data (as-of 2026-09-30, one advisor, 14
accounts) `data/assets/scripts/gold/irpt_custody/client_report_figures.py` reported SI as `NO_DATA` on every account and household because
no anchor resolved. Round 2 also held SI for any pre-2024 inception (`HELD_CALENDAR_FIX`); that hold is lifted: `lib/trading_calendar.py`
now covers 2010-01-01 to 2027-12-31 and raises, naming the year, outside it.

**The ruling (CTO, verbatim order -- implement exactly this):**
1. the custodian's own account inception date, where the accounts file carries one;
2. otherwise the gold's first data date for that account, labelled on the report as `since <date>, the first date Opal holds`, NEVER as
   "since inception";
3. an account whose anchor is before 2010-01-01 reports SI as not available, with that reason; never guess past the calendar.
"A report that calls a data-start date 'inception' overstates what it measured."

**What exists (READ):** `client_report_figures.py` (the client-report contract, `RULED_PERIODS` from
`data/assets/scripts/gold/runners_49f/parity_period_returns.py` via `link()` / `period_window(period, asof, anchor)`); the accounts file it
reads (`household_id,account[,household_name[,inception]]`) and Schwab silver `dim_account` under `opal-data-assets/schwab/<master>/silver/`
(look for an open/inception date column -- that is rule 1's custodian date when present); the returns gold producer
`data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (`first_data_dates(s3, src, end, accounts, workers)`; the gold
manifest's `first_data_date`) for rule 2. The returns gold in `opal-data-49financial` is readable from dell2.

**The field (fixed by the decomposition; another cell reads it):** every account document carries
`"si_anchor": {"date": "<YYYY-MM-DD>"|null, "rule": 1|2|3|null, "label": "<text>", "status": "OK|NOT_AVAILABLE|NO_ANCHOR"}` with labels:
rule 1 `since inception <date>`; rule 2 `since <date>, the first date Opal holds`; rule 3 status `NOT_AVAILABLE`, label
`not available: data before 2010-01-01`; no anchor at all: rule null, status `NO_ANCHOR`. The SI return figure uses the anchor: computed
(status OK) for a rule-1 or rule-2 anchor on or after 2010-01-01; for rule 3 its status is `NOT_AVAILABLE`; for no anchor `NO_DATA`.

**Build:**
1. In `client_report_figures.py`: resolve the anchor per account by the ruling; write `si_anchor`; compute SI from it; retire the 2024 floor
   and the `HELD_CALENDAR_FIX` status (the status set becomes `OK | NO_DATA | WINDOW_NOT_RULED | NOT_AVAILABLE`); the household SI is not
   OK when any member's is not. Never call the calendar for a date before 2010-01-01.
2. A NEW script `data/assets/scripts/gold/irpt_custody/si_anchor_probe.py --accounts-from-advisor <slug> --as-of <d>` that resolves the
   advisor's accounts the way `hop3_real_run.py` does (import it; no second copy), resolves each anchor through `client_report_figures`, and
   prints one line per account (masked to last 4: anchor date, rule, status) then
   `SI-ANCHOR advisor=<slug> accounts=<n> rule1=<n> rule2=<n> rule3=<n> no_anchor=<n> labels_ok=<True|False>` (`labels_ok`: no rule-2
   anchor carries the word "inception").
3. Tests in a NEW file `data/assets/scripts/gold/irpt_custody/tests/test_si_anchor.py`: rule 1 wins over rule 2; rule 2 labelled exactly
   `since <date>, the first date Opal holds`; **a test that fails if a rule-2 account is labelled "inception"**; rule 3 for a 2009 anchor
   is `NOT_AVAILABLE` and the calendar is never called for it; a 2015 anchor computes SI. Update round 2's tests
   (`test_client_report_figures.py`, `test_client_report_held_si.py`) only where the retired floor or the new field requires; they must pass.

### ACCEPTANCE

<criterion id="CU10-AC1" cell_refs="CU-d-1"><invocation>python -m pytest -q data/assets/scripts/gold/irpt_custody/tests/test_si_anchor.py</invocation><expect>passed</expect></criterion>
`CU10-AC1` -- the ruling's three rules, the exact rule-2 label, the "inception" guard test, the 2010 floor, on fixtures.

<criterion id="CU10-AC2" cell_refs="CU-d-1"><invocation>python data/assets/scripts/gold/irpt_custody/si_anchor_probe.py --accounts-from-advisor matthew_gooch --as-of 2026-09-30</invocation><expect>labels_ok=True</expect></criterion>
`CU10-AC2` -- the seam against its REAL neighbour: the chosen advisor's real accounts, Schwab silver and returns gold on dell2. The per-rule
counts are reported, not graded.

<criterion id="CU10-AC3" cell_refs="CU-d-1"><invocation>python data/assets/scripts/gold/irpt_custody/tests/run_suite_check.py</invocation><expect>failed=0 errors=0</expect></criterion>
`CU10-AC3` (AMENDMENT 1) -- the whole `irpt_custody` suite on your branch, after merging CLOUD, reads 0 failed and 0 errors: retiring the
2024 floor must not leave `test_hop3_real_run.py` or `hop3_real_run.py --self-test` red (row W9-S3).

<expected_criteria>CU10-AC1,CU10-AC2,CU10-AC3</expected_criteria>

### AMENDMENT 1 (issuer, 2026-10-07 ~11:2xZ) -- disarms row IRPT_CUSTDY-W9-S3

Your first pass (e25f6f33ab, criteria AC1 and AC2 PASS) retired the 2024 floor, which leaves two tests in `tests/test_hop3_real_run.py`
(`test_file_shape`, `test_si_held_for_a_pre_2024_inception`) and the `held_ok` flag of `hop3_real_run.py --self-test` red: their fixture
is a 2019 first-data date, now on the calendar. Those two files are added to your grant. FIRST merge CLOUD into your branch
(`git merge CLOUD`; CLOUD carries round 4's other two cells -- `hop3_real_run.py` was changed by CU-d-2 @7361085932 and the suite
runner `tests/run_suite_check.py` landed @e05799d167). Resolve a conflict in the channel file by keeping BOTH sides' rows in order, and in
this order file by taking CLOUD's version. Then re-express the two tests and the self-test flag under the new rule (a 2019 anchor now
computes or reports by rules 1-3; nothing is `HELD_CALENDAR_FIX`), keep their intent, and do not skip or xfail. Then AC3.

### AMENDMENT 2 (issuer, 2026-10-07 ~11:3xZ) -- the CTO's ruling on row W9-S2 (msg 423), verbatim branches

Rule 1 now splits by whether Opal holds the opening date; print, per account, which branch it took (`branch=a|b|c|rule2|rule3|none`):
- **(a)** Opal's data covers the open date, and the days from opening to first funding show ZERO holdings (measure it: read the holdings
  between the open date and the first funded day): SI runs from first funding and IS since inception; label it
  `since inception (first funded <date>)`.
- **(b)** the open date precedes Opal's first partition: rule 1 yields to rule 2, label `since <date>, the first date Opal holds`, never
  "inception".
- **(c)** holdings exist before Opal's first partition: rule 2, as (b).
Real data (round-4 probe): 12 of the chosen advisor's 14 accounts are expected under (a), 2 (opened 2022) under (b) -- reported, not graded.
Tests (in `tests/test_si_anchor.py`): one per branch; the (a) label only when the zero-holdings read is confirmed; a (b)/(c) account is
never labelled "inception". The probe's per-account line adds `branch=`; its `labels_ok` also checks (b)/(c) carry no "inception".

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **AWS: read only** (Schwab silver, the returns gold, the ownership map via `legacy_address`). No write; never `--apply`.
- **Never print a full account number.** Edit `hop3_real_run.py` and `tests/test_hop3_real_run.py` only as AMENDMENT 1 says; never edit
  another cell's or project's file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `IRPT_CUSTDY-W9-S<k>`; `disposition` one of UNDER_INVESTIGATION | GRADUATED | DISMISSED_WITH_REASON | DECOMP_INVALIDATING), and do
  not weaken the test.

<paths>
data/assets/scripts/gold/irpt_custody/client_report_figures.py
data/assets/scripts/gold/irpt_custody/si_anchor_probe.py
data/assets/scripts/gold/irpt_custody/tests/test_si_anchor.py
data/assets/scripts/gold/irpt_custody/tests/test_client_report_figures.py
data/assets/scripts/gold/irpt_custody/tests/test_client_report_held_si.py
data/assets/scripts/gold/irpt_custody/hop3_real_run.py
data/assets/scripts/gold/irpt_custody/tests/test_hop3_real_run.py
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.round4.md</decomp_doc> (round 4), cell `CU-d-1`.
<owned_cells>CU-d-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU10-AC1, CU10-AC2, CU10-AC3. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~9/IRPT_CUSTDY.TO-CU-d-1.si-anchor.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU10-AC1,CU10-AC2,CU10-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the real `SI-ANCHOR` line with the per-rule counts, where rule 1's date comes from (file, column), the test list, rows, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE round 4 runs by hand; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; reads opal-data-assets, opal-data-bd and opal-data-49financial with the dell2 box profile (49financial measured readable ~10:44Z, msgs 358/367).
comp-adversary: RUN -- cross-firm (49financial only); read-only; the label guard is a test; BLIND: whether the custodian files carry an inception date (rule 1's source).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: round-3 analysis @ec25e39844 section 2 S8(a) and section 3 E1; HOLD A lift (msgs 317, 322); decomposition round 4 constraint 1 and the anchor field.
