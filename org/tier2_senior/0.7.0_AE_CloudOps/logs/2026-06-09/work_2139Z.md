# Work Log — 0.7.0_AE_CloudOps~B — 2026-06-09T21:39Z

## TO: NFRA_COSTAWS Track-2 — Security Walkthrough (W1/W3/W4/W5)

**Dispatch received:** 20260609T213413Z from 2.0.0_SA_COO  
**RAVC2-COMPLETE sent:** 20260609T213923Z to 2.0.0_SA_COO

---

## Walkthrough Scope

PRD: `docs/architecture/NFRA_COSTRED_PRD.md` v0.2  
Project: `org/projects/NFRA_COSTAWS.json` (active; W2(a) VALIDATED PASS 2026-06-08)  
Track-2 = IAM/permission security audit of W1/W3/W4/W5 changes before execution.

---

## Findings by Workstream

### W4 — R8 (Universal ec2-auto-shutdown-enforcer)

**Verdict: ALREADY FULLY DEPLOYED. No action needed.**

- `infra/aws/lambda/ec2-auto-shutdown-enforcer/lambda_function.py`: universal model  
  live — no allowlist, `AutoShutdown=disabled` tag as only exemption, idle-aware  
  3h cap (IDLE_CPU_THRESHOLD=1.0%, IDLE_CEILING_HOURS=3.0)
- `infra/aws/lambda/ec2-auto-shutdown-enforcer/main.tf`:  
  - `ec2:StopInstances Resource: "*"` — covers all instances  
  - `ec2:DescribeTags Resource: "*"` — required to read exemption tag  
  - EventBridge rate(5 minutes) — active  
- IAM: adequate. No gaps. No regression risk from any other W workstream.

### W1 — R1 (Cost-allocation tag backfill)

**Verdict: CLEARED with BINDING constraint.**

**Critical finding:** Two IAM policies use `ec2:ResourceTag/System` conditions
that gate pipeline trigger operations:

- `infra/aws/terraform/bd-pipeline/iam.tf`:
  - `ec2:StartInstances + ec2:StopInstances` gated on `ec2:ResourceTag/System = "BDGoldLayer"`
  - `ec2:TerminateInstances` gated on `ec2:ResourceTag/ManagedBy = "lambda-scheduler"`
- `infra/aws/terraform/inf-pipeline/iam.tf`:
  - `ec2:StopInstances` gated on `ec2:ResourceTag/System = "InflectionPipeline"`

**Binding constraint on R1 backfill script:**
- MUST NOT modify `System` tag value on `bd-gold-layer-runner` (`"BDGoldLayer"`)
- MUST NOT modify `System` tag value on `inf-gold-layer-runner` (`"InflectionPipeline"`)
- MUST NOT modify `ManagedBy = "lambda-scheduler"` on any instance with that tag
- SAFE: ADD new tag keys (`Project`, `Pipeline`, `Environment`, `Macro`, `Owner`)
- SAFE: normalize `Environment` casing; activate keys in Billing console (metadata-only)

Silently changing a load-bearing `System` tag causes zero IAM error at tag-change
time but a silent nightly failure when the trigger Lambda can't start the runner.

### W3 — R3 (bd-gold right-sizing)

**Verdict: CLEARED with pre-apply verification note.**

- `infra/aws/terraform/bd-pipeline/ec2.tf:125`: `instance_type = "r6i.xlarge"`,
  `System = "BDGoldLayer"` — tag defined in TF resource, persists through any
  instance_type change (stop+modify+start) or forced replacement.
- bd-gold-trigger IAM: uses `${aws_instance.bd_gold_layer_runner.id}` ARN ref —
  auto-updates on TF re-apply.
- **Discrepancy flag:** PRD NFRA_COSTRED v0.2 described live instance as
  `c6i.16xlarge`; current TF shows `r6i.xlarge`. Before R3 apply: run
  `terraform plan` on bd-pipeline to confirm actual change delta.
- IAM regression: NONE.

### W4 — R2 (S3 lifecycle — opal-data-bd noncurrent expiry)

**Verdict: CLEARED.**

- opal-data-bd bucket policy: single statement `AllowCloudFrontOACReadGold` uses
  `AWS:SourceArn` condition for CloudFront EVTSA9VEHNZVH only.
- No tag-based conditions; no policy interaction with lifecycle rules.
- Lifecycle changes (tightening 90d→14d noncurrent expiry) have zero IAM/permission
  regression.
- Andrew-gate applies (C2) for the expiry apply due to data-destruction scope.

### W4 — R4/R5 (Leaked runners + hygiene sweep)

**Verdict: CLEARED.**

- R8 universal enforcer structurally covers the no-lifecycle-tag class — leaked
  runners will self-reap when idle >3h (already live).
- Destructive hygiene (EBS delete, EIP release, instance terminate) = C2
  Andrew-gated. IAM is not the constraint.
- No CloudFront or S3 policy regressions.

### W5 — Standing governance (R7 cadence/ownership)

**Verdict: CLEARED.**

- Cost-anomaly-scanner, EventBridge alarms: read-only observability infra.
- No permission changes to active data paths.

---

## Compiler Tools Run

| Tool | Output |
|---|---|
| `comp-iam gaps` | No gaps — 136 services x 85 roles |
| `comp-iam service ec2-auto-shutdown-enforcer` | Role not mapped in compiler; 4 ops UNKNOWN — manually verified via main.tf |
| `comp-iam service inf-gold-trigger` | Adequate for current ops |
| `comp-iam service bd-gold-trigger` | Adequate for current ops |

---

## RAVC2 to COO

Sent 20260609T213923Z. All workstreams CLEARED.  
W1/W3/W4/W5 unblocked for execution.  
Recommended sequence: R1 (forward-only) → R2 (S3, best risk/reward) → R3 (after plan verify).
