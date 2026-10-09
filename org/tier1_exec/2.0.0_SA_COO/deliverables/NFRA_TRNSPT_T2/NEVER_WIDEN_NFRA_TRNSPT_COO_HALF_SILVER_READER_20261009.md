# Never-widen COO half (NFRA_TRNSPT) -- FWD-5: the silver-only reader role (TR-a-21)

Signer `2.0.0_SA_COO~T2` (NFRA_TRNSPT, dell2), 2026-10-09 ~12:3xZ. Ordered by CTO ADDENDUM 12.1 ("reads Teams and outlook SILVER only, never
bronze, through `name()`, under a never-widen pair"), holders RULED by `1.0.0_SA_CTO~DELL2` msg 3248 (@374553467d: the raw-tier readers, Andrew
and the two Dell agent users). Bound to TO-TR-r21 as drained @365a08577e: `infra/aws/terraform/transcripts/readers.tf` (`silver_reader` role,
policy, attachment, `local.silver_reader_trust_arns`) and `main.tf` (`SilverReaderDecryptOnly`). Names: `data/transcripts/scripts/teams/NAMES.json`
`silver_reader`, `lib/opal_naming.py` `name()` output.

**Paired with:** the CTO half (owed by `1.0.0_SA_CTO~DELL2`); not effective until it is committed.

## The act -- exactly this

ONE `safe-apply` of `infra/aws/terraform/transcripts` at a pin carrying @365a08577e, `-target`ed to `aws_iam_role.silver_reader`,
`aws_iam_policy.silver_reader`, `aws_iam_role_policy_attachment.silver_reader` and `aws_kms_key.transcripts`. The plan shows those three
CREATES and ONE in-place update of the key policy whose ONLY difference is the added `SilverReaderDecryptOnly` statement; anything else = STOP.

**Ordering with TO-APPLY-a18** (the second reader, at the laptop, also an in-place update of the same key policy): `-target` pulls in
dependencies, so a key-policy apply at a pin carrying BOTH readers' code changes the key for both. Either a18 lands first at its own pin and this
act's key diff is the one statement, or the two run as ONE apply whose key diff is exactly the two statements, under both pairs. A key diff
naming anything else = STOP.

**Executor:** an identity that administers the transcripts key -- the laptop (MSTR route), as for a18; dell2's identity does not.

## Writers of the named properties

| property | writers | N | rule read |
|---|---|---|---|
| key policy `SilverReaderDecryptOnly` | this act | 1 | Decrypt + DescribeKey for the silver role only, `kms:ViaService` = S3 us-east-1 |
| any other key-policy statement | this act (unchanged) / a18 | 2 | this act changes none; a18's `NamedReadersUseTheKey` principal is a18's pair (ordering above) |
| the silver role's S3 reach | this act | 1 | GetObject on `teams/transcripts/silver/*` + `outlook/transcripts/silver/*`; prefixed ListBucket; explicit Deny on `teams/transcripts/silver/research_meeting/*` (row D2-S13); no bronze, no write |
| who may assume the role | this act | 1 | `concat(var.reader_principal_arns, the two Dell agent users)` -- principals who already read the raw tier |

## Both branches

- **Applied as planned:** the three ruled principals gain a NARROWER path to what they already read; nobody new reads anything. Research
  silver is unreadable through the role while its held-out text is kept at the writer.
- **Plan differs (an extra create, a changed principal, any other key statement):** STOP before apply; nothing changes.

## Proof (FWD-8's pattern, on demand after apply)

The Dell2 agent user assumes the role and makes three reads, statuses only, no content:
- one Teams silver object (monday_meeting) -> 200;
- one Teams bronze object -> AccessDenied;
- one research_meeting silver object -> AccessDenied.

FWD-5 grades on Andrew's own read through the role (the CTO ruling).

## Rollback per key

The role, policy and attachment are CREATES; destroying them is Andrew's word. The key-policy statement is removed by re-applying the prior
policy: the plan's before-image goes in the ledger. That is an update, not a delete.

## Conditions

- A change ledger opened and closed with the pin.
- The key-policy diff printed in full in the ledger.
- No transcript content anywhere.

-- 2.0.0_SA_COO~T2
