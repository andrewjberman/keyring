# TO MDPF_SECCLASS.TO-SC-e101 -- round 25 SC-e-101: the re-based acceptance read (bars, advisors, totals, the D1-S27 bound) with a baseline captured from the served objects now

<to_id>MDPF_SECCLASS.TO-SC-e101</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~91</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-101` (`decompositions/MDPF_SECCLASS_DECOMP_R25.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none | **source:** CTO round-24 analysis section 4 item 1, msg 5506

---

## WORKER FACE

### THE CELL

`SC-e-101`. A gold job (C_06, then D_03 and D_04) rebuilds the Black Diamond firm and advisor mix objects every night. Round 24's acceptance script compared those
objects with a baseline taken on 2026-10-12, before two upstream restatements of the assets-under-administration (AUA) series, so its bars and advisors clauses read
FAIL against numbers that are stale. This cell builds the replacement read, and captures a NEW baseline from the served objects as they stand NOW. The issuer then runs
the read on the first scheduled fire after tonight's 23:00Z start. **Nothing is written to S3 or to a table: you read S3 and write repo files only.**

**One script**, `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R25_CHECKS/r25_rebase_read.py`, run from the repo root, three subcommands. Each prints ONE
verdict line; exit 0 when ok, 1 when not ok, 3 when the baseline file is absent. **Read first, in full:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R24_CHECKS/r24_legg_read.py`
(912 lines). It already reads every object you need through `lib/platinum_dest.source()` (never name a bucket), reads the AUA series
(`gold/timeseries/client_performance.parquet`, summed by date the way D_03 builds `cp_daily_total`) and grades the period bars. **Import it by path** with
`importlib.util.spec_from_file_location` and reuse its readers (`get_json`, `resolve_mode`, `canonical_six`, the AUA reader inside `cmd_e97`, the bar reader inside
`crit_bars`); do not copy them and do not edit it. If a function you need is buried inside `cmd_e97`, copy the few lines you need and cite the file:line.
Mode is `canonical` (the default of that module) for every read.

**The served objects (read through `source()`):** `gold/views/mix_daily_summary.json` (`firm[date]` = class dollars plus `total`; `advisors[advisor_key][date]` = the
advisor's day; `restated_through`), `platinum/firm/mix_summary.json` (also carries `restated_through`), `gold/artifacts/firm_mix_views.json` (the period bars), and
the AUA series. Five bars: `2026-Q3`, `2026-09`, `2026-Q4`, `2026-10`, `2026` (see `LABEL_MAP` in the r24 script).

**Subcommand `capture --out <path>`.** Reads the four sources and writes ONE JSON file (sorted keys, 2-space indent) with: `captured_at` (UTC ISO), `served` (for each of
the four sources: bucket, key, VersionId, LastModified), `restated_through`, `aua_by_date` (every date of the AUA series that is at or after `restated_through`),
`firm` (for each date at or after `restated_through`: the whole `firm[date]` dict), `advisor_days` (each advisor key to each date at or after `restated_through`
to that advisor's day TOTAL, the number the r24 `crit_advisors` compares), and `bars` (each of the five: its end date, its total, its class dollars, read the way r24
`crit_bars` reads them). Advisor keys appear exactly as the committed `R23_RADIUS/advisor_window_table.csv` has them; no client name, account id or relationship id
appears anywhere in the file. Print `R25-CAPTURE ok=<bool> dates=<n> advisors=<n> bars=<n> out=<path>`; `ok` is False if any of the five bars or any source is missing.

**Subcommand `read --baseline <path>`.** Reads the same four sources live and grades them against the baseline file. Definitions: `rt` = the live
`restated_through`; the WINDOW is every baseline date that is at or after `rt` and present in the live `firm`; `move(d)` = live AUA(d) minus baseline `aua_by_date`[d];
a date is STRICT when `abs(move) <= 1.00` and MOVED otherwise. Tolerances are named constants at the top of the script: `TOL_AUA = 1.00`, `TOL_ROUND = 250.00` (the
rounding the code carries; see the r24 constants and row D1-W85-S6), `TOL_S27 = 1000.00`. Clauses (each prints its own `R25-C <name> ok=<bool> ...` line):
1. `totals`: for every window date, `abs(live firm[d].total - live AUA(d)) <= TOL_AUA`.
2. `classes`: for every window date, the class key SET equals the baseline's. STRICT date: every class key (every numeric value of `firm[d]` except `total`) is within
   `TOL_ROUND` of its baseline value. MOVED date: `abs(sum over those class keys of (live - baseline) - move(d)) <= TOL_ROUND` (the move is conserved; nothing is claimed about
   which class takes it).
3. `advisors`: the live advisor key set equals the baseline's. For every window date: STRICT date, every advisor-day is within `TOL_ROUND` of its baseline value;
   MOVED date, `abs(sum over advisors of (live - baseline) - move(d)) <= TOL_ROUND`. A baseline advisor-day absent from the live object counts as a live value of 0.
4. `bars`: for each of the five bars: the live bar total equals the live AUA at the bar's live end date within `TOL_AUA`. If the live end date is also a baseline
   date at or after `rt`: the class dollars are graded as in clause 2 (strict or conserved with that date's move). If it is not (a new date), the classes are PRINTED and
   not graded, and the label is listed in `bars_ungraded=`.
5. `s27`: over EVERY live `firm` date, `abs(total - sum of every other numeric value of firm[d])` is at most `TOL_S27`. Print the maximum and its date. (This is the
   owner's bound for the share-rounding difference between C_06's total and its class sum.)
6. `restated`: `restated_through` is present on both `mix_daily_summary.json` and `platinum/firm/mix_summary.json` and equal on the two.
Summary line: `R25-REBASE ok=<bool> window=<n> strict=<n> moved=<n> dropped_from_window=<n> totals=<bool> classes=<bool> advisors=<bool> bars=<bool> s27=<bool> max_s27=<usd> restated=<bool>`;
`ok` is the AND of the six. `dropped_from_window` is the count of baseline dates before the live `rt`, printed and not graded (the window rolls forward every fire).

**Subcommand `selftest`**: the controls, with NO AWS call. Write each clause as a pure function over plain dicts so a fixture can drive it. Build fixtures FROM A
SMALL SYNTHETIC BASELINE you construct in the test (three dates, two advisors, three classes, two bars). POSITIVES (each must grade `ok=True`): live equals baseline;
one date MOVED by +300 with the total, one class (+300) and one advisor-day (+300) all moved by 300; one baseline date dropped below `rt`. NEGATIVES (each must grade
`ok=False` on exactly its own clause and no other): a total off the AUA by 5 (`totals`); on a STRICT date one class off by 1000 (`classes`); on a MOVED date a class moved by
300 + 1000 (`classes`, not conserved); one advisor missing from the live set (`advisors`); on a MOVED date the advisor sum moved by 300 + 1000 (`advisors`); a bar total
off the AUA by 5 (`bars`); a firm date whose total differs from its class sum by 1001 (`s27`); `restated_through` absent on one object (`restated`). Print
`R25-SELFTEST ok=<bool> positives=<n of n> negatives=<n of n>`.

### ACCEPTANCE

<criterion id="SC25-e101-AC1" cell_refs="SC-e-101"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R25_CHECKS/r25_rebase_read.py selftest</invocation><expect>R25-SELFTEST ok=True</expect></criterion>
`SC25-e101-AC1` -- every positive fixture grades ok and every negative fixture fails on exactly its own clause.

<criterion id="SC25-e101-AC2" cell_refs="SC-e-101"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R25_CHECKS/r25_rebase_read.py capture --out org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R25_CHECKS/baseline/REBASE_BASELINE_20261014.json</invocation><expect>R25-CAPTURE ok=True</expect></criterion>
`SC25-e101-AC2` -- the live capture writes the baseline file. Run it ONCE, today, and commit the file: it must be captured BEFORE 2026-10-14T23:00Z, because the next
scheduled fire rewrites the objects it reads. If you reach this step after 22:30Z, stop and report instead.

<criterion id="SC25-e101-AC3" cell_refs="SC-e-101"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R25_CHECKS/r25_rebase_read.py read --baseline org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R25_CHECKS/baseline/REBASE_BASELINE_20261014.json</invocation><expect>R25-REBASE ok=True</expect></criterion>
`SC25-e101-AC3` -- the live read against the baseline just captured grades ok with every date STRICT (nothing has moved between the two reads); the summary line prints
`moved=0` and the window count.

<expected_criteria>SC25-e101-AC1, SC25-e101-AC2, SC25-e101-AC3</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-14 ~12:5xZ): all three FAIL as expected (the script and the baseline file are absent). Every invocation must end inside
`timeout 120`; the round-24 `e97` read took 53 s in total, so `capture` and `read` fit. If one does not, run it with `run_in_background` and read its output when it ends.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, curl or tool fetch). pyarrow and pandas are already installed.
- **AWS is READ-ONLY** (get, list, head, list_object_versions): no write to any bucket or table, no deploy, no invoke. Never push.
- **Never edit** `data/black_diamond/`, `lib/`, `.tools/`, `R21_CHECKS`, `R22_CHECKS`, `R23_CHECKS`, `R24_CHECKS`, or the `R23_RADIUS/` files.
- **Client data stays out.** No client name or account id in the script, its output, the baseline file, the report or a surprise row.
- **Never type a dollar figure into the script** except the three tolerances above. Every expected value comes from the baseline file or the live objects.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id `MDPF_SECCLASS-D1-W91-S<k>`, `surfaced_at` =
  `date -u +%FT%TZ` at filing). Do not weaken a control.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R25_CHECKS/r25_rebase_read.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R25_CHECKS/baseline/REBASE_BASELINE_20261014.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R25.md</decomp_doc> (round 25), cell `SC-e-101`.
<owned_cells>SC-e-101</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC25-e101-AC1, SC25-e101-AC2, SC25-e101-AC3. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~91/MDPF_SECCLASS.TO-SC-e101.rebase-read-instrument.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC25-e101-AC1,SC25-e101-AC2,SC25-e101-AC3`.
</proof_of_spec>

**REPORT:** what you read (file:line for the AUA reader and the bar reader you reused), each criterion's output verbatim, the elapsed time of `capture` and `read`, the
fixtures and which clause each negative breaks, the count of dates, advisors and bars in the baseline, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only instrument schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE the reads the seat's role already makes (the same reads as SC-e-99).
comp-adversary: RUN -- a baseline taken from objects that were already wrong (the capture rests on leg Q: two C_06 re-derives of the current inputs rewrote 0 relationships and left the content equal; the baseline carries the VersionIds it read); a conserved-move clause that passes anything (the negative fixtures move by move+1000 and must fail); a window that silently shrinks (`dropped_from_window` is printed); an expected value typed into the script (forbidden). BLIND: class-level allocation of an AUA move (the read says conserved, not correct); D_03/D_04 timing within the fire chain.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-24 analysis section 4 item 1 (msg 5506); XA-20261014T014758Z-01a0; row D1-S36; leg Q (D1-S37, D1-S38); DECOMP_R25.
