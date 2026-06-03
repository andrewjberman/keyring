# 0.7.0_AE_CloudOps — Session 2026-06-03 ~1441Z

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, COORDINATE

## ADVI_FEREFI.W2 #6 INF — Lambda deploy (DS request, COO-prioritized, Andrew-direct batch)
DEPLOYED inf-pipeline-v1.7.69: inf-portal-advisor-publisher F11-B (982394f01) + F11-C (c42c5e6ed) real daily fee-split.
- Pre-flight (deploy-discipline): live CodeSha256 qkgJq (5/13) == source-map recorded sha (no drift). The 3 commits between live-5/13 and F11-B were all pre-5/13-23:46-deploy = already live; apply shipped ONLY F11-B+F11-C. Delta = pure additive (pandas groupby/cumsum + new dict keys), no new boto3/IAM/deps (verified via diff grep). comp-iam not needed (no new AWS surface).
- Sequence: build-and-upload.sh (sha GoNrrvM6) -> commit source-map (0d594979c) -> plan (0 add/1 change/0 destroy, only source_code_hash+s3 version) -> safe-apply HALTGT (modified 6s) -> 0-diff verified -> record-terraform-deploy (hit concurrent index.lock; committed its outputs manually 07b19f5b4) -> tag inf-pipeline-v1.7.69 + push --follow-tags.
- LIVE: CodeSha256=GoNrrvM6, LastModified 14:32:33Z.
- DS publisher-trigger Q answered: apply alone does NOT republish (Lambda emits artifacts only on run; fan-out-invoked async by inf-portal-publisher). TRIGGERED regen: async-invoked inf-portal-advisor-publisher {} (StatusCode 202, 14:35:50Z).
- DS VERIFY PASS (gen 14:36:56Z, 4 advisors): 8/8 fee-split fields served, hasFeeSplitSeries fires, total_aua+inflows reconcile $0, nna $0 except IWM $87.46 (0.006% pre-existing ffill rounding, non-blocking). DS RAVC2 -> COO+CTO. INF #6 leg CLOSED.

## bd advisor-timeseries producer-ambiguity ruling (DS W2b 49F blocker; COO DRIVE)
Investigated (comp-trace-style source read). Findings:
- Served platinum/advisors/{id}/timeseries.json: SOLE writer = D_04.client_portal_summary.py:725-729 (pass-through of ts_data = gold/entities/advisors/{id}/timeseries.json, D_04:633).
- That gold key has TWO writers: D_02.advisor_client_detail.py (RICH, authoritative) + bd-portal-advisor-publisher build_advisor_timeseries (lambda:647, LIVE :1147, SIMPLE subset). bd-portal-publisher fan-out-invokes the publisher async every publish (:1965).
- (A) LATENT CLOBBER confirmed (not dead code): masked today only by cascade order (D_04 reads D_02 fresh-rich before publisher's async clobber). Any publisher-gold-write-before-D_04-read -> served loses W2b total_aua_fee_paying + existing NNA-mode nna_canonical_fee_paying. Recommended AE hardening: remove :1147 call+fn (D_02 sole producer). Pending COO/CTO go.
- (B) W2b path: D_02(--upload) -> D_04(--upload) back-to-back, NO publisher between. D_02-alone does not update served. DS unblocked.
- Ruling -> COO; DS-actionable copy -> DS; CC -> CTO (architectural call on hardening).

## MDPF_SCOPED.OPS1
AC4 run#2 = today 15:00Z (~19 min out at tick time). /work cron catches it post-completion -> verify -> AC6 RAVC2. Self-managing.

## Compiler Tools
- Deploy pre-flight: lambda get-function-configuration (live sha), git diff/log (delta scope), build-and-upload.sh (artifact), terraform plan/safe-apply (0-diff). comp-iam service NOT run — diff confirmed zero new boto3/AWS surface, so no IAM delta possible (1-sentence justification per gate).
- bd ruling: source-read trace (D_02/D_04/publisher key wiring + call-sites + fan-out). comp-blast would corroborate the two-writer same-key finding; the direct grep of put-keys + D_04:633 read + :1147 call-site was conclusive.
