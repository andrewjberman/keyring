# TO IRPT_CUSTDY.TO-CU-c-1 -- round 3 CU-c-1 (E2): the hop-3 real-run wrapper -- one advisor's client-report documents to a FILE, run where the firm bucket is readable

<to_id>IRPT_CUSTDY.TO-CU-c-1</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~7</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~K2</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-c-1` (`decompositions/IRPT_CUSTDY_DECOMP.round3.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (rounds 1-2 code is at HEAD)

---

## WORKER FACE

### THE CELL

`CU-c-1`, item E2 of the CTO's round-2 analysis: "hop 3 on the real returns". FWD-1: one 49 Financial advisor's quarter-end client
reports, built by Opal from Schwab's records. The figures code exists:
`data/assets/scripts/gold/irpt_custody/client_report_figures.py` builds one client-report document per household (returns over
`RULED_PERIODS` QTD/YTD/1Y/SI; SI `HELD_CALENDAR_FIX` before 2024 under HOLD A, never calling `lib/trading_calendar.py` for a pre-2024
date; market value, holdings, activity, fees; every figure carries `source` `{table, partition, rows}`).
`data/assets/scripts/gold/irpt_custody/advisor_client_list.py` resolves an advisor's accounts and households from the ownership map
(`book_of`; a projection-refused account is UNCOVERED with reason `PROJECTION_REFUSED`, never raised).

**The constraint that shapes this cell:** the returns gold lives in the firm bucket `opal-data-49financial`, which is an explicit deny for
the dell2 user. So this wrapper is BUILT on dell2 and RUN on the laptop, and its whole output is ONE FILE that is carried back. On dell2 it
must record the AccessDenied in that file and exit nonzero -- never work around a deny.

**Build `data/assets/scripts/gold/irpt_custody/hop3_real_run.py`:**
1. CLI: `--advisor <slug>` (default none; required), `--as-of <YYYY-MM-DD>` (default `2026-09-30`), `--out <file.json>` (required),
   `--self-test`. Device-free. Read-only: no S3 write, and `client_report_figures`'s `--apply` path is never called.
2. The ownership map comes from `opal_naming.legacy_address('blackdiamond-platinum-49financial-ownership-map')` (registry row in
   `infra/logic/registry/legacy_addresses.json`); never type the key. Resolve the advisor's households and accounts with
   `advisor_client_list`'s functions (import them; no second copy). Uncovered accounts are listed with their reason and not computed.
3. Build the documents with `client_report_figures`'s functions (import them). Write ONE JSON file: `{"advisor", "as_of", "map_key",
   "run_at", "host_note", "households": [<client-report documents>], "uncovered": [{"account": <last 4>, "reason"}], "error": null|"..."}`.
   Every account anywhere in the file is masked to the last 4. Any exception, an AccessDenied included, is written to `error` and the
   process exits 1 -- the file is written in every case.
4. Print one summary line: `HOP3-REAL-RUN advisor=<slug> as_of=<d> households=<n> accounts=<n> uncovered=<n> held_si=<n> error=<none|class>`.
5. `--self-test`: run the wrapper end to end against a fixture map, fixture silver and fixture returns (inject the readers; no AWS), with
   one household holding a pre-2024 account; print, as the LAST line, `HOP3-REAL-RUN-SELFTEST file_ok=<True|False> masked_ok=<True|False>
   held_ok=<True|False> error_written_ok=<True|False>` (`error_written_ok`: a reader that raises AccessDenied still yields a file with
   `error` set and exit 1).
6. Tests `data/assets/scripts/gold/irpt_custody/tests/test_hop3_real_run.py` (pytest, `tmp_path`, insert the module's directory into
   `sys.path`; no `__init__.py`): the file shape; no unmasked account (no run of 8 or more digits in the file); an uncovered account is
   listed not computed; SI held for a pre-2024 inception; a raising reader still writes the file with `error` and exits 1.

### ACCEPTANCE

<criterion id="CU8-AC1" cell_refs="CU-c-1"><invocation>python -m pytest -q data/assets/scripts/gold/irpt_custody/tests/test_hop3_real_run.py</invocation><expect>passed</expect></criterion>
`CU8-AC1` -- the wrapper's behaviour on fixtures: shape, masking, uncovered, SI held, the error-in-file path.

<criterion id="CU8-AC2" cell_refs="CU-c-1"><invocation>python data/assets/scripts/gold/irpt_custody/hop3_real_run.py --self-test</invocation><expect>HOP3-REAL-RUN-SELFTEST file_ok=True masked_ok=True held_ok=True error_written_ok=True</expect></criterion>
`CU8-AC2` -- the seam end to end through the real CLI on fixtures. The real run is the laptop's (its FILE grades E2); on dell2 the real
neighbour is fenced (rows S4, S6).

<expected_criteria>CU8-AC1,CU8-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS call in tests or self-test.** You may run the real CLI once on dell2 to see the fence recorded in the file; write that file
  under `.scratch/` only, and never commit it. No S3 write, ever.
- **Never print or write a full account number.** Never edit another cell's or another project's file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `IRPT_CUSTDY-W7-S<k>`; a row's `disposition` is one of UNDER_INVESTIGATION | GRADUATED | DISMISSED_WITH_REASON | DECOMP_INVALIDATING),
  and do not weaken the test.

<paths>
data/assets/scripts/gold/irpt_custody/hop3_real_run.py
data/assets/scripts/gold/irpt_custody/tests/test_hop3_real_run.py
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.round3.md</decomp_doc> (round 3), cell `CU-c-1`.
<owned_cells>CU-c-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU8-AC1, CU8-AC2. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~7/IRPT_CUSTDY.TO-CU-c-1.hop3-real-run.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU8-AC1,CU8-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the self-test line, the summary line from a dell2 real run (with the recorded error class), the exact laptop command, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-off real run by hand on the laptop; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; built on dell2 with no AWS call in its checks; the laptop's run reads with the laptop profile under the standing fenced-read rule.
comp-adversary: RUN -- cross-firm (49financial only, lookup and legacy_address); read-only; masking enforced in code and test; BLIND: the real figures until the laptop FILE returns.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: round-2 analysis @10e64fe9df section 3 (gate 'S4 FILE lands' -> E2); rows S4, S6; decomposition round 3 constraints 1-4.
