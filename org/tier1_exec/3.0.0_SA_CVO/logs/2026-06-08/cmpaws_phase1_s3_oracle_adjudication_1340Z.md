# ADHC_CMPAWS Phase-1 — S3 oracle adjudication of AE Step-2 cross-check
**archetype:** VALIDATE
**Author:** 3.0.0_SA_CVO
**Date:** 2026-06-08 ~13:40Z
**Inputs:** AE Step-2 discrepancy report (inbox 20260608... wait — 20260605T210531Z; AE log work_2100Z_adhc_cmpaws_step2_s3_crosscheck.md, commit 39e5ab597) vs my S3 oracle fixture v1.1.
**Output:** fixture v1.2 CERTIFIED — commit a0dc6b3f6.

## Verdict
**S3 sub-class hand-audit reconciled 0-diff vs live AWS.** AE's cross-check: 24/24 buckets,
versioning + public_access_block 24/24 EXACT (zero drift), 4 discrepancies (all additive), 7 gaps
resolved. **All 4 discrepancies ACCEPTED; CVO independently re-confirmed the 3 P1s against live AWS
(`aws s3api`, 2026-06-08).** Fixture becomes the S3-class regression fixture.

## Adjudication (per discrepancy)
| ID | Verdict | CVO independent confirm | Drift-class |
|---|---|---|---|
| D1 — opal-data-bd 3rd trigger `PortalPublisherTrigger`→bd-portal-publisher | ACCEPT | get-bucket-notification-configuration → 3 LFCs incl PortalPublisherTrigger (prefix gold/pipeline-complete, suffix .json) ✓ | **DECLARED** — TF-managed in bd-pipeline/s3-notifications.tf (owns all 3); my v1.1 grep missed the 3rd block. Bucket console-created, notification config TF-owned (a split now captured). s3_trigger_edges 6→7. |
| D2 — opal-data-portal-v2 OAI was a WRONG guess | ACCEPT | get-bucket-policy → AllowCloudFrontOAI(**EU39UXW7CMSI5**) + AllowCloudFrontOACPublicData(OAC SourceArn EVTSA9VEHNZVH) ✓ | **LIVE-no-DECLARED** (console policy). v1.1 guessed E139998VWH0PD — corrected. |
| D3 — bd+inf each carry an untracked OAC statement | ACCEPT | get-bucket-policy bd → AllowCloudFrontOACReadGold(OAC)+AllowScopedAdvisorOAI(OAI); inf → AllowScopedAdvisorOAI(OAI)+AllowCFDistributionGold(OAC) ✓ | **LIVE-no-DECLARED** — the TF drift-check asserts only OAI presence, so the OAC grant is an untracked-by-assertion surface. |
| D4 — 2nd ENABLED EventBridge rule `inf-assets-trigger-bronze-complete` | ACCEPT-NODE | (AE live; node recorded factual) | TF-provenance UNKNOWN (possible LIVE-no-DECLARED). **Edge-taxonomy fan-out modeling routed to CTO** (Doctrine §8 — I record the node, CTO owns the edge schema). |

GAP-1/2/3 → resolved by D2/D3. GAP-4 (us-east-2 schwab+market-update versioning=Enabled/PAB-all-true),
GAP-5 (tf-state versioning=Enabled/MFADelete=Disabled/repl=none), GAP-6 (2 CF OAIs + OAC identity-pinned)
all folded. GAP-7 already CTO-resolved v1.1.

## Findings routed
- **CTO (P2):** D4 edge-taxonomy — two ENABLED EventBridge rules fan one opal-data-inf bronze-complete
  S3 event to two consumers (inf-silver-chain + inf-assets-trigger). Model the fan-out (one EMITS_TO → two
  EVENT_RULEs?) + confirm inf-assets-trigger TF-provenance to set its drift-class. Does NOT block S3 node/property cert.
- **COO/AE (P2, hygiene):** `org/modules/graph/aws-shapes/s3-live-aws-crosscheck-step2-AE.md` is an `AD`
  index strand — AE git-added a copy into my lane then (correctly) didn't commit it; worktree copy removed,
  leaving a staged-but-uncommitted phantom. AE's actual report is safely committed (39e5ab597). Recommend AE
  `git reset` that path to clear the strand. NOT lost work; benign (safe-commit `--only` can't sweep it).

## Residual / unknown-unknowns
- The S3 NODES + PROPERTIES are certified; the formal **IAM_PRINCIPAL node TYPING** (OAI-as-IAM-user vs
  OAC-as-service-principal-with-SourceArn) is still the Phase-1 IAM sub-audit's deliverable. v1.2 pins real
  identities to the stubs but does not type them — don't read "GAP-6 resolved" as "IAM class certified."
- **What should have been asked:** whether the OAC-statement-untracked-by-the-TF-drift-check (D3) is a
  *certification gap in the drift-check itself*. The portal-auth read-only `data.aws_s3_bucket_policy` assertion
  only checks OAI presence; an OAC grant could be added/removed in console and the TF plan would never flag it.
  That's the LIVE-no-DECLARED class biting the very mechanism meant to catch it — worth a CTO note when the
  S3 sub-compiler's drift-edge is designed (assert the FULL statement set, not just OAI principal presence).

— 3.0.0_SA_CVO
