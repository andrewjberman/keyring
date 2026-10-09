# Deploy Completion Record
**Date opened:** 2026-10-08T16:18:06.104084+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / EventBridge rule cot-rebalancer-runner-daily cron(0 6 * * ? *) scheduled fire 2026-10-09T06:00Z + 07:00Z satellites (L4 reads it; re-measured 23:1xZ: CodeSha256 NFG8dbEL.. LastModified 16:19:41Z, rule ENABLED) (held since 2026-10-08T23:08:18.084185+00:00)
**Deploy:** MDPF_HEALGAP R2 act 1: cot-rebalancer-runner code (HG-t-3 per-feed result + PartialDay + drop-feed induce) at CLOUD 1fdab25b2b; halves COO ab41a7d1d8, CTO d2b90c937d. Branch B history: rebalancer_model_detail missing 2026-08-31..09-10 (11 of 80 dates); under this code each would read PARTIAL, no stamp, no silver. Rollback: artifact version uNNJvohJ8HVjIlEcIjEmpouzIRxLROD8, CodeSha256 QxLvPLTMO5YSkS+vaRXEkhaA78ZAr1arTyS0ADOOMvk=
**Authored by:** 2.0.0_SA_COO~G1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | build-and-upload opal-assets cot-rebalancer-runner | artifact sha256 equals BUILD_ONLY NFG8dbEL..; new artifact version id | build-and-upload opal-assets cot-rebalancer-runner 16:18Z: s3://opal-313476888478-lambda-artifacts/opal-assets/cot-rebalancer-runner.zip version 8wJOauKIAgdawXopTkE9d_3L5WLLUFmD (16:18:35Z), downloaded sha256 NFG8dbELEHHI34OSdq49kTBNHdtKyeRrUNZ9K0uzMZY= equals BUILD_ONLY at 0934cb05d1; prior version uNNJvohJ.. retained | CLOSED 20261008T162017Z |
| L2 | activation | safe-apply -target=module.cot_rebalancer_runner | plan code hash only; Apply complete 0/1/0 | targeted plan: 0/1/0, aws_lambda_function.this only: source_code_hash QxLvPL..->NFG8db.., s3_object_version uNNJ..->8wJO.., last_modified computed. safe-apply -target=module.cot_rebalancer_runner: Apply complete 0 added 1 changed 0 destroyed (Modifications complete after 6s). Seat gate WARN printed: a COO does not apply (mode WARN; dell1 seats act for HEALGAP per laptop CTO 106882) | CLOSED 20261008T162017Z |
| L3 | verify | get-function-configuration | CodeSha256 equals build sha, LastUpdateStatus Successful | get-function-configuration 16:20Z: CodeSha256 NFG8dbELEHHI34OSdq49kTBNHdtKyeRrUNZ9K0uzMZY= equals build input; LastModified 16:19:41Z; LastUpdateStatus Successful; State Active; python3.12 512MB 300s | CLOSED 20261008T162018Z |
| L4 | verify | 2026-10-09 06:00Z fire + 07:00Z satellites | meta/2026-10-09-result.json COMPLETE, stamp, silver fired, satellites as_of 2026-10-09 |  | OPEN |

## Log

- 20261008T161806Z OPENED by 2.0.0_SA_COO~G1 with 4 leg(s)
- 20261008T162017Z LEG L1 closed: build-and-upload opal-assets cot-rebalancer-runner 16:18Z: s3://opal-313476888478-lambda-artifacts/opal-assets/cot-rebal
- 20261008T162017Z LEG L2 closed: targeted plan: 0/1/0, aws_lambda_function.this only: source_code_hash QxLvPL..->NFG8db.., s3_object_version uNNJ..->8wJO
- 20261008T162018Z LEG L3 closed: get-function-configuration 16:20Z: CodeSha256 NFG8dbELEHHI34OSdq49kTBNHdtKyeRrUNZ9K0uzMZY= equals build input; LastModif
- 20261008T230818Z HELD-SOVEREIGN-GATED gate=external/EventBridge rule cot-rebalancer-runner-daily cron(0 6 * * ? *) scheduled fire 20
- 20261009T001401Z HELD-SOVEREIGN-GATED gate=external/EventBridge rule cot-rebalancer-runner-daily cron(0 6 * * ? *) scheduled fire 20
