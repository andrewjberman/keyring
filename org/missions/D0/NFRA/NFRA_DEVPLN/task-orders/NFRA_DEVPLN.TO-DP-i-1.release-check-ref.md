# TO NFRA_DEVPLN.TO-DP-i-1 -- round 7 ENRICHMENT DP-i-1: the release check reads `origin/<trunk>` and says which ref it read; a test stops making a real ref lookup

<to_id>NFRA_DEVPLN.TO-DP-i-1</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~1</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>ENRICHMENT</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-i-1` (`decompositions/NFRA_DEVPLN_DECOMP.round7.md`) | **outcome_ref:** FWD-5, FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Two small repairs, batched. Your worktree has the portal repo at `portal/` (a linked worktree of the real portal repository; read only for you; its local branch `PROD` is stale at `10e7664d` while `origin/PROD` is `7d5cb34d`; do not fetch).

### BUILD

1. (row S4) `.tools/portal-release-build.sh --check <name> [--repo <path>] [--prod-ref <ref>]`. In `main_check` (around lines 146-152) the release branch is resolved as `refs/heads/<name>` first, then `refs/remotes/origin/<name>`. MEASURED: `--check PROD` read the stale LOCAL `PROD` (`10e7664d`, `features=1`) when `origin/PROD` (`7d5cb34d`) holds 2 first-parent merges since the settlement. Change the resolution: for a TRUNK name (`DEV` or `PROD`) prefer `refs/remotes/origin/<name>` and fall back to `refs/heads/<name>` only when `origin/<name>` does not exist; for any other name keep the current order (local first), because the normal flow checks a `release/<stamp>` branch that was just built locally.
2. (row S4) Print the ref actually read. Append ` ref=<full ref> sha=<12-char sha>` to the END of the `RELEASE-CHECK ...` line and the `RELEASE result=...` line (so the existing prefixes `RELEASE-CHECK features=... unapproved=...` and `RELEASE result=...` are unchanged for every consumer). A refusal before any ref is resolved prints `ref=- sha=-`. The value printed is the ref that was read, never the name that was asked for.
3. (row S4) The self-test gains exactly TWO cases (its last line goes from `cases=10/10` to `cases=12/12`): (a) a stale local `PROD` and a newer `origin/PROD`: `--check PROD` reads `refs/remotes/origin/PROD` and prints that ref and sha; (b) a non-trunk name that exists locally and on origin with different tips still reads the LOCAL one (the order is unchanged for it) and prints `refs/heads/<name>`. Every existing case stays.
4. (row W1-S16) In `.tools/tests/test_open_calls_cloudread.py`, case 9 (the stand-in set, `OPAL_STATE_ROOT` unset, box `zz9`) runs the PRODUCTION git source, which does `git show origin/box/zz9` against the real repository. Make that case run its subprocess with `GIT_DIR` pointing at an EMPTY temporary repository (create one with `git init` in a temporary directory), so no real ref is looked up. The case's assertions and the test's 10 cases and last line stay unchanged.

### RULES FOR THIS CELL

Tests use `mktemp -d` repositories and a temporary state root; no S3 call; the real portal is read only. No push, merge or rebase. Git Bash default utilities only; quote every expansion. No non-ASCII in anything you add. Ruff clean on the Python file you touch. The open-calls suites stay green (run them). Do not put `MSYS_NO_PATHCONV=1` on a command that takes an absolute path. Run every command under `timeout 120` or less.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W1-S<k>`, next unused k after the highest `W1-S` in the file, `surfaced_at` = `date -u +%FT%TZ`) and keep working. Copy the shape of an existing row in that file (schema enums: `class` OBSERVATION or BLOCKING, `hazard_standing` ARMED or INERT, `disposition` UNDER_INVESTIGATION).

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPi1-AC1" cell_refs="DP-i-1"><invocation>bash .tools/portal-release-build.sh --check PROD --repo portal --prod-ref 63c4f9e35f259ad76071b1099aeb9dddb150409f</invocation><expect>unapproved=0 ref=refs/remotes/origin/PROD</expect></criterion>
`DPi1-AC1` -- the seam against the REAL portal: the check reads `origin/PROD`, not the stale local branch, and says so.

<criterion id="DPi1-AC2" cell_refs="DP-i-1"><invocation>bash .tools/portal-release-build.sh --selftest</invocation><expect>cases=12/12 ok=True</expect></criterion>
`DPi1-AC2` -- the self-test with its two new cases (it reads 10/10 at the base).

<criterion id="DPi1-AC3" cell_refs="DP-i-1"><invocation>grep -c "GIT_DIR" .tools/tests/test_open_calls_cloudread.py</invocation><expect>^[1-9]</expect></criterion>
`DPi1-AC3` -- case 9 isolates its git from the real repository (the count is 0 at the base).

<criterion id="DPi1-AC4" cell_refs="DP-i-1"><invocation>python .tools/tests/test_open_calls_cloudread.py</invocation><expect>cases=10/10 ok=True</expect></criterion>
`DPi1-AC4` -- a fourth criterion, with its reason: the edited test must stay green with the same 10 cases.
</proof_of_spec>

<expected_criteria>DPi1-AC1,DPi1-AC2,DPi1-AC3,DPi1-AC4</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~1/NFRA_DEVPLN.TO-DP-i-1.release-check-ref.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPi1-AC1,DPi1-AC2,DPi1-AC3,DPi1-AC4`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID. Commit with safe-commit under your serial. Report once at the end: criteria with output, commit hashes, rows.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round7.md</decomp_doc>
<owned_cells>DP-i-1</owned_cells>
</decomp_ref>

<paths>
.tools/portal-release-build.sh
.tools/tests/test_open_calls_cloudread.py
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-i-1.release-check-ref.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE the cell touches no IAM.
comp-adversary: RUN over the cell's own invocations and the measurement above; BLIND to the filesystem around the cited paths. Finding inlined: the printed ref must be the one actually read, not the name asked for.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `ledger/ROUND_ANALYSIS.round6.md` section 2 (S4 and W1-S16: one small repair in round 7). Portal worktree: this order needs `--portal-ref` at the spawn.
