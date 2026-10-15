# TO NFRA_CTLPLN.TO-CT-ak-4 -- workstream OUTCOME round 11 (cell CT-ak-4): the one-line signed change to diag_sleeve_fix.py and the positive-arm read test, committed by a worker serial (the registry lanes POD4 and TOOL_BATTERIES admit no CloudOps seat) -- the commits CT-ak-3 needs (S9130)

<to_id>NFRA_CTLPLN.TO-CT-ak-4</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~118</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run (worker tree wk-NFRA_CTLPLN-118 @8bd7603422, merged 57f13ba60a, and in the main tree after the merge): FWD5-PRE ... differs=True others_differ=0 ok=True (68 of 68 other top-level gold scripts equal S3); AST-IDENTICAL ast_identical=True (comment-only noqa change, commit 461e3f64ee, blob 8d6f273a9e, md5 c204fd9be3bbfc43346a14b4c71051af); PARSE-OK; ruff All checks passed; proof VALID against the amended order. AC2 was amended from --docstring-only to --ast-identical (9b2702a5a5) after W118-S1: the script fails ruff at the previous commit and its line-2 string is not a module docstring.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ak-4` (`decompositions/NFRA_CTLPLN_DECOMP.round21.md`) | **outcome_ref:** FWD-5 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

PRD outcome FWD-5 (`prd/NFRA_CTLPLN_PRD.md` line 67). Cell `CT-ak-3` (read its order, `task-orders/NFRA_CTLPLN.TO-CT-ak-3.signed-change-deploys-exactly-one-script.md`, whole, with AMENDMENT 1) is the real deploy: a CloudOps seat opens a ledger entry pinning ONE script and pushes. Its seat could not commit the script (lane POD4) or the read test (lane TOOL_BATTERIES): row `NFRA_CTLPLN-S9130`. A worker serial can, under this order's `<paths>`. YOU make those two commits and nothing else; you deploy nothing, you open no ledger entry and you push nothing. Read first: the CRO's research `org/tier1_exec/4.0.0_SA_CRO/deliverables/NFRA_CTLPLN_R21_FWD5_ONE_SIGNED_CHANGE_ONE_SCRIPT_RESEARCH_20261015.md` (why `diag_sleeve_fix.py`: a hand diagnostic no schedule runs and nothing imports), rows `S9130` and `S9131` (Grep each id in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`). A DRAFT of the read test exists UNTRACKED in the main tree at `C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/tests/test_round21_fwd5_positive_read.py` (100 lines, written by the CloudOps seat; read it, copy it into your worktree, then fix it; do not edit the main-tree copy).

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. **The signed change (AMENDMENT 1, issuer, after row W118-S1).** The commit gate runs ruff and the script fails it at HEAD with 7 pre-existing findings (E402 x6 for imports after the `sys.path` insert, F401 for the unused numpy import), so a docstring edit cannot be committed, and the string on line 2 is not a module docstring by Python's rule (`from __future__` precedes it). The signed change is therefore COMMENT-ONLY: DISCARD the uncommitted line-2 edit (`git checkout -- data/black_diamond/scripts/gold/diag_sleeve_fix.py`), run `ruff check data/black_diamond/scripts/gold/diag_sleeve_fix.py` to list each finding with its line, and append a `# noqa: E402` or `# noqa: F401` comment (the code ruff names for that line) to exactly the lines it names (7 findings on 6 lines; line 8 carries two codes: `# noqa: E402, F401`). No code token, string or line order changes, so the AST of the file is identical before and after; `python -m py_compile` and the commit gate (ruff) then pass. Commit it ALONE with `.tools/safe-commit.sh` (explicit path). Do not touch any other file in that commit. Record the new blob id (10+ hex), its sha256 and its md5 in your report.
2. **The read test.** Copy the draft to `.tools/tests/test_round21_fwd5_positive_read.py` in your worktree and complete it (standard library plus the repository `.tools/aws` shim; read-only AWS `get`/`head`/`list` calls only; ASCII; no write). Flags: (default) the post-deploy read: prints `FWD5-POSITIVE versions=<n> etag_equals_repo_md5=<True|False> other_changed=<n> audit_actor=<serial|NONE-WRITTEN|UNKNOWN> ok=<True|False>` as in the draft, where `other_changed` counts, CLIENT-SIDE with explicit pagination (never `--query length()` on a paginated list), the keys of `s3://opal-data-bd/code/gold/` other than the target whose LastModified is later than the entry's opened time (the entry is `org/critical_paths/.open_deploys/ctlpln-r21-fwd5-one-script-20261015.json`, key `opened_at` or its equivalent; if the entry does not exist yet print `other_changed=-1` and `ok=False`), and `audit_actor` is `NONE-WRITTEN` when the audit log has no row for the path (row S9131: a ledgered box-diff deploy writes none; that is not a failure by itself); `--pre`: the pre-deploy state: prints `FWD5-PRE target=diag_sleeve_fix.py versions=<n> repo_blob=<10 hex> repo_md5=<hex> s3_etag=<hex> differs=<True|False> others_differ=<n> ok=<True|False>` with `ok=True` exactly when the target's repository md5 differs from the S3 ETag and none of the other top-level gold scripts in the repository differs from its S3 object (read the S3 side with `head-object` ETags for the top-level gold scripts; a multipart ETag is reported as `skipped` and counted, not as a difference); `--ast-identical`: prints `AST-IDENTICAL ast_identical=<True|False>` comparing `ast.dump` of the file at the commit before yours and at yours (docstrings kept; the only change is comments, which the AST does not carry). Remove the `--docstring-only` flag.
3. Commit the test with `.tools/safe-commit.sh` as its own commit (explicit path). The AWS reads are the only network calls; if any call would be a write, STOP and file a BLOCKING row.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~118/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W118-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. You may ask for no override; if safe-commit REFUSES, STOP and file a BLOCKING row.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTak4-AC1" cell_refs="CT-ak-4"><invocation>python .tools/tests/test_round21_fwd5_positive_read.py --pre</invocation><expect>ok=True</expect></criterion>
`CTak4-AC1` -- before the deploy, exactly the target differs from S3 and no other top-level gold script does (base: the file is untracked and has no `--pre` flag); report the whole `FWD5-PRE` line.

<criterion id="CTak4-AC2" cell_refs="CT-ak-4"><invocation>python .tools/tests/test_round21_fwd5_positive_read.py --ast-identical</invocation><expect>ast_identical=True</expect></criterion>
`CTak4-AC2` -- the signed change is comment-only: the AST of the script is identical before and after (base: no such flag); report the whole line.

<criterion id="CTak4-AC3" cell_refs="CT-ak-4"><invocation>python -m py_compile data/black_diamond/scripts/gold/diag_sleeve_fix.py && echo PARSE-OK</invocation><expect>PARSE-OK</expect></criterion>
`CTak4-AC3` -- the edited script still compiles (base: it compiles; a control); report the output.
</proof_of_spec>

<expected_criteria>CTak4-AC1,CTak4-AC2,CTak4-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~118/NFRA_CTLPLN.TO-CT-ak-4.signed-change-commit-and-positive-read-test.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTak4-AC1,CTak4-AC2,CTak4-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round21.md</decomp_doc>
<owned_cells>CT-ak-4</owned_cells>
</decomp_ref>

<paths>
data/black_diamond/scripts/gold/diag_sleeve_fix.py
.tools/tests/test_round21_fwd5_positive_read.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write; reads only (`s3api head-object` and `list-objects-v2` through the `.tools/aws` shim).
comp-adversary: RUN -- a code token changing in the script (the AST-identical arm); the commit carrying a second file; a multipart ETag read as a difference (counted as skipped); the test writing to AWS (read-only calls, asserted by reading the file); the merge of this commit making the next box-sync push deploy the script before the ledger entry opens: it cannot, because the hook HOLDS an unledgered deploy-scope script and writes a HELD-DEPLOY row (the round-19 negative arm), which is expected noise; BLIND: the deploy itself is CT-ak-3's.
risk: LOCAL -- a docstring edit and a read-only test; nothing deploys until a ledger entry pins this blob (CT-ak-3).
lane: the <paths> block IS the grant (worker RULING 1). `data/black_diamond/scripts/gold/diag_sleeve_fix.py` is lane POD4 and the test is lane TOOL_BATTERIES; both admit a `0.9.0_WK_NFRA_CTLPLN~<n>` serial through this order's `<paths>` (ADHC_OWNPTH.005). The deploy seat CT-ak-3 does not write either.
</preflight>

Base checks, dry-run by the issuer before the cut: CTak4-AC1 and CTak4-AC2 FAIL as expected (the committed test does not exist; the draft is untracked and lacks the flags); CTak4-AC3 PASSES (the script compiles).
Source: CTO round-20 analysis sections 2-3 (`ledger/ROUND_ANALYSIS.round20.md` @5df0b0af31), msg 109441; FWD-5.
