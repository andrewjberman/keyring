# TO IRPT_BCKEND.TO-IB-hm-1 -- READ the facts the served account-id HMAC list producer is built on (CTO ruling B, msg 10161): where the refresh's last stage goes, where the served ids live, how they are spelled, the naming and IAM additions, the gate, the tests

<to_id>IRPT_BCKEND.TO-IB-hm-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~447</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>~PM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `IB-hm-1` (decomposition section 242) | **outcome_ref:** FWD-21 | **Ordered by:** the plan `deliverables/2.0.0_SA_COO~P2/ACCOUNT_ID_HMAC_LIST_PRODUCER_PLAN_20261017.md` (blob `f1f250ab37`) and the CTO's ruling B (msg 10161): the HMAC step goes in `irpt-directory-refresh`, LAST stage, after the directory write commits; the role gains `GetSecretValue` on one ARN and `PutObject` on one key.

---

## WORKER FACE

**Cell `IB-hm-1` (inlined).** A READ-ONLY measurement of the repository. Nothing is built, nothing is changed except your one record file, and **no AWS call is made**. You answer seven questions with evidence a reader can open: every answer cites `path:line` of the repository at the worktree HEAD, and the line must exist. The facts feed the next cells (the producer code, the Terraform, the pair); a wrong or guessed fact misleads them, so say `NOT FOUND` and what you searched rather than guess. **Never write an account id, a client id, a holding name or a value into the record: field NAMES and counts of code lines only.** Paths you post are `file:///` absolute URIs or markdown links (CLAUDE.md rule 33).

Read-only tools: `Read`, `Grep`, `Glob` and Bash `git`/`python` for reads; no recursive grep over the repository root (scope every search to the named folders below).

**The seven questions** (answer each in the record under `q1` to `q7`):

1. **The last stage.** In `infra/aws/lambda/investor-reporting/directory/refresh.py` (`lambda_handler`, from line 1200), name the line after which every firm's directory write has committed and per-firm results are collected, and say whether any `try/except` wraps that loop. A stage appended after it must never be able to change, roll back or mask the loop's outcome: state in one sentence where a failure of the new stage would be caught so that it does not alter the returned result.
2. **Where the served ids live.** Which structure carries the served account ids per firm during a refresh (`refresh_firm`, line 944; `compute_delta`, `entries`, `source_client_ids`): name the field(s), say whether they are ACCOUNT ids or CLIENT ids, and say how a firm's directory object is read (the S3 key pattern from `local.directory_prefix` and the object format). Field names only.
3. **The spelling.** The normalisation of the ids in the directory (case, padding, prefix) against what the hook hashes: read `.tools/git-hooks/client-data-check.py` and name the token regex it hashes and the `UPPER` it applies. State whether `UPPER(id)` of the directory's id equals the hook's token for the same id.
4. **The names.** Which `lib/opal_naming.py` builders and `infra/logic/registry/` rows exist (a) for a Secrets Manager secret in the irpt tier and (b) for the globgrph fabric bucket's product folder and a key in it; list the registry rows that would have to be ADDED (names only), or `NOT FOUND` with what you searched.
5. **The IAM and env additions.** In `infra/aws/terraform/investor-reporting/directory/schedule.tf` the policy `data.aws_iam_policy_document.irpt_directory_refresh` lists its statements; name the ones that exist (Sids) and the exact two statements a `secretsmanager:GetSecretValue` on ONE secret ARN and an `s3:PutObject` on ONE key require, which file holds the Lambda environment map, and whether a new environment variable is needed.
6. **The gate.** Read the enumeration in `.tools/ds-precommit-check.py` (`_CROSS_FIRM_FOREIGN_BUCKETS`, `_CROSS_FIRM_FOREIGN_KEY_PREFIXES`) and say whether the refresh Lambda source or its Terraform root would be flagged for a reference to the globgrph fabric bucket or its product-folder key; a read, not a run.
7. **The tests.** Name the test file(s) for `refresh.py` and the pattern they use to inject a failure (a stub client, a monkeypatch), with one test name as the model for a planted-failure test.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~447/IBhm1_facts.json`:
`{"q1":{"answer":"<text>","evidence":["path:line", ...]},"q2":{"answer":"<text>","id_kind":"account|client","field_names":["..."],"evidence":[...]},"q3":{"answer":"<text>","hook_token_regex":"<regex>","upper_equal":true|false,"evidence":[...]},"q4":{"answer":"<text>","registry_rows_to_add":["<name>", ...],"evidence":[...]},"q5":{"answer":"<text>","existing_sids":["..."],"statements_to_add":["secretsmanager:GetSecretValue","s3:PutObject"],"env_file":"<path>","new_env_var":true|false,"evidence":[...]},"q6":{"answer":"<text>","flagged":true|false,"evidence":[...]},"q7":{"answer":"<text>","test_files":["..."],"model_test":"<name>","evidence":[...]},"notes":"<text>"}`. Every `evidence` entry is `repo/relative/path:line`.

**Run the three criteria below from the repository root**, record each output and exit code verbatim in `IBhm1_criteria_output.txt` (same folder), write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, commit with explicit paths (`.tools/safe-commit.sh`, your own author, `-F`). Report once, under 150 words.

**Criteria (run each under `timeout 120` from the repository root):**

<criterion id="IBHM1-AC1" cell_refs="IB-hm-1"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r247/p247_cells.py" . IBHM1-AC1</invocation><expect>IBHM1-AC1 PASS</expect></criterion>
<criterion id="IBHM1-AC2" cell_refs="IB-hm-1"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r247/p247_cells.py" . IBHM1-AC2</invocation><expect>IBHM1-AC2 PASS</expect></criterion>
<criterion id="IBHM1-AC3" cell_refs="IB-hm-1"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r247/p247_cells.py" . IBHM1-AC3</invocation><expect>IBHM1-AC3 PASS</expect></criterion>

<expected_criteria>IBHM1-AC1, IBHM1-AC2, IBHM1-AC3</expected_criteria>

What the checks grade: AC1 all seven answers present, each with at least one evidence entry whose file exists and whose cited line exists; AC2 no id-like token in the record (no run of 8 or more digits, no `acc_`-shaped token) and the id kind named; AC3 the registry rows to add listed, the two IAM statements named exactly, the hook regex and the equality stated. Do not edit the checks.

## BOUNDS

- **Grant:** read access to the repository at your worktree HEAD; write only `deliverables/0.9.0_WK_IRPT_BCKEND~447/` (your record, criteria output and proof instance). **NO AWS call of any kind; NO edit of any other file; NO account or client id, holding name or value in any record; no push.**
- **Refusal clause:** STOP and report, writing nothing further, if a cited file does not exist at HEAD, or if answering a question would need a live read (say which question and what you would have read). A surprise is a ROW: file one (`spec_asserts` plus `world_is`) in the project's surprise channel and keep working; a broker message is never the carrier.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~447/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-hm-1.read-the-hmac-list-producer-facts.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 242 (round 6, workstream ~PM), cell `IB-hm-1`.
<owned_cells>IB-hm-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBHM1-AC1, IBHM1-AC2, IBHM1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~447/IRPT_BCKEND.TO-IB-hm-1.read-the-hmac-list-producer-facts.proof_of_spec.json` (the file stem of THIS order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read of repository files; nothing is deployed, written or changed beyond one record folder.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface is touched.
comp-adversary: RUN -- p247_cells.py IBHM1 dry-run at base on dell2 2026-10-17 ~03:0xZ: AC1 to AC3 FAIL (no record). Positive control (control247.py): the three positives PASS and each negative (a missing question, an evidence cite to a missing file or a line past the end, an id-like token, a missing id kind, an empty registry-row list, the wrong IAM statements, a missing hook regex or equality flag, a non-dict record) fails its own arm. NOT measured by me: every answer itself (the worker reads the repository), whether the facts are right (the issuer reads the cited lines at the drain), anything live.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~447`. Class LOCAL.
</preflight>
