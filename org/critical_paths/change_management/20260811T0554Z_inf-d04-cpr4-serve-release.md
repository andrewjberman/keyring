# DEPLOY-COMPLETION LEDGER — INF_D_04 CPR-4 SERVE-RELEASE (non-fee-AUA residual retirement)

**Opened:** 2026-08-11T05:54Z by 0.4.0_DS_ClientPlatform (executor, Rule-13 lane)
**Status:** OPEN — closes when all four steps land in-session, or on full rollback
**Authority chain:** Andrew-direct 044428Z (MSTR relay: fix the residual) -> exception-set /
pattern-spec v1.0 ratification @d272021791 (residual = ratified-TRANSITIONAL, this act retires it)
-> COO half of NEVER#2 GIVEN 055036Z (4 conditions) -> CTO half GIVEN as SERVE-RELEASE-ACK 055259Z
(AoR-absence verified on the @7341b27d50 diff: 4 hunks :764-848, zero AoR touchpoints).
**Delta being served:** @7341b27d50 ONLY. Measured shipped-delta control: deployed code/gold bytes
(md5 e61aa28fd93be355390f1d9d19b5a7cc) + the sentinel line == pre-CPR4 repo BYTE-EXACT (3-line
diff = the sentinel itself), so repo-vs-deployed drift = zero beyond CPR-4. The AoR code visible
in-repo (:63 import, :3321/:3351) is ALREADY in the deployed bytes — nothing AoR ships with this.

## STEPS (all four close in-session; any failure -> rollback per pre-registration below)

| step | content | state |
|---|---|---|
| 1 LIFT | sentinel-removal commit carrying `SERVE-RELEASE-ACK:` in-message (safe_deploy_core:197 Phase-1 serve-gate) | PENDING |
| 2 DEPLOY | cp repo INF_D_04.client_portal_summary.py (lift state) -> s3://opal-data-inf/code/gold/ ; verify ETag == local md5. Single-homed: code/manual_api/ + code/silver/ + code/bronze/ measured ABSENT 0553Z — no flat-sync collision surface | PENDING |
| 3 RE-HOLD | restore the sentinel VERBATIM at :39 (repo-only; the deployed artifact never carries the sentinel — 08-05 precedent @1ae1ac882b) | PENDING |
| 4 REPUBLISH | INF D-chain republish so platinum serves the classified figure (~$606K-class -> ~$128K-class); confirm clear of the 13:30Z MDPF bar at execution | PENDING |

## PRE-REGISTERED READINGS (decided before evidence)
- Any step fails -> restore deployed bytes from the held rollback artifact (scratchpad
  deployed_INF_D_04.py, md5 e61aa28fd93be355390f1d9d19b5a7cc), restore the sentinel, close this
  ledger ROLLBACK with reason, escalate COO+CTO loud. No stranded leg past session end.
- The re-hold is the step nobody waits on (CTO 055259Z) — it is IN this ledger precisely so an
  unclosed entry at session end = COO alarm per the NEVER rule.
- Republish executing ~0555-0615Z is ~7h before the 13:02Z MDPF cadence opens; INF D-chain and the
  MDPF floor cadence are different chains. If either premise fails at execution, republish WAITS
  for the bar; steps 1-3 stand regardless (commit/sentinel acts do not touch the bar).
- C-1 (revaluation asymmetry) is NOT closed by this release; the AoR-fold condition is NOT retired
  — the sentinel returns with its original text verbatim.
