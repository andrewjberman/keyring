# CMPAWS sovereign 95%-F1 — CVO oracle roadmap + enumeration checkpoint
**archetype:** COORDINATE
**Author:** 3.0.0_SA_CVO
**Date:** 2026-06-08 ~15:17Z
**Mandate:** Andrew-sovereign Stop-hook session goal (COO 150807Z) — all CMPAWS per-class compilers
to ≥95% F1 + brittleness, CVO-independent cert as the done-gate.

## Delivered this turn
1. **F1 cert methodology (the done-gate)** — `CMPAWS_F1_CERT_METHODOLOGY.md`. Strict 95%-F1 (existence
   vs live re-pull + typing/provenance vs certified oracle) + brittleness-pass + 0-untyped; CVO-independent
   (AE builds / CVO measures with CVO scorer); volatile-set rule; per-class CVO-signed scorecard = done-evidence.
   Aligned COO/AE/CTO.
2. **Eventing oracle v0.2** — `eventing-hand-audit-fixture-v0.1.yaml` (006a1d408). 92 rules (85 sched/7
   event-pattern), event-pattern subgraph + D4 3-edge chain fully audited, reconciled to CTO schema §3.3.
3. **EV-SCHEMA-GAP-1** surfaced → CTO: §3.3 EMITS_TO source is S3-only, but 3 live rules have
   EC2-state-change / CloudTrail-API sources = a 0-untyped blocker → vocabulary-add ruling pending.
4. Schema alignment confirmed against CTO's canonical `ADHC_CMPAWS_SCHEMA.md` (51218a486) — one vocabulary.

## Cert sequencing (locked w/ COO)
- **Wave-1 (S3 + IAM/EC2):** oracles CERTIFIED (v1.5 / v0.2). F1-measurement fires the moment AE delivers
  those two compilers → first 2 scorecards = the methodology proving ground.
- **Eventing:** oracle v0.2 is CURRENT-state. Re-base to post-swap state after the MDPF_CADENCE EventBridge
  apply (0.6.0_AE pings at apply), THEN run eventing F1-cert (the one class with a sequencing dep). Also
  blocked on the EV-SCHEMA-GAP-1 CTO ruling before the eventing compiler builds.
- **All other classes:** cert as built (no sequencing dep).

## Remaining-class oracle plan (live enumeration captured 2026-06-08 ~15:15Z — de-risks each build)
| Class | §  | Live count | Oracle grain plan | Anchors / ties |
|---|---|---|---|---|
| **Lambda** | 3.4 | (comp-lambdamap) | subsumes comp-lambdamap; fold its source-map drift as the `code_sha` DECLARED-vs-LIVE class | do NOT double-build |
| **SNS** | 3.5 | 8 topics | full hand-audit (small): topic + kms + access-policy(§1.5) + PUBLISHES_TO/SUBSCRIBES edges | inf-otp-alert (OTP), opal-infrastructure-alerts (the eventing SNS target), trade-pipeline-ses-* |
| **SQS** | 3.6 | 2 queues | full (tiny): mdpf-daily-trigger-dlq (+1) + DEAD_LETTERS_TO + TRIGGERS edges | mdpf-daily-trigger DLQ ties to the eventing/MDPF chain |
| **KMS** | 3.10 | 2 CMK | full (tiny): find-insure-data-key, inf-ebs-key + key-policy(§1.5) + ENCRYPTS_WITH inbound + GRANTS (the CreateGrant class that bit ORIAPI) | inf-ebs-key ↔ EC2 EBS encryption |
| **CloudFront** | 3.8 | 4 dists | full (small): EVTSA9VEHNZVH (portal, the OAI/OAC from S3 oracle), E398SP0DG1ME0Y, +2; ORIGIN/INVOKES(L@E)/USES_OAC/USES_OAI + cache-behavior path→origin drift | folds the comp-routes path→dist map; EVTSA9/E398 path-patterns from memory |
| **DynamoDB** | 3.7 | 35 tables | SET + per-table props (billing/pitr/deletion-protection/gsi/stream) + READS/WRITES/STREAMS_TO; pitr/del-protect OFF = held finding | opal-partner-{49financial,inflection,cottonwood,demo}, TRSB_LEDGER trade-users/submissions hardening tie |
| **Secrets** | 3.9 | 59 | SET + per-secret (kms/rotation) + READS_SECRET (role GRANTS ∩ GetSecretValue); LIVE-no-DECLARED secrets = exposure-attribution class | Orion JWT dual-path (S3 + SM orion/jwt/current); smartx creds; the openai-key fleet |
| **CloudWatch** | 3.11 | 35 alarms / 194 log groups | alarms full + log-groups at SET+retention grain; MONITORS/NOTIFIES/LOGS_TO; LIVE-no-DECLARED alarms | mdpf-freshness-checker treat_missing_data=breaching (canonical correctness case) |

## Pace
Small classes (SNS/SQS/KMS/CloudFront, all ≤8) = quick full hand-audits next; DynamoDB/Secrets/CloudWatch =
SET+exception grain (like IAM's 111 roles), per-item bodies via AE cross-check. All built ahead of AE's
per-class compiler. Each oracle → AE cross-check → CVO adjudicate → certify → F1-measure vs the done-gate.

## Standing interrupts
- MDPF 15:00Z scheduled-cadence: adjudicate AE's RAVC2 when it lands → close MDPF+MDLP pair.
- 0.6.0_AE MDPF_CADENCE apply ping → re-base + eventing F1-cert.
- CTO EV-SCHEMA-GAP-1 ruling → unblocks eventing compiler.
- AE Wave-1 compiler delivery → first F1 scorecards.

— 3.0.0_SA_CVO
