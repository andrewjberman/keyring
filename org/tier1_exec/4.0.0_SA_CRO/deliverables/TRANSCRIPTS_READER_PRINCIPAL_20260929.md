# The second reader of opal-data-transcripts: what opalbloomberg@opalinvest.com is

- Author: `4.0.0_SA_CRO~T`, 2026-09-29. Step 4 of
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_PLACEMENT_20260929_170xZ_TRANSCRIPTS_BUCKET_LANDING.md`.

## Finding (measured from source; AWS IAM not read)

opalbloomberg@opalinvest.com is a Microsoft Entra identity. It is the sign-in of the Bloomberg terminal seat
(`0.0.3_BG_BBGTerminal`) to the Opal gateway, where it is a tool-scoped identity.

| Evidence | File |
|---|---|
| Entra login secret `opal/mcp/opalbloomberg-login`, "the MS ENTRA login for the SAME SEAT" | `integrations/bloomberg/auth/bbg_credentials.py:8` |
| Gateway per-identity tool allowlist seeded for this address | `infra/aws/ec2/opal-gateway/app/identity_scope.py:52` |
| Mailbox that requests@opalinvest.com forwards into | `infra/aws/terraform/investor-reporting/core/roles.tf:31` |

No AWS principal for it appears in first-party source. Denominator: 46 first-party files matching the address
(`comp-find -i opalbloomberg --band SURFACED`), 3 read as carrying its identity, 0 naming an IAM user or role.
The live IAM plane was not read, so an IAM identity created outside the repository is not excluded.

## Consequence

A Microsoft account cannot be written into a KMS key policy or an S3 grant. "Two readers" therefore needs one of:

| Route | What is built | Who holds key use |
|---|---|---|
| A. Through the gateway (recommended) | a gateway read tool over the bucket, admitted to exactly the two addresses by the existing per-identity allowlist | the gateway's instance role, plus Andrew's IAM user |
| B. A dedicated IAM role for the terminal seat | a role the terminal box assumes | that role, plus Andrew's IAM user |

Route A keeps the rule in the place that already knows both Microsoft identities. Its cost: the gateway role can
decrypt, so the gateway's own allowlist becomes the control that holds the two-reader rule.

## Owner

Andrew chooses the route. Until then the key grants use to `arn:aws:iam::313476888478:user/Andrew_Berman` only.
