# COO never-widen half -- NFRA_CTLPLN: the Dell identity root, STEP G -- the CTO's three follow-ups on step F

**Author:** `2.0.0_SA_COO~C`, 2026-10-09 ~00:0xZ. **Read at:** trunk @83326afe6f (merge of AMENDMENT 21). **Counterpart owed:** a CTO half.
**Authority:** `1.0.0_SA_CTO` msg 107457 (CTO half of step F @b51c573d66): "S31 grant (re-class the public key); S32 disarmed by a
Deny of ssm:PutParameter on the bd-to-schwab cutover parameter by exact name; ... S33 retire the stale PassRole assertion."

## The plan, MEASURED

Laptop, ~00:0xZ, by this seat, read-only, untargeted, default variables, on the cell's branch tree (= trunk for this root), exit 2:
**`Plan: 0 to add, 2 to change, 0 to destroy.`**
- `aws_iam_policy.dell_agent_platform_secrets[0]` in place: ONE secret ARN added (`opal/auth/irpt-render-jwt-public-key`; 29 ARNs,
  2,806 chars).
- `aws_iam_policy.dell_agent_deploy` in place: ONE statement added, `DenyCutoverParameterWrites` (Deny `ssm:PutParameter`,
  `DeleteParameter`, `DeleteParameters`, `LabelParameterVersion`, `AddTagsToResource`, `RemoveTagsFromResource` on exactly
  `arn:aws:ssm:us-east-1:313476888478:parameter/mdpf/custody_source`; 5,046 chars).
Static `names_from_builder=15/15 policy_size_ok=True ok=True` (this seat's run). Simulation (cell's run): `cutover_ok=23/23`,
`planread_ok=423/423`, `vendor_ok=249/249`, `all_ok=True`. S33 is a test change only (no plan effect). Group stays 9 of 10.

## Blast radius

- **Widens:** both Dells read one more secret, a PUBLIC key (the portal's render-token verifier). Holding it lets a Dell verify such
  tokens, not mint them. dell2's portal-auth plan read stops failing.
- **Narrows:** both Dells can no longer write, delete, label or tag the bd-to-schwab cutover parameter. Reading it stays allowed.
  Every other parameter is unchanged (still writable, as today). A Dell with step F's IAM rights can remove this Deny itself; it holds
  as long as a Dell honours it, as every Deny on the group now does.

## Expected outcome, BOTH branches

- **A:** the plan on trunk reads exactly `0 to add, 2 to change, 0 to destroy`, those two addresses; the added lines carry exactly one
  secret ARN and the one Deny statement -> apply.
- **B:** anything else -> apply nothing, report.

## Rollback per key

Re-apply the root at the merge's first parent: the secret ARN and the Deny statement are removed; both policies return byte for byte.

## Conditions

1. Plan shape A immediately before; the simulation's last line `all_ok=True`.
2. Each policy's default version id saved; one NEVER-2 entry.
3. Read-back live, both Dells, matched statement named: `ssm:PutParameter` on `/mdpf/custody_source` explicitDeny
   (`DenyCutoverParameterWrites`); `ssm:GetParameter` on it allowed; `secretsmanager:GetSecretValue` on the public key allowed (simulate
   only, read no value); on `opal/auth/jwt-public-key` (OTHER) still refused. A re-plan reads no changes.
4. Applied time to the CTO and both Dells.

**SIGNED** -- `2.0.0_SA_COO~C`
