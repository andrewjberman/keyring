# NFRA_OPLGTW task order -- `OG-ap-8` -- APPLY: OG-mu-1's market_update PutObject grant (one inline policy, `-target`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-8</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-8</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one IAM inline policy; no host, schedule or release touched. Run it after OG-ap-7's ledger closes (one act in flight on this seat).
comp-iam: RUN-BY-ISSUER -- ONE new inline policy on opal-gateway-role, aws_iam_role_policy.market_update_gateway_put: s3:PutObject on opal-data-transcripts/sharepoint/transcripts/bronze/market_update/* only. Live before: absent (the role's 21+ inline policies carry no market_update put). KMS leg already live (GatewayWritesTranscripts, CTO read @e0ca80f880).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the signed pair over org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~55/NEVER_WIDEN_ASK_OG-mu-1.md: COO org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_HALF_COO_OG-mu-1_20261011.md @34bf3d67a4, CTO org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_OG-mu-1_20261011.md @e0ca80f880.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-8` (decomposition addendum R3-T.43)

Land ONE IAM statement so the gateway's `.pptx` writer (built in OG-mu-1, NOT yet released) can later write the
market_update bronze prefix. READ the ask and both halves; they BIND, especially the COO half's conditions A and B.

1. **Ledger** `nfra-oplgtw-mu1-put-policy`: entry AND sentinel committed before the act.
2. **Plan, from a DETACHED worktree at box/sitez HEAD** (`C:/tmp/og-tf-ap8`; never a release root, row Z-S81). In
   `infra/aws/terraform/opal-gateway`, run
   `terraform plan -target=aws_iam_role_policy.market_update_gateway_put -var market_update_s3_root=<R>`.
   Take `<R>` from the builder, never typed:
   `python -c 'from lib.opal_naming import address; a=address("sharepoint","transcripts","bronze","market_update","date=X"); print(a[:-len("date=X")])'`.
   It must end in `/bronze/market_update/`. Save the plan to `W/ap8_plan_target.txt` and its exit code to
   `W/ap8_plan_target.rc`. It must read `1 to add, 0 to change, 0 to destroy` at rc=0, on that one address (the
   pure-name module adds no resource). Any other row is a STOP, and a summary at rc!=0 is not a verdict.
3. **Apply** with `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply`, with the same `-target` and
   `-var`. Then re-plan the same target into `W/ap8_replan.txt` / `.rc`: 0/0/0 at rc=0.
4. **Read back.** Write `W/ap8_policy.json` = `{"role": "opal-gateway-role", "policy_name": "<the live name>"}`. AC2 reads
   it live.
5. Close the ledger, commit, run AC1 and AC2, and report once to `2.0.0_SA_COO~O`. Rollback, if any read-back
   disagrees: `terraform destroy -target=aws_iam_role_policy.market_update_gateway_put` through the same path, then an
   ARMED row naming `2.0.0_SA_COO~O`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`.

## 2. BOUNDS

- The one inline policy. No other resource in the root, no release, no gateway host act, no object written.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform apply`; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-mu1-put-policy.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-8"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/ap8.AC1.sh; echo "exit=$?"</invocation><expect>(?s)entries at HEAD [1-9]\d*; status CLOSED=yes; sentinel at HEAD=no.*ap8_plan_target\.txt: rc=0 summary=\(1, 0, 0\).*ap8_replan\.txt: rc=0 summary=\(0, 0, 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-8"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/ap8.AC2.sh; echo "exit=$?"</invocation><expect>(?s)live read rc=0; statements 1; actions \['s3:PutObject'\]; resources \['arn:aws:s3:::opal-data-transcripts/sharepoint/transcripts/bronze/market_update/\*'\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the act is landed and closed, planned and re-planned at rc=0. `AC2`: the live policy is exactly the signed one.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-8.market-update-grant-apply.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, and flip the ONE `<status>` tag
to `complete` only if both PASS.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 34, workstream APPLY-R34 (the applies of round 34's signed Phase A cells). The `.pptx` code ships only in a later
  gateway release, after this ledger closes (COO half condition C).
- Pre-cut: ap8.AC1 and ap8.AC2 base FAIL as expected. Control: ap8.AC2 run against the live E2 policy
  `gateway-49f-advi-billing-put-policy` parsed it (rc=0, 1 statement, PutObject) and FAILED only on the resource. The
  control record was removed.

<status>pending</status>
<round>34</round>
<workstream>APPLY-R34</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
