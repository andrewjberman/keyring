# TO NFRA_DEVPLN.TO-DP-e-1 -- round 4 ENRICHMENT DP-e-1: a `withdrawn` close decision for approval rows

<to_id>NFRA_DEVPLN.TO-DP-e-1</to_id>
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

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-e-1` (`decompositions/NFRA_DEVPLN_DECOMP.round4.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none (your slot's next order, `DP-e-2`, edits the same file after this one)

---

## WORKER FACE

### THE CELL

An `approval` row in `.tools/open-calls.py` ends only as `approved` or `declined` (`close --id <id> --ruled-by andrew|cto --ruling <file> --decision approved|declined`). A real case: a builder registered the SAME branch twice, so two OPEN rows exist for it, and `approval-status` reads the NEWEST row per branch (the duplicate). The duplicate cannot be closed without reading as a decision on the feature: closing it `declined` looks like a decline of the feature. Add a third ending that says "this row is withdrawn, it is not a decision".
Read first: `approval_read`, `cmd_approval_status` (around lines 1450-1560), the `close` command and its `--decision` handling, and `validate_doc` (an unknown value is refused by every reader, so the accepted decision set must be widened where it is validated).

### BUILD

1. `close --id <id> --ruled-by andrew|cto --ruling <file> --decision withdrawn` is accepted for an `approval` row, only when the row is OPEN. Withdrawing a row that is already CLOSED (approved, declined or withdrawn) is refused: `REFUSED: row <id> is already closed (<decision>); a withdraw ends only an OPEN row`, rc 2, nothing written. `--decision` is still refused on any other kind. The closure stores `closed.decision: "withdrawn"`.
2. `approval-status` skips withdrawn rows when it picks the row for a branch (the newest NON-withdrawn row wins). If every row for the branch is withdrawn the line reads exactly as for no row: `state=ABSENT valid=- row=- ...`. The pinned one-line grammar does not change and the state set does not gain a value.
3. `validate_doc` accepts `withdrawn` as a decision, so a list holding a withdrawn row is not refused by any reader (`list`, `list --all --cloud`, `approval-status`).
4. `list` shows a withdrawn approval row as CLOSED with its decision visible; nothing else in `list` changes.
5. Test `.tools/tests/test_open_calls_withdraw.py` on a temporary state root (`OPAL_STATE_ROOT`) and temporary git repositories: two OPEN rows for one branch, the newer withdrawn, the older then reads as the row (`state=OPEN row=<older id>`); withdraw the only row: `ABSENT`; withdraw an APPROVED row: refused; withdraw a DECLINED row: refused; `--decision withdrawn` on a `fork` row: refused; a list holding a withdrawn row still passes `list`. Last line `OPEN-CALLS-WITHDRAW-TEST cases=<k>/<n> ok=True|False`. The existing `test_open_calls_waiver.py`, `test_open_calls_register.py`, `test_open_calls_approval.py` and `test_open_calls.py` stay green (run them).

### RULES FOR THIS CELL

Tests use a temporary state root and temporary git repositories, never the live lists or S3 (`OPAL_STATE_ROOT` also skips the cluster copy). You change no row of the real `org/devices/state/*/open_calls.json`. No push, merge or rebase. No non-ASCII. Python standard library only; ruff clean on the files you edit or add.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W1-S<k>`, next unused k after the highest `W1-S` in the file, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPe1-AC1" cell_refs="DP-e-1"><invocation>python .tools/tests/test_open_calls_withdraw.py</invocation><expect>ok=True</expect></criterion>
`DPe1-AC1` -- the test above, every case passing.

<criterion id="DPe1-AC2" cell_refs="DP-e-1"><invocation>python .tools/open-calls.py close --help</invocation><expect>withdrawn</expect></criterion>
`DPe1-AC2` -- the real tool offers the new decision (its `--decision` help names it).

<criterion id="DPe1-AC3" cell_refs="DP-e-1"><invocation>python .tools/open-calls.py approval-status --branch cand/laptop/declined-example</invocation><expect>state=DECLINED</expect></criterion>
`DPe1-AC3` -- the control against the REAL laptop list: a real DECLINED row still reads DECLINED (a read; nothing written).
</proof_of_spec>

<expected_criteria>DPe1-AC1,DPe1-AC2,DPe1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~1/NFRA_DEVPLN.TO-DP-e-1.withdraw-decision.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPe1-AC1,DPe1-AC2,DPe1-AC3`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID.
Your slot's NEXT order (`DP-e-2`) is a separate file the issuer hands you after this one drains; do not start it early.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round4.md</decomp_doc>
<owned_cells>DP-e-1</owned_cells>
</decomp_ref>

<paths>
.tools/open-calls.py
.tools/tests/test_open_calls_withdraw.py
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-e-1.withdraw-decision.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE the cell touches no IAM.
comp-adversary: RUN over the cell's own invocations; BLIND to the filesystem around the cited paths. Finding inlined: a withdraw must only end an OPEN row, or a builder could erase a DECLINED or APPROVED row.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: surprise row `NFRA_DEVPLN-S2` (relay from 0.0.0_AB_MSTR, bus 4ac17c50, CTO~DELL2 msg 7302); `decompositions/NFRA_DEVPLN_DECOMP.round4.md` S2a. Not a portal cell: no `--portal-ref`.
