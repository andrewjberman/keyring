# /Peers SI double-annualization fix -- DEV->PROD promote (v2.1.127)

**archetype:** DEPLOY

## Summary

Promoted the Andrew-direct /Peers Since-Inception double-annualization fix (0.2.0_DE commit
016dd9cc, PeersTab.tsx) from portal DEV to PROD via the canonical /prod-deploy procedure.
Single-commit, single-file promote; CI deployed + tagged portal-v2.1.127. RAVC'd COO GREEN,
released the DEV-push freeze, handed live served-SI re-verify to 0.2.0_DE.

## Deployment Sequence

1. Startup: /watcher (registered LIVE PID 32016, persistent inbox Monitor task b1no6o8pe armed),
   pulled 3 inbox msgs (DE promote-request, COO [DRIVE] dispatch, COO [HOLD precaution] auth-TF).
2. Confirmed HOLD non-applicable: /prod-deploy promotes portal APP submodule only -- never
   touches infra/aws/terraform/portal-auth, so the opal_users_v2 de-dup HOLD does not gate.
3. Step 1 DEV hygiene: main tree on DEV, HEAD=016dd9cc == origin/DEV (0 ahead, already pushed).
   PROD..DEV delta = exactly 1 commit (016dd9cc) -- no passengers.
4. Step 2 typecheck: `bun run typecheck` (tsc -b --noEmit) PASS, 0 errors.
5. Step 3: re-asserted local PROD = origin/PROD (bee2842f) via update-ref.
6. Step 4: ephemeral worktree .runtmp/portal-promote-20260626T181234Z on PROD; foreground
   `bun install` (420 pkgs, 133.75s); `git merge --no-ff origin/DEV` (only PeersTab.tsx, 12+/65-);
   PARITY GATE empty (git diff origin/DEV HEAD = empty); push origin PROD.
7. Step 5: VALGATE D-1 PASS (no adapter files), push-time tsc PASS. CI run 28256867173
   conclusion=success. Tag portal-v2.1.127 peeled-verified (^{commit}==95703cc8==PROD head).
8. Step 6: workspace submodule pointer bump cdf8adf3b on CLOUD (portal -> 016dd9cc); HALTGT
   ack'd a routine DE FYI (non-STOP) via HALT_ACK=1; pushed 4f4cf5202..cdf8adf3b.
9. Step 7: worktree prune (physical remove failed on long-path -- gitignored+inert, acceptable);
   main tree confirmed back on DEV; pwd workspace root.
10. Step 8: RAVC GREEN to COO (freeze released), handoff to 0.2.0_DE for live served re-verify.

## Verification (actual output)

- Merge parity: `git diff origin/DEV HEAD` -> EMPTY (exact-match merge, no drift).
- Push: `bee2842f..95703cc8  PROD -> PROD` (VALGATE D-1 PASS, tsc PASS).
- CI: `{"conclusion":"success","status":"completed"}` run 28256867173.
- Tag peel: `git rev-parse portal-v2.1.127^{commit}` = 95703cc873... = origin/PROD head.
- Pointer push: `4f4cf5202..cdf8adf3b  CLOUD -> CLOUD`.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| (none) | -- | -- |

This was a single-file FE-commit portal app promote (no gold/silver/infra/IAM change); the
relevant gates are the portal-native ones that ran in-band -- VALGATE D-1 (adapter-threading,
PASS no-op), surface-check (in safe-commit, OK no critical surface), push-time tsc. No
comp-tool query was warranted: the dependency surface for a pure PeersTab.tsx render fix was
already established by DE's pre-promote verify (served peer_performance.json ties 30/30,
schema-check benign-WARN-only, no dangling refs) cited in the promote request.

## Files Modified

- portal: PeersTab.tsx (via 0.2.0_DE 016dd9cc; merge 95703cc8) -- 12 insertions, 65 deletions.
- workspace pointer: portal submodule -> 016dd9cc (commit cdf8adf3b).

## Current State

- LIVE PROD: portal merge 95703cc8, tag portal-v2.1.127, CI run 28256867173 SUCCESS. The
  /Peers Since-Inception quartile charts now render served data directly (FE re-annualization
  removed, mirroring BenchmarkHeatmap.tsx:309). Expected SI render: INT ~13.87%, LTC/LTA
  ~18.5/18.4%, UST ~4.67% (un-halving the prior ~6.3/8.3/8.2/2.2).
- Workspace CLOUD pointer cdf8adf3b -> portal 016dd9cc. Main portal tree on DEV (Rule 19 held).
- COO HOLD on portal-auth TF (opal_users_v2 de-dup) UNTOUCHED -- this promote never reached
  auth TF. 0.7.0_AE remains the auth-TF applier under HOLD.

## Blockers

None.

## Next Steps

- [0.2.0_DE_PortfolioAnalytics] Live served-SI re-verify (option-a): once CF/edge serves fresh,
  confirm /Peers SI column renders FULL values (not halved); RAVC COO GREEN.
- [2.0.0_SA_COO] Promote leg RAVC'd GREEN, DEV-push freeze released -- close the Andrew-direct
  once DE confirms live render.
