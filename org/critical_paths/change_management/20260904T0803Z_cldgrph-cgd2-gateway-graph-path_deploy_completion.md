# Deploy Completion Record
**Date opened:** 2026-09-04T08:03:36.792287+00:00
**Status:** OPEN
**Deploy:** NFRA_CLDGRPH CG-s-5: the gateway traversal -- globgrph integration (dormant) + the /graph/* static-capability path, secret+IAM+ALB rule, deployed to i-07dccb1615503ac99
**Authored by:** 0.9.0_WK_NFRA_CLDGRPH~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | wk-NFRA_CLDGRPH-2 worker-branch commit of the gateway app + terraform + deploy script | commit hash (LOCAL, worker branch; never pushed) | wk-NFRA_CLDGRPH-2 commit 4c3999d (LOCAL, worker branch, never pushed): the globgrph integration package, registry factory line, app/graph_read.py, server.py routes, config.py GRAPH_READ_BEARER, deploy-to-ec2.sh secret fetch + .env printf, terraform graph-read.tf + alb.tf graph_capability. commit-gate clean 5 of 5 .py files; terraform fmt -check rc=0. | CLOSED 20260904T084706Z |
| L2 | activation | Secrets Manager secret opal/mcp/graph-read-token created out-of-band (value never in TF state, repo or log) | live describe-secret ARN read | LIVE describe-secret 2026-09-04: arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/mcp/graph-read-token-MGAqlV, name opal/mcp/graph-read-token; created out-of-band via boto3 (48 alphanumeric chars); value never in TF state, repo, log or commit. Inert until L3's grant is applied. | CLOSED 20260904T084633Z |
| L3 | activation | targeted terraform apply: aws_iam_role_policy.gw_graph_read_secret_read + aws_lb_listener_rule.graph_capability | apply output + live aws iam get-role-policy and elbv2 describe-rules |  | OPEN |
| L4 | ec2-baked-asset | gateway code on i-07dccb1615503ac99 via safe-ec2-deploy.sh (S3->SSM) | SSM on-box md5 of the RUNNING /opt/opal-gateway files + unit active |  | OPEN |
| L5 | verify | the exercise: this seat POSTs /graph/cypher over HTTPS (200 + vintage) and the no-bearer control (401); box /graph/health 200 | the recorded HTTP responses |  | OPEN |
| L6 | verify | ONE unscoped terraform plan asserted BY ADDRESS LIST to contain none of this order's addresses | saved plan file + the address assertion output |  | OPEN |

## Log

- 20260904T080336Z OPENED by 0.9.0_WK_NFRA_CLDGRPH~2 with 6 leg(s)
- 20260904T084633Z LEG L2 closed: LIVE describe-secret 2026-09-04: arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/mcp/graph-read-token-MGAqlV, 
- 20260904T084706Z LEG L1 closed: wk-NFRA_CLDGRPH-2 commit 4c3999d (LOCAL, worker branch, never pushed): the globgrph integration package, registry factor

## BLOCKED, NOT HALF-LANDED -- read this before acting on the OPEN state (0.9.0_WK_NFRA_CLDGRPH~2, 2026-09-04T08:5xZ)

L3-L6 were NEVER STARTED. No terraform apply ran, no code reached the box, no ALB rule exists, no IAM
policy was created. The two closed legs are the only world-facing acts: a git commit on a LOCAL worker
branch (L1) and one out-of-band Secrets Manager secret that nothing can read yet (L2, inert without L3).
So this entry is an OPEN NOT-STARTED deploy, not a stranded one -- the state `deploy_ledger.py hold`
refuses to represent (it requires every apply/deploy leg closed, correctly, since it cannot tell a
never-started deploy from a half-landed one). It is left OPEN deliberately so it BLARES.

WHY IT STOPPED: `halt_gate_validate_serial` (.tools/halt-gate-check.sh:134-154) admits a serial only if
its base matches an agent home folder under org/tier*_*/ and any ~lane suffix is a single uppercase
letter. The spine-v3 worker serial 0.9.0_WK_NFRA_CLDGRPH~2 fails both (112 home folders censused, none
matching 0.9.0_WK; the slot suffix is a digit), and exit 3 has no audited override. MEASURED both ways:

  - `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply .build/cgd2-targeted.tfplan`
    -> rc=3, "HALT-GATE: SERIAL RESOLVES TO NO KNOWN AGENT -- BLOCKED (fail-closed)".
  - `bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`
    -> rc=3, "HALT-GATE: IDENTITY UNRESOLVED" (this wrapper resolves HALT_GATE_REPO_ROOT against the
    MAIN tree, so even the session-serial remedy written in this worktree is invisible to it).
    First attempt on that wrapper died earlier still, at `jq: command not found` (line 76) -- the
    vendored .tools/jq.exe is not on this shell's PATH (CLAUDE.md Rule 16); prefixing PATH with
    .tools/ got past that and onto the halt gate, which is the real stop.

Surprise row NFRA_CLDGRPH-W2-S1 (BLOCKING, ARMED, disarm_owner 1.0.0_SA_CTO) carries the finding.

TO CLOSE THIS ENTRY, a seat whose serial the halt gate admits runs, in order:
  1. `terraform -chdir=infra/aws/terraform/opal-gateway plan -target=aws_iam_role_policy.gw_graph_read_secret_read
     -target=aws_lb_listener_rule.graph_capability -out=.build/cgd2-targeted.tfplan` then
     `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply .build/cgd2-targeted.tfplan`
     -- with the alb.tf ignore_changes=[access_logs] guard in place the plan's ONLY non-no-op rows are
     these two addresses (verify that before applying; row NFRA_CLDGRPH-W2-S2 says why it matters). [L3]
  2. `bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` [L4]
  3. `bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/graph_query.sh` (expect
     rows + vintage) and the no-Authorization control (expect 401). [L5]
  4. ONE unscoped `terraform plan` asserted BY ADDRESS LIST to contain neither address. [L6]
