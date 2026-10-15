# TO NFRA_CTLPLN.TO-CT-aj-2 -- workstream OUTCOME round 7 (cell CT-aj-2): D1-S8 -- the pre-push deploy gate also deploys a file named by an open pinned change whose S3 bytes differ, whatever the box diff (FWD-5, positive arm part 1)

<to_id>NFRA_CTLPLN.TO-CT-aj-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~113</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-aj-2` (`decompositions/NFRA_CTLPLN_DECOMP.round20.md`) | **outcome_ref:** FWD-5 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

PRD outcome FWD-5 (`prd/NFRA_CTLPLN_PRD.md` line 67): a push deploys only what a signed change names, at the exact version it signed. The positive arm (a signed change that names a script deploys exactly that script, in a real push) is the next round, through a CloudOps seat; this cell lands the gate fix it needs first. Row `NFRA_CTLPLN-D1-S8` (ARMED, owner the issuer; Grep it in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/remediations/REMEDIATION_v2.md`): `.tools/git-hooks/pre-push-safe-deploy.sh` (lines about 56-57, 82, 104) bounds its deploy set by the box's diff against `origin/CLOUD`, so a file named by an OPEN, pinned change-management entry that reached CLOUD by integrate before its box push is in no later box diff and no push deploys it. Remedy P1 in that row: the gate also deploys any deploy-scope file named by an OPEN pinned entry whose S3 bytes differ from the pinned blob, regardless of the box diff. Read first: the hook, `.tools/safe-deploy.sh`, the round-19 test `.tools/tests/test_round19_unsigned_push.py` (it builds a temporary repository with the real hook, stubbed `aws` and a stubbed deploy core, and a fixture order for the halt gate), and one entry of `org/critical_paths/.open_deploys/` for the pinned-entry shape. `.tools/safe_deploy_core.py` has ONE WRITER, IRPT_BCKEND on dell2 (CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261015_134xZ_SAFE_DEPLOY_CORE_ONE_WRITER.md`): do NOT edit it. If the fix cannot be made without editing it, STOP and file a BLOCKING row naming the exact change needed.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. Make the fix in `.tools/git-hooks/pre-push-safe-deploy.sh` and/or `.tools/safe-deploy.sh` (your `<paths>`): for each OPEN pinned entry that names a deploy-scope file, compare the object the entry pins with what S3 holds for it and, if they differ, add the file to the deploy set for this push. In the test, S3 is a local directory standing in for the bucket behind the stubbed `aws` (no real AWS call can happen).
2. A NEW test `.tools/tests/test_round20_pinned_entry_deploy.py` (standard library; temporary repositories only; reuse the round-19 fixture). Planted case: a pinned file already on CLOUD, absent from the box diff, with stale bytes in the stub bucket; the next `git push origin box/laptop` through the real hook deploys it, and the stub bucket's sha256 for that file then equals the pinned blob's. Last line `PINNED-ENTRY-DEPLOY deployed=<n> bucket_sha_equals_pin=<True|False> ok=<True|False>`.
3. Negative arms in the same test (flag `--negative`): (a) the pinned file's bucket bytes already equal the pin: deployed 0; (b) an UNPINNED deploy-scope file in the push: deployed 0 and held (the round-19 arm); (c) a pinned entry that is CLOSED: deployed 0. Last line `PINNED-ENTRY-NEGATIVE arms=<k>/3 ok=<True|False>`.
Keep `python .tools/tests/test_round19_unsigned_push.py` passing.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~113/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W113-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. Because this edits a gate on every push, commit the hook change in its own commit so it can be reverted alone.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTaj2-AC1" cell_refs="CT-aj-2"><invocation>python .tools/tests/test_round20_pinned_entry_deploy.py</invocation><expect>bucket_sha_equals_pin=True</expect></criterion>
`CTaj2-AC1` -- the planted case (a pinned file on CLOUD, absent from the box diff, stale in the bucket) is deployed by the next push and the bucket sha equals the pin (base: the file does not exist); report the whole last line.

<criterion id="CTaj2-AC2" cell_refs="CT-aj-2"><invocation>python .tools/tests/test_round20_pinned_entry_deploy.py --negative</invocation><expect>arms=3/3</expect></criterion>
`CTaj2-AC2` -- an equal-bytes pin, an unpinned file and a closed entry each deploy nothing (base: the file does not exist); report the whole last line.

<criterion id="CTaj2-AC3" cell_refs="CT-aj-2"><invocation>python .tools/tests/test_round19_unsigned_push.py</invocation><expect>ok=True</expect></criterion>
`CTaj2-AC3` -- the round-19 unsigned-push negative arm still holds (base: `UNSIGNED-PUSH push_rc=0 deployed=0 held=1 ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTaj2-AC1,CTaj2-AC2,CTaj2-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~113/NFRA_CTLPLN.TO-CT-aj-2.pre-push-deploys-open-pinned-entry-file.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTaj2-AC1,CTaj2-AC2,CTaj2-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round20.md</decomp_doc>
<owned_cells>CT-aj-2</owned_cells>
</decomp_ref>

<paths>
.tools/git-hooks/pre-push-safe-deploy.sh
.tools/safe-deploy.sh
.tools/tests/test_round20_pinned_entry_deploy.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; `aws` is a stub on PATH in a temporary repository and the bucket is a local folder.
comp-adversary: RUN -- the fix deploying more than the pinned file (the unpinned and closed-entry arms; the deploy set is printed and asserted); the fix deploying on a pin it cannot read (an unreadable entry must hold, not deploy: add that arm if the format allows); the hook changed in a way that breaks a push that has nothing to deploy (run `bash -n` and a no-script push in the fixture); this hook is on every push from this box, so a regression blocks pushes (the fixture asserts a plain push still exits 0); BLIND: a real push, a real bucket and a real signed change are the next round's WORLD cell through `0.7.0_AE_CloudOps~U7`; `safe_deploy_core.py` is not edited.
risk: LOCAL -- temporary repositories, a stub `aws` and a local-folder bucket; no real push, no real AWS.
lane: the <paths> block IS the grant (worker RULING 1). The hook and `.tools/safe-deploy.sh` are the pre-push deploy gate; D1-S8 is the issuer's row and the CTO ordered this cell (round-19 analysis ruling 3). `safe_deploy_core.py` is IRPT_BCKEND's and is not touched.
</preflight>

Base checks, dry-run by the issuer before the cut: CTaj2-AC1 and CTaj2-AC2 FAIL as expected (the file does not exist); CTaj2-AC3 base `UNSIGNED-PUSH push_rc=0 deployed=0 held=1 ok=True` (a control).
Source: CTO round-19 analysis sections 2-3 (`ledger/ROUND_ANALYSIS.round19.md` @2009d89478), msg 109424; FWD-5.
