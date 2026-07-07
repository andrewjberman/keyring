# CVO Exercise-Cert — NFRA_FEDOBS P1 AC2 (read-only-on-truth boundary): PASS

**Date:** 2026-07-07T11:57Z
**Agent:** 3.0.0_SA_CVO
**Target:** the FEDOBS emitter role read-only-on-truth boundary (0.5.0, fedobs.tf db0753623, applied 0.7.0~B safe-apply 0-diff). Federation-plane boundary law: FEDOBS OBSERVES, it does not write semantic truth (only PROMOTE materializes truth).
**Grounding:** Rule 22a — DESIRED (fedobs.tf, pre-verified pre-apply) + APPLIED (live get-role-policy, INDEPENDENTLY run, not 0.5.0's report). Applied-check is the definitive cert for a deterministic Deny (INTEGRATIONS-leg-2 precedent, CTO-affirmed).
**Verdict:** AC2 boundary = PASS.

## APPLIED (live get-role-policy opal-globgrph-fedobs-emitter-task/FedobsWriteScoped — I ran it myself)
```
FedobsDenyWriteTruth : Deny  [s3:PutObject, s3:DeleteObject]  on
    arn:aws:s3:::opal-313476888478-globgrph/warehouse/globgrph/*      (graph_nodes/edges/contracts + cse_events = C1/C0 truth)
    arn:aws:s3:::opal-313476888478-globgrph/warehouse/tool_activity/*  (behavior catalog)
FedobsFindingsAndSignalsWrite : Allow [s3:PutObject] on  warehouse/fedobs_obs_findings/* + warehouse/fedobs_signals/*  (evidence ONLY)
FedobsOwnRead : Allow [s3:GetObject, s3:ListBucket] on the bucket + the fedobs prefixes
```
- APPLIED == DESIRED (the fedobs.tf I pre-verified pre-apply): byte-for-byte -- Sid, Effect, Action, all Resource ARNs match. NO DRIFT (a fresh IAM apply -> live get-role-policy is the Rule-22a-mandated applied-truth; comp-iam DESIRED could not confirm landed-vs-planned).
- **Deny-overrides-Allow** => the FEDOBS emitter role physically CANNOT PutObject/DeleteObject the semantic truth (C1/C0 graph + CSE log + tool_activity), even if a future Allow drifts in. The write-scope is CORRECT (Allow only to findings/signals -- evidence, not truth), not over-broad. This is the charter's Federation boundary law ("Trino observes/correlates; it does not define semantic truth") made PHYSICAL at IAM, not app-level. Same deterministic-Deny class as the DenyCrossFirmBuckets I certed tonight.

## EXERCISED belt (wired, in-task) + honest sequencing
- 0.5.0 wired fedobs_emit.py --assert-boundary (c42c9fb98) to run FROM WITHIN the emitter's ECS task (where the ECS-only trust allows): attempt PutObject to warehouse/globgrph/ -> assert AccessDenied (FATAL fail-closed if not denied) + confirm a fedobs_obs_findings write succeeds. So the EXERCISED limb fires organically in-task each run -- no role-assume by me needed (the role's trust is ECS-only, my earlier point). The applied-check above is the DEFINITIVE cert for this deterministic Deny; the in-task self-assert is the confirming belt each run.
- HELD (sequences after the next deploy increment): the two-observer x C1 JOIN re-run (obs_findings_enriched) + the evidence_ref decompress -- the obs_findings Trino binding isn't landed yet (0.5.0 pings on landed). AC1 (the two-DISTINCT-observer overlap: D8 x PIPESCRIPT x C1 = 3 hotspots) is already CTO-accepted.

## Verdict
FEDOBS-P1 AC2 (read-only-on-truth boundary) = PASS -- the Deny is APPLIED (== desired, no drift), Deny-overrides-Allow makes truth-writes structurally impossible, write-scope correct. The join/evidence_ref re-verify sequences after the obs_findings binding lands (held). This closes the FEDOBS-P1 boundary -- the Federation plane can observe-and-emit-evidence but cannot write the compiled substrate truth (the charter's separation-of-concerns, physical). Ties to my SEMCTL analysis: this IS the "FEDOBS = federate-the-shipped-observers over the store, boundary-enforced" re-scope, now with the read-only boundary certed.
