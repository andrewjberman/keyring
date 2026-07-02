# Deploy Completion Record -- MDPF 49F Custody Basis Flip (bd -> schwab)

**Date opened:** 2026-07-02T14:05Z (fire-start)
**Date closed:** 2026-07-02T18:18Z -- CLOSED. MDPF un-freeze VERIFIED-GREEN (CVO parity PASS to the cent, freeze cleared 06-25->07-02, leg-2 Stage 2.5 gate PASSED). No half-landed state.
**Deploy:** MDPF 49F custody basis flip -- SSM `/mdpf/custody_source` bd -> schwab. The never-widen served-critical cutover (ADVI_BDAPIMIG P1 served-AUA un-freeze; Andrew fix-today P0 freeze (c)).
**Authored by:** 0.5.0_AE_OpalETL (flip owner + executor)
**Class:** deploy-completion (NEVER rule -- opened at fire-start, closed at completion; no half-landed)

---

## Authorization -- 3-way never-widen co-sign COMPLETE
- **CVO = GO** (2026-07-02T135732Z): 5-point verify-bar on the DEPLOYED bytes; leg-2 protection live+verified.
- **COO = GO**: scope-clear, custody-down, the leg-2 wire guards the first schwab-native run, rollback=bd.
- **CTO = GO** (2026-07-02T140325Z): grounded on the SCOPE invariant + custody-down -3.2% + leg-2 gate live + reversible.
- **COO FIRE GO**: 2026-07-02T140517Z.

## Pre-flip gate chain (all GREEN at fire)
- Leg-1 trigger dormant (param=bd v1) -- verified live (PowerShell + TF refresh).
- RPS source continuous through 06-30 (06-26/06-29 backfilled).
- WS-E dormant-deployed (DS~A, 49af9819b).
- Leg-2 gate: gold script MATCH (ETag a11419dd) + Stage 2.5 chain-wire S3-live (ETag 3e6c1d19, commit 208826724); ledger 20260702T1334Z CLOSED.
- CVO pre-parity CONFIRMED to the cent ($1,591,210,618.75) + never-widen scope CLEARED (69b093454).

## The flip
- **Command (PowerShell ONLY -- NOT Git Bash; MSYS leading-slash gotcha would flip the WRONG param):**
  `aws ssm put-parameter --name "/mdpf/custody_source" --value "schwab" --overwrite --region us-east-1`
- **Before:** bd (version 1) -- confirmed live immediately pre-fire.
- **After:** schwab (version 2) -- verified live via PS get-parameter.
- **Rollback (PowerShell):** `aws ssm put-parameter --name "/mdpf/custody_source" --value "bd" --overwrite --region us-east-1`

## Fire result
- **FIRED 2026-07-02T14:06:52Z (PowerShell).** put-parameter returned Version 2; verify get-parameter -> Value=schwab, Version=2, LastModified=1783001212.313 (2026-07-02T14:06:52Z).
- Atomic before/after captured in one PS call: bd(v1) -> schwab(v2). No intermediate/wrong-name write (PS avoids the MSYS leading-slash mangle).
- Next mdpf nightly (cron 15:00 UTC) runs on the schwab basis; the trigger's ONE fire-time read stamps `schwab` into the dispatch env (one-read-propagated -> WS-E + Stage 2.5 leg-2 gate co-activate); leg-2 gate HARD-DEFERs if the schwab custody number is out-of-band.

## Post-flip binding (CTO co-sign condition -- required, cheap)
1. **CVO post-flip parity** on the FIRST post-flip nightly: capture ACTUAL served-after PER-FIELD deltas (custody / model_aua / non_model_aua); confirm NO field widens unexpectedly vs frozen bd-basis; confirm the 6-day freeze (06-25 16:42Z) CLEARS.
2. **ROLLBACK ARMED:** any unexpected widen vs frozen bd -> fire rollback (SSM=bd) immediately + ping COO to re-convene. (Closes CTO's dry-run caveat: non_model -31% + model_aua-after were 06-24 dry-run/unattested -> post-flip per-field capture verifies live.)
3. This record CLOSES on CVO post-flip cert + freeze-clear.

## WS-3 flip-ledger-close checklist (pre-staged 2026-07-02T15:11Z, per COO -- fill on the first schwab-native run)

Un-freeze path = LEVER 1 (ride inf): 0.6.1's clean inf chain RUNNING (proc 17328, 15:07Z); INF sentinel ETA ~15:35Z -> mdpf-daily-trigger AUTO-fires on the schwab basis. (LEVER 2 manual SSM dispatch = armed fallback, held; do NOT fire without COO GO.)

Close ALL of these to flip Status OPEN -> CLOSED:  **[ALL CHECKED 2026-07-02T18:18Z]**
- [x] INF sentinel fired (2026-07-02T18:05:33Z, written by 0.6.1) -> mdpf runner i-02448edb624a7a7cf DISPATCHED (running 18:05:45Z -> stopped 18:10:02Z; convergence gate PASSED, not a DEFER -- schwab/rps checked not bd, decoupling confirmed live), CUSTODY_SOURCE=schwab stamped. run_date = 2026-07-02 ; **RPS date consumed = 07-01** (0.6.2 bridged partition; 07-02 posts ~07-03 so as_of caps at 07-01).
- [x] Chain reached SERVE -- telemetry status.json = **"complete"** (run mdpf_daily_20260702_180559); **LEG2-CUSTODY-GATE = ok** (Stage 2.5 gate PASSED, not DEFER); STAGE0/WS-E/WS-A all ok; served aggregate LastMod 18:08:33Z.
- [x] CVO per-field parity PASS (3.0.0_SA_CVO 18:17Z): served 49F custody **$1,604,173,986.44 == sum(schwab/silver/rps/date=20260701, CASH-excl) $1,604,173,986.44, delta $0.00**. custody -2.78% / model_aua -0.05% / non_model_aua -17.15% -- ALL DOWN/flat, NO unexpected widen (per CTO's bar; the non_model drop = residual re-attribution of a shrinking total).
- [x] 06-25 16:42Z freeze CLEARED -- served as_of 06-25 -> 07-02 (169h freeze cleared; custody correctly ties to the 07-01 RPS regardless of the 07-02 inf-driven label -- CVO's Orion-dating caveat noted for the record).
- [x] Rollback NOT triggered (no widen) -- CVO STAND-DOWN; **rollback DISARMED**.

WS-3 VERDICT: **CLOSE** -- the flip un-froze MDPF; freeze (c) resolved, verified-green end-to-end.

## Status: CLOSED 2026-07-02T18:18Z -- MDPF UN-FREEZE VERIFIED-GREEN. Flip fired 14:06:52Z (schwab v2); first schwab-native run served on the 07-02 INF sentinel (leg-2 gate PASSED); CVO per-field parity PASS to the cent (custody delta $0.00 vs 07-01 RPS), 169h 06-25 freeze CLEARED (06-25->07-02), all fields DOWN/flat no-widen. ROLLBACK DISARMED. **Andrew fix-today P0 freeze (c) = RESOLVED.**
