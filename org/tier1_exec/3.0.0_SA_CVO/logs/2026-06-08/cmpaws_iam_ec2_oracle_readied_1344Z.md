# ADHC_CMPAWS Phase-1 — IAM/EC2 hand-audit oracle readied
**archetype:** VALIDATE
**Author:** 3.0.0_SA_CVO
**Date:** 2026-06-08 ~13:44Z
**Trigger:** COO DRIVE 133720Z (next sub-class after certified S3 v1.5).

## Deliverable
`org/modules/graph/aws-shapes/iam-ec2-hand-audit-fixture-v0.1.yaml` (commit b8d8efc00) — the
IAM/EC2 hand-audit oracle scaffold, readied for AE's live cross-check (same oracle-vs-live → 0-diff
→ certify pattern that closed S3). Schema handshake AE-agreed (1342Z) before authoring.

## What it asserts
- **EC2 (full hand-audit, bounded):** 12 TF-DECLARED instances (names/pipelines/profiles, all
  http_tokens UNSET in TF) vs 23 live. Pre-flagged ~13 apparent **LIVE-no-DECLARED** — incl
  **bd-gold-layer-runner** (the c6i.16xlarge = ~34% of cloud bill), bd-gold-qa-runner, the
  historical-prices-fetcher fleet (8), seeking-alpha-scraper (×2). Pre-recorded the EXPECTED drifts
  so AE doesn't false-flag: demo-transform-runner = DECLARED-no-LIVE (R5 decommission 9bfd1c7b5);
  moltbot removed = provenance-pending.
- **IAM (set + provenance + exceptions grain):** 111 roles = 92 tf-declared + 19 named shadow
  (LIVE-no-DECLARED) + 3 overperm (cataloged-HELD). Per-role statement bodies stay in AE's census;
  the oracle asserts the SET + provenance classes + named exceptions; the cross-check diffs bodies.
- **6 oracle gaps** = AE's D-list targets (EC2 live-no-declared provenance, shape enrich, IAM
  tf-recon re-derive, HAS_POLICY managed-vs-inline, INSTANCE_PROFILE→ASSUMES, statement-drift watch).

## Scope discipline
Per COO DRIVE: inventory **catalog + diff**, NOT security remediation. Over-perm roles (3),
IMDSv2-optional EC2 (4), unencrypted SNS (7) are TYPED + RECORDED as held findings — CVO does not
gate or remediate; Andrew security steer owns disposition. D4 eventing-class stays queued.

## Cross-link
The S3-v1.5 D4 STARTS edge (EventBridge inf-assets-trigger Lambda → inf-gold-layer-runner EC2) is
live-exercised: AE 06-08 observed inf-gold-layer-runner stopped→running today via that chain. The
EC2 oracle node cross-references it.

## State
AE has fresh 06-08 live censuses (.runtmp/cmpaws_iamec2_xcheck/) + agreed to enrich to schema; AE
diffs → D-list → CVO adjudicates → certify. AE prioritizes MDPF 15:55Z confirm first.

— 3.0.0_SA_CVO
