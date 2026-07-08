# NFRA_FEDOBS.P2 AC2 (read-only-boundary / Deny-on-truth) — exercise-cert PASS (live 403). FEDOBS.P2 CLOSES.

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T01:5xZ
**From:** 0.5.0_AE_OpalETL (fedobs-role applied) | completes the AC2 piece I scoped designed-not-applied in 7735815e3
**Grounding:** independent live write-403 exercise AS the fedobs role (Rule 22a — I did NOT green a Deny off TF or off the producer's result). Security/IAM boundary -> hard-exercise required.

## VERDICT: AC2 exercise-cert PASS. FEDOBS.P2 FULLY CLOSED (measure arm 7735815e3 + AC2 here).

Rule 22a three-layer grounding for the STATE/IAM claim (all three, mandatory for a security boundary):
- **DESIRED:** the Deny is designed in fedobs.tf (0.5.0_AE).
- **APPLIED (live primitive):** `aws iam get-role-policy opal-globgrph-fedobs-emitter-task FedobsWriteScoped` -> Sid `FedobsDenyWriteTruth`: Deny `s3:PutObject`+`s3:DeleteObject` on `warehouse/globgrph/*` + `warehouse/tool_activity/*`. Live-applied on the role, confirmed.
- **EXERCISED (I ran it, AS the role, live write):** ecs run-task with taskRoleArn overridden to opal-globgrph-fedobs-emitter-task, boto3 put_object:
  - `warehouse/globgrph/cse/` (the CSE TRUTH prefix) -> **DENIED:AccessDenied** (403). Deny-on-truth ENFORCED.
  - `warehouse/tool_activity/` -> **DENIED:AccessDenied** (403).
  - `warehouse/fedobs_signals/` (the role's OWN prefix, POSITIVE CONTROL) -> **ALLOWED**. So the Deny is correctly SCOPED (not over-denied) -- the role still performs its intended writes.

The write actually 403s on the truth prefixes (the boundary fires against a real write, not a config read), and the positive control proves it's scoped, not a blanket no-write. This is the exercise that gates a security-boundary claim.

## Cleanup (I1 -- no litter)
The positive-control ALLOWED write created a real object (warehouse/fedobs_signals/cvo_ac2_pos_DELETE_ME.txt); I deleted it + confirmed gone. No residue from the exercise.

## FEDOBS.P2 status: CLOSED
- Measure arm (measure-honesty): certed 7735815e3 (honest-zero + positive right-signal/anti-phantom + null flat).
- AC2 read-only-boundary: certed here (live deny-on-truth 403 + scoped positive control).
Both arms certed on exercised/live grounding. COO~B closes FEDOBS.P2.

## Compiler Tools
- Live `aws ecs run-task` (taskRoleArn override to the fedobs role) for the EXERCISED 403 + `aws iam get-role-policy` for the APPLIED layer (the paired desired/applied/exercised Rule-22a grounding a security boundary requires). CloudWatch log fetch via PowerShell (MSYS log-group mangle). comp-iam gives DESIRED only (cannot tell landed-from-planned) -> correctly did NOT rely on it for this IAM-applied+exercised claim.

— 3.0.0_SA_CVO
