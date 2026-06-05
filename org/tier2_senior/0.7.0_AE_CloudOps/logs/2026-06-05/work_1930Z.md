# work-cycle 0016 — demo-transform-runner i-03343a60 full decommission

**archetype:** DECOMMISSION **secondary:** MANIFEST
**Date:** 2026-06-05 ~1926-1930Z
**Trigger:** 0.6.0 TERMINATE GO 192558Z (R5 PASS: 22414 scanned, leak_count=0) + COO GO 192621Z (Andrew pre-cleared)

## All gates cleared
- 0.6.0 RAVC2 complete: DEMOAUTH.002 done, 22414/22414 written
- Phase C R5 pii_leak_scan: leak_count=0, zero HardErrors
- COO confirm: Andrew direct "$61/mo demo-transform, decommission the ceremony"

## Actions taken

1. AMI snapshot: ami-0c4e0350b8cce8ff0 (30d insurance, no-reboot)
2. Enforcer exclusion check: enforcer redesigned 2026-06-05 to universal idle-ceiling model (no per-ID list); no entry to remove
3. Terminate: i-03343a6072834f77d -> shutting-down (Andrew ran the CLI command; pre-approved by COO + Andrew-direct)
4. EC2_MANIFEST.json: removed demo-transform-runner entry; JSON validated clean
5. /tmp run script and demo-reclone* transient units die with the box (no separate teardown needed)

## Cost recovery
$61/mo demo-transform-runner (t3.large, launched 2026-05-23) fully recovered. Dataset lives in opal-data-demo/platinum (static, independent of the box). DS final PII sign-off tomorrow = read-only on bucket, does not need the instance.

## Notes
- TF resources (infra/aws/terraform/shared-infra/demo-transform.tf IAM role/SG) left in place pending COO/MSTR decision on TF destroy; instance itself is terminated
- Future rebuild (extremely unlikely per Andrew) = local `python demo_transform.py --apply`, no EC2 needed
