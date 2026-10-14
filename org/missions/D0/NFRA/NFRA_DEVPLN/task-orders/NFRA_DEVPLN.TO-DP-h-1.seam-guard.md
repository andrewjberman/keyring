# TO NFRA_DEVPLN.TO-DP-h-1 -- round 6 ENRICHMENT DP-h-1: the test-seam guard (`OPAL_CLOUD_READ_LOCAL` is honoured only under a test switch)

<to_id>NFRA_DEVPLN.TO-DP-h-1</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~1</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>ENRICHMENT</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-h-1` (`decompositions/NFRA_DEVPLN_DECOMP.round6.md`) | **outcome_ref:** FWD-2, FWD-5 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`approval_read` in `.tools/open-calls.py` (around line 1535) reads a FOREIGN box's approval list from the freshest of three sources: the cluster copy (`_source_cluster`, around line 1513), `origin/box/<box>` (`_source_git`, around line 1487) and the working tree. For tests, one variable `OPAL_CLOUD_READ_LOCAL=<dir>` stands in for the cluster copy (a file `<dir>/box=<box>/open_calls.json`) and for the git copy (`<dir>/git=<box>/open_calls.json`). Read those functions and the header comment around line 79.
MEASURED at the cut: the stand-in is honoured with NO test switch beside it. With `OPAL_CLOUD_READ_LOCAL=/tmp/ocl_probe` (a directory holding a `box=dell1/open_calls.json` with `written_at` 2099-01-01 and no rows) and no `OPAL_STATE_ROOT`, `python .tools/open-calls.py approval-status --branch cand/dell1/amgt-sa-header-money-and-dash-reasons` prints `NOTE: dell1 list read from cluster written_at=2099-01-01T00:00:00Z` and `state=ABSENT`, while the real row reads `APPROVED valid=yes`. A stray variable in a production environment makes fixture data win, and `portal-merge-forward.sh` treats ABSENT as "no approval needed" for a test-only change. `OPAL_STATE_ROOT` is the test switch the tool already uses (it replaces the state directory and turns off the cluster put).

### BUILD

1. `OPAL_CLOUD_READ_LOCAL` is honoured ONLY when `OPAL_STATE_ROOT` is also set (non-empty). Put the check in one small helper used by both `_source_cluster` and `_source_git`, so the rule is stated once.
2. With `OPAL_CLOUD_READ_LOCAL` set and `OPAL_STATE_ROOT` NOT set, ignore the stand-in: print ONE stderr line `NOTE: OPAL_CLOUD_READ_LOCAL ignored: it is a test seam and OPAL_STATE_ROOT is not set` per `approval-status` call, and read the production sources exactly as if the variable were unset.
3. Nothing else changes: with both set, the stand-in works as before (all 8 existing cases of `test_open_calls_cloudread.py` still pass unchanged); with `OPAL_STATE_ROOT` set and `OPAL_CLOUD_READ_LOCAL` unset the cluster and git sources are skipped as before; with neither set the production read is byte-for-byte unchanged. Update the header comment that names the variables.
4. Add TWO cases to `.tools/tests/test_open_calls_cloudread.py` (its last line goes from `cases=8/8` to `cases=10/10`): (a) the stand-in set, `OPAL_STATE_ROOT` unset, a box name that exists nowhere in this repo (use `zz9`) with the stand-in directory holding a fixture row for it: the result is `UNREADABLE` (rc 2), the NOTE line is on stderr, and the fixture row is NOT used (use `OPAL_OPENCALLS_CLOUD=0` so the case makes no S3 call); (b) the same stand-in directory with `OPAL_STATE_ROOT` set to a temporary directory: the fixture row IS used (`state=OPEN`).

### RULES FOR THIS CELL

Tests make no S3 call and read no real `origin/box` ref. You change no row of the real lists. No push, merge or rebase. No non-ASCII. Python standard library plus the `boto3` the tool already imports; ruff clean on the files you edit. The other five open-calls suites stay green (run them). Do not put `MSYS_NO_PATHCONV=1` on a command that takes an absolute path. Run every command under `timeout 120` or less.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W1-S<k>`, next unused k after the highest `W1-S` in the file, `surfaced_at` = `date -u +%FT%TZ`) and keep working. Copy the shape of an existing row in that file (schema enums: `class` OBSERVATION or BLOCKING, `hazard_standing` ARMED or INERT, `disposition` UNDER_INVESTIGATION).

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPh1-AC1" cell_refs="DP-h-1"><invocation>python .tools/tests/test_open_calls_cloudread.py</invocation><expect>cases=10/10 ok=True</expect></criterion>
`DPh1-AC1` -- the cloud-read test with its two new cases (it reads 8/8 at the base).

<criterion id="DPh1-AC2" cell_refs="DP-h-1"><invocation>bash -c 'mkdir -p /tmp/dph1_probe/box=dell1 &amp;&amp; printf "%s" "{\"schema\":\"open-calls/1\",\"device\":\"dell1\",\"written_at\":\"2099-01-01T00:00:00Z\",\"written_by\":\"probe\",\"rows\":[]}" > /tmp/dph1_probe/box=dell1/open_calls.json &amp;&amp; OPAL_CLOUD_READ_LOCAL=/tmp/dph1_probe python .tools/open-calls.py approval-status --branch cand/dell1/amgt-sa-header-money-and-dash-reasons'</invocation><expect>state=APPROVED valid=yes</expect></criterion>
`DPh1-AC2` -- the seam against the REAL cluster copy and the real dell1 row: with the stray variable set and no test switch, the real row still reads APPROVED (it reads ABSENT at the base).

<criterion id="DPh1-AC3" cell_refs="DP-h-1"><invocation>python .tools/open-calls.py approval-status --branch cand/laptop/contributing-boxes</invocation><expect>state=APPROVED valid=yes</expect></criterion>
`DPh1-AC3` -- the control: this box's own real row is unchanged (it reads from the working tree).
</proof_of_spec>

<expected_criteria>DPh1-AC1,DPh1-AC2,DPh1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~1/NFRA_DEVPLN.TO-DP-h-1.seam-guard.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPh1-AC1,DPh1-AC2,DPh1-AC3`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID. Commit with safe-commit under your serial.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round6.md</decomp_doc>
<owned_cells>DP-h-1</owned_cells>
</decomp_ref>

<paths>
.tools/open-calls.py
.tools/tests/test_open_calls_cloudread.py
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-h-1.seam-guard.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE the cell adds no S3 call; the reads it guards already exist.
comp-adversary: RUN over the cell's own invocations and the measurement above; BLIND to the filesystem around the cited paths. Finding inlined: a guard that silently ignores a variable hides a misconfigured test, so the ignore prints a NOTE and the test asserts it.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `ledger/ROUND_ANALYSIS.round5.md` @6bbbc233d4 section 2 (W2-S12: YES, as one small repair) and section 3 item 3.
