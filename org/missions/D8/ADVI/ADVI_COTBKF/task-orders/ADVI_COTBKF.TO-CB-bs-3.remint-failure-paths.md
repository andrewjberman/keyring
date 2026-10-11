# TO ADVI_COTBKF.TO-CB-bs-3.remint-failure-paths -- round 71 CB-bs-3: the re-mint mode's failure paths as a record: what it leaves behind on each kind of failure

<to_id>ADVI_COTBKF.TO-CB-bs-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~118</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>71</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bs-3` (`decompositions/ADVI_COTBKF_DECOMP.round71.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This cell writes a RECORD of what the re-mint mode leaves behind when it fails. It runs the mode against NOTHING but the tests' faked
bucket. No AWS call.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_71_20261011.md` section 2 item 4 and section 3 item 3; the mode: `data/assets/scripts/silver/commonwealth_account_return_daily.py`,
`remint_days` and its helpers (`_remint_failure`, `served_day_hash`, `_read_key`, `check_pair_files`), the module docstring's entry for
`--remint`, and its help text; its tests `data/assets/scripts/silver/tests/test_commonwealth_ard_remint.py` (the versioned fake bucket
and every test); the producer's writers the mode calls, `emit_day` and `emit_method_row` in
`data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (read only: the order in which each writes its keys).

**Why.** The mode replaces named day files of a served table and, by design, rolls nothing back: on a failed read-back it stops, names
the keys written, and returns non-zero. The CTO accepts that as built, on one condition: the sign-off that uses it must name the
rollback per key and who runs it. That sign-off cannot be written until it is KNOWN, for each kind of failure, exactly what the bucket
holds afterwards.

**Your item.**

1. **Enumerate the failure points of a run that has passed every refusal and begun to write.** For each: where in the code (file and
   line), what the bucket holds afterwards (which keys are new, which are old, which are half of a pair: a day's `data.parquet`
   replaced and its `manifest.json` not, or the reverse), what the mode prints, what it returns, and what a person must do to restore
   the served table to its captured state (the copy of a captured version id, per key; the mode keeps versions and deletes nothing).
   At least these: a put of a day's data fails; the data lands and its manifest put fails; a day lands whole and its read-back hash
   differs; a day lands and its manifest's read-back check fails; a failure on the SECOND listed day after the first is whole; the
   sidecar put or read-back fails after all days landed; the method row's write or read-back fails; the process is killed between two
   puts (no handler runs: what the bucket holds and what was printed); a read (not a write) fails mid-check BEFORE any put (the run
   must leave nothing).
2. **Show each one, do not argue it.** For every failure point there is a test in the mode's test file that injects it into the fake
   bucket and asserts the bucket's state and the printed lines. Where a test already exists, name it. Where none does, ADD it to
   `test_commonwealth_ard_remint.py` (synthetic values; the fake bucket may gain a way to fail the n-th put or the n-th get; keep
   every existing `==`). A killed process cannot be tested by a handler: test it as "the put list at the moment of an exception the
   mode does not catch", and say that is what it is.
3. **If a test shows the mode leaves the table in a state its own printed lines do not describe** (a key written and not named, a
   half pair not flagged), that is a DEFECT of the mode: do NOT fix the mode (it is not in your grant); file the row and record the
   failure point as `DESCRIBED: false`. The record is worth more than a clean table.
4. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~118/REMINT_FAILURE_PATHS.json` and a short `.md` beside it that a person holding a sign-off can follow. Top-level keys, exactly:
   `mode`, `not_run_against_the_bucket` (true), `failure_points` (a list of `{"id", "where", "bucket_after", "half_pair", "printed",
   "returns", "restore", "test", "described"}`), `before_any_put` (the read-failure case), `tests_added`, `rollback_note` (who runs a
   restore and from what: the captured version ids; quoted from the mode's help text), `not_established`.

### ACCEPTANCE

<criterion id="CB71bs3-AC1" cell_refs="CB-bs-3"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests -q</invocation><expect>passed</expect></criterion>
`CB71bs3-AC1` -- the silver suite passes with the variable unset: 0 failed, 0 errors, 12 skipped as before.

<criterion id="CB71bs3-AC2" cell_refs="CB-bs-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~118/REMINT_FAILURE_PATHS.json',encoding='utf-8'));f=d['failure_points'];print('REMINT-FAILURE-PATHS points=%d with_a_test=%d half_pairs=%d described=%d not_described=%d tests_added=%d not_run_against_the_bucket=%s'%(len(f),sum(1 for x in f if x['test']),sum(1 for x in f if x['half_pair']),sum(1 for x in f if x['described']),sum(1 for x in f if not x['described']),len(d['tests_added']),d['not_run_against_the_bucket']))"</invocation><expect>REMINT-FAILURE-PATHS points=</expect></criterion>
`CB71bs3-AC2` -- every failure point is recorded with its test, whether it leaves half a pair, and whether the mode's own output
describes what it left. The issuer reads `not_described`.

<expected_criteria>CB71bs3-AC1,CB71bs3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **You do NOT edit the adapter or the producer.** Tests only. If a failure point shows a defect of the mode, record it and file the
  row; the fix is a later order.
- **The mode is NEVER run against S3.** No AWS call of any kind.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete.** No push. No `--refresh`. No vendor call
  (no Yahoo, no Bloomberg): the Yahoo cache on disk is read, never refreshed.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, tickers, a security's price or
  per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W118-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
data/assets/scripts/silver/tests/test_commonwealth_ard_remint.py
data/assets/scripts/silver/tests/
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round71.md</decomp_doc> (round 71), cell `CB-bs-3`.
<owned_cells>CB-bs-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB71bs3-AC1, CB71bs3-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~118/ADVI_COTBKF.TO-CB-bs-3.remint-failure-paths.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB71bs3-AC1,CB71bs3-AC2` BEFORE the flip. Both are mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** each failure point with where it is, what the bucket holds afterwards, whether it leaves half a pair, what is printed and returned, how a person restores, and the test that shows it; any point the mode's own output does not describe; tests added, by name; the pytest line; the `REMINT-FAILURE-PATHS` line; a statement that the mode was not run against the bucket; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE tests and a record; the mode is not run.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; tests fake S3.
comp-adversary: RUN -- every failure point is shown by a test that injects it and asserts the bucket's state, not argued from the code; a state the mode's output does not describe is recorded as a defect and not fixed here; the killed-process case is named for what the test can and cannot show; BLIND: real S3 partial-failure behaviour (a put that lands and whose response is lost) is not reproduced by a fake.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-71 analysis @efaa09a585 (msg 5458), section 3 item 3; `3.0.0_SA_CVO` REMEDIATION_v41 @76875db91b.
