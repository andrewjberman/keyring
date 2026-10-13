# TO MDPF_SECCLASS.TO-SC-e99 -- round 24 SC-e-99: the two leg-G instruments (SC-e-91's first-fire read and SC-e-97's acceptance read), read-only, with controls

<to_id>MDPF_SECCLASS.TO-SC-e99</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~89</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-12</issued_date>
<status>in_progress</status>
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
  1. `unclassified_window`: for each of 2026-09-30..2026-10-06, the D_04 remainder lies in `-250 .. bound+250` (amendment 1; the bound is the largest per-date rebuilt
     Unclassified of the SC-e-96 record, `WINDOW_READ_C06_ROLLING_20261012.json`, `per_date[].rebuilt_unclassified`: read the maximum from that file
     rather than typing it) plus $250;
  2. `w86_s5_remainder`: for 2026-10-03, 10-04, 10-05 the absolute difference between the stored `unclassified` key and the D_04 remainder is under $250 (amendment 1;
     it was about $6.5M);
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

### AMENDMENT 1 -- the tolerances are the rounding the code carries, and the idempotence count is C_06's keys only (issuer 2.0.0_SA_COO~M1, 2026-10-12 ~21:3xZ; answers your rows MDPF_SECCLASS-D1-W88-S1..S6)

Your stop was right and your report is exact: the order's own positive fixture cannot pass the order's own criteria, so the fault is in the order, not
in your script. The cause is one thing I wrote twice: I took the six-place rounding the code carries (row D1-W85-S6: up to $128.58 per snapshot) as
if it were absent from the post-act objects. It is not, and it moves the remainder and the key by a few dollars to about $170 a day.
1. **`unclassified_window` (your S2).** The lower bound is `-250`, not `0`: the criterion is `-250 <= remainder <= bound_max + 250` for each of
   2026-09-30..2026-10-06. A rebuild that places every dollar leaves a remainder of a few dollars either side of zero (the radius shows -$42.15 on 10-06,
   whose rebuilt Unclassified is $0.00). The CTO's "$0 to $53,010.45" is read with that rounding, as every other tolerance in the pair is.
2. **`w86_s5` (your S3).** The tolerance is `$250`, not `$1.00`: the criterion is `|stored unclassified key - D_04 remainder| < 250` on 2026-10-03,
   10-04 and 10-05. The defect it guards is about $6.5M; the post-act key and remainder still differ by the same rounding ($3.94 to $166.72 in your
   fixture, $69.72 at 10-09 in the radius). Keep your fixture's key set to the remainder only if that is what you did; say which in the report.
3. **`--since` idempotence count (your S5).** Count only the keys C_06 writes: under `gold/entities/clients/` and under `gold/client_timeseries/`
   the keys whose name after the prefix has NO further `/` and ends `.json` and does not end `_composition.json` (so `{rid}.json` and `{rid}_views.json`
   only). The subdirectory keys (`{rid}/detail.json`, `{rid}/aua_timeseries.json`, written by D_02 on every fire) are not C_06's and must not count.
   Print the count per prefix, the denominator per prefix and the page counts. The expected value of a second fire is still 0.
4. **Accepted as read:** S1 (the bound is the maximum of `per_date.rebuilt_unclassified` over the seven dates 2026-09-30..10-06, $53,010.45; 10-09's
   $883,483.05 is not in that window), S4 (the five per-class bar figures come from the request's `Period bars` table because `bars.json` holds
   Unclassified only; name that section in the script), S6 (10-09's Reach is $653,857.12 and the re-derive's move is $962,919.40; both are right,
   they are different acts). Your row S2 (BLOCKING) is dispositioned by items 1 and 2.
5. **Re-run, then finish.** With items 1 to 3 the e97 positive fixture grades `ok=True` and every negative fails on exactly its own criterion
   (strict reading). Re-run AC1 to AC3, validate the proof instance (the `controls.mutant` check must fire), flip `complete` only when all three
   pass, commit with the same paths and report.
6. **Gate limb.** The issuer amends its own criteria without a CTO ruling; no gate limb grades an amendment to an existing order's criteria and
   `<status>` (this order declares `<placeholders>NONE`).

### AMENDMENT 2 -- the instruments read where the runner WRITES: the canonical destination (issuer 2.0.0_SA_COO~M1, 2026-10-13 ~01:3xZ; answers my own row MDPF_SECCLASS-D1-S33)

The order is reopened (in_progress) for one addition, and the fault is mine. Your instruments passed every control and then read the wrong place. Since the
FB-f-9 mode move (2026-10-12 06:18Z) the gold runner runs with `BD_PLATINUM_MODE=canonical`: `data/black_diamond/scripts/gold/lib/platinum_dest.py`
maps the SERVED classes (the keys `gold/entities/clients/*`, `gold/views/mix_daily_summary.json`, `platinum/firm/mix_summary.json`,
`gold/artifacts/firm_mix_views.json`, ...) to bucket `opal-data-49financial` under `advi/49financial/platinum/...`, while keys that are not a served
class (`gold/client_timeseries/*`, `gold/meta/client_timeseries_watermark.json`) stay in `opal-data-bd` unchanged. The first scheduled fire after
SC-e-91's ship (launch 2026-10-12T23:00:11Z, chain end 01:12:06Z) therefore wrote C_06's results to the canonical destination and left the legacy
objects your `e91` reads untouched: it printed `NO-CHANGE-SINCE-BASELINE` while 796 relationships (1,592 legacy keys, and the canonical keys) had moved.
Read first: `lib/platinum_dest.py` and `lib/platinum_dest_view.py` (the class table), and the issuer's read of that fire,
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/LEGG_E91_FIRST_FIRE_READ_20261013.json` (its numbers are your live controls below).
1. **Every served key is read through `source(key)`** of `lib/platinum_dest.py` (import it by path: insert the `gold` directory on `sys.path`;
   it imports only `lib.config` and `lib.platinum_dest_view`). Add `--mode canonical|legacy` to `e91` and `e97`, DEFAULT `canonical`; pass it to
   `source(key, mode)`. Print the (bucket, key) of every object read on its `E91-READ` / `E97-READ` line. Nothing in the script names a bucket: the
   mapping is the module's.
2. **`e91` takes `--fire-start T` (ISO UTC, required for the CHANGED comparison).** BEFORE = the newest version of each of
   `mix_daily_summary.json` and `platinum/firm/mix_summary.json` whose LastModified is earlier than T (`list-object-versions` on the mapped
   bucket/key); AFTER = the current version. If AFTER is BEFORE, print `E91-LEGG state=NO-CHANGE-SINCE-FIRE` and exit 3. Otherwise grade as in the order
   (the D_04 remainder fall at 2026-10-09 and 2026-10-08, the class census, `total_held`, `advisors_same`), with BEFORE's day values in place of the
   committed baseline's (print both and the difference of the two: they must be equal to the cent for the dates that had not moved).
3. **`in_range` is `0 <= fall <= bound + 250`** (the rounding the code carries, row D1-W85-S6; the issuer's read had 10-09 at $0.35 over). Also print,
   for EVERY firm day that changed between BEFORE and AFTER, the date, the fall and `named=<bool>` (whether the date is in `reach_bounds_usd`): an unnamed date
   that moved is printed, not graded (row D1-S33).
4. **`--since T` counts on both destinations**, C_06 keys only (the same filter as amendment 1): the canonical prefix of `gold/entities/clients/` as
   `source()` maps it (bucket and prefix printed) and `gold/client_timeseries/` in `opal-data-bd`. Print the count, denominator and pages per prefix.
5. **`e97` reads the same mapped objects** (the mix daily summary, the D_04 mix summary, `firm_mix_views.json`, the relationship JSONs for
   `added_dropped`) and the AUA source (`gold/timeseries/client_performance.parquet`: map it through `source()` as well and say what it maps to).
6. **Live controls (the order's new acceptance, in place of the old AC2):**
   `python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R24_CHECKS/r24_legg_read.py e91 --fire-start 2026-10-12T23:00:00Z --since 2026-10-12T23:00:00Z`
   must print `E91-LEGG state=CHANGED ok=True d10_09_fall=653857.47 d10_08_fall=629530.84` (to the cent; the figures are the issuer's read) and
   `keys_modified_since=3184` (1,592 canonical + 1,592 legacy; if the live count differs, say by how much and why: a later fire may have rewritten
   keys). The unnamed changed dates 2026-09-30..2026-10-07 print with `named=False`. AC3 (`e97` live) still prints `E97-ACCEPT shipped=False ok=False`
   because the canonical mix daily summary carries no `restated_through`. AC1 (`selftest`) gains three negatives: the legacy-mode read of an object
   that moved only at the canonical destination must NOT grade as unchanged by default; a fall of the bound plus $251 fails `in_range`; a canonical
   BEFORE equal to AFTER prints NO-CHANGE-SINCE-FIRE.
7. **Fresh session on a fresh worktree: slot ~89.** The earlier branch and worktree were removed at the drain; read your own earlier script from trunk
   (`R24_CHECKS/r24_legg_read.py`) and change it; do not rewrite it. Keep every amendment-1 behaviour.
8. **Gate limb.** The issuer amends its own criteria without a CTO ruling; no gate limb grades an amendment to an existing order's criteria and
   `<status>` (this order declares `<placeholders>NONE`).

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
