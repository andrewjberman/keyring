# 0.7.0_AE_CloudOps~A -- F1+F2 auth-chain deploy + drift-#2 sub-restore + CI-drift tranche-1 (window 3)
**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE
**window:** 2026-07-02 ~19:55Z -> ~23:30Z (lane ~A; continues bd_49f_box_rollout_5d9cc4649_deploy.md)

## Summary
Four closed arcs this window: (1) CI drift-coverage tranche-1 -- 6 sensitive-Lambda sha-baselines under CVO gate; (2) F1+F2 auth-chain hardening -- stood down my authoring on a COO deconflict, sealed + deployed 0.6.0's version with an on-box Rule-22a exercise; (3) bd-TF drift-#2 -- a Rule-22 CATCH (the gated "orphan-remove" would have enshrined a live silent-alarm gap) -> re-gated to CREATE -> sub restored; (4) the 5d9cc4649 box-rollout prove-out CLOSED GREEN (guard exercised+recovered on the 22:20Z mint). Plus a reuse-not-rederive consultation to 0.6.2 (SI2 liveness alarm) and 2 follow-on TOs filed.

## Work done
1. **CI drift-coverage tranche-1 -- CLOSED-GREEN (CVO cert).** Grounded 40/172 .functions lack artifact_sha256 (matches CVO audit). Found `comp-lambdamap derive` can't baseline-init null-sha (only reconciles drifted) -> distinct baseline-INIT op needed. CVO GATE=GREEN (22a-dogfooded: independent live CodeSha256 pull, 6/6 match). Wrote artifact_sha256 = live-CodeSha256 snapshot + artifact_sha256_provenance for 6 sensitive Lambdas (trade-authorizer/trade-auth-handler/trade-identifier-cache/opal-bd-transaction-consolidator/opal-inf-value-parity/opal-globgrph-freeze-monitor). Surgical additive diff (18ins/6del, round-trip-fidelity-verified, JSON re-validated). Commit 97059db92. CVO re-confirm cert GREEN from committed blob. Filed comp-lambdamap baseline-mode follow-on TO for the ~34 (COO+CVO endorsed).
2. **F1+F2 auth-chain hardening -- DEPLOYED + on-box-exercised.** COO greenlit F1 (kimiVision no request-timeout -> hung Kimi socket hangs login forever) + F2 (smPut FALSE-SUCCESS -> PutSecretValue throw hits outer catch, rc stays 0 = silent-freeze). Authored both + Rule-22a-exercised (node local: F2 old->rc=0 bug, fixed->rc=1; F1 hung-socket rejects ~1s); CTO arch-gate PASS. THEN COO DECONFLICT: 0.6.0 (the .js author) owns edits, I own deploy -> STOOD DOWN my authoring (git checkout, preserved diff), handed 0.6.0 my CTO-gated F2 hunk. 0.6.0 committed 4619a0dc4. SEALED it (superset-no-regression vs 5d9cc4649 = only F1 setTimeout + F2 wrap, guard untouched; byte-parity to gated content; node --check). DEPLOYED to i-0fa1846f: on-box md5 e215b90f + ON-BOX Rule-22a exercise PASS (ran on box node, SSM 89df3690). Ledger 4/4. Proves on 00:00Z main mint (self-check cron 1e7075e6 @00:15Z).
3. **bd-TF drift-#2 -- Rule-22 CATCH -> RESTORE (not remove).** COO/CTO gated a "remove the orphaned bd_49f_cookie_alerts_email sub" (framed as completing my authtoken-retire). Executed CTO's step-1 orphan-check FIRST: the sub is the SHARED email delivery for topic opal-bd-49f-cookie-alerts = alarm_actions for 7 LIVE alarms + 2 pager paths (interim.tf:52-56/197/378/407) -- NOT orphaned. My retire (b649eacf0) never touched it. LIVE: topic had 0 subs -> all bd-49f alerts firing SILENT (a real monitoring gap; the missing sub = an unconfirmed email that AWS expired after 3d). Removing would enshrine the gap. Surfaced -> CTO RE-GATED to CREATE -> targeted safe-apply created the sub (1 added, 0-diff, ledger 2/2, commit 84e41e72d). NOW Andrew-decision (via CTO): route to an OPS CHANNEL not andrew@ -> sub re-point HELD for COO to name the ops-channel target.
4. **5d9cc4649 prove-out -- CLOSED GREEN.** 22:20Z fees mint (SSM e9ac0227 Success/rc=0) minted fresh cookie (captured_at 22:22:49Z), AND the Kimi-guard was EXERCISED: log "classify: KIMI_EMPTY reply (try 1/2)" @step4 -> step5 LOGGED_IN -> OK: fresh written -> rc=0 (guard caught a real KIMI_EMPTY + recovered; N_CONSECUTIVE_UNKNOWN never hit 3). Co-RAVC-closed with 0.6.2 + CTO.
5. **Consultation + memory.** Answered 0.6.2's reuse-not-rederive ask (SI2/SDD session-liveness alarm = the bd 2-layer pattern: active 401-probe + absence belts; + the PendingConfirmation false-GREEN trap I just caught; + headless re-mint fallback). Saved memory reference-sns-alarm-delivery-verify-subscription-confirmed. Filed 2 follow-on TOs (NFRA_LAMBDAMAP.BASELINE-INIT, ADVI_BDAPIMIG.AUTHCHAIN-F3F6).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-lambdamap derive/sha | ground the sha-baseline model (live CodeSha256, not source) | PASS (found derive can't baseline-init null-sha -- real gap) |
| deploy_ledger.py | 2 deploy ledgers (drift-2 sub-restore, F1+F2) | PASS (both CLOSED 2/2 + 4/4) |
| safe-apply.sh | targeted CREATE the cookie-alerts sub | PASS (1 added, 0-diff, never-full-apply interim honored) |
| safe-commit.sh | source-map + manifest + ledgers | PASS (surgical diffs; 2 git-op timeouts -> commit landed, retried push) |
| Grep/live aws | drift-#2 mechanism grounding (TF coupling + live 0-subs) | PASS (the Rule-22 catch) |

What worked: executing CTO's step-1 orphan-check BEFORE the remove caught that the "orphan" was the shared delivery for 7 live alarms firing silent. comp-lambdamap grounded the baseline-vs-source-parity honesty. What failed: git commit/push timed out twice at 2min (commit landed; ledger-close + push completed on retry -- intermittent git hang during heavy concurrent-agent window). Gap: none new.

## Deployment Sequence + Verification (AE)
**Deploy A -- cookie-alerts sub RESTORE (drift-#2):** plan -target (1 to add) -> ledger open -> safe-apply -target (Apply complete 1 added, HALT-gate clean) -> live list-subscriptions = 1 sub (email PendingConfirmation) -> 0-diff re-plan -> ledger 2/2 (commit 84e41e72d, origin). Targeted-only (never-full-apply interim). No code change.
**Deploy B -- F1+F2 (4619a0dc4):** S3 push (md5 e215b90f) -> StartInstances -> wait status-ok/SSM-online -> SSM-pull (f6b11afe) on-box md5 e215b90f == artifact -> on-box exercise (89df3690 Success, ALL PASS) -> StopInstances -> EC2_MANIFEST deployed_commit=4619a0dc4 (e06641544) -> ledger 4/4 (origin). Proves 00:00Z.

## Blockers
None. Pending items gated on hard external triggers (00:00Z mint; COO's ops-channel target).

## Current State (handoff)
- **F1+F2 DEPLOYED** on i-0fa1846f (/opt/bd-49f-auto-login/bd_49f_auto_login.js = 4619a0dc4, md5 e215b90f5cfc9c0b7b186e30ee92d371). Box stopped/idle. Proves on the 00:00Z bd-49f-session-daily mint -> self-check cron 1e7075e6 fires 00:15Z to verify + RAVC-close.
- **5d9cc4649 slice CLOSED GREEN.** **CI drift tranche-1 CLOSED GREEN** (97059db92); baseline-mode follow-on TO filed.
- **drift-#2 sub RESTORED** (84e41e72d) -- topic opal-bd-49f-cookie-alerts now has 1 sub (andrew@ PendingConfirmation). RE-POINT to ops-channel HELD for COO's target (Andrew-decision); then targeted apply -> verify -> ledger -> RAVC.
- Live cookie: captured_at 22:22:49Z (session_live). All bd-49f alarms exist but currently deliver to a PendingConfirmation sub -> NOT yet live-delivering until the ops-channel re-point lands (or Andrew confirms, but Andrew ruled ops-channel).

## Next Steps (trigger-gated)
- **[0.7.0_AE_CloudOps~A]** verify the 00:00Z mint proves F1+F2 clean (cron 1e7075e6 @00:15Z) -> RAVC CTO+COO+0.6.0+0.6.2 -> auth-chain hardening slice fully closes.
- **[0.7.0_AE_CloudOps~A]** re-point cookie-alerts sub to the ops channel once [2.0.0_SA_COO] names the target -> targeted apply -> ledger -> RAVC CTO+COO.
- **[0.7.0_AE_CloudOps~A]** comp-lambdamap baseline-mode (the ~34) + F3-F6 durable-auth batch -- filed TOs, non-urgent.
- Not mine: [0.6.0] D3 belt; [0.6.2] SI2 liveness-alarm draft (will ping me to sanity-check).
