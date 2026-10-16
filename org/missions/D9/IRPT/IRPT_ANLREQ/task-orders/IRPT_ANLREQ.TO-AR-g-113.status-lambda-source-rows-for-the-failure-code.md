# TO-AR-g-113 -- the irpt-status source map re-pins its two staged rows (status.py, durable_job.py) to the merged failure-code work, so the next Lambda build carries it

<to_id>IRPT_ANLREQ.TO-AR-g-113</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~254</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>31</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-113` (`decompositions/IRPT_ANLREQ_DECOMP_R31_G.md`) |
**outcome_ref:** FWD-4 (C-HOP-FAILURE) | **depends_on:** `AR-g-109` (merged `bc0e7e96c4`) and `AR-g-111` (merged `766ec706ee`). Order: CTO msgs 8907, 8971.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~254`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-254` (branch `wk-IRPT_ANLREQ-254`), provisioned by the issuer with the whole of `infra/`, `docs/`, `data/`, `lib/`, `org/standards` and the project folder on disk. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~254 <0.9.0_WK_IRPT_ANLREQ~254@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W254-S<k>` (take the next free `<k>`; check the channel file for `W254` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- No live call, NO PUSH, no deploy, no AWS call, no terraform, no network, no install. Scratch outside the product tree. Edit `lambda-source-map.json` BYTE-PRESERVING: keep its indentation, key order and line endings, and change only the lines named below.

### Read first

- `infra/aws/lambda/ci/lambda-source-map.json`: the function `irpt-status` and its `staged_from` rows. A row is `{"repo_path", "pin", "packaged_as", "sha256"}` on four lines (10 spaces); the builder packages `packaged_as` from `git show <pin>:<repo_path>` and refuses unless that blob's sha256 equals the row's. NOTE: other functions have rows with the same `packaged_as` names (`status.py` and `durable_job.py` appear under more than one function); edit ONLY the rows inside `"irpt-status": {` (its `staged_from` array).

### THE CELL (`AR-g-113`, inlined)

**The source map.** For each of the two rows of the function `irpt-status` below, set `pin` to the 40-hex sha of the LAST commit touching `repo_path` (`git log -1 --format=%H -- <repo_path>`; that commit's blob equals HEAD's) and `sha256` to the hex sha256 of that blob (`git show <pin>:<repo_path>`); change nothing else in the row.
- `packaged_as` `status.py` -> `repo_path` `infra/aws/lambda/investor-reporting/ops/status.py`.
- `packaged_as` `durable_job.py` -> `repo_path` `infra/aws/lambda/investor-reporting/ycharts/generate/durable_job.py`.

Exactly four lines of the map change (a `pin` line and a `sha256` line in each of the two rows); the checker counts the changed lines of the diff, `-` and `+` together, and wants eight. No other row, field, function or key of the map changes (not `last_deployed_*`, not `_staged_from_note`, not the `files` list, not `irpt-ycharts-generate`). `owned_status.py` is a native member of the function (packaged from the tree) and needs no edit.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR113-g-AC1" cell_refs="AR-g-113"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g113_checks.py g113</invocation><expect>^AR-G113-OK</expect></criterion>

<criterion id="AR113-g-AC2" cell_refs="AR-g-113"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g113_checks.py scope</invocation><expect>^AR-G113-SCOPE-OK</expect></criterion>

<expected_criteria>AR113-g-AC1,AR113-g-AC2</expected_criteria>

- AC1 diffs your map against the merge-base with `box/dell2` and requires: only the two `irpt-status` rows change (identity, order and every other row, function and key identical); each new pin is a full commit, an ancestor of HEAD, whose blob's sha256 equals the row's and equals the tree's file and is the blob of the last commit touching the path; the edit is byte-preserving (only `pin` and `sha256` lines change: eight changed lines in the diff, `-` and `+` together); and the generated `irpt-status` package differs from the base package in exactly `durable_job.py` and `status.py`. At base it FAILs.
- AC2 checks that your branch changes only the map and your own files (against the merge-base with `box/dell2`). At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no terraform.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~254/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-113.status-lambda-source-rows-for-the-failure-code.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R31_G.md</decomp_doc> round 31, workstream ~G, cell `AR-g-113`.
<owned_cells>AR-g-113</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR113-g-AC1, AR113-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~254/IRPT_ANLREQ.TO-AR-g-113.status-lambda-source-rows-for-the-failure-code.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-113`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the map first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR113-g-AC1,AR113-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** each criterion's output lines; the four map lines you changed (old and new); commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- the source map is read by the Lambda builder and the release census; changing two staged pins changes what the NEXT build of `irpt-status` packages (`status.py` with the failure words, `durable_job.py` with `get_state` carrying `hop_failure`) and nothing else; no function is rebuilt, uploaded or applied by this cell. The delta since the pins is only our merged commits (measured: `git log` since each pin touches only AR-g-109 and AR-g-111 commits). The package's native `owned_status.py` changes with the tree. A later cell builds the package (BUILD ONLY) and a signed pair releases it.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- by the issuer's reference edit in a scratch tree (the checker prints AR-G113-OK, 4 cases; at base 4 cases fail). Traps: re-pinning the same-named row of ANOTHER function (`status.py` and `durable_job.py` appear under several functions); a pin that is not the last commit touching the path (it would package a stale or a foreign version); an edit that reformats the map; a changed `files` list or `last_deployed_*`; the sha256 of the tree instead of the blob at the pin.
</preflight>

- Cut on CTO msgs 8907 and 8971 and the issuer's reference edit. Risk WORLD: the floor of an infrastructure path; source only, nothing deployed. Base: `AR113-g-AC1` FAILs and `AR113-g-AC2` PASSes, as expected.
