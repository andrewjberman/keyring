# Deploy Completion Record -- MDPF 49F Custody Basis Flip (bd -> schwab)

**Date opened:** 2026-07-02T14:05Z (fire-start)
**Date closed:** OPEN -- closes on CVO post-flip parity cert + 06-25 freeze-clear
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

## Status: OPEN (FIRED + verified 2026-07-02T14:06:52Z, param=schwab v2; ROLLBACK ARMED; awaiting CVO post-flip parity cert on the first schwab-native nightly + 06-25 freeze-clear)
