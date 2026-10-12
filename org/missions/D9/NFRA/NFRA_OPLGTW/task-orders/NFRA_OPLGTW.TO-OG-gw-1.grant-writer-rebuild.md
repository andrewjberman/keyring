# NFRA_OPLGTW task order -- `OG-gw-1` -- rebuild `mcportal-grant-writer` from the live gateway release (E2), PHASE A: build, plan, ask

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gw-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gw-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~56</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- Phase A builds and plans; nothing is applied or uploaded.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; its role and policies are unchanged (the plan proves it).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's round-32 analysis @3566a85699 row W42-S1 (cell E2), and its C3 ruling @eb37eb2e29 that the grant-writer drift row belongs to this cell.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (plan-time reads).
</preflight>

## 1. THE CELL -- `OG-gw-1` (decomposition addendum R3-T.42, E2)

The Lambda `mcportal-grant-writer` writes portal grants. It ships its own copy of the gateway's `data_entitlement.py` and
entitlement contract, pinned at an old gateway commit, so it refuses every `calendar_months` grant (row W42-S1). Its
package is built by `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/build_package.py`, which reads the released
commit from `infra/aws/ec2/EC2_MANIFEST.json` `services.opal-gateway.deployed_commit` (live: `c3af8687e4`). Its
Terraform is `infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf`: read lines 20-60 first. A
`data.external` stage builds at plan time, and `source_code_hash` follows the deployed version unless a rebuild is
staged.

1. Build: `python infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/build_package.py --out W/mcportal-grant-writer.zip`.
   Its `data_entitlement.py` and contract members must equal the live release's blobs (AC1).
2. Plan, read only, from a DETACHED worktree at box/sitez HEAD (`C:/tmp/og-tf-gw1`; never a release branch, row Z-S81).
   Run `terraform plan -target=aws_lambda_function.mcportal_grant_writer` in `infra/aws/terraform/opal-gateway`, staged
   so the rebuild is what the plan reads. The two required variables `mcportal_owner_key_claim` and
   `mcportal_owner_key` come from the secret `gateway/principals/rosters`, by `TF_VAR_` env only: never argv, never a
   file, values redacted from saves. Save the plan to `W/gw1_plan.txt` and its exit code to `W/gw1_plan.rc`. A plan at
   rc!=0 is not a verdict: re-run it to rc=0.
3. The never-widen ask, `W/NEVER_WIDEN_ASK_OG-gw-1.md`, for `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~O`. It carries:
   - the code delta (old pinned commit -> c3af8687e4, by member);
   - the one Terraform change;
   - both branches of a grant write (refused vs written);
   - the rollback (redeploy the prior code_sha256);
   - the read-back: one 13-month grant written through the rebuilt function, read back.
4. Run AC1 and AC2, commit, REPORT, STOP. The apply is a later applier order under the signed pair.

## 2. BOUNDS

- Build and plan only. No apply, no upload, no `aws lambda update-function-code`, no grant written.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform apply`; print a secret; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Everything you write goes in `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~56/`, or in
gitignored `.build/` output. Rows: id `NFRA_OPLGTW-Z-W56-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`;
`surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gw-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/gw1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)entitlement members checked [2-9]\d* \(want >=2\); differing 0 \[\].*contract-staging test: pytest rc=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gw-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/gw1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)plan rc=0; summary: Plan: 0 to add, 1 to change, 0 to destroy\.; changed addresses 1: aws_lambda_function\.mcportal_grant_writer.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the package carries the live entitlement code. `AC2`: the only planned change is that one function.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gw-1.grant-writer-rebuild.proof_of_spec.json` and validate it with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`. Phase A leaves the order
`pending`. Report once. Your next order (OG-wr-1) follows on this same slot.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 34, E2. This clears the opal-gateway half of row W39-S5. The opal-assets half went to 2.0.0_SA_COO~C (ADVI_COTBKF).
- Pre-cut: gw1.AC1 and gw1.AC2 base FAIL as expected (zip and plan absent).

<status>complete</status>
<round>34</round>
<slot>~56</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
