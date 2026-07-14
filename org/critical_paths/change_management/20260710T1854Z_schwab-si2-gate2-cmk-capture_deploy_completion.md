# Deploy Completion Record
**Date opened:** 2026-07-10T18:54:42.161677+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260710T193053Z
**Deploy:** ADVI_SCHWABAUTO A-PRIME Gate-2: CMK/secret/iam apply + on-box SDD session capture
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD: capturer 4fbf13563 + TF 5e0467c74 | both hashes on origin/CLOUD | capturer 4fbf13563 + TF 5e0467c74 both pushed to origin/CLOUD | CLOSED 20260710T185840Z |
| L2 | activation | safe-apply CMK+alias+secret+inline-KMS (targeted, HALT-gated) | apply complete + 0-diff re-plan | safe-apply HALTGT-passed: 3 added/1 changed/0 destroyed; 0-diff re-plan 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260710T185841Z |
| L3 | verify | live: CMK enabled+rotation, secret CMK-encrypted, role KMS grant | aws describe outputs | CMK 8863d4ac Enabled/CUSTOMER, rotation=True; secret schwab/sdd/session KmsKeyId=CMK ARN + Versions=null (empty by design); role SchwabSddSessionKms grant present (Decrypt/GenerateDataKey/DescribeKey via secretsmanager, scoped to key ARN) | CLOSED 20260710T185841Z |
| L4 | s3-prefix | capturer -> s3 opal-data-schwab/_ops/canonical-schwab-si2/ | aws s3 cp + head-object | capturer + bootstrap.ps1 on s3://opal-data-schwab/_ops/canonical-schwab-si2/; box bootstrapped (embeddable py3.12.7 + cryptography 49.0.0 + boto3 1.43.45); capturer 17618 bytes on box, deps import OK | CLOSED 20260710T192450Z |
| L5 | activation | on-box console-session capture: --dry-run PASS then --live | SSM task log rc=0 | console-session task (Administrator InteractiveToken): --dry-run rc=0 (located real WebView2 profile, decrypted 8 schwab cookies + access-token JWT, no SM write); --live rc=0 (session blob written). CommandIds 10847d9f (dry) / 92ba9d18 (live) | CLOSED 20260710T193052Z |
| L6 | verify | SM schwab/sdd/session has a well-formed version (jar+token) | describe-secret VersionId | SM schwab/sdd/session version 76c9f5d4-7bbd-48b6-87fc-de6de8f021f7=AWSCURRENT, KmsKeyId=CMK 8863d4ac; blob=8-cookie schwab jar + access token, expires_at 2026-07-17 | CLOSED 20260710T193052Z |

## Log

- 20260710T185442Z OPENED by 0.7.0_AE_CloudOps with 6 leg(s)
- 20260710T185840Z LEG L1 closed: capturer 4fbf13563 + TF 5e0467c74 both pushed to origin/CLOUD
- 20260710T185841Z LEG L2 closed: safe-apply HALTGT-passed: 3 added/1 changed/0 destroyed; 0-diff re-plan 'No changes. Your infrastructure matches the con
- 20260710T185841Z LEG L3 closed: CMK 8863d4ac Enabled/CUSTOMER, rotation=True; secret schwab/sdd/session KmsKeyId=CMK ARN + Versions=null (empty by desig
- 20260710T192450Z LEG L4 closed: capturer + bootstrap.ps1 on s3://opal-data-schwab/_ops/canonical-schwab-si2/; box bootstrapped (embeddable py3.12.7 + cr
- 20260710T193052Z LEG L5 closed: console-session task (Administrator InteractiveToken): --dry-run rc=0 (located real WebView2 profile, decrypted 8 schwab
- 20260710T193052Z LEG L6 closed: SM schwab/sdd/session version 76c9f5d4-7bbd-48b6-87fc-de6de8f021f7=AWSCURRENT, KmsKeyId=CMK 8863d4ac; blob=8-cookie schw
- 20260710T193053Z CLOSED -- all 6 legs proven
