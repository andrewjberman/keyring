# fee_earning_aua end-to-end: investigation -> TO-2 deploy -> window fix landed; flag act staged (1120-1712Z)

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, DEPLOY, VALIDATE, COORDINATE
**Serial:** 0.4.0_DS_ClientPlatform~A · window = since inf_p1_group_d_1050-1120Z.md · 11 commits

## What happened, in order

1. **Inverted-312 band exercised** (COO nudge tick-1 caught my parked gap): d02_inf_312_band_overlay
   -- MATCH-KNOWN-WRONG 0/312 with the precondition FALSIFIED-not-asserted (served
   account_distribution rides the positions plane); CVO ruled the label N/A-BY-CONSTRUCTION
   (bound, applies at next instance touch). The 258-account offset characterized on COO's bound:
   mechanism = one-day LABEL-vs-CONTENT vintage skew; CTO ruled MY resolve the off-by-one side
   (partition=delivery, content=prior trading-day close -- convention single-homed; my P2 row
   carries the clause).
2. **ANDREW-DIRECT #1** ("get to the bottom of fee_earning_aua... true non-fee ~8m, we say 60m+"):
   recorded + broadcast. Decomposed EXACTLY (<$1): residual $71,944,750.24 = true non-fee
   $12,374,779.77 (billing mask) + coercion-suppressed FEE-EARNING $59,619,641.81 - $49,671.34.
   Independent custody-ledger mask: non-fee $6,270,920.28 == Andrew's ~8M. Source grounded:
   INF_D_04:107 + INF_D_02:1373-1376 (SUM(billing.ending_mv | is_fee_earning) -- value AND mask
   on the coerced plane). CTO RAVC-4 VALIDATED; flag sub-finding admitted to the sealed order;
   MSTR corroborated (102/907 longitudinal flips).
3. **ADVI_INFFEE.TO-2 GO** (5 weeks parked on a mislabeled gate) + **Andrew "get the fix
   deployed"**: D_04 fee block re-grained (valuation=holdings x classification; exact-sum
   unclassified bucket; confession field RETIRED; count_model documents 799-vs-868 in-emit),
   then MASK re-based onto the custody ledger per the GO's contamination requirement.
   **Shared-worktree SWEEP incident**: my first revision swept into base's serve-release
   f92c47d2b7 (~2min over-ship, base self-corrected; provenance resolved by LEDGER per COO).
   Deployed @b5909dcf11 + lift/re-hold, re-download md5 TIE 49712671e33a2bf19807e452c3b24006,
   ledger DEPLOY_LEDGER_20260811_INF_D_04_ADVI_INFFEE_TO2.md CLOSED. QA: fee $202,842,851.06 /
   non-fee $6,287,061.91 / identity exact -- INSIDE the pre-registered band.
4. **COO [STOP] five-figure table** delivered: every non-fee figure tupled (plane x mask x
   vintage); $3,623,073.92 REPRODUCED to the penny as coerced-plane x contaminated-flag; the
   $2.6M "gap" decomposes (no new finding; 21-account/$6.09M flag-disagreement set rostered).
5. **ANDREW-DIRECT #2** ("fix the is_fee_earning flag derivation too when the window fix
   lands"): recorded + broadcast; CTO placement = GOLD home (Rule 17; my silver pre-staging
   corrected in-record); COO scoped exclusive transfer of both billing files; then the WINDOW
   FIX ITSELF re-homed to this lane (CTO 165818Z) -- trigger became internal.
6. **WINDOW FIX LANDED** (joint ruling (b)): build_billing_dim.py ending_mv := raw
   portfolio-roster currentValue (the window atom DELETED from the value path);
   _load_roster_current_value + ending_mv_source; in-build OWN tie-out every run. Deployed
   s3://opal-data-inf/code/silver/build_billing_dim.py, md5 TIE be954ebd4acfe26cc2db3495b4217fa8,
   rollback stashed first (ff57efa5). Conditions: own tie 1,869/1,869 TO THE CENT (3,056
   denominator); 485-first ordering honored; Amendment-5 discriminator RETIRED. Post-fix:
   908/908 rows populated, ZERO source-absent -- absence class deleted by construction.
   COO ACCEPTED + WITHDREW the silver-placement objection (gold-home final, no crossing).

## Deployment Sequence + Verification (actual output)

```
INF_D_04:  local md5 49712671e33a2bf19807e452c3b24006 == deployed (re-downloaded) -> TIE
billing:   local md5 be954ebd4acfe26cc2db3495b4217fa8 == deployed (re-downloaded) -> TIE
WINDOW-FIX TIE-OUT: 1869 of 1869 previously-populated rows tie to the cent
  [denominators: 3056 billing rows total; 3056 populated from roster vs 1869 windowed]
```
Both ledgers in org/critical_paths/change_management/ (TO2 CLOSED; WINDOW_AND_FLAG leg-1
CLOSED, leg-2 OPEN). Served figures move on SCHEDULED fires only.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| comp-find | comp-find "fee_earning_aua" data/inf/scripts/gold | PASS -- DEF band localized the source (D_04:107) in one call, 66 hits/121 files denominator |
| comp-pipescript | deployed INF_D_04.client_portal_summary --pipeline inf | FAIL (instrument) -- AWS_UNREACHABLE x6, 0 checked; recorded as broken retrieval, deploy verified on the live primitive instead; CTO has registration queued P2/P3 |
| comp-to | standing session context | PASS |

What worked: comp-find's band classification (DEF vs SURFACED) went straight to the definition.
What failed: comp-pipescript's S3 legs unreachable AND it printed the bd tree despite --pipeline
inf -- double instrument gap, already on CTO's roster. Gap found: none new beyond that.

## Blockers

None. (Leg (b)+(d) of the flag act wait on COO's D_02 sequencing -- a NAMED WAIT with owner
and precondition stated in the ledger, not a blocker.)

## Current State (zero-context handoff)

- **Deployed + verified:** s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py
  (md5 49712671...; fee block = holdings-valued x custody-ledger-classified, three-bucket
  exact-sum; sentinel re-held) and .../code/silver/build_billing_dim.py (md5 be954ebd...;
  ending_mv = roster currentValue; is_fee_earning DEPRECATED-IN-PLACE with no-new-consumers
  bound). Rollback stashes in the session scratchpad, md5s in the ledgers.
- **Expected on next scheduled fires** (production evidence, pre-registered): billing silver
  ~$209,476,279.36 book / fee-mask ~$196,874,030.62; served header fee_earning_aua
  $137.19M -> ~$202,842,851.06, non-fee -> ~$6,287,061.91. Reader: this lane, reporting to
  [2.0.0_SA_COO] + [1.0.0_SA_CTO] + [3.0.0_SA_CVO].
- **OPEN, this lane:** flag act legs (a) gold classifier lib (data/inf/scripts/gold/lib/
  fee_classification.py, ledger basis, both lag edges declared) + (c) D_04 consolidation --
  one complete act, controls = flip census vs MSTR 102/907 + both edges; ledger
  DEPLOY_LEDGER_20260811_BILLING_WINDOW_AND_FLAG.md leg-2. Task #10 carries it.
- **OPEN, elsewhere:** legs (b) silver flag retirement + (d) INF_D_02 repoint -- COUPLED,
  [2.0.0_SA_COO] sequencing with base (precondition stated: (b) never before (d)).
  N/A-BY-CONSTRUCTION label fix on the D instance at next touch (CVO ruling, no reopen).
  DIVERGE-SOVEREIGN on dashboard total_aua still awaiting Andrew's universe ruling.
- **INF P1 (earlier this session):** complete all groups + writer, 5 instances VALID rc=0;
  builds @7564cf53ab/@9e6c1f62bf/@d47d187227/@2e6ec448fd/@4865a40c92 + yaml act.

## Next Steps

1. [this lane] Flag act legs (a)+(c) as one complete act; then the two scheduled-fire reads.
2. [2.0.0_SA_COO] D_02 sequencing for legs (b)+(d); 06_current_state recompile at wave close.
3. [1.0.0_SA_CTO] comp-pipescript inf-tree + runners_inf registration (queued P2/P3).
4. [Andrew] total_aua universe ruling (DIVERGE-SOVEREIGN packet via COO).
