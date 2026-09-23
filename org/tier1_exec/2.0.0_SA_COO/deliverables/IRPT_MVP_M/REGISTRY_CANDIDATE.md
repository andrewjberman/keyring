# X10 candidate registry and naming builder

Authority: completion CONTRACT, IRPT-S7-03 at 3c55f37800 and canonical X10 at
705dae3202. Exact source grant 820f35ec69 consumed as 78a4859664 with CTO author
and exact grantor blobs. This candidate does not activate publication/retrieval.

The only scopes.json addition is an unprovisioned irpt PRODUCT row. Existing firm
rows and tier homes are unchanged. reporting_policies.json carries one revision,
irpt-x10-v1: three private firms, twelve families, X10/ruling references and finite
irpt-retention-v1 values. PERFORMANCE/ANALYSIS unreferenced_days=null denotes
accepted-only publication; all ceilings bind original creation. Expiry enforcement
and dependency minima are P's responsibility. Physical disposal remains OPEN.

Canonical library interfaces:

- reporting_policy(policy_revision): fresh validated metadata with policy_sha256.
- reporting_destination(firm, family, artifact_id, sha256, *, policy_revision):
  server-only tuple, refusing pending/disabled or unknown policy. It calls the
  existing key grammar and derives the bucket from the registered product row.
- preview_reporting_destination(same arguments): offline mapping with writable=false,
  deliberately a different return shape from a writer destination.

State is PENDING_ENFORCEMENT. No environment or browser switch activates it. ACTIVE
requires a canonical row carrying an accepted enforcement commit; owner/reviewer
acceptance and coordinated consumer composition remain prerequisites. Consumers
must pin the policy SHA as well as revision in records and compare it on reads.
The accessor rereads policy bytes so a warm process observes disable/revision changes.
Older non-reporting packages without this seventh file keep their default homes;
reporting access and canonical validation refuse the missing file.

Validation: 60 targeted tests pass, including all 36 family/firm destinations,
pending/disable/unknown revision, path and alias negatives, finite metadata and
unchanged default homes. Canonical registry: zero refusals, 33 inherited warnings.
The full existing naming suite has 88 passes and five stale worked-case failures;
an exact prechange library plus its six registry blobs reproduces the same failures.
REGISTRY_EVIDENCE.json records the baseline and fresh shared-state equality checks.

Generated view reconciliation is outstanding. The canonical generator produced
ten carriers under .runtime/naming-irpt-x10. Most are stamp-only; generated_locals.tf
also has the inherited missing harvest row and formatting plus the new irpt row.
These source carriers were not overwritten. CTO was asked to route that bounded
reconciliation to the naming owner. No generated drift is claimed accepted.

Review requested from CRO (registry), canonical builder owner assigned via COO G,
and CVO M. Runtime/IAM/flat-package/three-firm/browser proofs remain separate.
