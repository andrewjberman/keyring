# TO NFRA_TRNSPT.TO-TR-f6 -- the FWD-4 completeness builder: every meeting occurrence is "here" or exactly one cause

<to_id>NFRA_TRNSPT.TO-TR-f6</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-f-6` (`decompositions/NFRA_TRNSPT_DECOMP_R6.md`) |
**outcome_ref:** FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-f-6` (CTO round-5 analysis @a8931c9d12, section 3, E2): "FWD-4, the completeness record: for each of the 4 meeting series and each
occurrence over the last 120 days, either 'here' or a cause ... a versioned record lists every occurrence with exactly one of: here /
never recorded / expired / refused / not allowlisted, with counts per series; ... a test refuses a row with no cause." PRD FWD-4 ACCEPT
(`org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md:44`): "for any meeting and date, the answer is 'here' or a cause (never
recorded, expired, refused); never a shrug".

You build the BUILDER and its test against a fixture. The issuer feeds it live inputs after your merge; you make no live call.

**Read-only context:**
- The four series: `data/transcripts/scripts/teams/series.json` (`table` = `monday_meeting`, `ocio_ic`, `asset_management_ic`,
  `research_meeting`).
- The allowlist data asset: `data/transcripts/scripts/teams/meeting_allowlist.json` (+ `meeting_allowlist.py` `load()`).
- Bronze layout: `data/transcripts/scripts/teams/land_bronze.py:69-71` -- `teams/transcripts/bronze/<series>/date=<YYYY-MM-DD>/<object>`.

**Build:**
1. `data/transcripts/scripts/teams/completeness.py`, stdlib only:
   - `build(inputs: dict) -> dict`. `inputs` is:
     ```
     {"as_of": "YYYY-MM-DD", "window_days": 120,
      "occurrences":       [{"series": "<table>", "date": "YYYY-MM-DD", "source": "<where the occurrence came from>"}],
      "series_refused":    {"<table>": "<source of the refusal>"},          # the series' transcript listing is refused (e.g. 403 not invited)
      "listed_now":        [{"series": "<table>", "date": "YYYY-MM-DD"}],   # transcripts Microsoft lists today
      "previously_listed": [{"series": "<table>", "date": "YYYY-MM-DD", "source": "..."}],  # evidence a transcript once existed
      "bronze":            [{"series": "<table>", "date": "YYYY-MM-DD"}],   # bronze objects present (date partitions)
      "live_allowlist":    ["<table>", ...]}                                # series the RUNNING gateway admits
     ```
     For every occurrence inside `[as_of - window_days, as_of]` it emits ONE row `{"series", "date", "cause", "basis"}` where `cause` is
     decided in THIS precedence order:
     1. `here` -- a bronze entry for that series and date;
     2. `refused` -- the series is in `series_refused`;
     3. `not_allowlisted` -- Microsoft lists it now (`listed_now`) but the series is not in `live_allowlist`;
     4. `expired` -- it is in `previously_listed` and not in `listed_now`;
     5. `never_recorded` -- none of the above.
     One case fits none of the five: Microsoft lists it now, the series IS in `live_allowlist`, and it is not in bronze (a pull miss).
     For it `build` raises `ValueError("unclassifiable: listed, allowlisted, not in bronze")`, so the issuer sees it; it never becomes
     `never_recorded` and never a sixth cause.
     `basis` is a short string naming which input decided it (e.g. `"bronze"`, `"series_refused: <source>"`).
     Returns `{"as_of", "window_days", "rows": [...sorted by series, date], "counts": {"<series>": {"<cause>": n}}}`.
   - `validate_rows(rows)` raises `ValueError` for a row whose `cause` is missing, empty, not one of the five, or a list/combined value
     (two causes); `build` calls it before returning.
   - `main()`: `--inputs <json> --out <json>`; writes the `build` result. Dates and series only -- never a subject, name or address.
2. `data/transcripts/scripts/tests/fixtures/completeness/inputs.json`: a SYNTHETIC fixture (invented dates, the four real series names)
   in which each of the five causes occurs at least once and at least one occurrence falls outside the window (and is dropped).
3. `data/transcripts/scripts/tests/test_completeness.py`, at least: `test_refuse_row_without_cause`,
   `test_refuse_row_with_two_causes` (both on `validate_rows`), a precedence test (an occurrence both in bronze and in `series_refused` is
   `here`), the window-drop test, the unclassifiable `ValueError`, and a test that the fixture run's per-series counts sum to its row count.

### ACCEPTANCE

<criterion id="TR6-f6-AC1" cell_refs="TR-f-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R6_CHECKS/r6_checks.py f6-build</invocation><expect>R6-F6-BUILD-OK</expect></criterion>
`TR6-f6-AC1` -- the builder on the shipped fixture gives every row exactly one of the five causes, all five appear, counts sum to rows.

<criterion id="TR6-f6-AC2" cell_refs="TR-f-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R6_CHECKS/r6_checks.py f6-test</invocation><expect>R6-F6-TEST-OK</expect></criterion>
`TR6-f6-AC2` -- the test file passes and holds the two refusal tests by name.

<expected_criteria>TR6-f6-AC1, TR6-f6-AC2</expected_criteria>

Dry-run at the base (CLOUD 94d866956b): AC1 `R6-F6-BUILD-FAIL absent`, AC2 `R6-F6-TEST-FAIL absent` -- FAIL as expected. The live record
and its one-traced-occurrence-per-cause are the issuer's close act.

## BOUNDS

- **Grant.** The three files above, this order's file, your deliverables folder and the investigation file. Nothing else is written.
  Do NOT edit any other proof instance or order (a `PENDING-THIS-COMMIT` value in another order's instance is not yours).
- **LOCAL.** No gateway, Graph, HTTP or AWS call. Synthetic fixture only.
- Run `python -m pytest data/transcripts/scripts/tests/test_completeness.py -q -p no:cacheprovider` from the worktree root.
- **Refusal clause.** If the precedence above cannot classify a fixture case, do not invent a sixth cause: raise, test the raise, and file
  a surprise row (id `NFRA_TRNSPT-D2-W1-S<k>`, next unused across every document under `surprise-channel/`; a dell2 worker id carries
  the `D2-` coordinate).

<paths>
data/transcripts/scripts/teams/completeness.py
data/transcripts/scripts/tests/test_completeness.py
data/transcripts/scripts/tests/fixtures/completeness/inputs.json
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ and
never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R6.md</decomp_doc> (round 6), cell `TR-f-6`.
<owned_cells>TR-f-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR6-f6-AC1, TR6-f6-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-f6.completeness-builder.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR6-f6-AC1,TR6-f6-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the fixture run's counts per series and cause, the two check lines, the test names, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- an offline builder; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- 6 files read (series.json, meeting_allowlist.json, land_bronze.py, pull.py, teams_route.py, the PRD); BLIND to the live calendar and Microsoft's transcript listing, which no repo file holds (the issuer's close inputs). Traps: a sixth "unknown" cause (a shrug), a guessed retention period, content in the record; the face fixes the vocabulary, makes expired evidence-based and limits the record to series and dates.
lane: three new files under data/transcripts/scripts/, the investigation file.
</preflight>

Source: CTO round-5 analysis @a8931c9d12 section 3 E2; decomposition round 6 cell TR-f-6 and issuer rulings 2-4.
