# TO NFRA_DEVPLN.TO-DP-e-2 -- round 4 ENRICHMENT DP-e-2: `approval-status` reads another box's list from the freshest readable source

<to_id>NFRA_DEVPLN.TO-DP-e-2</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~1</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>ENRICHMENT</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-e-2` (`decompositions/NFRA_DEVPLN_DECOMP.round4.md`) | **outcome_ref:** FWD-2, FWD-5 |
**depends_on:** `DP-e-1` (same slot, same file; this order starts only after `DP-e-1` has drained and merged)

---

## WORKER FACE

### THE CELL

`approval_read(box, store_dir)` in `.tools/open-calls.py` (around line 1450) reads a box's list from `--store-dir`, else the working tree if a file exists for that box, else `git show origin/box/<box>:...`. MEASURED: on the laptop, the working-tree copy of dell2's list exists, is readable, and predates two real OPEN rows dell2 registered, so `approval-status --branch cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal` prints `state=ABSENT`. A stale readable copy reads as "no row", and for a test-only change `portal-merge-forward.sh` treats ABSENT as "no approval needed".
Every box also puts its list to the cluster copy on each write (`cloud_put`, key `fabric/open-calls/v1/box=<box>/open_calls.json`), and `cloud_read_all([box])` already reads it (read both; it returns `({box: (doc, last_modified)}, absent boxes, refused)`). Each list has a top-level `written_at`.

### BUILD

1. For a box that is NOT this box (`this_box(...)`), `approval_read` gathers every readable source: the cluster copy (via `cloud_read_all`), `origin/box/<box>` (git show), and the working-tree file. It returns the one with the greatest `written_at`; on a tie the order of preference is cluster copy, then git, then working tree. A source that is absent or unreadable is skipped, but if NO source is readable it raises BadFile (so the line reads `state=UNREADABLE`, rc 2, never `ABSENT`).
2. For THIS box, the working tree stays the only source (it is the single writer's own file).
3. `--store-dir` still overrides everything (tests).
4. The cluster read must not run under the test switches: when `OPAL_STATE_ROOT` is set or `OPAL_OPENCALLS_CLOUD=0` (the existing off-switches that `cloud_put` honours), skip the cluster source. Add one test-only variable `OPAL_CLOUD_READ_LOCAL=<dir>` that stands in for S3: a directory holding `box=<box>/open_calls.json`, read when set (the same pattern as `OPAL_MODE_LOCAL`); it overrides the off-switch for the read only.
5. Print one stderr line `NOTE: <box> list read from <cluster|git|working-tree> written_at=<t>` so the source is visible; the pinned one-line stdout grammar of `approval-status` does not change.
6. Test `.tools/tests/test_open_calls_cloudread.py` on a temporary state root and `OPAL_CLOUD_READ_LOCAL`: a foreign box whose cluster copy is newer than its stale working-tree copy reads the cluster rows (`state=OPEN`); a foreign box whose git copy is newer than a stale cluster copy reads git; equal `written_at` takes the cluster copy; a foreign box with no readable source is `UNREADABLE` rc 2; this box reads only its working tree even when a newer cluster file exists. Last line `OPEN-CALLS-CLOUDREAD-TEST cases=<k>/<n> ok=True|False`. The existing four open-calls suites and `test_open_calls_withdraw.py` stay green.

### RULES FOR THIS CELL

Tests never touch the live lists or S3. The only S3 call allowed is the read-only `get_object` of one `open_calls.json` that the AC2 command below makes through the tool's own reader. You change no row of the real lists. No push, merge or rebase. No non-ASCII. Python standard library plus the `boto3` the tool already imports; ruff clean on the files you edit or add.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W1-S<k>`, next unused k after the highest `W1-S` in the file, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPe2-AC1" cell_refs="DP-e-2"><invocation>python .tools/tests/test_open_calls_cloudread.py</invocation><expect>ok=True</expect></criterion>
`DPe2-AC1` -- the test above, every case passing.

<criterion id="DPe2-AC2" cell_refs="DP-e-2"><invocation>python .tools/open-calls.py approval-status --branch cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal</invocation><expect>APPROVAL branch=cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal state=OPEN</expect></criterion>
`DPe2-AC2` -- the seam against the REAL cluster copy: dell2's real row, invisible to the laptop's stale copy, now reads OPEN (a read; nothing written).

<criterion id="DPe2-AC3" cell_refs="DP-e-2"><invocation>python .tools/open-calls.py approval-status --branch cand/laptop/contributing-boxes</invocation><expect>state=APPROVED valid=yes</expect></criterion>
`DPe2-AC3` -- the control: this box's own real row still reads from the working tree, unchanged.
</proof_of_spec>

<expected_criteria>DPe2-AC1,DPe2-AC2,DPe2-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~1/NFRA_DEVPLN.TO-DP-e-2.cluster-first-read.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPe2-AC1,DPe2-AC2,DPe2-AC3`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round4.md</decomp_doc>
<owned_cells>DP-e-2</owned_cells>
</decomp_ref>

<paths>
.tools/open-calls.py
.tools/tests/test_open_calls_cloudread.py
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-e-2.cluster-first-read.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE one read-only s3:GetObject through the tool's own existing reader; no policy is created or changed.
comp-adversary: RUN over the cell's own invocations; BLIND to the filesystem around the cited paths. Findings inlined: a freshest-source rule needs a tie-break and must fail closed (no readable source is UNREADABLE, never ABSENT).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: surprise row `NFRA_DEVPLN-S2`; `decompositions/NFRA_DEVPLN_DECOMP.round4.md` S2b.
