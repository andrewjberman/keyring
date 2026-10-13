# TO IRPT_ANLREQ.TO-AR-y-217.irpt-status-with-status-py -- irpt-status with the current status.py (the 24 correction words) on the live package

<to_id>IRPT_ANLREQ.TO-AR-y-217</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~66</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-217` (`decompositions/IRPT_ANLREQ_DECOMP_R20S_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~66`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-66` (branch `wk-IRPT_ANLREQ-66`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~66 <0.9.0_WK_IRPT_ANLREQ~66@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W66-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call EXCEPT the read-only `get-function` and the download of its `Code.Location` zip named below; no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-217`, inlined) -- irpt-status WITH THE CURRENT ops/status.py. Nothing is uploaded, deployed or applied.

*The deployed `irpt-status` has 4 of the 28 correction words; the finding words the upload door now returns have no words in its envelope (row W55-S25).* The CTO ruled (round 20, row D2-W55-S25) that the status rule's all-eight pair carries the current `ops/status.py` to `irpt-status`. `AR-y-212` (record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~61/r20/STATUS_RULE_REBASE_GROUP_A.json`) already built `irpt-status` with `served.py` moved to pin `564e60483858a3cc5c51ffea6aed0f76ff291abe`; this cell adds `ops/status.py`.

**READ FIRST, AND TWICE: never run `build-and-upload.sh` without `BUILD_ONLY=1`, and never at a commit whose copy lacks the guard (check `git show <commit>:infra/aws/lambda/ci/build-and-upload.sh | grep -c BUILD_ONLY` is at least 1 BEFORE the first build). At commits older than the guard the script UPLOADS to the artifact key; it did so on 2026-10-13 and this seat had to restore a key (row D2-S69). The base below carries the guard (8 mentions).**

**Read first:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~61/r20/STATUS_RULE_REBASE_GROUP_A.json` (the `irpt-status` object: `live_code_sha256`, `base_commit`, `holds_only_control`, `release`, `patch`), and the pinned and trunk `ops/status.py` (`CORRECTION_WORDS`, around lines 86-150 of the pinned file; the function `build_status_envelope` adds a `CORRECT` action only when the code has words).

1. **Live read.** `.tools/aws lambda get-function --function-name irpt-status --query Configuration.CodeSha256 --output text` must print `JmOhV/ep4mR1mt2NKKqyUlohgO3mlDw1GEM4eAWYKdw=` (a single-resource read; the `.tools/aws` shim); anything else: STOP, record it, file a BLOCKING row. Download `Code.Location` into a NEW EMPTY folder under your `.scratch/r20/` (write the URL to a file and read it from Python run with `-I`), check its sha256 base64 equals the CodeSha256, and take `live_member_manifest` (member name -> sha256).
2. **Base.** A throwaway worktree OUTSIDE the product tree, DETACHED at `5d8b0390ed` (group A's base: its holds-only build reproduced the live CodeSha256). Check the guard (above), then `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-status`; copy the zip at once. It must print the live CodeSha256: that is `holds_only_control`.
3. **The release patch.** In that worktree move TWO `staged_from` rows of the `irpt-status` entry of `infra/aws/lambda/ci/lambda-source-map.json`: `_authz/served.py` to `564e60483858a3cc5c51ffea6aed0f76ff291abe` (sha256 of that blob) and `ops/status.py` to `status_py_pin`, the latest trunk commit that touched it (`git log -1 --format=%H -- infra/aws/lambda/investor-reporting/ops/status.py`; expected `e93258c650...`; give the FULL sha), each with the sha256 of its blob at that commit. Save `r20/irpt-status.release2.diff` (git diff of the map only; the trunk map is NOT edited) and print `git hash-object`. BUILD_ONLY. The release's members against the live manifest: `served.py` and `status.py` differ and nothing else, unless one cannot be imported without another member at a newer version (then name it in `must_move_with` with the import line as `reason`; move no other).
4. **Is the status.py difference words only?** Parse the pinned `ops/status.py` (`361c44fa9d`) and the released one with `ast`; remove the module-level assignment `CORRECTION_WORDS` from both; the two trees must be equal (`ast.dump`). Record `status_py_diff_words_only` and `correction_words` {`before`: count of keys in the pinned dict, `after`: count in the released}.
5. **Tests.** Extract the release zip to a scratch folder; run the `ops/tests` folder with the release `served.py` and `status.py` staged in place of the head ones (in a scratch copy of the tree), under `timeout 580`; record `tests` {`folder`, `passed`, `failed`, `failed_names`, `control_failed_names` (the same run with the ORIGINAL live `served.py` and `status.py`), `staging`}. Then the parity test `infra/aws/lambda/investor-reporting/intake/tests/test_correction_words.py::test_correction_words_are_the_envelopes_words` against the released `status.py` and the trunk's `intake/uploads.py` (the one the Lambda runs since release 19): `parity` {`passed`: true or false, `output_tail`}.
6. **Write the record** `r20/IRPT_STATUS_STATUS_PY_RELEASE.json`: `live_code_sha256`, `live_member_manifest`, `base_commit`, `holds_only_control` {`code_sha256`}, `release` {`code_sha256_b64`, `package_sha256`, `member_manifest`}, `status_py_pin`, `status_py_diff_words_only`, `correction_words`, `must_move_with`, `tests`, `parity`, `patch` {`path`, `git_hash_object`}, `claim`, `not_read`.
7. **In your report:** the live read, the holds-only result, the members that differ, the words before and after, the tests and the parity result.

### ACCEPTANCE

<criterion id="AR217-y-AC1" cell_refs="AR-y-217"><invocation>python C:/dev/wk-irpt-anlreq-66/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r20/ar20_checks.py y217-status --root C:/dev/wk-irpt-anlreq-66</invocation><expect>Y217-STATUS-OK</expect></criterion>
`AR217-y-AC1`: the record holds the live read, a holds-only control that reproduces the live CodeSha256, a release that differs from the live package in `served.py` and `status.py` only (but members named with a reason), a `status.py` difference that is words only (24 or more words added), the ops tests passing (pre-existing failures excepted as named), and the parity test passing.

<criterion id="AR217-y-AC2J" cell_refs="AR-y-217" judgment="true"/>
`AR217-y-AC2J` (judgment, graded at L9, never by you): the live package was read from AWS in this run, the base was proved by a holds-only build, the guard was checked before every build, and the words-only claim rests on the AST comparison and not on reading the diff.

<expected_criteria>AR217-y-AC1 AR217-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~66/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R20S_Y.md</decomp_doc>
<owned_cells>AR-y-217</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~66/IRPT_ANLREQ.TO-AR-y-217.irpt-status-with-status-py.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-217`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read-only `get-function` and a zip download, local BUILD_ONLY builds (guard checked) in a throwaway worktree outside the product tree; nothing is uploaded, deployed or applied.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading row D2-S69 (a build at a pre-guard commit uploaded) against the cell; the lens: a build at a commit without the guard, or a status.py difference called words-only by reading. The order requires the guard check before every build and an AST comparison. NOT seen: the Lambda's configuration.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-20 analysis row D2-W55-S25 as workstream `YR` round 11. Base: `AR217-y-AC1` FAIL as expected (no record).
- The PAIR and the APPLY are not this order.
