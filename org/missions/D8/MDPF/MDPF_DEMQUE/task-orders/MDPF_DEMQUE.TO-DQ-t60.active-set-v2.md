# TO MDPF_DEMQUE.TO-DQ-t60 -- round 9 DQ-t-60: the B1 builder reads dell2's active Cottonwood set V2 (it supersedes V1), and the four bond and T-bill CUSIPs V1 held back window in
<to_id>MDPF_DEMQUE.TO-DQ-t60</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~52</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>ACTIVEV2</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-60` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 23) |
**outcome_ref:** C-IDENTITY, C-QUOTE, C-PRIORITY, FWD-5, FWD-9 | **depends_on:** DQ-t-57 (merged @2ff948f093)

---

## WORKER FACE

### THE CELL

CTO msg 5292: dell2 published **Active Cottonwood set V2**, which SUPERSEDES V1 for P1 windows. Commit `4d427d3bbb` (on origin/box/dell2; the issuer fetched it, so it is present in this repository's object store: `git show 4d427d3bbb:<path>`), folder `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/`:
`ACTIVE_COTTONWOOD_SET_V2.csv`, 41,826 rows, sha256 `5cef7ab0c9e10fe299cb757d4dba31792d069bad35f7250defa76e18773046ae` (verified by the issuer against the commit), same seven columns as V1, **860 distinct account keys, 3,368 distinct non-blank CUSIPs, 834 blank-CUSIP rows**; "active" now means open at Black Diamond on the latest snapshot, cash included, 139 zero-unit accounts excluded.
The four B1 CUSIPs V1 did not hold (`35907XEW3`, `38150V6Q7`, `912796Y37`, `912797GE1`) now have one row each. `REVERSE_MATCH_V3.csv` (sha256 `0783f088aecbf29e46751aa5d80239b8aa53f16484778162e34ee1c09783c66f`, 860 rows) is NOT read by this cell.
**The file carries RAW account numbers: this cell reads `account_key` only to count and group, and prints, logs and writes counts only. Never print an account number.** **This cell makes no vendor call and writes nothing to S3.**

**Build** (read `active_set.py` in full, `b1_request.py`, `test_demque_active_windows.py`; the V1 constants are `COMMIT`, `REL_PATH`, `SHA256` and the counts quoted in the module docstring; import, do not copy):
1. **Pin V2.** `COMMIT = "4d427d3bbb"`, `REL_PATH` ends `ACTIVE_COTTONWOOD_SET_V2.csv`, `SHA256` is the value above. The loader keeps its rule: the working-tree file when it is there, else `git show COMMIT:REL_PATH`; either way the sha256 must equal `SHA256`, and a mismatch (including the V1 hash) is a loud `SystemExit` naming both hashes. Update the module docstring (file name, 41,826 rows, 860 accounts, 3,368 securities). Everything else in the module (the 2012-01-01 floor, `open` handling, the blank-CUSIP ticker windows, `skipped`) is unchanged.
2. **`--census`** prints the same keys; for V2 it must read `sha256_ok` true, `accounts` 860, `securities` 3368.
3. **`b1_request.py`** needs no logic change; if a docstring or the `--build` help names V1 or the 613/608 counts, update the words. The four CUSIPs now window in because they have rows, or are counted in `emptied_cusips` if their window opens after all their history.
4. **Tests** in `test_demque_active_windows.py`: update any assertion that pins the V1 hash or counts, and add exactly these two named tests:
   `test_the_pinned_active_set_is_the_v2_file_and_a_v1_hash_is_refused`,
   `test_the_four_bonds_v1_held_back_window_in_when_the_v2_set_names_them` (a stub V2 CSV with one row for each of four made-up CUSIPs that a stub V1 lacked: they are in `securities`, not in `held_back`).
5. **Re-file nothing.** The issuer re-files and re-quotes the B1 request on the merged bytes. Run `b1_request.py --build --out .scratch/b1_v2.json` for your report only.

### ACCEPTANCE

<criterion id="DQ9-t60-AC1" cell_refs="DQ-t-60"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t60_tests.py</invocation><expect>V2-OK</expect></criterion>
<criterion id="DQ9-t60-AC2" cell_refs="DQ-t-60"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t60_real.py</invocation><expect>WIN-REAL-OK</expect></criterion>
`DQ9-t60-AC1` -- the two named tests. `DQ9-t60-AC2` -- on the REAL V2 file: sha256 verified, 860 accounts and 3,368 securities counted, the B1 line (608 to 613 CUSIPs, at least one held back, cells strictly below the 37,514 base), the four bonds in the request, deterministic, valid, nothing earlier than 2012-01-01, no account key and zero oracle hits. Each build call is allowed 110 seconds.
Report the whole folder `pytest data/mdpf/scripts/demque` once, and the census and `--build` lines verbatim.

<expected_criteria>DQ9-t60-AC1,DQ9-t60-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `V2-BAD not-passed=...`; `WIN-REAL-BAD arm1 census does not match the published set`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: NO vendor call, no write to S3, any ledger, the queue or any pacer state; no AWS write; no deploy; no timer.** **Never print, log, commit or return an account number**; tests use a stub CSV with made-up keys. Build no alarm, monitor or notification.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W52-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1` (it is blocked by a foreign row); the issuer unions at the drain.

<paths>
data/mdpf/scripts/demque/active_set.py
data/mdpf/scripts/demque/b1_request.py
data/mdpf/scripts/demque/test_demque_active_windows.py
data/mdpf/scripts/demque/test_demque_b1_request.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-60`.
<owned_cells>DQ-t-60</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t60-AC1, DQ9-t60-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~52/MDPF_DEMQUE.TO-DQ-t60.active-set-v2.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t60-AC1,DQ9-t60-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the census and `--build` lines verbatim, the folder count, commits (never an account number).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE a read of a repo file or a git object; no AWS access.
comp-adversary: DECLARED-NOT-APPLICABLE a request builder; nothing is drawn or served. The input carries raw account numbers: read only to count, never emitted.
risk: LOCAL -- code and tests.
direct_act: false -- a worker order.
</preflight>

Source: CTO msg 5292; dell2 commit `4d427d3bbb`; decomposition round 9.
