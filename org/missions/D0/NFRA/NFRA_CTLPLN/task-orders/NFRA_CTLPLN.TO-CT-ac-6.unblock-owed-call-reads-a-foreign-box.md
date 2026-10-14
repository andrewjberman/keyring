# TO NFRA_CTLPLN.TO-CT-ac-6 -- workstream KEEPDRIVE round 1 (cell CT-ac-6): `unblock.py tick --owed-call` reads a call on ANOTHER box's list through the freshest source, so a project waiting on it records a WAIT and not an empty tick (row S9123, routed by the CTO)

<to_id>NFRA_CTLPLN.TO-CT-ac-6</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~90</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>KEEPDRIVE</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ac-6` (`decompositions/NFRA_CTLPLN_DECOMP.round13.md`, Recut 2) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Read row `NFRA_CTLPLN-S9123` (search the id with the Grep tool in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`). `.tools/unblock.py tick --owed-call <id>` is meant to record a WAIT while the open call the project waits on is OPEN or HELD (`call_waiting`, about :323). MEASURED: `open_call_row(call_id)` (about :333) takes the box from the id's prefix and reads `org/devices/state/<box>/open_calls.json` from the WORKING TREE only (or `$OPAL_OPEN_CALLS_STATE_ROOT/<box>/open_calls.json`). For a call on ANOTHER box that file is a possibly stale copy (the laptop's copy of dell2's list predates dell2's rows), so the row reads absent and the tick counts EMPTY (the `OWED-CALL` branch, about :407-409); five ticks on five OPEN dell2 calls read `empty=1..5` and reached `THIRD-EMPTY-TICK`. The reader that exists for exactly this is `approval_read(box, store_dir)` in `.tools/open-calls.py` (about :1545; merged by NFRA_DEVPLN DP-e-2 at `965f9eff8a`): this box reads its own working tree; a FOREIGN box reads every readable source (the cluster copy, `origin/box/<box>`, the working-tree copy) and takes the greatest `written_at`; it raises `BadFile` when no source is readable, so a result is UNREADABLE and never absent. Its test seams: `--store-dir` / `OPAL_STATE_ROOT`, and `OPAL_CLOUD_READ_LOCAL=<dir>` (files `<dir>/box=<box>/open_calls.json`), honoured only under `OPAL_STATE_ROOT` (see `open-calls.py` about :80-83 and :1489-1563). Read those lines first. `python .tools/unblock.py --selftest` reads `UNBLOCK-SELFTEST cases=32/32 ok=True` at your base.

### BUILD

1. In `.tools/unblock.py`, make `open_call_row` use `approval_read` (import `open-calls.py` by file path with `importlib`, the file name has a hyphen) when the call's box prefix is NOT this box (`lib/devices.py` names this box; derive it, never type it). THIS box's own calls keep the working-tree read exactly as today. If `approval_read` returns a document with a `rows` list, find the row by id as today. If it raises `BadFile`, the tick prints `OWED-CALL: id=<id> counts=EMPTY reason=call-unreadable` (a distinct reason, never `call-absent`) and counts EMPTY. A readable source that lacks the row prints `reason=call-absent` as today. If importing `open-calls.py` or finding this box fails, fail closed to the old working-tree read and print one `NOTE:` line saying so.
2. Print the source used on the `OWED-CALL` line (`source=<cluster|git|working-tree|own>`), taken from the second value `approval_read` returns, so a reader can see which copy answered.
3. A NEW test `.tools/tests/test_unblock_owed_call_foreign.py` (standard library; temporary directories only; the seams above; no network, no real git ref): (a) a foreign call whose row is OPEN only in the freshest source (the working-tree copy stale and lacking the row, the `OPAL_CLOUD_READ_LOCAL` copy newer and holding it) reads WAITING with that source named; (b) the same call HELD reads WAITING; (c) the same call CLOSED reads EMPTY `reason=call-closed`; (d) no readable source reads EMPTY `reason=call-unreadable`; (e) a call on THIS box still reads from the working tree and is unchanged; (f) the working-tree copy NEWER than the cluster copy wins. Final line `UNBLOCK-OWED-FOREIGN cases=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. No aws, no network, no push; tests in temporary directories only; do not run `unblock.py tick` against the real repository except under the seams (it writes counters). `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink. ASCII only; Python 3.11. CLAUDE.md and org/XXX.md are LOCKED. The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it (`git log --oneline -1 -- <path>`), never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W90-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTac6-AC1" cell_refs="CT-ac-6"><invocation>python .tools/tests/test_unblock_owed_call_foreign.py</invocation><expect>ok=True</expect></criterion>
`CTac6-AC1` -- every case passes, the unreadable and own-box cases included (base: the file does not exist); report the whole last line with its denominator.

<criterion id="CTac6-AC2" cell_refs="CT-ac-6"><invocation>python .tools/unblock.py --selftest</invocation><expect>ok=True</expect></criterion>
`CTac6-AC2` -- the existing self-test still passes (base: `UNBLOCK-SELFTEST cases=32/32 ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTac6-AC1,CTac6-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~90/NFRA_CTLPLN.TO-CT-ac-6.unblock-owed-call-reads-a-foreign-box.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTac6-AC1,CTac6-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round13.md</decomp_doc>
<owned_cells>CT-ac-6</owned_cells>
</decomp_ref>

<paths>
.tools/unblock.py
.tools/tests/test_unblock_owed_call_foreign.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a foreign call read from a stale working-tree copy (case a); an unreadable source reported as absent (case d); this box's own calls changed by the fix (case e); a stale cluster copy beating a newer working-tree copy (case f); the test seam honoured outside OPAL_STATE_ROOT (the open-calls reader already ignores it with a NOTE); BLIND: a call id whose prefix is not a box name.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base checks, dry-run by the issuer before the cut: CTac6-AC1 base: FAIL as expected (the file does not exist); CTac6-AC2 base: PASS as expected (`UNBLOCK-SELFTEST cases=32/32 ok=True`).
Source: row NFRA_CTLPLN-S9123 (2.0.0_SA_COO~DV, CTO-routed from NFRA_DEVPLN round 7 analysis section 2).
