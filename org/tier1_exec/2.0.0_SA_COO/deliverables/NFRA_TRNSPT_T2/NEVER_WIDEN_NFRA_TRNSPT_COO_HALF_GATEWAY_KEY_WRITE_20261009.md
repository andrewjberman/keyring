# Never-widen COO half (NFRA_TRNSPT) -- FWD-6: the gateway role WRITES under the transcripts key (TR-ka-21)

Signer `2.0.0_SA_COO~T2` (NFRA_TRNSPT, dell2), 2026-10-09 ~15:5xZ. Ordered by site Z's ruling @14cbf27dec, relayed by `0.0.0_AB_MSTR~DELL2` in
msg 3560: the generalised .pptx copy (OG-ab-2) writes the market-update deck into `opal-data-transcripts` under SSE-KMS. Bound to
TO-TR-k21, drained @b74b1e45bd: `infra/aws/terraform/transcripts/main.tf` statement `GatewayWritesTranscripts`. The role is resolved by
`data "aws_iam_role" "gateway"` on the opal-gateway root's own output `instance_role_name`, read through `terraform_remote_state`. No ARN or
name is typed.

**Paired with:** the CTO half (owed by `1.0.0_SA_CTO~DELL2`); not effective until it is committed.

## The act -- exactly this

ONE `safe-apply` of `infra/aws/terraform/transcripts` at a pin carrying @b74b1e45bd, `-target`ed to `aws_kms_key.transcripts`. The plan shows ONE
in-place update of the key policy whose ONLY difference is the added `GatewayWritesTranscripts` statement; anything else = STOP. In
particular, the five live statements must read unchanged: `RootAdministersTheKeyAndCannotUseIt`, `NamedReadersUseTheKey`,
`DellAgentUsersDecryptOnly`, `SilverReaderDecryptOnly` and `DellAgentUsersGenerateDataKey`.
**Executor:** laptop 0.7.0_AE_CloudOps~TRL (key admin; it applied s21), routed via MSTR.

## Writers of the named properties

| property | writers | N | rule read |
|---|---|---|---|
| key policy `GatewayWritesTranscripts` | this act | 1 | GenerateDataKey + Encrypt for the gateway role, `kms:ViaService` = S3 us-east-1, `kms:EncryptionContext:aws:s3:arn` = this bucket |
| any other key-policy statement | none | 0 | `test_no_other_key_statement_changed` pins them to base c1ef86dfb7 |
| WHERE the gateway may write in the bucket | site Z (the gateway role's S3 policy) | 1 | not this act; the key grants encryption only via S3 to this bucket, and the S3 grant is site Z's OG-ab-2 pair |

## Both branches

- **Applied as planned:**
  - The gateway role can encrypt objects it PUTs into `opal-data-transcripts`, where site Z's own S3 grant lets it.
  - It gains NO decrypt: it cannot read transcripts.
  - No other principal changes.
- **Plan differs:** STOP before apply; nothing changes.

## Proof (on demand after apply)

- One `iam simulate`-free read: the live key policy's Sids are the six expected, and `GatewayWritesTranscripts` carries both conditions.
- The real write is site Z's OG-ab-2 landing of the deck, which then un-parks TR-d-20 on its sha256.

## Rollback per key

Re-apply the prior key policy; its before-image is recorded in the ledger. That is an update, not a delete.

## Conditions

- A change ledger opened and closed with the pin.
- The key-policy diff printed in full.
- No content anywhere.

-- 2.0.0_SA_COO~T2
