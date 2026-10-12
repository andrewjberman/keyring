# TO MDPF_SECCLASS.TO-SC-e99 -- round 24 SC-e-99: the two leg-G instruments (SC-e-91's first-fire read and SC-e-97's acceptance read), read-only, with controls

<to_id>MDPF_SECCLASS.TO-SC-e99</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~88</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>24</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-99` (`decompositions/MDPF_SECCLASS_DECOMP_R24.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none | **source:** CTO round-23 analysis section 2 items 1 and 2, msg 4552

---

## WORKER FACE

### THE CELL

`SC-e-99`. Two timed reads follow BD fires: SC-e-91's **leg G** (the first scheduled fire after its 09:55Z ship) and SC-e-97's **acceptance** (the first
scheduled fire after its ship, which is a later act). The issuer performs both. This cell builds the INSTRUMENT for each, now, read-only, so that the
reads are mechanical when the fire lands. Nothing is written to S3 or to a table. The served objects are in bucket `opal-data-bd`.

**One script**, `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R24_CHECKS/r24_legg_read.py`, run from the repo root, three subcommands, each
printing ONE verdict line and exiting 0 when ok, 1 when not ok, 3 when the thing it reads has not happened yet. AWS reads go through `.tools/aws`
(`.tools/aws.cmd` on Windows, as `R23_CHECKS/e97_shipped_check.py` does: read it first). Every expected value comes from a COMMITTED file or the order
text below; **no dollar figure is typed into the script** except the two Reach bounds read from the baseline file.

**Committed inputs (read them with python; they are on your branch):**
- `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/LEGG_E91_PREFIRE_BASELINE_20261012.json` (keys: `served_versions` per object,
  `firm_days` for 2026-10-06..09 with `total`, `classes` and `d04_remainder_unclassified`, `advisor_count`, `reach_bounds_usd`).
- `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R23_RADIUS/`: `advisor_window_table.csv` (advisor_key, date, served_total, rebuilt_total,
  move), `added_dropped_top10.csv` (date, side added|dropped, rank, relationship_id, usd, store_status), `bars.json` (the four bars and the annual bar,
  total and class dollars before and after), `aua_vs_firm_by_date.csv`, `d04_unclassified_by_date.csv`.
- The request `NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_ROLLING_REDERIVE_20261012.md` (same folder as the baseline): its `Totals and AUA` and
  `Period bars` sections say where the AUA and the bars come from (`D_03.composition_artifacts.py` :523 `cp_daily_total` and `lib/mix_views.py`
  :66-107); read them to replicate the AUA and the bar function.

**Subcommand `e91 [--since <ISO UTC>]`** (SC-e-91's leg G):
- Reads the live `gold/views/mix_daily_summary.json`, `platinum/firm/mix_summary.json` and `gold/meta/client_timeseries_watermark.json` (VersionId,
  LastModified, ETag via head-object) and compares to the baseline's `served_versions`. If the `mix_daily_summary.json` VersionId equals the baseline's,
  print `E91-LEGG state=NO-CHANGE-SINCE-BASELINE` and exit 3 (a fire that moved nothing and no fire at all look the same here; the line says so).
- Otherwise: for 2026-10-09 and 2026-10-08, the D_04 remainder (`total` minus the six canonical classes present in `firm[date]`, the rule of
  `D_04.client_portal_summary.py` :440-462; import `CANONICAL_MIX_CLASSES` from that module if it imports cleanly without side effects, else
  read the list from its source by AST) now against the baseline; the FALL is `baseline - now`. Reach: `0 <= fall <= reach_bounds_usd[date]`
  (to the cent); outside is `in_range=False` (a STOP). Also print: the class CENSUS (the set of class keys across `firm[date]` for 2026-10-06..09 now
  against the baseline's: any NEW key is `census_new=<keys>`), `total_held` (each date's `total` equals the baseline's: a re-class moves dollars
  between classes and leaves the total), `advisor_keys_same` (56 against `advisor_count`), and the D_04 page's own `Unclassified` line now against the
  baseline's `mix_summary_unclassified_line` (a printed figure, not graded: `platinum/firm/mix_summary.json` is rewritten by D_04, which may not
  have run).
- Verdict line: `E91-LEGG state=CHANGED ok=<bool> d10_09_fall=<usd> d10_08_fall=<usd> in_range=<bool> census_new=<n> total_held=<bool>
  advisors_same=<bool>`; `ok` is the AND of in_range, census_new == 0, total_held and advisors_same.
- With `--since T` it ALSO prints the idempotence line `E91-LEGG-B keys_modified_since=<n> of <N>` (list-objects-v2 over `gold/entities/clients/`,
  paginated to exhaustion, counting keys whose LastModified is at or after T) and `mds_unchanged_since=<bool>` (the `mix_daily_summary.json`
  LastModified before T). The SECOND fire's expected value is 0 keys and True. The page count and denominator are printed.

**Subcommand `e97`** (the CTO half's post-ship acceptance and the COO half's conditions 9 and 10; read it in
`NEVER_WIDEN_CTO_HALF_SECCLASS_C06_ROLLING_REDERIVE_20261012.md` ADDENDUM 2 and the COO half's addendum 1):
- Reads the live `mix_daily_summary.json`; if it carries no `restated_through` key, print `E97-ACCEPT shipped=False ok=False` and exit 3 (the
  ship has not read back). Otherwise grade ALL of these and print one line per criterion then the summary:
  1. `unclassified_window`: for each of 2026-09-30..2026-10-06, the D_04 remainder lies in `0 .. 53010.45` (the bound is the largest per-date rebuilt
     Unclassified of the SC-e-96 record, `WINDOW_READ_C06_ROLLING_20261012.json`, `per_date[].rebuilt_unclassified`: read the maximum from that file
     rather than typing it) plus $250;
  2. `w86_s5_remainder`: for 2026-10-03, 10-04, 10-05 the absolute difference between the stored `unclassified` key and the D_04 remainder is under $1.00
     (it was about $6.5M);
  3. `totals_equal_aua`: for each of the 15 window dates 2026-09-25..2026-10-09, `firm[date].total` equals the AUA within $1.00. The AUA is the
     `client_performance` source the request names (`gold/timeseries/client_performance.parquet`; read it with pyarrow or pandas the way D_03 builds
     `cp_daily_total`, citing the file:line you replicated, and state the column you used);
  4. `bars`: from the served `gold/artifacts/firm_mix_views.json` the Q3 2026 and September 2026 bars (end 2026-09-30): the bar total equals the
     `before` total of `bars.json` (it does not move) and each class dollar is within $250 of the `after` figure of `bars.json`; the same for
     Q4 2026, October 2026 and 2026 annual (end 2026-10-09);
  5. `restated_through`: equals `2026-09-25` on `mix_daily_summary.json` AND on `platinum/firm/mix_summary.json`;
  6. `advisors`: the advisor key set equals the baseline's 56; every (advisor_key, date) row of `advisor_window_table.csv` has the served advisor-day
     total within $250 of the `rebuilt_total` (a row with no served day and a rebuilt of 0 is fine); print the count of rows beyond $250;
  7. `added_dropped`: for every row of `added_dropped_top10.csv`, read the stored `gold/entities/clients/{relationship_id}.json` and check the date is
     PRESENT for `added` rows and ABSENT for `dropped` rows (the radius's lists); print the denominator (the count of rows read) and the count
     that disagree. Bounded concurrency; read each JSON once.
- Summary: `E97-ACCEPT shipped=True ok=<bool> unclassified_window=<bool> w86_s5=<bool> totals_aua=<bool> bars=<bool> restated=<bool>
  advisors=<bool> added_dropped=<bool>`; `ok` is the AND of the seven.

**Subcommand `selftest`**: the instruments' controls, with no AWS call. Structure each grader as a pure function over plain dicts (the served
objects loaded by a separate reader) so a fixture can drive it. Build fixtures FROM THE COMMITTED FILES: a synthetic "post-act" served object set made
from the baseline plus the radius tables (each window date's total set to the AUA of `aua_vs_firm_by_date.csv`, the remainder set to
`d04_unclassified_by_date.csv`'s after, advisor-days set to `advisor_window_table.csv`'s rebuilt, `restated_through` set) must grade `ok=True`
for `e97`; for `e91` a synthetic fall inside the range grades `ok=True`. Then NEGATIVE controls, each must grade `ok=False` on exactly its own
criterion: a 10-09 fall of the bound plus $1 (`in_range`), a new class key (`census`), a window date's total off the AUA by $5
(`totals_equal_aua`), a W86-S5 gap of $50 (`w86_s5`), a bar class $1,000 off (`bars`), a missing advisor key (`advisors`), a dropped relationship that
still carries its date (`added_dropped`), and `restated_through` absent (`shipped=False`). Print `R24-SELFTEST ok=<bool> positives=<n of n>
negatives=<n of n>`.

### ACCEPTANCE

<criterion id="SC24-e99-AC1" cell_refs="SC-e-99"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R24_CHECKS/r24_legg_read.py selftest</invocation><expect>R24-SELFTEST ok=True</expect></criterion>
`SC24-e99-AC1` -- every positive fixture grades ok and every negative fixture fails on exactly its own criterion.

<criterion id="SC24-e99-AC2" cell_refs="SC-e-99"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R24_CHECKS/r24_legg_read.py e91</invocation><expect>E91-LEGG state=NO-CHANGE-SINCE-BASELINE</expect></criterion>
`SC24-e99-AC2` -- run against the LIVE served objects as they are today (no fire has run the shipped C_06), the e91 instrument reads the baseline versions and prints the no-change state, exit 3, writing nothing.

<criterion id="SC24-e99-AC3" cell_refs="SC-e-99"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R24_CHECKS/r24_legg_read.py e97</invocation><expect>E97-ACCEPT shipped=False ok=False</expect></criterion>
`SC24-e99-AC3` -- run against the live served objects as they are today (the ship has not happened, no `restated_through`), the e97 instrument prints shipped=False and ok=False, exit 3, writing nothing.

<expected_criteria>SC24-e99-AC1, SC24-e99-AC2, SC24-e99-AC3</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-12 ~21:0xZ): all three FAIL as expected (the script is absent). The served objects read the baseline
versions (`mix_daily_summary.json` VersionId `VrrTn2RrESHBImlLOMHQbNP6Fvzi9NZD`, no `restated_through` key), so AC2 and AC3 are reachable.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment). pyarrow and
  pandas are already installed (the SC-e-95 and SC-e-96 workers used them).
- **AWS is READ-ONLY** (get, list, head, list_object_versions): no write to any bucket or table, no deploy, no invoke. Never push.
- **Never edit** `data/black_diamond/`, `lib/`, `.tools/`, `R21_CHECKS`, `R22_CHECKS`, `R23_CHECKS`, the baseline or the radius files.
- A command that needs more than `timeout 120` runs in the background (`run_in_background`) and is read when it ends; the `added_dropped` read is
  up to about 300 small GETs: bound the concurrency (8) and print the elapsed time.
- **Client data stays out.** Relationship ids are opaque identifiers and the radius files already carry them; no client name or account id in the
  script, its output, the report or a surprise row. Advisor keys appear only as the committed table has them.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W88-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken a control and do not type a figure.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R24_CHECKS/r24_legg_read.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R24.md</decomp_doc> (round 24), cell `SC-e-99`.
<owned_cells>SC-e-99</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC24-e99-AC1, SC24-e99-AC2, SC24-e99-AC3. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~88/MDPF_SECCLASS.TO-SC-e99.legg-read-instruments.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC24-e99-AC1,SC24-e99-AC2,SC24-e99-AC3`.
</proof_of_spec>

**REPORT:** what you read (file:line for the AUA source and the bar function), each criterion's output verbatim, the elapsed time of `e97` and of its
`added_dropped` read, the list of the fixtures and which criterion each negative breaks, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only instrument schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE reads the seat's role already makes (the same reads as SC-e-95, SC-e-96 and SC-e-98).
comp-adversary: RUN -- an instrument that passes on anything (every negative control must fail on exactly its own criterion); an expected value typed into the script (the order forbids it: every one is read from a committed file); a "no change" read mistaken for "a fire that moved nothing" (the line says it cannot tell them apart; the issuer reads the runner's C_06 telemetry beside it); a pass on the wrong object version (the verdict prints the VersionIds it read). BLIND: the runner's wall time and C_06's own log lines, which are telemetry and not served objects; the issuer reads those.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-23 analysis section 2 items 1 and 2 (msg 4552); COO half addendum 1 conditions 9 and 10; CTO half addendum 2; the baseline
(`5fb3dd235b`) and `R23_RADIUS/` (`ef7f425cc8`); DECOMP_R24.
