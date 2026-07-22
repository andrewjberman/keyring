# MDPF_REVAMP.S5 exact-9 cutover -- FLIP APPLIED + LIVE (rollback ARMED, awaiting Andrew live-render verify)
**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE
**serial:** 0.7.0_AE_CloudOps
**window:** 2026-07-22 ~00:51Z -> ~02:59Z (since last log @ed6510618)

## Summary
Executed the MDPF exact-9 portal serving cutover end-to-end on Andrew's sovereign FINAL GO (all 3 never-widen limbs: CTO + COO + Andrew ~0159Z). The flip is APPLIED + LIVE; the 9 /api/general/{mdpf,portfolios}/* paths now serve from opal-data-assets (OAC) instead of portal-v2. Rollback is ARMED + proven (clean-inverse revert-plan). Only residual = the direct authed-path 200 verify, steered by CTO to Andrew's live Model Portfolios render (custom-JWT auth, no Cognito to mint a test token). NO DISARM until Andrew-render-clean + CVO verify-before-serve + explicit CTO disarm.

## The cutover sequence (all CTO-gated, each step reported verbatim)
Ledger: org/critical_paths/change_management/20260722T0100Z_mdpf-exact9-cutover (L1-L7 CLOSED, L8 open).
1. **opal-assets --target apply** (bucket-policy + mdpf_publisher_scoped ONLY; bd49f WS-R3 EXCLUDED via --target, scope-isolate CTO ruling): 0-add/2-change/0-destroy, 0-diff. [L2]
2. **publisher lambda deploy**: build-and-upload (sha ixhMa8...) -> safe-apply module.mdpf_publisher -> live CodeSha256 matches. [L3]
3. **populate**: manual invoke -> 9 json/ keys landed on opal-data-assets, INDEPENDENT ListObjectsV2 verified (@01:10Z, sizes==source). [L4]
4. **C-pre-flight** on an isolated throwaway distro (E2EBWIU5ZLD3BB + throwaway OAC + temp bucket-policy grant, b1-pattern): POS 200 application/json both shapes + 3 firms; NEG 403 non-granted. DE render-through PASS (all 9 200/json byte-identical, 3 runs). [L6]
5. **teardown ZERO-RESIDUAL** (CTO independently re-verified live): bucket-policy reverted to 2 TF stmts (throwaway gone); distro + OAC deleted (NoSuchDistribution/NoSuchOriginAccessControl). [L5/L6]
6. **THE FLIP** (portal-auth safe-apply, +OAC +origin +9 behaviors): attempt-1 comp-tagauthz fail-closed on a transient IAM-endpoint blip (Andrew's shaky local internet) -- I did NOT override (rc=1 could-not-evaluate is never a pass), grounded no-partial-apply (24 behaviors, 0 assets origin), re-fired the SAME pinned planfile; attempt-2 PASSED (205 roles swept, no collision) -> Apply complete 1-add/1-change/0-destroy; OAC E31ME0INK9BJE1; distro 33 behaviors/8 origins. [L7]

## Post-flip gates
- **Revert-plan HARD GATE = CLEAN INVERSE** (ran the pre-flip TF against the flipped live state, file-swap zero-residual): Plan 0-add/1-change/1-destroy -- DELETE OAC, origins 8->7 (-assets), behaviors 33->24 (-exactly-9), 0 existing changed. HARD GATE CLEAN INVERSE = TRUE. CTO independently corroborated. **ROLLBACK ARMED.**
- **Step-2(i) wiring verify**: all 9 live URLs (opalinvest.dev) -> 401 application/json (behaviors LIVE + auth-gated + correctly routed, NOT 404/CF-HTML). CTO corroborated. ACCEPTED.
- **Step-2(ii) direct 200 verify -- token-blocked, steered to Andrew**: portal auth is CUSTOM JWT (0 Cognito pools), no self-serve creds. CTO steer (a): Andrew's live Model Portfolios render on opalinvest.dev IS the real authed-path exercise (CTO surfacing to Andrew now). Composition proof accepted as pre-condition (C-pre-flight 200 + real-distro 401 + auth-edge-unchanged-clone + rollback clean-inverse). NOT pursuing custom-auth minting.

## Current State (handoff -- CRITICAL: the flip is LIVE)
- **LIVE:** distro EVTSA9VEHNZVH = 33 behaviors / 8 origins. The 9 /api/general/{mdpf/*,portfolios/*} exact paths (idx 17-25) -> S3-opal-data-assets (new OAC-backed origin, serving opal-data-assets/json/{mdpf,portfolios}/*). Catch-all /api/general/* (idx 26) -> S3-opal-data-portal-v2-json (LEGACY SHADOW INTACT -- legacy nightly keeps writing portal-v2).
- **Publisher HELD/manual** through cycle-1 (verify-before-serve). It writes json/mdpf|portfolios/* on opal-data-assets (PUBLISH_MAP retargeted; role writes json/*). Auto-arm DEFERRED.
- **ROLLBACK ARMED (prepped for same-turn execute):** restore pre-flip cloudfront-distribution.tf (staged $SP/preflip_cfdist.tf, byte-verified) -> safe-apply portal-auth -> the exact clean-inverse (-9/-origin/-OAC, 33->24) -> 9 paths fall to catch-all #8 -> portal-v2 shadow (instant). ~1-2min CF propagation. Execute ONLY on explicit CTO word.
- **NO DISARM** until: Andrew live-render CLEAN + CVO verify-before-serve clean + explicit CTO disarm call.

## Next Steps
- **[1.0.0_SA_CTO / Andrew]** Andrew confirms his live Model Portfolios page renders clean on opalinvest.dev (incl the inflection bell-curve). CLEAN -> CVO gate. WRONG -> CTO calls the armed rollback -> I execute same-turn.
- **[0.7.0_AE_CloudOps]** on a handed session JWT: curl the 9 direct 200 (verbatim sizes + revamp content) + hand DE for headless checkpoint-2. On CTO disarm: close L8 + tag + record.
- **[3.0.0_SA_CVO]** verify-before-serve read on the flipped serve.
- **[0.4.0_DE_ClientPlatform]** headless checkpoint-2 on the real distro (incl NAMED inflection bell-curve) once a token is available.

## Compiler Tools
| tool | run | result | note |
|---|---|---|---|
| terraform plan/apply (-json) | portal-auth flip + revert-plan | PASS | -json is the acceptance instrument for the CF ordered-LIST diff (additive +9; clean-inverse revert -9); positional human-plan churn is cosmetic. |
| safe-apply (HALTGT + comp-tagauthz) | portal-auth flip | PASS on retry | attempt-1 fail-closed on transient IAM blip -- NO override (rc=1 could-not-evaluate never a pass), re-fired pinned planfile. Guardrail worked. |
| deploy_ledger.py | open/close-leg x7 | PASS | multi-leg cutover ledger. |
| (raw aws) curl / ListObjectsV2 / get-bucket-policy / cloudfront | throwaway + real distro | PASS | rail-checked; the behavioral exercises Rule 22a demands (200/401/403 discriminating). |

- **Gap/learning banked:** a comp-tagauthz rc=1 (could-not-evaluate) on a transient IAM-endpoint network blip is a fail-closed, NOT an override case -- ground no-partial-apply + re-fire the pinned plan; never TAGAUTHZ_OVERRIDE a could-not-evaluate. And the CF ordered-list plan is only readable via -json before/after (human plan = positional churn).

## Blockers
None. Step-2(ii) direct-200 is token-gated (custom JWT, no Cognito) -> CTO steered to Andrew's live render -- a gate state, not a blocker. Flip live + rollback armed.
