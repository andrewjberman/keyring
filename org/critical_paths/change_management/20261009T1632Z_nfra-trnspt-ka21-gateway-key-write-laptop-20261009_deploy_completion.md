# Deploy Completion Record
**Date opened:** 2026-10-09T16:32:57.435334+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T165325Z
**Deploy:** NFRA_TRNSPT ka21 gateway key-write statement at pin 95a62b9f29fdff643344667b82e5364203e3c002 carrying b74b1e45bd (pair COO 6791d6ebc2 + CTO ad98587dfa)
**Authored by:** 0.7.0_AE_CloudOps~TRL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| PRECHECK | verify | the opal-gateway runtime role's S3 write reach into opal-data-transcripts | every policy attached to the role enumerated (managed + inline) with the statement denominator printed; each S3 write statement and the probe ARNs it matches; the verdict reached by SUBTRACTION, with a planted-statement control proving the matcher fires on a wildcard | CASE: NO S3 WRITE GRANT. Role resolved the way main.tf does it (data.terraform_remote_state.opal_gateway.outputs.instance_role_name from s3://opal-313476888478-terraform-state/opal-gateway/tfstate) -> opal-gateway-role, confirmed live. Every attached policy enumerated and decoded: 22 documents (1 managed, 21 inline), 29 statements, 11 of them naming an S3 action. Verdict by SUBTRACTION over all 29 rather than by searching for the bucket name, with 20 S3 write actions pattern-matched against 5 probe ARNs including wildcards: 0 Allow statements grant a write reaching opal-data-transcripts and 0 Deny statements reach it. The role's only S3 write anywhere is AuditLakePutOnly, s3:PutObject on arn:aws:s3:::opal-mcp-audit/audit/* -- a different bucket. CONTROL: five planted statements through the same matcher -- s3:PutObject on arn:aws:s3:::*/* FLAGGED (4 probes), s3:* on * FLAGGED (20 writes, 5 probes), the permitted-prefix shape FLAGGED, another bucket not flagged, a read-only grant not flagged -- so the zero comes from a matcher that demonstrably fires. The order names this a pass: the key statement alone writes nothing. Site Z's OG-ab-2 owns the S3 grant and the CTO half's branch-2 prefix condition binds it when it lands. Bucket Key read by the applier: BucketKeyEnabled=true -> branch 2 governs. | CLOSED 20261009T163601Z |
| APPLY | activation | aws_kms_key.transcripts | safe-apply from a saved plan showing ONE in-place key-policy update whose ONLY difference is the added GatewayWritesTranscripts statement; the five live statements byte-identical; full key diff printed in this entry | safe-apply SUCCESS from the SAVED plan ka21.tfplan at pin 95a62b9f29fdff643344667b82e5364203e3c002 (carries b74b1e45bd; negative control HEAD-in-b74b1e45bd read NO). Apply complete: 0 added, 1 changed, 0 destroyed; aws_kms_key.transcripts Modifications complete after 5s. Plan graded from terraform show -json BEFORE the apply: 1 non-no-op over a denominator of 4 resource_changes, the only changed attribute being policy, with aws_iam_role.second_reader, aws_iam_role.silver_reader and aws_s3_bucket.transcripts all no-op and zero changes from the four Lambda files. No attribute was after_unknown, so unlike s21 the PLAN ITSELF was the oracle: planned statements 5 to 6, ADDED GatewayWritesTranscripts only, REMOVED none, all five pre-existing statements byte-identical in the plan's after-document. EXACTLY ONE key-policy write landed, measured twice: a live get-key-policy between the two safe-apply invocations read 5 statements with the new Sid absent (the first invocation was truncated by a head pipe and wrote nothing), and CloudTrail lookup-events for PutKeyPolicy from 16:30:00Z returned a denominator of 1 event, at 16:44:04Z, carrying 6 statements, errorCode census {none: 1}. Gates: APPLY-WHO ADMITTED (the CTO half names this seat executor); CROSSBOX-DEPLOY STOP in WARN mode on the same token match plus this entry's own open row; naming-apply-gate listed 26 expression-computed LGIC names as unresolved-before-plan and refused nothing. | CLOSED 20261009T165323Z |
| AFTER | verify | the live transcripts key policy | six Sids read back, GatewayWritesTranscripts carrying both conditions (kms:ViaService s3.us-east-1 and kms:EncryptionContext:aws:s3:arn = the bucket), no kms:Decrypt granted; AC1's invocation run as the order states it | Live key policy reads SIX Sids: RootAdministersTheKeyAndCannotUseIt, NamedReadersUseTheKey, DellAgentUsersDecryptOnly, SilverReaderDecryptOnly, DellAgentUsersGenerateDataKey, GatewayWritesTranscripts. Measured before vs after: statements 5 to 6, ADDED GatewayWritesTranscripts, REMOVED none, 0 of 35 before leaf-values gone after, shared-statement drift 0 of 5 -- the five statements the COO half names by hand are each semantically identical. The new statement carries BOTH conditions: kms:ViaService = s3.us-east-1.amazonaws.com and kms:EncryptionContext:aws:s3:arn = arn:aws:s3:::opal-data-transcripts. Actions are kms:GenerateDataKey and kms:Encrypt only -- kms:Decrypt is ABSENT, checked by matching the action list, so the gateway cannot read a transcript. Live matches the plan's after-document exactly (order-insensitive, KMS scalar/list normalised): True. AC1 run as the order states it, resolving the key through the bucket's own encryption configuration rather than a typed key id: True. Targeted re-plan -detailed-exitcode rc=0, 'No changes. Your infrastructure matches the configuration.' Rollback is one put-key-policy of the before-image recorded verbatim in the ledger's step 0. No transcripts-v* tag taken: that is cell TR-g-21, the issuer's, after the drain, and git tag -l reads 0. | CLOSED 20261009T165323Z |

## Log

- 20261009T163257Z OPENED by 0.7.0_AE_CloudOps~TRL with 3 leg(s)
- 20261009T163601Z LEG PRECHECK closed: CASE: NO S3 WRITE GRANT. Role resolved the way main.tf does it (data.terraform_remote_state.opal_gateway.outputs.instanc
- 20261009T165323Z LEG APPLY closed: safe-apply SUCCESS from the SAVED plan ka21.tfplan at pin 95a62b9f29fdff643344667b82e5364203e3c002 (carries b74b1e45bd; 
- 20261009T165323Z LEG AFTER closed: Live key policy reads SIX Sids: RootAdministersTheKeyAndCannotUseIt, NamedReadersUseTheKey, DellAgentUsersDecryptOnly, S
- 20261009T165325Z CLOSED -- all 3 legs proven

## Step 0 -- the pin, the branch decider, and the LIVE key policy before the apply

Apply pin `95a62b9f29fdff643344667b82e5364203e3c002` on `box/laptop`. `b74b1e45bd` (TO-TR-k21's drain) is an ancestor: YES. Negative control, the reverse direction (`HEAD` in `b74b1e45bd`): NO. The order's amendment pin `c9d94e9dff` and both pair halves (`6791d6ebc2`, `ad98587dfa`) are ancestors too, as is the box pass `0b2018ac25`. Applying identity: `arn:aws:iam::313476888478:user/Andrew_Berman`.

### The CTO half's condition 3: the Bucket Key read, made by the APPLIER

One `get-bucket-encryption` on `opal-data-transcripts`:

```json
{
  "SSEAlgorithm": "aws:kms",
  "KMSMasterKeyID": "arn:aws:kms:us-east-1:313476888478:key/44a2284f-1e14-4ea1-b6cb-f6121bfde35a",
  "BucketKeyEnabled": true,
  "BlockedEncryptionTypes": {
    "EncryptionType": [
      "SSE-C"
    ]
  }
}
```

**`BucketKeyEnabled` is TRUE, so BRANCH 2 of the CTO half governs.** The encryption context S3 sends is the BUCKET ARN, so the key statement cannot be narrowed to a prefix, and the prefix boundary has to live in the gateway role's own S3 grant. That is what the half makes conditional on step 1, and it is why step 1 runs before the apply rather than after. (The issuer read the same value at ~15:5xZ; this is the applier's own read, as condition 3 requires.)

### Live key policy Sids, names only -- 5 of 5 statements

- `RootAdministersTheKeyAndCannotUseIt`
- `NamedReadersUseTheKey`
- `DellAgentUsersDecryptOnly`
- `SilverReaderDecryptOnly`
- `DellAgentUsersGenerateDataKey`

Five live, six expected after this act. `GatewayWritesTranscripts` is ABSENT.

#### Before-image -- the rollback source, verbatim

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RootAdministersTheKeyAndCannotUseIt",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::313476888478:root"
      },
      "Action": [
        "kms:Create*",
        "kms:Describe*",
        "kms:Enable*",
        "kms:List*",
        "kms:Put*",
        "kms:Update*",
        "kms:Revoke*",
        "kms:Disable*",
        "kms:Get*",
        "kms:Delete*",
        "kms:TagResource",
        "kms:UntagResource",
        "kms:ScheduleKeyDeletion",
        "kms:CancelKeyDeletion"
      ],
      "Resource": "*"
    },
    {
      "Sid": "NamedReadersUseTheKey",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::313476888478:role/teams-global-transcripts-second-reader-role",
          "arn:aws:iam::313476888478:user/Andrew_Berman"
        ]
      },
      "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DellAgentUsersDecryptOnly",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::313476888478:user/cloudops-dell1-agent-user",
          "arn:aws:iam::313476888478:user/cloudops-dell2-agent-user"
        ]
      },
      "Action": [
        "kms:Decrypt",
        "kms:DescribeKey"
      ],
      "Resource": "*"
    },
    {
      "Sid": "SilverReaderDecryptOnly",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::313476888478:role/teams-global-transcripts-silver-reader-role"
      },
      "Action": [
        "kms:Decrypt",
        "kms:DescribeKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "s3.us-east-1.amazonaws.com"
        }
      }
    },
    {
      "Sid": "DellAgentUsersGenerateDataKey",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::313476888478:user/cloudops-dell1-agent-user",
          "arn:aws:iam::313476888478:user/cloudops-dell2-agent-user"
        ]
      },
      "Action": "kms:GenerateDataKey",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "s3.us-east-1.amazonaws.com",
          "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::opal-data-transcripts"
        }
      }
    }
  ]
}
```

## Step 1 -- PRECONDITION: the gateway role's S3 write reach. CASE: NO WRITE GRANT

The role was resolved the way `main.tf` does it and NOT typed: `data.terraform_remote_state.opal_gateway.outputs.instance_role_name`, read from `s3://opal-313476888478-terraform-state/opal-gateway/tfstate` -> **`opal-gateway-role`** (`arn:aws:iam::313476888478:role/opal-gateway-role`, confirmed live by `iam get-role`).

**Method, because the answer here is a NEGATIVE and a negative needs a denominator.** Every policy attached to the role was enumerated and decoded -- 1 managed plus 21 inline, **22 documents, 29 statements**. The verdict is reached by SUBTRACTION over those 29, not by searching the documents for the string `opal-data-transcripts`: a statement granting `s3:PutObject` on `arn:aws:s3:::*/*` reaches this bucket without ever naming it. So each statement's actions were pattern-matched against a list of 20 S3 WRITE actions, and its resources pattern-matched against five probe ARNs -- the permitted market_update object, a Teams silver transcript, a Teams bronze transcript, an outlook silver transcript, and the bucket itself.

**VERDICT: 0 Allow statements grant an S3 write that reaches `opal-data-transcripts`, and 0 Deny statements reach it either.** 11 of the 29 statements name an S3 action at all; none of those 11 touches this bucket. The role's only S3 write anywhere is `opal-gateway-audit-lake-write` / `AuditLakePutOnly`, `s3:PutObject` on `arn:aws:s3:::opal-mcp-audit/audit/*` -- a different bucket.

So the case that held is the order's explicitly permitted one: *"NO grant yet is also a pass: the key statement alone writes nothing."* This act grants the ability to ENCRYPT under the key; it grants no path to put bytes in the bucket. Site Z's OG-ab-2 pair owns that S3 grant, and when it lands it must be `s3:PutObject` on `sharepoint/transcripts/bronze/market_update/*` alone -- the CTO half's branch-2 condition, which this reading does not and cannot discharge in advance.

**CONTROL -- the matcher was proven to fire before its zero was believed.** Five planted statements (not live policy) were run through the same matcher:

| planted statement | result |
|---|---|
| `s3:PutObject` on `arn:aws:s3:::*/*` | **WOULD BE FLAGGED** (1 write action, 4 probes matched) |
| `s3:*` on `*` | **WOULD BE FLAGGED** (20 write actions, 5 probes matched) |
| `s3:PutObject` on the permitted market_update prefix | **WOULD BE FLAGGED** (1 write, 1 probe) |
| `s3:PutObject` on `arn:aws:s3:::opal-data-bd/*` | not flagged (another bucket) |
| `s3:GetObject` on this bucket | not flagged (4 probes, but no write action) |

The two wildcard shapes are the ones that would have made this zero a lie, and both are caught. A zero from a matcher that cannot fire reads identically to a true absence; this one can fire.

### The census, verbatim

```
POLICY DENOMINATOR: 22 document(s) -- 1 managed, 21 inline
STATEMENT DENOMINATOR: 29 statement(s) across those documents
S3-touching (or '*' action) statements: 11 -- the other 18 name no S3 action at all

=== every S3-touching statement, and what it reaches in opal-data-transcripts ===
  [inline/gateway-firm-deny-policy] Sid=DenyFirmSegments Effect=Deny
      actions:   ['s3:GetObject']
      resources: ['arn:aws:s3:::opal-data-portal-v2/platinum/mdpf/49financial/*', 'arn:aws:s3:::opal-data-portal-v2/platinum/mdpf/inflection/*', 'arn:aws:s3:::opal-data-portal-v2/platinum/mdpf/cottonwood/*']
      S3 WRITE actions it covers: none
      probe targets in this bucket it matches: none
  [inline/gateway-mcportal-close-request-write-policy] Sid=McportalCloseRequestWriteOnly Effect=Allow
      actions:   ['s3:PutObject']
      resources: ['arn:aws:s3:::opal-313476888478-globgrph/fabric/open-calls/v1/box=*/requests/*']
      S3 WRITE actions it covers: s3:PutObject
      probe targets in this bucket it matches: none
  [inline/gateway-mcportal-fabric-read-policy] Sid=McportalFabricPrefixReadOnly Effect=Allow
      actions:   ['s3:GetObject']
      resources: ['arn:aws:s3:::opal-313476888478-globgrph/fabric/activity/v1/*', 'arn:aws:s3:::opal-313476888478-globgrph/fabric/open-calls/v1/*']
      S3 WRITE actions it covers: none
      probe targets in this bucket it matches: none
  [inline/gateway-mcportal-fabric-read-policy] Sid=McportalFabricPrefixListOnly Effect=Allow
      actions:   ['s3:ListBucket']
      resources: ['arn:aws:s3:::opal-313476888478-globgrph']
      S3 WRITE actions it covers: none
      probe targets in this bucket it matches: none
      condition: {"StringLike": {"s3:prefix": ["fabric/activity/v1/*", "fabric/open-calls/v1/*", "fabric/activity/v1/", "fabric/open-calls/v1/"]}}
  [inline/gateway-rivalfunds-read-policy] Sid=RivalfundsPageGet Effect=Allow
      actions:   ['s3:GetObject']
      resources: ['arn:aws:s3:::opal-data-etfs/rivalfunds/etfs/platinum/page/*']
      S3 WRITE actions it covers: none
      probe targets in this bucket it matches: none
  [inline/gateway-rivalfunds-read-policy] Sid=RivalfundsPageListPrefix Effect=Allow
      actions:   ['s3:ListBucket']
      resources: ['arn:aws:s3:::opal-data-etfs']
      S3 WRITE actions it covers: none
      probe targets in this bucket it matches: none
      condition: {"StringLike": {"s3:prefix": ["rivalfunds/etfs/platinum/page/", "rivalfunds/etfs/platinum/page/*"]}}
  [inline/opal-gateway-audit-lake-write] Sid=AuditLakePutOnly Effect=Allow
      actions:   ['s3:PutObject']
      resources: ['arn:aws:s3:::opal-mcp-audit/audit/*']
      S3 WRITE actions it covers: s3:PutObject
      probe targets in this bucket it matches: none
  [inline/opal-gateway-daily-reports-read] Sid=DailyReportsGet Effect=Allow
      actions:   ['s3:GetObject']
      resources: ['arn:aws:s3:::opal-data-portal-v2/daily-reports/*']
      S3 WRITE actions it covers: none
      probe targets in this bucket it matches: none
  [inline/opal-gateway-daily-reports-read] Sid=DailyReportsListPrefix Effect=Allow
      actions:   ['s3:ListBucket']
      resources: ['arn:aws:s3:::opal-data-portal-v2']
      S3 WRITE actions it covers: none
      probe targets in this bucket it matches: none
      condition: {"StringLike": {"s3:prefix": ["daily-reports/", "daily-reports/*"]}}
  [inline/opal-gateway-golive] Sid=ArtifactPull Effect=Allow
      actions:   ['s3:GetObject']
      resources: ['arn:aws:s3:::opal-313476888478-lambda-artifacts/ec2/opal-gateway/*']
      S3 WRITE actions it covers: none
      probe targets in this bucket it matches: none
  [inline/opal-gateway-queryv0-portal-read] Sid=QueryV0PortalCatalogRead Effect=Allow
      actions:   ['s3:GetObject']
      resources: ['arn:aws:s3:::opal-data-portal-v2/json/*', 'arn:aws:s3:::opal-data-portal-v2/platinum/*']
      S3 WRITE actions it covers: none
      probe targets in this bucket it matches: none

=== VERDICT -- step 1 of the order ===
Allow statements granting an S3 WRITE that reaches opal-data-transcripts: 0
Deny statements reaching opal-data-transcripts: 0

CASE HELD: **NO S3 WRITE GRANT** on opal-data-transcripts anywhere in this role, established by SUBTRACTION from 29 statements across 22 documents -- not by searching for the bucket's name. No statement with an S3 write action matches any probe ARN in the bucket, including the wildcard check.
The order's step 1 names this a PASS: 'NO grant yet is also a pass: the key statement alone writes nothing.'

=== CONTROL: does the matcher actually fire? planted statements, not live policy ===
  s3:PutObject on arn:aws:s3:::*/*           -> WOULD BE FLAGGED  (writes=1, reaches=4)
  s3:* on * (admin shape)                    -> WOULD BE FLAGGED  (writes=20, reaches=5)
  PutObject on the permitted prefix only     -> WOULD BE FLAGGED  (writes=1, reaches=1)
  PutObject on another bucket                -> not flagged  (writes=1, reaches=0)
  GetObject only on this bucket              -> not flagged  (writes=0, reaches=4)
```

## Step 2a -- the PLAN, graded before the apply

```
terraform -chdir=infra/aws/terraform/transcripts plan -input=false \
  -var 'second_reader_trust_principal_arns=["arn:aws:iam::313476888478:user/Opal_Terminal"]' \
  -target=aws_kms_key.transcripts -out=ka21.tfplan
```

(The `-var` is passed because `second_reader_trust_principal_arns` has no default and terraform refuses any plan without it. Its value is the one a18 applied -- `aws_iam_role.second_reader` plans as a no-op below, which is what proves the value matches live rather than changing it.)

**Plan line: `0 to add, 1 to change, 0 to destroy.`**

Graded from `terraform show -json`: **1 non-no-op over a denominator of 4 resource_changes**.

- `aws_kms_key.transcripts` -- **update**

No-op in the same plan: `aws_iam_role.second_reader`, `aws_iam_role.silver_reader`, `aws_s3_bucket.transcripts`. The four Lambda files in this root produce zero resource_changes.

### The key-policy diff, KNOWN at plan time

The only changed attribute of `aws_kms_key.transcripts` is `policy`, and **no attribute is `after_unknown`** -- unlike s21, where the new statement's principal was a role created in the same plan. Here the principal comes from `data.aws_iam_role.gateway`, resolved through the opal-gateway root's remote state, so terraform renders the whole after-document and **the plan itself is the oracle for the pair's condition**. No prediction is needed.

- Statements **5 -> 6**. ADDED Sids: **`GatewayWritesTranscripts`**. REMOVED Sids: ****none****.

| the five live Sids | identical in the plan's after-document |
|---|---|
| `RootAdministersTheKeyAndCannotUseIt` | True |
| `NamedReadersUseTheKey` | True |
| `DellAgentUsersDecryptOnly` | True |
| `SilverReaderDecryptOnly` | True |
| `DellAgentUsersGenerateDataKey` | True |

**Shared-statement drift: 0 of 5.** The COO half names those five explicitly and all five are byte-identical, so `s21`'s, `a18`'s and both Dell statements hold.

The added statement, from the plan:

```json
{
  "Action": [
    "kms:GenerateDataKey",
    "kms:Encrypt"
  ],
  "Condition": {
    "StringEquals": {
      "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::opal-data-transcripts",
      "kms:ViaService": "s3.us-east-1.amazonaws.com"
    }
  },
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::313476888478:role/opal-gateway-role"
  },
  "Resource": "*",
  "Sid": "GatewayWritesTranscripts"
}
```

- Actions: `kms:GenerateDataKey`, `kms:Encrypt`. **`kms:Decrypt` is NOT granted** -- checked by matching the action list, not by eye. The gateway can encrypt what it writes and cannot read a transcript.
- Principal `arn:aws:iam::313476888478:role/opal-gateway-role`, resolved from the gateway root's own `instance_role_name` output. No ARN is typed anywhere in the configuration.
- Both conditions present: `kms:ViaService` = `s3.us-east-1.amazonaws.com`, and `kms:EncryptionContext:aws:s3:arn` = `arn:aws:s3:::opal-data-transcripts`. Under Bucket Keys that context IS the bucket, so this is the narrowest the key can be made; the prefix boundary stays with site Z's S3 grant, which step 1 found does not exist yet.

### Both branches

- **Applied as planned:** the gateway role gains the ability to encrypt under this key via S3 to this bucket, and nothing else. It still has no way to PUT bytes into the bucket (step 1), and no way to read one. No other principal changes.
- **Plan differs:** STOP before the apply; nothing changes. The plan above was graded and did not differ.

## Step 2b -- the APPLY, and what landed, measured

```
.tools/safe-apply.sh -chdir=infra/aws/terraform/transcripts apply -input=false \
  -lock-timeout=120s ka21.tfplan
  -> aws_kms_key.transcripts: Modifications complete after 5s
  -> Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
```

### ONE write, not two -- stated because the first invocation was truncated

safe-apply was invoked TWICE. The first invocation's output was piped into `head -30`, which closed the pipe early; it is NOT established from that output whether the apply ran. It did not, and the claim is measured twice over rather than assumed:
1. A live `get-key-policy` read BETWEEN the two invocations returned **5** statements with `GatewayWritesTranscripts` absent.
2. CloudTrail `lookup-events` for `EventName=PutKeyPolicy` from 16:30:00Z returned a **denominator of 1 event**, and that one event is **16:44:04Z**, the second invocation, carrying 6 statements. Zero other events, successful or failed, in the window; the errorCode census over all 1 returned is `{none: 1}`.

So the key policy was written **exactly once** by this act. (The 4 `MalformedPolicyDocumentException` retries that preceded the s21 and a18 applies do not appear here, which fits their explanation: there is no just-created principal for IAM to propagate, because the gateway role already existed.)

### Gates the wrapper printed

- `APPLY-WHO serial=0.7.0_AE_CloudOps~TRL kind=CLOUDOPS root=transcripts verdict=ADMITTED` -- and the CTO half's condition 2 names this seat as the executor.
- `CROSSBOX-DEPLOY ... open_call=hit open_deploy=hit verdict=STOP`, mode **WARN**. 3 hits, same classes as the s21 apply: the OPEN-CALL is `XB-20261009T093642Z-9ec5`, an ORDER to dell1's `~CT1` about NFRA_CTLPLN rows that matches only on a token inside its body document, and the OPEN-DEPLOY hits are a18's held entry and this entry's own open row.
- `naming-apply-gate` listed 26 names it could not resolve before the plan, every one of the form `name = local.<x>` or `name = <resource>.id`. That is the gate reporting that an LGIC name computed in an expression has no value until a plan exists -- it is the CONFORMANT shape this root uses deliberately (rule 30: names come from the builders, never typed), and the gate refused nothing.

## Step 3 -- the after-read

### Sids, names only -- **6**, the six expected

- `RootAdministersTheKeyAndCannotUseIt`
- `NamedReadersUseTheKey`
- `DellAgentUsersDecryptOnly`
- `SilverReaderDecryptOnly`
- `DellAgentUsersGenerateDataKey`
- `GatewayWritesTranscripts`  <- added by this act

### The diff, measured BEFORE vs AFTER on the live key

- Statements **5 -> 6**. ADDED: **`GatewayWritesTranscripts`**. REMOVED: ****none****.
- Leaf-value subtraction over the whole document: **0** values present before are gone after (denominator 35 before / 37 after).
- **Shared-statement drift: 0 of 5.** The five statements the COO half names by hand are each semantically identical across the edit:

| Sid | identical |
|---|---|
| `RootAdministersTheKeyAndCannotUseIt` | True |
| `NamedReadersUseTheKey` | True |
| `DellAgentUsersDecryptOnly` | True |
| `SilverReaderDecryptOnly` | True |
| `DellAgentUsersGenerateDataKey` | True |

(Comparison is order-insensitive on principal arrays, because KMS's renderer reorders them between reads -- the s21 ledger records that finding. The comparator was proven to catch a real one-value change there with a planted mutant.)

### `GatewayWritesTranscripts`, verbatim from the live key policy

```json
{
  "Sid": "GatewayWritesTranscripts",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::313476888478:role/opal-gateway-role"
  },
  "Action": [
    "kms:GenerateDataKey",
    "kms:Encrypt"
  ],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::opal-data-transcripts",
      "kms:ViaService": "s3.us-east-1.amazonaws.com"
    }
  }
}
```

**Its two conditions** (the order's step 3):

- `kms:EncryptionContext:aws:s3:arn` = `arn:aws:s3:::opal-data-transcripts`
- `kms:ViaService` = `s3.us-east-1.amazonaws.com`

**No decrypt:** the action list is `kms:GenerateDataKey`, `kms:Encrypt` -- `kms:Decrypt` is absent, checked by matching the list rather than by eye. The gateway can encrypt what it writes under this key and cannot read a transcript.

**Live matches the plan's after-document exactly** (order-insensitive, KMS scalar/list normalised): True. The plan was the oracle here, and the world agrees with it.

### AC1, the order's own invocation

```
python -c "...get_bucket_encryption -> KMSMasterKeyID -> get_key_policy -> 'GatewayWritesTranscripts' in [Sid...]"
  -> True
```

That invocation resolves the key through the BUCKET's encryption configuration rather than from a typed key id, so it also re-proves that the statement landed on the key the bucket actually encrypts with.

### Rollback

`kms put-key-policy` with the step-0 before-image restores the five-statement policy. That is an update, not a delete, and the before-image is recorded above verbatim.

### Not done, deliberately

No `transcripts-v*` tag: the first tag on this root is cell `TR-g-21`, the ISSUER's after the drain, and `git tag -l "transcripts-v*"` still reads 0. No role, bucket policy or other root touched -- the plan's denominator shows the only non-no-op was the key.

## Addendum to step 1 -- the DESIRED plane, because a LIVE zero does not cover it

Step 1's census read the LIVE attached policies, which is what governs access today and what the order asks for. It does NOT answer a second question the CTO half's branch 2 makes relevant: is a wider write grant already WRITTEN IN TERRAFORM, waiting for an apply? That is the declared-but-unapplied class, and a live-only zero is silent on it. So the DESIRED plane was read too.

`comp-iam role opal-gateway-role` resolves the role from `infra/aws/terraform/opal-gateway/main.tf` and reports **25 statements**, against the **29 across 22 documents** the live census found. The two planes have different denominators and that is expected -- the live set includes the attached managed policy (`AmazonSSMManagedInstanceCore`) and policies declared outside that one file -- so neither count is quoted as the other's.

Two S3 `PutObject` statements appear in the DESIRED plane, and both were resolved rather than read as opaque interpolations:

1. `s3:PutObject` on `arn:aws:s3:::${local.advi_billing_bucket}/${local.advi_billing_key_prefix}*`. Resolved in `infra/aws/terraform/opal-gateway/advi_billing_gateway_iam.tf:36,38`: the bucket is `local.advi_billing_tiers.homes.FIRM.bronze.bucket` and the prefix is `smartx/${local.advi_billing_scope}/bronze/fee_statement/`. A SmartX fee-statement bronze home -- a different bucket and a different prefix.
2. `s3:PutObject` on `${aws_s3_bucket.audit.arn}/audit/*` -- the audit lake, which is the live `AuditLakePutOnly` statement on `opal-mcp-audit`.

And the direct question, with its denominator: `comp-find 'opal-data-transcripts'` over `infra/aws/terraform/opal-gateway` returns **0 hits across 40 files scanned**. The gateway root does not name the transcripts bucket anywhere. **CAVEAT, stated rather than swallowed: 4 in-scope files in that root are BINARY and were not searched, so that zero does not cover them.**

So both planes agree: the gateway role has no write path into `opal-data-transcripts` today, and none is pending an apply from its own root. Site Z's OG-ab-2 pair still owns minting that grant, and the CTO half's branch-2 condition -- `s3:PutObject` on `sharepoint/transcripts/bronze/market_update/*` ALONE, no Delete, no other prefix -- binds it when it lands. **This act does not and cannot discharge that condition in advance**; it grants encryption under the key and nothing more.
