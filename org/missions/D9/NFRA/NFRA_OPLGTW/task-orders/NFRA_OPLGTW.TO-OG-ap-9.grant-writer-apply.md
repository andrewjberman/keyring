# NFRA_OPLGTW task order -- `OG-ap-9` -- APPLY: rebuild `mcportal-grant-writer` from the live gateway release (OG-gw-1), `-target`

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-9</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-9</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one Lambda's code by Terraform; no schedule touched. Run it after OG-ap-8's ledger closes (one act in flight on this seat).
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; its role and policies are unchanged (the targeted plan proves it).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the signed pair over org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~56/NEVER_WIDEN_ASK_OG-gw-1.md: COO org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_HALF_COO_OG-gw-1_20261011.md @88926383b1, CTO org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_OG-gw-1_20261011.md @bef54b9b62.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-9` (decomposition addendum R3-T.43)

`mcportal-grant-writer` ships an old copy of the gateway's `data_entitlement.py` and contract, so it refuses every
`calendar_months` grant (row W42-S1). Rebuild it from the live release. READ the ask and both halves; they BIND, and the
COO half's condition B REPLACES the ask's section-5 owner-session grant (no grant is written by this order).

1. **Ledger** `nfra-oplgtw-grant-writer-rebuild`: entry AND sentinel committed before the act.
2. **Prior.** Record the live `CodeSha256` (expected `ZyYCPPyP5CV53eZP+UJHIgAjq834J4OsvePgmS6k8rI=`) and download the
   PRIOR package (`get-function` Code.Location) to `W/ap9_prior.zip`.
3. **Plan, FRESH, from a DETACHED worktree at box/sitez HEAD** (`C:/tmp/og-tf-ap9`). Read
   `infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf` lines 20-60 for how the `data.external` stage builds. Run
   `terraform plan -target=aws_lambda_function.mcportal_grant_writer -var market_update_s3_root=<R>`, with `<R>` from
   `address()` as in OG-ap-8. Save it to `W/ap9_plan_target.txt` / `.rc`: `0 to add, 1 to change, 0 to destroy` at
   rc=0, that address only, `source_code_hash` only. Any other row is a STOP.
4. **Apply** with `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply`, with the same `-target` and
   `-var`. Never use `aws lambda update-function-code`. Re-plan into `W/ap9_replan.txt` / `.rc`: 0/0/0 at rc=0. Write
   `W/ap9_build.json` = `{"code_sha256": <the live CodeSha256 after the apply, which equals the built zip's>}`.
5. **Session-free read-back** (COO half condition B). Download the DEPLOYED package. With each package's OWN
   `parse_scope` (deployed and `W/ap9_prior.zip`), parse `{"mode":"rolling_complete_window","calendar_months":13}`.
   Write `W/ap9_parse.json` = `{"deployed_accepts_13": true|false, "prior_accepts_13": true|false}`. The prior package
   must refuse it (the negative control).
6. Update `infra/aws/lambda/ci/lambda-source-map.json`'s grant-writer entry to the deployed build (deploy rule 4), close
   the ledger, commit, run AC1 and AC2, and report once to `2.0.0_SA_COO~O`. Rollback, if any read-back disagrees:
   redeploy the prior `code_sha256` through the same path, then an ARMED row naming `2.0.0_SA_COO~O`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`.

## 2. BOUNDS

- That one function's code. No grant written or revoked, no principal changed, no other resource in the root.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform apply`; print a secret; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-grant-writer-rebuild.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-9"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/ap9.AC1.sh; echo "exit=$?"</invocation><expect>(?s)entries at HEAD [1-9]\d*; status CLOSED=yes; sentinel at HEAD=no.*ap9_plan_target\.txt: rc=0 summary=\(0, 1, 0\).*ap9_replan\.txt: rc=0 summary=\(0, 0, 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-9"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/ap9.AC2.sh; echo "exit=$?"</invocation><expect>(?s)live CodeSha256 equals the build: yes; differs from the prior: yes.*deployed package accepts calendar_months 13: True; prior package accepts it: False.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the act is landed and closed, planned and re-planned at rc=0. `AC2`: the live code is the build, and it takes a
  13-month scope that the prior code refused.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-9.grant-writer-apply.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, and flip the ONE `<status>` tag
to `complete` only if both PASS.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 34, workstream APPLY-R34. This closes the opal-gateway half of row W39-S5 and row W42-S1.
- Pre-cut: ap9.AC1 and ap9.AC2 base FAIL as expected (records absent). Control: _tfplan.py read OG-gw-1's saved plan as
  0/1/0 at rc=0 on the one address (PASS), and FAILED when asked for 1/0/0.

<status>complete</status>
<round>34</round>
<workstream>APPLY-R34</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
