# DEPLOY COMPLETION LEDGER -- the device drift publisher's SCOPED ROLE (NFRA_OUTSET.TO-OS-s-21)

**Opened:** 2026-09-09T16:50Z by `0.7.0_AE_CloudOps~W`
**Status:** OPEN -- the apply has NOT been performed at this write
**TO:** `org/missions/D11/NFRA/NFRA_OUTSET/task-orders/NFRA_OUTSET.TO-OS-s-21.the-cadence-scheduled-publish.md`
AMENDED @`eb2d27b6e4` on the CTO's ruling @`054353ac5e` (row `NFRA_OUTSET-S25`, shape **(d)**)

⛔ **Committed OPEN before the apply**, so "opened first" is a fact in git history rather than a
claim in prose. Closed after the legs verify. Fourth use of this shape today.

## What

Two IAM resources in `infra/aws/terraform/estate-report/iam.tf`, applied with `safe-apply`:

- `aws_iam_role.outset_drift_publisher_laptop` -- name `outset-drift-publisher-laptop`, trust
  limited to `arn:aws:iam::313476888478:user/Andrew_Berman` **by ARN**, with a condition pinning
  `sts:RoleSessionName` to **`outset-drift-laptop`**, and `max_session_duration = 3600` (the AWS
  minimum).
- `aws_iam_role_policy.outset_drift_publisher_laptop` -- **ONE statement, ONE action, ONE EXACT
  KEY**: `s3:PutObject` on `arn:aws:s3:::opal-estate-report/outset/laptop/comp_heat_drift.json`.

**No S3 object moves in this act and nothing is served differently.** It creates an identity; the
first publish under it is a separate act.

## WHY THIS SHAPE -- the ruling, and the three it refused

Drift is a property of a DEVICE and must be produced where people write files (row `S23`). But
`TO-OS-s-21` disqualifies ambient reach in its own words, and this laptop's principal is an admin
USER carrying `AdministratorAccess`. I offered three shapes in row `S25` and the CTO refused all
three: **(a)** a new IAM user with long-lived keys on the laptop, **(b)** publish-to-git with a
cloud hop, **(c)** a permanent hand publish. The ruling is **(d)**, which I had not offered: assume
a role scoped to ONE KEY from the principal already present. Nothing new is stored on the device,
the published identity is NAMED rather than ambient, and the blast radius is one key.

## THE PATTERN IS THE ESTATE'S OWN, and two things are TIGHTER

`aws_iam_role.capture_writer` in this same file is already "assumed by the device-side capture
tool", so this is build-ladder rung 2 rather than a new idea. Two deliberate differences:

1. **The resource is an EXACT KEY, not a wildcard.** `capture_writer` needs `????-??-??` because its
   day segment varies, and the comment above it records what that cost to get right: **IAM's `*`
   matches `/`**, so a mid-key wildcard spans directory boundaries and a grant that reads as "one
   segment, any value" is really "any depth, any path". This publisher writes ONE key forever, so it
   names that key and the entire class of hazard is absent rather than defended against.
2. **The session name is PINNED.** Without the condition, any assumption of this role looks like any
   other in CloudTrail. With it, the drift publish is attributable to a named session -- which is
   what makes `O21-AC1`'s CloudTrail arm possible at all.

No `ListBucket` (this publisher enumerates nothing), no `GetObject` (it reads its subject from the
local working tree), and no other device's key -- so a laptop cannot overwrite `site-z`'s artifact
even by accident, and neither can touch the freshness key, the group-B key or either probe.

## Pre-state

`comp-iam` census 2026-09-09T16:38:06Z: **228 roles**; no role named `outset-drift-publisher-laptop`
exists, and the applied-plane sweep for `s3:PutObject` reaching
`opal-estate-report/outset/laptop/*` returns **0** holders. Coverage qualifier: attached-managed
statements in that census are UNRESOLVED and therefore uncovered, never absent.

## Legs

1. [ ] `safe-apply` (never bare `terraform apply`; vendored `.tools/terraform.exe`)
2. [ ] Unscoped re-plan reads 0/0/0
3. [ ] APPLIED-plane read after a census refresh: the role exists, ONE statement, the ONE key, and
       the trust names the user ARN with the session-name condition
4. [ ] **EXERCISED**: assume the role under the pinned session name and confirm the caller ARN is
       the assumed-role session, not the ambient admin user. NEGATIVE CONTROL: assuming with a
       DIFFERENT session name must be DENIED, or the condition is decoration.

## Rollback

`terraform destroy -target` on the two resources, or revert the iam.tf block and re-apply. Nothing
depends on the role until the device timer is installed, and the timer is not installed by this act.
No data plane is touched in either direction.

## Close condition

All four legs checked. **The ACCEPT is not this entry** -- `O21-AC1`'s drift arm reads on a SERVED
DAY across three planes (desired == applied, a CloudTrail PutObject by the named session at the
fire, and group A naming `laptop` with n equal to the device's porcelain count). The first exercised
drift read is **2026-09-11** at the earliest.
