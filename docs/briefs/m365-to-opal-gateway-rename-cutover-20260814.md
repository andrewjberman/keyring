# Brief: rename `m365-mcp-gateway` -> `opal-gateway` across ALL infrastructure

**Authorization (Andrew-direct 2026-08-14, verbatim):** *"is the opal-gateway properly named opal
gateway in all relevant infrastructure? i do not want it named m365 or any bullshit like that
anywhere"* + *"scope the full rename and bring me the cutover plan."*

**Owner:** `0.0.0_AB_MSTR` scopes + routes; an **AE/DT-class seat** executes (EC2 / IAM / ALB lane).
**Governance:** falls under Andrew's 2026-08-14 no-hanging-items order -- explicit owner + day, nothing
past the agreed window.

## The finding

The rename to `opal-gateway` (commit `042f96d446`) was **cosmetic -- only the MCP service's
presented name.** The underlying infrastructure is pervasively still `m365`. The service *works*;
the name being m365 is not a functional defect -- this is a naming-hygiene cutover, and its benefit
is cosmetic, which sets the risk bar: do NOT break a live client-M365-adjacent service for a name.

## Complete inventory (measured live 2026-08-14 via AWS CLI; reproducible)

### Live AWS
- **EC2 instance `i-07dccb1615503ac99`:** `Name` tag `m365-mcp-gateway`, `System` tag `M365MCPGateway`
  (both mutable). `Project=OpalPortal`, `Environment=Production` already fine.
- **IAM:** roles `m365-mcp-gateway-role`, `m365-ms-ingest-liveness-role`, `m365-otp-liveness-role`;
  instance profile `m365-mcp-gateway-profile`. (immutable names)
- **Secrets Manager:** `opal/mcp/m365-login`, `opal/mcp/m365-graph`, `opal/mcp/m365-fernet`,
  `opal/mcp/m365-gateway-jwt`. (the box reads these BY NAME at boot)
- **Network:** ALB `m365-mcp-gateway`; target group `m365-mcp-gateway-tg`; security groups
  `m365-mcp-gateway-alb-sg`, `m365-mcp-gateway-sg`; WAF (log group `aws-waf-logs-m365-mcp-gateway`
  -> get the web-ACL's own name). (immutable names)
- **Lambda:** `m365-otp-liveness`, `m365-ms-ingest-liveness`.
- **CloudWatch log groups:** `/aws/lambda/m365-ms-ingest-liveness`, `/aws/lambda/m365-otp-liveness`,
  `aws-waf-logs-m365-mcp-gateway`.
- **S3 code path:** IAM scoped to `ec2/m365-mcp-gateway/*` (confirm exact bucket -- the deploy
  artifact store used by safe-ec2-deploy).
- **On-box:** systemd unit `m365-mcp-gateway`; remote path `/opt/m365-mcp-gateway`.
- **CLEAN (no m365):** Route53/DNS, SSM params. **This matters** -- the external endpoint is not
  m365-named, so the CLIENT-FACING address likely does not change; only the backend renames.

### Repo
- Code home `infra/aws/ec2/m365-mcp-gateway/` (entire app, config, `.service`, `deploy-to-ec2.sh`).
- `infra/aws/ec2/EC2_MANIFEST.json` entry (keys: `instance_name_tag`, `source_path`, `remote_path`,
  `deploy_script`, `iam_role`).
- Runbooks: `docs/runbooks/m365-gateway-readonly-scope-gap.md`,
  `docs/runbooks/m365-gateway-secrets-rotation.md`.
- Historical change-mgmt records + org logs (low priority; leave or sweep last).

## Load-bearing constraint

Most of these have **immutable names in AWS** (IAM roles, ALB, TG, SGs, Lambda, log groups,
secrets). A "rename" is therefore **create the `opal-*` twin -> repoint dependents -> verify ->
delete `m365-*`**, NOT an in-place edit. The service is **live + client-M365-adjacent** (agents'
access to real client mailboxes/SharePoint), so the cutover MUST keep it serving throughout, with
rollback at every step.

## Cutover plan -- blue/green, 4 phases

- **P0 -- repo + metadata (ZERO service impact, safe now):** `git mv infra/aws/ec2/m365-mcp-gateway
  -> .../opal-gateway`; rewrite EC2_MANIFEST keys/paths; rename the runbooks + `.service`; update
  every code ref; retag the instance (`Name`->`opal-gateway`, `System`->`OpalGateway`). Mechanical.
- **P1 -- build the `opal-*` twins (additive, nothing live changes):** create
  `opal-gateway-role`/`-profile` + the 2 liveness roles mirroring the m365 policies, scoped to the
  new `ec2/opal-gateway/*` S3 prefix; copy the 4 secrets to `opal/mcp/opal-gateway-{login,graph,
  fernet,jwt}`; stand up `opal-gateway` TG + SGs + Lambdas + WAF web-ACL. All parallel.
- **P2 -- the flip (health-gated, rollback-ready):** deploy the code from the new S3 prefix onto the
  box (or a fresh instance -- decide) reading the `opal-*` secrets under the `opal-*` profile;
  register in the new TG; **flip the ALB listener m365-TG -> opal-TG**; verify a live MCP round-trip
  THROUGHOUT (health + one real tool call); swap SGs. **Rollback = flip the listener back.**
- **P3 -- retire m365-* (after a soak):** delete the m365 secrets, IAM roles/profile, ALB/TG/SGs,
  Lambdas, log groups, WAF, and the old S3 prefix. Update EC2_MANIFEST + verify-ec2 parity.

## Open items to resolve BEFORE P2 (execution-scoping, not blockers)

1. **How clients address the gateway** -- ALB DNS directly, or a clean Route53 alias? Determines
   whether the ENDPOINT changes or only the backend. DNS is clean, so likely endpoint-stable, but
   confirm; if any MCP registration string embeds the ALB name, update it atomically at the flip.
2. **The WAF web-ACL's own name** (only the log group name is known).
3. **Exact S3 deploy bucket** for the `ec2/m365-mcp-gateway/*` prefix.
4. **In-place vs fresh instance** for P2 -- a fresh blue/green instance is cleaner (no live-box IAM/
   secret surgery) but heavier; the box was already replaced once (i-01d75... -> i-07dcc...), so a
   fresh-instance cutover is a proven path here.

## Deploy discipline (CLAUDE.md)

EC2 code deploys via S3 -> SSM (`safe-ec2-deploy.sh`), Terraform manages EC2 *infra* not code,
`EC2_MANIFEST.json` is the source of truth, verify parity (`infra/aws/ec2/verify-ec2.sh`). Any
TF-managed resources among the above (IAM/ALB/SG/TG likely are) must be renamed THROUGH Terraform
(state move or create/destroy), never in the console. The safe-ec2-deploy wrapper has a known
Windows-charmap false-negative (reports failure after a successful SSM deploy) -- verify on-box, not
by the wrapper's exit.

## Reproduce the inventory
`aws ec2 describe-instances --instance-ids i-07dccb1615503ac99 --query 'Reservations[0].Instances[0].Tags'`
; `aws iam list-roles`/`list-instance-profiles`; `aws secretsmanager list-secrets`;
`aws elbv2 describe-load-balancers`/`describe-target-groups`; `aws ec2 describe-security-groups`;
`aws lambda list-functions --query 'Functions[].FunctionName' --output text | grep m365` (materialize,
do not per-page filter); `aws logs describe-log-groups`; `aws route53 list-resource-record-sets`.
Filter each for `m365`/`M365`.
