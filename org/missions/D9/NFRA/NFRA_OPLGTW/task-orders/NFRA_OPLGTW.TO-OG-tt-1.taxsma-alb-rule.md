# NFRA_OPLGTW task order -- `OG-tt-1` -- the ALB rule for EXACTLY /ms/taxsma-workbook (Tax SMA release, half 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-tt-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~18</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one listener rule, created once; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; an ALB listener rule only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the shape is the CTO's (msg 27986: exact path, no /ms/* wildcard, plan 1/0/0) under Andrew-direct ~17:2xZ.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (ELBv2 via safe-apply) and unauthenticated GETs to the public gateway URL.
</preflight>

## 1. THE CELL -- `OG-tt-1` (decomposition addendum R3-T.4)

Andrew-direct ~17:2xZ: site Z runs the Tax SMA gateway release; the MDPF_TAXSMA exclusion is lifted for this one
release. The route `GET /ms/taxsma-workbook` checks its own capability bearer, so the edge must forward that exact path
without the Entra sign-in, as `infra/aws/terraform/opal-gateway/hx-capability.tf` (your OG-al-1) does for `/hx/*` and
`ms-ingest.tf`'s exact `/ms/*` rules do (priorities 31 and 33).

1. Write `infra/aws/terraform/opal-gateway/taxsma-capability.tf` on the `hx-capability.tf` pattern: ONE
   `aws_lb_listener_rule` on `aws_lb_listener.https.arn`, ONE `forward` to `aws_lb_target_group.gw.arn`, ONE
   `path_pattern` with EXACTLY `/ms/taxsma-workbook`, a priority unused on the live listener (re-read with
   `aws elbv2 describe-rules`; live at ~17:2xZ: 10 20 30 31 32 33 34 35; 36 if free). Any name or Name tag is
   `lib/opal_naming.py` `name()` output (a builder refusal: no name, as OG-al-1). Header comment: why, the post-apply
   verify. No other resource.
2. Targeted plan of that one resource, fed as OG-al-1 was (owner-key variables from the live grant-writer Lambda into
   `TF_VAR_*`, never printed; `build_package.py --out <scratch zip>`; the deps-layer zip copied from the main tree
   `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/`). It must read exactly 1 to add, 0 to change, 0 to destroy.
3. **GO is given in advance for this cell, conditioned:** if step 2 reads 1/0/0, the priority is free and no other
   `safe-apply` on `infra/aws/terraform/opal-gateway` is in flight (`ls -a org/critical_paths/.open_deploys/` names no
   gateway Terraform ledger), proceed. Otherwise STOP with a BLOCKING row.
4. Open the NEVER-2 ledger, slug `nfra-oplgtw-taxsma-alb-rule` (legs: rule, probe); commit the entry AND its sentinel
   BEFORE the act. TARGETED `safe-apply` of that one rule, fed as in step 2; capture the `Apply complete!` line itself.
5. Run AC2. If any arm fails after the apply, roll back (targeted destroy of that one resource through `safe-apply` if it
   admits it, otherwise STOP and report loud with the ledger left open and named) and close ROLLED BACK. Otherwise close
   every leg with proof.

## 2. BOUNDS

One listener rule, nothing else: no change to `alb.tf`, `ms-ingest.tf`, `hx-capability.tf`, the listener default, the
target group, any security group, IAM or the instance. No gateway release. Never print a variable value. Never push,
merge, rebase, stash, `checkout --` or `clean`; never override a gate. Commit with `.tools/safe-commit.sh`.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/taxsma-capability.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-taxsma-alb-rule.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~18/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W18-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-tt-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/tt.AC1.sh; echo "exit=$?"</invocation><expect>(?s)listener rules 1 .*path patterns \['/ms/taxsma-workbook'\].*action types \['forward'\].*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-tt-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/tt.AC2.sh; echo "exit=$?"</invocation><expect>(?s)live rules carrying the Tax path: 1 .*probe tax: status \d+, redirects to sign-in False.*probe ms_unknown: status 302, redirects to sign-in True.*probe root: status 302, redirects to sign-in True.*probe ms_sites: status 401, redirects to sign-in False.*sentinel at HEAD=no.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: one forward-only rule, exactly the Tax path, nothing else declared.
- `AC2`: APPLIED and EXERCISED: the Tax path reaches the app (404 until OG-tr-1 mounts it), the negative arms hold.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~18/NFRA_OPLGTW.TO-OG-tt-1.taxsma-alb-rule.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`; if both PASS, append a `complete` status tag after
the order's last status line in the same commit. Report once: the priority, the rule ARN, plan and apply lines, the literal AC1-AC2 output, commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 12 (addendum R3-T.4) with `OG-tr-1`. Train Terraform act #4 (after MS-dn-1 #3, closed ~15:1xZ).
- Pre-cut control: `tt.AC2.sh` reads 0 Tax rules; the Tax path, an unknown /ms path and / all 302 to sign-in; /ms/sites 401.
- `<risk>` WORLD: a public-surface rule; the route's capability bearer is the gate.

<status>pending</status>
<status>complete</status>
<round>12</round>
<slot>~18</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
