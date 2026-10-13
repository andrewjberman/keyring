# NFRA_MCPORTAL task order -- `MP-n-5` -- WORKSTREAM C17 ROUND 2: the deploy helper keeps previous_deployed_commit (E2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-n-5</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-n-5</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~19</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a deploy wrapper's helper; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM; a local JSON rewrite.
comp-adversary: DECLARED-NOT-APPLICABLE -- the equal-commit arm is the adversary.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MP-n-5` (workstream C17 round 2, decomposition section C17R2.1)

Your worktree is `C:/tmp/mp-n5-19` (branch `wk-NFRA_MCPORTAL-n5-19`). Work and commit only there.

`infra/aws/ec2/safe-ec2-deploy.sh` rewrites `infra/aws/ec2/EC2_MANIFEST.json` after a deploy through an embedded Python
helper (the heredoc between `<<'MANIFEST_HELPER_PY'` and its terminator, about `:206-232`). `update_manifest()` moves only
`services.<svc>.deployed_commit`, `deployed_at`, `deployed_by` and `_last_updated`. It never writes
`previous_deployed_commit`, so that field goes stale on every release and has been hand-fixed three times (MP-x-4,
MP-r-2, MP-n-1).

Build:
1. **In the helper only:** before setting `deployed_commit`, when the new `commit` differs from the recorded
   `svc.get("deployed_commit")`, copy the recorded value into `svc["previous_deployed_commit"]`. An equal commit (a
   re-deploy) moves nothing in that field. A service with no recorded `deployed_commit` gets no
   `previous_deployed_commit`. Keep the heredoc terminator exact; keep escape style, key order, newline convention and
   trailing newline as the helper keeps them now. Update the comment block above the heredoc to list the field it now
   moves.
2. **`.tools/tests/test_safe_ec2_deploy_manifest.py`:** it already extracts and runs the heredoc. Add two arms, by these
   exact names:
   - `test_new_commit_moves_previous_deployed_commit` -- a manifest whose service records commit A; run the helper with
     commit B: `previous_deployed_commit` == A and `deployed_commit` == B.
   - `test_equal_commit_leaves_previous_unchanged` -- record B with `previous_deployed_commit` == A; run with B again:
     `previous_deployed_commit` is still A, and the file differs from before only in `deployed_at`, `deployed_by` and
     `_last_updated`.
   Every existing arm must still pass (the module's MOVABLE tuple already names `previous_deployed_commit`).

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Change nothing in `safe-ec2-deploy.sh` outside the helper body and its
   comment block. No deploy, no AWS call, no manifest edit.
2. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md
   14a). If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/safe-ec2-deploy.sh
.tools/tests/test_safe_ec2_deploy_manifest.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~19/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/EC2_MANIFEST.json`, `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/c17r2/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W19-S<k>` (the next free k for W19). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an
ARMED row is `2.0.0_SA_COO~MP`. Append a row as ONE whole fenced ```json block.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-n-5"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/c17r2/checks/n5.AC1.sh; echo "exit=$?"</invocation><expect>manifest helper tests: 0 failed; named tests PASSED 2 of 2 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~19/NFRA_MCPORTAL.TO-MP-n-5.manifest-previous-commit.proof_of_spec.json`.
Report once, with: the check output; the commit hash; the helper diff; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the C17 round-2 issuance (decomposition v8) from ROUND_ANALYSIS.c17-round1.md E2 ("LOCAL. It
may run as a DIRECT ACT"); the L6 gate floors it WORLD because <paths> names infra/aws/ec2/safe-ec2-deploy.sh, so it is
cut as a WORLD build order without the direct-act flag. It changes no deployed thing: the next release run of the
wrapper is its first real use. Check dry-run at the base: AC1 FAIL (8 passed, named 0 of 2). Close: the issuer's drain run
of the file.

<status>pending</status>
<round>2</round>
<workstream>C17</workstream>
<slot>~19</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<status>complete</status>
