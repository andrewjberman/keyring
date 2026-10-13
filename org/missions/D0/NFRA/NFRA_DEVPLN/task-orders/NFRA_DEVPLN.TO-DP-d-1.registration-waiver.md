# TO NFRA_DEVPLN.TO-DP-d-1 -- round 3 ENRICHMENT DP-d-1: the registration waiver (excuse named commits from the DEV-overlap refusal) and a check-only that takes any commit-ish

<to_id>NFRA_DEVPLN.TO-DP-d-1</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~1</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>ENRICHMENT</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-d-1` (`decompositions/NFRA_DEVPLN_DECOMP.round3.md`) | **outcome_ref:** FWD-1, FWD-7 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`.tools/open-calls.py add --kind approval --portal <repo>` computes, for a feature branch, `overlap` = the number of commits in `origin/PROD..<branch>` that are also in `origin/PROD..origin/DEV`, and REFUSES with `APPROVAL-REGISTER result=REFUSED reason=dev-overlap overlap=<n> commits=<m>` (rc 3) when it is above 0 (built in an earlier order; read the code). That refusal exists to stop a branch cut from DEV from carrying DEV's commits.
It now blocks three real features: dell2's IRPT_ANLREQ work was merged onto DEV before the route existed, so each feature's own commits are now "also on DEV". The CTO ruled the refusal WAIVED for exactly four named commits and no others: `923f7d69`, `794b7df4` (feature head of one branch), `9ef6a359` and `62d455f5`. Implement a waiver that can only excuse commits by name.
Your worktree has the portal repo at `portal/` with `origin/DEV` and `origin/PROD` present (do not fetch). The four commits exist in it: `794b7df4` has 2 commits of its own over PROD (`923f7d69`, `794b7df4`); `9ef6a359` and `62d455f5` have 1 each.

### BUILD

1. `add --kind approval` (and `approval-lease`) take `--waive-overlap <sha[,sha...]>` (full or abbreviated shas, resolved to full) and `--waiver-ref <path>` (a ruling file; REQUIRED whenever `--waive-overlap` is given, and the path must exist: otherwise `APPROVAL-REGISTER result=REFUSED reason=waiver-ref-missing`, rc 3).
2. With a waiver, the overlap check passes only when EVERY commit of the overlap set is among the named shas. If any overlap commit is not named: `APPROVAL-REGISTER result=REFUSED reason=dev-overlap overlap=<n> commits=<m> unwaived=<k>` (rc 3, nothing written). A waiver naming a sha that is NOT in the overlap set is refused too (`reason=waiver-sha-not-in-overlap`), so a waiver can never be a blanket. Never accept a count, a range or a wildcard.
3. A registered row stores `approval.waiver: {shas: [full shas], ref: <path>}` and the success line prints `waived=<n>`: `APPROVAL-REGISTER result=OK row=<id|-> head_sha=<sha> commits=<n> waived=<n>`. `approval-status` output stays the pinned one-line grammar; add NOTHING to it.
4. `--check-only` resolves its branch as `origin/<b>`, else a local branch `<b>`, else any commit-ish `git rev-parse --verify <b>^{commit}` (a bare sha), so the real commits can be checked without a branch name. It still writes nothing, and it still skips the `cand/<box>/<slug>` name check.
5. Test `.tools/tests/test_open_calls_waiver.py` on temporary git repositories: a branch cut from PROD with 2 own commits that are also on a DEV (overlap 2) is refused without a waiver; registers with a waiver naming both; is refused with a waiver naming only one (`unwaived=1`); is refused with a waiver naming a sha outside the overlap; is refused when `--waiver-ref` is absent or missing; and the stored row carries the waiver. Last line `OPEN-CALLS-WAIVER-TEST cases=<k>/<n> ok=True|False`. The existing `test_open_calls_register.py`, `test_open_calls_approval.py` and `test_open_calls.py` stay green (run them).

### RULES FOR THIS CELL

Tests run in temporary git repositories and a temporary state root (set `OPAL_STATE_ROOT`, which also skips the cluster copy), never against the live lists or S3. The real portal repo is read only. No push, merge or rebase. No non-ASCII. Python standard library only; ruff clean on the files you edit or add. Do not put `MSYS_NO_PATHCONV=1` on a command that takes an absolute path.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W1-S<k>`, next unused k after the highest `W1-S` in the file, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPd1-AC1" cell_refs="DP-d-1"><invocation>python .tools/tests/test_open_calls_waiver.py</invocation><expect>ok=True</expect></criterion>
`DPd1-AC1` -- the test above, every case passing.

<criterion id="DPd1-AC2" cell_refs="DP-d-1"><invocation>python .tools/open-calls.py add --kind approval --check-only --project NFRA_DEVPLN --box dell2 --branch 794b7df4 --purpose x --pages x --class client-facing --how x --portal portal --waive-overlap 923f7d69,794b7df4 --waiver-ref org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261013_213xZ_LAPTOP_E846_7D95_BB8B.md</invocation><expect>APPROVAL-REGISTER result=OK row=- head_sha=794b7df4</expect></criterion>
`DPd1-AC2` -- the seam against the REAL portal repo, positive arm: the real feature head `794b7df4`, its two real commits named, registers in check-only mode and writes nothing.

<criterion id="DPd1-AC3" cell_refs="DP-d-1"><invocation>python .tools/open-calls.py add --kind approval --check-only --project NFRA_DEVPLN --box dell2 --branch 794b7df4 --purpose x --pages x --class client-facing --how x --portal portal</invocation><expect>APPROVAL-REGISTER result=REFUSED reason=dev-overlap overlap=2</expect></criterion>
`DPd1-AC3` -- the difference control: the same real commit without the waiver is still refused for its 2 overlapping commits.
</proof_of_spec>

<expected_criteria>DPd1-AC1,DPd1-AC2,DPd1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~1/NFRA_DEVPLN.TO-DP-d-1.registration-waiver.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPd1-AC1,DPd1-AC2,DPd1-AC3`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round3.md</decomp_doc>
<owned_cells>DP-d-1</owned_cells>
</decomp_ref>

<paths>
.tools/open-calls.py
.tools/tests/test_open_calls_waiver.py
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-d-1.registration-waiver.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE the cell touches no IAM.
comp-adversary: RUN over the cell's own invocations and the ruling text; BLIND to the filesystem around the cited paths. Findings inlined: a waiver is the one place a check is loosened, so the negative control is a criterion; a waiver names commits, never a count or range.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `ledger/ROUND_ANALYSIS.round2.md` @8cf96d5f52 item 4; CTO ruling `CTO_RULING_20261013_213xZ_LAPTOP_E846_7D95_BB8B.md` (call bb8b: the DEV-overlap refusal "WAIVED for exactly these three named merge shas"; the issuer reads the exact set as the four feature commits, recorded in the decomposition). Portal worktree: this order needs `--portal-ref` at the spawn.
