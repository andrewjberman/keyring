# work_1437Z — FIND_INSURE.024 live-wire + cost-gate-verify + canary caught Lusha v3 shape bug; .037 closed

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, VALIDATE, COORDINATE

**Agent:** 0.1.0_DS_MarketIntelligence~C (respawn — Phase 2A LIVE-DISPATCH directive)

## Headline
Respawned to "fire .024 LIVE-DISPATCH (both gates GREEN, fire on boot)." Empirical recon showed "fire on boot" was the STUB-mode framing, not the live substrate. Drove .024 from there to one-bug-from-firing, and a canary caught that last bug — the LushaClient v3 request shapes are systematically wrong (stub-masked) — BEFORE any credit burn. Also closed .037 (aggregator run-date hardening) in parallel.

## .024 — what happened (in order)
1. **Recon (DIAGNOSE):** caught 3 readiness gaps vs "fire on boot": (1) serving/scoring.json absent (subset input); (2) bronze handler stub-only even at stub_mode=False (credit-burn-zero-output); (3) crawl/parse/score-linkedin Lambdas undeployed. Surfaced to COO; CTO ruled model B (local driver) for v0.1 (A=productionization, deferred); FIND_INSURE backgrounded today (ADVI IWM demo priority).
2. **Blocker-2 live-wire (IMPLEMENT):** added LiveCostGate (DDB atomic-ADD), LiveS3Writer (explicit SSE-KMS, bucket default is AES256 not KMS), LiveAlerter (SNS 402) to crawl_linkedin_bronze, selected on stub_mode=False, injectable. 56/56 tests (12 new). Commit f4d424037, COO-accepted. (parse/score already had correct live boto3 fallback — no change.)
3. **scoring.json:** DS~E shipped it (.023, 99/99). Subset input cleared.
4. **Cost-gate live-verify (VALIDATE):** probe proved DDB atomic-ADD + SNS + S3 SSE-KMS fire vs real AWS, no Lusha. PASSED. costgate_live_verify_probe.py (d7b472a97).
5. **Subset (DIAGNOSE):** literal rule computed to 20, but ratified intent = 24 (present+adjacent). Flagged pre-burn; COO confirmed 24 + corrected config (f1ff2c16e). Driver intent24 = wm_classification in {present,adjacent}.
6. **Driver + dry-run:** phase2a_subset_driver.py — 24/24 resolved, 0 missing-domain. Uploaded missing S3 configs (cost-budgets-v0.1, scoring-weights-v0.1).
7. **Canary-1 (VALIDATE — the catch):** real Lusha on allianz-life → no_company_match. Root cause: LushaClient v3 request shapes WRONG. companies/search sent {"domains":[]}; correct (confirmed 200): {"companies":[{"domain":...}]}. prospecting rejects top-level "pages"; companies/enrich rejects "companies". Stub fixtures encoded the same wrong assumptions → 56 tests green while live integration broken. $0 burned (400s free).

## .024 status
BLOCKED on LushaClient v3 request-shape reconstruction + stub realignment (next item, task #6). All other gates proven: live-wire ✓, cost-gate-live ✓, scoring.json ✓, subset=24 ✓, driver ✓.

## .037 — CLOSED
Aggregator run-date hardening: --run-date now AUTO (per-slug latest populated partition) vs the wall-clock-today footgun; explicit override retained. Real-data smoke: 99/99 BARS_MET vs old false 1/99. 12/12 tests. Commit 0fb7a064e, COO ACCEPTED+CLOSED. v2 tier-independent DEFERRED (not built speculatively).

## Compiler Tools
None run this cycle — work was Lambda/script live-wiring + API-integration diagnosis + S3/DDB/SNS empirical probing, not pipeline dependency tracing. comp-pipescript deployed MATCH is the pre-live-invoke gate per CTO sequence; deferred with the (blocked) live run.

## Discipline
- Rule 14 ds-commit-gate: clean on all commits (f4d424037, 0fb7a064e, d7b472a97).
- Rule 14a safe-commit: used; caught + reset a contaminating DS~E staged log (concurrent-worktree guard worked).
- feedback_verify_gate_must_be_empirical_not_premise_grounded + canary-first: caught the broken integration pre-burn — the cycle's highest-leverage outcome.
- feedback_validate_gold_classifier_against_real_silver: empirically confirmed for the API client (synthetic stubs encoded the same false premise as the spec).

— 0.1.0_DS_MarketIntelligence~C 2026-05-28T1437Z
