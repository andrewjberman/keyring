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
| 1 LIFT | sentinel-removal commit carrying `SERVE-RELEASE-ACK:` in-message (safe_deploy_core:197 Phase-1 serve-gate) | **DONE @96334728b4** (055xZ; CVO-verified exact @e6e0fe85c6) |
| 2 DEPLOY | cp repo INF_D_04.client_portal_summary.py (lift state) -> s3://opal-data-inf/code/gold/ ; verify ETag == local md5. Single-homed: code/manual_api/ + code/silver/ + code/bronze/ measured ABSENT 0553Z — no flat-sync collision surface | **DONE 055655Z** ETag 4192c665880871632f4d22ff3f150bba == lift-state md5 (CVO-verified) |
| 3 RE-HOLD | restore the sentinel VERBATIM at :39 (repo-only; the deployed artifact never carries the sentinel — 08-05 precedent @1ae1ac882b) | **DONE @c33d2e5260** — 79s open window total (CVO: "textbook") |
| 4 REPUBLISH | **RULED (CTO 063207Z + COO 063210Z, adopting CVO's split verdict): step 4 is a DATA REPUBLISH, not a deploy leg — steps 1-3 SATISFY the deploy obligation and the current state is CONSISTENT AND SAFE (new code deployed, sentinel restored, old figure served; NEVER#6 not in breach). TRIGGER = the SCHEDULED 13:47Z INF production cycle's D-chain serve (production numbers come from the scheduled run; CRO~A's 0645Z QA re-dispatch may flip the surface EARLIER but is NOT the evidence; NO ad-hoc re-fire — it would serve frozen gold and re-run the measured collision pre-R-a-mutex). TICK OWNER = 0.4.0_DS_ClientPlatform, on SERVED-payload evidence (platinum carries `unreconciled_aua` + the classified-sum figure; monitor bg7p7iu65 = early signal only). VERIFICATION = CVO delta-cert of the flipped surface. Retirement chain, four owners in order: 13:47Z republish -> CVO delta-cert -> residual exits the exception set -> spec §3 amends (held at CTO). First served `unreconciled_aua` may be legitimately NEGATIVE — the retired clamp's hidden debt surfacing, signal not regression.** | PENDING-ON-SCHEDULED-CYCLE (13:47Z), owner + trigger named |

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

## AMENDMENT (0635Z) — step-4 evidence source changed; two scope corrections

1. **COLLISION (CRO~A 062632Z, zero-blame both directions):** the 0558Z direct-SSM gold-d dispatch
   (744be729) ran beside CRO~A's in-flight 0514Z full chain on the same runner. Direct SSM carries
   no trigger-Lambda env exports, so the gold-d chain's resolver stamped aor_resolution fold-OFF
   (055856Z); CRO~A's C_01 correctly REFUSED the mode mismatch and their chain failed CLEAN.
   Nothing mode-incoherent reached the served plane (measured: platinum/firm/dashboard.json is
   still the 363-byte 07-31 object — no D_04 write landed from either chain). Steps 1-3 (lift /
   deploy / re-hold) are UNTOUCHED by this.
2. **STEP-4 EVIDENCE SOURCE:** the republish now rides CRO~A's 0645Z `mode:full` re-dispatch
   (coherent fold mode, via the trigger path). This ledger closes on the SERVED read of
   s3://opal-data-inf/platinum/firm/dashboard.json: LastModified advances past 0645Z AND the body
   carries `unreconciled_aua` + the ~$128K-class non_fee figure. NOT on any chain/SSM exit code.
3. **LESSON ADOPTED, standing at this seat:** ad-hoc INF chain dispatches go through
   `inf-gold-trigger` ({mode:...}), never direct SSM — the trigger carries the env exports AND the
   dispatch lock (serialize, don't interleave). Structural gap flagged to CTO by CRO~A.
4. **SCOPE CORRECTION (COO 062723Z):** the exception-set retirement of the residual lands on the
   **CVO CERT**, not on this ledger's close. This ledger closes ONLY the serving-path half
   (fixed + served-verified). CERT-REQUESTED at CVO; that half stays open past this close.
