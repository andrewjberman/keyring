# NFRA_OPLGTW task order -- `OG-gw-2` -- the one catch-up apply: the grant writer redeployed from af2d762970's closure

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gw-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~26</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot targeted apply; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the function's role and policies stay as they are (a targeted plan of the function alone).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling R1 (ledger/ROUND_ANALYSIS.round14.md @cf6e539a6d).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (Lambda read/update through Terraform, the presigned code URL of Opal's own function).
</preflight>

## 1. THE CELL -- `OG-gw-2` (decomposition addendum R3-T.8, item 2)

Handed only after `OG-gw-1` is drained to CLOUD (the builder stages from the manifest's `deployed_commit`).

`mcportal-grant-writer-lambda` runs a 2026-09-30 build of the gateway's `app.config`, `app.data_entitlement` and the
contract JSON (`deliverables/0.9.0_WK_NFRA_OPLGTW~17/TF_ROOT_FIX.md` s.1). The CTO's ruling R1 says to redeploy it ONCE
from the released gateway ref `af2d7629702528c050860314a7867d8ea0cecfbf`'s closure, in its own apply cell under CTO +
COO + CVO halves. The CVO half is required because `data_entitlement` decides whom grants admit.

### PHASE A (pre-GO): read-only; no apply

1. **The released ref.** The manifest at HEAD names `af2d762970` for `services.opal-gateway`. Run `build_package.py` and
   confirm it printed that commit.
2. **Content diff, deployed vs staged.**
   - Read the deployed zip IN MEMORY (`aws lambda get-function` `Code.Location`). Table each file's sha256, deployed vs
     staged.
   - For each differing file, write the `git diff` from the deployed blob to the staged blob (`TF_ROOT_FIX.md` names
     the deployed blobs: `config.py` = `c19f86c295`, `data_entitlement.py` = `aac92bdff8`, contract = `c2f5d5a071`).
   - Under each diff, NAME EVERY BEHAVIOUR CHANGE the grant writer will see. Trace each changed symbol to the grant
     writer's use of it (`lambda_function.py`, `app.access_state`, `ops.schwab_entitlement_admin`): which grants it
     would now admit or refuse differently, and which config keys it would now require.
   - Write all of this to `GW2_BEHAVIOUR_DIFF.md`. The CVO grades this file.
3. **Environment before-record.** Write `GW2_ENV_BEFORE.json` as `{"env": {NAME: sha256(value)}}` for every key of the
   function's current environment: names and hashes only.
4. **Targeted plan.**
   - Make it from a FRESH sparse worktree of your branch, `-target=aws_lambda_function.mcportal_grant_writer` only.
   - The root has two required variables with no default (`mcportal_owner_key_claim`, `mcportal_owner_key`; `OG-tf-2`
     removes them later). Feed them ONLY as `TF_VAR_*` read in memory from the live function's own environment, as
     OG-pr-1 A1 did. Never print them, never write them to a file.
   - The plan must show exactly one in-place update, of that function, whose only changing attributes are the code hash
     (`source_code_hash`, and `last_modified` as computed). `environment` must be unchanged.
   - Any other diff: STOP and report. Save the plan out of the repo.
5. **The tests** of the grant writer (`tests/`) pass against the staged package's closure.
6. **Rollback, Terraform only** (CLAUDE.md bars `aws lambda update-function-code`).
   - Save the deployed zip's bytes OUTSIDE the repo and record their sha256.
   - The rollback is: extract those bytes into a rollback worktree's `.build/staged`, then run the SAME targeted
     `safe-apply` with the same variable feed.
   - Prove at PHASE A, without applying, that this rollback plan exists and is equal in shape to step 4's plan: one
     in-place update of the function, code hash only.
7. Write `ANNOUNCE_OG-gw-2.md` (steps 1-6, numbers only, no value). Commit and report. Do NOT apply.

### PHASE B (GO): only after the issuer says GO (CTO + COO + CVO halves SIGNED)

8. Re-read: the deployed `CodeSha256` is unchanged since PHASE A and the manifest still names `af2d762970`. If either
   moved, re-cut PHASE A.
9. Open the NEVER-2 ledger `nfra-oplgtw-grant-writer-catchup` (legs: apply, read-back, rollback-proven). Commit the entry
   AND the sentinel BEFORE the act.
10. Re-plan with the same target and the same variable feed, confirm it is equal in shape to step 4, then `safe-apply`
    it. Capture the apply line literally.
11. Read back IMMEDIATELY:
    - `gw2.AC1.sh` (deployed = staged, file by file);
    - the environment hashes equal `GW2_ENV_BEFORE.json`;
    - one invocation-free health read: `get-function-configuration` `State`/`LastUpdateStatus` = `Active`/`Successful`;
    - CloudWatch Logs for the function show no ERROR in the window after the apply, if it was invoked.
    Any failure: roll back per step 6 (the targeted apply of the saved bytes), re-verify, close ROLLED BACK.
12. Close every leg with proof, remove the sentinel, commit.

## 2. BOUNDS

- **May change:** ONLY `aws_lambda_function.mcportal_grant_writer`'s code. Its environment, role, policies, layer and
  every other resource stay untouched.
- **Never:** an untargeted apply; `aws lambda update-function-code` (Terraform only, rollback included); print or
  commit a variable's value.
- **Not exercised here:** no grant is written and no portal flow is driven. The grant writer's behaviour is graded from
  the code diff (step 2) by the CVO, not by a live grant.
- **Never:** push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-grant-writer-catchup.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~26/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W26-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gw-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r15/checks/gw2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)diff 0 only-deployed 0 only-staged 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gw-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r15/checks/gw2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)entry files at HEAD=[1-9]\d*; sentinel at HEAD=no.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the deployed grant writer equals, file by file, the closure of the released gateway ref.
- `AC2`: NEVER-2 closed, and the function's environment unchanged by the act.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~26/NFRA_OPLGTW.TO-OG-gw-2.grant-writer-catchup-apply.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 15 (addendum R3-T.8, item 2). Chained after `OG-gw-1`; `OG-tf-2` follows it.
- Halves: CTO + COO + CVO (R1). The never-widen ask is written at PHASE A from `GW2_BEHAVIOUR_DIFF.md`.
- Pre-cut 18:2xZ: `gw2.AC1` FAIL with 3 DIFF; `gw2.AC2` FAIL (no ledger, no before-record).

<status>pending</status>
<round>15</round>
<slot>~26</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
