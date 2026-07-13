# Deploy Completion Record
**Date opened:** 2026-07-13T11:35:27.702576+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260713T114631Z
**Deploy:** INF gold dispatch HOLD -- fail-closed chokepoint on inf-gold-trigger + both EventBridge rules DISABLED (b7bce51bd)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commits d60d201e3 (control+test+TF) + 9cc163f86 (source-map) | hashes pushed to origin/CLOUD, verified via git branch -r --contains | CLOUD d60d201e3 (control + test_dispatch_hold.py + lambdas.tf + eventbridge.tf) and 9cc163f86 (source-map). Authored 0.7.0_AE_CloudOps under SoD review (infra/aws = CLOUD_OPS_OR_ETL; owned-paths correctly refused CTO~B). safe-commit -F (LD-0276). | CLOSED 20260713T114631Z |
| L2 | s3-prefix | inf-gold-trigger.zip -> s3://opal-313476888478-lambda-artifacts/inf-pipeline/ | head-object ContentLength + Metadata.content-sha256 match this build (upload-verify gate da5af3c8c) | s3://opal-313476888478-lambda-artifacts/inf-pipeline/inf-gold-trigger.zip WRITE-VERIFIED by the build-and-upload gate (da5af3c8c): size=9819 + Metadata.content-sha256 match. head-object: ContentLength 9819, sha eKBESdXU7E3cNqkDsnsXCLEKzgzBgDRlNEz7oVNLz/U=, LastModified Mon 13 Jul 2026 11:34:08 GMT. Baseline was 4769B / GlLZHbChl24oJGjmmMz2bw7g3Wc+4MQUYcxb4o8JnjE= -- the object DEMONSTRABLY changed, so terraform did not hash a stale zip. | CLOSED 20260713T114631Z |
| L3 | activation | safe-apply TF: INF_GOLD_DISPATCH_HOLD env + both rules state=DISABLED | 0-diff replan AND live CodeSha256 == new artifact sha (a stale-zip 0-diff is a FALSE GREEN) | safe-apply (HALT_ACK=1): Apply complete -- 0 added, 3 changed, 0 destroyed. 0-DIFF REPLAN: 'No changes. Your infrastructure matches the configuration.' APPLIED-TRUTH GATE (Rule 22a -- a 0-diff off a STALE zip is a FALSE GREEN): live get-function-configuration CodeSha256 = eKBESdXU7E3cNqkDsnsXCLEKzgzBgDRlNEz7oVNLz/U= == the artifact sha I uploaded and verified, and != the GlLZ... baseline. So the HOLD IS THE DEPLOYED CODE, not merely the planned code. Live env: INF_GOLD_DISPATCH_RELEASE ABSENT (its absence is what holds the chain -- fail-closed), INF_GOLD_DISPATCH_HOLD present (reason string only, never consulted as a control). | CLOSED 20260713T114631Z |
| L4 | verify | LIVE ON-arm exercise: invoke -> held:true, NO dispatch lock, NO SSM SendCommand, EC2 state unchanged; both rules DISABLED on the live primitive | the ABSENCE OF THE SIDE EFFECT is the proof; the return value is a self-report | LIVE ON-ARM EXERCISE, all four arms GREEN, every negative POSITIVE-CONTROLLED. (a) RESPONSE: StatusCode 200, held=true, dispatched=false. (b) PROOF-OF-REACH (this is the arm that nearly did not exist): my marker 'ae-hold-exercise-0.7.0' had 0 log events BEFORE the invoke and 3 AFTER -- so the invocation DEMONSTRABLY reached the function. My FIRST two invoke attempts silently FAILED on 'Unknown option --cli-binary-format' (aws-cli 1.44.44), and the side-effect assertions PASSED anyway because nothing had run: A CONTROL THAT CANNOT FAIL IS NOT A CONTROL. Re-run with v1 syntax. CloudWatch carries 'BLOCKED: INF gold dispatch HOLD is ACTIVE'. (c) NO LOCK: 'Dispatch lock acquired' = 0 events; dispatch-lock.json LastModified UNCHANGED at Sun 12 Jul 2026 13:34:11 GMT (identical to the pre-invoke baseline -- no new lock object). (d) NO DISPATCH: 'Dispatch complete' = 0, 'SSM SendCommand success' = 0, 'Starting in background' = 0; EC2 i-0ed5afded2ebd4ed4 state = stopped, UNCHANGED from the pre-invoke baseline (the trigger never called start_instances). CENSUS-BY-MENTION CAUGHT IN MY OWN INSTRUMENT: a bare filter on 'SendCommand' returned 1 -- it matched the REFUSAL LINE'S OWN PROSE ('...no dispatch lock, no SSM SendCommand'), scoring the denial as the deed. Re-scoped to the ACT (4 act-specific patterns) -> all 0. POSITIVE CONTROL on the negatives: the same 'Dispatch complete' query returns 1 for 07-12, when it DID dispatch -- so the query CAN fire and today's 0 is a TRUE absence, not a broken read. RULES ON THE LIVE PRIMITIVE (aws events describe-rule, not TF): inf-canonical-prices-daily = DISABLED, inf-gold-full-on-bronze-complete = DISABLED. THE ABSENCE OF THE SIDE EFFECT IS THE PROOF; the return value is a self-report. | CLOSED 20260713T114631Z |

## Log

- 20260713T113527Z OPENED by 0.7.0_AE_CloudOps with 4 leg(s)
- 20260713T114631Z LEG L1 closed: CLOUD d60d201e3 (control + test_dispatch_hold.py + lambdas.tf + eventbridge.tf) and 9cc163f86 (source-map). Authored 0.7
- 20260713T114631Z LEG L2 closed: s3://opal-313476888478-lambda-artifacts/inf-pipeline/inf-gold-trigger.zip WRITE-VERIFIED by the build-and-upload gate (d
- 20260713T114631Z LEG L3 closed: safe-apply (HALT_ACK=1): Apply complete -- 0 added, 3 changed, 0 destroyed. 0-DIFF REPLAN: 'No changes. Your infrastruct
- 20260713T114631Z LEG L4 closed: LIVE ON-ARM EXERCISE, all four arms GREEN, every negative POSITIVE-CONTROLLED. (a) RESPONSE: StatusCode 200, held=true, 
- 20260713T114631Z CLOSED -- all 4 legs proven
