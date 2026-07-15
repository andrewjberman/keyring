# DEPLOY-COMPLETION LEDGER — GLDRNS.B1 AoR RELEASE WINDOW (opened 2026-07-15 22:42Z)

**Status: OPEN — closes only with the chokepoint RE-ARMED (NEVER#6 + COO condition: the safety back = closed)**
**Owner: 0.4.0_DS_ClientPlatform~B · Authority: Andrew sovereign GO verbatim x2 @ aab5f21d5 · CTO gate-owner
confirmation 224747Z · COO both-halves co-sign 225320Z/225340Z (AMEND-48 conditions verbatim) · Door-5 open by
0.7.0 225853Z (their ledger closed 22:58Z)**

## REVERT ARTIFACTS — CITED BY PATH, PRE-STAGED BEFORE THE CHOKEPOINT FLIPS (the binding condition)

| # | surface | revert artifact (path) | exercised? |
|---|---|---|---|
| 1 | served platinum spine (firm 2,316 + advisors 26 objects) | `s3://opal-data-inf/backup/served_spine_PRE_AOR_RELEASE_20260715T225000Z/{firm,advisors}/` — counts tied 2,316/2,316 + 26/26 | **YES** — one key restored via `backup/_restore_exercise_20260715T225000Z/` and md5-tied to live (`5c1910ad…`) per CTO pin 1 |
| 2 | gold/canonical (the stamp surface, 1,410 partitions) | the 07-13 ETag-verified 8,805-object backup (`s3://opal-data-inf/backup/served_spine_PRE_TIMELOCK_2026-07-13T184646Z/` family) — **still current: gold last written 07-10, before the backup** | verified-current by LastModified; restore = the un-stamp recovery op (AMEND 20: a recovery, not a rollback — which is WHY the pre-stamp verify is the binding control) |
| 3 | fold switch | delete the `INF_AOR_FOLD_ACTIVE = "1"` line (commit `9932a3dd5`) + `safe-apply` → empty export → dispatch default 0 (servicing basis returns) | mechanism exercised in reverse tonight (the dark introduction) |
| 4 | silver rescue converter | `s3://opal-data-inf/backup/pre_rescue_20260715T2259Z/convert_transactions_to_silver.py` (one `cp` back) | banked pre-overwrite, md5 of banked == pre-deploy live read (`70110fbe…`) |
| 5 | Door-5 collision state | `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/door5_decollide_20260715/revert.sh` — 0.7.0's one-command full-state restore, 4 copies banked md5==ETag 4/4, committed `030ffaeb7` BEFORE the open | 0.7.0's ledger, closed 22:58Z |
| 6 | chokepoint re-arm | remove `INF_GOLD_DISPATCH_RELEASE` from the trigger env (CTO's mechanism, same vehicle that sets it) — **fires in-session the moment stage-B outputs are verified** | the refusal side exercised live tonight (harness ARM 4) and on 07-13 (0.7.0, mode-agnostic) |

## STAGE-1 MOTIONS — COMPLETE, evidence inline

1. **Step-0 snapshot + exercised restore** — row 1 above. MANDATORY-FIRST honored (taken 22:50Z, before any motion).
2. **Fold switch ON (dark wrt dispatch):** TF commit `9932a3dd5`; plan diff = exactly `+ INF_AOR_FOLD_ACTIVE = "1"`;
   applied ~22:56Z; live env verified: `INF_AOR_FOLD_ACTIVE=1`, `INF_GOLD_DISPATCH_RELEASE` ABSENT (still held),
   `INF_GOLD_DISPATCH_HOLD` present, PERF ceiling untouched (Door 2 sealed — the risk-reflex HOLD citations on
   lambdas.tf were read; the ceiling var was not touched).
3. **Silver rescue deployed (the frozen-3 in-order chain step, CTO-confirmed 224747Z):** pre-rescue banked (row 4),
   siblings 0/0/0, local==origin `77009b25…`, deployed + download-verified TIE. The rescue = `10273505d`
   (rep_id rescued from household_rep_mapping — the same canonical map — + `rep_id_source` provenance column).
4. **Door-5 de-collided by 0.7.0** (225853Z): silver→gold both basenames, annotated copy PRESERVED (CTO pin 2),
   post-verify ETags identical pairs, silver keys untouched, revert armed (row 5). Step-zero FATAL clears.

## THE RUN PLAN (modes grounded in the deployed trigger + dispatch)

```
SENTINEL (CTO+COO string on inf-gold-trigger)             <- THEIR motion; window's only remaining pre-run gate
STAGE A  trigger mode=gold-a                              <- resolver (fold ON, pin auto-set) + A-group dims.
                                                             INF_C_01 NOT in this chain; D-group NOT in this chain.
                                                             NOTHING STAMPS, NOTHING SERVES.
PRE-STAMP VERIFY (the sovereign's "see if it gets it right"):
         timelock_preview on the FRESH SSOT (pinned to the partition the resolver read)
         + fold_map == 164 / explicit == 837
         + invariants: FIRM TOTAL $133,107,667.64 UNCHANGED TO THE CENT · phantom resolution path armed ·
           joe DOWN ~$2.1M / peter UP ~$1.6M / patrick UP ~$1.03M (incl. $52,604.80) on the proposed re-key
         ANY OTHER READING = STOP -> restore from rows 1-5 -> chain re-held -> report. NO STAMP.
STAGE B  trigger mode=full                                <- bronze pulls revive (txn feed catches up 07-10->now;
                                                             ceiling self-heals on fresh bronze) -> silver (RESCUED
                                                             converter; rep_id rescue kills the phantom at source)
                                                             -> resolver re-pins -> gold A/B/C: INF_C_01
                                                             FOLD -> LOCK -> STAMP with the full guard battery
                                                             (residual RAISES if the phantom survives; coverage
                                                             continuity; roster usability; fold-landed 6-way)
                                                             -> D-group serves the platinum surfaces.
POST     served-spine read vs the invariants + vintage DISCLOSED TO ANDREW with the numbers (COO c2)
         -> CHOKEPOINT RE-ARMED same session (row 6) -> this ledger CLOSED
         -> CVO~B V4 re-take on the served artifact (their lane, live since 22:37Z).
```

**Stamp-order absolute throughout: the fold carries real data (837/874 explicit AoR on the 07-15 scheduled row,
verified twice today by independent derivations) BEFORE any lock; the first stamp is immutable and is taken only
after the pre-stamp verify reads exactly the pre-registered numbers.**
