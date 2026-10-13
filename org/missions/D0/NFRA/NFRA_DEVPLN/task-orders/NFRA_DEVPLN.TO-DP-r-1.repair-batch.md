# TO NFRA_DEVPLN.TO-DP-r-1 -- round 2 ENRICHMENT DP-r-1: the batch repair (a red test, merge-forward fetch and merge sha, a required --project)

<to_id>NFRA_DEVPLN.TO-DP-r-1</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~2</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>ENRICHMENT</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-r-1` (`decompositions/NFRA_DEVPLN_DECOMP.round2.md`) | **outcome_ref:** FWD-2, FWD-3 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Four small repairs from round 1, batched in one order. Your worktree has the portal repo at `portal/` (read only for you; its `origin/DEV` and `origin/PROD` are present; do not fetch it).

### BUILD

1. `.tools/tests/test_open_calls.py` is red at the base: it prints `OPEN-CALLS-TEST cases=0/2 ok=False`, with a `FileNotFoundError` on `<tmp>/state/laptop/open_calls.json` and the first case `add writes this box's list ...` failing. Find the cause by running it
   (a fork add that lacks `--context`, or a scratch state file the test never creates, are the suspects) and repair the TEST so it passes both cases with `ok=True`. Repair the tool only if the test is right and the tool is wrong, and say which in your report.
2. `.tools/portal-merge-forward.sh`: (a) before it decides, it fetches `origin` for `DEV` and for the branch (a failed fetch is REFUSED `fetch-failed`), unless `--no-fetch` is given (the self-test uses `--no-fetch` against its temporary origin where it needs a fixed state,
   and one new case proves the default fetch picks up a branch pushed to the temporary origin after the clone); (b) the result line carries the merge commit: `MERGE-FORWARD branch=<b> result=MERGED reason=- dev_before=<sha> dev_after=<sha> pushed=<yes|no> merge=<sha>` (`merge=-` on a refusal); update the
   self-test's expectations for the new field and keep every existing case; (c) `--no-fetch` on an unknown branch still prints `... result=REFUSED reason=branch-not-found ...`.
3. `.tools/open-calls.py` `approval-lease`: `--project` becomes required (argparse's own message, `the following arguments are required: --project`). Touch nothing else in that file, and keep `.tools/tests/test_open_calls_approval.py` and `test_open_calls_register.py` green.
4. (Amended by the issuer after your row W2-S6.) `.tools/tests/test_open_calls_register.py` is now in your `<paths>`: its `register_lease` helper omits `--project`, so four lease cases go red when item 3 lands. Add `--project NFRA_DEVPLN` to that helper's `approval-lease` call (the one-line fix you named) and change nothing else in that file; it must read `ok=True` again.

### RULES FOR THIS CELL

Nothing you run pushes, or changes the real portal's DEV, PROD or main tree: tests use `mktemp -d` repositories. Git Bash default utilities only; quote every expansion. No non-ASCII in anything you add. Ruff clean on the Python files you touch.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W2-S<k>`, next unused k after the highest `W2-S` in the file, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPr1-AC1" cell_refs="DP-r-1"><invocation>python .tools/tests/test_open_calls.py</invocation><expect>ok=True</expect></criterion>
`DPr1-AC1` -- repair 1: the test is green (it prints `OPEN-CALLS-TEST cases=2/2 ok=True`).

<criterion id="DPr1-AC2" cell_refs="DP-r-1"><invocation>bash .tools/portal-merge-forward.sh cand/laptop/none-9 --repo portal --no-fetch</invocation><expect>MERGE-FORWARD branch=cand/laptop/none-9 result=REFUSED reason=branch-not-found</expect></criterion>
`DPr1-AC2` -- repair 2 against the REAL portal repo: `--no-fetch` exists, and an unknown branch is refused before any worktree is made.

<criterion id="DPr1-AC3" cell_refs="DP-r-1"><invocation>python .tools/open-calls.py approval-lease --branch cand/laptop/none-9 --box laptop --purpose x --pages x --class opal-internal --how x --portal portal --lease-file none.json</invocation><expect>required: --project</expect></criterion>
`DPr1-AC3` -- repair 3: with no `--project` the command is refused by argparse.

<criterion id="DPr1-AC4" cell_refs="DP-r-1"><invocation>bash .tools/portal-merge-forward.sh --selftest</invocation><expect>ok=True</expect></criterion>
`DPr1-AC4` -- a fourth criterion, with its reason: this order edits an existing script whose 18 self-test cases must stay green with the new `merge=` field and the fetch case added.

<criterion id="DPr1-AC5" cell_refs="DP-r-1"><invocation>python .tools/tests/test_open_calls_register.py</invocation><expect>ok=True</expect></criterion>
`DPr1-AC5` -- a fifth criterion, with its reason (row W2-S6): the required `--project` must not leave the register test red; this one command is what BUILD item 3 promised and item 4 repairs.
</proof_of_spec>

<expected_criteria>DPr1-AC1,DPr1-AC2,DPr1-AC3,DPr1-AC4,DPr1-AC5</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~2/NFRA_DEVPLN.TO-DP-r-1.repair-batch.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPr1-AC1,DPr1-AC2,DPr1-AC3,DPr1-AC4,DPr1-AC5`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round2.md</decomp_doc>
<owned_cells>DP-r-1</owned_cells>
</decomp_ref>

<paths>
.tools/tests/test_open_calls.py
.tools/tests/test_open_calls_register.py
.tools/portal-merge-forward.sh
.tools/open-calls.py
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-r-1.repair-batch.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE the cell touches no IAM.
comp-adversary: RUN over the cell's own invocations; BLIND to the filesystem around the cited paths. Finding inlined: the default fetch reaches the network, so the self-test must keep its fixed-state cases on --no-fetch.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: L10 round analysis `ledger/ROUND_ANALYSIS.round1.md` @14a0501ee5 item 6 (rows W1-S7, W1-S8, W2-S2 and the no-merge-sha note); W3-S3 is resolved by DP-b-3 and not repaired here. Portal worktree: this order needs `--portal-ref` at the spawn.
