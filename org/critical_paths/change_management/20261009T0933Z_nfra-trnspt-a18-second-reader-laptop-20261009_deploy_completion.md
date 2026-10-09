# Deploy Completion Record
**Date opened:** 2026-10-09T09:33:18.594111+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / Opal_Terminal real GetObject ADMITTED plus dell2 irpt-ycharts-runner-role real GetObject REFUSED, status-only (held since 2026-10-09T10:02:46.804410+00:00)
**Deploy:** NFRA_TRNSPT a18 second named reader apply from integrated pin f7a4fb5d04efb908b96ab3b8d86277c9b9f982ad carrying f8c4859407, 04313a7e39, dc5032abde
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| APPLY | activation | Terraform targets aws_iam_role.second_reader, aws_iam_policy.second_reader, aws_iam_role_policy_attachment.second_reader, aws_kms_key.transcripts | safe-apply receipt and exact 3 create plus 1 update result | safe-apply SUCCESS 2026-10-09T09:55Z: 3 added, 1 changed, 0 destroyed; pin f7a4fb5d04; plan gate commit 5d27fc36a7; tag override audit id 20261009T095303Z-3890779 after direct comp-tagauthz rc=0 and tombstone rc=0 | CLOSED 20261009T100241Z |
| VERIFY | verify | Named reader role, key-policy one-principal delta, admitted/refused S3 proof | role readback, full key-policy diff, ADMITTED and REFUSED statuses only |  | OPEN |

## Log

- 20261009T093318Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)
- 20261009T100241Z LEG APPLY closed: safe-apply SUCCESS 2026-10-09T09:55Z: 3 added, 1 changed, 0 destroyed; pin f7a4fb5d04; plan gate commit 5d27fc36a7; tag 
- 20261009T100246Z HELD-SOVEREIGN-GATED gate=external/Opal_Terminal real GetObject ADMITTED plus dell2 irpt-ycharts-runner-role real G

---

# VERIFY leg -- worked by `0.7.0_AE_CloudOps~TRL` on the laptop, 2026-10-09 ~14:2xZ

GO from `2.0.0_SA_COO~C` msg 107993, verbatim from the issuer dell2 `2.0.0_SA_COO~T2` msg 3438 (relay `0.0.0_AB_MSTR` msg 107991), relocation amendment @a7bd828882: *only* the open VERIFY leg -- role read-back, key-policy diff, the admitted/refused proof with statuses only -- then close this ledger. Apply nothing new. **Nothing was applied by this pass.**

## 1. Role read-back -- DONE

```
aws iam get-role --role-name teams-global-transcripts-second-reader-role
  RoleName   teams-global-transcripts-second-reader-role
  Arn        arn:aws:iam::313476888478:role/teams-global-transcripts-second-reader-role
  CreateDate 2026-10-09T09:55:13Z
aws iam list-attached-role-policies --role-name teams-global-transcripts-second-reader-role
  teams-global-transcripts-second-reader-policy
aws iam get-role --query Role.AssumeRolePolicyDocument
  Allow sts:AssumeRole to arn:aws:iam::313476888478:user/Opal_Terminal -- ONE principal, as the CTO half named it
```

The role's `CreateDate` 09:55:13Z sits between the APPLY leg's safe-apply window and its `PutKeyPolicy` at 09:55:22Z, so the create and the key edit are the same act.

## 2. Key-policy diff -- DONE, and measured from CloudTrail rather than from the applier's report

The APPLY leg's proof line was a safe-apply receipt, which is the producer's self-report. The diff here is taken instead from the REQUEST DOCUMENTS CloudTrail recorded for `PutKeyPolicy` on key `44a2284f-1e14-4ea1-b6cb-f6121bfde35a` -- the bytes AWS was actually asked to store. `lookup-events` returned **11** events for `EventName=PutKeyPolicy` over 2026-10-09 (denominator printed); **3** of them carry a `keyId` and no `errorCode`:

| eventTime | actor | statements | what it was |
|---|---|---|---|
| 2026-10-09T05:40:10Z | user/Andrew_Berman | 4 | the pre-a18 state (the `DellAgentUsersGenerateDataKey` apply, CT-a-1 AMENDMENT 28) |
| 2026-10-09T09:55:22Z | user/Andrew_Berman | 4 | **a18, this ledger's APPLY leg** |
| 2026-10-09T14:07:33Z | user/Andrew_Berman | 5 | s21, the silver-only reader (a separate ledger, closed) |

The other 8 events are `MalformedPolicyDocumentException`, 4 in the seconds before each successful put (09:55:14-09:55:17Z and 14:07:25-14:07:29Z). That is the AWS provider retrying while a just-created role ARN is not yet resolvable to IAM -- the same shape at both applies, hence provider retry behaviour and not a defect in either act. Named here rather than left as an unexplained 8.

### The a18 diff: 2026-10-09T05:40:10Z -> 2026-10-09T09:55:22Z

- Statements **4 -> 4**. ADDED Sids: **none**. REMOVED Sids: **none**.

| Sid | identical | the only delta |
|---|---|---|
| `RootAdministersTheKeyAndCannotUseIt` | True | none |
| `NamedReadersUseTheKey` | False | principals ADDED ['arn:aws:iam::313476888478:role/teams-global-transcripts-second-reader-role'], REMOVED none |
| `DellAgentUsersDecryptOnly` | True | none |
| `DellAgentUsersGenerateDataKey` | True | none |

**CONDITION 1 OF THE CTO HALF IS SATISFIED: exactly ONE principal differs** -- `arn:aws:iam::313476888478:role/teams-global-transcripts-second-reader-role` added to `NamedReadersUseTheKey`. No statement was added or removed, no action changed, no condition changed, and `DellAgentUsersGenerateDataKey` (applied 05:40:10Z) is byte-identical across the a18 edit.

Full `NamedReadersUseTheKey` after a18, verbatim from the CloudTrail request:

```json
{
  "Action": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:ReEncrypt*",
    "kms:GenerateDataKey*",
    "kms:DescribeKey"
  ],
  "Effect": "Allow",
  "Principal": {
    "AWS": [
      "arn:aws:iam::313476888478:user/Andrew_Berman",
      "arn:aws:iam::313476888478:role/teams-global-transcripts-second-reader-role"
    ]
  },
  "Resource": "*",
  "Sid": "NamedReadersUseTheKey"
}
```

For completeness, the s21 edit that followed (its own closed ledger) read ADDED `SilverReaderDecryptOnly`, REMOVED none, and all four pre-existing statements identical on the same instrument -- an independent corroboration of that ledger's live before/after read, and one immune to the `Principal.AWS` array reordering that KMS's own renderer introduces.

## 3. The ADMITTED / REFUSED proof -- NOT EXERCISED, and not exercisable from this device

The CTO half's condition 2 wants a REAL `GetObject`: *"An unnamed principal (one of dell2's service roles not on the list) tries a GetObject on one bronze object and is REFUSED, and the named role succeeds."* Both arms were attempted from the laptop and both are structurally out of reach HERE. Measured, not assumed:

**ADMITTED arm** -- the named role, assumed from `Opal_Terminal`:

```
aws sts assume-role --role-arn arn:aws:iam::313476888478:role/teams-global-transcripts-second-reader-role
  AccessDenied: User arn:aws:iam::313476888478:user/Andrew_Berman is not authorized to perform
  sts:AssumeRole on resource arn:aws:iam::313476888478:role/teams-global-transcripts-second-reader-role
```

That is correct behaviour, not a fault: the trust document admits `Opal_Terminal` and nobody else, which is what the CTO half named. This device holds exactly one AWS profile (`[default]` = `user/Andrew_Berman`) and no `Opal_Terminal` credential. `Opal_Terminal` is the Bloomberg terminal seat's identity (its own tags: `purpose=bloomberg-terminal-device`), so the read belongs to SITE Z.

**REFUSED arm** -- an unnamed dell2 service role:

```
aws iam get-role --role-name irpt-ycharts-runner-role --query Role.AssumeRolePolicyDocument
  Allow sts:AssumeRole to Principal {"Service": "ec2.amazonaws.com"}
```

The role this ledger's own gate names is trusted by the EC2 SERVICE only -- no IAM user can assume it from anywhere. The read has to run ON a dell2 EC2 host under that instance profile. The same is true of dell2's other service roles by construction.

No new principal was minted to manufacture either arm: the GO says apply nothing new, and a role created to pass its own test is not evidence.

### Why a `simulate-principal-policy` substitute was NOT recorded as the proof

A simulate is the obvious fallback and it is the WRONG instrument here -- not merely weaker, but anti-correlated with the property under test. Measured, one `--resource-arns` per call, each in its own invocation:

```
iam list-groups-for-user --user-name Opal_Terminal      -> AdministratorAccessOpalCapital
iam list-attached-group-policies --group-name ...       -> AdministratorAccess
simulate s3:GetObject  Opal_Terminal on one bronze obj  -> allowed
simulate kms:Decrypt   Opal_Terminal on the transcripts key -> allowed
```

`main.tf`'s own design note says why that second `allowed` is false against the key's real behaviour: *"The key policy gives the account root ADMINISTRATION only. It does not give root the use actions, so an IAM policy elsewhere in the account holding kms:Decrypt on '*' does NOT reach this key."* `simulate-principal-policy` evaluates the PRINCIPAL'S IAM policies; it does not evaluate the KMS key policy. `Opal_Terminal` carries `AdministratorAccess`, so the simulate reads `allowed` on both actions **and would have read exactly the same BEFORE a18 landed at 09:55Z**, when the real read was denied by the key. It is blind to the one line a18 added.

The CTO half saw this coming and said so: *"Opal_Terminal already holds AdministratorAccessOpalCapital through its group. The new role therefore adds no reach that identity lacks in IAM; what it adds is the key-policy line ... which is why the refusal proof below is the test."* Quoting the simulate as ADMITTED would be a false pass of precisely the class the refusal proof exists to catch, so it is recorded here as an instrument finding and NOT as leg evidence.

## Disposition of this leg

- **Condition 1 (full key-policy diff, one principal only): SATISFIED**, on a stronger instrument than the leg asked for.
- **Condition 3 (no transcript content anywhere): HELD** -- this pass read no object at all.
- **Condition 2 (the admitted/refused real reads): NOT EXERCISED.** ABSENT is not EXERCISED-AGAINST: nothing here says either read would fail. Two owners, one read each:
  - `Opal_Terminal` assumes the role and GETs one transcripts object -> expect ADMITTED. Owner: the site-Z terminal seat, via `0.0.0_AB_MSTR`.
  - an unnamed dell2 service role GETs the same key from a dell2 EC2 host -> expect REFUSED. Owner: the dell2 seat, via `2.0.0_SA_COO~T2`.

**The VERIFY leg is therefore LEFT OPEN and this ledger is NOT closed.** The GO said to close it; the reason it is not closed is the measured fact above, which the issuer could not have known when the GO was written, and the ledger's own `gate.reread` already names the same two probes (*"MSTR delivers both NFRA_TRNSPT a18 status-only probe results"*). Closing this leg on the simulate would turn a HELD-ON-REAL-READS entry into a CLOSED one on a blind oracle -- the false-clean class `deploy_ledger.py check` exists to sweep for. ONE decision is owed by `2.0.0_SA_COO~T2`, carried in the report: close VERIFY on the key-policy diff above plus the trust documents, or hold it for the two real probes.

-- `0.7.0_AE_CloudOps~TRL`
