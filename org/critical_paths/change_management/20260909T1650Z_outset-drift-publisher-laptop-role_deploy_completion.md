# DEPLOY COMPLETION LEDGER -- the device drift publisher's SCOPED ROLE (NFRA_OUTSET.TO-OS-s-21)

**Opened:** 2026-09-09T16:50Z by `0.7.0_AE_CloudOps~W` (committed OPEN at `569c698d4a`)
**Status:** **CLOSED 2026-09-09T16:55Z** -- all four legs verified, including a negative
control proving the session-name condition is enforced rather than decorative
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

## Legs -- ALL FOUR VERIFIED

1. [x] `safe-apply`: **2 added, 0 changed, 0 destroyed**. Role created in 1s, policy in 0s.
2. [x] Unscoped re-plan: **"no differences, so no changes are needed"**.
3. [x] APPLIED plane, census refreshed first (2026-09-09T16:52:15Z, **229 roles**):
       `outset-drift-publisher-laptop` holds **exactly 1 statement** --
       `PublishThisDevicesDriftArtifactOnly`, `["s3:PutObject"]`,
       `["arn:aws:s3:::opal-estate-report/outset/laptop/comp_heat_drift.json"]`. Trust principal
       `{"AWS": "arn:aws:iam::313476888478:user/Andrew_Berman"}`; trust condition
       `{"StringEquals": {"sts:RoleSessionName": "outset-drift-laptop"}}`. DESIRED == APPLIED.
4. [x] **EXERCISED, with the control that makes it mean anything.**
       ambient caller -> `arn:aws:iam::313476888478:user/Andrew_Berman`
       GREEN, assume as `outset-drift-laptop` -> the caller becomes
       `arn:aws:sts::313476888478:assumed-role/outset-drift-publisher-laptop/outset-drift-laptop`
       **NEGATIVE CONTROL, assume as `some-other-session` -> DENIED.** Without this arm the
       condition would be untested and indistinguishable from decoration.
       AND THE REAL PUBLISH, end to end under the named identity:
       `OK: device=laptop publisher_arn=arn:aws:sts::313476888478:assumed-role/`
       `outset-drift-publisher-laptop/outset-drift-laptop answer_state=OK n=156`
       `tracked_total=30835 git_head=2befa0e9ff10 bytes=27572`
       `dest=s3://opal-estate-report/outset/laptop/comp_heat_drift.json`

## SHARPENING (2) ANSWERED: NO SEAM-MODULE CHANGE, NO BLOCKING ROW

`publisher_arn` rides in `denominators.tool_scalars` beside `device` / `tree_root` / `git_head` --
the node `_denominators_of` already surfaces a tool's scalars into, and the node the consumer's
`_outset_device_fields` already reads from. `publish_artifact` already accepts an `s3_client`, which
is exactly the hook a scoped-session publish needs. `org/modules/heatmap/outset_seam.py` is READ and
unedited; the lane resolver was run with that file as the NEGATIVE CONTROL and refused it, while the
device path and `iam.tf` were PERMITTED.

## SHARPENING (5): THE INSTALL LINE, REPORTED BEFORE INSTALLING

Reported to `2.0.0_SA_COO` before the task is created, as the amendment requires. The task did NOT
exist beforehand (`Get-ScheduledTask` -> ABSENT), so nothing is installed over blind.

**INSTALL** (run in PowerShell -- `schtasks` through Git Bash is mangled by MSYS path conversion,
which rewrote `/Query` into `C:/Program Files/Git/Query` when measured):

    schtasks.exe /Create /TN "OpalOutsetDriftLaptop" /SC DAILY /ST 07:30 /F /TR "cmd /c cd /d C:\Users\AndrewBerman\Desktop\ajb_workspace && C:\Users\AndrewBerman\AppData\Local\Programs\Python\Python312\python.exe infra\aws\ec2\outset-drift-device\publish_drift.py --out-prefix s3://opal-estate-report/outset"

**REMOVAL, one line:**

    schtasks.exe /Delete /TN "OpalOutsetDriftLaptop" /F

07:30 local is **11:30Z** in September (ET, UTC-4) -- ninety minutes before the 13:00Z report, which
is the ordering `O21-AC1` grades. The `cd /d` is REQUIRED: the script DERIVES its tree from
`git rev-parse --show-toplevel` and Task Scheduler sets no working directory. The interpreter path
and the repo root were both MEASURED on this device, never assumed.

## Rollback

`terraform destroy -target` on the two resources, or revert the iam.tf block and re-apply. Nothing
depends on the role until the device timer is installed, and the timer is not installed by this act.
No data plane is touched in either direction.

## Close condition

All four legs checked. **The ACCEPT is not this entry** -- `O21-AC1`'s drift arm reads on a SERVED
DAY across three planes (desired == applied, a CloudTrail PutObject by the named session at the
fire, and group A naming `laptop` with n equal to the device's porcelain count). The first exercised
drift read is **2026-09-11** at the earliest.
