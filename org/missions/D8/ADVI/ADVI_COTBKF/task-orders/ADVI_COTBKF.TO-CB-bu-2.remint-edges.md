# TO ADVI_COTBKF.TO-CB-bu-2.remint-edges -- round 73 CB-bu-2: the re-mint mode's two edges: a second writer in the gap is refused and never read as this run's write; the record and the line agree on a hard kill

<to_id>ADVI_COTBKF.TO-CB-bu-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~124</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>73</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bu-2` (`decompositions/ADVI_COTBKF_DECOMP.round73.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_73_20261011.md` section 2 item 3 and section 3 item 2; the round-72 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~121/REMINT_REPAIR.json` and its `.md` (four repairs; the
"before" state is the CAPTURE's ids, so "a second writer between the capture check and the puts would read as WRITTEN by this run"; F8
is recorded `described` for an uncaught exception while a hard kill is listed under `still_not_described`, so the printed line says 18
of 18 described and the record says otherwise); the mode `data/assets/scripts/silver/commonwealth_account_return_daily.py`
(`remint_days`, `_remint_state`, `_remint_report`, `_head_key`, the capture check) and its tests
`data/assets/scripts/silver/tests/test_commonwealth_ard_remint.py`; READ ONLY, the producer's writers
(`data/assets/scripts/gold/irpt_reporting/account_return_daily.py` `emit_day`, `emit_method_row`) and the put path under them
(`lib/stream_parquet.py`): which client call lands each object.

**The ruling.** "The re-mint repair holds; two edges are closed before it is ever run against the bucket: the printed line and the
record agree on a hard kill, and the 'before' state is read at the write (a conditional write on the version read), so a second writer
in the gap is refused and never read as this run's write. Built and tested against the faked bucket only."

**Your item. No AWS call: tests fake S3. The mode is NEVER run against a real bucket.**

1. **The second writer is refused.** The mode hands the producer its S3 client. Make every put of a PLANNED key conditional on the
   state the run read for that key (the captured ETag; S3's `IfMatch` on a put), by passing the producer a thin client wrapper defined
   in the adapter that adds the condition to the put call the producer's path actually makes for those keys, and by adding it to the
   mode's own sidecar put. A key changed by anyone after the capture check then fails its put (a precondition failure), the run
   stops, and the key prints `NOT-WRITTEN` with the reason. State in the code comment that the condition is the ETag read, and what
   that does and does not cover (an identical-bytes rewrite keeps the ETag).
2. **And it is never read as this run's write.** After a stop, a key whose version moved but whose put this run did NOT complete
   (the conditional put failed, or was never issued) prints `CHANGED-BY-ANOTHER-WRITER`, never `WRITTEN`. The mode knows which puts
   returned: the wrapper records each put that returned, with the version id the bucket gave it.
3. **If the producer's put path cannot carry the condition** (it does not go through a call the wrapper can condition), do NOT edit
   the producer: build the detection half only (item 2, plus a head of each key immediately before its write that refuses on a
   difference from the capture), say plainly in the record that the gap is narrowed and detected, not closed, and file a row.
4. **The hard kill, in the record and the line alike.** The record's failure points carry the hard kill as its OWN point with
   `described: false` (an uncaught exception stays its own point, described); the mode's help text and docstring say the same.
5. **Tests on the faked bucket** (extend the fake with `IfMatch` on put: a mismatch raises a precondition-failed client error and
   lands nothing): a second writer changes a planned key after the capture check and before its put -> the put is refused, the run
   stops non-zero, the key prints `CHANGED-BY-ANOTHER-WRITER` and is never `WRITTEN`; the same for the sidecar and for the method row;
   a second writer on a key the run already wrote (after its put) -> reported as changed since this run's write; a clean run passes
   the condition on every put and prints no failure report. Every existing test still passes; every refusal still precedes any put;
   nothing is deleted.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~124/REMINT_EDGES.json` and a short `.md`. Top-level keys, exactly: `edges` (a list of two `{"edge", "how", "where", "test"}`),
   `conditional_write` (`{"mechanism", "refuses_before_the_put": true|false, "detects_after": true|false, "covers", "does_not_cover"}`),
   `failure_points_now` (round 72's points by id plus the hard kill as its own, each `{"id", "described", "test"}`), `hard_kill`
   (`{"described": false, "what_the_operator_has"}`), `tests_added`, `tests_changed`, `not_run_against_the_bucket` (true),
   `not_established`.

### ACCEPTANCE

<criterion id="CB73bu2-AC1" cell_refs="CB-bu-2"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests -q</invocation><expect>passed</expect></criterion>
`CB73bu2-AC1` -- the silver suite passes with the variable unset: 0 failed, 0 errors, 12 skipped as before.

<criterion id="CB73bu2-AC2" cell_refs="CB-bu-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~124/REMINT_EDGES.json',encoding='utf-8'));f=d['failure_points_now'];c=d['conditional_write'];a=open('data/assets/scripts/silver/commonwealth_account_return_daily.py',encoding='utf-8').read();print('REMINT-EDGES edges=%d hard_kill_described=%s points=%d described=%d not_described=%d refuses_before_the_put=%s detects_after=%s other_writer_line=%s if_match=%s delete_calls=%d not_run_against_the_bucket=%s'%(len(d['edges']),d['hard_kill']['described'],len(f),sum(1 for x in f if x['described']),sum(1 for x in f if not x['described']),c['refuses_before_the_put'],c['detects_after'],'CHANGED-BY-ANOTHER-WRITER' in a,'IfMatch' in a,a.count('delete_object'),d['not_run_against_the_bucket']))"</invocation><expect>REMINT-EDGES edges=2 hard_kill_described=False</expect></criterion>
`CB73bu2-AC2` -- both edges are recorded; the hard kill is a point of its own and not described; the issuer reads whether the put
is refused before it lands or only detected after.

<criterion id="CB73bu2-AC3" cell_refs="CB-bu-2" judgment="true"/>
`CB73bu2-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: a second writer in the gap is shown by a test to be
refused, or the record says plainly that it is only detected; a key another writer changed is never printed as this run's write; the
record and the printed line agree on the hard kill; the producer was not edited; the mode was not run against a real bucket.

<expected_criteria>CB73bu2-AC1,CB73bu2-AC2,CB73bu2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch** the gold producer (`data/assets/scripts/gold/irpt_reporting/account_return_daily.py`), `lib/`,
  `commonwealth_fwd3_serve.py`, `commonwealth_daily_valuation.py`, `commonwealth_sweep_regrade.py`, `commonwealth_flows.py`.
- **The mode is NEVER run against S3 by you.** No AWS call of any kind. `--apply`, `--build` and `--verify-served` are unchanged.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`.
  **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull): what is on disk is read, never refreshed.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity, share balance or return. Counts, dates, CUSIPs, tickers, a
  security's price or per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W124-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
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
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round73.md</decomp_doc> (round 73), cell `CB-bu-2`.
<owned_cells>CB-bu-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB73bu2-AC1, CB73bu2-AC2, CB73bu2-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~124/ADVI_COTBKF.TO-CB-bu-2.remint-edges.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB73bu2-AC1,CB73bu2-AC2,CB73bu2-AC3` BEFORE the flip. Mechanical: CB73bu2-AC1 and CB73bu2-AC2. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** which client call the producer's put path makes and whether the condition rides it; each edge with where it is in the code and the test that plants it; whether a second writer is REFUSED before the put or only DETECTED, said plainly; what the condition covers and does not; the failure points as they now read, the hard kill its own point; tests added and changed, by name; the diff of the adapter; the pytest line; the `REMINT-EDGES` line; a statement that the mode was not run against a real bucket, deletes nothing, and that the producer was not edited; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one hand-run adapter and its tests; the mode is not run.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; tests fake S3.
comp-adversary: RUN -- a test plants a second writer in the gap for a day key, the sidecar and the method row; the key another writer changed must never print as this run's write; if the producer's put path cannot carry the condition the cell says detected-not-closed and files a row instead of editing the producer; the hard kill is its own point, not described, in the record and the line alike; BLIND: a real bucket's handling of the condition is not exercised by a fake, and an identical-bytes rewrite keeps its ETag.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-73 analysis @35cf1a97dd (msg 5633), section 3 item 2; `3.0.0_SA_CVO` REMEDIATION_v43 @bf44c1d294.
