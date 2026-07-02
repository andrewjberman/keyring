# 0.7.0_AE_CloudOps~A -- 5d9cc4649 Kimi-guard box-rollout to i-0fa1846f (deploy + prove-out setup)
**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE
**window:** 2026-07-02 ~19:28Z -> ~20:05Z (lane ~A; continues advi_bdapimig_bd_durability_arc.md)

## Summary
Executed the COO CONDITIONAL-GO (relayed by 0.6.2) for the 5d9cc4649 Kimi-health-guard box-rollout the moment both gates opened (i-0fa1846f idle + mint-clear window). Minimal-blast EC2 code deploy (single file, S3-artifact -> SSM-pull, md5-verified byte-identical on-box), NO off-cycle mint fired (no OTP burn). Then verify-don't-trust'd the prove-out gate itself (chain-head crons ENABLED, box idle, today=Thursday -> 22:20Z fees mint fires) and armed a self-check to drive the functional prove-out + RAVC-close.

## Work done
1. **5d9cc4649 box-rollout DEPLOY -- COMPLETE + on-box verified.** i-0fa1846f04ed7e337 (the SURVIVING mint box -- explicitly NOT a retiring scrape box). Pushed ONLY bd_49f_auto_login.js (41609B, 0.6.2's Kimi-health-guard + DOM-fallback classifyState) to s3://opal-313476888478-lambda-artifacts/ec2/bd-49f-auto-login/ (prior was 37675B/06-29). SSM-pulled onto /opt/bd-49f-auto-login/ (ssm 3543ce8f Success) -> on-box md5 5dafe6db5e2b45199b015a5aa8b2d7ff == local == 0.6.2's node-check-validated file. Box returned to stopped/idle. EC2_MANIFEST.json updated (deployed_commit=5d9cc4649, deployed_at=2026-07-02T19:50Z, checksum recorded; commit e4f80f856).
2. **Deploy-completion ledger CLOSED 3/3.** 20260702T1947Z_bd-49f-auto-login-kimi-guard-5d9cc4649: L1 S3-push, L2 SSM-pull+md5-verify, L3 manifest-record. All proven; committed + pushed (64c89d675..77d9d78d7). safe-deploy: "no deploy-scope script files detected" (EC2 code path, not gold/silver/bronze).
3. **Prove-out gate VERIFIED real (verify-don't-trust).** 0.6.0's cutover-sequencing disabled a bd-49f-RUNNER cron -> checked the SESSION chain-heads weren't caught: bd-49f-fees-session-daily State=ENABLED cron(20 22 ? * MON-FRI *); bd-49f-session-daily State=ENABLED cron(0 0). Today 2026-07-02 = Thursday -> the 22:20Z fees mint FIRES tonight (00:00Z main is the every-night belt). i-0fa1846f State=stopped -> ready for the mint StartInstances.
4. **Self-check armed for the prove-out.** One-shot cron b680452b at 22:33Z (18:33 EDT, 13min post-fire) with a self-contained prompt: verify SSM opal-bd-49f-session-fetch Success + fresh cookie (captured_at advances, session_live=TRUE, NO raw-value read) + Kimi-guard regression check (clean=pass; if flaky-Kimi hits, look for KIMI_ERROR/KIMI_EMPTY + "classify: DOM-fallback -> <state>" + N_CONSECUTIVE_UNKNOWN<3) -> ping 0.6.2 + RAVC-close with CTO.
5. **Coordination:** RAVC'd 0.6.2 (co-watch locked -- they co-verify the guard path at 22:20Z) + COO (FYI: CONDITIONAL-GO executed, last execute-on-trigger tail cleared for this window).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| deploy_ledger.py | box-rollout deploy-completion ledger | PASS (CLOSED 3/3) |
| safe-commit.sh | manifest + ledger commits | PASS (pathspec-scoped, no contamination) |
| (EC2 code deploy) | S3-artifact + SSM-pull per Rule 12 | PASS (on-box md5 == local) |

No comp-* graph tool this window: a single-file EC2 code deploy to an already-scoped box (box-consumer map + bd-assets SEV1 exclusion were already grounded via `pipescript advi-bd` in the prior arc log). Rule-20 dependency-check rode that grounding; this window is the mechanical S3->box execution + a read-only EventBridge/EC2 state verify (aws events describe-rule / ec2 describe-instances -- operational inspect, off-rail).

## Deployment Sequence + Verification (AE)
**EC2 code deploy (Rule 12, not TF -- code not infra):**
local bd_49f_auto_login.js (5d9cc4649, 41609B) -> `aws s3 cp` to s3://opal-313476888478-lambda-artifacts/ec2/bd-49f-auto-login/ -> `aws ssm send-command` (AWS-RunShellScript, --parameters file://ssm_params.json to bypass PS/aws.cmd JSON-quote strip) pulling the file + md5sum -> get-command-invocation Status=Success, on-box md5 5dafe6db5e2b45199b015a5aa8b2d7ff == local -> box StopInstances (back to idle) -> EC2_MANIFEST.json recorded + committed (e4f80f856) + ledger CLOSED 3/3 -> push 64c89d675..77d9d78d7. NO mint fired (functional prove-out deferred to the scheduled 22:20Z fees mint = no OTP burn).
**Gate verify (read-only):** aws events describe-rule bd-49f-fees-session-daily=ENABLED/cron(20 22 ?*MON-FRI*) + bd-49f-session-daily=ENABLED/cron(0 0); aws ec2 describe-instances i-0fa1846f=stopped.

## Blockers
None. Prove-out is HELD on a hard external gate (the 22:20Z scheduled fees mint -- cannot accelerate without an OTP-burning off-cycle mint, which is forbidden). Self-check armed (b680452b); co-watch locked (0.6.2). Not blocked, scheduled.

## Current State (handoff)
- **5d9cc4649 box-rollout: DEPLOYED + on-box md5-verified; PROVE-OUT PENDING the 22:20Z fees mint.** i-0fa1846f04ed7e337 /opt/bd-49f-auto-login/bd_49f_auto_login.js = 5d9cc4649 (md5 5dafe6db..., 41609B). Box stopped/idle. EC2_MANIFEST deployed_commit=5d9cc4649 (e4f80f856). Ledger CLOSED 3/3.
- **Prove-out mechanism:** one-shot cron b680452b fires 22:33Z -> verifies the mint minted a clean fresh cookie on 5d9cc4649 -> pings 0.6.2 + RAVC-closes the slice with 1.0.0_SA_CTO. If session dies before 22:33Z, 0.6.2 co-watches as the belt; the deploy is reversible (re-pull 06-29 37675B from the same S3 prefix via SSM).
- **Everything else unchanged from advi_bdapimig_bd_durability_arc.md:** bd durability slice CLOSED-GREEN; bd-v2.43.0 (ModeMarker +GetObject) + bd-v2.44.0 (authtoken-dead retire) live; box-retire CTO-blessed+HELD; BDPL_ASTDIM bounded-stale-metadata (COO to slot).

## Next Steps (all trigger-gated)
- **[0.7.0_AE_CloudOps~A]** VERIFY the 22:20Z fees mint proves out 5d9cc4649 (cron b680452b @22:33Z) -> ping [0.6.2_AE_PartnerETL] -> RAVC-close the box-rollout slice with [1.0.0_SA_CTO]. TONIGHT.
- **[0.7.0_AE_CloudOps~A]** box-retire teardown -- execute-on-trigger when [0.6.0_AE_PartnerETL] signals N-nightly-proven + D1/D2 land + human confirm on instance-IDs.
- **[0.7.0_AE_CloudOps~A]** BDPL_ASTDIM auth/box-durability half -- when [2.0.0_SA_COO] slots it.
- **[0.7.0_AE_CloudOps~A]** WS-2 per-firm-OTP-mailbox hardening -- L2 backlog; [1.0.0_SA_CTO] arch-gates.
