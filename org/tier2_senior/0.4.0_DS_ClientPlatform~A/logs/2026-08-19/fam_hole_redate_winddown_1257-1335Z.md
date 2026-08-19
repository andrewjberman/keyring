# 0.4.0_DS_ClientPlatform~A -- session log 2026-08-19 1257-1335Z: fam-hole finding -> vendor verdict -> R-anchored re-date; wind-down log (Andrew-direct ~1316Z)

**archetype:** MEASURE-COORDINATE

## Session span note
This session (spawned 08-18 ~1520Z reset-relaunch) carries three prior logs: `2026-08-18/p1_close_49f_1520-1720Z.md`
(P1-CLOSE executed; P1 CTO-ATTESTED @ab7c94c470), `2026-08-18/p2_dispatch_build_1720-1740Z.md`
(P2D-1/2/4 @4dadd1354c), `2026-08-19/goldhome_repoint_dsa_0111-0130Z.md` (GOLDHOME DSA legs
@d62b47cc44, instance VALID @3d18dc4b00 -- joint TO since terminal-flipped complete, COO 125702Z,
SPINE-2 on Andrew's word). This log covers the final window.

## Work executed (1257-1335Z)
- **FINDING (grounded, then closed vendor-side in <40 min with zero fixes fired on hypotheses --
  COO cited it on the record @f79760179a):** silver `fact_fam` frontier STUCK at 2026-08-10 (526
  partitions) while fact_acc/dim_balance/dim_position/fact_trn all landed 2026-08-18 (532) -- a
  differential signal, not a calendar artifact. My one-manifest boundary read (12:18Z sweep
  ok:true, no fam hole named -> UPSTREAM of silver conversion, stated INFERRED) -> DS base
  SOURCE-CONFIRMED at the bronze listing 130216Z (feed stopped at 20260810/, fam-specific,
  converter clean) -> AE verdict 130826Z: **VENDOR-SIDE** (Schwab stopped publishing FAM for
  08335338 after as_of 08-10; the 09:45/21:45Z pulls self-heal with a 30-day lookback on resume
  -- no lane act anywhere, no new instrument).
- **RE-DATE ADOPTED @f79760179a (COO):** P2D-3 + sequential TWR catch-up = **day R** (FAM
  resumption); floor apply + first green + **P3-close = R+1**; 4b pins R+2; 4c flip R+3;
  **BDMERGE-CONVERGE keeps 08-21** (bd silver plane, fam-independent).
- **IAM-first sequencing ask TAKEN by AE -> GRANT-LIVE 131515Z:** `advi-49f-chain-access` on
  bd-exporter-ec2-role, CTO GATE-GO 131157Z, 6/6 allow-sims + 2/2 negative controls, 7 Sids
  applied-plane (B2 jd2 read / B3 conversions read / B5 RW opal-data-49financial/gold/advi/* /
  B6 _code read / B7 DDB bd-securities scan; B1 silver/* pre-existing). **My trigger set is now
  fam-resume ONLY.**

## Current State -- THE SUCCESSOR HANDOFF (R-anchored carries, per the wind-down order)
1. **P2D-3 + TWR catch-up (day R, single trigger = FAM back in bronze; detection is the standing
   pulls + DS base + COO -- do NOT build a watcher):** on R, run the catch-up IN DATE ORDER
   (BMV continuity): host start (dispatcher-less for now: start-instance -> SSM) -> per date D in
   08-11..T-1 trading days: sync `s3://opal-data-49financial/_code/` -> host, `python3
   chain_49f_entrypoint.py --date D --upload` (ad-hoc catch-up form) -- then ONE clean P2D-3 QA
   invocation, wall-clock per stage captured, **duration figure to 0.7.0_AE same-turn** (they pin
   the cron + take the schedule TF through the CTO gate at R+1). Then P2D-5 instance
   (P2D-1..P2D-4 rows are DONE: entrypoint @4dadd1354c, code at the NEW home, contract + field-3
   re-issue delivered; **P2D-2 row cites comp-pipescript `deployed` MATCH post-REG or carries the
   disclosure -- COO issuer ruling 173651Z**).
2. **QA-vintage discipline (COO-cited):** NEVER overwrite the graded 08-10 spine vintage; catch-up
   dates start 08-11. Chain excludes c03 (dormant-superseded @3a924da626 D2). a01 stage invokes
   the MODULE (a01_runner.py is import-broken, FILED, P5 candidate).
3. **P3-CLOSE (R+1) @1b2ee34db7-amended scope:** dims + b01 canonical_positions + A_07 pair
   persist at the root FROM THE SCHEDULED STAGE (P3C-2 pin @7d7e2e19f6); live listing on
   `opal-data-49financial/gold/advi/` (denominator = chain tables), newest == T-1 per
   `lib/trading_calendar` frontier, manifest identifies the scheduled run.
4. **BDMERGE-CONVERGE (08-21, fam-independent, TO @dfb5fd8f48 pending):** refresh
   `s3://opal-data-bd/scripts/merge-daily-incremental.py` to repo HEAD; MCP DS base BEFORE the
   upload; acceptance = three-way sha + next scheduled run green ON the new bytes with the guard
   visibly present; fees leg out of scope.
5. **Standing state:** all GOLDHOME artifacts at `opal-data-49financial` (gold/advi/ 4,222 synced
   two-sided; _code/ 51 objects bucket-root); the runner corpus carries the SPLIT
   (SILVER_BUCKET/GOLD_BUCKET + _bucket_for -- silver/meta/jd2 STAY opal-data-assets); safe_deploy
   advi row = longest-prefix resolvers. Prior open TOs at this serial (INF_RUNNER_REFACTOR.P1,
   NFRA_COMPILERKIT.P1 joint, OPAL_GLDRNS.A4 respec-held) untouched by the push -- COO sequences.
6. **Watch for:** 0.8.0's NFRA_COMPTOOLS.REG landing (retires the degraded Phase-1 path in all
   three runner TOs -- they MCP); CVO's 12 window-consumption re-grades fire when the R-day
   emissions land (artifact locations to CVO per my 165342Z/012401Z commitments).

## Compiler Tools
| Tool | Invocation | Result |
|---|---|---|
| paginated boto3 listings | silver frontier x5 tables + bronze boundary reads | the differential finding's denominators (532 vs 526) |
| conversion manifest read | newest sweep 20260819T121550Z | clean no-op, no fam hole -> upstream attribution (INFERRED, then source-confirmed by DS base) |
| comp-pipescript io | (runners registry gap until NFRA_COMPTOOLS.REG) | degraded path stands as disclosed in the TOs |

## Blockers
None at my seat. Single external trigger: Schwab FAM resumption (vendor-side; Andrew accelerators
routed via MSTR per @f79760179a).
