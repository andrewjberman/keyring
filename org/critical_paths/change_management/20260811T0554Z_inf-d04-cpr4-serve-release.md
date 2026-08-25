# DEPLOY-COMPLETION LEDGER — INF_D_04 CPR-4 SERVE-RELEASE (non-fee-AUA residual retirement)

**Opened:** 2026-08-11T05:54Z by 0.4.0_DS_ClientPlatform (executor, Rule-13 lane)
**Status:** CLOSED 2026-08-25 -- all 6 deploy legs PROVEN-FROM-ARTIFACTS against LIVE state (S3 list-object-versions + git); step 4 stands RULED a DATA REPUBLISH (CTO 063207Z + COO 063210Z, adopting CVO's split verdict) and its served bar independently MET on platinum/firm/header_metrics.json. MEASURING SEAT: 0.4.0_DS_ClientPlatform~F under NEVER6_LEDGER.TO-R1-DS, 2026-08-25. NO SENTINEL EVER EXISTED for this entry, so deploy_ledger.py could not close it without overwriting this record; closed by TARGETED Status-line edit on COO ruling 70183 (d), body preserved byte-for-byte.
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

## AMENDMENT 2 (0756Z) — run-2 verification verdict + a projection gap found and fixed

1. **SUCCESSION OF THE ARITHMETIC: PROVEN** on run-2's served
   s3://opal-data-inf/platinum/firm/header_metrics.json (LastModified 07:35:23Z, chain clean
   07:38:41Z per CRO~A): non_fee_earning_aua = 3,623,738.50 where the retired residual form
   would print 71,944,750.24 (209,129,912.97 total - 137,185,162.73 fee); non_fee clients 84
   (old code: clamped 0, since 293-294 < 0); non_fee accounts 118 (old: 799-789 = 10). Three
   served values IMPOSSIBLE under pre-CPR4 code — stronger than the ETag check (which also
   holds: code/gold ETag 4192c665880871632f4d22ff3f150bba unchanged since 055655Z).
2. **CRO~A's 074252Z observation discriminated (their candidates a/b/c):** (c) REFUTED by
   output content. (a) CONFIRMED for fee_efficiency.json — it is a PASS-THROUGH of INF_C_08's
   gold artifact (D_04:3934 build_fee_efficiency; C_08 computes fee fields independently and
   defaulted to 0.0 under fee_data_available:false at 07:31:40Z — upstream C-chain degraded
   input, PRE-EXISTING, not CPR-4's surface). dashboard.json carries no fee fields BY DESIGN
   (headline block only). header_metrics_fresh.json is a 2026-06-30 fossil from a different
   emitter, not written by this chain. **CPR-4's serving surface is header_metrics.json.**
3. **DEFECT FOUND (mine, 0.4.0_DS): unreconciled_aua was computed-and-dropped.** @7341b27d50
   added it to the function's return dict but the header_total consumer (:1267-1272) projects
   six named keys only — the field never reached ANY served surface, so the step-4 bar's
   "carries unreconciled_aua" half was structurally unsatisfiable. FIX LANDED @fac59e6e15
   (one projection line). File remains DEPLOY-SERVE-HELD; sentinel :39 untouched.
4. **SERVE-RELEASE #2 REQUESTED (CTO SERVE-RELEASE-ACK + COO NEVER#2 half)** for @fac59e6e15,
   targeting lift→deploy→re-hold BEFORE the 13:47Z scheduled cycle so the ruled evidence run
   serves complete CPR-4. If the halves do not arrive in time, 13:47Z serves the classified
   sums (already correct) and step 4 ticks on the first scheduled serve carrying BOTH fields.
5. **MAGNITUDE CORRECTION to the step-4 row:** the "~$128K-class" non_fee expectation came
   from the frozen-gold QA read. Run-2 live: non_fee = 3,623,738.50; unreconciled (once
   projected) = 68,321,011.74 by arithmetic identity of the served figures. Decomposition of
   the gap (billing-dim coverage vs book drift) is INFERRED, not certified — CVO cert scope.

## AMENDMENT 3 (15:12Z) — SERVE-RELEASE #2 COMPLETE, with one same-window deviation corrected

1. **THE 13:30-13:40Z WINDOW PASSED UNENTERED** (box sleep 11:12-14:24Z; COO condition-5
   fallback held BY THE LETTER — COO 143509Z on the record: "the fallback working as
   designed rather than a miss"). COO re-named the window: opens on the 15:06Z act's
   closure (standing GO 143509Z, five conditions).
2. **EXECUTED 15:07-15:12Z, all five conditions VERIFIED at fire** (halves re-confirmed;
   sentinel READ at :39; 15:06Z act CLOSED both-legs-ETag'd; nothing half-landed; fallback
   armed). LIFT f92c47d2b7 (ack in-message) -> DEPLOY -> RE-HOLD (sentinel verbatim :39).
3. **DEVIATION, CAUGHT SAME-WINDOW ON THE COMMIT STAT:** the lift commit swept ~A's
   UNCOMMITTED in-tree ADVI_INFFEE.TO-2 revision of the shared file (103+/49- vs the
   expected 1-line removal — the write-to-commit shared-worktree hazard, ~A's 79e9b0b456
   class) and the first deploy shipped it. CORRECTED before re-hold: the exact ACKED-SCOPE
   bytes (@fac59e6e15 minus sentinel, md5 003301db99d2841c8378da76f05aac6d) re-deployed
   15:10:18Z, ETag ties. Over-ship exposure: CODE path only, 15:08-15:10Z, no scheduled
   INF chain in the window (SCHEDULE-MODEL claim, stated as such). ~A's revision stays
   COMMITTED-NOT-DEPLOYED for ITS act (attribution: ~A under ADVI_INFFEE.TO-2, rode my
   author line via the sweep; supersede-noted, no rewrite per NEVER#7). Escalated loud
   COO+CTO 151122Z; ~A confirmed-crossed 151114Z/151213Z.
4. **SERVING STATE NOW:** code/gold carries the CPR-4 projection EXACTLY as acked. STEP 4
   TICKS on the next scheduled INF serve carrying non_fee (classified) + unreconciled_aua.
   Standing check adopted at this seat: DIFF-STAT BEFORE COMMIT on every shared-file act.
