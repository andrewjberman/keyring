# TO NFRA_CTLPLN.TO-CT-ai-3 -- workstream OUTCOME round 3 (cell CT-ai-3): a box push carrying a pipeline script no open change names deploys nothing, and the script is held and written down (FWD-5, negative arm)

<to_id>NFRA_CTLPLN.TO-CT-ai-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~108</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ai-3` (`decompositions/NFRA_CTLPLN_DECOMP.round19.md`) | **outcome_ref:** FWD-5 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

PRD outcome FWD-5 (`prd/NFRA_CTLPLN_PRD.md` line 67): pushing from any box never puts anything into production except what a signed change names for that exact build. DONE WHEN: a box push carrying a pipeline script no open change names, and nothing deployed. ACCEPT: any other script in the push is held and written down, and the push still goes through. Read first: `.tools/git-hooks/pre-push-safe-deploy.sh`, `.tools/safe-deploy.sh`, `.tools/tests/test_named_commit_deploy.py`. Row `D1-S8` of the REMEDIATION channel (the deploy set is bounded by the box diff; a named file can miss its deploy) is OPEN and the issuer's; do not fix it here.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. A NEW test `.tools/tests/test_round19_unsigned_push.py` (standard library; temporary repositories only). Build a temporary bare `origin` and a temporary working repository with branches `CLOUD` and `box/laptop`, install the REAL hook `.tools/git-hooks/pre-push-safe-deploy.sh` and the REAL `.tools/safe-deploy.sh` into it, and set `AGENTBUS_DEVICE=laptop`. Replace every deploy executor and every `aws` call with a stub on a shadowing `PATH` that only records its argv to a file (no real AWS call can happen; if the real scripts call something you cannot stub, STOP and file a BLOCKING row). Commit a new file `data/fixture/scripts/fixture_unsigned.py` that NO open change names (no entry for it in the fixture's `org/critical_paths/.open_deploys/`), then `git push origin box/laptop`. Require: the push exits 0 (it goes through), the stub recorded 0 deploy calls, and the hold is written down (find where the hook or `safe-deploy.sh` writes it, a held-list file or its printed output, and require the script's path in it). Last line: `UNSIGNED-PUSH push_rc=<rc> deployed=<n> held=<n> ok=<True|False>`.
2. The flag `--stub-control`: the same fixture with the stub called once by hand, to show the stub sees a call. Last line `STUB-CONTROL stub_saw=<n>`.
3. The signed-change arm (a script an open signed change names deploys only what it names) is OUT of this cell: it needs an open signed change from a CloudOps seat. Say so in your report. If the push deploys, tries AWS, or leaves no hold record, that is the finding: file a BLOCKING row, report `ok=False` honestly, and do not edit the hook or `safe-deploy.sh`.
Known at the cut: `python .tools/tests/test_named_commit_deploy.py` stops after case 7 on this box with `ModuleNotFoundError: No module named 'git_bash_resolver'` (a temporary repository without `.tools/`). It is not a control for this cell. File one row for it.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~108/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W108-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. 

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTai3-AC1" cell_refs="CT-ai-3"><invocation>python .tools/tests/test_round19_unsigned_push.py</invocation><expect>ok=True</expect></criterion>
`CTai3-AC1` -- the real hook, with every executor stubbed, lets the push through and deploys nothing for a script no open change names, and the script is held on a record (base: the file does not exist); report the whole last line.

<criterion id="CTai3-AC2" cell_refs="CT-ai-3"><invocation>python .tools/tests/test_round19_unsigned_push.py --stub-control</invocation><expect>stub_saw=1</expect></criterion>
`CTai3-AC2` -- the stub sees a call made through it, so `deployed=0` above is a reading and not blindness (base: the file does not exist); report the whole last line.
</proof_of_spec>

<expected_criteria>CTai3-AC1,CTai3-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~108/NFRA_CTLPLN.TO-CT-ai-3.unsigned-script-push-deploys-nothing.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTai3-AC1,CTai3-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round19.md</decomp_doc>
<owned_cells>CT-ai-3</owned_cells>
</decomp_ref>

<paths>
.tools/tests/test_round19_unsigned_push.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; every `aws` and deploy executor is stubbed on PATH in the temporary repository.
comp-adversary: RUN -- a real deploy or AWS call reached through a script the stub does not shadow (the stub control and the argv log are the check; STOP if the real scripts call one you cannot stub); the hook installed from a copy that differs from the real one (use the real file bytes and print their sha); the push held for a reason other than the unsigned script (print the hold record); BLIND: the positive arm (a signed change deploys exactly what it names) is not exercised here; the real push to the real origin is not exercised; `D1-S8` stays open.
risk: LOCAL -- temporary repositories and stubs; no real push, no real AWS.
lane: the <paths> block IS the grant (worker RULING 1). Only a new test file is written; the hook and `safe-deploy.sh` are read, never edited.
</preflight>

Base checks, dry-run by the issuer before the cut: CTai3-AC1 and CTai3-AC2 FAIL as expected (the test file does not exist). `test_named_commit_deploy.py` stops after case 7 at the cut (git_bash_resolver), so it is not a control.
Source: CTO round-18 analysis section 3 (`ledger/ROUND_ANALYSIS.round18.md` @721e05298f), msg 109398; FWD-5.
