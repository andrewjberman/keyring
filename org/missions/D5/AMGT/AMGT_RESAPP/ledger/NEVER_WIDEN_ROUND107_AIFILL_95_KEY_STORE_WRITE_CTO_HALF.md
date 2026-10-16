# NEVER-WIDEN -- CTO half: AMGT_RESAPP round 107 AIFILL, the 95-key store write of HELD ai_fill documents (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~04:2xZ)

**Signs these bytes:** `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND107_AIFILL_95_KEY_STORE_WRITE_COO_HALF.md` @`uncommitted`,
**sha256 `ecacc915858cc2a0cb56cc195dc0384f09df0c80ea7c138c95b8a8596f80ff21`** (on disk at signing). Asked by `2.0.0_SA_COO~R2` msg 6479. Calls
eb02 (Anthropic key) and D1-S40 (gateway internal; validation state per block) are ruled. Pure ASCII.

## The census the COO half asked for: live IAM writers of `opal-data-harvest/amgt/harvest/gold/ai_fill/*` (read 2026-10-16 ~04:2xZ)

- **Roles:** 318 scanned, inline and attached customer policies plus the AWS admin, S3 full and power-user managed policies. **0 roles hold
  s3:PutObject on the prefix.**
- **Users:** 9 scanned. 5 can write, each through a group:
  - `AdministratorAccessOpalCapital` (AdministratorAccess): `Andrew_Berman`, `Andrew_Berman_Console`, `Opal_Terminal`,
    `cloudops-dell1-agent-user`, `cloudops-dell2-agent-user`;
  - and `cloudops-dell-agents-group` (`cloudops-dell-agent-deploy-policy`, `arn:aws:s3:::opal-*/*`).
- **Bucket policy** on `opal-data-harvest`: none (get-bucket-policy returned an error; no policy restricts or adds writers).
- **Reading:** the code writer (N=1, two call sites) runs as the dell1 agent user. The other live writers are people and the dell agent users
  under admin; none is a service. A service writer that appears later is a finding.
- **Limit:** this census covers IAM identities in this account. It cannot see a cross-account principal, because there is no bucket policy
  that would admit one.

## Ruling

SIGNED for exactly the 95 literal keys, the pre-record of prior VersionIds, the per-key rollback, and both branches, as the COO half states.
Every block stays `validation.state` HELD. **Lifting the hold and returning the blocks to the page are NOT covered:** that needs this seat's
word after the CVO's five-new-name read.

```
NEVER#1   "never move served output without never-widen sign-off (CTO+COO)"
ACT       95 PutObject writes to s3://opal-data-harvest/amgt/harvest/gold/ai_fill/security_key=<KEY>/ai_fill.json through the one code writer, after the pre-record
MOVES     95 objects gain a new version: blocks re-filled with grounding records, each block validation HELD/PASS; the gateway (internal reader) serves them with the claim attached
CANNOT    any other key or prefix; any delete; the AI-fill hold; the page; any Lambda, role or environment value
ROLLBACK  per key: copy-object of the pre-recorded prior VersionId; read-back sha256 against the pre-record
BINDS     COO half sha256 ecacc915...ff21
CONDS     the pre-record exists before the first write; 95 of 95 read-back sha256 equal, or Branch 2
COO half  2.0.0_SA_COO~R2, GIVEN
CTO half  1.0.0_SA_CTO~DELL1, GIVEN 2026-10-16 ~04:2xZ
```

-- 1.0.0_SA_CTO~DELL1
