# Never-widen COO half (NFRA_TRNSPT) -- FWD-8: the second named reader's role (TR-a-18)

Signer `2.0.0_SA_COO~T2` (NFRA_TRNSPT, dell2), 2026-10-09 ~08:4xZ. Ordered by CTO ADDENDUM 6 @7558d41da5 ("the principal is minted by name
through name(), under a pair ... a laptop identity-allow-list act if dell2 cannot write it ... routes it through MSTR"). Bound to TR-p-18 merged
@f8c4859407: `infra/aws/terraform/transcripts/readers.tf` + `main.tf` (`NamedReadersUseTheKey` reads `local.named_reader_arns`).

**Paired with:** the CTO half (owed by `1.0.0_SA_CTO~DELL2`); not effective until it is committed.

## The act -- exactly this

ONE `safe-apply` of `infra/aws/terraform/transcripts`, `-target`ed to `aws_iam_role.second_reader`, `aws_iam_policy.second_reader`, its
attachment, and `aws_kms_key.transcripts` (the key policy's `NamedReadersUseTheKey` gains ONE principal: the new role). The plan shows those
three CREATES and ONE in-place update of the key policy whose only difference is that principal; anything else = STOP.
Executor: an identity that may edit the transcripts key policy -- the laptop (MSTR route), since dell2's identity does not administer the key.

## The open decision this half does NOT make (the trust)

`var.second_reader_trust_principal_arns` has no default (readers.tf). Who may ASSUME the role is the mapping of Andrew's named account
`opalbloomberg@opalinvest.com` to an AWS identity. An IAM user `Opal_Terminal` exists (issuer read 08:2xZ) but nothing on the record maps it to
that account. This half signs the role and the key-policy line; the trust value is named in the CTO half, on Andrew's routing, never inferred.

## Writers of the named properties

| property | writers | N | rule read |
|---|---|---|---|
| `NamedReadersUseTheKey` principals | this act | 1 | `concat(var.reader_principal_arns, [second_reader])`; Andrew_Berman unchanged |
| any other key-policy statement | none | 0 | TR-p-18's test asserts them byte-identical to ffa3c6987d |
| the role's S3 reach | this act | 1 | GetObject on `opal-data-transcripts/*`, ListBucket on the bucket; no write |

## Both branches

- **Trust supplied:** the named identity can assume the role and read the original transcripts; no other principal gains anything (FWD-8's
  "only the readers he named"; the refusal of an unnamed principal is the FWD-8 proof, run on demand after apply).
- **Trust not supplied:** terraform refuses the plan (no default); nothing changes.

## Rollback per key

The role, policy and attachment are CREATES (destroy = Andrew's word). The key-policy line is restored by re-applying the prior policy (the
plan's before-image is recorded in the ledger); that is an update, not a delete.

## Conditions

A change ledger opened and closed with the pin; the plan's key-policy diff printed in full in the ledger; no transcript content anywhere.

-- 2.0.0_SA_COO~T2
