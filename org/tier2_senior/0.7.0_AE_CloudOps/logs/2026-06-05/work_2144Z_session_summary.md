# Session Summary — 0.7.0_AE_CloudOps — 2026-06-05 (post-compaction continuation, ~19:30-21:44Z)

**Role:** AWS Engineer / CloudOps-Security. **Mode:** event-driven (persistent inbox Monitor, LD-0157).
**Net:** 5 threads closed + 1 standing hold. 0 incidents. All Andrew-watched surfaces GREEN; repo==deploy coherence maintained throughout.

---

## 1. demo-transform-runner FULL decommission — CLOSED (RAVC2-Accept)
Trigger: 0.6.0 TERMINATE GO + COO GO (R5 pii_leak_scan PASS, leak_count=0; Andrew pre-cleared).
- AMI snapshot ami-0c4e0350b8cce8ff0 (30d insurance) -> terminated i-03343a6072834f77d (Andrew ran the CLI; sandbox denied AE) -> removed from EC2_MANIFEST.json -> commit 9bfd1c7b5.
- Enforcer: no per-ID exclusion (redesigned 2026-06-05 to universal idle-ceiling; no allowlist).
- ~$61/mo recovered. COO RAVC2-Accept 193222Z. TF IAM role/SG deferred ($0/mo, queued for TF audit pass).

## 2. aum-metrics donut $1.71B -> $1.808B — CLOSED (DT-validated)
Andrew caught the Global "Total AUA" showing $1.71B (should $1.81B). Verify-before-execute: the PRODUCER artifacts were CORRECT; root cause was FE-side.
- ROOT CAUSE (ModelPortfolios.tsx:670-674): Global Total AUA is FE-computed = modelAUM (aum-metrics by_model, Inflection PRESENT) + non_model_assets.non_model_aum. PROD served an Inflection-blind non_model_assets.json (~$218M) -> $1.71B. Tell: older quarters matched my artifact exactly; only the current period was ~$100M short = exactly Inflection.
- All 4 S3 artifacts verified correct/fresh: non_model_assets.json non_model_aum $315.8M (inflection $90.9M) -> enterprise_total $1.808B; aum-metrics $1.808B; account-distribution 7,301/$1.492B; aggregate-aua union correct. Donut identity exact.
- DE independently re-derived; DEV correct (Andrew-confirmed). DT shipped portal v2.1.115 (62767be0 + 253045ec + 86f7e8da). I CF-flushed I28A6LWFSQID3J22I48YVNMD3X (Completed). DT validated + RAVC2'd COO.

## 3. Blend-split architecture — Andrew chose FE-side; producer reverted to granular
- DS authored producer-side blend-split (c61a45a05 + comment-fix be788e8d4); I deployed to S3 (crossed DE's HOLD).
- Andrew ruling: roll blends on the FRONTEND, not the producer (DE 86f7e8da: VALUE 50/50-split, COUNT full-to-each). Producer stays granular (blend-keyed) for analysis.
- REVERTED my S3 deploy to granular 3c31f8ea; COO git-reverted repo (4386bdc2d). Re-verified live: repo HEAD == S3 deploy == 3c31f8ea (0 blend markers). Full coherence. (Caught + flagged: be788e8d4 was a comment fix ATOP the blend-split, not comment-only -> deploying it carried logic; re-verified live state, not ACK.)

## 4. Portfolio Analytics "Total Holdings" 7,301 -> 7,465 — CLOSED (joint AE+DE, Andrew GO, DT-validated)
Andrew-direct collab: the Total Holdings stat didn't apply the blend-split the trend chart does.
- AE data-source trace: "Total Holdings" = AccountDistributionMetrics.tsx:27 -> activeDistribution.total.account_count -> account-distribution.json (Global 7,301). DIFFERENT artifact from the trend (aggregate-aua-timeseries.json); that's why 86f7e8da didn't touch it.
- Joint rec (AE source+backend / DE FE-shape, independently identical): FE-side fold, splitTotal = 7,301 + 164 blend = 7,465; backend rejected (granular-producer). Scoped to headline-only (defer per-model + histogram to avoid label-vs-histogram mismatch). 2 Andrew rulings flagged (semantic distinct-account-vs-sleeve; histogram redistribution = separate/backend).
- Andrew GO (chose 7,465). DT shipped v2.1.116 (d18cd8c8). I CF-flushed I6ON5TX8YEWM477ZM6RFDGQFB8 (Completed). DT served-verified (chunk CLvJh6i4->GSwwcBlO) + RAVC2'd COO.

## 5. ADHC_CMPAWS Phase 1 Step 2 — live-AWS S3 cross-check — COMPLETE (report->CVO)
COO /drive dispatch. Cross-checked CVO oracle fixture v1.0 (7cfd37b1e, 24 buckets) vs live AWS.
- Versioning + public-access-block: 24/24 EXACT (zero drift).
- 4 additive discrepancies: D1 bd 3rd notification trigger (bd-portal-publisher); D2 portal-v2 OAI=EU39UXW7CMSI5 (not fixture-guessed E139998VWH0PD) + OAC; D3 bd+inf OAC statements untracked; D4 GAP-7 2 EventBridge rules (fixture named 1).
- GAP-1..7 all resolved (3 bucket policies, us-east-2 both Enabled/all-true, tf-state Enabled/no-replication, 2 CF OAIs + OAC pattern).
- Report committed 39e5ab597 (AE log dir — owned-paths hook blocked the CVO module dir; routed correctly, no --force). Sent to CVO; CVO adjudicates oracle.

---

## Standing hold (timed)
- **smartx-exporter R5 decommission** — gated on tomorrow's ~11:30Z MDLP nightly (validates the 3-producer distribution path runs unattended) + COO->Andrew GO. AMI-snapshot-then-terminate plan ready; TF-managed (ec2.tf + autostart Lambda + ECR).

## Discipline notes reinforced this session
- Verify-before-execute / verify-LIVE-not-ACK: caught the be788e8d4-carries-logic revert + the COO-URGENT-read-stale-ACK; resolved by re-verifying live S3 SHA, not trusting messages.
- FE-computed aggregates: a served value may equal NO stored artifact field; trace the FE computation (modelAUM + nonModel).
- Owned-paths: org/modules/graph is CVO-owned; relocated my report to AE log dir rather than --force.
- Cost discipline: blend-split + comment-fix deployed to S3 but NO ad-hoc run (C1; scheduled nightly).

## Compiler / tooling
sha256 byte-verify (deploy/revert/coherence), s3api versioning/PAB/notification/policy across 24 buckets, list-object-versions (prior-version diff), cloudfront create/get-invalidation (PowerShell), events list-rules, git revert/pull coherence, safe-commit.sh (owned-paths-aware), Monitor re-arm after exit-143.
