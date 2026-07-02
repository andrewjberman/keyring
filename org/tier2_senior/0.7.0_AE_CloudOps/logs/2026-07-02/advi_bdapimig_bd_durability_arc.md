# 0.7.0_AE_CloudOps~A -- ADVI_BDAPIMIG bd durability arc (kill-cookie gate, IAM-bug fix, box-retire design, authtoken retire)
**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE
**window:** 2026-07-02 ~18:02Z -> ~19:28Z (lane ~A; base 0.7.0 on /ycharts-report)

## Summary
Fired the COO-GO'd kill-cookie resilience VERIFY-GATE the moment 0.6.0's backfill cleared (18:02Z). The gate CAUGHT A REAL LATENT BUG (auto-ingest silently broken since 06-29), which I fixed + re-verified end-to-end + deployed. Then drove the newly-expanded ADVI_BDAPIMIG lane (Andrew-direct parallel-NOW): box-retire comp-blast/design (CTO-blessed), asset-dim fail-silent hunt (bounded, not P0), and the Andrew-approved authtoken-dead alarm retirement. Two clean TF deploys, both ledgers CLOSED.

## Work done
1. **Kill-cookie resilience VERIFY-GATE -- CLOSED-GREEN.** Phased the deliberate cookie-kill just after the 18:18Z keepalive (page-avoidance), put a dead payload (6752c75e), fired the re-auth chain (bd-49f-session-trigger {session-refresh,main}). Chain re-minted a LIVE cookie (42d728f4 @18:26:16Z, session_live=TRUE, captured_at advanced ~18h). Dead-window ~6min, contained between keepalives -> no page. Restore-on-fail (AWSPREVIOUS promote) not needed.
2. **CAUGHT: runner-run auto-ingest leg IAM-broken since 06-29.** Session-trigger log: runner-run fail-closed on `AccessDenied s3:GetObject` on the mode-marker. Root cause: bd-49f-session-trigger-role ModeMarker sid = PutObject-ONLY -> writes the marker but can't read it back -> runner NEVER auto-invoked (Invocations=0 since 06-29; masked by 0.6.0's out-of-band backfill). The fail-closed guard + SNS alarm worked as designed (no wrong-ingest). Verify-don't-trust win: "box stopped = success" would have hidden it.
3. **FIX + re-verify (bd-v2.43.0).** +s3:GetObject on ModeMarker (49f-scoped). safe-apply 0-diff; LIVE get-role-policy confirmed. Re-fired {runner-run} on the valid marker -> "marker ok -> bd-49f-runner" -> auth OK (no 401) on the fresh cookie -> FRESH 07-02 bronze LANDED (forwardfill_v2/{allocations,realized,unrealized}_2026-07-02.xlsx @18:46Z). transactions = known BD 14d-window export error (separate P1, 0.6.0/DS lane).
4. **Box-retire design + comp-blast -- CTO BLESSED.** Grounded via pipescript advi-bd + EC2_MANIFEST: retire = 3 boxes (bd-allocations/transactions/fees) + 5 crons, NOT 4/6. LOAD-BEARING: EXCLUDE bd-assets (it's asset-dim/BDPL_ASTDIM -> gold positions_cube -> AdvisorIntelligence SEV1; REST doesn't replace it -> retiring it strands a SEV1 surface). Per-box readiness gates. Teardown HELD for N-nightly + human confirm.
5. **asset-dim fail-silent hunt (CTO follow-up).** asset-dim scrape-frozen (daily silver/assets/ froze 06-18; weekly bd_assets_dim.parquet 04-14/~79d) BUT positions_cube FRESH (07-01, rebuilt 07-02T16:55Z) -> BOUNDED stale-metadata (new-security classification gap), NOT a served-freeze. Converged with CTO's independent grounding; tracked as BDPL_ASTDIM REST-migration follow-on (COO to slot).
6. **authtoken-dead alarm RETIRE (bd-v2.44.0).** Andrew-approved via COO. Guardrail (a) durability re-confirmed GREEN (session-check); (b) safe-apply 1-destroy. Live describe-alarms: bd-49f-authtoken-dead GONE; 7 sibling alarms retained (coverage intact); 0-diff.
7. **Groundings/coordination:** answered 0.6.0's D3 belt question (chain fires runner EVERY night unconditionally; keep D3 as belt for mint-FAIL nights); clarified 5d9cc4649 box-rollout stays in-scope (i-0fa1846f = surviving mint box, not a retiring scrape box).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-which | route box-dep mapping | PARTIAL (near-tie -> pipescript) |
| pipescript advi-bd | box-retire consumer map | PASS (surfaced bd-assets=asset-dim SEV1 exclusion) |
| comp-iam service bd-49f-session-trigger | verify the GetObject fix | PASS (all 9 ops GRANTED, DESIRED view) |
| comp-freshness --list/all | asset-dim + positions_cube cadence | PASS (grounded the bounded-metadata read) |
| deploy_ledger.py | 2 deploy-completion ledgers | PASS (both CLOSED, 5/5 + 3/3) |
| safe-commit / safe-apply / terraform | 2 TF deploys | PASS (both 0-diff verified) |

What worked: pipescript advi-bd surfaced the bd-assets/AdvisorIntelligence coupling that raw teardown-scoping would have stranded. comp-iam confirmed the fix at DESIRED; live get-role-policy (rail-checked, fresh-IAM-change exception) confirmed landed. What failed: comp-rail HUD gated the live get-role-policy -> re-ran with the sanctioned `# rail-checked:` marker (the CLAUDE.md fresh-IAM carve-out). Gap: none new.

## Deployment Sequence + Verification (AE)
**Deploy 1 -- bd-v2.43.0 (IAM fix):** commit bb638b747 -> comp-iam PASS -> terraform plan (1 change: +s3:GetObject) -> safe-apply (Apply complete! 0 added, 1 changed, 0 destroyed) -> 0-diff re-plan ("No changes") -> live get-role-policy [PutObject,GetObject] -> functional re-verify (bd-49f-runner Invocations 0->1, auth OK, fresh 07-02 bronze landed) -> tag bd-v2.43.0 pushed -> ledger 5/5 CLOSED.
**Deploy 2 -- bd-v2.44.0 (authtoken-dead retire):** commit b649eacf0 -> plan (1 to destroy) -> safe-apply (Apply complete! 1 destroyed) -> live describe-alarms (bd-49f-authtoken-dead=[], 7 siblings survive) -> 0-diff -> tag bd-v2.44.0 pushed -> ledger 3/3 CLOSED.

## MCP traffic
~20 messages handled. Significant: COO GO (kill-cookie fire + ADVI_BDAPIMIG parallel-NOW role: durability/kill-cookie/box-retire) + SAFEGUARD (teardown human-confirm) + ACCEPT (durability slice CLOSED) + GO (authtoken-retire Andrew-approved). CVO RAVC-2 GREEN (live-confirmed + exercised). CTO ACK (fix arch-clean, self-heal realized) + box-retire BLESSED + asset-dim converged. 0.6.0: backfill CLEARED (trigger), fix VERIFIED, D3 Q, cutover-sequencing, WS-2 OTP-mailbox backlog item. RAVC opened+closed: kill-cookie durability slice (COO+CVO), box-retire arch-gate (CTO), authtoken-retire (COO).

## Blockers
None. All remaining items gated on hard external triggers (stated below) -- not blocked, HELD.

## Current State (handoff)
- **bd durability resilience slice: CLOSED-GREEN.** Re-auth chain provably re-mints AND auto-ingests on a genuinely-dead cookie. Live cookie = blackdiamond/49f/session AWSCURRENT 42d728f4 (session_live=TRUE). bd-49f-runner works via the chain (session-complete -> runner-run -> invoke, GetObject fixed).
- **Deploys live:** bd-v2.43.0 (ModeMarker +GetObject, commit bb638b747) + bd-v2.44.0 (bd-49f-authtoken-dead alarm removed, commit b649eacf0). Both on origin/CLOUD. Ledgers CLOSED: 20260702T1835Z_bd-49f-session-trigger-modemarker-getobject + 20260702T1922Z_bd-49f-authtoken-dead-alarm-retire.
- **Alarm coverage now:** keepalive-absence + authtoken-absence + silver-stale-{allocations,fees,realized,transactions,unrealized}. (authtoken-dead retired.)
- **Box-retire (CTO-blessed, HELD):** scope = bd-allocations (i-0800437d1dbb0b5cc, SHARED: alloc+realized+unrealized+price-update), bd-transactions (i-00c7568bc510f7423), bd-fees (i-0868fc7e7ebec26f2) + their 5 pipeline-trigger crons. EXCLUDE bd-assets (i-0e6f6dc014fdcf1cd = asset-dim/AdvisorIntelligence). Teardown gated: 0.6.0 N-nightly-proven + D1(txn chunk)/D2(realized-unrealized silver-trigger) + CTO gate + human confirm on instance-IDs. bd-allocations retires LAST (coupling).
- **asset-dim:** bounded stale-metadata (frozen daily 06-18/weekly 04-14; positions_cube fresh). Follow-on = BDPL_ASTDIM REST migration (COO to slot, non-urgent).

## Next Steps (all trigger-gated)
- **[0.7.0_AE_CloudOps~A]** 5d9cc4649 Kimi-guard box-rollout to i-0fa1846f -- awaiting COO deploy-GO (re-context clarified: box survives -> in-scope; 0.6.2 relays).
- **[0.7.0_AE_CloudOps~A]** box-retire teardown -- execute-on-trigger when [0.6.0_AE_PartnerETL] signals N-nightly-proven + D1/D2 land + human confirm.
- **[0.7.0_AE_CloudOps~A]** BDPL_ASTDIM auth/box-durability half -- when [2.0.0_SA_COO] slots it (after Phase-1 wave).
- **[0.7.0_AE_CloudOps~A]** WS-2 per-firm-OTP-mailbox hardening -- L2 backlog, [1.0.0_SA_CTO] arch-gates when L2 leg is worked.
- Not mine: [0.6.0_AE_PartnerETL] D1/D2 + REST productionize + N-nightly proof; [2.0.0_SA_COO] relay authtoken-retire to MSTR.
