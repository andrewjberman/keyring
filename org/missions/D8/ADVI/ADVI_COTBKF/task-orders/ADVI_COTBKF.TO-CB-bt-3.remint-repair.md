# TO ADVI_COTBKF.TO-CB-bt-3.remint-repair -- round 72 CB-bt-3: the re-mint mode repaired: a key named written only after its put; half pairs flagged; the method row's manifest read back; an interruption prints its keys

<to_id>ADVI_COTBKF.TO-CB-bt-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~121</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>72</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bt-3` (`decompositions/ADVI_COTBKF_DECOMP.round72.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_72_20261011.md` section 2 item 3 and section 4 item 3; rows ADVI_COTBKF-D2-W118-S1, D2-W118-S2 and D2-W118-S3 in the channel;
the round-71 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~118/REMINT_FAILURE_PATHS.json` and its `.md` (18
failure points, 10 of them `described: false`); the mode: `data/assets/scripts/silver/commonwealth_account_return_daily.py`
(`remint_days`, `_remint_failure`, the write section); its tests `data/assets/scripts/silver/tests/test_commonwealth_ard_remint.py` (the
versioned fake bucket with its fault switches; the `test_failure_F*` tests, which today PIN the defective behaviour and carry
`# DEFECT (CB-bs-3):` comments).

**The ruling.** "The re-mint mode is REPAIRED, not papered over in a pair. ... The mode names a key as written only after its put
returns; flags a day or a method row whose two files are of different runs; reads the method row's manifest back and refuses on a
mismatch; and on any interruption, a kill included, prints the keys it had written before it exits. Each with a test that plants the
failure."

**Your item. No AWS call: tests fake S3. The mode is NEVER run against a real bucket.**

1. **A key is named written only after its put returns.** The mode calls the producer's `emit_day` and `emit_method_row`, each of which
   puts two keys; the producer is NOT in your grant. So the mode must learn what actually landed without trusting a list it built
   beforehand: after each call, and in every failure path, establish per key whether its served version changed (a `head_object`
   against the version id seen before the write) and print `WRITTEN` only for keys whose version moved, and `NOT-WRITTEN` for a key
   it attempted that did not. Say in the code comment why it is done by reading the bucket.
2. **Half pairs are flagged.** Whenever a day's `data.parquet` is of this run and its `manifest.json` is not (or the reverse), and the
   same for the method row's two objects, the mode prints one line beginning `HALF-PAIR` naming both keys and which is new, before
   it exits.
3. **The method row's manifest is read back** after its write and compared with what the producer returns for it; a mismatch stops
   the run as a read-back failure (non-zero, the keys printed), never the success line.
4. **Any interruption prints the keys written.** A `KeyboardInterrupt` or other `BaseException` raised during the write section is
   caught at the outermost level of the write section, the same per-key report is printed (from the bucket, as in 1), and the
   exception is re-raised. A hard kill cannot run a handler: say so in the docstring, and print one line BEFORE the first put,
   `REMINT-BEGIN keys=<n>` followed by one `WILL-WRITE` line per key in order, so an operator with only the log of a killed run
   knows exactly which keys to inspect.
5. **The tests change WITH the behaviour.** Every `test_failure_F*` test that pins a defect is updated to assert the repaired
   behaviour, and its `# DEFECT (CB-bs-3):` comment is removed; a test that already asserts correct behaviour stays as it is. Add a
   test for each of the four repairs that plants the failure (the fake's fault switches exist). Every refusal still fires before any
   put; the mode still deletes nothing and rolls nothing back; `--apply` is unchanged.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~121/REMINT_REPAIR.json`: top-level keys, exactly: `repairs` (a list of four `{"repair", "row", "where", "test"}`),
   `failure_points_now` (the 18 points of round 71 by id, each `{"id", "described", "half_pair_flagged", "test"}`),
   `still_not_described` (ids, with why; expect only the hard-kill case), `tests_changed`, `tests_added`,
   `not_run_against_the_bucket` (true), `not_established`.

### ACCEPTANCE

<criterion id="CB72bt3-AC1" cell_refs="CB-bt-3"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests -q</invocation><expect>passed</expect></criterion>
`CB72bt3-AC1` -- the silver suite passes with the variable unset: 0 failed, 0 errors, 12 skipped as before.

<criterion id="CB72bt3-AC2" cell_refs="CB-bt-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~121/REMINT_REPAIR.json',encoding='utf-8'));f=d['failure_points_now'];a=open('data/assets/scripts/silver/commonwealth_account_return_daily.py',encoding='utf-8').read();t=open('data/assets/scripts/silver/tests/test_commonwealth_ard_remint.py',encoding='utf-8').read();print('REMINT-REPAIR repairs=%d points=%d described=%d not_described=%d defect_comments_left=%d half_pair_line=%s begin_line=%s delete_calls=%d not_run_against_the_bucket=%s'%(len(d['repairs']),len(f),sum(1 for x in f if x['described']),sum(1 for x in f if not x['described']),t.count('DEFECT (CB-bs-3)'),'HALF-PAIR' in a,'REMINT-BEGIN' in a,a.count('delete_object'),d['not_run_against_the_bucket']))"</invocation><expect>REMINT-REPAIR repairs=4 points=18</expect></criterion>
`CB72bt3-AC2` -- the four repairs are recorded against the 18 failure points; the issuer reads `not_described`, the count of defect
comments left in the tests (0), and the delete calls (0).

<criterion id="CB72bt3-AC3" cell_refs="CB-bt-3" judgment="true"/>
`CB72bt3-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: each repair is shown by a test that plants the
failure; a key is reported written from the bucket's own state; every refusal still precedes any put; nothing is deleted; what a
hard kill leaves is stated for what it is; the mode was not run against a real bucket.

<expected_criteria>CB72bt3-AC1,CB72bt3-AC2,CB72bt3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch** the gold producer (`data/assets/scripts/gold/irpt_reporting/account_return_daily.py`), `commonwealth_fwd3_serve.py`,
  `commonwealth_daily_valuation.py`, `commonwealth_sweep_regrade.py`, `commonwealth_flows.py`, `lib/`. If a repair cannot be made
  without the producer, stop: that is the refusal clause, and say which.
- **The mode is NEVER run against S3 by you.** No AWS call of any kind.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`.
  **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull): what is on disk is read, never refreshed.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity, share balance or return. Counts, dates, CUSIPs, tickers, a
  security's price or per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W121-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
data/assets/scripts/silver/commonwealth_account_return_daily.py
data/assets/scripts/silver/tests/
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round72.md</decomp_doc> (round 72), cell `CB-bt-3`.
<owned_cells>CB-bt-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB72bt3-AC1, CB72bt3-AC2, CB72bt3-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~121/ADVI_COTBKF.TO-CB-bt-3.remint-repair.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB72bt3-AC1,CB72bt3-AC2,CB72bt3-AC3` BEFORE the flip. Mechanical: CB72bt3-AC1 and CB72bt3-AC2. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** each of the four repairs with where it is in the code and the test that plants its failure; the 18 failure points as they now read (described, half pair flagged); any still not described and why; every test changed (by name, with what its assertion was and is) and every test added; the diff of the adapter; the pytest line; the `REMINT-REPAIR` line; a statement that the mode was not run against a real bucket and deletes nothing; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one hand-run adapter and its tests; the mode is not run.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; tests fake S3.
comp-adversary: RUN -- each repair has a test that plants its failure; a written key is established from the bucket's version, not from a list built before the put; the defect-pinning tests are turned to assert the repaired behaviour and their defect comments must be gone; refusals still precede any put and nothing is deleted, by test; BLIND: a hard kill runs no handler, so the pre-write list is all a killed run leaves, and real S3 partial failures are not reproduced by a fake.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-72 analysis @19911afdeb (msg 5561), section 4 item 3; `3.0.0_SA_CVO` REMEDIATION_v42 @fd300b1f97.
