# WSE_COTMDL.WS1 -- canonical BD-REST rebuild (cot-rebalancer-runner)

**archetype:** IMPLEMENT
**secondary_archetypes:** TRACE, VALIDATE, SCRIBE

**Agent:** 0.6.2_AE_PartnerETL · **Window:** 2026-07-21 ~21:35Z -> ~21:53Z · **TO:** WSE_COTMDL.WS1 (pending; deploy-gated)

## Summary

Andrew-direct redirect (@64fdd919c): standing cot-BD egress GRANTED + a design correction -- my WS-1 producer mirrored opal-assets-bd49f (a DataMining->xlsx MONOLITH, the WRONG sibling for a REST pull). Andrew: build like cot_bronze_ingest.py, pulling the model data through the Rebalancer endpoint daily, in the canonical BD-Lambda format (BD_API_DESIGN.md). Grounded the canonical pattern, brought CTO a design DELTA for the gate, and on his GO (all 5 decisions ratified) REBUILT as cot-rebalancer-runner. 15 tests green; old producer retired.

## Andrew-direct (verbatim, recorded @64fdd919c)

> "You have my word for egress. THis is not going to be a manual pull though. The entire point of this is to do it programmatically... look at the structure of the existing daily cottonwood REST API pull, there are BD API docs in /data/assets/docs... We need one of those set up for this exact purpose in the same canonical format." + "I'm referring to the cot_bronze_ingest.py" + "we need something like that which pulls in the model data through the rebalance endpoint every day."

Recorded + broadcast COO/CTO/MSTR same turn. Standing egress now in memory (cot-BD, COTTONWOOD only, firm-sep binds).

## Work done

1. **Grounded the canonical pattern:** BD_API_DESIGN.md (cookie-riding REST pull, dumb-about-auth, session-refresh chain), cot_bronze_ingest.py (the cot runner: load session -> mint token -> per-type pull -> land, idempotent, stdlib urllib, firm-parameterized Model-B), bd-49f-runner (the Lambda auth-aware retry/re-mint classification). Confirmed the runner is READ-ONLY on the session (zero put_secret_value; the WRITE is the separate refresh chain's).
2. **Design DELTA -> CTO gate (@385602022):** 5 decisions with recs; CTO gated all 5 GO (monolith landing / self-contained Lambda / AE-lane cot-pipeline / meta-stamp / retire-old).
3. **REBUILT as cot-rebalancer-runner** (@5050ea130): canonical structure -- load_bd_session (GetSecretValue-only) -> mint_rebalancer_bearer (in-memory) -> Puller (auth-aware re-mint-once) -> per-type pull -> content-grounded _already_landed idempotence -> complete-stamp LAST. stdlib urllib (NO layer). CLI + lambda_handler. Firm-parameterized. Carry-overs re-homed INTACT: strict per-page bronze, manifest->meta, 2 fail-closed gates, transitive Opal closure, firm-sep, set-identity guard.
4. **Retired** the superseded opal-assets-bd-rebalancer-daily-pull (git rm, recoverable).
5. **Re-synced:** CTO (deploy-gate ready) + WS-5/0.7.0 (function rename + NO LAYER + flexible runtime -- the stdlib approach drops the pandas-pyarrow-requests-layer + the python3.11 cp-constraint; role unchanged read-only).

## Compiler Tools

| Tool | Result vs expect |
|---|---|
| grep (canonical runner read-only session check) | cot_bronze_ingest + bd-49f-runner + my runner = GetSecretValue-only, ZERO put_secret_value -> read-only cookie-rider CONFIRMED (COO verify ask satisfied). |
| `.tools/commit-gate.sh` (3 runner .py) | PASS (py_compile + ds-precommit + ruff). |
| `python -m pytest` | 15 passed (11 runner + 2 auth-aware re-mint/dead-cookie + 2 landing_guard). |
| comp-iam / exact-ARN simulate | Deferred to deploy-gate (role doesn't exist yet; WS-5 owns it) -- Rule 22a at deploy. |

**What worked:** grounding cot_bronze_ingest first turned Andrew's "canonical format" into a precise structure; the stdlib-urllib canonical convention removed the whole layer/runtime hazard (no requests layer, no cp311 constraint). **What failed:** n/a. **Gap:** the initial bd49f mirror was a shared mis-mirror (my discovery sec7 AND CTO's PRD sec7 both said "mirror opal-assets-bd49f") -- caught by Andrew; CTO corrected the PRD.

## Files Modified

- NEW `infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/{lambda_function.py, test_lambda_function.py, landing_guard.py}` @5050ea130.
- DELETED `infra/aws/lambda/opal-assets/opal-assets-bd-rebalancer-daily-pull/` (retired).
- Records: `deliverables/COT_BD_EGRESS_STANDING_AND_CANONICAL_REDIRECT_20260721.md` @64fdd919c, `deliverables/WSE_WS1_CANONICAL_REWORK_DELTA_20260721.md` @385602022.
- All pushed CLOUD.

## Compliance

Zero live egress this session (mocked tests only). Read-only cookie-rider (GetSecretValue-only). Firm-clean (blackdiamond/cottonwood only, asserted + tested). No parquet at bronze (17a). stdlib only (no layer). No session write/rotation (rides the chain).

## Blockers / Next Steps

- **[1.0.0_SA_CTO]** deploy-gate code review of @5050ea130 (canonical structure vs BD_API_DESIGN.md; GetSecretValue-only; gates+closure re-homed; firm-clean).
- **[0.7.0_AE_CloudOps]** WS-5 TF update (rename + drop layer + flexible runtime; role unchanged); then pair on the Rule-22a exact-ARN verify at deploy.
- **[self]** reachable for the CTO deploy-gate + the WS-5 verify pair. Egress deploy-hold LIFTED; now gates on code-review + TF + verify.
